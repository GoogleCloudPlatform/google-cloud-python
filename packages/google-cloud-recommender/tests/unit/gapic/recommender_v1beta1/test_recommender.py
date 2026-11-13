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
import google.protobuf.struct_pb2 as struct_pb2  # type: ignore
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

from google.cloud.recommender_v1beta1.services.recommender import (
    RecommenderAsyncClient,
    RecommenderClient,
    pagers,
    transports,
)
from google.cloud.recommender_v1beta1.types import (
    insight,
    insight_type_config,
    recommendation,
    recommender_config,
    recommender_service,
)
from google.cloud.recommender_v1beta1.types import (
    insight_type_config as gcr_insight_type_config,
)
from google.cloud.recommender_v1beta1.types import (
    recommender_config as gcr_recommender_config,
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

    assert RecommenderClient._get_client_cert_source(None, False) is None
    assert (
        RecommenderClient._get_client_cert_source(mock_provided_cert_source, False)
        is None
    )
    assert (
        RecommenderClient._get_client_cert_source(mock_provided_cert_source, True)
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
                RecommenderClient._get_client_cert_source(None, True)
                is mock_default_cert_source
            )
            assert (
                RecommenderClient._get_client_cert_source(
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
    client = RecommenderClient(credentials=cred)
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
    client = RecommenderClient(credentials=cred)
    client._transport._credentials = cred

    error = core_exceptions.GoogleAPICallError("message", details=[])
    error.code = error_code

    client._add_cred_info_for_auth_errors(error)
    assert error.details == []


@pytest.mark.parametrize(
    "client_class,transport_name",
    [
        (RecommenderClient, "grpc"),
        (RecommenderAsyncClient, "grpc_asyncio"),
        (RecommenderClient, "rest"),
    ],
)
def test_recommender_client_from_service_account_info(client_class, transport_name):
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
            "recommender.googleapis.com:443"
            if transport_name in ["grpc", "grpc_asyncio"]
            else "https://recommender.googleapis.com"
        )


@pytest.mark.parametrize(
    "transport_class,transport_name",
    [
        (transports.RecommenderGrpcTransport, "grpc"),
        (transports.RecommenderGrpcAsyncIOTransport, "grpc_asyncio"),
        (transports.RecommenderRestTransport, "rest"),
    ],
)
def test_recommender_client_service_account_always_use_jwt(
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
        (RecommenderClient, "grpc"),
        (RecommenderAsyncClient, "grpc_asyncio"),
        (RecommenderClient, "rest"),
    ],
)
def test_recommender_client_from_service_account_file(client_class, transport_name):
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
            "recommender.googleapis.com:443"
            if transport_name in ["grpc", "grpc_asyncio"]
            else "https://recommender.googleapis.com"
        )


def test_recommender_client_get_transport_class():
    transport = RecommenderClient.get_transport_class()
    available_transports = [
        transports.RecommenderGrpcTransport,
        transports.RecommenderRestTransport,
    ]
    assert transport in available_transports

    transport = RecommenderClient.get_transport_class("grpc")
    assert transport == transports.RecommenderGrpcTransport


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name",
    [
        (RecommenderClient, transports.RecommenderGrpcTransport, "grpc"),
        (
            RecommenderAsyncClient,
            transports.RecommenderGrpcAsyncIOTransport,
            "grpc_asyncio",
        ),
        (RecommenderClient, transports.RecommenderRestTransport, "rest"),
    ],
)
@mock.patch.object(
    RecommenderClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(RecommenderClient),
)
@mock.patch.object(
    RecommenderAsyncClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(RecommenderAsyncClient),
)
def test_recommender_client_client_options(
    client_class, transport_class, transport_name
):
    # Check that if channel is provided we won't create a new one.
    with mock.patch.object(RecommenderClient, "get_transport_class") as gtc:
        transport = transport_class(credentials=ga_credentials.AnonymousCredentials())
        client = client_class(transport=transport)
        gtc.assert_not_called()

    # Check that if channel is provided via str we will create a new one.
    with mock.patch.object(RecommenderClient, "get_transport_class") as gtc:
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
        (RecommenderClient, transports.RecommenderGrpcTransport, "grpc", "true"),
        (
            RecommenderAsyncClient,
            transports.RecommenderGrpcAsyncIOTransport,
            "grpc_asyncio",
            "true",
        ),
        (RecommenderClient, transports.RecommenderGrpcTransport, "grpc", "false"),
        (
            RecommenderAsyncClient,
            transports.RecommenderGrpcAsyncIOTransport,
            "grpc_asyncio",
            "false",
        ),
        (RecommenderClient, transports.RecommenderRestTransport, "rest", "true"),
        (RecommenderClient, transports.RecommenderRestTransport, "rest", "false"),
    ],
)
@mock.patch.object(
    RecommenderClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(RecommenderClient),
)
@mock.patch.object(
    RecommenderAsyncClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(RecommenderAsyncClient),
)
@mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "auto"})
def test_recommender_client_mtls_env_auto(
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


@pytest.mark.parametrize("client_class", [RecommenderClient, RecommenderAsyncClient])
@mock.patch.object(
    RecommenderClient, "DEFAULT_ENDPOINT", modify_default_endpoint(RecommenderClient)
)
@mock.patch.object(
    RecommenderAsyncClient,
    "DEFAULT_ENDPOINT",
    modify_default_endpoint(RecommenderAsyncClient),
)
def test_recommender_client_get_mtls_endpoint_and_cert_source(client_class):
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


@pytest.mark.parametrize("client_class", [RecommenderClient, RecommenderAsyncClient])
@mock.patch.object(
    RecommenderClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(RecommenderClient),
)
@mock.patch.object(
    RecommenderAsyncClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(RecommenderAsyncClient),
)
def test_recommender_client_client_api_endpoint(client_class):
    mock_client_cert_source = client_cert_source_callback
    api_override = "foo.com"
    default_universe = RecommenderClient._DEFAULT_UNIVERSE
    default_endpoint = RecommenderClient._DEFAULT_ENDPOINT_TEMPLATE.format(
        UNIVERSE_DOMAIN=default_universe
    )
    mock_universe = "bar.com"
    mock_endpoint = RecommenderClient._DEFAULT_ENDPOINT_TEMPLATE.format(
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
        (RecommenderClient, transports.RecommenderGrpcTransport, "grpc"),
        (
            RecommenderAsyncClient,
            transports.RecommenderGrpcAsyncIOTransport,
            "grpc_asyncio",
        ),
        (RecommenderClient, transports.RecommenderRestTransport, "rest"),
    ],
)
def test_recommender_client_client_options_scopes(
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
        (RecommenderClient, transports.RecommenderGrpcTransport, "grpc", grpc_helpers),
        (
            RecommenderAsyncClient,
            transports.RecommenderGrpcAsyncIOTransport,
            "grpc_asyncio",
            grpc_helpers_async,
        ),
        (RecommenderClient, transports.RecommenderRestTransport, "rest", None),
    ],
)
def test_recommender_client_client_options_credentials_file(
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


def test_recommender_client_client_options_from_dict():
    with mock.patch(
        "google.cloud.recommender_v1beta1.services.recommender.transports.RecommenderGrpcTransport.__init__"
    ) as grpc_transport:
        grpc_transport.return_value = None
        client = RecommenderClient(client_options={"api_endpoint": "squid.clam.whelk"})
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
        (RecommenderClient, transports.RecommenderGrpcTransport, "grpc", grpc_helpers),
        (
            RecommenderAsyncClient,
            transports.RecommenderGrpcAsyncIOTransport,
            "grpc_asyncio",
            grpc_helpers_async,
        ),
    ],
)
def test_recommender_client_create_channel_credentials_file(
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
            "recommender.googleapis.com:443",
            credentials=file_creds,
            credentials_file=None,
            quota_project_id=None,
            default_scopes=("https://www.googleapis.com/auth/cloud-platform",),
            scopes=None,
            default_host="recommender.googleapis.com",
            ssl_credentials=None,
            options=[
                ("grpc.max_send_message_length", -1),
                ("grpc.max_receive_message_length", -1),
            ],
        )


@pytest.mark.parametrize(
    "request_type",
    [
        recommender_service.ListInsightsRequest(),
        {},
    ],
)
def test_list_insights(request_type, transport: str = "grpc"):
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_insights), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = recommender_service.ListInsightsResponse(
            next_page_token="next_page_token_value",
        )
        response = client.list_insights(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = recommender_service.ListInsightsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListInsightsPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_insights_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = recommender_service.ListInsightsRequest(
        parent="parent_value",
        page_token="page_token_value",
        filter="filter_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_insights), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.list_insights(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = recommender_service.ListInsightsRequest(
            parent="parent_value",
            page_token="page_token_value",
            filter="filter_value",
        )
        assert args[0] == request_msg


def test_list_insights_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = RecommenderClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.list_insights in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.list_insights] = mock_rpc
        request = {}
        client.list_insights(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_insights(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_list_insights_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = RecommenderAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.list_insights
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.list_insights
        ] = mock_rpc

        request = {}
        await client.list_insights(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.list_insights(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        recommender_service.ListInsightsRequest(),
        {},
    ],
)
async def test_list_insights_async(request_type, transport: str = "grpc_asyncio"):
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_insights), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            recommender_service.ListInsightsResponse(
                next_page_token="next_page_token_value",
            )
        )
        response = await client.list_insights(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = recommender_service.ListInsightsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListInsightsAsyncPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_insights_field_headers():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = recommender_service.ListInsightsRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_insights), "__call__") as call:
        call.return_value = recommender_service.ListInsightsResponse()
        client.list_insights(request)

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
async def test_list_insights_field_headers_async():
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = recommender_service.ListInsightsRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_insights), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            recommender_service.ListInsightsResponse()
        )
        await client.list_insights(request)

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


def test_list_insights_flattened():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_insights), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = recommender_service.ListInsightsResponse()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.list_insights(
            parent="parent_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val


def test_list_insights_flattened_error():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_insights(
            recommender_service.ListInsightsRequest(),
            parent="parent_value",
        )


@pytest.mark.asyncio
async def test_list_insights_flattened_async():
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_insights), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = recommender_service.ListInsightsResponse()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            recommender_service.ListInsightsResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.list_insights(
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
async def test_list_insights_flattened_error_async():
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.list_insights(
            recommender_service.ListInsightsRequest(),
            parent="parent_value",
        )


def test_list_insights_pager(transport_name: str = "grpc"):
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_insights), "__call__") as call:
        # Set the response to a series of pages.
        call.side_effect = (
            recommender_service.ListInsightsResponse(
                insights=[
                    insight.Insight(),
                    insight.Insight(),
                    insight.Insight(),
                ],
                next_page_token="abc",
            ),
            recommender_service.ListInsightsResponse(
                insights=[],
                next_page_token="def",
            ),
            recommender_service.ListInsightsResponse(
                insights=[
                    insight.Insight(),
                ],
                next_page_token="ghi",
            ),
            recommender_service.ListInsightsResponse(
                insights=[
                    insight.Insight(),
                    insight.Insight(),
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
        pager = client.list_insights(request={}, retry=retry, timeout=timeout)

        assert pager._metadata == expected_metadata
        assert pager._retry == retry
        assert pager._timeout == timeout

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, insight.Insight) for i in results)


def test_list_insights_pages(transport_name: str = "grpc"):
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_insights), "__call__") as call:
        # Set the response to a series of pages.
        call.side_effect = (
            recommender_service.ListInsightsResponse(
                insights=[
                    insight.Insight(),
                    insight.Insight(),
                    insight.Insight(),
                ],
                next_page_token="abc",
            ),
            recommender_service.ListInsightsResponse(
                insights=[],
                next_page_token="def",
            ),
            recommender_service.ListInsightsResponse(
                insights=[
                    insight.Insight(),
                ],
                next_page_token="ghi",
            ),
            recommender_service.ListInsightsResponse(
                insights=[
                    insight.Insight(),
                    insight.Insight(),
                ],
            ),
            RuntimeError,
        )
        pages = list(client.list_insights(request={}).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.asyncio
async def test_list_insights_async_pager():
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_insights), "__call__", new_callable=mock.AsyncMock
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            recommender_service.ListInsightsResponse(
                insights=[
                    insight.Insight(),
                    insight.Insight(),
                    insight.Insight(),
                ],
                next_page_token="abc",
            ),
            recommender_service.ListInsightsResponse(
                insights=[],
                next_page_token="def",
            ),
            recommender_service.ListInsightsResponse(
                insights=[
                    insight.Insight(),
                ],
                next_page_token="ghi",
            ),
            recommender_service.ListInsightsResponse(
                insights=[
                    insight.Insight(),
                    insight.Insight(),
                ],
            ),
            RuntimeError,
        )
        async_pager = await client.list_insights(
            request={},
        )
        assert async_pager.next_page_token == "abc"
        assert str(async_pager).startswith(f"{async_pager.__class__.__name__}<")

        responses = []
        async for response in async_pager:  # pragma: no branch
            responses.append(response)

        assert len(responses) == 6
        assert all(isinstance(i, insight.Insight) for i in responses)


@pytest.mark.asyncio
async def test_list_insights_async_pages():
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_insights), "__call__", new_callable=mock.AsyncMock
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            recommender_service.ListInsightsResponse(
                insights=[
                    insight.Insight(),
                    insight.Insight(),
                    insight.Insight(),
                ],
                next_page_token="abc",
            ),
            recommender_service.ListInsightsResponse(
                insights=[],
                next_page_token="def",
            ),
            recommender_service.ListInsightsResponse(
                insights=[
                    insight.Insight(),
                ],
                next_page_token="ghi",
            ),
            recommender_service.ListInsightsResponse(
                insights=[
                    insight.Insight(),
                    insight.Insight(),
                ],
            ),
            RuntimeError,
        )
        pages = []
        async for page_ in (await client.list_insights(request={})).pages:
            pages.append(page_)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.parametrize(
    "request_type",
    [
        recommender_service.GetInsightRequest(),
        {},
    ],
)
def test_get_insight(request_type, transport: str = "grpc"):
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_insight), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = insight.Insight(
            name="name_value",
            description="description_value",
            target_resources=["target_resources_value"],
            insight_subtype="insight_subtype_value",
            category=insight.Insight.Category.COST,
            severity=insight.Insight.Severity.LOW,
            etag="etag_value",
        )
        response = client.get_insight(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = recommender_service.GetInsightRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, insight.Insight)
    assert response.name == "name_value"
    assert response.description == "description_value"
    assert response.target_resources == ["target_resources_value"]
    assert response.insight_subtype == "insight_subtype_value"
    assert response.category == insight.Insight.Category.COST
    assert response.severity == insight.Insight.Severity.LOW
    assert response.etag == "etag_value"


def test_get_insight_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = recommender_service.GetInsightRequest(
        name="name_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_insight), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.get_insight(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = recommender_service.GetInsightRequest(
            name="name_value",
        )
        assert args[0] == request_msg


def test_get_insight_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = RecommenderClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.get_insight in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.get_insight] = mock_rpc
        request = {}
        client.get_insight(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_insight(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_get_insight_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = RecommenderAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.get_insight
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.get_insight
        ] = mock_rpc

        request = {}
        await client.get_insight(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.get_insight(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        recommender_service.GetInsightRequest(),
        {},
    ],
)
async def test_get_insight_async(request_type, transport: str = "grpc_asyncio"):
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_insight), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            insight.Insight(
                name="name_value",
                description="description_value",
                target_resources=["target_resources_value"],
                insight_subtype="insight_subtype_value",
                category=insight.Insight.Category.COST,
                severity=insight.Insight.Severity.LOW,
                etag="etag_value",
            )
        )
        response = await client.get_insight(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = recommender_service.GetInsightRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, insight.Insight)
    assert response.name == "name_value"
    assert response.description == "description_value"
    assert response.target_resources == ["target_resources_value"]
    assert response.insight_subtype == "insight_subtype_value"
    assert response.category == insight.Insight.Category.COST
    assert response.severity == insight.Insight.Severity.LOW
    assert response.etag == "etag_value"


def test_get_insight_field_headers():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = recommender_service.GetInsightRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_insight), "__call__") as call:
        call.return_value = insight.Insight()
        client.get_insight(request)

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
async def test_get_insight_field_headers_async():
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = recommender_service.GetInsightRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_insight), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(insight.Insight())
        await client.get_insight(request)

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


def test_get_insight_flattened():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_insight), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = insight.Insight()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.get_insight(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_get_insight_flattened_error():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_insight(
            recommender_service.GetInsightRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_get_insight_flattened_async():
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_insight), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = insight.Insight()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(insight.Insight())
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.get_insight(
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
async def test_get_insight_flattened_error_async():
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.get_insight(
            recommender_service.GetInsightRequest(),
            name="name_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        recommender_service.MarkInsightAcceptedRequest(),
        {},
    ],
)
def test_mark_insight_accepted(request_type, transport: str = "grpc"):
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.mark_insight_accepted), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = insight.Insight(
            name="name_value",
            description="description_value",
            target_resources=["target_resources_value"],
            insight_subtype="insight_subtype_value",
            category=insight.Insight.Category.COST,
            severity=insight.Insight.Severity.LOW,
            etag="etag_value",
        )
        response = client.mark_insight_accepted(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = recommender_service.MarkInsightAcceptedRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, insight.Insight)
    assert response.name == "name_value"
    assert response.description == "description_value"
    assert response.target_resources == ["target_resources_value"]
    assert response.insight_subtype == "insight_subtype_value"
    assert response.category == insight.Insight.Category.COST
    assert response.severity == insight.Insight.Severity.LOW
    assert response.etag == "etag_value"


def test_mark_insight_accepted_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = recommender_service.MarkInsightAcceptedRequest(
        name="name_value",
        etag="etag_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.mark_insight_accepted), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.mark_insight_accepted(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = recommender_service.MarkInsightAcceptedRequest(
            name="name_value",
            etag="etag_value",
        )
        assert args[0] == request_msg


