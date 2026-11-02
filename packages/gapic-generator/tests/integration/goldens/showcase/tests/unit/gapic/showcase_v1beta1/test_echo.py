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
import os
import asyncio
import re
from unittest import mock
from unittest.mock import AsyncMock

import grpc
from grpc.experimental import aio
from collections.abc import Iterable, AsyncIterable
from google.protobuf import json_format
import json
import math
import pytest
from collections.abc import Sequence, Mapping
from google.api_core import api_core_version
from proto.marshal.rules.dates import DurationRule, TimestampRule
from proto.marshal.rules import wrappers
from requests import Response
from requests import Request, PreparedRequest
from requests.sessions import Session
from google.protobuf import json_format

try:
    from google.auth.aio import credentials as ga_credentials_async
    HAS_GOOGLE_AUTH_AIO = True
except ImportError: # pragma: NO COVER
    HAS_GOOGLE_AUTH_AIO = False

from google.api_core import client_options
from google.api_core import exceptions as core_exceptions
from google.api_core import future
from google.api_core import gapic_v1
from google.api_core import grpc_helpers
from google.api_core import grpc_helpers_async
from google.api_core import operation
from google.api_core import operations_v1
from google.api_core import path_template
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials
from google.auth.exceptions import MutualTLSChannelError
from google.cloud.location import locations_pb2
from google.iam.v1 import iam_policy_pb2  # type: ignore
from google.iam.v1 import options_pb2  # type: ignore
from google.iam.v1 import policy_pb2  # type: ignore
from google.longrunning import operations_pb2 # type: ignore
from google.oauth2 import service_account
from google.showcase_v1beta1.services.echo import EchoAsyncClient
from google.showcase_v1beta1.services.echo import EchoClient
from google.showcase_v1beta1.services.echo import pagers
from google.showcase_v1beta1.services.echo import transports
from google.showcase_v1beta1.services.echo.client import _observability
from google.showcase_v1beta1.types import echo as gs_echo
import google.api_core.operation_async as operation_async  # type: ignore
import google.auth
import google.protobuf.any_pb2 as any_pb2  # type: ignore
import google.protobuf.duration_pb2 as duration_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.rpc.status_pb2 as status_pb2  # type: ignore
try:
    from google.api_core import version_header
    HAS_GOOGLE_API_CORE_VERSION_HEADER = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    HAS_GOOGLE_API_CORE_VERSION_HEADER = False



CRED_INFO_JSON = {
    "credential_source": "/path/to/file",
    "credential_type": "service account credentials",
    "principal": "service-account@example.com",
}
CRED_INFO_STRING = json.dumps(CRED_INFO_JSON)
_UUID4_RE = re.compile(r"[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}")


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
    return "foo.googleapis.com" if ("localhost" in client.DEFAULT_ENDPOINT) else client.DEFAULT_ENDPOINT

# If default endpoint template is localhost, then default mtls endpoint will be the same.
# This method modifies the default endpoint template so the client can produce a different
# mtls endpoint for endpoint testing purposes.
def modify_default_endpoint_template(client):
    return "test.{UNIVERSE_DOMAIN}" if ("localhost" in client._DEFAULT_ENDPOINT_TEMPLATE) else client._DEFAULT_ENDPOINT_TEMPLATE


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

    assert EchoClient._get_client_cert_source(None, False) is None
    assert EchoClient._get_client_cert_source(mock_provided_cert_source, False) is None
    assert EchoClient._get_client_cert_source(mock_provided_cert_source, True) == mock_provided_cert_source

    with mock.patch('google.auth.transport.mtls.has_default_client_cert_source', return_value=True):
        with mock.patch('google.auth.transport.mtls.default_client_cert_source', return_value=mock_default_cert_source):
            assert EchoClient._get_client_cert_source(None, True) is mock_default_cert_source
            assert EchoClient._get_client_cert_source(mock_provided_cert_source, "true") is mock_provided_cert_source


@pytest.mark.parametrize("transport_name", [
    ("grpc"),
    ("rest"),
])
def test_echo_api_version_header(transport_name):
    client = EchoClient(credentials=ga_credentials.AnonymousCredentials(), transport=transport_name)
    # TODO: Make this test unconditional once the minimum supported version of
    # google-api-core becomes 2.19.0 or higher.
    api_core_major, api_core_minor = [int(part) for part in api_core_version.__version__.split(".")[0:2]]
    if api_core_major > 2 or (api_core_major == 2 and api_core_minor >= 19):
        # Mock the actual call within the gRPC stub, and fake the request.
        with mock.patch.object(
                type(client.transport.echo),
                '__call__'
            ) as call:
                call.return_value = gs_echo.EchoResponse()
                client.echo()

        # Establish that the api version header was sent.
        _, _, kw = call.mock_calls[0]
        assert (
            version_header.API_VERSION_METADATA_KEY,
            "v1_20240408",
        ) in kw['metadata']
    else:
        pytest.skip("google-api-core>=2.19.0 is required for `google.api_core.version_header`")
@pytest.mark.parametrize("transport_name", [
    ("grpc"),
    ("rest"),
])
def test_echo_error_details_api_version_header(transport_name):
    client = EchoClient(credentials=ga_credentials.AnonymousCredentials(), transport=transport_name)
    # TODO: Make this test unconditional once the minimum supported version of
    # google-api-core becomes 2.19.0 or higher.
    api_core_major, api_core_minor = [int(part) for part in api_core_version.__version__.split(".")[0:2]]
    if api_core_major > 2 or (api_core_major == 2 and api_core_minor >= 19):
        # Mock the actual call within the gRPC stub, and fake the request.
        with mock.patch.object(
                type(client.transport.echo_error_details),
                '__call__'
            ) as call:
                call.return_value = gs_echo.EchoErrorDetailsResponse()
                client.echo_error_details()

        # Establish that the api version header was sent.
        _, _, kw = call.mock_calls[0]
        assert (
            version_header.API_VERSION_METADATA_KEY,
            "v1_20240408",
        ) in kw['metadata']
    else:
        pytest.skip("google-api-core>=2.19.0 is required for `google.api_core.version_header`")
@pytest.mark.parametrize("transport_name", [
    ("grpc"),
    ("rest"),
])
def test_fail_echo_with_details_api_version_header(transport_name):
    client = EchoClient(credentials=ga_credentials.AnonymousCredentials(), transport=transport_name)
    # TODO: Make this test unconditional once the minimum supported version of
    # google-api-core becomes 2.19.0 or higher.
    api_core_major, api_core_minor = [int(part) for part in api_core_version.__version__.split(".")[0:2]]
    if api_core_major > 2 or (api_core_major == 2 and api_core_minor >= 19):
        # Mock the actual call within the gRPC stub, and fake the request.
        with mock.patch.object(
                type(client.transport.fail_echo_with_details),
                '__call__'
            ) as call:
                call.return_value = gs_echo.FailEchoWithDetailsResponse()
                client.fail_echo_with_details()

        # Establish that the api version header was sent.
        _, _, kw = call.mock_calls[0]
        assert (
            version_header.API_VERSION_METADATA_KEY,
            "v1_20240408",
        ) in kw['metadata']
    else:
        pytest.skip("google-api-core>=2.19.0 is required for `google.api_core.version_header`")
@pytest.mark.parametrize("transport_name", [
    ("grpc"),
    ("rest"),
])
def test_expand_api_version_header(transport_name):
    client = EchoClient(credentials=ga_credentials.AnonymousCredentials(), transport=transport_name)
    # TODO: Make this test unconditional once the minimum supported version of
    # google-api-core becomes 2.19.0 or higher.
    api_core_major, api_core_minor = [int(part) for part in api_core_version.__version__.split(".")[0:2]]
    if api_core_major > 2 or (api_core_major == 2 and api_core_minor >= 19):
        # Mock the actual call within the gRPC stub, and fake the request.
        with mock.patch.object(
                type(client.transport.expand),
                '__call__'
            ) as call:
                call.return_value = gs_echo.EchoResponse()
                client.expand()

        # Establish that the api version header was sent.
        _, _, kw = call.mock_calls[0]
        assert (
            version_header.API_VERSION_METADATA_KEY,
            "v1_20240408",
        ) in kw['metadata']
    else:
        pytest.skip("google-api-core>=2.19.0 is required for `google.api_core.version_header`")
@pytest.mark.parametrize("transport_name", [
    ("grpc"),
    ("rest"),
])
def test_collect_api_version_header(transport_name):
    client = EchoClient(credentials=ga_credentials.AnonymousCredentials(), transport=transport_name)
    # TODO: Make this test unconditional once the minimum supported version of
    # google-api-core becomes 2.19.0 or higher.
    api_core_major, api_core_minor = [int(part) for part in api_core_version.__version__.split(".")[0:2]]
    if api_core_major > 2 or (api_core_major == 2 and api_core_minor >= 19):
        # Mock the actual call within the gRPC stub, and fake the request.
        with mock.patch.object(
                type(client.transport.collect),
                '__call__'
            ) as call:
                call.return_value = gs_echo.EchoResponse()
                client.collect()

        # Establish that the api version header was sent.
        _, _, kw = call.mock_calls[0]
        assert (
            version_header.API_VERSION_METADATA_KEY,
            "v1_20240408",
        ) in kw['metadata']
    else:
        pytest.skip("google-api-core>=2.19.0 is required for `google.api_core.version_header`")
@pytest.mark.parametrize("transport_name", [
    ("grpc"),
    ("rest"),
])
def test_chat_api_version_header(transport_name):
    client = EchoClient(credentials=ga_credentials.AnonymousCredentials(), transport=transport_name)
    # TODO: Make this test unconditional once the minimum supported version of
    # google-api-core becomes 2.19.0 or higher.
    api_core_major, api_core_minor = [int(part) for part in api_core_version.__version__.split(".")[0:2]]
    if api_core_major > 2 or (api_core_major == 2 and api_core_minor >= 19):
        # Mock the actual call within the gRPC stub, and fake the request.
        with mock.patch.object(
                type(client.transport.chat),
                '__call__'
            ) as call:
                call.return_value = gs_echo.EchoResponse()
                client.chat()

        # Establish that the api version header was sent.
        _, _, kw = call.mock_calls[0]
        assert (
            version_header.API_VERSION_METADATA_KEY,
            "v1_20240408",
        ) in kw['metadata']
    else:
        pytest.skip("google-api-core>=2.19.0 is required for `google.api_core.version_header`")
@pytest.mark.parametrize("transport_name", [
    ("grpc"),
    ("rest"),
])
def test_paged_expand_api_version_header(transport_name):
    client = EchoClient(credentials=ga_credentials.AnonymousCredentials(), transport=transport_name)
    # TODO: Make this test unconditional once the minimum supported version of
    # google-api-core becomes 2.19.0 or higher.
    api_core_major, api_core_minor = [int(part) for part in api_core_version.__version__.split(".")[0:2]]
    if api_core_major > 2 or (api_core_major == 2 and api_core_minor >= 19):
        # Mock the actual call within the gRPC stub, and fake the request.
        with mock.patch.object(
                type(client.transport.paged_expand),
                '__call__'
            ) as call:
                call.return_value = gs_echo.PagedExpandResponse()
                client.paged_expand()

        # Establish that the api version header was sent.
        _, _, kw = call.mock_calls[0]
        assert (
            version_header.API_VERSION_METADATA_KEY,
            "v1_20240408",
        ) in kw['metadata']
    else:
        pytest.skip("google-api-core>=2.19.0 is required for `google.api_core.version_header`")
@pytest.mark.parametrize("transport_name", [
    ("grpc"),
    ("rest"),
])
def test_paged_expand_legacy_api_version_header(transport_name):
    client = EchoClient(credentials=ga_credentials.AnonymousCredentials(), transport=transport_name)
    # TODO: Make this test unconditional once the minimum supported version of
    # google-api-core becomes 2.19.0 or higher.
    api_core_major, api_core_minor = [int(part) for part in api_core_version.__version__.split(".")[0:2]]
    if api_core_major > 2 or (api_core_major == 2 and api_core_minor >= 19):
        # Mock the actual call within the gRPC stub, and fake the request.
        with mock.patch.object(
                type(client.transport.paged_expand_legacy),
                '__call__'
            ) as call:
                call.return_value = gs_echo.PagedExpandResponse()
                client.paged_expand_legacy()

        # Establish that the api version header was sent.
        _, _, kw = call.mock_calls[0]
        assert (
            version_header.API_VERSION_METADATA_KEY,
            "v1_20240408",
        ) in kw['metadata']
    else:
        pytest.skip("google-api-core>=2.19.0 is required for `google.api_core.version_header`")
@pytest.mark.parametrize("transport_name", [
    ("grpc"),
    ("rest"),
])
def test_paged_expand_legacy_mapped_api_version_header(transport_name):
    client = EchoClient(credentials=ga_credentials.AnonymousCredentials(), transport=transport_name)
    # TODO: Make this test unconditional once the minimum supported version of
    # google-api-core becomes 2.19.0 or higher.
    api_core_major, api_core_minor = [int(part) for part in api_core_version.__version__.split(".")[0:2]]
    if api_core_major > 2 or (api_core_major == 2 and api_core_minor >= 19):
        # Mock the actual call within the gRPC stub, and fake the request.
        with mock.patch.object(
                type(client.transport.paged_expand_legacy_mapped),
                '__call__'
            ) as call:
                call.return_value = gs_echo.PagedExpandLegacyMappedResponse()
                client.paged_expand_legacy_mapped()

        # Establish that the api version header was sent.
        _, _, kw = call.mock_calls[0]
        assert (
            version_header.API_VERSION_METADATA_KEY,
            "v1_20240408",
        ) in kw['metadata']
    else:
        pytest.skip("google-api-core>=2.19.0 is required for `google.api_core.version_header`")
@pytest.mark.parametrize("transport_name", [
    ("grpc"),
    ("rest"),
])
def test_wait_api_version_header(transport_name):
    client = EchoClient(credentials=ga_credentials.AnonymousCredentials(), transport=transport_name)
    # TODO: Make this test unconditional once the minimum supported version of
    # google-api-core becomes 2.19.0 or higher.
    api_core_major, api_core_minor = [int(part) for part in api_core_version.__version__.split(".")[0:2]]
    if api_core_major > 2 or (api_core_major == 2 and api_core_minor >= 19):
        # Mock the actual call within the gRPC stub, and fake the request.
        with mock.patch.object(
                type(client.transport.wait),
                '__call__'
            ) as call:
                call.return_value = operations_pb2.Operation()
                client.wait()

        # Establish that the api version header was sent.
        _, _, kw = call.mock_calls[0]
        assert (
            version_header.API_VERSION_METADATA_KEY,
            "v1_20240408",
        ) in kw['metadata']
    else:
        pytest.skip("google-api-core>=2.19.0 is required for `google.api_core.version_header`")
@pytest.mark.parametrize("transport_name", [
    ("grpc"),
    ("rest"),
])
def test_block_api_version_header(transport_name):
    client = EchoClient(credentials=ga_credentials.AnonymousCredentials(), transport=transport_name)
    # TODO: Make this test unconditional once the minimum supported version of
    # google-api-core becomes 2.19.0 or higher.
    api_core_major, api_core_minor = [int(part) for part in api_core_version.__version__.split(".")[0:2]]
    if api_core_major > 2 or (api_core_major == 2 and api_core_minor >= 19):
        # Mock the actual call within the gRPC stub, and fake the request.
        with mock.patch.object(
                type(client.transport.block),
                '__call__'
            ) as call:
                call.return_value = gs_echo.BlockResponse()
                client.block()

        # Establish that the api version header was sent.
        _, _, kw = call.mock_calls[0]
        assert (
            version_header.API_VERSION_METADATA_KEY,
            "v1_20240408",
        ) in kw['metadata']
    else:
        pytest.skip("google-api-core>=2.19.0 is required for `google.api_core.version_header`")


@pytest.mark.parametrize("error_code,cred_info_json,show_cred_info", [
    (401, CRED_INFO_JSON, True),
    (403, CRED_INFO_JSON, True),
    (404, CRED_INFO_JSON, True),
    (500, CRED_INFO_JSON, False),
    (401, None, False),
    (403, None, False),
    (404, None, False),
    (500, None, False)
])
def test__add_cred_info_for_auth_errors(error_code, cred_info_json, show_cred_info):
    cred = mock.Mock(["get_cred_info"])
    cred.get_cred_info = mock.Mock(return_value=cred_info_json)
    client = EchoClient(credentials=cred)
    client._transport._credentials = cred

    error = core_exceptions.GoogleAPICallError("message", details=["foo"])
    error.code = error_code

    client._add_cred_info_for_auth_errors(error)
    if show_cred_info:
        assert error.details == ["foo", CRED_INFO_STRING]
    else:
        assert error.details == ["foo"]

@pytest.mark.parametrize("error_code", [401,403,404,500])
def test__add_cred_info_for_auth_errors_no_get_cred_info(error_code):
    cred = mock.Mock([])
    assert not hasattr(cred, "get_cred_info")
    client = EchoClient(credentials=cred)
    client._transport._credentials = cred

    error = core_exceptions.GoogleAPICallError("message", details=[])
    error.code = error_code

    client._add_cred_info_for_auth_errors(error)
    assert error.details == []

@pytest.mark.parametrize("client_class,transport_name", [
    (EchoClient, "grpc"),
    (EchoAsyncClient, "grpc_asyncio"),
    (EchoClient, "rest"),
])
def test_echo_client_from_service_account_info(client_class, transport_name):
    creds = ga_credentials.AnonymousCredentials()
    with mock.patch.object(service_account.Credentials, 'from_service_account_info') as factory:
        factory.return_value = creds
        info = {"valid": True}
        client = client_class.from_service_account_info(info, transport=transport_name)
        assert client.transport._credentials == creds
        assert isinstance(client, client_class)

        assert client.transport._host == (
            'localhost:7469'
            if transport_name in ['grpc', 'grpc_asyncio']
            else
            'https://localhost:7469'
        )


@pytest.mark.parametrize("transport_class,transport_name", [
    (transports.EchoGrpcTransport, "grpc"),
    (transports.EchoGrpcAsyncIOTransport, "grpc_asyncio"),
    (transports.EchoRestTransport, "rest"),
])
def test_echo_client_service_account_always_use_jwt(transport_class, transport_name):
    with mock.patch.object(service_account.Credentials, 'with_always_use_jwt_access', create=True) as use_jwt:
        creds = service_account.Credentials(None, None, None)
        transport = transport_class(credentials=creds, always_use_jwt_access=True)
        use_jwt.assert_called_once_with(True)

    with mock.patch.object(service_account.Credentials, 'with_always_use_jwt_access', create=True) as use_jwt:
        creds = service_account.Credentials(None, None, None)
        transport = transport_class(credentials=creds, always_use_jwt_access=False)
        use_jwt.assert_not_called()


@pytest.mark.parametrize("client_class,transport_name", [
    (EchoClient, "grpc"),
    (EchoAsyncClient, "grpc_asyncio"),
    (EchoClient, "rest"),
])
def test_echo_client_from_service_account_file(client_class, transport_name):
    creds = ga_credentials.AnonymousCredentials()
    with mock.patch.object(service_account.Credentials, 'from_service_account_file') as factory:
        factory.return_value = creds
        client = client_class.from_service_account_file("dummy/file/path.json", transport=transport_name)
        assert client.transport._credentials == creds
        assert isinstance(client, client_class)

        client = client_class.from_service_account_json("dummy/file/path.json", transport=transport_name)
        assert client.transport._credentials == creds
        assert isinstance(client, client_class)

        assert client.transport._host == (
            'localhost:7469'
            if transport_name in ['grpc', 'grpc_asyncio']
            else
            'https://localhost:7469'
        )


def test_echo_client_get_transport_class():
    transport = EchoClient.get_transport_class()
    available_transports = [
        transports.EchoGrpcTransport,
        transports.EchoRestTransport,
    ]
    assert transport in available_transports

    transport = EchoClient.get_transport_class("grpc")
    assert transport == transports.EchoGrpcTransport


@pytest.mark.parametrize("client_class,transport_class,transport_name", [
    (EchoClient, transports.EchoGrpcTransport, "grpc"),
    (EchoAsyncClient, transports.EchoGrpcAsyncIOTransport, "grpc_asyncio"),
    (EchoClient, transports.EchoRestTransport, "rest"),
])
@mock.patch.object(EchoClient, "_DEFAULT_ENDPOINT_TEMPLATE", modify_default_endpoint_template(EchoClient))
@mock.patch.object(EchoAsyncClient, "_DEFAULT_ENDPOINT_TEMPLATE", modify_default_endpoint_template(EchoAsyncClient))
def test_echo_client_client_options(client_class, transport_class, transport_name):
    # Check that if channel is provided we won't create a new one.
    with mock.patch.object(EchoClient, 'get_transport_class') as gtc:
        transport = transport_class(
            credentials=ga_credentials.AnonymousCredentials()
        )
        client = client_class(transport=transport)
        gtc.assert_not_called()

    # Check that if channel is provided via str we will create a new one.
    with mock.patch.object(EchoClient, 'get_transport_class') as gtc:
        client = client_class(transport=transport_name)
        gtc.assert_called()

    # Check the case api_endpoint is provided.
    options = client_options.ClientOptions(api_endpoint="squid.clam.whelk")
    with mock.patch.object(transport_class, '__init__') as patched:
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
        with mock.patch.object(transport_class, '__init__') as patched:
            patched.return_value = None
            client = client_class(transport=transport_name)
            patched.assert_called_once_with(
                credentials=None,
                credentials_file=None,
                host=client._DEFAULT_ENDPOINT_TEMPLATE.format(UNIVERSE_DOMAIN=client._DEFAULT_UNIVERSE),
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
        with mock.patch.object(transport_class, '__init__') as patched:
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
    assert str(excinfo.value) == "Environment variable `GOOGLE_API_USE_MTLS_ENDPOINT` must be `never`, `auto` or `always`"

    # Check the case quota_project_id is provided
    options = client_options.ClientOptions(quota_project_id="octopus")
    with mock.patch.object(transport_class, '__init__') as patched:
        patched.return_value = None
        client = client_class(client_options=options, transport=transport_name)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host=client._DEFAULT_ENDPOINT_TEMPLATE.format(UNIVERSE_DOMAIN=client._DEFAULT_UNIVERSE),
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id="octopus",
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
            api_audience=None,
        )
    # Check the case api_endpoint is provided
    options = client_options.ClientOptions(api_audience="https://language.googleapis.com")
    with mock.patch.object(transport_class, '__init__') as patched:
        patched.return_value = None
        client = client_class(client_options=options, transport=transport_name)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host=client._DEFAULT_ENDPOINT_TEMPLATE.format(UNIVERSE_DOMAIN=client._DEFAULT_UNIVERSE),
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
            api_audience="https://language.googleapis.com"
        )

