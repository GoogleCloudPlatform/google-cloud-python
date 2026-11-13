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
from google.iam.v1 import (
    iam_policy_pb2,  # type: ignore
    policy_pb2,  # type: ignore
)
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.devtools.cloudbuild_v2._compat import transcode_request
from google.cloud.devtools.cloudbuild_v2.types import repositories

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseRepositoryManagerRestTransport

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


class RepositoryManagerRestInterceptor:
    """Interceptor for RepositoryManager.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the RepositoryManagerRestTransport.

    .. code-block:: python
        class MyCustomRepositoryManagerInterceptor(RepositoryManagerRestInterceptor):
            def pre_batch_create_repositories(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_create_repositories(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_connection(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_connection(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_repository(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_repository(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_connection(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_connection(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_repository(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_repository(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_fetch_git_refs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_fetch_git_refs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_fetch_linkable_repositories(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_fetch_linkable_repositories(self, response):
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

            def pre_get_connection(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_connection(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_repository(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_repository(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_connections(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_connections(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_repositories(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_repositories(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_connection(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_connection(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = RepositoryManagerRestTransport(interceptor=MyCustomRepositoryManagerInterceptor())
        client = RepositoryManagerClient(transport=transport)


    """

    def pre_batch_create_repositories(
        self,
        request: repositories.BatchCreateRepositoriesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        repositories.BatchCreateRepositoriesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_create_repositories

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RepositoryManager server.
        """
        return request, metadata

    def post_batch_create_repositories(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for batch_create_repositories

        DEPRECATED. Please use the `post_batch_create_repositories_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the RepositoryManager server but before
        it is returned to user code. This `post_batch_create_repositories` interceptor runs
        before the `post_batch_create_repositories_with_metadata` interceptor.
        """
        return response

    def post_batch_create_repositories_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for batch_create_repositories

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the RepositoryManager server but before it is returned to user code.

        We recommend only using this `post_batch_create_repositories_with_metadata`
        interceptor in new development instead of the `post_batch_create_repositories` interceptor.
        When both interceptors are used, this `post_batch_create_repositories_with_metadata` interceptor runs after the
        `post_batch_create_repositories` interceptor. The (possibly modified) response returned by
        `post_batch_create_repositories` will be passed to
        `post_batch_create_repositories_with_metadata`.
        """
        return response, metadata

    def pre_create_connection(
        self,
        request: repositories.CreateConnectionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        repositories.CreateConnectionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_connection

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RepositoryManager server.
        """
        return request, metadata

    def post_create_connection(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_connection

        DEPRECATED. Please use the `post_create_connection_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the RepositoryManager server but before
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
        is returned by the RepositoryManager server but before it is returned to user code.

        We recommend only using this `post_create_connection_with_metadata`
        interceptor in new development instead of the `post_create_connection` interceptor.
        When both interceptors are used, this `post_create_connection_with_metadata` interceptor runs after the
        `post_create_connection` interceptor. The (possibly modified) response returned by
        `post_create_connection` will be passed to
        `post_create_connection_with_metadata`.
        """
        return response, metadata

    def pre_create_repository(
        self,
        request: repositories.CreateRepositoryRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        repositories.CreateRepositoryRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_repository

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RepositoryManager server.
        """
        return request, metadata

    def post_create_repository(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_repository

        DEPRECATED. Please use the `post_create_repository_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the RepositoryManager server but before
        it is returned to user code. This `post_create_repository` interceptor runs
        before the `post_create_repository_with_metadata` interceptor.
        """
        return response

    def post_create_repository_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_repository

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the RepositoryManager server but before it is returned to user code.

        We recommend only using this `post_create_repository_with_metadata`
        interceptor in new development instead of the `post_create_repository` interceptor.
        When both interceptors are used, this `post_create_repository_with_metadata` interceptor runs after the
        `post_create_repository` interceptor. The (possibly modified) response returned by
        `post_create_repository` will be passed to
        `post_create_repository_with_metadata`.
        """
        return response, metadata

    def pre_delete_connection(
        self,
        request: repositories.DeleteConnectionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        repositories.DeleteConnectionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_connection

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RepositoryManager server.
        """
        return request, metadata

    def post_delete_connection(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_connection

        DEPRECATED. Please use the `post_delete_connection_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the RepositoryManager server but before
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
        is returned by the RepositoryManager server but before it is returned to user code.

        We recommend only using this `post_delete_connection_with_metadata`
        interceptor in new development instead of the `post_delete_connection` interceptor.
        When both interceptors are used, this `post_delete_connection_with_metadata` interceptor runs after the
        `post_delete_connection` interceptor. The (possibly modified) response returned by
        `post_delete_connection` will be passed to
        `post_delete_connection_with_metadata`.
        """
        return response, metadata

    def pre_delete_repository(
        self,
        request: repositories.DeleteRepositoryRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        repositories.DeleteRepositoryRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_repository

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RepositoryManager server.
        """
        return request, metadata

    def post_delete_repository(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_repository

        DEPRECATED. Please use the `post_delete_repository_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the RepositoryManager server but before
        it is returned to user code. This `post_delete_repository` interceptor runs
        before the `post_delete_repository_with_metadata` interceptor.
        """
        return response

    def post_delete_repository_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_repository

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the RepositoryManager server but before it is returned to user code.

        We recommend only using this `post_delete_repository_with_metadata`
        interceptor in new development instead of the `post_delete_repository` interceptor.
        When both interceptors are used, this `post_delete_repository_with_metadata` interceptor runs after the
        `post_delete_repository` interceptor. The (possibly modified) response returned by
        `post_delete_repository` will be passed to
        `post_delete_repository_with_metadata`.
        """
        return response, metadata

    def pre_fetch_git_refs(
        self,
        request: repositories.FetchGitRefsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        repositories.FetchGitRefsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for fetch_git_refs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RepositoryManager server.
        """
        return request, metadata

    def post_fetch_git_refs(
        self, response: repositories.FetchGitRefsResponse
    ) -> repositories.FetchGitRefsResponse:
        """Post-rpc interceptor for fetch_git_refs

        DEPRECATED. Please use the `post_fetch_git_refs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the RepositoryManager server but before
        it is returned to user code. This `post_fetch_git_refs` interceptor runs
        before the `post_fetch_git_refs_with_metadata` interceptor.
        """
        return response

    def post_fetch_git_refs_with_metadata(
        self,
        response: repositories.FetchGitRefsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        repositories.FetchGitRefsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for fetch_git_refs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the RepositoryManager server but before it is returned to user code.

        We recommend only using this `post_fetch_git_refs_with_metadata`
        interceptor in new development instead of the `post_fetch_git_refs` interceptor.
        When both interceptors are used, this `post_fetch_git_refs_with_metadata` interceptor runs after the
        `post_fetch_git_refs` interceptor. The (possibly modified) response returned by
        `post_fetch_git_refs` will be passed to
        `post_fetch_git_refs_with_metadata`.
        """
        return response, metadata

    def pre_fetch_linkable_repositories(
        self,
        request: repositories.FetchLinkableRepositoriesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        repositories.FetchLinkableRepositoriesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for fetch_linkable_repositories

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RepositoryManager server.
        """
        return request, metadata

    def post_fetch_linkable_repositories(
        self, response: repositories.FetchLinkableRepositoriesResponse
    ) -> repositories.FetchLinkableRepositoriesResponse:
        """Post-rpc interceptor for fetch_linkable_repositories

        DEPRECATED. Please use the `post_fetch_linkable_repositories_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the RepositoryManager server but before
        it is returned to user code. This `post_fetch_linkable_repositories` interceptor runs
        before the `post_fetch_linkable_repositories_with_metadata` interceptor.
        """
        return response

    def post_fetch_linkable_repositories_with_metadata(
        self,
        response: repositories.FetchLinkableRepositoriesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        repositories.FetchLinkableRepositoriesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for fetch_linkable_repositories

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the RepositoryManager server but before it is returned to user code.

        We recommend only using this `post_fetch_linkable_repositories_with_metadata`
        interceptor in new development instead of the `post_fetch_linkable_repositories` interceptor.
        When both interceptors are used, this `post_fetch_linkable_repositories_with_metadata` interceptor runs after the
        `post_fetch_linkable_repositories` interceptor. The (possibly modified) response returned by
        `post_fetch_linkable_repositories` will be passed to
        `post_fetch_linkable_repositories_with_metadata`.
        """
        return response, metadata

    def pre_fetch_read_token(
        self,
        request: repositories.FetchReadTokenRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        repositories.FetchReadTokenRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for fetch_read_token

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RepositoryManager server.
        """
        return request, metadata

    def post_fetch_read_token(
        self, response: repositories.FetchReadTokenResponse
    ) -> repositories.FetchReadTokenResponse:
        """Post-rpc interceptor for fetch_read_token

        DEPRECATED. Please use the `post_fetch_read_token_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the RepositoryManager server but before
        it is returned to user code. This `post_fetch_read_token` interceptor runs
        before the `post_fetch_read_token_with_metadata` interceptor.
        """
        return response

    def post_fetch_read_token_with_metadata(
        self,
        response: repositories.FetchReadTokenResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        repositories.FetchReadTokenResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for fetch_read_token

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the RepositoryManager server but before it is returned to user code.

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
        request: repositories.FetchReadWriteTokenRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        repositories.FetchReadWriteTokenRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for fetch_read_write_token

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RepositoryManager server.
        """
        return request, metadata

    def post_fetch_read_write_token(
        self, response: repositories.FetchReadWriteTokenResponse
    ) -> repositories.FetchReadWriteTokenResponse:
        """Post-rpc interceptor for fetch_read_write_token

        DEPRECATED. Please use the `post_fetch_read_write_token_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the RepositoryManager server but before
        it is returned to user code. This `post_fetch_read_write_token` interceptor runs
        before the `post_fetch_read_write_token_with_metadata` interceptor.
        """
        return response

    def post_fetch_read_write_token_with_metadata(
        self,
        response: repositories.FetchReadWriteTokenResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        repositories.FetchReadWriteTokenResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for fetch_read_write_token

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the RepositoryManager server but before it is returned to user code.

        We recommend only using this `post_fetch_read_write_token_with_metadata`
        interceptor in new development instead of the `post_fetch_read_write_token` interceptor.
        When both interceptors are used, this `post_fetch_read_write_token_with_metadata` interceptor runs after the
        `post_fetch_read_write_token` interceptor. The (possibly modified) response returned by
        `post_fetch_read_write_token` will be passed to
        `post_fetch_read_write_token_with_metadata`.
        """
        return response, metadata

    def pre_get_connection(
        self,
        request: repositories.GetConnectionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        repositories.GetConnectionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_connection

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RepositoryManager server.
        """
        return request, metadata

    def post_get_connection(
        self, response: repositories.Connection
    ) -> repositories.Connection:
        """Post-rpc interceptor for get_connection

        DEPRECATED. Please use the `post_get_connection_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the RepositoryManager server but before
        it is returned to user code. This `post_get_connection` interceptor runs
        before the `post_get_connection_with_metadata` interceptor.
        """
        return response

    def post_get_connection_with_metadata(
        self,
        response: repositories.Connection,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[repositories.Connection, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_connection

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the RepositoryManager server but before it is returned to user code.

        We recommend only using this `post_get_connection_with_metadata`
        interceptor in new development instead of the `post_get_connection` interceptor.
        When both interceptors are used, this `post_get_connection_with_metadata` interceptor runs after the
        `post_get_connection` interceptor. The (possibly modified) response returned by
        `post_get_connection` will be passed to
        `post_get_connection_with_metadata`.
        """
        return response, metadata

    def pre_get_repository(
        self,
        request: repositories.GetRepositoryRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        repositories.GetRepositoryRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_repository

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RepositoryManager server.
        """
        return request, metadata

    def post_get_repository(
        self, response: repositories.Repository
    ) -> repositories.Repository:
        """Post-rpc interceptor for get_repository

        DEPRECATED. Please use the `post_get_repository_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the RepositoryManager server but before
        it is returned to user code. This `post_get_repository` interceptor runs
        before the `post_get_repository_with_metadata` interceptor.
        """
        return response

    def post_get_repository_with_metadata(
        self,
        response: repositories.Repository,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[repositories.Repository, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_repository

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the RepositoryManager server but before it is returned to user code.

        We recommend only using this `post_get_repository_with_metadata`
        interceptor in new development instead of the `post_get_repository` interceptor.
        When both interceptors are used, this `post_get_repository_with_metadata` interceptor runs after the
        `post_get_repository` interceptor. The (possibly modified) response returned by
        `post_get_repository` will be passed to
        `post_get_repository_with_metadata`.
        """
        return response, metadata

    def pre_list_connections(
        self,
        request: repositories.ListConnectionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        repositories.ListConnectionsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_connections

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RepositoryManager server.
        """
        return request, metadata

    def post_list_connections(
        self, response: repositories.ListConnectionsResponse
    ) -> repositories.ListConnectionsResponse:
        """Post-rpc interceptor for list_connections

        DEPRECATED. Please use the `post_list_connections_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the RepositoryManager server but before
        it is returned to user code. This `post_list_connections` interceptor runs
        before the `post_list_connections_with_metadata` interceptor.
        """
        return response

    def post_list_connections_with_metadata(
        self,
        response: repositories.ListConnectionsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        repositories.ListConnectionsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_connections

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the RepositoryManager server but before it is returned to user code.

        We recommend only using this `post_list_connections_with_metadata`
        interceptor in new development instead of the `post_list_connections` interceptor.
        When both interceptors are used, this `post_list_connections_with_metadata` interceptor runs after the
        `post_list_connections` interceptor. The (possibly modified) response returned by
        `post_list_connections` will be passed to
        `post_list_connections_with_metadata`.
        """
        return response, metadata

    def pre_list_repositories(
        self,
        request: repositories.ListRepositoriesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        repositories.ListRepositoriesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_repositories

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RepositoryManager server.
        """
        return request, metadata

    def post_list_repositories(
        self, response: repositories.ListRepositoriesResponse
    ) -> repositories.ListRepositoriesResponse:
        """Post-rpc interceptor for list_repositories

        DEPRECATED. Please use the `post_list_repositories_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the RepositoryManager server but before
        it is returned to user code. This `post_list_repositories` interceptor runs
        before the `post_list_repositories_with_metadata` interceptor.
        """
        return response

    def post_list_repositories_with_metadata(
        self,
        response: repositories.ListRepositoriesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        repositories.ListRepositoriesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_repositories

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the RepositoryManager server but before it is returned to user code.

        We recommend only using this `post_list_repositories_with_metadata`
        interceptor in new development instead of the `post_list_repositories` interceptor.
        When both interceptors are used, this `post_list_repositories_with_metadata` interceptor runs after the
        `post_list_repositories` interceptor. The (possibly modified) response returned by
        `post_list_repositories` will be passed to
        `post_list_repositories_with_metadata`.
        """
        return response, metadata

    def pre_update_connection(
        self,
        request: repositories.UpdateConnectionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        repositories.UpdateConnectionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_connection

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RepositoryManager server.
        """
        return request, metadata

    def post_update_connection(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_connection

        DEPRECATED. Please use the `post_update_connection_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the RepositoryManager server but before
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
        is returned by the RepositoryManager server but before it is returned to user code.

        We recommend only using this `post_update_connection_with_metadata`
        interceptor in new development instead of the `post_update_connection` interceptor.
        When both interceptors are used, this `post_update_connection_with_metadata` interceptor runs after the
        `post_update_connection` interceptor. The (possibly modified) response returned by
        `post_update_connection` will be passed to
        `post_update_connection_with_metadata`.
        """
        return response, metadata

    def pre_get_iam_policy(
        self,
        request: iam_policy_pb2.GetIamPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        iam_policy_pb2.GetIamPolicyRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_iam_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RepositoryManager server.
        """
        return request, metadata

    def post_get_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for get_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the RepositoryManager server but before
        it is returned to user code.
        """
        return response

    def pre_set_iam_policy(
        self,
        request: iam_policy_pb2.SetIamPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        iam_policy_pb2.SetIamPolicyRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for set_iam_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RepositoryManager server.
        """
        return request, metadata

    def post_set_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for set_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the RepositoryManager server but before
        it is returned to user code.
        """
        return response

    def pre_test_iam_permissions(
        self,
        request: iam_policy_pb2.TestIamPermissionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        iam_policy_pb2.TestIamPermissionsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for test_iam_permissions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RepositoryManager server.
        """
        return request, metadata

    def post_test_iam_permissions(
        self, response: iam_policy_pb2.TestIamPermissionsResponse
    ) -> iam_policy_pb2.TestIamPermissionsResponse:
        """Post-rpc interceptor for test_iam_permissions

        Override in a subclass to manipulate the response
        after it is returned by the RepositoryManager server but before
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
        before they are sent to the RepositoryManager server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the RepositoryManager server but before
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
        before they are sent to the RepositoryManager server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the RepositoryManager server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class RepositoryManagerRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: RepositoryManagerRestInterceptor


class RepositoryManagerRestTransport(_BaseRepositoryManagerRestTransport):
    """REST backend synchronous transport for RepositoryManager.

    Manages connections to source code repositories.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "cloudbuild.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[RepositoryManagerRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'cloudbuild.googleapis.com').
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
            interceptor (Optional[RepositoryManagerRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or RepositoryManagerRestInterceptor()
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
                        "uri": "/v2/{name=projects/*/locations/*/operations/*}:cancel",
                        "body": "*",
                    },
                ],
                "google.longrunning.Operations.GetOperation": [
                    {
                        "method": "get",
                        "uri": "/v2/{name=projects/*/locations/*/operations/*}",
                    },
                ],
            }

            rest_transport = operations_v1.OperationsRestTransport(
                host=self._host,
                # use the credentials which are saved
                credentials=self._credentials,
                scopes=self._scopes,
                http_options=http_options,
                path_prefix="v2",
            )

            self._operations_client = operations_v1.AbstractOperationsClient(
                transport=rest_transport
            )

        # Return the client from cache.
        return self._operations_client

    class _BatchCreateRepositories(
        _BaseRepositoryManagerRestTransport._BaseBatchCreateRepositories,
        RepositoryManagerRestStub,
    ):
        def __hash__(self):
            return hash("RepositoryManagerRestTransport.BatchCreateRepositories")

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
            request: repositories.BatchCreateRepositoriesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the batch create repositories method over HTTP.

            Args:
                request (~.repositories.BatchCreateRepositoriesRequest):
                    The request object. Message for creating repositoritories
                in batch.
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

            http_options = _BaseRepositoryManagerRestTransport._BaseBatchCreateRepositories._get_http_options()
            request, metadata = self._interceptor.pre_batch_create_repositories(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRepositoryManagerRestTransport._BaseBatchCreateRepositories,
                    "_BaseBatchCreateRepositories__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devtools.cloudbuild_v2.RepositoryManagerClient.BatchCreateRepositories",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v2.RepositoryManager",
                        "rpcName": "BatchCreateRepositories",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                RepositoryManagerRestTransport._BatchCreateRepositories._get_response(
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

            resp = self._interceptor.post_batch_create_repositories(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_create_repositories_with_metadata(
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
                    "Received response for google.devtools.cloudbuild_v2.RepositoryManagerClient.batch_create_repositories",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v2.RepositoryManager",
                        "rpcName": "BatchCreateRepositories",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateConnection(
        _BaseRepositoryManagerRestTransport._BaseCreateConnection,
        RepositoryManagerRestStub,
    ):
        def __hash__(self):
            return hash("RepositoryManagerRestTransport.CreateConnection")

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
            request: repositories.CreateConnectionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create connection method over HTTP.

            Args:
                request (~.repositories.CreateConnectionRequest):
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

            http_options = _BaseRepositoryManagerRestTransport._BaseCreateConnection._get_http_options()
            request, metadata = self._interceptor.pre_create_connection(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRepositoryManagerRestTransport._BaseCreateConnection,
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
                    f"Sending request for google.devtools.cloudbuild_v2.RepositoryManagerClient.CreateConnection",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v2.RepositoryManager",
                        "rpcName": "CreateConnection",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RepositoryManagerRestTransport._CreateConnection._get_response(
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
                    "Received response for google.devtools.cloudbuild_v2.RepositoryManagerClient.create_connection",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v2.RepositoryManager",
                        "rpcName": "CreateConnection",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateRepository(
        _BaseRepositoryManagerRestTransport._BaseCreateRepository,
        RepositoryManagerRestStub,
    ):
        def __hash__(self):
            return hash("RepositoryManagerRestTransport.CreateRepository")

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
            request: repositories.CreateRepositoryRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create repository method over HTTP.

            Args:
                request (~.repositories.CreateRepositoryRequest):
                    The request object. Message for creating a Repository.
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

            http_options = _BaseRepositoryManagerRestTransport._BaseCreateRepository._get_http_options()
            request, metadata = self._interceptor.pre_create_repository(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRepositoryManagerRestTransport._BaseCreateRepository,
                    "_BaseCreateRepository__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devtools.cloudbuild_v2.RepositoryManagerClient.CreateRepository",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v2.RepositoryManager",
                        "rpcName": "CreateRepository",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RepositoryManagerRestTransport._CreateRepository._get_response(
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

            resp = self._interceptor.post_create_repository(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_repository_with_metadata(
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
                    "Received response for google.devtools.cloudbuild_v2.RepositoryManagerClient.create_repository",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v2.RepositoryManager",
                        "rpcName": "CreateRepository",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteConnection(
        _BaseRepositoryManagerRestTransport._BaseDeleteConnection,
        RepositoryManagerRestStub,
    ):
        def __hash__(self):
            return hash("RepositoryManagerRestTransport.DeleteConnection")

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
            request: repositories.DeleteConnectionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete connection method over HTTP.

            Args:
                request (~.repositories.DeleteConnectionRequest):
                    The request object. Message for deleting a Connection.
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

            http_options = _BaseRepositoryManagerRestTransport._BaseDeleteConnection._get_http_options()
            request, metadata = self._interceptor.pre_delete_connection(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRepositoryManagerRestTransport._BaseDeleteConnection,
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
                    f"Sending request for google.devtools.cloudbuild_v2.RepositoryManagerClient.DeleteConnection",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v2.RepositoryManager",
                        "rpcName": "DeleteConnection",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RepositoryManagerRestTransport._DeleteConnection._get_response(
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
                    "Received response for google.devtools.cloudbuild_v2.RepositoryManagerClient.delete_connection",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v2.RepositoryManager",
                        "rpcName": "DeleteConnection",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteRepository(
        _BaseRepositoryManagerRestTransport._BaseDeleteRepository,
        RepositoryManagerRestStub,
    ):
        def __hash__(self):
            return hash("RepositoryManagerRestTransport.DeleteRepository")

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
            request: repositories.DeleteRepositoryRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete repository method over HTTP.

            Args:
                request (~.repositories.DeleteRepositoryRequest):
                    The request object. Message for deleting a Repository.
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

            http_options = _BaseRepositoryManagerRestTransport._BaseDeleteRepository._get_http_options()
            request, metadata = self._interceptor.pre_delete_repository(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRepositoryManagerRestTransport._BaseDeleteRepository,
                    "_BaseDeleteRepository__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devtools.cloudbuild_v2.RepositoryManagerClient.DeleteRepository",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v2.RepositoryManager",
                        "rpcName": "DeleteRepository",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RepositoryManagerRestTransport._DeleteRepository._get_response(
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

            resp = self._interceptor.post_delete_repository(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_repository_with_metadata(
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
                    "Received response for google.devtools.cloudbuild_v2.RepositoryManagerClient.delete_repository",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v2.RepositoryManager",
                        "rpcName": "DeleteRepository",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _FetchGitRefs(
        _BaseRepositoryManagerRestTransport._BaseFetchGitRefs, RepositoryManagerRestStub
    ):
        def __hash__(self):
            return hash("RepositoryManagerRestTransport.FetchGitRefs")

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
            request: repositories.FetchGitRefsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> repositories.FetchGitRefsResponse:
            r"""Call the fetch git refs method over HTTP.

            Args:
                request (~.repositories.FetchGitRefsRequest):
                    The request object. Request for fetching git refs
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.repositories.FetchGitRefsResponse:
                    Response for fetching git refs
            """

            http_options = _BaseRepositoryManagerRestTransport._BaseFetchGitRefs._get_http_options()
            request, metadata = self._interceptor.pre_fetch_git_refs(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRepositoryManagerRestTransport._BaseFetchGitRefs,
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
                    f"Sending request for google.devtools.cloudbuild_v2.RepositoryManagerClient.FetchGitRefs",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v2.RepositoryManager",
                        "rpcName": "FetchGitRefs",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RepositoryManagerRestTransport._FetchGitRefs._get_response(
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
            resp = repositories.FetchGitRefsResponse()
            pb_resp = repositories.FetchGitRefsResponse.pb(resp)

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
                    response_payload = repositories.FetchGitRefsResponse.to_json(
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
                    "Received response for google.devtools.cloudbuild_v2.RepositoryManagerClient.fetch_git_refs",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v2.RepositoryManager",
                        "rpcName": "FetchGitRefs",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _FetchLinkableRepositories(
        _BaseRepositoryManagerRestTransport._BaseFetchLinkableRepositories,
        RepositoryManagerRestStub,
    ):
        def __hash__(self):
            return hash("RepositoryManagerRestTransport.FetchLinkableRepositories")

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
            request: repositories.FetchLinkableRepositoriesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> repositories.FetchLinkableRepositoriesResponse:
            r"""Call the fetch linkable
            repositories method over HTTP.

                Args:
                    request (~.repositories.FetchLinkableRepositoriesRequest):
                        The request object. Request message for
                    FetchLinkableRepositories.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.repositories.FetchLinkableRepositoriesResponse:
                        Response message for
                    FetchLinkableRepositories.

            """

            http_options = _BaseRepositoryManagerRestTransport._BaseFetchLinkableRepositories._get_http_options()
            request, metadata = self._interceptor.pre_fetch_linkable_repositories(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRepositoryManagerRestTransport._BaseFetchLinkableRepositories,
                    "_BaseFetchLinkableRepositories__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devtools.cloudbuild_v2.RepositoryManagerClient.FetchLinkableRepositories",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v2.RepositoryManager",
                        "rpcName": "FetchLinkableRepositories",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                RepositoryManagerRestTransport._FetchLinkableRepositories._get_response(
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
            resp = repositories.FetchLinkableRepositoriesResponse()
            pb_resp = repositories.FetchLinkableRepositoriesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_fetch_linkable_repositories(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_fetch_linkable_repositories_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        repositories.FetchLinkableRepositoriesResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.devtools.cloudbuild_v2.RepositoryManagerClient.fetch_linkable_repositories",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v2.RepositoryManager",
                        "rpcName": "FetchLinkableRepositories",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _FetchReadToken(
        _BaseRepositoryManagerRestTransport._BaseFetchReadToken,
        RepositoryManagerRestStub,
    ):
        def __hash__(self):
            return hash("RepositoryManagerRestTransport.FetchReadToken")

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
            request: repositories.FetchReadTokenRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> repositories.FetchReadTokenResponse:
            r"""Call the fetch read token method over HTTP.

            Args:
                request (~.repositories.FetchReadTokenRequest):
                    The request object. Message for fetching SCM read token.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.repositories.FetchReadTokenResponse:
                    Message for responding to get read
                token.

            """

            http_options = _BaseRepositoryManagerRestTransport._BaseFetchReadToken._get_http_options()
            request, metadata = self._interceptor.pre_fetch_read_token(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRepositoryManagerRestTransport._BaseFetchReadToken,
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
                    f"Sending request for google.devtools.cloudbuild_v2.RepositoryManagerClient.FetchReadToken",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v2.RepositoryManager",
                        "rpcName": "FetchReadToken",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RepositoryManagerRestTransport._FetchReadToken._get_response(
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
            resp = repositories.FetchReadTokenResponse()
            pb_resp = repositories.FetchReadTokenResponse.pb(resp)

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
                    response_payload = repositories.FetchReadTokenResponse.to_json(
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
                    "Received response for google.devtools.cloudbuild_v2.RepositoryManagerClient.fetch_read_token",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v2.RepositoryManager",
                        "rpcName": "FetchReadToken",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _FetchReadWriteToken(
        _BaseRepositoryManagerRestTransport._BaseFetchReadWriteToken,
        RepositoryManagerRestStub,
    ):
        def __hash__(self):
            return hash("RepositoryManagerRestTransport.FetchReadWriteToken")

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
            request: repositories.FetchReadWriteTokenRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> repositories.FetchReadWriteTokenResponse:
            r"""Call the fetch read write token method over HTTP.

            Args:
                request (~.repositories.FetchReadWriteTokenRequest):
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
                ~.repositories.FetchReadWriteTokenResponse:
                    Message for responding to get
                read/write token.

            """

            http_options = _BaseRepositoryManagerRestTransport._BaseFetchReadWriteToken._get_http_options()
            request, metadata = self._interceptor.pre_fetch_read_write_token(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRepositoryManagerRestTransport._BaseFetchReadWriteToken,
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
                    f"Sending request for google.devtools.cloudbuild_v2.RepositoryManagerClient.FetchReadWriteToken",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v2.RepositoryManager",
                        "rpcName": "FetchReadWriteToken",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                RepositoryManagerRestTransport._FetchReadWriteToken._get_response(
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
            resp = repositories.FetchReadWriteTokenResponse()
            pb_resp = repositories.FetchReadWriteTokenResponse.pb(resp)

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
                    response_payload = repositories.FetchReadWriteTokenResponse.to_json(
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
                    "Received response for google.devtools.cloudbuild_v2.RepositoryManagerClient.fetch_read_write_token",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v2.RepositoryManager",
                        "rpcName": "FetchReadWriteToken",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetConnection(
        _BaseRepositoryManagerRestTransport._BaseGetConnection,
        RepositoryManagerRestStub,
    ):
        def __hash__(self):
            return hash("RepositoryManagerRestTransport.GetConnection")

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
            request: repositories.GetConnectionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> repositories.Connection:
            r"""Call the get connection method over HTTP.

            Args:
                request (~.repositories.GetConnectionRequest):
                    The request object. Message for getting the details of a
                Connection.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.repositories.Connection:
                    A connection to a SCM like GitHub,
                GitHub Enterprise, Bitbucket Data
                Center, Bitbucket Cloud or GitLab.

            """

            http_options = _BaseRepositoryManagerRestTransport._BaseGetConnection._get_http_options()
            request, metadata = self._interceptor.pre_get_connection(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRepositoryManagerRestTransport._BaseGetConnection,
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
                    f"Sending request for google.devtools.cloudbuild_v2.RepositoryManagerClient.GetConnection",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v2.RepositoryManager",
                        "rpcName": "GetConnection",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RepositoryManagerRestTransport._GetConnection._get_response(
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
            resp = repositories.Connection()
            pb_resp = repositories.Connection.pb(resp)

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
                    response_payload = repositories.Connection.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.devtools.cloudbuild_v2.RepositoryManagerClient.get_connection",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v2.RepositoryManager",
                        "rpcName": "GetConnection",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetRepository(
        _BaseRepositoryManagerRestTransport._BaseGetRepository,
        RepositoryManagerRestStub,
    ):
        def __hash__(self):
            return hash("RepositoryManagerRestTransport.GetRepository")

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
            request: repositories.GetRepositoryRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> repositories.Repository:
            r"""Call the get repository method over HTTP.

            Args:
                request (~.repositories.GetRepositoryRequest):
                    The request object. Message for getting the details of a
                Repository.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.repositories.Repository:
                    A repository associated to a parent
                connection.

            """

            http_options = _BaseRepositoryManagerRestTransport._BaseGetRepository._get_http_options()
            request, metadata = self._interceptor.pre_get_repository(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRepositoryManagerRestTransport._BaseGetRepository,
                    "_BaseGetRepository__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devtools.cloudbuild_v2.RepositoryManagerClient.GetRepository",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v2.RepositoryManager",
                        "rpcName": "GetRepository",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RepositoryManagerRestTransport._GetRepository._get_response(
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
            resp = repositories.Repository()
            pb_resp = repositories.Repository.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_repository(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_repository_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = repositories.Repository.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.devtools.cloudbuild_v2.RepositoryManagerClient.get_repository",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v2.RepositoryManager",
                        "rpcName": "GetRepository",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListConnections(
        _BaseRepositoryManagerRestTransport._BaseListConnections,
        RepositoryManagerRestStub,
    ):
        def __hash__(self):
            return hash("RepositoryManagerRestTransport.ListConnections")

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
            request: repositories.ListConnectionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> repositories.ListConnectionsResponse:
            r"""Call the list connections method over HTTP.

            Args:
                request (~.repositories.ListConnectionsRequest):
                    The request object. Message for requesting list of
                Connections.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.repositories.ListConnectionsResponse:
                    Message for response to listing
                Connections.

            """

            http_options = _BaseRepositoryManagerRestTransport._BaseListConnections._get_http_options()
            request, metadata = self._interceptor.pre_list_connections(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRepositoryManagerRestTransport._BaseListConnections,
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
                    f"Sending request for google.devtools.cloudbuild_v2.RepositoryManagerClient.ListConnections",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v2.RepositoryManager",
                        "rpcName": "ListConnections",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RepositoryManagerRestTransport._ListConnections._get_response(
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
            resp = repositories.ListConnectionsResponse()
            pb_resp = repositories.ListConnectionsResponse.pb(resp)

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
                    response_payload = repositories.ListConnectionsResponse.to_json(
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
                    "Received response for google.devtools.cloudbuild_v2.RepositoryManagerClient.list_connections",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v2.RepositoryManager",
                        "rpcName": "ListConnections",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListRepositories(
        _BaseRepositoryManagerRestTransport._BaseListRepositories,
        RepositoryManagerRestStub,
    ):
        def __hash__(self):
            return hash("RepositoryManagerRestTransport.ListRepositories")

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
            request: repositories.ListRepositoriesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> repositories.ListRepositoriesResponse:
            r"""Call the list repositories method over HTTP.

            Args:
                request (~.repositories.ListRepositoriesRequest):
                    The request object. Message for requesting list of
                Repositories.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.repositories.ListRepositoriesResponse:
                    Message for response to listing
                Repositories.

            """

            http_options = _BaseRepositoryManagerRestTransport._BaseListRepositories._get_http_options()
            request, metadata = self._interceptor.pre_list_repositories(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRepositoryManagerRestTransport._BaseListRepositories,
                    "_BaseListRepositories__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devtools.cloudbuild_v2.RepositoryManagerClient.ListRepositories",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v2.RepositoryManager",
                        "rpcName": "ListRepositories",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RepositoryManagerRestTransport._ListRepositories._get_response(
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
            resp = repositories.ListRepositoriesResponse()
            pb_resp = repositories.ListRepositoriesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_repositories(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_repositories_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = repositories.ListRepositoriesResponse.to_json(
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
                    "Received response for google.devtools.cloudbuild_v2.RepositoryManagerClient.list_repositories",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v2.RepositoryManager",
                        "rpcName": "ListRepositories",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateConnection(
        _BaseRepositoryManagerRestTransport._BaseUpdateConnection,
        RepositoryManagerRestStub,
    ):
        def __hash__(self):
            return hash("RepositoryManagerRestTransport.UpdateConnection")

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
            request: repositories.UpdateConnectionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update connection method over HTTP.

            Args:
                request (~.repositories.UpdateConnectionRequest):
                    The request object. Message for updating a Connection.
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

            http_options = _BaseRepositoryManagerRestTransport._BaseUpdateConnection._get_http_options()
            request, metadata = self._interceptor.pre_update_connection(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRepositoryManagerRestTransport._BaseUpdateConnection,
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
                    f"Sending request for google.devtools.cloudbuild_v2.RepositoryManagerClient.UpdateConnection",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v2.RepositoryManager",
                        "rpcName": "UpdateConnection",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RepositoryManagerRestTransport._UpdateConnection._get_response(
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
                    "Received response for google.devtools.cloudbuild_v2.RepositoryManagerClient.update_connection",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v2.RepositoryManager",
                        "rpcName": "UpdateConnection",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def batch_create_repositories(
        self,
    ) -> Callable[
        [repositories.BatchCreateRepositoriesRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchCreateRepositories(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_connection(
        self,
    ) -> Callable[[repositories.CreateConnectionRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateConnection(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_repository(
        self,
    ) -> Callable[[repositories.CreateRepositoryRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateRepository(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_connection(
        self,
    ) -> Callable[[repositories.DeleteConnectionRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteConnection(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_repository(
        self,
    ) -> Callable[[repositories.DeleteRepositoryRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteRepository(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def fetch_git_refs(
        self,
    ) -> Callable[
        [repositories.FetchGitRefsRequest], repositories.FetchGitRefsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._FetchGitRefs(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def fetch_linkable_repositories(
        self,
    ) -> Callable[
        [repositories.FetchLinkableRepositoriesRequest],
        repositories.FetchLinkableRepositoriesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._FetchLinkableRepositories(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def fetch_read_token(
        self,
    ) -> Callable[
        [repositories.FetchReadTokenRequest], repositories.FetchReadTokenResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._FetchReadToken(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def fetch_read_write_token(
        self,
    ) -> Callable[
        [repositories.FetchReadWriteTokenRequest],
        repositories.FetchReadWriteTokenResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._FetchReadWriteToken(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_connection(
        self,
    ) -> Callable[[repositories.GetConnectionRequest], repositories.Connection]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetConnection(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_repository(
        self,
    ) -> Callable[[repositories.GetRepositoryRequest], repositories.Repository]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetRepository(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_connections(
        self,
    ) -> Callable[
        [repositories.ListConnectionsRequest], repositories.ListConnectionsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListConnections(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_repositories(
        self,
    ) -> Callable[
        [repositories.ListRepositoriesRequest], repositories.ListRepositoriesResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListRepositories(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_connection(
        self,
    ) -> Callable[[repositories.UpdateConnectionRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateConnection(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_iam_policy(self):
        return self._GetIamPolicy(self._session, self._host, self._interceptor)  # type: ignore

    class _GetIamPolicy(
        _BaseRepositoryManagerRestTransport._BaseGetIamPolicy, RepositoryManagerRestStub
    ):
        def __hash__(self):
            return hash("RepositoryManagerRestTransport.GetIamPolicy")

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
            request: iam_policy_pb2.GetIamPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> policy_pb2.Policy:
            r"""Call the get iam policy method over HTTP.

            Args:
                request (iam_policy_pb2.GetIamPolicyRequest):
                    The request object for GetIamPolicy method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                policy_pb2.Policy: Response from GetIamPolicy method.
            """

            http_options = _BaseRepositoryManagerRestTransport._BaseGetIamPolicy._get_http_options()
            request, metadata = self._interceptor.pre_get_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRepositoryManagerRestTransport._BaseGetIamPolicy,
                    "_BaseGetIamPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devtools.cloudbuild_v2.RepositoryManagerClient.GetIamPolicy",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v2.RepositoryManager",
                        "rpcName": "GetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RepositoryManagerRestTransport._GetIamPolicy._get_response(
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
            resp = policy_pb2.Policy()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_get_iam_policy(resp)
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
                    "Received response for google.devtools.cloudbuild_v2.RepositoryManagerAsyncClient.GetIamPolicy",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v2.RepositoryManager",
                        "rpcName": "GetIamPolicy",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def set_iam_policy(self):
        return self._SetIamPolicy(self._session, self._host, self._interceptor)  # type: ignore

    class _SetIamPolicy(
        _BaseRepositoryManagerRestTransport._BaseSetIamPolicy, RepositoryManagerRestStub
    ):
        def __hash__(self):
            return hash("RepositoryManagerRestTransport.SetIamPolicy")

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
            request: iam_policy_pb2.SetIamPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> policy_pb2.Policy:
            r"""Call the set iam policy method over HTTP.

            Args:
                request (iam_policy_pb2.SetIamPolicyRequest):
                    The request object for SetIamPolicy method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                policy_pb2.Policy: Response from SetIamPolicy method.
            """

            http_options = _BaseRepositoryManagerRestTransport._BaseSetIamPolicy._get_http_options()
            request, metadata = self._interceptor.pre_set_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRepositoryManagerRestTransport._BaseSetIamPolicy,
                    "_BaseSetIamPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devtools.cloudbuild_v2.RepositoryManagerClient.SetIamPolicy",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v2.RepositoryManager",
                        "rpcName": "SetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RepositoryManagerRestTransport._SetIamPolicy._get_response(
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

            content = response.content.decode("utf-8")
            resp = policy_pb2.Policy()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_set_iam_policy(resp)
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
                    "Received response for google.devtools.cloudbuild_v2.RepositoryManagerAsyncClient.SetIamPolicy",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v2.RepositoryManager",
                        "rpcName": "SetIamPolicy",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def test_iam_permissions(self):
        return self._TestIamPermissions(self._session, self._host, self._interceptor)  # type: ignore

    class _TestIamPermissions(
        _BaseRepositoryManagerRestTransport._BaseTestIamPermissions,
        RepositoryManagerRestStub,
    ):
        def __hash__(self):
            return hash("RepositoryManagerRestTransport.TestIamPermissions")

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
            request: iam_policy_pb2.TestIamPermissionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> iam_policy_pb2.TestIamPermissionsResponse:
            r"""Call the test iam permissions method over HTTP.

            Args:
                request (iam_policy_pb2.TestIamPermissionsRequest):
                    The request object for TestIamPermissions method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                iam_policy_pb2.TestIamPermissionsResponse: Response from TestIamPermissions method.
            """

            http_options = _BaseRepositoryManagerRestTransport._BaseTestIamPermissions._get_http_options()
            request, metadata = self._interceptor.pre_test_iam_permissions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRepositoryManagerRestTransport._BaseTestIamPermissions,
                    "_BaseTestIamPermissions__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devtools.cloudbuild_v2.RepositoryManagerClient.TestIamPermissions",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v2.RepositoryManager",
                        "rpcName": "TestIamPermissions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RepositoryManagerRestTransport._TestIamPermissions._get_response(
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

            content = response.content.decode("utf-8")
            resp = iam_policy_pb2.TestIamPermissionsResponse()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_test_iam_permissions(resp)
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
                    "Received response for google.devtools.cloudbuild_v2.RepositoryManagerAsyncClient.TestIamPermissions",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v2.RepositoryManager",
                        "rpcName": "TestIamPermissions",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseRepositoryManagerRestTransport._BaseCancelOperation,
        RepositoryManagerRestStub,
    ):
        def __hash__(self):
            return hash("RepositoryManagerRestTransport.CancelOperation")

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

            http_options = _BaseRepositoryManagerRestTransport._BaseCancelOperation._get_http_options()
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRepositoryManagerRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.devtools.cloudbuild_v2.RepositoryManagerClient.CancelOperation",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v2.RepositoryManager",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RepositoryManagerRestTransport._CancelOperation._get_response(
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
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetOperation(
        _BaseRepositoryManagerRestTransport._BaseGetOperation, RepositoryManagerRestStub
    ):
        def __hash__(self):
            return hash("RepositoryManagerRestTransport.GetOperation")

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

            http_options = _BaseRepositoryManagerRestTransport._BaseGetOperation._get_http_options()
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRepositoryManagerRestTransport._BaseGetOperation,
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
                    f"Sending request for google.devtools.cloudbuild_v2.RepositoryManagerClient.GetOperation",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v2.RepositoryManager",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RepositoryManagerRestTransport._GetOperation._get_response(
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
                    "Received response for google.devtools.cloudbuild_v2.RepositoryManagerAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v2.RepositoryManager",
                        "rpcName": "GetOperation",
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


__all__ = ("RepositoryManagerRestTransport",)