def test_mark_insight_accepted_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = RecommenderClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.mark_insight_accepted
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.mark_insight_accepted] = (
            mock_rpc
        )
        request = {}
        client.mark_insight_accepted(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.mark_insight_accepted(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_mark_insight_accepted_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = RecommenderAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.mark_insight_accepted
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.mark_insight_accepted
        ] = mock_rpc

        request = {}
        await client.mark_insight_accepted(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.mark_insight_accepted(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        recommender_service.MarkInsightAcceptedRequest(),
        {},
    ],
)
async def test_mark_insight_accepted_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.mark_insight_accepted), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            insight.Insight(
                name="name_value",
                description="description_value",
                target_resources=["target_resources_value"],
                insight_subtype="insight_subtype_value",
                category=insight.Insight.Category.COST,
                severity=insight.Insight.Severity.LOW,
                etag="etag_value",
            )
        )
        response = await client.mark_insight_accepted(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = recommender_service.MarkInsightAcceptedRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, insight.Insight)
    assert response.name == "name_value"
    assert response.description == "description_value"
    assert response.target_resources == ["target_resources_value"]
    assert response.insight_subtype == "insight_subtype_value"
    assert response.category == insight.Insight.Category.COST
    assert response.severity == insight.Insight.Severity.LOW
    assert response.etag == "etag_value"


def test_mark_insight_accepted_field_headers():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = recommender_service.MarkInsightAcceptedRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.mark_insight_accepted), "__call__"
    ) as call:
        call.return_value = insight.Insight()
        client.mark_insight_accepted(request)

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
async def test_mark_insight_accepted_field_headers_async():
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = recommender_service.MarkInsightAcceptedRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.mark_insight_accepted), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(insight.Insight())
        await client.mark_insight_accepted(request)

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


def test_mark_insight_accepted_flattened():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.mark_insight_accepted), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = insight.Insight()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.mark_insight_accepted(
            name="name_value",
            state_metadata={"key_value": "value_value"},
            etag="etag_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val
        arg = args[0].state_metadata
        mock_val = {"key_value": "value_value"}
        assert arg == mock_val
        arg = args[0].etag
        mock_val = "etag_value"
        assert arg == mock_val


def test_mark_insight_accepted_flattened_error():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.mark_insight_accepted(
            recommender_service.MarkInsightAcceptedRequest(),
            name="name_value",
            state_metadata={"key_value": "value_value"},
            etag="etag_value",
        )


@pytest.mark.asyncio
async def test_mark_insight_accepted_flattened_async():
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.mark_insight_accepted), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = insight.Insight()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(insight.Insight())
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.mark_insight_accepted(
            name="name_value",
            state_metadata={"key_value": "value_value"},
            etag="etag_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val
        arg = args[0].state_metadata
        mock_val = {"key_value": "value_value"}
        assert arg == mock_val
        arg = args[0].etag
        mock_val = "etag_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_mark_insight_accepted_flattened_error_async():
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.mark_insight_accepted(
            recommender_service.MarkInsightAcceptedRequest(),
            name="name_value",
            state_metadata={"key_value": "value_value"},
            etag="etag_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        recommender_service.ListRecommendationsRequest(),
        {},
    ],
)
def test_list_recommendations(request_type, transport: str = "grpc"):
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_recommendations), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = recommender_service.ListRecommendationsResponse(
            next_page_token="next_page_token_value",
        )
        response = client.list_recommendations(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = recommender_service.ListRecommendationsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListRecommendationsPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_recommendations_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = recommender_service.ListRecommendationsRequest(
        parent="parent_value",
        page_token="page_token_value",
        filter="filter_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_recommendations), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.list_recommendations(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = recommender_service.ListRecommendationsRequest(
            parent="parent_value",
            page_token="page_token_value",
            filter="filter_value",
        )
        assert args[0] == request_msg


def test_list_recommendations_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = RecommenderClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.list_recommendations in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.list_recommendations] = (
            mock_rpc
        )
        request = {}
        client.list_recommendations(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_recommendations(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_list_recommendations_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = RecommenderAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.list_recommendations
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.list_recommendations
        ] = mock_rpc

        request = {}
        await client.list_recommendations(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.list_recommendations(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        recommender_service.ListRecommendationsRequest(),
        {},
    ],
)
async def test_list_recommendations_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_recommendations), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            recommender_service.ListRecommendationsResponse(
                next_page_token="next_page_token_value",
            )
        )
        response = await client.list_recommendations(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = recommender_service.ListRecommendationsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListRecommendationsAsyncPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_recommendations_field_headers():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = recommender_service.ListRecommendationsRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_recommendations), "__call__"
    ) as call:
        call.return_value = recommender_service.ListRecommendationsResponse()
        client.list_recommendations(request)

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
async def test_list_recommendations_field_headers_async():
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = recommender_service.ListRecommendationsRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_recommendations), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            recommender_service.ListRecommendationsResponse()
        )
        await client.list_recommendations(request)

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


def test_list_recommendations_flattened():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_recommendations), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = recommender_service.ListRecommendationsResponse()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.list_recommendations(
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


def test_list_recommendations_flattened_error():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_recommendations(
            recommender_service.ListRecommendationsRequest(),
            parent="parent_value",
            filter="filter_value",
        )


@pytest.mark.asyncio
async def test_list_recommendations_flattened_async():
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_recommendations), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = recommender_service.ListRecommendationsResponse()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            recommender_service.ListRecommendationsResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.list_recommendations(
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
async def test_list_recommendations_flattened_error_async():
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.list_recommendations(
            recommender_service.ListRecommendationsRequest(),
            parent="parent_value",
            filter="filter_value",
        )


def test_list_recommendations_pager(transport_name: str = "grpc"):
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_recommendations), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            recommender_service.ListRecommendationsResponse(
                recommendations=[
                    recommendation.Recommendation(),
                    recommendation.Recommendation(),
                    recommendation.Recommendation(),
                ],
                next_page_token="abc",
            ),
            recommender_service.ListRecommendationsResponse(
                recommendations=[],
                next_page_token="def",
            ),
            recommender_service.ListRecommendationsResponse(
                recommendations=[
                    recommendation.Recommendation(),
                ],
                next_page_token="ghi",
            ),
            recommender_service.ListRecommendationsResponse(
                recommendations=[
                    recommendation.Recommendation(),
                    recommendation.Recommendation(),
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
        pager = client.list_recommendations(request={}, retry=retry, timeout=timeout)

        assert pager._metadata == expected_metadata
        assert pager._retry == retry
        assert pager._timeout == timeout

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, recommendation.Recommendation) for i in results)


def test_list_recommendations_pages(transport_name: str = "grpc"):
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_recommendations), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            recommender_service.ListRecommendationsResponse(
                recommendations=[
                    recommendation.Recommendation(),
                    recommendation.Recommendation(),
                    recommendation.Recommendation(),
                ],
                next_page_token="abc",
            ),
            recommender_service.ListRecommendationsResponse(
                recommendations=[],
                next_page_token="def",
            ),
            recommender_service.ListRecommendationsResponse(
                recommendations=[
                    recommendation.Recommendation(),
                ],
                next_page_token="ghi",
            ),
            recommender_service.ListRecommendationsResponse(
                recommendations=[
                    recommendation.Recommendation(),
                    recommendation.Recommendation(),
                ],
            ),
            RuntimeError,
        )
        pages = list(client.list_recommendations(request={}).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.asyncio
async def test_list_recommendations_async_pager():
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_recommendations),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            recommender_service.ListRecommendationsResponse(
                recommendations=[
                    recommendation.Recommendation(),
                    recommendation.Recommendation(),
                    recommendation.Recommendation(),
                ],
                next_page_token="abc",
            ),
            recommender_service.ListRecommendationsResponse(
                recommendations=[],
                next_page_token="def",
            ),
            recommender_service.ListRecommendationsResponse(
                recommendations=[
                    recommendation.Recommendation(),
                ],
                next_page_token="ghi",
            ),
            recommender_service.ListRecommendationsResponse(
                recommendations=[
                    recommendation.Recommendation(),
                    recommendation.Recommendation(),
                ],
            ),
            RuntimeError,
        )
        async_pager = await client.list_recommendations(
            request={},
        )
        assert async_pager.next_page_token == "abc"
        assert str(async_pager).startswith(f"{async_pager.__class__.__name__}<")

        responses = []
        async for response in async_pager:  # pragma: no branch
            responses.append(response)

        assert len(responses) == 6
        assert all(isinstance(i, recommendation.Recommendation) for i in responses)


@pytest.mark.asyncio
async def test_list_recommendations_async_pages():
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_recommendations),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            recommender_service.ListRecommendationsResponse(
                recommendations=[
                    recommendation.Recommendation(),
                    recommendation.Recommendation(),
                    recommendation.Recommendation(),
                ],
                next_page_token="abc",
            ),
            recommender_service.ListRecommendationsResponse(
                recommendations=[],
                next_page_token="def",
            ),
            recommender_service.ListRecommendationsResponse(
                recommendations=[
                    recommendation.Recommendation(),
                ],
                next_page_token="ghi",
            ),
            recommender_service.ListRecommendationsResponse(
                recommendations=[
                    recommendation.Recommendation(),
                    recommendation.Recommendation(),
                ],
            ),
            RuntimeError,
        )
        pages = []
        async for page_ in (await client.list_recommendations(request={})).pages:
            pages.append(page_)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.parametrize(
    "request_type",
    [
        recommender_service.GetRecommendationRequest(),
        {},
    ],
)
def test_get_recommendation(request_type, transport: str = "grpc"):
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_recommendation), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = recommendation.Recommendation(
            name="name_value",
            description="description_value",
            recommender_subtype="recommender_subtype_value",
            priority=recommendation.Recommendation.Priority.P4,
            etag="etag_value",
            xor_group_id="xor_group_id_value",
        )
        response = client.get_recommendation(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = recommender_service.GetRecommendationRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, recommendation.Recommendation)
    assert response.name == "name_value"
    assert response.description == "description_value"
    assert response.recommender_subtype == "recommender_subtype_value"
    assert response.priority == recommendation.Recommendation.Priority.P4
    assert response.etag == "etag_value"
    assert response.xor_group_id == "xor_group_id_value"


def test_get_recommendation_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = recommender_service.GetRecommendationRequest(
        name="name_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_recommendation), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.get_recommendation(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = recommender_service.GetRecommendationRequest(
            name="name_value",
        )
        assert args[0] == request_msg


def test_get_recommendation_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = RecommenderClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.get_recommendation in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.get_recommendation] = (
            mock_rpc
        )
        request = {}
        client.get_recommendation(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_recommendation(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_get_recommendation_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = RecommenderAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.get_recommendation
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.get_recommendation
        ] = mock_rpc

        request = {}
        await client.get_recommendation(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.get_recommendation(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        recommender_service.GetRecommendationRequest(),
        {},
    ],
)
async def test_get_recommendation_async(request_type, transport: str = "grpc_asyncio"):
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_recommendation), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            recommendation.Recommendation(
                name="name_value",
                description="description_value",
                recommender_subtype="recommender_subtype_value",
                priority=recommendation.Recommendation.Priority.P4,
                etag="etag_value",
                xor_group_id="xor_group_id_value",
            )
        )
        response = await client.get_recommendation(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = recommender_service.GetRecommendationRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, recommendation.Recommendation)
    assert response.name == "name_value"
    assert response.description == "description_value"
    assert response.recommender_subtype == "recommender_subtype_value"
    assert response.priority == recommendation.Recommendation.Priority.P4
    assert response.etag == "etag_value"
    assert response.xor_group_id == "xor_group_id_value"


def test_get_recommendation_field_headers():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = recommender_service.GetRecommendationRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_recommendation), "__call__"
    ) as call:
        call.return_value = recommendation.Recommendation()
        client.get_recommendation(request)

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
async def test_get_recommendation_field_headers_async():
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = recommender_service.GetRecommendationRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_recommendation), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            recommendation.Recommendation()
        )
        await client.get_recommendation(request)

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


def test_get_recommendation_flattened():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_recommendation), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = recommendation.Recommendation()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.get_recommendation(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_get_recommendation_flattened_error():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_recommendation(
            recommender_service.GetRecommendationRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_get_recommendation_flattened_async():
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_recommendation), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = recommendation.Recommendation()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            recommendation.Recommendation()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.get_recommendation(
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
async def test_get_recommendation_flattened_error_async():
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.get_recommendation(
            recommender_service.GetRecommendationRequest(),
            name="name_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        recommender_service.MarkRecommendationClaimedRequest(),
        {},
    ],
)
def test_mark_recommendation_claimed(request_type, transport: str = "grpc"):
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.mark_recommendation_claimed), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = recommendation.Recommendation(
            name="name_value",
            description="description_value",
            recommender_subtype="recommender_subtype_value",
            priority=recommendation.Recommendation.Priority.P4,
            etag="etag_value",
            xor_group_id="xor_group_id_value",
        )
        response = client.mark_recommendation_claimed(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = recommender_service.MarkRecommendationClaimedRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, recommendation.Recommendation)
    assert response.name == "name_value"
    assert response.description == "description_value"
    assert response.recommender_subtype == "recommender_subtype_value"
    assert response.priority == recommendation.Recommendation.Priority.P4
    assert response.etag == "etag_value"
    assert response.xor_group_id == "xor_group_id_value"


def test_mark_recommendation_claimed_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = recommender_service.MarkRecommendationClaimedRequest(
        name="name_value",
        etag="etag_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.mark_recommendation_claimed), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.mark_recommendation_claimed(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = recommender_service.MarkRecommendationClaimedRequest(
            name="name_value",
            etag="etag_value",
        )
        assert args[0] == request_msg


def test_mark_recommendation_claimed_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = RecommenderClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.mark_recommendation_claimed
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.mark_recommendation_claimed
        ] = mock_rpc
        request = {}
        client.mark_recommendation_claimed(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.mark_recommendation_claimed(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_mark_recommendation_claimed_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = RecommenderAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.mark_recommendation_claimed
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.mark_recommendation_claimed
        ] = mock_rpc

        request = {}
        await client.mark_recommendation_claimed(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.mark_recommendation_claimed(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        recommender_service.MarkRecommendationClaimedRequest(),
        {},
    ],
)
async def test_mark_recommendation_claimed_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.mark_recommendation_claimed), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            recommendation.Recommendation(
                name="name_value",
                description="description_value",
                recommender_subtype="recommender_subtype_value",
                priority=recommendation.Recommendation.Priority.P4,
                etag="etag_value",
                xor_group_id="xor_group_id_value",
            )
        )
        response = await client.mark_recommendation_claimed(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = recommender_service.MarkRecommendationClaimedRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, recommendation.Recommendation)
    assert response.name == "name_value"
    assert response.description == "description_value"
    assert response.recommender_subtype == "recommender_subtype_value"
    assert response.priority == recommendation.Recommendation.Priority.P4
    assert response.etag == "etag_value"
    assert response.xor_group_id == "xor_group_id_value"


def test_mark_recommendation_claimed_field_headers():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = recommender_service.MarkRecommendationClaimedRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.mark_recommendation_claimed), "__call__"
    ) as call:
        call.return_value = recommendation.Recommendation()
        client.mark_recommendation_claimed(request)

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
async def test_mark_recommendation_claimed_field_headers_async():
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = recommender_service.MarkRecommendationClaimedRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.mark_recommendation_claimed), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            recommendation.Recommendation()
        )
        await client.mark_recommendation_claimed(request)

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


def test_mark_recommendation_claimed_flattened():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.mark_recommendation_claimed), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = recommendation.Recommendation()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.mark_recommendation_claimed(
            name="name_value",
            state_metadata={"key_value": "value_value"},
            etag="etag_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val
        arg = args[0].state_metadata
        mock_val = {"key_value": "value_value"}
        assert arg == mock_val
        arg = args[0].etag
        mock_val = "etag_value"
        assert arg == mock_val


def test_mark_recommendation_claimed_flattened_error():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.mark_recommendation_claimed(
            recommender_service.MarkRecommendationClaimedRequest(),
            name="name_value",
            state_metadata={"key_value": "value_value"},
            etag="etag_value",
        )


@pytest.mark.asyncio
async def test_mark_recommendation_claimed_flattened_async():
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.mark_recommendation_claimed), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = recommendation.Recommendation()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            recommendation.Recommendation()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.mark_recommendation_claimed(
            name="name_value",
            state_metadata={"key_value": "value_value"},
            etag="etag_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val
        arg = args[0].state_metadata
        mock_val = {"key_value": "value_value"}
        assert arg == mock_val
        arg = args[0].etag
        mock_val = "etag_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_mark_recommendation_claimed_flattened_error_async():
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.mark_recommendation_claimed(
            recommender_service.MarkRecommendationClaimedRequest(),
            name="name_value",
            state_metadata={"key_value": "value_value"},
            etag="etag_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        recommender_service.MarkRecommendationSucceededRequest(),
        {},
    ],
)
def test_mark_recommendation_succeeded(request_type, transport: str = "grpc"):
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.mark_recommendation_succeeded), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = recommendation.Recommendation(
            name="name_value",
            description="description_value",
            recommender_subtype="recommender_subtype_value",
            priority=recommendation.Recommendation.Priority.P4,
            etag="etag_value",
            xor_group_id="xor_group_id_value",
        )
        response = client.mark_recommendation_succeeded(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = recommender_service.MarkRecommendationSucceededRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, recommendation.Recommendation)
    assert response.name == "name_value"
    assert response.description == "description_value"
    assert response.recommender_subtype == "recommender_subtype_value"
    assert response.priority == recommendation.Recommendation.Priority.P4
    assert response.etag == "etag_value"
    assert response.xor_group_id == "xor_group_id_value"


def test_mark_recommendation_succeeded_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = recommender_service.MarkRecommendationSucceededRequest(
        name="name_value",
        etag="etag_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.mark_recommendation_succeeded), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.mark_recommendation_succeeded(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = recommender_service.MarkRecommendationSucceededRequest(
            name="name_value",
            etag="etag_value",
        )
        assert args[0] == request_msg


