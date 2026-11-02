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
from google.longrunning import operations_pb2  # type: ignore
from google.oauth2 import service_account

from google.cloud.chronicle_v1.services.findings_refinement_service import (
    FindingsRefinementServiceAsyncClient,
    FindingsRefinementServiceClient,
    pagers,
    transports,
)
from google.cloud.chronicle_v1.types import findings_refinement
from google.cloud.chronicle_v1.types import (
    findings_refinement as gcc_findings_refinement,
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

    assert FindingsRefinementServiceClient._get_client_cert_source(None, False) is None
    assert (
        FindingsRefinementServiceClient._get_client_cert_source(
            mock_provided_cert_source, False
        )
        is None
    )
    assert (
        FindingsRefinementServiceClient._get_client_cert_source(
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
                FindingsRefinementServiceClient._get_client_cert_source(None, True)
                is mock_default_cert_source
            )
            assert (
                FindingsRefinementServiceClient._get_client_cert_source(
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
    client = FindingsRefinementServiceClient(credentials=cred)
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
    client = FindingsRefinementServiceClient(credentials=cred)
    client._transport._credentials = cred

    error = core_exceptions.GoogleAPICallError("message", details=[])
    error.code = error_code

    client._add_cred_info_for_auth_errors(error)
    assert error.details == []


@pytest.mark.parametrize(
    "client_class,transport_name",
    [
        (FindingsRefinementServiceClient, "grpc"),
        (FindingsRefinementServiceAsyncClient, "grpc_asyncio"),
        (FindingsRefinementServiceClient, "rest"),
    ],
)
def test_findings_refinement_service_client_from_service_account_info(
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
            "chronicle.googleapis.com:443"
            if transport_name in ["grpc", "grpc_asyncio"]
            else "https://chronicle.googleapis.com"
        )


@pytest.mark.parametrize(
    "transport_class,transport_name",
    [
        (transports.FindingsRefinementServiceGrpcTransport, "grpc"),
        (transports.FindingsRefinementServiceGrpcAsyncIOTransport, "grpc_asyncio"),
        (transports.FindingsRefinementServiceRestTransport, "rest"),
    ],
)
def test_findings_refinement_service_client_service_account_always_use_jwt(
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
        (FindingsRefinementServiceClient, "grpc"),
        (FindingsRefinementServiceAsyncClient, "grpc_asyncio"),
        (FindingsRefinementServiceClient, "rest"),
    ],
)
def test_findings_refinement_service_client_from_service_account_file(
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
            "chronicle.googleapis.com:443"
            if transport_name in ["grpc", "grpc_asyncio"]
            else "https://chronicle.googleapis.com"
        )


def test_findings_refinement_service_client_get_transport_class():
    transport = FindingsRefinementServiceClient.get_transport_class()
    available_transports = [
        transports.FindingsRefinementServiceGrpcTransport,
        transports.FindingsRefinementServiceRestTransport,
    ]
    assert transport in available_transports

    transport = FindingsRefinementServiceClient.get_transport_class("grpc")
    assert transport == transports.FindingsRefinementServiceGrpcTransport


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name",
    [
        (
            FindingsRefinementServiceClient,
            transports.FindingsRefinementServiceGrpcTransport,
            "grpc",
        ),
        (
            FindingsRefinementServiceAsyncClient,
            transports.FindingsRefinementServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
        ),
        (
            FindingsRefinementServiceClient,
            transports.FindingsRefinementServiceRestTransport,
            "rest",
        ),
    ],
)
@mock.patch.object(
    FindingsRefinementServiceClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(FindingsRefinementServiceClient),
)
@mock.patch.object(
    FindingsRefinementServiceAsyncClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(FindingsRefinementServiceAsyncClient),
)
def test_findings_refinement_service_client_client_options(
    client_class, transport_class, transport_name
):
    # Check that if channel is provided we won't create a new one.
    with mock.patch.object(
        FindingsRefinementServiceClient, "get_transport_class"
    ) as gtc:
        transport = transport_class(credentials=ga_credentials.AnonymousCredentials())
        client = client_class(transport=transport)
        gtc.assert_not_called()

    # Check that if channel is provided via str we will create a new one.
    with mock.patch.object(
        FindingsRefinementServiceClient, "get_transport_class"
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
            FindingsRefinementServiceClient,
            transports.FindingsRefinementServiceGrpcTransport,
            "grpc",
            "true",
        ),
        (
            FindingsRefinementServiceAsyncClient,
            transports.FindingsRefinementServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
            "true",
        ),
        (
            FindingsRefinementServiceClient,
            transports.FindingsRefinementServiceGrpcTransport,
            "grpc",
            "false",
        ),
        (
            FindingsRefinementServiceAsyncClient,
            transports.FindingsRefinementServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
            "false",
        ),
        (
            FindingsRefinementServiceClient,
            transports.FindingsRefinementServiceRestTransport,
            "rest",
            "true",
        ),
        (
            FindingsRefinementServiceClient,
            transports.FindingsRefinementServiceRestTransport,
            "rest",
            "false",
        ),
    ],
)
@mock.patch.object(
    FindingsRefinementServiceClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(FindingsRefinementServiceClient),
)
@mock.patch.object(
    FindingsRefinementServiceAsyncClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(FindingsRefinementServiceAsyncClient),
)
@mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "auto"})
def test_findings_refinement_service_client_mtls_env_auto(
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
    [FindingsRefinementServiceClient, FindingsRefinementServiceAsyncClient],
)
@mock.patch.object(
    FindingsRefinementServiceClient,
    "DEFAULT_ENDPOINT",
    modify_default_endpoint(FindingsRefinementServiceClient),
)
@mock.patch.object(
    FindingsRefinementServiceAsyncClient,
    "DEFAULT_ENDPOINT",
    modify_default_endpoint(FindingsRefinementServiceAsyncClient),
)
def test_findings_refinement_service_client_get_mtls_endpoint_and_cert_source(
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
    [FindingsRefinementServiceClient, FindingsRefinementServiceAsyncClient],
)
@mock.patch.object(
    FindingsRefinementServiceClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(FindingsRefinementServiceClient),
)
@mock.patch.object(
    FindingsRefinementServiceAsyncClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(FindingsRefinementServiceAsyncClient),
)
def test_findings_refinement_service_client_client_api_endpoint(client_class):
    mock_client_cert_source = client_cert_source_callback
    api_override = "foo.com"
    default_universe = FindingsRefinementServiceClient._DEFAULT_UNIVERSE
    default_endpoint = (
        FindingsRefinementServiceClient._DEFAULT_ENDPOINT_TEMPLATE.format(
            UNIVERSE_DOMAIN=default_universe
        )
    )
    mock_universe = "bar.com"
    mock_endpoint = FindingsRefinementServiceClient._DEFAULT_ENDPOINT_TEMPLATE.format(
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
            FindingsRefinementServiceClient,
            transports.FindingsRefinementServiceGrpcTransport,
            "grpc",
        ),
        (
            FindingsRefinementServiceAsyncClient,
            transports.FindingsRefinementServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
        ),
        (
            FindingsRefinementServiceClient,
            transports.FindingsRefinementServiceRestTransport,
            "rest",
        ),
    ],
)
def test_findings_refinement_service_client_client_options_scopes(
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
            FindingsRefinementServiceClient,
            transports.FindingsRefinementServiceGrpcTransport,
            "grpc",
            grpc_helpers,
        ),
        (
            FindingsRefinementServiceAsyncClient,
            transports.FindingsRefinementServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
            grpc_helpers_async,
        ),
        (
            FindingsRefinementServiceClient,
            transports.FindingsRefinementServiceRestTransport,
            "rest",
            None,
        ),
    ],
)
def test_findings_refinement_service_client_client_options_credentials_file(
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


def test_findings_refinement_service_client_client_options_from_dict():
    with mock.patch(
        "google.cloud.chronicle_v1.services.findings_refinement_service.transports.FindingsRefinementServiceGrpcTransport.__init__"
    ) as grpc_transport:
        grpc_transport.return_value = None
        client = FindingsRefinementServiceClient(
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
            FindingsRefinementServiceClient,
            transports.FindingsRefinementServiceGrpcTransport,
            "grpc",
            grpc_helpers,
        ),
        (
            FindingsRefinementServiceAsyncClient,
            transports.FindingsRefinementServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
            grpc_helpers_async,
        ),
    ],
)
def test_findings_refinement_service_client_create_channel_credentials_file(
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
        findings_refinement.GetFindingsRefinementRequest(),
        {},
    ],
)
def test_get_findings_refinement(request_type, transport: str = "grpc"):
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_findings_refinement), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = findings_refinement.FindingsRefinement(
            name="name_value",
            display_name="display_name_value",
            type_=findings_refinement.FindingsRefinementType.DETECTION_EXCLUSION,
            query="query_value",
        )
        response = client.get_findings_refinement(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = findings_refinement.GetFindingsRefinementRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, findings_refinement.FindingsRefinement)
    assert response.name == "name_value"
    assert response.display_name == "display_name_value"
    assert (
        response.type_ == findings_refinement.FindingsRefinementType.DETECTION_EXCLUSION
    )
    assert response.query == "query_value"


def test_get_findings_refinement_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = findings_refinement.GetFindingsRefinementRequest(
        name="name_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_findings_refinement), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.get_findings_refinement(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = findings_refinement.GetFindingsRefinementRequest(
            name="name_value",
        )
        assert args[0] == request_msg


def test_get_findings_refinement_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = FindingsRefinementServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.get_findings_refinement
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.get_findings_refinement
        ] = mock_rpc
        request = {}
        client.get_findings_refinement(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_findings_refinement(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_get_findings_refinement_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = FindingsRefinementServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.get_findings_refinement
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.get_findings_refinement
        ] = mock_rpc

        request = {}
        await client.get_findings_refinement(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.get_findings_refinement(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        findings_refinement.GetFindingsRefinementRequest(),
        {},
    ],
)
async def test_get_findings_refinement_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = FindingsRefinementServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_findings_refinement), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            findings_refinement.FindingsRefinement(
                name="name_value",
                display_name="display_name_value",
                type_=findings_refinement.FindingsRefinementType.DETECTION_EXCLUSION,
                query="query_value",
            )
        )
        response = await client.get_findings_refinement(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = findings_refinement.GetFindingsRefinementRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, findings_refinement.FindingsRefinement)
    assert response.name == "name_value"
    assert response.display_name == "display_name_value"
    assert (
        response.type_ == findings_refinement.FindingsRefinementType.DETECTION_EXCLUSION
    )
    assert response.query == "query_value"


def test_get_findings_refinement_field_headers():
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = findings_refinement.GetFindingsRefinementRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_findings_refinement), "__call__"
    ) as call:
        call.return_value = findings_refinement.FindingsRefinement()
        client.get_findings_refinement(request)

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
async def test_get_findings_refinement_field_headers_async():
    client = FindingsRefinementServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = findings_refinement.GetFindingsRefinementRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_findings_refinement), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            findings_refinement.FindingsRefinement()
        )
        await client.get_findings_refinement(request)

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


def test_get_findings_refinement_flattened():
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_findings_refinement), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = findings_refinement.FindingsRefinement()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.get_findings_refinement(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_get_findings_refinement_flattened_error():
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_findings_refinement(
            findings_refinement.GetFindingsRefinementRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_get_findings_refinement_flattened_async():
    client = FindingsRefinementServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_findings_refinement), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = findings_refinement.FindingsRefinement()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            findings_refinement.FindingsRefinement()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.get_findings_refinement(
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
async def test_get_findings_refinement_flattened_error_async():
    client = FindingsRefinementServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.get_findings_refinement(
            findings_refinement.GetFindingsRefinementRequest(),
            name="name_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        findings_refinement.ListFindingsRefinementsRequest(),
        {},
    ],
)
def test_list_findings_refinements(request_type, transport: str = "grpc"):
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_findings_refinements), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = findings_refinement.ListFindingsRefinementsResponse(
            next_page_token="next_page_token_value",
        )
        response = client.list_findings_refinements(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = findings_refinement.ListFindingsRefinementsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListFindingsRefinementsPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_findings_refinements_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = findings_refinement.ListFindingsRefinementsRequest(
        parent="parent_value",
        page_token="page_token_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_findings_refinements), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.list_findings_refinements(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = findings_refinement.ListFindingsRefinementsRequest(
            parent="parent_value",
            page_token="page_token_value",
        )
        assert args[0] == request_msg


def test_list_findings_refinements_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = FindingsRefinementServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.list_findings_refinements
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.list_findings_refinements
        ] = mock_rpc
        request = {}
        client.list_findings_refinements(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_findings_refinements(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_list_findings_refinements_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = FindingsRefinementServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.list_findings_refinements
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.list_findings_refinements
        ] = mock_rpc

        request = {}
        await client.list_findings_refinements(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.list_findings_refinements(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        findings_refinement.ListFindingsRefinementsRequest(),
        {},
    ],
)
async def test_list_findings_refinements_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = FindingsRefinementServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_findings_refinements), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            findings_refinement.ListFindingsRefinementsResponse(
                next_page_token="next_page_token_value",
            )
        )
        response = await client.list_findings_refinements(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = findings_refinement.ListFindingsRefinementsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListFindingsRefinementsAsyncPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_findings_refinements_field_headers():
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = findings_refinement.ListFindingsRefinementsRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_findings_refinements), "__call__"
    ) as call:
        call.return_value = findings_refinement.ListFindingsRefinementsResponse()
        client.list_findings_refinements(request)

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
async def test_list_findings_refinements_field_headers_async():
    client = FindingsRefinementServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = findings_refinement.ListFindingsRefinementsRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_findings_refinements), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            findings_refinement.ListFindingsRefinementsResponse()
        )
        await client.list_findings_refinements(request)

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


