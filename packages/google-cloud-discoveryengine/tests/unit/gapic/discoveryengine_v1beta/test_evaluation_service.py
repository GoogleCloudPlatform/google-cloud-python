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
import google.protobuf.any_pb2 as any_pb2  # type: ignore
import google.protobuf.struct_pb2 as struct_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.rpc.status_pb2 as status_pb2  # type: ignore
import google.type.latlng_pb2 as latlng_pb2  # type: ignore
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

from google.cloud.discoveryengine_v1beta.services.evaluation_service import (
    EvaluationServiceAsyncClient,
    EvaluationServiceClient,
    pagers,
    transports,
)
from google.cloud.discoveryengine_v1beta.types import (
    common,
    evaluation,
    evaluation_service,
    search_service,
)
from google.cloud.discoveryengine_v1beta.types import evaluation as gcd_evaluation

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

    assert EvaluationServiceClient._get_client_cert_source(None, False) is None
    assert (
        EvaluationServiceClient._get_client_cert_source(
            mock_provided_cert_source, False
        )
        is None
    )
    assert (
        EvaluationServiceClient._get_client_cert_source(mock_provided_cert_source, True)
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
                EvaluationServiceClient._get_client_cert_source(None, True)
                is mock_default_cert_source
            )
            assert (
                EvaluationServiceClient._get_client_cert_source(
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
    client = EvaluationServiceClient(credentials=cred)
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
    client = EvaluationServiceClient(credentials=cred)
    client._transport._credentials = cred

    error = core_exceptions.GoogleAPICallError("message", details=[])
    error.code = error_code

    client._add_cred_info_for_auth_errors(error)
    assert error.details == []


@pytest.mark.parametrize(
    "client_class,transport_name",
    [
        (EvaluationServiceClient, "grpc"),
        (EvaluationServiceAsyncClient, "grpc_asyncio"),
        (EvaluationServiceClient, "rest"),
    ],
)
def test_evaluation_service_client_from_service_account_info(
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
            "discoveryengine.googleapis.com:443"
            if transport_name in ["grpc", "grpc_asyncio"]
            else "https://discoveryengine.googleapis.com"
        )


@pytest.mark.parametrize(
    "transport_class,transport_name",
    [
        (transports.EvaluationServiceGrpcTransport, "grpc"),
        (transports.EvaluationServiceGrpcAsyncIOTransport, "grpc_asyncio"),
        (transports.EvaluationServiceRestTransport, "rest"),
    ],
)
def test_evaluation_service_client_service_account_always_use_jwt(
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
        (EvaluationServiceClient, "grpc"),
        (EvaluationServiceAsyncClient, "grpc_asyncio"),
        (EvaluationServiceClient, "rest"),
    ],
)
def test_evaluation_service_client_from_service_account_file(
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
            "discoveryengine.googleapis.com:443"
            if transport_name in ["grpc", "grpc_asyncio"]
            else "https://discoveryengine.googleapis.com"
        )


def test_evaluation_service_client_get_transport_class():
    transport = EvaluationServiceClient.get_transport_class()
    available_transports = [
        transports.EvaluationServiceGrpcTransport,
        transports.EvaluationServiceRestTransport,
    ]
    assert transport in available_transports

    transport = EvaluationServiceClient.get_transport_class("grpc")
    assert transport == transports.EvaluationServiceGrpcTransport


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name",
    [
        (EvaluationServiceClient, transports.EvaluationServiceGrpcTransport, "grpc"),
        (
            EvaluationServiceAsyncClient,
            transports.EvaluationServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
        ),
        (EvaluationServiceClient, transports.EvaluationServiceRestTransport, "rest"),
    ],
)
@mock.patch.object(
    EvaluationServiceClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(EvaluationServiceClient),
)
@mock.patch.object(
    EvaluationServiceAsyncClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(EvaluationServiceAsyncClient),
)
def test_evaluation_service_client_client_options(
    client_class, transport_class, transport_name
):
    # Check that if channel is provided we won't create a new one.
    with mock.patch.object(EvaluationServiceClient, "get_transport_class") as gtc:
        transport = transport_class(credentials=ga_credentials.AnonymousCredentials())
        client = client_class(transport=transport)
        gtc.assert_not_called()

    # Check that if channel is provided via str we will create a new one.
    with mock.patch.object(EvaluationServiceClient, "get_transport_class") as gtc:
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
            EvaluationServiceClient,
            transports.EvaluationServiceGrpcTransport,
            "grpc",
            "true",
        ),
        (
            EvaluationServiceAsyncClient,
            transports.EvaluationServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
            "true",
        ),
        (
            EvaluationServiceClient,
            transports.EvaluationServiceGrpcTransport,
            "grpc",
            "false",
        ),
        (
            EvaluationServiceAsyncClient,
            transports.EvaluationServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
            "false",
        ),
        (
            EvaluationServiceClient,
            transports.EvaluationServiceRestTransport,
            "rest",
            "true",
        ),
        (
            EvaluationServiceClient,
            transports.EvaluationServiceRestTransport,
            "rest",
            "false",
        ),
    ],
)
@mock.patch.object(
    EvaluationServiceClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(EvaluationServiceClient),
)
@mock.patch.object(
    EvaluationServiceAsyncClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(EvaluationServiceAsyncClient),
)
@mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "auto"})
def test_evaluation_service_client_mtls_env_auto(
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
    "client_class", [EvaluationServiceClient, EvaluationServiceAsyncClient]
)
@mock.patch.object(
    EvaluationServiceClient,
    "DEFAULT_ENDPOINT",
    modify_default_endpoint(EvaluationServiceClient),
)
@mock.patch.object(
    EvaluationServiceAsyncClient,
    "DEFAULT_ENDPOINT",
    modify_default_endpoint(EvaluationServiceAsyncClient),
)
def test_evaluation_service_client_get_mtls_endpoint_and_cert_source(client_class):
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
    "client_class", [EvaluationServiceClient, EvaluationServiceAsyncClient]
)
@mock.patch.object(
    EvaluationServiceClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(EvaluationServiceClient),
)
@mock.patch.object(
    EvaluationServiceAsyncClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(EvaluationServiceAsyncClient),
)
def test_evaluation_service_client_client_api_endpoint(client_class):
    mock_client_cert_source = client_cert_source_callback
    api_override = "foo.com"
    default_universe = EvaluationServiceClient._DEFAULT_UNIVERSE
    default_endpoint = EvaluationServiceClient._DEFAULT_ENDPOINT_TEMPLATE.format(
        UNIVERSE_DOMAIN=default_universe
    )
    mock_universe = "bar.com"
    mock_endpoint = EvaluationServiceClient._DEFAULT_ENDPOINT_TEMPLATE.format(
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
        (EvaluationServiceClient, transports.EvaluationServiceGrpcTransport, "grpc"),
        (
            EvaluationServiceAsyncClient,
            transports.EvaluationServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
        ),
        (EvaluationServiceClient, transports.EvaluationServiceRestTransport, "rest"),
    ],
)
def test_evaluation_service_client_client_options_scopes(
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
            EvaluationServiceClient,
            transports.EvaluationServiceGrpcTransport,
            "grpc",
            grpc_helpers,
        ),
        (
            EvaluationServiceAsyncClient,
            transports.EvaluationServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
            grpc_helpers_async,
        ),
        (
            EvaluationServiceClient,
            transports.EvaluationServiceRestTransport,
            "rest",
            None,
        ),
    ],
)
def test_evaluation_service_client_client_options_credentials_file(
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


def test_evaluation_service_client_client_options_from_dict():
    with mock.patch(
        "google.cloud.discoveryengine_v1beta.services.evaluation_service.transports.EvaluationServiceGrpcTransport.__init__"
    ) as grpc_transport:
        grpc_transport.return_value = None
        client = EvaluationServiceClient(
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
            EvaluationServiceClient,
            transports.EvaluationServiceGrpcTransport,
            "grpc",
            grpc_helpers,
        ),
        (
            EvaluationServiceAsyncClient,
            transports.EvaluationServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
            grpc_helpers_async,
        ),
    ],
)
def test_evaluation_service_client_create_channel_credentials_file(
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
            "discoveryengine.googleapis.com:443",
            credentials=file_creds,
            credentials_file=None,
            quota_project_id=None,
            default_scopes=(
                "https://www.googleapis.com/auth/cloud-platform",
                "https://www.googleapis.com/auth/discoveryengine.assist.readwrite",
                "https://www.googleapis.com/auth/discoveryengine.readwrite",
                "https://www.googleapis.com/auth/discoveryengine.serving.readwrite",
            ),
            scopes=None,
            default_host="discoveryengine.googleapis.com",
            ssl_credentials=None,
            options=[
                ("grpc.max_send_message_length", -1),
                ("grpc.max_receive_message_length", -1),
            ],
        )


@pytest.mark.parametrize(
    "request_type",
    [
        evaluation_service.GetEvaluationRequest(),
        {},
    ],
)
def test_get_evaluation(request_type, transport: str = "grpc"):
    client = EvaluationServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_evaluation), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = evaluation.Evaluation(
            name="name_value",
            state=evaluation.Evaluation.State.PENDING,
        )
        response = client.get_evaluation(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = evaluation_service.GetEvaluationRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, evaluation.Evaluation)
    assert response.name == "name_value"
    assert response.state == evaluation.Evaluation.State.PENDING


def test_get_evaluation_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = EvaluationServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = evaluation_service.GetEvaluationRequest(
        name="name_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_evaluation), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.get_evaluation(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = evaluation_service.GetEvaluationRequest(
            name="name_value",
        )
        assert args[0] == request_msg