def test_mark_recommendation_succeeded_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = RecommenderClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.mark_recommendation_succeeded
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.mark_recommendation_succeeded
        ] = mock_rpc
        request = {}
        client.mark_recommendation_succeeded(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.mark_recommendation_succeeded(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_mark_recommendation_succeeded_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = RecommenderAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.mark_recommendation_succeeded
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.mark_recommendation_succeeded
        ] = mock_rpc

        request = {}
        await client.mark_recommendation_succeeded(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.mark_recommendation_succeeded(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        recommender_service.MarkRecommendationSucceededRequest(),
        {},
    ],
)
async def test_mark_recommendation_succeeded_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.mark_recommendation_succeeded), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            recommendation.Recommendation(
                name="name_value",
                description="description_value",
                recommender_subtype="recommender_subtype_value",
                priority=recommendation.Recommendation.Priority.P4,
                etag="etag_value",
                xor_group_id="xor_group_id_value",
            )
        )
        response = await client.mark_recommendation_succeeded(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = recommender_service.MarkRecommendationSucceededRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, recommendation.Recommendation)
    assert response.name == "name_value"
    assert response.description == "description_value"
    assert response.recommender_subtype == "recommender_subtype_value"
    assert response.priority == recommendation.Recommendation.Priority.P4
    assert response.etag == "etag_value"
    assert response.xor_group_id == "xor_group_id_value"


def test_mark_recommendation_succeeded_field_headers():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = recommender_service.MarkRecommendationSucceededRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.mark_recommendation_succeeded), "__call__"
    ) as call:
        call.return_value = recommendation.Recommendation()
        client.mark_recommendation_succeeded(request)

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
async def test_mark_recommendation_succeeded_field_headers_async():
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = recommender_service.MarkRecommendationSucceededRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.mark_recommendation_succeeded), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            recommendation.Recommendation()
        )
        await client.mark_recommendation_succeeded(request)

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


def test_mark_recommendation_succeeded_flattened():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.mark_recommendation_succeeded), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = recommendation.Recommendation()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.mark_recommendation_succeeded(
            name="name_value",
            state_metadata={"key_value": "value_value"},
            etag="etag_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val
        arg = args[0].state_metadata
        mock_val = {"key_value": "value_value"}
        assert arg == mock_val
        arg = args[0].etag
        mock_val = "etag_value"
        assert arg == mock_val


def test_mark_recommendation_succeeded_flattened_error():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.mark_recommendation_succeeded(
            recommender_service.MarkRecommendationSucceededRequest(),
            name="name_value",
            state_metadata={"key_value": "value_value"},
            etag="etag_value",
        )


@pytest.mark.asyncio
async def test_mark_recommendation_succeeded_flattened_async():
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.mark_recommendation_succeeded), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = recommendation.Recommendation()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            recommendation.Recommendation()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.mark_recommendation_succeeded(
            name="name_value",
            state_metadata={"key_value": "value_value"},
            etag="etag_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val
        arg = args[0].state_metadata
        mock_val = {"key_value": "value_value"}
        assert arg == mock_val
        arg = args[0].etag
        mock_val = "etag_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_mark_recommendation_succeeded_flattened_error_async():
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.mark_recommendation_succeeded(
            recommender_service.MarkRecommendationSucceededRequest(),
            name="name_value",
            state_metadata={"key_value": "value_value"},
            etag="etag_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        recommender_service.MarkRecommendationFailedRequest(),
        {},
    ],
)
def test_mark_recommendation_failed(request_type, transport: str = "grpc"):
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.mark_recommendation_failed), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = recommendation.Recommendation(
            name="name_value",
            description="description_value",
            recommender_subtype="recommender_subtype_value",
            priority=recommendation.Recommendation.Priority.P4,
            etag="etag_value",
            xor_group_id="xor_group_id_value",
        )
        response = client.mark_recommendation_failed(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = recommender_service.MarkRecommendationFailedRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, recommendation.Recommendation)
    assert response.name == "name_value"
    assert response.description == "description_value"
    assert response.recommender_subtype == "recommender_subtype_value"
    assert response.priority == recommendation.Recommendation.Priority.P4
    assert response.etag == "etag_value"
    assert response.xor_group_id == "xor_group_id_value"


def test_mark_recommendation_failed_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = recommender_service.MarkRecommendationFailedRequest(
        name="name_value",
        etag="etag_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.mark_recommendation_failed), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.mark_recommendation_failed(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = recommender_service.MarkRecommendationFailedRequest(
            name="name_value",
            etag="etag_value",
        )
        assert args[0] == request_msg


def test_mark_recommendation_failed_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = RecommenderClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.mark_recommendation_failed
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.mark_recommendation_failed
        ] = mock_rpc
        request = {}
        client.mark_recommendation_failed(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.mark_recommendation_failed(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_mark_recommendation_failed_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = RecommenderAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.mark_recommendation_failed
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.mark_recommendation_failed
        ] = mock_rpc

        request = {}
        await client.mark_recommendation_failed(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.mark_recommendation_failed(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        recommender_service.MarkRecommendationFailedRequest(),
        {},
    ],
)
async def test_mark_recommendation_failed_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.mark_recommendation_failed), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            recommendation.Recommendation(
                name="name_value",
                description="description_value",
                recommender_subtype="recommender_subtype_value",
                priority=recommendation.Recommendation.Priority.P4,
                etag="etag_value",
                xor_group_id="xor_group_id_value",
            )
        )
        response = await client.mark_recommendation_failed(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = recommender_service.MarkRecommendationFailedRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, recommendation.Recommendation)
    assert response.name == "name_value"
    assert response.description == "description_value"
    assert response.recommender_subtype == "recommender_subtype_value"
    assert response.priority == recommendation.Recommendation.Priority.P4
    assert response.etag == "etag_value"
    assert response.xor_group_id == "xor_group_id_value"


def test_mark_recommendation_failed_field_headers():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = recommender_service.MarkRecommendationFailedRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.mark_recommendation_failed), "__call__"
    ) as call:
        call.return_value = recommendation.Recommendation()
        client.mark_recommendation_failed(request)

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
async def test_mark_recommendation_failed_field_headers_async():
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = recommender_service.MarkRecommendationFailedRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.mark_recommendation_failed), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            recommendation.Recommendation()
        )
        await client.mark_recommendation_failed(request)

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


def test_mark_recommendation_failed_flattened():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.mark_recommendation_failed), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = recommendation.Recommendation()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.mark_recommendation_failed(
            name="name_value",
            state_metadata={"key_value": "value_value"},
            etag="etag_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val
        arg = args[0].state_metadata
        mock_val = {"key_value": "value_value"}
        assert arg == mock_val
        arg = args[0].etag
        mock_val = "etag_value"
        assert arg == mock_val


def test_mark_recommendation_failed_flattened_error():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.mark_recommendation_failed(
            recommender_service.MarkRecommendationFailedRequest(),
            name="name_value",
            state_metadata={"key_value": "value_value"},
            etag="etag_value",
        )


@pytest.mark.asyncio
async def test_mark_recommendation_failed_flattened_async():
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.mark_recommendation_failed), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = recommendation.Recommendation()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            recommendation.Recommendation()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.mark_recommendation_failed(
            name="name_value",
            state_metadata={"key_value": "value_value"},
            etag="etag_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val
        arg = args[0].state_metadata
        mock_val = {"key_value": "value_value"}
        assert arg == mock_val
        arg = args[0].etag
        mock_val = "etag_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_mark_recommendation_failed_flattened_error_async():
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.mark_recommendation_failed(
            recommender_service.MarkRecommendationFailedRequest(),
            name="name_value",
            state_metadata={"key_value": "value_value"},
            etag="etag_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        recommender_service.GetRecommenderConfigRequest(),
        {},
    ],
)
def test_get_recommender_config(request_type, transport: str = "grpc"):
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_recommender_config), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = recommender_config.RecommenderConfig(
            name="name_value",
            etag="etag_value",
            revision_id="revision_id_value",
            display_name="display_name_value",
        )
        response = client.get_recommender_config(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = recommender_service.GetRecommenderConfigRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, recommender_config.RecommenderConfig)
    assert response.name == "name_value"
    assert response.etag == "etag_value"
    assert response.revision_id == "revision_id_value"
    assert response.display_name == "display_name_value"


def test_get_recommender_config_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = recommender_service.GetRecommenderConfigRequest(
        name="name_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_recommender_config), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.get_recommender_config(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = recommender_service.GetRecommenderConfigRequest(
            name="name_value",
        )
        assert args[0] == request_msg


def test_get_recommender_config_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = RecommenderClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.get_recommender_config
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.get_recommender_config] = (
            mock_rpc
        )
        request = {}
        client.get_recommender_config(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_recommender_config(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_get_recommender_config_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = RecommenderAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.get_recommender_config
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.get_recommender_config
        ] = mock_rpc

        request = {}
        await client.get_recommender_config(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.get_recommender_config(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        recommender_service.GetRecommenderConfigRequest(),
        {},
    ],
)
async def test_get_recommender_config_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_recommender_config), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            recommender_config.RecommenderConfig(
                name="name_value",
                etag="etag_value",
                revision_id="revision_id_value",
                display_name="display_name_value",
            )
        )
        response = await client.get_recommender_config(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = recommender_service.GetRecommenderConfigRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, recommender_config.RecommenderConfig)
    assert response.name == "name_value"
    assert response.etag == "etag_value"
    assert response.revision_id == "revision_id_value"
    assert response.display_name == "display_name_value"


def test_get_recommender_config_field_headers():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = recommender_service.GetRecommenderConfigRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_recommender_config), "__call__"
    ) as call:
        call.return_value = recommender_config.RecommenderConfig()
        client.get_recommender_config(request)

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
async def test_get_recommender_config_field_headers_async():
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = recommender_service.GetRecommenderConfigRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_recommender_config), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            recommender_config.RecommenderConfig()
        )
        await client.get_recommender_config(request)

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


def test_get_recommender_config_flattened():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_recommender_config), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = recommender_config.RecommenderConfig()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.get_recommender_config(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_get_recommender_config_flattened_error():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_recommender_config(
            recommender_service.GetRecommenderConfigRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_get_recommender_config_flattened_async():
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_recommender_config), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = recommender_config.RecommenderConfig()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            recommender_config.RecommenderConfig()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.get_recommender_config(
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
async def test_get_recommender_config_flattened_error_async():
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.get_recommender_config(
            recommender_service.GetRecommenderConfigRequest(),
            name="name_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        recommender_service.UpdateRecommenderConfigRequest(),
        {},
    ],
)
def test_update_recommender_config(request_type, transport: str = "grpc"):
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_recommender_config), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = gcr_recommender_config.RecommenderConfig(
            name="name_value",
            etag="etag_value",
            revision_id="revision_id_value",
            display_name="display_name_value",
        )
        response = client.update_recommender_config(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = recommender_service.UpdateRecommenderConfigRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, gcr_recommender_config.RecommenderConfig)
    assert response.name == "name_value"
    assert response.etag == "etag_value"
    assert response.revision_id == "revision_id_value"
    assert response.display_name == "display_name_value"


def test_update_recommender_config_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = recommender_service.UpdateRecommenderConfigRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_recommender_config), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.update_recommender_config(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = recommender_service.UpdateRecommenderConfigRequest()
        assert args[0] == request_msg


def test_update_recommender_config_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = RecommenderClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.update_recommender_config
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.update_recommender_config
        ] = mock_rpc
        request = {}
        client.update_recommender_config(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.update_recommender_config(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_update_recommender_config_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = RecommenderAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.update_recommender_config
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.update_recommender_config
        ] = mock_rpc

        request = {}
        await client.update_recommender_config(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.update_recommender_config(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        recommender_service.UpdateRecommenderConfigRequest(),
        {},
    ],
)
async def test_update_recommender_config_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_recommender_config), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            gcr_recommender_config.RecommenderConfig(
                name="name_value",
                etag="etag_value",
                revision_id="revision_id_value",
                display_name="display_name_value",
            )
        )
        response = await client.update_recommender_config(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = recommender_service.UpdateRecommenderConfigRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, gcr_recommender_config.RecommenderConfig)
    assert response.name == "name_value"
    assert response.etag == "etag_value"
    assert response.revision_id == "revision_id_value"
    assert response.display_name == "display_name_value"


def test_update_recommender_config_field_headers():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = recommender_service.UpdateRecommenderConfigRequest()

    request.recommender_config.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_recommender_config), "__call__"
    ) as call:
        call.return_value = gcr_recommender_config.RecommenderConfig()
        client.update_recommender_config(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "recommender_config.name=name_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_update_recommender_config_field_headers_async():
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = recommender_service.UpdateRecommenderConfigRequest()

    request.recommender_config.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_recommender_config), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            gcr_recommender_config.RecommenderConfig()
        )
        await client.update_recommender_config(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "recommender_config.name=name_value",
    ) in kw["metadata"]


def test_update_recommender_config_flattened():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_recommender_config), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = gcr_recommender_config.RecommenderConfig()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.update_recommender_config(
            recommender_config=gcr_recommender_config.RecommenderConfig(
                name="name_value"
            ),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].recommender_config
        mock_val = gcr_recommender_config.RecommenderConfig(name="name_value")
        assert arg == mock_val
        arg = args[0].update_mask
        mock_val = field_mask_pb2.FieldMask(paths=["paths_value"])
        assert arg == mock_val


def test_update_recommender_config_flattened_error():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.update_recommender_config(
            recommender_service.UpdateRecommenderConfigRequest(),
            recommender_config=gcr_recommender_config.RecommenderConfig(
                name="name_value"
            ),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


@pytest.mark.asyncio
async def test_update_recommender_config_flattened_async():
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_recommender_config), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = gcr_recommender_config.RecommenderConfig()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            gcr_recommender_config.RecommenderConfig()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.update_recommender_config(
            recommender_config=gcr_recommender_config.RecommenderConfig(
                name="name_value"
            ),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].recommender_config
        mock_val = gcr_recommender_config.RecommenderConfig(name="name_value")
        assert arg == mock_val
        arg = args[0].update_mask
        mock_val = field_mask_pb2.FieldMask(paths=["paths_value"])
        assert arg == mock_val


@pytest.mark.asyncio
async def test_update_recommender_config_flattened_error_async():
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.update_recommender_config(
            recommender_service.UpdateRecommenderConfigRequest(),
            recommender_config=gcr_recommender_config.RecommenderConfig(
                name="name_value"
            ),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


@pytest.mark.parametrize(
    "request_type",
    [
        recommender_service.GetInsightTypeConfigRequest(),
        {},
    ],
)
def test_get_insight_type_config(request_type, transport: str = "grpc"):
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_insight_type_config), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = insight_type_config.InsightTypeConfig(
            name="name_value",
            etag="etag_value",
            revision_id="revision_id_value",
            display_name="display_name_value",
        )
        response = client.get_insight_type_config(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = recommender_service.GetInsightTypeConfigRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, insight_type_config.InsightTypeConfig)
    assert response.name == "name_value"
    assert response.etag == "etag_value"
    assert response.revision_id == "revision_id_value"
    assert response.display_name == "display_name_value"


def test_get_insight_type_config_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = recommender_service.GetInsightTypeConfigRequest(
        name="name_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_insight_type_config), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.get_insight_type_config(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = recommender_service.GetInsightTypeConfigRequest(
            name="name_value",
        )
        assert args[0] == request_msg


def test_get_insight_type_config_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = RecommenderClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.get_insight_type_config
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.get_insight_type_config
        ] = mock_rpc
        request = {}
        client.get_insight_type_config(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_insight_type_config(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_get_insight_type_config_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = RecommenderAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.get_insight_type_config
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.get_insight_type_config
        ] = mock_rpc

        request = {}
        await client.get_insight_type_config(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.get_insight_type_config(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        recommender_service.GetInsightTypeConfigRequest(),
        {},
    ],
)
async def test_get_insight_type_config_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_insight_type_config), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            insight_type_config.InsightTypeConfig(
                name="name_value",
                etag="etag_value",
                revision_id="revision_id_value",
                display_name="display_name_value",
            )
        )
        response = await client.get_insight_type_config(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = recommender_service.GetInsightTypeConfigRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, insight_type_config.InsightTypeConfig)
    assert response.name == "name_value"
    assert response.etag == "etag_value"
    assert response.revision_id == "revision_id_value"
    assert response.display_name == "display_name_value"


def test_get_insight_type_config_field_headers():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = recommender_service.GetInsightTypeConfigRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_insight_type_config), "__call__"
    ) as call:
        call.return_value = insight_type_config.InsightTypeConfig()
        client.get_insight_type_config(request)

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
async def test_get_insight_type_config_field_headers_async():
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = recommender_service.GetInsightTypeConfigRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_insight_type_config), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            insight_type_config.InsightTypeConfig()
        )
        await client.get_insight_type_config(request)

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


def test_get_insight_type_config_flattened():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_insight_type_config), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = insight_type_config.InsightTypeConfig()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.get_insight_type_config(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_get_insight_type_config_flattened_error():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_insight_type_config(
            recommender_service.GetInsightTypeConfigRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_get_insight_type_config_flattened_async():
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_insight_type_config), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = insight_type_config.InsightTypeConfig()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            insight_type_config.InsightTypeConfig()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.get_insight_type_config(
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
async def test_get_insight_type_config_flattened_error_async():
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.get_insight_type_config(
            recommender_service.GetInsightTypeConfigRequest(),
            name="name_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        recommender_service.UpdateInsightTypeConfigRequest(),
        {},
    ],
)
def test_update_insight_type_config(request_type, transport: str = "grpc"):
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_insight_type_config), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = gcr_insight_type_config.InsightTypeConfig(
            name="name_value",
            etag="etag_value",
            revision_id="revision_id_value",
            display_name="display_name_value",
        )
        response = client.update_insight_type_config(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = recommender_service.UpdateInsightTypeConfigRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, gcr_insight_type_config.InsightTypeConfig)
    assert response.name == "name_value"
    assert response.etag == "etag_value"
    assert response.revision_id == "revision_id_value"
    assert response.display_name == "display_name_value"


def test_update_insight_type_config_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = recommender_service.UpdateInsightTypeConfigRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_insight_type_config), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.update_insight_type_config(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = recommender_service.UpdateInsightTypeConfigRequest()
        assert args[0] == request_msg


def test_update_insight_type_config_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = RecommenderClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.update_insight_type_config
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.update_insight_type_config
        ] = mock_rpc
        request = {}
        client.update_insight_type_config(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.update_insight_type_config(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_update_insight_type_config_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = RecommenderAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.update_insight_type_config
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.update_insight_type_config
        ] = mock_rpc

        request = {}
        await client.update_insight_type_config(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.update_insight_type_config(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        recommender_service.UpdateInsightTypeConfigRequest(),
        {},
    ],
)
async def test_update_insight_type_config_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_insight_type_config), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            gcr_insight_type_config.InsightTypeConfig(
                name="name_value",
                etag="etag_value",
                revision_id="revision_id_value",
                display_name="display_name_value",
            )
        )
        response = await client.update_insight_type_config(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = recommender_service.UpdateInsightTypeConfigRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, gcr_insight_type_config.InsightTypeConfig)
    assert response.name == "name_value"
    assert response.etag == "etag_value"
    assert response.revision_id == "revision_id_value"
    assert response.display_name == "display_name_value"


