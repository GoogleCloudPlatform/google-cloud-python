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

from google.cloud.osconfig_v1alpha.services.os_config_zonal_service import (
    OsConfigZonalServiceAsyncClient,
    OsConfigZonalServiceClient,
    pagers,
    transports,
)
from google.cloud.osconfig_v1alpha.types import (
    config_common,
    instance_os_policies_compliance,
    inventory,
    os_policy,
    os_policy_assignment_reports,
    os_policy_assignments,
    osconfig_common,
    vulnerability,
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

    assert OsConfigZonalServiceClient._get_client_cert_source(None, False) is None
    assert (
        OsConfigZonalServiceClient._get_client_cert_source(
            mock_provided_cert_source, False
        )
        is None
    )
    assert (
        OsConfigZonalServiceClient._get_client_cert_source(
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
                OsConfigZonalServiceClient._get_client_cert_source(None, True)
                is mock_default_cert_source
            )
            assert (
                OsConfigZonalServiceClient._get_client_cert_source(
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
    client = OsConfigZonalServiceClient(credentials=cred)
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
    client = OsConfigZonalServiceClient(credentials=cred)
    client._transport._credentials = cred

    error = core_exceptions.GoogleAPICallError("message", details=[])
    error.code = error_code

    client._add_cred_info_for_auth_errors(error)
    assert error.details == []


@pytest.mark.parametrize(
    "client_class,transport_name",
    [
        (OsConfigZonalServiceClient, "grpc"),
        (OsConfigZonalServiceAsyncClient, "grpc_asyncio"),
        (OsConfigZonalServiceClient, "rest"),
    ],
)
def test_os_config_zonal_service_client_from_service_account_info(
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
            "osconfig.googleapis.com:443"
            if transport_name in ["grpc", "grpc_asyncio"]
            else "https://osconfig.googleapis.com"
        )


@pytest.mark.parametrize(
    "transport_class,transport_name",
    [
        (transports.OsConfigZonalServiceGrpcTransport, "grpc"),
        (transports.OsConfigZonalServiceGrpcAsyncIOTransport, "grpc_asyncio"),
        (transports.OsConfigZonalServiceRestTransport, "rest"),
    ],
)
def test_os_config_zonal_service_client_service_account_always_use_jwt(
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
        (OsConfigZonalServiceClient, "grpc"),
        (OsConfigZonalServiceAsyncClient, "grpc_asyncio"),
        (OsConfigZonalServiceClient, "rest"),
    ],
)
def test_os_config_zonal_service_client_from_service_account_file(
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
            "osconfig.googleapis.com:443"
            if transport_name in ["grpc", "grpc_asyncio"]
            else "https://osconfig.googleapis.com"
        )


def test_os_config_zonal_service_client_get_transport_class():
    transport = OsConfigZonalServiceClient.get_transport_class()
    available_transports = [
        transports.OsConfigZonalServiceGrpcTransport,
        transports.OsConfigZonalServiceRestTransport,
    ]
    assert transport in available_transports

    transport = OsConfigZonalServiceClient.get_transport_class("grpc")
    assert transport == transports.OsConfigZonalServiceGrpcTransport


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name",
    [
        (
            OsConfigZonalServiceClient,
            transports.OsConfigZonalServiceGrpcTransport,
            "grpc",
        ),
        (
            OsConfigZonalServiceAsyncClient,
            transports.OsConfigZonalServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
        ),
        (
            OsConfigZonalServiceClient,
            transports.OsConfigZonalServiceRestTransport,
            "rest",
        ),
    ],
)
@mock.patch.object(
    OsConfigZonalServiceClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(OsConfigZonalServiceClient),
)
@mock.patch.object(
    OsConfigZonalServiceAsyncClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(OsConfigZonalServiceAsyncClient),
)
def test_os_config_zonal_service_client_client_options(
    client_class, transport_class, transport_name
):
    # Check that if channel is provided we won't create a new one.
    with mock.patch.object(OsConfigZonalServiceClient, "get_transport_class") as gtc:
        transport = transport_class(credentials=ga_credentials.AnonymousCredentials())
        client = client_class(transport=transport)
        gtc.assert_not_called()

    # Check that if channel is provided via str we will create a new one.
    with mock.patch.object(OsConfigZonalServiceClient, "get_transport_class") as gtc:
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
            OsConfigZonalServiceClient,
            transports.OsConfigZonalServiceGrpcTransport,
            "grpc",
            "true",
        ),
        (
            OsConfigZonalServiceAsyncClient,
            transports.OsConfigZonalServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
            "true",
        ),
        (
            OsConfigZonalServiceClient,
            transports.OsConfigZonalServiceGrpcTransport,
            "grpc",
            "false",
        ),
        (
            OsConfigZonalServiceAsyncClient,
            transports.OsConfigZonalServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
            "false",
        ),
        (
            OsConfigZonalServiceClient,
            transports.OsConfigZonalServiceRestTransport,
            "rest",
            "true",
        ),
        (
            OsConfigZonalServiceClient,
            transports.OsConfigZonalServiceRestTransport,
            "rest",
            "false",
        ),
    ],
)
@mock.patch.object(
    OsConfigZonalServiceClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(OsConfigZonalServiceClient),
)
@mock.patch.object(
    OsConfigZonalServiceAsyncClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(OsConfigZonalServiceAsyncClient),
)
@mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "auto"})
def test_os_config_zonal_service_client_mtls_env_auto(
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
    "client_class", [OsConfigZonalServiceClient, OsConfigZonalServiceAsyncClient]
)
@mock.patch.object(
    OsConfigZonalServiceClient,
    "DEFAULT_ENDPOINT",
    modify_default_endpoint(OsConfigZonalServiceClient),
)
@mock.patch.object(
    OsConfigZonalServiceAsyncClient,
    "DEFAULT_ENDPOINT",
    modify_default_endpoint(OsConfigZonalServiceAsyncClient),
)
def test_os_config_zonal_service_client_get_mtls_endpoint_and_cert_source(client_class):
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
    "client_class", [OsConfigZonalServiceClient, OsConfigZonalServiceAsyncClient]
)
@mock.patch.object(
    OsConfigZonalServiceClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(OsConfigZonalServiceClient),
)
@mock.patch.object(
    OsConfigZonalServiceAsyncClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(OsConfigZonalServiceAsyncClient),
)
def test_os_config_zonal_service_client_client_api_endpoint(client_class):
    mock_client_cert_source = client_cert_source_callback
    api_override = "foo.com"
    default_universe = OsConfigZonalServiceClient._DEFAULT_UNIVERSE
    default_endpoint = OsConfigZonalServiceClient._DEFAULT_ENDPOINT_TEMPLATE.format(
        UNIVERSE_DOMAIN=default_universe
    )
    mock_universe = "bar.com"
    mock_endpoint = OsConfigZonalServiceClient._DEFAULT_ENDPOINT_TEMPLATE.format(
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
            OsConfigZonalServiceClient,
            transports.OsConfigZonalServiceGrpcTransport,
            "grpc",
        ),
        (
            OsConfigZonalServiceAsyncClient,
            transports.OsConfigZonalServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
        ),
        (
            OsConfigZonalServiceClient,
            transports.OsConfigZonalServiceRestTransport,
            "rest",
        ),
    ],
)
def test_os_config_zonal_service_client_client_options_scopes(
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
            OsConfigZonalServiceClient,
            transports.OsConfigZonalServiceGrpcTransport,
            "grpc",
            grpc_helpers,
        ),
        (
            OsConfigZonalServiceAsyncClient,
            transports.OsConfigZonalServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
            grpc_helpers_async,
        ),
        (
            OsConfigZonalServiceClient,
            transports.OsConfigZonalServiceRestTransport,
            "rest",
            None,
        ),
    ],
)
def test_os_config_zonal_service_client_client_options_credentials_file(
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


def test_os_config_zonal_service_client_client_options_from_dict():
    with mock.patch(
        "google.cloud.osconfig_v1alpha.services.os_config_zonal_service.transports.OsConfigZonalServiceGrpcTransport.__init__"
    ) as grpc_transport:
        grpc_transport.return_value = None
        client = OsConfigZonalServiceClient(
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
            OsConfigZonalServiceClient,
            transports.OsConfigZonalServiceGrpcTransport,
            "grpc",
            grpc_helpers,
        ),
        (
            OsConfigZonalServiceAsyncClient,
            transports.OsConfigZonalServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
            grpc_helpers_async,
        ),
    ],
)
def test_os_config_zonal_service_client_create_channel_credentials_file(
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
            "osconfig.googleapis.com:443",
            credentials=file_creds,
            credentials_file=None,
            quota_project_id=None,
            default_scopes=("https://www.googleapis.com/auth/cloud-platform",),
            scopes=None,
            default_host="osconfig.googleapis.com",
            ssl_credentials=None,
            options=[
                ("grpc.max_send_message_length", -1),
                ("grpc.max_receive_message_length", -1),
            ],
        )


@pytest.mark.parametrize(
    "request_type",
    [
        os_policy_assignments.CreateOSPolicyAssignmentRequest(),
        {},
    ],
)
def test_create_os_policy_assignment(request_type, transport: str = "grpc"):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_os_policy_assignment), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/spam")
        response = client.create_os_policy_assignment(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = os_policy_assignments.CreateOSPolicyAssignmentRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_create_os_policy_assignment_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = os_policy_assignments.CreateOSPolicyAssignmentRequest(
        parent="parent_value",
        os_policy_assignment_id="os_policy_assignment_id_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_os_policy_assignment), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.create_os_policy_assignment(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = os_policy_assignments.CreateOSPolicyAssignmentRequest(
            parent="parent_value",
            os_policy_assignment_id="os_policy_assignment_id_value",
        )
        assert args[0] == request_msg


def test_create_os_policy_assignment_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = OsConfigZonalServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.create_os_policy_assignment
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.create_os_policy_assignment
        ] = mock_rpc
        request = {}
        client.create_os_policy_assignment(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods call wrapper_fn to build a cached
        # client._transport.operations_client instance on first rpc call.
        # Subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.create_os_policy_assignment(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_create_os_policy_assignment_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = OsConfigZonalServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.create_os_policy_assignment
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.create_os_policy_assignment
        ] = mock_rpc

        request = {}
        await client.create_os_policy_assignment(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods call wrapper_fn to build a cached
        # client._transport.operations_client instance on first rpc call.
        # Subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        await client.create_os_policy_assignment(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        os_policy_assignments.CreateOSPolicyAssignmentRequest(),
        {},
    ],
)
async def test_create_os_policy_assignment_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_os_policy_assignment), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        response = await client.create_os_policy_assignment(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = os_policy_assignments.CreateOSPolicyAssignmentRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_create_os_policy_assignment_field_headers():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = os_policy_assignments.CreateOSPolicyAssignmentRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_os_policy_assignment), "__call__"
    ) as call:
        call.return_value = operations_pb2.Operation(name="operations/op")
        client.create_os_policy_assignment(request)

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
async def test_create_os_policy_assignment_field_headers_async():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = os_policy_assignments.CreateOSPolicyAssignmentRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_os_policy_assignment), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/op")
        )
        await client.create_os_policy_assignment(request)

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


def test_create_os_policy_assignment_flattened():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_os_policy_assignment), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.create_os_policy_assignment(
            parent="parent_value",
            os_policy_assignment=os_policy_assignments.OSPolicyAssignment(
                name="name_value"
            ),
            os_policy_assignment_id="os_policy_assignment_id_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val
        arg = args[0].os_policy_assignment
        mock_val = os_policy_assignments.OSPolicyAssignment(name="name_value")
        assert arg == mock_val
        arg = args[0].os_policy_assignment_id
        mock_val = "os_policy_assignment_id_value"
        assert arg == mock_val


def test_create_os_policy_assignment_flattened_error():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.create_os_policy_assignment(
            os_policy_assignments.CreateOSPolicyAssignmentRequest(),
            parent="parent_value",
            os_policy_assignment=os_policy_assignments.OSPolicyAssignment(
                name="name_value"
            ),
            os_policy_assignment_id="os_policy_assignment_id_value",
        )


@pytest.mark.asyncio
async def test_create_os_policy_assignment_flattened_async():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_os_policy_assignment), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.create_os_policy_assignment(
            parent="parent_value",
            os_policy_assignment=os_policy_assignments.OSPolicyAssignment(
                name="name_value"
            ),
            os_policy_assignment_id="os_policy_assignment_id_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val
        arg = args[0].os_policy_assignment
        mock_val = os_policy_assignments.OSPolicyAssignment(name="name_value")
        assert arg == mock_val
        arg = args[0].os_policy_assignment_id
        mock_val = "os_policy_assignment_id_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_create_os_policy_assignment_flattened_error_async():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.create_os_policy_assignment(
            os_policy_assignments.CreateOSPolicyAssignmentRequest(),
            parent="parent_value",
            os_policy_assignment=os_policy_assignments.OSPolicyAssignment(
                name="name_value"
            ),
            os_policy_assignment_id="os_policy_assignment_id_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        os_policy_assignments.UpdateOSPolicyAssignmentRequest(),
        {},
    ],
)
def test_update_os_policy_assignment(request_type, transport: str = "grpc"):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_os_policy_assignment), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/spam")
        response = client.update_os_policy_assignment(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = os_policy_assignments.UpdateOSPolicyAssignmentRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_update_os_policy_assignment_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = os_policy_assignments.UpdateOSPolicyAssignmentRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_os_policy_assignment), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.update_os_policy_assignment(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = os_policy_assignments.UpdateOSPolicyAssignmentRequest()
        assert args[0] == request_msg


def test_update_os_policy_assignment_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = OsConfigZonalServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.update_os_policy_assignment
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.update_os_policy_assignment
        ] = mock_rpc
        request = {}
        client.update_os_policy_assignment(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods call wrapper_fn to build a cached
        # client._transport.operations_client instance on first rpc call.
        # Subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.update_os_policy_assignment(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_update_os_policy_assignment_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = OsConfigZonalServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.update_os_policy_assignment
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.update_os_policy_assignment
        ] = mock_rpc

        request = {}
        await client.update_os_policy_assignment(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods call wrapper_fn to build a cached
        # client._transport.operations_client instance on first rpc call.
        # Subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        await client.update_os_policy_assignment(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        os_policy_assignments.UpdateOSPolicyAssignmentRequest(),
        {},
    ],
)
async def test_update_os_policy_assignment_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_os_policy_assignment), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        response = await client.update_os_policy_assignment(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = os_policy_assignments.UpdateOSPolicyAssignmentRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_update_os_policy_assignment_field_headers():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = os_policy_assignments.UpdateOSPolicyAssignmentRequest()

    request.os_policy_assignment.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_os_policy_assignment), "__call__"
    ) as call:
        call.return_value = operations_pb2.Operation(name="operations/op")
        client.update_os_policy_assignment(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "os_policy_assignment.name=name_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_update_os_policy_assignment_field_headers_async():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = os_policy_assignments.UpdateOSPolicyAssignmentRequest()

    request.os_policy_assignment.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_os_policy_assignment), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/op")
        )
        await client.update_os_policy_assignment(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "os_policy_assignment.name=name_value",
    ) in kw["metadata"]


def test_update_os_policy_assignment_flattened():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_os_policy_assignment), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.update_os_policy_assignment(
            os_policy_assignment=os_policy_assignments.OSPolicyAssignment(
                name="name_value"
            ),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].os_policy_assignment
        mock_val = os_policy_assignments.OSPolicyAssignment(name="name_value")
        assert arg == mock_val
        arg = args[0].update_mask
        mock_val = field_mask_pb2.FieldMask(paths=["paths_value"])
        assert arg == mock_val


def test_update_os_policy_assignment_flattened_error():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.update_os_policy_assignment(
            os_policy_assignments.UpdateOSPolicyAssignmentRequest(),
            os_policy_assignment=os_policy_assignments.OSPolicyAssignment(
                name="name_value"
            ),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


@pytest.mark.asyncio
async def test_update_os_policy_assignment_flattened_async():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_os_policy_assignment), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.update_os_policy_assignment(
            os_policy_assignment=os_policy_assignments.OSPolicyAssignment(
                name="name_value"
            ),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].os_policy_assignment
        mock_val = os_policy_assignments.OSPolicyAssignment(name="name_value")
        assert arg == mock_val
        arg = args[0].update_mask
        mock_val = field_mask_pb2.FieldMask(paths=["paths_value"])
        assert arg == mock_val


@pytest.mark.asyncio
async def test_update_os_policy_assignment_flattened_error_async():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.update_os_policy_assignment(
            os_policy_assignments.UpdateOSPolicyAssignmentRequest(),
            os_policy_assignment=os_policy_assignments.OSPolicyAssignment(
                name="name_value"
            ),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


@pytest.mark.parametrize(
    "request_type",
    [
        os_policy_assignments.GetOSPolicyAssignmentRequest(),
        {},
    ],
)
def test_get_os_policy_assignment(request_type, transport: str = "grpc"):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_os_policy_assignment), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = os_policy_assignments.OSPolicyAssignment(
            name="name_value",
            description="description_value",
            revision_id="revision_id_value",
            etag="etag_value",
            rollout_state=os_policy_assignments.OSPolicyAssignment.RolloutState.IN_PROGRESS,
            baseline=True,
            deleted=True,
            reconciling=True,
            uid="uid_value",
        )
        response = client.get_os_policy_assignment(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = os_policy_assignments.GetOSPolicyAssignmentRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, os_policy_assignments.OSPolicyAssignment)
    assert response.name == "name_value"
    assert response.description == "description_value"
    assert response.revision_id == "revision_id_value"
    assert response.etag == "etag_value"
    assert (
        response.rollout_state
        == os_policy_assignments.OSPolicyAssignment.RolloutState.IN_PROGRESS
    )
    assert response.baseline is True
    assert response.deleted is True
    assert response.reconciling is True
    assert response.uid == "uid_value"


def test_get_os_policy_assignment_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = os_policy_assignments.GetOSPolicyAssignmentRequest(
        name="name_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_os_policy_assignment), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.get_os_policy_assignment(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = os_policy_assignments.GetOSPolicyAssignmentRequest(
            name="name_value",
        )
        assert args[0] == request_msg


def test_get_os_policy_assignment_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = OsConfigZonalServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.get_os_policy_assignment
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.get_os_policy_assignment
        ] = mock_rpc
        request = {}
        client.get_os_policy_assignment(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_os_policy_assignment(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_get_os_policy_assignment_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = OsConfigZonalServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.get_os_policy_assignment
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.get_os_policy_assignment
        ] = mock_rpc

        request = {}
        await client.get_os_policy_assignment(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.get_os_policy_assignment(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        os_policy_assignments.GetOSPolicyAssignmentRequest(),
        {},
    ],
)
async def test_get_os_policy_assignment_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_os_policy_assignment), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            os_policy_assignments.OSPolicyAssignment(
                name="name_value",
                description="description_value",
                revision_id="revision_id_value",
                etag="etag_value",
                rollout_state=os_policy_assignments.OSPolicyAssignment.RolloutState.IN_PROGRESS,
                baseline=True,
                deleted=True,
                reconciling=True,
                uid="uid_value",
            )
        )
        response = await client.get_os_policy_assignment(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = os_policy_assignments.GetOSPolicyAssignmentRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, os_policy_assignments.OSPolicyAssignment)
    assert response.name == "name_value"
    assert response.description == "description_value"
    assert response.revision_id == "revision_id_value"
    assert response.etag == "etag_value"
    assert (
        response.rollout_state
        == os_policy_assignments.OSPolicyAssignment.RolloutState.IN_PROGRESS
    )
    assert response.baseline is True
    assert response.deleted is True
    assert response.reconciling is True
    assert response.uid == "uid_value"


def test_get_os_policy_assignment_field_headers():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = os_policy_assignments.GetOSPolicyAssignmentRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_os_policy_assignment), "__call__"
    ) as call:
        call.return_value = os_policy_assignments.OSPolicyAssignment()
        client.get_os_policy_assignment(request)

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
async def test_get_os_policy_assignment_field_headers_async():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = os_policy_assignments.GetOSPolicyAssignmentRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_os_policy_assignment), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            os_policy_assignments.OSPolicyAssignment()
        )
        await client.get_os_policy_assignment(request)

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


def test_get_os_policy_assignment_flattened():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_os_policy_assignment), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = os_policy_assignments.OSPolicyAssignment()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.get_os_policy_assignment(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_get_os_policy_assignment_flattened_error():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_os_policy_assignment(
            os_policy_assignments.GetOSPolicyAssignmentRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_get_os_policy_assignment_flattened_async():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_os_policy_assignment), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = os_policy_assignments.OSPolicyAssignment()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            os_policy_assignments.OSPolicyAssignment()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.get_os_policy_assignment(
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
async def test_get_os_policy_assignment_flattened_error_async():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.get_os_policy_assignment(
            os_policy_assignments.GetOSPolicyAssignmentRequest(),
            name="name_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        os_policy_assignments.ListOSPolicyAssignmentsRequest(),
        {},
    ],
)
def test_list_os_policy_assignments(request_type, transport: str = "grpc"):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_os_policy_assignments), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = os_policy_assignments.ListOSPolicyAssignmentsResponse(
            next_page_token="next_page_token_value",
        )
        response = client.list_os_policy_assignments(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = os_policy_assignments.ListOSPolicyAssignmentsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListOSPolicyAssignmentsPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_os_policy_assignments_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = os_policy_assignments.ListOSPolicyAssignmentsRequest(
        parent="parent_value",
        page_token="page_token_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_os_policy_assignments), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.list_os_policy_assignments(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = os_policy_assignments.ListOSPolicyAssignmentsRequest(
            parent="parent_value",
            page_token="page_token_value",
        )
        assert args[0] == request_msg


def test_list_os_policy_assignments_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = OsConfigZonalServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.list_os_policy_assignments
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.list_os_policy_assignments
        ] = mock_rpc
        request = {}
        client.list_os_policy_assignments(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_os_policy_assignments(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_list_os_policy_assignments_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = OsConfigZonalServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.list_os_policy_assignments
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.list_os_policy_assignments
        ] = mock_rpc

        request = {}
        await client.list_os_policy_assignments(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.list_os_policy_assignments(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        os_policy_assignments.ListOSPolicyAssignmentsRequest(),
        {},
    ],
)
async def test_list_os_policy_assignments_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_os_policy_assignments), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            os_policy_assignments.ListOSPolicyAssignmentsResponse(
                next_page_token="next_page_token_value",
            )
        )
        response = await client.list_os_policy_assignments(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = os_policy_assignments.ListOSPolicyAssignmentsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListOSPolicyAssignmentsAsyncPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_os_policy_assignments_field_headers():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = os_policy_assignments.ListOSPolicyAssignmentsRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_os_policy_assignments), "__call__"
    ) as call:
        call.return_value = os_policy_assignments.ListOSPolicyAssignmentsResponse()
        client.list_os_policy_assignments(request)

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
async def test_list_os_policy_assignments_field_headers_async():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = os_policy_assignments.ListOSPolicyAssignmentsRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_os_policy_assignments), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            os_policy_assignments.ListOSPolicyAssignmentsResponse()
        )
        await client.list_os_policy_assignments(request)

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