def test_get_evaluation_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = EvaluationServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.get_evaluation in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.get_evaluation] = mock_rpc
        request = {}
        client.get_evaluation(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_evaluation(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_get_evaluation_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = EvaluationServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.get_evaluation
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.get_evaluation
        ] = mock_rpc

        request = {}
        await client.get_evaluation(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.get_evaluation(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        evaluation_service.GetEvaluationRequest(),
        {},
    ],
)
async def test_get_evaluation_async(request_type, transport: str = "grpc_asyncio"):
    client = EvaluationServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_evaluation), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            evaluation.Evaluation(
                name="name_value",
                state=evaluation.Evaluation.State.PENDING,
            )
        )
        response = await client.get_evaluation(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = evaluation_service.GetEvaluationRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, evaluation.Evaluation)
    assert response.name == "name_value"
    assert response.state == evaluation.Evaluation.State.PENDING


def test_get_evaluation_field_headers():
    client = EvaluationServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = evaluation_service.GetEvaluationRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_evaluation), "__call__") as call:
        call.return_value = evaluation.Evaluation()
        client.get_evaluation(request)

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
async def test_get_evaluation_field_headers_async():
    client = EvaluationServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = evaluation_service.GetEvaluationRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_evaluation), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            evaluation.Evaluation()
        )
        await client.get_evaluation(request)

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


def test_get_evaluation_flattened():
    client = EvaluationServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_evaluation), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = evaluation.Evaluation()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.get_evaluation(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_get_evaluation_flattened_error():
    client = EvaluationServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_evaluation(
            evaluation_service.GetEvaluationRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_get_evaluation_flattened_async():
    client = EvaluationServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_evaluation), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = evaluation.Evaluation()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            evaluation.Evaluation()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.get_evaluation(
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
async def test_get_evaluation_flattened_error_async():
    client = EvaluationServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.get_evaluation(
            evaluation_service.GetEvaluationRequest(),
            name="name_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        evaluation_service.ListEvaluationsRequest(),
        {},
    ],
)
def test_list_evaluations(request_type, transport: str = "grpc"):
    client = EvaluationServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_evaluations), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = evaluation_service.ListEvaluationsResponse(
            next_page_token="next_page_token_value",
        )
        response = client.list_evaluations(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = evaluation_service.ListEvaluationsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListEvaluationsPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_evaluations_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = EvaluationServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = evaluation_service.ListEvaluationsRequest(
        parent="parent_value",
        page_token="page_token_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_evaluations), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.list_evaluations(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = evaluation_service.ListEvaluationsRequest(
            parent="parent_value",
            page_token="page_token_value",
        )
        assert args[0] == request_msg


def test_list_evaluations_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = EvaluationServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.list_evaluations in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.list_evaluations] = (
            mock_rpc
        )
        request = {}
        client.list_evaluations(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_evaluations(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_list_evaluations_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = EvaluationServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.list_evaluations
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.list_evaluations
        ] = mock_rpc

        request = {}
        await client.list_evaluations(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.list_evaluations(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        evaluation_service.ListEvaluationsRequest(),
        {},
    ],
)
async def test_list_evaluations_async(request_type, transport: str = "grpc_asyncio"):
    client = EvaluationServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_evaluations), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            evaluation_service.ListEvaluationsResponse(
                next_page_token="next_page_token_value",
            )
        )
        response = await client.list_evaluations(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = evaluation_service.ListEvaluationsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListEvaluationsAsyncPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_evaluations_field_headers():
    client = EvaluationServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = evaluation_service.ListEvaluationsRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_evaluations), "__call__") as call:
        call.return_value = evaluation_service.ListEvaluationsResponse()
        client.list_evaluations(request)

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
async def test_list_evaluations_field_headers_async():
    client = EvaluationServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = evaluation_service.ListEvaluationsRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_evaluations), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            evaluation_service.ListEvaluationsResponse()
        )
        await client.list_evaluations(request)

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


def test_list_evaluations_flattened():
    client = EvaluationServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_evaluations), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = evaluation_service.ListEvaluationsResponse()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.list_evaluations(
            parent="parent_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val


def test_list_evaluations_flattened_error():
    client = EvaluationServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_evaluations(
            evaluation_service.ListEvaluationsRequest(),
            parent="parent_value",
        )


@pytest.mark.asyncio
async def test_list_evaluations_flattened_async():
    client = EvaluationServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_evaluations), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = evaluation_service.ListEvaluationsResponse()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            evaluation_service.ListEvaluationsResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.list_evaluations(
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
async def test_list_evaluations_flattened_error_async():
    client = EvaluationServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.list_evaluations(
            evaluation_service.ListEvaluationsRequest(),
            parent="parent_value",
        )


def test_list_evaluations_pager(transport_name: str = "grpc"):
    client = EvaluationServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_evaluations), "__call__") as call:
        # Set the response to a series of pages.
        call.side_effect = (
            evaluation_service.ListEvaluationsResponse(
                evaluations=[
                    evaluation.Evaluation(),
                    evaluation.Evaluation(),
                    evaluation.Evaluation(),
                ],
                next_page_token="abc",
            ),
            evaluation_service.ListEvaluationsResponse(
                evaluations=[],
                next_page_token="def",
            ),
            evaluation_service.ListEvaluationsResponse(
                evaluations=[
                    evaluation.Evaluation(),
                ],
                next_page_token="ghi",
            ),
            evaluation_service.ListEvaluationsResponse(
                evaluations=[
                    evaluation.Evaluation(),
                    evaluation.Evaluation(),
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
        pager = client.list_evaluations(request={}, retry=retry, timeout=timeout)

        assert pager._metadata == expected_metadata
        assert pager._retry == retry
        assert pager._timeout == timeout

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, evaluation.Evaluation) for i in results)


def test_list_evaluations_pages(transport_name: str = "grpc"):
    client = EvaluationServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_evaluations), "__call__") as call:
        # Set the response to a series of pages.
        call.side_effect = (
            evaluation_service.ListEvaluationsResponse(
                evaluations=[
                    evaluation.Evaluation(),
                    evaluation.Evaluation(),
                    evaluation.Evaluation(),
                ],
                next_page_token="abc",
            ),
            evaluation_service.ListEvaluationsResponse(
                evaluations=[],
                next_page_token="def",
            ),
            evaluation_service.ListEvaluationsResponse(
                evaluations=[
                    evaluation.Evaluation(),
                ],
                next_page_token="ghi",
            ),
            evaluation_service.ListEvaluationsResponse(
                evaluations=[
                    evaluation.Evaluation(),
                    evaluation.Evaluation(),
                ],
            ),
            RuntimeError,
        )
        pages = list(client.list_evaluations(request={}).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.asyncio
async def test_list_evaluations_async_pager():
    client = EvaluationServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_evaluations), "__call__", new_callable=mock.AsyncMock
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            evaluation_service.ListEvaluationsResponse(
                evaluations=[
                    evaluation.Evaluation(),
                    evaluation.Evaluation(),
                    evaluation.Evaluation(),
                ],
                next_page_token="abc",
            ),
            evaluation_service.ListEvaluationsResponse(
                evaluations=[],
                next_page_token="def",
            ),
            evaluation_service.ListEvaluationsResponse(
                evaluations=[
                    evaluation.Evaluation(),
                ],
                next_page_token="ghi",
            ),
            evaluation_service.ListEvaluationsResponse(
                evaluations=[
                    evaluation.Evaluation(),
                    evaluation.Evaluation(),
                ],
            ),
            RuntimeError,
        )
        async_pager = await client.list_evaluations(
            request={},
        )
        assert async_pager.next_page_token == "abc"
        assert str(async_pager).startswith(f"{async_pager.__class__.__name__}<")

        responses = []
        async for response in async_pager:  # pragma: no branch
            responses.append(response)

        assert len(responses) == 6
        assert all(isinstance(i, evaluation.Evaluation) for i in responses)


@pytest.mark.asyncio
async def test_list_evaluations_async_pages():
    client = EvaluationServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_evaluations), "__call__", new_callable=mock.AsyncMock
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            evaluation_service.ListEvaluationsResponse(
                evaluations=[
                    evaluation.Evaluation(),
                    evaluation.Evaluation(),
                    evaluation.Evaluation(),
                ],
                next_page_token="abc",
            ),
            evaluation_service.ListEvaluationsResponse(
                evaluations=[],
                next_page_token="def",
            ),
            evaluation_service.ListEvaluationsResponse(
                evaluations=[
                    evaluation.Evaluation(),
                ],
                next_page_token="ghi",
            ),
            evaluation_service.ListEvaluationsResponse(
                evaluations=[
                    evaluation.Evaluation(),
                    evaluation.Evaluation(),
                ],
            ),
            RuntimeError,
        )
        pages = []
        async for page_ in (await client.list_evaluations(request={})).pages:
            pages.append(page_)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.parametrize(
    "request_type",
    [
        evaluation_service.CreateEvaluationRequest(),
        {},
    ],
)
def test_create_evaluation(request_type, transport: str = "grpc"):
    client = EvaluationServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_evaluation), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/spam")
        response = client.create_evaluation(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = evaluation_service.CreateEvaluationRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_create_evaluation_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = EvaluationServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = evaluation_service.CreateEvaluationRequest(
        parent="parent_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_evaluation), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.create_evaluation(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = evaluation_service.CreateEvaluationRequest(
            parent="parent_value",
        )
        assert args[0] == request_msg


def test_create_evaluation_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = EvaluationServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.create_evaluation in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.create_evaluation] = (
            mock_rpc
        )
        request = {}
        client.create_evaluation(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods call wrapper_fn to build a cached
        # client._transport.operations_client instance on first rpc call.
        # Subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.create_evaluation(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_create_evaluation_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = EvaluationServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.create_evaluation
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.create_evaluation
        ] = mock_rpc

        request = {}
        await client.create_evaluation(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods call wrapper_fn to build a cached
        # client._transport.operations_client instance on first rpc call.
        # Subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        await client.create_evaluation(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        evaluation_service.CreateEvaluationRequest(),
        {},
    ],
)
async def test_create_evaluation_async(request_type, transport: str = "grpc_asyncio"):
    client = EvaluationServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_evaluation), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        response = await client.create_evaluation(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = evaluation_service.CreateEvaluationRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_create_evaluation_field_headers():
    client = EvaluationServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = evaluation_service.CreateEvaluationRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_evaluation), "__call__"
    ) as call:
        call.return_value = operations_pb2.Operation(name="operations/op")
        client.create_evaluation(request)

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
async def test_create_evaluation_field_headers_async():
    client = EvaluationServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = evaluation_service.CreateEvaluationRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_evaluation), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/op")
        )
        await client.create_evaluation(request)

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