@pytest.mark.parametrize("client_class,transport_class,transport_name,use_client_cert_env", [
    (EchoClient, transports.EchoGrpcTransport, "grpc", "true"),
    (EchoAsyncClient, transports.EchoGrpcAsyncIOTransport, "grpc_asyncio", "true"),
    (EchoClient, transports.EchoGrpcTransport, "grpc", "false"),
    (EchoAsyncClient, transports.EchoGrpcAsyncIOTransport, "grpc_asyncio", "false"),
    (EchoClient, transports.EchoRestTransport, "rest", "true"),
    (EchoClient, transports.EchoRestTransport, "rest", "false"),
])
@mock.patch.object(EchoClient, "_DEFAULT_ENDPOINT_TEMPLATE", modify_default_endpoint_template(EchoClient))
@mock.patch.object(EchoAsyncClient, "_DEFAULT_ENDPOINT_TEMPLATE", modify_default_endpoint_template(EchoAsyncClient))
@mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "auto"})
def test_echo_client_mtls_env_auto(client_class, transport_class, transport_name, use_client_cert_env):
    # This tests the endpoint autoswitch behavior. Endpoint is autoswitched to the default
    # mtls endpoint, if GOOGLE_API_USE_CLIENT_CERTIFICATE is "true" and client cert exists.

    # Check the case client_cert_source is provided. Whether client cert is used depends on
    # GOOGLE_API_USE_CLIENT_CERTIFICATE value.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": use_client_cert_env}):
        options = client_options.ClientOptions(client_cert_source=client_cert_source_callback)
        with mock.patch.object(transport_class, '__init__') as patched:
            patched.return_value = None
            client = client_class(client_options=options, transport=transport_name)

            if use_client_cert_env == "false":
                expected_client_cert_source = None
                expected_host = client._DEFAULT_ENDPOINT_TEMPLATE.format(UNIVERSE_DOMAIN=client._DEFAULT_UNIVERSE)
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
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": use_client_cert_env}):
        with mock.patch.object(transport_class, '__init__') as patched:
            with mock.patch('google.auth.transport.mtls.has_default_client_cert_source', return_value=True):
                with mock.patch('google.auth.transport.mtls.default_client_cert_source', return_value=client_cert_source_callback):
                    if use_client_cert_env == "false":
                        expected_host = client._DEFAULT_ENDPOINT_TEMPLATE.format(UNIVERSE_DOMAIN=client._DEFAULT_UNIVERSE)
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
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": use_client_cert_env}):
        with mock.patch.object(transport_class, '__init__') as patched:
            with mock.patch("google.auth.transport.mtls.has_default_client_cert_source", return_value=False):
                patched.return_value = None
                client = client_class(transport=transport_name)
                patched.assert_called_once_with(
                    credentials=None,
                    credentials_file=None,
                    host=client._DEFAULT_ENDPOINT_TEMPLATE.format(UNIVERSE_DOMAIN=client._DEFAULT_UNIVERSE),
                    scopes=None,
                    client_cert_source_for_mtls=None,
                    quota_project_id=None,
                    client_info=transports.base.DEFAULT_CLIENT_INFO,
                    always_use_jwt_access=True,
                    api_audience=None,
                )


@pytest.mark.parametrize("client_class", [
    EchoClient, EchoAsyncClient
])
@mock.patch.object(EchoClient, "DEFAULT_ENDPOINT", modify_default_endpoint(EchoClient))
@mock.patch.object(EchoAsyncClient, "DEFAULT_ENDPOINT", modify_default_endpoint(EchoAsyncClient))
def test_echo_client_get_mtls_endpoint_and_cert_source(client_class):
    mock_client_cert_source = mock.Mock()

    # Test the case GOOGLE_API_USE_CLIENT_CERTIFICATE is "true".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "true"}):
        mock_api_endpoint = "foo"
        options = client_options.ClientOptions(client_cert_source=mock_client_cert_source, api_endpoint=mock_api_endpoint)
        api_endpoint, cert_source = client_class.get_mtls_endpoint_and_cert_source(options)
        assert api_endpoint == mock_api_endpoint
        assert cert_source == mock_client_cert_source

    # Test the case GOOGLE_API_USE_CLIENT_CERTIFICATE is "false".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "false"}):
        mock_client_cert_source = mock.Mock()
        mock_api_endpoint = "foo"
        options = client_options.ClientOptions(client_cert_source=mock_client_cert_source, api_endpoint=mock_api_endpoint)
        api_endpoint, cert_source = client_class.get_mtls_endpoint_and_cert_source(options)
        assert api_endpoint == mock_api_endpoint
        assert cert_source is None

    # Test the case GOOGLE_API_USE_CLIENT_CERTIFICATE is "Unsupported".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "Unsupported"}):
        if hasattr(google.auth.transport.mtls, "should_use_client_cert"):
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
                    with mock.patch("builtins.open", m), mock.patch("os.path.exists", side_effect=lambda path: os.path.basename(path) == config_filename):
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
                    with mock.patch("builtins.open", m), mock.patch("os.path.exists", side_effect=lambda path: os.path.basename(path) == config_filename):
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
        with mock.patch('google.auth.transport.mtls.has_default_client_cert_source', return_value=False):
            api_endpoint, cert_source = client_class.get_mtls_endpoint_and_cert_source()
            assert api_endpoint == client_class.DEFAULT_ENDPOINT
            assert cert_source is None

    # Test the case GOOGLE_API_USE_MTLS_ENDPOINT is "auto" and default cert exists.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "true"}):
        with mock.patch('google.auth.transport.mtls.has_default_client_cert_source', return_value=True):
            with mock.patch('google.auth.transport.mtls.default_client_cert_source', return_value=mock_client_cert_source):
                api_endpoint, cert_source = client_class.get_mtls_endpoint_and_cert_source()
                assert api_endpoint == client_class.DEFAULT_MTLS_ENDPOINT
                assert cert_source == mock_client_cert_source

    # Check the case api_endpoint is not provided and GOOGLE_API_USE_MTLS_ENDPOINT has
    # unsupported value.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "Unsupported"}):
        with pytest.raises(MutualTLSChannelError) as excinfo:
            client_class.get_mtls_endpoint_and_cert_source()

        assert str(excinfo.value) == "Environment variable `GOOGLE_API_USE_MTLS_ENDPOINT` must be `never`, `auto` or `always`"

@pytest.mark.parametrize("client_class", [
    EchoClient, EchoAsyncClient
])
@mock.patch.object(EchoClient, "_DEFAULT_ENDPOINT_TEMPLATE", modify_default_endpoint_template(EchoClient))
@mock.patch.object(EchoAsyncClient, "_DEFAULT_ENDPOINT_TEMPLATE", modify_default_endpoint_template(EchoAsyncClient))
def test_echo_client_client_api_endpoint(client_class):
    mock_client_cert_source = client_cert_source_callback
    api_override = "foo.com"
    default_universe = EchoClient._DEFAULT_UNIVERSE
    default_endpoint = EchoClient._DEFAULT_ENDPOINT_TEMPLATE.format(UNIVERSE_DOMAIN=default_universe)
    mock_universe = "bar.com"
    mock_endpoint = EchoClient._DEFAULT_ENDPOINT_TEMPLATE.format(UNIVERSE_DOMAIN=mock_universe)

    # If ClientOptions.api_endpoint is set and GOOGLE_API_USE_CLIENT_CERTIFICATE="true",
    # use ClientOptions.api_endpoint as the api endpoint regardless.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "true"}):
        with mock.patch("google.auth.transport.requests.AuthorizedSession.configure_mtls_channel"):
            options = client_options.ClientOptions(client_cert_source=mock_client_cert_source, api_endpoint=api_override)
            client = client_class(client_options=options, credentials=ga_credentials.AnonymousCredentials())
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
        client = client_class(client_options=options, credentials=ga_credentials.AnonymousCredentials())
    else:
        client = client_class(client_options=options, credentials=ga_credentials.AnonymousCredentials())
    assert client.api_endpoint == (mock_endpoint if universe_exists else default_endpoint)
    assert client.universe_domain == (mock_universe if universe_exists else default_universe)

    # If ClientOptions does not have a universe domain attribute and GOOGLE_API_USE_MTLS_ENDPOINT="never",
    # use the _DEFAULT_ENDPOINT_TEMPLATE populated with GDU as the api endpoint.
    options = client_options.ClientOptions()
    if hasattr(options, "universe_domain"):
        delattr(options, "universe_domain")
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "never"}):
        client = client_class(client_options=options, credentials=ga_credentials.AnonymousCredentials())
        assert client.api_endpoint == default_endpoint


@pytest.mark.parametrize("client_class,transport_class,transport_name", [
    (EchoClient, transports.EchoGrpcTransport, "grpc"),
    (EchoAsyncClient, transports.EchoGrpcAsyncIOTransport, "grpc_asyncio"),
    (EchoClient, transports.EchoRestTransport, "rest"),
])
def test_echo_client_client_options_scopes(client_class, transport_class, transport_name):
    # Check the case scopes are provided.
    options = client_options.ClientOptions(
        scopes=["1", "2"],
    )
    with mock.patch.object(transport_class, '__init__') as patched:
        patched.return_value = None
        client = client_class(client_options=options, transport=transport_name)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host=client._DEFAULT_ENDPOINT_TEMPLATE.format(UNIVERSE_DOMAIN=client._DEFAULT_UNIVERSE),
            scopes=["1", "2"],
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
            api_audience=None,
        )

@pytest.mark.parametrize("client_class,transport_class,transport_name,grpc_helpers", [
    (EchoClient, transports.EchoGrpcTransport, "grpc", grpc_helpers),
    (EchoAsyncClient, transports.EchoGrpcAsyncIOTransport, "grpc_asyncio", grpc_helpers_async),
    (EchoClient, transports.EchoRestTransport, "rest", None),
])
def test_echo_client_client_options_credentials_file(client_class, transport_class, transport_name, grpc_helpers):
    # Check the case credentials file is provided.
    options = client_options.ClientOptions(
        credentials_file="credentials.json"
    )

    with mock.patch.object(transport_class, '__init__') as patched:
        patched.return_value = None
        client = client_class(client_options=options, transport=transport_name)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file="credentials.json",
            host=client._DEFAULT_ENDPOINT_TEMPLATE.format(UNIVERSE_DOMAIN=client._DEFAULT_UNIVERSE),
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
            api_audience=None,
        )

def test_echo_client_client_options_from_dict():
    with mock.patch('google.showcase_v1beta1.services.echo.transports.EchoGrpcTransport.__init__') as grpc_transport:
        grpc_transport.return_value = None
        client = EchoClient(
            client_options={'api_endpoint': 'squid.clam.whelk'}
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


@pytest.mark.skipif(
    _observability is None,
    reason="Requires google-api-core with OpenTelemetry support (>= 2.36.0)",
)
@pytest.mark.parametrize("capabilities_enabled, expected_options_injected", [
    pytest.param(True, True, id="otel_injection_enabled"),
    pytest.param(False, False, id="otel_injection_disabled"),
])
def test_echo_client_otel_channel_injection(capabilities_enabled, expected_options_injected):
    with (
        mock.patch.object(
            _observability,
            "is_otel_capabilities_enabled",
            return_value=capabilities_enabled,
            autospec=True,
        ) as mock_is_otel_enabled,
        mock.patch.object(
            transports.EchoGrpcTransport, "__init__", return_value=None
        ) as patched_transport_init,
    ):
        client = EchoClient(transport="grpc")

        mock_is_otel_enabled.assert_called_once_with(client._client_options)
        called_kwargs = patched_transport_init.call_args.kwargs
        if expected_options_injected:
            assert called_kwargs.get("client_options") == client._client_options
        else:
            assert not called_kwargs.get("client_options")


def test_echo_grpc_transport_channel_interceptors():
    mock_interceptor = mock.Mock()
    mock_channel = mock.Mock()

    with (
        mock.patch.object(
            transports.EchoGrpcTransport,
            "create_channel",
            return_value=mock_channel,
        ),
        mock.patch.object(
            grpc_helpers,
            "apply_channel_interceptors",
            return_value=mock_channel,
            create=True,
        ) as mock_apply_interceptors,
    ):
        transport = transports.EchoGrpcTransport(
            credentials=ga_credentials.AnonymousCredentials(),
            interceptors=[mock_interceptor],
        )

        mock_apply_interceptors.assert_called_once_with(
            mock_channel, [mock_interceptor]
        )
        assert transport.grpc_channel == mock_channel


@pytest.mark.skipif(
    _observability is None,
    reason="Requires google-api-core with OpenTelemetry support (>= 2.36.0)",
)
def test_echo_grpc_transport_otel_channel_interceptor():
    mock_otel_interceptor = mock.Mock()
    mock_channel = mock.Mock()

    with (
        mock.patch.object(
            _observability,
            "get_otel_interceptor",
            return_value=mock_otel_interceptor,
        ) as mock_get_interceptor,
        mock.patch.object(
            transports.EchoGrpcTransport,
            "create_channel",
            return_value=mock_channel,
        ),
        mock.patch.object(
            grpc_helpers,
            "apply_channel_interceptors",
            return_value=mock_channel,
            create=True,
        ) as mock_apply_interceptors,
    ):
        options = client_options.ClientOptions()
        transport = transports.EchoGrpcTransport(
            credentials=ga_credentials.AnonymousCredentials(),
            client_options=options,
        )

        mock_get_interceptor.assert_called_once_with(options)
        mock_apply_interceptors.assert_called_once_with(
            mock_channel, [mock_otel_interceptor]
        )
        assert transport.grpc_channel == mock_channel


def test_echo_grpc_transport_custom_channel_interceptors():
    mock_interceptor = mock.Mock()
    mock_custom_channel = mock.Mock(spec=grpc.Channel)

    with mock.patch.object(
        grpc_helpers,
        "apply_channel_interceptors",
        return_value=mock_custom_channel,
        create=True,
    ) as mock_apply_interceptors:
        transport = transports.EchoGrpcTransport(
            channel=mock_custom_channel,
            interceptors=[mock_interceptor],
        )

        mock_apply_interceptors.assert_called_once_with(
            mock_custom_channel, [mock_interceptor]
        )
        assert transport.grpc_channel == mock_custom_channel


def test_echo_grpc_asyncio_transport_channel_interceptors():
    mock_interceptor = mock.Mock()
    mock_channel = mock.Mock()
    mock_channel._unary_unary_interceptors = []

    with mock.patch.object(
        transports.EchoGrpcAsyncIOTransport,
        "create_channel",
        return_value=mock_channel,
    ) as mock_create_channel:
        transport = transports.EchoGrpcAsyncIOTransport(
            credentials=ga_credentials.AnonymousCredentials(),
            interceptors=[mock_interceptor],
        )

        assert mock_create_channel.call_count == 1
        assert mock_interceptor in transport.grpc_channel._unary_unary_interceptors
        assert transport.grpc_channel == mock_channel


@pytest.mark.skipif(
    _observability is None or not hasattr(_observability, "apply_otel_async_channel_interceptors"),
    reason="Requires google-api-core with OpenTelemetry async channel interceptors support (>= v2.43.0)",
)
def test_echo_grpc_asyncio_transport_otel_channel_interceptor():
    mock_channel = mock.Mock()
    mock_channel._unary_unary_interceptors = []

    with (
        mock.patch.object(
            _observability,
            "apply_otel_async_channel_interceptors",
            return_value=mock_channel,
        ) as mock_apply_async_interceptors,
        mock.patch.object(
            transports.EchoGrpcAsyncIOTransport,
            "create_channel",
            return_value=mock_channel,
        ) as mock_create_channel,
    ):
        options = client_options.ClientOptions()
        transport = transports.EchoGrpcAsyncIOTransport(
            credentials=ga_credentials.AnonymousCredentials(),
            client_options=options,
        )

        mock_apply_async_interceptors.assert_called_once_with(mock_channel, options)
        assert mock_create_channel.call_count == 1
        assert transport.grpc_channel == mock_channel


def test_echo_grpc_asyncio_transport_custom_channel():
    mock_custom_channel = mock.Mock(spec=aio.Channel)

    with mock.patch.object(
        transports.EchoGrpcAsyncIOTransport,
        "create_channel",
    ) as mock_create_channel:
        transport = transports.EchoGrpcAsyncIOTransport(
            channel=mock_custom_channel,
        )

        assert mock_create_channel.call_count == 0
        assert transport.grpc_channel == mock_custom_channel


@pytest.mark.parametrize("client_class,transport_class,transport_name,grpc_helpers", [
    (EchoClient, transports.EchoGrpcTransport, "grpc", grpc_helpers),
    (EchoAsyncClient, transports.EchoGrpcAsyncIOTransport, "grpc_asyncio", grpc_helpers_async),
])
def test_echo_client_create_channel_credentials_file(client_class, transport_class, transport_name, grpc_helpers):
    # Check the case credentials file is provided.
    options = client_options.ClientOptions(
        credentials_file="credentials.json"
    )

    with mock.patch.object(transport_class, '__init__') as patched:
        patched.return_value = None
        client = client_class(client_options=options, transport=transport_name)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file="credentials.json",
            host=client._DEFAULT_ENDPOINT_TEMPLATE.format(UNIVERSE_DOMAIN=client._DEFAULT_UNIVERSE),
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
            api_audience=None,
        )

    # test that the credentials from file are saved and used as the credentials.
    with mock.patch.object(
        google.auth, "load_credentials_from_file", autospec=True
    ) as load_creds, mock.patch.object(
        google.auth, "default", autospec=True
    ) as adc, mock.patch.object(
        grpc_helpers, "create_channel"
    ) as create_channel:
        creds = ga_credentials.AnonymousCredentials()
        file_creds = ga_credentials.AnonymousCredentials()
        load_creds.return_value = (file_creds, None)
        adc.return_value = (creds, None)
        client = client_class(client_options=options, transport=transport_name)
        create_channel.assert_called_with(
            "localhost:7469",
            credentials=file_creds,
            credentials_file=None,
            quota_project_id=None,
            default_scopes=(
),
            scopes=None,
            default_host="localhost:7469",
            ssl_credentials=None,
            options=[
                ("grpc.max_send_message_length", -1),
                ("grpc.max_receive_message_length", -1),
            ],
        )


@pytest.mark.parametrize("request_type", [
  # Pure protobuf messages (non-proto-plus) require keyword arguments.
  gs_echo.EchoRequest(**{
    "request_id": "explicit value for autopopulate-able field",
    "other_request_id": "explicit value for autopopulate-able field",
  }),
  {
    "request_id": "explicit value for autopopulate-able field",
    "other_request_id": "explicit value for autopopulate-able field",
  },
])
def test_echo(request_type, transport: str = 'grpc'):
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.echo),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = gs_echo.EchoResponse(
            content='content_value',
            severity=gs_echo.Severity.NECESSARY,
            request_id='request_id_value',
            other_request_id='other_request_id_value',
        )
        response = client.echo(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = gs_echo.EchoRequest()
        request.request_id = "explicit value for autopopulate-able field"
        request.other_request_id = "explicit value for autopopulate-able field"
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, gs_echo.EchoResponse)
    assert response.content == 'content_value'
    assert response.severity == gs_echo.Severity.NECESSARY
    assert response.request_id == 'request_id_value'
    assert response.other_request_id == 'other_request_id_value'


