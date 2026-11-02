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
import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1, rest_helpers, rest_streaming
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.requests import AuthorizedSession  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.iam.v1 import (
    iam_policy_pb2,  # type: ignore
    policy_pb2,  # type: ignore
)
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.agentidentity_v1._compat import transcode_request
from google.cloud.agentidentity_v1.types import auth_provider_service

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseAuthProviderServiceRestTransport

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


class AuthProviderServiceRestInterceptor:
    """Interceptor for AuthProviderService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the AuthProviderServiceRestTransport.

    .. code-block:: python
        class MyCustomAuthProviderServiceInterceptor(AuthProviderServiceRestInterceptor):
            def pre_create_auth_provider(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_auth_provider(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_authorization(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_auth_provider(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_disable_auth_provider(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_disable_auth_provider(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_enable_auth_provider(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_enable_auth_provider(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_access_summary(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_access_summary(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_authorization(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_authorization(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_auth_provider(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_auth_provider(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_access_summaries(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_access_summaries(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_authorizations(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_authorizations(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_auth_providers(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_auth_providers(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_query_auth_providers(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_query_auth_providers(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_query_workloads(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_query_workloads(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_revoke_authorization(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_revoke_authorization(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_undelete_auth_provider(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_undelete_auth_provider(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_auth_provider(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_auth_provider(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = AuthProviderServiceRestTransport(interceptor=MyCustomAuthProviderServiceInterceptor())
        client = AuthProviderServiceClient(transport=transport)


    """

    def pre_create_auth_provider(
        self,
        request: auth_provider_service.CreateAuthProviderRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        auth_provider_service.CreateAuthProviderRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_auth_provider

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AuthProviderService server.
        """
        return request, metadata

    def post_create_auth_provider(
        self, response: auth_provider_service.AuthProvider
    ) -> auth_provider_service.AuthProvider:
        """Post-rpc interceptor for create_auth_provider

        DEPRECATED. Please use the `post_create_auth_provider_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AuthProviderService server but before
        it is returned to user code. This `post_create_auth_provider` interceptor runs
        before the `post_create_auth_provider_with_metadata` interceptor.
        """
        return response

    def post_create_auth_provider_with_metadata(
        self,
        response: auth_provider_service.AuthProvider,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        auth_provider_service.AuthProvider, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for create_auth_provider

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AuthProviderService server but before it is returned to user code.

        We recommend only using this `post_create_auth_provider_with_metadata`
        interceptor in new development instead of the `post_create_auth_provider` interceptor.
        When both interceptors are used, this `post_create_auth_provider_with_metadata` interceptor runs after the
        `post_create_auth_provider` interceptor. The (possibly modified) response returned by
        `post_create_auth_provider` will be passed to
        `post_create_auth_provider_with_metadata`.
        """
        return response, metadata

    def pre_delete_authorization(
        self,
        request: auth_provider_service.DeleteAuthorizationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        auth_provider_service.DeleteAuthorizationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_authorization

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AuthProviderService server.
        """
        return request, metadata

    def pre_delete_auth_provider(
        self,
        request: auth_provider_service.DeleteAuthProviderRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        auth_provider_service.DeleteAuthProviderRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_auth_provider

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AuthProviderService server.
        """
        return request, metadata

    def pre_disable_auth_provider(
        self,
        request: auth_provider_service.DisableAuthProviderRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        auth_provider_service.DisableAuthProviderRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for disable_auth_provider

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AuthProviderService server.
        """
        return request, metadata

    def post_disable_auth_provider(
        self, response: auth_provider_service.AuthProvider
    ) -> auth_provider_service.AuthProvider:
        """Post-rpc interceptor for disable_auth_provider

        DEPRECATED. Please use the `post_disable_auth_provider_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AuthProviderService server but before
        it is returned to user code. This `post_disable_auth_provider` interceptor runs
        before the `post_disable_auth_provider_with_metadata` interceptor.
        """
        return response

    def post_disable_auth_provider_with_metadata(
        self,
        response: auth_provider_service.AuthProvider,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        auth_provider_service.AuthProvider, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for disable_auth_provider

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AuthProviderService server but before it is returned to user code.

        We recommend only using this `post_disable_auth_provider_with_metadata`
        interceptor in new development instead of the `post_disable_auth_provider` interceptor.
        When both interceptors are used, this `post_disable_auth_provider_with_metadata` interceptor runs after the
        `post_disable_auth_provider` interceptor. The (possibly modified) response returned by
        `post_disable_auth_provider` will be passed to
        `post_disable_auth_provider_with_metadata`.
        """
        return response, metadata

    def pre_enable_auth_provider(
        self,
        request: auth_provider_service.EnableAuthProviderRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        auth_provider_service.EnableAuthProviderRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for enable_auth_provider

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AuthProviderService server.
        """
        return request, metadata

    def post_enable_auth_provider(
        self, response: auth_provider_service.AuthProvider
    ) -> auth_provider_service.AuthProvider:
        """Post-rpc interceptor for enable_auth_provider

        DEPRECATED. Please use the `post_enable_auth_provider_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AuthProviderService server but before
        it is returned to user code. This `post_enable_auth_provider` interceptor runs
        before the `post_enable_auth_provider_with_metadata` interceptor.
        """
        return response

    def post_enable_auth_provider_with_metadata(
        self,
        response: auth_provider_service.AuthProvider,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        auth_provider_service.AuthProvider, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for enable_auth_provider

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AuthProviderService server but before it is returned to user code.

        We recommend only using this `post_enable_auth_provider_with_metadata`
        interceptor in new development instead of the `post_enable_auth_provider` interceptor.
        When both interceptors are used, this `post_enable_auth_provider_with_metadata` interceptor runs after the
        `post_enable_auth_provider` interceptor. The (possibly modified) response returned by
        `post_enable_auth_provider` will be passed to
        `post_enable_auth_provider_with_metadata`.
        """
        return response, metadata

    def pre_get_access_summary(
        self,
        request: auth_provider_service.GetAccessSummaryRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        auth_provider_service.GetAccessSummaryRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_access_summary

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AuthProviderService server.
        """
        return request, metadata

    def post_get_access_summary(
        self, response: auth_provider_service.AccessSummary
    ) -> auth_provider_service.AccessSummary:
        """Post-rpc interceptor for get_access_summary

        DEPRECATED. Please use the `post_get_access_summary_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AuthProviderService server but before
        it is returned to user code. This `post_get_access_summary` interceptor runs
        before the `post_get_access_summary_with_metadata` interceptor.
        """
        return response

    def post_get_access_summary_with_metadata(
        self,
        response: auth_provider_service.AccessSummary,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        auth_provider_service.AccessSummary, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_access_summary

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AuthProviderService server but before it is returned to user code.

        We recommend only using this `post_get_access_summary_with_metadata`
        interceptor in new development instead of the `post_get_access_summary` interceptor.
        When both interceptors are used, this `post_get_access_summary_with_metadata` interceptor runs after the
        `post_get_access_summary` interceptor. The (possibly modified) response returned by
        `post_get_access_summary` will be passed to
        `post_get_access_summary_with_metadata`.
        """
        return response, metadata

    def pre_get_authorization(
        self,
        request: auth_provider_service.GetAuthorizationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        auth_provider_service.GetAuthorizationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_authorization

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AuthProviderService server.
        """
        return request, metadata

    def post_get_authorization(
        self, response: auth_provider_service.Authorization
    ) -> auth_provider_service.Authorization:
        """Post-rpc interceptor for get_authorization

        DEPRECATED. Please use the `post_get_authorization_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AuthProviderService server but before
        it is returned to user code. This `post_get_authorization` interceptor runs
        before the `post_get_authorization_with_metadata` interceptor.
        """
        return response

    def post_get_authorization_with_metadata(
        self,
        response: auth_provider_service.Authorization,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        auth_provider_service.Authorization, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_authorization

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AuthProviderService server but before it is returned to user code.

        We recommend only using this `post_get_authorization_with_metadata`
        interceptor in new development instead of the `post_get_authorization` interceptor.
        When both interceptors are used, this `post_get_authorization_with_metadata` interceptor runs after the
        `post_get_authorization` interceptor. The (possibly modified) response returned by
        `post_get_authorization` will be passed to
        `post_get_authorization_with_metadata`.
        """
        return response, metadata

    def pre_get_auth_provider(
        self,
        request: auth_provider_service.GetAuthProviderRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        auth_provider_service.GetAuthProviderRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_auth_provider

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AuthProviderService server.
        """
        return request, metadata

    def post_get_auth_provider(
        self, response: auth_provider_service.AuthProvider
    ) -> auth_provider_service.AuthProvider:
        """Post-rpc interceptor for get_auth_provider

        DEPRECATED. Please use the `post_get_auth_provider_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AuthProviderService server but before
        it is returned to user code. This `post_get_auth_provider` interceptor runs
        before the `post_get_auth_provider_with_metadata` interceptor.
        """
        return response

    def post_get_auth_provider_with_metadata(
        self,
        response: auth_provider_service.AuthProvider,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        auth_provider_service.AuthProvider, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_auth_provider

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AuthProviderService server but before it is returned to user code.

        We recommend only using this `post_get_auth_provider_with_metadata`
        interceptor in new development instead of the `post_get_auth_provider` interceptor.
        When both interceptors are used, this `post_get_auth_provider_with_metadata` interceptor runs after the
        `post_get_auth_provider` interceptor. The (possibly modified) response returned by
        `post_get_auth_provider` will be passed to
        `post_get_auth_provider_with_metadata`.
        """
        return response, metadata

    def pre_list_access_summaries(
        self,
        request: auth_provider_service.ListAccessSummariesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        auth_provider_service.ListAccessSummariesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_access_summaries

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AuthProviderService server.
        """
        return request, metadata

    def post_list_access_summaries(
        self, response: auth_provider_service.ListAccessSummariesResponse
    ) -> auth_provider_service.ListAccessSummariesResponse:
        """Post-rpc interceptor for list_access_summaries

        DEPRECATED. Please use the `post_list_access_summaries_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AuthProviderService server but before
        it is returned to user code. This `post_list_access_summaries` interceptor runs
        before the `post_list_access_summaries_with_metadata` interceptor.
        """
        return response

    def post_list_access_summaries_with_metadata(
        self,
        response: auth_provider_service.ListAccessSummariesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        auth_provider_service.ListAccessSummariesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_access_summaries

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AuthProviderService server but before it is returned to user code.

        We recommend only using this `post_list_access_summaries_with_metadata`
        interceptor in new development instead of the `post_list_access_summaries` interceptor.
        When both interceptors are used, this `post_list_access_summaries_with_metadata` interceptor runs after the
        `post_list_access_summaries` interceptor. The (possibly modified) response returned by
        `post_list_access_summaries` will be passed to
        `post_list_access_summaries_with_metadata`.
        """
        return response, metadata

    def pre_list_authorizations(
        self,
        request: auth_provider_service.ListAuthorizationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        auth_provider_service.ListAuthorizationsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_authorizations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AuthProviderService server.
        """
        return request, metadata

    def post_list_authorizations(
        self, response: auth_provider_service.ListAuthorizationsResponse
    ) -> auth_provider_service.ListAuthorizationsResponse:
        """Post-rpc interceptor for list_authorizations

        DEPRECATED. Please use the `post_list_authorizations_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AuthProviderService server but before
        it is returned to user code. This `post_list_authorizations` interceptor runs
        before the `post_list_authorizations_with_metadata` interceptor.
        """
        return response

    def post_list_authorizations_with_metadata(
        self,
        response: auth_provider_service.ListAuthorizationsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        auth_provider_service.ListAuthorizationsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_authorizations

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AuthProviderService server but before it is returned to user code.

        We recommend only using this `post_list_authorizations_with_metadata`
        interceptor in new development instead of the `post_list_authorizations` interceptor.
        When both interceptors are used, this `post_list_authorizations_with_metadata` interceptor runs after the
        `post_list_authorizations` interceptor. The (possibly modified) response returned by
        `post_list_authorizations` will be passed to
        `post_list_authorizations_with_metadata`.
        """
        return response, metadata

    def pre_list_auth_providers(
        self,
        request: auth_provider_service.ListAuthProvidersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        auth_provider_service.ListAuthProvidersRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_auth_providers

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AuthProviderService server.
        """
        return request, metadata

    def post_list_auth_providers(
        self, response: auth_provider_service.ListAuthProvidersResponse
    ) -> auth_provider_service.ListAuthProvidersResponse:
        """Post-rpc interceptor for list_auth_providers

        DEPRECATED. Please use the `post_list_auth_providers_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AuthProviderService server but before
        it is returned to user code. This `post_list_auth_providers` interceptor runs
        before the `post_list_auth_providers_with_metadata` interceptor.
        """
        return response

    def post_list_auth_providers_with_metadata(
        self,
        response: auth_provider_service.ListAuthProvidersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        auth_provider_service.ListAuthProvidersResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_auth_providers

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AuthProviderService server but before it is returned to user code.

        We recommend only using this `post_list_auth_providers_with_metadata`
        interceptor in new development instead of the `post_list_auth_providers` interceptor.
        When both interceptors are used, this `post_list_auth_providers_with_metadata` interceptor runs after the
        `post_list_auth_providers` interceptor. The (possibly modified) response returned by
        `post_list_auth_providers` will be passed to
        `post_list_auth_providers_with_metadata`.
        """
        return response, metadata

    def pre_query_auth_providers(
        self,
        request: auth_provider_service.QueryAuthProvidersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        auth_provider_service.QueryAuthProvidersRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for query_auth_providers

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AuthProviderService server.
        """
        return request, metadata

    def post_query_auth_providers(
        self, response: auth_provider_service.QueryAuthProvidersResponse
    ) -> auth_provider_service.QueryAuthProvidersResponse:
        """Post-rpc interceptor for query_auth_providers

        DEPRECATED. Please use the `post_query_auth_providers_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AuthProviderService server but before
        it is returned to user code. This `post_query_auth_providers` interceptor runs
        before the `post_query_auth_providers_with_metadata` interceptor.
        """
        return response

    def post_query_auth_providers_with_metadata(
        self,
        response: auth_provider_service.QueryAuthProvidersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        auth_provider_service.QueryAuthProvidersResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for query_auth_providers

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AuthProviderService server but before it is returned to user code.

        We recommend only using this `post_query_auth_providers_with_metadata`
        interceptor in new development instead of the `post_query_auth_providers` interceptor.
        When both interceptors are used, this `post_query_auth_providers_with_metadata` interceptor runs after the
        `post_query_auth_providers` interceptor. The (possibly modified) response returned by
        `post_query_auth_providers` will be passed to
        `post_query_auth_providers_with_metadata`.
        """
        return response, metadata

    def pre_query_workloads(
        self,
        request: auth_provider_service.QueryWorkloadsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        auth_provider_service.QueryWorkloadsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for query_workloads

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AuthProviderService server.
        """
        return request, metadata

    def post_query_workloads(
        self, response: auth_provider_service.QueryWorkloadsResponse
    ) -> auth_provider_service.QueryWorkloadsResponse:
        """Post-rpc interceptor for query_workloads

        DEPRECATED. Please use the `post_query_workloads_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AuthProviderService server but before
        it is returned to user code. This `post_query_workloads` interceptor runs
        before the `post_query_workloads_with_metadata` interceptor.
        """
        return response

    def post_query_workloads_with_metadata(
        self,
        response: auth_provider_service.QueryWorkloadsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        auth_provider_service.QueryWorkloadsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for query_workloads

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AuthProviderService server but before it is returned to user code.

        We recommend only using this `post_query_workloads_with_metadata`
        interceptor in new development instead of the `post_query_workloads` interceptor.
        When both interceptors are used, this `post_query_workloads_with_metadata` interceptor runs after the
        `post_query_workloads` interceptor. The (possibly modified) response returned by
        `post_query_workloads` will be passed to
        `post_query_workloads_with_metadata`.
        """
        return response, metadata

    def pre_revoke_authorization(
        self,
        request: auth_provider_service.RevokeAuthorizationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        auth_provider_service.RevokeAuthorizationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for revoke_authorization

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AuthProviderService server.
        """
        return request, metadata

    def post_revoke_authorization(
        self, response: auth_provider_service.RevokeAuthorizationResponse
    ) -> auth_provider_service.RevokeAuthorizationResponse:
        """Post-rpc interceptor for revoke_authorization

        DEPRECATED. Please use the `post_revoke_authorization_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AuthProviderService server but before
        it is returned to user code. This `post_revoke_authorization` interceptor runs
        before the `post_revoke_authorization_with_metadata` interceptor.
        """
        return response

    def post_revoke_authorization_with_metadata(
        self,
        response: auth_provider_service.RevokeAuthorizationResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        auth_provider_service.RevokeAuthorizationResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for revoke_authorization

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AuthProviderService server but before it is returned to user code.

        We recommend only using this `post_revoke_authorization_with_metadata`
        interceptor in new development instead of the `post_revoke_authorization` interceptor.
        When both interceptors are used, this `post_revoke_authorization_with_metadata` interceptor runs after the
        `post_revoke_authorization` interceptor. The (possibly modified) response returned by
        `post_revoke_authorization` will be passed to
        `post_revoke_authorization_with_metadata`.
        """
        return response, metadata

    def pre_undelete_auth_provider(
        self,
        request: auth_provider_service.UndeleteAuthProviderRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        auth_provider_service.UndeleteAuthProviderRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for undelete_auth_provider

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AuthProviderService server.
        """
        return request, metadata

    def post_undelete_auth_provider(
        self, response: auth_provider_service.AuthProvider
    ) -> auth_provider_service.AuthProvider:
        """Post-rpc interceptor for undelete_auth_provider

        DEPRECATED. Please use the `post_undelete_auth_provider_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AuthProviderService server but before
        it is returned to user code. This `post_undelete_auth_provider` interceptor runs
        before the `post_undelete_auth_provider_with_metadata` interceptor.
        """
        return response

    def post_undelete_auth_provider_with_metadata(
        self,
        response: auth_provider_service.AuthProvider,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        auth_provider_service.AuthProvider, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for undelete_auth_provider

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AuthProviderService server but before it is returned to user code.

        We recommend only using this `post_undelete_auth_provider_with_metadata`
        interceptor in new development instead of the `post_undelete_auth_provider` interceptor.
        When both interceptors are used, this `post_undelete_auth_provider_with_metadata` interceptor runs after the
        `post_undelete_auth_provider` interceptor. The (possibly modified) response returned by
        `post_undelete_auth_provider` will be passed to
        `post_undelete_auth_provider_with_metadata`.
        """
        return response, metadata

    def pre_update_auth_provider(
        self,
        request: auth_provider_service.UpdateAuthProviderRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        auth_provider_service.UpdateAuthProviderRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_auth_provider

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AuthProviderService server.
        """
        return request, metadata

    def post_update_auth_provider(
        self, response: auth_provider_service.AuthProvider
    ) -> auth_provider_service.AuthProvider:
        """Post-rpc interceptor for update_auth_provider

        DEPRECATED. Please use the `post_update_auth_provider_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AuthProviderService server but before
        it is returned to user code. This `post_update_auth_provider` interceptor runs
        before the `post_update_auth_provider_with_metadata` interceptor.
        """
        return response

    def post_update_auth_provider_with_metadata(
        self,
        response: auth_provider_service.AuthProvider,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        auth_provider_service.AuthProvider, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for update_auth_provider

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AuthProviderService server but before it is returned to user code.

        We recommend only using this `post_update_auth_provider_with_metadata`
        interceptor in new development instead of the `post_update_auth_provider` interceptor.
        When both interceptors are used, this `post_update_auth_provider_with_metadata` interceptor runs after the
        `post_update_auth_provider` interceptor. The (possibly modified) response returned by
        `post_update_auth_provider` will be passed to
        `post_update_auth_provider_with_metadata`.
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
        before they are sent to the AuthProviderService server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the AuthProviderService server but before
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
        before they are sent to the AuthProviderService server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the AuthProviderService server but before
        it is returned to user code.
        """
        return response

    def pre_get_iam_policy(
        self,
        request: iam_policy_pb2.GetIamPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        iam_policy_pb2.GetIamPolicyRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_iam_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AuthProviderService server.
        """
        return request, metadata

    def post_get_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for get_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the AuthProviderService server but before
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
        before they are sent to the AuthProviderService server.
        """
        return request, metadata

    def post_set_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for set_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the AuthProviderService server but before
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
        before they are sent to the AuthProviderService server.
        """
        return request, metadata

    def post_test_iam_permissions(
        self, response: iam_policy_pb2.TestIamPermissionsResponse
    ) -> iam_policy_pb2.TestIamPermissionsResponse:
        """Post-rpc interceptor for test_iam_permissions

        Override in a subclass to manipulate the response
        after it is returned by the AuthProviderService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class AuthProviderServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: AuthProviderServiceRestInterceptor


class AuthProviderServiceRestTransport(_BaseAuthProviderServiceRestTransport):
    """REST backend synchronous transport for AuthProviderService.

    Service describing handlers for resources

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "agentidentity.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[AuthProviderServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'agentidentity.googleapis.com').
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
            interceptor (Optional[AuthProviderServiceRestInterceptor]): Interceptor used
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
        if client_cert_source_for_mtls:
            self._session.configure_mtls_channel(client_cert_source_for_mtls)
        self._interceptor = interceptor or AuthProviderServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _CreateAuthProvider(
        _BaseAuthProviderServiceRestTransport._BaseCreateAuthProvider,
        AuthProviderServiceRestStub,
    ):
        def __hash__(self):
            return hash("AuthProviderServiceRestTransport.CreateAuthProvider")

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
            request: auth_provider_service.CreateAuthProviderRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> auth_provider_service.AuthProvider:
            r"""Call the create auth provider method over HTTP.

            Args:
                request (~.auth_provider_service.CreateAuthProviderRequest):
                    The request object. Message for creating a AuthProvider
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.auth_provider_service.AuthProvider:
                    Message describing AuthProvider
                object

            """

            http_options = _BaseAuthProviderServiceRestTransport._BaseCreateAuthProvider._get_http_options()
            request, metadata = self._interceptor.pre_create_auth_provider(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAuthProviderServiceRestTransport._BaseCreateAuthProvider,
                    "_BaseCreateAuthProvider__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.agentidentity_v1.AuthProviderServiceClient.CreateAuthProvider",
                    extra={
                        "serviceName": "google.cloud.agentidentity.v1.AuthProviderService",
                        "rpcName": "CreateAuthProvider",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AuthProviderServiceRestTransport._CreateAuthProvider._get_response(
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
            resp = auth_provider_service.AuthProvider()
            pb_resp = auth_provider_service.AuthProvider.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_auth_provider(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_auth_provider_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = auth_provider_service.AuthProvider.to_json(
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
                    "Received response for google.cloud.agentidentity_v1.AuthProviderServiceClient.create_auth_provider",
                    extra={
                        "serviceName": "google.cloud.agentidentity.v1.AuthProviderService",
                        "rpcName": "CreateAuthProvider",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteAuthorization(
        _BaseAuthProviderServiceRestTransport._BaseDeleteAuthorization,
        AuthProviderServiceRestStub,
    ):
        def __hash__(self):
            return hash("AuthProviderServiceRestTransport.DeleteAuthorization")

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
            request: auth_provider_service.DeleteAuthorizationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete authorization method over HTTP.

            Args:
                request (~.auth_provider_service.DeleteAuthorizationRequest):
                    The request object. Message for deleting an Authorization
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseAuthProviderServiceRestTransport._BaseDeleteAuthorization._get_http_options()
            request, metadata = self._interceptor.pre_delete_authorization(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAuthProviderServiceRestTransport._BaseDeleteAuthorization,
                    "_BaseDeleteAuthorization__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.agentidentity_v1.AuthProviderServiceClient.DeleteAuthorization",
                    extra={
                        "serviceName": "google.cloud.agentidentity.v1.AuthProviderService",
                        "rpcName": "DeleteAuthorization",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AuthProviderServiceRestTransport._DeleteAuthorization._get_response(
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

    class _DeleteAuthProvider(
        _BaseAuthProviderServiceRestTransport._BaseDeleteAuthProvider,
        AuthProviderServiceRestStub,
    ):
        def __hash__(self):
            return hash("AuthProviderServiceRestTransport.DeleteAuthProvider")

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
            request: auth_provider_service.DeleteAuthProviderRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete auth provider method over HTTP.

            Args:
                request (~.auth_provider_service.DeleteAuthProviderRequest):
                    The request object. Message for deleting a AuthProvider
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseAuthProviderServiceRestTransport._BaseDeleteAuthProvider._get_http_options()
            request, metadata = self._interceptor.pre_delete_auth_provider(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAuthProviderServiceRestTransport._BaseDeleteAuthProvider,
                    "_BaseDeleteAuthProvider__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.agentidentity_v1.AuthProviderServiceClient.DeleteAuthProvider",
                    extra={
                        "serviceName": "google.cloud.agentidentity.v1.AuthProviderService",
                        "rpcName": "DeleteAuthProvider",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AuthProviderServiceRestTransport._DeleteAuthProvider._get_response(
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

    class _DisableAuthProvider(
        _BaseAuthProviderServiceRestTransport._BaseDisableAuthProvider,
        AuthProviderServiceRestStub,
    ):
        def __hash__(self):
            return hash("AuthProviderServiceRestTransport.DisableAuthProvider")

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
            request: auth_provider_service.DisableAuthProviderRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> auth_provider_service.AuthProvider:
            r"""Call the disable auth provider method over HTTP.

            Args:
                request (~.auth_provider_service.DisableAuthProviderRequest):
                    The request object. Message for disabling an AuthProvider
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.auth_provider_service.AuthProvider:
                    Message describing AuthProvider
                object

            """

            http_options = _BaseAuthProviderServiceRestTransport._BaseDisableAuthProvider._get_http_options()
            request, metadata = self._interceptor.pre_disable_auth_provider(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAuthProviderServiceRestTransport._BaseDisableAuthProvider,
                    "_BaseDisableAuthProvider__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.agentidentity_v1.AuthProviderServiceClient.DisableAuthProvider",
                    extra={
                        "serviceName": "google.cloud.agentidentity.v1.AuthProviderService",
                        "rpcName": "DisableAuthProvider",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AuthProviderServiceRestTransport._DisableAuthProvider._get_response(
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
            resp = auth_provider_service.AuthProvider()
            pb_resp = auth_provider_service.AuthProvider.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_disable_auth_provider(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_disable_auth_provider_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = auth_provider_service.AuthProvider.to_json(
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
                    "Received response for google.cloud.agentidentity_v1.AuthProviderServiceClient.disable_auth_provider",
                    extra={
                        "serviceName": "google.cloud.agentidentity.v1.AuthProviderService",
                        "rpcName": "DisableAuthProvider",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _EnableAuthProvider(
        _BaseAuthProviderServiceRestTransport._BaseEnableAuthProvider,
        AuthProviderServiceRestStub,
    ):
        def __hash__(self):
            return hash("AuthProviderServiceRestTransport.EnableAuthProvider")

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
            request: auth_provider_service.EnableAuthProviderRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> auth_provider_service.AuthProvider:
            r"""Call the enable auth provider method over HTTP.

            Args:
                request (~.auth_provider_service.EnableAuthProviderRequest):
                    The request object. Message for enabling an AuthProvider
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.auth_provider_service.AuthProvider:
                    Message describing AuthProvider
                object

            """

            http_options = _BaseAuthProviderServiceRestTransport._BaseEnableAuthProvider._get_http_options()
            request, metadata = self._interceptor.pre_enable_auth_provider(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAuthProviderServiceRestTransport._BaseEnableAuthProvider,
                    "_BaseEnableAuthProvider__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.agentidentity_v1.AuthProviderServiceClient.EnableAuthProvider",
                    extra={
                        "serviceName": "google.cloud.agentidentity.v1.AuthProviderService",
                        "rpcName": "EnableAuthProvider",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AuthProviderServiceRestTransport._EnableAuthProvider._get_response(
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
            resp = auth_provider_service.AuthProvider()
            pb_resp = auth_provider_service.AuthProvider.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_enable_auth_provider(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_enable_auth_provider_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = auth_provider_service.AuthProvider.to_json(
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
                    "Received response for google.cloud.agentidentity_v1.AuthProviderServiceClient.enable_auth_provider",
                    extra={
                        "serviceName": "google.cloud.agentidentity.v1.AuthProviderService",
                        "rpcName": "EnableAuthProvider",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetAccessSummary(
        _BaseAuthProviderServiceRestTransport._BaseGetAccessSummary,
        AuthProviderServiceRestStub,
    ):
        def __hash__(self):
            return hash("AuthProviderServiceRestTransport.GetAccessSummary")

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
            request: auth_provider_service.GetAccessSummaryRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> auth_provider_service.AccessSummary:
            r"""Call the get access summary method over HTTP.

            Args:
                request (~.auth_provider_service.GetAccessSummaryRequest):
                    The request object. Message for getting a AccessSummary
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.auth_provider_service.AccessSummary:
                    Message describing AccessSummary
                object

            """

            http_options = _BaseAuthProviderServiceRestTransport._BaseGetAccessSummary._get_http_options()
            request, metadata = self._interceptor.pre_get_access_summary(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAuthProviderServiceRestTransport._BaseGetAccessSummary,
                    "_BaseGetAccessSummary__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.agentidentity_v1.AuthProviderServiceClient.GetAccessSummary",
                    extra={
                        "serviceName": "google.cloud.agentidentity.v1.AuthProviderService",
                        "rpcName": "GetAccessSummary",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AuthProviderServiceRestTransport._GetAccessSummary._get_response(
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
            resp = auth_provider_service.AccessSummary()
            pb_resp = auth_provider_service.AccessSummary.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_access_summary(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_access_summary_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = auth_provider_service.AccessSummary.to_json(
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
                    "Received response for google.cloud.agentidentity_v1.AuthProviderServiceClient.get_access_summary",
                    extra={
                        "serviceName": "google.cloud.agentidentity.v1.AuthProviderService",
                        "rpcName": "GetAccessSummary",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetAuthorization(
        _BaseAuthProviderServiceRestTransport._BaseGetAuthorization,
        AuthProviderServiceRestStub,
    ):
        def __hash__(self):
            return hash("AuthProviderServiceRestTransport.GetAuthorization")

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
            request: auth_provider_service.GetAuthorizationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> auth_provider_service.Authorization:
            r"""Call the get authorization method over HTTP.

            Args:
                request (~.auth_provider_service.GetAuthorizationRequest):
                    The request object. Message for getting a Authorization
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.auth_provider_service.Authorization:
                    Message describing Authorization
                object

            """

            http_options = _BaseAuthProviderServiceRestTransport._BaseGetAuthorization._get_http_options()
            request, metadata = self._interceptor.pre_get_authorization(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAuthProviderServiceRestTransport._BaseGetAuthorization,
                    "_BaseGetAuthorization__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.agentidentity_v1.AuthProviderServiceClient.GetAuthorization",
                    extra={
                        "serviceName": "google.cloud.agentidentity.v1.AuthProviderService",
                        "rpcName": "GetAuthorization",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AuthProviderServiceRestTransport._GetAuthorization._get_response(
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
            resp = auth_provider_service.Authorization()
            pb_resp = auth_provider_service.Authorization.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_authorization(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_authorization_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = auth_provider_service.Authorization.to_json(
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
                    "Received response for google.cloud.agentidentity_v1.AuthProviderServiceClient.get_authorization",
                    extra={
                        "serviceName": "google.cloud.agentidentity.v1.AuthProviderService",
                        "rpcName": "GetAuthorization",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetAuthProvider(
        _BaseAuthProviderServiceRestTransport._BaseGetAuthProvider,
        AuthProviderServiceRestStub,
    ):
        def __hash__(self):
            return hash("AuthProviderServiceRestTransport.GetAuthProvider")

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
            request: auth_provider_service.GetAuthProviderRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> auth_provider_service.AuthProvider:
            r"""Call the get auth provider method over HTTP.

            Args:
                request (~.auth_provider_service.GetAuthProviderRequest):
                    The request object. Message for getting a AuthProvider
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.auth_provider_service.AuthProvider:
                    Message describing AuthProvider
                object

            """

            http_options = _BaseAuthProviderServiceRestTransport._BaseGetAuthProvider._get_http_options()
            request, metadata = self._interceptor.pre_get_auth_provider(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAuthProviderServiceRestTransport._BaseGetAuthProvider,
                    "_BaseGetAuthProvider__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.agentidentity_v1.AuthProviderServiceClient.GetAuthProvider",
                    extra={
                        "serviceName": "google.cloud.agentidentity.v1.AuthProviderService",
                        "rpcName": "GetAuthProvider",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AuthProviderServiceRestTransport._GetAuthProvider._get_response(
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
            resp = auth_provider_service.AuthProvider()
            pb_resp = auth_provider_service.AuthProvider.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_auth_provider(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_auth_provider_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = auth_provider_service.AuthProvider.to_json(
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
                    "Received response for google.cloud.agentidentity_v1.AuthProviderServiceClient.get_auth_provider",
                    extra={
                        "serviceName": "google.cloud.agentidentity.v1.AuthProviderService",
                        "rpcName": "GetAuthProvider",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListAccessSummaries(
        _BaseAuthProviderServiceRestTransport._BaseListAccessSummaries,
        AuthProviderServiceRestStub,
    ):
        def __hash__(self):
            return hash("AuthProviderServiceRestTransport.ListAccessSummaries")

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
            request: auth_provider_service.ListAccessSummariesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> auth_provider_service.ListAccessSummariesResponse:
            r"""Call the list access summaries method over HTTP.

            Args:
                request (~.auth_provider_service.ListAccessSummariesRequest):
                    The request object. Message for requesting list of
                AccessSummaries
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.auth_provider_service.ListAccessSummariesResponse:
                    Message for response to listing
                AccessSummaries

            """

            http_options = _BaseAuthProviderServiceRestTransport._BaseListAccessSummaries._get_http_options()
            request, metadata = self._interceptor.pre_list_access_summaries(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAuthProviderServiceRestTransport._BaseListAccessSummaries,
                    "_BaseListAccessSummaries__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.agentidentity_v1.AuthProviderServiceClient.ListAccessSummaries",
                    extra={
                        "serviceName": "google.cloud.agentidentity.v1.AuthProviderService",
                        "rpcName": "ListAccessSummaries",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AuthProviderServiceRestTransport._ListAccessSummaries._get_response(
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
            resp = auth_provider_service.ListAccessSummariesResponse()
            pb_resp = auth_provider_service.ListAccessSummariesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_access_summaries(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_access_summaries_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        auth_provider_service.ListAccessSummariesResponse.to_json(
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
                    "Received response for google.cloud.agentidentity_v1.AuthProviderServiceClient.list_access_summaries",
                    extra={
                        "serviceName": "google.cloud.agentidentity.v1.AuthProviderService",
                        "rpcName": "ListAccessSummaries",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListAuthorizations(
        _BaseAuthProviderServiceRestTransport._BaseListAuthorizations,
        AuthProviderServiceRestStub,
    ):
        def __hash__(self):
            return hash("AuthProviderServiceRestTransport.ListAuthorizations")

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
            request: auth_provider_service.ListAuthorizationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> auth_provider_service.ListAuthorizationsResponse:
            r"""Call the list authorizations method over HTTP.

            Args:
                request (~.auth_provider_service.ListAuthorizationsRequest):
                    The request object. Message for requesting list of
                Authorizations
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.auth_provider_service.ListAuthorizationsResponse:
                    Message for response to listing
                Authorizations

            """

            http_options = _BaseAuthProviderServiceRestTransport._BaseListAuthorizations._get_http_options()
            request, metadata = self._interceptor.pre_list_authorizations(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAuthProviderServiceRestTransport._BaseListAuthorizations,
                    "_BaseListAuthorizations__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.agentidentity_v1.AuthProviderServiceClient.ListAuthorizations",
                    extra={
                        "serviceName": "google.cloud.agentidentity.v1.AuthProviderService",
                        "rpcName": "ListAuthorizations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AuthProviderServiceRestTransport._ListAuthorizations._get_response(
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
            resp = auth_provider_service.ListAuthorizationsResponse()
            pb_resp = auth_provider_service.ListAuthorizationsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_authorizations(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_authorizations_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        auth_provider_service.ListAuthorizationsResponse.to_json(
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
                    "Received response for google.cloud.agentidentity_v1.AuthProviderServiceClient.list_authorizations",
                    extra={
                        "serviceName": "google.cloud.agentidentity.v1.AuthProviderService",
                        "rpcName": "ListAuthorizations",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListAuthProviders(
        _BaseAuthProviderServiceRestTransport._BaseListAuthProviders,
        AuthProviderServiceRestStub,
    ):
        def __hash__(self):
            return hash("AuthProviderServiceRestTransport.ListAuthProviders")

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
            request: auth_provider_service.ListAuthProvidersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> auth_provider_service.ListAuthProvidersResponse:
            r"""Call the list auth providers method over HTTP.

            Args:
                request (~.auth_provider_service.ListAuthProvidersRequest):
                    The request object. Message for requesting list of
                AuthProviders
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.auth_provider_service.ListAuthProvidersResponse:
                    Message for response to listing
                AuthProviders

            """

            http_options = _BaseAuthProviderServiceRestTransport._BaseListAuthProviders._get_http_options()
            request, metadata = self._interceptor.pre_list_auth_providers(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAuthProviderServiceRestTransport._BaseListAuthProviders,
                    "_BaseListAuthProviders__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.agentidentity_v1.AuthProviderServiceClient.ListAuthProviders",
                    extra={
                        "serviceName": "google.cloud.agentidentity.v1.AuthProviderService",
                        "rpcName": "ListAuthProviders",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AuthProviderServiceRestTransport._ListAuthProviders._get_response(
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
            resp = auth_provider_service.ListAuthProvidersResponse()
            pb_resp = auth_provider_service.ListAuthProvidersResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_auth_providers(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_auth_providers_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        auth_provider_service.ListAuthProvidersResponse.to_json(
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
                    "Received response for google.cloud.agentidentity_v1.AuthProviderServiceClient.list_auth_providers",
                    extra={
                        "serviceName": "google.cloud.agentidentity.v1.AuthProviderService",
                        "rpcName": "ListAuthProviders",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _QueryAuthProviders(
        _BaseAuthProviderServiceRestTransport._BaseQueryAuthProviders,
        AuthProviderServiceRestStub,
    ):
        def __hash__(self):
            return hash("AuthProviderServiceRestTransport.QueryAuthProviders")

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
            request: auth_provider_service.QueryAuthProvidersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> auth_provider_service.QueryAuthProvidersResponse:
            r"""Call the query auth providers method over HTTP.

            Args:
                request (~.auth_provider_service.QueryAuthProvidersRequest):
                    The request object. Request message for
                QueryAuthProviders.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.auth_provider_service.QueryAuthProvidersResponse:
                    Response message for
                QueryAuthProviders.

            """

            http_options = _BaseAuthProviderServiceRestTransport._BaseQueryAuthProviders._get_http_options()
            request, metadata = self._interceptor.pre_query_auth_providers(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAuthProviderServiceRestTransport._BaseQueryAuthProviders,
                    "_BaseQueryAuthProviders__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.agentidentity_v1.AuthProviderServiceClient.QueryAuthProviders",
                    extra={
                        "serviceName": "google.cloud.agentidentity.v1.AuthProviderService",
                        "rpcName": "QueryAuthProviders",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AuthProviderServiceRestTransport._QueryAuthProviders._get_response(
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
            resp = auth_provider_service.QueryAuthProvidersResponse()
            pb_resp = auth_provider_service.QueryAuthProvidersResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_query_auth_providers(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_query_auth_providers_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        auth_provider_service.QueryAuthProvidersResponse.to_json(
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
                    "Received response for google.cloud.agentidentity_v1.AuthProviderServiceClient.query_auth_providers",
                    extra={
                        "serviceName": "google.cloud.agentidentity.v1.AuthProviderService",
                        "rpcName": "QueryAuthProviders",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _QueryWorkloads(
        _BaseAuthProviderServiceRestTransport._BaseQueryWorkloads,
        AuthProviderServiceRestStub,
    ):
        def __hash__(self):
            return hash("AuthProviderServiceRestTransport.QueryWorkloads")

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
            request: auth_provider_service.QueryWorkloadsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> auth_provider_service.QueryWorkloadsResponse:
            r"""Call the query workloads method over HTTP.

            Args:
                request (~.auth_provider_service.QueryWorkloadsRequest):
                    The request object. Request message for QueryWorkloads.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.auth_provider_service.QueryWorkloadsResponse:
                    Response message for QueryWorkloads.
            """

            http_options = _BaseAuthProviderServiceRestTransport._BaseQueryWorkloads._get_http_options()
            request, metadata = self._interceptor.pre_query_workloads(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAuthProviderServiceRestTransport._BaseQueryWorkloads,
                    "_BaseQueryWorkloads__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.agentidentity_v1.AuthProviderServiceClient.QueryWorkloads",
                    extra={
                        "serviceName": "google.cloud.agentidentity.v1.AuthProviderService",
                        "rpcName": "QueryWorkloads",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AuthProviderServiceRestTransport._QueryWorkloads._get_response(
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
            resp = auth_provider_service.QueryWorkloadsResponse()
            pb_resp = auth_provider_service.QueryWorkloadsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_query_workloads(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_query_workloads_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        auth_provider_service.QueryWorkloadsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.agentidentity_v1.AuthProviderServiceClient.query_workloads",
                    extra={
                        "serviceName": "google.cloud.agentidentity.v1.AuthProviderService",
                        "rpcName": "QueryWorkloads",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RevokeAuthorization(
        _BaseAuthProviderServiceRestTransport._BaseRevokeAuthorization,
        AuthProviderServiceRestStub,
    ):
        def __hash__(self):
            return hash("AuthProviderServiceRestTransport.RevokeAuthorization")

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
            request: auth_provider_service.RevokeAuthorizationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> auth_provider_service.RevokeAuthorizationResponse:
            r"""Call the revoke authorization method over HTTP.

            Args:
                request (~.auth_provider_service.RevokeAuthorizationRequest):
                    The request object. Request message for
                RevokeAuthorization.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.auth_provider_service.RevokeAuthorizationResponse:
                    Response message for
                RevokeAuthorization.

            """

            http_options = _BaseAuthProviderServiceRestTransport._BaseRevokeAuthorization._get_http_options()
            request, metadata = self._interceptor.pre_revoke_authorization(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAuthProviderServiceRestTransport._BaseRevokeAuthorization,
                    "_BaseRevokeAuthorization__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.agentidentity_v1.AuthProviderServiceClient.RevokeAuthorization",
                    extra={
                        "serviceName": "google.cloud.agentidentity.v1.AuthProviderService",
                        "rpcName": "RevokeAuthorization",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AuthProviderServiceRestTransport._RevokeAuthorization._get_response(
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
            resp = auth_provider_service.RevokeAuthorizationResponse()
            pb_resp = auth_provider_service.RevokeAuthorizationResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_revoke_authorization(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_revoke_authorization_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        auth_provider_service.RevokeAuthorizationResponse.to_json(
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
                    "Received response for google.cloud.agentidentity_v1.AuthProviderServiceClient.revoke_authorization",
                    extra={
                        "serviceName": "google.cloud.agentidentity.v1.AuthProviderService",
                        "rpcName": "RevokeAuthorization",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UndeleteAuthProvider(
        _BaseAuthProviderServiceRestTransport._BaseUndeleteAuthProvider,
        AuthProviderServiceRestStub,
    ):
        def __hash__(self):
            return hash("AuthProviderServiceRestTransport.UndeleteAuthProvider")

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
            request: auth_provider_service.UndeleteAuthProviderRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> auth_provider_service.AuthProvider:
            r"""Call the undelete auth provider method over HTTP.

            Args:
                request (~.auth_provider_service.UndeleteAuthProviderRequest):
                    The request object. Message for undeleting a AuthProvider
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.auth_provider_service.AuthProvider:
                    Message describing AuthProvider
                object

            """

            http_options = _BaseAuthProviderServiceRestTransport._BaseUndeleteAuthProvider._get_http_options()
            request, metadata = self._interceptor.pre_undelete_auth_provider(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAuthProviderServiceRestTransport._BaseUndeleteAuthProvider,
                    "_BaseUndeleteAuthProvider__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.agentidentity_v1.AuthProviderServiceClient.UndeleteAuthProvider",
                    extra={
                        "serviceName": "google.cloud.agentidentity.v1.AuthProviderService",
                        "rpcName": "UndeleteAuthProvider",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AuthProviderServiceRestTransport._UndeleteAuthProvider._get_response(
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
            resp = auth_provider_service.AuthProvider()
            pb_resp = auth_provider_service.AuthProvider.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_undelete_auth_provider(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_undelete_auth_provider_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = auth_provider_service.AuthProvider.to_json(
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
                    "Received response for google.cloud.agentidentity_v1.AuthProviderServiceClient.undelete_auth_provider",
                    extra={
                        "serviceName": "google.cloud.agentidentity.v1.AuthProviderService",
                        "rpcName": "UndeleteAuthProvider",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateAuthProvider(
        _BaseAuthProviderServiceRestTransport._BaseUpdateAuthProvider,
        AuthProviderServiceRestStub,
    ):
        def __hash__(self):
            return hash("AuthProviderServiceRestTransport.UpdateAuthProvider")

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
            request: auth_provider_service.UpdateAuthProviderRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> auth_provider_service.AuthProvider:
            r"""Call the update auth provider method over HTTP.

            Args:
                request (~.auth_provider_service.UpdateAuthProviderRequest):
                    The request object. Message for updating a AuthProvider
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.auth_provider_service.AuthProvider:
                    Message describing AuthProvider
                object

            """

            http_options = _BaseAuthProviderServiceRestTransport._BaseUpdateAuthProvider._get_http_options()
            request, metadata = self._interceptor.pre_update_auth_provider(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAuthProviderServiceRestTransport._BaseUpdateAuthProvider,
                    "_BaseUpdateAuthProvider__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.agentidentity_v1.AuthProviderServiceClient.UpdateAuthProvider",
                    extra={
                        "serviceName": "google.cloud.agentidentity.v1.AuthProviderService",
                        "rpcName": "UpdateAuthProvider",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AuthProviderServiceRestTransport._UpdateAuthProvider._get_response(
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
            resp = auth_provider_service.AuthProvider()
            pb_resp = auth_provider_service.AuthProvider.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_auth_provider(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_auth_provider_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = auth_provider_service.AuthProvider.to_json(
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
                    "Received response for google.cloud.agentidentity_v1.AuthProviderServiceClient.update_auth_provider",
                    extra={
                        "serviceName": "google.cloud.agentidentity.v1.AuthProviderService",
                        "rpcName": "UpdateAuthProvider",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_auth_provider(
        self,
    ) -> Callable[
        [auth_provider_service.CreateAuthProviderRequest],
        auth_provider_service.AuthProvider,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateAuthProvider(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_authorization(
        self,
    ) -> Callable[[auth_provider_service.DeleteAuthorizationRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteAuthorization(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_auth_provider(
        self,
    ) -> Callable[[auth_provider_service.DeleteAuthProviderRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteAuthProvider(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def disable_auth_provider(
        self,
    ) -> Callable[
        [auth_provider_service.DisableAuthProviderRequest],
        auth_provider_service.AuthProvider,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DisableAuthProvider(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def enable_auth_provider(
        self,
    ) -> Callable[
        [auth_provider_service.EnableAuthProviderRequest],
        auth_provider_service.AuthProvider,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._EnableAuthProvider(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_access_summary(
        self,
    ) -> Callable[
        [auth_provider_service.GetAccessSummaryRequest],
        auth_provider_service.AccessSummary,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetAccessSummary(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_authorization(
        self,
    ) -> Callable[
        [auth_provider_service.GetAuthorizationRequest],
        auth_provider_service.Authorization,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetAuthorization(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_auth_provider(
        self,
    ) -> Callable[
        [auth_provider_service.GetAuthProviderRequest],
        auth_provider_service.AuthProvider,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetAuthProvider(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_access_summaries(
        self,
    ) -> Callable[
        [auth_provider_service.ListAccessSummariesRequest],
        auth_provider_service.ListAccessSummariesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListAccessSummaries(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_authorizations(
        self,
    ) -> Callable[
        [auth_provider_service.ListAuthorizationsRequest],
        auth_provider_service.ListAuthorizationsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListAuthorizations(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_auth_providers(
        self,
    ) -> Callable[
        [auth_provider_service.ListAuthProvidersRequest],
        auth_provider_service.ListAuthProvidersResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListAuthProviders(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def query_auth_providers(
        self,
    ) -> Callable[
        [auth_provider_service.QueryAuthProvidersRequest],
        auth_provider_service.QueryAuthProvidersResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._QueryAuthProviders(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def query_workloads(
        self,
    ) -> Callable[
        [auth_provider_service.QueryWorkloadsRequest],
        auth_provider_service.QueryWorkloadsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._QueryWorkloads(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def revoke_authorization(
        self,
    ) -> Callable[
        [auth_provider_service.RevokeAuthorizationRequest],
        auth_provider_service.RevokeAuthorizationResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RevokeAuthorization(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def undelete_auth_provider(
        self,
    ) -> Callable[
        [auth_provider_service.UndeleteAuthProviderRequest],
        auth_provider_service.AuthProvider,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UndeleteAuthProvider(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_auth_provider(
        self,
    ) -> Callable[
        [auth_provider_service.UpdateAuthProviderRequest],
        auth_provider_service.AuthProvider,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateAuthProvider(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(
        _BaseAuthProviderServiceRestTransport._BaseGetLocation,
        AuthProviderServiceRestStub,
    ):
        def __hash__(self):
            return hash("AuthProviderServiceRestTransport.GetLocation")

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

            http_options = _BaseAuthProviderServiceRestTransport._BaseGetLocation._get_http_options()
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAuthProviderServiceRestTransport._BaseGetLocation,
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
                    f"Sending request for google.cloud.agentidentity_v1.AuthProviderServiceClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.agentidentity.v1.AuthProviderService",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AuthProviderServiceRestTransport._GetLocation._get_response(
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
                    "Received response for google.cloud.agentidentity_v1.AuthProviderServiceAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.agentidentity.v1.AuthProviderService",
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
        _BaseAuthProviderServiceRestTransport._BaseListLocations,
        AuthProviderServiceRestStub,
    ):
        def __hash__(self):
            return hash("AuthProviderServiceRestTransport.ListLocations")

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

            http_options = _BaseAuthProviderServiceRestTransport._BaseListLocations._get_http_options()
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAuthProviderServiceRestTransport._BaseListLocations,
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
                    f"Sending request for google.cloud.agentidentity_v1.AuthProviderServiceClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.agentidentity.v1.AuthProviderService",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AuthProviderServiceRestTransport._ListLocations._get_response(
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
                    "Received response for google.cloud.agentidentity_v1.AuthProviderServiceAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.agentidentity.v1.AuthProviderService",
                        "rpcName": "ListLocations",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def get_iam_policy(self):
        return self._GetIamPolicy(self._session, self._host, self._interceptor)  # type: ignore

    class _GetIamPolicy(
        _BaseAuthProviderServiceRestTransport._BaseGetIamPolicy,
        AuthProviderServiceRestStub,
    ):
        def __hash__(self):
            return hash("AuthProviderServiceRestTransport.GetIamPolicy")

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

            http_options = _BaseAuthProviderServiceRestTransport._BaseGetIamPolicy._get_http_options()
            request, metadata = self._interceptor.pre_get_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAuthProviderServiceRestTransport._BaseGetIamPolicy,
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
                    f"Sending request for google.cloud.agentidentity_v1.AuthProviderServiceClient.GetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.agentidentity.v1.AuthProviderService",
                        "rpcName": "GetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AuthProviderServiceRestTransport._GetIamPolicy._get_response(
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
                    "Received response for google.cloud.agentidentity_v1.AuthProviderServiceAsyncClient.GetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.agentidentity.v1.AuthProviderService",
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
        _BaseAuthProviderServiceRestTransport._BaseSetIamPolicy,
        AuthProviderServiceRestStub,
    ):
        def __hash__(self):
            return hash("AuthProviderServiceRestTransport.SetIamPolicy")

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

            http_options = _BaseAuthProviderServiceRestTransport._BaseSetIamPolicy._get_http_options()
            request, metadata = self._interceptor.pre_set_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAuthProviderServiceRestTransport._BaseSetIamPolicy,
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
                    f"Sending request for google.cloud.agentidentity_v1.AuthProviderServiceClient.SetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.agentidentity.v1.AuthProviderService",
                        "rpcName": "SetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AuthProviderServiceRestTransport._SetIamPolicy._get_response(
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
                    "Received response for google.cloud.agentidentity_v1.AuthProviderServiceAsyncClient.SetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.agentidentity.v1.AuthProviderService",
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
        _BaseAuthProviderServiceRestTransport._BaseTestIamPermissions,
        AuthProviderServiceRestStub,
    ):
        def __hash__(self):
            return hash("AuthProviderServiceRestTransport.TestIamPermissions")

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

            http_options = _BaseAuthProviderServiceRestTransport._BaseTestIamPermissions._get_http_options()
            request, metadata = self._interceptor.pre_test_iam_permissions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAuthProviderServiceRestTransport._BaseTestIamPermissions,
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
                    f"Sending request for google.cloud.agentidentity_v1.AuthProviderServiceClient.TestIamPermissions",
                    extra={
                        "serviceName": "google.cloud.agentidentity.v1.AuthProviderService",
                        "rpcName": "TestIamPermissions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AuthProviderServiceRestTransport._TestIamPermissions._get_response(
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
                    "Received response for google.cloud.agentidentity_v1.AuthProviderServiceAsyncClient.TestIamPermissions",
                    extra={
                        "serviceName": "google.cloud.agentidentity.v1.AuthProviderService",
                        "rpcName": "TestIamPermissions",
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


__all__ = ("AuthProviderServiceRestTransport",)