def test_list_findings_refinements_flattened():
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_findings_refinements), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = findings_refinement.ListFindingsRefinementsResponse()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.list_findings_refinements(
            parent="parent_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val


def test_list_findings_refinements_flattened_error():
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_findings_refinements(
            findings_refinement.ListFindingsRefinementsRequest(),
            parent="parent_value",
        )


@pytest.mark.asyncio
async def test_list_findings_refinements_flattened_async():
    client = FindingsRefinementServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_findings_refinements), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = findings_refinement.ListFindingsRefinementsResponse()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            findings_refinement.ListFindingsRefinementsResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.list_findings_refinements(
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
async def test_list_findings_refinements_flattened_error_async():
    client = FindingsRefinementServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.list_findings_refinements(
            findings_refinement.ListFindingsRefinementsRequest(),
            parent="parent_value",
        )


def test_list_findings_refinements_pager(transport_name: str = "grpc"):
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_findings_refinements), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            findings_refinement.ListFindingsRefinementsResponse(
                findings_refinements=[
                    findings_refinement.FindingsRefinement(),
                    findings_refinement.FindingsRefinement(),
                    findings_refinement.FindingsRefinement(),
                ],
                next_page_token="abc",
            ),
            findings_refinement.ListFindingsRefinementsResponse(
                findings_refinements=[],
                next_page_token="def",
            ),
            findings_refinement.ListFindingsRefinementsResponse(
                findings_refinements=[
                    findings_refinement.FindingsRefinement(),
                ],
                next_page_token="ghi",
            ),
            findings_refinement.ListFindingsRefinementsResponse(
                findings_refinements=[
                    findings_refinement.FindingsRefinement(),
                    findings_refinement.FindingsRefinement(),
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
        pager = client.list_findings_refinements(
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
            isinstance(i, findings_refinement.FindingsRefinement) for i in results
        )


def test_list_findings_refinements_pages(transport_name: str = "grpc"):
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_findings_refinements), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            findings_refinement.ListFindingsRefinementsResponse(
                findings_refinements=[
                    findings_refinement.FindingsRefinement(),
                    findings_refinement.FindingsRefinement(),
                    findings_refinement.FindingsRefinement(),
                ],
                next_page_token="abc",
            ),
            findings_refinement.ListFindingsRefinementsResponse(
                findings_refinements=[],
                next_page_token="def",
            ),
            findings_refinement.ListFindingsRefinementsResponse(
                findings_refinements=[
                    findings_refinement.FindingsRefinement(),
                ],
                next_page_token="ghi",
            ),
            findings_refinement.ListFindingsRefinementsResponse(
                findings_refinements=[
                    findings_refinement.FindingsRefinement(),
                    findings_refinement.FindingsRefinement(),
                ],
            ),
            RuntimeError,
        )
        pages = list(client.list_findings_refinements(request={}).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.asyncio
async def test_list_findings_refinements_async_pager():
    client = FindingsRefinementServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_findings_refinements),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            findings_refinement.ListFindingsRefinementsResponse(
                findings_refinements=[
                    findings_refinement.FindingsRefinement(),
                    findings_refinement.FindingsRefinement(),
                    findings_refinement.FindingsRefinement(),
                ],
                next_page_token="abc",
            ),
            findings_refinement.ListFindingsRefinementsResponse(
                findings_refinements=[],
                next_page_token="def",
            ),
            findings_refinement.ListFindingsRefinementsResponse(
                findings_refinements=[
                    findings_refinement.FindingsRefinement(),
                ],
                next_page_token="ghi",
            ),
            findings_refinement.ListFindingsRefinementsResponse(
                findings_refinements=[
                    findings_refinement.FindingsRefinement(),
                    findings_refinement.FindingsRefinement(),
                ],
            ),
            RuntimeError,
        )
        async_pager = await client.list_findings_refinements(
            request={},
        )
        assert async_pager.next_page_token == "abc"
        assert str(async_pager).startswith(f"{async_pager.__class__.__name__}<")

        responses = []
        async for response in async_pager:  # pragma: no branch
            responses.append(response)

        assert len(responses) == 6
        assert all(
            isinstance(i, findings_refinement.FindingsRefinement) for i in responses
        )


@pytest.mark.asyncio
async def test_list_findings_refinements_async_pages():
    client = FindingsRefinementServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_findings_refinements),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            findings_refinement.ListFindingsRefinementsResponse(
                findings_refinements=[
                    findings_refinement.FindingsRefinement(),
                    findings_refinement.FindingsRefinement(),
                    findings_refinement.FindingsRefinement(),
                ],
                next_page_token="abc",
            ),
            findings_refinement.ListFindingsRefinementsResponse(
                findings_refinements=[],
                next_page_token="def",
            ),
            findings_refinement.ListFindingsRefinementsResponse(
                findings_refinements=[
                    findings_refinement.FindingsRefinement(),
                ],
                next_page_token="ghi",
            ),
            findings_refinement.ListFindingsRefinementsResponse(
                findings_refinements=[
                    findings_refinement.FindingsRefinement(),
                    findings_refinement.FindingsRefinement(),
                ],
            ),
            RuntimeError,
        )
        pages = []
        async for page_ in (await client.list_findings_refinements(request={})).pages:
            pages.append(page_)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.parametrize(
    "request_type",
    [
        gcc_findings_refinement.CreateFindingsRefinementRequest(),
        {},
    ],
)
def test_create_findings_refinement(request_type, transport: str = "grpc"):
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_findings_refinement), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = gcc_findings_refinement.FindingsRefinement(
            name="name_value",
            display_name="display_name_value",
            type_=gcc_findings_refinement.FindingsRefinementType.DETECTION_EXCLUSION,
            query="query_value",
        )
        response = client.create_findings_refinement(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = gcc_findings_refinement.CreateFindingsRefinementRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, gcc_findings_refinement.FindingsRefinement)
    assert response.name == "name_value"
    assert response.display_name == "display_name_value"
    assert (
        response.type_
        == gcc_findings_refinement.FindingsRefinementType.DETECTION_EXCLUSION
    )
    assert response.query == "query_value"


def test_create_findings_refinement_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = gcc_findings_refinement.CreateFindingsRefinementRequest(
        parent="parent_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_findings_refinement), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.create_findings_refinement(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gcc_findings_refinement.CreateFindingsRefinementRequest(
            parent="parent_value",
        )
        assert args[0] == request_msg


def test_create_findings_refinement_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = FindingsRefinementServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.create_findings_refinement
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.create_findings_refinement
        ] = mock_rpc
        request = {}
        client.create_findings_refinement(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.create_findings_refinement(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_create_findings_refinement_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = FindingsRefinementServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.create_findings_refinement
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.create_findings_refinement
        ] = mock_rpc

        request = {}
        await client.create_findings_refinement(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.create_findings_refinement(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        gcc_findings_refinement.CreateFindingsRefinementRequest(),
        {},
    ],
)
async def test_create_findings_refinement_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = FindingsRefinementServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_findings_refinement), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            gcc_findings_refinement.FindingsRefinement(
                name="name_value",
                display_name="display_name_value",
                type_=gcc_findings_refinement.FindingsRefinementType.DETECTION_EXCLUSION,
                query="query_value",
            )
        )
        response = await client.create_findings_refinement(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = gcc_findings_refinement.CreateFindingsRefinementRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, gcc_findings_refinement.FindingsRefinement)
    assert response.name == "name_value"
    assert response.display_name == "display_name_value"
    assert (
        response.type_
        == gcc_findings_refinement.FindingsRefinementType.DETECTION_EXCLUSION
    )
    assert response.query == "query_value"


def test_create_findings_refinement_field_headers():
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = gcc_findings_refinement.CreateFindingsRefinementRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_findings_refinement), "__call__"
    ) as call:
        call.return_value = gcc_findings_refinement.FindingsRefinement()
        client.create_findings_refinement(request)

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
async def test_create_findings_refinement_field_headers_async():
    client = FindingsRefinementServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = gcc_findings_refinement.CreateFindingsRefinementRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_findings_refinement), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            gcc_findings_refinement.FindingsRefinement()
        )
        await client.create_findings_refinement(request)

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


def test_create_findings_refinement_flattened():
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_findings_refinement), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = gcc_findings_refinement.FindingsRefinement()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.create_findings_refinement(
            parent="parent_value",
            findings_refinement=gcc_findings_refinement.FindingsRefinement(
                name="name_value"
            ),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val
        arg = args[0].findings_refinement
        mock_val = gcc_findings_refinement.FindingsRefinement(name="name_value")
        assert arg == mock_val


def test_create_findings_refinement_flattened_error():
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.create_findings_refinement(
            gcc_findings_refinement.CreateFindingsRefinementRequest(),
            parent="parent_value",
            findings_refinement=gcc_findings_refinement.FindingsRefinement(
                name="name_value"
            ),
        )


@pytest.mark.asyncio
async def test_create_findings_refinement_flattened_async():
    client = FindingsRefinementServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_findings_refinement), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = gcc_findings_refinement.FindingsRefinement()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            gcc_findings_refinement.FindingsRefinement()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.create_findings_refinement(
            parent="parent_value",
            findings_refinement=gcc_findings_refinement.FindingsRefinement(
                name="name_value"
            ),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val
        arg = args[0].findings_refinement
        mock_val = gcc_findings_refinement.FindingsRefinement(name="name_value")
        assert arg == mock_val


@pytest.mark.asyncio
async def test_create_findings_refinement_flattened_error_async():
    client = FindingsRefinementServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.create_findings_refinement(
            gcc_findings_refinement.CreateFindingsRefinementRequest(),
            parent="parent_value",
            findings_refinement=gcc_findings_refinement.FindingsRefinement(
                name="name_value"
            ),
        )


@pytest.mark.parametrize(
    "request_type",
    [
        gcc_findings_refinement.UpdateFindingsRefinementRequest(),
        {},
    ],
)
def test_update_findings_refinement(request_type, transport: str = "grpc"):
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_findings_refinement), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = gcc_findings_refinement.FindingsRefinement(
            name="name_value",
            display_name="display_name_value",
            type_=gcc_findings_refinement.FindingsRefinementType.DETECTION_EXCLUSION,
            query="query_value",
        )
        response = client.update_findings_refinement(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = gcc_findings_refinement.UpdateFindingsRefinementRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, gcc_findings_refinement.FindingsRefinement)
    assert response.name == "name_value"
    assert response.display_name == "display_name_value"
    assert (
        response.type_
        == gcc_findings_refinement.FindingsRefinementType.DETECTION_EXCLUSION
    )
    assert response.query == "query_value"


def test_update_findings_refinement_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = gcc_findings_refinement.UpdateFindingsRefinementRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_findings_refinement), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.update_findings_refinement(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gcc_findings_refinement.UpdateFindingsRefinementRequest()
        assert args[0] == request_msg


def test_update_findings_refinement_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = FindingsRefinementServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.update_findings_refinement
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.update_findings_refinement
        ] = mock_rpc
        request = {}
        client.update_findings_refinement(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.update_findings_refinement(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_update_findings_refinement_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = FindingsRefinementServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.update_findings_refinement
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.update_findings_refinement
        ] = mock_rpc

        request = {}
        await client.update_findings_refinement(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.update_findings_refinement(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        gcc_findings_refinement.UpdateFindingsRefinementRequest(),
        {},
    ],
)
async def test_update_findings_refinement_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = FindingsRefinementServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_findings_refinement), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            gcc_findings_refinement.FindingsRefinement(
                name="name_value",
                display_name="display_name_value",
                type_=gcc_findings_refinement.FindingsRefinementType.DETECTION_EXCLUSION,
                query="query_value",
            )
        )
        response = await client.update_findings_refinement(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = gcc_findings_refinement.UpdateFindingsRefinementRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, gcc_findings_refinement.FindingsRefinement)
    assert response.name == "name_value"
    assert response.display_name == "display_name_value"
    assert (
        response.type_
        == gcc_findings_refinement.FindingsRefinementType.DETECTION_EXCLUSION
    )
    assert response.query == "query_value"


def test_update_findings_refinement_field_headers():
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = gcc_findings_refinement.UpdateFindingsRefinementRequest()

    request.findings_refinement.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_findings_refinement), "__call__"
    ) as call:
        call.return_value = gcc_findings_refinement.FindingsRefinement()
        client.update_findings_refinement(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "findings_refinement.name=name_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_update_findings_refinement_field_headers_async():
    client = FindingsRefinementServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = gcc_findings_refinement.UpdateFindingsRefinementRequest()

    request.findings_refinement.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_findings_refinement), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            gcc_findings_refinement.FindingsRefinement()
        )
        await client.update_findings_refinement(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "findings_refinement.name=name_value",
    ) in kw["metadata"]


def test_update_findings_refinement_flattened():
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_findings_refinement), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = gcc_findings_refinement.FindingsRefinement()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.update_findings_refinement(
            findings_refinement=gcc_findings_refinement.FindingsRefinement(
                name="name_value"
            ),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].findings_refinement
        mock_val = gcc_findings_refinement.FindingsRefinement(name="name_value")
        assert arg == mock_val
        arg = args[0].update_mask
        mock_val = field_mask_pb2.FieldMask(paths=["paths_value"])
        assert arg == mock_val


def test_update_findings_refinement_flattened_error():
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.update_findings_refinement(
            gcc_findings_refinement.UpdateFindingsRefinementRequest(),
            findings_refinement=gcc_findings_refinement.FindingsRefinement(
                name="name_value"
            ),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


@pytest.mark.asyncio
async def test_update_findings_refinement_flattened_async():
    client = FindingsRefinementServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_findings_refinement), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = gcc_findings_refinement.FindingsRefinement()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            gcc_findings_refinement.FindingsRefinement()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.update_findings_refinement(
            findings_refinement=gcc_findings_refinement.FindingsRefinement(
                name="name_value"
            ),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].findings_refinement
        mock_val = gcc_findings_refinement.FindingsRefinement(name="name_value")
        assert arg == mock_val
        arg = args[0].update_mask
        mock_val = field_mask_pb2.FieldMask(paths=["paths_value"])
        assert arg == mock_val


@pytest.mark.asyncio
async def test_update_findings_refinement_flattened_error_async():
    client = FindingsRefinementServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.update_findings_refinement(
            gcc_findings_refinement.UpdateFindingsRefinementRequest(),
            findings_refinement=gcc_findings_refinement.FindingsRefinement(
                name="name_value"
            ),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


@pytest.mark.parametrize(
    "request_type",
    [
        findings_refinement.GetFindingsRefinementDeploymentRequest(),
        {},
    ],
)
def test_get_findings_refinement_deployment(request_type, transport: str = "grpc"):
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_findings_refinement_deployment), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = findings_refinement.FindingsRefinementDeployment(
            name="name_value",
            enabled=True,
            archived=True,
        )
        response = client.get_findings_refinement_deployment(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = findings_refinement.GetFindingsRefinementDeploymentRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, findings_refinement.FindingsRefinementDeployment)
    assert response.name == "name_value"
    assert response.enabled is True
    assert response.archived is True


def test_get_findings_refinement_deployment_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = findings_refinement.GetFindingsRefinementDeploymentRequest(
        name="name_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_findings_refinement_deployment), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.get_findings_refinement_deployment(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = findings_refinement.GetFindingsRefinementDeploymentRequest(
            name="name_value",
        )
        assert args[0] == request_msg


def test_get_findings_refinement_deployment_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = FindingsRefinementServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.get_findings_refinement_deployment
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.get_findings_refinement_deployment
        ] = mock_rpc
        request = {}
        client.get_findings_refinement_deployment(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_findings_refinement_deployment(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_get_findings_refinement_deployment_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = FindingsRefinementServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.get_findings_refinement_deployment
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.get_findings_refinement_deployment
        ] = mock_rpc

        request = {}
        await client.get_findings_refinement_deployment(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.get_findings_refinement_deployment(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        findings_refinement.GetFindingsRefinementDeploymentRequest(),
        {},
    ],
)
async def test_get_findings_refinement_deployment_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = FindingsRefinementServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_findings_refinement_deployment), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            findings_refinement.FindingsRefinementDeployment(
                name="name_value",
                enabled=True,
                archived=True,
            )
        )
        response = await client.get_findings_refinement_deployment(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = findings_refinement.GetFindingsRefinementDeploymentRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, findings_refinement.FindingsRefinementDeployment)
    assert response.name == "name_value"
    assert response.enabled is True
    assert response.archived is True


def test_get_findings_refinement_deployment_field_headers():
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = findings_refinement.GetFindingsRefinementDeploymentRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_findings_refinement_deployment), "__call__"
    ) as call:
        call.return_value = findings_refinement.FindingsRefinementDeployment()
        client.get_findings_refinement_deployment(request)

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
async def test_get_findings_refinement_deployment_field_headers_async():
    client = FindingsRefinementServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = findings_refinement.GetFindingsRefinementDeploymentRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_findings_refinement_deployment), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            findings_refinement.FindingsRefinementDeployment()
        )
        await client.get_findings_refinement_deployment(request)

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