def test_echo_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='grpc',
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = gs_echo.EchoRequest(
        content='content_value',
        header='header_value',
        other_header='other_header_value',
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.echo),
            '__call__') as call:
        call.return_value.name = "foo" # operation_request.operation in compute client(s) expect a string.
        client.echo(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gs_echo.EchoRequest(
            content='content_value',
            header='header_value',
            other_header='other_header_value',
        )
        # Ensure that the uuid4 field is set according to AIP 4235
        assert _UUID4_RE.fullmatch(args[0].request_id)
        request_msg.request_id = args[0].request_id
        # Ensure that the uuid4 field is set according to AIP 4235
        assert _UUID4_RE.fullmatch(args[0].other_request_id)
        request_msg.other_request_id = args[0].other_request_id
        assert args[0] == request_msg

def test_echo_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = EchoClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.echo in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = "foo" # operation_request.operation in compute client(s) expect a string.
        client._transport._wrapped_methods[client._transport.echo] = mock_rpc
        request = {}
        client.echo(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.echo(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2

@pytest.mark.asyncio
async def test_echo_async_use_cached_wrapped_rpc(transport: str = "grpc_asyncio"):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = EchoAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._client._transport.echo in client._client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[client._client._transport.echo] = mock_rpc

        request = {}
        await client.echo(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.echo(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2

@pytest.mark.asyncio
@pytest.mark.parametrize("request_type", [
  # Pure protobuf messages (non-proto-plus) require keyword arguments.
  gs_echo.EchoRequest(**{    "request_id": "explicit value for autopopulate-able field",    "other_request_id": "explicit value for autopopulate-able field",  }),
  {    "request_id": "explicit value for autopopulate-able field",    "other_request_id": "explicit value for autopopulate-able field",  },
])
async def test_echo_async(request_type, transport: str = 'grpc_asyncio'):
    client = EchoAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.echo),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value =grpc_helpers_async.FakeUnaryUnaryCall(gs_echo.EchoResponse(
            content='content_value',
            severity=gs_echo.Severity.NECESSARY,
            request_id='request_id_value',
            other_request_id='other_request_id_value',
        ))
        response = await client.echo(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = gs_echo.EchoRequest()
        request.request_id = "explicit value for autopopulate-able field"
        request.other_request_id = "explicit value for autopopulate-able field"
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, gs_echo.EchoResponse)
    assert response.content == 'content_value'
    assert response.severity == gs_echo.Severity.NECESSARY
    assert response.request_id == 'request_id_value'
    assert response.other_request_id == 'other_request_id_value'


@pytest.mark.parametrize("request_type", [
  gs_echo.EchoErrorDetailsRequest(),
  {},
])
def test_echo_error_details(request_type, transport: str = 'grpc'):
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.echo_error_details),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = gs_echo.EchoErrorDetailsResponse(
        )
        response = client.echo_error_details(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = gs_echo.EchoErrorDetailsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, gs_echo.EchoErrorDetailsResponse)


def test_echo_error_details_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='grpc',
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = gs_echo.EchoErrorDetailsRequest(
        single_detail_text='single_detail_text_value',
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.echo_error_details),
            '__call__') as call:
        call.return_value.name = "foo" # operation_request.operation in compute client(s) expect a string.
        client.echo_error_details(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gs_echo.EchoErrorDetailsRequest(
            single_detail_text='single_detail_text_value',
        )
        assert args[0] == request_msg

def test_echo_error_details_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = EchoClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.echo_error_details in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = "foo" # operation_request.operation in compute client(s) expect a string.
        client._transport._wrapped_methods[client._transport.echo_error_details] = mock_rpc
        request = {}
        client.echo_error_details(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.echo_error_details(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2

@pytest.mark.asyncio
async def test_echo_error_details_async_use_cached_wrapped_rpc(transport: str = "grpc_asyncio"):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = EchoAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._client._transport.echo_error_details in client._client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[client._client._transport.echo_error_details] = mock_rpc

        request = {}
        await client.echo_error_details(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.echo_error_details(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2

@pytest.mark.asyncio
@pytest.mark.parametrize("request_type", [
  gs_echo.EchoErrorDetailsRequest(),
  {},
])
async def test_echo_error_details_async(request_type, transport: str = 'grpc_asyncio'):
    client = EchoAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.echo_error_details),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value =grpc_helpers_async.FakeUnaryUnaryCall(gs_echo.EchoErrorDetailsResponse(
        ))
        response = await client.echo_error_details(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = gs_echo.EchoErrorDetailsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, gs_echo.EchoErrorDetailsResponse)


@pytest.mark.parametrize("request_type", [
  gs_echo.FailEchoWithDetailsRequest(),
  {},
])
def test_fail_echo_with_details(request_type, transport: str = 'grpc'):
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.fail_echo_with_details),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = gs_echo.FailEchoWithDetailsResponse(
        )
        response = client.fail_echo_with_details(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = gs_echo.FailEchoWithDetailsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, gs_echo.FailEchoWithDetailsResponse)


def test_fail_echo_with_details_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='grpc',
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = gs_echo.FailEchoWithDetailsRequest(
        message='message_value',
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.fail_echo_with_details),
            '__call__') as call:
        call.return_value.name = "foo" # operation_request.operation in compute client(s) expect a string.
        client.fail_echo_with_details(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gs_echo.FailEchoWithDetailsRequest(
            message='message_value',
        )
        assert args[0] == request_msg

def test_fail_echo_with_details_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = EchoClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.fail_echo_with_details in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = "foo" # operation_request.operation in compute client(s) expect a string.
        client._transport._wrapped_methods[client._transport.fail_echo_with_details] = mock_rpc
        request = {}
        client.fail_echo_with_details(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.fail_echo_with_details(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2

@pytest.mark.asyncio
async def test_fail_echo_with_details_async_use_cached_wrapped_rpc(transport: str = "grpc_asyncio"):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = EchoAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._client._transport.fail_echo_with_details in client._client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[client._client._transport.fail_echo_with_details] = mock_rpc

        request = {}
        await client.fail_echo_with_details(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.fail_echo_with_details(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2

@pytest.mark.asyncio
@pytest.mark.parametrize("request_type", [
  gs_echo.FailEchoWithDetailsRequest(),
  {},
])
async def test_fail_echo_with_details_async(request_type, transport: str = 'grpc_asyncio'):
    client = EchoAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.fail_echo_with_details),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value =grpc_helpers_async.FakeUnaryUnaryCall(gs_echo.FailEchoWithDetailsResponse(
        ))
        response = await client.fail_echo_with_details(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = gs_echo.FailEchoWithDetailsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, gs_echo.FailEchoWithDetailsResponse)


@pytest.mark.parametrize("request_type", [
  gs_echo.ExpandRequest(),
  {},
])
def test_expand(request_type, transport: str = 'grpc'):
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.expand),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = iter([gs_echo.EchoResponse()])
        response = client.expand(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = gs_echo.ExpandRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    for message in response:
        assert isinstance(message, gs_echo.EchoResponse)


def test_expand_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='grpc',
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = gs_echo.ExpandRequest(
        content='content_value',
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.expand),
            '__call__') as call:
        call.return_value.name = "foo" # operation_request.operation in compute client(s) expect a string.
        client.expand(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gs_echo.ExpandRequest(
            content='content_value',
        )
        assert args[0] == request_msg

def test_expand_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = EchoClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.expand in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = "foo" # operation_request.operation in compute client(s) expect a string.
        client._transport._wrapped_methods[client._transport.expand] = mock_rpc
        request = {}
        client.expand(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.expand(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2

@pytest.mark.asyncio
async def test_expand_async_use_cached_wrapped_rpc(transport: str = "grpc_asyncio"):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = EchoAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._client._transport.expand in client._client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[client._client._transport.expand] = mock_rpc

        request = {}
        await client.expand(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.expand(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2

@pytest.mark.asyncio
@pytest.mark.parametrize("request_type", [
  gs_echo.ExpandRequest(),
  {},
])
async def test_expand_async(request_type, transport: str = 'grpc_asyncio'):
    client = EchoAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.expand),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = mock.Mock(aio.UnaryStreamCall, autospec=True)
        call.return_value.read = mock.AsyncMock(side_effect=[gs_echo.EchoResponse()])
        response = await client.expand(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = gs_echo.ExpandRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    message = await response.read()
    assert isinstance(message, gs_echo.EchoResponse)


def test_expand_flattened():
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.expand),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = iter([gs_echo.EchoResponse()])
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.expand(
            content='content_value',
            error=status_pb2.Status(code=411),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].content
        mock_val = 'content_value'
        assert arg == mock_val
        arg = args[0].error
        mock_val = status_pb2.Status(code=411)
        assert arg == mock_val


def test_expand_flattened_error():
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.expand(
            gs_echo.ExpandRequest(),
            content='content_value',
            error=status_pb2.Status(code=411),
        )

@pytest.mark.asyncio
async def test_expand_flattened_async():
    client = EchoAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.expand),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = iter([gs_echo.EchoResponse()])

        call.return_value = mock.Mock(aio.UnaryStreamCall, autospec=True)
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.expand(
            content='content_value',
            error=status_pb2.Status(code=411),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].content
        mock_val = 'content_value'
        assert arg == mock_val
        arg = args[0].error
        mock_val = status_pb2.Status(code=411)
        assert arg == mock_val

@pytest.mark.asyncio
async def test_expand_flattened_error_async():
    client = EchoAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.expand(
            gs_echo.ExpandRequest(),
            content='content_value',
            error=status_pb2.Status(code=411),
        )


@pytest.mark.parametrize("request_type", [
  gs_echo.EchoRequest(),
  {},
])
def test_collect(request_type, transport: str = 'grpc'):
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type
    requests = [request]

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.collect),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = gs_echo.EchoResponse(
            content='content_value',
            severity=gs_echo.Severity.NECESSARY,
            request_id='request_id_value',
            other_request_id='other_request_id_value',
        )
        response = client.collect(iter(requests))

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert next(args[0]) == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, gs_echo.EchoResponse)
    assert response.content == 'content_value'
    assert response.severity == gs_echo.Severity.NECESSARY
    assert response.request_id == 'request_id_value'
    assert response.other_request_id == 'other_request_id_value'

def test_collect_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = EchoClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.collect in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = "foo" # operation_request.operation in compute client(s) expect a string.
        client._transport._wrapped_methods[client._transport.collect] = mock_rpc
        request = [{}]
        client.collect(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.collect(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2

@pytest.mark.asyncio
async def test_collect_async_use_cached_wrapped_rpc(transport: str = "grpc_asyncio"):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = EchoAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._client._transport.collect in client._client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[client._client._transport.collect] = mock_rpc

        request = [{}]
        await client.collect(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.collect(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2

@pytest.mark.asyncio
@pytest.mark.parametrize("request_type", [
  gs_echo.EchoRequest(),
  {},
])
async def test_collect_async(request_type, transport: str = 'grpc_asyncio'):
    client = EchoAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type
    requests = [request]

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.collect),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value =grpc_helpers_async.FakeStreamUnaryCall(gs_echo.EchoResponse(
            content='content_value',
            severity=gs_echo.Severity.NECESSARY,
            request_id='request_id_value',
            other_request_id='other_request_id_value',
        ))
        response = await (await client.collect(iter(requests)))

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert next(args[0]) == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, gs_echo.EchoResponse)
    assert response.content == 'content_value'
    assert response.severity == gs_echo.Severity.NECESSARY
    assert response.request_id == 'request_id_value'
    assert response.other_request_id == 'other_request_id_value'


@pytest.mark.parametrize("request_type", [
  gs_echo.EchoRequest(),
  {},
])
def test_chat(request_type, transport: str = 'grpc'):
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type
    requests = [request]

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.chat),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = iter([gs_echo.EchoResponse()])
        response = client.chat(iter(requests))

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert next(args[0]) == request

    # Establish that the response is the type that we expect.
    for message in response:
        assert isinstance(message, gs_echo.EchoResponse)

def test_chat_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = EchoClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.chat in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = "foo" # operation_request.operation in compute client(s) expect a string.
        client._transport._wrapped_methods[client._transport.chat] = mock_rpc
        request = [{}]
        client.chat(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.chat(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2

@pytest.mark.asyncio
async def test_chat_async_use_cached_wrapped_rpc(transport: str = "grpc_asyncio"):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = EchoAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._client._transport.chat in client._client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[client._client._transport.chat] = mock_rpc

        request = [{}]
        await client.chat(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.chat(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2

@pytest.mark.asyncio
@pytest.mark.parametrize("request_type", [
  gs_echo.EchoRequest(),
  {},
])
async def test_chat_async(request_type, transport: str = 'grpc_asyncio'):
    client = EchoAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type
    requests = [request]

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.chat),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = mock.Mock(aio.StreamStreamCall, autospec=True)
        call.return_value.read = mock.AsyncMock(side_effect=[gs_echo.EchoResponse()])
        response = await client.chat(iter(requests))

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert next(args[0]) == request

    # Establish that the response is the type that we expect.
    message = await response.read()
    assert isinstance(message, gs_echo.EchoResponse)


@pytest.mark.parametrize("request_type", [
  gs_echo.PagedExpandRequest(),
  {},
])
def test_paged_expand(request_type, transport: str = 'grpc'):
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.paged_expand),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = gs_echo.PagedExpandResponse(
            next_page_token='next_page_token_value',
        )
        response = client.paged_expand(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = gs_echo.PagedExpandRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.PagedExpandPager)
    assert response.next_page_token == 'next_page_token_value'


def test_paged_expand_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='grpc',
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = gs_echo.PagedExpandRequest(
        content='content_value',
        page_token='page_token_value',
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.paged_expand),
            '__call__') as call:
        call.return_value.name = "foo" # operation_request.operation in compute client(s) expect a string.
        client.paged_expand(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gs_echo.PagedExpandRequest(
            content='content_value',
            page_token='page_token_value',
        )
        assert args[0] == request_msg

def test_paged_expand_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = EchoClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.paged_expand in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = "foo" # operation_request.operation in compute client(s) expect a string.
        client._transport._wrapped_methods[client._transport.paged_expand] = mock_rpc
        request = {}
        client.paged_expand(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.paged_expand(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2

@pytest.mark.asyncio
async def test_paged_expand_async_use_cached_wrapped_rpc(transport: str = "grpc_asyncio"):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = EchoAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._client._transport.paged_expand in client._client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[client._client._transport.paged_expand] = mock_rpc

        request = {}
        await client.paged_expand(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.paged_expand(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2

@pytest.mark.asyncio
@pytest.mark.parametrize("request_type", [
  gs_echo.PagedExpandRequest(),
  {},
])
async def test_paged_expand_async(request_type, transport: str = 'grpc_asyncio'):
    client = EchoAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.paged_expand),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value =grpc_helpers_async.FakeUnaryUnaryCall(gs_echo.PagedExpandResponse(
            next_page_token='next_page_token_value',
        ))
        response = await client.paged_expand(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = gs_echo.PagedExpandRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.PagedExpandAsyncPager)
    assert response.next_page_token == 'next_page_token_value'


def test_paged_expand_pager(transport_name: str = "grpc"):
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.paged_expand),
            '__call__') as call:
        # Set the response to a series of pages.
        call.side_effect = (
            gs_echo.PagedExpandResponse(
                responses=[
                    gs_echo.EchoResponse(),
                    gs_echo.EchoResponse(),
                    gs_echo.EchoResponse(),
                ],
                next_page_token='abc',
            ),
            gs_echo.PagedExpandResponse(
                responses=[],
                next_page_token='def',
            ),
            gs_echo.PagedExpandResponse(
                responses=[
                    gs_echo.EchoResponse(),
                ],
                next_page_token='ghi',
            ),
            gs_echo.PagedExpandResponse(
                responses=[
                    gs_echo.EchoResponse(),
                    gs_echo.EchoResponse(),
                ],
            ),
            RuntimeError,
        )

        expected_metadata = ()
        retry = retries.Retry()
        timeout = 5
        if HAS_GOOGLE_API_CORE_VERSION_HEADER:
            expected_metadata = tuple(expected_metadata) + (
                version_header.to_api_version_header("v1_20240408"),
            )
        pager = client.paged_expand(request={}, retry=retry, timeout=timeout)

        assert pager._metadata == expected_metadata
        assert pager._retry == retry
        assert pager._timeout == timeout

        assert pager.next_page_token == 'abc'
        assert str(pager).startswith(f'{pager.__class__.__name__}<')

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, gs_echo.EchoResponse)
                   for i in results)
def test_paged_expand_pages(transport_name: str = "grpc"):
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.paged_expand),
            '__call__') as call:
        # Set the response to a series of pages.
        call.side_effect = (
            gs_echo.PagedExpandResponse(
                responses=[
                    gs_echo.EchoResponse(),
                    gs_echo.EchoResponse(),
                    gs_echo.EchoResponse(),
                ],
                next_page_token='abc',
            ),
            gs_echo.PagedExpandResponse(
                responses=[],
                next_page_token='def',
            ),
            gs_echo.PagedExpandResponse(
                responses=[
                    gs_echo.EchoResponse(),
                ],
                next_page_token='ghi',
            ),
            gs_echo.PagedExpandResponse(
                responses=[
                    gs_echo.EchoResponse(),
                    gs_echo.EchoResponse(),
                ],
            ),
            RuntimeError,
        )
        pages = list(client.paged_expand(request={}).pages)
        for page_, token in zip(pages, ['abc','def','ghi', '']):
            assert page_.raw_page.next_page_token == token

@pytest.mark.asyncio
async def test_paged_expand_async_pager():
    client = EchoAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.paged_expand),
            '__call__', new_callable=mock.AsyncMock) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            gs_echo.PagedExpandResponse(
                responses=[
                    gs_echo.EchoResponse(),
                    gs_echo.EchoResponse(),
                    gs_echo.EchoResponse(),
                ],
                next_page_token='abc',
            ),
            gs_echo.PagedExpandResponse(
                responses=[],
                next_page_token='def',
            ),
            gs_echo.PagedExpandResponse(
                responses=[
                    gs_echo.EchoResponse(),
                ],
                next_page_token='ghi',
            ),
            gs_echo.PagedExpandResponse(
                responses=[
                    gs_echo.EchoResponse(),
                    gs_echo.EchoResponse(),
                ],
            ),
            RuntimeError,
        )
        async_pager = await client.paged_expand(request={},)
        assert async_pager.next_page_token == 'abc'
        assert str(async_pager).startswith(f'{async_pager.__class__.__name__}<')

        responses = []
        async for response in async_pager: # pragma: no branch
            responses.append(response)

        assert len(responses) == 6
        assert all(isinstance(i, gs_echo.EchoResponse)
                for i in responses)


@pytest.mark.asyncio
async def test_paged_expand_async_pages():
    client = EchoAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.paged_expand),
            '__call__', new_callable=mock.AsyncMock) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            gs_echo.PagedExpandResponse(
                responses=[
                    gs_echo.EchoResponse(),
                    gs_echo.EchoResponse(),
                    gs_echo.EchoResponse(),
                ],
                next_page_token='abc',
            ),
            gs_echo.PagedExpandResponse(
                responses=[],
                next_page_token='def',
            ),
            gs_echo.PagedExpandResponse(
                responses=[
                    gs_echo.EchoResponse(),
                ],
                next_page_token='ghi',
            ),
            gs_echo.PagedExpandResponse(
                responses=[
                    gs_echo.EchoResponse(),
                    gs_echo.EchoResponse(),
                ],
            ),
            RuntimeError,
        )
        pages = []
        async for page_ in (
            await client.paged_expand(request={})
        ).pages:
            pages.append(page_)
        for page_, token in zip(pages, ['abc','def','ghi', '']):
            assert page_.raw_page.next_page_token == token

@pytest.mark.parametrize("request_type", [
  gs_echo.PagedExpandLegacyRequest(),
  {},
])
def test_paged_expand_legacy(request_type, transport: str = 'grpc'):
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.paged_expand_legacy),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = gs_echo.PagedExpandResponse(
            next_page_token='next_page_token_value',
        )
        response = client.paged_expand_legacy(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = gs_echo.PagedExpandLegacyRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.PagedExpandLegacyPager)
    assert response.next_page_token == 'next_page_token_value'


def test_paged_expand_legacy_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='grpc',
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = gs_echo.PagedExpandLegacyRequest(
        content='content_value',
        page_token='page_token_value',
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.paged_expand_legacy),
            '__call__') as call:
        call.return_value.name = "foo" # operation_request.operation in compute client(s) expect a string.
        client.paged_expand_legacy(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gs_echo.PagedExpandLegacyRequest(
            content='content_value',
            page_token='page_token_value',
        )
        assert args[0] == request_msg

def test_paged_expand_legacy_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = EchoClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.paged_expand_legacy in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = "foo" # operation_request.operation in compute client(s) expect a string.
        client._transport._wrapped_methods[client._transport.paged_expand_legacy] = mock_rpc
        request = {}
        client.paged_expand_legacy(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.paged_expand_legacy(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2

@pytest.mark.asyncio
async def test_paged_expand_legacy_async_use_cached_wrapped_rpc(transport: str = "grpc_asyncio"):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = EchoAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._client._transport.paged_expand_legacy in client._client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[client._client._transport.paged_expand_legacy] = mock_rpc

        request = {}
        await client.paged_expand_legacy(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.paged_expand_legacy(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2

@pytest.mark.asyncio
@pytest.mark.parametrize("request_type", [
  gs_echo.PagedExpandLegacyRequest(),
  {},
])
async def test_paged_expand_legacy_async(request_type, transport: str = 'grpc_asyncio'):
    client = EchoAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.paged_expand_legacy),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value =grpc_helpers_async.FakeUnaryUnaryCall(gs_echo.PagedExpandResponse(
            next_page_token='next_page_token_value',
        ))
        response = await client.paged_expand_legacy(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = gs_echo.PagedExpandLegacyRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.PagedExpandLegacyAsyncPager)
    assert response.next_page_token == 'next_page_token_value'


def test_paged_expand_legacy_pager(transport_name: str = "grpc"):
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.paged_expand_legacy),
            '__call__') as call:
        # Set the response to a series of pages.
        call.side_effect = (
            gs_echo.PagedExpandResponse(
                responses=[
                    gs_echo.EchoResponse(),
                    gs_echo.EchoResponse(),
                    gs_echo.EchoResponse(),
                ],
                next_page_token='abc',
            ),
            gs_echo.PagedExpandResponse(
                responses=[],
                next_page_token='def',
            ),
            gs_echo.PagedExpandResponse(
                responses=[
                    gs_echo.EchoResponse(),
                ],
                next_page_token='ghi',
            ),
            gs_echo.PagedExpandResponse(
                responses=[
                    gs_echo.EchoResponse(),
                    gs_echo.EchoResponse(),
                ],
            ),
            RuntimeError,
        )

        expected_metadata = ()
        retry = retries.Retry()
        timeout = 5
        if HAS_GOOGLE_API_CORE_VERSION_HEADER:
            expected_metadata = tuple(expected_metadata) + (
                version_header.to_api_version_header("v1_20240408"),
            )
        pager = client.paged_expand_legacy(request={}, retry=retry, timeout=timeout)

        assert pager._metadata == expected_metadata
        assert pager._retry == retry
        assert pager._timeout == timeout

        assert pager.next_page_token == 'abc'
        assert str(pager).startswith(f'{pager.__class__.__name__}<')

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, gs_echo.EchoResponse)
                   for i in results)
def test_paged_expand_legacy_pages(transport_name: str = "grpc"):
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.paged_expand_legacy),
            '__call__') as call:
        # Set the response to a series of pages.
        call.side_effect = (
            gs_echo.PagedExpandResponse(
                responses=[
                    gs_echo.EchoResponse(),
                    gs_echo.EchoResponse(),
                    gs_echo.EchoResponse(),
                ],
                next_page_token='abc',
            ),
            gs_echo.PagedExpandResponse(
                responses=[],
                next_page_token='def',
            ),
            gs_echo.PagedExpandResponse(
                responses=[
                    gs_echo.EchoResponse(),
                ],
                next_page_token='ghi',
            ),
            gs_echo.PagedExpandResponse(
                responses=[
                    gs_echo.EchoResponse(),
                    gs_echo.EchoResponse(),
                ],
            ),
            RuntimeError,
        )
        pages = list(client.paged_expand_legacy(request={}).pages)
        for page_, token in zip(pages, ['abc','def','ghi', '']):
            assert page_.raw_page.next_page_token == token

@pytest.mark.asyncio
async def test_paged_expand_legacy_async_pager():
    client = EchoAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.paged_expand_legacy),
            '__call__', new_callable=mock.AsyncMock) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            gs_echo.PagedExpandResponse(
                responses=[
                    gs_echo.EchoResponse(),
                    gs_echo.EchoResponse(),
                    gs_echo.EchoResponse(),
                ],
                next_page_token='abc',
            ),
            gs_echo.PagedExpandResponse(
                responses=[],
                next_page_token='def',
            ),
            gs_echo.PagedExpandResponse(
                responses=[
                    gs_echo.EchoResponse(),
                ],
                next_page_token='ghi',
            ),
            gs_echo.PagedExpandResponse(
                responses=[
                    gs_echo.EchoResponse(),
                    gs_echo.EchoResponse(),
                ],
            ),
            RuntimeError,
        )
        async_pager = await client.paged_expand_legacy(request={},)
        assert async_pager.next_page_token == 'abc'
        assert str(async_pager).startswith(f'{async_pager.__class__.__name__}<')

        responses = []
        async for response in async_pager: # pragma: no branch
            responses.append(response)

        assert len(responses) == 6
        assert all(isinstance(i, gs_echo.EchoResponse)
                for i in responses)


@pytest.mark.asyncio
async def test_paged_expand_legacy_async_pages():
    client = EchoAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.paged_expand_legacy),
            '__call__', new_callable=mock.AsyncMock) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            gs_echo.PagedExpandResponse(
                responses=[
                    gs_echo.EchoResponse(),
                    gs_echo.EchoResponse(),
                    gs_echo.EchoResponse(),
                ],
                next_page_token='abc',
            ),
            gs_echo.PagedExpandResponse(
                responses=[],
                next_page_token='def',
            ),
            gs_echo.PagedExpandResponse(
                responses=[
                    gs_echo.EchoResponse(),
                ],
                next_page_token='ghi',
            ),
            gs_echo.PagedExpandResponse(
                responses=[
                    gs_echo.EchoResponse(),
                    gs_echo.EchoResponse(),
                ],
            ),
            RuntimeError,
        )
        pages = []
        async for page_ in (
            await client.paged_expand_legacy(request={})
        ).pages:
            pages.append(page_)
        for page_, token in zip(pages, ['abc','def','ghi', '']):
            assert page_.raw_page.next_page_token == token

@pytest.mark.parametrize("request_type", [
  gs_echo.PagedExpandRequest(),
  {},
])
def test_paged_expand_legacy_mapped(request_type, transport: str = 'grpc'):
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.paged_expand_legacy_mapped),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = gs_echo.PagedExpandLegacyMappedResponse(
            next_page_token='next_page_token_value',
        )
        response = client.paged_expand_legacy_mapped(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = gs_echo.PagedExpandRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.PagedExpandLegacyMappedPager)
    assert response.next_page_token == 'next_page_token_value'