def test_update_insight_type_config_field_headers():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = recommender_service.UpdateInsightTypeConfigRequest()

    request.insight_type_config.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_insight_type_config), "__call__"
    ) as call:
        call.return_value = gcr_insight_type_config.InsightTypeConfig()
        client.update_insight_type_config(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "insight_type_config.name=name_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_update_insight_type_config_field_headers_async():
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = recommender_service.UpdateInsightTypeConfigRequest()

    request.insight_type_config.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_insight_type_config), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            gcr_insight_type_config.InsightTypeConfig()
        )
        await client.update_insight_type_config(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "insight_type_config.name=name_value",
    ) in kw["metadata"]


def test_update_insight_type_config_flattened():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_insight_type_config), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = gcr_insight_type_config.InsightTypeConfig()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.update_insight_type_config(
            insight_type_config=gcr_insight_type_config.InsightTypeConfig(
                name="name_value"
            ),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].insight_type_config
        mock_val = gcr_insight_type_config.InsightTypeConfig(name="name_value")
        assert arg == mock_val
        arg = args[0].update_mask
        mock_val = field_mask_pb2.FieldMask(paths=["paths_value"])
        assert arg == mock_val


def test_update_insight_type_config_flattened_error():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.update_insight_type_config(
            recommender_service.UpdateInsightTypeConfigRequest(),
            insight_type_config=gcr_insight_type_config.InsightTypeConfig(
                name="name_value"
            ),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


@pytest.mark.asyncio
async def test_update_insight_type_config_flattened_async():
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_insight_type_config), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = gcr_insight_type_config.InsightTypeConfig()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            gcr_insight_type_config.InsightTypeConfig()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.update_insight_type_config(
            insight_type_config=gcr_insight_type_config.InsightTypeConfig(
                name="name_value"
            ),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].insight_type_config
        mock_val = gcr_insight_type_config.InsightTypeConfig(name="name_value")
        assert arg == mock_val
        arg = args[0].update_mask
        mock_val = field_mask_pb2.FieldMask(paths=["paths_value"])
        assert arg == mock_val


@pytest.mark.asyncio
async def test_update_insight_type_config_flattened_error_async():
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.update_insight_type_config(
            recommender_service.UpdateInsightTypeConfigRequest(),
            insight_type_config=gcr_insight_type_config.InsightTypeConfig(
                name="name_value"
            ),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


@pytest.mark.parametrize(
    "request_type",
    [
        recommender_service.ListRecommendersRequest(),
        {},
    ],
)
def test_list_recommenders(request_type, transport: str = "grpc"):
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_recommenders), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = recommender_service.ListRecommendersResponse(
            next_page_token="next_page_token_value",
        )
        response = client.list_recommenders(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = recommender_service.ListRecommendersRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListRecommendersPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_recommenders_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = recommender_service.ListRecommendersRequest(
        page_token="page_token_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_recommenders), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.list_recommenders(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = recommender_service.ListRecommendersRequest(
            page_token="page_token_value",
        )
        assert args[0] == request_msg


def test_list_recommenders_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = RecommenderClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.list_recommenders in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.list_recommenders] = (
            mock_rpc
        )
        request = {}
        client.list_recommenders(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_recommenders(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_list_recommenders_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = RecommenderAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.list_recommenders
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.list_recommenders
        ] = mock_rpc

        request = {}
        await client.list_recommenders(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.list_recommenders(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        recommender_service.ListRecommendersRequest(),
        {},
    ],
)
async def test_list_recommenders_async(request_type, transport: str = "grpc_asyncio"):
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_recommenders), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            recommender_service.ListRecommendersResponse(
                next_page_token="next_page_token_value",
            )
        )
        response = await client.list_recommenders(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = recommender_service.ListRecommendersRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListRecommendersAsyncPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_recommenders_pager(transport_name: str = "grpc"):
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_recommenders), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            recommender_service.ListRecommendersResponse(
                recommenders=[
                    recommendation.RecommenderType(),
                    recommendation.RecommenderType(),
                    recommendation.RecommenderType(),
                ],
                next_page_token="abc",
            ),
            recommender_service.ListRecommendersResponse(
                recommenders=[],
                next_page_token="def",
            ),
            recommender_service.ListRecommendersResponse(
                recommenders=[
                    recommendation.RecommenderType(),
                ],
                next_page_token="ghi",
            ),
            recommender_service.ListRecommendersResponse(
                recommenders=[
                    recommendation.RecommenderType(),
                    recommendation.RecommenderType(),
                ],
            ),
            RuntimeError,
        )

        expected_metadata = ()
        retry = retries.Retry()
        timeout = 5
        pager = client.list_recommenders(request={}, retry=retry, timeout=timeout)

        assert pager._metadata == expected_metadata
        assert pager._retry == retry
        assert pager._timeout == timeout

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, recommendation.RecommenderType) for i in results)


def test_list_recommenders_pages(transport_name: str = "grpc"):
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_recommenders), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            recommender_service.ListRecommendersResponse(
                recommenders=[
                    recommendation.RecommenderType(),
                    recommendation.RecommenderType(),
                    recommendation.RecommenderType(),
                ],
                next_page_token="abc",
            ),
            recommender_service.ListRecommendersResponse(
                recommenders=[],
                next_page_token="def",
            ),
            recommender_service.ListRecommendersResponse(
                recommenders=[
                    recommendation.RecommenderType(),
                ],
                next_page_token="ghi",
            ),
            recommender_service.ListRecommendersResponse(
                recommenders=[
                    recommendation.RecommenderType(),
                    recommendation.RecommenderType(),
                ],
            ),
            RuntimeError,
        )
        pages = list(client.list_recommenders(request={}).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.asyncio
async def test_list_recommenders_async_pager():
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_recommenders),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            recommender_service.ListRecommendersResponse(
                recommenders=[
                    recommendation.RecommenderType(),
                    recommendation.RecommenderType(),
                    recommendation.RecommenderType(),
                ],
                next_page_token="abc",
            ),
            recommender_service.ListRecommendersResponse(
                recommenders=[],
                next_page_token="def",
            ),
            recommender_service.ListRecommendersResponse(
                recommenders=[
                    recommendation.RecommenderType(),
                ],
                next_page_token="ghi",
            ),
            recommender_service.ListRecommendersResponse(
                recommenders=[
                    recommendation.RecommenderType(),
                    recommendation.RecommenderType(),
                ],
            ),
            RuntimeError,
        )
        async_pager = await client.list_recommenders(
            request={},
        )
        assert async_pager.next_page_token == "abc"
        assert str(async_pager).startswith(f"{async_pager.__class__.__name__}<")

        responses = []
        async for response in async_pager:  # pragma: no branch
            responses.append(response)

        assert len(responses) == 6
        assert all(isinstance(i, recommendation.RecommenderType) for i in responses)


@pytest.mark.asyncio
async def test_list_recommenders_async_pages():
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_recommenders),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            recommender_service.ListRecommendersResponse(
                recommenders=[
                    recommendation.RecommenderType(),
                    recommendation.RecommenderType(),
                    recommendation.RecommenderType(),
                ],
                next_page_token="abc",
            ),
            recommender_service.ListRecommendersResponse(
                recommenders=[],
                next_page_token="def",
            ),
            recommender_service.ListRecommendersResponse(
                recommenders=[
                    recommendation.RecommenderType(),
                ],
                next_page_token="ghi",
            ),
            recommender_service.ListRecommendersResponse(
                recommenders=[
                    recommendation.RecommenderType(),
                    recommendation.RecommenderType(),
                ],
            ),
            RuntimeError,
        )
        pages = []
        async for page_ in (await client.list_recommenders(request={})).pages:
            pages.append(page_)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.parametrize(
    "request_type",
    [
        recommender_service.ListInsightTypesRequest(),
        {},
    ],
)
def test_list_insight_types(request_type, transport: str = "grpc"):
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_insight_types), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = recommender_service.ListInsightTypesResponse(
            next_page_token="next_page_token_value",
        )
        response = client.list_insight_types(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = recommender_service.ListInsightTypesRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListInsightTypesPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_insight_types_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = recommender_service.ListInsightTypesRequest(
        page_token="page_token_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_insight_types), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.list_insight_types(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = recommender_service.ListInsightTypesRequest(
            page_token="page_token_value",
        )
        assert args[0] == request_msg


def test_list_insight_types_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = RecommenderClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.list_insight_types in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.list_insight_types] = (
            mock_rpc
        )
        request = {}
        client.list_insight_types(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_insight_types(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_list_insight_types_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = RecommenderAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.list_insight_types
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.list_insight_types
        ] = mock_rpc

        request = {}
        await client.list_insight_types(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.list_insight_types(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        recommender_service.ListInsightTypesRequest(),
        {},
    ],
)
async def test_list_insight_types_async(request_type, transport: str = "grpc_asyncio"):
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_insight_types), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            recommender_service.ListInsightTypesResponse(
                next_page_token="next_page_token_value",
            )
        )
        response = await client.list_insight_types(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = recommender_service.ListInsightTypesRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListInsightTypesAsyncPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_insight_types_pager(transport_name: str = "grpc"):
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_insight_types), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            recommender_service.ListInsightTypesResponse(
                insight_types=[
                    insight.InsightType(),
                    insight.InsightType(),
                    insight.InsightType(),
                ],
                next_page_token="abc",
            ),
            recommender_service.ListInsightTypesResponse(
                insight_types=[],
                next_page_token="def",
            ),
            recommender_service.ListInsightTypesResponse(
                insight_types=[
                    insight.InsightType(),
                ],
                next_page_token="ghi",
            ),
            recommender_service.ListInsightTypesResponse(
                insight_types=[
                    insight.InsightType(),
                    insight.InsightType(),
                ],
            ),
            RuntimeError,
        )

        expected_metadata = ()
        retry = retries.Retry()
        timeout = 5
        pager = client.list_insight_types(request={}, retry=retry, timeout=timeout)

        assert pager._metadata == expected_metadata
        assert pager._retry == retry
        assert pager._timeout == timeout

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, insight.InsightType) for i in results)


def test_list_insight_types_pages(transport_name: str = "grpc"):
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_insight_types), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            recommender_service.ListInsightTypesResponse(
                insight_types=[
                    insight.InsightType(),
                    insight.InsightType(),
                    insight.InsightType(),
                ],
                next_page_token="abc",
            ),
            recommender_service.ListInsightTypesResponse(
                insight_types=[],
                next_page_token="def",
            ),
            recommender_service.ListInsightTypesResponse(
                insight_types=[
                    insight.InsightType(),
                ],
                next_page_token="ghi",
            ),
            recommender_service.ListInsightTypesResponse(
                insight_types=[
                    insight.InsightType(),
                    insight.InsightType(),
                ],
            ),
            RuntimeError,
        )
        pages = list(client.list_insight_types(request={}).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.asyncio
async def test_list_insight_types_async_pager():
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_insight_types),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            recommender_service.ListInsightTypesResponse(
                insight_types=[
                    insight.InsightType(),
                    insight.InsightType(),
                    insight.InsightType(),
                ],
                next_page_token="abc",
            ),
            recommender_service.ListInsightTypesResponse(
                insight_types=[],
                next_page_token="def",
            ),
            recommender_service.ListInsightTypesResponse(
                insight_types=[
                    insight.InsightType(),
                ],
                next_page_token="ghi",
            ),
            recommender_service.ListInsightTypesResponse(
                insight_types=[
                    insight.InsightType(),
                    insight.InsightType(),
                ],
            ),
            RuntimeError,
        )
        async_pager = await client.list_insight_types(
            request={},
        )
        assert async_pager.next_page_token == "abc"
        assert str(async_pager).startswith(f"{async_pager.__class__.__name__}<")

        responses = []
        async for response in async_pager:  # pragma: no branch
            responses.append(response)

        assert len(responses) == 6
        assert all(isinstance(i, insight.InsightType) for i in responses)


@pytest.mark.asyncio
async def test_list_insight_types_async_pages():
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_insight_types),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            recommender_service.ListInsightTypesResponse(
                insight_types=[
                    insight.InsightType(),
                    insight.InsightType(),
                    insight.InsightType(),
                ],
                next_page_token="abc",
            ),
            recommender_service.ListInsightTypesResponse(
                insight_types=[],
                next_page_token="def",
            ),
            recommender_service.ListInsightTypesResponse(
                insight_types=[
                    insight.InsightType(),
                ],
                next_page_token="ghi",
            ),
            recommender_service.ListInsightTypesResponse(
                insight_types=[
                    insight.InsightType(),
                    insight.InsightType(),
                ],
            ),
            RuntimeError,
        )
        pages = []
        async for page_ in (await client.list_insight_types(request={})).pages:
            pages.append(page_)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