def test_get_findings_refinement_deployment_flattened():
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_findings_refinement_deployment), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = findings_refinement.FindingsRefinementDeployment()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.get_findings_refinement_deployment(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_get_findings_refinement_deployment_flattened_error():
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_findings_refinement_deployment(
            findings_refinement.GetFindingsRefinementDeploymentRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_get_findings_refinement_deployment_flattened_async():
    client = FindingsRefinementServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_findings_refinement_deployment), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = findings_refinement.FindingsRefinementDeployment()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            findings_refinement.FindingsRefinementDeployment()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.get_findings_refinement_deployment(
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
async def test_get_findings_refinement_deployment_flattened_error_async():
    client = FindingsRefinementServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.get_findings_refinement_deployment(
            findings_refinement.GetFindingsRefinementDeploymentRequest(),
            name="name_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        findings_refinement.UpdateFindingsRefinementDeploymentRequest(),
        {},
    ],
)
def test_update_findings_refinement_deployment(request_type, transport: str = "grpc"):
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_findings_refinement_deployment), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = findings_refinement.FindingsRefinementDeployment(
            name="name_value",
            enabled=True,
            archived=True,
        )
        response = client.update_findings_refinement_deployment(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = findings_refinement.UpdateFindingsRefinementDeploymentRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, findings_refinement.FindingsRefinementDeployment)
    assert response.name == "name_value"
    assert response.enabled is True
    assert response.archived is True


def test_update_findings_refinement_deployment_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = findings_refinement.UpdateFindingsRefinementDeploymentRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_findings_refinement_deployment), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.update_findings_refinement_deployment(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = findings_refinement.UpdateFindingsRefinementDeploymentRequest()
        assert args[0] == request_msg


def test_update_findings_refinement_deployment_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = FindingsRefinementServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.update_findings_refinement_deployment
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.update_findings_refinement_deployment
        ] = mock_rpc
        request = {}
        client.update_findings_refinement_deployment(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.update_findings_refinement_deployment(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_update_findings_refinement_deployment_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = FindingsRefinementServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.update_findings_refinement_deployment
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.update_findings_refinement_deployment
        ] = mock_rpc

        request = {}
        await client.update_findings_refinement_deployment(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.update_findings_refinement_deployment(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        findings_refinement.UpdateFindingsRefinementDeploymentRequest(),
        {},
    ],
)
async def test_update_findings_refinement_deployment_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = FindingsRefinementServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_findings_refinement_deployment), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            findings_refinement.FindingsRefinementDeployment(
                name="name_value",
                enabled=True,
                archived=True,
            )
        )
        response = await client.update_findings_refinement_deployment(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = findings_refinement.UpdateFindingsRefinementDeploymentRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, findings_refinement.FindingsRefinementDeployment)
    assert response.name == "name_value"
    assert response.enabled is True
    assert response.archived is True


def test_update_findings_refinement_deployment_field_headers():
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = findings_refinement.UpdateFindingsRefinementDeploymentRequest()

    request.findings_refinement_deployment.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_findings_refinement_deployment), "__call__"
    ) as call:
        call.return_value = findings_refinement.FindingsRefinementDeployment()
        client.update_findings_refinement_deployment(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "findings_refinement_deployment.name=name_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_update_findings_refinement_deployment_field_headers_async():
    client = FindingsRefinementServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = findings_refinement.UpdateFindingsRefinementDeploymentRequest()

    request.findings_refinement_deployment.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_findings_refinement_deployment), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            findings_refinement.FindingsRefinementDeployment()
        )
        await client.update_findings_refinement_deployment(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "findings_refinement_deployment.name=name_value",
    ) in kw["metadata"]


def test_update_findings_refinement_deployment_flattened():
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_findings_refinement_deployment), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = findings_refinement.FindingsRefinementDeployment()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.update_findings_refinement_deployment(
            findings_refinement_deployment=findings_refinement.FindingsRefinementDeployment(
                detection_exclusion_application=findings_refinement.DetectionExclusionApplication(
                    curated_rule_sets=["curated_rule_sets_value"]
                )
            ),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].findings_refinement_deployment
        mock_val = findings_refinement.FindingsRefinementDeployment(
            detection_exclusion_application=findings_refinement.DetectionExclusionApplication(
                curated_rule_sets=["curated_rule_sets_value"]
            )
        )
        assert arg == mock_val
        arg = args[0].update_mask
        mock_val = field_mask_pb2.FieldMask(paths=["paths_value"])
        assert arg == mock_val


def test_update_findings_refinement_deployment_flattened_error():
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.update_findings_refinement_deployment(
            findings_refinement.UpdateFindingsRefinementDeploymentRequest(),
            findings_refinement_deployment=findings_refinement.FindingsRefinementDeployment(
                detection_exclusion_application=findings_refinement.DetectionExclusionApplication(
                    curated_rule_sets=["curated_rule_sets_value"]
                )
            ),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


@pytest.mark.asyncio
async def test_update_findings_refinement_deployment_flattened_async():
    client = FindingsRefinementServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_findings_refinement_deployment), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = findings_refinement.FindingsRefinementDeployment()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            findings_refinement.FindingsRefinementDeployment()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.update_findings_refinement_deployment(
            findings_refinement_deployment=findings_refinement.FindingsRefinementDeployment(
                detection_exclusion_application=findings_refinement.DetectionExclusionApplication(
                    curated_rule_sets=["curated_rule_sets_value"]
                )
            ),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].findings_refinement_deployment
        mock_val = findings_refinement.FindingsRefinementDeployment(
            detection_exclusion_application=findings_refinement.DetectionExclusionApplication(
                curated_rule_sets=["curated_rule_sets_value"]
            )
        )
        assert arg == mock_val
        arg = args[0].update_mask
        mock_val = field_mask_pb2.FieldMask(paths=["paths_value"])
        assert arg == mock_val


@pytest.mark.asyncio
async def test_update_findings_refinement_deployment_flattened_error_async():
    client = FindingsRefinementServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.update_findings_refinement_deployment(
            findings_refinement.UpdateFindingsRefinementDeploymentRequest(),
            findings_refinement_deployment=findings_refinement.FindingsRefinementDeployment(
                detection_exclusion_application=findings_refinement.DetectionExclusionApplication(
                    curated_rule_sets=["curated_rule_sets_value"]
                )
            ),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


@pytest.mark.parametrize(
    "request_type",
    [
        findings_refinement.ListAllFindingsRefinementDeploymentsRequest(),
        {},
    ],
)
def test_list_all_findings_refinement_deployments(
    request_type, transport: str = "grpc"
):
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_all_findings_refinement_deployments), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = (
            findings_refinement.ListAllFindingsRefinementDeploymentsResponse(
                next_page_token="next_page_token_value",
            )
        )
        response = client.list_all_findings_refinement_deployments(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = findings_refinement.ListAllFindingsRefinementDeploymentsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListAllFindingsRefinementDeploymentsPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_all_findings_refinement_deployments_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = findings_refinement.ListAllFindingsRefinementDeploymentsRequest(
        instance="instance_value",
        page_token="page_token_value",
        filter="filter_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_all_findings_refinement_deployments), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.list_all_findings_refinement_deployments(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = findings_refinement.ListAllFindingsRefinementDeploymentsRequest(
            instance="instance_value",
            page_token="page_token_value",
            filter="filter_value",
        )
        assert args[0] == request_msg


def test_list_all_findings_refinement_deployments_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = FindingsRefinementServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.list_all_findings_refinement_deployments
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.list_all_findings_refinement_deployments
        ] = mock_rpc
        request = {}
        client.list_all_findings_refinement_deployments(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_all_findings_refinement_deployments(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_list_all_findings_refinement_deployments_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = FindingsRefinementServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.list_all_findings_refinement_deployments
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.list_all_findings_refinement_deployments
        ] = mock_rpc

        request = {}
        await client.list_all_findings_refinement_deployments(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.list_all_findings_refinement_deployments(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        findings_refinement.ListAllFindingsRefinementDeploymentsRequest(),
        {},
    ],
)
async def test_list_all_findings_refinement_deployments_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = FindingsRefinementServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_all_findings_refinement_deployments), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            findings_refinement.ListAllFindingsRefinementDeploymentsResponse(
                next_page_token="next_page_token_value",
            )
        )
        response = await client.list_all_findings_refinement_deployments(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = findings_refinement.ListAllFindingsRefinementDeploymentsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListAllFindingsRefinementDeploymentsAsyncPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_all_findings_refinement_deployments_field_headers():
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = findings_refinement.ListAllFindingsRefinementDeploymentsRequest()

    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_all_findings_refinement_deployments), "__call__"
    ) as call:
        call.return_value = (
            findings_refinement.ListAllFindingsRefinementDeploymentsResponse()
        )
        client.list_all_findings_refinement_deployments(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_list_all_findings_refinement_deployments_field_headers_async():
    client = FindingsRefinementServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = findings_refinement.ListAllFindingsRefinementDeploymentsRequest()

    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_all_findings_refinement_deployments), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            findings_refinement.ListAllFindingsRefinementDeploymentsResponse()
        )
        await client.list_all_findings_refinement_deployments(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "instance=instance_value",
    ) in kw["metadata"]


def test_list_all_findings_refinement_deployments_flattened():
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_all_findings_refinement_deployments), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = (
            findings_refinement.ListAllFindingsRefinementDeploymentsResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.list_all_findings_refinement_deployments(
            instance="instance_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].instance
        mock_val = "instance_value"
        assert arg == mock_val


def test_list_all_findings_refinement_deployments_flattened_error():
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_all_findings_refinement_deployments(
            findings_refinement.ListAllFindingsRefinementDeploymentsRequest(),
            instance="instance_value",
        )


@pytest.mark.asyncio
async def test_list_all_findings_refinement_deployments_flattened_async():
    client = FindingsRefinementServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_all_findings_refinement_deployments), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = (
            findings_refinement.ListAllFindingsRefinementDeploymentsResponse()
        )

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            findings_refinement.ListAllFindingsRefinementDeploymentsResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.list_all_findings_refinement_deployments(
            instance="instance_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].instance
        mock_val = "instance_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_list_all_findings_refinement_deployments_flattened_error_async():
    client = FindingsRefinementServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.list_all_findings_refinement_deployments(
            findings_refinement.ListAllFindingsRefinementDeploymentsRequest(),
            instance="instance_value",
        )


def test_list_all_findings_refinement_deployments_pager(transport_name: str = "grpc"):
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_all_findings_refinement_deployments), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            findings_refinement.ListAllFindingsRefinementDeploymentsResponse(
                all_findings_refinement_deployments=[
                    findings_refinement.FindingsRefinementDeployment(),
                    findings_refinement.FindingsRefinementDeployment(),
                    findings_refinement.FindingsRefinementDeployment(),
                ],
                next_page_token="abc",
            ),
            findings_refinement.ListAllFindingsRefinementDeploymentsResponse(
                all_findings_refinement_deployments=[],
                next_page_token="def",
            ),
            findings_refinement.ListAllFindingsRefinementDeploymentsResponse(
                all_findings_refinement_deployments=[
                    findings_refinement.FindingsRefinementDeployment(),
                ],
                next_page_token="ghi",
            ),
            findings_refinement.ListAllFindingsRefinementDeploymentsResponse(
                all_findings_refinement_deployments=[
                    findings_refinement.FindingsRefinementDeployment(),
                    findings_refinement.FindingsRefinementDeployment(),
                ],
            ),
            RuntimeError,
        )

        expected_metadata = ()
        retry = retries.Retry()
        timeout = 5
        expected_metadata = tuple(expected_metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("instance", ""),)),
        )
        pager = client.list_all_findings_refinement_deployments(
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
            isinstance(i, findings_refinement.FindingsRefinementDeployment)
            for i in results
        )


def test_list_all_findings_refinement_deployments_pages(transport_name: str = "grpc"):
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_all_findings_refinement_deployments), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            findings_refinement.ListAllFindingsRefinementDeploymentsResponse(
                all_findings_refinement_deployments=[
                    findings_refinement.FindingsRefinementDeployment(),
                    findings_refinement.FindingsRefinementDeployment(),
                    findings_refinement.FindingsRefinementDeployment(),
                ],
                next_page_token="abc",
            ),
            findings_refinement.ListAllFindingsRefinementDeploymentsResponse(
                all_findings_refinement_deployments=[],
                next_page_token="def",
            ),
            findings_refinement.ListAllFindingsRefinementDeploymentsResponse(
                all_findings_refinement_deployments=[
                    findings_refinement.FindingsRefinementDeployment(),
                ],
                next_page_token="ghi",
            ),
            findings_refinement.ListAllFindingsRefinementDeploymentsResponse(
                all_findings_refinement_deployments=[
                    findings_refinement.FindingsRefinementDeployment(),
                    findings_refinement.FindingsRefinementDeployment(),
                ],
            ),
            RuntimeError,
        )
        pages = list(client.list_all_findings_refinement_deployments(request={}).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.asyncio
async def test_list_all_findings_refinement_deployments_async_pager():
    client = FindingsRefinementServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_all_findings_refinement_deployments),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            findings_refinement.ListAllFindingsRefinementDeploymentsResponse(
                all_findings_refinement_deployments=[
                    findings_refinement.FindingsRefinementDeployment(),
                    findings_refinement.FindingsRefinementDeployment(),
                    findings_refinement.FindingsRefinementDeployment(),
                ],
                next_page_token="abc",
            ),
            findings_refinement.ListAllFindingsRefinementDeploymentsResponse(
                all_findings_refinement_deployments=[],
                next_page_token="def",
            ),
            findings_refinement.ListAllFindingsRefinementDeploymentsResponse(
                all_findings_refinement_deployments=[
                    findings_refinement.FindingsRefinementDeployment(),
                ],
                next_page_token="ghi",
            ),
            findings_refinement.ListAllFindingsRefinementDeploymentsResponse(
                all_findings_refinement_deployments=[
                    findings_refinement.FindingsRefinementDeployment(),
                    findings_refinement.FindingsRefinementDeployment(),
                ],
            ),
            RuntimeError,
        )
        async_pager = await client.list_all_findings_refinement_deployments(
            request={},
        )
        assert async_pager.next_page_token == "abc"
        assert str(async_pager).startswith(f"{async_pager.__class__.__name__}<")

        responses = []
        async for response in async_pager:  # pragma: no branch
            responses.append(response)

        assert len(responses) == 6
        assert all(
            isinstance(i, findings_refinement.FindingsRefinementDeployment)
            for i in responses
        )