def test_paged_expand_legacy_mapped_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='grpc',
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = gs_echo.PagedExpandRequest(
        content='content_value',
        page_token='page_token_value',
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.paged_expand_legacy_mapped),
            '__call__') as call:
        call.return_value.name = "foo" # operation_request.operation in compute client(s) expect a string.
        client.paged_expand_legacy_mapped(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gs_echo.PagedExpandRequest(
            content='content_value',
            page_token='page_token_value',
        )
        assert args[0] == request_msg

def test_paged_expand_legacy_mapped_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = EchoClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.paged_expand_legacy_mapped in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = "foo" # operation_request.operation in compute client(s) expect a string.
        client._transport._wrapped_methods[client._transport.paged_expand_legacy_mapped] = mock_rpc
        request = {}
        client.paged_expand_legacy_mapped(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.paged_expand_legacy_mapped(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2

@pytest.mark.asyncio
async def test_paged_expand_legacy_mapped_async_use_cached_wrapped_rpc(transport: str = "grpc_asyncio"):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = EchoAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._client._transport.paged_expand_legacy_mapped in client._client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[client._client._transport.paged_expand_legacy_mapped] = mock_rpc

        request = {}
        await client.paged_expand_legacy_mapped(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.paged_expand_legacy_mapped(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2

@pytest.mark.asyncio
@pytest.mark.parametrize("request_type", [
  gs_echo.PagedExpandRequest(),
  {},
])
async def test_paged_expand_legacy_mapped_async(request_type, transport: str = 'grpc_asyncio'):
    client = EchoAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.paged_expand_legacy_mapped),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value =grpc_helpers_async.FakeUnaryUnaryCall(gs_echo.PagedExpandLegacyMappedResponse(
            next_page_token='next_page_token_value',
        ))
        response = await client.paged_expand_legacy_mapped(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = gs_echo.PagedExpandRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.PagedExpandLegacyMappedAsyncPager)
    assert response.next_page_token == 'next_page_token_value'


def test_paged_expand_legacy_mapped_pages(transport_name: str = "grpc"):
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.paged_expand_legacy_mapped),
            '__call__') as call:
        # Set the response to a series of pages.
        call.side_effect = (
            gs_echo.PagedExpandLegacyMappedResponse(
                alphabetized={
                    'a':gs_echo.PagedExpandResponseList(),
                    'b':gs_echo.PagedExpandResponseList(),
                    'c':gs_echo.PagedExpandResponseList(),
                },
                next_page_token='abc',
            ),
            gs_echo.PagedExpandLegacyMappedResponse(
                alphabetized={},
                next_page_token='def',
            ),
            gs_echo.PagedExpandLegacyMappedResponse(
                alphabetized={
                    'g':gs_echo.PagedExpandResponseList(),
                },
                next_page_token='ghi',
            ),
            gs_echo.PagedExpandLegacyMappedResponse(
                alphabetized={
                    'h':gs_echo.PagedExpandResponseList(),
                    'i':gs_echo.PagedExpandResponseList(),
                },
            ),
            RuntimeError,
        )
        pages = list(client.paged_expand_legacy_mapped(request={}).pages)
        for page_, token in zip(pages, ['abc','def','ghi', '']):
            assert page_.raw_page.next_page_token == token

@pytest.mark.asyncio
async def test_paged_expand_legacy_mapped_async_pager():
    client = EchoAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.paged_expand_legacy_mapped),
            '__call__', new_callable=mock.AsyncMock) as call:
        # Set the response to a series of pages.
        call.side_effect = (
              gs_echo.PagedExpandLegacyMappedResponse(
                  alphabetized={
                      'a':gs_echo.PagedExpandResponseList(),
                      'b':gs_echo.PagedExpandResponseList(),
                      'c':gs_echo.PagedExpandResponseList(),
                  },
                  next_page_token='abc',
              ),
              gs_echo.PagedExpandLegacyMappedResponse(
                  alphabetized={},
                  next_page_token='def',
              ),
              gs_echo.PagedExpandLegacyMappedResponse(
                  alphabetized={
                      'g':gs_echo.PagedExpandResponseList(),
                  },
                  next_page_token='ghi',
              ),
              gs_echo.PagedExpandLegacyMappedResponse(
                  alphabetized={
                      'h':gs_echo.PagedExpandResponseList(),
                      'i':gs_echo.PagedExpandResponseList(),
                  },
              ),
            RuntimeError,
        )
        async_pager = await client.paged_expand_legacy_mapped(request={},)
        assert async_pager.next_page_token == 'abc'
        assert str(async_pager).startswith(f'{async_pager.__class__.__name__}<')

        responses = []
        async for response in async_pager: # pragma: no branch
            responses.append(response)

        assert len(responses) == 6

        assert all(
            isinstance(i, tuple)
                for i in responses)
        for result in responses:
            assert isinstance(result, tuple)
            assert tuple(type(t) for t in result) == (str, gs_echo.PagedExpandResponseList)

        assert async_pager.get('a') is None
        assert isinstance(async_pager.get('h'), gs_echo.PagedExpandResponseList)


@pytest.mark.asyncio
async def test_paged_expand_legacy_mapped_async_pages():
    client = EchoAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.paged_expand_legacy_mapped),
            '__call__', new_callable=mock.AsyncMock) as call:
        # Set the response to a series of pages.
        call.side_effect = (
              gs_echo.PagedExpandLegacyMappedResponse(
                  alphabetized={
                      'a':gs_echo.PagedExpandResponseList(),
                      'b':gs_echo.PagedExpandResponseList(),
                      'c':gs_echo.PagedExpandResponseList(),
                  },
                  next_page_token='abc',
              ),
              gs_echo.PagedExpandLegacyMappedResponse(
                  alphabetized={},
                  next_page_token='def',
              ),
              gs_echo.PagedExpandLegacyMappedResponse(
                  alphabetized={
                      'g':gs_echo.PagedExpandResponseList(),
                  },
                  next_page_token='ghi',
              ),
              gs_echo.PagedExpandLegacyMappedResponse(
                  alphabetized={
                      'h':gs_echo.PagedExpandResponseList(),
                      'i':gs_echo.PagedExpandResponseList(),
                  },
              ),
            RuntimeError,
        )
        pages = []
        async for page_ in (
            await client.paged_expand_legacy_mapped(request={})
        ).pages:
            pages.append(page_)
        for page_, token in zip(pages, ['abc','def','ghi', '']):
            assert page_.raw_page.next_page_token == token

@pytest.mark.parametrize("request_type", [
  gs_echo.WaitRequest(),
  {},
])
def test_wait(request_type, transport: str = 'grpc'):
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.wait),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name='operations/spam')
        response = client.wait(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = gs_echo.WaitRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_wait_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='grpc',
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = gs_echo.WaitRequest(
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.wait),
            '__call__') as call:
        call.return_value.name = "foo" # operation_request.operation in compute client(s) expect a string.
        client.wait(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gs_echo.WaitRequest(
        )
        assert args[0] == request_msg

def test_wait_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = EchoClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.wait in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = "foo" # operation_request.operation in compute client(s) expect a string.
        client._transport._wrapped_methods[client._transport.wait] = mock_rpc
        request = {}
        client.wait(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods call wrapper_fn to build a cached
        # client._transport.operations_client instance on first rpc call.
        # Subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.wait(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2

@pytest.mark.asyncio
async def test_wait_async_use_cached_wrapped_rpc(transport: str = "grpc_asyncio"):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = EchoAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._client._transport.wait in client._client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[client._client._transport.wait] = mock_rpc

        request = {}
        await client.wait(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods call wrapper_fn to build a cached
        # client._transport.operations_client instance on first rpc call.
        # Subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        await client.wait(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2

@pytest.mark.asyncio
@pytest.mark.parametrize("request_type", [
  gs_echo.WaitRequest(),
  {},
])
async def test_wait_async(request_type, transport: str = 'grpc_asyncio'):
    client = EchoAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.wait),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name='operations/spam')
        )
        response = await client.wait(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = gs_echo.WaitRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


@pytest.mark.parametrize("request_type", [
  gs_echo.BlockRequest(),
  {},
])
def test_block(request_type, transport: str = 'grpc'):
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.block),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = gs_echo.BlockResponse(
            content='content_value',
        )
        response = client.block(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = gs_echo.BlockRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, gs_echo.BlockResponse)
    assert response.content == 'content_value'


def test_block_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='grpc',
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = gs_echo.BlockRequest(
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.block),
            '__call__') as call:
        call.return_value.name = "foo" # operation_request.operation in compute client(s) expect a string.
        client.block(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gs_echo.BlockRequest(
        )
        assert args[0] == request_msg

def test_block_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = EchoClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.block in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = "foo" # operation_request.operation in compute client(s) expect a string.
        client._transport._wrapped_methods[client._transport.block] = mock_rpc
        request = {}
        client.block(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.block(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2

@pytest.mark.asyncio
async def test_block_async_use_cached_wrapped_rpc(transport: str = "grpc_asyncio"):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = EchoAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._client._transport.block in client._client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[client._client._transport.block] = mock_rpc

        request = {}
        await client.block(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.block(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2

@pytest.mark.asyncio
@pytest.mark.parametrize("request_type", [
  gs_echo.BlockRequest(),
  {},
])
async def test_block_async(request_type, transport: str = 'grpc_asyncio'):
    client = EchoAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.block),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value =grpc_helpers_async.FakeUnaryUnaryCall(gs_echo.BlockResponse(
            content='content_value',
        ))
        response = await client.block(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = gs_echo.BlockRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, gs_echo.BlockResponse)
    assert response.content == 'content_value'


def test_echo_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = EchoClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.echo in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = "foo" # operation_request.operation in compute client(s) expect a string.
        client._transport._wrapped_methods[client._transport.echo] = mock_rpc

        request = {}
        client.echo(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.echo(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_echo_error_details_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = EchoClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.echo_error_details in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = "foo" # operation_request.operation in compute client(s) expect a string.
        client._transport._wrapped_methods[client._transport.echo_error_details] = mock_rpc

        request = {}
        client.echo_error_details(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.echo_error_details(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_fail_echo_with_details_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = EchoClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.fail_echo_with_details in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = "foo" # operation_request.operation in compute client(s) expect a string.
        client._transport._wrapped_methods[client._transport.fail_echo_with_details] = mock_rpc

        request = {}
        client.fail_echo_with_details(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.fail_echo_with_details(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_expand_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = EchoClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.expand in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = "foo" # operation_request.operation in compute client(s) expect a string.
        client._transport._wrapped_methods[client._transport.expand] = mock_rpc

        request = {}
        client.expand(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.expand(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_expand_rest_flattened():
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), 'request') as req:
        # Designate an appropriate value for the returned response.
        return_value = gs_echo.EchoResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {}

        # get truthy value for each flattened field
        mock_args = dict(
            content='content_value',
            error=status_pb2.Status(code=411),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = gs_echo.EchoResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        json_return_value = "[{}]".format(json_return_value)
        response_value._content = json_return_value.encode('UTF-8')
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        with mock.patch.object(response_value, 'iter_content') as iter_content:
            iter_content.return_value = iter(json_return_value)
            client.expand(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate("%s/v1beta1/echo:expand" % client.transport._host, args[1])


def test_expand_rest_flattened_error(transport: str = 'rest'):
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.expand(
            gs_echo.ExpandRequest(),
            content='content_value',
            error=status_pb2.Status(code=411),
        )


def test_collect_rest_unimplemented():
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = gs_echo.EchoRequest()
    requests = [request]
    with pytest.raises(NotImplementedError):
        client.collect(requests)


def test_chat_rest_no_http_options():
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = gs_echo.EchoRequest()
    requests = [request]
    with pytest.raises(RuntimeError):
        client.chat(requests)


def test_paged_expand_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = EchoClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.paged_expand in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = "foo" # operation_request.operation in compute client(s) expect a string.
        client._transport._wrapped_methods[client._transport.paged_expand] = mock_rpc

        request = {}
        client.paged_expand(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.paged_expand(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_paged_expand_rest_required_fields(request_type=gs_echo.PagedExpandRequest):
    transport_class = transports.EchoRestTransport

    request_init = {}
    request_init["content"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(json_format.MessageToJson(
        pb_request,
        use_integers_for_enums=False
    ))

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BasePagedExpand,
        "_BasePagedExpand__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {k: v for k, v in default_values.items() if k not in jsonified_request}
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["content"] = 'content_value'

    # verify required fields with non-default values are left alone
    assert "content" in jsonified_request
    assert jsonified_request["content"] == 'content_value'

    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='rest',
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = gs_echo.PagedExpandResponse()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, 'request') as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, 'transcode') as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                'uri': 'v1/sample_method',
                'method': "post",
                'query_params': pb_request,
            }
            transcode_result['body'] = pb_request
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            # Convert return value to protobuf type
            return_value = gs_echo.PagedExpandResponse.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode('UTF-8')
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.paged_expand(request)

            expected_params = [
                ('$alt', 'json;enum-encoding=int')
            ]
            actual_params = req.call_args.kwargs['params']
            assert sorted(expected_params) == sorted(actual_params)


def test_paged_expand_rest_pager(transport: str = 'rest'):
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, 'request') as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        #with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            gs_echo.PagedExpandResponse(
                responses=[
                    gs_echo.EchoResponse(),
                    gs_echo.EchoResponse(),
                    gs_echo.EchoResponse(),
                ],
                next_page_token='abc',
            ),
            gs_echo.PagedExpandResponse(
                responses=[],
                next_page_token='def',
            ),
            gs_echo.PagedExpandResponse(
                responses=[
                    gs_echo.EchoResponse(),
                ],
                next_page_token='ghi',
            ),
            gs_echo.PagedExpandResponse(
                responses=[
                    gs_echo.EchoResponse(),
                    gs_echo.EchoResponse(),
                ],
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(gs_echo.PagedExpandResponse.to_json(x) for x in response)
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode('UTF-8')
            return_val.status_code = 200
        req.side_effect = return_values

        sample_request = {}

        pager = client.paged_expand(request=sample_request)

        assert pager.next_page_token == 'abc'
        assert str(pager).startswith(f'{pager.__class__.__name__}<')

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, gs_echo.EchoResponse)
                for i in results)

        pages = list(client.paged_expand(request=sample_request).pages)
        for page_, token in zip(pages, ['abc','def','ghi', '']):
            assert page_.raw_page.next_page_token == token


def test_paged_expand_legacy_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = EchoClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.paged_expand_legacy in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = "foo" # operation_request.operation in compute client(s) expect a string.
        client._transport._wrapped_methods[client._transport.paged_expand_legacy] = mock_rpc

        request = {}
        client.paged_expand_legacy(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.paged_expand_legacy(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_paged_expand_legacy_rest_required_fields(request_type=gs_echo.PagedExpandLegacyRequest):
    transport_class = transports.EchoRestTransport

    request_init = {}
    request_init["content"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(json_format.MessageToJson(
        pb_request,
        use_integers_for_enums=False
    ))

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BasePagedExpandLegacy,
        "_BasePagedExpandLegacy__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {k: v for k, v in default_values.items() if k not in jsonified_request}
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["content"] = 'content_value'

    # verify required fields with non-default values are left alone
    assert "content" in jsonified_request
    assert jsonified_request["content"] == 'content_value'

    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='rest',
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = gs_echo.PagedExpandResponse()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, 'request') as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, 'transcode') as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                'uri': 'v1/sample_method',
                'method': "post",
                'query_params': pb_request,
            }
            transcode_result['body'] = pb_request
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            # Convert return value to protobuf type
            return_value = gs_echo.PagedExpandResponse.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode('UTF-8')
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.paged_expand_legacy(request)

            expected_params = [
                ('$alt', 'json;enum-encoding=int')
            ]
            actual_params = req.call_args.kwargs['params']
            assert sorted(expected_params) == sorted(actual_params)


def test_paged_expand_legacy_rest_pager(transport: str = 'rest'):
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, 'request') as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        #with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            gs_echo.PagedExpandResponse(
                responses=[
                    gs_echo.EchoResponse(),
                    gs_echo.EchoResponse(),
                    gs_echo.EchoResponse(),
                ],
                next_page_token='abc',
            ),
            gs_echo.PagedExpandResponse(
                responses=[],
                next_page_token='def',
            ),
            gs_echo.PagedExpandResponse(
                responses=[
                    gs_echo.EchoResponse(),
                ],
                next_page_token='ghi',
            ),
            gs_echo.PagedExpandResponse(
                responses=[
                    gs_echo.EchoResponse(),
                    gs_echo.EchoResponse(),
                ],
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(gs_echo.PagedExpandResponse.to_json(x) for x in response)
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode('UTF-8')
            return_val.status_code = 200
        req.side_effect = return_values

        sample_request = {}

        pager = client.paged_expand_legacy(request=sample_request)

        assert pager.next_page_token == 'abc'
        assert str(pager).startswith(f'{pager.__class__.__name__}<')

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, gs_echo.EchoResponse)
                for i in results)

        pages = list(client.paged_expand_legacy(request=sample_request).pages)
        for page_, token in zip(pages, ['abc','def','ghi', '']):
            assert page_.raw_page.next_page_token == token


def test_paged_expand_legacy_mapped_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = EchoClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.paged_expand_legacy_mapped in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = "foo" # operation_request.operation in compute client(s) expect a string.
        client._transport._wrapped_methods[client._transport.paged_expand_legacy_mapped] = mock_rpc

        request = {}
        client.paged_expand_legacy_mapped(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.paged_expand_legacy_mapped(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_paged_expand_legacy_mapped_rest_required_fields(request_type=gs_echo.PagedExpandRequest):
    transport_class = transports.EchoRestTransport

    request_init = {}
    request_init["content"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(json_format.MessageToJson(
        pb_request,
        use_integers_for_enums=False
    ))

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BasePagedExpandLegacyMapped,
        "_BasePagedExpandLegacyMapped__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {k: v for k, v in default_values.items() if k not in jsonified_request}
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["content"] = 'content_value'

    # verify required fields with non-default values are left alone
    assert "content" in jsonified_request
    assert jsonified_request["content"] == 'content_value'

    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='rest',
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = gs_echo.PagedExpandLegacyMappedResponse()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, 'request') as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, 'transcode') as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                'uri': 'v1/sample_method',
                'method': "post",
                'query_params': pb_request,
            }
            transcode_result['body'] = pb_request
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            # Convert return value to protobuf type
            return_value = gs_echo.PagedExpandLegacyMappedResponse.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode('UTF-8')
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.paged_expand_legacy_mapped(request)

            expected_params = [
                ('$alt', 'json;enum-encoding=int')
            ]
            actual_params = req.call_args.kwargs['params']
            assert sorted(expected_params) == sorted(actual_params)


def test_paged_expand_legacy_mapped_rest_pager(transport: str = 'rest'):
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, 'request') as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        #with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            gs_echo.PagedExpandLegacyMappedResponse(
                alphabetized={
                    'a':gs_echo.PagedExpandResponseList(),
                    'b':gs_echo.PagedExpandResponseList(),
                    'c':gs_echo.PagedExpandResponseList(),
                },
                next_page_token='abc',
            ),
            gs_echo.PagedExpandLegacyMappedResponse(
                alphabetized={},
                next_page_token='def',
            ),
            gs_echo.PagedExpandLegacyMappedResponse(
                alphabetized={
                    'g':gs_echo.PagedExpandResponseList(),
                },
                next_page_token='ghi',
            ),
            gs_echo.PagedExpandLegacyMappedResponse(
                alphabetized={
                    'h':gs_echo.PagedExpandResponseList(),
                    'i':gs_echo.PagedExpandResponseList(),
                },
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(gs_echo.PagedExpandLegacyMappedResponse.to_json(x) for x in response)
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode('UTF-8')
            return_val.status_code = 200
        req.side_effect = return_values

        sample_request = {}

        pager = client.paged_expand_legacy_mapped(request=sample_request)

        assert pager.next_page_token == 'abc'
        assert str(pager).startswith(f'{pager.__class__.__name__}<')

        assert isinstance(pager.get('a'), gs_echo.PagedExpandResponseList)
        assert pager.get('h') is None

        results = list(pager)
        assert len(results) == 6
        assert all(
            isinstance(i, tuple)
                for i in results)
        for result in results:
            assert isinstance(result, tuple)
            assert tuple(type(t) for t in result) == (str, gs_echo.PagedExpandResponseList)

        assert pager.get('a') is None
        assert isinstance(pager.get('h'), gs_echo.PagedExpandResponseList)

        pages = list(client.paged_expand_legacy_mapped(request=sample_request).pages)
        for page_, token in zip(pages, ['abc','def','ghi', '']):
            assert page_.raw_page.next_page_token == token


def test_wait_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = EchoClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.wait in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = "foo" # operation_request.operation in compute client(s) expect a string.
        client._transport._wrapped_methods[client._transport.wait] = mock_rpc

        request = {}
        client.wait(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods build a cached wrapper on first rpc call
        # subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.wait(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_block_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = EchoClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.block in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = "foo" # operation_request.operation in compute client(s) expect a string.
        client._transport._wrapped_methods[client._transport.block] = mock_rpc

        request = {}
        client.block(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.block(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_chat_rest_error():
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='rest'
    )
    # Since a `google.api.http` annotation is required for using a rest transport
    # method, this should error.
    with pytest.raises(NotImplementedError) as not_implemented_error:
        client.chat({})
    assert (
        "Method Chat is not available over REST transport"
        in str(not_implemented_error.value)
    )


def test_credentials_transport_error():
    # It is an error to provide credentials and a transport instance.
    transport = transports.EchoGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = EchoClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport=transport,
        )

    # It is an error to provide a credentials file and a transport instance.
    transport = transports.EchoGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = EchoClient(
            client_options={"credentials_file": "credentials.json"},
            transport=transport,
        )

    # It is an error to provide an api_key and a transport instance.
    transport = transports.EchoGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    options = client_options.ClientOptions()
    options.api_key = "api_key"
    with pytest.raises(ValueError):
        client = EchoClient(
            client_options=options,
            transport=transport,
        )

    # It is an error to provide an api_key and a credential.
    options = client_options.ClientOptions()
    options.api_key = "api_key"
    with pytest.raises(ValueError):
        client = EchoClient(
            client_options=options,
            credentials=ga_credentials.AnonymousCredentials()
        )

    # It is an error to provide scopes and a transport instance.
    transport = transports.EchoGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = EchoClient(
            client_options={"scopes": ["1", "2"]},
            transport=transport,
        )


def test_transport_instance():
    # A client may be instantiated with a custom transport instance.
    transport = transports.EchoGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    client = EchoClient(transport=transport)
    assert client.transport is transport

def test_transport_get_channel():
    # A client may be instantiated with a custom transport instance.
    transport = transports.EchoGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    channel = transport.grpc_channel
    assert channel

    transport = transports.EchoGrpcAsyncIOTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    channel = transport.grpc_channel
    assert channel

@pytest.mark.parametrize("transport_class", [
    transports.EchoGrpcTransport,
    transports.EchoGrpcAsyncIOTransport,
    transports.EchoRestTransport,
])
def test_transport_adc(transport_class):
    # Test default credentials are used if not provided.
    with mock.patch.object(google.auth, 'default') as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport_class()
        adc.assert_called_once()

def test_transport_kind_grpc():
    transport = EchoClient.get_transport_class("grpc")(
        credentials=ga_credentials.AnonymousCredentials()
    )
    assert transport.kind == "grpc"


def test_initialize_client_w_grpc():
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc"
    )
    assert client is not None


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_echo_empty_call_grpc():
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.echo),
            '__call__') as call:
        call.return_value = gs_echo.EchoResponse()
        client.echo(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gs_echo.EchoRequest()
        # Ensure that the uuid4 field is set according to AIP 4235
        assert _UUID4_RE.fullmatch(args[0].request_id)
        request_msg.request_id = args[0].request_id
        # Ensure that the uuid4 field is set according to AIP 4235
        assert _UUID4_RE.fullmatch(args[0].other_request_id)
        request_msg.other_request_id = args[0].other_request_id
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_echo_error_details_empty_call_grpc():
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.echo_error_details),
            '__call__') as call:
        call.return_value = gs_echo.EchoErrorDetailsResponse()
        client.echo_error_details(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gs_echo.EchoErrorDetailsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_fail_echo_with_details_empty_call_grpc():
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.fail_echo_with_details),
            '__call__') as call:
        call.return_value = gs_echo.FailEchoWithDetailsResponse()
        client.fail_echo_with_details(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gs_echo.FailEchoWithDetailsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_expand_empty_call_grpc():
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.expand),
            '__call__') as call:
        call.return_value = iter([gs_echo.EchoResponse()])
        client.expand(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gs_echo.ExpandRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_paged_expand_empty_call_grpc():
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.paged_expand),
            '__call__') as call:
        call.return_value = gs_echo.PagedExpandResponse()
        client.paged_expand(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gs_echo.PagedExpandRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_paged_expand_legacy_empty_call_grpc():
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.paged_expand_legacy),
            '__call__') as call:
        call.return_value = gs_echo.PagedExpandResponse()
        client.paged_expand_legacy(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gs_echo.PagedExpandLegacyRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_paged_expand_legacy_mapped_empty_call_grpc():
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.paged_expand_legacy_mapped),
            '__call__') as call:
        call.return_value = gs_echo.PagedExpandLegacyMappedResponse()
        client.paged_expand_legacy_mapped(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gs_echo.PagedExpandRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_wait_empty_call_grpc():
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.wait),
            '__call__') as call:
        call.return_value = operations_pb2.Operation(name='operations/op')
        client.wait(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gs_echo.WaitRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_block_empty_call_grpc():
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.block),
            '__call__') as call:
        call.return_value = gs_echo.BlockResponse()
        client.block(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gs_echo.BlockRequest()
        assert args[0] == request_msg


def test_echo_routing_parameters_request_1_grpc():
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.echo),
            '__call__') as call:
        call.return_value = gs_echo.EchoResponse()
        client.echo(request={"header": "sample1"})

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = gs_echo.EchoRequest(**{"header": "sample1"})
        # Ensure that the uuid4 field is set according to AIP 4235
        assert _UUID4_RE.fullmatch(args[0].request_id)
        request_msg.request_id = args[0].request_id
        # Ensure that the uuid4 field is set according to AIP 4235
        assert _UUID4_RE.fullmatch(args[0].other_request_id)
        request_msg.other_request_id = args[0].other_request_id
        assert args[0] == request_msg

        expected_headers = {'header': 'sample1', 'routing_id': 'sample1'}
        assert gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw['metadata']