def test_create_evaluation_flattened():
    client = EvaluationServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_evaluation), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.create_evaluation(
            parent="parent_value",
            evaluation=gcd_evaluation.Evaluation(name="name_value"),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val
        arg = args[0].evaluation
        mock_val = gcd_evaluation.Evaluation(name="name_value")
        assert arg == mock_val


def test_create_evaluation_flattened_error():
    client = EvaluationServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.create_evaluation(
            evaluation_service.CreateEvaluationRequest(),
            parent="parent_value",
            evaluation=gcd_evaluation.Evaluation(name="name_value"),
        )


@pytest.mark.asyncio
async def test_create_evaluation_flattened_async():
    client = EvaluationServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_evaluation), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.create_evaluation(
            parent="parent_value",
            evaluation=gcd_evaluation.Evaluation(name="name_value"),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val
        arg = args[0].evaluation
        mock_val = gcd_evaluation.Evaluation(name="name_value")
        assert arg == mock_val


@pytest.mark.asyncio
async def test_create_evaluation_flattened_error_async():
    client = EvaluationServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.create_evaluation(
            evaluation_service.CreateEvaluationRequest(),
            parent="parent_value",
            evaluation=gcd_evaluation.Evaluation(name="name_value"),
        )


@pytest.mark.parametrize(
    "request_type",
    [
        evaluation_service.ListEvaluationResultsRequest(),
        {},
    ],
)
def test_list_evaluation_results(request_type, transport: str = "grpc"):
    client = EvaluationServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_evaluation_results), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = evaluation_service.ListEvaluationResultsResponse(
            next_page_token="next_page_token_value",
        )
        response = client.list_evaluation_results(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = evaluation_service.ListEvaluationResultsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListEvaluationResultsPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_evaluation_results_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = EvaluationServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = evaluation_service.ListEvaluationResultsRequest(
        evaluation="evaluation_value",
        page_token="page_token_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_evaluation_results), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.list_evaluation_results(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = evaluation_service.ListEvaluationResultsRequest(
            evaluation="evaluation_value",
            page_token="page_token_value",
        )
        assert args[0] == request_msg


def test_list_evaluation_results_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = EvaluationServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.list_evaluation_results
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.list_evaluation_results
        ] = mock_rpc
        request = {}
        client.list_evaluation_results(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_evaluation_results(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_list_evaluation_results_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = EvaluationServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.list_evaluation_results
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.list_evaluation_results
        ] = mock_rpc

        request = {}
        await client.list_evaluation_results(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.list_evaluation_results(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        evaluation_service.ListEvaluationResultsRequest(),
        {},
    ],
)
async def test_list_evaluation_results_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = EvaluationServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_evaluation_results), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            evaluation_service.ListEvaluationResultsResponse(
                next_page_token="next_page_token_value",
            )
        )
        response = await client.list_evaluation_results(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = evaluation_service.ListEvaluationResultsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListEvaluationResultsAsyncPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_evaluation_results_field_headers():
    client = EvaluationServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = evaluation_service.ListEvaluationResultsRequest()

    request.evaluation = "evaluation_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_evaluation_results), "__call__"
    ) as call:
        call.return_value = evaluation_service.ListEvaluationResultsResponse()
        client.list_evaluation_results(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "evaluation=evaluation_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_list_evaluation_results_field_headers_async():
    client = EvaluationServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = evaluation_service.ListEvaluationResultsRequest()

    request.evaluation = "evaluation_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_evaluation_results), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            evaluation_service.ListEvaluationResultsResponse()
        )
        await client.list_evaluation_results(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "evaluation=evaluation_value",
    ) in kw["metadata"]


def test_list_evaluation_results_flattened():
    client = EvaluationServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_evaluation_results), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = evaluation_service.ListEvaluationResultsResponse()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.list_evaluation_results(
            evaluation="evaluation_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].evaluation
        mock_val = "evaluation_value"
        assert arg == mock_val


def test_list_evaluation_results_flattened_error():
    client = EvaluationServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_evaluation_results(
            evaluation_service.ListEvaluationResultsRequest(),
            evaluation="evaluation_value",
        )


@pytest.mark.asyncio
async def test_list_evaluation_results_flattened_async():
    client = EvaluationServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_evaluation_results), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = evaluation_service.ListEvaluationResultsResponse()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            evaluation_service.ListEvaluationResultsResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.list_evaluation_results(
            evaluation="evaluation_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].evaluation
        mock_val = "evaluation_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_list_evaluation_results_flattened_error_async():
    client = EvaluationServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.list_evaluation_results(
            evaluation_service.ListEvaluationResultsRequest(),
            evaluation="evaluation_value",
        )


def test_list_evaluation_results_pager(transport_name: str = "grpc"):
    client = EvaluationServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_evaluation_results), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            evaluation_service.ListEvaluationResultsResponse(
                evaluation_results=[
                    evaluation_service.ListEvaluationResultsResponse.EvaluationResult(),
                    evaluation_service.ListEvaluationResultsResponse.EvaluationResult(),
                    evaluation_service.ListEvaluationResultsResponse.EvaluationResult(),
                ],
                next_page_token="abc",
            ),
            evaluation_service.ListEvaluationResultsResponse(
                evaluation_results=[],
                next_page_token="def",
            ),
            evaluation_service.ListEvaluationResultsResponse(
                evaluation_results=[
                    evaluation_service.ListEvaluationResultsResponse.EvaluationResult(),
                ],
                next_page_token="ghi",
            ),
            evaluation_service.ListEvaluationResultsResponse(
                evaluation_results=[
                    evaluation_service.ListEvaluationResultsResponse.EvaluationResult(),
                    evaluation_service.ListEvaluationResultsResponse.EvaluationResult(),
                ],
            ),
            RuntimeError,
        )

        expected_metadata = ()
        retry = retries.Retry()
        timeout = 5
        expected_metadata = tuple(expected_metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("evaluation", ""),)),
        )
        pager = client.list_evaluation_results(request={}, retry=retry, timeout=timeout)

        assert pager._metadata == expected_metadata
        assert pager._retry == retry
        assert pager._timeout == timeout

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(
            isinstance(
                i, evaluation_service.ListEvaluationResultsResponse.EvaluationResult
            )
            for i in results
        )


def test_list_evaluation_results_pages(transport_name: str = "grpc"):
    client = EvaluationServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_evaluation_results), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            evaluation_service.ListEvaluationResultsResponse(
                evaluation_results=[
                    evaluation_service.ListEvaluationResultsResponse.EvaluationResult(),
                    evaluation_service.ListEvaluationResultsResponse.EvaluationResult(),
                    evaluation_service.ListEvaluationResultsResponse.EvaluationResult(),
                ],
                next_page_token="abc",
            ),
            evaluation_service.ListEvaluationResultsResponse(
                evaluation_results=[],
                next_page_token="def",
            ),
            evaluation_service.ListEvaluationResultsResponse(
                evaluation_results=[
                    evaluation_service.ListEvaluationResultsResponse.EvaluationResult(),
                ],
                next_page_token="ghi",
            ),
            evaluation_service.ListEvaluationResultsResponse(
                evaluation_results=[
                    evaluation_service.ListEvaluationResultsResponse.EvaluationResult(),
                    evaluation_service.ListEvaluationResultsResponse.EvaluationResult(),
                ],
            ),
            RuntimeError,
        )
        pages = list(client.list_evaluation_results(request={}).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.asyncio
async def test_list_evaluation_results_async_pager():
    client = EvaluationServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_evaluation_results),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            evaluation_service.ListEvaluationResultsResponse(
                evaluation_results=[
                    evaluation_service.ListEvaluationResultsResponse.EvaluationResult(),
                    evaluation_service.ListEvaluationResultsResponse.EvaluationResult(),
                    evaluation_service.ListEvaluationResultsResponse.EvaluationResult(),
                ],
                next_page_token="abc",
            ),
            evaluation_service.ListEvaluationResultsResponse(
                evaluation_results=[],
                next_page_token="def",
            ),
            evaluation_service.ListEvaluationResultsResponse(
                evaluation_results=[
                    evaluation_service.ListEvaluationResultsResponse.EvaluationResult(),
                ],
                next_page_token="ghi",
            ),
            evaluation_service.ListEvaluationResultsResponse(
                evaluation_results=[
                    evaluation_service.ListEvaluationResultsResponse.EvaluationResult(),
                    evaluation_service.ListEvaluationResultsResponse.EvaluationResult(),
                ],
            ),
            RuntimeError,
        )
        async_pager = await client.list_evaluation_results(
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
                i, evaluation_service.ListEvaluationResultsResponse.EvaluationResult
            )
            for i in responses
        )