@pytest.mark.asyncio
async def test_list_all_findings_refinement_deployments_async_pages():
    client = FindingsRefinementServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_all_findings_refinement_deployments),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            findings_refinement.ListAllFindingsRefinementDeploymentsResponse(
                all_findings_refinement_deployments=[
                    findings_refinement.FindingsRefinementDeployment(),
                    findings_refinement.FindingsRefinementDeployment(),
                    findings_refinement.FindingsRefinementDeployment(),
                ],
                next_page_token="abc",
            ),
            findings_refinement.ListAllFindingsRefinementDeploymentsResponse(
                all_findings_refinement_deployments=[],
                next_page_token="def",
            ),
            findings_refinement.ListAllFindingsRefinementDeploymentsResponse(
                all_findings_refinement_deployments=[
                    findings_refinement.FindingsRefinementDeployment(),
                ],
                next_page_token="ghi",
            ),
            findings_refinement.ListAllFindingsRefinementDeploymentsResponse(
                all_findings_refinement_deployments=[
                    findings_refinement.FindingsRefinementDeployment(),
                    findings_refinement.FindingsRefinementDeployment(),
                ],
            ),
            RuntimeError,
        )
        pages = []
        async for page_ in (
            await client.list_all_findings_refinement_deployments(request={})
        ).pages:
            pages.append(page_)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.parametrize(
    "request_type",
    [
        findings_refinement.ComputeFindingsRefinementActivityRequest(),
        {},
    ],
)
def test_compute_findings_refinement_activity(request_type, transport: str = "grpc"):
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.compute_findings_refinement_activity), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = (
            findings_refinement.ComputeFindingsRefinementActivityResponse()
        )
        response = client.compute_findings_refinement_activity(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = findings_refinement.ComputeFindingsRefinementActivityRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(
        response, findings_refinement.ComputeFindingsRefinementActivityResponse
    )


def test_compute_findings_refinement_activity_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = findings_refinement.ComputeFindingsRefinementActivityRequest(
        name="name_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.compute_findings_refinement_activity), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.compute_findings_refinement_activity(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = findings_refinement.ComputeFindingsRefinementActivityRequest(
            name="name_value",
        )
        assert args[0] == request_msg


def test_compute_findings_refinement_activity_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = FindingsRefinementServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.compute_findings_refinement_activity
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.compute_findings_refinement_activity
        ] = mock_rpc
        request = {}
        client.compute_findings_refinement_activity(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.compute_findings_refinement_activity(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_compute_findings_refinement_activity_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = FindingsRefinementServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.compute_findings_refinement_activity
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.compute_findings_refinement_activity
        ] = mock_rpc

        request = {}
        await client.compute_findings_refinement_activity(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.compute_findings_refinement_activity(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        findings_refinement.ComputeFindingsRefinementActivityRequest(),
        {},
    ],
)
async def test_compute_findings_refinement_activity_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = FindingsRefinementServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.compute_findings_refinement_activity), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            findings_refinement.ComputeFindingsRefinementActivityResponse()
        )
        response = await client.compute_findings_refinement_activity(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = findings_refinement.ComputeFindingsRefinementActivityRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(
        response, findings_refinement.ComputeFindingsRefinementActivityResponse
    )


def test_compute_findings_refinement_activity_field_headers():
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = findings_refinement.ComputeFindingsRefinementActivityRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.compute_findings_refinement_activity), "__call__"
    ) as call:
        call.return_value = (
            findings_refinement.ComputeFindingsRefinementActivityResponse()
        )
        client.compute_findings_refinement_activity(request)

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
async def test_compute_findings_refinement_activity_field_headers_async():
    client = FindingsRefinementServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = findings_refinement.ComputeFindingsRefinementActivityRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.compute_findings_refinement_activity), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            findings_refinement.ComputeFindingsRefinementActivityResponse()
        )
        await client.compute_findings_refinement_activity(request)

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


def test_compute_findings_refinement_activity_flattened():
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.compute_findings_refinement_activity), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = (
            findings_refinement.ComputeFindingsRefinementActivityResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.compute_findings_refinement_activity(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_compute_findings_refinement_activity_flattened_error():
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.compute_findings_refinement_activity(
            findings_refinement.ComputeFindingsRefinementActivityRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_compute_findings_refinement_activity_flattened_async():
    client = FindingsRefinementServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.compute_findings_refinement_activity), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = (
            findings_refinement.ComputeFindingsRefinementActivityResponse()
        )

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            findings_refinement.ComputeFindingsRefinementActivityResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.compute_findings_refinement_activity(
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
async def test_compute_findings_refinement_activity_flattened_error_async():
    client = FindingsRefinementServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.compute_findings_refinement_activity(
            findings_refinement.ComputeFindingsRefinementActivityRequest(),
            name="name_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        findings_refinement.ComputeAllFindingsRefinementActivitiesRequest(),
        {},
    ],
)
def test_compute_all_findings_refinement_activities(
    request_type, transport: str = "grpc"
):
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.compute_all_findings_refinement_activities), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = (
            findings_refinement.ComputeAllFindingsRefinementActivitiesResponse()
        )
        response = client.compute_all_findings_refinement_activities(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = findings_refinement.ComputeAllFindingsRefinementActivitiesRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(
        response, findings_refinement.ComputeAllFindingsRefinementActivitiesResponse
    )


def test_compute_all_findings_refinement_activities_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = findings_refinement.ComputeAllFindingsRefinementActivitiesRequest(
        instance="instance_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.compute_all_findings_refinement_activities), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.compute_all_findings_refinement_activities(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = findings_refinement.ComputeAllFindingsRefinementActivitiesRequest(
            instance="instance_value",
        )
        assert args[0] == request_msg


def test_compute_all_findings_refinement_activities_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = FindingsRefinementServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.compute_all_findings_refinement_activities
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.compute_all_findings_refinement_activities
        ] = mock_rpc
        request = {}
        client.compute_all_findings_refinement_activities(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.compute_all_findings_refinement_activities(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_compute_all_findings_refinement_activities_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = FindingsRefinementServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.compute_all_findings_refinement_activities
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.compute_all_findings_refinement_activities
        ] = mock_rpc

        request = {}
        await client.compute_all_findings_refinement_activities(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.compute_all_findings_refinement_activities(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        findings_refinement.ComputeAllFindingsRefinementActivitiesRequest(),
        {},
    ],
)
async def test_compute_all_findings_refinement_activities_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = FindingsRefinementServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.compute_all_findings_refinement_activities), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            findings_refinement.ComputeAllFindingsRefinementActivitiesResponse()
        )
        response = await client.compute_all_findings_refinement_activities(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = findings_refinement.ComputeAllFindingsRefinementActivitiesRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(
        response, findings_refinement.ComputeAllFindingsRefinementActivitiesResponse
    )


def test_compute_all_findings_refinement_activities_field_headers():
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = findings_refinement.ComputeAllFindingsRefinementActivitiesRequest()

    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.compute_all_findings_refinement_activities), "__call__"
    ) as call:
        call.return_value = (
            findings_refinement.ComputeAllFindingsRefinementActivitiesResponse()
        )
        client.compute_all_findings_refinement_activities(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_compute_all_findings_refinement_activities_field_headers_async():
    client = FindingsRefinementServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = findings_refinement.ComputeAllFindingsRefinementActivitiesRequest()

    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.compute_all_findings_refinement_activities), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            findings_refinement.ComputeAllFindingsRefinementActivitiesResponse()
        )
        await client.compute_all_findings_refinement_activities(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "instance=instance_value",
    ) in kw["metadata"]


