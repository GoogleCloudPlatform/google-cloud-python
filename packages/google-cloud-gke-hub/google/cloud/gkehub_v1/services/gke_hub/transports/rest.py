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
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.gkehub_v1._compat import transcode_request
from google.cloud.gkehub_v1.types import feature, fleet, membership, service

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseGkeHubRestTransport

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


class GkeHubRestInterceptor:
    """Interceptor for GkeHub.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the GkeHubRestTransport.

    .. code-block:: python
        class MyCustomGkeHubInterceptor(GkeHubRestInterceptor):
            def pre_create_feature(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_feature(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_fleet(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_fleet(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_membership(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_membership(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_membership_binding(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_membership_binding(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_membership_rbac_role_binding(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_membership_rbac_role_binding(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_scope(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_scope(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_scope_namespace(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_scope_namespace(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_scope_rbac_role_binding(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_scope_rbac_role_binding(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_feature(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_feature(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_fleet(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_fleet(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_membership(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_membership(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_membership_binding(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_membership_binding(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_membership_rbac_role_binding(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_membership_rbac_role_binding(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_scope(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_scope(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_scope_namespace(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_scope_namespace(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_scope_rbac_role_binding(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_scope_rbac_role_binding(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_generate_connect_manifest(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_generate_connect_manifest(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_generate_membership_rbac_role_binding_yaml(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_generate_membership_rbac_role_binding_yaml(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_feature(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_feature(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_fleet(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_fleet(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_membership(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_membership(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_membership_binding(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_membership_binding(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_membership_rbac_role_binding(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_membership_rbac_role_binding(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_scope(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_scope(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_scope_namespace(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_scope_namespace(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_scope_rbac_role_binding(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_scope_rbac_role_binding(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_bound_memberships(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_bound_memberships(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_features(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_features(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_fleets(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_fleets(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_membership_bindings(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_membership_bindings(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_membership_rbac_role_bindings(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_membership_rbac_role_bindings(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_memberships(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_memberships(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_permitted_scopes(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_permitted_scopes(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_scope_namespaces(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_scope_namespaces(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_scope_rbac_role_bindings(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_scope_rbac_role_bindings(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_scopes(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_scopes(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_feature(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_feature(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_fleet(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_fleet(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_membership(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_membership(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_membership_binding(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_membership_binding(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_membership_rbac_role_binding(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_membership_rbac_role_binding(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_scope(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_scope(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_scope_namespace(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_scope_namespace(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_scope_rbac_role_binding(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_scope_rbac_role_binding(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = GkeHubRestTransport(interceptor=MyCustomGkeHubInterceptor())
        client = GkeHubClient(transport=transport)


    """

    def pre_create_feature(
        self,
        request: service.CreateFeatureRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.CreateFeatureRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_feature

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GkeHub server.
        """
        return request, metadata

    def post_create_feature(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_feature

        DEPRECATED. Please use the `post_create_feature_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the GkeHub server but before
        it is returned to user code. This `post_create_feature` interceptor runs
        before the `post_create_feature_with_metadata` interceptor.
        """
        return response

    def post_create_feature_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_feature

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the GkeHub server but before it is returned to user code.

        We recommend only using this `post_create_feature_with_metadata`
        interceptor in new development instead of the `post_create_feature` interceptor.
        When both interceptors are used, this `post_create_feature_with_metadata` interceptor runs after the
        `post_create_feature` interceptor. The (possibly modified) response returned by
        `post_create_feature` will be passed to
        `post_create_feature_with_metadata`.
        """
        return response, metadata

    def pre_create_fleet(
        self,
        request: service.CreateFleetRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.CreateFleetRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_fleet

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GkeHub server.
        """
        return request, metadata

    def post_create_fleet(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_fleet

        DEPRECATED. Please use the `post_create_fleet_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the GkeHub server but before
        it is returned to user code. This `post_create_fleet` interceptor runs
        before the `post_create_fleet_with_metadata` interceptor.
        """
        return response

    def post_create_fleet_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_fleet

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the GkeHub server but before it is returned to user code.

        We recommend only using this `post_create_fleet_with_metadata`
        interceptor in new development instead of the `post_create_fleet` interceptor.
        When both interceptors are used, this `post_create_fleet_with_metadata` interceptor runs after the
        `post_create_fleet` interceptor. The (possibly modified) response returned by
        `post_create_fleet` will be passed to
        `post_create_fleet_with_metadata`.
        """
        return response, metadata

    def pre_create_membership(
        self,
        request: service.CreateMembershipRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.CreateMembershipRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_membership

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GkeHub server.
        """
        return request, metadata

    def post_create_membership(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_membership

        DEPRECATED. Please use the `post_create_membership_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the GkeHub server but before
        it is returned to user code. This `post_create_membership` interceptor runs
        before the `post_create_membership_with_metadata` interceptor.
        """
        return response

    def post_create_membership_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_membership

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the GkeHub server but before it is returned to user code.

        We recommend only using this `post_create_membership_with_metadata`
        interceptor in new development instead of the `post_create_membership` interceptor.
        When both interceptors are used, this `post_create_membership_with_metadata` interceptor runs after the
        `post_create_membership` interceptor. The (possibly modified) response returned by
        `post_create_membership` will be passed to
        `post_create_membership_with_metadata`.
        """
        return response, metadata

    def pre_create_membership_binding(
        self,
        request: service.CreateMembershipBindingRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.CreateMembershipBindingRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_membership_binding

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GkeHub server.
        """
        return request, metadata

    def post_create_membership_binding(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_membership_binding

        DEPRECATED. Please use the `post_create_membership_binding_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the GkeHub server but before
        it is returned to user code. This `post_create_membership_binding` interceptor runs
        before the `post_create_membership_binding_with_metadata` interceptor.
        """
        return response

    def post_create_membership_binding_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_membership_binding

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the GkeHub server but before it is returned to user code.

        We recommend only using this `post_create_membership_binding_with_metadata`
        interceptor in new development instead of the `post_create_membership_binding` interceptor.
        When both interceptors are used, this `post_create_membership_binding_with_metadata` interceptor runs after the
        `post_create_membership_binding` interceptor. The (possibly modified) response returned by
        `post_create_membership_binding` will be passed to
        `post_create_membership_binding_with_metadata`.
        """
        return response, metadata

    def pre_create_membership_rbac_role_binding(
        self,
        request: service.CreateMembershipRBACRoleBindingRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.CreateMembershipRBACRoleBindingRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_membership_rbac_role_binding

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GkeHub server.
        """
        return request, metadata

    def post_create_membership_rbac_role_binding(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_membership_rbac_role_binding

        DEPRECATED. Please use the `post_create_membership_rbac_role_binding_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the GkeHub server but before
        it is returned to user code. This `post_create_membership_rbac_role_binding` interceptor runs
        before the `post_create_membership_rbac_role_binding_with_metadata` interceptor.
        """
        return response

    def post_create_membership_rbac_role_binding_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_membership_rbac_role_binding

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the GkeHub server but before it is returned to user code.

        We recommend only using this `post_create_membership_rbac_role_binding_with_metadata`
        interceptor in new development instead of the `post_create_membership_rbac_role_binding` interceptor.
        When both interceptors are used, this `post_create_membership_rbac_role_binding_with_metadata` interceptor runs after the
        `post_create_membership_rbac_role_binding` interceptor. The (possibly modified) response returned by
        `post_create_membership_rbac_role_binding` will be passed to
        `post_create_membership_rbac_role_binding_with_metadata`.
        """
        return response, metadata

    def pre_create_scope(
        self,
        request: service.CreateScopeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.CreateScopeRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_scope

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GkeHub server.
        """
        return request, metadata

    def post_create_scope(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_scope

        DEPRECATED. Please use the `post_create_scope_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the GkeHub server but before
        it is returned to user code. This `post_create_scope` interceptor runs
        before the `post_create_scope_with_metadata` interceptor.
        """
        return response

    def post_create_scope_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_scope

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the GkeHub server but before it is returned to user code.

        We recommend only using this `post_create_scope_with_metadata`
        interceptor in new development instead of the `post_create_scope` interceptor.
        When both interceptors are used, this `post_create_scope_with_metadata` interceptor runs after the
        `post_create_scope` interceptor. The (possibly modified) response returned by
        `post_create_scope` will be passed to
        `post_create_scope_with_metadata`.
        """
        return response, metadata

    def pre_create_scope_namespace(
        self,
        request: service.CreateScopeNamespaceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.CreateScopeNamespaceRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_scope_namespace

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GkeHub server.
        """
        return request, metadata

    def post_create_scope_namespace(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_scope_namespace

        DEPRECATED. Please use the `post_create_scope_namespace_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the GkeHub server but before
        it is returned to user code. This `post_create_scope_namespace` interceptor runs
        before the `post_create_scope_namespace_with_metadata` interceptor.
        """
        return response

    def post_create_scope_namespace_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_scope_namespace

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the GkeHub server but before it is returned to user code.

        We recommend only using this `post_create_scope_namespace_with_metadata`
        interceptor in new development instead of the `post_create_scope_namespace` interceptor.
        When both interceptors are used, this `post_create_scope_namespace_with_metadata` interceptor runs after the
        `post_create_scope_namespace` interceptor. The (possibly modified) response returned by
        `post_create_scope_namespace` will be passed to
        `post_create_scope_namespace_with_metadata`.
        """
        return response, metadata

    def pre_create_scope_rbac_role_binding(
        self,
        request: service.CreateScopeRBACRoleBindingRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.CreateScopeRBACRoleBindingRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_scope_rbac_role_binding

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GkeHub server.
        """
        return request, metadata

    def post_create_scope_rbac_role_binding(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_scope_rbac_role_binding

        DEPRECATED. Please use the `post_create_scope_rbac_role_binding_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the GkeHub server but before
        it is returned to user code. This `post_create_scope_rbac_role_binding` interceptor runs
        before the `post_create_scope_rbac_role_binding_with_metadata` interceptor.
        """
        return response

    def post_create_scope_rbac_role_binding_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_scope_rbac_role_binding

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the GkeHub server but before it is returned to user code.

        We recommend only using this `post_create_scope_rbac_role_binding_with_metadata`
        interceptor in new development instead of the `post_create_scope_rbac_role_binding` interceptor.
        When both interceptors are used, this `post_create_scope_rbac_role_binding_with_metadata` interceptor runs after the
        `post_create_scope_rbac_role_binding` interceptor. The (possibly modified) response returned by
        `post_create_scope_rbac_role_binding` will be passed to
        `post_create_scope_rbac_role_binding_with_metadata`.
        """
        return response, metadata

    def pre_delete_feature(
        self,
        request: service.DeleteFeatureRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.DeleteFeatureRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_feature

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GkeHub server.
        """
        return request, metadata

    def post_delete_feature(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_feature

        DEPRECATED. Please use the `post_delete_feature_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the GkeHub server but before
        it is returned to user code. This `post_delete_feature` interceptor runs
        before the `post_delete_feature_with_metadata` interceptor.
        """
        return response

    def post_delete_feature_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_feature

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the GkeHub server but before it is returned to user code.

        We recommend only using this `post_delete_feature_with_metadata`
        interceptor in new development instead of the `post_delete_feature` interceptor.
        When both interceptors are used, this `post_delete_feature_with_metadata` interceptor runs after the
        `post_delete_feature` interceptor. The (possibly modified) response returned by
        `post_delete_feature` will be passed to
        `post_delete_feature_with_metadata`.
        """
        return response, metadata

    def pre_delete_fleet(
        self,
        request: service.DeleteFleetRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.DeleteFleetRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_fleet

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GkeHub server.
        """
        return request, metadata

    def post_delete_fleet(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_fleet

        DEPRECATED. Please use the `post_delete_fleet_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the GkeHub server but before
        it is returned to user code. This `post_delete_fleet` interceptor runs
        before the `post_delete_fleet_with_metadata` interceptor.
        """
        return response

    def post_delete_fleet_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_fleet

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the GkeHub server but before it is returned to user code.

        We recommend only using this `post_delete_fleet_with_metadata`
        interceptor in new development instead of the `post_delete_fleet` interceptor.
        When both interceptors are used, this `post_delete_fleet_with_metadata` interceptor runs after the
        `post_delete_fleet` interceptor. The (possibly modified) response returned by
        `post_delete_fleet` will be passed to
        `post_delete_fleet_with_metadata`.
        """
        return response, metadata

    def pre_delete_membership(
        self,
        request: service.DeleteMembershipRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.DeleteMembershipRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_membership

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GkeHub server.
        """
        return request, metadata

    def post_delete_membership(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_membership

        DEPRECATED. Please use the `post_delete_membership_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the GkeHub server but before
        it is returned to user code. This `post_delete_membership` interceptor runs
        before the `post_delete_membership_with_metadata` interceptor.
        """
        return response

    def post_delete_membership_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_membership

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the GkeHub server but before it is returned to user code.

        We recommend only using this `post_delete_membership_with_metadata`
        interceptor in new development instead of the `post_delete_membership` interceptor.
        When both interceptors are used, this `post_delete_membership_with_metadata` interceptor runs after the
        `post_delete_membership` interceptor. The (possibly modified) response returned by
        `post_delete_membership` will be passed to
        `post_delete_membership_with_metadata`.
        """
        return response, metadata

    def pre_delete_membership_binding(
        self,
        request: service.DeleteMembershipBindingRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.DeleteMembershipBindingRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_membership_binding

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GkeHub server.
        """
        return request, metadata

    def post_delete_membership_binding(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_membership_binding

        DEPRECATED. Please use the `post_delete_membership_binding_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the GkeHub server but before
        it is returned to user code. This `post_delete_membership_binding` interceptor runs
        before the `post_delete_membership_binding_with_metadata` interceptor.
        """
        return response

    def post_delete_membership_binding_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_membership_binding

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the GkeHub server but before it is returned to user code.

        We recommend only using this `post_delete_membership_binding_with_metadata`
        interceptor in new development instead of the `post_delete_membership_binding` interceptor.
        When both interceptors are used, this `post_delete_membership_binding_with_metadata` interceptor runs after the
        `post_delete_membership_binding` interceptor. The (possibly modified) response returned by
        `post_delete_membership_binding` will be passed to
        `post_delete_membership_binding_with_metadata`.
        """
        return response, metadata

    def pre_delete_membership_rbac_role_binding(
        self,
        request: service.DeleteMembershipRBACRoleBindingRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.DeleteMembershipRBACRoleBindingRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_membership_rbac_role_binding

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GkeHub server.
        """
        return request, metadata

    def post_delete_membership_rbac_role_binding(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_membership_rbac_role_binding

        DEPRECATED. Please use the `post_delete_membership_rbac_role_binding_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the GkeHub server but before
        it is returned to user code. This `post_delete_membership_rbac_role_binding` interceptor runs
        before the `post_delete_membership_rbac_role_binding_with_metadata` interceptor.
        """
        return response

    def post_delete_membership_rbac_role_binding_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_membership_rbac_role_binding

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the GkeHub server but before it is returned to user code.

        We recommend only using this `post_delete_membership_rbac_role_binding_with_metadata`
        interceptor in new development instead of the `post_delete_membership_rbac_role_binding` interceptor.
        When both interceptors are used, this `post_delete_membership_rbac_role_binding_with_metadata` interceptor runs after the
        `post_delete_membership_rbac_role_binding` interceptor. The (possibly modified) response returned by
        `post_delete_membership_rbac_role_binding` will be passed to
        `post_delete_membership_rbac_role_binding_with_metadata`.
        """
        return response, metadata

    def pre_delete_scope(
        self,
        request: service.DeleteScopeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.DeleteScopeRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_scope

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GkeHub server.
        """
        return request, metadata

    def post_delete_scope(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_scope

        DEPRECATED. Please use the `post_delete_scope_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the GkeHub server but before
        it is returned to user code. This `post_delete_scope` interceptor runs
        before the `post_delete_scope_with_metadata` interceptor.
        """
        return response

    def post_delete_scope_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_scope

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the GkeHub server but before it is returned to user code.

        We recommend only using this `post_delete_scope_with_metadata`
        interceptor in new development instead of the `post_delete_scope` interceptor.
        When both interceptors are used, this `post_delete_scope_with_metadata` interceptor runs after the
        `post_delete_scope` interceptor. The (possibly modified) response returned by
        `post_delete_scope` will be passed to
        `post_delete_scope_with_metadata`.
        """
        return response, metadata

    def pre_delete_scope_namespace(
        self,
        request: service.DeleteScopeNamespaceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.DeleteScopeNamespaceRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_scope_namespace

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GkeHub server.
        """
        return request, metadata

    def post_delete_scope_namespace(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_scope_namespace

        DEPRECATED. Please use the `post_delete_scope_namespace_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the GkeHub server but before
        it is returned to user code. This `post_delete_scope_namespace` interceptor runs
        before the `post_delete_scope_namespace_with_metadata` interceptor.
        """
        return response

    def post_delete_scope_namespace_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_scope_namespace

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the GkeHub server but before it is returned to user code.

        We recommend only using this `post_delete_scope_namespace_with_metadata`
        interceptor in new development instead of the `post_delete_scope_namespace` interceptor.
        When both interceptors are used, this `post_delete_scope_namespace_with_metadata` interceptor runs after the
        `post_delete_scope_namespace` interceptor. The (possibly modified) response returned by
        `post_delete_scope_namespace` will be passed to
        `post_delete_scope_namespace_with_metadata`.
        """
        return response, metadata

    def pre_delete_scope_rbac_role_binding(
        self,
        request: service.DeleteScopeRBACRoleBindingRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.DeleteScopeRBACRoleBindingRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_scope_rbac_role_binding

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GkeHub server.
        """
        return request, metadata

    def post_delete_scope_rbac_role_binding(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_scope_rbac_role_binding

        DEPRECATED. Please use the `post_delete_scope_rbac_role_binding_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the GkeHub server but before
        it is returned to user code. This `post_delete_scope_rbac_role_binding` interceptor runs
        before the `post_delete_scope_rbac_role_binding_with_metadata` interceptor.
        """
        return response

    def post_delete_scope_rbac_role_binding_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_scope_rbac_role_binding

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the GkeHub server but before it is returned to user code.

        We recommend only using this `post_delete_scope_rbac_role_binding_with_metadata`
        interceptor in new development instead of the `post_delete_scope_rbac_role_binding` interceptor.
        When both interceptors are used, this `post_delete_scope_rbac_role_binding_with_metadata` interceptor runs after the
        `post_delete_scope_rbac_role_binding` interceptor. The (possibly modified) response returned by
        `post_delete_scope_rbac_role_binding` will be passed to
        `post_delete_scope_rbac_role_binding_with_metadata`.
        """
        return response, metadata

    def pre_generate_connect_manifest(
        self,
        request: service.GenerateConnectManifestRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.GenerateConnectManifestRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for generate_connect_manifest

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GkeHub server.
        """
        return request, metadata

    def post_generate_connect_manifest(
        self, response: service.GenerateConnectManifestResponse
    ) -> service.GenerateConnectManifestResponse:
        """Post-rpc interceptor for generate_connect_manifest

        DEPRECATED. Please use the `post_generate_connect_manifest_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the GkeHub server but before
        it is returned to user code. This `post_generate_connect_manifest` interceptor runs
        before the `post_generate_connect_manifest_with_metadata` interceptor.
        """
        return response

    def post_generate_connect_manifest_with_metadata(
        self,
        response: service.GenerateConnectManifestResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.GenerateConnectManifestResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for generate_connect_manifest

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the GkeHub server but before it is returned to user code.

        We recommend only using this `post_generate_connect_manifest_with_metadata`
        interceptor in new development instead of the `post_generate_connect_manifest` interceptor.
        When both interceptors are used, this `post_generate_connect_manifest_with_metadata` interceptor runs after the
        `post_generate_connect_manifest` interceptor. The (possibly modified) response returned by
        `post_generate_connect_manifest` will be passed to
        `post_generate_connect_manifest_with_metadata`.
        """
        return response, metadata

    def pre_generate_membership_rbac_role_binding_yaml(
        self,
        request: service.GenerateMembershipRBACRoleBindingYAMLRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.GenerateMembershipRBACRoleBindingYAMLRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for generate_membership_rbac_role_binding_yaml

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GkeHub server.
        """
        return request, metadata

    def post_generate_membership_rbac_role_binding_yaml(
        self, response: service.GenerateMembershipRBACRoleBindingYAMLResponse
    ) -> service.GenerateMembershipRBACRoleBindingYAMLResponse:
        """Post-rpc interceptor for generate_membership_rbac_role_binding_yaml

        DEPRECATED. Please use the `post_generate_membership_rbac_role_binding_yaml_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the GkeHub server but before
        it is returned to user code. This `post_generate_membership_rbac_role_binding_yaml` interceptor runs
        before the `post_generate_membership_rbac_role_binding_yaml_with_metadata` interceptor.
        """
        return response

    def post_generate_membership_rbac_role_binding_yaml_with_metadata(
        self,
        response: service.GenerateMembershipRBACRoleBindingYAMLResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.GenerateMembershipRBACRoleBindingYAMLResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for generate_membership_rbac_role_binding_yaml

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the GkeHub server but before it is returned to user code.

        We recommend only using this `post_generate_membership_rbac_role_binding_yaml_with_metadata`
        interceptor in new development instead of the `post_generate_membership_rbac_role_binding_yaml` interceptor.
        When both interceptors are used, this `post_generate_membership_rbac_role_binding_yaml_with_metadata` interceptor runs after the
        `post_generate_membership_rbac_role_binding_yaml` interceptor. The (possibly modified) response returned by
        `post_generate_membership_rbac_role_binding_yaml` will be passed to
        `post_generate_membership_rbac_role_binding_yaml_with_metadata`.
        """
        return response, metadata

    def pre_get_feature(
        self,
        request: service.GetFeatureRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.GetFeatureRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_feature

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GkeHub server.
        """
        return request, metadata

    def post_get_feature(self, response: feature.Feature) -> feature.Feature:
        """Post-rpc interceptor for get_feature

        DEPRECATED. Please use the `post_get_feature_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the GkeHub server but before
        it is returned to user code. This `post_get_feature` interceptor runs
        before the `post_get_feature_with_metadata` interceptor.
        """
        return response

    def post_get_feature_with_metadata(
        self,
        response: feature.Feature,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[feature.Feature, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_feature

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the GkeHub server but before it is returned to user code.

        We recommend only using this `post_get_feature_with_metadata`
        interceptor in new development instead of the `post_get_feature` interceptor.
        When both interceptors are used, this `post_get_feature_with_metadata` interceptor runs after the
        `post_get_feature` interceptor. The (possibly modified) response returned by
        `post_get_feature` will be passed to
        `post_get_feature_with_metadata`.
        """
        return response, metadata

    def pre_get_fleet(
        self,
        request: service.GetFleetRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.GetFleetRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_fleet

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GkeHub server.
        """
        return request, metadata

    def post_get_fleet(self, response: fleet.Fleet) -> fleet.Fleet:
        """Post-rpc interceptor for get_fleet

        DEPRECATED. Please use the `post_get_fleet_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the GkeHub server but before
        it is returned to user code. This `post_get_fleet` interceptor runs
        before the `post_get_fleet_with_metadata` interceptor.
        """
        return response

    def post_get_fleet_with_metadata(
        self, response: fleet.Fleet, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[fleet.Fleet, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_fleet

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the GkeHub server but before it is returned to user code.

        We recommend only using this `post_get_fleet_with_metadata`
        interceptor in new development instead of the `post_get_fleet` interceptor.
        When both interceptors are used, this `post_get_fleet_with_metadata` interceptor runs after the
        `post_get_fleet` interceptor. The (possibly modified) response returned by
        `post_get_fleet` will be passed to
        `post_get_fleet_with_metadata`.
        """
        return response, metadata

    def pre_get_membership(
        self,
        request: service.GetMembershipRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.GetMembershipRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_membership

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GkeHub server.
        """
        return request, metadata

    def post_get_membership(
        self, response: membership.Membership
    ) -> membership.Membership:
        """Post-rpc interceptor for get_membership

        DEPRECATED. Please use the `post_get_membership_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the GkeHub server but before
        it is returned to user code. This `post_get_membership` interceptor runs
        before the `post_get_membership_with_metadata` interceptor.
        """
        return response

    def post_get_membership_with_metadata(
        self,
        response: membership.Membership,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[membership.Membership, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_membership

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the GkeHub server but before it is returned to user code.

        We recommend only using this `post_get_membership_with_metadata`
        interceptor in new development instead of the `post_get_membership` interceptor.
        When both interceptors are used, this `post_get_membership_with_metadata` interceptor runs after the
        `post_get_membership` interceptor. The (possibly modified) response returned by
        `post_get_membership` will be passed to
        `post_get_membership_with_metadata`.
        """
        return response, metadata

    def pre_get_membership_binding(
        self,
        request: service.GetMembershipBindingRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.GetMembershipBindingRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_membership_binding

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GkeHub server.
        """
        return request, metadata

    def post_get_membership_binding(
        self, response: fleet.MembershipBinding
    ) -> fleet.MembershipBinding:
        """Post-rpc interceptor for get_membership_binding

        DEPRECATED. Please use the `post_get_membership_binding_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the GkeHub server but before
        it is returned to user code. This `post_get_membership_binding` interceptor runs
        before the `post_get_membership_binding_with_metadata` interceptor.
        """
        return response

    def post_get_membership_binding_with_metadata(
        self,
        response: fleet.MembershipBinding,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[fleet.MembershipBinding, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_membership_binding

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the GkeHub server but before it is returned to user code.

        We recommend only using this `post_get_membership_binding_with_metadata`
        interceptor in new development instead of the `post_get_membership_binding` interceptor.
        When both interceptors are used, this `post_get_membership_binding_with_metadata` interceptor runs after the
        `post_get_membership_binding` interceptor. The (possibly modified) response returned by
        `post_get_membership_binding` will be passed to
        `post_get_membership_binding_with_metadata`.
        """
        return response, metadata

    def pre_get_membership_rbac_role_binding(
        self,
        request: service.GetMembershipRBACRoleBindingRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.GetMembershipRBACRoleBindingRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_membership_rbac_role_binding

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GkeHub server.
        """
        return request, metadata

    def post_get_membership_rbac_role_binding(
        self, response: fleet.RBACRoleBinding
    ) -> fleet.RBACRoleBinding:
        """Post-rpc interceptor for get_membership_rbac_role_binding

        DEPRECATED. Please use the `post_get_membership_rbac_role_binding_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the GkeHub server but before
        it is returned to user code. This `post_get_membership_rbac_role_binding` interceptor runs
        before the `post_get_membership_rbac_role_binding_with_metadata` interceptor.
        """
        return response

    def post_get_membership_rbac_role_binding_with_metadata(
        self,
        response: fleet.RBACRoleBinding,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[fleet.RBACRoleBinding, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_membership_rbac_role_binding

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the GkeHub server but before it is returned to user code.

        We recommend only using this `post_get_membership_rbac_role_binding_with_metadata`
        interceptor in new development instead of the `post_get_membership_rbac_role_binding` interceptor.
        When both interceptors are used, this `post_get_membership_rbac_role_binding_with_metadata` interceptor runs after the
        `post_get_membership_rbac_role_binding` interceptor. The (possibly modified) response returned by
        `post_get_membership_rbac_role_binding` will be passed to
        `post_get_membership_rbac_role_binding_with_metadata`.
        """
        return response, metadata

    def pre_get_scope(
        self,
        request: service.GetScopeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.GetScopeRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_scope

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GkeHub server.
        """
        return request, metadata

    def post_get_scope(self, response: fleet.Scope) -> fleet.Scope:
        """Post-rpc interceptor for get_scope

        DEPRECATED. Please use the `post_get_scope_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the GkeHub server but before
        it is returned to user code. This `post_get_scope` interceptor runs
        before the `post_get_scope_with_metadata` interceptor.
        """
        return response

    def post_get_scope_with_metadata(
        self, response: fleet.Scope, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[fleet.Scope, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_scope

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the GkeHub server but before it is returned to user code.

        We recommend only using this `post_get_scope_with_metadata`
        interceptor in new development instead of the `post_get_scope` interceptor.
        When both interceptors are used, this `post_get_scope_with_metadata` interceptor runs after the
        `post_get_scope` interceptor. The (possibly modified) response returned by
        `post_get_scope` will be passed to
        `post_get_scope_with_metadata`.
        """
        return response, metadata

    def pre_get_scope_namespace(
        self,
        request: service.GetScopeNamespaceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.GetScopeNamespaceRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_scope_namespace

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GkeHub server.
        """
        return request, metadata

    def post_get_scope_namespace(self, response: fleet.Namespace) -> fleet.Namespace:
        """Post-rpc interceptor for get_scope_namespace

        DEPRECATED. Please use the `post_get_scope_namespace_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the GkeHub server but before
        it is returned to user code. This `post_get_scope_namespace` interceptor runs
        before the `post_get_scope_namespace_with_metadata` interceptor.
        """
        return response

    def post_get_scope_namespace_with_metadata(
        self,
        response: fleet.Namespace,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[fleet.Namespace, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_scope_namespace

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the GkeHub server but before it is returned to user code.

        We recommend only using this `post_get_scope_namespace_with_metadata`
        interceptor in new development instead of the `post_get_scope_namespace` interceptor.
        When both interceptors are used, this `post_get_scope_namespace_with_metadata` interceptor runs after the
        `post_get_scope_namespace` interceptor. The (possibly modified) response returned by
        `post_get_scope_namespace` will be passed to
        `post_get_scope_namespace_with_metadata`.
        """
        return response, metadata

    def pre_get_scope_rbac_role_binding(
        self,
        request: service.GetScopeRBACRoleBindingRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.GetScopeRBACRoleBindingRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_scope_rbac_role_binding

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GkeHub server.
        """
        return request, metadata

    def post_get_scope_rbac_role_binding(
        self, response: fleet.RBACRoleBinding
    ) -> fleet.RBACRoleBinding:
        """Post-rpc interceptor for get_scope_rbac_role_binding

        DEPRECATED. Please use the `post_get_scope_rbac_role_binding_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the GkeHub server but before
        it is returned to user code. This `post_get_scope_rbac_role_binding` interceptor runs
        before the `post_get_scope_rbac_role_binding_with_metadata` interceptor.
        """
        return response

    def post_get_scope_rbac_role_binding_with_metadata(
        self,
        response: fleet.RBACRoleBinding,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[fleet.RBACRoleBinding, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_scope_rbac_role_binding

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the GkeHub server but before it is returned to user code.

        We recommend only using this `post_get_scope_rbac_role_binding_with_metadata`
        interceptor in new development instead of the `post_get_scope_rbac_role_binding` interceptor.
        When both interceptors are used, this `post_get_scope_rbac_role_binding_with_metadata` interceptor runs after the
        `post_get_scope_rbac_role_binding` interceptor. The (possibly modified) response returned by
        `post_get_scope_rbac_role_binding` will be passed to
        `post_get_scope_rbac_role_binding_with_metadata`.
        """
        return response, metadata

    def pre_list_bound_memberships(
        self,
        request: service.ListBoundMembershipsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.ListBoundMembershipsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_bound_memberships

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GkeHub server.
        """
        return request, metadata

    def post_list_bound_memberships(
        self, response: service.ListBoundMembershipsResponse
    ) -> service.ListBoundMembershipsResponse:
        """Post-rpc interceptor for list_bound_memberships

        DEPRECATED. Please use the `post_list_bound_memberships_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the GkeHub server but before
        it is returned to user code. This `post_list_bound_memberships` interceptor runs
        before the `post_list_bound_memberships_with_metadata` interceptor.
        """
        return response

    def post_list_bound_memberships_with_metadata(
        self,
        response: service.ListBoundMembershipsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.ListBoundMembershipsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_bound_memberships

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the GkeHub server but before it is returned to user code.

        We recommend only using this `post_list_bound_memberships_with_metadata`
        interceptor in new development instead of the `post_list_bound_memberships` interceptor.
        When both interceptors are used, this `post_list_bound_memberships_with_metadata` interceptor runs after the
        `post_list_bound_memberships` interceptor. The (possibly modified) response returned by
        `post_list_bound_memberships` will be passed to
        `post_list_bound_memberships_with_metadata`.
        """
        return response, metadata

    def pre_list_features(
        self,
        request: service.ListFeaturesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ListFeaturesRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_features

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GkeHub server.
        """
        return request, metadata

    def post_list_features(
        self, response: service.ListFeaturesResponse
    ) -> service.ListFeaturesResponse:
        """Post-rpc interceptor for list_features

        DEPRECATED. Please use the `post_list_features_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the GkeHub server but before
        it is returned to user code. This `post_list_features` interceptor runs
        before the `post_list_features_with_metadata` interceptor.
        """
        return response

    def post_list_features_with_metadata(
        self,
        response: service.ListFeaturesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ListFeaturesResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_features

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the GkeHub server but before it is returned to user code.

        We recommend only using this `post_list_features_with_metadata`
        interceptor in new development instead of the `post_list_features` interceptor.
        When both interceptors are used, this `post_list_features_with_metadata` interceptor runs after the
        `post_list_features` interceptor. The (possibly modified) response returned by
        `post_list_features` will be passed to
        `post_list_features_with_metadata`.
        """
        return response, metadata

    def pre_list_fleets(
        self,
        request: service.ListFleetsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ListFleetsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_fleets

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GkeHub server.
        """
        return request, metadata

    def post_list_fleets(
        self, response: service.ListFleetsResponse
    ) -> service.ListFleetsResponse:
        """Post-rpc interceptor for list_fleets

        DEPRECATED. Please use the `post_list_fleets_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the GkeHub server but before
        it is returned to user code. This `post_list_fleets` interceptor runs
        before the `post_list_fleets_with_metadata` interceptor.
        """
        return response

    def post_list_fleets_with_metadata(
        self,
        response: service.ListFleetsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ListFleetsResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_fleets

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the GkeHub server but before it is returned to user code.

        We recommend only using this `post_list_fleets_with_metadata`
        interceptor in new development instead of the `post_list_fleets` interceptor.
        When both interceptors are used, this `post_list_fleets_with_metadata` interceptor runs after the
        `post_list_fleets` interceptor. The (possibly modified) response returned by
        `post_list_fleets` will be passed to
        `post_list_fleets_with_metadata`.
        """
        return response, metadata

    def pre_list_membership_bindings(
        self,
        request: service.ListMembershipBindingsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.ListMembershipBindingsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_membership_bindings

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GkeHub server.
        """
        return request, metadata

    def post_list_membership_bindings(
        self, response: service.ListMembershipBindingsResponse
    ) -> service.ListMembershipBindingsResponse:
        """Post-rpc interceptor for list_membership_bindings

        DEPRECATED. Please use the `post_list_membership_bindings_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the GkeHub server but before
        it is returned to user code. This `post_list_membership_bindings` interceptor runs
        before the `post_list_membership_bindings_with_metadata` interceptor.
        """
        return response

    def post_list_membership_bindings_with_metadata(
        self,
        response: service.ListMembershipBindingsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.ListMembershipBindingsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_membership_bindings

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the GkeHub server but before it is returned to user code.

        We recommend only using this `post_list_membership_bindings_with_metadata`
        interceptor in new development instead of the `post_list_membership_bindings` interceptor.
        When both interceptors are used, this `post_list_membership_bindings_with_metadata` interceptor runs after the
        `post_list_membership_bindings` interceptor. The (possibly modified) response returned by
        `post_list_membership_bindings` will be passed to
        `post_list_membership_bindings_with_metadata`.
        """
        return response, metadata

    def pre_list_membership_rbac_role_bindings(
        self,
        request: service.ListMembershipRBACRoleBindingsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.ListMembershipRBACRoleBindingsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_membership_rbac_role_bindings

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GkeHub server.
        """
        return request, metadata

    def post_list_membership_rbac_role_bindings(
        self, response: service.ListMembershipRBACRoleBindingsResponse
    ) -> service.ListMembershipRBACRoleBindingsResponse:
        """Post-rpc interceptor for list_membership_rbac_role_bindings

        DEPRECATED. Please use the `post_list_membership_rbac_role_bindings_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the GkeHub server but before
        it is returned to user code. This `post_list_membership_rbac_role_bindings` interceptor runs
        before the `post_list_membership_rbac_role_bindings_with_metadata` interceptor.
        """
        return response

    def post_list_membership_rbac_role_bindings_with_metadata(
        self,
        response: service.ListMembershipRBACRoleBindingsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.ListMembershipRBACRoleBindingsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_membership_rbac_role_bindings

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the GkeHub server but before it is returned to user code.

        We recommend only using this `post_list_membership_rbac_role_bindings_with_metadata`
        interceptor in new development instead of the `post_list_membership_rbac_role_bindings` interceptor.
        When both interceptors are used, this `post_list_membership_rbac_role_bindings_with_metadata` interceptor runs after the
        `post_list_membership_rbac_role_bindings` interceptor. The (possibly modified) response returned by
        `post_list_membership_rbac_role_bindings` will be passed to
        `post_list_membership_rbac_role_bindings_with_metadata`.
        """
        return response, metadata

    def pre_list_memberships(
        self,
        request: service.ListMembershipsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ListMembershipsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_memberships

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GkeHub server.
        """
        return request, metadata

    def post_list_memberships(
        self, response: service.ListMembershipsResponse
    ) -> service.ListMembershipsResponse:
        """Post-rpc interceptor for list_memberships

        DEPRECATED. Please use the `post_list_memberships_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the GkeHub server but before
        it is returned to user code. This `post_list_memberships` interceptor runs
        before the `post_list_memberships_with_metadata` interceptor.
        """
        return response

    def post_list_memberships_with_metadata(
        self,
        response: service.ListMembershipsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.ListMembershipsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_memberships

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the GkeHub server but before it is returned to user code.

        We recommend only using this `post_list_memberships_with_metadata`
        interceptor in new development instead of the `post_list_memberships` interceptor.
        When both interceptors are used, this `post_list_memberships_with_metadata` interceptor runs after the
        `post_list_memberships` interceptor. The (possibly modified) response returned by
        `post_list_memberships` will be passed to
        `post_list_memberships_with_metadata`.
        """
        return response, metadata

    def pre_list_permitted_scopes(
        self,
        request: service.ListPermittedScopesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.ListPermittedScopesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_permitted_scopes

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GkeHub server.
        """
        return request, metadata

    def post_list_permitted_scopes(
        self, response: service.ListPermittedScopesResponse
    ) -> service.ListPermittedScopesResponse:
        """Post-rpc interceptor for list_permitted_scopes

        DEPRECATED. Please use the `post_list_permitted_scopes_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the GkeHub server but before
        it is returned to user code. This `post_list_permitted_scopes` interceptor runs
        before the `post_list_permitted_scopes_with_metadata` interceptor.
        """
        return response

    def post_list_permitted_scopes_with_metadata(
        self,
        response: service.ListPermittedScopesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.ListPermittedScopesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_permitted_scopes

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the GkeHub server but before it is returned to user code.

        We recommend only using this `post_list_permitted_scopes_with_metadata`
        interceptor in new development instead of the `post_list_permitted_scopes` interceptor.
        When both interceptors are used, this `post_list_permitted_scopes_with_metadata` interceptor runs after the
        `post_list_permitted_scopes` interceptor. The (possibly modified) response returned by
        `post_list_permitted_scopes` will be passed to
        `post_list_permitted_scopes_with_metadata`.
        """
        return response, metadata

    def pre_list_scope_namespaces(
        self,
        request: service.ListScopeNamespacesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.ListScopeNamespacesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_scope_namespaces

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GkeHub server.
        """
        return request, metadata

    def post_list_scope_namespaces(
        self, response: service.ListScopeNamespacesResponse
    ) -> service.ListScopeNamespacesResponse:
        """Post-rpc interceptor for list_scope_namespaces

        DEPRECATED. Please use the `post_list_scope_namespaces_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the GkeHub server but before
        it is returned to user code. This `post_list_scope_namespaces` interceptor runs
        before the `post_list_scope_namespaces_with_metadata` interceptor.
        """
        return response

    def post_list_scope_namespaces_with_metadata(
        self,
        response: service.ListScopeNamespacesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.ListScopeNamespacesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_scope_namespaces

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the GkeHub server but before it is returned to user code.

        We recommend only using this `post_list_scope_namespaces_with_metadata`
        interceptor in new development instead of the `post_list_scope_namespaces` interceptor.
        When both interceptors are used, this `post_list_scope_namespaces_with_metadata` interceptor runs after the
        `post_list_scope_namespaces` interceptor. The (possibly modified) response returned by
        `post_list_scope_namespaces` will be passed to
        `post_list_scope_namespaces_with_metadata`.
        """
        return response, metadata

    def pre_list_scope_rbac_role_bindings(
        self,
        request: service.ListScopeRBACRoleBindingsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.ListScopeRBACRoleBindingsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_scope_rbac_role_bindings

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GkeHub server.
        """
        return request, metadata

    def post_list_scope_rbac_role_bindings(
        self, response: service.ListScopeRBACRoleBindingsResponse
    ) -> service.ListScopeRBACRoleBindingsResponse:
        """Post-rpc interceptor for list_scope_rbac_role_bindings

        DEPRECATED. Please use the `post_list_scope_rbac_role_bindings_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the GkeHub server but before
        it is returned to user code. This `post_list_scope_rbac_role_bindings` interceptor runs
        before the `post_list_scope_rbac_role_bindings_with_metadata` interceptor.
        """
        return response

    def post_list_scope_rbac_role_bindings_with_metadata(
        self,
        response: service.ListScopeRBACRoleBindingsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.ListScopeRBACRoleBindingsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_scope_rbac_role_bindings

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the GkeHub server but before it is returned to user code.

        We recommend only using this `post_list_scope_rbac_role_bindings_with_metadata`
        interceptor in new development instead of the `post_list_scope_rbac_role_bindings` interceptor.
        When both interceptors are used, this `post_list_scope_rbac_role_bindings_with_metadata` interceptor runs after the
        `post_list_scope_rbac_role_bindings` interceptor. The (possibly modified) response returned by
        `post_list_scope_rbac_role_bindings` will be passed to
        `post_list_scope_rbac_role_bindings_with_metadata`.
        """
        return response, metadata

    def pre_list_scopes(
        self,
        request: service.ListScopesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ListScopesRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_scopes

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GkeHub server.
        """
        return request, metadata

    def post_list_scopes(
        self, response: service.ListScopesResponse
    ) -> service.ListScopesResponse:
        """Post-rpc interceptor for list_scopes

        DEPRECATED. Please use the `post_list_scopes_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the GkeHub server but before
        it is returned to user code. This `post_list_scopes` interceptor runs
        before the `post_list_scopes_with_metadata` interceptor.
        """
        return response

    def post_list_scopes_with_metadata(
        self,
        response: service.ListScopesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ListScopesResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_scopes

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the GkeHub server but before it is returned to user code.

        We recommend only using this `post_list_scopes_with_metadata`
        interceptor in new development instead of the `post_list_scopes` interceptor.
        When both interceptors are used, this `post_list_scopes_with_metadata` interceptor runs after the
        `post_list_scopes` interceptor. The (possibly modified) response returned by
        `post_list_scopes` will be passed to
        `post_list_scopes_with_metadata`.
        """
        return response, metadata

    def pre_update_feature(
        self,
        request: service.UpdateFeatureRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.UpdateFeatureRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for update_feature

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GkeHub server.
        """
        return request, metadata

    def post_update_feature(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_feature

        DEPRECATED. Please use the `post_update_feature_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the GkeHub server but before
        it is returned to user code. This `post_update_feature` interceptor runs
        before the `post_update_feature_with_metadata` interceptor.
        """
        return response

    def post_update_feature_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_feature

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the GkeHub server but before it is returned to user code.

        We recommend only using this `post_update_feature_with_metadata`
        interceptor in new development instead of the `post_update_feature` interceptor.
        When both interceptors are used, this `post_update_feature_with_metadata` interceptor runs after the
        `post_update_feature` interceptor. The (possibly modified) response returned by
        `post_update_feature` will be passed to
        `post_update_feature_with_metadata`.
        """
        return response, metadata

    def pre_update_fleet(
        self,
        request: service.UpdateFleetRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.UpdateFleetRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for update_fleet

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GkeHub server.
        """
        return request, metadata

    def post_update_fleet(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_fleet

        DEPRECATED. Please use the `post_update_fleet_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the GkeHub server but before
        it is returned to user code. This `post_update_fleet` interceptor runs
        before the `post_update_fleet_with_metadata` interceptor.
        """
        return response

    def post_update_fleet_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_fleet

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the GkeHub server but before it is returned to user code.

        We recommend only using this `post_update_fleet_with_metadata`
        interceptor in new development instead of the `post_update_fleet` interceptor.
        When both interceptors are used, this `post_update_fleet_with_metadata` interceptor runs after the
        `post_update_fleet` interceptor. The (possibly modified) response returned by
        `post_update_fleet` will be passed to
        `post_update_fleet_with_metadata`.
        """
        return response, metadata

    def pre_update_membership(
        self,
        request: service.UpdateMembershipRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.UpdateMembershipRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_membership

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GkeHub server.
        """
        return request, metadata

    def post_update_membership(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_membership

        DEPRECATED. Please use the `post_update_membership_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the GkeHub server but before
        it is returned to user code. This `post_update_membership` interceptor runs
        before the `post_update_membership_with_metadata` interceptor.
        """
        return response

    def post_update_membership_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_membership

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the GkeHub server but before it is returned to user code.

        We recommend only using this `post_update_membership_with_metadata`
        interceptor in new development instead of the `post_update_membership` interceptor.
        When both interceptors are used, this `post_update_membership_with_metadata` interceptor runs after the
        `post_update_membership` interceptor. The (possibly modified) response returned by
        `post_update_membership` will be passed to
        `post_update_membership_with_metadata`.
        """
        return response, metadata

    def pre_update_membership_binding(
        self,
        request: service.UpdateMembershipBindingRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.UpdateMembershipBindingRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_membership_binding

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GkeHub server.
        """
        return request, metadata

    def post_update_membership_binding(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_membership_binding

        DEPRECATED. Please use the `post_update_membership_binding_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the GkeHub server but before
        it is returned to user code. This `post_update_membership_binding` interceptor runs
        before the `post_update_membership_binding_with_metadata` interceptor.
        """
        return response

    def post_update_membership_binding_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_membership_binding

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the GkeHub server but before it is returned to user code.

        We recommend only using this `post_update_membership_binding_with_metadata`
        interceptor in new development instead of the `post_update_membership_binding` interceptor.
        When both interceptors are used, this `post_update_membership_binding_with_metadata` interceptor runs after the
        `post_update_membership_binding` interceptor. The (possibly modified) response returned by
        `post_update_membership_binding` will be passed to
        `post_update_membership_binding_with_metadata`.
        """
        return response, metadata

    def pre_update_membership_rbac_role_binding(
        self,
        request: service.UpdateMembershipRBACRoleBindingRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.UpdateMembershipRBACRoleBindingRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_membership_rbac_role_binding

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GkeHub server.
        """
        return request, metadata

    def post_update_membership_rbac_role_binding(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_membership_rbac_role_binding

        DEPRECATED. Please use the `post_update_membership_rbac_role_binding_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the GkeHub server but before
        it is returned to user code. This `post_update_membership_rbac_role_binding` interceptor runs
        before the `post_update_membership_rbac_role_binding_with_metadata` interceptor.
        """
        return response

    def post_update_membership_rbac_role_binding_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_membership_rbac_role_binding

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the GkeHub server but before it is returned to user code.

        We recommend only using this `post_update_membership_rbac_role_binding_with_metadata`
        interceptor in new development instead of the `post_update_membership_rbac_role_binding` interceptor.
        When both interceptors are used, this `post_update_membership_rbac_role_binding_with_metadata` interceptor runs after the
        `post_update_membership_rbac_role_binding` interceptor. The (possibly modified) response returned by
        `post_update_membership_rbac_role_binding` will be passed to
        `post_update_membership_rbac_role_binding_with_metadata`.
        """
        return response, metadata

    def pre_update_scope(
        self,
        request: service.UpdateScopeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.UpdateScopeRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for update_scope

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GkeHub server.
        """
        return request, metadata

    def post_update_scope(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_scope

        DEPRECATED. Please use the `post_update_scope_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the GkeHub server but before
        it is returned to user code. This `post_update_scope` interceptor runs
        before the `post_update_scope_with_metadata` interceptor.
        """
        return response

    def post_update_scope_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_scope

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the GkeHub server but before it is returned to user code.

        We recommend only using this `post_update_scope_with_metadata`
        interceptor in new development instead of the `post_update_scope` interceptor.
        When both interceptors are used, this `post_update_scope_with_metadata` interceptor runs after the
        `post_update_scope` interceptor. The (possibly modified) response returned by
        `post_update_scope` will be passed to
        `post_update_scope_with_metadata`.
        """
        return response, metadata

    def pre_update_scope_namespace(
        self,
        request: service.UpdateScopeNamespaceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.UpdateScopeNamespaceRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_scope_namespace

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GkeHub server.
        """
        return request, metadata

    def post_update_scope_namespace(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_scope_namespace

        DEPRECATED. Please use the `post_update_scope_namespace_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the GkeHub server but before
        it is returned to user code. This `post_update_scope_namespace` interceptor runs
        before the `post_update_scope_namespace_with_metadata` interceptor.
        """
        return response

    def post_update_scope_namespace_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_scope_namespace

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the GkeHub server but before it is returned to user code.

        We recommend only using this `post_update_scope_namespace_with_metadata`
        interceptor in new development instead of the `post_update_scope_namespace` interceptor.
        When both interceptors are used, this `post_update_scope_namespace_with_metadata` interceptor runs after the
        `post_update_scope_namespace` interceptor. The (possibly modified) response returned by
        `post_update_scope_namespace` will be passed to
        `post_update_scope_namespace_with_metadata`.
        """
        return response, metadata

    def pre_update_scope_rbac_role_binding(
        self,
        request: service.UpdateScopeRBACRoleBindingRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.UpdateScopeRBACRoleBindingRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_scope_rbac_role_binding

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GkeHub server.
        """
        return request, metadata

    def post_update_scope_rbac_role_binding(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_scope_rbac_role_binding

        DEPRECATED. Please use the `post_update_scope_rbac_role_binding_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the GkeHub server but before
        it is returned to user code. This `post_update_scope_rbac_role_binding` interceptor runs
        before the `post_update_scope_rbac_role_binding_with_metadata` interceptor.
        """
        return response

    def post_update_scope_rbac_role_binding_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_scope_rbac_role_binding

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the GkeHub server but before it is returned to user code.

        We recommend only using this `post_update_scope_rbac_role_binding_with_metadata`
        interceptor in new development instead of the `post_update_scope_rbac_role_binding` interceptor.
        When both interceptors are used, this `post_update_scope_rbac_role_binding_with_metadata` interceptor runs after the
        `post_update_scope_rbac_role_binding` interceptor. The (possibly modified) response returned by
        `post_update_scope_rbac_role_binding` will be passed to
        `post_update_scope_rbac_role_binding_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class GkeHubRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: GkeHubRestInterceptor


class GkeHubRestTransport(_BaseGkeHubRestTransport):
    """REST backend synchronous transport for GkeHub.

    The GKE Hub service handles the registration of many Kubernetes
    clusters to Google Cloud, and the management of multi-cluster
    features over those clusters.

    The GKE Hub service operates on the following resources:

    - [Membership][google.cloud.gkehub.v1.Membership]
    - [Feature][google.cloud.gkehub.v1.Feature]

    GKE Hub is currently available in the global region and all regions
    in https://cloud.google.com/compute/docs/regions-zones. Feature is
    only available in global region while membership is global region
    and all the regions.

    **Membership management may be non-trivial:** it is recommended to
    use one of the Google-provided client libraries or tools where
    possible when working with Membership resources.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "gkehub.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[GkeHubRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'gkehub.googleapis.com').
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
            interceptor (Optional[GkeHubRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or GkeHubRestInterceptor()
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

    class _CreateFeature(_BaseGkeHubRestTransport._BaseCreateFeature, GkeHubRestStub):
        def __hash__(self):
            return hash("GkeHubRestTransport.CreateFeature")

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
            request: service.CreateFeatureRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create feature method over HTTP.

            Args:
                request (~.service.CreateFeatureRequest):
                    The request object. Request message for the ``GkeHub.CreateFeature`` method.
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
                _BaseGkeHubRestTransport._BaseCreateFeature._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_feature(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGkeHubRestTransport._BaseCreateFeature,
                    "_BaseCreateFeature__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gkehub_v1.GkeHubClient.CreateFeature",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "CreateFeature",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GkeHubRestTransport._CreateFeature._get_response(
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

            resp = self._interceptor.post_create_feature(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_feature_with_metadata(
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
                    "Received response for google.cloud.gkehub_v1.GkeHubClient.create_feature",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "CreateFeature",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateFleet(_BaseGkeHubRestTransport._BaseCreateFleet, GkeHubRestStub):
        def __hash__(self):
            return hash("GkeHubRestTransport.CreateFleet")

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
            request: service.CreateFleetRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create fleet method over HTTP.

            Args:
                request (~.service.CreateFleetRequest):
                    The request object. Request message for the ``GkeHub.CreateFleet`` method.
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

            http_options = _BaseGkeHubRestTransport._BaseCreateFleet._get_http_options()
            request, metadata = self._interceptor.pre_create_fleet(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGkeHubRestTransport._BaseCreateFleet,
                    "_BaseCreateFleet__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gkehub_v1.GkeHubClient.CreateFleet",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "CreateFleet",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GkeHubRestTransport._CreateFleet._get_response(
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

            resp = self._interceptor.post_create_fleet(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_fleet_with_metadata(
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
                    "Received response for google.cloud.gkehub_v1.GkeHubClient.create_fleet",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "CreateFleet",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateMembership(
        _BaseGkeHubRestTransport._BaseCreateMembership, GkeHubRestStub
    ):
        def __hash__(self):
            return hash("GkeHubRestTransport.CreateMembership")

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
            request: service.CreateMembershipRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create membership method over HTTP.

            Args:
                request (~.service.CreateMembershipRequest):
                    The request object. Request message for the ``GkeHub.CreateMembership``
                method.
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
                _BaseGkeHubRestTransport._BaseCreateMembership._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_membership(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGkeHubRestTransport._BaseCreateMembership,
                    "_BaseCreateMembership__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gkehub_v1.GkeHubClient.CreateMembership",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "CreateMembership",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GkeHubRestTransport._CreateMembership._get_response(
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

            resp = self._interceptor.post_create_membership(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_membership_with_metadata(
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
                    "Received response for google.cloud.gkehub_v1.GkeHubClient.create_membership",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "CreateMembership",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateMembershipBinding(
        _BaseGkeHubRestTransport._BaseCreateMembershipBinding, GkeHubRestStub
    ):
        def __hash__(self):
            return hash("GkeHubRestTransport.CreateMembershipBinding")

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
            request: service.CreateMembershipBindingRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create membership binding method over HTTP.

            Args:
                request (~.service.CreateMembershipBindingRequest):
                    The request object. Request to create a
                MembershipBinding.
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

            http_options = _BaseGkeHubRestTransport._BaseCreateMembershipBinding._get_http_options()
            request, metadata = self._interceptor.pre_create_membership_binding(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGkeHubRestTransport._BaseCreateMembershipBinding,
                    "_BaseCreateMembershipBinding__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gkehub_v1.GkeHubClient.CreateMembershipBinding",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "CreateMembershipBinding",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GkeHubRestTransport._CreateMembershipBinding._get_response(
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

            resp = self._interceptor.post_create_membership_binding(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_membership_binding_with_metadata(
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
                    "Received response for google.cloud.gkehub_v1.GkeHubClient.create_membership_binding",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "CreateMembershipBinding",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateMembershipRBACRoleBinding(
        _BaseGkeHubRestTransport._BaseCreateMembershipRBACRoleBinding, GkeHubRestStub
    ):
        def __hash__(self):
            return hash("GkeHubRestTransport.CreateMembershipRBACRoleBinding")

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
            request: service.CreateMembershipRBACRoleBindingRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create membership rbac
            role binding method over HTTP.

                Args:
                    request (~.service.CreateMembershipRBACRoleBindingRequest):
                        The request object. Request to create a rbacrolebindings.
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

            http_options = _BaseGkeHubRestTransport._BaseCreateMembershipRBACRoleBinding._get_http_options()
            request, metadata = (
                self._interceptor.pre_create_membership_rbac_role_binding(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGkeHubRestTransport._BaseCreateMembershipRBACRoleBinding,
                    "_BaseCreateMembershipRBACRoleBinding__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gkehub_v1.GkeHubClient.CreateMembershipRBACRoleBinding",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "CreateMembershipRBACRoleBinding",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                GkeHubRestTransport._CreateMembershipRBACRoleBinding._get_response(
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

            resp = self._interceptor.post_create_membership_rbac_role_binding(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_create_membership_rbac_role_binding_with_metadata(
                    resp, response_metadata
                )
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
                    "Received response for google.cloud.gkehub_v1.GkeHubClient.create_membership_rbac_role_binding",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "CreateMembershipRBACRoleBinding",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateScope(_BaseGkeHubRestTransport._BaseCreateScope, GkeHubRestStub):
        def __hash__(self):
            return hash("GkeHubRestTransport.CreateScope")

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
            request: service.CreateScopeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create scope method over HTTP.

            Args:
                request (~.service.CreateScopeRequest):
                    The request object. Request to create a Scope.
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

            http_options = _BaseGkeHubRestTransport._BaseCreateScope._get_http_options()
            request, metadata = self._interceptor.pre_create_scope(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGkeHubRestTransport._BaseCreateScope,
                    "_BaseCreateScope__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gkehub_v1.GkeHubClient.CreateScope",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "CreateScope",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GkeHubRestTransport._CreateScope._get_response(
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

            resp = self._interceptor.post_create_scope(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_scope_with_metadata(
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
                    "Received response for google.cloud.gkehub_v1.GkeHubClient.create_scope",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "CreateScope",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateScopeNamespace(
        _BaseGkeHubRestTransport._BaseCreateScopeNamespace, GkeHubRestStub
    ):
        def __hash__(self):
            return hash("GkeHubRestTransport.CreateScopeNamespace")

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
            request: service.CreateScopeNamespaceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create scope namespace method over HTTP.

            Args:
                request (~.service.CreateScopeNamespaceRequest):
                    The request object. Request to create a fleet namespace.
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
                _BaseGkeHubRestTransport._BaseCreateScopeNamespace._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_scope_namespace(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGkeHubRestTransport._BaseCreateScopeNamespace,
                    "_BaseCreateScopeNamespace__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gkehub_v1.GkeHubClient.CreateScopeNamespace",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "CreateScopeNamespace",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GkeHubRestTransport._CreateScopeNamespace._get_response(
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

            resp = self._interceptor.post_create_scope_namespace(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_scope_namespace_with_metadata(
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
                    "Received response for google.cloud.gkehub_v1.GkeHubClient.create_scope_namespace",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "CreateScopeNamespace",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateScopeRBACRoleBinding(
        _BaseGkeHubRestTransport._BaseCreateScopeRBACRoleBinding, GkeHubRestStub
    ):
        def __hash__(self):
            return hash("GkeHubRestTransport.CreateScopeRBACRoleBinding")

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
            request: service.CreateScopeRBACRoleBindingRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create scope rbac role
            binding method over HTTP.

                Args:
                    request (~.service.CreateScopeRBACRoleBindingRequest):
                        The request object. Request to create a rbacrolebindings.
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

            http_options = _BaseGkeHubRestTransport._BaseCreateScopeRBACRoleBinding._get_http_options()
            request, metadata = self._interceptor.pre_create_scope_rbac_role_binding(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGkeHubRestTransport._BaseCreateScopeRBACRoleBinding,
                    "_BaseCreateScopeRBACRoleBinding__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gkehub_v1.GkeHubClient.CreateScopeRBACRoleBinding",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "CreateScopeRBACRoleBinding",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GkeHubRestTransport._CreateScopeRBACRoleBinding._get_response(
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

            resp = self._interceptor.post_create_scope_rbac_role_binding(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_create_scope_rbac_role_binding_with_metadata(
                    resp, response_metadata
                )
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
                    "Received response for google.cloud.gkehub_v1.GkeHubClient.create_scope_rbac_role_binding",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "CreateScopeRBACRoleBinding",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteFeature(_BaseGkeHubRestTransport._BaseDeleteFeature, GkeHubRestStub):
        def __hash__(self):
            return hash("GkeHubRestTransport.DeleteFeature")

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
            request: service.DeleteFeatureRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete feature method over HTTP.

            Args:
                request (~.service.DeleteFeatureRequest):
                    The request object. Request message for ``GkeHub.DeleteFeature`` method.
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
                _BaseGkeHubRestTransport._BaseDeleteFeature._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_feature(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGkeHubRestTransport._BaseDeleteFeature,
                    "_BaseDeleteFeature__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gkehub_v1.GkeHubClient.DeleteFeature",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "DeleteFeature",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GkeHubRestTransport._DeleteFeature._get_response(
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

            resp = self._interceptor.post_delete_feature(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_feature_with_metadata(
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
                    "Received response for google.cloud.gkehub_v1.GkeHubClient.delete_feature",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "DeleteFeature",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteFleet(_BaseGkeHubRestTransport._BaseDeleteFleet, GkeHubRestStub):
        def __hash__(self):
            return hash("GkeHubRestTransport.DeleteFleet")

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
            request: service.DeleteFleetRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete fleet method over HTTP.

            Args:
                request (~.service.DeleteFleetRequest):
                    The request object. Request message for ``GkeHub.DeleteFleet`` method.
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

            http_options = _BaseGkeHubRestTransport._BaseDeleteFleet._get_http_options()
            request, metadata = self._interceptor.pre_delete_fleet(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGkeHubRestTransport._BaseDeleteFleet,
                    "_BaseDeleteFleet__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gkehub_v1.GkeHubClient.DeleteFleet",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "DeleteFleet",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GkeHubRestTransport._DeleteFleet._get_response(
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

            resp = self._interceptor.post_delete_fleet(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_fleet_with_metadata(
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
                    "Received response for google.cloud.gkehub_v1.GkeHubClient.delete_fleet",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "DeleteFleet",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteMembership(
        _BaseGkeHubRestTransport._BaseDeleteMembership, GkeHubRestStub
    ):
        def __hash__(self):
            return hash("GkeHubRestTransport.DeleteMembership")

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
            request: service.DeleteMembershipRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete membership method over HTTP.

            Args:
                request (~.service.DeleteMembershipRequest):
                    The request object. Request message for ``GkeHub.DeleteMembership`` method.
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
                _BaseGkeHubRestTransport._BaseDeleteMembership._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_membership(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGkeHubRestTransport._BaseDeleteMembership,
                    "_BaseDeleteMembership__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gkehub_v1.GkeHubClient.DeleteMembership",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "DeleteMembership",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GkeHubRestTransport._DeleteMembership._get_response(
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

            resp = self._interceptor.post_delete_membership(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_membership_with_metadata(
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
                    "Received response for google.cloud.gkehub_v1.GkeHubClient.delete_membership",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "DeleteMembership",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteMembershipBinding(
        _BaseGkeHubRestTransport._BaseDeleteMembershipBinding, GkeHubRestStub
    ):
        def __hash__(self):
            return hash("GkeHubRestTransport.DeleteMembershipBinding")

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
            request: service.DeleteMembershipBindingRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete membership binding method over HTTP.

            Args:
                request (~.service.DeleteMembershipBindingRequest):
                    The request object. Request to delete a Binding.
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

            http_options = _BaseGkeHubRestTransport._BaseDeleteMembershipBinding._get_http_options()
            request, metadata = self._interceptor.pre_delete_membership_binding(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGkeHubRestTransport._BaseDeleteMembershipBinding,
                    "_BaseDeleteMembershipBinding__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gkehub_v1.GkeHubClient.DeleteMembershipBinding",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "DeleteMembershipBinding",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GkeHubRestTransport._DeleteMembershipBinding._get_response(
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

            resp = self._interceptor.post_delete_membership_binding(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_membership_binding_with_metadata(
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
                    "Received response for google.cloud.gkehub_v1.GkeHubClient.delete_membership_binding",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "DeleteMembershipBinding",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteMembershipRBACRoleBinding(
        _BaseGkeHubRestTransport._BaseDeleteMembershipRBACRoleBinding, GkeHubRestStub
    ):
        def __hash__(self):
            return hash("GkeHubRestTransport.DeleteMembershipRBACRoleBinding")

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
            request: service.DeleteMembershipRBACRoleBindingRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete membership rbac
            role binding method over HTTP.

                Args:
                    request (~.service.DeleteMembershipRBACRoleBindingRequest):
                        The request object. Request to delete a Membership
                    RBACRoleBinding.
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

            http_options = _BaseGkeHubRestTransport._BaseDeleteMembershipRBACRoleBinding._get_http_options()
            request, metadata = (
                self._interceptor.pre_delete_membership_rbac_role_binding(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGkeHubRestTransport._BaseDeleteMembershipRBACRoleBinding,
                    "_BaseDeleteMembershipRBACRoleBinding__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gkehub_v1.GkeHubClient.DeleteMembershipRBACRoleBinding",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "DeleteMembershipRBACRoleBinding",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                GkeHubRestTransport._DeleteMembershipRBACRoleBinding._get_response(
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

            resp = self._interceptor.post_delete_membership_rbac_role_binding(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_delete_membership_rbac_role_binding_with_metadata(
                    resp, response_metadata
                )
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
                    "Received response for google.cloud.gkehub_v1.GkeHubClient.delete_membership_rbac_role_binding",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "DeleteMembershipRBACRoleBinding",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteScope(_BaseGkeHubRestTransport._BaseDeleteScope, GkeHubRestStub):
        def __hash__(self):
            return hash("GkeHubRestTransport.DeleteScope")

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
            request: service.DeleteScopeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete scope method over HTTP.

            Args:
                request (~.service.DeleteScopeRequest):
                    The request object. Request to delete a Scope.
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

            http_options = _BaseGkeHubRestTransport._BaseDeleteScope._get_http_options()
            request, metadata = self._interceptor.pre_delete_scope(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGkeHubRestTransport._BaseDeleteScope,
                    "_BaseDeleteScope__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gkehub_v1.GkeHubClient.DeleteScope",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "DeleteScope",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GkeHubRestTransport._DeleteScope._get_response(
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

            resp = self._interceptor.post_delete_scope(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_scope_with_metadata(
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
                    "Received response for google.cloud.gkehub_v1.GkeHubClient.delete_scope",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "DeleteScope",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteScopeNamespace(
        _BaseGkeHubRestTransport._BaseDeleteScopeNamespace, GkeHubRestStub
    ):
        def __hash__(self):
            return hash("GkeHubRestTransport.DeleteScopeNamespace")

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
            request: service.DeleteScopeNamespaceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete scope namespace method over HTTP.

            Args:
                request (~.service.DeleteScopeNamespaceRequest):
                    The request object. Request to delete a fleet namespace.
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
                _BaseGkeHubRestTransport._BaseDeleteScopeNamespace._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_scope_namespace(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGkeHubRestTransport._BaseDeleteScopeNamespace,
                    "_BaseDeleteScopeNamespace__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gkehub_v1.GkeHubClient.DeleteScopeNamespace",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "DeleteScopeNamespace",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GkeHubRestTransport._DeleteScopeNamespace._get_response(
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

            resp = self._interceptor.post_delete_scope_namespace(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_scope_namespace_with_metadata(
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
                    "Received response for google.cloud.gkehub_v1.GkeHubClient.delete_scope_namespace",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "DeleteScopeNamespace",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteScopeRBACRoleBinding(
        _BaseGkeHubRestTransport._BaseDeleteScopeRBACRoleBinding, GkeHubRestStub
    ):
        def __hash__(self):
            return hash("GkeHubRestTransport.DeleteScopeRBACRoleBinding")

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
            request: service.DeleteScopeRBACRoleBindingRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete scope rbac role
            binding method over HTTP.

                Args:
                    request (~.service.DeleteScopeRBACRoleBindingRequest):
                        The request object. Request to delete a Scope
                    RBACRoleBinding.
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

            http_options = _BaseGkeHubRestTransport._BaseDeleteScopeRBACRoleBinding._get_http_options()
            request, metadata = self._interceptor.pre_delete_scope_rbac_role_binding(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGkeHubRestTransport._BaseDeleteScopeRBACRoleBinding,
                    "_BaseDeleteScopeRBACRoleBinding__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gkehub_v1.GkeHubClient.DeleteScopeRBACRoleBinding",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "DeleteScopeRBACRoleBinding",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GkeHubRestTransport._DeleteScopeRBACRoleBinding._get_response(
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

            resp = self._interceptor.post_delete_scope_rbac_role_binding(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_delete_scope_rbac_role_binding_with_metadata(
                    resp, response_metadata
                )
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
                    "Received response for google.cloud.gkehub_v1.GkeHubClient.delete_scope_rbac_role_binding",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "DeleteScopeRBACRoleBinding",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GenerateConnectManifest(
        _BaseGkeHubRestTransport._BaseGenerateConnectManifest, GkeHubRestStub
    ):
        def __hash__(self):
            return hash("GkeHubRestTransport.GenerateConnectManifest")

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
            request: service.GenerateConnectManifestRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.GenerateConnectManifestResponse:
            r"""Call the generate connect manifest method over HTTP.

            Args:
                request (~.service.GenerateConnectManifestRequest):
                    The request object. Request message for ``GkeHub.GenerateConnectManifest``
                method. .
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.GenerateConnectManifestResponse:
                    GenerateConnectManifestResponse
                contains manifest information for
                installing/upgrading a Connect agent.

            """

            http_options = _BaseGkeHubRestTransport._BaseGenerateConnectManifest._get_http_options()
            request, metadata = self._interceptor.pre_generate_connect_manifest(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGkeHubRestTransport._BaseGenerateConnectManifest,
                    "_BaseGenerateConnectManifest__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gkehub_v1.GkeHubClient.GenerateConnectManifest",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "GenerateConnectManifest",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GkeHubRestTransport._GenerateConnectManifest._get_response(
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
            resp = service.GenerateConnectManifestResponse()
            pb_resp = service.GenerateConnectManifestResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_generate_connect_manifest(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_generate_connect_manifest_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.GenerateConnectManifestResponse.to_json(
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
                    "Received response for google.cloud.gkehub_v1.GkeHubClient.generate_connect_manifest",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "GenerateConnectManifest",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GenerateMembershipRBACRoleBindingYAML(
        _BaseGkeHubRestTransport._BaseGenerateMembershipRBACRoleBindingYAML,
        GkeHubRestStub,
    ):
        def __hash__(self):
            return hash("GkeHubRestTransport.GenerateMembershipRBACRoleBindingYAML")

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
            request: service.GenerateMembershipRBACRoleBindingYAMLRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.GenerateMembershipRBACRoleBindingYAMLResponse:
            r"""Call the generate membership rbac
            role binding yaml method over HTTP.

                Args:
                    request (~.service.GenerateMembershipRBACRoleBindingYAMLRequest):
                        The request object. Request to generate a YAML of the
                    RBAC policies for the specified
                    RoleBinding and its associated
                    impersonation resources.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.service.GenerateMembershipRBACRoleBindingYAMLResponse:
                        Response for
                    GenerateRBACRoleBindingYAML.

            """

            http_options = _BaseGkeHubRestTransport._BaseGenerateMembershipRBACRoleBindingYAML._get_http_options()
            request, metadata = (
                self._interceptor.pre_generate_membership_rbac_role_binding_yaml(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGkeHubRestTransport._BaseGenerateMembershipRBACRoleBindingYAML,
                    "_BaseGenerateMembershipRBACRoleBindingYAML__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gkehub_v1.GkeHubClient.GenerateMembershipRBACRoleBindingYAML",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "GenerateMembershipRBACRoleBindingYAML",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GkeHubRestTransport._GenerateMembershipRBACRoleBindingYAML._get_response(
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
            resp = service.GenerateMembershipRBACRoleBindingYAMLResponse()
            pb_resp = service.GenerateMembershipRBACRoleBindingYAMLResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_generate_membership_rbac_role_binding_yaml(
                resp
            )
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_generate_membership_rbac_role_binding_yaml_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        service.GenerateMembershipRBACRoleBindingYAMLResponse.to_json(
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
                    "Received response for google.cloud.gkehub_v1.GkeHubClient.generate_membership_rbac_role_binding_yaml",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "GenerateMembershipRBACRoleBindingYAML",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetFeature(_BaseGkeHubRestTransport._BaseGetFeature, GkeHubRestStub):
        def __hash__(self):
            return hash("GkeHubRestTransport.GetFeature")

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
            request: service.GetFeatureRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> feature.Feature:
            r"""Call the get feature method over HTTP.

            Args:
                request (~.service.GetFeatureRequest):
                    The request object. Request message for ``GkeHub.GetFeature`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.feature.Feature:
                    Feature represents the settings and
                status of any Fleet Feature.

            """

            http_options = _BaseGkeHubRestTransport._BaseGetFeature._get_http_options()
            request, metadata = self._interceptor.pre_get_feature(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGkeHubRestTransport._BaseGetFeature,
                    "_BaseGetFeature__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gkehub_v1.GkeHubClient.GetFeature",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "GetFeature",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GkeHubRestTransport._GetFeature._get_response(
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
            resp = feature.Feature()
            pb_resp = feature.Feature.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_feature(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_feature_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = feature.Feature.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.gkehub_v1.GkeHubClient.get_feature",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "GetFeature",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetFleet(_BaseGkeHubRestTransport._BaseGetFleet, GkeHubRestStub):
        def __hash__(self):
            return hash("GkeHubRestTransport.GetFleet")

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
            request: service.GetFleetRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> fleet.Fleet:
            r"""Call the get fleet method over HTTP.

            Args:
                request (~.service.GetFleetRequest):
                    The request object. Request message for the ``GkeHub.GetFleet`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.fleet.Fleet:
                    Fleet contains the Fleet-wide
                metadata and configuration.

            """

            http_options = _BaseGkeHubRestTransport._BaseGetFleet._get_http_options()
            request, metadata = self._interceptor.pre_get_fleet(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGkeHubRestTransport._BaseGetFleet,
                    "_BaseGetFleet__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gkehub_v1.GkeHubClient.GetFleet",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "GetFleet",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GkeHubRestTransport._GetFleet._get_response(
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
            resp = fleet.Fleet()
            pb_resp = fleet.Fleet.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_fleet(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_fleet_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = fleet.Fleet.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.gkehub_v1.GkeHubClient.get_fleet",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "GetFleet",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetMembership(_BaseGkeHubRestTransport._BaseGetMembership, GkeHubRestStub):
        def __hash__(self):
            return hash("GkeHubRestTransport.GetMembership")

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
            request: service.GetMembershipRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> membership.Membership:
            r"""Call the get membership method over HTTP.

            Args:
                request (~.service.GetMembershipRequest):
                    The request object. Request message for ``GkeHub.GetMembership`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.membership.Membership:
                    Membership contains information about
                a member cluster.

            """

            http_options = (
                _BaseGkeHubRestTransport._BaseGetMembership._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_membership(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGkeHubRestTransport._BaseGetMembership,
                    "_BaseGetMembership__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gkehub_v1.GkeHubClient.GetMembership",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "GetMembership",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GkeHubRestTransport._GetMembership._get_response(
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
            resp = membership.Membership()
            pb_resp = membership.Membership.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_membership(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_membership_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = membership.Membership.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.gkehub_v1.GkeHubClient.get_membership",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "GetMembership",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetMembershipBinding(
        _BaseGkeHubRestTransport._BaseGetMembershipBinding, GkeHubRestStub
    ):
        def __hash__(self):
            return hash("GkeHubRestTransport.GetMembershipBinding")

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
            request: service.GetMembershipBindingRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> fleet.MembershipBinding:
            r"""Call the get membership binding method over HTTP.

            Args:
                request (~.service.GetMembershipBindingRequest):
                    The request object. Request message for the ``GkeHub.GetMembershipBinding``
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.fleet.MembershipBinding:
                    MembershipBinding is a subresource of
                a Membership, representing what Fleet
                Scopes (or other, future Fleet
                resources) a Membership is bound to.

            """

            http_options = (
                _BaseGkeHubRestTransport._BaseGetMembershipBinding._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_membership_binding(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGkeHubRestTransport._BaseGetMembershipBinding,
                    "_BaseGetMembershipBinding__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gkehub_v1.GkeHubClient.GetMembershipBinding",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "GetMembershipBinding",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GkeHubRestTransport._GetMembershipBinding._get_response(
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
            resp = fleet.MembershipBinding()
            pb_resp = fleet.MembershipBinding.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_membership_binding(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_membership_binding_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = fleet.MembershipBinding.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.gkehub_v1.GkeHubClient.get_membership_binding",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "GetMembershipBinding",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetMembershipRBACRoleBinding(
        _BaseGkeHubRestTransport._BaseGetMembershipRBACRoleBinding, GkeHubRestStub
    ):
        def __hash__(self):
            return hash("GkeHubRestTransport.GetMembershipRBACRoleBinding")

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
            request: service.GetMembershipRBACRoleBindingRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> fleet.RBACRoleBinding:
            r"""Call the get membership rbac role
            binding method over HTTP.

                Args:
                    request (~.service.GetMembershipRBACRoleBindingRequest):
                        The request object. Request message for the
                    ``GkeHub.GetMembershipRBACRoleBinding`` method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.fleet.RBACRoleBinding:
                        RBACRoleBinding represents a
                    rbacrolebinding across the Fleet

            """

            http_options = _BaseGkeHubRestTransport._BaseGetMembershipRBACRoleBinding._get_http_options()
            request, metadata = self._interceptor.pre_get_membership_rbac_role_binding(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGkeHubRestTransport._BaseGetMembershipRBACRoleBinding,
                    "_BaseGetMembershipRBACRoleBinding__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gkehub_v1.GkeHubClient.GetMembershipRBACRoleBinding",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "GetMembershipRBACRoleBinding",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GkeHubRestTransport._GetMembershipRBACRoleBinding._get_response(
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
            resp = fleet.RBACRoleBinding()
            pb_resp = fleet.RBACRoleBinding.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_membership_rbac_role_binding(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_get_membership_rbac_role_binding_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = fleet.RBACRoleBinding.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.gkehub_v1.GkeHubClient.get_membership_rbac_role_binding",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "GetMembershipRBACRoleBinding",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetScope(_BaseGkeHubRestTransport._BaseGetScope, GkeHubRestStub):
        def __hash__(self):
            return hash("GkeHubRestTransport.GetScope")

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
            request: service.GetScopeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> fleet.Scope:
            r"""Call the get scope method over HTTP.

            Args:
                request (~.service.GetScopeRequest):
                    The request object. Request message for the ``GkeHub.GetScope`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.fleet.Scope:
                    Scope represents a Scope in a Fleet.
            """

            http_options = _BaseGkeHubRestTransport._BaseGetScope._get_http_options()
            request, metadata = self._interceptor.pre_get_scope(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGkeHubRestTransport._BaseGetScope,
                    "_BaseGetScope__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gkehub_v1.GkeHubClient.GetScope",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "GetScope",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GkeHubRestTransport._GetScope._get_response(
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
            resp = fleet.Scope()
            pb_resp = fleet.Scope.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_scope(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_scope_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = fleet.Scope.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.gkehub_v1.GkeHubClient.get_scope",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "GetScope",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetScopeNamespace(
        _BaseGkeHubRestTransport._BaseGetScopeNamespace, GkeHubRestStub
    ):
        def __hash__(self):
            return hash("GkeHubRestTransport.GetScopeNamespace")

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
            request: service.GetScopeNamespaceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> fleet.Namespace:
            r"""Call the get scope namespace method over HTTP.

            Args:
                request (~.service.GetScopeNamespaceRequest):
                    The request object. Request message for the ``GkeHub.GetNamespace`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.fleet.Namespace:
                    Namespace represents a namespace
                across the Fleet

            """

            http_options = (
                _BaseGkeHubRestTransport._BaseGetScopeNamespace._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_scope_namespace(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGkeHubRestTransport._BaseGetScopeNamespace,
                    "_BaseGetScopeNamespace__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gkehub_v1.GkeHubClient.GetScopeNamespace",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "GetScopeNamespace",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GkeHubRestTransport._GetScopeNamespace._get_response(
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
            resp = fleet.Namespace()
            pb_resp = fleet.Namespace.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_scope_namespace(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_scope_namespace_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = fleet.Namespace.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.gkehub_v1.GkeHubClient.get_scope_namespace",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "GetScopeNamespace",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetScopeRBACRoleBinding(
        _BaseGkeHubRestTransport._BaseGetScopeRBACRoleBinding, GkeHubRestStub
    ):
        def __hash__(self):
            return hash("GkeHubRestTransport.GetScopeRBACRoleBinding")

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
            request: service.GetScopeRBACRoleBindingRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> fleet.RBACRoleBinding:
            r"""Call the get scope rbac role
            binding method over HTTP.

                Args:
                    request (~.service.GetScopeRBACRoleBindingRequest):
                        The request object. Request message for the
                    ``GkeHub.GetScopeRBACRoleBinding`` method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.fleet.RBACRoleBinding:
                        RBACRoleBinding represents a
                    rbacrolebinding across the Fleet

            """

            http_options = _BaseGkeHubRestTransport._BaseGetScopeRBACRoleBinding._get_http_options()
            request, metadata = self._interceptor.pre_get_scope_rbac_role_binding(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGkeHubRestTransport._BaseGetScopeRBACRoleBinding,
                    "_BaseGetScopeRBACRoleBinding__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gkehub_v1.GkeHubClient.GetScopeRBACRoleBinding",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "GetScopeRBACRoleBinding",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GkeHubRestTransport._GetScopeRBACRoleBinding._get_response(
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
            resp = fleet.RBACRoleBinding()
            pb_resp = fleet.RBACRoleBinding.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_scope_rbac_role_binding(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_scope_rbac_role_binding_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = fleet.RBACRoleBinding.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.gkehub_v1.GkeHubClient.get_scope_rbac_role_binding",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "GetScopeRBACRoleBinding",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListBoundMemberships(
        _BaseGkeHubRestTransport._BaseListBoundMemberships, GkeHubRestStub
    ):
        def __hash__(self):
            return hash("GkeHubRestTransport.ListBoundMemberships")

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
            request: service.ListBoundMembershipsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.ListBoundMembershipsResponse:
            r"""Call the list bound memberships method over HTTP.

            Args:
                request (~.service.ListBoundMembershipsRequest):
                    The request object. Request to list Memberships bound to
                a Scope.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.ListBoundMembershipsResponse:
                    List of Memberships bound to a Scope.
            """

            http_options = (
                _BaseGkeHubRestTransport._BaseListBoundMemberships._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_bound_memberships(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGkeHubRestTransport._BaseListBoundMemberships,
                    "_BaseListBoundMemberships__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gkehub_v1.GkeHubClient.ListBoundMemberships",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "ListBoundMemberships",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GkeHubRestTransport._ListBoundMemberships._get_response(
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
            resp = service.ListBoundMembershipsResponse()
            pb_resp = service.ListBoundMembershipsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_bound_memberships(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_bound_memberships_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.ListBoundMembershipsResponse.to_json(
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
                    "Received response for google.cloud.gkehub_v1.GkeHubClient.list_bound_memberships",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "ListBoundMemberships",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListFeatures(_BaseGkeHubRestTransport._BaseListFeatures, GkeHubRestStub):
        def __hash__(self):
            return hash("GkeHubRestTransport.ListFeatures")

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
            request: service.ListFeaturesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.ListFeaturesResponse:
            r"""Call the list features method over HTTP.

            Args:
                request (~.service.ListFeaturesRequest):
                    The request object. Request message for ``GkeHub.ListFeatures`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.ListFeaturesResponse:
                    Response message for the ``GkeHub.ListFeatures`` method.
            """

            http_options = (
                _BaseGkeHubRestTransport._BaseListFeatures._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_features(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGkeHubRestTransport._BaseListFeatures,
                    "_BaseListFeatures__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gkehub_v1.GkeHubClient.ListFeatures",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "ListFeatures",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GkeHubRestTransport._ListFeatures._get_response(
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
            resp = service.ListFeaturesResponse()
            pb_resp = service.ListFeaturesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_features(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_features_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.ListFeaturesResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.gkehub_v1.GkeHubClient.list_features",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "ListFeatures",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListFleets(_BaseGkeHubRestTransport._BaseListFleets, GkeHubRestStub):
        def __hash__(self):
            return hash("GkeHubRestTransport.ListFleets")

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
            request: service.ListFleetsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.ListFleetsResponse:
            r"""Call the list fleets method over HTTP.

            Args:
                request (~.service.ListFleetsRequest):
                    The request object. Request message for the ``GkeHub.ListFleets`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.ListFleetsResponse:
                    Response message for the ``GkeHub.ListFleetsResponse``
                method.

            """

            http_options = _BaseGkeHubRestTransport._BaseListFleets._get_http_options()
            request, metadata = self._interceptor.pre_list_fleets(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGkeHubRestTransport._BaseListFleets,
                    "_BaseListFleets__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gkehub_v1.GkeHubClient.ListFleets",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "ListFleets",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GkeHubRestTransport._ListFleets._get_response(
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
            resp = service.ListFleetsResponse()
            pb_resp = service.ListFleetsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_fleets(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_fleets_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.ListFleetsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.gkehub_v1.GkeHubClient.list_fleets",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "ListFleets",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListMembershipBindings(
        _BaseGkeHubRestTransport._BaseListMembershipBindings, GkeHubRestStub
    ):
        def __hash__(self):
            return hash("GkeHubRestTransport.ListMembershipBindings")

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
            request: service.ListMembershipBindingsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.ListMembershipBindingsResponse:
            r"""Call the list membership bindings method over HTTP.

            Args:
                request (~.service.ListMembershipBindingsRequest):
                    The request object. Request to list MembershipBinding.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.ListMembershipBindingsResponse:
                    List of MembershipBindings.
            """

            http_options = (
                _BaseGkeHubRestTransport._BaseListMembershipBindings._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_membership_bindings(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGkeHubRestTransport._BaseListMembershipBindings,
                    "_BaseListMembershipBindings__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gkehub_v1.GkeHubClient.ListMembershipBindings",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "ListMembershipBindings",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GkeHubRestTransport._ListMembershipBindings._get_response(
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
            resp = service.ListMembershipBindingsResponse()
            pb_resp = service.ListMembershipBindingsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_membership_bindings(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_membership_bindings_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.ListMembershipBindingsResponse.to_json(
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
                    "Received response for google.cloud.gkehub_v1.GkeHubClient.list_membership_bindings",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "ListMembershipBindings",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListMembershipRBACRoleBindings(
        _BaseGkeHubRestTransport._BaseListMembershipRBACRoleBindings, GkeHubRestStub
    ):
        def __hash__(self):
            return hash("GkeHubRestTransport.ListMembershipRBACRoleBindings")

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
            request: service.ListMembershipRBACRoleBindingsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.ListMembershipRBACRoleBindingsResponse:
            r"""Call the list membership rbac role
            bindings method over HTTP.

                Args:
                    request (~.service.ListMembershipRBACRoleBindingsRequest):
                        The request object. Request to list Membership
                    RBACRoleBindings.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.service.ListMembershipRBACRoleBindingsResponse:
                        List of Membership RBACRoleBindings.
            """

            http_options = _BaseGkeHubRestTransport._BaseListMembershipRBACRoleBindings._get_http_options()
            request, metadata = (
                self._interceptor.pre_list_membership_rbac_role_bindings(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGkeHubRestTransport._BaseListMembershipRBACRoleBindings,
                    "_BaseListMembershipRBACRoleBindings__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gkehub_v1.GkeHubClient.ListMembershipRBACRoleBindings",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "ListMembershipRBACRoleBindings",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                GkeHubRestTransport._ListMembershipRBACRoleBindings._get_response(
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
            resp = service.ListMembershipRBACRoleBindingsResponse()
            pb_resp = service.ListMembershipRBACRoleBindingsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_membership_rbac_role_bindings(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_list_membership_rbac_role_bindings_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        service.ListMembershipRBACRoleBindingsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.gkehub_v1.GkeHubClient.list_membership_rbac_role_bindings",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "ListMembershipRBACRoleBindings",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListMemberships(
        _BaseGkeHubRestTransport._BaseListMemberships, GkeHubRestStub
    ):
        def __hash__(self):
            return hash("GkeHubRestTransport.ListMemberships")

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
            request: service.ListMembershipsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.ListMembershipsResponse:
            r"""Call the list memberships method over HTTP.

            Args:
                request (~.service.ListMembershipsRequest):
                    The request object. Request message for ``GkeHub.ListMemberships`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.ListMembershipsResponse:
                    Response message for the ``GkeHub.ListMemberships``
                method.

            """

            http_options = (
                _BaseGkeHubRestTransport._BaseListMemberships._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_memberships(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGkeHubRestTransport._BaseListMemberships,
                    "_BaseListMemberships__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gkehub_v1.GkeHubClient.ListMemberships",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "ListMemberships",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GkeHubRestTransport._ListMemberships._get_response(
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
            resp = service.ListMembershipsResponse()
            pb_resp = service.ListMembershipsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_memberships(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_memberships_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.ListMembershipsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.gkehub_v1.GkeHubClient.list_memberships",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "ListMemberships",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListPermittedScopes(
        _BaseGkeHubRestTransport._BaseListPermittedScopes, GkeHubRestStub
    ):
        def __hash__(self):
            return hash("GkeHubRestTransport.ListPermittedScopes")

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
            request: service.ListPermittedScopesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.ListPermittedScopesResponse:
            r"""Call the list permitted scopes method over HTTP.

            Args:
                request (~.service.ListPermittedScopesRequest):
                    The request object. Request to list permitted Scopes.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.ListPermittedScopesResponse:
                    List of permitted Scopes.
            """

            http_options = (
                _BaseGkeHubRestTransport._BaseListPermittedScopes._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_permitted_scopes(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGkeHubRestTransport._BaseListPermittedScopes,
                    "_BaseListPermittedScopes__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gkehub_v1.GkeHubClient.ListPermittedScopes",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "ListPermittedScopes",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GkeHubRestTransport._ListPermittedScopes._get_response(
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
            resp = service.ListPermittedScopesResponse()
            pb_resp = service.ListPermittedScopesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_permitted_scopes(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_permitted_scopes_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.ListPermittedScopesResponse.to_json(
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
                    "Received response for google.cloud.gkehub_v1.GkeHubClient.list_permitted_scopes",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "ListPermittedScopes",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListScopeNamespaces(
        _BaseGkeHubRestTransport._BaseListScopeNamespaces, GkeHubRestStub
    ):
        def __hash__(self):
            return hash("GkeHubRestTransport.ListScopeNamespaces")

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
            request: service.ListScopeNamespacesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.ListScopeNamespacesResponse:
            r"""Call the list scope namespaces method over HTTP.

            Args:
                request (~.service.ListScopeNamespacesRequest):
                    The request object. Request to list fleet namespaces.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.ListScopeNamespacesResponse:
                    List of fleet namespaces.
            """

            http_options = (
                _BaseGkeHubRestTransport._BaseListScopeNamespaces._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_scope_namespaces(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGkeHubRestTransport._BaseListScopeNamespaces,
                    "_BaseListScopeNamespaces__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gkehub_v1.GkeHubClient.ListScopeNamespaces",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "ListScopeNamespaces",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GkeHubRestTransport._ListScopeNamespaces._get_response(
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
            resp = service.ListScopeNamespacesResponse()
            pb_resp = service.ListScopeNamespacesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_scope_namespaces(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_scope_namespaces_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.ListScopeNamespacesResponse.to_json(
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
                    "Received response for google.cloud.gkehub_v1.GkeHubClient.list_scope_namespaces",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "ListScopeNamespaces",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListScopeRBACRoleBindings(
        _BaseGkeHubRestTransport._BaseListScopeRBACRoleBindings, GkeHubRestStub
    ):
        def __hash__(self):
            return hash("GkeHubRestTransport.ListScopeRBACRoleBindings")

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
            request: service.ListScopeRBACRoleBindingsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.ListScopeRBACRoleBindingsResponse:
            r"""Call the list scope rbac role
            bindings method over HTTP.

                Args:
                    request (~.service.ListScopeRBACRoleBindingsRequest):
                        The request object. Request to list Scope
                    RBACRoleBindings.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.service.ListScopeRBACRoleBindingsResponse:
                        List of Scope RBACRoleBindings.
            """

            http_options = _BaseGkeHubRestTransport._BaseListScopeRBACRoleBindings._get_http_options()
            request, metadata = self._interceptor.pre_list_scope_rbac_role_bindings(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGkeHubRestTransport._BaseListScopeRBACRoleBindings,
                    "_BaseListScopeRBACRoleBindings__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gkehub_v1.GkeHubClient.ListScopeRBACRoleBindings",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "ListScopeRBACRoleBindings",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GkeHubRestTransport._ListScopeRBACRoleBindings._get_response(
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
            resp = service.ListScopeRBACRoleBindingsResponse()
            pb_resp = service.ListScopeRBACRoleBindingsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_scope_rbac_role_bindings(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_list_scope_rbac_role_bindings_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        service.ListScopeRBACRoleBindingsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.gkehub_v1.GkeHubClient.list_scope_rbac_role_bindings",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "ListScopeRBACRoleBindings",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListScopes(_BaseGkeHubRestTransport._BaseListScopes, GkeHubRestStub):
        def __hash__(self):
            return hash("GkeHubRestTransport.ListScopes")

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
            request: service.ListScopesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.ListScopesResponse:
            r"""Call the list scopes method over HTTP.

            Args:
                request (~.service.ListScopesRequest):
                    The request object. Request to list Scopes.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.ListScopesResponse:
                    List of Scopes.
            """

            http_options = _BaseGkeHubRestTransport._BaseListScopes._get_http_options()
            request, metadata = self._interceptor.pre_list_scopes(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGkeHubRestTransport._BaseListScopes,
                    "_BaseListScopes__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gkehub_v1.GkeHubClient.ListScopes",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "ListScopes",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GkeHubRestTransport._ListScopes._get_response(
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
            resp = service.ListScopesResponse()
            pb_resp = service.ListScopesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_scopes(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_scopes_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.ListScopesResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.gkehub_v1.GkeHubClient.list_scopes",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "ListScopes",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateFeature(_BaseGkeHubRestTransport._BaseUpdateFeature, GkeHubRestStub):
        def __hash__(self):
            return hash("GkeHubRestTransport.UpdateFeature")

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
            request: service.UpdateFeatureRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update feature method over HTTP.

            Args:
                request (~.service.UpdateFeatureRequest):
                    The request object. Request message for ``GkeHub.UpdateFeature`` method.
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
                _BaseGkeHubRestTransport._BaseUpdateFeature._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_feature(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGkeHubRestTransport._BaseUpdateFeature,
                    "_BaseUpdateFeature__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gkehub_v1.GkeHubClient.UpdateFeature",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "UpdateFeature",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GkeHubRestTransport._UpdateFeature._get_response(
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

            resp = self._interceptor.post_update_feature(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_feature_with_metadata(
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
                    "Received response for google.cloud.gkehub_v1.GkeHubClient.update_feature",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "UpdateFeature",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateFleet(_BaseGkeHubRestTransport._BaseUpdateFleet, GkeHubRestStub):
        def __hash__(self):
            return hash("GkeHubRestTransport.UpdateFleet")

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
            request: service.UpdateFleetRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update fleet method over HTTP.

            Args:
                request (~.service.UpdateFleetRequest):
                    The request object. Request message for the ``GkeHub.UpdateFleet`` method.
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

            http_options = _BaseGkeHubRestTransport._BaseUpdateFleet._get_http_options()
            request, metadata = self._interceptor.pre_update_fleet(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGkeHubRestTransport._BaseUpdateFleet,
                    "_BaseUpdateFleet__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gkehub_v1.GkeHubClient.UpdateFleet",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "UpdateFleet",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GkeHubRestTransport._UpdateFleet._get_response(
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

            resp = self._interceptor.post_update_fleet(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_fleet_with_metadata(
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
                    "Received response for google.cloud.gkehub_v1.GkeHubClient.update_fleet",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "UpdateFleet",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateMembership(
        _BaseGkeHubRestTransport._BaseUpdateMembership, GkeHubRestStub
    ):
        def __hash__(self):
            return hash("GkeHubRestTransport.UpdateMembership")

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
            request: service.UpdateMembershipRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update membership method over HTTP.

            Args:
                request (~.service.UpdateMembershipRequest):
                    The request object. Request message for ``GkeHub.UpdateMembership`` method.
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
                _BaseGkeHubRestTransport._BaseUpdateMembership._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_membership(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGkeHubRestTransport._BaseUpdateMembership,
                    "_BaseUpdateMembership__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gkehub_v1.GkeHubClient.UpdateMembership",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "UpdateMembership",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GkeHubRestTransport._UpdateMembership._get_response(
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

            resp = self._interceptor.post_update_membership(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_membership_with_metadata(
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
                    "Received response for google.cloud.gkehub_v1.GkeHubClient.update_membership",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "UpdateMembership",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateMembershipBinding(
        _BaseGkeHubRestTransport._BaseUpdateMembershipBinding, GkeHubRestStub
    ):
        def __hash__(self):
            return hash("GkeHubRestTransport.UpdateMembershipBinding")

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
            request: service.UpdateMembershipBindingRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update membership binding method over HTTP.

            Args:
                request (~.service.UpdateMembershipBindingRequest):
                    The request object. Request to update a
                MembershipBinding.
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

            http_options = _BaseGkeHubRestTransport._BaseUpdateMembershipBinding._get_http_options()
            request, metadata = self._interceptor.pre_update_membership_binding(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGkeHubRestTransport._BaseUpdateMembershipBinding,
                    "_BaseUpdateMembershipBinding__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gkehub_v1.GkeHubClient.UpdateMembershipBinding",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "UpdateMembershipBinding",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GkeHubRestTransport._UpdateMembershipBinding._get_response(
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

            resp = self._interceptor.post_update_membership_binding(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_membership_binding_with_metadata(
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
                    "Received response for google.cloud.gkehub_v1.GkeHubClient.update_membership_binding",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "UpdateMembershipBinding",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateMembershipRBACRoleBinding(
        _BaseGkeHubRestTransport._BaseUpdateMembershipRBACRoleBinding, GkeHubRestStub
    ):
        def __hash__(self):
            return hash("GkeHubRestTransport.UpdateMembershipRBACRoleBinding")

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
            request: service.UpdateMembershipRBACRoleBindingRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update membership rbac
            role binding method over HTTP.

                Args:
                    request (~.service.UpdateMembershipRBACRoleBindingRequest):
                        The request object. Request to update a membership
                    rbacrolebinding.
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

            http_options = _BaseGkeHubRestTransport._BaseUpdateMembershipRBACRoleBinding._get_http_options()
            request, metadata = (
                self._interceptor.pre_update_membership_rbac_role_binding(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGkeHubRestTransport._BaseUpdateMembershipRBACRoleBinding,
                    "_BaseUpdateMembershipRBACRoleBinding__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gkehub_v1.GkeHubClient.UpdateMembershipRBACRoleBinding",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "UpdateMembershipRBACRoleBinding",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                GkeHubRestTransport._UpdateMembershipRBACRoleBinding._get_response(
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

            resp = self._interceptor.post_update_membership_rbac_role_binding(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_update_membership_rbac_role_binding_with_metadata(
                    resp, response_metadata
                )
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
                    "Received response for google.cloud.gkehub_v1.GkeHubClient.update_membership_rbac_role_binding",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "UpdateMembershipRBACRoleBinding",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateScope(_BaseGkeHubRestTransport._BaseUpdateScope, GkeHubRestStub):
        def __hash__(self):
            return hash("GkeHubRestTransport.UpdateScope")

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
            request: service.UpdateScopeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update scope method over HTTP.

            Args:
                request (~.service.UpdateScopeRequest):
                    The request object. Request to update a Scope.
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

            http_options = _BaseGkeHubRestTransport._BaseUpdateScope._get_http_options()
            request, metadata = self._interceptor.pre_update_scope(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGkeHubRestTransport._BaseUpdateScope,
                    "_BaseUpdateScope__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gkehub_v1.GkeHubClient.UpdateScope",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "UpdateScope",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GkeHubRestTransport._UpdateScope._get_response(
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

            resp = self._interceptor.post_update_scope(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_scope_with_metadata(
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
                    "Received response for google.cloud.gkehub_v1.GkeHubClient.update_scope",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "UpdateScope",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateScopeNamespace(
        _BaseGkeHubRestTransport._BaseUpdateScopeNamespace, GkeHubRestStub
    ):
        def __hash__(self):
            return hash("GkeHubRestTransport.UpdateScopeNamespace")

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
            request: service.UpdateScopeNamespaceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update scope namespace method over HTTP.

            Args:
                request (~.service.UpdateScopeNamespaceRequest):
                    The request object. Request to update a fleet namespace.
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
                _BaseGkeHubRestTransport._BaseUpdateScopeNamespace._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_scope_namespace(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGkeHubRestTransport._BaseUpdateScopeNamespace,
                    "_BaseUpdateScopeNamespace__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gkehub_v1.GkeHubClient.UpdateScopeNamespace",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "UpdateScopeNamespace",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GkeHubRestTransport._UpdateScopeNamespace._get_response(
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

            resp = self._interceptor.post_update_scope_namespace(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_scope_namespace_with_metadata(
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
                    "Received response for google.cloud.gkehub_v1.GkeHubClient.update_scope_namespace",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "UpdateScopeNamespace",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateScopeRBACRoleBinding(
        _BaseGkeHubRestTransport._BaseUpdateScopeRBACRoleBinding, GkeHubRestStub
    ):
        def __hash__(self):
            return hash("GkeHubRestTransport.UpdateScopeRBACRoleBinding")

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
            request: service.UpdateScopeRBACRoleBindingRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update scope rbac role
            binding method over HTTP.

                Args:
                    request (~.service.UpdateScopeRBACRoleBindingRequest):
                        The request object. Request to update a scope
                    rbacrolebinding.
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

            http_options = _BaseGkeHubRestTransport._BaseUpdateScopeRBACRoleBinding._get_http_options()
            request, metadata = self._interceptor.pre_update_scope_rbac_role_binding(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGkeHubRestTransport._BaseUpdateScopeRBACRoleBinding,
                    "_BaseUpdateScopeRBACRoleBinding__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.gkehub_v1.GkeHubClient.UpdateScopeRBACRoleBinding",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "UpdateScopeRBACRoleBinding",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GkeHubRestTransport._UpdateScopeRBACRoleBinding._get_response(
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

            resp = self._interceptor.post_update_scope_rbac_role_binding(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_update_scope_rbac_role_binding_with_metadata(
                    resp, response_metadata
                )
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
                    "Received response for google.cloud.gkehub_v1.GkeHubClient.update_scope_rbac_role_binding",
                    extra={
                        "serviceName": "google.cloud.gkehub.v1.GkeHub",
                        "rpcName": "UpdateScopeRBACRoleBinding",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_feature(
        self,
    ) -> Callable[[service.CreateFeatureRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateFeature(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_fleet(
        self,
    ) -> Callable[[service.CreateFleetRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateFleet(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_membership(
        self,
    ) -> Callable[[service.CreateMembershipRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateMembership(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_membership_binding(
        self,
    ) -> Callable[[service.CreateMembershipBindingRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateMembershipBinding(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_membership_rbac_role_binding(
        self,
    ) -> Callable[
        [service.CreateMembershipRBACRoleBindingRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateMembershipRBACRoleBinding(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_scope(
        self,
    ) -> Callable[[service.CreateScopeRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateScope(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_scope_namespace(
        self,
    ) -> Callable[[service.CreateScopeNamespaceRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateScopeNamespace(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_scope_rbac_role_binding(
        self,
    ) -> Callable[
        [service.CreateScopeRBACRoleBindingRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateScopeRBACRoleBinding(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_feature(
        self,
    ) -> Callable[[service.DeleteFeatureRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteFeature(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_fleet(
        self,
    ) -> Callable[[service.DeleteFleetRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteFleet(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_membership(
        self,
    ) -> Callable[[service.DeleteMembershipRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteMembership(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_membership_binding(
        self,
    ) -> Callable[[service.DeleteMembershipBindingRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteMembershipBinding(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_membership_rbac_role_binding(
        self,
    ) -> Callable[
        [service.DeleteMembershipRBACRoleBindingRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteMembershipRBACRoleBinding(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_scope(
        self,
    ) -> Callable[[service.DeleteScopeRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteScope(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_scope_namespace(
        self,
    ) -> Callable[[service.DeleteScopeNamespaceRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteScopeNamespace(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_scope_rbac_role_binding(
        self,
    ) -> Callable[
        [service.DeleteScopeRBACRoleBindingRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteScopeRBACRoleBinding(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def generate_connect_manifest(
        self,
    ) -> Callable[
        [service.GenerateConnectManifestRequest],
        service.GenerateConnectManifestResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GenerateConnectManifest(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def generate_membership_rbac_role_binding_yaml(
        self,
    ) -> Callable[
        [service.GenerateMembershipRBACRoleBindingYAMLRequest],
        service.GenerateMembershipRBACRoleBindingYAMLResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GenerateMembershipRBACRoleBindingYAML(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_feature(self) -> Callable[[service.GetFeatureRequest], feature.Feature]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetFeature(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_fleet(self) -> Callable[[service.GetFleetRequest], fleet.Fleet]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetFleet(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_membership(
        self,
    ) -> Callable[[service.GetMembershipRequest], membership.Membership]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetMembership(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_membership_binding(
        self,
    ) -> Callable[[service.GetMembershipBindingRequest], fleet.MembershipBinding]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetMembershipBinding(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_membership_rbac_role_binding(
        self,
    ) -> Callable[[service.GetMembershipRBACRoleBindingRequest], fleet.RBACRoleBinding]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetMembershipRBACRoleBinding(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_scope(self) -> Callable[[service.GetScopeRequest], fleet.Scope]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetScope(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_scope_namespace(
        self,
    ) -> Callable[[service.GetScopeNamespaceRequest], fleet.Namespace]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetScopeNamespace(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_scope_rbac_role_binding(
        self,
    ) -> Callable[[service.GetScopeRBACRoleBindingRequest], fleet.RBACRoleBinding]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetScopeRBACRoleBinding(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_bound_memberships(
        self,
    ) -> Callable[
        [service.ListBoundMembershipsRequest], service.ListBoundMembershipsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListBoundMemberships(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_features(
        self,
    ) -> Callable[[service.ListFeaturesRequest], service.ListFeaturesResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListFeatures(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_fleets(
        self,
    ) -> Callable[[service.ListFleetsRequest], service.ListFleetsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListFleets(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_membership_bindings(
        self,
    ) -> Callable[
        [service.ListMembershipBindingsRequest], service.ListMembershipBindingsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListMembershipBindings(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_membership_rbac_role_bindings(
        self,
    ) -> Callable[
        [service.ListMembershipRBACRoleBindingsRequest],
        service.ListMembershipRBACRoleBindingsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListMembershipRBACRoleBindings(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_memberships(
        self,
    ) -> Callable[[service.ListMembershipsRequest], service.ListMembershipsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListMemberships(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_permitted_scopes(
        self,
    ) -> Callable[
        [service.ListPermittedScopesRequest], service.ListPermittedScopesResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListPermittedScopes(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_scope_namespaces(
        self,
    ) -> Callable[
        [service.ListScopeNamespacesRequest], service.ListScopeNamespacesResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListScopeNamespaces(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_scope_rbac_role_bindings(
        self,
    ) -> Callable[
        [service.ListScopeRBACRoleBindingsRequest],
        service.ListScopeRBACRoleBindingsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListScopeRBACRoleBindings(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_scopes(
        self,
    ) -> Callable[[service.ListScopesRequest], service.ListScopesResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListScopes(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_feature(
        self,
    ) -> Callable[[service.UpdateFeatureRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateFeature(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_fleet(
        self,
    ) -> Callable[[service.UpdateFleetRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateFleet(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_membership(
        self,
    ) -> Callable[[service.UpdateMembershipRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateMembership(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_membership_binding(
        self,
    ) -> Callable[[service.UpdateMembershipBindingRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateMembershipBinding(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_membership_rbac_role_binding(
        self,
    ) -> Callable[
        [service.UpdateMembershipRBACRoleBindingRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateMembershipRBACRoleBinding(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_scope(
        self,
    ) -> Callable[[service.UpdateScopeRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateScope(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_scope_namespace(
        self,
    ) -> Callable[[service.UpdateScopeNamespaceRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateScopeNamespace(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_scope_rbac_role_binding(
        self,
    ) -> Callable[
        [service.UpdateScopeRBACRoleBindingRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateScopeRBACRoleBinding(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("GkeHubRestTransport",)
