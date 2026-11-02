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
import dataclasses
import json  # type: ignore
import logging
import warnings
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Union

import google.protobuf
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1, operations_v1, rest_helpers, rest_streaming
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.requests import AuthorizedSession  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.developerconnect_v1._compat import transcode_request
from google.cloud.developerconnect_v1.types import developer_connect

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseDeveloperConnectRestTransport

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object, None]  # type: ignore

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = logging.getLogger(__name__)

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=BASE_DEFAULT_CLIENT_INFO.gapic_version,
    grpc_version=None,
    rest_version=f"requests@{requests_version}",
)

DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class DeveloperConnectRestInterceptor:
    """Interceptor for DeveloperConnect.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the DeveloperConnectRestTransport.

    .. code-block:: python
        class MyCustomDeveloperConnectInterceptor(DeveloperConnectRestInterceptor):
            def pre_create_account_connector(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_account_connector(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_connection(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_connection(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_git_repository_link(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_git_repository_link(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_account_connector(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_account_connector(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_connection(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_connection(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_git_repository_link(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_git_repository_link(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_self(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_self(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_user(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_user(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_fetch_access_token(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_fetch_access_token(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_fetch_git_hub_installations(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_fetch_git_hub_installations(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_fetch_git_refs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_fetch_git_refs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_fetch_linkable_git_repositories(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_fetch_linkable_git_repositories(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_fetch_read_token(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_fetch_read_token(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_fetch_read_write_token(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_fetch_read_write_token(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_fetch_self(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_fetch_self(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_finish_o_auth(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_finish_o_auth(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_account_connector(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_account_connector(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_connection(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_connection(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_git_repository_link(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_git_repository_link(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_account_connectors(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_account_connectors(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_connections(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_connections(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_git_repository_links(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_git_repository_links(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_users(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_users(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_start_o_auth(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_start_o_auth(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_account_connector(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_account_connector(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_connection(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_connection(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = DeveloperConnectRestTransport(interceptor=MyCustomDeveloperConnectInterceptor())
        client = DeveloperConnectClient(transport=transport)


    """

    def pre_create_account_connector(
        self,
        request: developer_connect.CreateAccountConnectorRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        developer_connect.CreateAccountConnectorRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_account_connector

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DeveloperConnect server.
        """
        return request, metadata

    def post_create_account_connector(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_account_connector

        DEPRECATED. Please use the `post_create_account_connector_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DeveloperConnect server but before
        it is returned to user code. This `post_create_account_connector` interceptor runs
        before the `post_create_account_connector_with_metadata` interceptor.
        """
        return response

    def post_create_account_connector_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_account_connector

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DeveloperConnect server but before it is returned to user code.

        We recommend only using this `post_create_account_connector_with_metadata`
        interceptor in new development instead of the `post_create_account_connector` interceptor.
        When both interceptors are used, this `post_create_account_connector_with_metadata` interceptor runs after the
        `post_create_account_connector` interceptor. The (possibly modified) response returned by
        `post_create_account_connector` will be passed to
        `post_create_account_connector_with_metadata`.
        """
        return response, metadata

    def pre_create_connection(
        self,
        request: developer_connect.CreateConnectionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        developer_connect.CreateConnectionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_connection

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DeveloperConnect server.
        """
        return request, metadata

    def post_create_connection(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_connection

        DEPRECATED. Please use the `post_create_connection_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DeveloperConnect server but before
        it is returned to user code. This `post_create_connection` interceptor runs
        before the `post_create_connection_with_metadata` interceptor.
        """
        return response

    def post_create_connection_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_connection

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DeveloperConnect server but before it is returned to user code.

        We recommend only using this `post_create_connection_with_metadata`
        interceptor in new development instead of the `post_create_connection` interceptor.
        When both interceptors are used, this `post_create_connection_with_metadata` interceptor runs after the
        `post_create_connection` interceptor. The (possibly modified) response returned by
        `post_create_connection` will be passed to
        `post_create_connection_with_metadata`.
        """
        return response, metadata

    def pre_create_git_repository_link(
        self,
        request: developer_connect.CreateGitRepositoryLinkRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        developer_connect.CreateGitRepositoryLinkRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_git_repository_link

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DeveloperConnect server.
        """
        return request, metadata

    def post_create_git_repository_link(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_git_repository_link

        DEPRECATED. Please use the `post_create_git_repository_link_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DeveloperConnect server but before
        it is returned to user code. This `post_create_git_repository_link` interceptor runs
        before the `post_create_git_repository_link_with_metadata` interceptor.
        """
        return response

    def post_create_git_repository_link_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_git_repository_link

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DeveloperConnect server but before it is returned to user code.

        We recommend only using this `post_create_git_repository_link_with_metadata`
        interceptor in new development instead of the `post_create_git_repository_link` interceptor.
        When both interceptors are used, this `post_create_git_repository_link_with_metadata` interceptor runs after the
        `post_create_git_repository_link` interceptor. The (possibly modified) response returned by
        `post_create_git_repository_link` will be passed to
        `post_create_git_repository_link_with_metadata`.
        """
        return response, metadata

    def pre_delete_account_connector(
        self,
        request: developer_connect.DeleteAccountConnectorRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        developer_connect.DeleteAccountConnectorRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_account_connector

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DeveloperConnect server.
        """
        return request, metadata

    def post_delete_account_connector(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_account_connector

        DEPRECATED. Please use the `post_delete_account_connector_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DeveloperConnect server but before
        it is returned to user code. This `post_delete_account_connector` interceptor runs
        before the `post_delete_account_connector_with_metadata` interceptor.
        """
        return response

    def post_delete_account_connector_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_account_connector

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DeveloperConnect server but before it is returned to user code.

        We recommend only using this `post_delete_account_connector_with_metadata`
        interceptor in new development instead of the `post_delete_account_connector` interceptor.
        When both interceptors are used, this `post_delete_account_connector_with_metadata` interceptor runs after the
        `post_delete_account_connector` interceptor. The (possibly modified) response returned by
        `post_delete_account_connector` will be passed to
        `post_delete_account_connector_with_metadata`.
        """
        return response, metadata

    def pre_delete_connection(
        self,
        request: developer_connect.DeleteConnectionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        developer_connect.DeleteConnectionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_connection

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DeveloperConnect server.
        """
        return request, metadata

    def post_delete_connection(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_connection

        DEPRECATED. Please use the `post_delete_connection_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DeveloperConnect server but before
        it is returned to user code. This `post_delete_connection` interceptor runs
        before the `post_delete_connection_with_metadata` interceptor.
        """
        return response

    def post_delete_connection_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_connection

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DeveloperConnect server but before it is returned to user code.

        We recommend only using this `post_delete_connection_with_metadata`
        interceptor in new development instead of the `post_delete_connection` interceptor.
        When both interceptors are used, this `post_delete_connection_with_metadata` interceptor runs after the
        `post_delete_connection` interceptor. The (possibly modified) response returned by
        `post_delete_connection` will be passed to
        `post_delete_connection_with_metadata`.
        """
        return response, metadata

    def pre_delete_git_repository_link(
        self,
        request: developer_connect.DeleteGitRepositoryLinkRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        developer_connect.DeleteGitRepositoryLinkRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_git_repository_link

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DeveloperConnect server.
        """
        return request, metadata

    def post_delete_git_repository_link(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_git_repository_link

        DEPRECATED. Please use the `post_delete_git_repository_link_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DeveloperConnect server but before
        it is returned to user code. This `post_delete_git_repository_link` interceptor runs
        before the `post_delete_git_repository_link_with_metadata` interceptor.
        """
        return response

    def post_delete_git_repository_link_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_git_repository_link

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DeveloperConnect server but before it is returned to user code.

        We recommend only using this `post_delete_git_repository_link_with_metadata`
        interceptor in new development instead of the `post_delete_git_repository_link` interceptor.
        When both interceptors are used, this `post_delete_git_repository_link_with_metadata` interceptor runs after the
        `post_delete_git_repository_link` interceptor. The (possibly modified) response returned by
        `post_delete_git_repository_link` will be passed to
        `post_delete_git_repository_link_with_metadata`.
        """
        return response, metadata

    def pre_delete_self(
        self,
        request: developer_connect.DeleteSelfRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        developer_connect.DeleteSelfRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_self

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DeveloperConnect server.
        """
        return request, metadata

    def post_delete_self(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_self

        DEPRECATED. Please use the `post_delete_self_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DeveloperConnect server but before
        it is returned to user code. This `post_delete_self` interceptor runs
        before the `post_delete_self_with_metadata` interceptor.
        """
        return response

    def post_delete_self_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_self

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DeveloperConnect server but before it is returned to user code.

        We recommend only using this `post_delete_self_with_metadata`
        interceptor in new development instead of the `post_delete_self` interceptor.
        When both interceptors are used, this `post_delete_self_with_metadata` interceptor runs after the
        `post_delete_self` interceptor. The (possibly modified) response returned by
        `post_delete_self` will be passed to
        `post_delete_self_with_metadata`.
        """
        return response, metadata

    def pre_delete_user(
        self,
        request: developer_connect.DeleteUserRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        developer_connect.DeleteUserRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_user

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DeveloperConnect server.
        """
        return request, metadata

    def post_delete_user(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_user

        DEPRECATED. Please use the `post_delete_user_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DeveloperConnect server but before
        it is returned to user code. This `post_delete_user` interceptor runs
        before the `post_delete_user_with_metadata` interceptor.
        """
        return response

    def post_delete_user_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_user

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DeveloperConnect server but before it is returned to user code.

        We recommend only using this `post_delete_user_with_metadata`
        interceptor in new development instead of the `post_delete_user` interceptor.
        When both interceptors are used, this `post_delete_user_with_metadata` interceptor runs after the
        `post_delete_user` interceptor. The (possibly modified) response returned by
        `post_delete_user` will be passed to
        `post_delete_user_with_metadata`.
        """
        return response, metadata

    def pre_fetch_access_token(
        self,
        request: developer_connect.FetchAccessTokenRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        developer_connect.FetchAccessTokenRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for fetch_access_token

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DeveloperConnect server.
        """
        return request, metadata

    def post_fetch_access_token(
        self, response: developer_connect.FetchAccessTokenResponse
    ) -> developer_connect.FetchAccessTokenResponse:
        """Post-rpc interceptor for fetch_access_token

        DEPRECATED. Please use the `post_fetch_access_token_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DeveloperConnect server but before
        it is returned to user code. This `post_fetch_access_token` interceptor runs
        before the `post_fetch_access_token_with_metadata` interceptor.
        """
        return response

    def post_fetch_access_token_with_metadata(
        self,
        response: developer_connect.FetchAccessTokenResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        developer_connect.FetchAccessTokenResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for fetch_access_token

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DeveloperConnect server but before it is returned to user code.

        We recommend only using this `post_fetch_access_token_with_metadata`
        interceptor in new development instead of the `post_fetch_access_token` interceptor.
        When both interceptors are used, this `post_fetch_access_token_with_metadata` interceptor runs after the
        `post_fetch_access_token` interceptor. The (possibly modified) response returned by
        `post_fetch_access_token` will be passed to
        `post_fetch_access_token_with_metadata`.
        """
        return response, metadata

    def pre_fetch_git_hub_installations(
        self,
        request: developer_connect.FetchGitHubInstallationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        developer_connect.FetchGitHubInstallationsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for fetch_git_hub_installations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DeveloperConnect server.
        """
        return request, metadata

    def post_fetch_git_hub_installations(
        self, response: developer_connect.FetchGitHubInstallationsResponse
    ) -> developer_connect.FetchGitHubInstallationsResponse:
        """Post-rpc interceptor for fetch_git_hub_installations

        DEPRECATED. Please use the `post_fetch_git_hub_installations_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DeveloperConnect server but before
        it is returned to user code. This `post_fetch_git_hub_installations` interceptor runs
        before the `post_fetch_git_hub_installations_with_metadata` interceptor.
        """
        return response

    def post_fetch_git_hub_installations_with_metadata(
        self,
        response: developer_connect.FetchGitHubInstallationsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        developer_connect.FetchGitHubInstallationsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for fetch_git_hub_installations

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DeveloperConnect server but before it is returned to user code.

        We recommend only using this `post_fetch_git_hub_installations_with_metadata`
        interceptor in new development instead of the `post_fetch_git_hub_installations` interceptor.
        When both interceptors are used, this `post_fetch_git_hub_installations_with_metadata` interceptor runs after the
        `post_fetch_git_hub_installations` interceptor. The (possibly modified) response returned by
        `post_fetch_git_hub_installations` will be passed to
        `post_fetch_git_hub_installations_with_metadata`.
        """
        return response, metadata

    def pre_fetch_git_refs(
        self,
        request: developer_connect.FetchGitRefsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        developer_connect.FetchGitRefsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for fetch_git_refs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DeveloperConnect server.
        """
        return request, metadata

    def post_fetch_git_refs(
        self, response: developer_connect.FetchGitRefsResponse
    ) -> developer_connect.FetchGitRefsResponse:
        """Post-rpc interceptor for fetch_git_refs

        DEPRECATED. Please use the `post_fetch_git_refs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DeveloperConnect server but before
        it is returned to user code. This `post_fetch_git_refs` interceptor runs
        before the `post_fetch_git_refs_with_metadata` interceptor.
        """
        return response

    def post_fetch_git_refs_with_metadata(
        self,
        response: developer_connect.FetchGitRefsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        developer_connect.FetchGitRefsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for fetch_git_refs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DeveloperConnect server but before it is returned to user code.

        We recommend only using this `post_fetch_git_refs_with_metadata`
        interceptor in new development instead of the `post_fetch_git_refs` interceptor.
        When both interceptors are used, this `post_fetch_git_refs_with_metadata` interceptor runs after the
        `post_fetch_git_refs` interceptor. The (possibly modified) response returned by
        `post_fetch_git_refs` will be passed to
        `post_fetch_git_refs_with_metadata`.
        """
        return response, metadata

    def pre_fetch_linkable_git_repositories(
        self,
        request: developer_connect.FetchLinkableGitRepositoriesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        developer_connect.FetchLinkableGitRepositoriesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for fetch_linkable_git_repositories

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DeveloperConnect server.
        """
        return request, metadata

    def post_fetch_linkable_git_repositories(
        self, response: developer_connect.FetchLinkableGitRepositoriesResponse
    ) -> developer_connect.FetchLinkableGitRepositoriesResponse:
        """Post-rpc interceptor for fetch_linkable_git_repositories

        DEPRECATED. Please use the `post_fetch_linkable_git_repositories_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DeveloperConnect server but before
        it is returned to user code. This `post_fetch_linkable_git_repositories` interceptor runs
        before the `post_fetch_linkable_git_repositories_with_metadata` interceptor.
        """
        return response

    def post_fetch_linkable_git_repositories_with_metadata(
        self,
        response: developer_connect.FetchLinkableGitRepositoriesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        developer_connect.FetchLinkableGitRepositoriesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for fetch_linkable_git_repositories

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DeveloperConnect server but before it is returned to user code.

        We recommend only using this `post_fetch_linkable_git_repositories_with_metadata`
        interceptor in new development instead of the `post_fetch_linkable_git_repositories` interceptor.
        When both interceptors are used, this `post_fetch_linkable_git_repositories_with_metadata` interceptor runs after the
        `post_fetch_linkable_git_repositories` interceptor. The (possibly modified) response returned by
        `post_fetch_linkable_git_repositories` will be passed to
        `post_fetch_linkable_git_repositories_with_metadata`.
        """
        return response, metadata

    def pre_fetch_read_token(
        self,
        request: developer_connect.FetchReadTokenRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        developer_connect.FetchReadTokenRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for fetch_read_token

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DeveloperConnect server.
        """
        return request, metadata

    def post_fetch_read_token(
        self, response: developer_connect.FetchReadTokenResponse
    ) -> developer_connect.FetchReadTokenResponse:
        """Post-rpc interceptor for fetch_read_token

        DEPRECATED. Please use the `post_fetch_read_token_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DeveloperConnect server but before
        it is returned to user code. This `post_fetch_read_token` interceptor runs
        before the `post_fetch_read_token_with_metadata` interceptor.
        """
        return response

    def post_fetch_read_token_with_metadata(
        self,
        response: developer_connect.FetchReadTokenResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        developer_connect.FetchReadTokenResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for fetch_read_token

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DeveloperConnect server but before it is returned to user code.

        We recommend only using this `post_fetch_read_token_with_metadata`
        interceptor in new development instead of the `post_fetch_read_token` interceptor.
        When both interceptors are used, this `post_fetch_read_token_with_metadata` interceptor runs after the
        `post_fetch_read_token` interceptor. The (possibly modified) response returned by
        `post_fetch_read_token` will be passed to
        `post_fetch_read_token_with_metadata`.
        """
        return response, metadata

    def pre_fetch_read_write_token(
        self,
        request: developer_connect.FetchReadWriteTokenRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        developer_connect.FetchReadWriteTokenRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for fetch_read_write_token

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DeveloperConnect server.
        """
        return request, metadata

    def post_fetch_read_write_token(
        self, response: developer_connect.FetchReadWriteTokenResponse
    ) -> developer_connect.FetchReadWriteTokenResponse:
        """Post-rpc interceptor for fetch_read_write_token

        DEPRECATED. Please use the `post_fetch_read_write_token_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DeveloperConnect server but before
        it is returned to user code. This `post_fetch_read_write_token` interceptor runs
        before the `post_fetch_read_write_token_with_metadata` interceptor.
        """
        return response

    def post_fetch_read_write_token_with_metadata(
        self,
        response: developer_connect.FetchReadWriteTokenResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        developer_connect.FetchReadWriteTokenResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for fetch_read_write_token

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DeveloperConnect server but before it is returned to user code.

        We recommend only using this `post_fetch_read_write_token_with_metadata`
        interceptor in new development instead of the `post_fetch_read_write_token` interceptor.
        When both interceptors are used, this `post_fetch_read_write_token_with_metadata` interceptor runs after the
        `post_fetch_read_write_token` interceptor. The (possibly modified) response returned by
        `post_fetch_read_write_token` will be passed to
        `post_fetch_read_write_token_with_metadata`.
        """
        return response, metadata

    def pre_fetch_self(
        self,
        request: developer_connect.FetchSelfRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        developer_connect.FetchSelfRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for fetch_self

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DeveloperConnect server.
        """
        return request, metadata

    def post_fetch_self(
        self, response: developer_connect.User
    ) -> developer_connect.User:
        """Post-rpc interceptor for fetch_self

        DEPRECATED. Please use the `post_fetch_self_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DeveloperConnect server but before
        it is returned to user code. This `post_fetch_self` interceptor runs
        before the `post_fetch_self_with_metadata` interceptor.
        """
        return response

    def post_fetch_self_with_metadata(
        self,
        response: developer_connect.User,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[developer_connect.User, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for fetch_self

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DeveloperConnect server but before it is returned to user code.

        We recommend only using this `post_fetch_self_with_metadata`
        interceptor in new development instead of the `post_fetch_self` interceptor.
        When both interceptors are used, this `post_fetch_self_with_metadata` interceptor runs after the
        `post_fetch_self` interceptor. The (possibly modified) response returned by
        `post_fetch_self` will be passed to
        `post_fetch_self_with_metadata`.
        """
        return response, metadata

    def pre_finish_o_auth(
        self,
        request: developer_connect.FinishOAuthRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        developer_connect.FinishOAuthRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for finish_o_auth

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DeveloperConnect server.
        """
        return request, metadata

    def post_finish_o_auth(
        self, response: developer_connect.FinishOAuthResponse
    ) -> developer_connect.FinishOAuthResponse:
        """Post-rpc interceptor for finish_o_auth

        DEPRECATED. Please use the `post_finish_o_auth_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DeveloperConnect server but before
        it is returned to user code. This `post_finish_o_auth` interceptor runs
        before the `post_finish_o_auth_with_metadata` interceptor.
        """
        return response

    def post_finish_o_auth_with_metadata(
        self,
        response: developer_connect.FinishOAuthResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        developer_connect.FinishOAuthResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for finish_o_auth

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DeveloperConnect server but before it is returned to user code.

        We recommend only using this `post_finish_o_auth_with_metadata`
        interceptor in new development instead of the `post_finish_o_auth` interceptor.
        When both interceptors are used, this `post_finish_o_auth_with_metadata` interceptor runs after the
        `post_finish_o_auth` interceptor. The (possibly modified) response returned by
        `post_finish_o_auth` will be passed to
        `post_finish_o_auth_with_metadata`.
        """
        return response, metadata

    def pre_get_account_connector(
        self,
        request: developer_connect.GetAccountConnectorRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        developer_connect.GetAccountConnectorRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_account_connector

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DeveloperConnect server.
        """
        return request, metadata

    def post_get_account_connector(
        self, response: developer_connect.AccountConnector
    ) -> developer_connect.AccountConnector:
        """Post-rpc interceptor for get_account_connector

        DEPRECATED. Please use the `post_get_account_connector_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DeveloperConnect server but before
        it is returned to user code. This `post_get_account_connector` interceptor runs
        before the `post_get_account_connector_with_metadata` interceptor.
        """
        return response

    def post_get_account_connector_with_metadata(
        self,
        response: developer_connect.AccountConnector,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        developer_connect.AccountConnector, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_account_connector

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DeveloperConnect server but before it is returned to user code.

        We recommend only using this `post_get_account_connector_with_metadata`
        interceptor in new development instead of the `post_get_account_connector` interceptor.
        When both interceptors are used, this `post_get_account_connector_with_metadata` interceptor runs after the
        `post_get_account_connector` interceptor. The (possibly modified) response returned by
        `post_get_account_connector` will be passed to
        `post_get_account_connector_with_metadata`.
        """
        return response, metadata

    def pre_get_connection(
        self,
        request: developer_connect.GetConnectionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        developer_connect.GetConnectionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_connection

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DeveloperConnect server.
        """
        return request, metadata

    def post_get_connection(
        self, response: developer_connect.Connection
    ) -> developer_connect.Connection:
        """Post-rpc interceptor for get_connection

        DEPRECATED. Please use the `post_get_connection_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DeveloperConnect server but before
        it is returned to user code. This `post_get_connection` interceptor runs
        before the `post_get_connection_with_metadata` interceptor.
        """
        return response

    def post_get_connection_with_metadata(
        self,
        response: developer_connect.Connection,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[developer_connect.Connection, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_connection

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DeveloperConnect server but before it is returned to user code.

        We recommend only using this `post_get_connection_with_metadata`
        interceptor in new development instead of the `post_get_connection` interceptor.
        When both interceptors are used, this `post_get_connection_with_metadata` interceptor runs after the
        `post_get_connection` interceptor. The (possibly modified) response returned by
        `post_get_connection` will be passed to
        `post_get_connection_with_metadata`.
        """
        return response, metadata

    def pre_get_git_repository_link(
        self,
        request: developer_connect.GetGitRepositoryLinkRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        developer_connect.GetGitRepositoryLinkRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_git_repository_link

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DeveloperConnect server.
        """
        return request, metadata

    def post_get_git_repository_link(
        self, response: developer_connect.GitRepositoryLink
    ) -> developer_connect.GitRepositoryLink:
        """Post-rpc interceptor for get_git_repository_link

        DEPRECATED. Please use the `post_get_git_repository_link_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DeveloperConnect server but before
        it is returned to user code. This `post_get_git_repository_link` interceptor runs
        before the `post_get_git_repository_link_with_metadata` interceptor.
        """
        return response

    def post_get_git_repository_link_with_metadata(
        self,
        response: developer_connect.GitRepositoryLink,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        developer_connect.GitRepositoryLink, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_git_repository_link

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DeveloperConnect server but before it is returned to user code.

        We recommend only using this `post_get_git_repository_link_with_metadata`
        interceptor in new development instead of the `post_get_git_repository_link` interceptor.
        When both interceptors are used, this `post_get_git_repository_link_with_metadata` interceptor runs after the
        `post_get_git_repository_link` interceptor. The (possibly modified) response returned by
        `post_get_git_repository_link` will be passed to
        `post_get_git_repository_link_with_metadata`.
        """
        return response, metadata

    def pre_list_account_connectors(
        self,
        request: developer_connect.ListAccountConnectorsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        developer_connect.ListAccountConnectorsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_account_connectors

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DeveloperConnect server.
        """
        return request, metadata

    def post_list_account_connectors(
        self, response: developer_connect.ListAccountConnectorsResponse
    ) -> developer_connect.ListAccountConnectorsResponse:
        """Post-rpc interceptor for list_account_connectors

        DEPRECATED. Please use the `post_list_account_connectors_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DeveloperConnect server but before
        it is returned to user code. This `post_list_account_connectors` interceptor runs
        before the `post_list_account_connectors_with_metadata` interceptor.
        """
        return response

    def post_list_account_connectors_with_metadata(
        self,
        response: developer_connect.ListAccountConnectorsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        developer_connect.ListAccountConnectorsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_account_connectors

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DeveloperConnect server but before it is returned to user code.

        We recommend only using this `post_list_account_connectors_with_metadata`
        interceptor in new development instead of the `post_list_account_connectors` interceptor.
        When both interceptors are used, this `post_list_account_connectors_with_metadata` interceptor runs after the
        `post_list_account_connectors` interceptor. The (possibly modified) response returned by
        `post_list_account_connectors` will be passed to
        `post_list_account_connectors_with_metadata`.
        """
        return response, metadata

    def pre_list_connections(
        self,
        request: developer_connect.ListConnectionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        developer_connect.ListConnectionsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_connections

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DeveloperConnect server.
        """
        return request, metadata

    def post_list_connections(
        self, response: developer_connect.ListConnectionsResponse
    ) -> developer_connect.ListConnectionsResponse:
        """Post-rpc interceptor for list_connections

        DEPRECATED. Please use the `post_list_connections_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DeveloperConnect server but before
        it is returned to user code. This `post_list_connections` interceptor runs
        before the `post_list_connections_with_metadata` interceptor.
        """
        return response

    def post_list_connections_with_metadata(
        self,
        response: developer_connect.ListConnectionsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        developer_connect.ListConnectionsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_connections

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DeveloperConnect server but before it is returned to user code.

        We recommend only using this `post_list_connections_with_metadata`
        interceptor in new development instead of the `post_list_connections` interceptor.
        When both interceptors are used, this `post_list_connections_with_metadata` interceptor runs after the
        `post_list_connections` interceptor. The (possibly modified) response returned by
        `post_list_connections` will be passed to
        `post_list_connections_with_metadata`.
        """
        return response, metadata

    def pre_list_git_repository_links(
        self,
        request: developer_connect.ListGitRepositoryLinksRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        developer_connect.ListGitRepositoryLinksRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_git_repository_links

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DeveloperConnect server.
        """
        return request, metadata

    def post_list_git_repository_links(
        self, response: developer_connect.ListGitRepositoryLinksResponse
    ) -> developer_connect.ListGitRepositoryLinksResponse:
        """Post-rpc interceptor for list_git_repository_links

        DEPRECATED. Please use the `post_list_git_repository_links_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DeveloperConnect server but before
        it is returned to user code. This `post_list_git_repository_links` interceptor runs
        before the `post_list_git_repository_links_with_metadata` interceptor.
        """
        return response

    def post_list_git_repository_links_with_metadata(
        self,
        response: developer_connect.ListGitRepositoryLinksResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        developer_connect.ListGitRepositoryLinksResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_git_repository_links

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DeveloperConnect server but before it is returned to user code.

        We recommend only using this `post_list_git_repository_links_with_metadata`
        interceptor in new development instead of the `post_list_git_repository_links` interceptor.
        When both interceptors are used, this `post_list_git_repository_links_with_metadata` interceptor runs after the
        `post_list_git_repository_links` interceptor. The (possibly modified) response returned by
        `post_list_git_repository_links` will be passed to
        `post_list_git_repository_links_with_metadata`.
        """
        return response, metadata

    def pre_list_users(
        self,
        request: developer_connect.ListUsersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        developer_connect.ListUsersRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_users

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DeveloperConnect server.
        """
        return request, metadata

    def post_list_users(
        self, response: developer_connect.ListUsersResponse
    ) -> developer_connect.ListUsersResponse:
        """Post-rpc interceptor for list_users

        DEPRECATED. Please use the `post_list_users_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DeveloperConnect server but before
        it is returned to user code. This `post_list_users` interceptor runs
        before the `post_list_users_with_metadata` interceptor.
        """
        return response

    def post_list_users_with_metadata(
        self,
        response: developer_connect.ListUsersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        developer_connect.ListUsersResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_users

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DeveloperConnect server but before it is returned to user code.

        We recommend only using this `post_list_users_with_metadata`
        interceptor in new development instead of the `post_list_users` interceptor.
        When both interceptors are used, this `post_list_users_with_metadata` interceptor runs after the
        `post_list_users` interceptor. The (possibly modified) response returned by
        `post_list_users` will be passed to
        `post_list_users_with_metadata`.
        """
        return response, metadata

    def pre_start_o_auth(
        self,
        request: developer_connect.StartOAuthRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        developer_connect.StartOAuthRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for start_o_auth

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DeveloperConnect server.
        """
        return request, metadata

    def post_start_o_auth(
        self, response: developer_connect.StartOAuthResponse
    ) -> developer_connect.StartOAuthResponse:
        """Post-rpc interceptor for start_o_auth

        DEPRECATED. Please use the `post_start_o_auth_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DeveloperConnect server but before
        it is returned to user code. This `post_start_o_auth` interceptor runs
        before the `post_start_o_auth_with_metadata` interceptor.
        """
        return response

    def post_start_o_auth_with_metadata(
        self,
        response: developer_connect.StartOAuthResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        developer_connect.StartOAuthResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for start_o_auth

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DeveloperConnect server but before it is returned to user code.

        We recommend only using this `post_start_o_auth_with_metadata`
        interceptor in new development instead of the `post_start_o_auth` interceptor.
        When both interceptors are used, this `post_start_o_auth_with_metadata` interceptor runs after the
        `post_start_o_auth` interceptor. The (possibly modified) response returned by
        `post_start_o_auth` will be passed to
        `post_start_o_auth_with_metadata`.
        """
        return response, metadata

    def pre_update_account_connector(
        self,
        request: developer_connect.UpdateAccountConnectorRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        developer_connect.UpdateAccountConnectorRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_account_connector

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DeveloperConnect server.
        """
        return request, metadata

    def post_update_account_connector(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_account_connector

        DEPRECATED. Please use the `post_update_account_connector_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DeveloperConnect server but before
        it is returned to user code. This `post_update_account_connector` interceptor runs
        before the `post_update_account_connector_with_metadata` interceptor.
        """
        return response

    def post_update_account_connector_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_account_connector

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DeveloperConnect server but before it is returned to user code.

        We recommend only using this `post_update_account_connector_with_metadata`
        interceptor in new development instead of the `post_update_account_connector` interceptor.
        When both interceptors are used, this `post_update_account_connector_with_metadata` interceptor runs after the
        `post_update_account_connector` interceptor. The (possibly modified) response returned by
        `post_update_account_connector` will be passed to
        `post_update_account_connector_with_metadata`.
        """
        return response, metadata

    def pre_update_connection(
        self,
        request: developer_connect.UpdateConnectionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        developer_connect.UpdateConnectionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_connection

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DeveloperConnect server.
        """
        return request, metadata

    def post_update_connection(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_connection

        DEPRECATED. Please use the `post_update_connection_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DeveloperConnect server but before
        it is returned to user code. This `post_update_connection` interceptor runs
        before the `post_update_connection_with_metadata` interceptor.
        """
        return response

    def post_update_connection_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_connection

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DeveloperConnect server but before it is returned to user code.

        We recommend only using this `post_update_connection_with_metadata`
        interceptor in new development instead of the `post_update_connection` interceptor.
        When both interceptors are used, this `post_update_connection_with_metadata` interceptor runs after the
        `post_update_connection` interceptor. The (possibly modified) response returned by
        `post_update_connection` will be passed to
        `post_update_connection_with_metadata`.
        """
        return response, metadata

    def pre_get_location(
        self,
        request: locations_pb2.GetLocationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        locations_pb2.GetLocationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_location

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DeveloperConnect server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the DeveloperConnect server but before
        it is returned to user code.
        """
        return response

    def pre_list_locations(
        self,
        request: locations_pb2.ListLocationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        locations_pb2.ListLocationsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_locations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DeveloperConnect server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the DeveloperConnect server but before
        it is returned to user code.
        """
        return response

    def pre_cancel_operation(
        self,
        request: operations_pb2.CancelOperationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        operations_pb2.CancelOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DeveloperConnect server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the DeveloperConnect server but before
        it is returned to user code.
        """
        return response

    def pre_delete_operation(
        self,
        request: operations_pb2.DeleteOperationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        operations_pb2.DeleteOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DeveloperConnect server.
        """
        return request, metadata

    def post_delete_operation(self, response: None) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the DeveloperConnect server but before
        it is returned to user code.
        """
        return response

    def pre_get_operation(
        self,
        request: operations_pb2.GetOperationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        operations_pb2.GetOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DeveloperConnect server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the DeveloperConnect server but before
        it is returned to user code.
        """
        return response

    def pre_list_operations(
        self,
        request: operations_pb2.ListOperationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        operations_pb2.ListOperationsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_operations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DeveloperConnect server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the DeveloperConnect server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class DeveloperConnectRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: DeveloperConnectRestInterceptor


class DeveloperConnectRestTransport(_BaseDeveloperConnectRestTransport):
    """REST backend synchronous transport for DeveloperConnect.

    Service describing handlers for resources

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "developerconnect.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[DeveloperConnectRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'developerconnect.googleapis.com').
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.

            credentials_file (Optional[str]): Deprecated. A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided. This argument will be
                removed in the next major version of this library.
            scopes (Optional(Sequence[str])): A list of scopes. This argument is
                ignored if ``channel`` is provided.
            client_cert_source_for_mtls (Callable[[], Tuple[bytes, bytes]]): Client
                certificate to configure mutual TLS HTTP channel. It is ignored
                if ``channel`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you are developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.
            url_scheme: the protocol scheme for the API endpoint.  Normally
                "https", but for testing or local servers,
                "http" can be specified.
            interceptor (Optional[DeveloperConnectRestInterceptor]): Interceptor used
                to manipulate requests, request metadata, and responses.
            api_audience (Optional[str]): The intended audience for the API calls
                to the service that will be set when using certain 3rd party
                authentication flows. Audience is typically a resource identifier.
                If not set, the host value will be used as a default.
        """
        # Run the base constructor
        # TODO(yon-mg): resolve other ctor params i.e. scopes, quota, etc.
        # TODO: When custom host (api_endpoint) is set, `scopes` must *also* be set on the
        # credentials object
        super().__init__(
            host=host,
            credentials=credentials,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
            url_scheme=url_scheme,
            api_audience=api_audience,
        )
        self._session = AuthorizedSession(
            self._credentials, default_host=self.DEFAULT_HOST
        )
        self._operations_client: Optional[operations_v1.AbstractOperationsClient] = None
        if client_cert_source_for_mtls:
            self._session.configure_mtls_channel(client_cert_source_for_mtls)
        self._interceptor = interceptor or DeveloperConnectRestInterceptor()
        self._prep_wrapped_messages(client_info)

    @property
    def operations_client(self) -> operations_v1.AbstractOperationsClient:
        """Create the client designed to process long-running operations.

        This property caches on the instance; repeated calls return the same
        client.
        """
        # Only create a new client if we do not already have one.
        if self._operations_client is None:
            http_options: Dict[str, List[Dict[str, str]]] = {
                "google.longrunning.Operations.CancelOperation": [
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/operations/*}:cancel",
                        "body": "*",
                    },
                ],
                "google.longrunning.Operations.DeleteOperation": [
                    {
                        "method": "delete",
                        "uri": "/v1/{name=projects/*/locations/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.GetOperation": [
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.ListOperations": [
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*}/operations",
                    },
                ],
            }

            rest_transport = operations_v1.OperationsRestTransport(
                host=self._host,
                # use the credentials which are saved
                credentials=self._credentials,
                scopes=self._scopes,
                http_options=http_options,
                path_prefix="v1",
            )

            self._operations_client = operations_v1.AbstractOperationsClient(
                transport=rest_transport
            )

        # Return the client from cache.
        return self._operations_client

    class _CreateAccountConnector(
        _BaseDeveloperConnectRestTransport._BaseCreateAccountConnector,
        DeveloperConnectRestStub,
    ):
        def __hash__(self):
            return hash("DeveloperConnectRestTransport.CreateAccountConnector")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: developer_connect.CreateAccountConnectorRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create account connector method over HTTP.

            Args:
                request (~.developer_connect.CreateAccountConnectorRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options = _BaseDeveloperConnectRestTransport._BaseCreateAccountConnector._get_http_options()
            request, metadata = self._interceptor.pre_create_account_connector(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDeveloperConnectRestTransport._BaseCreateAccountConnector,
                    "_BaseCreateAccountConnector__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.developerconnect_v1.DeveloperConnectClient.CreateAccountConnector",
                    extra={
                        "serviceName": "google.cloud.developerconnect.v1.DeveloperConnect",
                        "rpcName": "CreateAccountConnector",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DeveloperConnectRestTransport._CreateAccountConnector._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                    body,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_account_connector(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_account_connector_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.developerconnect_v1.DeveloperConnectClient.create_account_connector",
                    extra={
                        "serviceName": "google.cloud.developerconnect.v1.DeveloperConnect",
                        "rpcName": "CreateAccountConnector",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateConnection(
        _BaseDeveloperConnectRestTransport._BaseCreateConnection,
        DeveloperConnectRestStub,
    ):
        def __hash__(self):
            return hash("DeveloperConnectRestTransport.CreateConnection")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: developer_connect.CreateConnectionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create connection method over HTTP.

            Args:
                request (~.developer_connect.CreateConnectionRequest):
                    The request object. Message for creating a Connection
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options = _BaseDeveloperConnectRestTransport._BaseCreateConnection._get_http_options()
            request, metadata = self._interceptor.pre_create_connection(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDeveloperConnectRestTransport._BaseCreateConnection,
                    "_BaseCreateConnection__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.developerconnect_v1.DeveloperConnectClient.CreateConnection",
                    extra={
                        "serviceName": "google.cloud.developerconnect.v1.DeveloperConnect",
                        "rpcName": "CreateConnection",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DeveloperConnectRestTransport._CreateConnection._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_connection(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_connection_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.developerconnect_v1.DeveloperConnectClient.create_connection",
                    extra={
                        "serviceName": "google.cloud.developerconnect.v1.DeveloperConnect",
                        "rpcName": "CreateConnection",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateGitRepositoryLink(
        _BaseDeveloperConnectRestTransport._BaseCreateGitRepositoryLink,
        DeveloperConnectRestStub,
    ):
        def __hash__(self):
            return hash("DeveloperConnectRestTransport.CreateGitRepositoryLink")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: developer_connect.CreateGitRepositoryLinkRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create git repository
            link method over HTTP.

                Args:
                    request (~.developer_connect.CreateGitRepositoryLinkRequest):
                        The request object. Message for creating a
                    GitRepositoryLink
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.operations_pb2.Operation:
                        This resource represents a
                    long-running operation that is the
                    result of a network API call.

            """

            http_options = _BaseDeveloperConnectRestTransport._BaseCreateGitRepositoryLink._get_http_options()
            request, metadata = self._interceptor.pre_create_git_repository_link(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDeveloperConnectRestTransport._BaseCreateGitRepositoryLink,
                    "_BaseCreateGitRepositoryLink__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.developerconnect_v1.DeveloperConnectClient.CreateGitRepositoryLink",
                    extra={
                        "serviceName": "google.cloud.developerconnect.v1.DeveloperConnect",
                        "rpcName": "CreateGitRepositoryLink",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DeveloperConnectRestTransport._CreateGitRepositoryLink._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                    body,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_git_repository_link(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_git_repository_link_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.developerconnect_v1.DeveloperConnectClient.create_git_repository_link",
                    extra={
                        "serviceName": "google.cloud.developerconnect.v1.DeveloperConnect",
                        "rpcName": "CreateGitRepositoryLink",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteAccountConnector(
        _BaseDeveloperConnectRestTransport._BaseDeleteAccountConnector,
        DeveloperConnectRestStub,
    ):
        def __hash__(self):
            return hash("DeveloperConnectRestTransport.DeleteAccountConnector")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: developer_connect.DeleteAccountConnectorRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete account connector method over HTTP.

            Args:
                request (~.developer_connect.DeleteAccountConnectorRequest):
                    The request object. Message for deleting a
                AccountConnector
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options = _BaseDeveloperConnectRestTransport._BaseDeleteAccountConnector._get_http_options()
            request, metadata = self._interceptor.pre_delete_account_connector(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDeveloperConnectRestTransport._BaseDeleteAccountConnector,
                    "_BaseDeleteAccountConnector__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.developerconnect_v1.DeveloperConnectClient.DeleteAccountConnector",
                    extra={
                        "serviceName": "google.cloud.developerconnect.v1.DeveloperConnect",
                        "rpcName": "DeleteAccountConnector",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DeveloperConnectRestTransport._DeleteAccountConnector._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_delete_account_connector(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_account_connector_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.developerconnect_v1.DeveloperConnectClient.delete_account_connector",
                    extra={
                        "serviceName": "google.cloud.developerconnect.v1.DeveloperConnect",
                        "rpcName": "DeleteAccountConnector",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteConnection(
        _BaseDeveloperConnectRestTransport._BaseDeleteConnection,
        DeveloperConnectRestStub,
    ):
        def __hash__(self):
            return hash("DeveloperConnectRestTransport.DeleteConnection")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: developer_connect.DeleteConnectionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete connection method over HTTP.

            Args:
                request (~.developer_connect.DeleteConnectionRequest):
                    The request object. Message for deleting a Connection
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options = _BaseDeveloperConnectRestTransport._BaseDeleteConnection._get_http_options()
            request, metadata = self._interceptor.pre_delete_connection(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDeveloperConnectRestTransport._BaseDeleteConnection,
                    "_BaseDeleteConnection__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.developerconnect_v1.DeveloperConnectClient.DeleteConnection",
                    extra={
                        "serviceName": "google.cloud.developerconnect.v1.DeveloperConnect",
                        "rpcName": "DeleteConnection",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DeveloperConnectRestTransport._DeleteConnection._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_delete_connection(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_connection_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.developerconnect_v1.DeveloperConnectClient.delete_connection",
                    extra={
                        "serviceName": "google.cloud.developerconnect.v1.DeveloperConnect",
                        "rpcName": "DeleteConnection",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteGitRepositoryLink(
        _BaseDeveloperConnectRestTransport._BaseDeleteGitRepositoryLink,
        DeveloperConnectRestStub,
    ):
        def __hash__(self):
            return hash("DeveloperConnectRestTransport.DeleteGitRepositoryLink")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: developer_connect.DeleteGitRepositoryLinkRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete git repository
            link method over HTTP.

                Args:
                    request (~.developer_connect.DeleteGitRepositoryLinkRequest):
                        The request object. Message for deleting a
                    GitRepositoryLink
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.operations_pb2.Operation:
                        This resource represents a
                    long-running operation that is the
                    result of a network API call.

            """

            http_options = _BaseDeveloperConnectRestTransport._BaseDeleteGitRepositoryLink._get_http_options()
            request, metadata = self._interceptor.pre_delete_git_repository_link(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDeveloperConnectRestTransport._BaseDeleteGitRepositoryLink,
                    "_BaseDeleteGitRepositoryLink__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.developerconnect_v1.DeveloperConnectClient.DeleteGitRepositoryLink",
                    extra={
                        "serviceName": "google.cloud.developerconnect.v1.DeveloperConnect",
                        "rpcName": "DeleteGitRepositoryLink",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DeveloperConnectRestTransport._DeleteGitRepositoryLink._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_delete_git_repository_link(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_git_repository_link_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.developerconnect_v1.DeveloperConnectClient.delete_git_repository_link",
                    extra={
                        "serviceName": "google.cloud.developerconnect.v1.DeveloperConnect",
                        "rpcName": "DeleteGitRepositoryLink",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteSelf(
        _BaseDeveloperConnectRestTransport._BaseDeleteSelf, DeveloperConnectRestStub
    ):
        def __hash__(self):
            return hash("DeveloperConnectRestTransport.DeleteSelf")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: developer_connect.DeleteSelfRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete self method over HTTP.

            Args:
                request (~.developer_connect.DeleteSelfRequest):
                    The request object. Message for deleting a User of the
                user themselves.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options = (
                _BaseDeveloperConnectRestTransport._BaseDeleteSelf._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_self(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDeveloperConnectRestTransport._BaseDeleteSelf,
                    "_BaseDeleteSelf__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.developerconnect_v1.DeveloperConnectClient.DeleteSelf",
                    extra={
                        "serviceName": "google.cloud.developerconnect.v1.DeveloperConnect",
                        "rpcName": "DeleteSelf",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DeveloperConnectRestTransport._DeleteSelf._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_delete_self(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_self_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.developerconnect_v1.DeveloperConnectClient.delete_self",
                    extra={
                        "serviceName": "google.cloud.developerconnect.v1.DeveloperConnect",
                        "rpcName": "DeleteSelf",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteUser(
        _BaseDeveloperConnectRestTransport._BaseDeleteUser, DeveloperConnectRestStub
    ):
        def __hash__(self):
            return hash("DeveloperConnectRestTransport.DeleteUser")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: developer_connect.DeleteUserRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete user method over HTTP.

            Args:
                request (~.developer_connect.DeleteUserRequest):
                    The request object. Message for deleting a User
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options = (
                _BaseDeveloperConnectRestTransport._BaseDeleteUser._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_user(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDeveloperConnectRestTransport._BaseDeleteUser,
                    "_BaseDeleteUser__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.developerconnect_v1.DeveloperConnectClient.DeleteUser",
                    extra={
                        "serviceName": "google.cloud.developerconnect.v1.DeveloperConnect",
                        "rpcName": "DeleteUser",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DeveloperConnectRestTransport._DeleteUser._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_delete_user(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_user_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.developerconnect_v1.DeveloperConnectClient.delete_user",
                    extra={
                        "serviceName": "google.cloud.developerconnect.v1.DeveloperConnect",
                        "rpcName": "DeleteUser",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _FetchAccessToken(
        _BaseDeveloperConnectRestTransport._BaseFetchAccessToken,
        DeveloperConnectRestStub,
    ):
        def __hash__(self):
            return hash("DeveloperConnectRestTransport.FetchAccessToken")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: developer_connect.FetchAccessTokenRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> developer_connect.FetchAccessTokenResponse:
            r"""Call the fetch access token method over HTTP.

            Args:
                request (~.developer_connect.FetchAccessTokenRequest):
                    The request object. Message for fetching an OAuth access
                token.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.developer_connect.FetchAccessTokenResponse:
                    Message for responding to getting an
                OAuth access token.

            """

            http_options = _BaseDeveloperConnectRestTransport._BaseFetchAccessToken._get_http_options()
            request, metadata = self._interceptor.pre_fetch_access_token(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDeveloperConnectRestTransport._BaseFetchAccessToken,
                    "_BaseFetchAccessToken__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.developerconnect_v1.DeveloperConnectClient.FetchAccessToken",
                    extra={
                        "serviceName": "google.cloud.developerconnect.v1.DeveloperConnect",
                        "rpcName": "FetchAccessToken",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DeveloperConnectRestTransport._FetchAccessToken._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = developer_connect.FetchAccessTokenResponse()
            pb_resp = developer_connect.FetchAccessTokenResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_fetch_access_token(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_fetch_access_token_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        developer_connect.FetchAccessTokenResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.developerconnect_v1.DeveloperConnectClient.fetch_access_token",
                    extra={
                        "serviceName": "google.cloud.developerconnect.v1.DeveloperConnect",
                        "rpcName": "FetchAccessToken",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _FetchGitHubInstallations(
        _BaseDeveloperConnectRestTransport._BaseFetchGitHubInstallations,
        DeveloperConnectRestStub,
    ):
        def __hash__(self):
            return hash("DeveloperConnectRestTransport.FetchGitHubInstallations")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: developer_connect.FetchGitHubInstallationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> developer_connect.FetchGitHubInstallationsResponse:
            r"""Call the fetch git hub
            installations method over HTTP.

                Args:
                    request (~.developer_connect.FetchGitHubInstallationsRequest):
                        The request object. Request for fetching github
                    installations.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.developer_connect.FetchGitHubInstallationsResponse:
                        Response of fetching github
                    installations.

            """

            http_options = _BaseDeveloperConnectRestTransport._BaseFetchGitHubInstallations._get_http_options()
            request, metadata = self._interceptor.pre_fetch_git_hub_installations(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDeveloperConnectRestTransport._BaseFetchGitHubInstallations,
                    "_BaseFetchGitHubInstallations__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.developerconnect_v1.DeveloperConnectClient.FetchGitHubInstallations",
                    extra={
                        "serviceName": "google.cloud.developerconnect.v1.DeveloperConnect",
                        "rpcName": "FetchGitHubInstallations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DeveloperConnectRestTransport._FetchGitHubInstallations._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = developer_connect.FetchGitHubInstallationsResponse()
            pb_resp = developer_connect.FetchGitHubInstallationsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_fetch_git_hub_installations(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_fetch_git_hub_installations_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        developer_connect.FetchGitHubInstallationsResponse.to_json(
                            response
                        )
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.developerconnect_v1.DeveloperConnectClient.fetch_git_hub_installations",
                    extra={
                        "serviceName": "google.cloud.developerconnect.v1.DeveloperConnect",
                        "rpcName": "FetchGitHubInstallations",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _FetchGitRefs(
        _BaseDeveloperConnectRestTransport._BaseFetchGitRefs, DeveloperConnectRestStub
    ):
        def __hash__(self):
            return hash("DeveloperConnectRestTransport.FetchGitRefs")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: developer_connect.FetchGitRefsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> developer_connect.FetchGitRefsResponse:
            r"""Call the fetch git refs method over HTTP.

            Args:
                request (~.developer_connect.FetchGitRefsRequest):
                    The request object. Request for fetching git refs.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.developer_connect.FetchGitRefsResponse:
                    Response for fetching git refs.
            """

            http_options = (
                _BaseDeveloperConnectRestTransport._BaseFetchGitRefs._get_http_options()
            )
            request, metadata = self._interceptor.pre_fetch_git_refs(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDeveloperConnectRestTransport._BaseFetchGitRefs,
                    "_BaseFetchGitRefs__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.developerconnect_v1.DeveloperConnectClient.FetchGitRefs",
                    extra={
                        "serviceName": "google.cloud.developerconnect.v1.DeveloperConnect",
                        "rpcName": "FetchGitRefs",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DeveloperConnectRestTransport._FetchGitRefs._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = developer_connect.FetchGitRefsResponse()
            pb_resp = developer_connect.FetchGitRefsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_fetch_git_refs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_fetch_git_refs_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = developer_connect.FetchGitRefsResponse.to_json(
                        response
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.developerconnect_v1.DeveloperConnectClient.fetch_git_refs",
                    extra={
                        "serviceName": "google.cloud.developerconnect.v1.DeveloperConnect",
                        "rpcName": "FetchGitRefs",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _FetchLinkableGitRepositories(
        _BaseDeveloperConnectRestTransport._BaseFetchLinkableGitRepositories,
        DeveloperConnectRestStub,
    ):
        def __hash__(self):
            return hash("DeveloperConnectRestTransport.FetchLinkableGitRepositories")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: developer_connect.FetchLinkableGitRepositoriesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> developer_connect.FetchLinkableGitRepositoriesResponse:
            r"""Call the fetch linkable git
            repositories method over HTTP.

                Args:
                    request (~.developer_connect.FetchLinkableGitRepositoriesRequest):
                        The request object. Request message for
                    FetchLinkableGitRepositoriesRequest.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.developer_connect.FetchLinkableGitRepositoriesResponse:
                        Response message for
                    FetchLinkableGitRepositories.

            """

            http_options = _BaseDeveloperConnectRestTransport._BaseFetchLinkableGitRepositories._get_http_options()
            request, metadata = self._interceptor.pre_fetch_linkable_git_repositories(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDeveloperConnectRestTransport._BaseFetchLinkableGitRepositories,
                    "_BaseFetchLinkableGitRepositories__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.developerconnect_v1.DeveloperConnectClient.FetchLinkableGitRepositories",
                    extra={
                        "serviceName": "google.cloud.developerconnect.v1.DeveloperConnect",
                        "rpcName": "FetchLinkableGitRepositories",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DeveloperConnectRestTransport._FetchLinkableGitRepositories._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = developer_connect.FetchLinkableGitRepositoriesResponse()
            pb_resp = developer_connect.FetchLinkableGitRepositoriesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_fetch_linkable_git_repositories(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_fetch_linkable_git_repositories_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        developer_connect.FetchLinkableGitRepositoriesResponse.to_json(
                            response
                        )
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.developerconnect_v1.DeveloperConnectClient.fetch_linkable_git_repositories",
                    extra={
                        "serviceName": "google.cloud.developerconnect.v1.DeveloperConnect",
                        "rpcName": "FetchLinkableGitRepositories",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _FetchReadToken(
        _BaseDeveloperConnectRestTransport._BaseFetchReadToken, DeveloperConnectRestStub
    ):
        def __hash__(self):
            return hash("DeveloperConnectRestTransport.FetchReadToken")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: developer_connect.FetchReadTokenRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> developer_connect.FetchReadTokenResponse:
            r"""Call the fetch read token method over HTTP.

            Args:
                request (~.developer_connect.FetchReadTokenRequest):
                    The request object. Message for fetching SCM read token.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.developer_connect.FetchReadTokenResponse:
                    Message for responding to get read
                token.

            """

            http_options = _BaseDeveloperConnectRestTransport._BaseFetchReadToken._get_http_options()
            request, metadata = self._interceptor.pre_fetch_read_token(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDeveloperConnectRestTransport._BaseFetchReadToken,
                    "_BaseFetchReadToken__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.developerconnect_v1.DeveloperConnectClient.FetchReadToken",
                    extra={
                        "serviceName": "google.cloud.developerconnect.v1.DeveloperConnect",
                        "rpcName": "FetchReadToken",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DeveloperConnectRestTransport._FetchReadToken._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = developer_connect.FetchReadTokenResponse()
            pb_resp = developer_connect.FetchReadTokenResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_fetch_read_token(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_fetch_read_token_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = developer_connect.FetchReadTokenResponse.to_json(
                        response
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.developerconnect_v1.DeveloperConnectClient.fetch_read_token",
                    extra={
                        "serviceName": "google.cloud.developerconnect.v1.DeveloperConnect",
                        "rpcName": "FetchReadToken",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _FetchReadWriteToken(
        _BaseDeveloperConnectRestTransport._BaseFetchReadWriteToken,
        DeveloperConnectRestStub,
    ):
        def __hash__(self):
            return hash("DeveloperConnectRestTransport.FetchReadWriteToken")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: developer_connect.FetchReadWriteTokenRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> developer_connect.FetchReadWriteTokenResponse:
            r"""Call the fetch read write token method over HTTP.

            Args:
                request (~.developer_connect.FetchReadWriteTokenRequest):
                    The request object. Message for fetching SCM read/write
                token.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.developer_connect.FetchReadWriteTokenResponse:
                    Message for responding to get
                read/write token.

            """

            http_options = _BaseDeveloperConnectRestTransport._BaseFetchReadWriteToken._get_http_options()
            request, metadata = self._interceptor.pre_fetch_read_write_token(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDeveloperConnectRestTransport._BaseFetchReadWriteToken,
                    "_BaseFetchReadWriteToken__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.developerconnect_v1.DeveloperConnectClient.FetchReadWriteToken",
                    extra={
                        "serviceName": "google.cloud.developerconnect.v1.DeveloperConnect",
                        "rpcName": "FetchReadWriteToken",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DeveloperConnectRestTransport._FetchReadWriteToken._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = developer_connect.FetchReadWriteTokenResponse()
            pb_resp = developer_connect.FetchReadWriteTokenResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_fetch_read_write_token(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_fetch_read_write_token_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        developer_connect.FetchReadWriteTokenResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.developerconnect_v1.DeveloperConnectClient.fetch_read_write_token",
                    extra={
                        "serviceName": "google.cloud.developerconnect.v1.DeveloperConnect",
                        "rpcName": "FetchReadWriteToken",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _FetchSelf(
        _BaseDeveloperConnectRestTransport._BaseFetchSelf, DeveloperConnectRestStub
    ):
        def __hash__(self):
            return hash("DeveloperConnectRestTransport.FetchSelf")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: developer_connect.FetchSelfRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> developer_connect.User:
            r"""Call the fetch self method over HTTP.

            Args:
                request (~.developer_connect.FetchSelfRequest):
                    The request object. Message for fetching a User of the
                user themselves.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.developer_connect.User:
                    User represents a user connected to
                the service providers through a
                AccountConnector.

            """

            http_options = (
                _BaseDeveloperConnectRestTransport._BaseFetchSelf._get_http_options()
            )
            request, metadata = self._interceptor.pre_fetch_self(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDeveloperConnectRestTransport._BaseFetchSelf,
                    "_BaseFetchSelf__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.developerconnect_v1.DeveloperConnectClient.FetchSelf",
                    extra={
                        "serviceName": "google.cloud.developerconnect.v1.DeveloperConnect",
                        "rpcName": "FetchSelf",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DeveloperConnectRestTransport._FetchSelf._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = developer_connect.User()
            pb_resp = developer_connect.User.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_fetch_self(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_fetch_self_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = developer_connect.User.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.developerconnect_v1.DeveloperConnectClient.fetch_self",
                    extra={
                        "serviceName": "google.cloud.developerconnect.v1.DeveloperConnect",
                        "rpcName": "FetchSelf",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _FinishOAuth(
        _BaseDeveloperConnectRestTransport._BaseFinishOAuth, DeveloperConnectRestStub
    ):
        def __hash__(self):
            return hash("DeveloperConnectRestTransport.FinishOAuth")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: developer_connect.FinishOAuthRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> developer_connect.FinishOAuthResponse:
            r"""Call the finish o auth method over HTTP.

            Args:
                request (~.developer_connect.FinishOAuthRequest):
                    The request object. Message for finishing an OAuth flow.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.developer_connect.FinishOAuthResponse:
                    Message for responding to finishing
                an OAuth flow.

            """

            http_options = (
                _BaseDeveloperConnectRestTransport._BaseFinishOAuth._get_http_options()
            )
            request, metadata = self._interceptor.pre_finish_o_auth(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDeveloperConnectRestTransport._BaseFinishOAuth,
                    "_BaseFinishOAuth__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.developerconnect_v1.DeveloperConnectClient.FinishOAuth",
                    extra={
                        "serviceName": "google.cloud.developerconnect.v1.DeveloperConnect",
                        "rpcName": "FinishOAuth",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DeveloperConnectRestTransport._FinishOAuth._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = developer_connect.FinishOAuthResponse()
            pb_resp = developer_connect.FinishOAuthResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_finish_o_auth(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_finish_o_auth_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = developer_connect.FinishOAuthResponse.to_json(
                        response
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.developerconnect_v1.DeveloperConnectClient.finish_o_auth",
                    extra={
                        "serviceName": "google.cloud.developerconnect.v1.DeveloperConnect",
                        "rpcName": "FinishOAuth",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetAccountConnector(
        _BaseDeveloperConnectRestTransport._BaseGetAccountConnector,
        DeveloperConnectRestStub,
    ):
        def __hash__(self):
            return hash("DeveloperConnectRestTransport.GetAccountConnector")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: developer_connect.GetAccountConnectorRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> developer_connect.AccountConnector:
            r"""Call the get account connector method over HTTP.

            Args:
                request (~.developer_connect.GetAccountConnectorRequest):
                    The request object. Message for getting a
                AccountConnector
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.developer_connect.AccountConnector:
                    AccountConnector encapsulates what a
                platform administrator needs to
                configure for users to connect to the
                service providers, which includes, among
                other fields, the OAuth client ID,
                client secret, and authorization and
                token endpoints.

            """

            http_options = _BaseDeveloperConnectRestTransport._BaseGetAccountConnector._get_http_options()
            request, metadata = self._interceptor.pre_get_account_connector(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDeveloperConnectRestTransport._BaseGetAccountConnector,
                    "_BaseGetAccountConnector__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.developerconnect_v1.DeveloperConnectClient.GetAccountConnector",
                    extra={
                        "serviceName": "google.cloud.developerconnect.v1.DeveloperConnect",
                        "rpcName": "GetAccountConnector",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DeveloperConnectRestTransport._GetAccountConnector._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = developer_connect.AccountConnector()
            pb_resp = developer_connect.AccountConnector.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_account_connector(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_account_connector_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = developer_connect.AccountConnector.to_json(
                        response
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.developerconnect_v1.DeveloperConnectClient.get_account_connector",
                    extra={
                        "serviceName": "google.cloud.developerconnect.v1.DeveloperConnect",
                        "rpcName": "GetAccountConnector",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetConnection(
        _BaseDeveloperConnectRestTransport._BaseGetConnection, DeveloperConnectRestStub
    ):
        def __hash__(self):
            return hash("DeveloperConnectRestTransport.GetConnection")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: developer_connect.GetConnectionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> developer_connect.Connection:
            r"""Call the get connection method over HTTP.

            Args:
                request (~.developer_connect.GetConnectionRequest):
                    The request object. Message for getting a Connection
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.developer_connect.Connection:
                    Message describing Connection object
            """

            http_options = _BaseDeveloperConnectRestTransport._BaseGetConnection._get_http_options()
            request, metadata = self._interceptor.pre_get_connection(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDeveloperConnectRestTransport._BaseGetConnection,
                    "_BaseGetConnection__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.developerconnect_v1.DeveloperConnectClient.GetConnection",
                    extra={
                        "serviceName": "google.cloud.developerconnect.v1.DeveloperConnect",
                        "rpcName": "GetConnection",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DeveloperConnectRestTransport._GetConnection._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = developer_connect.Connection()
            pb_resp = developer_connect.Connection.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_connection(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_connection_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = developer_connect.Connection.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.developerconnect_v1.DeveloperConnectClient.get_connection",
                    extra={
                        "serviceName": "google.cloud.developerconnect.v1.DeveloperConnect",
                        "rpcName": "GetConnection",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetGitRepositoryLink(
        _BaseDeveloperConnectRestTransport._BaseGetGitRepositoryLink,
        DeveloperConnectRestStub,
    ):
        def __hash__(self):
            return hash("DeveloperConnectRestTransport.GetGitRepositoryLink")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: developer_connect.GetGitRepositoryLinkRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> developer_connect.GitRepositoryLink:
            r"""Call the get git repository link method over HTTP.

            Args:
                request (~.developer_connect.GetGitRepositoryLinkRequest):
                    The request object. Message for getting a
                GitRepositoryLink
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.developer_connect.GitRepositoryLink:
                    Message describing the
                GitRepositoryLink object

            """

            http_options = _BaseDeveloperConnectRestTransport._BaseGetGitRepositoryLink._get_http_options()
            request, metadata = self._interceptor.pre_get_git_repository_link(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDeveloperConnectRestTransport._BaseGetGitRepositoryLink,
                    "_BaseGetGitRepositoryLink__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.developerconnect_v1.DeveloperConnectClient.GetGitRepositoryLink",
                    extra={
                        "serviceName": "google.cloud.developerconnect.v1.DeveloperConnect",
                        "rpcName": "GetGitRepositoryLink",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DeveloperConnectRestTransport._GetGitRepositoryLink._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = developer_connect.GitRepositoryLink()
            pb_resp = developer_connect.GitRepositoryLink.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_git_repository_link(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_git_repository_link_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = developer_connect.GitRepositoryLink.to_json(
                        response
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.developerconnect_v1.DeveloperConnectClient.get_git_repository_link",
                    extra={
                        "serviceName": "google.cloud.developerconnect.v1.DeveloperConnect",
                        "rpcName": "GetGitRepositoryLink",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListAccountConnectors(
        _BaseDeveloperConnectRestTransport._BaseListAccountConnectors,
        DeveloperConnectRestStub,
    ):
        def __hash__(self):
            return hash("DeveloperConnectRestTransport.ListAccountConnectors")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: developer_connect.ListAccountConnectorsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> developer_connect.ListAccountConnectorsResponse:
            r"""Call the list account connectors method over HTTP.

            Args:
                request (~.developer_connect.ListAccountConnectorsRequest):
                    The request object. Message for requesting list of
                AccountConnectors
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.developer_connect.ListAccountConnectorsResponse:
                    Message for response to listing
                AccountConnectors

            """

            http_options = _BaseDeveloperConnectRestTransport._BaseListAccountConnectors._get_http_options()
            request, metadata = self._interceptor.pre_list_account_connectors(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDeveloperConnectRestTransport._BaseListAccountConnectors,
                    "_BaseListAccountConnectors__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.developerconnect_v1.DeveloperConnectClient.ListAccountConnectors",
                    extra={
                        "serviceName": "google.cloud.developerconnect.v1.DeveloperConnect",
                        "rpcName": "ListAccountConnectors",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DeveloperConnectRestTransport._ListAccountConnectors._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = developer_connect.ListAccountConnectorsResponse()
            pb_resp = developer_connect.ListAccountConnectorsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_account_connectors(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_account_connectors_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        developer_connect.ListAccountConnectorsResponse.to_json(
                            response
                        )
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.developerconnect_v1.DeveloperConnectClient.list_account_connectors",
                    extra={
                        "serviceName": "google.cloud.developerconnect.v1.DeveloperConnect",
                        "rpcName": "ListAccountConnectors",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListConnections(
        _BaseDeveloperConnectRestTransport._BaseListConnections,
        DeveloperConnectRestStub,
    ):
        def __hash__(self):
            return hash("DeveloperConnectRestTransport.ListConnections")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: developer_connect.ListConnectionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> developer_connect.ListConnectionsResponse:
            r"""Call the list connections method over HTTP.

            Args:
                request (~.developer_connect.ListConnectionsRequest):
                    The request object. Message for requesting list of
                Connections
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.developer_connect.ListConnectionsResponse:
                    Message for response to listing
                Connections

            """

            http_options = _BaseDeveloperConnectRestTransport._BaseListConnections._get_http_options()
            request, metadata = self._interceptor.pre_list_connections(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDeveloperConnectRestTransport._BaseListConnections,
                    "_BaseListConnections__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.developerconnect_v1.DeveloperConnectClient.ListConnections",
                    extra={
                        "serviceName": "google.cloud.developerconnect.v1.DeveloperConnect",
                        "rpcName": "ListConnections",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DeveloperConnectRestTransport._ListConnections._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = developer_connect.ListConnectionsResponse()
            pb_resp = developer_connect.ListConnectionsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_connections(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_connections_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        developer_connect.ListConnectionsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.developerconnect_v1.DeveloperConnectClient.list_connections",
                    extra={
                        "serviceName": "google.cloud.developerconnect.v1.DeveloperConnect",
                        "rpcName": "ListConnections",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListGitRepositoryLinks(
        _BaseDeveloperConnectRestTransport._BaseListGitRepositoryLinks,
        DeveloperConnectRestStub,
    ):
        def __hash__(self):
            return hash("DeveloperConnectRestTransport.ListGitRepositoryLinks")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: developer_connect.ListGitRepositoryLinksRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> developer_connect.ListGitRepositoryLinksResponse:
            r"""Call the list git repository links method over HTTP.

            Args:
                request (~.developer_connect.ListGitRepositoryLinksRequest):
                    The request object. Message for requesting a list of
                GitRepositoryLinks
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.developer_connect.ListGitRepositoryLinksResponse:
                    Message for response to listing
                GitRepositoryLinks

            """

            http_options = _BaseDeveloperConnectRestTransport._BaseListGitRepositoryLinks._get_http_options()
            request, metadata = self._interceptor.pre_list_git_repository_links(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDeveloperConnectRestTransport._BaseListGitRepositoryLinks,
                    "_BaseListGitRepositoryLinks__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.developerconnect_v1.DeveloperConnectClient.ListGitRepositoryLinks",
                    extra={
                        "serviceName": "google.cloud.developerconnect.v1.DeveloperConnect",
                        "rpcName": "ListGitRepositoryLinks",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DeveloperConnectRestTransport._ListGitRepositoryLinks._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = developer_connect.ListGitRepositoryLinksResponse()
            pb_resp = developer_connect.ListGitRepositoryLinksResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_git_repository_links(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_git_repository_links_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        developer_connect.ListGitRepositoryLinksResponse.to_json(
                            response
                        )
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.developerconnect_v1.DeveloperConnectClient.list_git_repository_links",
                    extra={
                        "serviceName": "google.cloud.developerconnect.v1.DeveloperConnect",
                        "rpcName": "ListGitRepositoryLinks",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListUsers(
        _BaseDeveloperConnectRestTransport._BaseListUsers, DeveloperConnectRestStub
    ):
        def __hash__(self):
            return hash("DeveloperConnectRestTransport.ListUsers")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: developer_connect.ListUsersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> developer_connect.ListUsersResponse:
            r"""Call the list users method over HTTP.

            Args:
                request (~.developer_connect.ListUsersRequest):
                    The request object. Message for requesting a list of
                Users
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.developer_connect.ListUsersResponse:
                    Message for response to listing Users
            """

            http_options = (
                _BaseDeveloperConnectRestTransport._BaseListUsers._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_users(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDeveloperConnectRestTransport._BaseListUsers,
                    "_BaseListUsers__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.developerconnect_v1.DeveloperConnectClient.ListUsers",
                    extra={
                        "serviceName": "google.cloud.developerconnect.v1.DeveloperConnect",
                        "rpcName": "ListUsers",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DeveloperConnectRestTransport._ListUsers._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = developer_connect.ListUsersResponse()
            pb_resp = developer_connect.ListUsersResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_users(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_users_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = developer_connect.ListUsersResponse.to_json(
                        response
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.developerconnect_v1.DeveloperConnectClient.list_users",
                    extra={
                        "serviceName": "google.cloud.developerconnect.v1.DeveloperConnect",
                        "rpcName": "ListUsers",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _StartOAuth(
        _BaseDeveloperConnectRestTransport._BaseStartOAuth, DeveloperConnectRestStub
    ):
        def __hash__(self):
            return hash("DeveloperConnectRestTransport.StartOAuth")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: developer_connect.StartOAuthRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> developer_connect.StartOAuthResponse:
            r"""Call the start o auth method over HTTP.

            Args:
                request (~.developer_connect.StartOAuthRequest):
                    The request object. Message for starting an OAuth flow.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.developer_connect.StartOAuthResponse:
                    Message for responding to starting an
                OAuth flow.

            """

            http_options = (
                _BaseDeveloperConnectRestTransport._BaseStartOAuth._get_http_options()
            )
            request, metadata = self._interceptor.pre_start_o_auth(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDeveloperConnectRestTransport._BaseStartOAuth,
                    "_BaseStartOAuth__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.developerconnect_v1.DeveloperConnectClient.StartOAuth",
                    extra={
                        "serviceName": "google.cloud.developerconnect.v1.DeveloperConnect",
                        "rpcName": "StartOAuth",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DeveloperConnectRestTransport._StartOAuth._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = developer_connect.StartOAuthResponse()
            pb_resp = developer_connect.StartOAuthResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_start_o_auth(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_start_o_auth_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = developer_connect.StartOAuthResponse.to_json(
                        response
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.developerconnect_v1.DeveloperConnectClient.start_o_auth",
                    extra={
                        "serviceName": "google.cloud.developerconnect.v1.DeveloperConnect",
                        "rpcName": "StartOAuth",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateAccountConnector(
        _BaseDeveloperConnectRestTransport._BaseUpdateAccountConnector,
        DeveloperConnectRestStub,
    ):
        def __hash__(self):
            return hash("DeveloperConnectRestTransport.UpdateAccountConnector")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: developer_connect.UpdateAccountConnectorRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update account connector method over HTTP.

            Args:
                request (~.developer_connect.UpdateAccountConnectorRequest):
                    The request object. Message for updating a
                AccountConnector
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options = _BaseDeveloperConnectRestTransport._BaseUpdateAccountConnector._get_http_options()
            request, metadata = self._interceptor.pre_update_account_connector(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDeveloperConnectRestTransport._BaseUpdateAccountConnector,
                    "_BaseUpdateAccountConnector__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.developerconnect_v1.DeveloperConnectClient.UpdateAccountConnector",
                    extra={
                        "serviceName": "google.cloud.developerconnect.v1.DeveloperConnect",
                        "rpcName": "UpdateAccountConnector",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DeveloperConnectRestTransport._UpdateAccountConnector._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                    body,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_account_connector(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_account_connector_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.developerconnect_v1.DeveloperConnectClient.update_account_connector",
                    extra={
                        "serviceName": "google.cloud.developerconnect.v1.DeveloperConnect",
                        "rpcName": "UpdateAccountConnector",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateConnection(
        _BaseDeveloperConnectRestTransport._BaseUpdateConnection,
        DeveloperConnectRestStub,
    ):
        def __hash__(self):
            return hash("DeveloperConnectRestTransport.UpdateConnection")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: developer_connect.UpdateConnectionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update connection method over HTTP.

            Args:
                request (~.developer_connect.UpdateConnectionRequest):
                    The request object. Message for updating a Connection
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options = _BaseDeveloperConnectRestTransport._BaseUpdateConnection._get_http_options()
            request, metadata = self._interceptor.pre_update_connection(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDeveloperConnectRestTransport._BaseUpdateConnection,
                    "_BaseUpdateConnection__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.developerconnect_v1.DeveloperConnectClient.UpdateConnection",
                    extra={
                        "serviceName": "google.cloud.developerconnect.v1.DeveloperConnect",
                        "rpcName": "UpdateConnection",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DeveloperConnectRestTransport._UpdateConnection._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_connection(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_connection_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.developerconnect_v1.DeveloperConnectClient.update_connection",
                    extra={
                        "serviceName": "google.cloud.developerconnect.v1.DeveloperConnect",
                        "rpcName": "UpdateConnection",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_account_connector(
        self,
    ) -> Callable[
        [developer_connect.CreateAccountConnectorRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateAccountConnector(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_connection(
        self,
    ) -> Callable[
        [developer_connect.CreateConnectionRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateConnection(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_git_repository_link(
        self,
    ) -> Callable[
        [developer_connect.CreateGitRepositoryLinkRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateGitRepositoryLink(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_account_connector(
        self,
    ) -> Callable[
        [developer_connect.DeleteAccountConnectorRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteAccountConnector(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_connection(
        self,
    ) -> Callable[
        [developer_connect.DeleteConnectionRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteConnection(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_git_repository_link(
        self,
    ) -> Callable[
        [developer_connect.DeleteGitRepositoryLinkRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteGitRepositoryLink(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_self(
        self,
    ) -> Callable[[developer_connect.DeleteSelfRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteSelf(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_user(
        self,
    ) -> Callable[[developer_connect.DeleteUserRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteUser(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def fetch_access_token(
        self,
    ) -> Callable[
        [developer_connect.FetchAccessTokenRequest],
        developer_connect.FetchAccessTokenResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._FetchAccessToken(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def fetch_git_hub_installations(
        self,
    ) -> Callable[
        [developer_connect.FetchGitHubInstallationsRequest],
        developer_connect.FetchGitHubInstallationsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._FetchGitHubInstallations(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def fetch_git_refs(
        self,
    ) -> Callable[
        [developer_connect.FetchGitRefsRequest], developer_connect.FetchGitRefsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._FetchGitRefs(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def fetch_linkable_git_repositories(
        self,
    ) -> Callable[
        [developer_connect.FetchLinkableGitRepositoriesRequest],
        developer_connect.FetchLinkableGitRepositoriesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._FetchLinkableGitRepositories(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def fetch_read_token(
        self,
    ) -> Callable[
        [developer_connect.FetchReadTokenRequest],
        developer_connect.FetchReadTokenResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._FetchReadToken(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def fetch_read_write_token(
        self,
    ) -> Callable[
        [developer_connect.FetchReadWriteTokenRequest],
        developer_connect.FetchReadWriteTokenResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._FetchReadWriteToken(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def fetch_self(
        self,
    ) -> Callable[[developer_connect.FetchSelfRequest], developer_connect.User]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._FetchSelf(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def finish_o_auth(
        self,
    ) -> Callable[
        [developer_connect.FinishOAuthRequest], developer_connect.FinishOAuthResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._FinishOAuth(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_account_connector(
        self,
    ) -> Callable[
        [developer_connect.GetAccountConnectorRequest],
        developer_connect.AccountConnector,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetAccountConnector(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_connection(
        self,
    ) -> Callable[
        [developer_connect.GetConnectionRequest], developer_connect.Connection
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetConnection(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_git_repository_link(
        self,
    ) -> Callable[
        [developer_connect.GetGitRepositoryLinkRequest],
        developer_connect.GitRepositoryLink,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetGitRepositoryLink(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_account_connectors(
        self,
    ) -> Callable[
        [developer_connect.ListAccountConnectorsRequest],
        developer_connect.ListAccountConnectorsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListAccountConnectors(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_connections(
        self,
    ) -> Callable[
        [developer_connect.ListConnectionsRequest],
        developer_connect.ListConnectionsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListConnections(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_git_repository_links(
        self,
    ) -> Callable[
        [developer_connect.ListGitRepositoryLinksRequest],
        developer_connect.ListGitRepositoryLinksResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListGitRepositoryLinks(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_users(
        self,
    ) -> Callable[
        [developer_connect.ListUsersRequest], developer_connect.ListUsersResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListUsers(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def start_o_auth(
        self,
    ) -> Callable[
        [developer_connect.StartOAuthRequest], developer_connect.StartOAuthResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._StartOAuth(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_account_connector(
        self,
    ) -> Callable[
        [developer_connect.UpdateAccountConnectorRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateAccountConnector(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_connection(
        self,
    ) -> Callable[
        [developer_connect.UpdateConnectionRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateConnection(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(
        _BaseDeveloperConnectRestTransport._BaseGetLocation, DeveloperConnectRestStub
    ):
        def __hash__(self):
            return hash("DeveloperConnectRestTransport.GetLocation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: locations_pb2.GetLocationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> locations_pb2.Location:
            r"""Call the get location method over HTTP.

            Args:
                request (locations_pb2.GetLocationRequest):
                    The request object for GetLocation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                locations_pb2.Location: Response from GetLocation method.
            """

            http_options = (
                _BaseDeveloperConnectRestTransport._BaseGetLocation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDeveloperConnectRestTransport._BaseGetLocation,
                    "_BaseGetLocation__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = json_format.MessageToJson(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.developerconnect_v1.DeveloperConnectClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.developerconnect.v1.DeveloperConnect",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DeveloperConnectRestTransport._GetLocation._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            content = response.content.decode("utf-8")
            resp = locations_pb2.Location()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_get_location(resp)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.developerconnect_v1.DeveloperConnectAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.developerconnect.v1.DeveloperConnect",
                        "rpcName": "GetLocation",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def list_locations(self):
        return self._ListLocations(self._session, self._host, self._interceptor)  # type: ignore

    class _ListLocations(
        _BaseDeveloperConnectRestTransport._BaseListLocations, DeveloperConnectRestStub
    ):
        def __hash__(self):
            return hash("DeveloperConnectRestTransport.ListLocations")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: locations_pb2.ListLocationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> locations_pb2.ListLocationsResponse:
            r"""Call the list locations method over HTTP.

            Args:
                request (locations_pb2.ListLocationsRequest):
                    The request object for ListLocations method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                locations_pb2.ListLocationsResponse: Response from ListLocations method.
            """

            http_options = _BaseDeveloperConnectRestTransport._BaseListLocations._get_http_options()
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDeveloperConnectRestTransport._BaseListLocations,
                    "_BaseListLocations__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = json_format.MessageToJson(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.developerconnect_v1.DeveloperConnectClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.developerconnect.v1.DeveloperConnect",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DeveloperConnectRestTransport._ListLocations._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            content = response.content.decode("utf-8")
            resp = locations_pb2.ListLocationsResponse()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_list_locations(resp)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.developerconnect_v1.DeveloperConnectAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.developerconnect.v1.DeveloperConnect",
                        "rpcName": "ListLocations",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseDeveloperConnectRestTransport._BaseCancelOperation,
        DeveloperConnectRestStub,
    ):
        def __hash__(self):
            return hash("DeveloperConnectRestTransport.CancelOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: operations_pb2.CancelOperationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> None:
            r"""Call the cancel operation method over HTTP.

            Args:
                request (operations_pb2.CancelOperationRequest):
                    The request object for CancelOperation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseDeveloperConnectRestTransport._BaseCancelOperation._get_http_options()
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDeveloperConnectRestTransport._BaseCancelOperation,
                    "_BaseCancelOperation__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = json_format.MessageToJson(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.developerconnect_v1.DeveloperConnectClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.developerconnect.v1.DeveloperConnect",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DeveloperConnectRestTransport._CancelOperation._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            return self._interceptor.post_cancel_operation(None)

    @property
    def delete_operation(self):
        return self._DeleteOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _DeleteOperation(
        _BaseDeveloperConnectRestTransport._BaseDeleteOperation,
        DeveloperConnectRestStub,
    ):
        def __hash__(self):
            return hash("DeveloperConnectRestTransport.DeleteOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: operations_pb2.DeleteOperationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> None:
            r"""Call the delete operation method over HTTP.

            Args:
                request (operations_pb2.DeleteOperationRequest):
                    The request object for DeleteOperation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseDeveloperConnectRestTransport._BaseDeleteOperation._get_http_options()
            request, metadata = self._interceptor.pre_delete_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDeveloperConnectRestTransport._BaseDeleteOperation,
                    "_BaseDeleteOperation__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = json_format.MessageToJson(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.developerconnect_v1.DeveloperConnectClient.DeleteOperation",
                    extra={
                        "serviceName": "google.cloud.developerconnect.v1.DeveloperConnect",
                        "rpcName": "DeleteOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DeveloperConnectRestTransport._DeleteOperation._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            return self._interceptor.post_delete_operation(None)

    @property
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetOperation(
        _BaseDeveloperConnectRestTransport._BaseGetOperation, DeveloperConnectRestStub
    ):
        def __hash__(self):
            return hash("DeveloperConnectRestTransport.GetOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: operations_pb2.GetOperationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the get operation method over HTTP.

            Args:
                request (operations_pb2.GetOperationRequest):
                    The request object for GetOperation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                operations_pb2.Operation: Response from GetOperation method.
            """

            http_options = (
                _BaseDeveloperConnectRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDeveloperConnectRestTransport._BaseGetOperation,
                    "_BaseGetOperation__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = json_format.MessageToJson(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.developerconnect_v1.DeveloperConnectClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.developerconnect.v1.DeveloperConnect",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DeveloperConnectRestTransport._GetOperation._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            content = response.content.decode("utf-8")
            resp = operations_pb2.Operation()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_get_operation(resp)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.developerconnect_v1.DeveloperConnectAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.developerconnect.v1.DeveloperConnect",
                        "rpcName": "GetOperation",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def list_operations(self):
        return self._ListOperations(self._session, self._host, self._interceptor)  # type: ignore

    class _ListOperations(
        _BaseDeveloperConnectRestTransport._BaseListOperations, DeveloperConnectRestStub
    ):
        def __hash__(self):
            return hash("DeveloperConnectRestTransport.ListOperations")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: operations_pb2.ListOperationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.ListOperationsResponse:
            r"""Call the list operations method over HTTP.

            Args:
                request (operations_pb2.ListOperationsRequest):
                    The request object for ListOperations method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                operations_pb2.ListOperationsResponse: Response from ListOperations method.
            """

            http_options = _BaseDeveloperConnectRestTransport._BaseListOperations._get_http_options()
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDeveloperConnectRestTransport._BaseListOperations,
                    "_BaseListOperations__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = json_format.MessageToJson(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.developerconnect_v1.DeveloperConnectClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.developerconnect.v1.DeveloperConnect",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DeveloperConnectRestTransport._ListOperations._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            content = response.content.decode("utf-8")
            resp = operations_pb2.ListOperationsResponse()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_list_operations(resp)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.developerconnect_v1.DeveloperConnectAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.developerconnect.v1.DeveloperConnect",
                        "rpcName": "ListOperations",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("DeveloperConnectRestTransport",)
