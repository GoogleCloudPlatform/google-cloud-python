# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
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

try:
    from unittest import mock
    from unittest.mock import AsyncMock  # pragma: NO COVER  # noqa: F401
except ImportError:  # pragma: NO COVER
    import mock  # type: ignore

from typing import Any, List

import pytest

from ...helpers import warn_deprecated_credentials_file

try:
    import grpc  # noqa: F401
except ImportError:  # pragma: NO COVER
    pytest.skip("No GRPC", allow_module_level=True)
from requests import Response  # noqa I201
from google.auth.transport.requests import AuthorizedSession

from google.api_core import client_options
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import parse_version_to_tuple
from google.api_core.operations_v1 import AbstractOperationsClient

import google.auth
from google.api_core.operations_v1 import pagers
from google.api_core.operations_v1 import pagers_async
from google.api_core.operations_v1 import transports
from google.auth import credentials as ga_credentials
from google.auth import __version__ as auth_version
from google.auth.exceptions import MutualTLSChannelError
from google.longrunning import operations_pb2
from google.oauth2 import service_account
from google.protobuf import json_format  # type: ignore
from google.rpc import status_pb2  # type: ignore

try:
    import aiohttp  # noqa: F401
    import google.auth.aio.transport
    from google.auth.aio import credentials as ga_credentials_async
    from google.auth.aio.transport.sessions import AsyncAuthorizedSession

    from google.api_core.operations_v1 import AsyncOperationsRestClient

    GOOGLE_AUTH_AIO_INSTALLED = True
except ImportError:
    GOOGLE_AUTH_AIO_INSTALLED = False

HTTP_OPTIONS = {
    "google.longrunning.Operations.CancelOperation": [
        {"method": "post", "uri": "/v3/{name=operations/*}:cancel", "body": "*"},
    ],
    "google.longrunning.Operations.DeleteOperation": [
        {"method": "delete", "uri": "/v3/{name=operations/*}"},
    ],
    "google.longrunning.Operations.GetOperation": [
        {"method": "get", "uri": "/v3/{name=operations/*}"},
    ],
    "google.longrunning.Operations.ListOperations": [
        {"method": "get", "uri": "/v3/{name=operations}"},
    ],
}

PYPARAM_CLIENT: List[Any] = [
    AbstractOperationsClient,
]
PYPARAM_CLIENT_TRANSPORT_NAME = [
    [AbstractOperationsClient, transports.OperationsRestTransport, "rest"],
]
PYPARAM_CLIENT_TRANSPORT_CREDENTIALS = [
    [
        AbstractOperationsClient,
        transports.OperationsRestTransport,
        ga_credentials.AnonymousCredentials(),
    ],
]

if GOOGLE_AUTH_AIO_INSTALLED:
    PYPARAM_CLIENT.append(AsyncOperationsRestClient)
    PYPARAM_CLIENT_TRANSPORT_NAME.append(
        [
            AsyncOperationsRestClient,
            transports.AsyncOperationsRestTransport,
            "rest_asyncio",
        ]
    )
    PYPARAM_CLIENT_TRANSPORT_CREDENTIALS.append(
        [
            AsyncOperationsRestClient,
            transports.AsyncOperationsRestTransport,
            ga_credentials_async.AnonymousCredentials(),
        ]
    )


def client_cert_source_callback():
    return b"cert bytes", b"key bytes"


def _get_session_type(is_async: bool):
    return (
        AsyncAuthorizedSession
        if is_async and GOOGLE_AUTH_AIO_INSTALLED
        else AuthorizedSession
    )


def _get_operations_client(is_async: bool, http_options=HTTP_OPTIONS):
    if is_async and GOOGLE_AUTH_AIO_INSTALLED:
        async_transport = transports.rest_asyncio.AsyncOperationsRestTransport(
            credentials=ga_credentials_async.AnonymousCredentials(),
            http_options=http_options,
        )
        return AsyncOperationsRestClient(transport=async_transport)
    else:
        sync_transport = transports.rest.OperationsRestTransport(
            credentials=ga_credentials.AnonymousCredentials(), http_options=http_options
        )
        return AbstractOperationsClient(transport=sync_transport)


# If default endpoint is localhost, then default mtls endpoint will be the same.
# This method modifies the default endpoint so the client can produce a different
# mtls endpoint for endpoint testing purposes.
def modify_default_endpoint(client):
    return (
        "foo.googleapis.com"
        if ("localhost" in client.DEFAULT_ENDPOINT)
        else client.DEFAULT_ENDPOINT
    )


# TODO: Add support for mtls in async rest
@pytest.mark.parametrize(
    "client_class",
    [
        AbstractOperationsClient,
    ],
)
def test__get_default_mtls_endpoint(client_class):
    api_endpoint = "example.googleapis.com"
    api_mtls_endpoint = "example.mtls.googleapis.com"
    sandbox_endpoint = "example.sandbox.googleapis.com"
    sandbox_mtls_endpoint = "example.mtls.sandbox.googleapis.com"
    non_googleapi = "api.example.com"

    assert client_class._get_default_mtls_endpoint(None) is None
    assert client_class._get_default_mtls_endpoint(api_endpoint) == api_mtls_endpoint
    assert (
        client_class._get_default_mtls_endpoint(api_mtls_endpoint) == api_mtls_endpoint
    )
    assert (
        client_class._get_default_mtls_endpoint(sandbox_endpoint)
        == sandbox_mtls_endpoint
    )
    assert (
        client_class._get_default_mtls_endpoint(sandbox_mtls_endpoint)
        == sandbox_mtls_endpoint
    )
    assert client_class._get_default_mtls_endpoint(non_googleapi) == non_googleapi