def test_echo_routing_parameters_request_2_grpc():
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.echo),
            '__call__') as call:
        call.return_value = gs_echo.EchoResponse()
        client.echo(request={"header": "sample1"})

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = gs_echo.EchoRequest(**{"header": "sample1"})
        # Ensure that the uuid4 field is set according to AIP 4235
        assert _UUID4_RE.fullmatch(args[0].request_id)
        request_msg.request_id = args[0].request_id
        # Ensure that the uuid4 field is set according to AIP 4235
        assert _UUID4_RE.fullmatch(args[0].other_request_id)
        request_msg.other_request_id = args[0].other_request_id
        assert args[0] == request_msg

        expected_headers = {'header': 'sample1', 'routing_id': 'sample1'}
        assert gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw['metadata']

def test_echo_routing_parameters_request_3_grpc():
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.echo),
            '__call__') as call:
        call.return_value = gs_echo.EchoResponse()
        client.echo(request={"header": "regions/sample1/zones/sample2/sample3"})

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = gs_echo.EchoRequest(**{"header": "regions/sample1/zones/sample2/sample3"})
        # Ensure that the uuid4 field is set according to AIP 4235
        assert _UUID4_RE.fullmatch(args[0].request_id)
        request_msg.request_id = args[0].request_id
        # Ensure that the uuid4 field is set according to AIP 4235
        assert _UUID4_RE.fullmatch(args[0].other_request_id)
        request_msg.other_request_id = args[0].other_request_id
        assert args[0] == request_msg

        expected_headers = {'header': 'regions/sample1/zones/sample2/sample3', 'routing_id': 'regions/sample1/zones/sample2/sample3', 'table_name': 'regions/sample1/zones/sample2/sample3'}
        assert gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw['metadata']

def test_echo_routing_parameters_request_4_grpc():
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.echo),
            '__call__') as call:
        call.return_value = gs_echo.EchoResponse()
        client.echo(request={"header": "projects/sample1/sample2"})

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = gs_echo.EchoRequest(**{"header": "projects/sample1/sample2"})
        # Ensure that the uuid4 field is set according to AIP 4235
        assert _UUID4_RE.fullmatch(args[0].request_id)
        request_msg.request_id = args[0].request_id
        # Ensure that the uuid4 field is set according to AIP 4235
        assert _UUID4_RE.fullmatch(args[0].other_request_id)
        request_msg.other_request_id = args[0].other_request_id
        assert args[0] == request_msg

        expected_headers = {'header': 'projects/sample1/sample2', 'routing_id': 'projects/sample1/sample2', 'super_id': 'projects/sample1'}
        assert gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw['metadata']

def test_echo_routing_parameters_request_5_grpc():
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.echo),
            '__call__') as call:
        call.return_value = gs_echo.EchoResponse()
        client.echo(request={"header": "projects/sample1/instances/sample2/sample3"})

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = gs_echo.EchoRequest(**{"header": "projects/sample1/instances/sample2/sample3"})
        # Ensure that the uuid4 field is set according to AIP 4235
        assert _UUID4_RE.fullmatch(args[0].request_id)
        request_msg.request_id = args[0].request_id
        # Ensure that the uuid4 field is set according to AIP 4235
        assert _UUID4_RE.fullmatch(args[0].other_request_id)
        request_msg.other_request_id = args[0].other_request_id
        assert args[0] == request_msg

        expected_headers = {'header': 'projects/sample1/instances/sample2/sample3', 'routing_id': 'projects/sample1/instances/sample2/sample3', 'super_id': 'projects/sample1', 'table_name': 'projects/sample1/instances/sample2/sample3', 'instance_id': 'instances/sample2'}
        assert gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw['metadata']

def test_echo_routing_parameters_request_6_grpc():
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.echo),
            '__call__') as call:
        call.return_value = gs_echo.EchoResponse()
        client.echo(request={"header": "projects/sample1/instances/sample2/sample3"})

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = gs_echo.EchoRequest(**{"header": "projects/sample1/instances/sample2/sample3"})
        # Ensure that the uuid4 field is set according to AIP 4235
        assert _UUID4_RE.fullmatch(args[0].request_id)
        request_msg.request_id = args[0].request_id
        # Ensure that the uuid4 field is set according to AIP 4235
        assert _UUID4_RE.fullmatch(args[0].other_request_id)
        request_msg.other_request_id = args[0].other_request_id
        assert args[0] == request_msg

        expected_headers = {'header': 'projects/sample1/instances/sample2/sample3', 'routing_id': 'projects/sample1/instances/sample2/sample3', 'super_id': 'projects/sample1', 'table_name': 'projects/sample1/instances/sample2/sample3', 'instance_id': 'instances/sample2'}
        assert gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw['metadata']

def test_echo_routing_parameters_request_7_grpc():
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.echo),
            '__call__') as call:
        call.return_value = gs_echo.EchoResponse()
        client.echo(request={"other_header": "sample1"})

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = gs_echo.EchoRequest(**{"other_header": "sample1"})
        # Ensure that the uuid4 field is set according to AIP 4235
        assert _UUID4_RE.fullmatch(args[0].request_id)
        request_msg.request_id = args[0].request_id
        # Ensure that the uuid4 field is set according to AIP 4235
        assert _UUID4_RE.fullmatch(args[0].other_request_id)
        request_msg.other_request_id = args[0].other_request_id
        assert args[0] == request_msg

        expected_headers = {'baz': 'sample1'}
        assert gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw['metadata']

def test_echo_routing_parameters_request_8_grpc():
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.echo),
            '__call__') as call:
        call.return_value = gs_echo.EchoResponse()
        client.echo(request={"other_header": "projects/sample1/sample2"})

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = gs_echo.EchoRequest(**{"other_header": "projects/sample1/sample2"})
        # Ensure that the uuid4 field is set according to AIP 4235
        assert _UUID4_RE.fullmatch(args[0].request_id)
        request_msg.request_id = args[0].request_id
        # Ensure that the uuid4 field is set according to AIP 4235
        assert _UUID4_RE.fullmatch(args[0].other_request_id)
        request_msg.other_request_id = args[0].other_request_id
        assert args[0] == request_msg

        expected_headers = {'baz': 'projects/sample1/sample2', 'qux': 'projects/sample1'}
        assert gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw['metadata']


def test_transport_kind_grpc_asyncio():
    transport = EchoAsyncClient.get_transport_class("grpc_asyncio")(
        credentials=async_anonymous_credentials()
    )
    assert transport.kind == "grpc_asyncio"


def test_initialize_client_w_grpc_asyncio():
    client = EchoAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio"
    )
    assert client is not None


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_echo_empty_call_grpc_asyncio():
    client = EchoAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.echo),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(gs_echo.EchoResponse(
            content='content_value',
            severity=gs_echo.Severity.NECESSARY,
            request_id='request_id_value',
            other_request_id='other_request_id_value',
        ))
        await client.echo(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gs_echo.EchoRequest()
        # Ensure that the uuid4 field is set according to AIP 4235
        assert _UUID4_RE.fullmatch(args[0].request_id)
        request_msg.request_id = args[0].request_id
        # Ensure that the uuid4 field is set according to AIP 4235
        assert _UUID4_RE.fullmatch(args[0].other_request_id)
        request_msg.other_request_id = args[0].other_request_id
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_echo_error_details_empty_call_grpc_asyncio():
    client = EchoAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.echo_error_details),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(gs_echo.EchoErrorDetailsResponse(
        ))
        await client.echo_error_details(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gs_echo.EchoErrorDetailsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_fail_echo_with_details_empty_call_grpc_asyncio():
    client = EchoAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.fail_echo_with_details),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(gs_echo.FailEchoWithDetailsResponse(
        ))
        await client.fail_echo_with_details(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gs_echo.FailEchoWithDetailsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_expand_empty_call_grpc_asyncio():
    client = EchoAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.expand),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = mock.Mock(aio.UnaryStreamCall, autospec=True)
        call.return_value.read = mock.AsyncMock(side_effect=[gs_echo.EchoResponse()])
        await client.expand(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gs_echo.ExpandRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_paged_expand_empty_call_grpc_asyncio():
    client = EchoAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.paged_expand),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(gs_echo.PagedExpandResponse(
            next_page_token='next_page_token_value',
        ))
        await client.paged_expand(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gs_echo.PagedExpandRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_paged_expand_legacy_empty_call_grpc_asyncio():
    client = EchoAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.paged_expand_legacy),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(gs_echo.PagedExpandResponse(
            next_page_token='next_page_token_value',
        ))
        await client.paged_expand_legacy(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gs_echo.PagedExpandLegacyRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_paged_expand_legacy_mapped_empty_call_grpc_asyncio():
    client = EchoAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.paged_expand_legacy_mapped),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(gs_echo.PagedExpandLegacyMappedResponse(
            next_page_token='next_page_token_value',
        ))
        await client.paged_expand_legacy_mapped(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gs_echo.PagedExpandRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_wait_empty_call_grpc_asyncio():
    client = EchoAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.wait),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name='operations/spam')
        )
        await client.wait(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gs_echo.WaitRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_block_empty_call_grpc_asyncio():
    client = EchoAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.block),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(gs_echo.BlockResponse(
            content='content_value',
        ))
        await client.block(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gs_echo.BlockRequest()
        assert args[0] == request_msg


@pytest.mark.asyncio
async def test_echo_routing_parameters_request_1_grpc_asyncio():
    client = EchoAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.echo),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(gs_echo.EchoResponse(
            content='content_value',
            severity=gs_echo.Severity.NECESSARY,
            request_id='request_id_value',
            other_request_id='other_request_id_value',
        ))
        await client.echo(request={"header": "sample1"})

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = gs_echo.EchoRequest(**{"header": "sample1"})
        # Ensure that the uuid4 field is set according to AIP 4235
        assert _UUID4_RE.fullmatch(args[0].request_id)
        request_msg.request_id = args[0].request_id
        # Ensure that the uuid4 field is set according to AIP 4235
        assert _UUID4_RE.fullmatch(args[0].other_request_id)
        request_msg.other_request_id = args[0].other_request_id
        assert args[0] == request_msg

        expected_headers = {'header': 'sample1', 'routing_id': 'sample1'}
        assert gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw['metadata']

@pytest.mark.asyncio
async def test_echo_routing_parameters_request_2_grpc_asyncio():
    client = EchoAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.echo),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(gs_echo.EchoResponse(
            content='content_value',
            severity=gs_echo.Severity.NECESSARY,
            request_id='request_id_value',
            other_request_id='other_request_id_value',
        ))
        await client.echo(request={"header": "sample1"})

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = gs_echo.EchoRequest(**{"header": "sample1"})
        # Ensure that the uuid4 field is set according to AIP 4235
        assert _UUID4_RE.fullmatch(args[0].request_id)
        request_msg.request_id = args[0].request_id
        # Ensure that the uuid4 field is set according to AIP 4235
        assert _UUID4_RE.fullmatch(args[0].other_request_id)
        request_msg.other_request_id = args[0].other_request_id
        assert args[0] == request_msg

        expected_headers = {'header': 'sample1', 'routing_id': 'sample1'}
        assert gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw['metadata']

@pytest.mark.asyncio
async def test_echo_routing_parameters_request_3_grpc_asyncio():
    client = EchoAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.echo),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(gs_echo.EchoResponse(
            content='content_value',
            severity=gs_echo.Severity.NECESSARY,
            request_id='request_id_value',
            other_request_id='other_request_id_value',
        ))
        await client.echo(request={"header": "regions/sample1/zones/sample2/sample3"})

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = gs_echo.EchoRequest(**{"header": "regions/sample1/zones/sample2/sample3"})
        # Ensure that the uuid4 field is set according to AIP 4235
        assert _UUID4_RE.fullmatch(args[0].request_id)
        request_msg.request_id = args[0].request_id
        # Ensure that the uuid4 field is set according to AIP 4235
        assert _UUID4_RE.fullmatch(args[0].other_request_id)
        request_msg.other_request_id = args[0].other_request_id
        assert args[0] == request_msg

        expected_headers = {'header': 'regions/sample1/zones/sample2/sample3', 'routing_id': 'regions/sample1/zones/sample2/sample3', 'table_name': 'regions/sample1/zones/sample2/sample3'}
        assert gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw['metadata']

@pytest.mark.asyncio
async def test_echo_routing_parameters_request_4_grpc_asyncio():
    client = EchoAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.echo),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(gs_echo.EchoResponse(
            content='content_value',
            severity=gs_echo.Severity.NECESSARY,
            request_id='request_id_value',
            other_request_id='other_request_id_value',
        ))
        await client.echo(request={"header": "projects/sample1/sample2"})

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = gs_echo.EchoRequest(**{"header": "projects/sample1/sample2"})
        # Ensure that the uuid4 field is set according to AIP 4235
        assert _UUID4_RE.fullmatch(args[0].request_id)
        request_msg.request_id = args[0].request_id
        # Ensure that the uuid4 field is set according to AIP 4235
        assert _UUID4_RE.fullmatch(args[0].other_request_id)
        request_msg.other_request_id = args[0].other_request_id
        assert args[0] == request_msg

        expected_headers = {'header': 'projects/sample1/sample2', 'routing_id': 'projects/sample1/sample2', 'super_id': 'projects/sample1'}
        assert gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw['metadata']

@pytest.mark.asyncio
async def test_echo_routing_parameters_request_5_grpc_asyncio():
    client = EchoAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.echo),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(gs_echo.EchoResponse(
            content='content_value',
            severity=gs_echo.Severity.NECESSARY,
            request_id='request_id_value',
            other_request_id='other_request_id_value',
        ))
        await client.echo(request={"header": "projects/sample1/instances/sample2/sample3"})

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = gs_echo.EchoRequest(**{"header": "projects/sample1/instances/sample2/sample3"})
        # Ensure that the uuid4 field is set according to AIP 4235
        assert _UUID4_RE.fullmatch(args[0].request_id)
        request_msg.request_id = args[0].request_id
        # Ensure that the uuid4 field is set according to AIP 4235
        assert _UUID4_RE.fullmatch(args[0].other_request_id)
        request_msg.other_request_id = args[0].other_request_id
        assert args[0] == request_msg

        expected_headers = {'header': 'projects/sample1/instances/sample2/sample3', 'routing_id': 'projects/sample1/instances/sample2/sample3', 'super_id': 'projects/sample1', 'table_name': 'projects/sample1/instances/sample2/sample3', 'instance_id': 'instances/sample2'}
        assert gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw['metadata']

@pytest.mark.asyncio
async def test_echo_routing_parameters_request_6_grpc_asyncio():
    client = EchoAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.echo),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(gs_echo.EchoResponse(
            content='content_value',
            severity=gs_echo.Severity.NECESSARY,
            request_id='request_id_value',
            other_request_id='other_request_id_value',
        ))
        await client.echo(request={"header": "projects/sample1/instances/sample2/sample3"})

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = gs_echo.EchoRequest(**{"header": "projects/sample1/instances/sample2/sample3"})
        # Ensure that the uuid4 field is set according to AIP 4235
        assert _UUID4_RE.fullmatch(args[0].request_id)
        request_msg.request_id = args[0].request_id
        # Ensure that the uuid4 field is set according to AIP 4235
        assert _UUID4_RE.fullmatch(args[0].other_request_id)
        request_msg.other_request_id = args[0].other_request_id
        assert args[0] == request_msg

        expected_headers = {'header': 'projects/sample1/instances/sample2/sample3', 'routing_id': 'projects/sample1/instances/sample2/sample3', 'super_id': 'projects/sample1', 'table_name': 'projects/sample1/instances/sample2/sample3', 'instance_id': 'instances/sample2'}
        assert gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw['metadata']

@pytest.mark.asyncio
async def test_echo_routing_parameters_request_7_grpc_asyncio():
    client = EchoAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.echo),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(gs_echo.EchoResponse(
            content='content_value',
            severity=gs_echo.Severity.NECESSARY,
            request_id='request_id_value',
            other_request_id='other_request_id_value',
        ))
        await client.echo(request={"other_header": "sample1"})

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = gs_echo.EchoRequest(**{"other_header": "sample1"})
        # Ensure that the uuid4 field is set according to AIP 4235
        assert _UUID4_RE.fullmatch(args[0].request_id)
        request_msg.request_id = args[0].request_id
        # Ensure that the uuid4 field is set according to AIP 4235
        assert _UUID4_RE.fullmatch(args[0].other_request_id)
        request_msg.other_request_id = args[0].other_request_id
        assert args[0] == request_msg

        expected_headers = {'baz': 'sample1'}
        assert gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw['metadata']

@pytest.mark.asyncio
async def test_echo_routing_parameters_request_8_grpc_asyncio():
    client = EchoAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.echo),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(gs_echo.EchoResponse(
            content='content_value',
            severity=gs_echo.Severity.NECESSARY,
            request_id='request_id_value',
            other_request_id='other_request_id_value',
        ))
        await client.echo(request={"other_header": "projects/sample1/sample2"})

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = gs_echo.EchoRequest(**{"other_header": "projects/sample1/sample2"})
        # Ensure that the uuid4 field is set according to AIP 4235
        assert _UUID4_RE.fullmatch(args[0].request_id)
        request_msg.request_id = args[0].request_id
        # Ensure that the uuid4 field is set according to AIP 4235
        assert _UUID4_RE.fullmatch(args[0].other_request_id)
        request_msg.other_request_id = args[0].other_request_id
        assert args[0] == request_msg

        expected_headers = {'baz': 'projects/sample1/sample2', 'qux': 'projects/sample1'}
        assert gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw['metadata']


def test_transport_kind_rest():
    transport = EchoClient.get_transport_class("rest")(
        credentials=ga_credentials.AnonymousCredentials()
    )
    assert transport.kind == "rest"


def test_echo_rest_bad_request(request_type=gs_echo.EchoRequest):
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, 'request') as req, pytest.raises(core_exceptions.BadRequest):
        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        json_return_value = ''
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = mock.Mock()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.echo(request)


@pytest.mark.parametrize("request_type", [
  gs_echo.EchoRequest,
  dict,
])
def test_echo_rest_call_success(request_type):
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), 'request') as req:
        # Designate an appropriate value for the returned response.
        return_value = gs_echo.EchoResponse(
              content='content_value',
              severity=gs_echo.Severity.NECESSARY,
              request_id='request_id_value',
              other_request_id='other_request_id_value',
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = gs_echo.EchoResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode('UTF-8')
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.echo(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, gs_echo.EchoResponse)
    assert response.content == 'content_value'
    assert response.severity == gs_echo.Severity.NECESSARY
    assert response.request_id == 'request_id_value'
    assert response.other_request_id == 'other_request_id_value'


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_echo_rest_interceptors(null_interceptor):
    transport = transports.EchoRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None if null_interceptor else transports.EchoRestInterceptor(),
        )
    client = EchoClient(transport=transport)

    with mock.patch.object(type(client.transport._session), "request") as req, \
        mock.patch.object(path_template, "transcode")  as transcode, \
        mock.patch.object(transports.EchoRestInterceptor, "post_echo") as post, \
        mock.patch.object(transports.EchoRestInterceptor, "post_echo_with_metadata") as post_with_metadata, \
        mock.patch.object(transports.EchoRestInterceptor, "pre_echo") as pre:
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = gs_echo.EchoRequest.pb(gs_echo.EchoRequest())
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = gs_echo.EchoResponse.to_json(gs_echo.EchoResponse())
        req.return_value.content = return_value

        request = gs_echo.EchoRequest()
        metadata =[
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = gs_echo.EchoResponse()
        post_with_metadata.return_value = gs_echo.EchoResponse(), metadata

        client.echo(request, metadata=[("key", "val"), ("cephalopod", "squid"),])

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_echo_error_details_rest_bad_request(request_type=gs_echo.EchoErrorDetailsRequest):
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, 'request') as req, pytest.raises(core_exceptions.BadRequest):
        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        json_return_value = ''
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = mock.Mock()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.echo_error_details(request)


@pytest.mark.parametrize("request_type", [
  gs_echo.EchoErrorDetailsRequest,
  dict,
])
def test_echo_error_details_rest_call_success(request_type):
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), 'request') as req:
        # Designate an appropriate value for the returned response.
        return_value = gs_echo.EchoErrorDetailsResponse(
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = gs_echo.EchoErrorDetailsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode('UTF-8')
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.echo_error_details(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, gs_echo.EchoErrorDetailsResponse)


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_echo_error_details_rest_interceptors(null_interceptor):
    transport = transports.EchoRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None if null_interceptor else transports.EchoRestInterceptor(),
        )
    client = EchoClient(transport=transport)

    with mock.patch.object(type(client.transport._session), "request") as req, \
        mock.patch.object(path_template, "transcode")  as transcode, \
        mock.patch.object(transports.EchoRestInterceptor, "post_echo_error_details") as post, \
        mock.patch.object(transports.EchoRestInterceptor, "post_echo_error_details_with_metadata") as post_with_metadata, \
        mock.patch.object(transports.EchoRestInterceptor, "pre_echo_error_details") as pre:
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = gs_echo.EchoErrorDetailsRequest.pb(gs_echo.EchoErrorDetailsRequest())
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = gs_echo.EchoErrorDetailsResponse.to_json(gs_echo.EchoErrorDetailsResponse())
        req.return_value.content = return_value

        request = gs_echo.EchoErrorDetailsRequest()
        metadata =[
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = gs_echo.EchoErrorDetailsResponse()
        post_with_metadata.return_value = gs_echo.EchoErrorDetailsResponse(), metadata

        client.echo_error_details(request, metadata=[("key", "val"), ("cephalopod", "squid"),])

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_fail_echo_with_details_rest_bad_request(request_type=gs_echo.FailEchoWithDetailsRequest):
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, 'request') as req, pytest.raises(core_exceptions.BadRequest):
        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        json_return_value = ''
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = mock.Mock()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.fail_echo_with_details(request)


