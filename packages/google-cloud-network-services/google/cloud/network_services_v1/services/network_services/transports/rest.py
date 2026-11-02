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

from google.cloud.network_services_v1._compat import transcode_request
from google.cloud.network_services_v1.types import (
    agent_gateway,
    endpoint_policy,
    extensibility,
    gateway,
    grpc_route,
    http_route,
    mesh,
    route_view,
    service_binding,
    service_lb_policy,
    tcp_route,
    tls_route,
)
from google.cloud.network_services_v1.types import agent_gateway as gcn_agent_gateway
from google.cloud.network_services_v1.types import (
    endpoint_policy as gcn_endpoint_policy,
)
from google.cloud.network_services_v1.types import gateway as gcn_gateway
from google.cloud.network_services_v1.types import grpc_route as gcn_grpc_route
from google.cloud.network_services_v1.types import http_route as gcn_http_route
from google.cloud.network_services_v1.types import mesh as gcn_mesh
from google.cloud.network_services_v1.types import (
    service_binding as gcn_service_binding,
)
from google.cloud.network_services_v1.types import (
    service_lb_policy as gcn_service_lb_policy,
)
from google.cloud.network_services_v1.types import tcp_route as gcn_tcp_route
from google.cloud.network_services_v1.types import tls_route as gcn_tls_route

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseNetworkServicesRestTransport

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