@pytest.mark.parametrize(
    "client_class",
    PYPARAM_CLIENT,
)
def test_operations_client_from_service_account_info(client_class):
    creds = ga_credentials.AnonymousCredentials()
    if "async" in str(client_class):
        # TODO(): Add support for service account info to async REST transport.
        with pytest.raises(NotImplementedError):
            info = {"valid": True}
            client_class.from_service_account_info(info)
    else:
        with mock.patch.object(
            service_account.Credentials, "from_service_account_info"
        ) as factory:
            factory.return_value = creds
            info = {"valid": True}
            client = client_class.from_service_account_info(info)
            assert client.transport._credentials == creds
            assert isinstance(client, client_class)

            assert client.transport._host == "https://longrunning.googleapis.com"


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.OperationsRestTransport,
        # TODO(https://github.com/googleapis/python-api-core/issues/706): Add support for
        # service account credentials in transports.AsyncOperationsRestTransport
    ],
)
def test_operations_client_service_account_always_use_jwt(transport_class):
    with mock.patch.object(
        service_account.Credentials, "with_always_use_jwt_access", create=True
    ) as use_jwt:
        creds = service_account.Credentials(None, None, None)
        transport_class(credentials=creds, always_use_jwt_access=True)
        use_jwt.assert_called_once_with(True)

    with mock.patch.object(
        service_account.Credentials, "with_always_use_jwt_access", create=True
    ) as use_jwt:
        creds = service_account.Credentials(None, None, None)
        transport_class(credentials=creds, always_use_jwt_access=False)
        use_jwt.assert_not_called()


@pytest.mark.parametrize(
    "client_class",
    PYPARAM_CLIENT,
)
def test_operations_client_from_service_account_file(client_class):
    if "async" in str(client_class):
        # TODO(): Add support for service account creds to async REST transport.
        with pytest.raises(NotImplementedError):
            client_class.from_service_account_file("dummy/file/path.json")
    else:
        creds = ga_credentials.AnonymousCredentials()
        with mock.patch.object(
            service_account.Credentials, "from_service_account_file"
        ) as factory:
            factory.return_value = creds
            client = client_class.from_service_account_file("dummy/file/path.json")
            assert client.transport._credentials == creds
            assert isinstance(client, client_class)

            client = client_class.from_service_account_json("dummy/file/path.json")
            assert client.transport._credentials == creds
            assert isinstance(client, client_class)

            assert client.transport._host == "https://longrunning.googleapis.com"


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name",
    PYPARAM_CLIENT_TRANSPORT_NAME,
)
def test_operations_client_get_transport_class(
    client_class, transport_class, transport_name
):
    transport = client_class.get_transport_class()
    available_transports = [
        transports.OperationsRestTransport,
    ]
    if GOOGLE_AUTH_AIO_INSTALLED:
        available_transports.append(transports.AsyncOperationsRestTransport)
    assert transport in available_transports

    transport = client_class.get_transport_class(transport_name)
    assert transport == transport_class