def test_list_os_policy_assignments_flattened():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_os_policy_assignments), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = os_policy_assignments.ListOSPolicyAssignmentsResponse()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.list_os_policy_assignments(
            parent="parent_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val


def test_list_os_policy_assignments_flattened_error():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_os_policy_assignments(
            os_policy_assignments.ListOSPolicyAssignmentsRequest(),
            parent="parent_value",
        )


@pytest.mark.asyncio
async def test_list_os_policy_assignments_flattened_async():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_os_policy_assignments), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = os_policy_assignments.ListOSPolicyAssignmentsResponse()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            os_policy_assignments.ListOSPolicyAssignmentsResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.list_os_policy_assignments(
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
async def test_list_os_policy_assignments_flattened_error_async():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.list_os_policy_assignments(
            os_policy_assignments.ListOSPolicyAssignmentsRequest(),
            parent="parent_value",
        )


def test_list_os_policy_assignments_pager(transport_name: str = "grpc"):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_os_policy_assignments), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            os_policy_assignments.ListOSPolicyAssignmentsResponse(
                os_policy_assignments=[
                    os_policy_assignments.OSPolicyAssignment(),
                    os_policy_assignments.OSPolicyAssignment(),
                    os_policy_assignments.OSPolicyAssignment(),
                ],
                next_page_token="abc",
            ),
            os_policy_assignments.ListOSPolicyAssignmentsResponse(
                os_policy_assignments=[],
                next_page_token="def",
            ),
            os_policy_assignments.ListOSPolicyAssignmentsResponse(
                os_policy_assignments=[
                    os_policy_assignments.OSPolicyAssignment(),
                ],
                next_page_token="ghi",
            ),
            os_policy_assignments.ListOSPolicyAssignmentsResponse(
                os_policy_assignments=[
                    os_policy_assignments.OSPolicyAssignment(),
                    os_policy_assignments.OSPolicyAssignment(),
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
        pager = client.list_os_policy_assignments(
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
            isinstance(i, os_policy_assignments.OSPolicyAssignment) for i in results
        )


def test_list_os_policy_assignments_pages(transport_name: str = "grpc"):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_os_policy_assignments), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            os_policy_assignments.ListOSPolicyAssignmentsResponse(
                os_policy_assignments=[
                    os_policy_assignments.OSPolicyAssignment(),
                    os_policy_assignments.OSPolicyAssignment(),
                    os_policy_assignments.OSPolicyAssignment(),
                ],
                next_page_token="abc",
            ),
            os_policy_assignments.ListOSPolicyAssignmentsResponse(
                os_policy_assignments=[],
                next_page_token="def",
            ),
            os_policy_assignments.ListOSPolicyAssignmentsResponse(
                os_policy_assignments=[
                    os_policy_assignments.OSPolicyAssignment(),
                ],
                next_page_token="ghi",
            ),
            os_policy_assignments.ListOSPolicyAssignmentsResponse(
                os_policy_assignments=[
                    os_policy_assignments.OSPolicyAssignment(),
                    os_policy_assignments.OSPolicyAssignment(),
                ],
            ),
            RuntimeError,
        )
        pages = list(client.list_os_policy_assignments(request={}).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.asyncio
async def test_list_os_policy_assignments_async_pager():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_os_policy_assignments),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            os_policy_assignments.ListOSPolicyAssignmentsResponse(
                os_policy_assignments=[
                    os_policy_assignments.OSPolicyAssignment(),
                    os_policy_assignments.OSPolicyAssignment(),
                    os_policy_assignments.OSPolicyAssignment(),
                ],
                next_page_token="abc",
            ),
            os_policy_assignments.ListOSPolicyAssignmentsResponse(
                os_policy_assignments=[],
                next_page_token="def",
            ),
            os_policy_assignments.ListOSPolicyAssignmentsResponse(
                os_policy_assignments=[
                    os_policy_assignments.OSPolicyAssignment(),
                ],
                next_page_token="ghi",
            ),
            os_policy_assignments.ListOSPolicyAssignmentsResponse(
                os_policy_assignments=[
                    os_policy_assignments.OSPolicyAssignment(),
                    os_policy_assignments.OSPolicyAssignment(),
                ],
            ),
            RuntimeError,
        )
        async_pager = await client.list_os_policy_assignments(
            request={},
        )
        assert async_pager.next_page_token == "abc"
        assert str(async_pager).startswith(f"{async_pager.__class__.__name__}<")

        responses = []
        async for response in async_pager:  # pragma: no branch
            responses.append(response)

        assert len(responses) == 6
        assert all(
            isinstance(i, os_policy_assignments.OSPolicyAssignment) for i in responses
        )


@pytest.mark.asyncio
async def test_list_os_policy_assignments_async_pages():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_os_policy_assignments),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            os_policy_assignments.ListOSPolicyAssignmentsResponse(
                os_policy_assignments=[
                    os_policy_assignments.OSPolicyAssignment(),
                    os_policy_assignments.OSPolicyAssignment(),
                    os_policy_assignments.OSPolicyAssignment(),
                ],
                next_page_token="abc",
            ),
            os_policy_assignments.ListOSPolicyAssignmentsResponse(
                os_policy_assignments=[],
                next_page_token="def",
            ),
            os_policy_assignments.ListOSPolicyAssignmentsResponse(
                os_policy_assignments=[
                    os_policy_assignments.OSPolicyAssignment(),
                ],
                next_page_token="ghi",
            ),
            os_policy_assignments.ListOSPolicyAssignmentsResponse(
                os_policy_assignments=[
                    os_policy_assignments.OSPolicyAssignment(),
                    os_policy_assignments.OSPolicyAssignment(),
                ],
            ),
            RuntimeError,
        )
        pages = []
        async for page_ in (await client.list_os_policy_assignments(request={})).pages:
            pages.append(page_)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.parametrize(
    "request_type",
    [
        os_policy_assignments.ListOSPolicyAssignmentRevisionsRequest(),
        {},
    ],
)
def test_list_os_policy_assignment_revisions(request_type, transport: str = "grpc"):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_os_policy_assignment_revisions), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = (
            os_policy_assignments.ListOSPolicyAssignmentRevisionsResponse(
                next_page_token="next_page_token_value",
            )
        )
        response = client.list_os_policy_assignment_revisions(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = os_policy_assignments.ListOSPolicyAssignmentRevisionsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListOSPolicyAssignmentRevisionsPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_os_policy_assignment_revisions_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = os_policy_assignments.ListOSPolicyAssignmentRevisionsRequest(
        name="name_value",
        page_token="page_token_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_os_policy_assignment_revisions), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.list_os_policy_assignment_revisions(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = os_policy_assignments.ListOSPolicyAssignmentRevisionsRequest(
            name="name_value",
            page_token="page_token_value",
        )
        assert args[0] == request_msg


def test_list_os_policy_assignment_revisions_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = OsConfigZonalServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.list_os_policy_assignment_revisions
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.list_os_policy_assignment_revisions
        ] = mock_rpc
        request = {}
        client.list_os_policy_assignment_revisions(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_os_policy_assignment_revisions(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_list_os_policy_assignment_revisions_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = OsConfigZonalServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.list_os_policy_assignment_revisions
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.list_os_policy_assignment_revisions
        ] = mock_rpc

        request = {}
        await client.list_os_policy_assignment_revisions(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.list_os_policy_assignment_revisions(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        os_policy_assignments.ListOSPolicyAssignmentRevisionsRequest(),
        {},
    ],
)
async def test_list_os_policy_assignment_revisions_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_os_policy_assignment_revisions), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            os_policy_assignments.ListOSPolicyAssignmentRevisionsResponse(
                next_page_token="next_page_token_value",
            )
        )
        response = await client.list_os_policy_assignment_revisions(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = os_policy_assignments.ListOSPolicyAssignmentRevisionsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListOSPolicyAssignmentRevisionsAsyncPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_os_policy_assignment_revisions_field_headers():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = os_policy_assignments.ListOSPolicyAssignmentRevisionsRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_os_policy_assignment_revisions), "__call__"
    ) as call:
        call.return_value = (
            os_policy_assignments.ListOSPolicyAssignmentRevisionsResponse()
        )
        client.list_os_policy_assignment_revisions(request)

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
async def test_list_os_policy_assignment_revisions_field_headers_async():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = os_policy_assignments.ListOSPolicyAssignmentRevisionsRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_os_policy_assignment_revisions), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            os_policy_assignments.ListOSPolicyAssignmentRevisionsResponse()
        )
        await client.list_os_policy_assignment_revisions(request)

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


def test_list_os_policy_assignment_revisions_flattened():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_os_policy_assignment_revisions), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = (
            os_policy_assignments.ListOSPolicyAssignmentRevisionsResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.list_os_policy_assignment_revisions(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_list_os_policy_assignment_revisions_flattened_error():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_os_policy_assignment_revisions(
            os_policy_assignments.ListOSPolicyAssignmentRevisionsRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_list_os_policy_assignment_revisions_flattened_async():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_os_policy_assignment_revisions), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = (
            os_policy_assignments.ListOSPolicyAssignmentRevisionsResponse()
        )

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            os_policy_assignments.ListOSPolicyAssignmentRevisionsResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.list_os_policy_assignment_revisions(
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
async def test_list_os_policy_assignment_revisions_flattened_error_async():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.list_os_policy_assignment_revisions(
            os_policy_assignments.ListOSPolicyAssignmentRevisionsRequest(),
            name="name_value",
        )


def test_list_os_policy_assignment_revisions_pager(transport_name: str = "grpc"):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_os_policy_assignment_revisions), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            os_policy_assignments.ListOSPolicyAssignmentRevisionsResponse(
                os_policy_assignments=[
                    os_policy_assignments.OSPolicyAssignment(),
                    os_policy_assignments.OSPolicyAssignment(),
                    os_policy_assignments.OSPolicyAssignment(),
                ],
                next_page_token="abc",
            ),
            os_policy_assignments.ListOSPolicyAssignmentRevisionsResponse(
                os_policy_assignments=[],
                next_page_token="def",
            ),
            os_policy_assignments.ListOSPolicyAssignmentRevisionsResponse(
                os_policy_assignments=[
                    os_policy_assignments.OSPolicyAssignment(),
                ],
                next_page_token="ghi",
            ),
            os_policy_assignments.ListOSPolicyAssignmentRevisionsResponse(
                os_policy_assignments=[
                    os_policy_assignments.OSPolicyAssignment(),
                    os_policy_assignments.OSPolicyAssignment(),
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
        pager = client.list_os_policy_assignment_revisions(
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
            isinstance(i, os_policy_assignments.OSPolicyAssignment) for i in results
        )


def test_list_os_policy_assignment_revisions_pages(transport_name: str = "grpc"):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_os_policy_assignment_revisions), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            os_policy_assignments.ListOSPolicyAssignmentRevisionsResponse(
                os_policy_assignments=[
                    os_policy_assignments.OSPolicyAssignment(),
                    os_policy_assignments.OSPolicyAssignment(),
                    os_policy_assignments.OSPolicyAssignment(),
                ],
                next_page_token="abc",
            ),
            os_policy_assignments.ListOSPolicyAssignmentRevisionsResponse(
                os_policy_assignments=[],
                next_page_token="def",
            ),
            os_policy_assignments.ListOSPolicyAssignmentRevisionsResponse(
                os_policy_assignments=[
                    os_policy_assignments.OSPolicyAssignment(),
                ],
                next_page_token="ghi",
            ),
            os_policy_assignments.ListOSPolicyAssignmentRevisionsResponse(
                os_policy_assignments=[
                    os_policy_assignments.OSPolicyAssignment(),
                    os_policy_assignments.OSPolicyAssignment(),
                ],
            ),
            RuntimeError,
        )
        pages = list(client.list_os_policy_assignment_revisions(request={}).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.asyncio
async def test_list_os_policy_assignment_revisions_async_pager():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_os_policy_assignment_revisions),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            os_policy_assignments.ListOSPolicyAssignmentRevisionsResponse(
                os_policy_assignments=[
                    os_policy_assignments.OSPolicyAssignment(),
                    os_policy_assignments.OSPolicyAssignment(),
                    os_policy_assignments.OSPolicyAssignment(),
                ],
                next_page_token="abc",
            ),
            os_policy_assignments.ListOSPolicyAssignmentRevisionsResponse(
                os_policy_assignments=[],
                next_page_token="def",
            ),
            os_policy_assignments.ListOSPolicyAssignmentRevisionsResponse(
                os_policy_assignments=[
                    os_policy_assignments.OSPolicyAssignment(),
                ],
                next_page_token="ghi",
            ),
            os_policy_assignments.ListOSPolicyAssignmentRevisionsResponse(
                os_policy_assignments=[
                    os_policy_assignments.OSPolicyAssignment(),
                    os_policy_assignments.OSPolicyAssignment(),
                ],
            ),
            RuntimeError,
        )
        async_pager = await client.list_os_policy_assignment_revisions(
            request={},
        )
        assert async_pager.next_page_token == "abc"
        assert str(async_pager).startswith(f"{async_pager.__class__.__name__}<")

        responses = []
        async for response in async_pager:  # pragma: no branch
            responses.append(response)

        assert len(responses) == 6
        assert all(
            isinstance(i, os_policy_assignments.OSPolicyAssignment) for i in responses
        )


@pytest.mark.asyncio
async def test_list_os_policy_assignment_revisions_async_pages():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_os_policy_assignment_revisions),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            os_policy_assignments.ListOSPolicyAssignmentRevisionsResponse(
                os_policy_assignments=[
                    os_policy_assignments.OSPolicyAssignment(),
                    os_policy_assignments.OSPolicyAssignment(),
                    os_policy_assignments.OSPolicyAssignment(),
                ],
                next_page_token="abc",
            ),
            os_policy_assignments.ListOSPolicyAssignmentRevisionsResponse(
                os_policy_assignments=[],
                next_page_token="def",
            ),
            os_policy_assignments.ListOSPolicyAssignmentRevisionsResponse(
                os_policy_assignments=[
                    os_policy_assignments.OSPolicyAssignment(),
                ],
                next_page_token="ghi",
            ),
            os_policy_assignments.ListOSPolicyAssignmentRevisionsResponse(
                os_policy_assignments=[
                    os_policy_assignments.OSPolicyAssignment(),
                    os_policy_assignments.OSPolicyAssignment(),
                ],
            ),
            RuntimeError,
        )
        pages = []
        async for page_ in (
            await client.list_os_policy_assignment_revisions(request={})
        ).pages:
            pages.append(page_)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.parametrize(
    "request_type",
    [
        os_policy_assignments.DeleteOSPolicyAssignmentRequest(),
        {},
    ],
)
def test_delete_os_policy_assignment(request_type, transport: str = "grpc"):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_os_policy_assignment), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/spam")
        response = client.delete_os_policy_assignment(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = os_policy_assignments.DeleteOSPolicyAssignmentRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_delete_os_policy_assignment_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = os_policy_assignments.DeleteOSPolicyAssignmentRequest(
        name="name_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_os_policy_assignment), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.delete_os_policy_assignment(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = os_policy_assignments.DeleteOSPolicyAssignmentRequest(
            name="name_value",
        )
        assert args[0] == request_msg


def test_delete_os_policy_assignment_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = OsConfigZonalServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.delete_os_policy_assignment
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.delete_os_policy_assignment
        ] = mock_rpc
        request = {}
        client.delete_os_policy_assignment(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods call wrapper_fn to build a cached
        # client._transport.operations_client instance on first rpc call.
        # Subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.delete_os_policy_assignment(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_delete_os_policy_assignment_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = OsConfigZonalServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.delete_os_policy_assignment
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.delete_os_policy_assignment
        ] = mock_rpc

        request = {}
        await client.delete_os_policy_assignment(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods call wrapper_fn to build a cached
        # client._transport.operations_client instance on first rpc call.
        # Subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        await client.delete_os_policy_assignment(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        os_policy_assignments.DeleteOSPolicyAssignmentRequest(),
        {},
    ],
)
async def test_delete_os_policy_assignment_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_os_policy_assignment), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        response = await client.delete_os_policy_assignment(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = os_policy_assignments.DeleteOSPolicyAssignmentRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_delete_os_policy_assignment_field_headers():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = os_policy_assignments.DeleteOSPolicyAssignmentRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_os_policy_assignment), "__call__"
    ) as call:
        call.return_value = operations_pb2.Operation(name="operations/op")
        client.delete_os_policy_assignment(request)

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
async def test_delete_os_policy_assignment_field_headers_async():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = os_policy_assignments.DeleteOSPolicyAssignmentRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_os_policy_assignment), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/op")
        )
        await client.delete_os_policy_assignment(request)

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


def test_delete_os_policy_assignment_flattened():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_os_policy_assignment), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.delete_os_policy_assignment(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_delete_os_policy_assignment_flattened_error():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.delete_os_policy_assignment(
            os_policy_assignments.DeleteOSPolicyAssignmentRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_delete_os_policy_assignment_flattened_async():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_os_policy_assignment), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.delete_os_policy_assignment(
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
async def test_delete_os_policy_assignment_flattened_error_async():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.delete_os_policy_assignment(
            os_policy_assignments.DeleteOSPolicyAssignmentRequest(),
            name="name_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        instance_os_policies_compliance.GetInstanceOSPoliciesComplianceRequest(),
        {},
    ],
)
def test_get_instance_os_policies_compliance(request_type, transport: str = "grpc"):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_instance_os_policies_compliance), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = (
            instance_os_policies_compliance.InstanceOSPoliciesCompliance(
                name="name_value",
                instance="instance_value",
                state=config_common.OSPolicyComplianceState.COMPLIANT,
                detailed_state="detailed_state_value",
                detailed_state_reason="detailed_state_reason_value",
                last_compliance_run_id="last_compliance_run_id_value",
            )
        )
        response = client.get_instance_os_policies_compliance(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = (
            instance_os_policies_compliance.GetInstanceOSPoliciesComplianceRequest()
        )
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(
        response, instance_os_policies_compliance.InstanceOSPoliciesCompliance
    )
    assert response.name == "name_value"
    assert response.instance == "instance_value"
    assert response.state == config_common.OSPolicyComplianceState.COMPLIANT
    assert response.detailed_state == "detailed_state_value"
    assert response.detailed_state_reason == "detailed_state_reason_value"
    assert response.last_compliance_run_id == "last_compliance_run_id_value"


def test_get_instance_os_policies_compliance_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = instance_os_policies_compliance.GetInstanceOSPoliciesComplianceRequest(
        name="name_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_instance_os_policies_compliance), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.get_instance_os_policies_compliance(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = (
            instance_os_policies_compliance.GetInstanceOSPoliciesComplianceRequest(
                name="name_value",
            )
        )
        assert args[0] == request_msg


def test_get_instance_os_policies_compliance_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = OsConfigZonalServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.get_instance_os_policies_compliance
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.get_instance_os_policies_compliance
        ] = mock_rpc
        request = {}
        client.get_instance_os_policies_compliance(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_instance_os_policies_compliance(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_get_instance_os_policies_compliance_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = OsConfigZonalServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.get_instance_os_policies_compliance
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.get_instance_os_policies_compliance
        ] = mock_rpc

        request = {}
        await client.get_instance_os_policies_compliance(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.get_instance_os_policies_compliance(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        instance_os_policies_compliance.GetInstanceOSPoliciesComplianceRequest(),
        {},
    ],
)
async def test_get_instance_os_policies_compliance_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_instance_os_policies_compliance), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            instance_os_policies_compliance.InstanceOSPoliciesCompliance(
                name="name_value",
                instance="instance_value",
                state=config_common.OSPolicyComplianceState.COMPLIANT,
                detailed_state="detailed_state_value",
                detailed_state_reason="detailed_state_reason_value",
                last_compliance_run_id="last_compliance_run_id_value",
            )
        )
        response = await client.get_instance_os_policies_compliance(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = (
            instance_os_policies_compliance.GetInstanceOSPoliciesComplianceRequest()
        )
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(
        response, instance_os_policies_compliance.InstanceOSPoliciesCompliance
    )
    assert response.name == "name_value"
    assert response.instance == "instance_value"
    assert response.state == config_common.OSPolicyComplianceState.COMPLIANT
    assert response.detailed_state == "detailed_state_value"
    assert response.detailed_state_reason == "detailed_state_reason_value"
    assert response.last_compliance_run_id == "last_compliance_run_id_value"


def test_get_instance_os_policies_compliance_field_headers():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = instance_os_policies_compliance.GetInstanceOSPoliciesComplianceRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_instance_os_policies_compliance), "__call__"
    ) as call:
        call.return_value = (
            instance_os_policies_compliance.InstanceOSPoliciesCompliance()
        )
        client.get_instance_os_policies_compliance(request)

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
async def test_get_instance_os_policies_compliance_field_headers_async():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = instance_os_policies_compliance.GetInstanceOSPoliciesComplianceRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_instance_os_policies_compliance), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            instance_os_policies_compliance.InstanceOSPoliciesCompliance()
        )
        await client.get_instance_os_policies_compliance(request)

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