class NetworkServicesRestInterceptor:
    """Interceptor for NetworkServices.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the NetworkServicesRestTransport.

    .. code-block:: python
        class MyCustomNetworkServicesInterceptor(NetworkServicesRestInterceptor):
            def pre_create_agent_gateway(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_agent_gateway(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_endpoint_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_endpoint_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_gateway(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_gateway(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_grpc_route(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_grpc_route(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_http_route(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_http_route(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_mesh(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_mesh(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_service_binding(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_service_binding(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_service_lb_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_service_lb_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_tcp_route(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_tcp_route(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_tls_route(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_tls_route(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_wasm_plugin(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_wasm_plugin(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_wasm_plugin_version(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_wasm_plugin_version(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_agent_gateway(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_agent_gateway(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_endpoint_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_endpoint_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_gateway(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_gateway(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_grpc_route(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_grpc_route(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_http_route(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_http_route(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_mesh(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_mesh(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_service_binding(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_service_binding(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_service_lb_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_service_lb_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_tcp_route(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_tcp_route(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_tls_route(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_tls_route(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_wasm_plugin(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_wasm_plugin(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_wasm_plugin_version(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_wasm_plugin_version(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_agent_gateway(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_agent_gateway(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_endpoint_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_endpoint_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_gateway(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_gateway(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_gateway_route_view(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_gateway_route_view(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_grpc_route(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_grpc_route(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_http_route(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_http_route(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_mesh(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_mesh(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_mesh_route_view(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_mesh_route_view(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_service_binding(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_service_binding(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_service_lb_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_service_lb_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_tcp_route(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_tcp_route(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_tls_route(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_tls_route(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_wasm_plugin(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_wasm_plugin(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_wasm_plugin_version(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_wasm_plugin_version(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_agent_gateways(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_agent_gateways(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_endpoint_policies(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_endpoint_policies(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_gateway_route_views(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_gateway_route_views(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_gateways(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_gateways(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_grpc_routes(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_grpc_routes(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_http_routes(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_http_routes(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_meshes(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_meshes(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_mesh_route_views(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_mesh_route_views(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_service_bindings(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_service_bindings(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_service_lb_policies(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_service_lb_policies(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_tcp_routes(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_tcp_routes(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_tls_routes(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_tls_routes(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_wasm_plugins(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_wasm_plugins(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_wasm_plugin_versions(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_wasm_plugin_versions(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_agent_gateway(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_agent_gateway(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_endpoint_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_endpoint_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_gateway(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_gateway(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_grpc_route(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_grpc_route(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_http_route(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_http_route(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_mesh(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_mesh(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_service_binding(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_service_binding(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_service_lb_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_service_lb_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_tcp_route(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_tcp_route(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_tls_route(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_tls_route(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_wasm_plugin(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_wasm_plugin(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = NetworkServicesRestTransport(interceptor=MyCustomNetworkServicesInterceptor())
        client = NetworkServicesClient(transport=transport)


    """

    def pre_create_agent_gateway(
        self,
        request: gcn_agent_gateway.CreateAgentGatewayRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcn_agent_gateway.CreateAgentGatewayRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_agent_gateway

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_create_agent_gateway(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_agent_gateway

        DEPRECATED. Please use the `post_create_agent_gateway_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkServices server but before
        it is returned to user code. This `post_create_agent_gateway` interceptor runs
        before the `post_create_agent_gateway_with_metadata` interceptor.
        """
        return response

    def post_create_agent_gateway_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_agent_gateway

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkServices server but before it is returned to user code.

        We recommend only using this `post_create_agent_gateway_with_metadata`
        interceptor in new development instead of the `post_create_agent_gateway` interceptor.
        When both interceptors are used, this `post_create_agent_gateway_with_metadata` interceptor runs after the
        `post_create_agent_gateway` interceptor. The (possibly modified) response returned by
        `post_create_agent_gateway` will be passed to
        `post_create_agent_gateway_with_metadata`.
        """
        return response, metadata

    def pre_create_endpoint_policy(
        self,
        request: gcn_endpoint_policy.CreateEndpointPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcn_endpoint_policy.CreateEndpointPolicyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_endpoint_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_create_endpoint_policy(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_endpoint_policy

        DEPRECATED. Please use the `post_create_endpoint_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkServices server but before
        it is returned to user code. This `post_create_endpoint_policy` interceptor runs
        before the `post_create_endpoint_policy_with_metadata` interceptor.
        """
        return response

    def post_create_endpoint_policy_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_endpoint_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkServices server but before it is returned to user code.

        We recommend only using this `post_create_endpoint_policy_with_metadata`
        interceptor in new development instead of the `post_create_endpoint_policy` interceptor.
        When both interceptors are used, this `post_create_endpoint_policy_with_metadata` interceptor runs after the
        `post_create_endpoint_policy` interceptor. The (possibly modified) response returned by
        `post_create_endpoint_policy` will be passed to
        `post_create_endpoint_policy_with_metadata`.
        """
        return response, metadata

    def pre_create_gateway(
        self,
        request: gcn_gateway.CreateGatewayRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcn_gateway.CreateGatewayRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_gateway

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_create_gateway(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_gateway

        DEPRECATED. Please use the `post_create_gateway_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkServices server but before
        it is returned to user code. This `post_create_gateway` interceptor runs
        before the `post_create_gateway_with_metadata` interceptor.
        """
        return response

    def post_create_gateway_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_gateway

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkServices server but before it is returned to user code.

        We recommend only using this `post_create_gateway_with_metadata`
        interceptor in new development instead of the `post_create_gateway` interceptor.
        When both interceptors are used, this `post_create_gateway_with_metadata` interceptor runs after the
        `post_create_gateway` interceptor. The (possibly modified) response returned by
        `post_create_gateway` will be passed to
        `post_create_gateway_with_metadata`.
        """
        return response, metadata

    def pre_create_grpc_route(
        self,
        request: gcn_grpc_route.CreateGrpcRouteRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcn_grpc_route.CreateGrpcRouteRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_grpc_route

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_create_grpc_route(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_grpc_route

        DEPRECATED. Please use the `post_create_grpc_route_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkServices server but before
        it is returned to user code. This `post_create_grpc_route` interceptor runs
        before the `post_create_grpc_route_with_metadata` interceptor.
        """
        return response

    def post_create_grpc_route_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_grpc_route

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkServices server but before it is returned to user code.

        We recommend only using this `post_create_grpc_route_with_metadata`
        interceptor in new development instead of the `post_create_grpc_route` interceptor.
        When both interceptors are used, this `post_create_grpc_route_with_metadata` interceptor runs after the
        `post_create_grpc_route` interceptor. The (possibly modified) response returned by
        `post_create_grpc_route` will be passed to
        `post_create_grpc_route_with_metadata`.
        """
        return response, metadata

    def pre_create_http_route(
        self,
        request: gcn_http_route.CreateHttpRouteRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcn_http_route.CreateHttpRouteRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_http_route

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_create_http_route(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_http_route

        DEPRECATED. Please use the `post_create_http_route_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkServices server but before
        it is returned to user code. This `post_create_http_route` interceptor runs
        before the `post_create_http_route_with_metadata` interceptor.
        """
        return response

    def post_create_http_route_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_http_route

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkServices server but before it is returned to user code.

        We recommend only using this `post_create_http_route_with_metadata`
        interceptor in new development instead of the `post_create_http_route` interceptor.
        When both interceptors are used, this `post_create_http_route_with_metadata` interceptor runs after the
        `post_create_http_route` interceptor. The (possibly modified) response returned by
        `post_create_http_route` will be passed to
        `post_create_http_route_with_metadata`.
        """
        return response, metadata

    def pre_create_mesh(
        self,
        request: gcn_mesh.CreateMeshRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gcn_mesh.CreateMeshRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_mesh

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_create_mesh(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_mesh

        DEPRECATED. Please use the `post_create_mesh_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkServices server but before
        it is returned to user code. This `post_create_mesh` interceptor runs
        before the `post_create_mesh_with_metadata` interceptor.
        """
        return response

    def post_create_mesh_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_mesh

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkServices server but before it is returned to user code.

        We recommend only using this `post_create_mesh_with_metadata`
        interceptor in new development instead of the `post_create_mesh` interceptor.
        When both interceptors are used, this `post_create_mesh_with_metadata` interceptor runs after the
        `post_create_mesh` interceptor. The (possibly modified) response returned by
        `post_create_mesh` will be passed to
        `post_create_mesh_with_metadata`.
        """
        return response, metadata

    def pre_create_service_binding(
        self,
        request: gcn_service_binding.CreateServiceBindingRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcn_service_binding.CreateServiceBindingRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_service_binding

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_create_service_binding(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_service_binding

        DEPRECATED. Please use the `post_create_service_binding_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkServices server but before
        it is returned to user code. This `post_create_service_binding` interceptor runs
        before the `post_create_service_binding_with_metadata` interceptor.
        """
        return response

    def post_create_service_binding_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_service_binding

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkServices server but before it is returned to user code.

        We recommend only using this `post_create_service_binding_with_metadata`
        interceptor in new development instead of the `post_create_service_binding` interceptor.
        When both interceptors are used, this `post_create_service_binding_with_metadata` interceptor runs after the
        `post_create_service_binding` interceptor. The (possibly modified) response returned by
        `post_create_service_binding` will be passed to
        `post_create_service_binding_with_metadata`.
        """
        return response, metadata

    def pre_create_service_lb_policy(
        self,
        request: gcn_service_lb_policy.CreateServiceLbPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcn_service_lb_policy.CreateServiceLbPolicyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_service_lb_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_create_service_lb_policy(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_service_lb_policy

        DEPRECATED. Please use the `post_create_service_lb_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkServices server but before
        it is returned to user code. This `post_create_service_lb_policy` interceptor runs
        before the `post_create_service_lb_policy_with_metadata` interceptor.
        """
        return response

    def post_create_service_lb_policy_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_service_lb_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkServices server but before it is returned to user code.

        We recommend only using this `post_create_service_lb_policy_with_metadata`
        interceptor in new development instead of the `post_create_service_lb_policy` interceptor.
        When both interceptors are used, this `post_create_service_lb_policy_with_metadata` interceptor runs after the
        `post_create_service_lb_policy` interceptor. The (possibly modified) response returned by
        `post_create_service_lb_policy` will be passed to
        `post_create_service_lb_policy_with_metadata`.
        """
        return response, metadata

    def pre_create_tcp_route(
        self,
        request: gcn_tcp_route.CreateTcpRouteRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcn_tcp_route.CreateTcpRouteRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_tcp_route

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_create_tcp_route(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_tcp_route

        DEPRECATED. Please use the `post_create_tcp_route_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkServices server but before
        it is returned to user code. This `post_create_tcp_route` interceptor runs
        before the `post_create_tcp_route_with_metadata` interceptor.
        """
        return response

    def post_create_tcp_route_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_tcp_route

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkServices server but before it is returned to user code.

        We recommend only using this `post_create_tcp_route_with_metadata`
        interceptor in new development instead of the `post_create_tcp_route` interceptor.
        When both interceptors are used, this `post_create_tcp_route_with_metadata` interceptor runs after the
        `post_create_tcp_route` interceptor. The (possibly modified) response returned by
        `post_create_tcp_route` will be passed to
        `post_create_tcp_route_with_metadata`.
        """
        return response, metadata

    def pre_create_tls_route(
        self,
        request: gcn_tls_route.CreateTlsRouteRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcn_tls_route.CreateTlsRouteRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_tls_route

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_create_tls_route(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_tls_route

        DEPRECATED. Please use the `post_create_tls_route_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkServices server but before
        it is returned to user code. This `post_create_tls_route` interceptor runs
        before the `post_create_tls_route_with_metadata` interceptor.
        """
        return response

    def post_create_tls_route_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_tls_route

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkServices server but before it is returned to user code.

        We recommend only using this `post_create_tls_route_with_metadata`
        interceptor in new development instead of the `post_create_tls_route` interceptor.
        When both interceptors are used, this `post_create_tls_route_with_metadata` interceptor runs after the
        `post_create_tls_route` interceptor. The (possibly modified) response returned by
        `post_create_tls_route` will be passed to
        `post_create_tls_route_with_metadata`.
        """
        return response, metadata

    def pre_create_wasm_plugin(
        self,
        request: extensibility.CreateWasmPluginRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        extensibility.CreateWasmPluginRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_wasm_plugin

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_create_wasm_plugin(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_wasm_plugin

        DEPRECATED. Please use the `post_create_wasm_plugin_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkServices server but before
        it is returned to user code. This `post_create_wasm_plugin` interceptor runs
        before the `post_create_wasm_plugin_with_metadata` interceptor.
        """
        return response

    def post_create_wasm_plugin_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_wasm_plugin

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkServices server but before it is returned to user code.

        We recommend only using this `post_create_wasm_plugin_with_metadata`
        interceptor in new development instead of the `post_create_wasm_plugin` interceptor.
        When both interceptors are used, this `post_create_wasm_plugin_with_metadata` interceptor runs after the
        `post_create_wasm_plugin` interceptor. The (possibly modified) response returned by
        `post_create_wasm_plugin` will be passed to
        `post_create_wasm_plugin_with_metadata`.
        """
        return response, metadata

    def pre_create_wasm_plugin_version(
        self,
        request: extensibility.CreateWasmPluginVersionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        extensibility.CreateWasmPluginVersionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_wasm_plugin_version

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_create_wasm_plugin_version(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_wasm_plugin_version

        DEPRECATED. Please use the `post_create_wasm_plugin_version_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkServices server but before
        it is returned to user code. This `post_create_wasm_plugin_version` interceptor runs
        before the `post_create_wasm_plugin_version_with_metadata` interceptor.
        """
        return response

    def post_create_wasm_plugin_version_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_wasm_plugin_version

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkServices server but before it is returned to user code.

        We recommend only using this `post_create_wasm_plugin_version_with_metadata`
        interceptor in new development instead of the `post_create_wasm_plugin_version` interceptor.
        When both interceptors are used, this `post_create_wasm_plugin_version_with_metadata` interceptor runs after the
        `post_create_wasm_plugin_version` interceptor. The (possibly modified) response returned by
        `post_create_wasm_plugin_version` will be passed to
        `post_create_wasm_plugin_version_with_metadata`.
        """
        return response, metadata

    def pre_delete_agent_gateway(
        self,
        request: agent_gateway.DeleteAgentGatewayRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        agent_gateway.DeleteAgentGatewayRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_agent_gateway

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_delete_agent_gateway(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_agent_gateway

        DEPRECATED. Please use the `post_delete_agent_gateway_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkServices server but before
        it is returned to user code. This `post_delete_agent_gateway` interceptor runs
        before the `post_delete_agent_gateway_with_metadata` interceptor.
        """
        return response

    def post_delete_agent_gateway_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_agent_gateway

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkServices server but before it is returned to user code.

        We recommend only using this `post_delete_agent_gateway_with_metadata`
        interceptor in new development instead of the `post_delete_agent_gateway` interceptor.
        When both interceptors are used, this `post_delete_agent_gateway_with_metadata` interceptor runs after the
        `post_delete_agent_gateway` interceptor. The (possibly modified) response returned by
        `post_delete_agent_gateway` will be passed to
        `post_delete_agent_gateway_with_metadata`.
        """
        return response, metadata

    def pre_delete_endpoint_policy(
        self,
        request: endpoint_policy.DeleteEndpointPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        endpoint_policy.DeleteEndpointPolicyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_endpoint_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_delete_endpoint_policy(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_endpoint_policy

        DEPRECATED. Please use the `post_delete_endpoint_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkServices server but before
        it is returned to user code. This `post_delete_endpoint_policy` interceptor runs
        before the `post_delete_endpoint_policy_with_metadata` interceptor.
        """
        return response

    def post_delete_endpoint_policy_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_endpoint_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkServices server but before it is returned to user code.

        We recommend only using this `post_delete_endpoint_policy_with_metadata`
        interceptor in new development instead of the `post_delete_endpoint_policy` interceptor.
        When both interceptors are used, this `post_delete_endpoint_policy_with_metadata` interceptor runs after the
        `post_delete_endpoint_policy` interceptor. The (possibly modified) response returned by
        `post_delete_endpoint_policy` will be passed to
        `post_delete_endpoint_policy_with_metadata`.
        """
        return response, metadata

    def pre_delete_gateway(
        self,
        request: gateway.DeleteGatewayRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gateway.DeleteGatewayRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_gateway

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_delete_gateway(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_gateway

        DEPRECATED. Please use the `post_delete_gateway_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkServices server but before
        it is returned to user code. This `post_delete_gateway` interceptor runs
        before the `post_delete_gateway_with_metadata` interceptor.
        """
        return response

    def post_delete_gateway_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_gateway

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkServices server but before it is returned to user code.

        We recommend only using this `post_delete_gateway_with_metadata`
        interceptor in new development instead of the `post_delete_gateway` interceptor.
        When both interceptors are used, this `post_delete_gateway_with_metadata` interceptor runs after the
        `post_delete_gateway` interceptor. The (possibly modified) response returned by
        `post_delete_gateway` will be passed to
        `post_delete_gateway_with_metadata`.
        """
        return response, metadata

    def pre_delete_grpc_route(
        self,
        request: grpc_route.DeleteGrpcRouteRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        grpc_route.DeleteGrpcRouteRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_grpc_route

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_delete_grpc_route(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_grpc_route

        DEPRECATED. Please use the `post_delete_grpc_route_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkServices server but before
        it is returned to user code. This `post_delete_grpc_route` interceptor runs
        before the `post_delete_grpc_route_with_metadata` interceptor.
        """
        return response

    def post_delete_grpc_route_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_grpc_route

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkServices server but before it is returned to user code.

        We recommend only using this `post_delete_grpc_route_with_metadata`
        interceptor in new development instead of the `post_delete_grpc_route` interceptor.
        When both interceptors are used, this `post_delete_grpc_route_with_metadata` interceptor runs after the
        `post_delete_grpc_route` interceptor. The (possibly modified) response returned by
        `post_delete_grpc_route` will be passed to
        `post_delete_grpc_route_with_metadata`.
        """
        return response, metadata

    def pre_delete_http_route(
        self,
        request: http_route.DeleteHttpRouteRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        http_route.DeleteHttpRouteRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_http_route

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_delete_http_route(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_http_route

        DEPRECATED. Please use the `post_delete_http_route_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkServices server but before
        it is returned to user code. This `post_delete_http_route` interceptor runs
        before the `post_delete_http_route_with_metadata` interceptor.
        """
        return response

    def post_delete_http_route_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_http_route

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkServices server but before it is returned to user code.

        We recommend only using this `post_delete_http_route_with_metadata`
        interceptor in new development instead of the `post_delete_http_route` interceptor.
        When both interceptors are used, this `post_delete_http_route_with_metadata` interceptor runs after the
        `post_delete_http_route` interceptor. The (possibly modified) response returned by
        `post_delete_http_route` will be passed to
        `post_delete_http_route_with_metadata`.
        """
        return response, metadata

    def pre_delete_mesh(
        self,
        request: mesh.DeleteMeshRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[mesh.DeleteMeshRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_mesh

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_delete_mesh(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_mesh

        DEPRECATED. Please use the `post_delete_mesh_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkServices server but before
        it is returned to user code. This `post_delete_mesh` interceptor runs
        before the `post_delete_mesh_with_metadata` interceptor.
        """
        return response

    def post_delete_mesh_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_mesh

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkServices server but before it is returned to user code.

        We recommend only using this `post_delete_mesh_with_metadata`
        interceptor in new development instead of the `post_delete_mesh` interceptor.
        When both interceptors are used, this `post_delete_mesh_with_metadata` interceptor runs after the
        `post_delete_mesh` interceptor. The (possibly modified) response returned by
        `post_delete_mesh` will be passed to
        `post_delete_mesh_with_metadata`.
        """
        return response, metadata

    def pre_delete_service_binding(
        self,
        request: service_binding.DeleteServiceBindingRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service_binding.DeleteServiceBindingRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_service_binding

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_delete_service_binding(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_service_binding

        DEPRECATED. Please use the `post_delete_service_binding_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkServices server but before
        it is returned to user code. This `post_delete_service_binding` interceptor runs
        before the `post_delete_service_binding_with_metadata` interceptor.
        """
        return response

    def post_delete_service_binding_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_service_binding

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkServices server but before it is returned to user code.

        We recommend only using this `post_delete_service_binding_with_metadata`
        interceptor in new development instead of the `post_delete_service_binding` interceptor.
        When both interceptors are used, this `post_delete_service_binding_with_metadata` interceptor runs after the
        `post_delete_service_binding` interceptor. The (possibly modified) response returned by
        `post_delete_service_binding` will be passed to
        `post_delete_service_binding_with_metadata`.
        """
        return response, metadata

    def pre_delete_service_lb_policy(
        self,
        request: service_lb_policy.DeleteServiceLbPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service_lb_policy.DeleteServiceLbPolicyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_service_lb_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_delete_service_lb_policy(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_service_lb_policy

        DEPRECATED. Please use the `post_delete_service_lb_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkServices server but before
        it is returned to user code. This `post_delete_service_lb_policy` interceptor runs
        before the `post_delete_service_lb_policy_with_metadata` interceptor.
        """
        return response

    def post_delete_service_lb_policy_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_service_lb_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkServices server but before it is returned to user code.

        We recommend only using this `post_delete_service_lb_policy_with_metadata`
        interceptor in new development instead of the `post_delete_service_lb_policy` interceptor.
        When both interceptors are used, this `post_delete_service_lb_policy_with_metadata` interceptor runs after the
        `post_delete_service_lb_policy` interceptor. The (possibly modified) response returned by
        `post_delete_service_lb_policy` will be passed to
        `post_delete_service_lb_policy_with_metadata`.
        """
        return response, metadata

    def pre_delete_tcp_route(
        self,
        request: tcp_route.DeleteTcpRouteRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        tcp_route.DeleteTcpRouteRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_tcp_route

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_delete_tcp_route(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_tcp_route

        DEPRECATED. Please use the `post_delete_tcp_route_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkServices server but before
        it is returned to user code. This `post_delete_tcp_route` interceptor runs
        before the `post_delete_tcp_route_with_metadata` interceptor.
        """
        return response

    def post_delete_tcp_route_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_tcp_route

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkServices server but before it is returned to user code.

        We recommend only using this `post_delete_tcp_route_with_metadata`
        interceptor in new development instead of the `post_delete_tcp_route` interceptor.
        When both interceptors are used, this `post_delete_tcp_route_with_metadata` interceptor runs after the
        `post_delete_tcp_route` interceptor. The (possibly modified) response returned by
        `post_delete_tcp_route` will be passed to
        `post_delete_tcp_route_with_metadata`.
        """
        return response, metadata

    def pre_delete_tls_route(
        self,
        request: tls_route.DeleteTlsRouteRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        tls_route.DeleteTlsRouteRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_tls_route

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_delete_tls_route(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_tls_route

        DEPRECATED. Please use the `post_delete_tls_route_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkServices server but before
        it is returned to user code. This `post_delete_tls_route` interceptor runs
        before the `post_delete_tls_route_with_metadata` interceptor.
        """
        return response

    def post_delete_tls_route_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_tls_route

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkServices server but before it is returned to user code.

        We recommend only using this `post_delete_tls_route_with_metadata`
        interceptor in new development instead of the `post_delete_tls_route` interceptor.
        When both interceptors are used, this `post_delete_tls_route_with_metadata` interceptor runs after the
        `post_delete_tls_route` interceptor. The (possibly modified) response returned by
        `post_delete_tls_route` will be passed to
        `post_delete_tls_route_with_metadata`.
        """
        return response, metadata

    def pre_delete_wasm_plugin(
        self,
        request: extensibility.DeleteWasmPluginRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        extensibility.DeleteWasmPluginRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_wasm_plugin

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_delete_wasm_plugin(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_wasm_plugin

        DEPRECATED. Please use the `post_delete_wasm_plugin_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkServices server but before
        it is returned to user code. This `post_delete_wasm_plugin` interceptor runs
        before the `post_delete_wasm_plugin_with_metadata` interceptor.
        """
        return response

    def post_delete_wasm_plugin_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_wasm_plugin

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkServices server but before it is returned to user code.

        We recommend only using this `post_delete_wasm_plugin_with_metadata`
        interceptor in new development instead of the `post_delete_wasm_plugin` interceptor.
        When both interceptors are used, this `post_delete_wasm_plugin_with_metadata` interceptor runs after the
        `post_delete_wasm_plugin` interceptor. The (possibly modified) response returned by
        `post_delete_wasm_plugin` will be passed to
        `post_delete_wasm_plugin_with_metadata`.
        """
        return response, metadata

    def pre_delete_wasm_plugin_version(
        self,
        request: extensibility.DeleteWasmPluginVersionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        extensibility.DeleteWasmPluginVersionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_wasm_plugin_version

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_delete_wasm_plugin_version(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_wasm_plugin_version

        DEPRECATED. Please use the `post_delete_wasm_plugin_version_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkServices server but before
        it is returned to user code. This `post_delete_wasm_plugin_version` interceptor runs
        before the `post_delete_wasm_plugin_version_with_metadata` interceptor.
        """
        return response

    def post_delete_wasm_plugin_version_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_wasm_plugin_version

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkServices server but before it is returned to user code.

        We recommend only using this `post_delete_wasm_plugin_version_with_metadata`
        interceptor in new development instead of the `post_delete_wasm_plugin_version` interceptor.
        When both interceptors are used, this `post_delete_wasm_plugin_version_with_metadata` interceptor runs after the
        `post_delete_wasm_plugin_version` interceptor. The (possibly modified) response returned by
        `post_delete_wasm_plugin_version` will be passed to
        `post_delete_wasm_plugin_version_with_metadata`.
        """
        return response, metadata

    def pre_get_agent_gateway(
        self,
        request: agent_gateway.GetAgentGatewayRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        agent_gateway.GetAgentGatewayRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_agent_gateway

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_get_agent_gateway(
        self, response: agent_gateway.AgentGateway
    ) -> agent_gateway.AgentGateway:
        """Post-rpc interceptor for get_agent_gateway

        DEPRECATED. Please use the `post_get_agent_gateway_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkServices server but before
        it is returned to user code. This `post_get_agent_gateway` interceptor runs
        before the `post_get_agent_gateway_with_metadata` interceptor.
        """
        return response

    def post_get_agent_gateway_with_metadata(
        self,
        response: agent_gateway.AgentGateway,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[agent_gateway.AgentGateway, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_agent_gateway

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkServices server but before it is returned to user code.

        We recommend only using this `post_get_agent_gateway_with_metadata`
        interceptor in new development instead of the `post_get_agent_gateway` interceptor.
        When both interceptors are used, this `post_get_agent_gateway_with_metadata` interceptor runs after the
        `post_get_agent_gateway` interceptor. The (possibly modified) response returned by
        `post_get_agent_gateway` will be passed to
        `post_get_agent_gateway_with_metadata`.
        """
        return response, metadata

    def pre_get_endpoint_policy(
        self,
        request: endpoint_policy.GetEndpointPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        endpoint_policy.GetEndpointPolicyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_endpoint_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_get_endpoint_policy(
        self, response: endpoint_policy.EndpointPolicy
    ) -> endpoint_policy.EndpointPolicy:
        """Post-rpc interceptor for get_endpoint_policy

        DEPRECATED. Please use the `post_get_endpoint_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkServices server but before
        it is returned to user code. This `post_get_endpoint_policy` interceptor runs
        before the `post_get_endpoint_policy_with_metadata` interceptor.
        """
        return response

    def post_get_endpoint_policy_with_metadata(
        self,
        response: endpoint_policy.EndpointPolicy,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[endpoint_policy.EndpointPolicy, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_endpoint_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkServices server but before it is returned to user code.

        We recommend only using this `post_get_endpoint_policy_with_metadata`
        interceptor in new development instead of the `post_get_endpoint_policy` interceptor.
        When both interceptors are used, this `post_get_endpoint_policy_with_metadata` interceptor runs after the
        `post_get_endpoint_policy` interceptor. The (possibly modified) response returned by
        `post_get_endpoint_policy` will be passed to
        `post_get_endpoint_policy_with_metadata`.
        """
        return response, metadata

    def pre_get_gateway(
        self,
        request: gateway.GetGatewayRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gateway.GetGatewayRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_gateway

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_get_gateway(self, response: gateway.Gateway) -> gateway.Gateway:
        """Post-rpc interceptor for get_gateway

        DEPRECATED. Please use the `post_get_gateway_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkServices server but before
        it is returned to user code. This `post_get_gateway` interceptor runs
        before the `post_get_gateway_with_metadata` interceptor.
        """
        return response

    def post_get_gateway_with_metadata(
        self,
        response: gateway.Gateway,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gateway.Gateway, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_gateway

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkServices server but before it is returned to user code.

        We recommend only using this `post_get_gateway_with_metadata`
        interceptor in new development instead of the `post_get_gateway` interceptor.
        When both interceptors are used, this `post_get_gateway_with_metadata` interceptor runs after the
        `post_get_gateway` interceptor. The (possibly modified) response returned by
        `post_get_gateway` will be passed to
        `post_get_gateway_with_metadata`.
        """
        return response, metadata

    def pre_get_gateway_route_view(
        self,
        request: route_view.GetGatewayRouteViewRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        route_view.GetGatewayRouteViewRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_gateway_route_view

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_get_gateway_route_view(
        self, response: route_view.GatewayRouteView
    ) -> route_view.GatewayRouteView:
        """Post-rpc interceptor for get_gateway_route_view

        DEPRECATED. Please use the `post_get_gateway_route_view_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkServices server but before
        it is returned to user code. This `post_get_gateway_route_view` interceptor runs
        before the `post_get_gateway_route_view_with_metadata` interceptor.
        """
        return response

    def post_get_gateway_route_view_with_metadata(
        self,
        response: route_view.GatewayRouteView,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[route_view.GatewayRouteView, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_gateway_route_view

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkServices server but before it is returned to user code.

        We recommend only using this `post_get_gateway_route_view_with_metadata`
        interceptor in new development instead of the `post_get_gateway_route_view` interceptor.
        When both interceptors are used, this `post_get_gateway_route_view_with_metadata` interceptor runs after the
        `post_get_gateway_route_view` interceptor. The (possibly modified) response returned by
        `post_get_gateway_route_view` will be passed to
        `post_get_gateway_route_view_with_metadata`.
        """
        return response, metadata

    def pre_get_grpc_route(
        self,
        request: grpc_route.GetGrpcRouteRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[grpc_route.GetGrpcRouteRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_grpc_route

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_get_grpc_route(
        self, response: grpc_route.GrpcRoute
    ) -> grpc_route.GrpcRoute:
        """Post-rpc interceptor for get_grpc_route

        DEPRECATED. Please use the `post_get_grpc_route_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkServices server but before
        it is returned to user code. This `post_get_grpc_route` interceptor runs
        before the `post_get_grpc_route_with_metadata` interceptor.
        """
        return response

    def post_get_grpc_route_with_metadata(
        self,
        response: grpc_route.GrpcRoute,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[grpc_route.GrpcRoute, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_grpc_route

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkServices server but before it is returned to user code.

        We recommend only using this `post_get_grpc_route_with_metadata`
        interceptor in new development instead of the `post_get_grpc_route` interceptor.
        When both interceptors are used, this `post_get_grpc_route_with_metadata` interceptor runs after the
        `post_get_grpc_route` interceptor. The (possibly modified) response returned by
        `post_get_grpc_route` will be passed to
        `post_get_grpc_route_with_metadata`.
        """
        return response, metadata

    def pre_get_http_route(
        self,
        request: http_route.GetHttpRouteRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[http_route.GetHttpRouteRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_http_route

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_get_http_route(
        self, response: http_route.HttpRoute
    ) -> http_route.HttpRoute:
        """Post-rpc interceptor for get_http_route

        DEPRECATED. Please use the `post_get_http_route_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkServices server but before
        it is returned to user code. This `post_get_http_route` interceptor runs
        before the `post_get_http_route_with_metadata` interceptor.
        """
        return response

    def post_get_http_route_with_metadata(
        self,
        response: http_route.HttpRoute,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[http_route.HttpRoute, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_http_route

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkServices server but before it is returned to user code.

        We recommend only using this `post_get_http_route_with_metadata`
        interceptor in new development instead of the `post_get_http_route` interceptor.
        When both interceptors are used, this `post_get_http_route_with_metadata` interceptor runs after the
        `post_get_http_route` interceptor. The (possibly modified) response returned by
        `post_get_http_route` will be passed to
        `post_get_http_route_with_metadata`.
        """
        return response, metadata

    def pre_get_mesh(
        self,
        request: mesh.GetMeshRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[mesh.GetMeshRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_mesh

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_get_mesh(self, response: mesh.Mesh) -> mesh.Mesh:
        """Post-rpc interceptor for get_mesh

        DEPRECATED. Please use the `post_get_mesh_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkServices server but before
        it is returned to user code. This `post_get_mesh` interceptor runs
        before the `post_get_mesh_with_metadata` interceptor.
        """
        return response

    def post_get_mesh_with_metadata(
        self, response: mesh.Mesh, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[mesh.Mesh, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_mesh

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkServices server but before it is returned to user code.

        We recommend only using this `post_get_mesh_with_metadata`
        interceptor in new development instead of the `post_get_mesh` interceptor.
        When both interceptors are used, this `post_get_mesh_with_metadata` interceptor runs after the
        `post_get_mesh` interceptor. The (possibly modified) response returned by
        `post_get_mesh` will be passed to
        `post_get_mesh_with_metadata`.
        """
        return response, metadata

    def pre_get_mesh_route_view(
        self,
        request: route_view.GetMeshRouteViewRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        route_view.GetMeshRouteViewRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_mesh_route_view

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_get_mesh_route_view(
        self, response: route_view.MeshRouteView
    ) -> route_view.MeshRouteView:
        """Post-rpc interceptor for get_mesh_route_view

        DEPRECATED. Please use the `post_get_mesh_route_view_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkServices server but before
        it is returned to user code. This `post_get_mesh_route_view` interceptor runs
        before the `post_get_mesh_route_view_with_metadata` interceptor.
        """
        return response

    def post_get_mesh_route_view_with_metadata(
        self,
        response: route_view.MeshRouteView,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[route_view.MeshRouteView, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_mesh_route_view

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkServices server but before it is returned to user code.

        We recommend only using this `post_get_mesh_route_view_with_metadata`
        interceptor in new development instead of the `post_get_mesh_route_view` interceptor.
        When both interceptors are used, this `post_get_mesh_route_view_with_metadata` interceptor runs after the
        `post_get_mesh_route_view` interceptor. The (possibly modified) response returned by
        `post_get_mesh_route_view` will be passed to
        `post_get_mesh_route_view_with_metadata`.
        """
        return response, metadata

    def pre_get_service_binding(
        self,
        request: service_binding.GetServiceBindingRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service_binding.GetServiceBindingRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_service_binding

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_get_service_binding(
        self, response: service_binding.ServiceBinding
    ) -> service_binding.ServiceBinding:
        """Post-rpc interceptor for get_service_binding

        DEPRECATED. Please use the `post_get_service_binding_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkServices server but before
        it is returned to user code. This `post_get_service_binding` interceptor runs
        before the `post_get_service_binding_with_metadata` interceptor.
        """
        return response

    def post_get_service_binding_with_metadata(
        self,
        response: service_binding.ServiceBinding,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service_binding.ServiceBinding, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_service_binding

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkServices server but before it is returned to user code.

        We recommend only using this `post_get_service_binding_with_metadata`
        interceptor in new development instead of the `post_get_service_binding` interceptor.
        When both interceptors are used, this `post_get_service_binding_with_metadata` interceptor runs after the
        `post_get_service_binding` interceptor. The (possibly modified) response returned by
        `post_get_service_binding` will be passed to
        `post_get_service_binding_with_metadata`.
        """
        return response, metadata

    def pre_get_service_lb_policy(
        self,
        request: service_lb_policy.GetServiceLbPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service_lb_policy.GetServiceLbPolicyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_service_lb_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_get_service_lb_policy(
        self, response: service_lb_policy.ServiceLbPolicy
    ) -> service_lb_policy.ServiceLbPolicy:
        """Post-rpc interceptor for get_service_lb_policy

        DEPRECATED. Please use the `post_get_service_lb_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkServices server but before
        it is returned to user code. This `post_get_service_lb_policy` interceptor runs
        before the `post_get_service_lb_policy_with_metadata` interceptor.
        """
        return response

    def post_get_service_lb_policy_with_metadata(
        self,
        response: service_lb_policy.ServiceLbPolicy,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service_lb_policy.ServiceLbPolicy, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_service_lb_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkServices server but before it is returned to user code.

        We recommend only using this `post_get_service_lb_policy_with_metadata`
        interceptor in new development instead of the `post_get_service_lb_policy` interceptor.
        When both interceptors are used, this `post_get_service_lb_policy_with_metadata` interceptor runs after the
        `post_get_service_lb_policy` interceptor. The (possibly modified) response returned by
        `post_get_service_lb_policy` will be passed to
        `post_get_service_lb_policy_with_metadata`.
        """
        return response, metadata

    def pre_get_tcp_route(
        self,
        request: tcp_route.GetTcpRouteRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[tcp_route.GetTcpRouteRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_tcp_route

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_get_tcp_route(self, response: tcp_route.TcpRoute) -> tcp_route.TcpRoute:
        """Post-rpc interceptor for get_tcp_route

        DEPRECATED. Please use the `post_get_tcp_route_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkServices server but before
        it is returned to user code. This `post_get_tcp_route` interceptor runs
        before the `post_get_tcp_route_with_metadata` interceptor.
        """
        return response

    def post_get_tcp_route_with_metadata(
        self,
        response: tcp_route.TcpRoute,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[tcp_route.TcpRoute, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_tcp_route

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkServices server but before it is returned to user code.

        We recommend only using this `post_get_tcp_route_with_metadata`
        interceptor in new development instead of the `post_get_tcp_route` interceptor.
        When both interceptors are used, this `post_get_tcp_route_with_metadata` interceptor runs after the
        `post_get_tcp_route` interceptor. The (possibly modified) response returned by
        `post_get_tcp_route` will be passed to
        `post_get_tcp_route_with_metadata`.
        """
        return response, metadata

    def pre_get_tls_route(
        self,
        request: tls_route.GetTlsRouteRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[tls_route.GetTlsRouteRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_tls_route

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_get_tls_route(self, response: tls_route.TlsRoute) -> tls_route.TlsRoute:
        """Post-rpc interceptor for get_tls_route

        DEPRECATED. Please use the `post_get_tls_route_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkServices server but before
        it is returned to user code. This `post_get_tls_route` interceptor runs
        before the `post_get_tls_route_with_metadata` interceptor.
        """
        return response

    def post_get_tls_route_with_metadata(
        self,
        response: tls_route.TlsRoute,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[tls_route.TlsRoute, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_tls_route

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkServices server but before it is returned to user code.

        We recommend only using this `post_get_tls_route_with_metadata`
        interceptor in new development instead of the `post_get_tls_route` interceptor.
        When both interceptors are used, this `post_get_tls_route_with_metadata` interceptor runs after the
        `post_get_tls_route` interceptor. The (possibly modified) response returned by
        `post_get_tls_route` will be passed to
        `post_get_tls_route_with_metadata`.
        """
        return response, metadata

    def pre_get_wasm_plugin(
        self,
        request: extensibility.GetWasmPluginRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        extensibility.GetWasmPluginRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_wasm_plugin

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_get_wasm_plugin(
        self, response: extensibility.WasmPlugin
    ) -> extensibility.WasmPlugin:
        """Post-rpc interceptor for get_wasm_plugin

        DEPRECATED. Please use the `post_get_wasm_plugin_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkServices server but before
        it is returned to user code. This `post_get_wasm_plugin` interceptor runs
        before the `post_get_wasm_plugin_with_metadata` interceptor.
        """
        return response

    def post_get_wasm_plugin_with_metadata(
        self,
        response: extensibility.WasmPlugin,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[extensibility.WasmPlugin, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_wasm_plugin

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkServices server but before it is returned to user code.

        We recommend only using this `post_get_wasm_plugin_with_metadata`
        interceptor in new development instead of the `post_get_wasm_plugin` interceptor.
        When both interceptors are used, this `post_get_wasm_plugin_with_metadata` interceptor runs after the
        `post_get_wasm_plugin` interceptor. The (possibly modified) response returned by
        `post_get_wasm_plugin` will be passed to
        `post_get_wasm_plugin_with_metadata`.
        """
        return response, metadata

    def pre_get_wasm_plugin_version(
        self,
        request: extensibility.GetWasmPluginVersionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        extensibility.GetWasmPluginVersionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_wasm_plugin_version

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_get_wasm_plugin_version(
        self, response: extensibility.WasmPluginVersion
    ) -> extensibility.WasmPluginVersion:
        """Post-rpc interceptor for get_wasm_plugin_version

        DEPRECATED. Please use the `post_get_wasm_plugin_version_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkServices server but before
        it is returned to user code. This `post_get_wasm_plugin_version` interceptor runs
        before the `post_get_wasm_plugin_version_with_metadata` interceptor.
        """
        return response

    def post_get_wasm_plugin_version_with_metadata(
        self,
        response: extensibility.WasmPluginVersion,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        extensibility.WasmPluginVersion, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_wasm_plugin_version

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkServices server but before it is returned to user code.

        We recommend only using this `post_get_wasm_plugin_version_with_metadata`
        interceptor in new development instead of the `post_get_wasm_plugin_version` interceptor.
        When both interceptors are used, this `post_get_wasm_plugin_version_with_metadata` interceptor runs after the
        `post_get_wasm_plugin_version` interceptor. The (possibly modified) response returned by
        `post_get_wasm_plugin_version` will be passed to
        `post_get_wasm_plugin_version_with_metadata`.
        """
        return response, metadata

    def pre_list_agent_gateways(
        self,
        request: agent_gateway.ListAgentGatewaysRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        agent_gateway.ListAgentGatewaysRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_agent_gateways

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_list_agent_gateways(
        self, response: agent_gateway.ListAgentGatewaysResponse
    ) -> agent_gateway.ListAgentGatewaysResponse:
        """Post-rpc interceptor for list_agent_gateways

        DEPRECATED. Please use the `post_list_agent_gateways_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkServices server but before
        it is returned to user code. This `post_list_agent_gateways` interceptor runs
        before the `post_list_agent_gateways_with_metadata` interceptor.
        """
        return response

    def post_list_agent_gateways_with_metadata(
        self,
        response: agent_gateway.ListAgentGatewaysResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        agent_gateway.ListAgentGatewaysResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_agent_gateways

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkServices server but before it is returned to user code.

        We recommend only using this `post_list_agent_gateways_with_metadata`
        interceptor in new development instead of the `post_list_agent_gateways` interceptor.
        When both interceptors are used, this `post_list_agent_gateways_with_metadata` interceptor runs after the
        `post_list_agent_gateways` interceptor. The (possibly modified) response returned by
        `post_list_agent_gateways` will be passed to
        `post_list_agent_gateways_with_metadata`.
        """
        return response, metadata

    def pre_list_endpoint_policies(
        self,
        request: endpoint_policy.ListEndpointPoliciesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        endpoint_policy.ListEndpointPoliciesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_endpoint_policies

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_list_endpoint_policies(
        self, response: endpoint_policy.ListEndpointPoliciesResponse
    ) -> endpoint_policy.ListEndpointPoliciesResponse:
        """Post-rpc interceptor for list_endpoint_policies

        DEPRECATED. Please use the `post_list_endpoint_policies_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkServices server but before
        it is returned to user code. This `post_list_endpoint_policies` interceptor runs
        before the `post_list_endpoint_policies_with_metadata` interceptor.
        """
        return response

    def post_list_endpoint_policies_with_metadata(
        self,
        response: endpoint_policy.ListEndpointPoliciesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        endpoint_policy.ListEndpointPoliciesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_endpoint_policies

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkServices server but before it is returned to user code.

        We recommend only using this `post_list_endpoint_policies_with_metadata`
        interceptor in new development instead of the `post_list_endpoint_policies` interceptor.
        When both interceptors are used, this `post_list_endpoint_policies_with_metadata` interceptor runs after the
        `post_list_endpoint_policies` interceptor. The (possibly modified) response returned by
        `post_list_endpoint_policies` will be passed to
        `post_list_endpoint_policies_with_metadata`.
        """
        return response, metadata

    def pre_list_gateway_route_views(
        self,
        request: route_view.ListGatewayRouteViewsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        route_view.ListGatewayRouteViewsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_gateway_route_views

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_list_gateway_route_views(
        self, response: route_view.ListGatewayRouteViewsResponse
    ) -> route_view.ListGatewayRouteViewsResponse:
        """Post-rpc interceptor for list_gateway_route_views

        DEPRECATED. Please use the `post_list_gateway_route_views_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkServices server but before
        it is returned to user code. This `post_list_gateway_route_views` interceptor runs
        before the `post_list_gateway_route_views_with_metadata` interceptor.
        """
        return response

    def post_list_gateway_route_views_with_metadata(
        self,
        response: route_view.ListGatewayRouteViewsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        route_view.ListGatewayRouteViewsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_gateway_route_views

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkServices server but before it is returned to user code.

        We recommend only using this `post_list_gateway_route_views_with_metadata`
        interceptor in new development instead of the `post_list_gateway_route_views` interceptor.
        When both interceptors are used, this `post_list_gateway_route_views_with_metadata` interceptor runs after the
        `post_list_gateway_route_views` interceptor. The (possibly modified) response returned by
        `post_list_gateway_route_views` will be passed to
        `post_list_gateway_route_views_with_metadata`.
        """
        return response, metadata

    def pre_list_gateways(
        self,
        request: gateway.ListGatewaysRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gateway.ListGatewaysRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_gateways

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_list_gateways(
        self, response: gateway.ListGatewaysResponse
    ) -> gateway.ListGatewaysResponse:
        """Post-rpc interceptor for list_gateways

        DEPRECATED. Please use the `post_list_gateways_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkServices server but before
        it is returned to user code. This `post_list_gateways` interceptor runs
        before the `post_list_gateways_with_metadata` interceptor.
        """
        return response

    def post_list_gateways_with_metadata(
        self,
        response: gateway.ListGatewaysResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gateway.ListGatewaysResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_gateways

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkServices server but before it is returned to user code.

        We recommend only using this `post_list_gateways_with_metadata`
        interceptor in new development instead of the `post_list_gateways` interceptor.
        When both interceptors are used, this `post_list_gateways_with_metadata` interceptor runs after the
        `post_list_gateways` interceptor. The (possibly modified) response returned by
        `post_list_gateways` will be passed to
        `post_list_gateways_with_metadata`.
        """
        return response, metadata

    def pre_list_grpc_routes(
        self,
        request: grpc_route.ListGrpcRoutesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        grpc_route.ListGrpcRoutesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_grpc_routes

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_list_grpc_routes(
        self, response: grpc_route.ListGrpcRoutesResponse
    ) -> grpc_route.ListGrpcRoutesResponse:
        """Post-rpc interceptor for list_grpc_routes

        DEPRECATED. Please use the `post_list_grpc_routes_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkServices server but before
        it is returned to user code. This `post_list_grpc_routes` interceptor runs
        before the `post_list_grpc_routes_with_metadata` interceptor.
        """
        return response

    def post_list_grpc_routes_with_metadata(
        self,
        response: grpc_route.ListGrpcRoutesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        grpc_route.ListGrpcRoutesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_grpc_routes

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkServices server but before it is returned to user code.

        We recommend only using this `post_list_grpc_routes_with_metadata`
        interceptor in new development instead of the `post_list_grpc_routes` interceptor.
        When both interceptors are used, this `post_list_grpc_routes_with_metadata` interceptor runs after the
        `post_list_grpc_routes` interceptor. The (possibly modified) response returned by
        `post_list_grpc_routes` will be passed to
        `post_list_grpc_routes_with_metadata`.
        """
        return response, metadata

    def pre_list_http_routes(
        self,
        request: http_route.ListHttpRoutesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        http_route.ListHttpRoutesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_http_routes

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_list_http_routes(
        self, response: http_route.ListHttpRoutesResponse
    ) -> http_route.ListHttpRoutesResponse:
        """Post-rpc interceptor for list_http_routes

        DEPRECATED. Please use the `post_list_http_routes_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkServices server but before
        it is returned to user code. This `post_list_http_routes` interceptor runs
        before the `post_list_http_routes_with_metadata` interceptor.
        """
        return response

    def post_list_http_routes_with_metadata(
        self,
        response: http_route.ListHttpRoutesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        http_route.ListHttpRoutesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_http_routes

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkServices server but before it is returned to user code.

        We recommend only using this `post_list_http_routes_with_metadata`
        interceptor in new development instead of the `post_list_http_routes` interceptor.
        When both interceptors are used, this `post_list_http_routes_with_metadata` interceptor runs after the
        `post_list_http_routes` interceptor. The (possibly modified) response returned by
        `post_list_http_routes` will be passed to
        `post_list_http_routes_with_metadata`.
        """
        return response, metadata

    def pre_list_meshes(
        self,
        request: mesh.ListMeshesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[mesh.ListMeshesRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_meshes

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_list_meshes(
        self, response: mesh.ListMeshesResponse
    ) -> mesh.ListMeshesResponse:
        """Post-rpc interceptor for list_meshes

        DEPRECATED. Please use the `post_list_meshes_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkServices server but before
        it is returned to user code. This `post_list_meshes` interceptor runs
        before the `post_list_meshes_with_metadata` interceptor.
        """
        return response

    def post_list_meshes_with_metadata(
        self,
        response: mesh.ListMeshesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[mesh.ListMeshesResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_meshes

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkServices server but before it is returned to user code.

        We recommend only using this `post_list_meshes_with_metadata`
        interceptor in new development instead of the `post_list_meshes` interceptor.
        When both interceptors are used, this `post_list_meshes_with_metadata` interceptor runs after the
        `post_list_meshes` interceptor. The (possibly modified) response returned by
        `post_list_meshes` will be passed to
        `post_list_meshes_with_metadata`.
        """
        return response, metadata

    def pre_list_mesh_route_views(
        self,
        request: route_view.ListMeshRouteViewsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        route_view.ListMeshRouteViewsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_mesh_route_views

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_list_mesh_route_views(
        self, response: route_view.ListMeshRouteViewsResponse
    ) -> route_view.ListMeshRouteViewsResponse:
        """Post-rpc interceptor for list_mesh_route_views

        DEPRECATED. Please use the `post_list_mesh_route_views_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkServices server but before
        it is returned to user code. This `post_list_mesh_route_views` interceptor runs
        before the `post_list_mesh_route_views_with_metadata` interceptor.
        """
        return response

    def post_list_mesh_route_views_with_metadata(
        self,
        response: route_view.ListMeshRouteViewsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        route_view.ListMeshRouteViewsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_mesh_route_views

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkServices server but before it is returned to user code.

        We recommend only using this `post_list_mesh_route_views_with_metadata`
        interceptor in new development instead of the `post_list_mesh_route_views` interceptor.
        When both interceptors are used, this `post_list_mesh_route_views_with_metadata` interceptor runs after the
        `post_list_mesh_route_views` interceptor. The (possibly modified) response returned by
        `post_list_mesh_route_views` will be passed to
        `post_list_mesh_route_views_with_metadata`.
        """
        return response, metadata

    def pre_list_service_bindings(
        self,
        request: service_binding.ListServiceBindingsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service_binding.ListServiceBindingsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_service_bindings

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_list_service_bindings(
        self, response: service_binding.ListServiceBindingsResponse
    ) -> service_binding.ListServiceBindingsResponse:
        """Post-rpc interceptor for list_service_bindings

        DEPRECATED. Please use the `post_list_service_bindings_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkServices server but before
        it is returned to user code. This `post_list_service_bindings` interceptor runs
        before the `post_list_service_bindings_with_metadata` interceptor.
        """
        return response

    def post_list_service_bindings_with_metadata(
        self,
        response: service_binding.ListServiceBindingsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service_binding.ListServiceBindingsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_service_bindings

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkServices server but before it is returned to user code.

        We recommend only using this `post_list_service_bindings_with_metadata`
        interceptor in new development instead of the `post_list_service_bindings` interceptor.
        When both interceptors are used, this `post_list_service_bindings_with_metadata` interceptor runs after the
        `post_list_service_bindings` interceptor. The (possibly modified) response returned by
        `post_list_service_bindings` will be passed to
        `post_list_service_bindings_with_metadata`.
        """
        return response, metadata

    def pre_list_service_lb_policies(
        self,
        request: service_lb_policy.ListServiceLbPoliciesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service_lb_policy.ListServiceLbPoliciesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_service_lb_policies

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_list_service_lb_policies(
        self, response: service_lb_policy.ListServiceLbPoliciesResponse
    ) -> service_lb_policy.ListServiceLbPoliciesResponse:
        """Post-rpc interceptor for list_service_lb_policies

        DEPRECATED. Please use the `post_list_service_lb_policies_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkServices server but before
        it is returned to user code. This `post_list_service_lb_policies` interceptor runs
        before the `post_list_service_lb_policies_with_metadata` interceptor.
        """
        return response

    def post_list_service_lb_policies_with_metadata(
        self,
        response: service_lb_policy.ListServiceLbPoliciesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service_lb_policy.ListServiceLbPoliciesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_service_lb_policies

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkServices server but before it is returned to user code.

        We recommend only using this `post_list_service_lb_policies_with_metadata`
        interceptor in new development instead of the `post_list_service_lb_policies` interceptor.
        When both interceptors are used, this `post_list_service_lb_policies_with_metadata` interceptor runs after the
        `post_list_service_lb_policies` interceptor. The (possibly modified) response returned by
        `post_list_service_lb_policies` will be passed to
        `post_list_service_lb_policies_with_metadata`.
        """
        return response, metadata

    def pre_list_tcp_routes(
        self,
        request: tcp_route.ListTcpRoutesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[tcp_route.ListTcpRoutesRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_tcp_routes

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_list_tcp_routes(
        self, response: tcp_route.ListTcpRoutesResponse
    ) -> tcp_route.ListTcpRoutesResponse:
        """Post-rpc interceptor for list_tcp_routes

        DEPRECATED. Please use the `post_list_tcp_routes_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkServices server but before
        it is returned to user code. This `post_list_tcp_routes` interceptor runs
        before the `post_list_tcp_routes_with_metadata` interceptor.
        """
        return response

    def post_list_tcp_routes_with_metadata(
        self,
        response: tcp_route.ListTcpRoutesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        tcp_route.ListTcpRoutesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_tcp_routes

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkServices server but before it is returned to user code.

        We recommend only using this `post_list_tcp_routes_with_metadata`
        interceptor in new development instead of the `post_list_tcp_routes` interceptor.
        When both interceptors are used, this `post_list_tcp_routes_with_metadata` interceptor runs after the
        `post_list_tcp_routes` interceptor. The (possibly modified) response returned by
        `post_list_tcp_routes` will be passed to
        `post_list_tcp_routes_with_metadata`.
        """
        return response, metadata

    def pre_list_tls_routes(
        self,
        request: tls_route.ListTlsRoutesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[tls_route.ListTlsRoutesRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_tls_routes

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_list_tls_routes(
        self, response: tls_route.ListTlsRoutesResponse
    ) -> tls_route.ListTlsRoutesResponse:
        """Post-rpc interceptor for list_tls_routes

        DEPRECATED. Please use the `post_list_tls_routes_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkServices server but before
        it is returned to user code. This `post_list_tls_routes` interceptor runs
        before the `post_list_tls_routes_with_metadata` interceptor.
        """
        return response

    def post_list_tls_routes_with_metadata(
        self,
        response: tls_route.ListTlsRoutesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        tls_route.ListTlsRoutesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_tls_routes

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkServices server but before it is returned to user code.

        We recommend only using this `post_list_tls_routes_with_metadata`
        interceptor in new development instead of the `post_list_tls_routes` interceptor.
        When both interceptors are used, this `post_list_tls_routes_with_metadata` interceptor runs after the
        `post_list_tls_routes` interceptor. The (possibly modified) response returned by
        `post_list_tls_routes` will be passed to
        `post_list_tls_routes_with_metadata`.
        """
        return response, metadata

    def pre_list_wasm_plugins(
        self,
        request: extensibility.ListWasmPluginsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        extensibility.ListWasmPluginsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_wasm_plugins

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_list_wasm_plugins(
        self, response: extensibility.ListWasmPluginsResponse
    ) -> extensibility.ListWasmPluginsResponse:
        """Post-rpc interceptor for list_wasm_plugins

        DEPRECATED. Please use the `post_list_wasm_plugins_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkServices server but before
        it is returned to user code. This `post_list_wasm_plugins` interceptor runs
        before the `post_list_wasm_plugins_with_metadata` interceptor.
        """
        return response

    def post_list_wasm_plugins_with_metadata(
        self,
        response: extensibility.ListWasmPluginsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        extensibility.ListWasmPluginsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_wasm_plugins

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkServices server but before it is returned to user code.

        We recommend only using this `post_list_wasm_plugins_with_metadata`
        interceptor in new development instead of the `post_list_wasm_plugins` interceptor.
        When both interceptors are used, this `post_list_wasm_plugins_with_metadata` interceptor runs after the
        `post_list_wasm_plugins` interceptor. The (possibly modified) response returned by
        `post_list_wasm_plugins` will be passed to
        `post_list_wasm_plugins_with_metadata`.
        """
        return response, metadata

    def pre_list_wasm_plugin_versions(
        self,
        request: extensibility.ListWasmPluginVersionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        extensibility.ListWasmPluginVersionsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_wasm_plugin_versions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_list_wasm_plugin_versions(
        self, response: extensibility.ListWasmPluginVersionsResponse
    ) -> extensibility.ListWasmPluginVersionsResponse:
        """Post-rpc interceptor for list_wasm_plugin_versions

        DEPRECATED. Please use the `post_list_wasm_plugin_versions_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkServices server but before
        it is returned to user code. This `post_list_wasm_plugin_versions` interceptor runs
        before the `post_list_wasm_plugin_versions_with_metadata` interceptor.
        """
        return response

    def post_list_wasm_plugin_versions_with_metadata(
        self,
        response: extensibility.ListWasmPluginVersionsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        extensibility.ListWasmPluginVersionsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_wasm_plugin_versions

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkServices server but before it is returned to user code.

        We recommend only using this `post_list_wasm_plugin_versions_with_metadata`
        interceptor in new development instead of the `post_list_wasm_plugin_versions` interceptor.
        When both interceptors are used, this `post_list_wasm_plugin_versions_with_metadata` interceptor runs after the
        `post_list_wasm_plugin_versions` interceptor. The (possibly modified) response returned by
        `post_list_wasm_plugin_versions` will be passed to
        `post_list_wasm_plugin_versions_with_metadata`.
        """
        return response, metadata

    def pre_update_agent_gateway(
        self,
        request: gcn_agent_gateway.UpdateAgentGatewayRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcn_agent_gateway.UpdateAgentGatewayRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_agent_gateway

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_update_agent_gateway(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_agent_gateway

        DEPRECATED. Please use the `post_update_agent_gateway_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkServices server but before
        it is returned to user code. This `post_update_agent_gateway` interceptor runs
        before the `post_update_agent_gateway_with_metadata` interceptor.
        """
        return response

    def post_update_agent_gateway_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_agent_gateway

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkServices server but before it is returned to user code.

        We recommend only using this `post_update_agent_gateway_with_metadata`
        interceptor in new development instead of the `post_update_agent_gateway` interceptor.
        When both interceptors are used, this `post_update_agent_gateway_with_metadata` interceptor runs after the
        `post_update_agent_gateway` interceptor. The (possibly modified) response returned by
        `post_update_agent_gateway` will be passed to
        `post_update_agent_gateway_with_metadata`.
        """
        return response, metadata

    def pre_update_endpoint_policy(
        self,
        request: gcn_endpoint_policy.UpdateEndpointPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcn_endpoint_policy.UpdateEndpointPolicyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_endpoint_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_update_endpoint_policy(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_endpoint_policy

        DEPRECATED. Please use the `post_update_endpoint_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkServices server but before
        it is returned to user code. This `post_update_endpoint_policy` interceptor runs
        before the `post_update_endpoint_policy_with_metadata` interceptor.
        """
        return response

    def post_update_endpoint_policy_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_endpoint_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkServices server but before it is returned to user code.

        We recommend only using this `post_update_endpoint_policy_with_metadata`
        interceptor in new development instead of the `post_update_endpoint_policy` interceptor.
        When both interceptors are used, this `post_update_endpoint_policy_with_metadata` interceptor runs after the
        `post_update_endpoint_policy` interceptor. The (possibly modified) response returned by
        `post_update_endpoint_policy` will be passed to
        `post_update_endpoint_policy_with_metadata`.
        """
        return response, metadata

    def pre_update_gateway(
        self,
        request: gcn_gateway.UpdateGatewayRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcn_gateway.UpdateGatewayRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_gateway

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_update_gateway(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_gateway

        DEPRECATED. Please use the `post_update_gateway_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkServices server but before
        it is returned to user code. This `post_update_gateway` interceptor runs
        before the `post_update_gateway_with_metadata` interceptor.
        """
        return response

    def post_update_gateway_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_gateway

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkServices server but before it is returned to user code.

        We recommend only using this `post_update_gateway_with_metadata`
        interceptor in new development instead of the `post_update_gateway` interceptor.
        When both interceptors are used, this `post_update_gateway_with_metadata` interceptor runs after the
        `post_update_gateway` interceptor. The (possibly modified) response returned by
        `post_update_gateway` will be passed to
        `post_update_gateway_with_metadata`.
        """
        return response, metadata

    def pre_update_grpc_route(
        self,
        request: gcn_grpc_route.UpdateGrpcRouteRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcn_grpc_route.UpdateGrpcRouteRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_grpc_route

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_update_grpc_route(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_grpc_route

        DEPRECATED. Please use the `post_update_grpc_route_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkServices server but before
        it is returned to user code. This `post_update_grpc_route` interceptor runs
        before the `post_update_grpc_route_with_metadata` interceptor.
        """
        return response

    def post_update_grpc_route_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_grpc_route

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkServices server but before it is returned to user code.

        We recommend only using this `post_update_grpc_route_with_metadata`
        interceptor in new development instead of the `post_update_grpc_route` interceptor.
        When both interceptors are used, this `post_update_grpc_route_with_metadata` interceptor runs after the
        `post_update_grpc_route` interceptor. The (possibly modified) response returned by
        `post_update_grpc_route` will be passed to
        `post_update_grpc_route_with_metadata`.
        """
        return response, metadata

    def pre_update_http_route(
        self,
        request: gcn_http_route.UpdateHttpRouteRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcn_http_route.UpdateHttpRouteRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_http_route

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_update_http_route(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_http_route

        DEPRECATED. Please use the `post_update_http_route_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkServices server but before
        it is returned to user code. This `post_update_http_route` interceptor runs
        before the `post_update_http_route_with_metadata` interceptor.
        """
        return response

    def post_update_http_route_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_http_route

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkServices server but before it is returned to user code.

        We recommend only using this `post_update_http_route_with_metadata`
        interceptor in new development instead of the `post_update_http_route` interceptor.
        When both interceptors are used, this `post_update_http_route_with_metadata` interceptor runs after the
        `post_update_http_route` interceptor. The (possibly modified) response returned by
        `post_update_http_route` will be passed to
        `post_update_http_route_with_metadata`.
        """
        return response, metadata

    def pre_update_mesh(
        self,
        request: gcn_mesh.UpdateMeshRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gcn_mesh.UpdateMeshRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for update_mesh

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_update_mesh(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_mesh

        DEPRECATED. Please use the `post_update_mesh_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkServices server but before
        it is returned to user code. This `post_update_mesh` interceptor runs
        before the `post_update_mesh_with_metadata` interceptor.
        """
        return response

    def post_update_mesh_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_mesh

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkServices server but before it is returned to user code.

        We recommend only using this `post_update_mesh_with_metadata`
        interceptor in new development instead of the `post_update_mesh` interceptor.
        When both interceptors are used, this `post_update_mesh_with_metadata` interceptor runs after the
        `post_update_mesh` interceptor. The (possibly modified) response returned by
        `post_update_mesh` will be passed to
        `post_update_mesh_with_metadata`.
        """
        return response, metadata

    def pre_update_service_binding(
        self,
        request: gcn_service_binding.UpdateServiceBindingRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcn_service_binding.UpdateServiceBindingRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_service_binding

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_update_service_binding(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_service_binding

        DEPRECATED. Please use the `post_update_service_binding_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkServices server but before
        it is returned to user code. This `post_update_service_binding` interceptor runs
        before the `post_update_service_binding_with_metadata` interceptor.
        """
        return response

    def post_update_service_binding_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_service_binding

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkServices server but before it is returned to user code.

        We recommend only using this `post_update_service_binding_with_metadata`
        interceptor in new development instead of the `post_update_service_binding` interceptor.
        When both interceptors are used, this `post_update_service_binding_with_metadata` interceptor runs after the
        `post_update_service_binding` interceptor. The (possibly modified) response returned by
        `post_update_service_binding` will be passed to
        `post_update_service_binding_with_metadata`.
        """
        return response, metadata

    def pre_update_service_lb_policy(
        self,
        request: gcn_service_lb_policy.UpdateServiceLbPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcn_service_lb_policy.UpdateServiceLbPolicyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_service_lb_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_update_service_lb_policy(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_service_lb_policy

        DEPRECATED. Please use the `post_update_service_lb_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkServices server but before
        it is returned to user code. This `post_update_service_lb_policy` interceptor runs
        before the `post_update_service_lb_policy_with_metadata` interceptor.
        """
        return response

    def post_update_service_lb_policy_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_service_lb_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkServices server but before it is returned to user code.

        We recommend only using this `post_update_service_lb_policy_with_metadata`
        interceptor in new development instead of the `post_update_service_lb_policy` interceptor.
        When both interceptors are used, this `post_update_service_lb_policy_with_metadata` interceptor runs after the
        `post_update_service_lb_policy` interceptor. The (possibly modified) response returned by
        `post_update_service_lb_policy` will be passed to
        `post_update_service_lb_policy_with_metadata`.
        """
        return response, metadata

    def pre_update_tcp_route(
        self,
        request: gcn_tcp_route.UpdateTcpRouteRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcn_tcp_route.UpdateTcpRouteRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_tcp_route

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_update_tcp_route(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_tcp_route

        DEPRECATED. Please use the `post_update_tcp_route_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkServices server but before
        it is returned to user code. This `post_update_tcp_route` interceptor runs
        before the `post_update_tcp_route_with_metadata` interceptor.
        """
        return response

    def post_update_tcp_route_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_tcp_route

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkServices server but before it is returned to user code.

        We recommend only using this `post_update_tcp_route_with_metadata`
        interceptor in new development instead of the `post_update_tcp_route` interceptor.
        When both interceptors are used, this `post_update_tcp_route_with_metadata` interceptor runs after the
        `post_update_tcp_route` interceptor. The (possibly modified) response returned by
        `post_update_tcp_route` will be passed to
        `post_update_tcp_route_with_metadata`.
        """
        return response, metadata

    def pre_update_tls_route(
        self,
        request: gcn_tls_route.UpdateTlsRouteRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcn_tls_route.UpdateTlsRouteRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_tls_route

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_update_tls_route(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_tls_route

        DEPRECATED. Please use the `post_update_tls_route_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkServices server but before
        it is returned to user code. This `post_update_tls_route` interceptor runs
        before the `post_update_tls_route_with_metadata` interceptor.
        """
        return response

    def post_update_tls_route_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_tls_route

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkServices server but before it is returned to user code.

        We recommend only using this `post_update_tls_route_with_metadata`
        interceptor in new development instead of the `post_update_tls_route` interceptor.
        When both interceptors are used, this `post_update_tls_route_with_metadata` interceptor runs after the
        `post_update_tls_route` interceptor. The (possibly modified) response returned by
        `post_update_tls_route` will be passed to
        `post_update_tls_route_with_metadata`.
        """
        return response, metadata

    def pre_update_wasm_plugin(
        self,
        request: extensibility.UpdateWasmPluginRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        extensibility.UpdateWasmPluginRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_wasm_plugin

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_update_wasm_plugin(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_wasm_plugin

        DEPRECATED. Please use the `post_update_wasm_plugin_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkServices server but before
        it is returned to user code. This `post_update_wasm_plugin` interceptor runs
        before the `post_update_wasm_plugin_with_metadata` interceptor.
        """
        return response

    def post_update_wasm_plugin_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_wasm_plugin

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkServices server but before it is returned to user code.

        We recommend only using this `post_update_wasm_plugin_with_metadata`
        interceptor in new development instead of the `post_update_wasm_plugin` interceptor.
        When both interceptors are used, this `post_update_wasm_plugin_with_metadata` interceptor runs after the
        `post_update_wasm_plugin` interceptor. The (possibly modified) response returned by
        `post_update_wasm_plugin` will be passed to
        `post_update_wasm_plugin_with_metadata`.
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
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the NetworkServices server but before
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
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the NetworkServices server but before
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
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_get_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for get_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the NetworkServices server but before
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
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_set_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for set_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the NetworkServices server but before
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
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_test_iam_permissions(
        self, response: iam_policy_pb2.TestIamPermissionsResponse
    ) -> iam_policy_pb2.TestIamPermissionsResponse:
        """Post-rpc interceptor for test_iam_permissions

        Override in a subclass to manipulate the response
        after it is returned by the NetworkServices server but before
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
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the NetworkServices server but before
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
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_delete_operation(self, response: None) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the NetworkServices server but before
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
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the NetworkServices server but before
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
        before they are sent to the NetworkServices server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the NetworkServices server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class NetworkServicesRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: NetworkServicesRestInterceptor


class NetworkServicesRestTransport(_BaseNetworkServicesRestTransport):
    """REST backend synchronous transport for NetworkServices.

    Service describing handlers for resources.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "networkservices.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[NetworkServicesRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'networkservices.googleapis.com').
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
            interceptor (Optional[NetworkServicesRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or NetworkServicesRestInterceptor()
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

    class _CreateAgentGateway(
        _BaseNetworkServicesRestTransport._BaseCreateAgentGateway,
        NetworkServicesRestStub,
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.CreateAgentGateway")

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
            request: gcn_agent_gateway.CreateAgentGatewayRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create agent gateway method over HTTP.

            Args:
                request (~.gcn_agent_gateway.CreateAgentGatewayRequest):
                    The request object. Request used by the
                CreateAgentGateway method.
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

            http_options = _BaseNetworkServicesRestTransport._BaseCreateAgentGateway._get_http_options()
            request, metadata = self._interceptor.pre_create_agent_gateway(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseCreateAgentGateway,
                    "_BaseCreateAgentGateway__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.CreateAgentGateway",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "CreateAgentGateway",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServicesRestTransport._CreateAgentGateway._get_response(
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

            resp = self._interceptor.post_create_agent_gateway(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_agent_gateway_with_metadata(
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
                    "Received response for google.cloud.networkservices_v1.NetworkServicesClient.create_agent_gateway",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "CreateAgentGateway",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateEndpointPolicy(
        _BaseNetworkServicesRestTransport._BaseCreateEndpointPolicy,
        NetworkServicesRestStub,
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.CreateEndpointPolicy")

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
            request: gcn_endpoint_policy.CreateEndpointPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create endpoint policy method over HTTP.

            Args:
                request (~.gcn_endpoint_policy.CreateEndpointPolicyRequest):
                    The request object. Request used with the
                CreateEndpointPolicy method.
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

            http_options = _BaseNetworkServicesRestTransport._BaseCreateEndpointPolicy._get_http_options()
            request, metadata = self._interceptor.pre_create_endpoint_policy(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseCreateEndpointPolicy,
                    "_BaseCreateEndpointPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.CreateEndpointPolicy",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "CreateEndpointPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServicesRestTransport._CreateEndpointPolicy._get_response(
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

            resp = self._interceptor.post_create_endpoint_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_endpoint_policy_with_metadata(
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
                    "Received response for google.cloud.networkservices_v1.NetworkServicesClient.create_endpoint_policy",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "CreateEndpointPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateGateway(
        _BaseNetworkServicesRestTransport._BaseCreateGateway, NetworkServicesRestStub
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.CreateGateway")

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
            request: gcn_gateway.CreateGatewayRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create gateway method over HTTP.

            Args:
                request (~.gcn_gateway.CreateGatewayRequest):
                    The request object. Request used by the CreateGateway
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
                _BaseNetworkServicesRestTransport._BaseCreateGateway._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_gateway(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseCreateGateway,
                    "_BaseCreateGateway__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.CreateGateway",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "CreateGateway",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServicesRestTransport._CreateGateway._get_response(
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

            resp = self._interceptor.post_create_gateway(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_gateway_with_metadata(
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
                    "Received response for google.cloud.networkservices_v1.NetworkServicesClient.create_gateway",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "CreateGateway",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateGrpcRoute(
        _BaseNetworkServicesRestTransport._BaseCreateGrpcRoute, NetworkServicesRestStub
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.CreateGrpcRoute")

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
            request: gcn_grpc_route.CreateGrpcRouteRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create grpc route method over HTTP.

            Args:
                request (~.gcn_grpc_route.CreateGrpcRouteRequest):
                    The request object. Request used by the CreateGrpcRoute
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

            http_options = _BaseNetworkServicesRestTransport._BaseCreateGrpcRoute._get_http_options()
            request, metadata = self._interceptor.pre_create_grpc_route(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseCreateGrpcRoute,
                    "_BaseCreateGrpcRoute__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.CreateGrpcRoute",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "CreateGrpcRoute",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServicesRestTransport._CreateGrpcRoute._get_response(
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

            resp = self._interceptor.post_create_grpc_route(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_grpc_route_with_metadata(
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
                    "Received response for google.cloud.networkservices_v1.NetworkServicesClient.create_grpc_route",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "CreateGrpcRoute",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateHttpRoute(
        _BaseNetworkServicesRestTransport._BaseCreateHttpRoute, NetworkServicesRestStub
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.CreateHttpRoute")

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
            request: gcn_http_route.CreateHttpRouteRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create http route method over HTTP.

            Args:
                request (~.gcn_http_route.CreateHttpRouteRequest):
                    The request object. Request used by the HttpRoute method.
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

            http_options = _BaseNetworkServicesRestTransport._BaseCreateHttpRoute._get_http_options()
            request, metadata = self._interceptor.pre_create_http_route(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseCreateHttpRoute,
                    "_BaseCreateHttpRoute__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.CreateHttpRoute",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "CreateHttpRoute",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServicesRestTransport._CreateHttpRoute._get_response(
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

            resp = self._interceptor.post_create_http_route(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_http_route_with_metadata(
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
                    "Received response for google.cloud.networkservices_v1.NetworkServicesClient.create_http_route",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "CreateHttpRoute",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateMesh(
        _BaseNetworkServicesRestTransport._BaseCreateMesh, NetworkServicesRestStub
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.CreateMesh")

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
            request: gcn_mesh.CreateMeshRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create mesh method over HTTP.

            Args:
                request (~.gcn_mesh.CreateMeshRequest):
                    The request object. Request used by the CreateMesh
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
                _BaseNetworkServicesRestTransport._BaseCreateMesh._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_mesh(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseCreateMesh,
                    "_BaseCreateMesh__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.CreateMesh",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "CreateMesh",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServicesRestTransport._CreateMesh._get_response(
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

            resp = self._interceptor.post_create_mesh(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_mesh_with_metadata(
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
                    "Received response for google.cloud.networkservices_v1.NetworkServicesClient.create_mesh",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "CreateMesh",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateServiceBinding(
        _BaseNetworkServicesRestTransport._BaseCreateServiceBinding,
        NetworkServicesRestStub,
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.CreateServiceBinding")

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
            request: gcn_service_binding.CreateServiceBindingRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create service binding method over HTTP.

            Args:
                request (~.gcn_service_binding.CreateServiceBindingRequest):
                    The request object. Request used by the ServiceBinding
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

            http_options = _BaseNetworkServicesRestTransport._BaseCreateServiceBinding._get_http_options()
            request, metadata = self._interceptor.pre_create_service_binding(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseCreateServiceBinding,
                    "_BaseCreateServiceBinding__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.CreateServiceBinding",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "CreateServiceBinding",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServicesRestTransport._CreateServiceBinding._get_response(
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

            resp = self._interceptor.post_create_service_binding(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_service_binding_with_metadata(
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
                    "Received response for google.cloud.networkservices_v1.NetworkServicesClient.create_service_binding",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "CreateServiceBinding",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateServiceLbPolicy(
        _BaseNetworkServicesRestTransport._BaseCreateServiceLbPolicy,
        NetworkServicesRestStub,
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.CreateServiceLbPolicy")

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
            request: gcn_service_lb_policy.CreateServiceLbPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create service lb policy method over HTTP.

            Args:
                request (~.gcn_service_lb_policy.CreateServiceLbPolicyRequest):
                    The request object. Request used by the ServiceLbPolicy
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

            http_options = _BaseNetworkServicesRestTransport._BaseCreateServiceLbPolicy._get_http_options()
            request, metadata = self._interceptor.pre_create_service_lb_policy(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseCreateServiceLbPolicy,
                    "_BaseCreateServiceLbPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.CreateServiceLbPolicy",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "CreateServiceLbPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                NetworkServicesRestTransport._CreateServiceLbPolicy._get_response(
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

            resp = self._interceptor.post_create_service_lb_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_service_lb_policy_with_metadata(
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
                    "Received response for google.cloud.networkservices_v1.NetworkServicesClient.create_service_lb_policy",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "CreateServiceLbPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateTcpRoute(
        _BaseNetworkServicesRestTransport._BaseCreateTcpRoute, NetworkServicesRestStub
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.CreateTcpRoute")

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
            request: gcn_tcp_route.CreateTcpRouteRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create tcp route method over HTTP.

            Args:
                request (~.gcn_tcp_route.CreateTcpRouteRequest):
                    The request object. Request used by the TcpRoute method.
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

            http_options = _BaseNetworkServicesRestTransport._BaseCreateTcpRoute._get_http_options()
            request, metadata = self._interceptor.pre_create_tcp_route(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseCreateTcpRoute,
                    "_BaseCreateTcpRoute__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.CreateTcpRoute",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "CreateTcpRoute",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServicesRestTransport._CreateTcpRoute._get_response(
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

            resp = self._interceptor.post_create_tcp_route(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_tcp_route_with_metadata(
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
                    "Received response for google.cloud.networkservices_v1.NetworkServicesClient.create_tcp_route",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "CreateTcpRoute",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateTlsRoute(
        _BaseNetworkServicesRestTransport._BaseCreateTlsRoute, NetworkServicesRestStub
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.CreateTlsRoute")

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
            request: gcn_tls_route.CreateTlsRouteRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create tls route method over HTTP.

            Args:
                request (~.gcn_tls_route.CreateTlsRouteRequest):
                    The request object. Request used by the TlsRoute method.
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

            http_options = _BaseNetworkServicesRestTransport._BaseCreateTlsRoute._get_http_options()
            request, metadata = self._interceptor.pre_create_tls_route(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseCreateTlsRoute,
                    "_BaseCreateTlsRoute__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.CreateTlsRoute",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "CreateTlsRoute",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServicesRestTransport._CreateTlsRoute._get_response(
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

            resp = self._interceptor.post_create_tls_route(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_tls_route_with_metadata(
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
                    "Received response for google.cloud.networkservices_v1.NetworkServicesClient.create_tls_route",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "CreateTlsRoute",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateWasmPlugin(
        _BaseNetworkServicesRestTransport._BaseCreateWasmPlugin, NetworkServicesRestStub
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.CreateWasmPlugin")

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
            request: extensibility.CreateWasmPluginRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create wasm plugin method over HTTP.

            Args:
                request (~.extensibility.CreateWasmPluginRequest):
                    The request object. Request used by the ``CreateWasmPlugin`` method.
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

            http_options = _BaseNetworkServicesRestTransport._BaseCreateWasmPlugin._get_http_options()
            request, metadata = self._interceptor.pre_create_wasm_plugin(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseCreateWasmPlugin,
                    "_BaseCreateWasmPlugin__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.CreateWasmPlugin",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "CreateWasmPlugin",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServicesRestTransport._CreateWasmPlugin._get_response(
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

            resp = self._interceptor.post_create_wasm_plugin(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_wasm_plugin_with_metadata(
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
                    "Received response for google.cloud.networkservices_v1.NetworkServicesClient.create_wasm_plugin",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "CreateWasmPlugin",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateWasmPluginVersion(
        _BaseNetworkServicesRestTransport._BaseCreateWasmPluginVersion,
        NetworkServicesRestStub,
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.CreateWasmPluginVersion")

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
            request: extensibility.CreateWasmPluginVersionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create wasm plugin
            version method over HTTP.

                Args:
                    request (~.extensibility.CreateWasmPluginVersionRequest):
                        The request object. Request used by the ``CreateWasmPluginVersion`` method.
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

            http_options = _BaseNetworkServicesRestTransport._BaseCreateWasmPluginVersion._get_http_options()
            request, metadata = self._interceptor.pre_create_wasm_plugin_version(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseCreateWasmPluginVersion,
                    "_BaseCreateWasmPluginVersion__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.CreateWasmPluginVersion",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "CreateWasmPluginVersion",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                NetworkServicesRestTransport._CreateWasmPluginVersion._get_response(
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

            resp = self._interceptor.post_create_wasm_plugin_version(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_wasm_plugin_version_with_metadata(
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
                    "Received response for google.cloud.networkservices_v1.NetworkServicesClient.create_wasm_plugin_version",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "CreateWasmPluginVersion",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteAgentGateway(
        _BaseNetworkServicesRestTransport._BaseDeleteAgentGateway,
        NetworkServicesRestStub,
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.DeleteAgentGateway")

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
            request: agent_gateway.DeleteAgentGatewayRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete agent gateway method over HTTP.

            Args:
                request (~.agent_gateway.DeleteAgentGatewayRequest):
                    The request object. Request used by the
                DeleteAgentGateway method.
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

            http_options = _BaseNetworkServicesRestTransport._BaseDeleteAgentGateway._get_http_options()
            request, metadata = self._interceptor.pre_delete_agent_gateway(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseDeleteAgentGateway,
                    "_BaseDeleteAgentGateway__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.DeleteAgentGateway",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "DeleteAgentGateway",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServicesRestTransport._DeleteAgentGateway._get_response(
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

            resp = self._interceptor.post_delete_agent_gateway(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_agent_gateway_with_metadata(
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
                    "Received response for google.cloud.networkservices_v1.NetworkServicesClient.delete_agent_gateway",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "DeleteAgentGateway",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteEndpointPolicy(
        _BaseNetworkServicesRestTransport._BaseDeleteEndpointPolicy,
        NetworkServicesRestStub,
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.DeleteEndpointPolicy")

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
            request: endpoint_policy.DeleteEndpointPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete endpoint policy method over HTTP.

            Args:
                request (~.endpoint_policy.DeleteEndpointPolicyRequest):
                    The request object. Request used with the
                DeleteEndpointPolicy method.
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

            http_options = _BaseNetworkServicesRestTransport._BaseDeleteEndpointPolicy._get_http_options()
            request, metadata = self._interceptor.pre_delete_endpoint_policy(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseDeleteEndpointPolicy,
                    "_BaseDeleteEndpointPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.DeleteEndpointPolicy",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "DeleteEndpointPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServicesRestTransport._DeleteEndpointPolicy._get_response(
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

            resp = self._interceptor.post_delete_endpoint_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_endpoint_policy_with_metadata(
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
                    "Received response for google.cloud.networkservices_v1.NetworkServicesClient.delete_endpoint_policy",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "DeleteEndpointPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteGateway(
        _BaseNetworkServicesRestTransport._BaseDeleteGateway, NetworkServicesRestStub
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.DeleteGateway")

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
            request: gateway.DeleteGatewayRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete gateway method over HTTP.

            Args:
                request (~.gateway.DeleteGatewayRequest):
                    The request object. Request used by the DeleteGateway
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
                _BaseNetworkServicesRestTransport._BaseDeleteGateway._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_gateway(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseDeleteGateway,
                    "_BaseDeleteGateway__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.DeleteGateway",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "DeleteGateway",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServicesRestTransport._DeleteGateway._get_response(
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

            resp = self._interceptor.post_delete_gateway(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_gateway_with_metadata(
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
                    "Received response for google.cloud.networkservices_v1.NetworkServicesClient.delete_gateway",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "DeleteGateway",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteGrpcRoute(
        _BaseNetworkServicesRestTransport._BaseDeleteGrpcRoute, NetworkServicesRestStub
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.DeleteGrpcRoute")

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
            request: grpc_route.DeleteGrpcRouteRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete grpc route method over HTTP.

            Args:
                request (~.grpc_route.DeleteGrpcRouteRequest):
                    The request object. Request used by the DeleteGrpcRoute
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

            http_options = _BaseNetworkServicesRestTransport._BaseDeleteGrpcRoute._get_http_options()
            request, metadata = self._interceptor.pre_delete_grpc_route(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseDeleteGrpcRoute,
                    "_BaseDeleteGrpcRoute__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.DeleteGrpcRoute",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "DeleteGrpcRoute",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServicesRestTransport._DeleteGrpcRoute._get_response(
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

            resp = self._interceptor.post_delete_grpc_route(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_grpc_route_with_metadata(
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
                    "Received response for google.cloud.networkservices_v1.NetworkServicesClient.delete_grpc_route",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "DeleteGrpcRoute",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteHttpRoute(
        _BaseNetworkServicesRestTransport._BaseDeleteHttpRoute, NetworkServicesRestStub
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.DeleteHttpRoute")

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
            request: http_route.DeleteHttpRouteRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete http route method over HTTP.

            Args:
                request (~.http_route.DeleteHttpRouteRequest):
                    The request object. Request used by the DeleteHttpRoute
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

            http_options = _BaseNetworkServicesRestTransport._BaseDeleteHttpRoute._get_http_options()
            request, metadata = self._interceptor.pre_delete_http_route(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseDeleteHttpRoute,
                    "_BaseDeleteHttpRoute__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.DeleteHttpRoute",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "DeleteHttpRoute",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServicesRestTransport._DeleteHttpRoute._get_response(
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

            resp = self._interceptor.post_delete_http_route(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_http_route_with_metadata(
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
                    "Received response for google.cloud.networkservices_v1.NetworkServicesClient.delete_http_route",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "DeleteHttpRoute",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteMesh(
        _BaseNetworkServicesRestTransport._BaseDeleteMesh, NetworkServicesRestStub
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.DeleteMesh")

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
            request: mesh.DeleteMeshRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete mesh method over HTTP.

            Args:
                request (~.mesh.DeleteMeshRequest):
                    The request object. Request used by the DeleteMesh
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
                _BaseNetworkServicesRestTransport._BaseDeleteMesh._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_mesh(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseDeleteMesh,
                    "_BaseDeleteMesh__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.DeleteMesh",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "DeleteMesh",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServicesRestTransport._DeleteMesh._get_response(
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

            resp = self._interceptor.post_delete_mesh(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_mesh_with_metadata(
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
                    "Received response for google.cloud.networkservices_v1.NetworkServicesClient.delete_mesh",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "DeleteMesh",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteServiceBinding(
        _BaseNetworkServicesRestTransport._BaseDeleteServiceBinding,
        NetworkServicesRestStub,
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.DeleteServiceBinding")

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
            request: service_binding.DeleteServiceBindingRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete service binding method over HTTP.

            Args:
                request (~.service_binding.DeleteServiceBindingRequest):
                    The request object. Request used by the
                DeleteServiceBinding method.
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

            http_options = _BaseNetworkServicesRestTransport._BaseDeleteServiceBinding._get_http_options()
            request, metadata = self._interceptor.pre_delete_service_binding(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseDeleteServiceBinding,
                    "_BaseDeleteServiceBinding__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.DeleteServiceBinding",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "DeleteServiceBinding",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServicesRestTransport._DeleteServiceBinding._get_response(
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

            resp = self._interceptor.post_delete_service_binding(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_service_binding_with_metadata(
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
                    "Received response for google.cloud.networkservices_v1.NetworkServicesClient.delete_service_binding",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "DeleteServiceBinding",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteServiceLbPolicy(
        _BaseNetworkServicesRestTransport._BaseDeleteServiceLbPolicy,
        NetworkServicesRestStub,
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.DeleteServiceLbPolicy")

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
            request: service_lb_policy.DeleteServiceLbPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete service lb policy method over HTTP.

            Args:
                request (~.service_lb_policy.DeleteServiceLbPolicyRequest):
                    The request object. Request used by the
                DeleteServiceLbPolicy method.
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

            http_options = _BaseNetworkServicesRestTransport._BaseDeleteServiceLbPolicy._get_http_options()
            request, metadata = self._interceptor.pre_delete_service_lb_policy(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseDeleteServiceLbPolicy,
                    "_BaseDeleteServiceLbPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.DeleteServiceLbPolicy",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "DeleteServiceLbPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                NetworkServicesRestTransport._DeleteServiceLbPolicy._get_response(
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

            resp = self._interceptor.post_delete_service_lb_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_service_lb_policy_with_metadata(
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
                    "Received response for google.cloud.networkservices_v1.NetworkServicesClient.delete_service_lb_policy",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "DeleteServiceLbPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteTcpRoute(
        _BaseNetworkServicesRestTransport._BaseDeleteTcpRoute, NetworkServicesRestStub
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.DeleteTcpRoute")

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
            request: tcp_route.DeleteTcpRouteRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete tcp route method over HTTP.

            Args:
                request (~.tcp_route.DeleteTcpRouteRequest):
                    The request object. Request used by the DeleteTcpRoute
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

            http_options = _BaseNetworkServicesRestTransport._BaseDeleteTcpRoute._get_http_options()
            request, metadata = self._interceptor.pre_delete_tcp_route(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseDeleteTcpRoute,
                    "_BaseDeleteTcpRoute__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.DeleteTcpRoute",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "DeleteTcpRoute",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServicesRestTransport._DeleteTcpRoute._get_response(
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

            resp = self._interceptor.post_delete_tcp_route(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_tcp_route_with_metadata(
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
                    "Received response for google.cloud.networkservices_v1.NetworkServicesClient.delete_tcp_route",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "DeleteTcpRoute",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteTlsRoute(
        _BaseNetworkServicesRestTransport._BaseDeleteTlsRoute, NetworkServicesRestStub
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.DeleteTlsRoute")

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
            request: tls_route.DeleteTlsRouteRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete tls route method over HTTP.

            Args:
                request (~.tls_route.DeleteTlsRouteRequest):
                    The request object. Request used by the DeleteTlsRoute
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

            http_options = _BaseNetworkServicesRestTransport._BaseDeleteTlsRoute._get_http_options()
            request, metadata = self._interceptor.pre_delete_tls_route(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseDeleteTlsRoute,
                    "_BaseDeleteTlsRoute__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.DeleteTlsRoute",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "DeleteTlsRoute",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServicesRestTransport._DeleteTlsRoute._get_response(
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

            resp = self._interceptor.post_delete_tls_route(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_tls_route_with_metadata(
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
                    "Received response for google.cloud.networkservices_v1.NetworkServicesClient.delete_tls_route",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "DeleteTlsRoute",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteWasmPlugin(
        _BaseNetworkServicesRestTransport._BaseDeleteWasmPlugin, NetworkServicesRestStub
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.DeleteWasmPlugin")

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
            request: extensibility.DeleteWasmPluginRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete wasm plugin method over HTTP.

            Args:
                request (~.extensibility.DeleteWasmPluginRequest):
                    The request object. Request used by the ``DeleteWasmPlugin`` method.
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

            http_options = _BaseNetworkServicesRestTransport._BaseDeleteWasmPlugin._get_http_options()
            request, metadata = self._interceptor.pre_delete_wasm_plugin(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseDeleteWasmPlugin,
                    "_BaseDeleteWasmPlugin__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.DeleteWasmPlugin",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "DeleteWasmPlugin",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServicesRestTransport._DeleteWasmPlugin._get_response(
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

            resp = self._interceptor.post_delete_wasm_plugin(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_wasm_plugin_with_metadata(
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
                    "Received response for google.cloud.networkservices_v1.NetworkServicesClient.delete_wasm_plugin",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "DeleteWasmPlugin",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteWasmPluginVersion(
        _BaseNetworkServicesRestTransport._BaseDeleteWasmPluginVersion,
        NetworkServicesRestStub,
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.DeleteWasmPluginVersion")

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
            request: extensibility.DeleteWasmPluginVersionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete wasm plugin
            version method over HTTP.

                Args:
                    request (~.extensibility.DeleteWasmPluginVersionRequest):
                        The request object. Request used by the ``DeleteWasmPluginVersion`` method.
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

            http_options = _BaseNetworkServicesRestTransport._BaseDeleteWasmPluginVersion._get_http_options()
            request, metadata = self._interceptor.pre_delete_wasm_plugin_version(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseDeleteWasmPluginVersion,
                    "_BaseDeleteWasmPluginVersion__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.DeleteWasmPluginVersion",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "DeleteWasmPluginVersion",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                NetworkServicesRestTransport._DeleteWasmPluginVersion._get_response(
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

            resp = self._interceptor.post_delete_wasm_plugin_version(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_wasm_plugin_version_with_metadata(
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
                    "Received response for google.cloud.networkservices_v1.NetworkServicesClient.delete_wasm_plugin_version",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "DeleteWasmPluginVersion",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetAgentGateway(
        _BaseNetworkServicesRestTransport._BaseGetAgentGateway, NetworkServicesRestStub
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.GetAgentGateway")

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
            request: agent_gateway.GetAgentGatewayRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> agent_gateway.AgentGateway:
            r"""Call the get agent gateway method over HTTP.

            Args:
                request (~.agent_gateway.GetAgentGatewayRequest):
                    The request object. Request used by the GetAgentGateway
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.agent_gateway.AgentGateway:
                    AgentGateway represents the agent
                gateway resource.

            """

            http_options = _BaseNetworkServicesRestTransport._BaseGetAgentGateway._get_http_options()
            request, metadata = self._interceptor.pre_get_agent_gateway(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseGetAgentGateway,
                    "_BaseGetAgentGateway__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.GetAgentGateway",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "GetAgentGateway",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServicesRestTransport._GetAgentGateway._get_response(
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
            resp = agent_gateway.AgentGateway()
            pb_resp = agent_gateway.AgentGateway.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_agent_gateway(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_agent_gateway_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = agent_gateway.AgentGateway.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.networkservices_v1.NetworkServicesClient.get_agent_gateway",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "GetAgentGateway",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetEndpointPolicy(
        _BaseNetworkServicesRestTransport._BaseGetEndpointPolicy,
        NetworkServicesRestStub,
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.GetEndpointPolicy")

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
            request: endpoint_policy.GetEndpointPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> endpoint_policy.EndpointPolicy:
            r"""Call the get endpoint policy method over HTTP.

            Args:
                request (~.endpoint_policy.GetEndpointPolicyRequest):
                    The request object. Request used with the
                GetEndpointPolicy method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.endpoint_policy.EndpointPolicy:
                    EndpointPolicy is a resource that
                helps apply desired configuration on the
                endpoints that match specific criteria.
                For example, this resource can be used
                to apply "authentication config" an all
                endpoints that serve on port 8080.

            """

            http_options = _BaseNetworkServicesRestTransport._BaseGetEndpointPolicy._get_http_options()
            request, metadata = self._interceptor.pre_get_endpoint_policy(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseGetEndpointPolicy,
                    "_BaseGetEndpointPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.GetEndpointPolicy",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "GetEndpointPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServicesRestTransport._GetEndpointPolicy._get_response(
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
            resp = endpoint_policy.EndpointPolicy()
            pb_resp = endpoint_policy.EndpointPolicy.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_endpoint_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_endpoint_policy_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = endpoint_policy.EndpointPolicy.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.networkservices_v1.NetworkServicesClient.get_endpoint_policy",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "GetEndpointPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetGateway(
        _BaseNetworkServicesRestTransport._BaseGetGateway, NetworkServicesRestStub
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.GetGateway")

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
            request: gateway.GetGatewayRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gateway.Gateway:
            r"""Call the get gateway method over HTTP.

            Args:
                request (~.gateway.GetGatewayRequest):
                    The request object. Request used by the GetGateway
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gateway.Gateway:
                    Gateway represents the configuration
                for a proxy, typically a load balancer.
                It captures the ip:port over which the
                services are exposed by the proxy, along
                with any policy configurations. Routes
                have reference to to Gateways to dictate
                how requests should be routed by this
                Gateway.

            """

            http_options = (
                _BaseNetworkServicesRestTransport._BaseGetGateway._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_gateway(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseGetGateway,
                    "_BaseGetGateway__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.GetGateway",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "GetGateway",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServicesRestTransport._GetGateway._get_response(
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
            resp = gateway.Gateway()
            pb_resp = gateway.Gateway.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_gateway(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_gateway_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gateway.Gateway.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.networkservices_v1.NetworkServicesClient.get_gateway",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "GetGateway",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetGatewayRouteView(
        _BaseNetworkServicesRestTransport._BaseGetGatewayRouteView,
        NetworkServicesRestStub,
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.GetGatewayRouteView")

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
            request: route_view.GetGatewayRouteViewRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> route_view.GatewayRouteView:
            r"""Call the get gateway route view method over HTTP.

            Args:
                request (~.route_view.GetGatewayRouteViewRequest):
                    The request object. Request used with the
                GetGatewayRouteView method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.route_view.GatewayRouteView:
                    GatewayRouteView defines view-only
                resource for Routes to a Gateway

            """

            http_options = _BaseNetworkServicesRestTransport._BaseGetGatewayRouteView._get_http_options()
            request, metadata = self._interceptor.pre_get_gateway_route_view(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseGetGatewayRouteView,
                    "_BaseGetGatewayRouteView__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.GetGatewayRouteView",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "GetGatewayRouteView",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServicesRestTransport._GetGatewayRouteView._get_response(
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
            resp = route_view.GatewayRouteView()
            pb_resp = route_view.GatewayRouteView.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_gateway_route_view(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_gateway_route_view_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = route_view.GatewayRouteView.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.networkservices_v1.NetworkServicesClient.get_gateway_route_view",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "GetGatewayRouteView",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetGrpcRoute(
        _BaseNetworkServicesRestTransport._BaseGetGrpcRoute, NetworkServicesRestStub
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.GetGrpcRoute")

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
            request: grpc_route.GetGrpcRouteRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> grpc_route.GrpcRoute:
            r"""Call the get grpc route method over HTTP.

            Args:
                request (~.grpc_route.GetGrpcRouteRequest):
                    The request object. Request used by the GetGrpcRoute
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.grpc_route.GrpcRoute:
                    GrpcRoute is the resource defining
                how gRPC traffic routed by a Mesh or
                Gateway resource is routed.

            """

            http_options = (
                _BaseNetworkServicesRestTransport._BaseGetGrpcRoute._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_grpc_route(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseGetGrpcRoute,
                    "_BaseGetGrpcRoute__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.GetGrpcRoute",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "GetGrpcRoute",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServicesRestTransport._GetGrpcRoute._get_response(
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
            resp = grpc_route.GrpcRoute()
            pb_resp = grpc_route.GrpcRoute.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_grpc_route(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_grpc_route_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = grpc_route.GrpcRoute.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.networkservices_v1.NetworkServicesClient.get_grpc_route",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "GetGrpcRoute",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetHttpRoute(
        _BaseNetworkServicesRestTransport._BaseGetHttpRoute, NetworkServicesRestStub
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.GetHttpRoute")

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
            request: http_route.GetHttpRouteRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> http_route.HttpRoute:
            r"""Call the get http route method over HTTP.

            Args:
                request (~.http_route.GetHttpRouteRequest):
                    The request object. Request used by the GetHttpRoute
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.http_route.HttpRoute:
                    HttpRoute is the resource defining
                how HTTP traffic should be routed by a
                Mesh or Gateway resource.

            """

            http_options = (
                _BaseNetworkServicesRestTransport._BaseGetHttpRoute._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_http_route(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseGetHttpRoute,
                    "_BaseGetHttpRoute__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.GetHttpRoute",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "GetHttpRoute",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServicesRestTransport._GetHttpRoute._get_response(
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
            resp = http_route.HttpRoute()
            pb_resp = http_route.HttpRoute.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_http_route(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_http_route_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = http_route.HttpRoute.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.networkservices_v1.NetworkServicesClient.get_http_route",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "GetHttpRoute",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetMesh(
        _BaseNetworkServicesRestTransport._BaseGetMesh, NetworkServicesRestStub
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.GetMesh")

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
            request: mesh.GetMeshRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> mesh.Mesh:
            r"""Call the get mesh method over HTTP.

            Args:
                request (~.mesh.GetMeshRequest):
                    The request object. Request used by the GetMesh method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.mesh.Mesh:
                    Mesh represents a logical
                configuration grouping for workload to
                workload communication within a service
                mesh. Routes that point to mesh dictate
                how requests are routed within this
                logical mesh boundary.

            """

            http_options = (
                _BaseNetworkServicesRestTransport._BaseGetMesh._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_mesh(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseGetMesh,
                    "_BaseGetMesh__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.GetMesh",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "GetMesh",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServicesRestTransport._GetMesh._get_response(
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
            resp = mesh.Mesh()
            pb_resp = mesh.Mesh.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_mesh(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_mesh_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = mesh.Mesh.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.networkservices_v1.NetworkServicesClient.get_mesh",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "GetMesh",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetMeshRouteView(
        _BaseNetworkServicesRestTransport._BaseGetMeshRouteView, NetworkServicesRestStub
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.GetMeshRouteView")

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
            request: route_view.GetMeshRouteViewRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> route_view.MeshRouteView:
            r"""Call the get mesh route view method over HTTP.

            Args:
                request (~.route_view.GetMeshRouteViewRequest):
                    The request object. Request used with the
                GetMeshRouteView method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.route_view.MeshRouteView:
                    MeshRouteView defines view-only
                resource for Routes to a Mesh

            """

            http_options = _BaseNetworkServicesRestTransport._BaseGetMeshRouteView._get_http_options()
            request, metadata = self._interceptor.pre_get_mesh_route_view(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseGetMeshRouteView,
                    "_BaseGetMeshRouteView__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.GetMeshRouteView",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "GetMeshRouteView",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServicesRestTransport._GetMeshRouteView._get_response(
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
            resp = route_view.MeshRouteView()
            pb_resp = route_view.MeshRouteView.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_mesh_route_view(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_mesh_route_view_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = route_view.MeshRouteView.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.networkservices_v1.NetworkServicesClient.get_mesh_route_view",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "GetMeshRouteView",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetServiceBinding(
        _BaseNetworkServicesRestTransport._BaseGetServiceBinding,
        NetworkServicesRestStub,
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.GetServiceBinding")

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
            request: service_binding.GetServiceBindingRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service_binding.ServiceBinding:
            r"""Call the get service binding method over HTTP.

            Args:
                request (~.service_binding.GetServiceBindingRequest):
                    The request object. Request used by the GetServiceBinding
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service_binding.ServiceBinding:
                    ServiceBinding can be used to:

                - Bind a Service Directory Service to be
                  used in a BackendService resource.
                  This feature will be deprecated soon.
                - Bind a Private Service Connect
                  producer service to be used in
                  consumer   Cloud Service Mesh or
                  Application Load Balancers.
                - Bind a Cloud Run service to be used in
                  consumer Cloud Service Mesh or
                  Application Load Balancers.

            """

            http_options = _BaseNetworkServicesRestTransport._BaseGetServiceBinding._get_http_options()
            request, metadata = self._interceptor.pre_get_service_binding(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseGetServiceBinding,
                    "_BaseGetServiceBinding__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.GetServiceBinding",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "GetServiceBinding",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServicesRestTransport._GetServiceBinding._get_response(
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
            resp = service_binding.ServiceBinding()
            pb_resp = service_binding.ServiceBinding.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_service_binding(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_service_binding_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service_binding.ServiceBinding.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.networkservices_v1.NetworkServicesClient.get_service_binding",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "GetServiceBinding",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetServiceLbPolicy(
        _BaseNetworkServicesRestTransport._BaseGetServiceLbPolicy,
        NetworkServicesRestStub,
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.GetServiceLbPolicy")

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
            request: service_lb_policy.GetServiceLbPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service_lb_policy.ServiceLbPolicy:
            r"""Call the get service lb policy method over HTTP.

            Args:
                request (~.service_lb_policy.GetServiceLbPolicyRequest):
                    The request object. Request used by the
                GetServiceLbPolicy method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service_lb_policy.ServiceLbPolicy:
                    ServiceLbPolicy holds global load
                balancing and traffic distribution
                configuration that can be applied to a
                BackendService.

            """

            http_options = _BaseNetworkServicesRestTransport._BaseGetServiceLbPolicy._get_http_options()
            request, metadata = self._interceptor.pre_get_service_lb_policy(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseGetServiceLbPolicy,
                    "_BaseGetServiceLbPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.GetServiceLbPolicy",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "GetServiceLbPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServicesRestTransport._GetServiceLbPolicy._get_response(
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
            resp = service_lb_policy.ServiceLbPolicy()
            pb_resp = service_lb_policy.ServiceLbPolicy.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_service_lb_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_service_lb_policy_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service_lb_policy.ServiceLbPolicy.to_json(
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
                    "Received response for google.cloud.networkservices_v1.NetworkServicesClient.get_service_lb_policy",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "GetServiceLbPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetTcpRoute(
        _BaseNetworkServicesRestTransport._BaseGetTcpRoute, NetworkServicesRestStub
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.GetTcpRoute")

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
            request: tcp_route.GetTcpRouteRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> tcp_route.TcpRoute:
            r"""Call the get tcp route method over HTTP.

            Args:
                request (~.tcp_route.GetTcpRouteRequest):
                    The request object. Request used by the GetTcpRoute
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.tcp_route.TcpRoute:
                    TcpRoute is the resource defining how
                TCP traffic should be routed by a
                Mesh/Gateway resource.

            """

            http_options = (
                _BaseNetworkServicesRestTransport._BaseGetTcpRoute._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_tcp_route(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseGetTcpRoute,
                    "_BaseGetTcpRoute__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.GetTcpRoute",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "GetTcpRoute",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServicesRestTransport._GetTcpRoute._get_response(
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
            resp = tcp_route.TcpRoute()
            pb_resp = tcp_route.TcpRoute.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_tcp_route(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_tcp_route_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = tcp_route.TcpRoute.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.networkservices_v1.NetworkServicesClient.get_tcp_route",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "GetTcpRoute",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetTlsRoute(
        _BaseNetworkServicesRestTransport._BaseGetTlsRoute, NetworkServicesRestStub
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.GetTlsRoute")

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
            request: tls_route.GetTlsRouteRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> tls_route.TlsRoute:
            r"""Call the get tls route method over HTTP.

            Args:
                request (~.tls_route.GetTlsRouteRequest):
                    The request object. Request used by the GetTlsRoute
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.tls_route.TlsRoute:
                    TlsRoute defines how traffic should
                be routed based on SNI and other
                matching L3 attributes.

            """

            http_options = (
                _BaseNetworkServicesRestTransport._BaseGetTlsRoute._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_tls_route(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseGetTlsRoute,
                    "_BaseGetTlsRoute__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.GetTlsRoute",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "GetTlsRoute",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServicesRestTransport._GetTlsRoute._get_response(
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
            resp = tls_route.TlsRoute()
            pb_resp = tls_route.TlsRoute.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_tls_route(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_tls_route_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = tls_route.TlsRoute.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.networkservices_v1.NetworkServicesClient.get_tls_route",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "GetTlsRoute",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetWasmPlugin(
        _BaseNetworkServicesRestTransport._BaseGetWasmPlugin, NetworkServicesRestStub
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.GetWasmPlugin")

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
            request: extensibility.GetWasmPluginRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> extensibility.WasmPlugin:
            r"""Call the get wasm plugin method over HTTP.

            Args:
                request (~.extensibility.GetWasmPluginRequest):
                    The request object. Request used by the ``GetWasmPlugin`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.extensibility.WasmPlugin:
                    ``WasmPlugin`` is a resource representing a service
                executing a customer-provided Wasm module.

            """

            http_options = (
                _BaseNetworkServicesRestTransport._BaseGetWasmPlugin._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_wasm_plugin(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseGetWasmPlugin,
                    "_BaseGetWasmPlugin__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.GetWasmPlugin",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "GetWasmPlugin",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServicesRestTransport._GetWasmPlugin._get_response(
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
            resp = extensibility.WasmPlugin()
            pb_resp = extensibility.WasmPlugin.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_wasm_plugin(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_wasm_plugin_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = extensibility.WasmPlugin.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.networkservices_v1.NetworkServicesClient.get_wasm_plugin",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "GetWasmPlugin",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetWasmPluginVersion(
        _BaseNetworkServicesRestTransport._BaseGetWasmPluginVersion,
        NetworkServicesRestStub,
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.GetWasmPluginVersion")

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
            request: extensibility.GetWasmPluginVersionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> extensibility.WasmPluginVersion:
            r"""Call the get wasm plugin version method over HTTP.

            Args:
                request (~.extensibility.GetWasmPluginVersionRequest):
                    The request object. Request used by the ``GetWasmPluginVersion`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.extensibility.WasmPluginVersion:
                    A single immutable version of a ``WasmPlugin`` resource.
                Defines the Wasm module used and optionally its runtime
                config.

            """

            http_options = _BaseNetworkServicesRestTransport._BaseGetWasmPluginVersion._get_http_options()
            request, metadata = self._interceptor.pre_get_wasm_plugin_version(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseGetWasmPluginVersion,
                    "_BaseGetWasmPluginVersion__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.GetWasmPluginVersion",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "GetWasmPluginVersion",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServicesRestTransport._GetWasmPluginVersion._get_response(
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
            resp = extensibility.WasmPluginVersion()
            pb_resp = extensibility.WasmPluginVersion.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_wasm_plugin_version(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_wasm_plugin_version_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = extensibility.WasmPluginVersion.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.networkservices_v1.NetworkServicesClient.get_wasm_plugin_version",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "GetWasmPluginVersion",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListAgentGateways(
        _BaseNetworkServicesRestTransport._BaseListAgentGateways,
        NetworkServicesRestStub,
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.ListAgentGateways")

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
            request: agent_gateway.ListAgentGatewaysRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> agent_gateway.ListAgentGatewaysResponse:
            r"""Call the list agent gateways method over HTTP.

            Args:
                request (~.agent_gateway.ListAgentGatewaysRequest):
                    The request object. Request used with the
                ListAgentGateways method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.agent_gateway.ListAgentGatewaysResponse:
                    Response returned by the
                ListAgentGateways method.

            """

            http_options = _BaseNetworkServicesRestTransport._BaseListAgentGateways._get_http_options()
            request, metadata = self._interceptor.pre_list_agent_gateways(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseListAgentGateways,
                    "_BaseListAgentGateways__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.ListAgentGateways",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "ListAgentGateways",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServicesRestTransport._ListAgentGateways._get_response(
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
            resp = agent_gateway.ListAgentGatewaysResponse()
            pb_resp = agent_gateway.ListAgentGatewaysResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_agent_gateways(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_agent_gateways_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = agent_gateway.ListAgentGatewaysResponse.to_json(
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
                    "Received response for google.cloud.networkservices_v1.NetworkServicesClient.list_agent_gateways",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "ListAgentGateways",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListEndpointPolicies(
        _BaseNetworkServicesRestTransport._BaseListEndpointPolicies,
        NetworkServicesRestStub,
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.ListEndpointPolicies")

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
            request: endpoint_policy.ListEndpointPoliciesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> endpoint_policy.ListEndpointPoliciesResponse:
            r"""Call the list endpoint policies method over HTTP.

            Args:
                request (~.endpoint_policy.ListEndpointPoliciesRequest):
                    The request object. Request used with the
                ListEndpointPolicies method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.endpoint_policy.ListEndpointPoliciesResponse:
                    Response returned by the
                ListEndpointPolicies method.

            """

            http_options = _BaseNetworkServicesRestTransport._BaseListEndpointPolicies._get_http_options()
            request, metadata = self._interceptor.pre_list_endpoint_policies(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseListEndpointPolicies,
                    "_BaseListEndpointPolicies__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.ListEndpointPolicies",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "ListEndpointPolicies",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServicesRestTransport._ListEndpointPolicies._get_response(
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
            resp = endpoint_policy.ListEndpointPoliciesResponse()
            pb_resp = endpoint_policy.ListEndpointPoliciesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_endpoint_policies(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_endpoint_policies_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        endpoint_policy.ListEndpointPoliciesResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.networkservices_v1.NetworkServicesClient.list_endpoint_policies",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "ListEndpointPolicies",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListGatewayRouteViews(
        _BaseNetworkServicesRestTransport._BaseListGatewayRouteViews,
        NetworkServicesRestStub,
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.ListGatewayRouteViews")

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
            request: route_view.ListGatewayRouteViewsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> route_view.ListGatewayRouteViewsResponse:
            r"""Call the list gateway route views method over HTTP.

            Args:
                request (~.route_view.ListGatewayRouteViewsRequest):
                    The request object. Request used with the
                ListGatewayRouteViews method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.route_view.ListGatewayRouteViewsResponse:
                    Response returned by the
                ListGatewayRouteViews method.

            """

            http_options = _BaseNetworkServicesRestTransport._BaseListGatewayRouteViews._get_http_options()
            request, metadata = self._interceptor.pre_list_gateway_route_views(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseListGatewayRouteViews,
                    "_BaseListGatewayRouteViews__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.ListGatewayRouteViews",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "ListGatewayRouteViews",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                NetworkServicesRestTransport._ListGatewayRouteViews._get_response(
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
            resp = route_view.ListGatewayRouteViewsResponse()
            pb_resp = route_view.ListGatewayRouteViewsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_gateway_route_views(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_gateway_route_views_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = route_view.ListGatewayRouteViewsResponse.to_json(
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
                    "Received response for google.cloud.networkservices_v1.NetworkServicesClient.list_gateway_route_views",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "ListGatewayRouteViews",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListGateways(
        _BaseNetworkServicesRestTransport._BaseListGateways, NetworkServicesRestStub
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.ListGateways")

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
            request: gateway.ListGatewaysRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gateway.ListGatewaysResponse:
            r"""Call the list gateways method over HTTP.

            Args:
                request (~.gateway.ListGatewaysRequest):
                    The request object. Request used with the ListGateways
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gateway.ListGatewaysResponse:
                    Response returned by the ListGateways
                method.

            """

            http_options = (
                _BaseNetworkServicesRestTransport._BaseListGateways._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_gateways(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseListGateways,
                    "_BaseListGateways__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.ListGateways",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "ListGateways",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServicesRestTransport._ListGateways._get_response(
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
            resp = gateway.ListGatewaysResponse()
            pb_resp = gateway.ListGatewaysResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_gateways(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_gateways_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gateway.ListGatewaysResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.networkservices_v1.NetworkServicesClient.list_gateways",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "ListGateways",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListGrpcRoutes(
        _BaseNetworkServicesRestTransport._BaseListGrpcRoutes, NetworkServicesRestStub
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.ListGrpcRoutes")

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
            request: grpc_route.ListGrpcRoutesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> grpc_route.ListGrpcRoutesResponse:
            r"""Call the list grpc routes method over HTTP.

            Args:
                request (~.grpc_route.ListGrpcRoutesRequest):
                    The request object. Request used with the ListGrpcRoutes
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.grpc_route.ListGrpcRoutesResponse:
                    Response returned by the
                ListGrpcRoutes method.

            """

            http_options = _BaseNetworkServicesRestTransport._BaseListGrpcRoutes._get_http_options()
            request, metadata = self._interceptor.pre_list_grpc_routes(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseListGrpcRoutes,
                    "_BaseListGrpcRoutes__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.ListGrpcRoutes",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "ListGrpcRoutes",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServicesRestTransport._ListGrpcRoutes._get_response(
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
            resp = grpc_route.ListGrpcRoutesResponse()
            pb_resp = grpc_route.ListGrpcRoutesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_grpc_routes(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_grpc_routes_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = grpc_route.ListGrpcRoutesResponse.to_json(
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
                    "Received response for google.cloud.networkservices_v1.NetworkServicesClient.list_grpc_routes",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "ListGrpcRoutes",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListHttpRoutes(
        _BaseNetworkServicesRestTransport._BaseListHttpRoutes, NetworkServicesRestStub
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.ListHttpRoutes")

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
            request: http_route.ListHttpRoutesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> http_route.ListHttpRoutesResponse:
            r"""Call the list http routes method over HTTP.

            Args:
                request (~.http_route.ListHttpRoutesRequest):
                    The request object. Request used with the ListHttpRoutes
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.http_route.ListHttpRoutesResponse:
                    Response returned by the
                ListHttpRoutes method.

            """

            http_options = _BaseNetworkServicesRestTransport._BaseListHttpRoutes._get_http_options()
            request, metadata = self._interceptor.pre_list_http_routes(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseListHttpRoutes,
                    "_BaseListHttpRoutes__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.ListHttpRoutes",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "ListHttpRoutes",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServicesRestTransport._ListHttpRoutes._get_response(
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
            resp = http_route.ListHttpRoutesResponse()
            pb_resp = http_route.ListHttpRoutesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_http_routes(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_http_routes_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = http_route.ListHttpRoutesResponse.to_json(
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
                    "Received response for google.cloud.networkservices_v1.NetworkServicesClient.list_http_routes",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "ListHttpRoutes",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListMeshes(
        _BaseNetworkServicesRestTransport._BaseListMeshes, NetworkServicesRestStub
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.ListMeshes")

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
            request: mesh.ListMeshesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> mesh.ListMeshesResponse:
            r"""Call the list meshes method over HTTP.

            Args:
                request (~.mesh.ListMeshesRequest):
                    The request object. Request used with the ListMeshes
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.mesh.ListMeshesResponse:
                    Response returned by the ListMeshes
                method.

            """

            http_options = (
                _BaseNetworkServicesRestTransport._BaseListMeshes._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_meshes(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseListMeshes,
                    "_BaseListMeshes__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.ListMeshes",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "ListMeshes",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServicesRestTransport._ListMeshes._get_response(
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
            resp = mesh.ListMeshesResponse()
            pb_resp = mesh.ListMeshesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_meshes(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_meshes_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = mesh.ListMeshesResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.networkservices_v1.NetworkServicesClient.list_meshes",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "ListMeshes",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListMeshRouteViews(
        _BaseNetworkServicesRestTransport._BaseListMeshRouteViews,
        NetworkServicesRestStub,
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.ListMeshRouteViews")

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
            request: route_view.ListMeshRouteViewsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> route_view.ListMeshRouteViewsResponse:
            r"""Call the list mesh route views method over HTTP.

            Args:
                request (~.route_view.ListMeshRouteViewsRequest):
                    The request object. Request used with the
                ListMeshRouteViews method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.route_view.ListMeshRouteViewsResponse:
                    Response returned by the
                ListMeshRouteViews method.

            """

            http_options = _BaseNetworkServicesRestTransport._BaseListMeshRouteViews._get_http_options()
            request, metadata = self._interceptor.pre_list_mesh_route_views(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseListMeshRouteViews,
                    "_BaseListMeshRouteViews__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.ListMeshRouteViews",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "ListMeshRouteViews",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServicesRestTransport._ListMeshRouteViews._get_response(
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
            resp = route_view.ListMeshRouteViewsResponse()
            pb_resp = route_view.ListMeshRouteViewsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_mesh_route_views(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_mesh_route_views_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = route_view.ListMeshRouteViewsResponse.to_json(
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
                    "Received response for google.cloud.networkservices_v1.NetworkServicesClient.list_mesh_route_views",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "ListMeshRouteViews",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListServiceBindings(
        _BaseNetworkServicesRestTransport._BaseListServiceBindings,
        NetworkServicesRestStub,
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.ListServiceBindings")

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
            request: service_binding.ListServiceBindingsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service_binding.ListServiceBindingsResponse:
            r"""Call the list service bindings method over HTTP.

            Args:
                request (~.service_binding.ListServiceBindingsRequest):
                    The request object. Request used with the
                ListServiceBindings method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service_binding.ListServiceBindingsResponse:
                    Response returned by the
                ListServiceBindings method.

            """

            http_options = _BaseNetworkServicesRestTransport._BaseListServiceBindings._get_http_options()
            request, metadata = self._interceptor.pre_list_service_bindings(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseListServiceBindings,
                    "_BaseListServiceBindings__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.ListServiceBindings",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "ListServiceBindings",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServicesRestTransport._ListServiceBindings._get_response(
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
            resp = service_binding.ListServiceBindingsResponse()
            pb_resp = service_binding.ListServiceBindingsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_service_bindings(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_service_bindings_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        service_binding.ListServiceBindingsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.networkservices_v1.NetworkServicesClient.list_service_bindings",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "ListServiceBindings",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListServiceLbPolicies(
        _BaseNetworkServicesRestTransport._BaseListServiceLbPolicies,
        NetworkServicesRestStub,
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.ListServiceLbPolicies")

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
            request: service_lb_policy.ListServiceLbPoliciesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service_lb_policy.ListServiceLbPoliciesResponse:
            r"""Call the list service lb policies method over HTTP.

            Args:
                request (~.service_lb_policy.ListServiceLbPoliciesRequest):
                    The request object. Request used with the
                ListServiceLbPolicies method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service_lb_policy.ListServiceLbPoliciesResponse:
                    Response returned by the
                ListServiceLbPolicies method.

            """

            http_options = _BaseNetworkServicesRestTransport._BaseListServiceLbPolicies._get_http_options()
            request, metadata = self._interceptor.pre_list_service_lb_policies(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseListServiceLbPolicies,
                    "_BaseListServiceLbPolicies__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.ListServiceLbPolicies",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "ListServiceLbPolicies",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                NetworkServicesRestTransport._ListServiceLbPolicies._get_response(
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
            resp = service_lb_policy.ListServiceLbPoliciesResponse()
            pb_resp = service_lb_policy.ListServiceLbPoliciesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_service_lb_policies(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_service_lb_policies_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        service_lb_policy.ListServiceLbPoliciesResponse.to_json(
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
                    "Received response for google.cloud.networkservices_v1.NetworkServicesClient.list_service_lb_policies",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "ListServiceLbPolicies",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListTcpRoutes(
        _BaseNetworkServicesRestTransport._BaseListTcpRoutes, NetworkServicesRestStub
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.ListTcpRoutes")

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
            request: tcp_route.ListTcpRoutesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> tcp_route.ListTcpRoutesResponse:
            r"""Call the list tcp routes method over HTTP.

            Args:
                request (~.tcp_route.ListTcpRoutesRequest):
                    The request object. Request used with the ListTcpRoutes
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.tcp_route.ListTcpRoutesResponse:
                    Response returned by the
                ListTcpRoutes method.

            """

            http_options = (
                _BaseNetworkServicesRestTransport._BaseListTcpRoutes._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_tcp_routes(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseListTcpRoutes,
                    "_BaseListTcpRoutes__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.ListTcpRoutes",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "ListTcpRoutes",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServicesRestTransport._ListTcpRoutes._get_response(
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
            resp = tcp_route.ListTcpRoutesResponse()
            pb_resp = tcp_route.ListTcpRoutesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_tcp_routes(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_tcp_routes_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = tcp_route.ListTcpRoutesResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.networkservices_v1.NetworkServicesClient.list_tcp_routes",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "ListTcpRoutes",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListTlsRoutes(
        _BaseNetworkServicesRestTransport._BaseListTlsRoutes, NetworkServicesRestStub
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.ListTlsRoutes")

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
            request: tls_route.ListTlsRoutesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> tls_route.ListTlsRoutesResponse:
            r"""Call the list tls routes method over HTTP.

            Args:
                request (~.tls_route.ListTlsRoutesRequest):
                    The request object. Request used with the ListTlsRoutes
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.tls_route.ListTlsRoutesResponse:
                    Response returned by the
                ListTlsRoutes method.

            """

            http_options = (
                _BaseNetworkServicesRestTransport._BaseListTlsRoutes._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_tls_routes(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseListTlsRoutes,
                    "_BaseListTlsRoutes__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.ListTlsRoutes",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "ListTlsRoutes",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServicesRestTransport._ListTlsRoutes._get_response(
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
            resp = tls_route.ListTlsRoutesResponse()
            pb_resp = tls_route.ListTlsRoutesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_tls_routes(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_tls_routes_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = tls_route.ListTlsRoutesResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.networkservices_v1.NetworkServicesClient.list_tls_routes",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "ListTlsRoutes",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListWasmPlugins(
        _BaseNetworkServicesRestTransport._BaseListWasmPlugins, NetworkServicesRestStub
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.ListWasmPlugins")

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
            request: extensibility.ListWasmPluginsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> extensibility.ListWasmPluginsResponse:
            r"""Call the list wasm plugins method over HTTP.

            Args:
                request (~.extensibility.ListWasmPluginsRequest):
                    The request object. Request used with the ``ListWasmPlugins`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.extensibility.ListWasmPluginsResponse:
                    Response returned by the ``ListWasmPlugins`` method.
            """

            http_options = _BaseNetworkServicesRestTransport._BaseListWasmPlugins._get_http_options()
            request, metadata = self._interceptor.pre_list_wasm_plugins(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseListWasmPlugins,
                    "_BaseListWasmPlugins__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.ListWasmPlugins",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "ListWasmPlugins",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServicesRestTransport._ListWasmPlugins._get_response(
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
            resp = extensibility.ListWasmPluginsResponse()
            pb_resp = extensibility.ListWasmPluginsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_wasm_plugins(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_wasm_plugins_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = extensibility.ListWasmPluginsResponse.to_json(
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
                    "Received response for google.cloud.networkservices_v1.NetworkServicesClient.list_wasm_plugins",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "ListWasmPlugins",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListWasmPluginVersions(
        _BaseNetworkServicesRestTransport._BaseListWasmPluginVersions,
        NetworkServicesRestStub,
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.ListWasmPluginVersions")

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
            request: extensibility.ListWasmPluginVersionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> extensibility.ListWasmPluginVersionsResponse:
            r"""Call the list wasm plugin versions method over HTTP.

            Args:
                request (~.extensibility.ListWasmPluginVersionsRequest):
                    The request object. Request used with the ``ListWasmPluginVersions`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.extensibility.ListWasmPluginVersionsResponse:
                    Response returned by the ``ListWasmPluginVersions``
                method.

            """

            http_options = _BaseNetworkServicesRestTransport._BaseListWasmPluginVersions._get_http_options()
            request, metadata = self._interceptor.pre_list_wasm_plugin_versions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseListWasmPluginVersions,
                    "_BaseListWasmPluginVersions__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.ListWasmPluginVersions",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "ListWasmPluginVersions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                NetworkServicesRestTransport._ListWasmPluginVersions._get_response(
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
            resp = extensibility.ListWasmPluginVersionsResponse()
            pb_resp = extensibility.ListWasmPluginVersionsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_wasm_plugin_versions(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_wasm_plugin_versions_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        extensibility.ListWasmPluginVersionsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.networkservices_v1.NetworkServicesClient.list_wasm_plugin_versions",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "ListWasmPluginVersions",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateAgentGateway(
        _BaseNetworkServicesRestTransport._BaseUpdateAgentGateway,
        NetworkServicesRestStub,
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.UpdateAgentGateway")

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
            request: gcn_agent_gateway.UpdateAgentGatewayRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update agent gateway method over HTTP.

            Args:
                request (~.gcn_agent_gateway.UpdateAgentGatewayRequest):
                    The request object. Request used by the
                UpdateAgentGateway method.
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

            http_options = _BaseNetworkServicesRestTransport._BaseUpdateAgentGateway._get_http_options()
            request, metadata = self._interceptor.pre_update_agent_gateway(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseUpdateAgentGateway,
                    "_BaseUpdateAgentGateway__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.UpdateAgentGateway",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "UpdateAgentGateway",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServicesRestTransport._UpdateAgentGateway._get_response(
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

            resp = self._interceptor.post_update_agent_gateway(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_agent_gateway_with_metadata(
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
                    "Received response for google.cloud.networkservices_v1.NetworkServicesClient.update_agent_gateway",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "UpdateAgentGateway",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateEndpointPolicy(
        _BaseNetworkServicesRestTransport._BaseUpdateEndpointPolicy,
        NetworkServicesRestStub,
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.UpdateEndpointPolicy")

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
            request: gcn_endpoint_policy.UpdateEndpointPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update endpoint policy method over HTTP.

            Args:
                request (~.gcn_endpoint_policy.UpdateEndpointPolicyRequest):
                    The request object. Request used with the
                UpdateEndpointPolicy method.
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

            http_options = _BaseNetworkServicesRestTransport._BaseUpdateEndpointPolicy._get_http_options()
            request, metadata = self._interceptor.pre_update_endpoint_policy(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseUpdateEndpointPolicy,
                    "_BaseUpdateEndpointPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.UpdateEndpointPolicy",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "UpdateEndpointPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServicesRestTransport._UpdateEndpointPolicy._get_response(
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

            resp = self._interceptor.post_update_endpoint_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_endpoint_policy_with_metadata(
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
                    "Received response for google.cloud.networkservices_v1.NetworkServicesClient.update_endpoint_policy",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "UpdateEndpointPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateGateway(
        _BaseNetworkServicesRestTransport._BaseUpdateGateway, NetworkServicesRestStub
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.UpdateGateway")

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
            request: gcn_gateway.UpdateGatewayRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update gateway method over HTTP.

            Args:
                request (~.gcn_gateway.UpdateGatewayRequest):
                    The request object. Request used by the UpdateGateway
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
                _BaseNetworkServicesRestTransport._BaseUpdateGateway._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_gateway(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseUpdateGateway,
                    "_BaseUpdateGateway__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.UpdateGateway",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "UpdateGateway",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServicesRestTransport._UpdateGateway._get_response(
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

            resp = self._interceptor.post_update_gateway(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_gateway_with_metadata(
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
                    "Received response for google.cloud.networkservices_v1.NetworkServicesClient.update_gateway",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "UpdateGateway",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateGrpcRoute(
        _BaseNetworkServicesRestTransport._BaseUpdateGrpcRoute, NetworkServicesRestStub
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.UpdateGrpcRoute")

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
            request: gcn_grpc_route.UpdateGrpcRouteRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update grpc route method over HTTP.

            Args:
                request (~.gcn_grpc_route.UpdateGrpcRouteRequest):
                    The request object. Request used by the UpdateGrpcRoute
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

            http_options = _BaseNetworkServicesRestTransport._BaseUpdateGrpcRoute._get_http_options()
            request, metadata = self._interceptor.pre_update_grpc_route(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseUpdateGrpcRoute,
                    "_BaseUpdateGrpcRoute__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.UpdateGrpcRoute",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "UpdateGrpcRoute",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServicesRestTransport._UpdateGrpcRoute._get_response(
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

            resp = self._interceptor.post_update_grpc_route(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_grpc_route_with_metadata(
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
                    "Received response for google.cloud.networkservices_v1.NetworkServicesClient.update_grpc_route",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "UpdateGrpcRoute",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateHttpRoute(
        _BaseNetworkServicesRestTransport._BaseUpdateHttpRoute, NetworkServicesRestStub
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.UpdateHttpRoute")

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
            request: gcn_http_route.UpdateHttpRouteRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update http route method over HTTP.

            Args:
                request (~.gcn_http_route.UpdateHttpRouteRequest):
                    The request object. Request used by the UpdateHttpRoute
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

            http_options = _BaseNetworkServicesRestTransport._BaseUpdateHttpRoute._get_http_options()
            request, metadata = self._interceptor.pre_update_http_route(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseUpdateHttpRoute,
                    "_BaseUpdateHttpRoute__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.UpdateHttpRoute",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "UpdateHttpRoute",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServicesRestTransport._UpdateHttpRoute._get_response(
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

            resp = self._interceptor.post_update_http_route(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_http_route_with_metadata(
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
                    "Received response for google.cloud.networkservices_v1.NetworkServicesClient.update_http_route",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "UpdateHttpRoute",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateMesh(
        _BaseNetworkServicesRestTransport._BaseUpdateMesh, NetworkServicesRestStub
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.UpdateMesh")

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
            request: gcn_mesh.UpdateMeshRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update mesh method over HTTP.

            Args:
                request (~.gcn_mesh.UpdateMeshRequest):
                    The request object. Request used by the UpdateMesh
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
                _BaseNetworkServicesRestTransport._BaseUpdateMesh._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_mesh(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseUpdateMesh,
                    "_BaseUpdateMesh__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.UpdateMesh",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "UpdateMesh",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServicesRestTransport._UpdateMesh._get_response(
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

            resp = self._interceptor.post_update_mesh(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_mesh_with_metadata(
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
                    "Received response for google.cloud.networkservices_v1.NetworkServicesClient.update_mesh",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "UpdateMesh",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateServiceBinding(
        _BaseNetworkServicesRestTransport._BaseUpdateServiceBinding,
        NetworkServicesRestStub,
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.UpdateServiceBinding")

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
            request: gcn_service_binding.UpdateServiceBindingRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update service binding method over HTTP.

            Args:
                request (~.gcn_service_binding.UpdateServiceBindingRequest):
                    The request object. Request used by the
                UpdateServiceBinding method.
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

            http_options = _BaseNetworkServicesRestTransport._BaseUpdateServiceBinding._get_http_options()
            request, metadata = self._interceptor.pre_update_service_binding(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseUpdateServiceBinding,
                    "_BaseUpdateServiceBinding__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.UpdateServiceBinding",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "UpdateServiceBinding",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServicesRestTransport._UpdateServiceBinding._get_response(
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

            resp = self._interceptor.post_update_service_binding(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_service_binding_with_metadata(
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
                    "Received response for google.cloud.networkservices_v1.NetworkServicesClient.update_service_binding",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "UpdateServiceBinding",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateServiceLbPolicy(
        _BaseNetworkServicesRestTransport._BaseUpdateServiceLbPolicy,
        NetworkServicesRestStub,
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.UpdateServiceLbPolicy")

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
            request: gcn_service_lb_policy.UpdateServiceLbPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update service lb policy method over HTTP.

            Args:
                request (~.gcn_service_lb_policy.UpdateServiceLbPolicyRequest):
                    The request object. Request used by the
                UpdateServiceLbPolicy method.
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

            http_options = _BaseNetworkServicesRestTransport._BaseUpdateServiceLbPolicy._get_http_options()
            request, metadata = self._interceptor.pre_update_service_lb_policy(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseUpdateServiceLbPolicy,
                    "_BaseUpdateServiceLbPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.UpdateServiceLbPolicy",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "UpdateServiceLbPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                NetworkServicesRestTransport._UpdateServiceLbPolicy._get_response(
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

            resp = self._interceptor.post_update_service_lb_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_service_lb_policy_with_metadata(
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
                    "Received response for google.cloud.networkservices_v1.NetworkServicesClient.update_service_lb_policy",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "UpdateServiceLbPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateTcpRoute(
        _BaseNetworkServicesRestTransport._BaseUpdateTcpRoute, NetworkServicesRestStub
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.UpdateTcpRoute")

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
            request: gcn_tcp_route.UpdateTcpRouteRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update tcp route method over HTTP.

            Args:
                request (~.gcn_tcp_route.UpdateTcpRouteRequest):
                    The request object. Request used by the UpdateTcpRoute
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

            http_options = _BaseNetworkServicesRestTransport._BaseUpdateTcpRoute._get_http_options()
            request, metadata = self._interceptor.pre_update_tcp_route(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseUpdateTcpRoute,
                    "_BaseUpdateTcpRoute__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.UpdateTcpRoute",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "UpdateTcpRoute",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServicesRestTransport._UpdateTcpRoute._get_response(
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

            resp = self._interceptor.post_update_tcp_route(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_tcp_route_with_metadata(
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
                    "Received response for google.cloud.networkservices_v1.NetworkServicesClient.update_tcp_route",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "UpdateTcpRoute",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateTlsRoute(
        _BaseNetworkServicesRestTransport._BaseUpdateTlsRoute, NetworkServicesRestStub
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.UpdateTlsRoute")

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
            request: gcn_tls_route.UpdateTlsRouteRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update tls route method over HTTP.

            Args:
                request (~.gcn_tls_route.UpdateTlsRouteRequest):
                    The request object. Request used by the UpdateTlsRoute
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

            http_options = _BaseNetworkServicesRestTransport._BaseUpdateTlsRoute._get_http_options()
            request, metadata = self._interceptor.pre_update_tls_route(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseUpdateTlsRoute,
                    "_BaseUpdateTlsRoute__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.UpdateTlsRoute",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "UpdateTlsRoute",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServicesRestTransport._UpdateTlsRoute._get_response(
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

            resp = self._interceptor.post_update_tls_route(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_tls_route_with_metadata(
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
                    "Received response for google.cloud.networkservices_v1.NetworkServicesClient.update_tls_route",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "UpdateTlsRoute",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateWasmPlugin(
        _BaseNetworkServicesRestTransport._BaseUpdateWasmPlugin, NetworkServicesRestStub
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.UpdateWasmPlugin")

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
            request: extensibility.UpdateWasmPluginRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update wasm plugin method over HTTP.

            Args:
                request (~.extensibility.UpdateWasmPluginRequest):
                    The request object. Request used by the ``UpdateWasmPlugin`` method.
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

            http_options = _BaseNetworkServicesRestTransport._BaseUpdateWasmPlugin._get_http_options()
            request, metadata = self._interceptor.pre_update_wasm_plugin(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseUpdateWasmPlugin,
                    "_BaseUpdateWasmPlugin__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.UpdateWasmPlugin",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "UpdateWasmPlugin",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServicesRestTransport._UpdateWasmPlugin._get_response(
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

            resp = self._interceptor.post_update_wasm_plugin(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_wasm_plugin_with_metadata(
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
                    "Received response for google.cloud.networkservices_v1.NetworkServicesClient.update_wasm_plugin",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "UpdateWasmPlugin",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_agent_gateway(
        self,
    ) -> Callable[
        [gcn_agent_gateway.CreateAgentGatewayRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateAgentGateway(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_endpoint_policy(
        self,
    ) -> Callable[
        [gcn_endpoint_policy.CreateEndpointPolicyRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateEndpointPolicy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_gateway(
        self,
    ) -> Callable[[gcn_gateway.CreateGatewayRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateGateway(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_grpc_route(
        self,
    ) -> Callable[[gcn_grpc_route.CreateGrpcRouteRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateGrpcRoute(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_http_route(
        self,
    ) -> Callable[[gcn_http_route.CreateHttpRouteRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateHttpRoute(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_mesh(
        self,
    ) -> Callable[[gcn_mesh.CreateMeshRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateMesh(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_service_binding(
        self,
    ) -> Callable[
        [gcn_service_binding.CreateServiceBindingRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateServiceBinding(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_service_lb_policy(
        self,
    ) -> Callable[
        [gcn_service_lb_policy.CreateServiceLbPolicyRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateServiceLbPolicy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_tcp_route(
        self,
    ) -> Callable[[gcn_tcp_route.CreateTcpRouteRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateTcpRoute(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_tls_route(
        self,
    ) -> Callable[[gcn_tls_route.CreateTlsRouteRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateTlsRoute(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_wasm_plugin(
        self,
    ) -> Callable[[extensibility.CreateWasmPluginRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateWasmPlugin(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_wasm_plugin_version(
        self,
    ) -> Callable[
        [extensibility.CreateWasmPluginVersionRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateWasmPluginVersion(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_agent_gateway(
        self,
    ) -> Callable[[agent_gateway.DeleteAgentGatewayRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteAgentGateway(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_endpoint_policy(
        self,
    ) -> Callable[
        [endpoint_policy.DeleteEndpointPolicyRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteEndpointPolicy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_gateway(
        self,
    ) -> Callable[[gateway.DeleteGatewayRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteGateway(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_grpc_route(
        self,
    ) -> Callable[[grpc_route.DeleteGrpcRouteRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteGrpcRoute(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_http_route(
        self,
    ) -> Callable[[http_route.DeleteHttpRouteRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteHttpRoute(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_mesh(
        self,
    ) -> Callable[[mesh.DeleteMeshRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteMesh(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_service_binding(
        self,
    ) -> Callable[
        [service_binding.DeleteServiceBindingRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteServiceBinding(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_service_lb_policy(
        self,
    ) -> Callable[
        [service_lb_policy.DeleteServiceLbPolicyRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteServiceLbPolicy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_tcp_route(
        self,
    ) -> Callable[[tcp_route.DeleteTcpRouteRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteTcpRoute(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_tls_route(
        self,
    ) -> Callable[[tls_route.DeleteTlsRouteRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteTlsRoute(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_wasm_plugin(
        self,
    ) -> Callable[[extensibility.DeleteWasmPluginRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteWasmPlugin(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_wasm_plugin_version(
        self,
    ) -> Callable[
        [extensibility.DeleteWasmPluginVersionRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteWasmPluginVersion(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_agent_gateway(
        self,
    ) -> Callable[[agent_gateway.GetAgentGatewayRequest], agent_gateway.AgentGateway]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetAgentGateway(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_endpoint_policy(
        self,
    ) -> Callable[
        [endpoint_policy.GetEndpointPolicyRequest], endpoint_policy.EndpointPolicy
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetEndpointPolicy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_gateway(self) -> Callable[[gateway.GetGatewayRequest], gateway.Gateway]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetGateway(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_gateway_route_view(
        self,
    ) -> Callable[[route_view.GetGatewayRouteViewRequest], route_view.GatewayRouteView]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetGatewayRouteView(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_grpc_route(
        self,
    ) -> Callable[[grpc_route.GetGrpcRouteRequest], grpc_route.GrpcRoute]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetGrpcRoute(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_http_route(
        self,
    ) -> Callable[[http_route.GetHttpRouteRequest], http_route.HttpRoute]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetHttpRoute(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_mesh(self) -> Callable[[mesh.GetMeshRequest], mesh.Mesh]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetMesh(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_mesh_route_view(
        self,
    ) -> Callable[[route_view.GetMeshRouteViewRequest], route_view.MeshRouteView]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetMeshRouteView(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_service_binding(
        self,
    ) -> Callable[
        [service_binding.GetServiceBindingRequest], service_binding.ServiceBinding
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetServiceBinding(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_service_lb_policy(
        self,
    ) -> Callable[
        [service_lb_policy.GetServiceLbPolicyRequest], service_lb_policy.ServiceLbPolicy
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetServiceLbPolicy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_tcp_route(
        self,
    ) -> Callable[[tcp_route.GetTcpRouteRequest], tcp_route.TcpRoute]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetTcpRoute(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_tls_route(
        self,
    ) -> Callable[[tls_route.GetTlsRouteRequest], tls_route.TlsRoute]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetTlsRoute(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_wasm_plugin(
        self,
    ) -> Callable[[extensibility.GetWasmPluginRequest], extensibility.WasmPlugin]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetWasmPlugin(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_wasm_plugin_version(
        self,
    ) -> Callable[
        [extensibility.GetWasmPluginVersionRequest], extensibility.WasmPluginVersion
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetWasmPluginVersion(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_agent_gateways(
        self,
    ) -> Callable[
        [agent_gateway.ListAgentGatewaysRequest],
        agent_gateway.ListAgentGatewaysResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListAgentGateways(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_endpoint_policies(
        self,
    ) -> Callable[
        [endpoint_policy.ListEndpointPoliciesRequest],
        endpoint_policy.ListEndpointPoliciesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListEndpointPolicies(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_gateway_route_views(
        self,
    ) -> Callable[
        [route_view.ListGatewayRouteViewsRequest],
        route_view.ListGatewayRouteViewsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListGatewayRouteViews(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_gateways(
        self,
    ) -> Callable[[gateway.ListGatewaysRequest], gateway.ListGatewaysResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListGateways(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_grpc_routes(
        self,
    ) -> Callable[
        [grpc_route.ListGrpcRoutesRequest], grpc_route.ListGrpcRoutesResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListGrpcRoutes(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_http_routes(
        self,
    ) -> Callable[
        [http_route.ListHttpRoutesRequest], http_route.ListHttpRoutesResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListHttpRoutes(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_meshes(
        self,
    ) -> Callable[[mesh.ListMeshesRequest], mesh.ListMeshesResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListMeshes(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_mesh_route_views(
        self,
    ) -> Callable[
        [route_view.ListMeshRouteViewsRequest], route_view.ListMeshRouteViewsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListMeshRouteViews(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_service_bindings(
        self,
    ) -> Callable[
        [service_binding.ListServiceBindingsRequest],
        service_binding.ListServiceBindingsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListServiceBindings(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_service_lb_policies(
        self,
    ) -> Callable[
        [service_lb_policy.ListServiceLbPoliciesRequest],
        service_lb_policy.ListServiceLbPoliciesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListServiceLbPolicies(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_tcp_routes(
        self,
    ) -> Callable[[tcp_route.ListTcpRoutesRequest], tcp_route.ListTcpRoutesResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListTcpRoutes(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_tls_routes(
        self,
    ) -> Callable[[tls_route.ListTlsRoutesRequest], tls_route.ListTlsRoutesResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListTlsRoutes(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_wasm_plugins(
        self,
    ) -> Callable[
        [extensibility.ListWasmPluginsRequest], extensibility.ListWasmPluginsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListWasmPlugins(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_wasm_plugin_versions(
        self,
    ) -> Callable[
        [extensibility.ListWasmPluginVersionsRequest],
        extensibility.ListWasmPluginVersionsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListWasmPluginVersions(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_agent_gateway(
        self,
    ) -> Callable[
        [gcn_agent_gateway.UpdateAgentGatewayRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateAgentGateway(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_endpoint_policy(
        self,
    ) -> Callable[
        [gcn_endpoint_policy.UpdateEndpointPolicyRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateEndpointPolicy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_gateway(
        self,
    ) -> Callable[[gcn_gateway.UpdateGatewayRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateGateway(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_grpc_route(
        self,
    ) -> Callable[[gcn_grpc_route.UpdateGrpcRouteRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateGrpcRoute(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_http_route(
        self,
    ) -> Callable[[gcn_http_route.UpdateHttpRouteRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateHttpRoute(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_mesh(
        self,
    ) -> Callable[[gcn_mesh.UpdateMeshRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateMesh(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_service_binding(
        self,
    ) -> Callable[
        [gcn_service_binding.UpdateServiceBindingRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateServiceBinding(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_service_lb_policy(
        self,
    ) -> Callable[
        [gcn_service_lb_policy.UpdateServiceLbPolicyRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateServiceLbPolicy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_tcp_route(
        self,
    ) -> Callable[[gcn_tcp_route.UpdateTcpRouteRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateTcpRoute(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_tls_route(
        self,
    ) -> Callable[[gcn_tls_route.UpdateTlsRouteRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateTlsRoute(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_wasm_plugin(
        self,
    ) -> Callable[[extensibility.UpdateWasmPluginRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateWasmPlugin(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(
        _BaseNetworkServicesRestTransport._BaseGetLocation, NetworkServicesRestStub
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.GetLocation")

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
                _BaseNetworkServicesRestTransport._BaseGetLocation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseGetLocation,
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServicesRestTransport._GetLocation._get_response(
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
                    "Received response for google.cloud.networkservices_v1.NetworkServicesAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
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
        _BaseNetworkServicesRestTransport._BaseListLocations, NetworkServicesRestStub
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.ListLocations")

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

            http_options = (
                _BaseNetworkServicesRestTransport._BaseListLocations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseListLocations,
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServicesRestTransport._ListLocations._get_response(
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
                    "Received response for google.cloud.networkservices_v1.NetworkServicesAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
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
        _BaseNetworkServicesRestTransport._BaseGetIamPolicy, NetworkServicesRestStub
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.GetIamPolicy")

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

            http_options = (
                _BaseNetworkServicesRestTransport._BaseGetIamPolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseGetIamPolicy,
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.GetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "GetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServicesRestTransport._GetIamPolicy._get_response(
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
                    "Received response for google.cloud.networkservices_v1.NetworkServicesAsyncClient.GetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
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
        _BaseNetworkServicesRestTransport._BaseSetIamPolicy, NetworkServicesRestStub
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.SetIamPolicy")

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

            http_options = (
                _BaseNetworkServicesRestTransport._BaseSetIamPolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_set_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseSetIamPolicy,
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.SetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "SetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServicesRestTransport._SetIamPolicy._get_response(
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
                    "Received response for google.cloud.networkservices_v1.NetworkServicesAsyncClient.SetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
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
        _BaseNetworkServicesRestTransport._BaseTestIamPermissions,
        NetworkServicesRestStub,
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.TestIamPermissions")

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

            http_options = _BaseNetworkServicesRestTransport._BaseTestIamPermissions._get_http_options()
            request, metadata = self._interceptor.pre_test_iam_permissions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseTestIamPermissions,
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.TestIamPermissions",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "TestIamPermissions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServicesRestTransport._TestIamPermissions._get_response(
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
                    "Received response for google.cloud.networkservices_v1.NetworkServicesAsyncClient.TestIamPermissions",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
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
        _BaseNetworkServicesRestTransport._BaseCancelOperation, NetworkServicesRestStub
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.CancelOperation")

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

            http_options = _BaseNetworkServicesRestTransport._BaseCancelOperation._get_http_options()
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServicesRestTransport._CancelOperation._get_response(
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
        _BaseNetworkServicesRestTransport._BaseDeleteOperation, NetworkServicesRestStub
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.DeleteOperation")

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

            http_options = _BaseNetworkServicesRestTransport._BaseDeleteOperation._get_http_options()
            request, metadata = self._interceptor.pre_delete_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseDeleteOperation,
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.DeleteOperation",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "DeleteOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServicesRestTransport._DeleteOperation._get_response(
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
        _BaseNetworkServicesRestTransport._BaseGetOperation, NetworkServicesRestStub
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.GetOperation")

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
                _BaseNetworkServicesRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServicesRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.networkservices_v1.NetworkServicesAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
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
        _BaseNetworkServicesRestTransport._BaseListOperations, NetworkServicesRestStub
    ):
        def __hash__(self):
            return hash("NetworkServicesRestTransport.ListOperations")

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

            http_options = _BaseNetworkServicesRestTransport._BaseListOperations._get_http_options()
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServicesRestTransport._BaseListOperations,
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
                    f"Sending request for google.cloud.networkservices_v1.NetworkServicesClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServicesRestTransport._ListOperations._get_response(
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
                    "Received response for google.cloud.networkservices_v1.NetworkServicesAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.networkservices.v1.NetworkServices",
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


__all__ = ("NetworkServicesRestTransport",)