# TODO(): Update this test case to include async REST once we have support for MTLS.
@pytest.mark.parametrize(
    "client_class,transport_class,transport_name",
    [(AbstractOperationsClient, transports.OperationsRestTransport, "rest")],
)
@mock.patch.object(
    AbstractOperationsClient,
    "DEFAULT_ENDPOINT",
    modify_default_endpoint(AbstractOperationsClient),
)
def test_operations_client_client_options(
    client_class, transport_class, transport_name
):
    # # Check that if channel is provided we won't create a new one.
    # with mock.patch.object(AbstractOperationsBaseClient, "get_transport_class") as gtc:
    #     client = client_class(transport=transport_class())
    #     gtc.assert_not_called()

    # # Check that if channel is provided via str we will create a new one.
    # with mock.patch.object(AbstractOperationsBaseClient, "get_transport_class") as gtc:
    #     client = client_class(transport=transport_name)
    #     gtc.assert_called()

    # Check the case api_endpoint is provided.
    options = client_options.ClientOptions(api_endpoint="squid.clam.whelk")
    with mock.patch.object(transport_class, "__init__") as patched:
        patched.return_value = None
        client = client_class(client_options=options, transport=transport_name)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host="squid.clam.whelk",
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
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
                host=client.DEFAULT_ENDPOINT,
                scopes=None,
                client_cert_source_for_mtls=None,
                quota_project_id=None,
                client_info=transports.base.DEFAULT_CLIENT_INFO,
                always_use_jwt_access=True,
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
            )

    # Check the case api_endpoint is not provided and GOOGLE_API_USE_MTLS_ENDPOINT has
    # unsupported value.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "Unsupported"}):
        with pytest.raises(MutualTLSChannelError):
            client = client_class()

    # Check the case GOOGLE_API_USE_CLIENT_CERTIFICATE has unsupported value
    with mock.patch.dict(
        os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "Unsupported"}
    ):
        # Test behavior for google.auth versions < 2.43.0.
        # These versions do not have the updated mtls.should_use_client_cert logic.
        # Verify that a ValueError is raised when GOOGLE_API_USE_CLIENT_CERTIFICATE
        # is set to an unsupported value, as expected in these older versions.
        if parse_version_to_tuple(auth_version) < (2, 43, 0):
            with pytest.raises(ValueError):
                client = client_class()
        # Test behavior for google.auth versions >= 2.43.0.
        # In these versions, if GOOGLE_API_USE_CLIENT_CERTIFICATE is set to an
        # unsupported value (e.g., not 'true' or 'false'), the expected behavior
        # of the internal google.auth.mtls.should_use_client_cert() function
        # is to return False. Expect should_use_client_cert to return False, so
        # client creation should proceed without requiring a client certificate.
        else:
            with mock.patch.object(transport_class, "__init__") as patched:
                patched.return_value = None
                client = client_class(
                    credentials=ga_credentials.AnonymousCredentials(),
                    transport=transport_name,
                )

    # Check the case quota_project_id is provided
    options = client_options.ClientOptions(quota_project_id="octopus")
    with mock.patch.object(transport_class, "__init__") as patched:
        patched.return_value = None
        client = client_class(client_options=options, transport=transport_name)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host=client.DEFAULT_ENDPOINT,
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id="octopus",
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
        )

    # Check the case credentials_file is provided
    with warn_deprecated_credentials_file():
        options = client_options.ClientOptions(credentials_file="credentials.json")
    with mock.patch.object(transport_class, "__init__") as patched:
        patched.return_value = None
        client = client_class(client_options=options, transport=transport_name)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file="credentials.json",
            host=client.DEFAULT_ENDPOINT,
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
        )


# TODO: Add support for mtls in async REST
@pytest.mark.parametrize(
    "client_class,transport_class,transport_name,use_client_cert_env",
    [
        (AbstractOperationsClient, transports.OperationsRestTransport, "rest", "true"),
        (AbstractOperationsClient, transports.OperationsRestTransport, "rest", "false"),
    ],
)
@mock.patch.object(
    AbstractOperationsClient,
    "DEFAULT_ENDPOINT",
    modify_default_endpoint(AbstractOperationsClient),
)
@mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "auto"})
def test_operations_client_mtls_env_auto(
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

        def fake_init(client_cert_source_for_mtls=None, **kwargs):
            """Invoke client_cert source if provided."""

            if client_cert_source_for_mtls:
                client_cert_source_for_mtls()
                return None

        with mock.patch.object(transport_class, "__init__") as patched:
            patched.side_effect = fake_init
            client = client_class(client_options=options)

            if use_client_cert_env == "false":
                expected_client_cert_source = None
                expected_host = client.DEFAULT_ENDPOINT
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
                        expected_host = client.DEFAULT_ENDPOINT
                        expected_client_cert_source = None
                    else:
                        expected_host = client.DEFAULT_MTLS_ENDPOINT
                        expected_client_cert_source = client_cert_source_callback

                    patched.return_value = None
                    client = client_class()
                    patched.assert_called_once_with(
                        credentials=None,
                        credentials_file=None,
                        host=expected_host,
                        scopes=None,
                        client_cert_source_for_mtls=expected_client_cert_source,
                        quota_project_id=None,
                        client_info=transports.base.DEFAULT_CLIENT_INFO,
                        always_use_jwt_access=True,
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
                client = client_class()
                patched.assert_called_once_with(
                    credentials=None,
                    credentials_file=None,
                    host=client.DEFAULT_ENDPOINT,
                    scopes=None,
                    client_cert_source_for_mtls=None,
                    quota_project_id=None,
                    client_info=transports.base.DEFAULT_CLIENT_INFO,
                    always_use_jwt_access=True,
                )


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name",
    PYPARAM_CLIENT_TRANSPORT_NAME,
)
def test_operations_client_client_options_scopes(
    client_class, transport_class, transport_name
):
    # Check the case scopes are provided.
    options = client_options.ClientOptions(
        scopes=["1", "2"],
    )
    if "async" in str(client_class):
        # TODO(): Add support for scopes to async REST transport.
        with pytest.raises(core_exceptions.AsyncRestUnsupportedParameterError):
            client_class(client_options=options, transport=transport_name)
    else:
        with mock.patch.object(transport_class, "__init__") as patched:
            patched.return_value = None
            client = client_class(client_options=options, transport=transport_name)
            patched.assert_called_once_with(
                credentials=None,
                credentials_file=None,
                host=client.DEFAULT_ENDPOINT,
                scopes=["1", "2"],
                client_cert_source_for_mtls=None,
                quota_project_id=None,
                client_info=transports.base.DEFAULT_CLIENT_INFO,
                always_use_jwt_access=True,
            )


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name",
    PYPARAM_CLIENT_TRANSPORT_NAME,
)
def test_operations_client_client_options_credentials_file(
    client_class, transport_class, transport_name
):
    # Check the case credentials file is provided.
    with warn_deprecated_credentials_file():
        options = client_options.ClientOptions(credentials_file="credentials.json")
    if "async" in str(client_class):
        # TODO(): Add support for credentials file to async REST transport.
        with pytest.raises(core_exceptions.AsyncRestUnsupportedParameterError):
            with warn_deprecated_credentials_file():
                client_class(client_options=options, transport=transport_name)
    else:
        with mock.patch.object(transport_class, "__init__") as patched:
            patched.return_value = None
            client = client_class(client_options=options, transport=transport_name)
            patched.assert_called_once_with(
                credentials=None,
                credentials_file="credentials.json",
                host=client.DEFAULT_ENDPOINT,
                scopes=None,
                client_cert_source_for_mtls=None,
                quota_project_id=None,
                client_info=transports.base.DEFAULT_CLIENT_INFO,
                always_use_jwt_access=True,
            )