def test_get_instance_os_policies_compliance_flattened():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_instance_os_policies_compliance), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = (
            instance_os_policies_compliance.InstanceOSPoliciesCompliance()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.get_instance_os_policies_compliance(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_get_instance_os_policies_compliance_flattened_error():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_instance_os_policies_compliance(
            instance_os_policies_compliance.GetInstanceOSPoliciesComplianceRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_get_instance_os_policies_compliance_flattened_async():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_instance_os_policies_compliance), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = (
            instance_os_policies_compliance.InstanceOSPoliciesCompliance()
        )

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            instance_os_policies_compliance.InstanceOSPoliciesCompliance()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.get_instance_os_policies_compliance(
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
async def test_get_instance_os_policies_compliance_flattened_error_async():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.get_instance_os_policies_compliance(
            instance_os_policies_compliance.GetInstanceOSPoliciesComplianceRequest(),
            name="name_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesRequest(),
        {},
    ],
)
def test_list_instance_os_policies_compliances(request_type, transport: str = "grpc"):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_instance_os_policies_compliances), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = (
            instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesResponse(
                next_page_token="next_page_token_value",
            )
        )
        response = client.list_instance_os_policies_compliances(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = (
            instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesRequest()
        )
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListInstanceOSPoliciesCompliancesPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_instance_os_policies_compliances_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesRequest(
        parent="parent_value",
        page_token="page_token_value",
        filter="filter_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_instance_os_policies_compliances), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.list_instance_os_policies_compliances(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = (
            instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesRequest(
                parent="parent_value",
                page_token="page_token_value",
                filter="filter_value",
            )
        )
        assert args[0] == request_msg


def test_list_instance_os_policies_compliances_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = OsConfigZonalServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.list_instance_os_policies_compliances
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.list_instance_os_policies_compliances
        ] = mock_rpc
        request = {}
        client.list_instance_os_policies_compliances(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_instance_os_policies_compliances(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_list_instance_os_policies_compliances_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = OsConfigZonalServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.list_instance_os_policies_compliances
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.list_instance_os_policies_compliances
        ] = mock_rpc

        request = {}
        await client.list_instance_os_policies_compliances(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.list_instance_os_policies_compliances(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesRequest(),
        {},
    ],
)
async def test_list_instance_os_policies_compliances_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_instance_os_policies_compliances), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesResponse(
                next_page_token="next_page_token_value",
            )
        )
        response = await client.list_instance_os_policies_compliances(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = (
            instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesRequest()
        )
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListInstanceOSPoliciesCompliancesAsyncPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_instance_os_policies_compliances_field_headers():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_instance_os_policies_compliances), "__call__"
    ) as call:
        call.return_value = (
            instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesResponse()
        )
        client.list_instance_os_policies_compliances(request)

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
async def test_list_instance_os_policies_compliances_field_headers_async():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_instance_os_policies_compliances), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesResponse()
        )
        await client.list_instance_os_policies_compliances(request)

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


def test_list_instance_os_policies_compliances_flattened():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_instance_os_policies_compliances), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = (
            instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.list_instance_os_policies_compliances(
            parent="parent_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val


def test_list_instance_os_policies_compliances_flattened_error():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_instance_os_policies_compliances(
            instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesRequest(),
            parent="parent_value",
        )


@pytest.mark.asyncio
async def test_list_instance_os_policies_compliances_flattened_async():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_instance_os_policies_compliances), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = (
            instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesResponse()
        )

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.list_instance_os_policies_compliances(
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
async def test_list_instance_os_policies_compliances_flattened_error_async():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.list_instance_os_policies_compliances(
            instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesRequest(),
            parent="parent_value",
        )


def test_list_instance_os_policies_compliances_pager(transport_name: str = "grpc"):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_instance_os_policies_compliances), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesResponse(
                instance_os_policies_compliances=[
                    instance_os_policies_compliance.InstanceOSPoliciesCompliance(),
                    instance_os_policies_compliance.InstanceOSPoliciesCompliance(),
                    instance_os_policies_compliance.InstanceOSPoliciesCompliance(),
                ],
                next_page_token="abc",
            ),
            instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesResponse(
                instance_os_policies_compliances=[],
                next_page_token="def",
            ),
            instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesResponse(
                instance_os_policies_compliances=[
                    instance_os_policies_compliance.InstanceOSPoliciesCompliance(),
                ],
                next_page_token="ghi",
            ),
            instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesResponse(
                instance_os_policies_compliances=[
                    instance_os_policies_compliance.InstanceOSPoliciesCompliance(),
                    instance_os_policies_compliance.InstanceOSPoliciesCompliance(),
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
        pager = client.list_instance_os_policies_compliances(
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
            isinstance(i, instance_os_policies_compliance.InstanceOSPoliciesCompliance)
            for i in results
        )


def test_list_instance_os_policies_compliances_pages(transport_name: str = "grpc"):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_instance_os_policies_compliances), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesResponse(
                instance_os_policies_compliances=[
                    instance_os_policies_compliance.InstanceOSPoliciesCompliance(),
                    instance_os_policies_compliance.InstanceOSPoliciesCompliance(),
                    instance_os_policies_compliance.InstanceOSPoliciesCompliance(),
                ],
                next_page_token="abc",
            ),
            instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesResponse(
                instance_os_policies_compliances=[],
                next_page_token="def",
            ),
            instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesResponse(
                instance_os_policies_compliances=[
                    instance_os_policies_compliance.InstanceOSPoliciesCompliance(),
                ],
                next_page_token="ghi",
            ),
            instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesResponse(
                instance_os_policies_compliances=[
                    instance_os_policies_compliance.InstanceOSPoliciesCompliance(),
                    instance_os_policies_compliance.InstanceOSPoliciesCompliance(),
                ],
            ),
            RuntimeError,
        )
        pages = list(client.list_instance_os_policies_compliances(request={}).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.asyncio
async def test_list_instance_os_policies_compliances_async_pager():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_instance_os_policies_compliances),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesResponse(
                instance_os_policies_compliances=[
                    instance_os_policies_compliance.InstanceOSPoliciesCompliance(),
                    instance_os_policies_compliance.InstanceOSPoliciesCompliance(),
                    instance_os_policies_compliance.InstanceOSPoliciesCompliance(),
                ],
                next_page_token="abc",
            ),
            instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesResponse(
                instance_os_policies_compliances=[],
                next_page_token="def",
            ),
            instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesResponse(
                instance_os_policies_compliances=[
                    instance_os_policies_compliance.InstanceOSPoliciesCompliance(),
                ],
                next_page_token="ghi",
            ),
            instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesResponse(
                instance_os_policies_compliances=[
                    instance_os_policies_compliance.InstanceOSPoliciesCompliance(),
                    instance_os_policies_compliance.InstanceOSPoliciesCompliance(),
                ],
            ),
            RuntimeError,
        )
        async_pager = await client.list_instance_os_policies_compliances(
            request={},
        )
        assert async_pager.next_page_token == "abc"
        assert str(async_pager).startswith(f"{async_pager.__class__.__name__}<")

        responses = []
        async for response in async_pager:  # pragma: no branch
            responses.append(response)

        assert len(responses) == 6
        assert all(
            isinstance(i, instance_os_policies_compliance.InstanceOSPoliciesCompliance)
            for i in responses
        )


@pytest.mark.asyncio
async def test_list_instance_os_policies_compliances_async_pages():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_instance_os_policies_compliances),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesResponse(
                instance_os_policies_compliances=[
                    instance_os_policies_compliance.InstanceOSPoliciesCompliance(),
                    instance_os_policies_compliance.InstanceOSPoliciesCompliance(),
                    instance_os_policies_compliance.InstanceOSPoliciesCompliance(),
                ],
                next_page_token="abc",
            ),
            instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesResponse(
                instance_os_policies_compliances=[],
                next_page_token="def",
            ),
            instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesResponse(
                instance_os_policies_compliances=[
                    instance_os_policies_compliance.InstanceOSPoliciesCompliance(),
                ],
                next_page_token="ghi",
            ),
            instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesResponse(
                instance_os_policies_compliances=[
                    instance_os_policies_compliance.InstanceOSPoliciesCompliance(),
                    instance_os_policies_compliance.InstanceOSPoliciesCompliance(),
                ],
            ),
            RuntimeError,
        )
        pages = []
        async for page_ in (
            await client.list_instance_os_policies_compliances(request={})
        ).pages:
            pages.append(page_)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.parametrize(
    "request_type",
    [
        os_policy_assignment_reports.GetOSPolicyAssignmentReportRequest(),
        {},
    ],
)
def test_get_os_policy_assignment_report(request_type, transport: str = "grpc"):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_os_policy_assignment_report), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = os_policy_assignment_reports.OSPolicyAssignmentReport(
            name="name_value",
            instance="instance_value",
            os_policy_assignment="os_policy_assignment_value",
            last_run_id="last_run_id_value",
        )
        response = client.get_os_policy_assignment_report(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = os_policy_assignment_reports.GetOSPolicyAssignmentReportRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, os_policy_assignment_reports.OSPolicyAssignmentReport)
    assert response.name == "name_value"
    assert response.instance == "instance_value"
    assert response.os_policy_assignment == "os_policy_assignment_value"
    assert response.last_run_id == "last_run_id_value"


def test_get_os_policy_assignment_report_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = os_policy_assignment_reports.GetOSPolicyAssignmentReportRequest(
        name="name_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_os_policy_assignment_report), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.get_os_policy_assignment_report(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = os_policy_assignment_reports.GetOSPolicyAssignmentReportRequest(
            name="name_value",
        )
        assert args[0] == request_msg


def test_get_os_policy_assignment_report_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = OsConfigZonalServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.get_os_policy_assignment_report
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.get_os_policy_assignment_report
        ] = mock_rpc
        request = {}
        client.get_os_policy_assignment_report(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_os_policy_assignment_report(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_get_os_policy_assignment_report_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = OsConfigZonalServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.get_os_policy_assignment_report
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.get_os_policy_assignment_report
        ] = mock_rpc

        request = {}
        await client.get_os_policy_assignment_report(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.get_os_policy_assignment_report(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        os_policy_assignment_reports.GetOSPolicyAssignmentReportRequest(),
        {},
    ],
)
async def test_get_os_policy_assignment_report_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_os_policy_assignment_report), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            os_policy_assignment_reports.OSPolicyAssignmentReport(
                name="name_value",
                instance="instance_value",
                os_policy_assignment="os_policy_assignment_value",
                last_run_id="last_run_id_value",
            )
        )
        response = await client.get_os_policy_assignment_report(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = os_policy_assignment_reports.GetOSPolicyAssignmentReportRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, os_policy_assignment_reports.OSPolicyAssignmentReport)
    assert response.name == "name_value"
    assert response.instance == "instance_value"
    assert response.os_policy_assignment == "os_policy_assignment_value"
    assert response.last_run_id == "last_run_id_value"


def test_get_os_policy_assignment_report_field_headers():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = os_policy_assignment_reports.GetOSPolicyAssignmentReportRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_os_policy_assignment_report), "__call__"
    ) as call:
        call.return_value = os_policy_assignment_reports.OSPolicyAssignmentReport()
        client.get_os_policy_assignment_report(request)

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
async def test_get_os_policy_assignment_report_field_headers_async():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = os_policy_assignment_reports.GetOSPolicyAssignmentReportRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_os_policy_assignment_report), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            os_policy_assignment_reports.OSPolicyAssignmentReport()
        )
        await client.get_os_policy_assignment_report(request)

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


def test_get_os_policy_assignment_report_flattened():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_os_policy_assignment_report), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = os_policy_assignment_reports.OSPolicyAssignmentReport()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.get_os_policy_assignment_report(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_get_os_policy_assignment_report_flattened_error():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_os_policy_assignment_report(
            os_policy_assignment_reports.GetOSPolicyAssignmentReportRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_get_os_policy_assignment_report_flattened_async():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_os_policy_assignment_report), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = os_policy_assignment_reports.OSPolicyAssignmentReport()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            os_policy_assignment_reports.OSPolicyAssignmentReport()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.get_os_policy_assignment_report(
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
async def test_get_os_policy_assignment_report_flattened_error_async():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.get_os_policy_assignment_report(
            os_policy_assignment_reports.GetOSPolicyAssignmentReportRequest(),
            name="name_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        os_policy_assignment_reports.ListOSPolicyAssignmentReportsRequest(),
        {},
    ],
)
def test_list_os_policy_assignment_reports(request_type, transport: str = "grpc"):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_os_policy_assignment_reports), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = (
            os_policy_assignment_reports.ListOSPolicyAssignmentReportsResponse(
                next_page_token="next_page_token_value",
            )
        )
        response = client.list_os_policy_assignment_reports(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = os_policy_assignment_reports.ListOSPolicyAssignmentReportsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListOSPolicyAssignmentReportsPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_os_policy_assignment_reports_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = os_policy_assignment_reports.ListOSPolicyAssignmentReportsRequest(
        parent="parent_value",
        filter="filter_value",
        page_token="page_token_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_os_policy_assignment_reports), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.list_os_policy_assignment_reports(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = os_policy_assignment_reports.ListOSPolicyAssignmentReportsRequest(
            parent="parent_value",
            filter="filter_value",
            page_token="page_token_value",
        )
        assert args[0] == request_msg


def test_list_os_policy_assignment_reports_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = OsConfigZonalServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.list_os_policy_assignment_reports
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.list_os_policy_assignment_reports
        ] = mock_rpc
        request = {}
        client.list_os_policy_assignment_reports(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_os_policy_assignment_reports(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_list_os_policy_assignment_reports_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = OsConfigZonalServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.list_os_policy_assignment_reports
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.list_os_policy_assignment_reports
        ] = mock_rpc

        request = {}
        await client.list_os_policy_assignment_reports(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.list_os_policy_assignment_reports(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        os_policy_assignment_reports.ListOSPolicyAssignmentReportsRequest(),
        {},
    ],
)
async def test_list_os_policy_assignment_reports_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_os_policy_assignment_reports), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            os_policy_assignment_reports.ListOSPolicyAssignmentReportsResponse(
                next_page_token="next_page_token_value",
            )
        )
        response = await client.list_os_policy_assignment_reports(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = os_policy_assignment_reports.ListOSPolicyAssignmentReportsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListOSPolicyAssignmentReportsAsyncPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_os_policy_assignment_reports_field_headers():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = os_policy_assignment_reports.ListOSPolicyAssignmentReportsRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_os_policy_assignment_reports), "__call__"
    ) as call:
        call.return_value = (
            os_policy_assignment_reports.ListOSPolicyAssignmentReportsResponse()
        )
        client.list_os_policy_assignment_reports(request)

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
async def test_list_os_policy_assignment_reports_field_headers_async():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = os_policy_assignment_reports.ListOSPolicyAssignmentReportsRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_os_policy_assignment_reports), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            os_policy_assignment_reports.ListOSPolicyAssignmentReportsResponse()
        )
        await client.list_os_policy_assignment_reports(request)

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


def test_list_os_policy_assignment_reports_flattened():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_os_policy_assignment_reports), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = (
            os_policy_assignment_reports.ListOSPolicyAssignmentReportsResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.list_os_policy_assignment_reports(
            parent="parent_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val


def test_list_os_policy_assignment_reports_flattened_error():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_os_policy_assignment_reports(
            os_policy_assignment_reports.ListOSPolicyAssignmentReportsRequest(),
            parent="parent_value",
        )


@pytest.mark.asyncio
async def test_list_os_policy_assignment_reports_flattened_async():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_os_policy_assignment_reports), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = (
            os_policy_assignment_reports.ListOSPolicyAssignmentReportsResponse()
        )

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            os_policy_assignment_reports.ListOSPolicyAssignmentReportsResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.list_os_policy_assignment_reports(
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
async def test_list_os_policy_assignment_reports_flattened_error_async():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.list_os_policy_assignment_reports(
            os_policy_assignment_reports.ListOSPolicyAssignmentReportsRequest(),
            parent="parent_value",
        )


def test_list_os_policy_assignment_reports_pager(transport_name: str = "grpc"):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_os_policy_assignment_reports), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            os_policy_assignment_reports.ListOSPolicyAssignmentReportsResponse(
                os_policy_assignment_reports=[
                    os_policy_assignment_reports.OSPolicyAssignmentReport(),
                    os_policy_assignment_reports.OSPolicyAssignmentReport(),
                    os_policy_assignment_reports.OSPolicyAssignmentReport(),
                ],
                next_page_token="abc",
            ),
            os_policy_assignment_reports.ListOSPolicyAssignmentReportsResponse(
                os_policy_assignment_reports=[],
                next_page_token="def",
            ),
            os_policy_assignment_reports.ListOSPolicyAssignmentReportsResponse(
                os_policy_assignment_reports=[
                    os_policy_assignment_reports.OSPolicyAssignmentReport(),
                ],
                next_page_token="ghi",
            ),
            os_policy_assignment_reports.ListOSPolicyAssignmentReportsResponse(
                os_policy_assignment_reports=[
                    os_policy_assignment_reports.OSPolicyAssignmentReport(),
                    os_policy_assignment_reports.OSPolicyAssignmentReport(),
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
        pager = client.list_os_policy_assignment_reports(
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
            isinstance(i, os_policy_assignment_reports.OSPolicyAssignmentReport)
            for i in results
        )


def test_list_os_policy_assignment_reports_pages(transport_name: str = "grpc"):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_os_policy_assignment_reports), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            os_policy_assignment_reports.ListOSPolicyAssignmentReportsResponse(
                os_policy_assignment_reports=[
                    os_policy_assignment_reports.OSPolicyAssignmentReport(),
                    os_policy_assignment_reports.OSPolicyAssignmentReport(),
                    os_policy_assignment_reports.OSPolicyAssignmentReport(),
                ],
                next_page_token="abc",
            ),
            os_policy_assignment_reports.ListOSPolicyAssignmentReportsResponse(
                os_policy_assignment_reports=[],
                next_page_token="def",
            ),
            os_policy_assignment_reports.ListOSPolicyAssignmentReportsResponse(
                os_policy_assignment_reports=[
                    os_policy_assignment_reports.OSPolicyAssignmentReport(),
                ],
                next_page_token="ghi",
            ),
            os_policy_assignment_reports.ListOSPolicyAssignmentReportsResponse(
                os_policy_assignment_reports=[
                    os_policy_assignment_reports.OSPolicyAssignmentReport(),
                    os_policy_assignment_reports.OSPolicyAssignmentReport(),
                ],
            ),
            RuntimeError,
        )
        pages = list(client.list_os_policy_assignment_reports(request={}).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.asyncio
async def test_list_os_policy_assignment_reports_async_pager():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_os_policy_assignment_reports),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            os_policy_assignment_reports.ListOSPolicyAssignmentReportsResponse(
                os_policy_assignment_reports=[
                    os_policy_assignment_reports.OSPolicyAssignmentReport(),
                    os_policy_assignment_reports.OSPolicyAssignmentReport(),
                    os_policy_assignment_reports.OSPolicyAssignmentReport(),
                ],
                next_page_token="abc",
            ),
            os_policy_assignment_reports.ListOSPolicyAssignmentReportsResponse(
                os_policy_assignment_reports=[],
                next_page_token="def",
            ),
            os_policy_assignment_reports.ListOSPolicyAssignmentReportsResponse(
                os_policy_assignment_reports=[
                    os_policy_assignment_reports.OSPolicyAssignmentReport(),
                ],
                next_page_token="ghi",
            ),
            os_policy_assignment_reports.ListOSPolicyAssignmentReportsResponse(
                os_policy_assignment_reports=[
                    os_policy_assignment_reports.OSPolicyAssignmentReport(),
                    os_policy_assignment_reports.OSPolicyAssignmentReport(),
                ],
            ),
            RuntimeError,
        )
        async_pager = await client.list_os_policy_assignment_reports(
            request={},
        )
        assert async_pager.next_page_token == "abc"
        assert str(async_pager).startswith(f"{async_pager.__class__.__name__}<")

        responses = []
        async for response in async_pager:  # pragma: no branch
            responses.append(response)

        assert len(responses) == 6
        assert all(
            isinstance(i, os_policy_assignment_reports.OSPolicyAssignmentReport)
            for i in responses
        )


@pytest.mark.asyncio
async def test_list_os_policy_assignment_reports_async_pages():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_os_policy_assignment_reports),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            os_policy_assignment_reports.ListOSPolicyAssignmentReportsResponse(
                os_policy_assignment_reports=[
                    os_policy_assignment_reports.OSPolicyAssignmentReport(),
                    os_policy_assignment_reports.OSPolicyAssignmentReport(),
                    os_policy_assignment_reports.OSPolicyAssignmentReport(),
                ],
                next_page_token="abc",
            ),
            os_policy_assignment_reports.ListOSPolicyAssignmentReportsResponse(
                os_policy_assignment_reports=[],
                next_page_token="def",
            ),
            os_policy_assignment_reports.ListOSPolicyAssignmentReportsResponse(
                os_policy_assignment_reports=[
                    os_policy_assignment_reports.OSPolicyAssignmentReport(),
                ],
                next_page_token="ghi",
            ),
            os_policy_assignment_reports.ListOSPolicyAssignmentReportsResponse(
                os_policy_assignment_reports=[
                    os_policy_assignment_reports.OSPolicyAssignmentReport(),
                    os_policy_assignment_reports.OSPolicyAssignmentReport(),
                ],
            ),
            RuntimeError,
        )
        pages = []
        async for page_ in (
            await client.list_os_policy_assignment_reports(request={})
        ).pages:
            pages.append(page_)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.parametrize(
    "request_type",
    [
        inventory.GetInventoryRequest(),
        {},
    ],
)
def test_get_inventory(request_type, transport: str = "grpc"):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_inventory), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = inventory.Inventory(
            name="name_value",
        )
        response = client.get_inventory(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = inventory.GetInventoryRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, inventory.Inventory)
    assert response.name == "name_value"


def test_get_inventory_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = inventory.GetInventoryRequest(
        name="name_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_inventory), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.get_inventory(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = inventory.GetInventoryRequest(
            name="name_value",
        )
        assert args[0] == request_msg


def test_get_inventory_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = OsConfigZonalServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.get_inventory in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.get_inventory] = mock_rpc
        request = {}
        client.get_inventory(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_inventory(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_get_inventory_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = OsConfigZonalServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.get_inventory
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.get_inventory
        ] = mock_rpc

        request = {}
        await client.get_inventory(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.get_inventory(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        inventory.GetInventoryRequest(),
        {},
    ],
)
async def test_get_inventory_async(request_type, transport: str = "grpc_asyncio"):
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_inventory), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            inventory.Inventory(
                name="name_value",
            )
        )
        response = await client.get_inventory(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = inventory.GetInventoryRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, inventory.Inventory)
    assert response.name == "name_value"


def test_get_inventory_field_headers():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = inventory.GetInventoryRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_inventory), "__call__") as call:
        call.return_value = inventory.Inventory()
        client.get_inventory(request)

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
async def test_get_inventory_field_headers_async():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = inventory.GetInventoryRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_inventory), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(inventory.Inventory())
        await client.get_inventory(request)

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