def test_compute_all_findings_refinement_activities_flattened():
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.compute_all_findings_refinement_activities), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = (
            findings_refinement.ComputeAllFindingsRefinementActivitiesResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.compute_all_findings_refinement_activities(
            instance="instance_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].instance
        mock_val = "instance_value"
        assert arg == mock_val


def test_compute_all_findings_refinement_activities_flattened_error():
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.compute_all_findings_refinement_activities(
            findings_refinement.ComputeAllFindingsRefinementActivitiesRequest(),
            instance="instance_value",
        )


@pytest.mark.asyncio
async def test_compute_all_findings_refinement_activities_flattened_async():
    client = FindingsRefinementServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.compute_all_findings_refinement_activities), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = (
            findings_refinement.ComputeAllFindingsRefinementActivitiesResponse()
        )

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            findings_refinement.ComputeAllFindingsRefinementActivitiesResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.compute_all_findings_refinement_activities(
            instance="instance_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].instance
        mock_val = "instance_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_compute_all_findings_refinement_activities_flattened_error_async():
    client = FindingsRefinementServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.compute_all_findings_refinement_activities(
            findings_refinement.ComputeAllFindingsRefinementActivitiesRequest(),
            instance="instance_value",
        )


def test_get_findings_refinement_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = FindingsRefinementServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.get_findings_refinement
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.get_findings_refinement
        ] = mock_rpc

        request = {}
        client.get_findings_refinement(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_findings_refinement(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_get_findings_refinement_rest_required_fields(
    request_type=findings_refinement.GetFindingsRefinementRequest,
):
    transport_class = transports.FindingsRefinementServiceRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseGetFindingsRefinement,
        "_BaseGetFindingsRefinement__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = findings_refinement.FindingsRefinement()
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
            return_value = findings_refinement.FindingsRefinement.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.get_findings_refinement(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_get_findings_refinement_rest_flattened():
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = findings_refinement.FindingsRefinement()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "name": "projects/sample1/locations/sample2/instances/sample3/findingsRefinements/sample4"
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
        return_value = findings_refinement.FindingsRefinement.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.get_findings_refinement(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{name=projects/*/locations/*/instances/*/findingsRefinements/*}"
            % client.transport._host,
            args[1],
        )


def test_get_findings_refinement_rest_flattened_error(transport: str = "rest"):
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_findings_refinement(
            findings_refinement.GetFindingsRefinementRequest(),
            name="name_value",
        )


def test_list_findings_refinements_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = FindingsRefinementServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.list_findings_refinements
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.list_findings_refinements
        ] = mock_rpc

        request = {}
        client.list_findings_refinements(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_findings_refinements(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_list_findings_refinements_rest_required_fields(
    request_type=findings_refinement.ListFindingsRefinementsRequest,
):
    transport_class = transports.FindingsRefinementServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseListFindingsRefinements,
        "_BaseListFindingsRefinements__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = findings_refinement.ListFindingsRefinementsResponse()
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
            return_value = findings_refinement.ListFindingsRefinementsResponse.pb(
                return_value
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.list_findings_refinements(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_list_findings_refinements_rest_flattened():
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = findings_refinement.ListFindingsRefinementsResponse()

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
        return_value = findings_refinement.ListFindingsRefinementsResponse.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.list_findings_refinements(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=projects/*/locations/*/instances/*}/findingsRefinements"
            % client.transport._host,
            args[1],
        )


def test_list_findings_refinements_rest_flattened_error(transport: str = "rest"):
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_findings_refinements(
            findings_refinement.ListFindingsRefinementsRequest(),
            parent="parent_value",
        )


def test_list_findings_refinements_rest_pager(transport: str = "rest"):
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        # with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            findings_refinement.ListFindingsRefinementsResponse(
                findings_refinements=[
                    findings_refinement.FindingsRefinement(),
                    findings_refinement.FindingsRefinement(),
                    findings_refinement.FindingsRefinement(),
                ],
                next_page_token="abc",
            ),
            findings_refinement.ListFindingsRefinementsResponse(
                findings_refinements=[],
                next_page_token="def",
            ),
            findings_refinement.ListFindingsRefinementsResponse(
                findings_refinements=[
                    findings_refinement.FindingsRefinement(),
                ],
                next_page_token="ghi",
            ),
            findings_refinement.ListFindingsRefinementsResponse(
                findings_refinements=[
                    findings_refinement.FindingsRefinement(),
                    findings_refinement.FindingsRefinement(),
                ],
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(
            findings_refinement.ListFindingsRefinementsResponse.to_json(x)
            for x in response
        )
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode("UTF-8")
            return_val.status_code = 200
        req.side_effect = return_values

        sample_request = {
            "parent": "projects/sample1/locations/sample2/instances/sample3"
        }

        pager = client.list_findings_refinements(request=sample_request)

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(
            isinstance(i, findings_refinement.FindingsRefinement) for i in results
        )

        pages = list(client.list_findings_refinements(request=sample_request).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


def test_create_findings_refinement_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = FindingsRefinementServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.create_findings_refinement
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.create_findings_refinement
        ] = mock_rpc

        request = {}
        client.create_findings_refinement(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.create_findings_refinement(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_create_findings_refinement_rest_required_fields(
    request_type=gcc_findings_refinement.CreateFindingsRefinementRequest,
):
    transport_class = transports.FindingsRefinementServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseCreateFindingsRefinement,
        "_BaseCreateFindingsRefinement__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = gcc_findings_refinement.FindingsRefinement()
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
            return_value = gcc_findings_refinement.FindingsRefinement.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.create_findings_refinement(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_create_findings_refinement_rest_flattened():
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = gcc_findings_refinement.FindingsRefinement()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "parent": "projects/sample1/locations/sample2/instances/sample3"
        }

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
            findings_refinement=gcc_findings_refinement.FindingsRefinement(
                name="name_value"
            ),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = gcc_findings_refinement.FindingsRefinement.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.create_findings_refinement(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=projects/*/locations/*/instances/*}/findingsRefinements"
            % client.transport._host,
            args[1],
        )


def test_create_findings_refinement_rest_flattened_error(transport: str = "rest"):
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.create_findings_refinement(
            gcc_findings_refinement.CreateFindingsRefinementRequest(),
            parent="parent_value",
            findings_refinement=gcc_findings_refinement.FindingsRefinement(
                name="name_value"
            ),
        )


def test_update_findings_refinement_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = FindingsRefinementServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.update_findings_refinement
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.update_findings_refinement
        ] = mock_rpc

        request = {}
        client.update_findings_refinement(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.update_findings_refinement(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_update_findings_refinement_rest_required_fields(
    request_type=gcc_findings_refinement.UpdateFindingsRefinementRequest,
):
    transport_class = transports.FindingsRefinementServiceRestTransport

    request_init = {}
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseUpdateFindingsRefinement,
        "_BaseUpdateFindingsRefinement__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = gcc_findings_refinement.FindingsRefinement()
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
            return_value = gcc_findings_refinement.FindingsRefinement.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.update_findings_refinement(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_update_findings_refinement_rest_flattened():
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = gcc_findings_refinement.FindingsRefinement()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "findings_refinement": {
                "name": "projects/sample1/locations/sample2/instances/sample3/findingsRefinements/sample4"
            }
        }

        # get truthy value for each flattened field
        mock_args = dict(
            findings_refinement=gcc_findings_refinement.FindingsRefinement(
                name="name_value"
            ),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = gcc_findings_refinement.FindingsRefinement.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.update_findings_refinement(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{findings_refinement.name=projects/*/locations/*/instances/*/findingsRefinements/*}"
            % client.transport._host,
            args[1],
        )


def test_update_findings_refinement_rest_flattened_error(transport: str = "rest"):
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.update_findings_refinement(
            gcc_findings_refinement.UpdateFindingsRefinementRequest(),
            findings_refinement=gcc_findings_refinement.FindingsRefinement(
                name="name_value"
            ),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


def test_get_findings_refinement_deployment_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = FindingsRefinementServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.get_findings_refinement_deployment
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.get_findings_refinement_deployment
        ] = mock_rpc

        request = {}
        client.get_findings_refinement_deployment(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_findings_refinement_deployment(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_get_findings_refinement_deployment_rest_required_fields(
    request_type=findings_refinement.GetFindingsRefinementDeploymentRequest,
):
    transport_class = transports.FindingsRefinementServiceRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseGetFindingsRefinementDeployment,
        "_BaseGetFindingsRefinementDeployment__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = findings_refinement.FindingsRefinementDeployment()
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
            return_value = findings_refinement.FindingsRefinementDeployment.pb(
                return_value
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.get_findings_refinement_deployment(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_get_findings_refinement_deployment_rest_flattened():
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = findings_refinement.FindingsRefinementDeployment()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "name": "projects/sample1/locations/sample2/instances/sample3/findingsRefinements/sample4/deployment"
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
        return_value = findings_refinement.FindingsRefinementDeployment.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.get_findings_refinement_deployment(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{name=projects/*/locations/*/instances/*/findingsRefinements/*/deployment}"
            % client.transport._host,
            args[1],
        )


def test_get_findings_refinement_deployment_rest_flattened_error(
    transport: str = "rest",
):
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_findings_refinement_deployment(
            findings_refinement.GetFindingsRefinementDeploymentRequest(),
            name="name_value",
        )


def test_update_findings_refinement_deployment_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = FindingsRefinementServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.update_findings_refinement_deployment
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.update_findings_refinement_deployment
        ] = mock_rpc

        request = {}
        client.update_findings_refinement_deployment(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.update_findings_refinement_deployment(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_update_findings_refinement_deployment_rest_required_fields(
    request_type=findings_refinement.UpdateFindingsRefinementDeploymentRequest,
):
    transport_class = transports.FindingsRefinementServiceRestTransport

    request_init = {}
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseUpdateFindingsRefinementDeployment,
        "_BaseUpdateFindingsRefinementDeployment__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = findings_refinement.FindingsRefinementDeployment()
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
            return_value = findings_refinement.FindingsRefinementDeployment.pb(
                return_value
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.update_findings_refinement_deployment(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_update_findings_refinement_deployment_rest_flattened():
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = findings_refinement.FindingsRefinementDeployment()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "findings_refinement_deployment": {
                "name": "projects/sample1/locations/sample2/instances/sample3/findingsRefinements/sample4/deployment"
            }
        }

        # get truthy value for each flattened field
        mock_args = dict(
            findings_refinement_deployment=findings_refinement.FindingsRefinementDeployment(
                detection_exclusion_application=findings_refinement.DetectionExclusionApplication(
                    curated_rule_sets=["curated_rule_sets_value"]
                )
            ),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = findings_refinement.FindingsRefinementDeployment.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.update_findings_refinement_deployment(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{findings_refinement_deployment.name=projects/*/locations/*/instances/*/findingsRefinements/*/deployment}"
            % client.transport._host,
            args[1],
        )


def test_update_findings_refinement_deployment_rest_flattened_error(
    transport: str = "rest",
):
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.update_findings_refinement_deployment(
            findings_refinement.UpdateFindingsRefinementDeploymentRequest(),
            findings_refinement_deployment=findings_refinement.FindingsRefinementDeployment(
                detection_exclusion_application=findings_refinement.DetectionExclusionApplication(
                    curated_rule_sets=["curated_rule_sets_value"]
                )
            ),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


def test_list_all_findings_refinement_deployments_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = FindingsRefinementServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.list_all_findings_refinement_deployments
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.list_all_findings_refinement_deployments
        ] = mock_rpc

        request = {}
        client.list_all_findings_refinement_deployments(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_all_findings_refinement_deployments(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_list_all_findings_refinement_deployments_rest_required_fields(
    request_type=findings_refinement.ListAllFindingsRefinementDeploymentsRequest,
):
    transport_class = transports.FindingsRefinementServiceRestTransport

    request_init = {}
    request_init["instance"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseListAllFindingsRefinementDeployments,
        "_BaseListAllFindingsRefinementDeployments__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["instance"] = "instance_value"

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(
        (
            "filter",
            "pageSize",
            "pageToken",
        )
    )

    # verify required fields with non-default values are left alone
    assert "instance" in jsonified_request
    assert jsonified_request["instance"] == "instance_value"

    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = findings_refinement.ListAllFindingsRefinementDeploymentsResponse()
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
            return_value = (
                findings_refinement.ListAllFindingsRefinementDeploymentsResponse.pb(
                    return_value
                )
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.list_all_findings_refinement_deployments(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_list_all_findings_refinement_deployments_rest_flattened():
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = (
            findings_refinement.ListAllFindingsRefinementDeploymentsResponse()
        )

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "instance": "projects/sample1/locations/sample2/instances/sample3"
        }

        # get truthy value for each flattened field
        mock_args = dict(
            instance="instance_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = (
            findings_refinement.ListAllFindingsRefinementDeploymentsResponse.pb(
                return_value
            )
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.list_all_findings_refinement_deployments(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{instance=projects/*/locations/*/instances/*}:listAllFindingsRefinementDeployments"
            % client.transport._host,
            args[1],
        )


def test_list_all_findings_refinement_deployments_rest_flattened_error(
    transport: str = "rest",
):
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_all_findings_refinement_deployments(
            findings_refinement.ListAllFindingsRefinementDeploymentsRequest(),
            instance="instance_value",
        )


def test_list_all_findings_refinement_deployments_rest_pager(transport: str = "rest"):
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        # with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            findings_refinement.ListAllFindingsRefinementDeploymentsResponse(
                all_findings_refinement_deployments=[
                    findings_refinement.FindingsRefinementDeployment(),
                    findings_refinement.FindingsRefinementDeployment(),
                    findings_refinement.FindingsRefinementDeployment(),
                ],
                next_page_token="abc",
            ),
            findings_refinement.ListAllFindingsRefinementDeploymentsResponse(
                all_findings_refinement_deployments=[],
                next_page_token="def",
            ),
            findings_refinement.ListAllFindingsRefinementDeploymentsResponse(
                all_findings_refinement_deployments=[
                    findings_refinement.FindingsRefinementDeployment(),
                ],
                next_page_token="ghi",
            ),
            findings_refinement.ListAllFindingsRefinementDeploymentsResponse(
                all_findings_refinement_deployments=[
                    findings_refinement.FindingsRefinementDeployment(),
                    findings_refinement.FindingsRefinementDeployment(),
                ],
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(
            findings_refinement.ListAllFindingsRefinementDeploymentsResponse.to_json(x)
            for x in response
        )
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode("UTF-8")
            return_val.status_code = 200
        req.side_effect = return_values

        sample_request = {
            "instance": "projects/sample1/locations/sample2/instances/sample3"
        }

        pager = client.list_all_findings_refinement_deployments(request=sample_request)

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(
            isinstance(i, findings_refinement.FindingsRefinementDeployment)
            for i in results
        )

        pages = list(
            client.list_all_findings_refinement_deployments(
                request=sample_request
            ).pages
        )
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


def test_compute_findings_refinement_activity_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = FindingsRefinementServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.compute_findings_refinement_activity
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.compute_findings_refinement_activity
        ] = mock_rpc

        request = {}
        client.compute_findings_refinement_activity(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.compute_findings_refinement_activity(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_compute_findings_refinement_activity_rest_required_fields(
    request_type=findings_refinement.ComputeFindingsRefinementActivityRequest,
):
    transport_class = transports.FindingsRefinementServiceRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseComputeFindingsRefinementActivity,
        "_BaseComputeFindingsRefinementActivity__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = findings_refinement.ComputeFindingsRefinementActivityResponse()
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
                findings_refinement.ComputeFindingsRefinementActivityResponse.pb(
                    return_value
                )
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.compute_findings_refinement_activity(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_compute_findings_refinement_activity_rest_flattened():
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = findings_refinement.ComputeFindingsRefinementActivityResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "name": "projects/sample1/locations/sample2/instances/sample3/findingsRefinements/sample4"
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
        return_value = findings_refinement.ComputeFindingsRefinementActivityResponse.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.compute_findings_refinement_activity(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{name=projects/*/locations/*/instances/*/findingsRefinements/*}:computeFindingsRefinementActivity"
            % client.transport._host,
            args[1],
        )


def test_compute_findings_refinement_activity_rest_flattened_error(
    transport: str = "rest",
):
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.compute_findings_refinement_activity(
            findings_refinement.ComputeFindingsRefinementActivityRequest(),
            name="name_value",
        )


def test_compute_all_findings_refinement_activities_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = FindingsRefinementServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.compute_all_findings_refinement_activities
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.compute_all_findings_refinement_activities
        ] = mock_rpc

        request = {}
        client.compute_all_findings_refinement_activities(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.compute_all_findings_refinement_activities(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_compute_all_findings_refinement_activities_rest_required_fields(
    request_type=findings_refinement.ComputeAllFindingsRefinementActivitiesRequest,
):
    transport_class = transports.FindingsRefinementServiceRestTransport

    request_init = {}
    request_init["instance"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseComputeAllFindingsRefinementActivities,
        "_BaseComputeAllFindingsRefinementActivities__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["instance"] = "instance_value"

    # verify required fields with non-default values are left alone
    assert "instance" in jsonified_request
    assert jsonified_request["instance"] == "instance_value"

    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = findings_refinement.ComputeAllFindingsRefinementActivitiesResponse()
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
                findings_refinement.ComputeAllFindingsRefinementActivitiesResponse.pb(
                    return_value
                )
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.compute_all_findings_refinement_activities(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_compute_all_findings_refinement_activities_rest_flattened():
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = (
            findings_refinement.ComputeAllFindingsRefinementActivitiesResponse()
        )

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "instance": "projects/sample1/locations/sample2/instances/sample3"
        }

        # get truthy value for each flattened field
        mock_args = dict(
            instance="instance_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = (
            findings_refinement.ComputeAllFindingsRefinementActivitiesResponse.pb(
                return_value
            )
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.compute_all_findings_refinement_activities(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{instance=projects/*/locations/*/instances/*}:computeAllFindingsRefinementActivities"
            % client.transport._host,
            args[1],
        )


def test_compute_all_findings_refinement_activities_rest_flattened_error(
    transport: str = "rest",
):
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.compute_all_findings_refinement_activities(
            findings_refinement.ComputeAllFindingsRefinementActivitiesRequest(),
            instance="instance_value",
        )


def test_credentials_transport_error():
    # It is an error to provide credentials and a transport instance.
    transport = transports.FindingsRefinementServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = FindingsRefinementServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport=transport,
        )

    # It is an error to provide a credentials file and a transport instance.
    transport = transports.FindingsRefinementServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = FindingsRefinementServiceClient(
            client_options={"credentials_file": "credentials.json"},
            transport=transport,
        )

    # It is an error to provide an api_key and a transport instance.
    transport = transports.FindingsRefinementServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    options = client_options.ClientOptions()
    options.api_key = "api_key"
    with pytest.raises(ValueError):
        client = FindingsRefinementServiceClient(
            client_options=options,
            transport=transport,
        )

    # It is an error to provide an api_key and a credential.
    options = client_options.ClientOptions()
    options.api_key = "api_key"
    with pytest.raises(ValueError):
        client = FindingsRefinementServiceClient(
            client_options=options, credentials=ga_credentials.AnonymousCredentials()
        )

    # It is an error to provide scopes and a transport instance.
    transport = transports.FindingsRefinementServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = FindingsRefinementServiceClient(
            client_options={"scopes": ["1", "2"]},
            transport=transport,
        )


def test_transport_instance():
    # A client may be instantiated with a custom transport instance.
    transport = transports.FindingsRefinementServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    client = FindingsRefinementServiceClient(transport=transport)
    assert client.transport is transport


def test_transport_get_channel():
    # A client may be instantiated with a custom transport instance.
    transport = transports.FindingsRefinementServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    channel = transport.grpc_channel
    assert channel

    transport = transports.FindingsRefinementServiceGrpcAsyncIOTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    channel = transport.grpc_channel
    assert channel


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.FindingsRefinementServiceGrpcTransport,
        transports.FindingsRefinementServiceGrpcAsyncIOTransport,
        transports.FindingsRefinementServiceRestTransport,
    ],
)
def test_transport_adc(transport_class):
    # Test default credentials are used if not provided.
    with mock.patch.object(google.auth, "default") as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport_class()
        adc.assert_called_once()


def test_transport_kind_grpc():
    transport = FindingsRefinementServiceClient.get_transport_class("grpc")(
        credentials=ga_credentials.AnonymousCredentials()
    )
    assert transport.kind == "grpc"


def test_initialize_client_w_grpc():
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="grpc"
    )
    assert client is not None


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_findings_refinement_empty_call_grpc():
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.get_findings_refinement), "__call__"
    ) as call:
        call.return_value = findings_refinement.FindingsRefinement()
        client.get_findings_refinement(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = findings_refinement.GetFindingsRefinementRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_findings_refinements_empty_call_grpc():
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_findings_refinements), "__call__"
    ) as call:
        call.return_value = findings_refinement.ListFindingsRefinementsResponse()
        client.list_findings_refinements(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = findings_refinement.ListFindingsRefinementsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_create_findings_refinement_empty_call_grpc():
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.create_findings_refinement), "__call__"
    ) as call:
        call.return_value = gcc_findings_refinement.FindingsRefinement()
        client.create_findings_refinement(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gcc_findings_refinement.CreateFindingsRefinementRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_update_findings_refinement_empty_call_grpc():
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.update_findings_refinement), "__call__"
    ) as call:
        call.return_value = gcc_findings_refinement.FindingsRefinement()
        client.update_findings_refinement(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gcc_findings_refinement.UpdateFindingsRefinementRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_findings_refinement_deployment_empty_call_grpc():
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.get_findings_refinement_deployment), "__call__"
    ) as call:
        call.return_value = findings_refinement.FindingsRefinementDeployment()
        client.get_findings_refinement_deployment(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = findings_refinement.GetFindingsRefinementDeploymentRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_update_findings_refinement_deployment_empty_call_grpc():
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.update_findings_refinement_deployment), "__call__"
    ) as call:
        call.return_value = findings_refinement.FindingsRefinementDeployment()
        client.update_findings_refinement_deployment(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = findings_refinement.UpdateFindingsRefinementDeploymentRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_all_findings_refinement_deployments_empty_call_grpc():
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_all_findings_refinement_deployments), "__call__"
    ) as call:
        call.return_value = (
            findings_refinement.ListAllFindingsRefinementDeploymentsResponse()
        )
        client.list_all_findings_refinement_deployments(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = findings_refinement.ListAllFindingsRefinementDeploymentsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_compute_findings_refinement_activity_empty_call_grpc():
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.compute_findings_refinement_activity), "__call__"
    ) as call:
        call.return_value = (
            findings_refinement.ComputeFindingsRefinementActivityResponse()
        )
        client.compute_findings_refinement_activity(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = findings_refinement.ComputeFindingsRefinementActivityRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_compute_all_findings_refinement_activities_empty_call_grpc():
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.compute_all_findings_refinement_activities), "__call__"
    ) as call:
        call.return_value = (
            findings_refinement.ComputeAllFindingsRefinementActivitiesResponse()
        )
        client.compute_all_findings_refinement_activities(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = (
            findings_refinement.ComputeAllFindingsRefinementActivitiesRequest()
        )
        assert args[0] == request_msg


def test_transport_kind_grpc_asyncio():
    transport = FindingsRefinementServiceAsyncClient.get_transport_class(
        "grpc_asyncio"
    )(credentials=async_anonymous_credentials())
    assert transport.kind == "grpc_asyncio"


def test_initialize_client_w_grpc_asyncio():
    client = FindingsRefinementServiceAsyncClient(
        credentials=async_anonymous_credentials(), transport="grpc_asyncio"
    )
    assert client is not None


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_get_findings_refinement_empty_call_grpc_asyncio():
    client = FindingsRefinementServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.get_findings_refinement), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            findings_refinement.FindingsRefinement(
                name="name_value",
                display_name="display_name_value",
                type_=findings_refinement.FindingsRefinementType.DETECTION_EXCLUSION,
                query="query_value",
            )
        )
        await client.get_findings_refinement(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = findings_refinement.GetFindingsRefinementRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_list_findings_refinements_empty_call_grpc_asyncio():
    client = FindingsRefinementServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_findings_refinements), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            findings_refinement.ListFindingsRefinementsResponse(
                next_page_token="next_page_token_value",
            )
        )
        await client.list_findings_refinements(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = findings_refinement.ListFindingsRefinementsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_create_findings_refinement_empty_call_grpc_asyncio():
    client = FindingsRefinementServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.create_findings_refinement), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            gcc_findings_refinement.FindingsRefinement(
                name="name_value",
                display_name="display_name_value",
                type_=gcc_findings_refinement.FindingsRefinementType.DETECTION_EXCLUSION,
                query="query_value",
            )
        )
        await client.create_findings_refinement(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gcc_findings_refinement.CreateFindingsRefinementRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_update_findings_refinement_empty_call_grpc_asyncio():
    client = FindingsRefinementServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.update_findings_refinement), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            gcc_findings_refinement.FindingsRefinement(
                name="name_value",
                display_name="display_name_value",
                type_=gcc_findings_refinement.FindingsRefinementType.DETECTION_EXCLUSION,
                query="query_value",
            )
        )
        await client.update_findings_refinement(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gcc_findings_refinement.UpdateFindingsRefinementRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_get_findings_refinement_deployment_empty_call_grpc_asyncio():
    client = FindingsRefinementServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.get_findings_refinement_deployment), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            findings_refinement.FindingsRefinementDeployment(
                name="name_value",
                enabled=True,
                archived=True,
            )
        )
        await client.get_findings_refinement_deployment(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = findings_refinement.GetFindingsRefinementDeploymentRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_update_findings_refinement_deployment_empty_call_grpc_asyncio():
    client = FindingsRefinementServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.update_findings_refinement_deployment), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            findings_refinement.FindingsRefinementDeployment(
                name="name_value",
                enabled=True,
                archived=True,
            )
        )
        await client.update_findings_refinement_deployment(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = findings_refinement.UpdateFindingsRefinementDeploymentRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_list_all_findings_refinement_deployments_empty_call_grpc_asyncio():
    client = FindingsRefinementServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_all_findings_refinement_deployments), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            findings_refinement.ListAllFindingsRefinementDeploymentsResponse(
                next_page_token="next_page_token_value",
            )
        )
        await client.list_all_findings_refinement_deployments(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = findings_refinement.ListAllFindingsRefinementDeploymentsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_compute_findings_refinement_activity_empty_call_grpc_asyncio():
    client = FindingsRefinementServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.compute_findings_refinement_activity), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            findings_refinement.ComputeFindingsRefinementActivityResponse()
        )
        await client.compute_findings_refinement_activity(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = findings_refinement.ComputeFindingsRefinementActivityRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_compute_all_findings_refinement_activities_empty_call_grpc_asyncio():
    client = FindingsRefinementServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.compute_all_findings_refinement_activities), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            findings_refinement.ComputeAllFindingsRefinementActivitiesResponse()
        )
        await client.compute_all_findings_refinement_activities(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = (
            findings_refinement.ComputeAllFindingsRefinementActivitiesRequest()
        )
        assert args[0] == request_msg


def test_transport_kind_rest():
    transport = FindingsRefinementServiceClient.get_transport_class("rest")(
        credentials=ga_credentials.AnonymousCredentials()
    )
    assert transport.kind == "rest"


def test_get_findings_refinement_rest_bad_request(
    request_type=findings_refinement.GetFindingsRefinementRequest,
):
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/instances/sample3/findingsRefinements/sample4"
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
        client.get_findings_refinement(request)


@pytest.mark.parametrize(
    "request_type",
    [
        findings_refinement.GetFindingsRefinementRequest,
        dict,
    ],
)
def test_get_findings_refinement_rest_call_success(request_type):
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/instances/sample3/findingsRefinements/sample4"
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = findings_refinement.FindingsRefinement(
            name="name_value",
            display_name="display_name_value",
            type_=findings_refinement.FindingsRefinementType.DETECTION_EXCLUSION,
            query="query_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = findings_refinement.FindingsRefinement.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.get_findings_refinement(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, findings_refinement.FindingsRefinement)
    assert response.name == "name_value"
    assert response.display_name == "display_name_value"
    assert (
        response.type_ == findings_refinement.FindingsRefinementType.DETECTION_EXCLUSION
    )
    assert response.query == "query_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_get_findings_refinement_rest_interceptors(null_interceptor):
    transport = transports.FindingsRefinementServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.FindingsRefinementServiceRestInterceptor(),
    )
    client = FindingsRefinementServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.FindingsRefinementServiceRestInterceptor,
            "post_get_findings_refinement",
        ) as post,
        mock.patch.object(
            transports.FindingsRefinementServiceRestInterceptor,
            "post_get_findings_refinement_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.FindingsRefinementServiceRestInterceptor,
            "pre_get_findings_refinement",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = findings_refinement.GetFindingsRefinementRequest.pb(
            findings_refinement.GetFindingsRefinementRequest()
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
        return_value = findings_refinement.FindingsRefinement.to_json(
            findings_refinement.FindingsRefinement()
        )
        req.return_value.content = return_value

        request = findings_refinement.GetFindingsRefinementRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = findings_refinement.FindingsRefinement()
        post_with_metadata.return_value = (
            findings_refinement.FindingsRefinement(),
            metadata,
        )

        client.get_findings_refinement(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_list_findings_refinements_rest_bad_request(
    request_type=findings_refinement.ListFindingsRefinementsRequest,
):
    client = FindingsRefinementServiceClient(
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
        client.list_findings_refinements(request)


@pytest.mark.parametrize(
    "request_type",
    [
        findings_refinement.ListFindingsRefinementsRequest,
        dict,
    ],
)
def test_list_findings_refinements_rest_call_success(request_type):
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1/locations/sample2/instances/sample3"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = findings_refinement.ListFindingsRefinementsResponse(
            next_page_token="next_page_token_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = findings_refinement.ListFindingsRefinementsResponse.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.list_findings_refinements(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListFindingsRefinementsPager)
    assert response.next_page_token == "next_page_token_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_list_findings_refinements_rest_interceptors(null_interceptor):
    transport = transports.FindingsRefinementServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.FindingsRefinementServiceRestInterceptor(),
    )
    client = FindingsRefinementServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.FindingsRefinementServiceRestInterceptor,
            "post_list_findings_refinements",
        ) as post,
        mock.patch.object(
            transports.FindingsRefinementServiceRestInterceptor,
            "post_list_findings_refinements_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.FindingsRefinementServiceRestInterceptor,
            "pre_list_findings_refinements",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = findings_refinement.ListFindingsRefinementsRequest.pb(
            findings_refinement.ListFindingsRefinementsRequest()
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
        return_value = findings_refinement.ListFindingsRefinementsResponse.to_json(
            findings_refinement.ListFindingsRefinementsResponse()
        )
        req.return_value.content = return_value

        request = findings_refinement.ListFindingsRefinementsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = findings_refinement.ListFindingsRefinementsResponse()
        post_with_metadata.return_value = (
            findings_refinement.ListFindingsRefinementsResponse(),
            metadata,
        )

        client.list_findings_refinements(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_create_findings_refinement_rest_bad_request(
    request_type=gcc_findings_refinement.CreateFindingsRefinementRequest,
):
    client = FindingsRefinementServiceClient(
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
        client.create_findings_refinement(request)


@pytest.mark.parametrize(
    "request_type",
    [
        gcc_findings_refinement.CreateFindingsRefinementRequest,
        dict,
    ],
)
def test_create_findings_refinement_rest_call_success(request_type):
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1/locations/sample2/instances/sample3"}
    request_init["findings_refinement"] = {
        "name": "name_value",
        "display_name": "display_name_value",
        "type_": 1,
        "create_time": {"seconds": 751, "nanos": 543},
        "update_time": {},
        "query": "query_value",
        "outcome_filters": [
            {
                "outcome_variable": "outcome_variable_value",
                "outcome_value": "outcome_value_value",
                "outcome_filter_operator": 1,
            }
        ],
    }
    # The version of a generated dependency at test runtime may differ from the version used during generation.
    # Delete any fields which are not present in the current runtime dependency
    # See https://github.com/googleapis/gapic-generator-python/issues/1748

    # Determine if the message type is proto-plus or protobuf
    test_field = gcc_findings_refinement.CreateFindingsRefinementRequest.meta.fields[
        "findings_refinement"
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
    for field, value in request_init["findings_refinement"].items():  # pragma: NO COVER
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
                for i in range(0, len(request_init["findings_refinement"][field])):
                    del request_init["findings_refinement"][field][i][subfield]
            else:
                del request_init["findings_refinement"][field][subfield]
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = gcc_findings_refinement.FindingsRefinement(
            name="name_value",
            display_name="display_name_value",
            type_=gcc_findings_refinement.FindingsRefinementType.DETECTION_EXCLUSION,
            query="query_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = gcc_findings_refinement.FindingsRefinement.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.create_findings_refinement(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, gcc_findings_refinement.FindingsRefinement)
    assert response.name == "name_value"
    assert response.display_name == "display_name_value"
    assert (
        response.type_
        == gcc_findings_refinement.FindingsRefinementType.DETECTION_EXCLUSION
    )
    assert response.query == "query_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_create_findings_refinement_rest_interceptors(null_interceptor):
    transport = transports.FindingsRefinementServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.FindingsRefinementServiceRestInterceptor(),
    )
    client = FindingsRefinementServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.FindingsRefinementServiceRestInterceptor,
            "post_create_findings_refinement",
        ) as post,
        mock.patch.object(
            transports.FindingsRefinementServiceRestInterceptor,
            "post_create_findings_refinement_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.FindingsRefinementServiceRestInterceptor,
            "pre_create_findings_refinement",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = gcc_findings_refinement.CreateFindingsRefinementRequest.pb(
            gcc_findings_refinement.CreateFindingsRefinementRequest()
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
        return_value = gcc_findings_refinement.FindingsRefinement.to_json(
            gcc_findings_refinement.FindingsRefinement()
        )
        req.return_value.content = return_value

        request = gcc_findings_refinement.CreateFindingsRefinementRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = gcc_findings_refinement.FindingsRefinement()
        post_with_metadata.return_value = (
            gcc_findings_refinement.FindingsRefinement(),
            metadata,
        )

        client.create_findings_refinement(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_update_findings_refinement_rest_bad_request(
    request_type=gcc_findings_refinement.UpdateFindingsRefinementRequest,
):
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {
        "findings_refinement": {
            "name": "projects/sample1/locations/sample2/instances/sample3/findingsRefinements/sample4"
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
        client.update_findings_refinement(request)


@pytest.mark.parametrize(
    "request_type",
    [
        gcc_findings_refinement.UpdateFindingsRefinementRequest,
        dict,
    ],
)
def test_update_findings_refinement_rest_call_success(request_type):
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {
        "findings_refinement": {
            "name": "projects/sample1/locations/sample2/instances/sample3/findingsRefinements/sample4"
        }
    }
    request_init["findings_refinement"] = {
        "name": "projects/sample1/locations/sample2/instances/sample3/findingsRefinements/sample4",
        "display_name": "display_name_value",
        "type_": 1,
        "create_time": {"seconds": 751, "nanos": 543},
        "update_time": {},
        "query": "query_value",
        "outcome_filters": [
            {
                "outcome_variable": "outcome_variable_value",
                "outcome_value": "outcome_value_value",
                "outcome_filter_operator": 1,
            }
        ],
    }
    # The version of a generated dependency at test runtime may differ from the version used during generation.
    # Delete any fields which are not present in the current runtime dependency
    # See https://github.com/googleapis/gapic-generator-python/issues/1748

    # Determine if the message type is proto-plus or protobuf
    test_field = gcc_findings_refinement.UpdateFindingsRefinementRequest.meta.fields[
        "findings_refinement"
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
    for field, value in request_init["findings_refinement"].items():  # pragma: NO COVER
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
                for i in range(0, len(request_init["findings_refinement"][field])):
                    del request_init["findings_refinement"][field][i][subfield]
            else:
                del request_init["findings_refinement"][field][subfield]
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = gcc_findings_refinement.FindingsRefinement(
            name="name_value",
            display_name="display_name_value",
            type_=gcc_findings_refinement.FindingsRefinementType.DETECTION_EXCLUSION,
            query="query_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = gcc_findings_refinement.FindingsRefinement.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.update_findings_refinement(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, gcc_findings_refinement.FindingsRefinement)
    assert response.name == "name_value"
    assert response.display_name == "display_name_value"
    assert (
        response.type_
        == gcc_findings_refinement.FindingsRefinementType.DETECTION_EXCLUSION
    )
    assert response.query == "query_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_update_findings_refinement_rest_interceptors(null_interceptor):
    transport = transports.FindingsRefinementServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.FindingsRefinementServiceRestInterceptor(),
    )
    client = FindingsRefinementServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.FindingsRefinementServiceRestInterceptor,
            "post_update_findings_refinement",
        ) as post,
        mock.patch.object(
            transports.FindingsRefinementServiceRestInterceptor,
            "post_update_findings_refinement_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.FindingsRefinementServiceRestInterceptor,
            "pre_update_findings_refinement",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = gcc_findings_refinement.UpdateFindingsRefinementRequest.pb(
            gcc_findings_refinement.UpdateFindingsRefinementRequest()
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
        return_value = gcc_findings_refinement.FindingsRefinement.to_json(
            gcc_findings_refinement.FindingsRefinement()
        )
        req.return_value.content = return_value

        request = gcc_findings_refinement.UpdateFindingsRefinementRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = gcc_findings_refinement.FindingsRefinement()
        post_with_metadata.return_value = (
            gcc_findings_refinement.FindingsRefinement(),
            metadata,
        )

        client.update_findings_refinement(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_get_findings_refinement_deployment_rest_bad_request(
    request_type=findings_refinement.GetFindingsRefinementDeploymentRequest,
):
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/instances/sample3/findingsRefinements/sample4/deployment"
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
        client.get_findings_refinement_deployment(request)


@pytest.mark.parametrize(
    "request_type",
    [
        findings_refinement.GetFindingsRefinementDeploymentRequest,
        dict,
    ],
)
def test_get_findings_refinement_deployment_rest_call_success(request_type):
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/instances/sample3/findingsRefinements/sample4/deployment"
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = findings_refinement.FindingsRefinementDeployment(
            name="name_value",
            enabled=True,
            archived=True,
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = findings_refinement.FindingsRefinementDeployment.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.get_findings_refinement_deployment(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, findings_refinement.FindingsRefinementDeployment)
    assert response.name == "name_value"
    assert response.enabled is True
    assert response.archived is True


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_get_findings_refinement_deployment_rest_interceptors(null_interceptor):
    transport = transports.FindingsRefinementServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.FindingsRefinementServiceRestInterceptor(),
    )
    client = FindingsRefinementServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.FindingsRefinementServiceRestInterceptor,
            "post_get_findings_refinement_deployment",
        ) as post,
        mock.patch.object(
            transports.FindingsRefinementServiceRestInterceptor,
            "post_get_findings_refinement_deployment_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.FindingsRefinementServiceRestInterceptor,
            "pre_get_findings_refinement_deployment",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = findings_refinement.GetFindingsRefinementDeploymentRequest.pb(
            findings_refinement.GetFindingsRefinementDeploymentRequest()
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
        return_value = findings_refinement.FindingsRefinementDeployment.to_json(
            findings_refinement.FindingsRefinementDeployment()
        )
        req.return_value.content = return_value

        request = findings_refinement.GetFindingsRefinementDeploymentRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = findings_refinement.FindingsRefinementDeployment()
        post_with_metadata.return_value = (
            findings_refinement.FindingsRefinementDeployment(),
            metadata,
        )

        client.get_findings_refinement_deployment(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_update_findings_refinement_deployment_rest_bad_request(
    request_type=findings_refinement.UpdateFindingsRefinementDeploymentRequest,
):
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {
        "findings_refinement_deployment": {
            "name": "projects/sample1/locations/sample2/instances/sample3/findingsRefinements/sample4/deployment"
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
        client.update_findings_refinement_deployment(request)


@pytest.mark.parametrize(
    "request_type",
    [
        findings_refinement.UpdateFindingsRefinementDeploymentRequest,
        dict,
    ],
)
def test_update_findings_refinement_deployment_rest_call_success(request_type):
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {
        "findings_refinement_deployment": {
            "name": "projects/sample1/locations/sample2/instances/sample3/findingsRefinements/sample4/deployment"
        }
    }
    request_init["findings_refinement_deployment"] = {
        "detection_exclusion_application": {
            "curated_rule_sets": [
                "curated_rule_sets_value1",
                "curated_rule_sets_value2",
            ],
            "curated_rules": ["curated_rules_value1", "curated_rules_value2"],
            "rules": ["rules_value1", "rules_value2"],
            "deleted_curated_rule_sets": [
                "deleted_curated_rule_sets_value1",
                "deleted_curated_rule_sets_value2",
            ],
        },
        "name": "projects/sample1/locations/sample2/instances/sample3/findingsRefinements/sample4/deployment",
        "enabled": True,
        "archived": True,
        "update_time": {"seconds": 751, "nanos": 543},
    }
    # The version of a generated dependency at test runtime may differ from the version used during generation.
    # Delete any fields which are not present in the current runtime dependency
    # See https://github.com/googleapis/gapic-generator-python/issues/1748

    # Determine if the message type is proto-plus or protobuf
    test_field = (
        findings_refinement.UpdateFindingsRefinementDeploymentRequest.meta.fields[
            "findings_refinement_deployment"
        ]
    )

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
        "findings_refinement_deployment"
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
                    0, len(request_init["findings_refinement_deployment"][field])
                ):
                    del request_init["findings_refinement_deployment"][field][i][
                        subfield
                    ]
            else:
                del request_init["findings_refinement_deployment"][field][subfield]
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = findings_refinement.FindingsRefinementDeployment(
            name="name_value",
            enabled=True,
            archived=True,
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = findings_refinement.FindingsRefinementDeployment.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.update_findings_refinement_deployment(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, findings_refinement.FindingsRefinementDeployment)
    assert response.name == "name_value"
    assert response.enabled is True
    assert response.archived is True


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_update_findings_refinement_deployment_rest_interceptors(null_interceptor):
    transport = transports.FindingsRefinementServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.FindingsRefinementServiceRestInterceptor(),
    )
    client = FindingsRefinementServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.FindingsRefinementServiceRestInterceptor,
            "post_update_findings_refinement_deployment",
        ) as post,
        mock.patch.object(
            transports.FindingsRefinementServiceRestInterceptor,
            "post_update_findings_refinement_deployment_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.FindingsRefinementServiceRestInterceptor,
            "pre_update_findings_refinement_deployment",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = findings_refinement.UpdateFindingsRefinementDeploymentRequest.pb(
            findings_refinement.UpdateFindingsRefinementDeploymentRequest()
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
        return_value = findings_refinement.FindingsRefinementDeployment.to_json(
            findings_refinement.FindingsRefinementDeployment()
        )
        req.return_value.content = return_value

        request = findings_refinement.UpdateFindingsRefinementDeploymentRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = findings_refinement.FindingsRefinementDeployment()
        post_with_metadata.return_value = (
            findings_refinement.FindingsRefinementDeployment(),
            metadata,
        )

        client.update_findings_refinement_deployment(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_list_all_findings_refinement_deployments_rest_bad_request(
    request_type=findings_refinement.ListAllFindingsRefinementDeploymentsRequest,
):
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"instance": "projects/sample1/locations/sample2/instances/sample3"}
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
        client.list_all_findings_refinement_deployments(request)


@pytest.mark.parametrize(
    "request_type",
    [
        findings_refinement.ListAllFindingsRefinementDeploymentsRequest,
        dict,
    ],
)
def test_list_all_findings_refinement_deployments_rest_call_success(request_type):
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"instance": "projects/sample1/locations/sample2/instances/sample3"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = findings_refinement.ListAllFindingsRefinementDeploymentsResponse(
            next_page_token="next_page_token_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = (
            findings_refinement.ListAllFindingsRefinementDeploymentsResponse.pb(
                return_value
            )
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.list_all_findings_refinement_deployments(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListAllFindingsRefinementDeploymentsPager)
    assert response.next_page_token == "next_page_token_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_list_all_findings_refinement_deployments_rest_interceptors(null_interceptor):
    transport = transports.FindingsRefinementServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.FindingsRefinementServiceRestInterceptor(),
    )
    client = FindingsRefinementServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.FindingsRefinementServiceRestInterceptor,
            "post_list_all_findings_refinement_deployments",
        ) as post,
        mock.patch.object(
            transports.FindingsRefinementServiceRestInterceptor,
            "post_list_all_findings_refinement_deployments_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.FindingsRefinementServiceRestInterceptor,
            "pre_list_all_findings_refinement_deployments",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = findings_refinement.ListAllFindingsRefinementDeploymentsRequest.pb(
            findings_refinement.ListAllFindingsRefinementDeploymentsRequest()
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
            findings_refinement.ListAllFindingsRefinementDeploymentsResponse.to_json(
                findings_refinement.ListAllFindingsRefinementDeploymentsResponse()
            )
        )
        req.return_value.content = return_value

        request = findings_refinement.ListAllFindingsRefinementDeploymentsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = (
            findings_refinement.ListAllFindingsRefinementDeploymentsResponse()
        )
        post_with_metadata.return_value = (
            findings_refinement.ListAllFindingsRefinementDeploymentsResponse(),
            metadata,
        )

        client.list_all_findings_refinement_deployments(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_compute_findings_refinement_activity_rest_bad_request(
    request_type=findings_refinement.ComputeFindingsRefinementActivityRequest,
):
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/instances/sample3/findingsRefinements/sample4"
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
        client.compute_findings_refinement_activity(request)


@pytest.mark.parametrize(
    "request_type",
    [
        findings_refinement.ComputeFindingsRefinementActivityRequest,
        dict,
    ],
)
def test_compute_findings_refinement_activity_rest_call_success(request_type):
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/instances/sample3/findingsRefinements/sample4"
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = findings_refinement.ComputeFindingsRefinementActivityResponse()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = findings_refinement.ComputeFindingsRefinementActivityResponse.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.compute_findings_refinement_activity(request)

    # Establish that the response is the type that we expect.
    assert isinstance(
        response, findings_refinement.ComputeFindingsRefinementActivityResponse
    )


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_compute_findings_refinement_activity_rest_interceptors(null_interceptor):
    transport = transports.FindingsRefinementServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.FindingsRefinementServiceRestInterceptor(),
    )
    client = FindingsRefinementServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.FindingsRefinementServiceRestInterceptor,
            "post_compute_findings_refinement_activity",
        ) as post,
        mock.patch.object(
            transports.FindingsRefinementServiceRestInterceptor,
            "post_compute_findings_refinement_activity_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.FindingsRefinementServiceRestInterceptor,
            "pre_compute_findings_refinement_activity",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = findings_refinement.ComputeFindingsRefinementActivityRequest.pb(
            findings_refinement.ComputeFindingsRefinementActivityRequest()
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
            findings_refinement.ComputeFindingsRefinementActivityResponse.to_json(
                findings_refinement.ComputeFindingsRefinementActivityResponse()
            )
        )
        req.return_value.content = return_value

        request = findings_refinement.ComputeFindingsRefinementActivityRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = (
            findings_refinement.ComputeFindingsRefinementActivityResponse()
        )
        post_with_metadata.return_value = (
            findings_refinement.ComputeFindingsRefinementActivityResponse(),
            metadata,
        )

        client.compute_findings_refinement_activity(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_compute_all_findings_refinement_activities_rest_bad_request(
    request_type=findings_refinement.ComputeAllFindingsRefinementActivitiesRequest,
):
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"instance": "projects/sample1/locations/sample2/instances/sample3"}
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
        client.compute_all_findings_refinement_activities(request)


@pytest.mark.parametrize(
    "request_type",
    [
        findings_refinement.ComputeAllFindingsRefinementActivitiesRequest,
        dict,
    ],
)
def test_compute_all_findings_refinement_activities_rest_call_success(request_type):
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"instance": "projects/sample1/locations/sample2/instances/sample3"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = (
            findings_refinement.ComputeAllFindingsRefinementActivitiesResponse()
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = (
            findings_refinement.ComputeAllFindingsRefinementActivitiesResponse.pb(
                return_value
            )
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.compute_all_findings_refinement_activities(request)

    # Establish that the response is the type that we expect.
    assert isinstance(
        response, findings_refinement.ComputeAllFindingsRefinementActivitiesResponse
    )


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_compute_all_findings_refinement_activities_rest_interceptors(null_interceptor):
    transport = transports.FindingsRefinementServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.FindingsRefinementServiceRestInterceptor(),
    )
    client = FindingsRefinementServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.FindingsRefinementServiceRestInterceptor,
            "post_compute_all_findings_refinement_activities",
        ) as post,
        mock.patch.object(
            transports.FindingsRefinementServiceRestInterceptor,
            "post_compute_all_findings_refinement_activities_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.FindingsRefinementServiceRestInterceptor,
            "pre_compute_all_findings_refinement_activities",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = (
            findings_refinement.ComputeAllFindingsRefinementActivitiesRequest.pb(
                findings_refinement.ComputeAllFindingsRefinementActivitiesRequest()
            )
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
            findings_refinement.ComputeAllFindingsRefinementActivitiesResponse.to_json(
                findings_refinement.ComputeAllFindingsRefinementActivitiesResponse()
            )
        )
        req.return_value.content = return_value

        request = findings_refinement.ComputeAllFindingsRefinementActivitiesRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = (
            findings_refinement.ComputeAllFindingsRefinementActivitiesResponse()
        )
        post_with_metadata.return_value = (
            findings_refinement.ComputeAllFindingsRefinementActivitiesResponse(),
            metadata,
        )

        client.compute_all_findings_refinement_activities(
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
    client = FindingsRefinementServiceClient(
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
    client = FindingsRefinementServiceClient(
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
    client = FindingsRefinementServiceClient(
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
    client = FindingsRefinementServiceClient(
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
    client = FindingsRefinementServiceClient(
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
    client = FindingsRefinementServiceClient(
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
    client = FindingsRefinementServiceClient(
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
    client = FindingsRefinementServiceClient(
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
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    assert client is not None


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_findings_refinement_empty_call_rest():
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.get_findings_refinement), "__call__"
    ) as call:
        client.get_findings_refinement(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = findings_refinement.GetFindingsRefinementRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_findings_refinements_empty_call_rest():
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_findings_refinements), "__call__"
    ) as call:
        client.list_findings_refinements(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = findings_refinement.ListFindingsRefinementsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_create_findings_refinement_empty_call_rest():
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.create_findings_refinement), "__call__"
    ) as call:
        client.create_findings_refinement(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gcc_findings_refinement.CreateFindingsRefinementRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_update_findings_refinement_empty_call_rest():
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.update_findings_refinement), "__call__"
    ) as call:
        client.update_findings_refinement(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gcc_findings_refinement.UpdateFindingsRefinementRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_findings_refinement_deployment_empty_call_rest():
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.get_findings_refinement_deployment), "__call__"
    ) as call:
        client.get_findings_refinement_deployment(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = findings_refinement.GetFindingsRefinementDeploymentRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_update_findings_refinement_deployment_empty_call_rest():
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.update_findings_refinement_deployment), "__call__"
    ) as call:
        client.update_findings_refinement_deployment(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = findings_refinement.UpdateFindingsRefinementDeploymentRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_all_findings_refinement_deployments_empty_call_rest():
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_all_findings_refinement_deployments), "__call__"
    ) as call:
        client.list_all_findings_refinement_deployments(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = findings_refinement.ListAllFindingsRefinementDeploymentsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_compute_findings_refinement_activity_empty_call_rest():
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.compute_findings_refinement_activity), "__call__"
    ) as call:
        client.compute_findings_refinement_activity(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = findings_refinement.ComputeFindingsRefinementActivityRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_compute_all_findings_refinement_activities_empty_call_rest():
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.compute_all_findings_refinement_activities), "__call__"
    ) as call:
        client.compute_all_findings_refinement_activities(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = (
            findings_refinement.ComputeAllFindingsRefinementActivitiesRequest()
        )
        assert args[0] == request_msg


def test_transport_grpc_default():
    # A client should use the gRPC transport by default.
    client = FindingsRefinementServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    assert isinstance(
        client.transport,
        transports.FindingsRefinementServiceGrpcTransport,
    )


def test_findings_refinement_service_base_transport_error():
    # Passing both a credentials object and credentials_file should raise an error
    with pytest.raises(core_exceptions.DuplicateCredentialArgs):
        transport = transports.FindingsRefinementServiceTransport(
            credentials=ga_credentials.AnonymousCredentials(),
            credentials_file="credentials.json",
        )


def test_findings_refinement_service_base_transport():
    # Instantiate the base transport.
    with mock.patch(
        "google.cloud.chronicle_v1.services.findings_refinement_service.transports.FindingsRefinementServiceTransport.__init__"
    ) as Transport:
        Transport.return_value = None
        transport = transports.FindingsRefinementServiceTransport(
            credentials=ga_credentials.AnonymousCredentials(),
        )

    # Every method on the transport should just blindly
    # raise NotImplementedError.
    methods = (
        "get_findings_refinement",
        "list_findings_refinements",
        "create_findings_refinement",
        "update_findings_refinement",
        "get_findings_refinement_deployment",
        "update_findings_refinement_deployment",
        "list_all_findings_refinement_deployments",
        "compute_findings_refinement_activity",
        "compute_all_findings_refinement_activities",
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


def test_findings_refinement_service_base_transport_with_credentials_file():
    # Instantiate the base transport with a credentials file
    with (
        mock.patch.object(
            google.auth, "load_credentials_from_file", autospec=True
        ) as load_creds,
        mock.patch(
            "google.cloud.chronicle_v1.services.findings_refinement_service.transports.FindingsRefinementServiceTransport._prep_wrapped_messages"
        ) as Transport,
    ):
        Transport.return_value = None
        load_creds.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.FindingsRefinementServiceTransport(
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


def test_findings_refinement_service_base_transport_with_adc():
    # Test the default credentials are used if credentials and credentials_file are None.
    with (
        mock.patch.object(google.auth, "default", autospec=True) as adc,
        mock.patch(
            "google.cloud.chronicle_v1.services.findings_refinement_service.transports.FindingsRefinementServiceTransport._prep_wrapped_messages"
        ) as Transport,
    ):
        Transport.return_value = None
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.FindingsRefinementServiceTransport()
        adc.assert_called_once()


def test_findings_refinement_service_auth_adc():
    # If no credentials are provided, we should use ADC credentials.
    with mock.patch.object(google.auth, "default", autospec=True) as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        FindingsRefinementServiceClient()
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
        transports.FindingsRefinementServiceGrpcTransport,
        transports.FindingsRefinementServiceGrpcAsyncIOTransport,
    ],
)
def test_findings_refinement_service_transport_auth_adc(transport_class):
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
        transports.FindingsRefinementServiceGrpcTransport,
        transports.FindingsRefinementServiceGrpcAsyncIOTransport,
        transports.FindingsRefinementServiceRestTransport,
    ],
)
def test_findings_refinement_service_transport_auth_gdch_credentials(transport_class):
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
        (transports.FindingsRefinementServiceGrpcTransport, grpc_helpers),
        (transports.FindingsRefinementServiceGrpcAsyncIOTransport, grpc_helpers_async),
    ],
)
def test_findings_refinement_service_transport_create_channel(
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
    [
        transports.FindingsRefinementServiceGrpcTransport,
        transports.FindingsRefinementServiceGrpcAsyncIOTransport,
    ],
)
def test_findings_refinement_service_grpc_transport_client_cert_source_for_mtls(
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


def test_findings_refinement_service_http_transport_client_cert_source_for_mtls():
    cred = ga_credentials.AnonymousCredentials()
    with mock.patch(
        "google.auth.transport.requests.AuthorizedSession.configure_mtls_channel"
    ) as mock_configure_mtls_channel:
        transports.FindingsRefinementServiceRestTransport(
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
def test_findings_refinement_service_host_no_port(transport_name):
    client = FindingsRefinementServiceClient(
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
def test_findings_refinement_service_host_with_port(transport_name):
    client = FindingsRefinementServiceClient(
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
def test_findings_refinement_service_client_transport_session_collision(transport_name):
    creds1 = ga_credentials.AnonymousCredentials()
    creds2 = ga_credentials.AnonymousCredentials()
    client1 = FindingsRefinementServiceClient(
        credentials=creds1,
        transport=transport_name,
    )
    client2 = FindingsRefinementServiceClient(
        credentials=creds2,
        transport=transport_name,
    )
    session1 = client1.transport.get_findings_refinement._session
    session2 = client2.transport.get_findings_refinement._session
    assert session1 != session2
    session1 = client1.transport.list_findings_refinements._session
    session2 = client2.transport.list_findings_refinements._session
    assert session1 != session2
    session1 = client1.transport.create_findings_refinement._session
    session2 = client2.transport.create_findings_refinement._session
    assert session1 != session2
    session1 = client1.transport.update_findings_refinement._session
    session2 = client2.transport.update_findings_refinement._session
    assert session1 != session2
    session1 = client1.transport.get_findings_refinement_deployment._session
    session2 = client2.transport.get_findings_refinement_deployment._session
    assert session1 != session2
    session1 = client1.transport.update_findings_refinement_deployment._session
    session2 = client2.transport.update_findings_refinement_deployment._session
    assert session1 != session2
    session1 = client1.transport.list_all_findings_refinement_deployments._session
    session2 = client2.transport.list_all_findings_refinement_deployments._session
    assert session1 != session2
    session1 = client1.transport.compute_findings_refinement_activity._session
    session2 = client2.transport.compute_findings_refinement_activity._session
    assert session1 != session2
    session1 = client1.transport.compute_all_findings_refinement_activities._session
    session2 = client2.transport.compute_all_findings_refinement_activities._session
    assert session1 != session2


def test_findings_refinement_service_grpc_transport_channel():
    channel = grpc.secure_channel("http://localhost/", grpc.local_channel_credentials())

    # Check that channel is used if provided.
    transport = transports.FindingsRefinementServiceGrpcTransport(
        host="squid.clam.whelk",
        channel=channel,
    )
    assert transport.grpc_channel == channel
    assert transport._host == "squid.clam.whelk:443"
    assert transport._ssl_channel_credentials == None


def test_findings_refinement_service_grpc_asyncio_transport_channel():
    channel = aio.secure_channel("http://localhost/", grpc.local_channel_credentials())

    # Check that channel is used if provided.
    transport = transports.FindingsRefinementServiceGrpcAsyncIOTransport(
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
        transports.FindingsRefinementServiceGrpcTransport,
        transports.FindingsRefinementServiceGrpcAsyncIOTransport,
    ],
)
def test_findings_refinement_service_transport_channel_mtls_with_client_cert_source(
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
        transports.FindingsRefinementServiceGrpcTransport,
        transports.FindingsRefinementServiceGrpcAsyncIOTransport,
    ],
)
def test_findings_refinement_service_transport_channel_mtls_with_adc(transport_class):
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


def test_curated_rule_path():
    project = "squid"
    location = "clam"
    instance = "whelk"
    curatedRule = "octopus"
    expected = "projects/{project}/locations/{location}/instances/{instance}/curatedRules/{curatedRule}".format(
        project=project,
        location=location,
        instance=instance,
        curatedRule=curatedRule,
    )
    actual = FindingsRefinementServiceClient.curated_rule_path(
        project, location, instance, curatedRule
    )
    assert expected == actual


def test_parse_curated_rule_path():
    expected = {
        "project": "oyster",
        "location": "nudibranch",
        "instance": "cuttlefish",
        "curatedRule": "mussel",
    }
    path = FindingsRefinementServiceClient.curated_rule_path(**expected)

    # Check that the path construction is reversible.
    actual = FindingsRefinementServiceClient.parse_curated_rule_path(path)
    assert expected == actual


def test_curated_rule_set_path():
    project = "winkle"
    location = "nautilus"
    instance = "scallop"
    category = "abalone"
    rule_set = "squid"
    expected = "projects/{project}/locations/{location}/instances/{instance}/curatedRuleSetCategories/{category}/curatedRuleSets/{rule_set}".format(
        project=project,
        location=location,
        instance=instance,
        category=category,
        rule_set=rule_set,
    )
    actual = FindingsRefinementServiceClient.curated_rule_set_path(
        project, location, instance, category, rule_set
    )
    assert expected == actual


def test_parse_curated_rule_set_path():
    expected = {
        "project": "clam",
        "location": "whelk",
        "instance": "octopus",
        "category": "oyster",
        "rule_set": "nudibranch",
    }
    path = FindingsRefinementServiceClient.curated_rule_set_path(**expected)

    # Check that the path construction is reversible.
    actual = FindingsRefinementServiceClient.parse_curated_rule_set_path(path)
    assert expected == actual


def test_findings_refinement_path():
    project = "cuttlefish"
    location = "mussel"
    instance = "winkle"
    findings_refinement = "nautilus"
    expected = "projects/{project}/locations/{location}/instances/{instance}/findingsRefinements/{findings_refinement}".format(
        project=project,
        location=location,
        instance=instance,
        findings_refinement=findings_refinement,
    )
    actual = FindingsRefinementServiceClient.findings_refinement_path(
        project, location, instance, findings_refinement
    )
    assert expected == actual


def test_parse_findings_refinement_path():
    expected = {
        "project": "scallop",
        "location": "abalone",
        "instance": "squid",
        "findings_refinement": "clam",
    }
    path = FindingsRefinementServiceClient.findings_refinement_path(**expected)

    # Check that the path construction is reversible.
    actual = FindingsRefinementServiceClient.parse_findings_refinement_path(path)
    assert expected == actual


def test_findings_refinement_deployment_path():
    project = "whelk"
    location = "octopus"
    instance = "oyster"
    findings_refinement = "nudibranch"
    expected = "projects/{project}/locations/{location}/instances/{instance}/findingsRefinements/{findings_refinement}/deployment".format(
        project=project,
        location=location,
        instance=instance,
        findings_refinement=findings_refinement,
    )
    actual = FindingsRefinementServiceClient.findings_refinement_deployment_path(
        project, location, instance, findings_refinement
    )
    assert expected == actual


def test_parse_findings_refinement_deployment_path():
    expected = {
        "project": "cuttlefish",
        "location": "mussel",
        "instance": "winkle",
        "findings_refinement": "nautilus",
    }
    path = FindingsRefinementServiceClient.findings_refinement_deployment_path(
        **expected
    )

    # Check that the path construction is reversible.
    actual = FindingsRefinementServiceClient.parse_findings_refinement_deployment_path(
        path
    )
    assert expected == actual


def test_instance_path():
    project = "scallop"
    location = "abalone"
    instance = "squid"
    expected = "projects/{project}/locations/{location}/instances/{instance}".format(
        project=project,
        location=location,
        instance=instance,
    )
    actual = FindingsRefinementServiceClient.instance_path(project, location, instance)
    assert expected == actual


def test_parse_instance_path():
    expected = {
        "project": "clam",
        "location": "whelk",
        "instance": "octopus",
    }
    path = FindingsRefinementServiceClient.instance_path(**expected)

    # Check that the path construction is reversible.
    actual = FindingsRefinementServiceClient.parse_instance_path(path)
    assert expected == actual


def test_rule_path():
    project = "oyster"
    location = "nudibranch"
    instance = "cuttlefish"
    rule = "mussel"
    expected = "projects/{project}/locations/{location}/instances/{instance}/rules/{rule}".format(
        project=project,
        location=location,
        instance=instance,
        rule=rule,
    )
    actual = FindingsRefinementServiceClient.rule_path(
        project, location, instance, rule
    )
    assert expected == actual


def test_parse_rule_path():
    expected = {
        "project": "winkle",
        "location": "nautilus",
        "instance": "scallop",
        "rule": "abalone",
    }
    path = FindingsRefinementServiceClient.rule_path(**expected)

    # Check that the path construction is reversible.
    actual = FindingsRefinementServiceClient.parse_rule_path(path)
    assert expected == actual


def test_common_billing_account_path():
    billing_account = "squid"
    expected = "billingAccounts/{billing_account}".format(
        billing_account=billing_account,
    )
    actual = FindingsRefinementServiceClient.common_billing_account_path(
        billing_account
    )
    assert expected == actual


def test_parse_common_billing_account_path():
    expected = {
        "billing_account": "clam",
    }
    path = FindingsRefinementServiceClient.common_billing_account_path(**expected)

    # Check that the path construction is reversible.
    actual = FindingsRefinementServiceClient.parse_common_billing_account_path(path)
    assert expected == actual


def test_common_folder_path():
    folder = "whelk"
    expected = "folders/{folder}".format(
        folder=folder,
    )
    actual = FindingsRefinementServiceClient.common_folder_path(folder)
    assert expected == actual


def test_parse_common_folder_path():
    expected = {
        "folder": "octopus",
    }
    path = FindingsRefinementServiceClient.common_folder_path(**expected)

    # Check that the path construction is reversible.
    actual = FindingsRefinementServiceClient.parse_common_folder_path(path)
    assert expected == actual


def test_common_organization_path():
    organization = "oyster"
    expected = "organizations/{organization}".format(
        organization=organization,
    )
    actual = FindingsRefinementServiceClient.common_organization_path(organization)
    assert expected == actual


def test_parse_common_organization_path():
    expected = {
        "organization": "nudibranch",
    }
    path = FindingsRefinementServiceClient.common_organization_path(**expected)

    # Check that the path construction is reversible.
    actual = FindingsRefinementServiceClient.parse_common_organization_path(path)
    assert expected == actual


def test_common_project_path():
    project = "cuttlefish"
    expected = "projects/{project}".format(
        project=project,
    )
    actual = FindingsRefinementServiceClient.common_project_path(project)
    assert expected == actual


def test_parse_common_project_path():
    expected = {
        "project": "mussel",
    }
    path = FindingsRefinementServiceClient.common_project_path(**expected)

    # Check that the path construction is reversible.
    actual = FindingsRefinementServiceClient.parse_common_project_path(path)
    assert expected == actual


def test_common_location_path():
    project = "winkle"
    location = "nautilus"
    expected = "projects/{project}/locations/{location}".format(
        project=project,
        location=location,
    )
    actual = FindingsRefinementServiceClient.common_location_path(project, location)
    assert expected == actual


def test_parse_common_location_path():
    expected = {
        "project": "scallop",
        "location": "abalone",
    }
    path = FindingsRefinementServiceClient.common_location_path(**expected)

    # Check that the path construction is reversible.
    actual = FindingsRefinementServiceClient.parse_common_location_path(path)
    assert expected == actual


def test_client_with_default_client_info():
    client_info = gapic_v1.client_info.ClientInfo()

    with mock.patch.object(
        transports.FindingsRefinementServiceTransport, "_prep_wrapped_messages"
    ) as prep:
        client = FindingsRefinementServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)

    with mock.patch.object(
        transports.FindingsRefinementServiceTransport, "_prep_wrapped_messages"
    ) as prep:
        transport_class = FindingsRefinementServiceClient.get_transport_class()
        transport = transport_class(
            credentials=ga_credentials.AnonymousCredentials(),
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)


def test_delete_operation(transport: str = "grpc"):
    client = FindingsRefinementServiceClient(
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
    client = FindingsRefinementServiceAsyncClient(
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
    client = FindingsRefinementServiceClient(
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
    client = FindingsRefinementServiceAsyncClient(
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
    client = FindingsRefinementServiceClient(
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
    client = FindingsRefinementServiceAsyncClient(
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
    client = FindingsRefinementServiceClient(
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
    client = FindingsRefinementServiceAsyncClient(
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
    client = FindingsRefinementServiceClient(
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
    client = FindingsRefinementServiceAsyncClient(
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
    client = FindingsRefinementServiceClient(
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
    client = FindingsRefinementServiceAsyncClient(
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
    client = FindingsRefinementServiceClient(
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
    client = FindingsRefinementServiceAsyncClient(
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
    client = FindingsRefinementServiceClient(
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
    client = FindingsRefinementServiceAsyncClient(
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
    client = FindingsRefinementServiceClient(
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
    client = FindingsRefinementServiceAsyncClient(
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
    client = FindingsRefinementServiceClient(
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
    client = FindingsRefinementServiceAsyncClient(
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
    client = FindingsRefinementServiceClient(
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
    client = FindingsRefinementServiceAsyncClient(
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
    client = FindingsRefinementServiceClient(
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
    client = FindingsRefinementServiceAsyncClient(
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
    client = FindingsRefinementServiceClient(
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
    client = FindingsRefinementServiceAsyncClient(
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
    client = FindingsRefinementServiceClient(
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
    client = FindingsRefinementServiceAsyncClient(
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
    client = FindingsRefinementServiceClient(
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
    client = FindingsRefinementServiceAsyncClient(
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
    client = FindingsRefinementServiceClient(
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
    client = FindingsRefinementServiceAsyncClient(
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
    client = FindingsRefinementServiceClient(
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
    client = FindingsRefinementServiceAsyncClient(
        credentials=async_anonymous_credentials(), transport="grpc_asyncio"
    )
    with mock.patch.object(
        type(getattr(client.transport, "_grpc_channel")), "close"
    ) as close:
        async with client:
            close.assert_not_called()
        close.assert_called_once()


def test_transport_close_rest():
    client = FindingsRefinementServiceClient(
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
        client = FindingsRefinementServiceClient(
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
            FindingsRefinementServiceClient,
            transports.FindingsRefinementServiceGrpcTransport,
        ),
        (
            FindingsRefinementServiceAsyncClient,
            transports.FindingsRefinementServiceGrpcAsyncIOTransport,
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