@pytest.mark.parametrize("request_type", [
  gs_echo.FailEchoWithDetailsRequest,
  dict,
])
def test_fail_echo_with_details_rest_call_success(request_type):
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), 'request') as req:
        # Designate an appropriate value for the returned response.
        return_value = gs_echo.FailEchoWithDetailsResponse(
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = gs_echo.FailEchoWithDetailsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode('UTF-8')
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.fail_echo_with_details(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, gs_echo.FailEchoWithDetailsResponse)


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_fail_echo_with_details_rest_interceptors(null_interceptor):
    transport = transports.EchoRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None if null_interceptor else transports.EchoRestInterceptor(),
        )
    client = EchoClient(transport=transport)

    with mock.patch.object(type(client.transport._session), "request") as req, \
        mock.patch.object(path_template, "transcode")  as transcode, \
        mock.patch.object(transports.EchoRestInterceptor, "post_fail_echo_with_details") as post, \
        mock.patch.object(transports.EchoRestInterceptor, "post_fail_echo_with_details_with_metadata") as post_with_metadata, \
        mock.patch.object(transports.EchoRestInterceptor, "pre_fail_echo_with_details") as pre:
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = gs_echo.FailEchoWithDetailsRequest.pb(gs_echo.FailEchoWithDetailsRequest())
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = gs_echo.FailEchoWithDetailsResponse.to_json(gs_echo.FailEchoWithDetailsResponse())
        req.return_value.content = return_value

        request = gs_echo.FailEchoWithDetailsRequest()
        metadata =[
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = gs_echo.FailEchoWithDetailsResponse()
        post_with_metadata.return_value = gs_echo.FailEchoWithDetailsResponse(), metadata

        client.fail_echo_with_details(request, metadata=[("key", "val"), ("cephalopod", "squid"),])

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_expand_rest_bad_request(request_type=gs_echo.ExpandRequest):
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, 'request') as req, pytest.raises(core_exceptions.BadRequest):
        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        json_return_value = ''
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = mock.Mock()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.expand(request)


@pytest.mark.parametrize("request_type", [
  gs_echo.ExpandRequest,
  dict,
])
def test_expand_rest_call_success(request_type):
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), 'request') as req:
        # Designate an appropriate value for the returned response.
        return_value = gs_echo.EchoResponse(
              content='content_value',
              severity=gs_echo.Severity.NECESSARY,
              request_id='request_id_value',
              other_request_id='other_request_id_value',
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = gs_echo.EchoResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        json_return_value = "[{}]".format(json_return_value)
        response_value.iter_content = mock.Mock(return_value=iter(json_return_value))
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.expand(request)

    assert isinstance(response, Iterable)
    response = next(response)

    # Establish that the response is the type that we expect.
    assert isinstance(response, gs_echo.EchoResponse)
    assert response.content == 'content_value'
    assert response.severity == gs_echo.Severity.NECESSARY
    assert response.request_id == 'request_id_value'
    assert response.other_request_id == 'other_request_id_value'


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_expand_rest_interceptors(null_interceptor):
    transport = transports.EchoRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None if null_interceptor else transports.EchoRestInterceptor(),
        )
    client = EchoClient(transport=transport)

    with mock.patch.object(type(client.transport._session), "request") as req, \
        mock.patch.object(path_template, "transcode")  as transcode, \
        mock.patch.object(transports.EchoRestInterceptor, "post_expand") as post, \
        mock.patch.object(transports.EchoRestInterceptor, "post_expand_with_metadata") as post_with_metadata, \
        mock.patch.object(transports.EchoRestInterceptor, "pre_expand") as pre:
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = gs_echo.ExpandRequest.pb(gs_echo.ExpandRequest())
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = gs_echo.EchoResponse.to_json(gs_echo.EchoResponse())
        req.return_value.iter_content = mock.Mock(return_value=iter(return_value))

        request = gs_echo.ExpandRequest()
        metadata =[
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = gs_echo.EchoResponse()
        post_with_metadata.return_value = gs_echo.EchoResponse(), metadata

        client.expand(request, metadata=[("key", "val"), ("cephalopod", "squid"),])

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_collect_rest_error():

    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest"
    )

    with pytest.raises(NotImplementedError) as not_implemented_error:
        client.collect({})
    assert (
        "Method Collect is not available over REST transport"
        in str(not_implemented_error.value)
    )


def test_chat_rest_error():

    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest"
    )

    with pytest.raises(NotImplementedError) as not_implemented_error:
        client.chat({})
    assert (
        "Method Chat is not available over REST transport"
        in str(not_implemented_error.value)
    )


def test_paged_expand_rest_bad_request(request_type=gs_echo.PagedExpandRequest):
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, 'request') as req, pytest.raises(core_exceptions.BadRequest):
        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        json_return_value = ''
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = mock.Mock()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.paged_expand(request)


@pytest.mark.parametrize("request_type", [
  gs_echo.PagedExpandRequest,
  dict,
])
def test_paged_expand_rest_call_success(request_type):
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), 'request') as req:
        # Designate an appropriate value for the returned response.
        return_value = gs_echo.PagedExpandResponse(
              next_page_token='next_page_token_value',
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = gs_echo.PagedExpandResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode('UTF-8')
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.paged_expand(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.PagedExpandPager)
    assert response.next_page_token == 'next_page_token_value'


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_paged_expand_rest_interceptors(null_interceptor):
    transport = transports.EchoRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None if null_interceptor else transports.EchoRestInterceptor(),
        )
    client = EchoClient(transport=transport)

    with mock.patch.object(type(client.transport._session), "request") as req, \
        mock.patch.object(path_template, "transcode")  as transcode, \
        mock.patch.object(transports.EchoRestInterceptor, "post_paged_expand") as post, \
        mock.patch.object(transports.EchoRestInterceptor, "post_paged_expand_with_metadata") as post_with_metadata, \
        mock.patch.object(transports.EchoRestInterceptor, "pre_paged_expand") as pre:
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = gs_echo.PagedExpandRequest.pb(gs_echo.PagedExpandRequest())
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = gs_echo.PagedExpandResponse.to_json(gs_echo.PagedExpandResponse())
        req.return_value.content = return_value

        request = gs_echo.PagedExpandRequest()
        metadata =[
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = gs_echo.PagedExpandResponse()
        post_with_metadata.return_value = gs_echo.PagedExpandResponse(), metadata

        client.paged_expand(request, metadata=[("key", "val"), ("cephalopod", "squid"),])

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_paged_expand_legacy_rest_bad_request(request_type=gs_echo.PagedExpandLegacyRequest):
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, 'request') as req, pytest.raises(core_exceptions.BadRequest):
        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        json_return_value = ''
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = mock.Mock()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.paged_expand_legacy(request)


@pytest.mark.parametrize("request_type", [
  gs_echo.PagedExpandLegacyRequest,
  dict,
])
def test_paged_expand_legacy_rest_call_success(request_type):
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), 'request') as req:
        # Designate an appropriate value for the returned response.
        return_value = gs_echo.PagedExpandResponse(
              next_page_token='next_page_token_value',
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = gs_echo.PagedExpandResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode('UTF-8')
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.paged_expand_legacy(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.PagedExpandLegacyPager)
    assert response.next_page_token == 'next_page_token_value'


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_paged_expand_legacy_rest_interceptors(null_interceptor):
    transport = transports.EchoRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None if null_interceptor else transports.EchoRestInterceptor(),
        )
    client = EchoClient(transport=transport)

    with mock.patch.object(type(client.transport._session), "request") as req, \
        mock.patch.object(path_template, "transcode")  as transcode, \
        mock.patch.object(transports.EchoRestInterceptor, "post_paged_expand_legacy") as post, \
        mock.patch.object(transports.EchoRestInterceptor, "post_paged_expand_legacy_with_metadata") as post_with_metadata, \
        mock.patch.object(transports.EchoRestInterceptor, "pre_paged_expand_legacy") as pre:
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = gs_echo.PagedExpandLegacyRequest.pb(gs_echo.PagedExpandLegacyRequest())
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = gs_echo.PagedExpandResponse.to_json(gs_echo.PagedExpandResponse())
        req.return_value.content = return_value

        request = gs_echo.PagedExpandLegacyRequest()
        metadata =[
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = gs_echo.PagedExpandResponse()
        post_with_metadata.return_value = gs_echo.PagedExpandResponse(), metadata

        client.paged_expand_legacy(request, metadata=[("key", "val"), ("cephalopod", "squid"),])

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_paged_expand_legacy_mapped_rest_bad_request(request_type=gs_echo.PagedExpandRequest):
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, 'request') as req, pytest.raises(core_exceptions.BadRequest):
        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        json_return_value = ''
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = mock.Mock()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.paged_expand_legacy_mapped(request)


@pytest.mark.parametrize("request_type", [
  gs_echo.PagedExpandRequest,
  dict,
])
def test_paged_expand_legacy_mapped_rest_call_success(request_type):
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), 'request') as req:
        # Designate an appropriate value for the returned response.
        return_value = gs_echo.PagedExpandLegacyMappedResponse(
              next_page_token='next_page_token_value',
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = gs_echo.PagedExpandLegacyMappedResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode('UTF-8')
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.paged_expand_legacy_mapped(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.PagedExpandLegacyMappedPager)
    assert response.next_page_token == 'next_page_token_value'


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_paged_expand_legacy_mapped_rest_interceptors(null_interceptor):
    transport = transports.EchoRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None if null_interceptor else transports.EchoRestInterceptor(),
        )
    client = EchoClient(transport=transport)

    with mock.patch.object(type(client.transport._session), "request") as req, \
        mock.patch.object(path_template, "transcode")  as transcode, \
        mock.patch.object(transports.EchoRestInterceptor, "post_paged_expand_legacy_mapped") as post, \
        mock.patch.object(transports.EchoRestInterceptor, "post_paged_expand_legacy_mapped_with_metadata") as post_with_metadata, \
        mock.patch.object(transports.EchoRestInterceptor, "pre_paged_expand_legacy_mapped") as pre:
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = gs_echo.PagedExpandRequest.pb(gs_echo.PagedExpandRequest())
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = gs_echo.PagedExpandLegacyMappedResponse.to_json(gs_echo.PagedExpandLegacyMappedResponse())
        req.return_value.content = return_value

        request = gs_echo.PagedExpandRequest()
        metadata =[
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = gs_echo.PagedExpandLegacyMappedResponse()
        post_with_metadata.return_value = gs_echo.PagedExpandLegacyMappedResponse(), metadata

        client.paged_expand_legacy_mapped(request, metadata=[("key", "val"), ("cephalopod", "squid"),])

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_wait_rest_bad_request(request_type=gs_echo.WaitRequest):
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, 'request') as req, pytest.raises(core_exceptions.BadRequest):
        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        json_return_value = ''
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = mock.Mock()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.wait(request)


@pytest.mark.parametrize("request_type", [
  gs_echo.WaitRequest,
  dict,
])
def test_wait_rest_call_success(request_type):
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), 'request') as req:
        # Designate an appropriate value for the returned response.
        return_value = operations_pb2.Operation(name='operations/spam')

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode('UTF-8')
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.wait(request)

    # Establish that the response is the type that we expect.
    json_return_value = json_format.MessageToJson(return_value)


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_wait_rest_interceptors(null_interceptor):
    transport = transports.EchoRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None if null_interceptor else transports.EchoRestInterceptor(),
        )
    client = EchoClient(transport=transport)

    with mock.patch.object(type(client.transport._session), "request") as req, \
        mock.patch.object(path_template, "transcode")  as transcode, \
        mock.patch.object(operation.Operation, "_set_result_from_operation"), \
        mock.patch.object(transports.EchoRestInterceptor, "post_wait") as post, \
        mock.patch.object(transports.EchoRestInterceptor, "post_wait_with_metadata") as post_with_metadata, \
        mock.patch.object(transports.EchoRestInterceptor, "pre_wait") as pre:
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = gs_echo.WaitRequest.pb(gs_echo.WaitRequest())
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

        request = gs_echo.WaitRequest()
        metadata =[
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = operations_pb2.Operation()
        post_with_metadata.return_value = operations_pb2.Operation(), metadata

        client.wait(request, metadata=[("key", "val"), ("cephalopod", "squid"),])

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_block_rest_bad_request(request_type=gs_echo.BlockRequest):
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, 'request') as req, pytest.raises(core_exceptions.BadRequest):
        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        json_return_value = ''
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = mock.Mock()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.block(request)


@pytest.mark.parametrize("request_type", [
  gs_echo.BlockRequest,
  dict,
])
def test_block_rest_call_success(request_type):
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), 'request') as req:
        # Designate an appropriate value for the returned response.
        return_value = gs_echo.BlockResponse(
              content='content_value',
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = gs_echo.BlockResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode('UTF-8')
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.block(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, gs_echo.BlockResponse)
    assert response.content == 'content_value'


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_block_rest_interceptors(null_interceptor):
    transport = transports.EchoRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None if null_interceptor else transports.EchoRestInterceptor(),
        )
    client = EchoClient(transport=transport)

    with mock.patch.object(type(client.transport._session), "request") as req, \
        mock.patch.object(path_template, "transcode")  as transcode, \
        mock.patch.object(transports.EchoRestInterceptor, "post_block") as post, \
        mock.patch.object(transports.EchoRestInterceptor, "post_block_with_metadata") as post_with_metadata, \
        mock.patch.object(transports.EchoRestInterceptor, "pre_block") as pre:
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = gs_echo.BlockRequest.pb(gs_echo.BlockRequest())
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = gs_echo.BlockResponse.to_json(gs_echo.BlockResponse())
        req.return_value.content = return_value

        request = gs_echo.BlockRequest()
        metadata =[
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = gs_echo.BlockResponse()
        post_with_metadata.return_value = gs_echo.BlockResponse(), metadata

        client.block(request, metadata=[("key", "val"), ("cephalopod", "squid"),])

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_list_locations_rest_bad_request(request_type=locations_pb2.ListLocationsRequest):
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type()
    request = json_format.ParseDict({'name': 'projects/sample1'}, request)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, 'request') as req, pytest.raises(core_exceptions.BadRequest):
        # Wrap the value into a proper Response obj
        response_value = Response()
        json_return_value = ''
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.list_locations(request)


@pytest.mark.parametrize("request_type", [
    locations_pb2.ListLocationsRequest,
    dict,
])
def test_list_locations_rest(request_type):
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    request_init = {'name': 'projects/sample1'}
    request = request_type(**request_init)
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, 'request') as req:
        # Designate an appropriate value for the returned response.
        return_value = locations_pb2.ListLocationsResponse()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode('UTF-8')

        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        response = client.list_locations(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, locations_pb2.ListLocationsResponse)


def test_get_location_rest_bad_request(request_type=locations_pb2.GetLocationRequest):
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type()
    request = json_format.ParseDict({'name': 'projects/sample1/locations/sample2'}, request)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, 'request') as req, pytest.raises(core_exceptions.BadRequest):
        # Wrap the value into a proper Response obj
        response_value = Response()
        json_return_value = ''
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.get_location(request)


@pytest.mark.parametrize("request_type", [
    locations_pb2.GetLocationRequest,
    dict,
])
def test_get_location_rest(request_type):
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    request_init = {'name': 'projects/sample1/locations/sample2'}
    request = request_type(**request_init)
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, 'request') as req:
        # Designate an appropriate value for the returned response.
        return_value = locations_pb2.Location()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode('UTF-8')

        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        response = client.get_location(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, locations_pb2.Location)


def test_set_iam_policy_rest_bad_request(request_type=iam_policy_pb2.SetIamPolicyRequest):
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type()
    request = json_format.ParseDict({'resource': 'users/sample1'}, request)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, 'request') as req, pytest.raises(core_exceptions.BadRequest):
        # Wrap the value into a proper Response obj
        response_value = Response()
        json_return_value = ''
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.set_iam_policy(request)


@pytest.mark.parametrize("request_type", [
    iam_policy_pb2.SetIamPolicyRequest,
    dict,
])
def test_set_iam_policy_rest(request_type):
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    request_init = {'resource': 'users/sample1'}
    request = request_type(**request_init)
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, 'request') as req:
        # Designate an appropriate value for the returned response.
        return_value = policy_pb2.Policy()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode('UTF-8')

        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        response = client.set_iam_policy(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, policy_pb2.Policy)


def test_get_iam_policy_rest_bad_request(request_type=iam_policy_pb2.GetIamPolicyRequest):
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type()
    request = json_format.ParseDict({'resource': 'users/sample1'}, request)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, 'request') as req, pytest.raises(core_exceptions.BadRequest):
        # Wrap the value into a proper Response obj
        response_value = Response()
        json_return_value = ''
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.get_iam_policy(request)


@pytest.mark.parametrize("request_type", [
    iam_policy_pb2.GetIamPolicyRequest,
    dict,
])
def test_get_iam_policy_rest(request_type):
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    request_init = {'resource': 'users/sample1'}
    request = request_type(**request_init)
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, 'request') as req:
        # Designate an appropriate value for the returned response.
        return_value = policy_pb2.Policy()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode('UTF-8')

        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        response = client.get_iam_policy(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, policy_pb2.Policy)


def test_test_iam_permissions_rest_bad_request(request_type=iam_policy_pb2.TestIamPermissionsRequest):
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type()
    request = json_format.ParseDict({'resource': 'users/sample1'}, request)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, 'request') as req, pytest.raises(core_exceptions.BadRequest):
        # Wrap the value into a proper Response obj
        response_value = Response()
        json_return_value = ''
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.test_iam_permissions(request)


@pytest.mark.parametrize("request_type", [
    iam_policy_pb2.TestIamPermissionsRequest,
    dict,
])
def test_test_iam_permissions_rest(request_type):
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    request_init = {'resource': 'users/sample1'}
    request = request_type(**request_init)
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, 'request') as req:
        # Designate an appropriate value for the returned response.
        return_value = iam_policy_pb2.TestIamPermissionsResponse()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode('UTF-8')

        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        response = client.test_iam_permissions(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, iam_policy_pb2.TestIamPermissionsResponse)


def test_list_operations_rest_bad_request(request_type=operations_pb2.ListOperationsRequest):
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type()
    request = json_format.ParseDict({}, request)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, 'request') as req, pytest.raises(core_exceptions.BadRequest):
        # Wrap the value into a proper Response obj
        response_value = Response()
        json_return_value = ''
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.list_operations(request)


@pytest.mark.parametrize("request_type", [
    operations_pb2.ListOperationsRequest,
    dict,
])
def test_list_operations_rest(request_type):
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    request_init = {}
    request = request_type(**request_init)
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, 'request') as req:
        # Designate an appropriate value for the returned response.
        return_value = operations_pb2.ListOperationsResponse()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode('UTF-8')

        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        response = client.list_operations(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, operations_pb2.ListOperationsResponse)


def test_get_operation_rest_bad_request(request_type=operations_pb2.GetOperationRequest):
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type()
    request = json_format.ParseDict({'name': 'operations/sample1'}, request)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, 'request') as req, pytest.raises(core_exceptions.BadRequest):
        # Wrap the value into a proper Response obj
        response_value = Response()
        json_return_value = ''
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.get_operation(request)


@pytest.mark.parametrize("request_type", [
    operations_pb2.GetOperationRequest,
    dict,
])
def test_get_operation_rest(request_type):
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    request_init = {'name': 'operations/sample1'}
    request = request_type(**request_init)
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, 'request') as req:
        # Designate an appropriate value for the returned response.
        return_value = operations_pb2.Operation()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode('UTF-8')

        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        response = client.get_operation(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, operations_pb2.Operation)


def test_delete_operation_rest_bad_request(request_type=operations_pb2.DeleteOperationRequest):
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type()
    request = json_format.ParseDict({'name': 'operations/sample1'}, request)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, 'request') as req, pytest.raises(core_exceptions.BadRequest):
        # Wrap the value into a proper Response obj
        response_value = Response()
        json_return_value = ''
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.delete_operation(request)


@pytest.mark.parametrize("request_type", [
    operations_pb2.DeleteOperationRequest,
    dict,
])
def test_delete_operation_rest(request_type):
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    request_init = {'name': 'operations/sample1'}
    request = request_type(**request_init)
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, 'request') as req:
        # Designate an appropriate value for the returned response.
        return_value = None

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200
        json_return_value = '{}'
        response_value.content = json_return_value.encode('UTF-8')

        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        response = client.delete_operation(request)

    # Establish that the response is the type that we expect.
    assert response is None


def test_cancel_operation_rest_bad_request(request_type=operations_pb2.CancelOperationRequest):
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type()
    request = json_format.ParseDict({'name': 'operations/sample1'}, request)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, 'request') as req, pytest.raises(core_exceptions.BadRequest):
        # Wrap the value into a proper Response obj
        response_value = Response()
        json_return_value = ''
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.cancel_operation(request)


@pytest.mark.parametrize("request_type", [
    operations_pb2.CancelOperationRequest,
    dict,
])
def test_cancel_operation_rest(request_type):
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    request_init = {'name': 'operations/sample1'}
    request = request_type(**request_init)
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, 'request') as req:
        # Designate an appropriate value for the returned response.
        return_value = None

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200
        json_return_value = '{}'
        response_value.content = json_return_value.encode('UTF-8')

        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        response = client.cancel_operation(request)

    # Establish that the response is the type that we expect.
    assert response is None

def test_initialize_client_w_rest():
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest"
    )
    assert client is not None


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_echo_empty_call_rest():
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.echo),
            '__call__') as call:
        client.echo(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gs_echo.EchoRequest()
        # Ensure that the uuid4 field is set according to AIP 4235
        assert _UUID4_RE.fullmatch(args[0].request_id)
        request_msg.request_id = args[0].request_id
        # Ensure that the uuid4 field is set according to AIP 4235
        assert _UUID4_RE.fullmatch(args[0].other_request_id)
        request_msg.other_request_id = args[0].other_request_id
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_echo_error_details_empty_call_rest():
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.echo_error_details),
            '__call__') as call:
        client.echo_error_details(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gs_echo.EchoErrorDetailsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_fail_echo_with_details_empty_call_rest():
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.fail_echo_with_details),
            '__call__') as call:
        client.fail_echo_with_details(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gs_echo.FailEchoWithDetailsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_expand_empty_call_rest():
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.expand),
            '__call__') as call:
        client.expand(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gs_echo.ExpandRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_paged_expand_empty_call_rest():
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.paged_expand),
            '__call__') as call:
        client.paged_expand(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gs_echo.PagedExpandRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_paged_expand_legacy_empty_call_rest():
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.paged_expand_legacy),
            '__call__') as call:
        client.paged_expand_legacy(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gs_echo.PagedExpandLegacyRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_paged_expand_legacy_mapped_empty_call_rest():
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.paged_expand_legacy_mapped),
            '__call__') as call:
        client.paged_expand_legacy_mapped(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gs_echo.PagedExpandRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_wait_empty_call_rest():
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.wait),
            '__call__') as call:
        client.wait(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gs_echo.WaitRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_block_empty_call_rest():
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.block),
            '__call__') as call:
        client.block(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gs_echo.BlockRequest()
        assert args[0] == request_msg


def test_echo_routing_parameters_request_1_rest():
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.echo),
            '__call__') as call:
        client.echo(request={"header": "sample1"})

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = gs_echo.EchoRequest(**{"header": "sample1"})
        # Ensure that the uuid4 field is set according to AIP 4235
        assert _UUID4_RE.fullmatch(args[0].request_id)
        request_msg.request_id = args[0].request_id
        # Ensure that the uuid4 field is set according to AIP 4235
        assert _UUID4_RE.fullmatch(args[0].other_request_id)
        request_msg.other_request_id = args[0].other_request_id
        assert args[0] == request_msg

        expected_headers = {'header': 'sample1', 'routing_id': 'sample1'}
        assert gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw['metadata']