@pytest.mark.parametrize(
    "credentials_file",
    [None, "credentials.json"],
)
@mock.patch(
    "google.auth.default",
    autospec=True,
    return_value=(mock.sentinel.credentials, mock.sentinel.project),
)
def test_list_operations_rest(google_auth_default, credentials_file):
    if credentials_file:
        with warn_deprecated_credentials_file():
            sync_transport = transports.rest.OperationsRestTransport(
                credentials_file=credentials_file,
                http_options=HTTP_OPTIONS,
            )
    else:
        # no warning expected
        sync_transport = transports.rest.OperationsRestTransport(
            credentials_file=credentials_file,
            http_options=HTTP_OPTIONS,
        )

    client = AbstractOperationsClient(transport=sync_transport)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(_get_session_type(is_async=False), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = operations_pb2.ListOperationsResponse(
            next_page_token="next_page_token_value",
        )

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        response = client.list_operations(
            name="operations", filter_="my_filter", page_size=10, page_token="abc"
        )

        actual_args = req.call_args
        assert actual_args.args[0] == "GET"
        assert actual_args.args[1] == "https://longrunning.googleapis.com/v3/operations"
        assert actual_args.kwargs["params"] == [
            ("filter", "my_filter"),
            ("pageSize", 10),
            ("pageToken", "abc"),
        ]

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListOperationsPager)
    assert response.next_page_token == "next_page_token_value"