@pytest.mark.asyncio
async def test_list_evaluation_results_async_pages():
    client = EvaluationServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_evaluation_results),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            evaluation_service.ListEvaluationResultsResponse(
                evaluation_results=[
                    evaluation_service.ListEvaluationResultsResponse.EvaluationResult(),
                    evaluation_service.ListEvaluationResultsResponse.EvaluationResult(),
                    evaluation_service.ListEvaluationResultsResponse.EvaluationResult(),
                ],
                next_page_token="abc",
            ),
            evaluation_service.ListEvaluationResultsResponse(
                evaluation_results=[],
                next_page_token="def",
            ),
            evaluation_service.ListEvaluationResultsResponse(
                evaluation_results=[
                    evaluation_service.ListEvaluationResultsResponse.EvaluationResult(),
                ],
                next_page_token="ghi",
            ),
            evaluation_service.ListEvaluationResultsResponse(
                evaluation_results=[
                    evaluation_service.ListEvaluationResultsResponse.EvaluationResult(),
                    evaluation_service.ListEvaluationResultsResponse.EvaluationResult(),
                ],
            ),
            RuntimeError,
        )
        pages = []
        async for page_ in (await client.list_evaluation_results(request={})).pages:
            pages.append(page_)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


def test_get_evaluation_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = EvaluationServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.get_evaluation in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.get_evaluation] = mock_rpc

        request = {}
        client.get_evaluation(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_evaluation(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_get_evaluation_rest_required_fields(
    request_type=evaluation_service.GetEvaluationRequest,
):
    transport_class = transports.EvaluationServiceRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseGetEvaluation,
        "_BaseGetEvaluation__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = EvaluationServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = evaluation.Evaluation()
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
            return_value = evaluation.Evaluation.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.get_evaluation(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_get_evaluation_rest_flattened():
    client = EvaluationServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = evaluation.Evaluation()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "name": "projects/sample1/locations/sample2/evaluations/sample3"
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
        return_value = evaluation.Evaluation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.get_evaluation(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1beta/{name=projects/*/locations/*/evaluations/*}"
            % client.transport._host,
            args[1],
        )


def test_get_evaluation_rest_flattened_error(transport: str = "rest"):
    client = EvaluationServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_evaluation(
            evaluation_service.GetEvaluationRequest(),
            name="name_value",
        )


def test_list_evaluations_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = EvaluationServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.list_evaluations in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.list_evaluations] = (
            mock_rpc
        )

        request = {}
        client.list_evaluations(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_evaluations(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_list_evaluations_rest_required_fields(
    request_type=evaluation_service.ListEvaluationsRequest,
):
    transport_class = transports.EvaluationServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseListEvaluations,
        "_BaseListEvaluations__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = EvaluationServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = evaluation_service.ListEvaluationsResponse()
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
            return_value = evaluation_service.ListEvaluationsResponse.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.list_evaluations(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_list_evaluations_rest_flattened():
    client = EvaluationServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = evaluation_service.ListEvaluationsResponse()

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
        return_value = evaluation_service.ListEvaluationsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.list_evaluations(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1beta/{parent=projects/*/locations/*}/evaluations"
            % client.transport._host,
            args[1],
        )


def test_list_evaluations_rest_flattened_error(transport: str = "rest"):
    client = EvaluationServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_evaluations(
            evaluation_service.ListEvaluationsRequest(),
            parent="parent_value",
        )


def test_list_evaluations_rest_pager(transport: str = "rest"):
    client = EvaluationServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        # with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            evaluation_service.ListEvaluationsResponse(
                evaluations=[
                    evaluation.Evaluation(),
                    evaluation.Evaluation(),
                    evaluation.Evaluation(),
                ],
                next_page_token="abc",
            ),
            evaluation_service.ListEvaluationsResponse(
                evaluations=[],
                next_page_token="def",
            ),
            evaluation_service.ListEvaluationsResponse(
                evaluations=[
                    evaluation.Evaluation(),
                ],
                next_page_token="ghi",
            ),
            evaluation_service.ListEvaluationsResponse(
                evaluations=[
                    evaluation.Evaluation(),
                    evaluation.Evaluation(),
                ],
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(
            evaluation_service.ListEvaluationsResponse.to_json(x) for x in response
        )
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode("UTF-8")
            return_val.status_code = 200
        req.side_effect = return_values

        sample_request = {"parent": "projects/sample1/locations/sample2"}

        pager = client.list_evaluations(request=sample_request)

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, evaluation.Evaluation) for i in results)

        pages = list(client.list_evaluations(request=sample_request).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


def test_create_evaluation_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = EvaluationServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.create_evaluation in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.create_evaluation] = (
            mock_rpc
        )

        request = {}
        client.create_evaluation(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods build a cached wrapper on first rpc call
        # subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.create_evaluation(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_create_evaluation_rest_required_fields(
    request_type=evaluation_service.CreateEvaluationRequest,
):
    transport_class = transports.EvaluationServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseCreateEvaluation,
        "_BaseCreateEvaluation__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = EvaluationServiceClient(
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

            response = client.create_evaluation(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_create_evaluation_rest_flattened():
    client = EvaluationServiceClient(
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
            evaluation=gcd_evaluation.Evaluation(name="name_value"),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.create_evaluation(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1beta/{parent=projects/*/locations/*}/evaluations"
            % client.transport._host,
            args[1],
        )


def test_create_evaluation_rest_flattened_error(transport: str = "rest"):
    client = EvaluationServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.create_evaluation(
            evaluation_service.CreateEvaluationRequest(),
            parent="parent_value",
            evaluation=gcd_evaluation.Evaluation(name="name_value"),
        )


def test_list_evaluation_results_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = EvaluationServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.list_evaluation_results
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.list_evaluation_results
        ] = mock_rpc

        request = {}
        client.list_evaluation_results(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_evaluation_results(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_list_evaluation_results_rest_required_fields(
    request_type=evaluation_service.ListEvaluationResultsRequest,
):
    transport_class = transports.EvaluationServiceRestTransport

    request_init = {}
    request_init["evaluation"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseListEvaluationResults,
        "_BaseListEvaluationResults__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["evaluation"] = "evaluation_value"

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(
        (
            "pageSize",
            "pageToken",
        )
    )

    # verify required fields with non-default values are left alone
    assert "evaluation" in jsonified_request
    assert jsonified_request["evaluation"] == "evaluation_value"

    client = EvaluationServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = evaluation_service.ListEvaluationResultsResponse()
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
            return_value = evaluation_service.ListEvaluationResultsResponse.pb(
                return_value
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.list_evaluation_results(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_list_evaluation_results_rest_flattened():
    client = EvaluationServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = evaluation_service.ListEvaluationResultsResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "evaluation": "projects/sample1/locations/sample2/evaluations/sample3"
        }

        # get truthy value for each flattened field
        mock_args = dict(
            evaluation="evaluation_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = evaluation_service.ListEvaluationResultsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.list_evaluation_results(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1beta/{evaluation=projects/*/locations/*/evaluations/*}:listResults"
            % client.transport._host,
            args[1],
        )


def test_list_evaluation_results_rest_flattened_error(transport: str = "rest"):
    client = EvaluationServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_evaluation_results(
            evaluation_service.ListEvaluationResultsRequest(),
            evaluation="evaluation_value",
        )


def test_list_evaluation_results_rest_pager(transport: str = "rest"):
    client = EvaluationServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        # with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            evaluation_service.ListEvaluationResultsResponse(
                evaluation_results=[
                    evaluation_service.ListEvaluationResultsResponse.EvaluationResult(),
                    evaluation_service.ListEvaluationResultsResponse.EvaluationResult(),
                    evaluation_service.ListEvaluationResultsResponse.EvaluationResult(),
                ],
                next_page_token="abc",
            ),
            evaluation_service.ListEvaluationResultsResponse(
                evaluation_results=[],
                next_page_token="def",
            ),
            evaluation_service.ListEvaluationResultsResponse(
                evaluation_results=[
                    evaluation_service.ListEvaluationResultsResponse.EvaluationResult(),
                ],
                next_page_token="ghi",
            ),
            evaluation_service.ListEvaluationResultsResponse(
                evaluation_results=[
                    evaluation_service.ListEvaluationResultsResponse.EvaluationResult(),
                    evaluation_service.ListEvaluationResultsResponse.EvaluationResult(),
                ],
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(
            evaluation_service.ListEvaluationResultsResponse.to_json(x)
            for x in response
        )
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode("UTF-8")
            return_val.status_code = 200
        req.side_effect = return_values

        sample_request = {
            "evaluation": "projects/sample1/locations/sample2/evaluations/sample3"
        }

        pager = client.list_evaluation_results(request=sample_request)

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(
            isinstance(
                i, evaluation_service.ListEvaluationResultsResponse.EvaluationResult
            )
            for i in results
        )

        pages = list(client.list_evaluation_results(request=sample_request).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


def test_credentials_transport_error():
    # It is an error to provide credentials and a transport instance.
    transport = transports.EvaluationServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = EvaluationServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport=transport,
        )

    # It is an error to provide a credentials file and a transport instance.
    transport = transports.EvaluationServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = EvaluationServiceClient(
            client_options={"credentials_file": "credentials.json"},
            transport=transport,
        )

    # It is an error to provide an api_key and a transport instance.
    transport = transports.EvaluationServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    options = client_options.ClientOptions()
    options.api_key = "api_key"
    with pytest.raises(ValueError):
        client = EvaluationServiceClient(
            client_options=options,
            transport=transport,
        )

    # It is an error to provide an api_key and a credential.
    options = client_options.ClientOptions()
    options.api_key = "api_key"
    with pytest.raises(ValueError):
        client = EvaluationServiceClient(
            client_options=options, credentials=ga_credentials.AnonymousCredentials()
        )

    # It is an error to provide scopes and a transport instance.
    transport = transports.EvaluationServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = EvaluationServiceClient(
            client_options={"scopes": ["1", "2"]},
            transport=transport,
        )


def test_transport_instance():
    # A client may be instantiated with a custom transport instance.
    transport = transports.EvaluationServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    client = EvaluationServiceClient(transport=transport)
    assert client.transport is transport


def test_transport_get_channel():
    # A client may be instantiated with a custom transport instance.
    transport = transports.EvaluationServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    channel = transport.grpc_channel
    assert channel

    transport = transports.EvaluationServiceGrpcAsyncIOTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    channel = transport.grpc_channel
    assert channel


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.EvaluationServiceGrpcTransport,
        transports.EvaluationServiceGrpcAsyncIOTransport,
        transports.EvaluationServiceRestTransport,
    ],
)
def test_transport_adc(transport_class):
    # Test default credentials are used if not provided.
    with mock.patch.object(google.auth, "default") as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport_class()
        adc.assert_called_once()


def test_transport_kind_grpc():
    transport = EvaluationServiceClient.get_transport_class("grpc")(
        credentials=ga_credentials.AnonymousCredentials()
    )
    assert transport.kind == "grpc"


def test_initialize_client_w_grpc():
    client = EvaluationServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="grpc"
    )
    assert client is not None


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_evaluation_empty_call_grpc():
    client = EvaluationServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_evaluation), "__call__") as call:
        call.return_value = evaluation.Evaluation()
        client.get_evaluation(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = evaluation_service.GetEvaluationRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_evaluations_empty_call_grpc():
    client = EvaluationServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.list_evaluations), "__call__") as call:
        call.return_value = evaluation_service.ListEvaluationsResponse()
        client.list_evaluations(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = evaluation_service.ListEvaluationsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_create_evaluation_empty_call_grpc():
    client = EvaluationServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.create_evaluation), "__call__"
    ) as call:
        call.return_value = operations_pb2.Operation(name="operations/op")
        client.create_evaluation(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = evaluation_service.CreateEvaluationRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_evaluation_results_empty_call_grpc():
    client = EvaluationServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_evaluation_results), "__call__"
    ) as call:
        call.return_value = evaluation_service.ListEvaluationResultsResponse()
        client.list_evaluation_results(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = evaluation_service.ListEvaluationResultsRequest()
        assert args[0] == request_msg


def test_transport_kind_grpc_asyncio():
    transport = EvaluationServiceAsyncClient.get_transport_class("grpc_asyncio")(
        credentials=async_anonymous_credentials()
    )
    assert transport.kind == "grpc_asyncio"


def test_initialize_client_w_grpc_asyncio():
    client = EvaluationServiceAsyncClient(
        credentials=async_anonymous_credentials(), transport="grpc_asyncio"
    )
    assert client is not None


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_get_evaluation_empty_call_grpc_asyncio():
    client = EvaluationServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_evaluation), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            evaluation.Evaluation(
                name="name_value",
                state=evaluation.Evaluation.State.PENDING,
            )
        )
        await client.get_evaluation(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = evaluation_service.GetEvaluationRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_list_evaluations_empty_call_grpc_asyncio():
    client = EvaluationServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.list_evaluations), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            evaluation_service.ListEvaluationsResponse(
                next_page_token="next_page_token_value",
            )
        )
        await client.list_evaluations(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = evaluation_service.ListEvaluationsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_create_evaluation_empty_call_grpc_asyncio():
    client = EvaluationServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.create_evaluation), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        await client.create_evaluation(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = evaluation_service.CreateEvaluationRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_list_evaluation_results_empty_call_grpc_asyncio():
    client = EvaluationServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_evaluation_results), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            evaluation_service.ListEvaluationResultsResponse(
                next_page_token="next_page_token_value",
            )
        )
        await client.list_evaluation_results(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = evaluation_service.ListEvaluationResultsRequest()
        assert args[0] == request_msg


def test_transport_kind_rest():
    transport = EvaluationServiceClient.get_transport_class("rest")(
        credentials=ga_credentials.AnonymousCredentials()
    )
    assert transport.kind == "rest"


def test_get_evaluation_rest_bad_request(
    request_type=evaluation_service.GetEvaluationRequest,
):
    client = EvaluationServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"name": "projects/sample1/locations/sample2/evaluations/sample3"}
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
        client.get_evaluation(request)


@pytest.mark.parametrize(
    "request_type",
    [
        evaluation_service.GetEvaluationRequest,
        dict,
    ],
)
def test_get_evaluation_rest_call_success(request_type):
    client = EvaluationServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"name": "projects/sample1/locations/sample2/evaluations/sample3"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = evaluation.Evaluation(
            name="name_value",
            state=evaluation.Evaluation.State.PENDING,
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = evaluation.Evaluation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.get_evaluation(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, evaluation.Evaluation)
    assert response.name == "name_value"
    assert response.state == evaluation.Evaluation.State.PENDING


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_get_evaluation_rest_interceptors(null_interceptor):
    transport = transports.EvaluationServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.EvaluationServiceRestInterceptor(),
    )
    client = EvaluationServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.EvaluationServiceRestInterceptor, "post_get_evaluation"
        ) as post,
        mock.patch.object(
            transports.EvaluationServiceRestInterceptor,
            "post_get_evaluation_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.EvaluationServiceRestInterceptor, "pre_get_evaluation"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = evaluation_service.GetEvaluationRequest.pb(
            evaluation_service.GetEvaluationRequest()
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
        return_value = evaluation.Evaluation.to_json(evaluation.Evaluation())
        req.return_value.content = return_value

        request = evaluation_service.GetEvaluationRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = evaluation.Evaluation()
        post_with_metadata.return_value = evaluation.Evaluation(), metadata

        client.get_evaluation(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_list_evaluations_rest_bad_request(
    request_type=evaluation_service.ListEvaluationsRequest,
):
    client = EvaluationServiceClient(
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
        client.list_evaluations(request)


@pytest.mark.parametrize(
    "request_type",
    [
        evaluation_service.ListEvaluationsRequest,
        dict,
    ],
)
def test_list_evaluations_rest_call_success(request_type):
    client = EvaluationServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1/locations/sample2"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = evaluation_service.ListEvaluationsResponse(
            next_page_token="next_page_token_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = evaluation_service.ListEvaluationsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.list_evaluations(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListEvaluationsPager)
    assert response.next_page_token == "next_page_token_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_list_evaluations_rest_interceptors(null_interceptor):
    transport = transports.EvaluationServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.EvaluationServiceRestInterceptor(),
    )
    client = EvaluationServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.EvaluationServiceRestInterceptor, "post_list_evaluations"
        ) as post,
        mock.patch.object(
            transports.EvaluationServiceRestInterceptor,
            "post_list_evaluations_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.EvaluationServiceRestInterceptor, "pre_list_evaluations"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = evaluation_service.ListEvaluationsRequest.pb(
            evaluation_service.ListEvaluationsRequest()
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
        return_value = evaluation_service.ListEvaluationsResponse.to_json(
            evaluation_service.ListEvaluationsResponse()
        )
        req.return_value.content = return_value

        request = evaluation_service.ListEvaluationsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = evaluation_service.ListEvaluationsResponse()
        post_with_metadata.return_value = (
            evaluation_service.ListEvaluationsResponse(),
            metadata,
        )

        client.list_evaluations(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_create_evaluation_rest_bad_request(
    request_type=evaluation_service.CreateEvaluationRequest,
):
    client = EvaluationServiceClient(
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
        client.create_evaluation(request)


@pytest.mark.parametrize(
    "request_type",
    [
        evaluation_service.CreateEvaluationRequest,
        dict,
    ],
)
def test_create_evaluation_rest_call_success(request_type):
    client = EvaluationServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1/locations/sample2"}
    request_init["evaluation"] = {
        "name": "name_value",
        "evaluation_spec": {
            "search_request": {
                "serving_config": "serving_config_value",
                "branch": "branch_value",
                "query": "query_value",
                "page_categories": ["page_categories_value1", "page_categories_value2"],
                "image_query": {"image_bytes": "image_bytes_value"},
                "page_size": 951,
                "page_token": "page_token_value",
                "offset": 647,
                "one_box_page_size": 1792,
                "data_store_specs": [
                    {
                        "data_store": "data_store_value",
                        "filter": "filter_value",
                        "boost_spec": {
                            "condition_boost_specs": [
                                {
                                    "condition": "condition_value",
                                    "boost": 0.551,
                                    "boost_control_spec": {
                                        "field_name": "field_name_value",
                                        "attribute_type": 1,
                                        "interpolation_type": 1,
                                        "control_points": [
                                            {
                                                "attribute_value": "attribute_value_value",
                                                "boost_amount": 0.1306,
                                            }
                                        ],
                                    },
                                }
                            ]
                        },
                        "custom_search_operators": "custom_search_operators_value",
                        "num_results": 1217,
                    }
                ],
                "num_results_per_data_store": 2796,
                "filter": "filter_value",
                "canonical_filter": "canonical_filter_value",
                "order_by": "order_by_value",
                "user_info": {
                    "user_id": "user_id_value",
                    "user_agent": "user_agent_value",
                    "time_zone": "time_zone_value",
                    "precise_location": {
                        "point": {"latitude": 0.86, "longitude": 0.971},
                        "address": "address_value",
                    },
                },
                "language_code": "language_code_value",
                "region_code": "region_code_value",
                "facet_specs": [
                    {
                        "facet_key": {
                            "key": "key_value",
                            "intervals": [
                                {
                                    "minimum": 0.764,
                                    "exclusive_minimum": 0.18430000000000002,
                                    "maximum": 0.766,
                                    "exclusive_maximum": 0.1845,
                                }
                            ],
                            "restricted_values": [
                                "restricted_values_value1",
                                "restricted_values_value2",
                            ],
                            "prefixes": ["prefixes_value1", "prefixes_value2"],
                            "contains": ["contains_value1", "contains_value2"],
                            "case_insensitive": True,
                            "order_by": "order_by_value",
                        },
                        "limit": 543,
                        "excluded_filter_keys": [
                            "excluded_filter_keys_value1",
                            "excluded_filter_keys_value2",
                        ],
                        "enable_dynamic_position": True,
                    }
                ],
                "boost_spec": {},
                "params": {},
                "query_expansion_spec": {
                    "condition": 1,
                    "pin_unexpanded_results": True,
                },
                "spell_correction_spec": {"mode": 1},
                "user_pseudo_id": "user_pseudo_id_value",
                "content_search_spec": {
                    "snippet_spec": {
                        "max_snippet_count": 1840,
                        "reference_only": True,
                        "return_snippet": True,
                    },
                    "summary_spec": {
                        "summary_result_count": 2196,
                        "include_citations": True,
                        "ignore_adversarial_query": True,
                        "ignore_non_summary_seeking_query": True,
                        "ignore_low_relevant_content": True,
                        "ignore_jail_breaking_query": True,
                        "multimodal_spec": {"image_source": 1},
                        "model_prompt_spec": {"preamble": "preamble_value"},
                        "language_code": "language_code_value",
                        "model_spec": {"version": "version_value"},
                        "use_semantic_chunks": True,
                    },
                    "extractive_content_spec": {
                        "max_extractive_answer_count": 2907,
                        "max_extractive_segment_count": 3006,
                        "return_extractive_segment_score": True,
                        "num_previous_segments": 2289,
                        "num_next_segments": 1843,
                    },
                    "search_result_mode": 1,
                    "chunk_spec": {
                        "num_previous_chunks": 2071,
                        "num_next_chunks": 1625,
                    },
                },
                "embedding_spec": {
                    "embedding_vectors": [
                        {"field_path": "field_path_value", "vector": [0.66, 0.661]}
                    ]
                },
                "ranking_expression": "ranking_expression_value",
                "ranking_expression_backend": 1,
                "safe_search": True,
                "user_labels": {},
                "natural_language_query_understanding_spec": {
                    "filter_extraction_condition": 1,
                    "geo_search_query_detection_field_names": [
                        "geo_search_query_detection_field_names_value1",
                        "geo_search_query_detection_field_names_value2",
                    ],
                    "extracted_filter_behavior": 1,
                    "allowed_field_names": [
                        "allowed_field_names_value1",
                        "allowed_field_names_value2",
                    ],
                },
                "search_as_you_type_spec": {"condition": 1},
                "display_spec": {"match_highlighting_condition": 1},
                "crowding_specs": [
                    {"field": "field_value", "max_count": 974, "mode": 1}
                ],
                "session": "session_value",
                "session_spec": {
                    "query_id": "query_id_value",
                    "search_result_persistence_count": 3328,
                },
                "relevance_threshold": 1,
                "relevance_filter_spec": {
                    "keyword_search_threshold": {
                        "relevance_threshold": 1,
                        "semantic_relevance_threshold": 0.2964,
                    },
                    "semantic_search_threshold": {},
                },
                "personalization_spec": {"mode": 1},
                "relevance_score_spec": {"return_relevance_score": True},
                "search_addon_spec": {
                    "disable_semantic_add_on": True,
                    "disable_kpi_personalization_add_on": True,
                    "disable_generative_answer_add_on": True,
                },
                "custom_ranking_params": {
                    "expressions_to_precompute": [
                        "expressions_to_precompute_value1",
                        "expressions_to_precompute_value2",
                    ]
                },
                "entity": "entity_value",
            },
            "query_set_spec": {"sample_query_set": "sample_query_set_value"},
        },
        "quality_metrics": {
            "doc_recall": {
                "top_1": 0.483,
                "top_3": 0.485,
                "top_5": 0.487,
                "top_10": 0.531,
            },
            "doc_precision": {},
            "doc_ndcg": {},
            "page_recall": {},
            "page_ndcg": {},
        },
        "state": 1,
        "error": {
            "code": 411,
            "message": "message_value",
            "details": [
                {
                    "type_url": "type.googleapis.com/google.protobuf.Duration",
                    "value": b"\x08\x0c\x10\xdb\x07",
                }
            ],
        },
        "create_time": {"seconds": 751, "nanos": 543},
        "end_time": {},
        "error_samples": {},
    }
    # The version of a generated dependency at test runtime may differ from the version used during generation.
    # Delete any fields which are not present in the current runtime dependency
    # See https://github.com/googleapis/gapic-generator-python/issues/1748

    # Determine if the message type is proto-plus or protobuf
    test_field = evaluation_service.CreateEvaluationRequest.meta.fields["evaluation"]

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
    for field, value in request_init["evaluation"].items():  # pragma: NO COVER
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
                for i in range(0, len(request_init["evaluation"][field])):
                    del request_init["evaluation"][field][i][subfield]
            else:
                del request_init["evaluation"][field][subfield]
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
        response = client.create_evaluation(request)

    # Establish that the response is the type that we expect.
    json_return_value = json_format.MessageToJson(return_value)


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_create_evaluation_rest_interceptors(null_interceptor):
    transport = transports.EvaluationServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.EvaluationServiceRestInterceptor(),
    )
    client = EvaluationServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(operation.Operation, "_set_result_from_operation"),
        mock.patch.object(
            transports.EvaluationServiceRestInterceptor, "post_create_evaluation"
        ) as post,
        mock.patch.object(
            transports.EvaluationServiceRestInterceptor,
            "post_create_evaluation_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.EvaluationServiceRestInterceptor, "pre_create_evaluation"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = evaluation_service.CreateEvaluationRequest.pb(
            evaluation_service.CreateEvaluationRequest()
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

        request = evaluation_service.CreateEvaluationRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = operations_pb2.Operation()
        post_with_metadata.return_value = operations_pb2.Operation(), metadata

        client.create_evaluation(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_list_evaluation_results_rest_bad_request(
    request_type=evaluation_service.ListEvaluationResultsRequest,
):
    client = EvaluationServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {
        "evaluation": "projects/sample1/locations/sample2/evaluations/sample3"
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
        client.list_evaluation_results(request)


@pytest.mark.parametrize(
    "request_type",
    [
        evaluation_service.ListEvaluationResultsRequest,
        dict,
    ],
)
def test_list_evaluation_results_rest_call_success(request_type):
    client = EvaluationServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {
        "evaluation": "projects/sample1/locations/sample2/evaluations/sample3"
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = evaluation_service.ListEvaluationResultsResponse(
            next_page_token="next_page_token_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = evaluation_service.ListEvaluationResultsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.list_evaluation_results(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListEvaluationResultsPager)
    assert response.next_page_token == "next_page_token_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_list_evaluation_results_rest_interceptors(null_interceptor):
    transport = transports.EvaluationServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.EvaluationServiceRestInterceptor(),
    )
    client = EvaluationServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.EvaluationServiceRestInterceptor, "post_list_evaluation_results"
        ) as post,
        mock.patch.object(
            transports.EvaluationServiceRestInterceptor,
            "post_list_evaluation_results_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.EvaluationServiceRestInterceptor, "pre_list_evaluation_results"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = evaluation_service.ListEvaluationResultsRequest.pb(
            evaluation_service.ListEvaluationResultsRequest()
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
        return_value = evaluation_service.ListEvaluationResultsResponse.to_json(
            evaluation_service.ListEvaluationResultsResponse()
        )
        req.return_value.content = return_value

        request = evaluation_service.ListEvaluationResultsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = evaluation_service.ListEvaluationResultsResponse()
        post_with_metadata.return_value = (
            evaluation_service.ListEvaluationResultsResponse(),
            metadata,
        )

        client.list_evaluation_results(
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
    client = EvaluationServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type()
    request = json_format.ParseDict(
        {
            "name": "projects/sample1/locations/sample2/collections/sample3/dataStores/sample4/branches/sample5/operations/sample6"
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
    client = EvaluationServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    request_init = {
        "name": "projects/sample1/locations/sample2/collections/sample3/dataStores/sample4/branches/sample5/operations/sample6"
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


def test_get_operation_rest_bad_request(
    request_type=operations_pb2.GetOperationRequest,
):
    client = EvaluationServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type()
    request = json_format.ParseDict(
        {
            "name": "projects/sample1/locations/sample2/collections/sample3/dataConnector/operations/sample4"
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
    client = EvaluationServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    request_init = {
        "name": "projects/sample1/locations/sample2/collections/sample3/dataConnector/operations/sample4"
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
    client = EvaluationServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type()
    request = json_format.ParseDict(
        {
            "name": "projects/sample1/locations/sample2/collections/sample3/dataConnector"
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
        client.list_operations(request)


@pytest.mark.parametrize(
    "request_type",
    [
        operations_pb2.ListOperationsRequest,
        dict,
    ],
)
def test_list_operations_rest(request_type):
    client = EvaluationServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    request_init = {
        "name": "projects/sample1/locations/sample2/collections/sample3/dataConnector"
    }
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
    client = EvaluationServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    assert client is not None


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_evaluation_empty_call_rest():
    client = EvaluationServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_evaluation), "__call__") as call:
        client.get_evaluation(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = evaluation_service.GetEvaluationRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_evaluations_empty_call_rest():
    client = EvaluationServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.list_evaluations), "__call__") as call:
        client.list_evaluations(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = evaluation_service.ListEvaluationsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_create_evaluation_empty_call_rest():
    client = EvaluationServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.create_evaluation), "__call__"
    ) as call:
        client.create_evaluation(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = evaluation_service.CreateEvaluationRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_evaluation_results_empty_call_rest():
    client = EvaluationServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_evaluation_results), "__call__"
    ) as call:
        client.list_evaluation_results(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = evaluation_service.ListEvaluationResultsRequest()
        assert args[0] == request_msg


def test_evaluation_service_rest_lro_client():
    client = EvaluationServiceClient(
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
    client = EvaluationServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    assert isinstance(
        client.transport,
        transports.EvaluationServiceGrpcTransport,
    )


def test_evaluation_service_base_transport_error():
    # Passing both a credentials object and credentials_file should raise an error
    with pytest.raises(core_exceptions.DuplicateCredentialArgs):
        transport = transports.EvaluationServiceTransport(
            credentials=ga_credentials.AnonymousCredentials(),
            credentials_file="credentials.json",
        )


def test_evaluation_service_base_transport():
    # Instantiate the base transport.
    with mock.patch(
        "google.cloud.discoveryengine_v1beta.services.evaluation_service.transports.EvaluationServiceTransport.__init__"
    ) as Transport:
        Transport.return_value = None
        transport = transports.EvaluationServiceTransport(
            credentials=ga_credentials.AnonymousCredentials(),
        )

    # Every method on the transport should just blindly
    # raise NotImplementedError.
    methods = (
        "get_evaluation",
        "list_evaluations",
        "create_evaluation",
        "list_evaluation_results",
        "get_operation",
        "cancel_operation",
        "list_operations",
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


def test_evaluation_service_base_transport_with_credentials_file():
    # Instantiate the base transport with a credentials file
    with (
        mock.patch.object(
            google.auth, "load_credentials_from_file", autospec=True
        ) as load_creds,
        mock.patch(
            "google.cloud.discoveryengine_v1beta.services.evaluation_service.transports.EvaluationServiceTransport._prep_wrapped_messages"
        ) as Transport,
    ):
        Transport.return_value = None
        load_creds.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.EvaluationServiceTransport(
            credentials_file="credentials.json",
            quota_project_id="octopus",
        )
        load_creds.assert_called_once_with(
            "credentials.json",
            scopes=None,
            default_scopes=(
                "https://www.googleapis.com/auth/cloud-platform",
                "https://www.googleapis.com/auth/discoveryengine.assist.readwrite",
                "https://www.googleapis.com/auth/discoveryengine.readwrite",
                "https://www.googleapis.com/auth/discoveryengine.serving.readwrite",
            ),
            quota_project_id="octopus",
        )


def test_evaluation_service_base_transport_with_adc():
    # Test the default credentials are used if credentials and credentials_file are None.
    with (
        mock.patch.object(google.auth, "default", autospec=True) as adc,
        mock.patch(
            "google.cloud.discoveryengine_v1beta.services.evaluation_service.transports.EvaluationServiceTransport._prep_wrapped_messages"
        ) as Transport,
    ):
        Transport.return_value = None
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.EvaluationServiceTransport()
        adc.assert_called_once()


def test_evaluation_service_auth_adc():
    # If no credentials are provided, we should use ADC credentials.
    with mock.patch.object(google.auth, "default", autospec=True) as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        EvaluationServiceClient()
        adc.assert_called_once_with(
            scopes=None,
            default_scopes=(
                "https://www.googleapis.com/auth/cloud-platform",
                "https://www.googleapis.com/auth/discoveryengine.assist.readwrite",
                "https://www.googleapis.com/auth/discoveryengine.readwrite",
                "https://www.googleapis.com/auth/discoveryengine.serving.readwrite",
            ),
            quota_project_id=None,
        )


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.EvaluationServiceGrpcTransport,
        transports.EvaluationServiceGrpcAsyncIOTransport,
    ],
)
def test_evaluation_service_transport_auth_adc(transport_class):
    # If credentials and host are not provided, the transport class should use
    # ADC credentials.
    with mock.patch.object(google.auth, "default", autospec=True) as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport_class(quota_project_id="octopus", scopes=["1", "2"])
        adc.assert_called_once_with(
            scopes=["1", "2"],
            default_scopes=(
                "https://www.googleapis.com/auth/cloud-platform",
                "https://www.googleapis.com/auth/discoveryengine.assist.readwrite",
                "https://www.googleapis.com/auth/discoveryengine.readwrite",
                "https://www.googleapis.com/auth/discoveryengine.serving.readwrite",
            ),
            quota_project_id="octopus",
        )


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.EvaluationServiceGrpcTransport,
        transports.EvaluationServiceGrpcAsyncIOTransport,
        transports.EvaluationServiceRestTransport,
    ],
)
def test_evaluation_service_transport_auth_gdch_credentials(transport_class):
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
        (transports.EvaluationServiceGrpcTransport, grpc_helpers),
        (transports.EvaluationServiceGrpcAsyncIOTransport, grpc_helpers_async),
    ],
)
def test_evaluation_service_transport_create_channel(transport_class, grpc_helpers):
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
            "discoveryengine.googleapis.com:443",
            credentials=creds,
            credentials_file=None,
            quota_project_id="octopus",
            default_scopes=(
                "https://www.googleapis.com/auth/cloud-platform",
                "https://www.googleapis.com/auth/discoveryengine.assist.readwrite",
                "https://www.googleapis.com/auth/discoveryengine.readwrite",
                "https://www.googleapis.com/auth/discoveryengine.serving.readwrite",
            ),
            scopes=["1", "2"],
            default_host="discoveryengine.googleapis.com",
            ssl_credentials=None,
            options=[
                ("grpc.max_send_message_length", -1),
                ("grpc.max_receive_message_length", -1),
            ],
        )


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.EvaluationServiceGrpcTransport,
        transports.EvaluationServiceGrpcAsyncIOTransport,
    ],
)
def test_evaluation_service_grpc_transport_client_cert_source_for_mtls(transport_class):
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


def test_evaluation_service_http_transport_client_cert_source_for_mtls():
    cred = ga_credentials.AnonymousCredentials()
    with mock.patch(
        "google.auth.transport.requests.AuthorizedSession.configure_mtls_channel"
    ) as mock_configure_mtls_channel:
        transports.EvaluationServiceRestTransport(
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
def test_evaluation_service_host_no_port(transport_name):
    client = EvaluationServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(
            api_endpoint="discoveryengine.googleapis.com"
        ),
        transport=transport_name,
    )
    assert client.transport._host == (
        "discoveryengine.googleapis.com:443"
        if transport_name in ["grpc", "grpc_asyncio"]
        else "https://discoveryengine.googleapis.com"
    )


@pytest.mark.parametrize(
    "transport_name",
    [
        "grpc",
        "grpc_asyncio",
        "rest",
    ],
)
def test_evaluation_service_host_with_port(transport_name):
    client = EvaluationServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(
            api_endpoint="discoveryengine.googleapis.com:8000"
        ),
        transport=transport_name,
    )
    assert client.transport._host == (
        "discoveryengine.googleapis.com:8000"
        if transport_name in ["grpc", "grpc_asyncio"]
        else "https://discoveryengine.googleapis.com:8000"
    )


@pytest.mark.parametrize(
    "transport_name",
    [
        "rest",
    ],
)
def test_evaluation_service_client_transport_session_collision(transport_name):
    creds1 = ga_credentials.AnonymousCredentials()
    creds2 = ga_credentials.AnonymousCredentials()
    client1 = EvaluationServiceClient(
        credentials=creds1,
        transport=transport_name,
    )
    client2 = EvaluationServiceClient(
        credentials=creds2,
        transport=transport_name,
    )
    session1 = client1.transport.get_evaluation._session
    session2 = client2.transport.get_evaluation._session
    assert session1 != session2
    session1 = client1.transport.list_evaluations._session
    session2 = client2.transport.list_evaluations._session
    assert session1 != session2
    session1 = client1.transport.create_evaluation._session
    session2 = client2.transport.create_evaluation._session
    assert session1 != session2
    session1 = client1.transport.list_evaluation_results._session
    session2 = client2.transport.list_evaluation_results._session
    assert session1 != session2


def test_evaluation_service_grpc_transport_channel():
    channel = grpc.secure_channel("http://localhost/", grpc.local_channel_credentials())

    # Check that channel is used if provided.
    transport = transports.EvaluationServiceGrpcTransport(
        host="squid.clam.whelk",
        channel=channel,
    )
    assert transport.grpc_channel == channel
    assert transport._host == "squid.clam.whelk:443"
    assert transport._ssl_channel_credentials == None


def test_evaluation_service_grpc_asyncio_transport_channel():
    channel = aio.secure_channel("http://localhost/", grpc.local_channel_credentials())

    # Check that channel is used if provided.
    transport = transports.EvaluationServiceGrpcAsyncIOTransport(
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
        transports.EvaluationServiceGrpcTransport,
        transports.EvaluationServiceGrpcAsyncIOTransport,
    ],
)
def test_evaluation_service_transport_channel_mtls_with_client_cert_source(
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
        transports.EvaluationServiceGrpcTransport,
        transports.EvaluationServiceGrpcAsyncIOTransport,
    ],
)
def test_evaluation_service_transport_channel_mtls_with_adc(transport_class):
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


def test_evaluation_service_grpc_lro_client():
    client = EvaluationServiceClient(
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


def test_evaluation_service_grpc_lro_async_client():
    client = EvaluationServiceAsyncClient(
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


def test_branch_path():
    project = "squid"
    location = "clam"
    data_store = "whelk"
    branch = "octopus"
    expected = "projects/{project}/locations/{location}/dataStores/{data_store}/branches/{branch}".format(
        project=project,
        location=location,
        data_store=data_store,
        branch=branch,
    )
    actual = EvaluationServiceClient.branch_path(project, location, data_store, branch)
    assert expected == actual


def test_parse_branch_path():
    expected = {
        "project": "oyster",
        "location": "nudibranch",
        "data_store": "cuttlefish",
        "branch": "mussel",
    }
    path = EvaluationServiceClient.branch_path(**expected)

    # Check that the path construction is reversible.
    actual = EvaluationServiceClient.parse_branch_path(path)
    assert expected == actual


def test_data_store_path():
    project = "winkle"
    location = "nautilus"
    data_store = "scallop"
    expected = "projects/{project}/locations/{location}/dataStores/{data_store}".format(
        project=project,
        location=location,
        data_store=data_store,
    )
    actual = EvaluationServiceClient.data_store_path(project, location, data_store)
    assert expected == actual


def test_parse_data_store_path():
    expected = {
        "project": "abalone",
        "location": "squid",
        "data_store": "clam",
    }
    path = EvaluationServiceClient.data_store_path(**expected)

    # Check that the path construction is reversible.
    actual = EvaluationServiceClient.parse_data_store_path(path)
    assert expected == actual


def test_evaluation_path():
    project = "whelk"
    location = "octopus"
    evaluation = "oyster"
    expected = (
        "projects/{project}/locations/{location}/evaluations/{evaluation}".format(
            project=project,
            location=location,
            evaluation=evaluation,
        )
    )
    actual = EvaluationServiceClient.evaluation_path(project, location, evaluation)
    assert expected == actual


def test_parse_evaluation_path():
    expected = {
        "project": "nudibranch",
        "location": "cuttlefish",
        "evaluation": "mussel",
    }
    path = EvaluationServiceClient.evaluation_path(**expected)

    # Check that the path construction is reversible.
    actual = EvaluationServiceClient.parse_evaluation_path(path)
    assert expected == actual


def test_location_path():
    project = "winkle"
    location = "nautilus"
    expected = "projects/{project}/locations/{location}".format(
        project=project,
        location=location,
    )
    actual = EvaluationServiceClient.location_path(project, location)
    assert expected == actual


def test_parse_location_path():
    expected = {
        "project": "scallop",
        "location": "abalone",
    }
    path = EvaluationServiceClient.location_path(**expected)

    # Check that the path construction is reversible.
    actual = EvaluationServiceClient.parse_location_path(path)
    assert expected == actual


def test_sample_query_path():
    project = "squid"
    location = "clam"
    sample_query_set = "whelk"
    sample_query = "octopus"
    expected = "projects/{project}/locations/{location}/sampleQuerySets/{sample_query_set}/sampleQueries/{sample_query}".format(
        project=project,
        location=location,
        sample_query_set=sample_query_set,
        sample_query=sample_query,
    )
    actual = EvaluationServiceClient.sample_query_path(
        project, location, sample_query_set, sample_query
    )
    assert expected == actual


def test_parse_sample_query_path():
    expected = {
        "project": "oyster",
        "location": "nudibranch",
        "sample_query_set": "cuttlefish",
        "sample_query": "mussel",
    }
    path = EvaluationServiceClient.sample_query_path(**expected)

    # Check that the path construction is reversible.
    actual = EvaluationServiceClient.parse_sample_query_path(path)
    assert expected == actual


def test_sample_query_set_path():
    project = "winkle"
    location = "nautilus"
    sample_query_set = "scallop"
    expected = "projects/{project}/locations/{location}/sampleQuerySets/{sample_query_set}".format(
        project=project,
        location=location,
        sample_query_set=sample_query_set,
    )
    actual = EvaluationServiceClient.sample_query_set_path(
        project, location, sample_query_set
    )
    assert expected == actual


def test_parse_sample_query_set_path():
    expected = {
        "project": "abalone",
        "location": "squid",
        "sample_query_set": "clam",
    }
    path = EvaluationServiceClient.sample_query_set_path(**expected)

    # Check that the path construction is reversible.
    actual = EvaluationServiceClient.parse_sample_query_set_path(path)
    assert expected == actual


def test_serving_config_path():
    project = "whelk"
    location = "octopus"
    data_store = "oyster"
    serving_config = "nudibranch"
    expected = "projects/{project}/locations/{location}/dataStores/{data_store}/servingConfigs/{serving_config}".format(
        project=project,
        location=location,
        data_store=data_store,
        serving_config=serving_config,
    )
    actual = EvaluationServiceClient.serving_config_path(
        project, location, data_store, serving_config
    )
    assert expected == actual


def test_parse_serving_config_path():
    expected = {
        "project": "cuttlefish",
        "location": "mussel",
        "data_store": "winkle",
        "serving_config": "nautilus",
    }
    path = EvaluationServiceClient.serving_config_path(**expected)

    # Check that the path construction is reversible.
    actual = EvaluationServiceClient.parse_serving_config_path(path)
    assert expected == actual


def test_session_path():
    project = "scallop"
    location = "abalone"
    data_store = "squid"
    session = "clam"
    expected = "projects/{project}/locations/{location}/dataStores/{data_store}/sessions/{session}".format(
        project=project,
        location=location,
        data_store=data_store,
        session=session,
    )
    actual = EvaluationServiceClient.session_path(
        project, location, data_store, session
    )
    assert expected == actual


def test_parse_session_path():
    expected = {
        "project": "whelk",
        "location": "octopus",
        "data_store": "oyster",
        "session": "nudibranch",
    }
    path = EvaluationServiceClient.session_path(**expected)

    # Check that the path construction is reversible.
    actual = EvaluationServiceClient.parse_session_path(path)
    assert expected == actual


def test_common_billing_account_path():
    billing_account = "cuttlefish"
    expected = "billingAccounts/{billing_account}".format(
        billing_account=billing_account,
    )
    actual = EvaluationServiceClient.common_billing_account_path(billing_account)
    assert expected == actual


def test_parse_common_billing_account_path():
    expected = {
        "billing_account": "mussel",
    }
    path = EvaluationServiceClient.common_billing_account_path(**expected)

    # Check that the path construction is reversible.
    actual = EvaluationServiceClient.parse_common_billing_account_path(path)
    assert expected == actual


def test_common_folder_path():
    folder = "winkle"
    expected = "folders/{folder}".format(
        folder=folder,
    )
    actual = EvaluationServiceClient.common_folder_path(folder)
    assert expected == actual


def test_parse_common_folder_path():
    expected = {
        "folder": "nautilus",
    }
    path = EvaluationServiceClient.common_folder_path(**expected)

    # Check that the path construction is reversible.
    actual = EvaluationServiceClient.parse_common_folder_path(path)
    assert expected == actual


def test_common_organization_path():
    organization = "scallop"
    expected = "organizations/{organization}".format(
        organization=organization,
    )
    actual = EvaluationServiceClient.common_organization_path(organization)
    assert expected == actual


def test_parse_common_organization_path():
    expected = {
        "organization": "abalone",
    }
    path = EvaluationServiceClient.common_organization_path(**expected)

    # Check that the path construction is reversible.
    actual = EvaluationServiceClient.parse_common_organization_path(path)
    assert expected == actual


def test_common_project_path():
    project = "squid"
    expected = "projects/{project}".format(
        project=project,
    )
    actual = EvaluationServiceClient.common_project_path(project)
    assert expected == actual


def test_parse_common_project_path():
    expected = {
        "project": "clam",
    }
    path = EvaluationServiceClient.common_project_path(**expected)

    # Check that the path construction is reversible.
    actual = EvaluationServiceClient.parse_common_project_path(path)
    assert expected == actual


def test_common_location_path():
    project = "whelk"
    location = "octopus"
    expected = "projects/{project}/locations/{location}".format(
        project=project,
        location=location,
    )
    actual = EvaluationServiceClient.common_location_path(project, location)
    assert expected == actual


def test_parse_common_location_path():
    expected = {
        "project": "oyster",
        "location": "nudibranch",
    }
    path = EvaluationServiceClient.common_location_path(**expected)

    # Check that the path construction is reversible.
    actual = EvaluationServiceClient.parse_common_location_path(path)
    assert expected == actual


def test_client_with_default_client_info():
    client_info = gapic_v1.client_info.ClientInfo()

    with mock.patch.object(
        transports.EvaluationServiceTransport, "_prep_wrapped_messages"
    ) as prep:
        client = EvaluationServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)

    with mock.patch.object(
        transports.EvaluationServiceTransport, "_prep_wrapped_messages"
    ) as prep:
        transport_class = EvaluationServiceClient.get_transport_class()
        transport = transport_class(
            credentials=ga_credentials.AnonymousCredentials(),
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)


def test_cancel_operation(transport: str = "grpc"):
    client = EvaluationServiceClient(
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
    client = EvaluationServiceAsyncClient(
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
    client = EvaluationServiceClient(
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
    client = EvaluationServiceAsyncClient(
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
    client = EvaluationServiceClient(
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
    client = EvaluationServiceAsyncClient(
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
    client = EvaluationServiceClient(
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
    client = EvaluationServiceAsyncClient(
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
    client = EvaluationServiceClient(
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
    client = EvaluationServiceAsyncClient(
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
    client = EvaluationServiceClient(
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
    client = EvaluationServiceAsyncClient(
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
    client = EvaluationServiceClient(
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
    client = EvaluationServiceAsyncClient(
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
    client = EvaluationServiceClient(
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
    client = EvaluationServiceAsyncClient(
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
    client = EvaluationServiceClient(
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
    client = EvaluationServiceAsyncClient(
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
    client = EvaluationServiceClient(
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
    client = EvaluationServiceAsyncClient(
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
    client = EvaluationServiceClient(
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
    client = EvaluationServiceAsyncClient(
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
    client = EvaluationServiceClient(
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
    client = EvaluationServiceAsyncClient(
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
    client = EvaluationServiceClient(
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
    client = EvaluationServiceAsyncClient(
        credentials=async_anonymous_credentials(), transport="grpc_asyncio"
    )
    with mock.patch.object(
        type(getattr(client.transport, "_grpc_channel")), "close"
    ) as close:
        async with client:
            close.assert_not_called()
        close.assert_called_once()


def test_transport_close_rest():
    client = EvaluationServiceClient(
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
        client = EvaluationServiceClient(
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
        (EvaluationServiceClient, transports.EvaluationServiceGrpcTransport),
        (
            EvaluationServiceAsyncClient,
            transports.EvaluationServiceGrpcAsyncIOTransport,
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