def test_echo_routing_parameters_request_2_rest():
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.echo),
            '__call__') as call:
        client.echo(request={"header": "sample1"})

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = gs_echo.EchoRequest(**{"header": "sample1"})
        # Ensure that the uuid4 field is set according to AIP 4235
        assert _UUID4_RE.fullmatch(args[0].request_id)
        request_msg.request_id = args[0].request_id
        # Ensure that the uuid4 field is set according to AIP 4235
        assert _UUID4_RE.fullmatch(args[0].other_request_id)
        request_msg.other_request_id = args[0].other_request_id
        assert args[0] == request_msg

        expected_headers = {'header': 'sample1', 'routing_id': 'sample1'}
        assert gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw['metadata']

def test_echo_routing_parameters_request_3_rest():
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.echo),
            '__call__') as call:
        client.echo(request={"header": "regions/sample1/zones/sample2/sample3"})

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = gs_echo.EchoRequest(**{"header": "regions/sample1/zones/sample2/sample3"})
        # Ensure that the uuid4 field is set according to AIP 4235
        assert _UUID4_RE.fullmatch(args[0].request_id)
        request_msg.request_id = args[0].request_id
        # Ensure that the uuid4 field is set according to AIP 4235
        assert _UUID4_RE.fullmatch(args[0].other_request_id)
        request_msg.other_request_id = args[0].other_request_id
        assert args[0] == request_msg

        expected_headers = {'header': 'regions/sample1/zones/sample2/sample3', 'routing_id': 'regions/sample1/zones/sample2/sample3', 'table_name': 'regions/sample1/zones/sample2/sample3'}
        assert gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw['metadata']

def test_echo_routing_parameters_request_4_rest():
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.echo),
            '__call__') as call:
        client.echo(request={"header": "projects/sample1/sample2"})

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = gs_echo.EchoRequest(**{"header": "projects/sample1/sample2"})
        # Ensure that the uuid4 field is set according to AIP 4235
        assert _UUID4_RE.fullmatch(args[0].request_id)
        request_msg.request_id = args[0].request_id
        # Ensure that the uuid4 field is set according to AIP 4235
        assert _UUID4_RE.fullmatch(args[0].other_request_id)
        request_msg.other_request_id = args[0].other_request_id
        assert args[0] == request_msg

        expected_headers = {'header': 'projects/sample1/sample2', 'routing_id': 'projects/sample1/sample2', 'super_id': 'projects/sample1'}
        assert gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw['metadata']

def test_echo_routing_parameters_request_5_rest():
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.echo),
            '__call__') as call:
        client.echo(request={"header": "projects/sample1/instances/sample2/sample3"})

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = gs_echo.EchoRequest(**{"header": "projects/sample1/instances/sample2/sample3"})
        # Ensure that the uuid4 field is set according to AIP 4235
        assert _UUID4_RE.fullmatch(args[0].request_id)
        request_msg.request_id = args[0].request_id
        # Ensure that the uuid4 field is set according to AIP 4235
        assert _UUID4_RE.fullmatch(args[0].other_request_id)
        request_msg.other_request_id = args[0].other_request_id
        assert args[0] == request_msg

        expected_headers = {'header': 'projects/sample1/instances/sample2/sample3', 'routing_id': 'projects/sample1/instances/sample2/sample3', 'super_id': 'projects/sample1', 'table_name': 'projects/sample1/instances/sample2/sample3', 'instance_id': 'instances/sample2'}
        assert gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw['metadata']

def test_echo_routing_parameters_request_6_rest():
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.echo),
            '__call__') as call:
        client.echo(request={"header": "projects/sample1/instances/sample2/sample3"})

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = gs_echo.EchoRequest(**{"header": "projects/sample1/instances/sample2/sample3"})
        # Ensure that the uuid4 field is set according to AIP 4235
        assert _UUID4_RE.fullmatch(args[0].request_id)
        request_msg.request_id = args[0].request_id
        # Ensure that the uuid4 field is set according to AIP 4235
        assert _UUID4_RE.fullmatch(args[0].other_request_id)
        request_msg.other_request_id = args[0].other_request_id
        assert args[0] == request_msg

        expected_headers = {'header': 'projects/sample1/instances/sample2/sample3', 'routing_id': 'projects/sample1/instances/sample2/sample3', 'super_id': 'projects/sample1', 'table_name': 'projects/sample1/instances/sample2/sample3', 'instance_id': 'instances/sample2'}
        assert gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw['metadata']

def test_echo_routing_parameters_request_7_rest():
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.echo),
            '__call__') as call:
        client.echo(request={"other_header": "sample1"})

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = gs_echo.EchoRequest(**{"other_header": "sample1"})
        # Ensure that the uuid4 field is set according to AIP 4235
        assert _UUID4_RE.fullmatch(args[0].request_id)
        request_msg.request_id = args[0].request_id
        # Ensure that the uuid4 field is set according to AIP 4235
        assert _UUID4_RE.fullmatch(args[0].other_request_id)
        request_msg.other_request_id = args[0].other_request_id
        assert args[0] == request_msg

        expected_headers = {'baz': 'sample1'}
        assert gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw['metadata']

def test_echo_routing_parameters_request_8_rest():
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.echo),
            '__call__') as call:
        client.echo(request={"other_header": "projects/sample1/sample2"})

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = gs_echo.EchoRequest(**{"other_header": "projects/sample1/sample2"})
        # Ensure that the uuid4 field is set according to AIP 4235
        assert _UUID4_RE.fullmatch(args[0].request_id)
        request_msg.request_id = args[0].request_id
        # Ensure that the uuid4 field is set according to AIP 4235
        assert _UUID4_RE.fullmatch(args[0].other_request_id)
        request_msg.other_request_id = args[0].other_request_id
        assert args[0] == request_msg

        expected_headers = {'baz': 'projects/sample1/sample2', 'qux': 'projects/sample1'}
        assert gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw['metadata']


def test_echo_rest_lro_client():
    client = EchoClient(
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
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    assert isinstance(
        client.transport,
        transports.EchoGrpcTransport,
    )

def test_echo_base_transport_error():
    # Passing both a credentials object and credentials_file should raise an error
    with pytest.raises(core_exceptions.DuplicateCredentialArgs):
        transport = transports.EchoTransport(
            credentials=ga_credentials.AnonymousCredentials(),
            credentials_file="credentials.json"
        )


def test_echo_base_transport():
    # Instantiate the base transport.
    with mock.patch('google.showcase_v1beta1.services.echo.transports.EchoTransport.__init__') as Transport:
        Transport.return_value = None
        transport = transports.EchoTransport(
            credentials=ga_credentials.AnonymousCredentials(),
        )

    # Every method on the transport should just blindly
    # raise NotImplementedError.
    methods = (
        'echo',
        'echo_error_details',
        'fail_echo_with_details',
        'expand',
        'collect',
        'chat',
        'paged_expand',
        'paged_expand_legacy',
        'paged_expand_legacy_mapped',
        'wait',
        'block',
        'set_iam_policy',
        'get_iam_policy',
        'test_iam_permissions',
        'get_location',
        'list_locations',
        'get_operation',
        'cancel_operation',
        'delete_operation',
        'list_operations',
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
        'kind',
    ]
    for r in remainder:
        with pytest.raises(NotImplementedError):
            getattr(transport, r)()


def test_echo_base_transport_with_credentials_file():
    # Instantiate the base transport with a credentials file
    with mock.patch.object(google.auth, 'load_credentials_from_file', autospec=True) as load_creds, mock.patch('google.showcase_v1beta1.services.echo.transports.EchoTransport._prep_wrapped_messages') as Transport:
        Transport.return_value = None
        load_creds.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.EchoTransport(
            credentials_file="credentials.json",
            quota_project_id="octopus",
        )
        load_creds.assert_called_once_with("credentials.json",
            scopes=None,
            default_scopes=(
),
            quota_project_id="octopus",
        )


def test_echo_base_transport_with_adc():
    # Test the default credentials are used if credentials and credentials_file are None.
    with mock.patch.object(google.auth, 'default', autospec=True) as adc, mock.patch('google.showcase_v1beta1.services.echo.transports.EchoTransport._prep_wrapped_messages') as Transport:
        Transport.return_value = None
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.EchoTransport()
        adc.assert_called_once()


def test_echo_auth_adc():
    # If no credentials are provided, we should use ADC credentials.
    with mock.patch.object(google.auth, 'default', autospec=True) as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        EchoClient()
        adc.assert_called_once_with(
            scopes=None,
            default_scopes=(
),
            quota_project_id=None,
        )


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.EchoGrpcTransport,
        transports.EchoGrpcAsyncIOTransport,
    ],
)
def test_echo_transport_auth_adc(transport_class):
    # If credentials and host are not provided, the transport class should use
    # ADC credentials.
    with mock.patch.object(google.auth, 'default', autospec=True) as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport_class(quota_project_id="octopus", scopes=["1", "2"])
        adc.assert_called_once_with(
            scopes=["1", "2"],
            default_scopes=(),
            quota_project_id="octopus",
        )


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.EchoGrpcTransport,
        transports.EchoGrpcAsyncIOTransport,
        transports.EchoRestTransport,
    ],
)
def test_echo_transport_auth_gdch_credentials(transport_class):
    host = 'https://language.com'
    api_audience_tests = [None, 'https://language2.com']
    api_audience_expect = [host, 'https://language2.com']
    for t, e in zip(api_audience_tests, api_audience_expect):
        with mock.patch.object(google.auth, 'default', autospec=True) as adc:
            gdch_mock = mock.MagicMock()
            type(gdch_mock).with_gdch_audience = mock.PropertyMock(return_value=gdch_mock)
            adc.return_value = (gdch_mock, None)
            transport_class(host=host, api_audience=t)
            gdch_mock.with_gdch_audience.assert_called_once_with(
                e
            )


@pytest.mark.parametrize(
    "transport_class,grpc_helpers",
    [
        (transports.EchoGrpcTransport, grpc_helpers),
        (transports.EchoGrpcAsyncIOTransport, grpc_helpers_async)
    ],
)
def test_echo_transport_create_channel(transport_class, grpc_helpers):
    # If credentials and host are not provided, the transport class should use
    # ADC credentials.
    with mock.patch.object(google.auth, "default", autospec=True) as adc, mock.patch.object(
        grpc_helpers, "create_channel", autospec=True
    ) as create_channel:
        creds = ga_credentials.AnonymousCredentials()
        adc.return_value = (creds, None)
        transport_class(
            quota_project_id="octopus",
            scopes=["1", "2"]
        )

        create_channel.assert_called_with(
            "localhost:7469",
            credentials=creds,
            credentials_file=None,
            quota_project_id="octopus",
            default_scopes=(
),
            scopes=["1", "2"],
            default_host="localhost:7469",
            ssl_credentials=None,
            options=[
                ("grpc.max_send_message_length", -1),
                ("grpc.max_receive_message_length", -1),
            ],
        )


@pytest.mark.parametrize("transport_class", [transports.EchoGrpcTransport, transports.EchoGrpcAsyncIOTransport])
def test_echo_grpc_transport_client_cert_source_for_mtls(
    transport_class
):
    cred = ga_credentials.AnonymousCredentials()

    # Check ssl_channel_credentials is used if provided.
    with mock.patch.object(transport_class, "create_channel") as mock_create_channel:
        mock_ssl_channel_creds = mock.Mock()
        transport_class(
            host="squid.clam.whelk",
            credentials=cred,
            ssl_channel_credentials=mock_ssl_channel_creds
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
                client_cert_source_for_mtls=client_cert_source_callback
            )
            expected_cert, expected_key = client_cert_source_callback()
            mock_ssl_cred.assert_called_once_with(
                certificate_chain=expected_cert,
                private_key=expected_key
            )

def test_echo_http_transport_client_cert_source_for_mtls():
    cred = ga_credentials.AnonymousCredentials()
    with mock.patch("google.auth.transport.requests.AuthorizedSession.configure_mtls_channel") as mock_configure_mtls_channel:
        transports.EchoRestTransport (
            credentials=cred,
            client_cert_source_for_mtls=client_cert_source_callback
        )
        mock_configure_mtls_channel.assert_called_once_with(client_cert_source_callback)


@pytest.mark.parametrize("transport_name", [
    "grpc",
    "grpc_asyncio",
    "rest",
])
def test_echo_host_no_port(transport_name):
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(api_endpoint='localhost'),
         transport=transport_name,
    )
    assert client.transport._host == (
        'localhost:443'
        if transport_name in ['grpc', 'grpc_asyncio']
        else 'https://localhost'
    )

@pytest.mark.parametrize("transport_name", [
    "grpc",
    "grpc_asyncio",
    "rest",
])
def test_echo_host_with_port(transport_name):
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(api_endpoint='localhost:8000'),
        transport=transport_name,
    )
    assert client.transport._host == (
        'localhost:8000'
        if transport_name in ['grpc', 'grpc_asyncio']
        else 'https://localhost:8000'
    )

@pytest.mark.parametrize("transport_name", [
    "rest",
])
def test_echo_client_transport_session_collision(transport_name):
    creds1 = ga_credentials.AnonymousCredentials()
    creds2 = ga_credentials.AnonymousCredentials()
    client1 = EchoClient(
        credentials=creds1,
        transport=transport_name,
    )
    client2 = EchoClient(
        credentials=creds2,
        transport=transport_name,
    )
    session1 = client1.transport.echo._session
    session2 = client2.transport.echo._session
    assert session1 != session2
    session1 = client1.transport.echo_error_details._session
    session2 = client2.transport.echo_error_details._session
    assert session1 != session2
    session1 = client1.transport.fail_echo_with_details._session
    session2 = client2.transport.fail_echo_with_details._session
    assert session1 != session2
    session1 = client1.transport.expand._session
    session2 = client2.transport.expand._session
    assert session1 != session2
    session1 = client1.transport.collect._session
    session2 = client2.transport.collect._session
    assert session1 != session2
    session1 = client1.transport.chat._session
    session2 = client2.transport.chat._session
    assert session1 != session2
    session1 = client1.transport.paged_expand._session
    session2 = client2.transport.paged_expand._session
    assert session1 != session2
    session1 = client1.transport.paged_expand_legacy._session
    session2 = client2.transport.paged_expand_legacy._session
    assert session1 != session2
    session1 = client1.transport.paged_expand_legacy_mapped._session
    session2 = client2.transport.paged_expand_legacy_mapped._session
    assert session1 != session2
    session1 = client1.transport.wait._session
    session2 = client2.transport.wait._session
    assert session1 != session2
    session1 = client1.transport.block._session
    session2 = client2.transport.block._session
    assert session1 != session2
def test_echo_grpc_transport_channel():
    channel = grpc.secure_channel('http://localhost/', grpc.local_channel_credentials())

    # Check that channel is used if provided.
    transport = transports.EchoGrpcTransport(
        host="squid.clam.whelk",
        channel=channel,
    )
    assert transport.grpc_channel == channel
    assert transport._host == "squid.clam.whelk:443"
    assert transport._ssl_channel_credentials == None


def test_echo_grpc_asyncio_transport_channel():
    channel = aio.secure_channel('http://localhost/', grpc.local_channel_credentials())

    # Check that channel is used if provided.
    transport = transports.EchoGrpcAsyncIOTransport(
        host="squid.clam.whelk",
        channel=channel,
    )
    assert transport.grpc_channel == channel
    assert transport._host == "squid.clam.whelk:443"
    assert transport._ssl_channel_credentials == None


# Remove this test when deprecated arguments (api_mtls_endpoint, client_cert_source) are
# removed from grpc/grpc_asyncio transport constructor.
@pytest.mark.filterwarnings("ignore::FutureWarning")
@pytest.mark.parametrize("transport_class", [transports.EchoGrpcTransport, transports.EchoGrpcAsyncIOTransport])
def test_echo_transport_channel_mtls_with_client_cert_source(
    transport_class
):
    with mock.patch("grpc.ssl_channel_credentials", autospec=True) as grpc_ssl_channel_cred:
        with mock.patch.object(transport_class, "create_channel") as grpc_create_channel:
            mock_ssl_cred = mock.Mock()
            grpc_ssl_channel_cred.return_value = mock_ssl_cred

            mock_grpc_channel = mock.Mock()
            grpc_create_channel.return_value = mock_grpc_channel

            cred = ga_credentials.AnonymousCredentials()
            with pytest.warns(DeprecationWarning):
                with mock.patch.object(google.auth, 'default') as adc:
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
@pytest.mark.parametrize("transport_class", [transports.EchoGrpcTransport, transports.EchoGrpcAsyncIOTransport])
def test_echo_transport_channel_mtls_with_adc(
    transport_class
):
    mock_ssl_cred = mock.Mock()
    with mock.patch.multiple(
        "google.auth.transport.grpc.SslCredentials",
        __init__=mock.Mock(return_value=None),
        ssl_credentials=mock.PropertyMock(return_value=mock_ssl_cred),
    ):
        with mock.patch.object(transport_class, "create_channel") as grpc_create_channel:
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


def test_echo_grpc_lro_client():
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='grpc',
    )
    transport = client.transport

    # Ensure that we have a api-core operations client.
    assert isinstance(
        transport.operations_client,
        operations_v1.OperationsClient,
    )

    # Ensure that subsequent calls to the property send the exact same object.
    assert transport.operations_client is transport.operations_client


def test_echo_grpc_lro_async_client():
    client = EchoAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='grpc_asyncio',
    )
    transport = client.transport

    # Ensure that we have a api-core operations client.
    assert isinstance(
        transport.operations_client,
        operations_v1.OperationsAsyncClient,
    )

    # Ensure that subsequent calls to the property send the exact same object.
    assert transport.operations_client is transport.operations_client


def test_common_billing_account_path():
    billing_account = "squid"
    expected = "billingAccounts/{billing_account}".format(billing_account=billing_account, )
    actual = EchoClient.common_billing_account_path(billing_account)
    assert expected == actual


def test_parse_common_billing_account_path():
    expected = {
        "billing_account": "clam",
    }
    path = EchoClient.common_billing_account_path(**expected)

    # Check that the path construction is reversible.
    actual = EchoClient.parse_common_billing_account_path(path)
    assert expected == actual

def test_common_folder_path():
    folder = "whelk"
    expected = "folders/{folder}".format(folder=folder, )
    actual = EchoClient.common_folder_path(folder)
    assert expected == actual


def test_parse_common_folder_path():
    expected = {
        "folder": "octopus",
    }
    path = EchoClient.common_folder_path(**expected)

    # Check that the path construction is reversible.
    actual = EchoClient.parse_common_folder_path(path)
    assert expected == actual

def test_common_organization_path():
    organization = "oyster"
    expected = "organizations/{organization}".format(organization=organization, )
    actual = EchoClient.common_organization_path(organization)
    assert expected == actual


def test_parse_common_organization_path():
    expected = {
        "organization": "nudibranch",
    }
    path = EchoClient.common_organization_path(**expected)

    # Check that the path construction is reversible.
    actual = EchoClient.parse_common_organization_path(path)
    assert expected == actual

def test_common_project_path():
    project = "cuttlefish"
    expected = "projects/{project}".format(project=project, )
    actual = EchoClient.common_project_path(project)
    assert expected == actual


def test_parse_common_project_path():
    expected = {
        "project": "mussel",
    }
    path = EchoClient.common_project_path(**expected)

    # Check that the path construction is reversible.
    actual = EchoClient.parse_common_project_path(path)
    assert expected == actual

def test_common_location_path():
    project = "winkle"
    location = "nautilus"
    expected = "projects/{project}/locations/{location}".format(project=project, location=location, )
    actual = EchoClient.common_location_path(project, location)
    assert expected == actual


def test_parse_common_location_path():
    expected = {
        "project": "scallop",
        "location": "abalone",
    }
    path = EchoClient.common_location_path(**expected)

    # Check that the path construction is reversible.
    actual = EchoClient.parse_common_location_path(path)
    assert expected == actual


def test_client_with_default_client_info():
    client_info = gapic_v1.client_info.ClientInfo()

    with mock.patch.object(transports.EchoTransport, '_prep_wrapped_messages') as prep:
        client = EchoClient(
            credentials=ga_credentials.AnonymousCredentials(),
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)

    with mock.patch.object(transports.EchoTransport, '_prep_wrapped_messages') as prep:
        transport_class = EchoClient.get_transport_class()
        transport = transport_class(
            credentials=ga_credentials.AnonymousCredentials(),
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)