@pytest.mark.asyncio
async def test_list_operations_rest_async():
    if not GOOGLE_AUTH_AIO_INSTALLED:
        pytest.skip("Skipped because google-api-core[async_rest] is not installed")

    client = _get_operations_client(is_async=True)
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(_get_session_type(is_async=True), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = operations_pb2.ListOperationsResponse(
            next_page_token="next_page_token_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)
        response_value.read = mock.AsyncMock(
            return_value=json_return_value.encode("UTF-8")
        )
        req.return_value = response_value
        response = await client.list_operations(
            name="operations", filter_="my_filter", page_size=10, page_token="abc"
        )

        actual_args = req.call_args
        assert actual_args.args[0] == "GET"
        assert actual_args.args[1] == "https://longrunning.googleapis.com/v3/operations"
        assert actual_args.kwargs["params"] == [
            ("filter", "my_filter"),
            ("pageSize", 10),
            ("pageToken", "abc"),
        ]

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers_async.ListOperationsAsyncPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_operations_rest_failure():
    client = _get_operations_client(is_async=False, http_options=None)

    with mock.patch.object(_get_session_type(is_async=False), "request") as req:
        response_value = Response()
        response_value.status_code = 400
        mock_request = mock.MagicMock()
        mock_request.method = "GET"
        mock_request.url = "https://longrunning.googleapis.com:443/v1/operations"
        response_value.request = mock_request
        req.return_value = response_value
        with pytest.raises(core_exceptions.GoogleAPIError):
            client.list_operations(name="operations")


@pytest.mark.asyncio
async def test_list_operations_rest_failure_async():
    if not GOOGLE_AUTH_AIO_INSTALLED:
        pytest.skip("Skipped because google-api-core[async_rest] is not installed")

    client = _get_operations_client(is_async=True, http_options=None)

    with mock.patch.object(_get_session_type(is_async=True), "request") as req:
        response_value = mock.Mock()
        response_value.status_code = 400
        response_value.read = mock.AsyncMock(return_value=b"{}")
        mock_request = mock.MagicMock()
        mock_request.method = "GET"
        mock_request.url = "https://longrunning.googleapis.com:443/v1/operations"
        response_value.request = mock_request
        req.return_value = response_value
        with pytest.raises(core_exceptions.GoogleAPIError):
            await client.list_operations(name="operations")


def test_list_operations_rest_pager():
    client = _get_operations_client(is_async=False, http_options=None)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(_get_session_type(is_async=False), "request") as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        # with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            operations_pb2.ListOperationsResponse(
                operations=[
                    operations_pb2.Operation(),
                    operations_pb2.Operation(),
                    operations_pb2.Operation(),
                ],
                next_page_token="abc",
            ),
            operations_pb2.ListOperationsResponse(
                operations=[],
                next_page_token="def",
            ),
            operations_pb2.ListOperationsResponse(
                operations=[operations_pb2.Operation()],
                next_page_token="ghi",
            ),
            operations_pb2.ListOperationsResponse(
                operations=[operations_pb2.Operation(), operations_pb2.Operation()],
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(json_format.MessageToJson(x) for x in response)
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode("UTF-8")
            return_val.status_code = 200
        req.side_effect = return_values

        pager = client.list_operations(name="operations")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, operations_pb2.Operation) for i in results)

        pages = list(client.list_operations(name="operations").pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.next_page_token == token


@pytest.mark.asyncio
async def test_list_operations_rest_pager_async():
    if not GOOGLE_AUTH_AIO_INSTALLED:
        pytest.skip("Skipped because google-api-core[async_rest] is not installed")
    client = _get_operations_client(is_async=True, http_options=None)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(_get_session_type(is_async=True), "request") as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        # with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            operations_pb2.ListOperationsResponse(
                operations=[
                    operations_pb2.Operation(),
                    operations_pb2.Operation(),
                    operations_pb2.Operation(),
                ],
                next_page_token="abc",
            ),
            operations_pb2.ListOperationsResponse(
                operations=[],
                next_page_token="def",
            ),
            operations_pb2.ListOperationsResponse(
                operations=[operations_pb2.Operation()],
                next_page_token="ghi",
            ),
            operations_pb2.ListOperationsResponse(
                operations=[operations_pb2.Operation(), operations_pb2.Operation()],
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(json_format.MessageToJson(x) for x in response)
        return_values = tuple(mock.Mock() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val.read = mock.AsyncMock(return_value=response_val.encode("UTF-8"))
            return_val.status_code = 200
        req.side_effect = return_values

        pager = await client.list_operations(name="operations")

        responses = []
        async for response in pager:
            responses.append(response)

        results = list(responses)
        assert len(results) == 6
        assert all(isinstance(i, operations_pb2.Operation) for i in results)
        pager = await client.list_operations(name="operations")

        responses = []
        async for response in pager:
            responses.append(response)

        assert len(responses) == 6
        assert all(isinstance(i, operations_pb2.Operation) for i in results)

        pages = []

        async for page in pager.pages:
            pages.append(page)
        for page_, token in zip(pages, ["", "", "", "abc", "def", "ghi", ""]):
            assert page_.next_page_token == token


def test_get_operation_rest():
    client = _get_operations_client(is_async=False)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(_get_session_type(is_async=False), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = operations_pb2.Operation(
            name="operations/sample1",
            done=True,
            error=status_pb2.Status(code=411),
        )

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        response = client.get_operation("operations/sample1")

    actual_args = req.call_args
    assert actual_args.args[0] == "GET"
    assert (
        actual_args.args[1]
        == "https://longrunning.googleapis.com/v3/operations/sample1"
    )

    # Establish that the response is the type that we expect.
    assert isinstance(response, operations_pb2.Operation)
    assert response.name == "operations/sample1"
    assert response.done is True


@pytest.mark.asyncio
async def test_get_operation_rest_async():
    if not GOOGLE_AUTH_AIO_INSTALLED:
        pytest.skip("Skipped because google-api-core[async_rest] is not installed")
    client = _get_operations_client(is_async=True)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(_get_session_type(is_async=True), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = operations_pb2.Operation(
            name="operations/sample1",
            done=True,
            error=status_pb2.Status(code=411),
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)
        response_value.read = mock.AsyncMock(return_value=json_return_value)
        req.return_value = response_value
        response = await client.get_operation("operations/sample1")

    actual_args = req.call_args
    assert actual_args.args[0] == "GET"
    assert (
        actual_args.args[1]
        == "https://longrunning.googleapis.com/v3/operations/sample1"
    )

    # Establish that the response is the type that we expect.
    assert isinstance(response, operations_pb2.Operation)
    assert response.name == "operations/sample1"
    assert response.done is True


def test_get_operation_rest_failure():
    client = _get_operations_client(is_async=False, http_options=None)

    with mock.patch.object(_get_session_type(is_async=False), "request") as req:
        response_value = Response()
        response_value.status_code = 400
        mock_request = mock.MagicMock()
        mock_request.method = "GET"
        mock_request.url = "https://longrunning.googleapis.com/v1/operations/sample1"
        response_value.request = mock_request
        req.return_value = response_value
        with pytest.raises(core_exceptions.GoogleAPIError):
            client.get_operation("sample0/operations/sample1")


@pytest.mark.asyncio
async def test_get_operation_rest_failure_async():
    if not GOOGLE_AUTH_AIO_INSTALLED:
        pytest.skip("Skipped because google-api-core[async_rest] is not installed")
    client = _get_operations_client(is_async=True, http_options=None)

    with mock.patch.object(_get_session_type(is_async=True), "request") as req:
        response_value = mock.Mock()
        response_value.status_code = 400
        response_value.read = mock.AsyncMock(return_value=b"{}")
        mock_request = mock.MagicMock()
        mock_request.method = "GET"
        mock_request.url = "https://longrunning.googleapis.com/v1/operations/sample1"
        response_value.request = mock_request
        req.return_value = response_value
        with pytest.raises(core_exceptions.GoogleAPIError):
            await client.get_operation("sample0/operations/sample1")


def test_delete_operation_rest():
    client = _get_operations_client(is_async=False)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(_get_session_type(is_async=False), "request") as req:
        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = ""
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        client.delete_operation(name="operations/sample1")
        assert req.call_count == 1
        actual_args = req.call_args
        assert actual_args.args[0] == "DELETE"
        assert (
            actual_args.args[1]
            == "https://longrunning.googleapis.com/v3/operations/sample1"
        )


@pytest.mark.asyncio
async def test_delete_operation_rest_async():
    if not GOOGLE_AUTH_AIO_INSTALLED:
        pytest.skip("Skipped because google-api-core[async_rest] is not installed")
    client = _get_operations_client(is_async=True)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(_get_session_type(is_async=True), "request") as req:
        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200
        json_return_value = ""
        response_value.read = mock.AsyncMock(
            return_value=json_return_value.encode("UTF-8")
        )
        req.return_value = response_value
        await client.delete_operation(name="operations/sample1")
        assert req.call_count == 1
        actual_args = req.call_args
        assert actual_args.args[0] == "DELETE"
        assert (
            actual_args.args[1]
            == "https://longrunning.googleapis.com/v3/operations/sample1"
        )


def test_delete_operation_rest_failure():
    client = _get_operations_client(is_async=False, http_options=None)

    with mock.patch.object(_get_session_type(is_async=False), "request") as req:
        response_value = Response()
        response_value.status_code = 400
        mock_request = mock.MagicMock()
        mock_request.method = "DELETE"
        mock_request.url = "https://longrunning.googleapis.com/v1/operations/sample1"
        response_value.request = mock_request
        req.return_value = response_value
        with pytest.raises(core_exceptions.GoogleAPIError):
            client.delete_operation(name="sample0/operations/sample1")


@pytest.mark.asyncio
async def test_delete_operation_rest_failure_async():
    if not GOOGLE_AUTH_AIO_INSTALLED:
        pytest.skip("Skipped because google-api-core[async_rest] is not installed")
    client = _get_operations_client(is_async=True, http_options=None)

    with mock.patch.object(_get_session_type(is_async=True), "request") as req:
        response_value = mock.Mock()
        response_value.status_code = 400
        response_value.read = mock.AsyncMock(return_value=b"{}")
        mock_request = mock.MagicMock()
        mock_request.method = "DELETE"
        mock_request.url = "https://longrunning.googleapis.com/v1/operations/sample1"
        response_value.request = mock_request
        req.return_value = response_value
        with pytest.raises(core_exceptions.GoogleAPIError):
            await client.delete_operation(name="sample0/operations/sample1")


def test_cancel_operation_rest():
    client = _get_operations_client(is_async=False)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(_get_session_type(is_async=False), "request") as req:
        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = ""
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        client.cancel_operation(name="operations/sample1")
        assert req.call_count == 1
        actual_args = req.call_args
        assert actual_args.args[0] == "POST"
        assert (
            actual_args.args[1]
            == "https://longrunning.googleapis.com/v3/operations/sample1:cancel"
        )


@pytest.mark.asyncio
async def test_cancel_operation_rest_async():
    if not GOOGLE_AUTH_AIO_INSTALLED:
        pytest.skip("Skipped because google-api-core[async_rest] is not installed")
    client = _get_operations_client(is_async=True)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(_get_session_type(is_async=True), "request") as req:
        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200
        json_return_value = ""
        response_value.read = mock.AsyncMock(
            return_value=json_return_value.encode("UTF-8")
        )
        req.return_value = response_value
        await client.cancel_operation(name="operations/sample1")
        assert req.call_count == 1
        actual_args = req.call_args
        assert actual_args.args[0] == "POST"
        assert (
            actual_args.args[1]
            == "https://longrunning.googleapis.com/v3/operations/sample1:cancel"
        )


def test_cancel_operation_rest_failure():
    client = _get_operations_client(is_async=False, http_options=None)

    with mock.patch.object(_get_session_type(is_async=False), "request") as req:
        response_value = Response()
        response_value.status_code = 400
        mock_request = mock.MagicMock()
        mock_request.method = "POST"
        mock_request.url = (
            "https://longrunning.googleapis.com/v1/operations/sample1:cancel"
        )
        response_value.request = mock_request
        req.return_value = response_value
        with pytest.raises(core_exceptions.GoogleAPIError):
            client.cancel_operation(name="sample0/operations/sample1")


@pytest.mark.asyncio
async def test_cancel_operation_rest_failure_async():
    if not GOOGLE_AUTH_AIO_INSTALLED:
        pytest.skip("Skipped because google-api-core[async_rest] is not installed")
    client = _get_operations_client(is_async=True, http_options=None)

    with mock.patch.object(_get_session_type(is_async=True), "request") as req:
        response_value = mock.Mock()
        response_value.status_code = 400
        response_value.read = mock.AsyncMock(return_value=b"{}")
        mock_request = mock.MagicMock()
        mock_request.method = "POST"
        mock_request.url = (
            "https://longrunning.googleapis.com/v1/operations/sample1:cancel"
        )
        response_value.request = mock_request
        req.return_value = response_value
        with pytest.raises(core_exceptions.GoogleAPIError):
            await client.cancel_operation(name="sample0/operations/sample1")


@pytest.mark.parametrize(
    "client_class,transport_class,credentials",
    PYPARAM_CLIENT_TRANSPORT_CREDENTIALS,
)
def test_credentials_transport_error(client_class, transport_class, credentials):
    # It is an error to provide credentials and a transport instance.
    transport = transport_class(credentials=credentials)
    with pytest.raises(ValueError):
        client_class(
            credentials=ga_credentials.AnonymousCredentials(),
            transport=transport,
        )

    # It is an error to provide a credentials file and a transport instance.
    transport = transport_class(credentials=credentials)
    with pytest.raises(ValueError):
        client_class(
            client_options={"credentials_file": "credentials.json"},
            transport=transport,
        )

    # It is an error to provide scopes and a transport instance.
    transport = transport_class(credentials=credentials)
    with pytest.raises(ValueError):
        client_class(
            client_options={"scopes": ["1", "2"]},
            transport=transport,
        )


@pytest.mark.parametrize(
    "client_class,transport_class,credentials",
    PYPARAM_CLIENT_TRANSPORT_CREDENTIALS,
)
def test_transport_instance(client_class, transport_class, credentials):
    # A client may be instantiated with a custom transport instance.
    transport = transport_class(
        credentials=credentials,
    )
    client = client_class(transport=transport)
    assert client.transport is transport


@pytest.mark.parametrize(
    "client_class,transport_class,credentials",
    PYPARAM_CLIENT_TRANSPORT_CREDENTIALS,
)
def test_transport_adc(client_class, transport_class, credentials):
    # Test default credentials are used if not provided.
    with mock.patch.object(google.auth, "default") as adc:
        adc.return_value = (credentials, None)
        transport_class()
        adc.assert_called_once()


def test_operations_base_transport_error():
    # Passing both a credentials object and credentials_file should raise an error
    with pytest.raises(core_exceptions.DuplicateCredentialArgs):
        with warn_deprecated_credentials_file():
            transports.OperationsTransport(
                credentials=ga_credentials.AnonymousCredentials(),
                credentials_file="credentials.json",
            )


def test_operations_base_transport():
    # Instantiate the base transport.
    with mock.patch(
        "google.api_core.operations_v1.transports.OperationsTransport.__init__"
    ) as Transport:
        Transport.return_value = None
        transport = transports.OperationsTransport(
            credentials=ga_credentials.AnonymousCredentials(),
        )

    # Every method on the transport should just blindly
    # raise NotImplementedError.
    methods = (
        "list_operations",
        "get_operation",
        "delete_operation",
        "cancel_operation",
    )
    for method in methods:
        with pytest.raises(NotImplementedError):
            getattr(transport, method)(request=object())

    with pytest.raises(NotImplementedError):
        transport.close()


def test_operations_base_transport_with_credentials_file():
    # Instantiate the base transport with a credentials file
    with (
        mock.patch.object(
            google.auth, "load_credentials_from_file", autospec=True
        ) as load_creds,
        mock.patch(
            "google.api_core.operations_v1.transports.OperationsTransport._prep_wrapped_messages"
        ) as Transport,
    ):
        Transport.return_value = None
        load_creds.return_value = (ga_credentials.AnonymousCredentials(), None)
        with warn_deprecated_credentials_file():
            transports.OperationsTransport(
                credentials_file="credentials.json",
                quota_project_id="octopus",
            )
        load_creds.assert_called_once_with(
            "credentials.json",
            scopes=None,
            default_scopes=(),
            quota_project_id="octopus",
        )


def test_operations_base_transport_with_adc():
    # Test the default credentials are used if credentials and credentials_file are None.
    with (
        mock.patch.object(google.auth, "default", autospec=True) as adc,
        mock.patch(
            "google.api_core.operations_v1.transports.OperationsTransport._prep_wrapped_messages"
        ) as Transport,
    ):
        Transport.return_value = None
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transports.OperationsTransport()
        adc.assert_called_once()


@pytest.mark.parametrize(
    "client_class",
    PYPARAM_CLIENT,
)
def test_operations_auth_adc(client_class):
    # If no credentials are provided, we should use ADC credentials.
    is_async = "async" in str(client_class).lower()
    if is_async and parse_version_to_tuple(auth_version) < (2, 60, 0):
        # Older versions of google-auth do not accept the synchronous credentials
        # returned by ADC in `AsyncAuthorizedSession`.
        pytest.skip("ADC with the async REST transport requires google-auth >= 2.60.0")

    with mock.patch.object(google.auth, "default", autospec=True) as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        client_class()
        adc.assert_called_once_with(
            scopes=None,
            default_scopes=(),
            quota_project_id=None,
        )


# TODO(https://github.com/googleapis/python-api-core/issues/705): Add
# testing for `transports.AsyncOperationsRestTransport` once MTLS is supported
# in `google.auth.aio.transport`.
@pytest.mark.parametrize(
    "transport_class",
    [
        transports.OperationsRestTransport,
    ],
)
def test_operations_http_transport_client_cert_source_for_mtls(transport_class):
    cred = ga_credentials.AnonymousCredentials()
    with mock.patch(
        "google.auth.transport.requests.AuthorizedSession.configure_mtls_channel"
    ) as mock_configure_mtls_channel:
        transport_class(
            credentials=cred, client_cert_source_for_mtls=client_cert_source_callback
        )
        mock_configure_mtls_channel.assert_called_once_with(client_cert_source_callback)


@pytest.mark.parametrize(
    "client_class,transport_class,credentials",
    PYPARAM_CLIENT_TRANSPORT_CREDENTIALS,
)
def test_operations_host_no_port(client_class, transport_class, credentials):
    client = client_class(
        credentials=credentials,
        client_options=client_options.ClientOptions(
            api_endpoint="longrunning.googleapis.com"
        ),
    )
    assert client.transport._host == "https://longrunning.googleapis.com"


@pytest.mark.parametrize(
    "client_class,transport_class,credentials",
    PYPARAM_CLIENT_TRANSPORT_CREDENTIALS,
)
def test_operations_host_with_port(client_class, transport_class, credentials):
    client = client_class(
        credentials=credentials,
        client_options=client_options.ClientOptions(
            api_endpoint="longrunning.googleapis.com:8000"
        ),
    )
    assert client.transport._host == "https://longrunning.googleapis.com:8000"


@pytest.mark.parametrize(
    "client_class",
    PYPARAM_CLIENT,
)
def test_common_billing_account_path(client_class):
    billing_account = "squid"
    expected = "billingAccounts/{billing_account}".format(
        billing_account=billing_account,
    )
    actual = client_class.common_billing_account_path(billing_account)
    assert expected == actual


@pytest.mark.parametrize(
    "client_class",
    PYPARAM_CLIENT,
)
def test_parse_common_billing_account_path(client_class):
    expected = {
        "billing_account": "clam",
    }
    path = client_class.common_billing_account_path(**expected)

    # Check that the path construction is reversible.
    actual = client_class.parse_common_billing_account_path(path)
    assert expected == actual


@pytest.mark.parametrize(
    "client_class",
    PYPARAM_CLIENT,
)
def test_common_folder_path(client_class):
    folder = "whelk"
    expected = "folders/{folder}".format(
        folder=folder,
    )
    actual = client_class.common_folder_path(folder)
    assert expected == actual


@pytest.mark.parametrize(
    "client_class",
    PYPARAM_CLIENT,
)
def test_parse_common_folder_path(client_class):
    expected = {
        "folder": "octopus",
    }
    path = client_class.common_folder_path(**expected)

    # Check that the path construction is reversible.
    actual = client_class.parse_common_folder_path(path)
    assert expected == actual


@pytest.mark.parametrize(
    "client_class",
    PYPARAM_CLIENT,
)
def test_common_organization_path(client_class):
    organization = "oyster"
    expected = "organizations/{organization}".format(
        organization=organization,
    )
    actual = client_class.common_organization_path(organization)
    assert expected == actual


@pytest.mark.parametrize(
    "client_class",
    PYPARAM_CLIENT,
)
def test_parse_common_organization_path(client_class):
    expected = {
        "organization": "nudibranch",
    }
    path = client_class.common_organization_path(**expected)

    # Check that the path construction is reversible.
    actual = client_class.parse_common_organization_path(path)
    assert expected == actual


@pytest.mark.parametrize(
    "client_class",
    PYPARAM_CLIENT,
)
def test_common_project_path(client_class):
    project = "cuttlefish"
    expected = "projects/{project}".format(
        project=project,
    )
    actual = client_class.common_project_path(project)
    assert expected == actual


@pytest.mark.parametrize(
    "client_class",
    PYPARAM_CLIENT,
)
def test_parse_common_project_path(client_class):
    expected = {
        "project": "mussel",
    }
    path = client_class.common_project_path(**expected)

    # Check that the path construction is reversible.
    actual = client_class.parse_common_project_path(path)
    assert expected == actual


@pytest.mark.parametrize(
    "client_class",
    PYPARAM_CLIENT,
)
def test_common_location_path(client_class):
    project = "winkle"
    location = "nautilus"
    expected = "projects/{project}/locations/{location}".format(
        project=project,
        location=location,
    )
    actual = client_class.common_location_path(project, location)
    assert expected == actual


@pytest.mark.parametrize(
    "client_class",
    PYPARAM_CLIENT,
)
def test_parse_common_location_path(client_class):
    expected = {
        "project": "scallop",
        "location": "abalone",
    }
    path = client_class.common_location_path(**expected)

    # Check that the path construction is reversible.
    actual = client_class.parse_common_location_path(path)
    assert expected == actual


@pytest.mark.parametrize(
    "client_class,transport_class,credentials",
    PYPARAM_CLIENT_TRANSPORT_CREDENTIALS,
)
def test_client_withDEFAULT_CLIENT_INFO(client_class, transport_class, credentials):
    client_info = gapic_v1.client_info.ClientInfo()
    with mock.patch.object(transport_class, "_prep_wrapped_messages") as prep:
        client_class(
            credentials=credentials,
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)

    with mock.patch.object(transport_class, "_prep_wrapped_messages") as prep:
        transport_class(
            credentials=credentials,
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)