def test_list_insights_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = RecommenderClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.list_insights in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.list_insights] = mock_rpc

        request = {}
        client.list_insights(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_insights(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_list_insights_rest_required_fields(
    request_type=recommender_service.ListInsightsRequest,
):
    transport_class = transports.RecommenderRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseListInsights,
        "_BaseListInsights__REQUIRED_FIELDS_DEFAULT_VALUES",
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
            "pageSize",
            "pageToken",
        )
    )

    # verify required fields with non-default values are left alone
    assert "parent" in jsonified_request
    assert jsonified_request["parent"] == "parent_value"

    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = recommender_service.ListInsightsResponse()
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
            return_value = recommender_service.ListInsightsResponse.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.list_insights(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_list_insights_rest_flattened():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = recommender_service.ListInsightsResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "parent": "projects/sample1/locations/sample2/insightTypes/sample3"
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
        return_value = recommender_service.ListInsightsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.list_insights(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1beta1/{parent=projects/*/locations/*/insightTypes/*}/insights"
            % client.transport._host,
            args[1],
        )


def test_list_insights_rest_flattened_error(transport: str = "rest"):
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_insights(
            recommender_service.ListInsightsRequest(),
            parent="parent_value",
        )


def test_list_insights_rest_pager(transport: str = "rest"):
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        # with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            recommender_service.ListInsightsResponse(
                insights=[
                    insight.Insight(),
                    insight.Insight(),
                    insight.Insight(),
                ],
                next_page_token="abc",
            ),
            recommender_service.ListInsightsResponse(
                insights=[],
                next_page_token="def",
            ),
            recommender_service.ListInsightsResponse(
                insights=[
                    insight.Insight(),
                ],
                next_page_token="ghi",
            ),
            recommender_service.ListInsightsResponse(
                insights=[
                    insight.Insight(),
                    insight.Insight(),
                ],
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(
            recommender_service.ListInsightsResponse.to_json(x) for x in response
        )
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode("UTF-8")
            return_val.status_code = 200
        req.side_effect = return_values

        sample_request = {
            "parent": "projects/sample1/locations/sample2/insightTypes/sample3"
        }

        pager = client.list_insights(request=sample_request)

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, insight.Insight) for i in results)

        pages = list(client.list_insights(request=sample_request).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


def test_get_insight_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = RecommenderClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.get_insight in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.get_insight] = mock_rpc

        request = {}
        client.get_insight(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_insight(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_get_insight_rest_required_fields(
    request_type=recommender_service.GetInsightRequest,
):
    transport_class = transports.RecommenderRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseGetInsight,
        "_BaseGetInsight__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = insight.Insight()
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
            return_value = insight.Insight.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.get_insight(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_get_insight_rest_flattened():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = insight.Insight()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "name": "projects/sample1/locations/sample2/insightTypes/sample3/insights/sample4"
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
        return_value = insight.Insight.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.get_insight(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1beta1/{name=projects/*/locations/*/insightTypes/*/insights/*}"
            % client.transport._host,
            args[1],
        )


def test_get_insight_rest_flattened_error(transport: str = "rest"):
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_insight(
            recommender_service.GetInsightRequest(),
            name="name_value",
        )


def test_mark_insight_accepted_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = RecommenderClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.mark_insight_accepted
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.mark_insight_accepted] = (
            mock_rpc
        )

        request = {}
        client.mark_insight_accepted(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.mark_insight_accepted(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_mark_insight_accepted_rest_required_fields(
    request_type=recommender_service.MarkInsightAcceptedRequest,
):
    transport_class = transports.RecommenderRestTransport

    request_init = {}
    request_init["name"] = ""
    request_init["etag"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseMarkInsightAccepted,
        "_BaseMarkInsightAccepted__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["name"] = "name_value"
    jsonified_request["etag"] = "etag_value"

    # verify required fields with non-default values are left alone
    assert "name" in jsonified_request
    assert jsonified_request["name"] == "name_value"
    assert "etag" in jsonified_request
    assert jsonified_request["etag"] == "etag_value"

    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = insight.Insight()
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
            return_value = insight.Insight.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.mark_insight_accepted(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_mark_insight_accepted_rest_flattened():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = insight.Insight()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "name": "projects/sample1/locations/sample2/insightTypes/sample3/insights/sample4"
        }

        # get truthy value for each flattened field
        mock_args = dict(
            name="name_value",
            state_metadata={"key_value": "value_value"},
            etag="etag_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = insight.Insight.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.mark_insight_accepted(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1beta1/{name=projects/*/locations/*/insightTypes/*/insights/*}:markAccepted"
            % client.transport._host,
            args[1],
        )


def test_mark_insight_accepted_rest_flattened_error(transport: str = "rest"):
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.mark_insight_accepted(
            recommender_service.MarkInsightAcceptedRequest(),
            name="name_value",
            state_metadata={"key_value": "value_value"},
            etag="etag_value",
        )


def test_list_recommendations_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = RecommenderClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.list_recommendations in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.list_recommendations] = (
            mock_rpc
        )

        request = {}
        client.list_recommendations(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_recommendations(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_list_recommendations_rest_required_fields(
    request_type=recommender_service.ListRecommendationsRequest,
):
    transport_class = transports.RecommenderRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseListRecommendations,
        "_BaseListRecommendations__REQUIRED_FIELDS_DEFAULT_VALUES",
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
            "pageSize",
            "pageToken",
        )
    )

    # verify required fields with non-default values are left alone
    assert "parent" in jsonified_request
    assert jsonified_request["parent"] == "parent_value"

    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = recommender_service.ListRecommendationsResponse()
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
            return_value = recommender_service.ListRecommendationsResponse.pb(
                return_value
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.list_recommendations(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_list_recommendations_rest_flattened():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = recommender_service.ListRecommendationsResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "parent": "projects/sample1/locations/sample2/recommenders/sample3"
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
        return_value = recommender_service.ListRecommendationsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.list_recommendations(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1beta1/{parent=projects/*/locations/*/recommenders/*}/recommendations"
            % client.transport._host,
            args[1],
        )


def test_list_recommendations_rest_flattened_error(transport: str = "rest"):
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_recommendations(
            recommender_service.ListRecommendationsRequest(),
            parent="parent_value",
            filter="filter_value",
        )


def test_list_recommendations_rest_pager(transport: str = "rest"):
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        # with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            recommender_service.ListRecommendationsResponse(
                recommendations=[
                    recommendation.Recommendation(),
                    recommendation.Recommendation(),
                    recommendation.Recommendation(),
                ],
                next_page_token="abc",
            ),
            recommender_service.ListRecommendationsResponse(
                recommendations=[],
                next_page_token="def",
            ),
            recommender_service.ListRecommendationsResponse(
                recommendations=[
                    recommendation.Recommendation(),
                ],
                next_page_token="ghi",
            ),
            recommender_service.ListRecommendationsResponse(
                recommendations=[
                    recommendation.Recommendation(),
                    recommendation.Recommendation(),
                ],
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(
            recommender_service.ListRecommendationsResponse.to_json(x) for x in response
        )
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode("UTF-8")
            return_val.status_code = 200
        req.side_effect = return_values

        sample_request = {
            "parent": "projects/sample1/locations/sample2/recommenders/sample3"
        }

        pager = client.list_recommendations(request=sample_request)

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, recommendation.Recommendation) for i in results)

        pages = list(client.list_recommendations(request=sample_request).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


def test_get_recommendation_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = RecommenderClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.get_recommendation in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.get_recommendation] = (
            mock_rpc
        )

        request = {}
        client.get_recommendation(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_recommendation(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_get_recommendation_rest_required_fields(
    request_type=recommender_service.GetRecommendationRequest,
):
    transport_class = transports.RecommenderRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseGetRecommendation,
        "_BaseGetRecommendation__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = recommendation.Recommendation()
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
            return_value = recommendation.Recommendation.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.get_recommendation(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_get_recommendation_rest_flattened():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = recommendation.Recommendation()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "name": "projects/sample1/locations/sample2/recommenders/sample3/recommendations/sample4"
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
        return_value = recommendation.Recommendation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.get_recommendation(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1beta1/{name=projects/*/locations/*/recommenders/*/recommendations/*}"
            % client.transport._host,
            args[1],
        )


def test_get_recommendation_rest_flattened_error(transport: str = "rest"):
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_recommendation(
            recommender_service.GetRecommendationRequest(),
            name="name_value",
        )


def test_mark_recommendation_claimed_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = RecommenderClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.mark_recommendation_claimed
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.mark_recommendation_claimed
        ] = mock_rpc

        request = {}
        client.mark_recommendation_claimed(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.mark_recommendation_claimed(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_mark_recommendation_claimed_rest_required_fields(
    request_type=recommender_service.MarkRecommendationClaimedRequest,
):
    transport_class = transports.RecommenderRestTransport

    request_init = {}
    request_init["name"] = ""
    request_init["etag"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseMarkRecommendationClaimed,
        "_BaseMarkRecommendationClaimed__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["name"] = "name_value"
    jsonified_request["etag"] = "etag_value"

    # verify required fields with non-default values are left alone
    assert "name" in jsonified_request
    assert jsonified_request["name"] == "name_value"
    assert "etag" in jsonified_request
    assert jsonified_request["etag"] == "etag_value"

    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = recommendation.Recommendation()
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
            return_value = recommendation.Recommendation.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.mark_recommendation_claimed(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_mark_recommendation_claimed_rest_flattened():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = recommendation.Recommendation()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "name": "projects/sample1/locations/sample2/recommenders/sample3/recommendations/sample4"
        }

        # get truthy value for each flattened field
        mock_args = dict(
            name="name_value",
            state_metadata={"key_value": "value_value"},
            etag="etag_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = recommendation.Recommendation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.mark_recommendation_claimed(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1beta1/{name=projects/*/locations/*/recommenders/*/recommendations/*}:markClaimed"
            % client.transport._host,
            args[1],
        )


def test_mark_recommendation_claimed_rest_flattened_error(transport: str = "rest"):
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.mark_recommendation_claimed(
            recommender_service.MarkRecommendationClaimedRequest(),
            name="name_value",
            state_metadata={"key_value": "value_value"},
            etag="etag_value",
        )


def test_mark_recommendation_succeeded_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = RecommenderClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.mark_recommendation_succeeded
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.mark_recommendation_succeeded
        ] = mock_rpc

        request = {}
        client.mark_recommendation_succeeded(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.mark_recommendation_succeeded(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_mark_recommendation_succeeded_rest_required_fields(
    request_type=recommender_service.MarkRecommendationSucceededRequest,
):
    transport_class = transports.RecommenderRestTransport

    request_init = {}
    request_init["name"] = ""
    request_init["etag"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseMarkRecommendationSucceeded,
        "_BaseMarkRecommendationSucceeded__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["name"] = "name_value"
    jsonified_request["etag"] = "etag_value"

    # verify required fields with non-default values are left alone
    assert "name" in jsonified_request
    assert jsonified_request["name"] == "name_value"
    assert "etag" in jsonified_request
    assert jsonified_request["etag"] == "etag_value"

    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = recommendation.Recommendation()
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
            return_value = recommendation.Recommendation.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.mark_recommendation_succeeded(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_mark_recommendation_succeeded_rest_flattened():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = recommendation.Recommendation()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "name": "projects/sample1/locations/sample2/recommenders/sample3/recommendations/sample4"
        }

        # get truthy value for each flattened field
        mock_args = dict(
            name="name_value",
            state_metadata={"key_value": "value_value"},
            etag="etag_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = recommendation.Recommendation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.mark_recommendation_succeeded(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1beta1/{name=projects/*/locations/*/recommenders/*/recommendations/*}:markSucceeded"
            % client.transport._host,
            args[1],
        )


def test_mark_recommendation_succeeded_rest_flattened_error(transport: str = "rest"):
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.mark_recommendation_succeeded(
            recommender_service.MarkRecommendationSucceededRequest(),
            name="name_value",
            state_metadata={"key_value": "value_value"},
            etag="etag_value",
        )


def test_mark_recommendation_failed_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = RecommenderClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.mark_recommendation_failed
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.mark_recommendation_failed
        ] = mock_rpc

        request = {}
        client.mark_recommendation_failed(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.mark_recommendation_failed(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_mark_recommendation_failed_rest_required_fields(
    request_type=recommender_service.MarkRecommendationFailedRequest,
):
    transport_class = transports.RecommenderRestTransport

    request_init = {}
    request_init["name"] = ""
    request_init["etag"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseMarkRecommendationFailed,
        "_BaseMarkRecommendationFailed__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["name"] = "name_value"
    jsonified_request["etag"] = "etag_value"

    # verify required fields with non-default values are left alone
    assert "name" in jsonified_request
    assert jsonified_request["name"] == "name_value"
    assert "etag" in jsonified_request
    assert jsonified_request["etag"] == "etag_value"

    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = recommendation.Recommendation()
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
            return_value = recommendation.Recommendation.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.mark_recommendation_failed(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_mark_recommendation_failed_rest_flattened():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = recommendation.Recommendation()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "name": "projects/sample1/locations/sample2/recommenders/sample3/recommendations/sample4"
        }

        # get truthy value for each flattened field
        mock_args = dict(
            name="name_value",
            state_metadata={"key_value": "value_value"},
            etag="etag_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = recommendation.Recommendation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.mark_recommendation_failed(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1beta1/{name=projects/*/locations/*/recommenders/*/recommendations/*}:markFailed"
            % client.transport._host,
            args[1],
        )


def test_mark_recommendation_failed_rest_flattened_error(transport: str = "rest"):
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.mark_recommendation_failed(
            recommender_service.MarkRecommendationFailedRequest(),
            name="name_value",
            state_metadata={"key_value": "value_value"},
            etag="etag_value",
        )


def test_get_recommender_config_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = RecommenderClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.get_recommender_config
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.get_recommender_config] = (
            mock_rpc
        )

        request = {}
        client.get_recommender_config(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_recommender_config(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_get_recommender_config_rest_required_fields(
    request_type=recommender_service.GetRecommenderConfigRequest,
):
    transport_class = transports.RecommenderRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseGetRecommenderConfig,
        "_BaseGetRecommenderConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = recommender_config.RecommenderConfig()
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
            return_value = recommender_config.RecommenderConfig.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.get_recommender_config(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_get_recommender_config_rest_flattened():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = recommender_config.RecommenderConfig()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "name": "projects/sample1/locations/sample2/recommenders/sample3/config"
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
        return_value = recommender_config.RecommenderConfig.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.get_recommender_config(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1beta1/{name=projects/*/locations/*/recommenders/*/config}"
            % client.transport._host,
            args[1],
        )


def test_get_recommender_config_rest_flattened_error(transport: str = "rest"):
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_recommender_config(
            recommender_service.GetRecommenderConfigRequest(),
            name="name_value",
        )


def test_update_recommender_config_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = RecommenderClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.update_recommender_config
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.update_recommender_config
        ] = mock_rpc

        request = {}
        client.update_recommender_config(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.update_recommender_config(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_update_recommender_config_rest_required_fields(
    request_type=recommender_service.UpdateRecommenderConfigRequest,
):
    transport_class = transports.RecommenderRestTransport

    request_init = {}
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseUpdateRecommenderConfig,
        "_BaseUpdateRecommenderConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = gcr_recommender_config.RecommenderConfig()
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
            return_value = gcr_recommender_config.RecommenderConfig.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.update_recommender_config(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_update_recommender_config_rest_flattened():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = gcr_recommender_config.RecommenderConfig()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "recommender_config": {
                "name": "projects/sample1/locations/sample2/recommenders/sample3/config"
            }
        }

        # get truthy value for each flattened field
        mock_args = dict(
            recommender_config=gcr_recommender_config.RecommenderConfig(
                name="name_value"
            ),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = gcr_recommender_config.RecommenderConfig.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.update_recommender_config(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1beta1/{recommender_config.name=projects/*/locations/*/recommenders/*/config}"
            % client.transport._host,
            args[1],
        )


def test_update_recommender_config_rest_flattened_error(transport: str = "rest"):
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.update_recommender_config(
            recommender_service.UpdateRecommenderConfigRequest(),
            recommender_config=gcr_recommender_config.RecommenderConfig(
                name="name_value"
            ),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


def test_get_insight_type_config_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = RecommenderClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.get_insight_type_config
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.get_insight_type_config
        ] = mock_rpc

        request = {}
        client.get_insight_type_config(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_insight_type_config(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_get_insight_type_config_rest_required_fields(
    request_type=recommender_service.GetInsightTypeConfigRequest,
):
    transport_class = transports.RecommenderRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseGetInsightTypeConfig,
        "_BaseGetInsightTypeConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = insight_type_config.InsightTypeConfig()
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
            return_value = insight_type_config.InsightTypeConfig.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.get_insight_type_config(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_get_insight_type_config_rest_flattened():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = insight_type_config.InsightTypeConfig()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "name": "projects/sample1/locations/sample2/insightTypes/sample3/config"
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
        return_value = insight_type_config.InsightTypeConfig.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.get_insight_type_config(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1beta1/{name=projects/*/locations/*/insightTypes/*/config}"
            % client.transport._host,
            args[1],
        )


def test_get_insight_type_config_rest_flattened_error(transport: str = "rest"):
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_insight_type_config(
            recommender_service.GetInsightTypeConfigRequest(),
            name="name_value",
        )


def test_update_insight_type_config_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = RecommenderClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.update_insight_type_config
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.update_insight_type_config
        ] = mock_rpc

        request = {}
        client.update_insight_type_config(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.update_insight_type_config(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_update_insight_type_config_rest_required_fields(
    request_type=recommender_service.UpdateInsightTypeConfigRequest,
):
    transport_class = transports.RecommenderRestTransport

    request_init = {}
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseUpdateInsightTypeConfig,
        "_BaseUpdateInsightTypeConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = gcr_insight_type_config.InsightTypeConfig()
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
            return_value = gcr_insight_type_config.InsightTypeConfig.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.update_insight_type_config(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_update_insight_type_config_rest_flattened():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = gcr_insight_type_config.InsightTypeConfig()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "insight_type_config": {
                "name": "projects/sample1/locations/sample2/insightTypes/sample3/config"
            }
        }

        # get truthy value for each flattened field
        mock_args = dict(
            insight_type_config=gcr_insight_type_config.InsightTypeConfig(
                name="name_value"
            ),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = gcr_insight_type_config.InsightTypeConfig.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.update_insight_type_config(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1beta1/{insight_type_config.name=projects/*/locations/*/insightTypes/*/config}"
            % client.transport._host,
            args[1],
        )


def test_update_insight_type_config_rest_flattened_error(transport: str = "rest"):
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.update_insight_type_config(
            recommender_service.UpdateInsightTypeConfigRequest(),
            insight_type_config=gcr_insight_type_config.InsightTypeConfig(
                name="name_value"
            ),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


def test_list_recommenders_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = RecommenderClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.list_recommenders in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.list_recommenders] = (
            mock_rpc
        )

        request = {}
        client.list_recommenders(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_recommenders(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_list_recommenders_rest_pager(transport: str = "rest"):
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        # with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            recommender_service.ListRecommendersResponse(
                recommenders=[
                    recommendation.RecommenderType(),
                    recommendation.RecommenderType(),
                    recommendation.RecommenderType(),
                ],
                next_page_token="abc",
            ),
            recommender_service.ListRecommendersResponse(
                recommenders=[],
                next_page_token="def",
            ),
            recommender_service.ListRecommendersResponse(
                recommenders=[
                    recommendation.RecommenderType(),
                ],
                next_page_token="ghi",
            ),
            recommender_service.ListRecommendersResponse(
                recommenders=[
                    recommendation.RecommenderType(),
                    recommendation.RecommenderType(),
                ],
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(
            recommender_service.ListRecommendersResponse.to_json(x) for x in response
        )
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode("UTF-8")
            return_val.status_code = 200
        req.side_effect = return_values

        sample_request = {}

        pager = client.list_recommenders(request=sample_request)

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, recommendation.RecommenderType) for i in results)

        pages = list(client.list_recommenders(request=sample_request).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


def test_list_insight_types_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = RecommenderClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.list_insight_types in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.list_insight_types] = (
            mock_rpc
        )

        request = {}
        client.list_insight_types(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_insight_types(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_list_insight_types_rest_pager(transport: str = "rest"):
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        # with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            recommender_service.ListInsightTypesResponse(
                insight_types=[
                    insight.InsightType(),
                    insight.InsightType(),
                    insight.InsightType(),
                ],
                next_page_token="abc",
            ),
            recommender_service.ListInsightTypesResponse(
                insight_types=[],
                next_page_token="def",
            ),
            recommender_service.ListInsightTypesResponse(
                insight_types=[
                    insight.InsightType(),
                ],
                next_page_token="ghi",
            ),
            recommender_service.ListInsightTypesResponse(
                insight_types=[
                    insight.InsightType(),
                    insight.InsightType(),
                ],
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(
            recommender_service.ListInsightTypesResponse.to_json(x) for x in response
        )
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode("UTF-8")
            return_val.status_code = 200
        req.side_effect = return_values

        sample_request = {}

        pager = client.list_insight_types(request=sample_request)

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, insight.InsightType) for i in results)

        pages = list(client.list_insight_types(request=sample_request).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


def test_credentials_transport_error():
    # It is an error to provide credentials and a transport instance.
    transport = transports.RecommenderGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = RecommenderClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport=transport,
        )

    # It is an error to provide a credentials file and a transport instance.
    transport = transports.RecommenderGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = RecommenderClient(
            client_options={"credentials_file": "credentials.json"},
            transport=transport,
        )

    # It is an error to provide an api_key and a transport instance.
    transport = transports.RecommenderGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    options = client_options.ClientOptions()
    options.api_key = "api_key"
    with pytest.raises(ValueError):
        client = RecommenderClient(
            client_options=options,
            transport=transport,
        )

    # It is an error to provide an api_key and a credential.
    options = client_options.ClientOptions()
    options.api_key = "api_key"
    with pytest.raises(ValueError):
        client = RecommenderClient(
            client_options=options, credentials=ga_credentials.AnonymousCredentials()
        )

    # It is an error to provide scopes and a transport instance.
    transport = transports.RecommenderGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = RecommenderClient(
            client_options={"scopes": ["1", "2"]},
            transport=transport,
        )


def test_transport_instance():
    # A client may be instantiated with a custom transport instance.
    transport = transports.RecommenderGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    client = RecommenderClient(transport=transport)
    assert client.transport is transport


def test_transport_get_channel():
    # A client may be instantiated with a custom transport instance.
    transport = transports.RecommenderGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    channel = transport.grpc_channel
    assert channel

    transport = transports.RecommenderGrpcAsyncIOTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    channel = transport.grpc_channel
    assert channel


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.RecommenderGrpcTransport,
        transports.RecommenderGrpcAsyncIOTransport,
        transports.RecommenderRestTransport,
    ],
)
def test_transport_adc(transport_class):
    # Test default credentials are used if not provided.
    with mock.patch.object(google.auth, "default") as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport_class()
        adc.assert_called_once()


def test_transport_kind_grpc():
    transport = RecommenderClient.get_transport_class("grpc")(
        credentials=ga_credentials.AnonymousCredentials()
    )
    assert transport.kind == "grpc"


def test_initialize_client_w_grpc():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="grpc"
    )
    assert client is not None


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_insights_empty_call_grpc():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.list_insights), "__call__") as call:
        call.return_value = recommender_service.ListInsightsResponse()
        client.list_insights(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = recommender_service.ListInsightsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_insight_empty_call_grpc():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_insight), "__call__") as call:
        call.return_value = insight.Insight()
        client.get_insight(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = recommender_service.GetInsightRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_mark_insight_accepted_empty_call_grpc():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.mark_insight_accepted), "__call__"
    ) as call:
        call.return_value = insight.Insight()
        client.mark_insight_accepted(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = recommender_service.MarkInsightAcceptedRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_recommendations_empty_call_grpc():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_recommendations), "__call__"
    ) as call:
        call.return_value = recommender_service.ListRecommendationsResponse()
        client.list_recommendations(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = recommender_service.ListRecommendationsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_recommendation_empty_call_grpc():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.get_recommendation), "__call__"
    ) as call:
        call.return_value = recommendation.Recommendation()
        client.get_recommendation(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = recommender_service.GetRecommendationRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_mark_recommendation_claimed_empty_call_grpc():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.mark_recommendation_claimed), "__call__"
    ) as call:
        call.return_value = recommendation.Recommendation()
        client.mark_recommendation_claimed(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = recommender_service.MarkRecommendationClaimedRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_mark_recommendation_succeeded_empty_call_grpc():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.mark_recommendation_succeeded), "__call__"
    ) as call:
        call.return_value = recommendation.Recommendation()
        client.mark_recommendation_succeeded(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = recommender_service.MarkRecommendationSucceededRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_mark_recommendation_failed_empty_call_grpc():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.mark_recommendation_failed), "__call__"
    ) as call:
        call.return_value = recommendation.Recommendation()
        client.mark_recommendation_failed(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = recommender_service.MarkRecommendationFailedRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_recommender_config_empty_call_grpc():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.get_recommender_config), "__call__"
    ) as call:
        call.return_value = recommender_config.RecommenderConfig()
        client.get_recommender_config(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = recommender_service.GetRecommenderConfigRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_update_recommender_config_empty_call_grpc():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.update_recommender_config), "__call__"
    ) as call:
        call.return_value = gcr_recommender_config.RecommenderConfig()
        client.update_recommender_config(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = recommender_service.UpdateRecommenderConfigRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_insight_type_config_empty_call_grpc():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.get_insight_type_config), "__call__"
    ) as call:
        call.return_value = insight_type_config.InsightTypeConfig()
        client.get_insight_type_config(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = recommender_service.GetInsightTypeConfigRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_update_insight_type_config_empty_call_grpc():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.update_insight_type_config), "__call__"
    ) as call:
        call.return_value = gcr_insight_type_config.InsightTypeConfig()
        client.update_insight_type_config(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = recommender_service.UpdateInsightTypeConfigRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_recommenders_empty_call_grpc():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_recommenders), "__call__"
    ) as call:
        call.return_value = recommender_service.ListRecommendersResponse()
        client.list_recommenders(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = recommender_service.ListRecommendersRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_insight_types_empty_call_grpc():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_insight_types), "__call__"
    ) as call:
        call.return_value = recommender_service.ListInsightTypesResponse()
        client.list_insight_types(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = recommender_service.ListInsightTypesRequest()
        assert args[0] == request_msg


def test_transport_kind_grpc_asyncio():
    transport = RecommenderAsyncClient.get_transport_class("grpc_asyncio")(
        credentials=async_anonymous_credentials()
    )
    assert transport.kind == "grpc_asyncio"


def test_initialize_client_w_grpc_asyncio():
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(), transport="grpc_asyncio"
    )
    assert client is not None


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_list_insights_empty_call_grpc_asyncio():
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.list_insights), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            recommender_service.ListInsightsResponse(
                next_page_token="next_page_token_value",
            )
        )
        await client.list_insights(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = recommender_service.ListInsightsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_get_insight_empty_call_grpc_asyncio():
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_insight), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            insight.Insight(
                name="name_value",
                description="description_value",
                target_resources=["target_resources_value"],
                insight_subtype="insight_subtype_value",
                category=insight.Insight.Category.COST,
                severity=insight.Insight.Severity.LOW,
                etag="etag_value",
            )
        )
        await client.get_insight(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = recommender_service.GetInsightRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_mark_insight_accepted_empty_call_grpc_asyncio():
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.mark_insight_accepted), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            insight.Insight(
                name="name_value",
                description="description_value",
                target_resources=["target_resources_value"],
                insight_subtype="insight_subtype_value",
                category=insight.Insight.Category.COST,
                severity=insight.Insight.Severity.LOW,
                etag="etag_value",
            )
        )
        await client.mark_insight_accepted(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = recommender_service.MarkInsightAcceptedRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_list_recommendations_empty_call_grpc_asyncio():
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_recommendations), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            recommender_service.ListRecommendationsResponse(
                next_page_token="next_page_token_value",
            )
        )
        await client.list_recommendations(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = recommender_service.ListRecommendationsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_get_recommendation_empty_call_grpc_asyncio():
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.get_recommendation), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            recommendation.Recommendation(
                name="name_value",
                description="description_value",
                recommender_subtype="recommender_subtype_value",
                priority=recommendation.Recommendation.Priority.P4,
                etag="etag_value",
                xor_group_id="xor_group_id_value",
            )
        )
        await client.get_recommendation(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = recommender_service.GetRecommendationRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_mark_recommendation_claimed_empty_call_grpc_asyncio():
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.mark_recommendation_claimed), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            recommendation.Recommendation(
                name="name_value",
                description="description_value",
                recommender_subtype="recommender_subtype_value",
                priority=recommendation.Recommendation.Priority.P4,
                etag="etag_value",
                xor_group_id="xor_group_id_value",
            )
        )
        await client.mark_recommendation_claimed(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = recommender_service.MarkRecommendationClaimedRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_mark_recommendation_succeeded_empty_call_grpc_asyncio():
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.mark_recommendation_succeeded), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            recommendation.Recommendation(
                name="name_value",
                description="description_value",
                recommender_subtype="recommender_subtype_value",
                priority=recommendation.Recommendation.Priority.P4,
                etag="etag_value",
                xor_group_id="xor_group_id_value",
            )
        )
        await client.mark_recommendation_succeeded(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = recommender_service.MarkRecommendationSucceededRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_mark_recommendation_failed_empty_call_grpc_asyncio():
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.mark_recommendation_failed), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            recommendation.Recommendation(
                name="name_value",
                description="description_value",
                recommender_subtype="recommender_subtype_value",
                priority=recommendation.Recommendation.Priority.P4,
                etag="etag_value",
                xor_group_id="xor_group_id_value",
            )
        )
        await client.mark_recommendation_failed(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = recommender_service.MarkRecommendationFailedRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_get_recommender_config_empty_call_grpc_asyncio():
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.get_recommender_config), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            recommender_config.RecommenderConfig(
                name="name_value",
                etag="etag_value",
                revision_id="revision_id_value",
                display_name="display_name_value",
            )
        )
        await client.get_recommender_config(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = recommender_service.GetRecommenderConfigRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_update_recommender_config_empty_call_grpc_asyncio():
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.update_recommender_config), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            gcr_recommender_config.RecommenderConfig(
                name="name_value",
                etag="etag_value",
                revision_id="revision_id_value",
                display_name="display_name_value",
            )
        )
        await client.update_recommender_config(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = recommender_service.UpdateRecommenderConfigRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_get_insight_type_config_empty_call_grpc_asyncio():
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.get_insight_type_config), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            insight_type_config.InsightTypeConfig(
                name="name_value",
                etag="etag_value",
                revision_id="revision_id_value",
                display_name="display_name_value",
            )
        )
        await client.get_insight_type_config(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = recommender_service.GetInsightTypeConfigRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_update_insight_type_config_empty_call_grpc_asyncio():
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.update_insight_type_config), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            gcr_insight_type_config.InsightTypeConfig(
                name="name_value",
                etag="etag_value",
                revision_id="revision_id_value",
                display_name="display_name_value",
            )
        )
        await client.update_insight_type_config(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = recommender_service.UpdateInsightTypeConfigRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_list_recommenders_empty_call_grpc_asyncio():
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_recommenders), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            recommender_service.ListRecommendersResponse(
                next_page_token="next_page_token_value",
            )
        )
        await client.list_recommenders(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = recommender_service.ListRecommendersRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_list_insight_types_empty_call_grpc_asyncio():
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_insight_types), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            recommender_service.ListInsightTypesResponse(
                next_page_token="next_page_token_value",
            )
        )
        await client.list_insight_types(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = recommender_service.ListInsightTypesRequest()
        assert args[0] == request_msg


def test_transport_kind_rest():
    transport = RecommenderClient.get_transport_class("rest")(
        credentials=ga_credentials.AnonymousCredentials()
    )
    assert transport.kind == "rest"


def test_list_insights_rest_bad_request(
    request_type=recommender_service.ListInsightsRequest,
):
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1/locations/sample2/insightTypes/sample3"}
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
        client.list_insights(request)


@pytest.mark.parametrize(
    "request_type",
    [
        recommender_service.ListInsightsRequest,
        dict,
    ],
)
def test_list_insights_rest_call_success(request_type):
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1/locations/sample2/insightTypes/sample3"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = recommender_service.ListInsightsResponse(
            next_page_token="next_page_token_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = recommender_service.ListInsightsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.list_insights(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListInsightsPager)
    assert response.next_page_token == "next_page_token_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_list_insights_rest_interceptors(null_interceptor):
    transport = transports.RecommenderRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.RecommenderRestInterceptor(),
    )
    client = RecommenderClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.RecommenderRestInterceptor, "post_list_insights"
        ) as post,
        mock.patch.object(
            transports.RecommenderRestInterceptor, "post_list_insights_with_metadata"
        ) as post_with_metadata,
        mock.patch.object(
            transports.RecommenderRestInterceptor, "pre_list_insights"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = recommender_service.ListInsightsRequest.pb(
            recommender_service.ListInsightsRequest()
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
        return_value = recommender_service.ListInsightsResponse.to_json(
            recommender_service.ListInsightsResponse()
        )
        req.return_value.content = return_value

        request = recommender_service.ListInsightsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = recommender_service.ListInsightsResponse()
        post_with_metadata.return_value = (
            recommender_service.ListInsightsResponse(),
            metadata,
        )

        client.list_insights(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_get_insight_rest_bad_request(
    request_type=recommender_service.GetInsightRequest,
):
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/insightTypes/sample3/insights/sample4"
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
        client.get_insight(request)


@pytest.mark.parametrize(
    "request_type",
    [
        recommender_service.GetInsightRequest,
        dict,
    ],
)
def test_get_insight_rest_call_success(request_type):
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/insightTypes/sample3/insights/sample4"
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = insight.Insight(
            name="name_value",
            description="description_value",
            target_resources=["target_resources_value"],
            insight_subtype="insight_subtype_value",
            category=insight.Insight.Category.COST,
            severity=insight.Insight.Severity.LOW,
            etag="etag_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = insight.Insight.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.get_insight(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, insight.Insight)
    assert response.name == "name_value"
    assert response.description == "description_value"
    assert response.target_resources == ["target_resources_value"]
    assert response.insight_subtype == "insight_subtype_value"
    assert response.category == insight.Insight.Category.COST
    assert response.severity == insight.Insight.Severity.LOW
    assert response.etag == "etag_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_get_insight_rest_interceptors(null_interceptor):
    transport = transports.RecommenderRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.RecommenderRestInterceptor(),
    )
    client = RecommenderClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.RecommenderRestInterceptor, "post_get_insight"
        ) as post,
        mock.patch.object(
            transports.RecommenderRestInterceptor, "post_get_insight_with_metadata"
        ) as post_with_metadata,
        mock.patch.object(
            transports.RecommenderRestInterceptor, "pre_get_insight"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = recommender_service.GetInsightRequest.pb(
            recommender_service.GetInsightRequest()
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
        return_value = insight.Insight.to_json(insight.Insight())
        req.return_value.content = return_value

        request = recommender_service.GetInsightRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = insight.Insight()
        post_with_metadata.return_value = insight.Insight(), metadata

        client.get_insight(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_mark_insight_accepted_rest_bad_request(
    request_type=recommender_service.MarkInsightAcceptedRequest,
):
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/insightTypes/sample3/insights/sample4"
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
        client.mark_insight_accepted(request)


@pytest.mark.parametrize(
    "request_type",
    [
        recommender_service.MarkInsightAcceptedRequest,
        dict,
    ],
)
def test_mark_insight_accepted_rest_call_success(request_type):
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/insightTypes/sample3/insights/sample4"
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = insight.Insight(
            name="name_value",
            description="description_value",
            target_resources=["target_resources_value"],
            insight_subtype="insight_subtype_value",
            category=insight.Insight.Category.COST,
            severity=insight.Insight.Severity.LOW,
            etag="etag_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = insight.Insight.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.mark_insight_accepted(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, insight.Insight)
    assert response.name == "name_value"
    assert response.description == "description_value"
    assert response.target_resources == ["target_resources_value"]
    assert response.insight_subtype == "insight_subtype_value"
    assert response.category == insight.Insight.Category.COST
    assert response.severity == insight.Insight.Severity.LOW
    assert response.etag == "etag_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_mark_insight_accepted_rest_interceptors(null_interceptor):
    transport = transports.RecommenderRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.RecommenderRestInterceptor(),
    )
    client = RecommenderClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.RecommenderRestInterceptor, "post_mark_insight_accepted"
        ) as post,
        mock.patch.object(
            transports.RecommenderRestInterceptor,
            "post_mark_insight_accepted_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.RecommenderRestInterceptor, "pre_mark_insight_accepted"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = recommender_service.MarkInsightAcceptedRequest.pb(
            recommender_service.MarkInsightAcceptedRequest()
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
        return_value = insight.Insight.to_json(insight.Insight())
        req.return_value.content = return_value

        request = recommender_service.MarkInsightAcceptedRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = insight.Insight()
        post_with_metadata.return_value = insight.Insight(), metadata

        client.mark_insight_accepted(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_list_recommendations_rest_bad_request(
    request_type=recommender_service.ListRecommendationsRequest,
):
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1/locations/sample2/recommenders/sample3"}
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
        client.list_recommendations(request)


@pytest.mark.parametrize(
    "request_type",
    [
        recommender_service.ListRecommendationsRequest,
        dict,
    ],
)
def test_list_recommendations_rest_call_success(request_type):
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1/locations/sample2/recommenders/sample3"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = recommender_service.ListRecommendationsResponse(
            next_page_token="next_page_token_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = recommender_service.ListRecommendationsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.list_recommendations(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListRecommendationsPager)
    assert response.next_page_token == "next_page_token_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_list_recommendations_rest_interceptors(null_interceptor):
    transport = transports.RecommenderRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.RecommenderRestInterceptor(),
    )
    client = RecommenderClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.RecommenderRestInterceptor, "post_list_recommendations"
        ) as post,
        mock.patch.object(
            transports.RecommenderRestInterceptor,
            "post_list_recommendations_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.RecommenderRestInterceptor, "pre_list_recommendations"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = recommender_service.ListRecommendationsRequest.pb(
            recommender_service.ListRecommendationsRequest()
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
        return_value = recommender_service.ListRecommendationsResponse.to_json(
            recommender_service.ListRecommendationsResponse()
        )
        req.return_value.content = return_value

        request = recommender_service.ListRecommendationsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = recommender_service.ListRecommendationsResponse()
        post_with_metadata.return_value = (
            recommender_service.ListRecommendationsResponse(),
            metadata,
        )

        client.list_recommendations(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_get_recommendation_rest_bad_request(
    request_type=recommender_service.GetRecommendationRequest,
):
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/recommenders/sample3/recommendations/sample4"
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
        client.get_recommendation(request)


@pytest.mark.parametrize(
    "request_type",
    [
        recommender_service.GetRecommendationRequest,
        dict,
    ],
)
def test_get_recommendation_rest_call_success(request_type):
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/recommenders/sample3/recommendations/sample4"
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = recommendation.Recommendation(
            name="name_value",
            description="description_value",
            recommender_subtype="recommender_subtype_value",
            priority=recommendation.Recommendation.Priority.P4,
            etag="etag_value",
            xor_group_id="xor_group_id_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = recommendation.Recommendation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.get_recommendation(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, recommendation.Recommendation)
    assert response.name == "name_value"
    assert response.description == "description_value"
    assert response.recommender_subtype == "recommender_subtype_value"
    assert response.priority == recommendation.Recommendation.Priority.P4
    assert response.etag == "etag_value"
    assert response.xor_group_id == "xor_group_id_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_get_recommendation_rest_interceptors(null_interceptor):
    transport = transports.RecommenderRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.RecommenderRestInterceptor(),
    )
    client = RecommenderClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.RecommenderRestInterceptor, "post_get_recommendation"
        ) as post,
        mock.patch.object(
            transports.RecommenderRestInterceptor,
            "post_get_recommendation_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.RecommenderRestInterceptor, "pre_get_recommendation"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = recommender_service.GetRecommendationRequest.pb(
            recommender_service.GetRecommendationRequest()
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
        return_value = recommendation.Recommendation.to_json(
            recommendation.Recommendation()
        )
        req.return_value.content = return_value

        request = recommender_service.GetRecommendationRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = recommendation.Recommendation()
        post_with_metadata.return_value = recommendation.Recommendation(), metadata

        client.get_recommendation(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_mark_recommendation_claimed_rest_bad_request(
    request_type=recommender_service.MarkRecommendationClaimedRequest,
):
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/recommenders/sample3/recommendations/sample4"
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
        client.mark_recommendation_claimed(request)


@pytest.mark.parametrize(
    "request_type",
    [
        recommender_service.MarkRecommendationClaimedRequest,
        dict,
    ],
)
def test_mark_recommendation_claimed_rest_call_success(request_type):
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/recommenders/sample3/recommendations/sample4"
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = recommendation.Recommendation(
            name="name_value",
            description="description_value",
            recommender_subtype="recommender_subtype_value",
            priority=recommendation.Recommendation.Priority.P4,
            etag="etag_value",
            xor_group_id="xor_group_id_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = recommendation.Recommendation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.mark_recommendation_claimed(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, recommendation.Recommendation)
    assert response.name == "name_value"
    assert response.description == "description_value"
    assert response.recommender_subtype == "recommender_subtype_value"
    assert response.priority == recommendation.Recommendation.Priority.P4
    assert response.etag == "etag_value"
    assert response.xor_group_id == "xor_group_id_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_mark_recommendation_claimed_rest_interceptors(null_interceptor):
    transport = transports.RecommenderRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.RecommenderRestInterceptor(),
    )
    client = RecommenderClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.RecommenderRestInterceptor, "post_mark_recommendation_claimed"
        ) as post,
        mock.patch.object(
            transports.RecommenderRestInterceptor,
            "post_mark_recommendation_claimed_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.RecommenderRestInterceptor, "pre_mark_recommendation_claimed"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = recommender_service.MarkRecommendationClaimedRequest.pb(
            recommender_service.MarkRecommendationClaimedRequest()
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
        return_value = recommendation.Recommendation.to_json(
            recommendation.Recommendation()
        )
        req.return_value.content = return_value

        request = recommender_service.MarkRecommendationClaimedRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = recommendation.Recommendation()
        post_with_metadata.return_value = recommendation.Recommendation(), metadata

        client.mark_recommendation_claimed(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_mark_recommendation_succeeded_rest_bad_request(
    request_type=recommender_service.MarkRecommendationSucceededRequest,
):
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/recommenders/sample3/recommendations/sample4"
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
        client.mark_recommendation_succeeded(request)


@pytest.mark.parametrize(
    "request_type",
    [
        recommender_service.MarkRecommendationSucceededRequest,
        dict,
    ],
)
def test_mark_recommendation_succeeded_rest_call_success(request_type):
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/recommenders/sample3/recommendations/sample4"
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = recommendation.Recommendation(
            name="name_value",
            description="description_value",
            recommender_subtype="recommender_subtype_value",
            priority=recommendation.Recommendation.Priority.P4,
            etag="etag_value",
            xor_group_id="xor_group_id_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = recommendation.Recommendation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.mark_recommendation_succeeded(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, recommendation.Recommendation)
    assert response.name == "name_value"
    assert response.description == "description_value"
    assert response.recommender_subtype == "recommender_subtype_value"
    assert response.priority == recommendation.Recommendation.Priority.P4
    assert response.etag == "etag_value"
    assert response.xor_group_id == "xor_group_id_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_mark_recommendation_succeeded_rest_interceptors(null_interceptor):
    transport = transports.RecommenderRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.RecommenderRestInterceptor(),
    )
    client = RecommenderClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.RecommenderRestInterceptor, "post_mark_recommendation_succeeded"
        ) as post,
        mock.patch.object(
            transports.RecommenderRestInterceptor,
            "post_mark_recommendation_succeeded_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.RecommenderRestInterceptor, "pre_mark_recommendation_succeeded"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = recommender_service.MarkRecommendationSucceededRequest.pb(
            recommender_service.MarkRecommendationSucceededRequest()
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
        return_value = recommendation.Recommendation.to_json(
            recommendation.Recommendation()
        )
        req.return_value.content = return_value

        request = recommender_service.MarkRecommendationSucceededRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = recommendation.Recommendation()
        post_with_metadata.return_value = recommendation.Recommendation(), metadata

        client.mark_recommendation_succeeded(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_mark_recommendation_failed_rest_bad_request(
    request_type=recommender_service.MarkRecommendationFailedRequest,
):
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/recommenders/sample3/recommendations/sample4"
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
        client.mark_recommendation_failed(request)


@pytest.mark.parametrize(
    "request_type",
    [
        recommender_service.MarkRecommendationFailedRequest,
        dict,
    ],
)
def test_mark_recommendation_failed_rest_call_success(request_type):
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/recommenders/sample3/recommendations/sample4"
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = recommendation.Recommendation(
            name="name_value",
            description="description_value",
            recommender_subtype="recommender_subtype_value",
            priority=recommendation.Recommendation.Priority.P4,
            etag="etag_value",
            xor_group_id="xor_group_id_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = recommendation.Recommendation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.mark_recommendation_failed(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, recommendation.Recommendation)
    assert response.name == "name_value"
    assert response.description == "description_value"
    assert response.recommender_subtype == "recommender_subtype_value"
    assert response.priority == recommendation.Recommendation.Priority.P4
    assert response.etag == "etag_value"
    assert response.xor_group_id == "xor_group_id_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_mark_recommendation_failed_rest_interceptors(null_interceptor):
    transport = transports.RecommenderRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.RecommenderRestInterceptor(),
    )
    client = RecommenderClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.RecommenderRestInterceptor, "post_mark_recommendation_failed"
        ) as post,
        mock.patch.object(
            transports.RecommenderRestInterceptor,
            "post_mark_recommendation_failed_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.RecommenderRestInterceptor, "pre_mark_recommendation_failed"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = recommender_service.MarkRecommendationFailedRequest.pb(
            recommender_service.MarkRecommendationFailedRequest()
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
        return_value = recommendation.Recommendation.to_json(
            recommendation.Recommendation()
        )
        req.return_value.content = return_value

        request = recommender_service.MarkRecommendationFailedRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = recommendation.Recommendation()
        post_with_metadata.return_value = recommendation.Recommendation(), metadata

        client.mark_recommendation_failed(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_get_recommender_config_rest_bad_request(
    request_type=recommender_service.GetRecommenderConfigRequest,
):
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/recommenders/sample3/config"
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
        client.get_recommender_config(request)


@pytest.mark.parametrize(
    "request_type",
    [
        recommender_service.GetRecommenderConfigRequest,
        dict,
    ],
)
def test_get_recommender_config_rest_call_success(request_type):
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/recommenders/sample3/config"
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = recommender_config.RecommenderConfig(
            name="name_value",
            etag="etag_value",
            revision_id="revision_id_value",
            display_name="display_name_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = recommender_config.RecommenderConfig.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.get_recommender_config(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, recommender_config.RecommenderConfig)
    assert response.name == "name_value"
    assert response.etag == "etag_value"
    assert response.revision_id == "revision_id_value"
    assert response.display_name == "display_name_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_get_recommender_config_rest_interceptors(null_interceptor):
    transport = transports.RecommenderRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.RecommenderRestInterceptor(),
    )
    client = RecommenderClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.RecommenderRestInterceptor, "post_get_recommender_config"
        ) as post,
        mock.patch.object(
            transports.RecommenderRestInterceptor,
            "post_get_recommender_config_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.RecommenderRestInterceptor, "pre_get_recommender_config"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = recommender_service.GetRecommenderConfigRequest.pb(
            recommender_service.GetRecommenderConfigRequest()
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
        return_value = recommender_config.RecommenderConfig.to_json(
            recommender_config.RecommenderConfig()
        )
        req.return_value.content = return_value

        request = recommender_service.GetRecommenderConfigRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = recommender_config.RecommenderConfig()
        post_with_metadata.return_value = (
            recommender_config.RecommenderConfig(),
            metadata,
        )

        client.get_recommender_config(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_update_recommender_config_rest_bad_request(
    request_type=recommender_service.UpdateRecommenderConfigRequest,
):
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {
        "recommender_config": {
            "name": "projects/sample1/locations/sample2/recommenders/sample3/config"
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
        client.update_recommender_config(request)


@pytest.mark.parametrize(
    "request_type",
    [
        recommender_service.UpdateRecommenderConfigRequest,
        dict,
    ],
)
def test_update_recommender_config_rest_call_success(request_type):
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {
        "recommender_config": {
            "name": "projects/sample1/locations/sample2/recommenders/sample3/config"
        }
    }
    request_init["recommender_config"] = {
        "name": "projects/sample1/locations/sample2/recommenders/sample3/config",
        "recommender_generation_config": {"params": {"fields": {}}},
        "etag": "etag_value",
        "update_time": {"seconds": 751, "nanos": 543},
        "revision_id": "revision_id_value",
        "annotations": {},
        "display_name": "display_name_value",
    }
    # The version of a generated dependency at test runtime may differ from the version used during generation.
    # Delete any fields which are not present in the current runtime dependency
    # See https://github.com/googleapis/gapic-generator-python/issues/1748

    # Determine if the message type is proto-plus or protobuf
    test_field = recommender_service.UpdateRecommenderConfigRequest.meta.fields[
        "recommender_config"
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
    for field, value in request_init["recommender_config"].items():  # pragma: NO COVER
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
                for i in range(0, len(request_init["recommender_config"][field])):
                    del request_init["recommender_config"][field][i][subfield]
            else:
                del request_init["recommender_config"][field][subfield]
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = gcr_recommender_config.RecommenderConfig(
            name="name_value",
            etag="etag_value",
            revision_id="revision_id_value",
            display_name="display_name_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = gcr_recommender_config.RecommenderConfig.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.update_recommender_config(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, gcr_recommender_config.RecommenderConfig)
    assert response.name == "name_value"
    assert response.etag == "etag_value"
    assert response.revision_id == "revision_id_value"
    assert response.display_name == "display_name_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_update_recommender_config_rest_interceptors(null_interceptor):
    transport = transports.RecommenderRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.RecommenderRestInterceptor(),
    )
    client = RecommenderClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.RecommenderRestInterceptor, "post_update_recommender_config"
        ) as post,
        mock.patch.object(
            transports.RecommenderRestInterceptor,
            "post_update_recommender_config_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.RecommenderRestInterceptor, "pre_update_recommender_config"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = recommender_service.UpdateRecommenderConfigRequest.pb(
            recommender_service.UpdateRecommenderConfigRequest()
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
        return_value = gcr_recommender_config.RecommenderConfig.to_json(
            gcr_recommender_config.RecommenderConfig()
        )
        req.return_value.content = return_value

        request = recommender_service.UpdateRecommenderConfigRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = gcr_recommender_config.RecommenderConfig()
        post_with_metadata.return_value = (
            gcr_recommender_config.RecommenderConfig(),
            metadata,
        )

        client.update_recommender_config(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_get_insight_type_config_rest_bad_request(
    request_type=recommender_service.GetInsightTypeConfigRequest,
):
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/insightTypes/sample3/config"
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
        client.get_insight_type_config(request)


@pytest.mark.parametrize(
    "request_type",
    [
        recommender_service.GetInsightTypeConfigRequest,
        dict,
    ],
)
def test_get_insight_type_config_rest_call_success(request_type):
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/insightTypes/sample3/config"
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = insight_type_config.InsightTypeConfig(
            name="name_value",
            etag="etag_value",
            revision_id="revision_id_value",
            display_name="display_name_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = insight_type_config.InsightTypeConfig.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.get_insight_type_config(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, insight_type_config.InsightTypeConfig)
    assert response.name == "name_value"
    assert response.etag == "etag_value"
    assert response.revision_id == "revision_id_value"
    assert response.display_name == "display_name_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_get_insight_type_config_rest_interceptors(null_interceptor):
    transport = transports.RecommenderRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.RecommenderRestInterceptor(),
    )
    client = RecommenderClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.RecommenderRestInterceptor, "post_get_insight_type_config"
        ) as post,
        mock.patch.object(
            transports.RecommenderRestInterceptor,
            "post_get_insight_type_config_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.RecommenderRestInterceptor, "pre_get_insight_type_config"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = recommender_service.GetInsightTypeConfigRequest.pb(
            recommender_service.GetInsightTypeConfigRequest()
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
        return_value = insight_type_config.InsightTypeConfig.to_json(
            insight_type_config.InsightTypeConfig()
        )
        req.return_value.content = return_value

        request = recommender_service.GetInsightTypeConfigRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = insight_type_config.InsightTypeConfig()
        post_with_metadata.return_value = (
            insight_type_config.InsightTypeConfig(),
            metadata,
        )

        client.get_insight_type_config(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_update_insight_type_config_rest_bad_request(
    request_type=recommender_service.UpdateInsightTypeConfigRequest,
):
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {
        "insight_type_config": {
            "name": "projects/sample1/locations/sample2/insightTypes/sample3/config"
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
        client.update_insight_type_config(request)


@pytest.mark.parametrize(
    "request_type",
    [
        recommender_service.UpdateInsightTypeConfigRequest,
        dict,
    ],
)
def test_update_insight_type_config_rest_call_success(request_type):
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {
        "insight_type_config": {
            "name": "projects/sample1/locations/sample2/insightTypes/sample3/config"
        }
    }
    request_init["insight_type_config"] = {
        "name": "projects/sample1/locations/sample2/insightTypes/sample3/config",
        "insight_type_generation_config": {"params": {"fields": {}}},
        "etag": "etag_value",
        "update_time": {"seconds": 751, "nanos": 543},
        "revision_id": "revision_id_value",
        "annotations": {},
        "display_name": "display_name_value",
    }
    # The version of a generated dependency at test runtime may differ from the version used during generation.
    # Delete any fields which are not present in the current runtime dependency
    # See https://github.com/googleapis/gapic-generator-python/issues/1748

    # Determine if the message type is proto-plus or protobuf
    test_field = recommender_service.UpdateInsightTypeConfigRequest.meta.fields[
        "insight_type_config"
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
    for field, value in request_init["insight_type_config"].items():  # pragma: NO COVER
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
                for i in range(0, len(request_init["insight_type_config"][field])):
                    del request_init["insight_type_config"][field][i][subfield]
            else:
                del request_init["insight_type_config"][field][subfield]
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = gcr_insight_type_config.InsightTypeConfig(
            name="name_value",
            etag="etag_value",
            revision_id="revision_id_value",
            display_name="display_name_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = gcr_insight_type_config.InsightTypeConfig.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.update_insight_type_config(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, gcr_insight_type_config.InsightTypeConfig)
    assert response.name == "name_value"
    assert response.etag == "etag_value"
    assert response.revision_id == "revision_id_value"
    assert response.display_name == "display_name_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_update_insight_type_config_rest_interceptors(null_interceptor):
    transport = transports.RecommenderRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.RecommenderRestInterceptor(),
    )
    client = RecommenderClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.RecommenderRestInterceptor, "post_update_insight_type_config"
        ) as post,
        mock.patch.object(
            transports.RecommenderRestInterceptor,
            "post_update_insight_type_config_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.RecommenderRestInterceptor, "pre_update_insight_type_config"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = recommender_service.UpdateInsightTypeConfigRequest.pb(
            recommender_service.UpdateInsightTypeConfigRequest()
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
        return_value = gcr_insight_type_config.InsightTypeConfig.to_json(
            gcr_insight_type_config.InsightTypeConfig()
        )
        req.return_value.content = return_value

        request = recommender_service.UpdateInsightTypeConfigRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = gcr_insight_type_config.InsightTypeConfig()
        post_with_metadata.return_value = (
            gcr_insight_type_config.InsightTypeConfig(),
            metadata,
        )

        client.update_insight_type_config(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_list_recommenders_rest_bad_request(
    request_type=recommender_service.ListRecommendersRequest,
):
    client = RecommenderClient(
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
        client.list_recommenders(request)


@pytest.mark.parametrize(
    "request_type",
    [
        recommender_service.ListRecommendersRequest,
        dict,
    ],
)
def test_list_recommenders_rest_call_success(request_type):
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = recommender_service.ListRecommendersResponse(
            next_page_token="next_page_token_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = recommender_service.ListRecommendersResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.list_recommenders(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListRecommendersPager)
    assert response.next_page_token == "next_page_token_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_list_recommenders_rest_interceptors(null_interceptor):
    transport = transports.RecommenderRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.RecommenderRestInterceptor(),
    )
    client = RecommenderClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.RecommenderRestInterceptor, "post_list_recommenders"
        ) as post,
        mock.patch.object(
            transports.RecommenderRestInterceptor,
            "post_list_recommenders_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.RecommenderRestInterceptor, "pre_list_recommenders"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = recommender_service.ListRecommendersRequest.pb(
            recommender_service.ListRecommendersRequest()
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
        return_value = recommender_service.ListRecommendersResponse.to_json(
            recommender_service.ListRecommendersResponse()
        )
        req.return_value.content = return_value

        request = recommender_service.ListRecommendersRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = recommender_service.ListRecommendersResponse()
        post_with_metadata.return_value = (
            recommender_service.ListRecommendersResponse(),
            metadata,
        )

        client.list_recommenders(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_list_insight_types_rest_bad_request(
    request_type=recommender_service.ListInsightTypesRequest,
):
    client = RecommenderClient(
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
        client.list_insight_types(request)


@pytest.mark.parametrize(
    "request_type",
    [
        recommender_service.ListInsightTypesRequest,
        dict,
    ],
)
def test_list_insight_types_rest_call_success(request_type):
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = recommender_service.ListInsightTypesResponse(
            next_page_token="next_page_token_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = recommender_service.ListInsightTypesResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.list_insight_types(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListInsightTypesPager)
    assert response.next_page_token == "next_page_token_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_list_insight_types_rest_interceptors(null_interceptor):
    transport = transports.RecommenderRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.RecommenderRestInterceptor(),
    )
    client = RecommenderClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.RecommenderRestInterceptor, "post_list_insight_types"
        ) as post,
        mock.patch.object(
            transports.RecommenderRestInterceptor,
            "post_list_insight_types_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.RecommenderRestInterceptor, "pre_list_insight_types"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = recommender_service.ListInsightTypesRequest.pb(
            recommender_service.ListInsightTypesRequest()
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
        return_value = recommender_service.ListInsightTypesResponse.to_json(
            recommender_service.ListInsightTypesResponse()
        )
        req.return_value.content = return_value

        request = recommender_service.ListInsightTypesRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = recommender_service.ListInsightTypesResponse()
        post_with_metadata.return_value = (
            recommender_service.ListInsightTypesResponse(),
            metadata,
        )

        client.list_insight_types(
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
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    assert client is not None


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_insights_empty_call_rest():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.list_insights), "__call__") as call:
        client.list_insights(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = recommender_service.ListInsightsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_insight_empty_call_rest():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_insight), "__call__") as call:
        client.get_insight(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = recommender_service.GetInsightRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_mark_insight_accepted_empty_call_rest():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.mark_insight_accepted), "__call__"
    ) as call:
        client.mark_insight_accepted(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = recommender_service.MarkInsightAcceptedRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_recommendations_empty_call_rest():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_recommendations), "__call__"
    ) as call:
        client.list_recommendations(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = recommender_service.ListRecommendationsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_recommendation_empty_call_rest():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.get_recommendation), "__call__"
    ) as call:
        client.get_recommendation(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = recommender_service.GetRecommendationRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_mark_recommendation_claimed_empty_call_rest():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.mark_recommendation_claimed), "__call__"
    ) as call:
        client.mark_recommendation_claimed(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = recommender_service.MarkRecommendationClaimedRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_mark_recommendation_succeeded_empty_call_rest():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.mark_recommendation_succeeded), "__call__"
    ) as call:
        client.mark_recommendation_succeeded(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = recommender_service.MarkRecommendationSucceededRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_mark_recommendation_failed_empty_call_rest():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.mark_recommendation_failed), "__call__"
    ) as call:
        client.mark_recommendation_failed(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = recommender_service.MarkRecommendationFailedRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_recommender_config_empty_call_rest():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.get_recommender_config), "__call__"
    ) as call:
        client.get_recommender_config(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = recommender_service.GetRecommenderConfigRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_update_recommender_config_empty_call_rest():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.update_recommender_config), "__call__"
    ) as call:
        client.update_recommender_config(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = recommender_service.UpdateRecommenderConfigRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_insight_type_config_empty_call_rest():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.get_insight_type_config), "__call__"
    ) as call:
        client.get_insight_type_config(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = recommender_service.GetInsightTypeConfigRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_update_insight_type_config_empty_call_rest():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.update_insight_type_config), "__call__"
    ) as call:
        client.update_insight_type_config(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = recommender_service.UpdateInsightTypeConfigRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_recommenders_empty_call_rest():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_recommenders), "__call__"
    ) as call:
        client.list_recommenders(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = recommender_service.ListRecommendersRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_insight_types_empty_call_rest():
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_insight_types), "__call__"
    ) as call:
        client.list_insight_types(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = recommender_service.ListInsightTypesRequest()
        assert args[0] == request_msg


def test_transport_grpc_default():
    # A client should use the gRPC transport by default.
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    assert isinstance(
        client.transport,
        transports.RecommenderGrpcTransport,
    )


def test_recommender_base_transport_error():
    # Passing both a credentials object and credentials_file should raise an error
    with pytest.raises(core_exceptions.DuplicateCredentialArgs):
        transport = transports.RecommenderTransport(
            credentials=ga_credentials.AnonymousCredentials(),
            credentials_file="credentials.json",
        )


def test_recommender_base_transport():
    # Instantiate the base transport.
    with mock.patch(
        "google.cloud.recommender_v1beta1.services.recommender.transports.RecommenderTransport.__init__"
    ) as Transport:
        Transport.return_value = None
        transport = transports.RecommenderTransport(
            credentials=ga_credentials.AnonymousCredentials(),
        )

    # Every method on the transport should just blindly
    # raise NotImplementedError.
    methods = (
        "list_insights",
        "get_insight",
        "mark_insight_accepted",
        "list_recommendations",
        "get_recommendation",
        "mark_recommendation_claimed",
        "mark_recommendation_succeeded",
        "mark_recommendation_failed",
        "get_recommender_config",
        "update_recommender_config",
        "get_insight_type_config",
        "update_insight_type_config",
        "list_recommenders",
        "list_insight_types",
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


def test_recommender_base_transport_with_credentials_file():
    # Instantiate the base transport with a credentials file
    with (
        mock.patch.object(
            google.auth, "load_credentials_from_file", autospec=True
        ) as load_creds,
        mock.patch(
            "google.cloud.recommender_v1beta1.services.recommender.transports.RecommenderTransport._prep_wrapped_messages"
        ) as Transport,
    ):
        Transport.return_value = None
        load_creds.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.RecommenderTransport(
            credentials_file="credentials.json",
            quota_project_id="octopus",
        )
        load_creds.assert_called_once_with(
            "credentials.json",
            scopes=None,
            default_scopes=("https://www.googleapis.com/auth/cloud-platform",),
            quota_project_id="octopus",
        )


def test_recommender_base_transport_with_adc():
    # Test the default credentials are used if credentials and credentials_file are None.
    with (
        mock.patch.object(google.auth, "default", autospec=True) as adc,
        mock.patch(
            "google.cloud.recommender_v1beta1.services.recommender.transports.RecommenderTransport._prep_wrapped_messages"
        ) as Transport,
    ):
        Transport.return_value = None
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.RecommenderTransport()
        adc.assert_called_once()


def test_recommender_auth_adc():
    # If no credentials are provided, we should use ADC credentials.
    with mock.patch.object(google.auth, "default", autospec=True) as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        RecommenderClient()
        adc.assert_called_once_with(
            scopes=None,
            default_scopes=("https://www.googleapis.com/auth/cloud-platform",),
            quota_project_id=None,
        )


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.RecommenderGrpcTransport,
        transports.RecommenderGrpcAsyncIOTransport,
    ],
)
def test_recommender_transport_auth_adc(transport_class):
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
        transports.RecommenderGrpcTransport,
        transports.RecommenderGrpcAsyncIOTransport,
        transports.RecommenderRestTransport,
    ],
)
def test_recommender_transport_auth_gdch_credentials(transport_class):
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
        (transports.RecommenderGrpcTransport, grpc_helpers),
        (transports.RecommenderGrpcAsyncIOTransport, grpc_helpers_async),
    ],
)
def test_recommender_transport_create_channel(transport_class, grpc_helpers):
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
            "recommender.googleapis.com:443",
            credentials=creds,
            credentials_file=None,
            quota_project_id="octopus",
            default_scopes=("https://www.googleapis.com/auth/cloud-platform",),
            scopes=["1", "2"],
            default_host="recommender.googleapis.com",
            ssl_credentials=None,
            options=[
                ("grpc.max_send_message_length", -1),
                ("grpc.max_receive_message_length", -1),
            ],
        )


@pytest.mark.parametrize(
    "transport_class",
    [transports.RecommenderGrpcTransport, transports.RecommenderGrpcAsyncIOTransport],
)
def test_recommender_grpc_transport_client_cert_source_for_mtls(transport_class):
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


def test_recommender_http_transport_client_cert_source_for_mtls():
    cred = ga_credentials.AnonymousCredentials()
    with mock.patch(
        "google.auth.transport.requests.AuthorizedSession.configure_mtls_channel"
    ) as mock_configure_mtls_channel:
        transports.RecommenderRestTransport(
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
def test_recommender_host_no_port(transport_name):
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(
            api_endpoint="recommender.googleapis.com"
        ),
        transport=transport_name,
    )
    assert client.transport._host == (
        "recommender.googleapis.com:443"
        if transport_name in ["grpc", "grpc_asyncio"]
        else "https://recommender.googleapis.com"
    )


@pytest.mark.parametrize(
    "transport_name",
    [
        "grpc",
        "grpc_asyncio",
        "rest",
    ],
)
def test_recommender_host_with_port(transport_name):
    client = RecommenderClient(
        credentials=ga_credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(
            api_endpoint="recommender.googleapis.com:8000"
        ),
        transport=transport_name,
    )
    assert client.transport._host == (
        "recommender.googleapis.com:8000"
        if transport_name in ["grpc", "grpc_asyncio"]
        else "https://recommender.googleapis.com:8000"
    )


@pytest.mark.parametrize(
    "transport_name",
    [
        "rest",
    ],
)
def test_recommender_client_transport_session_collision(transport_name):
    creds1 = ga_credentials.AnonymousCredentials()
    creds2 = ga_credentials.AnonymousCredentials()
    client1 = RecommenderClient(
        credentials=creds1,
        transport=transport_name,
    )
    client2 = RecommenderClient(
        credentials=creds2,
        transport=transport_name,
    )
    session1 = client1.transport.list_insights._session
    session2 = client2.transport.list_insights._session
    assert session1 != session2
    session1 = client1.transport.get_insight._session
    session2 = client2.transport.get_insight._session
    assert session1 != session2
    session1 = client1.transport.mark_insight_accepted._session
    session2 = client2.transport.mark_insight_accepted._session
    assert session1 != session2
    session1 = client1.transport.list_recommendations._session
    session2 = client2.transport.list_recommendations._session
    assert session1 != session2
    session1 = client1.transport.get_recommendation._session
    session2 = client2.transport.get_recommendation._session
    assert session1 != session2
    session1 = client1.transport.mark_recommendation_claimed._session
    session2 = client2.transport.mark_recommendation_claimed._session
    assert session1 != session2
    session1 = client1.transport.mark_recommendation_succeeded._session
    session2 = client2.transport.mark_recommendation_succeeded._session
    assert session1 != session2
    session1 = client1.transport.mark_recommendation_failed._session
    session2 = client2.transport.mark_recommendation_failed._session
    assert session1 != session2
    session1 = client1.transport.get_recommender_config._session
    session2 = client2.transport.get_recommender_config._session
    assert session1 != session2
    session1 = client1.transport.update_recommender_config._session
    session2 = client2.transport.update_recommender_config._session
    assert session1 != session2
    session1 = client1.transport.get_insight_type_config._session
    session2 = client2.transport.get_insight_type_config._session
    assert session1 != session2
    session1 = client1.transport.update_insight_type_config._session
    session2 = client2.transport.update_insight_type_config._session
    assert session1 != session2
    session1 = client1.transport.list_recommenders._session
    session2 = client2.transport.list_recommenders._session
    assert session1 != session2
    session1 = client1.transport.list_insight_types._session
    session2 = client2.transport.list_insight_types._session
    assert session1 != session2


def test_recommender_grpc_transport_channel():
    channel = grpc.secure_channel("http://localhost/", grpc.local_channel_credentials())

    # Check that channel is used if provided.
    transport = transports.RecommenderGrpcTransport(
        host="squid.clam.whelk",
        channel=channel,
    )
    assert transport.grpc_channel == channel
    assert transport._host == "squid.clam.whelk:443"
    assert transport._ssl_channel_credentials == None


def test_recommender_grpc_asyncio_transport_channel():
    channel = aio.secure_channel("http://localhost/", grpc.local_channel_credentials())

    # Check that channel is used if provided.
    transport = transports.RecommenderGrpcAsyncIOTransport(
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
    [transports.RecommenderGrpcTransport, transports.RecommenderGrpcAsyncIOTransport],
)
def test_recommender_transport_channel_mtls_with_client_cert_source(transport_class):
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
    [transports.RecommenderGrpcTransport, transports.RecommenderGrpcAsyncIOTransport],
)
def test_recommender_transport_channel_mtls_with_adc(transport_class):
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


def test_insight_path():
    project = "squid"
    location = "clam"
    insight_type = "whelk"
    insight = "octopus"
    expected = "projects/{project}/locations/{location}/insightTypes/{insight_type}/insights/{insight}".format(
        project=project,
        location=location,
        insight_type=insight_type,
        insight=insight,
    )
    actual = RecommenderClient.insight_path(project, location, insight_type, insight)
    assert expected == actual


def test_parse_insight_path():
    expected = {
        "project": "oyster",
        "location": "nudibranch",
        "insight_type": "cuttlefish",
        "insight": "mussel",
    }
    path = RecommenderClient.insight_path(**expected)

    # Check that the path construction is reversible.
    actual = RecommenderClient.parse_insight_path(path)
    assert expected == actual


def test_insight_type_path():
    project = "winkle"
    location = "nautilus"
    insight_type = "scallop"
    expected = (
        "projects/{project}/locations/{location}/insightTypes/{insight_type}".format(
            project=project,
            location=location,
            insight_type=insight_type,
        )
    )
    actual = RecommenderClient.insight_type_path(project, location, insight_type)
    assert expected == actual


def test_parse_insight_type_path():
    expected = {
        "project": "abalone",
        "location": "squid",
        "insight_type": "clam",
    }
    path = RecommenderClient.insight_type_path(**expected)

    # Check that the path construction is reversible.
    actual = RecommenderClient.parse_insight_type_path(path)
    assert expected == actual


def test_insight_type_config_path():
    project = "whelk"
    location = "octopus"
    insight_type = "oyster"
    expected = "projects/{project}/locations/{location}/insightTypes/{insight_type}/config".format(
        project=project,
        location=location,
        insight_type=insight_type,
    )
    actual = RecommenderClient.insight_type_config_path(project, location, insight_type)
    assert expected == actual


def test_parse_insight_type_config_path():
    expected = {
        "project": "nudibranch",
        "location": "cuttlefish",
        "insight_type": "mussel",
    }
    path = RecommenderClient.insight_type_config_path(**expected)

    # Check that the path construction is reversible.
    actual = RecommenderClient.parse_insight_type_config_path(path)
    assert expected == actual


def test_recommendation_path():
    project = "winkle"
    location = "nautilus"
    recommender = "scallop"
    recommendation = "abalone"
    expected = "projects/{project}/locations/{location}/recommenders/{recommender}/recommendations/{recommendation}".format(
        project=project,
        location=location,
        recommender=recommender,
        recommendation=recommendation,
    )
    actual = RecommenderClient.recommendation_path(
        project, location, recommender, recommendation
    )
    assert expected == actual


def test_parse_recommendation_path():
    expected = {
        "project": "squid",
        "location": "clam",
        "recommender": "whelk",
        "recommendation": "octopus",
    }
    path = RecommenderClient.recommendation_path(**expected)

    # Check that the path construction is reversible.
    actual = RecommenderClient.parse_recommendation_path(path)
    assert expected == actual


def test_recommender_path():
    project = "oyster"
    location = "nudibranch"
    recommender = "cuttlefish"
    expected = (
        "projects/{project}/locations/{location}/recommenders/{recommender}".format(
            project=project,
            location=location,
            recommender=recommender,
        )
    )
    actual = RecommenderClient.recommender_path(project, location, recommender)
    assert expected == actual


def test_parse_recommender_path():
    expected = {
        "project": "mussel",
        "location": "winkle",
        "recommender": "nautilus",
    }
    path = RecommenderClient.recommender_path(**expected)

    # Check that the path construction is reversible.
    actual = RecommenderClient.parse_recommender_path(path)
    assert expected == actual


def test_recommender_config_path():
    project = "scallop"
    location = "abalone"
    recommender = "squid"
    expected = "projects/{project}/locations/{location}/recommenders/{recommender}/config".format(
        project=project,
        location=location,
        recommender=recommender,
    )
    actual = RecommenderClient.recommender_config_path(project, location, recommender)
    assert expected == actual


def test_parse_recommender_config_path():
    expected = {
        "project": "clam",
        "location": "whelk",
        "recommender": "octopus",
    }
    path = RecommenderClient.recommender_config_path(**expected)

    # Check that the path construction is reversible.
    actual = RecommenderClient.parse_recommender_config_path(path)
    assert expected == actual


def test_common_billing_account_path():
    billing_account = "oyster"
    expected = "billingAccounts/{billing_account}".format(
        billing_account=billing_account,
    )
    actual = RecommenderClient.common_billing_account_path(billing_account)
    assert expected == actual


def test_parse_common_billing_account_path():
    expected = {
        "billing_account": "nudibranch",
    }
    path = RecommenderClient.common_billing_account_path(**expected)

    # Check that the path construction is reversible.
    actual = RecommenderClient.parse_common_billing_account_path(path)
    assert expected == actual


def test_common_folder_path():
    folder = "cuttlefish"
    expected = "folders/{folder}".format(
        folder=folder,
    )
    actual = RecommenderClient.common_folder_path(folder)
    assert expected == actual


def test_parse_common_folder_path():
    expected = {
        "folder": "mussel",
    }
    path = RecommenderClient.common_folder_path(**expected)

    # Check that the path construction is reversible.
    actual = RecommenderClient.parse_common_folder_path(path)
    assert expected == actual


def test_common_organization_path():
    organization = "winkle"
    expected = "organizations/{organization}".format(
        organization=organization,
    )
    actual = RecommenderClient.common_organization_path(organization)
    assert expected == actual


def test_parse_common_organization_path():
    expected = {
        "organization": "nautilus",
    }
    path = RecommenderClient.common_organization_path(**expected)

    # Check that the path construction is reversible.
    actual = RecommenderClient.parse_common_organization_path(path)
    assert expected == actual


def test_common_project_path():
    project = "scallop"
    expected = "projects/{project}".format(
        project=project,
    )
    actual = RecommenderClient.common_project_path(project)
    assert expected == actual


def test_parse_common_project_path():
    expected = {
        "project": "abalone",
    }
    path = RecommenderClient.common_project_path(**expected)

    # Check that the path construction is reversible.
    actual = RecommenderClient.parse_common_project_path(path)
    assert expected == actual


def test_common_location_path():
    project = "squid"
    location = "clam"
    expected = "projects/{project}/locations/{location}".format(
        project=project,
        location=location,
    )
    actual = RecommenderClient.common_location_path(project, location)
    assert expected == actual


def test_parse_common_location_path():
    expected = {
        "project": "whelk",
        "location": "octopus",
    }
    path = RecommenderClient.common_location_path(**expected)

    # Check that the path construction is reversible.
    actual = RecommenderClient.parse_common_location_path(path)
    assert expected == actual


def test_client_with_default_client_info():
    client_info = gapic_v1.client_info.ClientInfo()

    with mock.patch.object(
        transports.RecommenderTransport, "_prep_wrapped_messages"
    ) as prep:
        client = RecommenderClient(
            credentials=ga_credentials.AnonymousCredentials(),
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)

    with mock.patch.object(
        transports.RecommenderTransport, "_prep_wrapped_messages"
    ) as prep:
        transport_class = RecommenderClient.get_transport_class()
        transport = transport_class(
            credentials=ga_credentials.AnonymousCredentials(),
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)


def test_transport_close_grpc():
    client = RecommenderClient(
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
    client = RecommenderAsyncClient(
        credentials=async_anonymous_credentials(), transport="grpc_asyncio"
    )
    with mock.patch.object(
        type(getattr(client.transport, "_grpc_channel")), "close"
    ) as close:
        async with client:
            close.assert_not_called()
        close.assert_called_once()


def test_transport_close_rest():
    client = RecommenderClient(
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
        client = RecommenderClient(
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
        (RecommenderClient, transports.RecommenderGrpcTransport),
        (RecommenderAsyncClient, transports.RecommenderGrpcAsyncIOTransport),
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