def test_delete_operation(transport: str = "grpc"):
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
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
    client = EchoAsyncClient(
        credentials=async_anonymous_credentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = operations_pb2.DeleteOperationRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_operation), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            None
        )
        response = await client.delete_operation(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert response is None


def test_delete_operation_field_headers():
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = operations_pb2.DeleteOperationRequest()
    request.name = "locations"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_operation), "__call__") as call:
        call.return_value =  None

        client.delete_operation(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=locations",) in kw["metadata"]

@pytest.mark.asyncio
async def test_delete_operation_field_headers_async():
    client = EchoAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = operations_pb2.DeleteOperationRequest()
    request.name = "locations"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_operation), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            None
        )
        await client.delete_operation(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=locations",) in kw["metadata"]


def test_delete_operation_from_dict():
    client = EchoClient(
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
    client = EchoAsyncClient(
        credentials=async_anonymous_credentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_operation), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            None
        )
        response = await client.delete_operation(
            request={
                "name": "locations",
            }
        )
        call.assert_called()


def test_delete_operation_flattened():
    client = EchoClient(
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
    client = EchoAsyncClient(
        credentials=async_anonymous_credentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_operation), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            None
        )
        await client.delete_operation()
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == operations_pb2.DeleteOperationRequest()


def test_cancel_operation(transport: str = "grpc"):
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
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
    client = EchoAsyncClient(
        credentials=async_anonymous_credentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = operations_pb2.CancelOperationRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.cancel_operation), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            None
        )
        response = await client.cancel_operation(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert response is None


def test_cancel_operation_field_headers():
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = operations_pb2.CancelOperationRequest()
    request.name = "locations"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.cancel_operation), "__call__") as call:
        call.return_value =  None

        client.cancel_operation(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=locations",) in kw["metadata"]

@pytest.mark.asyncio
async def test_cancel_operation_field_headers_async():
    client = EchoAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = operations_pb2.CancelOperationRequest()
    request.name = "locations"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.cancel_operation), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            None
        )
        await client.cancel_operation(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=locations",) in kw["metadata"]


def test_cancel_operation_from_dict():
    client = EchoClient(
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
    client = EchoAsyncClient(
        credentials=async_anonymous_credentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.cancel_operation), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            None
        )
        response = await client.cancel_operation(
            request={
                "name": "locations",
            }
        )
        call.assert_called()


def test_cancel_operation_flattened():
    client = EchoClient(
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
    client = EchoAsyncClient(
        credentials=async_anonymous_credentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.cancel_operation), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            None
        )
        await client.cancel_operation()
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == operations_pb2.CancelOperationRequest()


def test_get_operation(transport: str = "grpc"):
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
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
    client = EchoAsyncClient(
        credentials=async_anonymous_credentials(), transport=transport,
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
    client = EchoClient(
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
    assert ("x-goog-request-params", "name=locations",) in kw["metadata"]

@pytest.mark.asyncio
async def test_get_operation_field_headers_async():
    client = EchoAsyncClient(
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
    assert ("x-goog-request-params", "name=locations",) in kw["metadata"]


def test_get_operation_from_dict():
    client = EchoClient(
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
    client = EchoAsyncClient(
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
    client = EchoClient(
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
    client = EchoAsyncClient(
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
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
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
    client = EchoAsyncClient(
        credentials=async_anonymous_credentials(), transport=transport,
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
    client = EchoClient(
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
    assert ("x-goog-request-params", "name=locations",) in kw["metadata"]

@pytest.mark.asyncio
async def test_list_operations_field_headers_async():
    client = EchoAsyncClient(
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
    assert ("x-goog-request-params", "name=locations",) in kw["metadata"]


def test_list_operations_from_dict():
    client = EchoClient(
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
    client = EchoAsyncClient(
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
    client = EchoClient(
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
    client = EchoAsyncClient(
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


def test_list_locations(transport: str = "grpc"):
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = locations_pb2.ListLocationsRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_locations), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = locations_pb2.ListLocationsResponse()
        response = client.list_locations(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, locations_pb2.ListLocationsResponse)

@pytest.mark.asyncio
async def test_list_locations_async(transport: str = "grpc_asyncio"):
    client = EchoAsyncClient(
        credentials=async_anonymous_credentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = locations_pb2.ListLocationsRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_locations), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            locations_pb2.ListLocationsResponse()
        )
        response = await client.list_locations(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, locations_pb2.ListLocationsResponse)


def test_list_locations_field_headers():
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = locations_pb2.ListLocationsRequest()
    request.name = "locations"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_locations), "__call__") as call:
        call.return_value = locations_pb2.ListLocationsResponse()

        client.list_locations(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=locations",) in kw["metadata"]

@pytest.mark.asyncio
async def test_list_locations_field_headers_async():
    client = EchoAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = locations_pb2.ListLocationsRequest()
    request.name = "locations"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_locations), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            locations_pb2.ListLocationsResponse()
        )
        await client.list_locations(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=locations",) in kw["metadata"]


def test_list_locations_from_dict():
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_locations), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = locations_pb2.ListLocationsResponse()

        response = client.list_locations(
            request={
                "name": "locations",
            }
        )
        call.assert_called()

@pytest.mark.asyncio
async def test_list_locations_from_dict_async():
    client = EchoAsyncClient(
        credentials=async_anonymous_credentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_locations), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            locations_pb2.ListLocationsResponse()
        )
        response = await client.list_locations(
            request={
                "name": "locations",
            }
        )
        call.assert_called()


def test_list_locations_flattened():
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_locations), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = locations_pb2.ListLocationsResponse()

        client.list_locations()
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == locations_pb2.ListLocationsRequest()

@pytest.mark.asyncio
async def test_list_locations_flattened_async():
    client = EchoAsyncClient(
        credentials=async_anonymous_credentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_locations), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            locations_pb2.ListLocationsResponse()
        )
        await client.list_locations()
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == locations_pb2.ListLocationsRequest()


def test_get_location(transport: str = "grpc"):
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = locations_pb2.GetLocationRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_location), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = locations_pb2.Location()
        response = client.get_location(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, locations_pb2.Location)

@pytest.mark.asyncio
async def test_get_location_async(transport: str = "grpc_asyncio"):
    client = EchoAsyncClient(
        credentials=async_anonymous_credentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = locations_pb2.GetLocationRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_location), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            locations_pb2.Location()
        )
        response = await client.get_location(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, locations_pb2.Location)


def test_get_location_field_headers():
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials())

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = locations_pb2.GetLocationRequest()
    request.name = "locations/abc"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_location), "__call__") as call:
        call.return_value = locations_pb2.Location()

        client.get_location(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=locations/abc",) in kw["metadata"]

@pytest.mark.asyncio
async def test_get_location_field_headers_async():
    client = EchoAsyncClient(
        credentials=async_anonymous_credentials()
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = locations_pb2.GetLocationRequest()
    request.name = "locations/abc"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_location), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            locations_pb2.Location()
        )
        await client.get_location(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=locations/abc",) in kw["metadata"]


def test_get_location_from_dict():
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_locations), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = locations_pb2.Location()

        response = client.get_location(
            request={
                "name": "locations/abc",
            }
        )
        call.assert_called()

@pytest.mark.asyncio
async def test_get_location_from_dict_async():
    client = EchoAsyncClient(
        credentials=async_anonymous_credentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_locations), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            locations_pb2.Location()
        )
        response = await client.get_location(
            request={
                "name": "locations",
            }
        )
        call.assert_called()


def test_get_location_flattened():
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_location), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = locations_pb2.Location()

        client.get_location()
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == locations_pb2.GetLocationRequest()

@pytest.mark.asyncio
async def test_get_location_flattened_async():
    client = EchoAsyncClient(
        credentials=async_anonymous_credentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_location), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            locations_pb2.Location()
        )
        await client.get_location()
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == locations_pb2.GetLocationRequest()


def test_set_iam_policy(transport: str = "grpc"):
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = iam_policy_pb2.SetIamPolicyRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.set_iam_policy), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = policy_pb2.Policy(version=774, etag=b"etag_blob",)
        response = client.set_iam_policy(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, policy_pb2.Policy)

    assert response.version == 774

    assert response.etag == b"etag_blob"

@pytest.mark.asyncio
async def test_set_iam_policy_async(transport: str = "grpc_asyncio"):
    client = EchoAsyncClient(
        credentials=async_anonymous_credentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = iam_policy_pb2.SetIamPolicyRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.set_iam_policy), "__call__") as call:
        # Designate an appropriate return value for the call.
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            policy_pb2.Policy(version=774, etag=b"etag_blob",)
        )
        response = await client.set_iam_policy(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, policy_pb2.Policy)

    assert response.version == 774

    assert response.etag == b"etag_blob"


def test_set_iam_policy_field_headers():
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = iam_policy_pb2.SetIamPolicyRequest()
    request.resource = "resource/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.set_iam_policy), "__call__") as call:
        call.return_value = policy_pb2.Policy()

        client.set_iam_policy(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "resource=resource/value",) in kw["metadata"]

@pytest.mark.asyncio
async def test_set_iam_policy_field_headers_async():
    client = EchoAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = iam_policy_pb2.SetIamPolicyRequest()
    request.resource = "resource/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.set_iam_policy), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(policy_pb2.Policy())

        await client.set_iam_policy(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "resource=resource/value",) in kw["metadata"]


def test_set_iam_policy_from_dict():
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.set_iam_policy), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = policy_pb2.Policy()

        response = client.set_iam_policy(
            request={
                "resource": "resource_value",
                "policy": policy_pb2.Policy(version=774),
            }
        )
        call.assert_called()


@pytest.mark.asyncio
async def test_set_iam_policy_from_dict_async():
    client = EchoAsyncClient(
        credentials=async_anonymous_credentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.set_iam_policy), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            policy_pb2.Policy()
        )

        response = await client.set_iam_policy(
            request={
                "resource": "resource_value",
                "policy": policy_pb2.Policy(version=774),
            }
        )
        call.assert_called()


def test_set_iam_policy_flattened():
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.set_iam_policy), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = policy_pb2.Policy()

        client.set_iam_policy()

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == iam_policy_pb2.SetIamPolicyRequest()


@pytest.mark.asyncio
async def test_set_iam_policy_flattened_async():
    client = EchoAsyncClient(
        credentials=async_anonymous_credentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.set_iam_policy), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            policy_pb2.Policy()
        )

        await client.set_iam_policy()

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == iam_policy_pb2.SetIamPolicyRequest()

def test_get_iam_policy(transport: str = "grpc"):
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = iam_policy_pb2.GetIamPolicyRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_iam_policy), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = policy_pb2.Policy(version=774, etag=b"etag_blob",)

        response = client.get_iam_policy(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, policy_pb2.Policy)

    assert response.version == 774

    assert response.etag == b"etag_blob"


@pytest.mark.asyncio
async def test_get_iam_policy_async(transport: str = "grpc_asyncio"):
    client = EchoAsyncClient(
        credentials=async_anonymous_credentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = iam_policy_pb2.GetIamPolicyRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_iam_policy), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            policy_pb2.Policy(version=774, etag=b"etag_blob",)
        )

        response = await client.get_iam_policy(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, policy_pb2.Policy)

    assert response.version == 774

    assert response.etag == b"etag_blob"


def test_get_iam_policy_field_headers():
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = iam_policy_pb2.GetIamPolicyRequest()
    request.resource = "resource/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_iam_policy), "__call__") as call:
        call.return_value = policy_pb2.Policy()

        client.get_iam_policy(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "resource=resource/value",) in kw["metadata"]


@pytest.mark.asyncio
async def test_get_iam_policy_field_headers_async():
    client = EchoAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = iam_policy_pb2.GetIamPolicyRequest()
    request.resource = "resource/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_iam_policy), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(policy_pb2.Policy())

        await client.get_iam_policy(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "resource=resource/value",) in kw["metadata"]


def test_get_iam_policy_from_dict():
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_iam_policy), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = policy_pb2.Policy()

        response = client.get_iam_policy(
            request={
                "resource": "resource_value",
                "options": options_pb2.GetPolicyOptions(requested_policy_version=2598),
            }
        )
        call.assert_called()

@pytest.mark.asyncio
async def test_get_iam_policy_from_dict_async():
    client = EchoAsyncClient(
        credentials=async_anonymous_credentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_iam_policy), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            policy_pb2.Policy()
        )

        response = await client.get_iam_policy(
            request={
                "resource": "resource_value",
                "options": options_pb2.GetPolicyOptions(requested_policy_version=2598),
            }
        )
        call.assert_called()


def test_get_iam_policy_flattened():
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_iam_policy), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = policy_pb2.Policy()

        client.get_iam_policy()

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == iam_policy_pb2.GetIamPolicyRequest()


@pytest.mark.asyncio
async def test_get_iam_policy_flattened_async():
    client = EchoAsyncClient(
        credentials=async_anonymous_credentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_iam_policy), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            policy_pb2.Policy()
        )

        await client.get_iam_policy()

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == iam_policy_pb2.GetIamPolicyRequest()

def test_test_iam_permissions(transport: str = "grpc"):
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = iam_policy_pb2.TestIamPermissionsRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.test_iam_permissions), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = iam_policy_pb2.TestIamPermissionsResponse(
            permissions=["permissions_value"],
        )

        response = client.test_iam_permissions(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, iam_policy_pb2.TestIamPermissionsResponse)

    assert response.permissions == ["permissions_value"]


@pytest.mark.asyncio
async def test_test_iam_permissions_async(transport: str = "grpc_asyncio"):
    client = EchoAsyncClient(
        credentials=async_anonymous_credentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = iam_policy_pb2.TestIamPermissionsRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.test_iam_permissions), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            iam_policy_pb2.TestIamPermissionsResponse(permissions=["permissions_value"],)
        )

        response = await client.test_iam_permissions(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, iam_policy_pb2.TestIamPermissionsResponse)

    assert response.permissions == ["permissions_value"]


def test_test_iam_permissions_field_headers():
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = iam_policy_pb2.TestIamPermissionsRequest()
    request.resource = "resource/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.test_iam_permissions), "__call__"
    ) as call:
        call.return_value = iam_policy_pb2.TestIamPermissionsResponse()

        client.test_iam_permissions(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "resource=resource/value",) in kw["metadata"]


@pytest.mark.asyncio
async def test_test_iam_permissions_field_headers_async():
    client = EchoAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = iam_policy_pb2.TestIamPermissionsRequest()
    request.resource = "resource/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.test_iam_permissions), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            iam_policy_pb2.TestIamPermissionsResponse()
        )

        await client.test_iam_permissions(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "resource=resource/value",) in kw["metadata"]


def test_test_iam_permissions_from_dict():
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.test_iam_permissions), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = iam_policy_pb2.TestIamPermissionsResponse()

        response = client.test_iam_permissions(
            request={
                "resource": "resource_value",
                "permissions": ["permissions_value"],
            }
        )
        call.assert_called()

@pytest.mark.asyncio
async def test_test_iam_permissions_from_dict_async():
    client = EchoAsyncClient(
        credentials=async_anonymous_credentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.test_iam_permissions), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            iam_policy_pb2.TestIamPermissionsResponse()
        )

        response = await client.test_iam_permissions(
            request={
                "resource": "resource_value",
                "permissions": ["permissions_value"],
            }
        )
        call.assert_called()


def test_test_iam_permissions_flattened():
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.test_iam_permissions), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = iam_policy_pb2.TestIamPermissionsResponse()

        client.test_iam_permissions()

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == iam_policy_pb2.TestIamPermissionsRequest()


@pytest.mark.asyncio
async def test_test_iam_permissions_flattened_async():
    client = EchoAsyncClient(
        credentials=async_anonymous_credentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.test_iam_permissions), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            iam_policy_pb2.TestIamPermissionsResponse()
        )

        await client.test_iam_permissions()

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == iam_policy_pb2.TestIamPermissionsRequest()


def test_transport_close_grpc():
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc"
    )
    with mock.patch.object(type(getattr(client.transport, "_grpc_channel")), "close") as close:
        with client:
            close.assert_not_called()
        close.assert_called_once()


@pytest.mark.asyncio
async def test_transport_close_grpc_asyncio():
    client = EchoAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio"
    )
    with mock.patch.object(type(getattr(client.transport, "_grpc_channel")), "close") as close:
        async with client:
            close.assert_not_called()
        close.assert_called_once()


def test_transport_close_rest():
    client = EchoClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest"
    )
    with mock.patch.object(type(getattr(client.transport, "_session")), "close") as close:
        with client:
            close.assert_not_called()
        close.assert_called_once()


def test_client_ctx():
    transports = [
        'rest',
        'grpc',
    ]
    for transport in transports:
        client = EchoClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport=transport
        )
        # Test client calls underlying transport.
        with mock.patch.object(type(client.transport), "close") as close:
            close.assert_not_called()
            with client:
                pass
            close.assert_called()

@pytest.mark.parametrize("client_class,transport_class", [
    (EchoClient, transports.EchoGrpcTransport),
    (EchoAsyncClient, transports.EchoGrpcAsyncIOTransport),
])
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
                host=client._DEFAULT_ENDPOINT_TEMPLATE.format(UNIVERSE_DOMAIN=client._DEFAULT_UNIVERSE),
                scopes=None,
                client_cert_source_for_mtls=None,
                quota_project_id=None,
                client_info=transports.base.DEFAULT_CLIENT_INFO,
                always_use_jwt_access=True,
                api_audience=None,
            )


def test_echo_base_transport_wrap_method_modern_api_core(monkeypatch):
    monkeypatch.setattr(transports.base, "_WRAP_METHOD_SUPPORTS_TRACING", True)
    # 1. Concrete transport: passes client_options=None and kind="grpc"
    with mock.patch.object(transports.base.gapic_v1.method, "wrap_method") as mock_wrap:
        transport = transports.EchoGrpcTransport(
            credentials=ga_credentials.AnonymousCredentials()
        )
        func = mock.MagicMock()
        transport._wrap_method(func)
        assert mock_wrap.call_args.kwargs["kind"] == "grpc"
        assert "client_options" in mock_wrap.call_args.kwargs

    # 2. Base transport: kind raises NotImplementedError and is cleanly omitted
    with mock.patch.object(transports.base.gapic_v1.method, "wrap_method") as mock_wrap:
        base_transport = transports.EchoTransport(
            credentials=ga_credentials.AnonymousCredentials()
        )
        func = mock.MagicMock()
        base_transport._wrap_method(func)
        assert "kind" not in mock_wrap.call_args.kwargs
        assert "client_options" in mock_wrap.call_args.kwargs


def test_echo_base_transport_wrap_method_older_api_core_fallbacks(monkeypatch):
    monkeypatch.setattr(transports.base, "_WRAP_METHOD_SUPPORTS_TRACING", False)
    with mock.patch.object(transports.base.gapic_v1.method, "wrap_method"):
        transport = transports.EchoGrpcTransport(
            credentials=ga_credentials.AnonymousCredentials()
        )

    # Era 1: Ancient google-api-core (< 2.29.0: can be removed once google-api-core < 2.29.0 is no longer supported)
    monkeypatch.setattr(transports.base, "_WRAP_METHOD_SUPPORTS_KIND", False)
    with mock.patch.object(transports.base.gapic_v1.method, "wrap_method") as mock_wrap:
        func = mock.MagicMock()
        transport._wrap_method(
            func,
            client_options="fake_options",
            method_name="fake_method",
            is_streaming=False,
        )
        kwargs = mock_wrap.call_args.kwargs
        assert "kind" not in kwargs
        assert "client_options" not in kwargs
        assert "method_name" not in kwargs
        assert "is_streaming" not in kwargs

    with mock.patch.object(transports.base.gapic_v1.method, "wrap_method") as mock_wrap:
        base_transport = transports.EchoTransport(
            credentials=ga_credentials.AnonymousCredentials()
        )
        func = mock.MagicMock()
        base_transport._wrap_method(
            func,
            client_options="fake_options",
            method_name="fake_method",
            is_streaming=False,
        )
        kwargs = mock_wrap.call_args.kwargs
        assert "kind" not in kwargs
        assert "client_options" not in kwargs
        assert "method_name" not in kwargs
        assert "is_streaming" not in kwargs

    # Era 2: Intermediate google-api-core (>= 2.29.0, < 2.36.0: can be removed once google-api-core < 2.36.0 is no longer supported)
    monkeypatch.setattr(transports.base, "_WRAP_METHOD_SUPPORTS_KIND", True)
    with mock.patch.object(transports.base.gapic_v1.method, "wrap_method") as mock_wrap:
        func = mock.MagicMock()
        transport._wrap_method(
            func,
            client_options="fake_options",
            method_name="fake_method",
            is_streaming=False,
        )
        kwargs = mock_wrap.call_args.kwargs
        assert kwargs.get("kind") == "grpc"
        assert "client_options" not in kwargs
        assert "method_name" not in kwargs
        assert "is_streaming" not in kwargs

    with mock.patch.object(transports.base.gapic_v1.method, "wrap_method") as mock_wrap:
        base_transport = transports.EchoTransport(
            credentials=ga_credentials.AnonymousCredentials()
        )
        func = mock.MagicMock()
        base_transport._wrap_method(
            func,
            client_options="fake_options",
            method_name="fake_method",
            is_streaming=False,
        )
        kwargs = mock_wrap.call_args.kwargs
        assert "kind" not in kwargs
        assert "client_options" not in kwargs
        assert "method_name" not in kwargs
        assert "is_streaming" not in kwargs


def test_echo_base_transport_wrap_async_method_modern_api_core(monkeypatch):
    monkeypatch.setattr(transports.base, "_ASYNC_WRAP_METHOD_SUPPORTS_TRACING", True)
    # 1. Concrete transport: passes client_options=None and kind="grpc_asyncio"
    with mock.patch.object(transports.base.gapic_v1.method_async, "wrap_method") as mock_wrap:
        transport = transports.EchoGrpcAsyncIOTransport(
            credentials=ga_credentials.AnonymousCredentials()
        )
        func = mock.MagicMock()
        transport._wrap_async_method(func)
        assert mock_wrap.call_args.kwargs["kind"] == "grpc_asyncio"
        assert "client_options" in mock_wrap.call_args.kwargs

    # 2. Base transport: kind raises NotImplementedError and is cleanly omitted
    with mock.patch.object(transports.base.gapic_v1.method_async, "wrap_method") as mock_wrap:
        base_transport = transports.EchoTransport(
            credentials=ga_credentials.AnonymousCredentials()
        )
        func = mock.MagicMock()
        base_transport._wrap_async_method(func)
        assert "kind" not in mock_wrap.call_args.kwargs
        assert "client_options" in mock_wrap.call_args.kwargs


def test_echo_base_transport_wrap_async_method_older_api_core_fallbacks(monkeypatch):
    monkeypatch.setattr(transports.base, "_ASYNC_WRAP_METHOD_SUPPORTS_TRACING", False)
    with mock.patch.object(transports.base.gapic_v1.method_async, "wrap_method"):
        transport = transports.EchoGrpcAsyncIOTransport(
            credentials=ga_credentials.AnonymousCredentials()
        )

    # Era 1: Ancient google-api-core (< 2.29.0: can be removed once google-api-core < 2.29.0 is no longer supported)
    monkeypatch.setattr(transports.base, "_ASYNC_WRAP_METHOD_SUPPORTS_KIND", False)
    with mock.patch.object(transports.base.gapic_v1.method_async, "wrap_method") as mock_wrap:
        func = mock.MagicMock()
        transport._wrap_async_method(
            func,
            client_options="fake_options",
            method_name="fake_method",
            is_streaming=False,
        )
        kwargs = mock_wrap.call_args.kwargs
        assert "kind" not in kwargs
        assert "client_options" not in kwargs
        assert "method_name" not in kwargs
        assert "is_streaming" not in kwargs

    with mock.patch.object(transports.base.gapic_v1.method_async, "wrap_method") as mock_wrap:
        base_transport = transports.EchoTransport(
            credentials=ga_credentials.AnonymousCredentials()
        )
        func = mock.MagicMock()
        base_transport._wrap_async_method(
            func,
            client_options="fake_options",
            method_name="fake_method",
            is_streaming=False,
        )
        kwargs = mock_wrap.call_args.kwargs
        assert "kind" not in kwargs
        assert "client_options" not in kwargs
        assert "method_name" not in kwargs
        assert "is_streaming" not in kwargs

    # Era 2: Intermediate google-api-core (>= 2.29.0, < 2.36.0: can be removed once google-api-core < 2.36.0 is no longer supported)
    monkeypatch.setattr(transports.base, "_ASYNC_WRAP_METHOD_SUPPORTS_KIND", True)
    with mock.patch.object(transports.base.gapic_v1.method_async, "wrap_method") as mock_wrap:
        func = mock.MagicMock()
        transport._wrap_async_method(
            func,
            client_options="fake_options",
            method_name="fake_method",
            is_streaming=False,
        )
        kwargs = mock_wrap.call_args.kwargs
        assert kwargs.get("kind") == "grpc_asyncio"
        assert "client_options" not in kwargs
        assert "method_name" not in kwargs
        assert "is_streaming" not in kwargs

    with mock.patch.object(transports.base.gapic_v1.method_async, "wrap_method") as mock_wrap:
        base_transport = transports.EchoTransport(
            credentials=ga_credentials.AnonymousCredentials()
        )
        func = mock.MagicMock()
        base_transport._wrap_async_method(
            func,
            client_options="fake_options",
            method_name="fake_method",
            is_streaming=False,
        )
        kwargs = mock_wrap.call_args.kwargs
        assert "kind" not in kwargs
        assert "client_options" not in kwargs
        assert "method_name" not in kwargs
        assert "is_streaming" not in kwargs