def test_get_inventory_flattened():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_inventory), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = inventory.Inventory()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.get_inventory(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_get_inventory_flattened_error():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_inventory(
            inventory.GetInventoryRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_get_inventory_flattened_async():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_inventory), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = inventory.Inventory()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(inventory.Inventory())
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.get_inventory(
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
async def test_get_inventory_flattened_error_async():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.get_inventory(
            inventory.GetInventoryRequest(),
            name="name_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        inventory.ListInventoriesRequest(),
        {},
    ],
)
def test_list_inventories(request_type, transport: str = "grpc"):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_inventories), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = inventory.ListInventoriesResponse(
            next_page_token="next_page_token_value",
        )
        response = client.list_inventories(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = inventory.ListInventoriesRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListInventoriesPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_inventories_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = inventory.ListInventoriesRequest(
        parent="parent_value",
        page_token="page_token_value",
        filter="filter_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_inventories), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.list_inventories(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = inventory.ListInventoriesRequest(
            parent="parent_value",
            page_token="page_token_value",
            filter="filter_value",
        )
        assert args[0] == request_msg


def test_list_inventories_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = OsConfigZonalServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.list_inventories in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.list_inventories] = (
            mock_rpc
        )
        request = {}
        client.list_inventories(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_inventories(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_list_inventories_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = OsConfigZonalServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.list_inventories
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.list_inventories
        ] = mock_rpc

        request = {}
        await client.list_inventories(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.list_inventories(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        inventory.ListInventoriesRequest(),
        {},
    ],
)
async def test_list_inventories_async(request_type, transport: str = "grpc_asyncio"):
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_inventories), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            inventory.ListInventoriesResponse(
                next_page_token="next_page_token_value",
            )
        )
        response = await client.list_inventories(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = inventory.ListInventoriesRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListInventoriesAsyncPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_inventories_field_headers():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = inventory.ListInventoriesRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_inventories), "__call__") as call:
        call.return_value = inventory.ListInventoriesResponse()
        client.list_inventories(request)

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
async def test_list_inventories_field_headers_async():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = inventory.ListInventoriesRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_inventories), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            inventory.ListInventoriesResponse()
        )
        await client.list_inventories(request)

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


def test_list_inventories_flattened():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_inventories), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = inventory.ListInventoriesResponse()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.list_inventories(
            parent="parent_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val


def test_list_inventories_flattened_error():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_inventories(
            inventory.ListInventoriesRequest(),
            parent="parent_value",
        )


@pytest.mark.asyncio
async def test_list_inventories_flattened_async():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_inventories), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = inventory.ListInventoriesResponse()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            inventory.ListInventoriesResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.list_inventories(
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
async def test_list_inventories_flattened_error_async():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.list_inventories(
            inventory.ListInventoriesRequest(),
            parent="parent_value",
        )


def test_list_inventories_pager(transport_name: str = "grpc"):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_inventories), "__call__") as call:
        # Set the response to a series of pages.
        call.side_effect = (
            inventory.ListInventoriesResponse(
                inventories=[
                    inventory.Inventory(),
                    inventory.Inventory(),
                    inventory.Inventory(),
                ],
                next_page_token="abc",
            ),
            inventory.ListInventoriesResponse(
                inventories=[],
                next_page_token="def",
            ),
            inventory.ListInventoriesResponse(
                inventories=[
                    inventory.Inventory(),
                ],
                next_page_token="ghi",
            ),
            inventory.ListInventoriesResponse(
                inventories=[
                    inventory.Inventory(),
                    inventory.Inventory(),
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
        pager = client.list_inventories(request={}, retry=retry, timeout=timeout)

        assert pager._metadata == expected_metadata
        assert pager._retry == retry
        assert pager._timeout == timeout

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, inventory.Inventory) for i in results)


def test_list_inventories_pages(transport_name: str = "grpc"):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_inventories), "__call__") as call:
        # Set the response to a series of pages.
        call.side_effect = (
            inventory.ListInventoriesResponse(
                inventories=[
                    inventory.Inventory(),
                    inventory.Inventory(),
                    inventory.Inventory(),
                ],
                next_page_token="abc",
            ),
            inventory.ListInventoriesResponse(
                inventories=[],
                next_page_token="def",
            ),
            inventory.ListInventoriesResponse(
                inventories=[
                    inventory.Inventory(),
                ],
                next_page_token="ghi",
            ),
            inventory.ListInventoriesResponse(
                inventories=[
                    inventory.Inventory(),
                    inventory.Inventory(),
                ],
            ),
            RuntimeError,
        )
        pages = list(client.list_inventories(request={}).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.asyncio
async def test_list_inventories_async_pager():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_inventories), "__call__", new_callable=mock.AsyncMock
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            inventory.ListInventoriesResponse(
                inventories=[
                    inventory.Inventory(),
                    inventory.Inventory(),
                    inventory.Inventory(),
                ],
                next_page_token="abc",
            ),
            inventory.ListInventoriesResponse(
                inventories=[],
                next_page_token="def",
            ),
            inventory.ListInventoriesResponse(
                inventories=[
                    inventory.Inventory(),
                ],
                next_page_token="ghi",
            ),
            inventory.ListInventoriesResponse(
                inventories=[
                    inventory.Inventory(),
                    inventory.Inventory(),
                ],
            ),
            RuntimeError,
        )
        async_pager = await client.list_inventories(
            request={},
        )
        assert async_pager.next_page_token == "abc"
        assert str(async_pager).startswith(f"{async_pager.__class__.__name__}<")

        responses = []
        async for response in async_pager:  # pragma: no branch
            responses.append(response)

        assert len(responses) == 6
        assert all(isinstance(i, inventory.Inventory) for i in responses)


@pytest.mark.asyncio
async def test_list_inventories_async_pages():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_inventories), "__call__", new_callable=mock.AsyncMock
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            inventory.ListInventoriesResponse(
                inventories=[
                    inventory.Inventory(),
                    inventory.Inventory(),
                    inventory.Inventory(),
                ],
                next_page_token="abc",
            ),
            inventory.ListInventoriesResponse(
                inventories=[],
                next_page_token="def",
            ),
            inventory.ListInventoriesResponse(
                inventories=[
                    inventory.Inventory(),
                ],
                next_page_token="ghi",
            ),
            inventory.ListInventoriesResponse(
                inventories=[
                    inventory.Inventory(),
                    inventory.Inventory(),
                ],
            ),
            RuntimeError,
        )
        pages = []
        async for page_ in (await client.list_inventories(request={})).pages:
            pages.append(page_)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.parametrize(
    "request_type",
    [
        vulnerability.GetVulnerabilityReportRequest(),
        {},
    ],
)
def test_get_vulnerability_report(request_type, transport: str = "grpc"):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_vulnerability_report), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = vulnerability.VulnerabilityReport(
            name="name_value",
        )
        response = client.get_vulnerability_report(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = vulnerability.GetVulnerabilityReportRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, vulnerability.VulnerabilityReport)
    assert response.name == "name_value"


def test_get_vulnerability_report_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = vulnerability.GetVulnerabilityReportRequest(
        name="name_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_vulnerability_report), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.get_vulnerability_report(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = vulnerability.GetVulnerabilityReportRequest(
            name="name_value",
        )
        assert args[0] == request_msg


def test_get_vulnerability_report_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = OsConfigZonalServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.get_vulnerability_report
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.get_vulnerability_report
        ] = mock_rpc
        request = {}
        client.get_vulnerability_report(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_vulnerability_report(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_get_vulnerability_report_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = OsConfigZonalServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.get_vulnerability_report
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.get_vulnerability_report
        ] = mock_rpc

        request = {}
        await client.get_vulnerability_report(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.get_vulnerability_report(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        vulnerability.GetVulnerabilityReportRequest(),
        {},
    ],
)
async def test_get_vulnerability_report_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_vulnerability_report), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            vulnerability.VulnerabilityReport(
                name="name_value",
            )
        )
        response = await client.get_vulnerability_report(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = vulnerability.GetVulnerabilityReportRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, vulnerability.VulnerabilityReport)
    assert response.name == "name_value"


def test_get_vulnerability_report_field_headers():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = vulnerability.GetVulnerabilityReportRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_vulnerability_report), "__call__"
    ) as call:
        call.return_value = vulnerability.VulnerabilityReport()
        client.get_vulnerability_report(request)

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
async def test_get_vulnerability_report_field_headers_async():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = vulnerability.GetVulnerabilityReportRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_vulnerability_report), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            vulnerability.VulnerabilityReport()
        )
        await client.get_vulnerability_report(request)

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


def test_get_vulnerability_report_flattened():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_vulnerability_report), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = vulnerability.VulnerabilityReport()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.get_vulnerability_report(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_get_vulnerability_report_flattened_error():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_vulnerability_report(
            vulnerability.GetVulnerabilityReportRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_get_vulnerability_report_flattened_async():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_vulnerability_report), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = vulnerability.VulnerabilityReport()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            vulnerability.VulnerabilityReport()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.get_vulnerability_report(
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
async def test_get_vulnerability_report_flattened_error_async():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.get_vulnerability_report(
            vulnerability.GetVulnerabilityReportRequest(),
            name="name_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        vulnerability.ListVulnerabilityReportsRequest(),
        {},
    ],
)
def test_list_vulnerability_reports(request_type, transport: str = "grpc"):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_vulnerability_reports), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = vulnerability.ListVulnerabilityReportsResponse(
            next_page_token="next_page_token_value",
        )
        response = client.list_vulnerability_reports(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = vulnerability.ListVulnerabilityReportsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListVulnerabilityReportsPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_vulnerability_reports_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = vulnerability.ListVulnerabilityReportsRequest(
        parent="parent_value",
        page_token="page_token_value",
        filter="filter_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_vulnerability_reports), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.list_vulnerability_reports(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = vulnerability.ListVulnerabilityReportsRequest(
            parent="parent_value",
            page_token="page_token_value",
            filter="filter_value",
        )
        assert args[0] == request_msg


def test_list_vulnerability_reports_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = OsConfigZonalServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.list_vulnerability_reports
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.list_vulnerability_reports
        ] = mock_rpc
        request = {}
        client.list_vulnerability_reports(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_vulnerability_reports(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_list_vulnerability_reports_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = OsConfigZonalServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.list_vulnerability_reports
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.list_vulnerability_reports
        ] = mock_rpc

        request = {}
        await client.list_vulnerability_reports(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.list_vulnerability_reports(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        vulnerability.ListVulnerabilityReportsRequest(),
        {},
    ],
)
async def test_list_vulnerability_reports_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_vulnerability_reports), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            vulnerability.ListVulnerabilityReportsResponse(
                next_page_token="next_page_token_value",
            )
        )
        response = await client.list_vulnerability_reports(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = vulnerability.ListVulnerabilityReportsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListVulnerabilityReportsAsyncPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_vulnerability_reports_field_headers():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = vulnerability.ListVulnerabilityReportsRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_vulnerability_reports), "__call__"
    ) as call:
        call.return_value = vulnerability.ListVulnerabilityReportsResponse()
        client.list_vulnerability_reports(request)

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
async def test_list_vulnerability_reports_field_headers_async():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = vulnerability.ListVulnerabilityReportsRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_vulnerability_reports), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            vulnerability.ListVulnerabilityReportsResponse()
        )
        await client.list_vulnerability_reports(request)

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


def test_list_vulnerability_reports_flattened():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_vulnerability_reports), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = vulnerability.ListVulnerabilityReportsResponse()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.list_vulnerability_reports(
            parent="parent_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val


def test_list_vulnerability_reports_flattened_error():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_vulnerability_reports(
            vulnerability.ListVulnerabilityReportsRequest(),
            parent="parent_value",
        )


@pytest.mark.asyncio
async def test_list_vulnerability_reports_flattened_async():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_vulnerability_reports), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = vulnerability.ListVulnerabilityReportsResponse()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            vulnerability.ListVulnerabilityReportsResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.list_vulnerability_reports(
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
async def test_list_vulnerability_reports_flattened_error_async():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.list_vulnerability_reports(
            vulnerability.ListVulnerabilityReportsRequest(),
            parent="parent_value",
        )


def test_list_vulnerability_reports_pager(transport_name: str = "grpc"):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_vulnerability_reports), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            vulnerability.ListVulnerabilityReportsResponse(
                vulnerability_reports=[
                    vulnerability.VulnerabilityReport(),
                    vulnerability.VulnerabilityReport(),
                    vulnerability.VulnerabilityReport(),
                ],
                next_page_token="abc",
            ),
            vulnerability.ListVulnerabilityReportsResponse(
                vulnerability_reports=[],
                next_page_token="def",
            ),
            vulnerability.ListVulnerabilityReportsResponse(
                vulnerability_reports=[
                    vulnerability.VulnerabilityReport(),
                ],
                next_page_token="ghi",
            ),
            vulnerability.ListVulnerabilityReportsResponse(
                vulnerability_reports=[
                    vulnerability.VulnerabilityReport(),
                    vulnerability.VulnerabilityReport(),
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
        pager = client.list_vulnerability_reports(
            request={}, retry=retry, timeout=timeout
        )

        assert pager._metadata == expected_metadata
        assert pager._retry == retry
        assert pager._timeout == timeout

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, vulnerability.VulnerabilityReport) for i in results)


def test_list_vulnerability_reports_pages(transport_name: str = "grpc"):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_vulnerability_reports), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            vulnerability.ListVulnerabilityReportsResponse(
                vulnerability_reports=[
                    vulnerability.VulnerabilityReport(),
                    vulnerability.VulnerabilityReport(),
                    vulnerability.VulnerabilityReport(),
                ],
                next_page_token="abc",
            ),
            vulnerability.ListVulnerabilityReportsResponse(
                vulnerability_reports=[],
                next_page_token="def",
            ),
            vulnerability.ListVulnerabilityReportsResponse(
                vulnerability_reports=[
                    vulnerability.VulnerabilityReport(),
                ],
                next_page_token="ghi",
            ),
            vulnerability.ListVulnerabilityReportsResponse(
                vulnerability_reports=[
                    vulnerability.VulnerabilityReport(),
                    vulnerability.VulnerabilityReport(),
                ],
            ),
            RuntimeError,
        )
        pages = list(client.list_vulnerability_reports(request={}).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.asyncio
async def test_list_vulnerability_reports_async_pager():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_vulnerability_reports),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            vulnerability.ListVulnerabilityReportsResponse(
                vulnerability_reports=[
                    vulnerability.VulnerabilityReport(),
                    vulnerability.VulnerabilityReport(),
                    vulnerability.VulnerabilityReport(),
                ],
                next_page_token="abc",
            ),
            vulnerability.ListVulnerabilityReportsResponse(
                vulnerability_reports=[],
                next_page_token="def",
            ),
            vulnerability.ListVulnerabilityReportsResponse(
                vulnerability_reports=[
                    vulnerability.VulnerabilityReport(),
                ],
                next_page_token="ghi",
            ),
            vulnerability.ListVulnerabilityReportsResponse(
                vulnerability_reports=[
                    vulnerability.VulnerabilityReport(),
                    vulnerability.VulnerabilityReport(),
                ],
            ),
            RuntimeError,
        )
        async_pager = await client.list_vulnerability_reports(
            request={},
        )
        assert async_pager.next_page_token == "abc"
        assert str(async_pager).startswith(f"{async_pager.__class__.__name__}<")

        responses = []
        async for response in async_pager:  # pragma: no branch
            responses.append(response)

        assert len(responses) == 6
        assert all(isinstance(i, vulnerability.VulnerabilityReport) for i in responses)


@pytest.mark.asyncio
async def test_list_vulnerability_reports_async_pages():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_vulnerability_reports),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            vulnerability.ListVulnerabilityReportsResponse(
                vulnerability_reports=[
                    vulnerability.VulnerabilityReport(),
                    vulnerability.VulnerabilityReport(),
                    vulnerability.VulnerabilityReport(),
                ],
                next_page_token="abc",
            ),
            vulnerability.ListVulnerabilityReportsResponse(
                vulnerability_reports=[],
                next_page_token="def",
            ),
            vulnerability.ListVulnerabilityReportsResponse(
                vulnerability_reports=[
                    vulnerability.VulnerabilityReport(),
                ],
                next_page_token="ghi",
            ),
            vulnerability.ListVulnerabilityReportsResponse(
                vulnerability_reports=[
                    vulnerability.VulnerabilityReport(),
                    vulnerability.VulnerabilityReport(),
                ],
            ),
            RuntimeError,
        )
        pages = []
        async for page_ in (await client.list_vulnerability_reports(request={})).pages:
            pages.append(page_)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


def test_create_os_policy_assignment_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = OsConfigZonalServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.create_os_policy_assignment
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.create_os_policy_assignment
        ] = mock_rpc

        request = {}
        client.create_os_policy_assignment(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods build a cached wrapper on first rpc call
        # subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.create_os_policy_assignment(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_create_os_policy_assignment_rest_required_fields(
    request_type=os_policy_assignments.CreateOSPolicyAssignmentRequest,
):
    transport_class = transports.OsConfigZonalServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request_init["os_policy_assignment_id"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped
    assert "osPolicyAssignmentId" not in jsonified_request

    default_values = getattr(
        transport_class._BaseCreateOSPolicyAssignment,
        "_BaseCreateOSPolicyAssignment__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present
    assert "osPolicyAssignmentId" in jsonified_request
    assert (
        jsonified_request["osPolicyAssignmentId"]
        == request_init["os_policy_assignment_id"]
    )

    jsonified_request["parent"] = "parent_value"
    jsonified_request["osPolicyAssignmentId"] = "os_policy_assignment_id_value"

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(("osPolicyAssignmentId",))

    # verify required fields with non-default values are left alone
    assert "parent" in jsonified_request
    assert jsonified_request["parent"] == "parent_value"
    assert "osPolicyAssignmentId" in jsonified_request
    assert jsonified_request["osPolicyAssignmentId"] == "os_policy_assignment_id_value"

    client = OsConfigZonalServiceClient(
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

            response = client.create_os_policy_assignment(request)

            expected_params = [
                (
                    "osPolicyAssignmentId",
                    "",
                ),
                ("$alt", "json;enum-encoding=int"),
            ]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_create_os_policy_assignment_rest_flattened():
    client = OsConfigZonalServiceClient(
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
            os_policy_assignment=os_policy_assignments.OSPolicyAssignment(
                name="name_value"
            ),
            os_policy_assignment_id="os_policy_assignment_id_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.create_os_policy_assignment(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1alpha/{parent=projects/*/locations/*}/osPolicyAssignments"
            % client.transport._host,
            args[1],
        )


def test_create_os_policy_assignment_rest_flattened_error(transport: str = "rest"):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.create_os_policy_assignment(
            os_policy_assignments.CreateOSPolicyAssignmentRequest(),
            parent="parent_value",
            os_policy_assignment=os_policy_assignments.OSPolicyAssignment(
                name="name_value"
            ),
            os_policy_assignment_id="os_policy_assignment_id_value",
        )


def test_update_os_policy_assignment_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = OsConfigZonalServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.update_os_policy_assignment
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.update_os_policy_assignment
        ] = mock_rpc

        request = {}
        client.update_os_policy_assignment(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods build a cached wrapper on first rpc call
        # subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.update_os_policy_assignment(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_update_os_policy_assignment_rest_required_fields(
    request_type=os_policy_assignments.UpdateOSPolicyAssignmentRequest,
):
    transport_class = transports.OsConfigZonalServiceRestTransport

    request_init = {}
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseUpdateOSPolicyAssignment,
        "_BaseUpdateOSPolicyAssignment__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = OsConfigZonalServiceClient(
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

            response = client.update_os_policy_assignment(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_update_os_policy_assignment_rest_flattened():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = operations_pb2.Operation(name="operations/spam")

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "os_policy_assignment": {
                "name": "projects/sample1/locations/sample2/osPolicyAssignments/sample3"
            }
        }

        # get truthy value for each flattened field
        mock_args = dict(
            os_policy_assignment=os_policy_assignments.OSPolicyAssignment(
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

        client.update_os_policy_assignment(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1alpha/{os_policy_assignment.name=projects/*/locations/*/osPolicyAssignments/*}"
            % client.transport._host,
            args[1],
        )


def test_update_os_policy_assignment_rest_flattened_error(transport: str = "rest"):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.update_os_policy_assignment(
            os_policy_assignments.UpdateOSPolicyAssignmentRequest(),
            os_policy_assignment=os_policy_assignments.OSPolicyAssignment(
                name="name_value"
            ),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


def test_get_os_policy_assignment_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = OsConfigZonalServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.get_os_policy_assignment
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.get_os_policy_assignment
        ] = mock_rpc

        request = {}
        client.get_os_policy_assignment(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_os_policy_assignment(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_get_os_policy_assignment_rest_required_fields(
    request_type=os_policy_assignments.GetOSPolicyAssignmentRequest,
):
    transport_class = transports.OsConfigZonalServiceRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseGetOSPolicyAssignment,
        "_BaseGetOSPolicyAssignment__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = os_policy_assignments.OSPolicyAssignment()
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
            return_value = os_policy_assignments.OSPolicyAssignment.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.get_os_policy_assignment(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_get_os_policy_assignment_rest_flattened():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = os_policy_assignments.OSPolicyAssignment()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "name": "projects/sample1/locations/sample2/osPolicyAssignments/sample3"
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
        return_value = os_policy_assignments.OSPolicyAssignment.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.get_os_policy_assignment(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1alpha/{name=projects/*/locations/*/osPolicyAssignments/*}"
            % client.transport._host,
            args[1],
        )


def test_get_os_policy_assignment_rest_flattened_error(transport: str = "rest"):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_os_policy_assignment(
            os_policy_assignments.GetOSPolicyAssignmentRequest(),
            name="name_value",
        )


def test_list_os_policy_assignments_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = OsConfigZonalServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.list_os_policy_assignments
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.list_os_policy_assignments
        ] = mock_rpc

        request = {}
        client.list_os_policy_assignments(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_os_policy_assignments(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_list_os_policy_assignments_rest_required_fields(
    request_type=os_policy_assignments.ListOSPolicyAssignmentsRequest,
):
    transport_class = transports.OsConfigZonalServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseListOSPolicyAssignments,
        "_BaseListOSPolicyAssignments__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = os_policy_assignments.ListOSPolicyAssignmentsResponse()
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
            return_value = os_policy_assignments.ListOSPolicyAssignmentsResponse.pb(
                return_value
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.list_os_policy_assignments(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_list_os_policy_assignments_rest_flattened():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = os_policy_assignments.ListOSPolicyAssignmentsResponse()

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
        return_value = os_policy_assignments.ListOSPolicyAssignmentsResponse.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.list_os_policy_assignments(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1alpha/{parent=projects/*/locations/*}/osPolicyAssignments"
            % client.transport._host,
            args[1],
        )


def test_list_os_policy_assignments_rest_flattened_error(transport: str = "rest"):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_os_policy_assignments(
            os_policy_assignments.ListOSPolicyAssignmentsRequest(),
            parent="parent_value",
        )


def test_list_os_policy_assignments_rest_pager(transport: str = "rest"):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        # with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            os_policy_assignments.ListOSPolicyAssignmentsResponse(
                os_policy_assignments=[
                    os_policy_assignments.OSPolicyAssignment(),
                    os_policy_assignments.OSPolicyAssignment(),
                    os_policy_assignments.OSPolicyAssignment(),
                ],
                next_page_token="abc",
            ),
            os_policy_assignments.ListOSPolicyAssignmentsResponse(
                os_policy_assignments=[],
                next_page_token="def",
            ),
            os_policy_assignments.ListOSPolicyAssignmentsResponse(
                os_policy_assignments=[
                    os_policy_assignments.OSPolicyAssignment(),
                ],
                next_page_token="ghi",
            ),
            os_policy_assignments.ListOSPolicyAssignmentsResponse(
                os_policy_assignments=[
                    os_policy_assignments.OSPolicyAssignment(),
                    os_policy_assignments.OSPolicyAssignment(),
                ],
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(
            os_policy_assignments.ListOSPolicyAssignmentsResponse.to_json(x)
            for x in response
        )
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode("UTF-8")
            return_val.status_code = 200
        req.side_effect = return_values

        sample_request = {"parent": "projects/sample1/locations/sample2"}

        pager = client.list_os_policy_assignments(request=sample_request)

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(
            isinstance(i, os_policy_assignments.OSPolicyAssignment) for i in results
        )

        pages = list(client.list_os_policy_assignments(request=sample_request).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


def test_list_os_policy_assignment_revisions_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = OsConfigZonalServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.list_os_policy_assignment_revisions
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.list_os_policy_assignment_revisions
        ] = mock_rpc

        request = {}
        client.list_os_policy_assignment_revisions(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_os_policy_assignment_revisions(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_list_os_policy_assignment_revisions_rest_required_fields(
    request_type=os_policy_assignments.ListOSPolicyAssignmentRevisionsRequest,
):
    transport_class = transports.OsConfigZonalServiceRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseListOSPolicyAssignmentRevisions,
        "_BaseListOSPolicyAssignmentRevisions__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = os_policy_assignments.ListOSPolicyAssignmentRevisionsResponse()
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
                os_policy_assignments.ListOSPolicyAssignmentRevisionsResponse.pb(
                    return_value
                )
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.list_os_policy_assignment_revisions(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_list_os_policy_assignment_revisions_rest_flattened():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = os_policy_assignments.ListOSPolicyAssignmentRevisionsResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "name": "projects/sample1/locations/sample2/osPolicyAssignments/sample3"
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
        return_value = os_policy_assignments.ListOSPolicyAssignmentRevisionsResponse.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.list_os_policy_assignment_revisions(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1alpha/{name=projects/*/locations/*/osPolicyAssignments/*}:listRevisions"
            % client.transport._host,
            args[1],
        )


def test_list_os_policy_assignment_revisions_rest_flattened_error(
    transport: str = "rest",
):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_os_policy_assignment_revisions(
            os_policy_assignments.ListOSPolicyAssignmentRevisionsRequest(),
            name="name_value",
        )


def test_list_os_policy_assignment_revisions_rest_pager(transport: str = "rest"):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        # with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            os_policy_assignments.ListOSPolicyAssignmentRevisionsResponse(
                os_policy_assignments=[
                    os_policy_assignments.OSPolicyAssignment(),
                    os_policy_assignments.OSPolicyAssignment(),
                    os_policy_assignments.OSPolicyAssignment(),
                ],
                next_page_token="abc",
            ),
            os_policy_assignments.ListOSPolicyAssignmentRevisionsResponse(
                os_policy_assignments=[],
                next_page_token="def",
            ),
            os_policy_assignments.ListOSPolicyAssignmentRevisionsResponse(
                os_policy_assignments=[
                    os_policy_assignments.OSPolicyAssignment(),
                ],
                next_page_token="ghi",
            ),
            os_policy_assignments.ListOSPolicyAssignmentRevisionsResponse(
                os_policy_assignments=[
                    os_policy_assignments.OSPolicyAssignment(),
                    os_policy_assignments.OSPolicyAssignment(),
                ],
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(
            os_policy_assignments.ListOSPolicyAssignmentRevisionsResponse.to_json(x)
            for x in response
        )
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode("UTF-8")
            return_val.status_code = 200
        req.side_effect = return_values

        sample_request = {
            "name": "projects/sample1/locations/sample2/osPolicyAssignments/sample3"
        }

        pager = client.list_os_policy_assignment_revisions(request=sample_request)

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(
            isinstance(i, os_policy_assignments.OSPolicyAssignment) for i in results
        )

        pages = list(
            client.list_os_policy_assignment_revisions(request=sample_request).pages
        )
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


def test_delete_os_policy_assignment_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = OsConfigZonalServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.delete_os_policy_assignment
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.delete_os_policy_assignment
        ] = mock_rpc

        request = {}
        client.delete_os_policy_assignment(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods build a cached wrapper on first rpc call
        # subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.delete_os_policy_assignment(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_delete_os_policy_assignment_rest_required_fields(
    request_type=os_policy_assignments.DeleteOSPolicyAssignmentRequest,
):
    transport_class = transports.OsConfigZonalServiceRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseDeleteOSPolicyAssignment,
        "_BaseDeleteOSPolicyAssignment__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = OsConfigZonalServiceClient(
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

            response = client.delete_os_policy_assignment(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_delete_os_policy_assignment_rest_flattened():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = operations_pb2.Operation(name="operations/spam")

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "name": "projects/sample1/locations/sample2/osPolicyAssignments/sample3"
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

        client.delete_os_policy_assignment(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1alpha/{name=projects/*/locations/*/osPolicyAssignments/*}"
            % client.transport._host,
            args[1],
        )


def test_delete_os_policy_assignment_rest_flattened_error(transport: str = "rest"):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.delete_os_policy_assignment(
            os_policy_assignments.DeleteOSPolicyAssignmentRequest(),
            name="name_value",
        )


def test_get_instance_os_policies_compliance_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = OsConfigZonalServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.get_instance_os_policies_compliance
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.get_instance_os_policies_compliance
        ] = mock_rpc

        request = {}
        client.get_instance_os_policies_compliance(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_instance_os_policies_compliance(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_get_instance_os_policies_compliance_rest_required_fields(
    request_type=instance_os_policies_compliance.GetInstanceOSPoliciesComplianceRequest,
):
    transport_class = transports.OsConfigZonalServiceRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseGetInstanceOSPoliciesCompliance,
        "_BaseGetInstanceOSPoliciesCompliance__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = instance_os_policies_compliance.InstanceOSPoliciesCompliance()
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
                instance_os_policies_compliance.InstanceOSPoliciesCompliance.pb(
                    return_value
                )
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.get_instance_os_policies_compliance(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_get_instance_os_policies_compliance_rest_flattened():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = instance_os_policies_compliance.InstanceOSPoliciesCompliance()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "name": "projects/sample1/locations/sample2/instanceOSPoliciesCompliances/sample3"
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
        return_value = instance_os_policies_compliance.InstanceOSPoliciesCompliance.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.get_instance_os_policies_compliance(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1alpha/{name=projects/*/locations/*/instanceOSPoliciesCompliances/*}"
            % client.transport._host,
            args[1],
        )


def test_get_instance_os_policies_compliance_rest_flattened_error(
    transport: str = "rest",
):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_instance_os_policies_compliance(
            instance_os_policies_compliance.GetInstanceOSPoliciesComplianceRequest(),
            name="name_value",
        )


def test_list_instance_os_policies_compliances_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = OsConfigZonalServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.list_instance_os_policies_compliances
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.list_instance_os_policies_compliances
        ] = mock_rpc

        request = {}
        client.list_instance_os_policies_compliances(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_instance_os_policies_compliances(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_list_instance_os_policies_compliances_rest_required_fields(
    request_type=instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesRequest,
):
    transport_class = transports.OsConfigZonalServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseListInstanceOSPoliciesCompliances,
        "_BaseListInstanceOSPoliciesCompliances__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = (
        instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesResponse()
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
            return_value = instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesResponse.pb(
                return_value
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.list_instance_os_policies_compliances(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_list_instance_os_policies_compliances_rest_flattened():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = (
            instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesResponse()
        )

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
        return_value = instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesResponse.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.list_instance_os_policies_compliances(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1alpha/{parent=projects/*/locations/*}/instanceOSPoliciesCompliances"
            % client.transport._host,
            args[1],
        )


def test_list_instance_os_policies_compliances_rest_flattened_error(
    transport: str = "rest",
):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_instance_os_policies_compliances(
            instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesRequest(),
            parent="parent_value",
        )


def test_list_instance_os_policies_compliances_rest_pager(transport: str = "rest"):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        # with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesResponse(
                instance_os_policies_compliances=[
                    instance_os_policies_compliance.InstanceOSPoliciesCompliance(),
                    instance_os_policies_compliance.InstanceOSPoliciesCompliance(),
                    instance_os_policies_compliance.InstanceOSPoliciesCompliance(),
                ],
                next_page_token="abc",
            ),
            instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesResponse(
                instance_os_policies_compliances=[],
                next_page_token="def",
            ),
            instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesResponse(
                instance_os_policies_compliances=[
                    instance_os_policies_compliance.InstanceOSPoliciesCompliance(),
                ],
                next_page_token="ghi",
            ),
            instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesResponse(
                instance_os_policies_compliances=[
                    instance_os_policies_compliance.InstanceOSPoliciesCompliance(),
                    instance_os_policies_compliance.InstanceOSPoliciesCompliance(),
                ],
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(
            instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesResponse.to_json(
                x
            )
            for x in response
        )
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode("UTF-8")
            return_val.status_code = 200
        req.side_effect = return_values

        sample_request = {"parent": "projects/sample1/locations/sample2"}

        pager = client.list_instance_os_policies_compliances(request=sample_request)

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(
            isinstance(i, instance_os_policies_compliance.InstanceOSPoliciesCompliance)
            for i in results
        )

        pages = list(
            client.list_instance_os_policies_compliances(request=sample_request).pages
        )
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


def test_get_os_policy_assignment_report_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = OsConfigZonalServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.get_os_policy_assignment_report
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.get_os_policy_assignment_report
        ] = mock_rpc

        request = {}
        client.get_os_policy_assignment_report(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_os_policy_assignment_report(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_get_os_policy_assignment_report_rest_required_fields(
    request_type=os_policy_assignment_reports.GetOSPolicyAssignmentReportRequest,
):
    transport_class = transports.OsConfigZonalServiceRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseGetOSPolicyAssignmentReport,
        "_BaseGetOSPolicyAssignmentReport__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = os_policy_assignment_reports.OSPolicyAssignmentReport()
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
            return_value = os_policy_assignment_reports.OSPolicyAssignmentReport.pb(
                return_value
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.get_os_policy_assignment_report(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_get_os_policy_assignment_report_rest_flattened():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = os_policy_assignment_reports.OSPolicyAssignmentReport()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "name": "projects/sample1/locations/sample2/instances/sample3/osPolicyAssignments/sample4/report"
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
        return_value = os_policy_assignment_reports.OSPolicyAssignmentReport.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.get_os_policy_assignment_report(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1alpha/{name=projects/*/locations/*/instances/*/osPolicyAssignments/*/report}"
            % client.transport._host,
            args[1],
        )


def test_get_os_policy_assignment_report_rest_flattened_error(transport: str = "rest"):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_os_policy_assignment_report(
            os_policy_assignment_reports.GetOSPolicyAssignmentReportRequest(),
            name="name_value",
        )


def test_list_os_policy_assignment_reports_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = OsConfigZonalServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.list_os_policy_assignment_reports
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.list_os_policy_assignment_reports
        ] = mock_rpc

        request = {}
        client.list_os_policy_assignment_reports(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_os_policy_assignment_reports(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_list_os_policy_assignment_reports_rest_required_fields(
    request_type=os_policy_assignment_reports.ListOSPolicyAssignmentReportsRequest,
):
    transport_class = transports.OsConfigZonalServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseListOSPolicyAssignmentReports,
        "_BaseListOSPolicyAssignmentReports__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = os_policy_assignment_reports.ListOSPolicyAssignmentReportsResponse()
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
                os_policy_assignment_reports.ListOSPolicyAssignmentReportsResponse.pb(
                    return_value
                )
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.list_os_policy_assignment_reports(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_list_os_policy_assignment_reports_rest_flattened():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = (
            os_policy_assignment_reports.ListOSPolicyAssignmentReportsResponse()
        )

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "parent": "projects/sample1/locations/sample2/instances/sample3/osPolicyAssignments/sample4"
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
        return_value = (
            os_policy_assignment_reports.ListOSPolicyAssignmentReportsResponse.pb(
                return_value
            )
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.list_os_policy_assignment_reports(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1alpha/{parent=projects/*/locations/*/instances/*/osPolicyAssignments/*}/reports"
            % client.transport._host,
            args[1],
        )


def test_list_os_policy_assignment_reports_rest_flattened_error(
    transport: str = "rest",
):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_os_policy_assignment_reports(
            os_policy_assignment_reports.ListOSPolicyAssignmentReportsRequest(),
            parent="parent_value",
        )


def test_list_os_policy_assignment_reports_rest_pager(transport: str = "rest"):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        # with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            os_policy_assignment_reports.ListOSPolicyAssignmentReportsResponse(
                os_policy_assignment_reports=[
                    os_policy_assignment_reports.OSPolicyAssignmentReport(),
                    os_policy_assignment_reports.OSPolicyAssignmentReport(),
                    os_policy_assignment_reports.OSPolicyAssignmentReport(),
                ],
                next_page_token="abc",
            ),
            os_policy_assignment_reports.ListOSPolicyAssignmentReportsResponse(
                os_policy_assignment_reports=[],
                next_page_token="def",
            ),
            os_policy_assignment_reports.ListOSPolicyAssignmentReportsResponse(
                os_policy_assignment_reports=[
                    os_policy_assignment_reports.OSPolicyAssignmentReport(),
                ],
                next_page_token="ghi",
            ),
            os_policy_assignment_reports.ListOSPolicyAssignmentReportsResponse(
                os_policy_assignment_reports=[
                    os_policy_assignment_reports.OSPolicyAssignmentReport(),
                    os_policy_assignment_reports.OSPolicyAssignmentReport(),
                ],
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(
            os_policy_assignment_reports.ListOSPolicyAssignmentReportsResponse.to_json(
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
            "parent": "projects/sample1/locations/sample2/instances/sample3/osPolicyAssignments/sample4"
        }

        pager = client.list_os_policy_assignment_reports(request=sample_request)

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(
            isinstance(i, os_policy_assignment_reports.OSPolicyAssignmentReport)
            for i in results
        )

        pages = list(
            client.list_os_policy_assignment_reports(request=sample_request).pages
        )
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


def test_get_inventory_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = OsConfigZonalServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.get_inventory in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.get_inventory] = mock_rpc

        request = {}
        client.get_inventory(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_inventory(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_get_inventory_rest_required_fields(request_type=inventory.GetInventoryRequest):
    transport_class = transports.OsConfigZonalServiceRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseGetInventory,
        "_BaseGetInventory__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["name"] = "name_value"

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(("view",))

    # verify required fields with non-default values are left alone
    assert "name" in jsonified_request
    assert jsonified_request["name"] == "name_value"

    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = inventory.Inventory()
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
            return_value = inventory.Inventory.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.get_inventory(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_get_inventory_rest_flattened():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = inventory.Inventory()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "name": "projects/sample1/locations/sample2/instances/sample3/inventory"
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
        return_value = inventory.Inventory.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.get_inventory(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1alpha/{name=projects/*/locations/*/instances/*/inventory}"
            % client.transport._host,
            args[1],
        )


def test_get_inventory_rest_flattened_error(transport: str = "rest"):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_inventory(
            inventory.GetInventoryRequest(),
            name="name_value",
        )


def test_list_inventories_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = OsConfigZonalServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.list_inventories in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.list_inventories] = (
            mock_rpc
        )

        request = {}
        client.list_inventories(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_inventories(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_list_inventories_rest_required_fields(
    request_type=inventory.ListInventoriesRequest,
):
    transport_class = transports.OsConfigZonalServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseListInventories,
        "_BaseListInventories__REQUIRED_FIELDS_DEFAULT_VALUES",
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
            "view",
        )
    )

    # verify required fields with non-default values are left alone
    assert "parent" in jsonified_request
    assert jsonified_request["parent"] == "parent_value"

    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = inventory.ListInventoriesResponse()
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
            return_value = inventory.ListInventoriesResponse.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.list_inventories(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_list_inventories_rest_flattened():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = inventory.ListInventoriesResponse()

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
        return_value = inventory.ListInventoriesResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.list_inventories(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1alpha/{parent=projects/*/locations/*/instances/*}/inventories"
            % client.transport._host,
            args[1],
        )


def test_list_inventories_rest_flattened_error(transport: str = "rest"):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_inventories(
            inventory.ListInventoriesRequest(),
            parent="parent_value",
        )


def test_list_inventories_rest_pager(transport: str = "rest"):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        # with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            inventory.ListInventoriesResponse(
                inventories=[
                    inventory.Inventory(),
                    inventory.Inventory(),
                    inventory.Inventory(),
                ],
                next_page_token="abc",
            ),
            inventory.ListInventoriesResponse(
                inventories=[],
                next_page_token="def",
            ),
            inventory.ListInventoriesResponse(
                inventories=[
                    inventory.Inventory(),
                ],
                next_page_token="ghi",
            ),
            inventory.ListInventoriesResponse(
                inventories=[
                    inventory.Inventory(),
                    inventory.Inventory(),
                ],
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(inventory.ListInventoriesResponse.to_json(x) for x in response)
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode("UTF-8")
            return_val.status_code = 200
        req.side_effect = return_values

        sample_request = {
            "parent": "projects/sample1/locations/sample2/instances/sample3"
        }

        pager = client.list_inventories(request=sample_request)

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, inventory.Inventory) for i in results)

        pages = list(client.list_inventories(request=sample_request).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


def test_get_vulnerability_report_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = OsConfigZonalServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.get_vulnerability_report
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.get_vulnerability_report
        ] = mock_rpc

        request = {}
        client.get_vulnerability_report(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_vulnerability_report(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_get_vulnerability_report_rest_required_fields(
    request_type=vulnerability.GetVulnerabilityReportRequest,
):
    transport_class = transports.OsConfigZonalServiceRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseGetVulnerabilityReport,
        "_BaseGetVulnerabilityReport__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = vulnerability.VulnerabilityReport()
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
            return_value = vulnerability.VulnerabilityReport.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.get_vulnerability_report(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_get_vulnerability_report_rest_flattened():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = vulnerability.VulnerabilityReport()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "name": "projects/sample1/locations/sample2/instances/sample3/vulnerabilityReport"
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
        return_value = vulnerability.VulnerabilityReport.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.get_vulnerability_report(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1alpha/{name=projects/*/locations/*/instances/*/vulnerabilityReport}"
            % client.transport._host,
            args[1],
        )


def test_get_vulnerability_report_rest_flattened_error(transport: str = "rest"):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_vulnerability_report(
            vulnerability.GetVulnerabilityReportRequest(),
            name="name_value",
        )


def test_list_vulnerability_reports_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = OsConfigZonalServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.list_vulnerability_reports
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.list_vulnerability_reports
        ] = mock_rpc

        request = {}
        client.list_vulnerability_reports(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_vulnerability_reports(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_list_vulnerability_reports_rest_required_fields(
    request_type=vulnerability.ListVulnerabilityReportsRequest,
):
    transport_class = transports.OsConfigZonalServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseListVulnerabilityReports,
        "_BaseListVulnerabilityReports__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = vulnerability.ListVulnerabilityReportsResponse()
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
            return_value = vulnerability.ListVulnerabilityReportsResponse.pb(
                return_value
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.list_vulnerability_reports(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_list_vulnerability_reports_rest_flattened():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = vulnerability.ListVulnerabilityReportsResponse()

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
        return_value = vulnerability.ListVulnerabilityReportsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.list_vulnerability_reports(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1alpha/{parent=projects/*/locations/*/instances/*}/vulnerabilityReports"
            % client.transport._host,
            args[1],
        )


def test_list_vulnerability_reports_rest_flattened_error(transport: str = "rest"):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_vulnerability_reports(
            vulnerability.ListVulnerabilityReportsRequest(),
            parent="parent_value",
        )


def test_list_vulnerability_reports_rest_pager(transport: str = "rest"):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        # with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            vulnerability.ListVulnerabilityReportsResponse(
                vulnerability_reports=[
                    vulnerability.VulnerabilityReport(),
                    vulnerability.VulnerabilityReport(),
                    vulnerability.VulnerabilityReport(),
                ],
                next_page_token="abc",
            ),
            vulnerability.ListVulnerabilityReportsResponse(
                vulnerability_reports=[],
                next_page_token="def",
            ),
            vulnerability.ListVulnerabilityReportsResponse(
                vulnerability_reports=[
                    vulnerability.VulnerabilityReport(),
                ],
                next_page_token="ghi",
            ),
            vulnerability.ListVulnerabilityReportsResponse(
                vulnerability_reports=[
                    vulnerability.VulnerabilityReport(),
                    vulnerability.VulnerabilityReport(),
                ],
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(
            vulnerability.ListVulnerabilityReportsResponse.to_json(x) for x in response
        )
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode("UTF-8")
            return_val.status_code = 200
        req.side_effect = return_values

        sample_request = {
            "parent": "projects/sample1/locations/sample2/instances/sample3"
        }

        pager = client.list_vulnerability_reports(request=sample_request)

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, vulnerability.VulnerabilityReport) for i in results)

        pages = list(client.list_vulnerability_reports(request=sample_request).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


def test_credentials_transport_error():
    # It is an error to provide credentials and a transport instance.
    transport = transports.OsConfigZonalServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = OsConfigZonalServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport=transport,
        )

    # It is an error to provide a credentials file and a transport instance.
    transport = transports.OsConfigZonalServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = OsConfigZonalServiceClient(
            client_options={"credentials_file": "credentials.json"},
            transport=transport,
        )

    # It is an error to provide an api_key and a transport instance.
    transport = transports.OsConfigZonalServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    options = client_options.ClientOptions()
    options.api_key = "api_key"
    with pytest.raises(ValueError):
        client = OsConfigZonalServiceClient(
            client_options=options,
            transport=transport,
        )

    # It is an error to provide an api_key and a credential.
    options = client_options.ClientOptions()
    options.api_key = "api_key"
    with pytest.raises(ValueError):
        client = OsConfigZonalServiceClient(
            client_options=options, credentials=ga_credentials.AnonymousCredentials()
        )

    # It is an error to provide scopes and a transport instance.
    transport = transports.OsConfigZonalServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = OsConfigZonalServiceClient(
            client_options={"scopes": ["1", "2"]},
            transport=transport,
        )


def test_transport_instance():
    # A client may be instantiated with a custom transport instance.
    transport = transports.OsConfigZonalServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    client = OsConfigZonalServiceClient(transport=transport)
    assert client.transport is transport


def test_transport_get_channel():
    # A client may be instantiated with a custom transport instance.
    transport = transports.OsConfigZonalServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    channel = transport.grpc_channel
    assert channel

    transport = transports.OsConfigZonalServiceGrpcAsyncIOTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    channel = transport.grpc_channel
    assert channel


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.OsConfigZonalServiceGrpcTransport,
        transports.OsConfigZonalServiceGrpcAsyncIOTransport,
        transports.OsConfigZonalServiceRestTransport,
    ],
)
def test_transport_adc(transport_class):
    # Test default credentials are used if not provided.
    with mock.patch.object(google.auth, "default") as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport_class()
        adc.assert_called_once()


def test_transport_kind_grpc():
    transport = OsConfigZonalServiceClient.get_transport_class("grpc")(
        credentials=ga_credentials.AnonymousCredentials()
    )
    assert transport.kind == "grpc"


def test_initialize_client_w_grpc():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="grpc"
    )
    assert client is not None


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_create_os_policy_assignment_empty_call_grpc():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.create_os_policy_assignment), "__call__"
    ) as call:
        call.return_value = operations_pb2.Operation(name="operations/op")
        client.create_os_policy_assignment(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = os_policy_assignments.CreateOSPolicyAssignmentRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_update_os_policy_assignment_empty_call_grpc():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.update_os_policy_assignment), "__call__"
    ) as call:
        call.return_value = operations_pb2.Operation(name="operations/op")
        client.update_os_policy_assignment(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = os_policy_assignments.UpdateOSPolicyAssignmentRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_os_policy_assignment_empty_call_grpc():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.get_os_policy_assignment), "__call__"
    ) as call:
        call.return_value = os_policy_assignments.OSPolicyAssignment()
        client.get_os_policy_assignment(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = os_policy_assignments.GetOSPolicyAssignmentRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_os_policy_assignments_empty_call_grpc():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_os_policy_assignments), "__call__"
    ) as call:
        call.return_value = os_policy_assignments.ListOSPolicyAssignmentsResponse()
        client.list_os_policy_assignments(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = os_policy_assignments.ListOSPolicyAssignmentsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_os_policy_assignment_revisions_empty_call_grpc():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_os_policy_assignment_revisions), "__call__"
    ) as call:
        call.return_value = (
            os_policy_assignments.ListOSPolicyAssignmentRevisionsResponse()
        )
        client.list_os_policy_assignment_revisions(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = os_policy_assignments.ListOSPolicyAssignmentRevisionsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_delete_os_policy_assignment_empty_call_grpc():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_os_policy_assignment), "__call__"
    ) as call:
        call.return_value = operations_pb2.Operation(name="operations/op")
        client.delete_os_policy_assignment(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = os_policy_assignments.DeleteOSPolicyAssignmentRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_instance_os_policies_compliance_empty_call_grpc():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.get_instance_os_policies_compliance), "__call__"
    ) as call:
        call.return_value = (
            instance_os_policies_compliance.InstanceOSPoliciesCompliance()
        )
        client.get_instance_os_policies_compliance(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = (
            instance_os_policies_compliance.GetInstanceOSPoliciesComplianceRequest()
        )
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_instance_os_policies_compliances_empty_call_grpc():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_instance_os_policies_compliances), "__call__"
    ) as call:
        call.return_value = (
            instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesResponse()
        )
        client.list_instance_os_policies_compliances(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = (
            instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesRequest()
        )
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_os_policy_assignment_report_empty_call_grpc():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.get_os_policy_assignment_report), "__call__"
    ) as call:
        call.return_value = os_policy_assignment_reports.OSPolicyAssignmentReport()
        client.get_os_policy_assignment_report(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = os_policy_assignment_reports.GetOSPolicyAssignmentReportRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_os_policy_assignment_reports_empty_call_grpc():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_os_policy_assignment_reports), "__call__"
    ) as call:
        call.return_value = (
            os_policy_assignment_reports.ListOSPolicyAssignmentReportsResponse()
        )
        client.list_os_policy_assignment_reports(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = (
            os_policy_assignment_reports.ListOSPolicyAssignmentReportsRequest()
        )
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_inventory_empty_call_grpc():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_inventory), "__call__") as call:
        call.return_value = inventory.Inventory()
        client.get_inventory(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = inventory.GetInventoryRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_inventories_empty_call_grpc():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.list_inventories), "__call__") as call:
        call.return_value = inventory.ListInventoriesResponse()
        client.list_inventories(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = inventory.ListInventoriesRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_vulnerability_report_empty_call_grpc():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.get_vulnerability_report), "__call__"
    ) as call:
        call.return_value = vulnerability.VulnerabilityReport()
        client.get_vulnerability_report(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = vulnerability.GetVulnerabilityReportRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_vulnerability_reports_empty_call_grpc():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_vulnerability_reports), "__call__"
    ) as call:
        call.return_value = vulnerability.ListVulnerabilityReportsResponse()
        client.list_vulnerability_reports(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = vulnerability.ListVulnerabilityReportsRequest()
        assert args[0] == request_msg


def test_transport_kind_grpc_asyncio():
    transport = OsConfigZonalServiceAsyncClient.get_transport_class("grpc_asyncio")(
        credentials=async_anonymous_credentials()
    )
    assert transport.kind == "grpc_asyncio"


def test_initialize_client_w_grpc_asyncio():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(), transport="grpc_asyncio"
    )
    assert client is not None


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_create_os_policy_assignment_empty_call_grpc_asyncio():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.create_os_policy_assignment), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        await client.create_os_policy_assignment(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = os_policy_assignments.CreateOSPolicyAssignmentRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_update_os_policy_assignment_empty_call_grpc_asyncio():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.update_os_policy_assignment), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        await client.update_os_policy_assignment(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = os_policy_assignments.UpdateOSPolicyAssignmentRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_get_os_policy_assignment_empty_call_grpc_asyncio():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.get_os_policy_assignment), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            os_policy_assignments.OSPolicyAssignment(
                name="name_value",
                description="description_value",
                revision_id="revision_id_value",
                etag="etag_value",
                rollout_state=os_policy_assignments.OSPolicyAssignment.RolloutState.IN_PROGRESS,
                baseline=True,
                deleted=True,
                reconciling=True,
                uid="uid_value",
            )
        )
        await client.get_os_policy_assignment(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = os_policy_assignments.GetOSPolicyAssignmentRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_list_os_policy_assignments_empty_call_grpc_asyncio():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_os_policy_assignments), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            os_policy_assignments.ListOSPolicyAssignmentsResponse(
                next_page_token="next_page_token_value",
            )
        )
        await client.list_os_policy_assignments(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = os_policy_assignments.ListOSPolicyAssignmentsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_list_os_policy_assignment_revisions_empty_call_grpc_asyncio():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_os_policy_assignment_revisions), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            os_policy_assignments.ListOSPolicyAssignmentRevisionsResponse(
                next_page_token="next_page_token_value",
            )
        )
        await client.list_os_policy_assignment_revisions(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = os_policy_assignments.ListOSPolicyAssignmentRevisionsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_delete_os_policy_assignment_empty_call_grpc_asyncio():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_os_policy_assignment), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        await client.delete_os_policy_assignment(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = os_policy_assignments.DeleteOSPolicyAssignmentRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_get_instance_os_policies_compliance_empty_call_grpc_asyncio():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.get_instance_os_policies_compliance), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            instance_os_policies_compliance.InstanceOSPoliciesCompliance(
                name="name_value",
                instance="instance_value",
                state=config_common.OSPolicyComplianceState.COMPLIANT,
                detailed_state="detailed_state_value",
                detailed_state_reason="detailed_state_reason_value",
                last_compliance_run_id="last_compliance_run_id_value",
            )
        )
        await client.get_instance_os_policies_compliance(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = (
            instance_os_policies_compliance.GetInstanceOSPoliciesComplianceRequest()
        )
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_list_instance_os_policies_compliances_empty_call_grpc_asyncio():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_instance_os_policies_compliances), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesResponse(
                next_page_token="next_page_token_value",
            )
        )
        await client.list_instance_os_policies_compliances(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = (
            instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesRequest()
        )
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_get_os_policy_assignment_report_empty_call_grpc_asyncio():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.get_os_policy_assignment_report), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            os_policy_assignment_reports.OSPolicyAssignmentReport(
                name="name_value",
                instance="instance_value",
                os_policy_assignment="os_policy_assignment_value",
                last_run_id="last_run_id_value",
            )
        )
        await client.get_os_policy_assignment_report(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = os_policy_assignment_reports.GetOSPolicyAssignmentReportRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_list_os_policy_assignment_reports_empty_call_grpc_asyncio():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_os_policy_assignment_reports), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            os_policy_assignment_reports.ListOSPolicyAssignmentReportsResponse(
                next_page_token="next_page_token_value",
            )
        )
        await client.list_os_policy_assignment_reports(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = (
            os_policy_assignment_reports.ListOSPolicyAssignmentReportsRequest()
        )
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_get_inventory_empty_call_grpc_asyncio():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_inventory), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            inventory.Inventory(
                name="name_value",
            )
        )
        await client.get_inventory(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = inventory.GetInventoryRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_list_inventories_empty_call_grpc_asyncio():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.list_inventories), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            inventory.ListInventoriesResponse(
                next_page_token="next_page_token_value",
            )
        )
        await client.list_inventories(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = inventory.ListInventoriesRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_get_vulnerability_report_empty_call_grpc_asyncio():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.get_vulnerability_report), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            vulnerability.VulnerabilityReport(
                name="name_value",
            )
        )
        await client.get_vulnerability_report(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = vulnerability.GetVulnerabilityReportRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_list_vulnerability_reports_empty_call_grpc_asyncio():
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_vulnerability_reports), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            vulnerability.ListVulnerabilityReportsResponse(
                next_page_token="next_page_token_value",
            )
        )
        await client.list_vulnerability_reports(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = vulnerability.ListVulnerabilityReportsRequest()
        assert args[0] == request_msg


def test_transport_kind_rest():
    transport = OsConfigZonalServiceClient.get_transport_class("rest")(
        credentials=ga_credentials.AnonymousCredentials()
    )
    assert transport.kind == "rest"


def test_create_os_policy_assignment_rest_bad_request(
    request_type=os_policy_assignments.CreateOSPolicyAssignmentRequest,
):
    client = OsConfigZonalServiceClient(
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
        client.create_os_policy_assignment(request)


@pytest.mark.parametrize(
    "request_type",
    [
        os_policy_assignments.CreateOSPolicyAssignmentRequest,
        dict,
    ],
)
def test_create_os_policy_assignment_rest_call_success(request_type):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1/locations/sample2"}
    request_init["os_policy_assignment"] = {
        "name": "name_value",
        "description": "description_value",
        "os_policies": [
            {
                "id": "id_value",
                "description": "description_value",
                "mode": 1,
                "resource_groups": [
                    {
                        "os_filter": {
                            "os_short_name": "os_short_name_value",
                            "os_version": "os_version_value",
                        },
                        "inventory_filters": [
                            {
                                "os_short_name": "os_short_name_value",
                                "os_version": "os_version_value",
                            }
                        ],
                        "resources": [
                            {
                                "id": "id_value",
                                "pkg": {
                                    "desired_state": 1,
                                    "apt": {"name": "name_value"},
                                    "deb": {
                                        "source": {
                                            "remote": {
                                                "uri": "uri_value",
                                                "sha256_checksum": "sha256_checksum_value",
                                            },
                                            "gcs": {
                                                "bucket": "bucket_value",
                                                "object_": "object__value",
                                                "generation": 1068,
                                            },
                                            "local_path": "local_path_value",
                                            "allow_insecure": True,
                                        },
                                        "pull_deps": True,
                                    },
                                    "yum": {"name": "name_value"},
                                    "zypper": {"name": "name_value"},
                                    "rpm": {"source": {}, "pull_deps": True},
                                    "googet": {"name": "name_value"},
                                    "msi": {
                                        "source": {},
                                        "properties": [
                                            "properties_value1",
                                            "properties_value2",
                                        ],
                                    },
                                },
                                "repository": {
                                    "apt": {
                                        "archive_type": 1,
                                        "uri": "uri_value",
                                        "distribution": "distribution_value",
                                        "components": [
                                            "components_value1",
                                            "components_value2",
                                        ],
                                        "gpg_key": "gpg_key_value",
                                    },
                                    "yum": {
                                        "id": "id_value",
                                        "display_name": "display_name_value",
                                        "base_url": "base_url_value",
                                        "gpg_keys": [
                                            "gpg_keys_value1",
                                            "gpg_keys_value2",
                                        ],
                                    },
                                    "zypper": {
                                        "id": "id_value",
                                        "display_name": "display_name_value",
                                        "base_url": "base_url_value",
                                        "gpg_keys": [
                                            "gpg_keys_value1",
                                            "gpg_keys_value2",
                                        ],
                                    },
                                    "goo": {"name": "name_value", "url": "url_value"},
                                },
                                "exec_": {
                                    "validate": {
                                        "file": {},
                                        "script": "script_value",
                                        "args": ["args_value1", "args_value2"],
                                        "interpreter": 1,
                                        "output_file_path": "output_file_path_value",
                                    },
                                    "enforce": {},
                                },
                                "file": {
                                    "file": {},
                                    "content": "content_value",
                                    "path": "path_value",
                                    "state": 1,
                                    "permissions": "permissions_value",
                                },
                            }
                        ],
                    }
                ],
                "allow_no_resource_group_match": True,
            }
        ],
        "instance_filter": {
            "all_": True,
            "os_short_names": ["os_short_names_value1", "os_short_names_value2"],
            "inclusion_labels": [{"labels": {}}],
            "exclusion_labels": {},
            "inventories": [
                {
                    "os_short_name": "os_short_name_value",
                    "os_version": "os_version_value",
                }
            ],
        },
        "rollout": {
            "disruption_budget": {"fixed": 528, "percent": 753},
            "min_wait_duration": {"seconds": 751, "nanos": 543},
        },
        "revision_id": "revision_id_value",
        "revision_create_time": {"seconds": 751, "nanos": 543},
        "etag": "etag_value",
        "rollout_state": 1,
        "baseline": True,
        "deleted": True,
        "reconciling": True,
        "uid": "uid_value",
    }
    # The version of a generated dependency at test runtime may differ from the version used during generation.
    # Delete any fields which are not present in the current runtime dependency
    # See https://github.com/googleapis/gapic-generator-python/issues/1748

    # Determine if the message type is proto-plus or protobuf
    test_field = os_policy_assignments.CreateOSPolicyAssignmentRequest.meta.fields[
        "os_policy_assignment"
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
        "os_policy_assignment"
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
                for i in range(0, len(request_init["os_policy_assignment"][field])):
                    del request_init["os_policy_assignment"][field][i][subfield]
            else:
                del request_init["os_policy_assignment"][field][subfield]
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
        response = client.create_os_policy_assignment(request)

    # Establish that the response is the type that we expect.
    json_return_value = json_format.MessageToJson(return_value)


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_create_os_policy_assignment_rest_interceptors(null_interceptor):
    transport = transports.OsConfigZonalServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.OsConfigZonalServiceRestInterceptor(),
    )
    client = OsConfigZonalServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(operation.Operation, "_set_result_from_operation"),
        mock.patch.object(
            transports.OsConfigZonalServiceRestInterceptor,
            "post_create_os_policy_assignment",
        ) as post,
        mock.patch.object(
            transports.OsConfigZonalServiceRestInterceptor,
            "post_create_os_policy_assignment_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.OsConfigZonalServiceRestInterceptor,
            "pre_create_os_policy_assignment",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = os_policy_assignments.CreateOSPolicyAssignmentRequest.pb(
            os_policy_assignments.CreateOSPolicyAssignmentRequest()
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

        request = os_policy_assignments.CreateOSPolicyAssignmentRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = operations_pb2.Operation()
        post_with_metadata.return_value = operations_pb2.Operation(), metadata

        client.create_os_policy_assignment(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_update_os_policy_assignment_rest_bad_request(
    request_type=os_policy_assignments.UpdateOSPolicyAssignmentRequest,
):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {
        "os_policy_assignment": {
            "name": "projects/sample1/locations/sample2/osPolicyAssignments/sample3"
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
        client.update_os_policy_assignment(request)


@pytest.mark.parametrize(
    "request_type",
    [
        os_policy_assignments.UpdateOSPolicyAssignmentRequest,
        dict,
    ],
)
def test_update_os_policy_assignment_rest_call_success(request_type):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {
        "os_policy_assignment": {
            "name": "projects/sample1/locations/sample2/osPolicyAssignments/sample3"
        }
    }
    request_init["os_policy_assignment"] = {
        "name": "projects/sample1/locations/sample2/osPolicyAssignments/sample3",
        "description": "description_value",
        "os_policies": [
            {
                "id": "id_value",
                "description": "description_value",
                "mode": 1,
                "resource_groups": [
                    {
                        "os_filter": {
                            "os_short_name": "os_short_name_value",
                            "os_version": "os_version_value",
                        },
                        "inventory_filters": [
                            {
                                "os_short_name": "os_short_name_value",
                                "os_version": "os_version_value",
                            }
                        ],
                        "resources": [
                            {
                                "id": "id_value",
                                "pkg": {
                                    "desired_state": 1,
                                    "apt": {"name": "name_value"},
                                    "deb": {
                                        "source": {
                                            "remote": {
                                                "uri": "uri_value",
                                                "sha256_checksum": "sha256_checksum_value",
                                            },
                                            "gcs": {
                                                "bucket": "bucket_value",
                                                "object_": "object__value",
                                                "generation": 1068,
                                            },
                                            "local_path": "local_path_value",
                                            "allow_insecure": True,
                                        },
                                        "pull_deps": True,
                                    },
                                    "yum": {"name": "name_value"},
                                    "zypper": {"name": "name_value"},
                                    "rpm": {"source": {}, "pull_deps": True},
                                    "googet": {"name": "name_value"},
                                    "msi": {
                                        "source": {},
                                        "properties": [
                                            "properties_value1",
                                            "properties_value2",
                                        ],
                                    },
                                },
                                "repository": {
                                    "apt": {
                                        "archive_type": 1,
                                        "uri": "uri_value",
                                        "distribution": "distribution_value",
                                        "components": [
                                            "components_value1",
                                            "components_value2",
                                        ],
                                        "gpg_key": "gpg_key_value",
                                    },
                                    "yum": {
                                        "id": "id_value",
                                        "display_name": "display_name_value",
                                        "base_url": "base_url_value",
                                        "gpg_keys": [
                                            "gpg_keys_value1",
                                            "gpg_keys_value2",
                                        ],
                                    },
                                    "zypper": {
                                        "id": "id_value",
                                        "display_name": "display_name_value",
                                        "base_url": "base_url_value",
                                        "gpg_keys": [
                                            "gpg_keys_value1",
                                            "gpg_keys_value2",
                                        ],
                                    },
                                    "goo": {"name": "name_value", "url": "url_value"},
                                },
                                "exec_": {
                                    "validate": {
                                        "file": {},
                                        "script": "script_value",
                                        "args": ["args_value1", "args_value2"],
                                        "interpreter": 1,
                                        "output_file_path": "output_file_path_value",
                                    },
                                    "enforce": {},
                                },
                                "file": {
                                    "file": {},
                                    "content": "content_value",
                                    "path": "path_value",
                                    "state": 1,
                                    "permissions": "permissions_value",
                                },
                            }
                        ],
                    }
                ],
                "allow_no_resource_group_match": True,
            }
        ],
        "instance_filter": {
            "all_": True,
            "os_short_names": ["os_short_names_value1", "os_short_names_value2"],
            "inclusion_labels": [{"labels": {}}],
            "exclusion_labels": {},
            "inventories": [
                {
                    "os_short_name": "os_short_name_value",
                    "os_version": "os_version_value",
                }
            ],
        },
        "rollout": {
            "disruption_budget": {"fixed": 528, "percent": 753},
            "min_wait_duration": {"seconds": 751, "nanos": 543},
        },
        "revision_id": "revision_id_value",
        "revision_create_time": {"seconds": 751, "nanos": 543},
        "etag": "etag_value",
        "rollout_state": 1,
        "baseline": True,
        "deleted": True,
        "reconciling": True,
        "uid": "uid_value",
    }
    # The version of a generated dependency at test runtime may differ from the version used during generation.
    # Delete any fields which are not present in the current runtime dependency
    # See https://github.com/googleapis/gapic-generator-python/issues/1748

    # Determine if the message type is proto-plus or protobuf
    test_field = os_policy_assignments.UpdateOSPolicyAssignmentRequest.meta.fields[
        "os_policy_assignment"
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
        "os_policy_assignment"
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
                for i in range(0, len(request_init["os_policy_assignment"][field])):
                    del request_init["os_policy_assignment"][field][i][subfield]
            else:
                del request_init["os_policy_assignment"][field][subfield]
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
        response = client.update_os_policy_assignment(request)

    # Establish that the response is the type that we expect.
    json_return_value = json_format.MessageToJson(return_value)


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_update_os_policy_assignment_rest_interceptors(null_interceptor):
    transport = transports.OsConfigZonalServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.OsConfigZonalServiceRestInterceptor(),
    )
    client = OsConfigZonalServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(operation.Operation, "_set_result_from_operation"),
        mock.patch.object(
            transports.OsConfigZonalServiceRestInterceptor,
            "post_update_os_policy_assignment",
        ) as post,
        mock.patch.object(
            transports.OsConfigZonalServiceRestInterceptor,
            "post_update_os_policy_assignment_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.OsConfigZonalServiceRestInterceptor,
            "pre_update_os_policy_assignment",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = os_policy_assignments.UpdateOSPolicyAssignmentRequest.pb(
            os_policy_assignments.UpdateOSPolicyAssignmentRequest()
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

        request = os_policy_assignments.UpdateOSPolicyAssignmentRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = operations_pb2.Operation()
        post_with_metadata.return_value = operations_pb2.Operation(), metadata

        client.update_os_policy_assignment(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_get_os_policy_assignment_rest_bad_request(
    request_type=os_policy_assignments.GetOSPolicyAssignmentRequest,
):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/osPolicyAssignments/sample3"
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
        client.get_os_policy_assignment(request)


@pytest.mark.parametrize(
    "request_type",
    [
        os_policy_assignments.GetOSPolicyAssignmentRequest,
        dict,
    ],
)
def test_get_os_policy_assignment_rest_call_success(request_type):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/osPolicyAssignments/sample3"
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = os_policy_assignments.OSPolicyAssignment(
            name="name_value",
            description="description_value",
            revision_id="revision_id_value",
            etag="etag_value",
            rollout_state=os_policy_assignments.OSPolicyAssignment.RolloutState.IN_PROGRESS,
            baseline=True,
            deleted=True,
            reconciling=True,
            uid="uid_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = os_policy_assignments.OSPolicyAssignment.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.get_os_policy_assignment(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, os_policy_assignments.OSPolicyAssignment)
    assert response.name == "name_value"
    assert response.description == "description_value"
    assert response.revision_id == "revision_id_value"
    assert response.etag == "etag_value"
    assert (
        response.rollout_state
        == os_policy_assignments.OSPolicyAssignment.RolloutState.IN_PROGRESS
    )
    assert response.baseline is True
    assert response.deleted is True
    assert response.reconciling is True
    assert response.uid == "uid_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_get_os_policy_assignment_rest_interceptors(null_interceptor):
    transport = transports.OsConfigZonalServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.OsConfigZonalServiceRestInterceptor(),
    )
    client = OsConfigZonalServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.OsConfigZonalServiceRestInterceptor,
            "post_get_os_policy_assignment",
        ) as post,
        mock.patch.object(
            transports.OsConfigZonalServiceRestInterceptor,
            "post_get_os_policy_assignment_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.OsConfigZonalServiceRestInterceptor,
            "pre_get_os_policy_assignment",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = os_policy_assignments.GetOSPolicyAssignmentRequest.pb(
            os_policy_assignments.GetOSPolicyAssignmentRequest()
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
        return_value = os_policy_assignments.OSPolicyAssignment.to_json(
            os_policy_assignments.OSPolicyAssignment()
        )
        req.return_value.content = return_value

        request = os_policy_assignments.GetOSPolicyAssignmentRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = os_policy_assignments.OSPolicyAssignment()
        post_with_metadata.return_value = (
            os_policy_assignments.OSPolicyAssignment(),
            metadata,
        )

        client.get_os_policy_assignment(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_list_os_policy_assignments_rest_bad_request(
    request_type=os_policy_assignments.ListOSPolicyAssignmentsRequest,
):
    client = OsConfigZonalServiceClient(
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
        client.list_os_policy_assignments(request)


@pytest.mark.parametrize(
    "request_type",
    [
        os_policy_assignments.ListOSPolicyAssignmentsRequest,
        dict,
    ],
)
def test_list_os_policy_assignments_rest_call_success(request_type):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1/locations/sample2"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = os_policy_assignments.ListOSPolicyAssignmentsResponse(
            next_page_token="next_page_token_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = os_policy_assignments.ListOSPolicyAssignmentsResponse.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.list_os_policy_assignments(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListOSPolicyAssignmentsPager)
    assert response.next_page_token == "next_page_token_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_list_os_policy_assignments_rest_interceptors(null_interceptor):
    transport = transports.OsConfigZonalServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.OsConfigZonalServiceRestInterceptor(),
    )
    client = OsConfigZonalServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.OsConfigZonalServiceRestInterceptor,
            "post_list_os_policy_assignments",
        ) as post,
        mock.patch.object(
            transports.OsConfigZonalServiceRestInterceptor,
            "post_list_os_policy_assignments_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.OsConfigZonalServiceRestInterceptor,
            "pre_list_os_policy_assignments",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = os_policy_assignments.ListOSPolicyAssignmentsRequest.pb(
            os_policy_assignments.ListOSPolicyAssignmentsRequest()
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
        return_value = os_policy_assignments.ListOSPolicyAssignmentsResponse.to_json(
            os_policy_assignments.ListOSPolicyAssignmentsResponse()
        )
        req.return_value.content = return_value

        request = os_policy_assignments.ListOSPolicyAssignmentsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = os_policy_assignments.ListOSPolicyAssignmentsResponse()
        post_with_metadata.return_value = (
            os_policy_assignments.ListOSPolicyAssignmentsResponse(),
            metadata,
        )

        client.list_os_policy_assignments(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_list_os_policy_assignment_revisions_rest_bad_request(
    request_type=os_policy_assignments.ListOSPolicyAssignmentRevisionsRequest,
):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/osPolicyAssignments/sample3"
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
        client.list_os_policy_assignment_revisions(request)


@pytest.mark.parametrize(
    "request_type",
    [
        os_policy_assignments.ListOSPolicyAssignmentRevisionsRequest,
        dict,
    ],
)
def test_list_os_policy_assignment_revisions_rest_call_success(request_type):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/osPolicyAssignments/sample3"
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = os_policy_assignments.ListOSPolicyAssignmentRevisionsResponse(
            next_page_token="next_page_token_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = os_policy_assignments.ListOSPolicyAssignmentRevisionsResponse.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.list_os_policy_assignment_revisions(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListOSPolicyAssignmentRevisionsPager)
    assert response.next_page_token == "next_page_token_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_list_os_policy_assignment_revisions_rest_interceptors(null_interceptor):
    transport = transports.OsConfigZonalServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.OsConfigZonalServiceRestInterceptor(),
    )
    client = OsConfigZonalServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.OsConfigZonalServiceRestInterceptor,
            "post_list_os_policy_assignment_revisions",
        ) as post,
        mock.patch.object(
            transports.OsConfigZonalServiceRestInterceptor,
            "post_list_os_policy_assignment_revisions_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.OsConfigZonalServiceRestInterceptor,
            "pre_list_os_policy_assignment_revisions",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = os_policy_assignments.ListOSPolicyAssignmentRevisionsRequest.pb(
            os_policy_assignments.ListOSPolicyAssignmentRevisionsRequest()
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
            os_policy_assignments.ListOSPolicyAssignmentRevisionsResponse.to_json(
                os_policy_assignments.ListOSPolicyAssignmentRevisionsResponse()
            )
        )
        req.return_value.content = return_value

        request = os_policy_assignments.ListOSPolicyAssignmentRevisionsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = (
            os_policy_assignments.ListOSPolicyAssignmentRevisionsResponse()
        )
        post_with_metadata.return_value = (
            os_policy_assignments.ListOSPolicyAssignmentRevisionsResponse(),
            metadata,
        )

        client.list_os_policy_assignment_revisions(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_delete_os_policy_assignment_rest_bad_request(
    request_type=os_policy_assignments.DeleteOSPolicyAssignmentRequest,
):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/osPolicyAssignments/sample3"
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
        client.delete_os_policy_assignment(request)


@pytest.mark.parametrize(
    "request_type",
    [
        os_policy_assignments.DeleteOSPolicyAssignmentRequest,
        dict,
    ],
)
def test_delete_os_policy_assignment_rest_call_success(request_type):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/osPolicyAssignments/sample3"
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
        response = client.delete_os_policy_assignment(request)

    # Establish that the response is the type that we expect.
    json_return_value = json_format.MessageToJson(return_value)


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_delete_os_policy_assignment_rest_interceptors(null_interceptor):
    transport = transports.OsConfigZonalServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.OsConfigZonalServiceRestInterceptor(),
    )
    client = OsConfigZonalServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(operation.Operation, "_set_result_from_operation"),
        mock.patch.object(
            transports.OsConfigZonalServiceRestInterceptor,
            "post_delete_os_policy_assignment",
        ) as post,
        mock.patch.object(
            transports.OsConfigZonalServiceRestInterceptor,
            "post_delete_os_policy_assignment_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.OsConfigZonalServiceRestInterceptor,
            "pre_delete_os_policy_assignment",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = os_policy_assignments.DeleteOSPolicyAssignmentRequest.pb(
            os_policy_assignments.DeleteOSPolicyAssignmentRequest()
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

        request = os_policy_assignments.DeleteOSPolicyAssignmentRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = operations_pb2.Operation()
        post_with_metadata.return_value = operations_pb2.Operation(), metadata

        client.delete_os_policy_assignment(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_get_instance_os_policies_compliance_rest_bad_request(
    request_type=instance_os_policies_compliance.GetInstanceOSPoliciesComplianceRequest,
):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/instanceOSPoliciesCompliances/sample3"
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
        client.get_instance_os_policies_compliance(request)


@pytest.mark.parametrize(
    "request_type",
    [
        instance_os_policies_compliance.GetInstanceOSPoliciesComplianceRequest,
        dict,
    ],
)
def test_get_instance_os_policies_compliance_rest_call_success(request_type):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/instanceOSPoliciesCompliances/sample3"
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = instance_os_policies_compliance.InstanceOSPoliciesCompliance(
            name="name_value",
            instance="instance_value",
            state=config_common.OSPolicyComplianceState.COMPLIANT,
            detailed_state="detailed_state_value",
            detailed_state_reason="detailed_state_reason_value",
            last_compliance_run_id="last_compliance_run_id_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = instance_os_policies_compliance.InstanceOSPoliciesCompliance.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.get_instance_os_policies_compliance(request)

    # Establish that the response is the type that we expect.
    assert isinstance(
        response, instance_os_policies_compliance.InstanceOSPoliciesCompliance
    )
    assert response.name == "name_value"
    assert response.instance == "instance_value"
    assert response.state == config_common.OSPolicyComplianceState.COMPLIANT
    assert response.detailed_state == "detailed_state_value"
    assert response.detailed_state_reason == "detailed_state_reason_value"
    assert response.last_compliance_run_id == "last_compliance_run_id_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_get_instance_os_policies_compliance_rest_interceptors(null_interceptor):
    transport = transports.OsConfigZonalServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.OsConfigZonalServiceRestInterceptor(),
    )
    client = OsConfigZonalServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.OsConfigZonalServiceRestInterceptor,
            "post_get_instance_os_policies_compliance",
        ) as post,
        mock.patch.object(
            transports.OsConfigZonalServiceRestInterceptor,
            "post_get_instance_os_policies_compliance_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.OsConfigZonalServiceRestInterceptor,
            "pre_get_instance_os_policies_compliance",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = (
            instance_os_policies_compliance.GetInstanceOSPoliciesComplianceRequest.pb(
                instance_os_policies_compliance.GetInstanceOSPoliciesComplianceRequest()
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
            instance_os_policies_compliance.InstanceOSPoliciesCompliance.to_json(
                instance_os_policies_compliance.InstanceOSPoliciesCompliance()
            )
        )
        req.return_value.content = return_value

        request = (
            instance_os_policies_compliance.GetInstanceOSPoliciesComplianceRequest()
        )
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = (
            instance_os_policies_compliance.InstanceOSPoliciesCompliance()
        )
        post_with_metadata.return_value = (
            instance_os_policies_compliance.InstanceOSPoliciesCompliance(),
            metadata,
        )

        client.get_instance_os_policies_compliance(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_list_instance_os_policies_compliances_rest_bad_request(
    request_type=instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesRequest,
):
    client = OsConfigZonalServiceClient(
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
        client.list_instance_os_policies_compliances(request)


@pytest.mark.parametrize(
    "request_type",
    [
        instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesRequest,
        dict,
    ],
)
def test_list_instance_os_policies_compliances_rest_call_success(request_type):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1/locations/sample2"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = (
            instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesResponse(
                next_page_token="next_page_token_value",
            )
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesResponse.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.list_instance_os_policies_compliances(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListInstanceOSPoliciesCompliancesPager)
    assert response.next_page_token == "next_page_token_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_list_instance_os_policies_compliances_rest_interceptors(null_interceptor):
    transport = transports.OsConfigZonalServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.OsConfigZonalServiceRestInterceptor(),
    )
    client = OsConfigZonalServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.OsConfigZonalServiceRestInterceptor,
            "post_list_instance_os_policies_compliances",
        ) as post,
        mock.patch.object(
            transports.OsConfigZonalServiceRestInterceptor,
            "post_list_instance_os_policies_compliances_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.OsConfigZonalServiceRestInterceptor,
            "pre_list_instance_os_policies_compliances",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesRequest.pb(
            instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesRequest()
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
        return_value = instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesResponse.to_json(
            instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesResponse()
        )
        req.return_value.content = return_value

        request = (
            instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesRequest()
        )
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = (
            instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesResponse()
        )
        post_with_metadata.return_value = (
            instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesResponse(),
            metadata,
        )

        client.list_instance_os_policies_compliances(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_get_os_policy_assignment_report_rest_bad_request(
    request_type=os_policy_assignment_reports.GetOSPolicyAssignmentReportRequest,
):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/instances/sample3/osPolicyAssignments/sample4/report"
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
        client.get_os_policy_assignment_report(request)


@pytest.mark.parametrize(
    "request_type",
    [
        os_policy_assignment_reports.GetOSPolicyAssignmentReportRequest,
        dict,
    ],
)
def test_get_os_policy_assignment_report_rest_call_success(request_type):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/instances/sample3/osPolicyAssignments/sample4/report"
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = os_policy_assignment_reports.OSPolicyAssignmentReport(
            name="name_value",
            instance="instance_value",
            os_policy_assignment="os_policy_assignment_value",
            last_run_id="last_run_id_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = os_policy_assignment_reports.OSPolicyAssignmentReport.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.get_os_policy_assignment_report(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, os_policy_assignment_reports.OSPolicyAssignmentReport)
    assert response.name == "name_value"
    assert response.instance == "instance_value"
    assert response.os_policy_assignment == "os_policy_assignment_value"
    assert response.last_run_id == "last_run_id_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_get_os_policy_assignment_report_rest_interceptors(null_interceptor):
    transport = transports.OsConfigZonalServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.OsConfigZonalServiceRestInterceptor(),
    )
    client = OsConfigZonalServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.OsConfigZonalServiceRestInterceptor,
            "post_get_os_policy_assignment_report",
        ) as post,
        mock.patch.object(
            transports.OsConfigZonalServiceRestInterceptor,
            "post_get_os_policy_assignment_report_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.OsConfigZonalServiceRestInterceptor,
            "pre_get_os_policy_assignment_report",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = os_policy_assignment_reports.GetOSPolicyAssignmentReportRequest.pb(
            os_policy_assignment_reports.GetOSPolicyAssignmentReportRequest()
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
        return_value = os_policy_assignment_reports.OSPolicyAssignmentReport.to_json(
            os_policy_assignment_reports.OSPolicyAssignmentReport()
        )
        req.return_value.content = return_value

        request = os_policy_assignment_reports.GetOSPolicyAssignmentReportRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = os_policy_assignment_reports.OSPolicyAssignmentReport()
        post_with_metadata.return_value = (
            os_policy_assignment_reports.OSPolicyAssignmentReport(),
            metadata,
        )

        client.get_os_policy_assignment_report(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_list_os_policy_assignment_reports_rest_bad_request(
    request_type=os_policy_assignment_reports.ListOSPolicyAssignmentReportsRequest,
):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {
        "parent": "projects/sample1/locations/sample2/instances/sample3/osPolicyAssignments/sample4"
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
        client.list_os_policy_assignment_reports(request)


@pytest.mark.parametrize(
    "request_type",
    [
        os_policy_assignment_reports.ListOSPolicyAssignmentReportsRequest,
        dict,
    ],
)
def test_list_os_policy_assignment_reports_rest_call_success(request_type):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {
        "parent": "projects/sample1/locations/sample2/instances/sample3/osPolicyAssignments/sample4"
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = (
            os_policy_assignment_reports.ListOSPolicyAssignmentReportsResponse(
                next_page_token="next_page_token_value",
            )
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = (
            os_policy_assignment_reports.ListOSPolicyAssignmentReportsResponse.pb(
                return_value
            )
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.list_os_policy_assignment_reports(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListOSPolicyAssignmentReportsPager)
    assert response.next_page_token == "next_page_token_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_list_os_policy_assignment_reports_rest_interceptors(null_interceptor):
    transport = transports.OsConfigZonalServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.OsConfigZonalServiceRestInterceptor(),
    )
    client = OsConfigZonalServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.OsConfigZonalServiceRestInterceptor,
            "post_list_os_policy_assignment_reports",
        ) as post,
        mock.patch.object(
            transports.OsConfigZonalServiceRestInterceptor,
            "post_list_os_policy_assignment_reports_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.OsConfigZonalServiceRestInterceptor,
            "pre_list_os_policy_assignment_reports",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = (
            os_policy_assignment_reports.ListOSPolicyAssignmentReportsRequest.pb(
                os_policy_assignment_reports.ListOSPolicyAssignmentReportsRequest()
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
            os_policy_assignment_reports.ListOSPolicyAssignmentReportsResponse.to_json(
                os_policy_assignment_reports.ListOSPolicyAssignmentReportsResponse()
            )
        )
        req.return_value.content = return_value

        request = os_policy_assignment_reports.ListOSPolicyAssignmentReportsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = (
            os_policy_assignment_reports.ListOSPolicyAssignmentReportsResponse()
        )
        post_with_metadata.return_value = (
            os_policy_assignment_reports.ListOSPolicyAssignmentReportsResponse(),
            metadata,
        )

        client.list_os_policy_assignment_reports(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_get_inventory_rest_bad_request(request_type=inventory.GetInventoryRequest):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/instances/sample3/inventory"
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
        client.get_inventory(request)


@pytest.mark.parametrize(
    "request_type",
    [
        inventory.GetInventoryRequest,
        dict,
    ],
)
def test_get_inventory_rest_call_success(request_type):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/instances/sample3/inventory"
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = inventory.Inventory(
            name="name_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = inventory.Inventory.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.get_inventory(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, inventory.Inventory)
    assert response.name == "name_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_get_inventory_rest_interceptors(null_interceptor):
    transport = transports.OsConfigZonalServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.OsConfigZonalServiceRestInterceptor(),
    )
    client = OsConfigZonalServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.OsConfigZonalServiceRestInterceptor, "post_get_inventory"
        ) as post,
        mock.patch.object(
            transports.OsConfigZonalServiceRestInterceptor,
            "post_get_inventory_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.OsConfigZonalServiceRestInterceptor, "pre_get_inventory"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = inventory.GetInventoryRequest.pb(inventory.GetInventoryRequest())
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = inventory.Inventory.to_json(inventory.Inventory())
        req.return_value.content = return_value

        request = inventory.GetInventoryRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = inventory.Inventory()
        post_with_metadata.return_value = inventory.Inventory(), metadata

        client.get_inventory(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_list_inventories_rest_bad_request(
    request_type=inventory.ListInventoriesRequest,
):
    client = OsConfigZonalServiceClient(
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
        client.list_inventories(request)


@pytest.mark.parametrize(
    "request_type",
    [
        inventory.ListInventoriesRequest,
        dict,
    ],
)
def test_list_inventories_rest_call_success(request_type):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1/locations/sample2/instances/sample3"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = inventory.ListInventoriesResponse(
            next_page_token="next_page_token_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = inventory.ListInventoriesResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.list_inventories(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListInventoriesPager)
    assert response.next_page_token == "next_page_token_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_list_inventories_rest_interceptors(null_interceptor):
    transport = transports.OsConfigZonalServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.OsConfigZonalServiceRestInterceptor(),
    )
    client = OsConfigZonalServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.OsConfigZonalServiceRestInterceptor, "post_list_inventories"
        ) as post,
        mock.patch.object(
            transports.OsConfigZonalServiceRestInterceptor,
            "post_list_inventories_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.OsConfigZonalServiceRestInterceptor, "pre_list_inventories"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = inventory.ListInventoriesRequest.pb(
            inventory.ListInventoriesRequest()
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
        return_value = inventory.ListInventoriesResponse.to_json(
            inventory.ListInventoriesResponse()
        )
        req.return_value.content = return_value

        request = inventory.ListInventoriesRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = inventory.ListInventoriesResponse()
        post_with_metadata.return_value = inventory.ListInventoriesResponse(), metadata

        client.list_inventories(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_get_vulnerability_report_rest_bad_request(
    request_type=vulnerability.GetVulnerabilityReportRequest,
):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/instances/sample3/vulnerabilityReport"
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
        client.get_vulnerability_report(request)


@pytest.mark.parametrize(
    "request_type",
    [
        vulnerability.GetVulnerabilityReportRequest,
        dict,
    ],
)
def test_get_vulnerability_report_rest_call_success(request_type):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/instances/sample3/vulnerabilityReport"
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = vulnerability.VulnerabilityReport(
            name="name_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = vulnerability.VulnerabilityReport.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.get_vulnerability_report(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, vulnerability.VulnerabilityReport)
    assert response.name == "name_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_get_vulnerability_report_rest_interceptors(null_interceptor):
    transport = transports.OsConfigZonalServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.OsConfigZonalServiceRestInterceptor(),
    )
    client = OsConfigZonalServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.OsConfigZonalServiceRestInterceptor,
            "post_get_vulnerability_report",
        ) as post,
        mock.patch.object(
            transports.OsConfigZonalServiceRestInterceptor,
            "post_get_vulnerability_report_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.OsConfigZonalServiceRestInterceptor,
            "pre_get_vulnerability_report",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = vulnerability.GetVulnerabilityReportRequest.pb(
            vulnerability.GetVulnerabilityReportRequest()
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
        return_value = vulnerability.VulnerabilityReport.to_json(
            vulnerability.VulnerabilityReport()
        )
        req.return_value.content = return_value

        request = vulnerability.GetVulnerabilityReportRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = vulnerability.VulnerabilityReport()
        post_with_metadata.return_value = vulnerability.VulnerabilityReport(), metadata

        client.get_vulnerability_report(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_list_vulnerability_reports_rest_bad_request(
    request_type=vulnerability.ListVulnerabilityReportsRequest,
):
    client = OsConfigZonalServiceClient(
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
        client.list_vulnerability_reports(request)


@pytest.mark.parametrize(
    "request_type",
    [
        vulnerability.ListVulnerabilityReportsRequest,
        dict,
    ],
)
def test_list_vulnerability_reports_rest_call_success(request_type):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1/locations/sample2/instances/sample3"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = vulnerability.ListVulnerabilityReportsResponse(
            next_page_token="next_page_token_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = vulnerability.ListVulnerabilityReportsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.list_vulnerability_reports(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListVulnerabilityReportsPager)
    assert response.next_page_token == "next_page_token_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_list_vulnerability_reports_rest_interceptors(null_interceptor):
    transport = transports.OsConfigZonalServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.OsConfigZonalServiceRestInterceptor(),
    )
    client = OsConfigZonalServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.OsConfigZonalServiceRestInterceptor,
            "post_list_vulnerability_reports",
        ) as post,
        mock.patch.object(
            transports.OsConfigZonalServiceRestInterceptor,
            "post_list_vulnerability_reports_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.OsConfigZonalServiceRestInterceptor,
            "pre_list_vulnerability_reports",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = vulnerability.ListVulnerabilityReportsRequest.pb(
            vulnerability.ListVulnerabilityReportsRequest()
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
        return_value = vulnerability.ListVulnerabilityReportsResponse.to_json(
            vulnerability.ListVulnerabilityReportsResponse()
        )
        req.return_value.content = return_value

        request = vulnerability.ListVulnerabilityReportsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = vulnerability.ListVulnerabilityReportsResponse()
        post_with_metadata.return_value = (
            vulnerability.ListVulnerabilityReportsResponse(),
            metadata,
        )

        client.list_vulnerability_reports(
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
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    assert client is not None


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_create_os_policy_assignment_empty_call_rest():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.create_os_policy_assignment), "__call__"
    ) as call:
        client.create_os_policy_assignment(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = os_policy_assignments.CreateOSPolicyAssignmentRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_update_os_policy_assignment_empty_call_rest():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.update_os_policy_assignment), "__call__"
    ) as call:
        client.update_os_policy_assignment(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = os_policy_assignments.UpdateOSPolicyAssignmentRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_os_policy_assignment_empty_call_rest():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.get_os_policy_assignment), "__call__"
    ) as call:
        client.get_os_policy_assignment(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = os_policy_assignments.GetOSPolicyAssignmentRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_os_policy_assignments_empty_call_rest():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_os_policy_assignments), "__call__"
    ) as call:
        client.list_os_policy_assignments(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = os_policy_assignments.ListOSPolicyAssignmentsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_os_policy_assignment_revisions_empty_call_rest():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_os_policy_assignment_revisions), "__call__"
    ) as call:
        client.list_os_policy_assignment_revisions(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = os_policy_assignments.ListOSPolicyAssignmentRevisionsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_delete_os_policy_assignment_empty_call_rest():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_os_policy_assignment), "__call__"
    ) as call:
        client.delete_os_policy_assignment(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = os_policy_assignments.DeleteOSPolicyAssignmentRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_instance_os_policies_compliance_empty_call_rest():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.get_instance_os_policies_compliance), "__call__"
    ) as call:
        client.get_instance_os_policies_compliance(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = (
            instance_os_policies_compliance.GetInstanceOSPoliciesComplianceRequest()
        )
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_instance_os_policies_compliances_empty_call_rest():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_instance_os_policies_compliances), "__call__"
    ) as call:
        client.list_instance_os_policies_compliances(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = (
            instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesRequest()
        )
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_os_policy_assignment_report_empty_call_rest():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.get_os_policy_assignment_report), "__call__"
    ) as call:
        client.get_os_policy_assignment_report(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = os_policy_assignment_reports.GetOSPolicyAssignmentReportRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_os_policy_assignment_reports_empty_call_rest():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_os_policy_assignment_reports), "__call__"
    ) as call:
        client.list_os_policy_assignment_reports(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = (
            os_policy_assignment_reports.ListOSPolicyAssignmentReportsRequest()
        )
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_inventory_empty_call_rest():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_inventory), "__call__") as call:
        client.get_inventory(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = inventory.GetInventoryRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_inventories_empty_call_rest():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.list_inventories), "__call__") as call:
        client.list_inventories(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = inventory.ListInventoriesRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_vulnerability_report_empty_call_rest():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.get_vulnerability_report), "__call__"
    ) as call:
        client.get_vulnerability_report(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = vulnerability.GetVulnerabilityReportRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_vulnerability_reports_empty_call_rest():
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_vulnerability_reports), "__call__"
    ) as call:
        client.list_vulnerability_reports(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = vulnerability.ListVulnerabilityReportsRequest()
        assert args[0] == request_msg


def test_os_config_zonal_service_rest_lro_client():
    client = OsConfigZonalServiceClient(
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
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    assert isinstance(
        client.transport,
        transports.OsConfigZonalServiceGrpcTransport,
    )


def test_os_config_zonal_service_base_transport_error():
    # Passing both a credentials object and credentials_file should raise an error
    with pytest.raises(core_exceptions.DuplicateCredentialArgs):
        transport = transports.OsConfigZonalServiceTransport(
            credentials=ga_credentials.AnonymousCredentials(),
            credentials_file="credentials.json",
        )


def test_os_config_zonal_service_base_transport():
    # Instantiate the base transport.
    with mock.patch(
        "google.cloud.osconfig_v1alpha.services.os_config_zonal_service.transports.OsConfigZonalServiceTransport.__init__"
    ) as Transport:
        Transport.return_value = None
        transport = transports.OsConfigZonalServiceTransport(
            credentials=ga_credentials.AnonymousCredentials(),
        )

    # Every method on the transport should just blindly
    # raise NotImplementedError.
    methods = (
        "create_os_policy_assignment",
        "update_os_policy_assignment",
        "get_os_policy_assignment",
        "list_os_policy_assignments",
        "list_os_policy_assignment_revisions",
        "delete_os_policy_assignment",
        "get_instance_os_policies_compliance",
        "list_instance_os_policies_compliances",
        "get_os_policy_assignment_report",
        "list_os_policy_assignment_reports",
        "get_inventory",
        "list_inventories",
        "get_vulnerability_report",
        "list_vulnerability_reports",
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


def test_os_config_zonal_service_base_transport_with_credentials_file():
    # Instantiate the base transport with a credentials file
    with (
        mock.patch.object(
            google.auth, "load_credentials_from_file", autospec=True
        ) as load_creds,
        mock.patch(
            "google.cloud.osconfig_v1alpha.services.os_config_zonal_service.transports.OsConfigZonalServiceTransport._prep_wrapped_messages"
        ) as Transport,
    ):
        Transport.return_value = None
        load_creds.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.OsConfigZonalServiceTransport(
            credentials_file="credentials.json",
            quota_project_id="octopus",
        )
        load_creds.assert_called_once_with(
            "credentials.json",
            scopes=None,
            default_scopes=("https://www.googleapis.com/auth/cloud-platform",),
            quota_project_id="octopus",
        )


def test_os_config_zonal_service_base_transport_with_adc():
    # Test the default credentials are used if credentials and credentials_file are None.
    with (
        mock.patch.object(google.auth, "default", autospec=True) as adc,
        mock.patch(
            "google.cloud.osconfig_v1alpha.services.os_config_zonal_service.transports.OsConfigZonalServiceTransport._prep_wrapped_messages"
        ) as Transport,
    ):
        Transport.return_value = None
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.OsConfigZonalServiceTransport()
        adc.assert_called_once()


def test_os_config_zonal_service_auth_adc():
    # If no credentials are provided, we should use ADC credentials.
    with mock.patch.object(google.auth, "default", autospec=True) as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        OsConfigZonalServiceClient()
        adc.assert_called_once_with(
            scopes=None,
            default_scopes=("https://www.googleapis.com/auth/cloud-platform",),
            quota_project_id=None,
        )


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.OsConfigZonalServiceGrpcTransport,
        transports.OsConfigZonalServiceGrpcAsyncIOTransport,
    ],
)
def test_os_config_zonal_service_transport_auth_adc(transport_class):
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
        transports.OsConfigZonalServiceGrpcTransport,
        transports.OsConfigZonalServiceGrpcAsyncIOTransport,
        transports.OsConfigZonalServiceRestTransport,
    ],
)
def test_os_config_zonal_service_transport_auth_gdch_credentials(transport_class):
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
        (transports.OsConfigZonalServiceGrpcTransport, grpc_helpers),
        (transports.OsConfigZonalServiceGrpcAsyncIOTransport, grpc_helpers_async),
    ],
)
def test_os_config_zonal_service_transport_create_channel(
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
            "osconfig.googleapis.com:443",
            credentials=creds,
            credentials_file=None,
            quota_project_id="octopus",
            default_scopes=("https://www.googleapis.com/auth/cloud-platform",),
            scopes=["1", "2"],
            default_host="osconfig.googleapis.com",
            ssl_credentials=None,
            options=[
                ("grpc.max_send_message_length", -1),
                ("grpc.max_receive_message_length", -1),
            ],
        )


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.OsConfigZonalServiceGrpcTransport,
        transports.OsConfigZonalServiceGrpcAsyncIOTransport,
    ],
)
def test_os_config_zonal_service_grpc_transport_client_cert_source_for_mtls(
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


def test_os_config_zonal_service_http_transport_client_cert_source_for_mtls():
    cred = ga_credentials.AnonymousCredentials()
    with mock.patch(
        "google.auth.transport.requests.AuthorizedSession.configure_mtls_channel"
    ) as mock_configure_mtls_channel:
        transports.OsConfigZonalServiceRestTransport(
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
def test_os_config_zonal_service_host_no_port(transport_name):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(
            api_endpoint="osconfig.googleapis.com"
        ),
        transport=transport_name,
    )
    assert client.transport._host == (
        "osconfig.googleapis.com:443"
        if transport_name in ["grpc", "grpc_asyncio"]
        else "https://osconfig.googleapis.com"
    )


@pytest.mark.parametrize(
    "transport_name",
    [
        "grpc",
        "grpc_asyncio",
        "rest",
    ],
)
def test_os_config_zonal_service_host_with_port(transport_name):
    client = OsConfigZonalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(
            api_endpoint="osconfig.googleapis.com:8000"
        ),
        transport=transport_name,
    )
    assert client.transport._host == (
        "osconfig.googleapis.com:8000"
        if transport_name in ["grpc", "grpc_asyncio"]
        else "https://osconfig.googleapis.com:8000"
    )


@pytest.mark.parametrize(
    "transport_name",
    [
        "rest",
    ],
)
def test_os_config_zonal_service_client_transport_session_collision(transport_name):
    creds1 = ga_credentials.AnonymousCredentials()
    creds2 = ga_credentials.AnonymousCredentials()
    client1 = OsConfigZonalServiceClient(
        credentials=creds1,
        transport=transport_name,
    )
    client2 = OsConfigZonalServiceClient(
        credentials=creds2,
        transport=transport_name,
    )
    session1 = client1.transport.create_os_policy_assignment._session
    session2 = client2.transport.create_os_policy_assignment._session
    assert session1 != session2
    session1 = client1.transport.update_os_policy_assignment._session
    session2 = client2.transport.update_os_policy_assignment._session
    assert session1 != session2
    session1 = client1.transport.get_os_policy_assignment._session
    session2 = client2.transport.get_os_policy_assignment._session
    assert session1 != session2
    session1 = client1.transport.list_os_policy_assignments._session
    session2 = client2.transport.list_os_policy_assignments._session
    assert session1 != session2
    session1 = client1.transport.list_os_policy_assignment_revisions._session
    session2 = client2.transport.list_os_policy_assignment_revisions._session
    assert session1 != session2
    session1 = client1.transport.delete_os_policy_assignment._session
    session2 = client2.transport.delete_os_policy_assignment._session
    assert session1 != session2
    session1 = client1.transport.get_instance_os_policies_compliance._session
    session2 = client2.transport.get_instance_os_policies_compliance._session
    assert session1 != session2
    session1 = client1.transport.list_instance_os_policies_compliances._session
    session2 = client2.transport.list_instance_os_policies_compliances._session
    assert session1 != session2
    session1 = client1.transport.get_os_policy_assignment_report._session
    session2 = client2.transport.get_os_policy_assignment_report._session
    assert session1 != session2
    session1 = client1.transport.list_os_policy_assignment_reports._session
    session2 = client2.transport.list_os_policy_assignment_reports._session
    assert session1 != session2
    session1 = client1.transport.get_inventory._session
    session2 = client2.transport.get_inventory._session
    assert session1 != session2
    session1 = client1.transport.list_inventories._session
    session2 = client2.transport.list_inventories._session
    assert session1 != session2
    session1 = client1.transport.get_vulnerability_report._session
    session2 = client2.transport.get_vulnerability_report._session
    assert session1 != session2
    session1 = client1.transport.list_vulnerability_reports._session
    session2 = client2.transport.list_vulnerability_reports._session
    assert session1 != session2


def test_os_config_zonal_service_grpc_transport_channel():
    channel = grpc.secure_channel("http://localhost/", grpc.local_channel_credentials())

    # Check that channel is used if provided.
    transport = transports.OsConfigZonalServiceGrpcTransport(
        host="squid.clam.whelk",
        channel=channel,
    )
    assert transport.grpc_channel == channel
    assert transport._host == "squid.clam.whelk:443"
    assert transport._ssl_channel_credentials == None


def test_os_config_zonal_service_grpc_asyncio_transport_channel():
    channel = aio.secure_channel("http://localhost/", grpc.local_channel_credentials())

    # Check that channel is used if provided.
    transport = transports.OsConfigZonalServiceGrpcAsyncIOTransport(
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
        transports.OsConfigZonalServiceGrpcTransport,
        transports.OsConfigZonalServiceGrpcAsyncIOTransport,
    ],
)
def test_os_config_zonal_service_transport_channel_mtls_with_client_cert_source(
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
        transports.OsConfigZonalServiceGrpcTransport,
        transports.OsConfigZonalServiceGrpcAsyncIOTransport,
    ],
)
def test_os_config_zonal_service_transport_channel_mtls_with_adc(transport_class):
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


def test_os_config_zonal_service_grpc_lro_client():
    client = OsConfigZonalServiceClient(
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


def test_os_config_zonal_service_grpc_lro_async_client():
    client = OsConfigZonalServiceAsyncClient(
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


def test_instance_path():
    project = "squid"
    location = "clam"
    instance = "whelk"
    expected = "projects/{project}/locations/{location}/instances/{instance}".format(
        project=project,
        location=location,
        instance=instance,
    )
    actual = OsConfigZonalServiceClient.instance_path(project, location, instance)
    assert expected == actual


def test_parse_instance_path():
    expected = {
        "project": "octopus",
        "location": "oyster",
        "instance": "nudibranch",
    }
    path = OsConfigZonalServiceClient.instance_path(**expected)

    # Check that the path construction is reversible.
    actual = OsConfigZonalServiceClient.parse_instance_path(path)
    assert expected == actual


def test_instance_os_policies_compliance_path():
    project = "cuttlefish"
    location = "mussel"
    instance = "winkle"
    expected = "projects/{project}/locations/{location}/instanceOSPoliciesCompliances/{instance}".format(
        project=project,
        location=location,
        instance=instance,
    )
    actual = OsConfigZonalServiceClient.instance_os_policies_compliance_path(
        project, location, instance
    )
    assert expected == actual


def test_parse_instance_os_policies_compliance_path():
    expected = {
        "project": "nautilus",
        "location": "scallop",
        "instance": "abalone",
    }
    path = OsConfigZonalServiceClient.instance_os_policies_compliance_path(**expected)

    # Check that the path construction is reversible.
    actual = OsConfigZonalServiceClient.parse_instance_os_policies_compliance_path(path)
    assert expected == actual


def test_instance_os_policy_assignment_path():
    project = "squid"
    location = "clam"
    instance = "whelk"
    assignment = "octopus"
    expected = "projects/{project}/locations/{location}/instances/{instance}/osPolicyAssignments/{assignment}".format(
        project=project,
        location=location,
        instance=instance,
        assignment=assignment,
    )
    actual = OsConfigZonalServiceClient.instance_os_policy_assignment_path(
        project, location, instance, assignment
    )
    assert expected == actual


def test_parse_instance_os_policy_assignment_path():
    expected = {
        "project": "oyster",
        "location": "nudibranch",
        "instance": "cuttlefish",
        "assignment": "mussel",
    }
    path = OsConfigZonalServiceClient.instance_os_policy_assignment_path(**expected)

    # Check that the path construction is reversible.
    actual = OsConfigZonalServiceClient.parse_instance_os_policy_assignment_path(path)
    assert expected == actual


def test_inventory_path():
    project = "winkle"
    location = "nautilus"
    instance = "scallop"
    expected = (
        "projects/{project}/locations/{location}/instances/{instance}/inventory".format(
            project=project,
            location=location,
            instance=instance,
        )
    )
    actual = OsConfigZonalServiceClient.inventory_path(project, location, instance)
    assert expected == actual


def test_parse_inventory_path():
    expected = {
        "project": "abalone",
        "location": "squid",
        "instance": "clam",
    }
    path = OsConfigZonalServiceClient.inventory_path(**expected)

    # Check that the path construction is reversible.
    actual = OsConfigZonalServiceClient.parse_inventory_path(path)
    assert expected == actual


def test_os_policy_assignment_path():
    project = "whelk"
    location = "octopus"
    os_policy_assignment = "oyster"
    expected = "projects/{project}/locations/{location}/osPolicyAssignments/{os_policy_assignment}".format(
        project=project,
        location=location,
        os_policy_assignment=os_policy_assignment,
    )
    actual = OsConfigZonalServiceClient.os_policy_assignment_path(
        project, location, os_policy_assignment
    )
    assert expected == actual


def test_parse_os_policy_assignment_path():
    expected = {
        "project": "nudibranch",
        "location": "cuttlefish",
        "os_policy_assignment": "mussel",
    }
    path = OsConfigZonalServiceClient.os_policy_assignment_path(**expected)

    # Check that the path construction is reversible.
    actual = OsConfigZonalServiceClient.parse_os_policy_assignment_path(path)
    assert expected == actual


def test_os_policy_assignment_report_path():
    project = "winkle"
    location = "nautilus"
    instance = "scallop"
    assignment = "abalone"
    expected = "projects/{project}/locations/{location}/instances/{instance}/osPolicyAssignments/{assignment}/report".format(
        project=project,
        location=location,
        instance=instance,
        assignment=assignment,
    )
    actual = OsConfigZonalServiceClient.os_policy_assignment_report_path(
        project, location, instance, assignment
    )
    assert expected == actual


def test_parse_os_policy_assignment_report_path():
    expected = {
        "project": "squid",
        "location": "clam",
        "instance": "whelk",
        "assignment": "octopus",
    }
    path = OsConfigZonalServiceClient.os_policy_assignment_report_path(**expected)

    # Check that the path construction is reversible.
    actual = OsConfigZonalServiceClient.parse_os_policy_assignment_report_path(path)
    assert expected == actual


def test_vulnerability_report_path():
    project = "oyster"
    location = "nudibranch"
    instance = "cuttlefish"
    expected = "projects/{project}/locations/{location}/instances/{instance}/vulnerabilityReport".format(
        project=project,
        location=location,
        instance=instance,
    )
    actual = OsConfigZonalServiceClient.vulnerability_report_path(
        project, location, instance
    )
    assert expected == actual


def test_parse_vulnerability_report_path():
    expected = {
        "project": "mussel",
        "location": "winkle",
        "instance": "nautilus",
    }
    path = OsConfigZonalServiceClient.vulnerability_report_path(**expected)

    # Check that the path construction is reversible.
    actual = OsConfigZonalServiceClient.parse_vulnerability_report_path(path)
    assert expected == actual


def test_common_billing_account_path():
    billing_account = "scallop"
    expected = "billingAccounts/{billing_account}".format(
        billing_account=billing_account,
    )
    actual = OsConfigZonalServiceClient.common_billing_account_path(billing_account)
    assert expected == actual


def test_parse_common_billing_account_path():
    expected = {
        "billing_account": "abalone",
    }
    path = OsConfigZonalServiceClient.common_billing_account_path(**expected)

    # Check that the path construction is reversible.
    actual = OsConfigZonalServiceClient.parse_common_billing_account_path(path)
    assert expected == actual


def test_common_folder_path():
    folder = "squid"
    expected = "folders/{folder}".format(
        folder=folder,
    )
    actual = OsConfigZonalServiceClient.common_folder_path(folder)
    assert expected == actual


def test_parse_common_folder_path():
    expected = {
        "folder": "clam",
    }
    path = OsConfigZonalServiceClient.common_folder_path(**expected)

    # Check that the path construction is reversible.
    actual = OsConfigZonalServiceClient.parse_common_folder_path(path)
    assert expected == actual


def test_common_organization_path():
    organization = "whelk"
    expected = "organizations/{organization}".format(
        organization=organization,
    )
    actual = OsConfigZonalServiceClient.common_organization_path(organization)
    assert expected == actual


def test_parse_common_organization_path():
    expected = {
        "organization": "octopus",
    }
    path = OsConfigZonalServiceClient.common_organization_path(**expected)

    # Check that the path construction is reversible.
    actual = OsConfigZonalServiceClient.parse_common_organization_path(path)
    assert expected == actual


def test_common_project_path():
    project = "oyster"
    expected = "projects/{project}".format(
        project=project,
    )
    actual = OsConfigZonalServiceClient.common_project_path(project)
    assert expected == actual


def test_parse_common_project_path():
    expected = {
        "project": "nudibranch",
    }
    path = OsConfigZonalServiceClient.common_project_path(**expected)

    # Check that the path construction is reversible.
    actual = OsConfigZonalServiceClient.parse_common_project_path(path)
    assert expected == actual


def test_common_location_path():
    project = "cuttlefish"
    location = "mussel"
    expected = "projects/{project}/locations/{location}".format(
        project=project,
        location=location,
    )
    actual = OsConfigZonalServiceClient.common_location_path(project, location)
    assert expected == actual


def test_parse_common_location_path():
    expected = {
        "project": "winkle",
        "location": "nautilus",
    }
    path = OsConfigZonalServiceClient.common_location_path(**expected)

    # Check that the path construction is reversible.
    actual = OsConfigZonalServiceClient.parse_common_location_path(path)
    assert expected == actual


def test_client_with_default_client_info():
    client_info = gapic_v1.client_info.ClientInfo()

    with mock.patch.object(
        transports.OsConfigZonalServiceTransport, "_prep_wrapped_messages"
    ) as prep:
        client = OsConfigZonalServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)

    with mock.patch.object(
        transports.OsConfigZonalServiceTransport, "_prep_wrapped_messages"
    ) as prep:
        transport_class = OsConfigZonalServiceClient.get_transport_class()
        transport = transport_class(
            credentials=ga_credentials.AnonymousCredentials(),
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)


def test_transport_close_grpc():
    client = OsConfigZonalServiceClient(
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
    client = OsConfigZonalServiceAsyncClient(
        credentials=async_anonymous_credentials(), transport="grpc_asyncio"
    )
    with mock.patch.object(
        type(getattr(client.transport, "_grpc_channel")), "close"
    ) as close:
        async with client:
            close.assert_not_called()
        close.assert_called_once()


def test_transport_close_rest():
    client = OsConfigZonalServiceClient(
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
        client = OsConfigZonalServiceClient(
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
        (OsConfigZonalServiceClient, transports.OsConfigZonalServiceGrpcTransport),
        (
            OsConfigZonalServiceAsyncClient,
            transports.OsConfigZonalServiceGrpcAsyncIOTransport,
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
