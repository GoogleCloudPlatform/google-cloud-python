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
from google.api_core import gapic_v1, rest_helpers, rest_streaming
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.requests import AuthorizedSession  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.compute_v1._compat import transcode_request
from google.cloud.compute_v1.types import compute

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseRoutersRestTransport

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


class RoutersRestInterceptor:
    """Interceptor for Routers.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the RoutersRestTransport.

    .. code-block:: python
        class MyCustomRoutersInterceptor(RoutersRestInterceptor):
            def pre_aggregated_list(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_aggregated_list(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_named_set(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_named_set(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_route_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_route_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_named_set(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_named_set(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_nat_ip_info(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_nat_ip_info(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_nat_mapping_info(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_nat_mapping_info(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_route_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_route_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_router_status(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_router_status(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_insert(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_insert(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_bgp_routes(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_bgp_routes(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_named_sets(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_named_sets(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_route_policies(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_route_policies(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_patch(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_patch(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_patch_named_set(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_patch_named_set(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_patch_route_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_patch_route_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_preview(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_preview(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_named_set(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_named_set(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_route_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_route_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = RoutersRestTransport(interceptor=MyCustomRoutersInterceptor())
        client = RoutersClient(transport=transport)


    """

    def pre_aggregated_list(
        self,
        request: compute.AggregatedListRoutersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.AggregatedListRoutersRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for aggregated_list

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Routers server.
        """
        return request, metadata

    def post_aggregated_list(
        self, response: compute.RouterAggregatedList
    ) -> compute.RouterAggregatedList:
        """Post-rpc interceptor for aggregated_list

        DEPRECATED. Please use the `post_aggregated_list_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Routers server but before
        it is returned to user code. This `post_aggregated_list` interceptor runs
        before the `post_aggregated_list_with_metadata` interceptor.
        """
        return response

    def post_aggregated_list_with_metadata(
        self,
        response: compute.RouterAggregatedList,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.RouterAggregatedList, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for aggregated_list

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Routers server but before it is returned to user code.

        We recommend only using this `post_aggregated_list_with_metadata`
        interceptor in new development instead of the `post_aggregated_list` interceptor.
        When both interceptors are used, this `post_aggregated_list_with_metadata` interceptor runs after the
        `post_aggregated_list` interceptor. The (possibly modified) response returned by
        `post_aggregated_list` will be passed to
        `post_aggregated_list_with_metadata`.
        """
        return response, metadata

    def pre_delete(
        self,
        request: compute.DeleteRouterRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.DeleteRouterRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Routers server.
        """
        return request, metadata

    def post_delete(self, response: compute.Operation) -> compute.Operation:
        """Post-rpc interceptor for delete

        DEPRECATED. Please use the `post_delete_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Routers server but before
        it is returned to user code. This `post_delete` interceptor runs
        before the `post_delete_with_metadata` interceptor.
        """
        return response

    def post_delete_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Routers server but before it is returned to user code.

        We recommend only using this `post_delete_with_metadata`
        interceptor in new development instead of the `post_delete` interceptor.
        When both interceptors are used, this `post_delete_with_metadata` interceptor runs after the
        `post_delete` interceptor. The (possibly modified) response returned by
        `post_delete` will be passed to
        `post_delete_with_metadata`.
        """
        return response, metadata

    def pre_delete_named_set(
        self,
        request: compute.DeleteNamedSetRouterRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.DeleteNamedSetRouterRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_named_set

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Routers server.
        """
        return request, metadata

    def post_delete_named_set(self, response: compute.Operation) -> compute.Operation:
        """Post-rpc interceptor for delete_named_set

        DEPRECATED. Please use the `post_delete_named_set_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Routers server but before
        it is returned to user code. This `post_delete_named_set` interceptor runs
        before the `post_delete_named_set_with_metadata` interceptor.
        """
        return response

    def post_delete_named_set_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_named_set

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Routers server but before it is returned to user code.

        We recommend only using this `post_delete_named_set_with_metadata`
        interceptor in new development instead of the `post_delete_named_set` interceptor.
        When both interceptors are used, this `post_delete_named_set_with_metadata` interceptor runs after the
        `post_delete_named_set` interceptor. The (possibly modified) response returned by
        `post_delete_named_set` will be passed to
        `post_delete_named_set_with_metadata`.
        """
        return response, metadata

    def pre_delete_route_policy(
        self,
        request: compute.DeleteRoutePolicyRouterRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.DeleteRoutePolicyRouterRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_route_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Routers server.
        """
        return request, metadata

    def post_delete_route_policy(
        self, response: compute.Operation
    ) -> compute.Operation:
        """Post-rpc interceptor for delete_route_policy

        DEPRECATED. Please use the `post_delete_route_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Routers server but before
        it is returned to user code. This `post_delete_route_policy` interceptor runs
        before the `post_delete_route_policy_with_metadata` interceptor.
        """
        return response

    def post_delete_route_policy_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_route_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Routers server but before it is returned to user code.

        We recommend only using this `post_delete_route_policy_with_metadata`
        interceptor in new development instead of the `post_delete_route_policy` interceptor.
        When both interceptors are used, this `post_delete_route_policy_with_metadata` interceptor runs after the
        `post_delete_route_policy` interceptor. The (possibly modified) response returned by
        `post_delete_route_policy` will be passed to
        `post_delete_route_policy_with_metadata`.
        """
        return response, metadata

    def pre_get(
        self,
        request: compute.GetRouterRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.GetRouterRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Routers server.
        """
        return request, metadata

    def post_get(self, response: compute.Router) -> compute.Router:
        """Post-rpc interceptor for get

        DEPRECATED. Please use the `post_get_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Routers server but before
        it is returned to user code. This `post_get` interceptor runs
        before the `post_get_with_metadata` interceptor.
        """
        return response

    def post_get_with_metadata(
        self,
        response: compute.Router,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Router, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Routers server but before it is returned to user code.

        We recommend only using this `post_get_with_metadata`
        interceptor in new development instead of the `post_get` interceptor.
        When both interceptors are used, this `post_get_with_metadata` interceptor runs after the
        `post_get` interceptor. The (possibly modified) response returned by
        `post_get` will be passed to
        `post_get_with_metadata`.
        """
        return response, metadata

    def pre_get_named_set(
        self,
        request: compute.GetNamedSetRouterRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.GetNamedSetRouterRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_named_set

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Routers server.
        """
        return request, metadata

    def post_get_named_set(
        self, response: compute.RoutersGetNamedSetResponse
    ) -> compute.RoutersGetNamedSetResponse:
        """Post-rpc interceptor for get_named_set

        DEPRECATED. Please use the `post_get_named_set_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Routers server but before
        it is returned to user code. This `post_get_named_set` interceptor runs
        before the `post_get_named_set_with_metadata` interceptor.
        """
        return response

    def post_get_named_set_with_metadata(
        self,
        response: compute.RoutersGetNamedSetResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.RoutersGetNamedSetResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_named_set

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Routers server but before it is returned to user code.

        We recommend only using this `post_get_named_set_with_metadata`
        interceptor in new development instead of the `post_get_named_set` interceptor.
        When both interceptors are used, this `post_get_named_set_with_metadata` interceptor runs after the
        `post_get_named_set` interceptor. The (possibly modified) response returned by
        `post_get_named_set` will be passed to
        `post_get_named_set_with_metadata`.
        """
        return response, metadata

    def pre_get_nat_ip_info(
        self,
        request: compute.GetNatIpInfoRouterRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.GetNatIpInfoRouterRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_nat_ip_info

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Routers server.
        """
        return request, metadata

    def post_get_nat_ip_info(
        self, response: compute.NatIpInfoResponse
    ) -> compute.NatIpInfoResponse:
        """Post-rpc interceptor for get_nat_ip_info

        DEPRECATED. Please use the `post_get_nat_ip_info_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Routers server but before
        it is returned to user code. This `post_get_nat_ip_info` interceptor runs
        before the `post_get_nat_ip_info_with_metadata` interceptor.
        """
        return response

    def post_get_nat_ip_info_with_metadata(
        self,
        response: compute.NatIpInfoResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.NatIpInfoResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_nat_ip_info

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Routers server but before it is returned to user code.

        We recommend only using this `post_get_nat_ip_info_with_metadata`
        interceptor in new development instead of the `post_get_nat_ip_info` interceptor.
        When both interceptors are used, this `post_get_nat_ip_info_with_metadata` interceptor runs after the
        `post_get_nat_ip_info` interceptor. The (possibly modified) response returned by
        `post_get_nat_ip_info` will be passed to
        `post_get_nat_ip_info_with_metadata`.
        """
        return response, metadata

    def pre_get_nat_mapping_info(
        self,
        request: compute.GetNatMappingInfoRoutersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.GetNatMappingInfoRoutersRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_nat_mapping_info

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Routers server.
        """
        return request, metadata

    def post_get_nat_mapping_info(
        self, response: compute.VmEndpointNatMappingsList
    ) -> compute.VmEndpointNatMappingsList:
        """Post-rpc interceptor for get_nat_mapping_info

        DEPRECATED. Please use the `post_get_nat_mapping_info_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Routers server but before
        it is returned to user code. This `post_get_nat_mapping_info` interceptor runs
        before the `post_get_nat_mapping_info_with_metadata` interceptor.
        """
        return response

    def post_get_nat_mapping_info_with_metadata(
        self,
        response: compute.VmEndpointNatMappingsList,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.VmEndpointNatMappingsList, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_nat_mapping_info

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Routers server but before it is returned to user code.

        We recommend only using this `post_get_nat_mapping_info_with_metadata`
        interceptor in new development instead of the `post_get_nat_mapping_info` interceptor.
        When both interceptors are used, this `post_get_nat_mapping_info_with_metadata` interceptor runs after the
        `post_get_nat_mapping_info` interceptor. The (possibly modified) response returned by
        `post_get_nat_mapping_info` will be passed to
        `post_get_nat_mapping_info_with_metadata`.
        """
        return response, metadata

    def pre_get_route_policy(
        self,
        request: compute.GetRoutePolicyRouterRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.GetRoutePolicyRouterRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_route_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Routers server.
        """
        return request, metadata

    def post_get_route_policy(
        self, response: compute.RoutersGetRoutePolicyResponse
    ) -> compute.RoutersGetRoutePolicyResponse:
        """Post-rpc interceptor for get_route_policy

        DEPRECATED. Please use the `post_get_route_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Routers server but before
        it is returned to user code. This `post_get_route_policy` interceptor runs
        before the `post_get_route_policy_with_metadata` interceptor.
        """
        return response

    def post_get_route_policy_with_metadata(
        self,
        response: compute.RoutersGetRoutePolicyResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.RoutersGetRoutePolicyResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_route_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Routers server but before it is returned to user code.

        We recommend only using this `post_get_route_policy_with_metadata`
        interceptor in new development instead of the `post_get_route_policy` interceptor.
        When both interceptors are used, this `post_get_route_policy_with_metadata` interceptor runs after the
        `post_get_route_policy` interceptor. The (possibly modified) response returned by
        `post_get_route_policy` will be passed to
        `post_get_route_policy_with_metadata`.
        """
        return response, metadata

    def pre_get_router_status(
        self,
        request: compute.GetRouterStatusRouterRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.GetRouterStatusRouterRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_router_status

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Routers server.
        """
        return request, metadata

    def post_get_router_status(
        self, response: compute.RouterStatusResponse
    ) -> compute.RouterStatusResponse:
        """Post-rpc interceptor for get_router_status

        DEPRECATED. Please use the `post_get_router_status_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Routers server but before
        it is returned to user code. This `post_get_router_status` interceptor runs
        before the `post_get_router_status_with_metadata` interceptor.
        """
        return response

    def post_get_router_status_with_metadata(
        self,
        response: compute.RouterStatusResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.RouterStatusResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_router_status

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Routers server but before it is returned to user code.

        We recommend only using this `post_get_router_status_with_metadata`
        interceptor in new development instead of the `post_get_router_status` interceptor.
        When both interceptors are used, this `post_get_router_status_with_metadata` interceptor runs after the
        `post_get_router_status` interceptor. The (possibly modified) response returned by
        `post_get_router_status` will be passed to
        `post_get_router_status_with_metadata`.
        """
        return response, metadata

    def pre_insert(
        self,
        request: compute.InsertRouterRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.InsertRouterRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for insert

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Routers server.
        """
        return request, metadata

    def post_insert(self, response: compute.Operation) -> compute.Operation:
        """Post-rpc interceptor for insert

        DEPRECATED. Please use the `post_insert_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Routers server but before
        it is returned to user code. This `post_insert` interceptor runs
        before the `post_insert_with_metadata` interceptor.
        """
        return response

    def post_insert_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for insert

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Routers server but before it is returned to user code.

        We recommend only using this `post_insert_with_metadata`
        interceptor in new development instead of the `post_insert` interceptor.
        When both interceptors are used, this `post_insert_with_metadata` interceptor runs after the
        `post_insert` interceptor. The (possibly modified) response returned by
        `post_insert` will be passed to
        `post_insert_with_metadata`.
        """
        return response, metadata

    def pre_list(
        self,
        request: compute.ListRoutersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.ListRoutersRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Routers server.
        """
        return request, metadata

    def post_list(self, response: compute.RouterList) -> compute.RouterList:
        """Post-rpc interceptor for list

        DEPRECATED. Please use the `post_list_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Routers server but before
        it is returned to user code. This `post_list` interceptor runs
        before the `post_list_with_metadata` interceptor.
        """
        return response

    def post_list_with_metadata(
        self,
        response: compute.RouterList,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.RouterList, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Routers server but before it is returned to user code.

        We recommend only using this `post_list_with_metadata`
        interceptor in new development instead of the `post_list` interceptor.
        When both interceptors are used, this `post_list_with_metadata` interceptor runs after the
        `post_list` interceptor. The (possibly modified) response returned by
        `post_list` will be passed to
        `post_list_with_metadata`.
        """
        return response, metadata

    def pre_list_bgp_routes(
        self,
        request: compute.ListBgpRoutesRoutersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.ListBgpRoutesRoutersRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_bgp_routes

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Routers server.
        """
        return request, metadata

    def post_list_bgp_routes(
        self, response: compute.RoutersListBgpRoutes
    ) -> compute.RoutersListBgpRoutes:
        """Post-rpc interceptor for list_bgp_routes

        DEPRECATED. Please use the `post_list_bgp_routes_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Routers server but before
        it is returned to user code. This `post_list_bgp_routes` interceptor runs
        before the `post_list_bgp_routes_with_metadata` interceptor.
        """
        return response

    def post_list_bgp_routes_with_metadata(
        self,
        response: compute.RoutersListBgpRoutes,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.RoutersListBgpRoutes, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_bgp_routes

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Routers server but before it is returned to user code.

        We recommend only using this `post_list_bgp_routes_with_metadata`
        interceptor in new development instead of the `post_list_bgp_routes` interceptor.
        When both interceptors are used, this `post_list_bgp_routes_with_metadata` interceptor runs after the
        `post_list_bgp_routes` interceptor. The (possibly modified) response returned by
        `post_list_bgp_routes` will be passed to
        `post_list_bgp_routes_with_metadata`.
        """
        return response, metadata

    def pre_list_named_sets(
        self,
        request: compute.ListNamedSetsRoutersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.ListNamedSetsRoutersRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_named_sets

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Routers server.
        """
        return request, metadata

    def post_list_named_sets(
        self, response: compute.RoutersListNamedSets
    ) -> compute.RoutersListNamedSets:
        """Post-rpc interceptor for list_named_sets

        DEPRECATED. Please use the `post_list_named_sets_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Routers server but before
        it is returned to user code. This `post_list_named_sets` interceptor runs
        before the `post_list_named_sets_with_metadata` interceptor.
        """
        return response

    def post_list_named_sets_with_metadata(
        self,
        response: compute.RoutersListNamedSets,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.RoutersListNamedSets, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_named_sets

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Routers server but before it is returned to user code.

        We recommend only using this `post_list_named_sets_with_metadata`
        interceptor in new development instead of the `post_list_named_sets` interceptor.
        When both interceptors are used, this `post_list_named_sets_with_metadata` interceptor runs after the
        `post_list_named_sets` interceptor. The (possibly modified) response returned by
        `post_list_named_sets` will be passed to
        `post_list_named_sets_with_metadata`.
        """
        return response, metadata

    def pre_list_route_policies(
        self,
        request: compute.ListRoutePoliciesRoutersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.ListRoutePoliciesRoutersRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_route_policies

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Routers server.
        """
        return request, metadata

    def post_list_route_policies(
        self, response: compute.RoutersListRoutePolicies
    ) -> compute.RoutersListRoutePolicies:
        """Post-rpc interceptor for list_route_policies

        DEPRECATED. Please use the `post_list_route_policies_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Routers server but before
        it is returned to user code. This `post_list_route_policies` interceptor runs
        before the `post_list_route_policies_with_metadata` interceptor.
        """
        return response

    def post_list_route_policies_with_metadata(
        self,
        response: compute.RoutersListRoutePolicies,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.RoutersListRoutePolicies, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_route_policies

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Routers server but before it is returned to user code.

        We recommend only using this `post_list_route_policies_with_metadata`
        interceptor in new development instead of the `post_list_route_policies` interceptor.
        When both interceptors are used, this `post_list_route_policies_with_metadata` interceptor runs after the
        `post_list_route_policies` interceptor. The (possibly modified) response returned by
        `post_list_route_policies` will be passed to
        `post_list_route_policies_with_metadata`.
        """
        return response, metadata

    def pre_patch(
        self,
        request: compute.PatchRouterRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.PatchRouterRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for patch

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Routers server.
        """
        return request, metadata

    def post_patch(self, response: compute.Operation) -> compute.Operation:
        """Post-rpc interceptor for patch

        DEPRECATED. Please use the `post_patch_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Routers server but before
        it is returned to user code. This `post_patch` interceptor runs
        before the `post_patch_with_metadata` interceptor.
        """
        return response

    def post_patch_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for patch

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Routers server but before it is returned to user code.

        We recommend only using this `post_patch_with_metadata`
        interceptor in new development instead of the `post_patch` interceptor.
        When both interceptors are used, this `post_patch_with_metadata` interceptor runs after the
        `post_patch` interceptor. The (possibly modified) response returned by
        `post_patch` will be passed to
        `post_patch_with_metadata`.
        """
        return response, metadata

    def pre_patch_named_set(
        self,
        request: compute.PatchNamedSetRouterRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.PatchNamedSetRouterRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for patch_named_set

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Routers server.
        """
        return request, metadata

    def post_patch_named_set(self, response: compute.Operation) -> compute.Operation:
        """Post-rpc interceptor for patch_named_set

        DEPRECATED. Please use the `post_patch_named_set_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Routers server but before
        it is returned to user code. This `post_patch_named_set` interceptor runs
        before the `post_patch_named_set_with_metadata` interceptor.
        """
        return response

    def post_patch_named_set_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for patch_named_set

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Routers server but before it is returned to user code.

        We recommend only using this `post_patch_named_set_with_metadata`
        interceptor in new development instead of the `post_patch_named_set` interceptor.
        When both interceptors are used, this `post_patch_named_set_with_metadata` interceptor runs after the
        `post_patch_named_set` interceptor. The (possibly modified) response returned by
        `post_patch_named_set` will be passed to
        `post_patch_named_set_with_metadata`.
        """
        return response, metadata

    def pre_patch_route_policy(
        self,
        request: compute.PatchRoutePolicyRouterRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.PatchRoutePolicyRouterRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for patch_route_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Routers server.
        """
        return request, metadata

    def post_patch_route_policy(self, response: compute.Operation) -> compute.Operation:
        """Post-rpc interceptor for patch_route_policy

        DEPRECATED. Please use the `post_patch_route_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Routers server but before
        it is returned to user code. This `post_patch_route_policy` interceptor runs
        before the `post_patch_route_policy_with_metadata` interceptor.
        """
        return response

    def post_patch_route_policy_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for patch_route_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Routers server but before it is returned to user code.

        We recommend only using this `post_patch_route_policy_with_metadata`
        interceptor in new development instead of the `post_patch_route_policy` interceptor.
        When both interceptors are used, this `post_patch_route_policy_with_metadata` interceptor runs after the
        `post_patch_route_policy` interceptor. The (possibly modified) response returned by
        `post_patch_route_policy` will be passed to
        `post_patch_route_policy_with_metadata`.
        """
        return response, metadata

    def pre_preview(
        self,
        request: compute.PreviewRouterRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.PreviewRouterRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for preview

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Routers server.
        """
        return request, metadata

    def post_preview(
        self, response: compute.RoutersPreviewResponse
    ) -> compute.RoutersPreviewResponse:
        """Post-rpc interceptor for preview

        DEPRECATED. Please use the `post_preview_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Routers server but before
        it is returned to user code. This `post_preview` interceptor runs
        before the `post_preview_with_metadata` interceptor.
        """
        return response

    def post_preview_with_metadata(
        self,
        response: compute.RoutersPreviewResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.RoutersPreviewResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for preview

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Routers server but before it is returned to user code.

        We recommend only using this `post_preview_with_metadata`
        interceptor in new development instead of the `post_preview` interceptor.
        When both interceptors are used, this `post_preview_with_metadata` interceptor runs after the
        `post_preview` interceptor. The (possibly modified) response returned by
        `post_preview` will be passed to
        `post_preview_with_metadata`.
        """
        return response, metadata

    def pre_update(
        self,
        request: compute.UpdateRouterRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.UpdateRouterRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for update

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Routers server.
        """
        return request, metadata

    def post_update(self, response: compute.Operation) -> compute.Operation:
        """Post-rpc interceptor for update

        DEPRECATED. Please use the `post_update_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Routers server but before
        it is returned to user code. This `post_update` interceptor runs
        before the `post_update_with_metadata` interceptor.
        """
        return response

    def post_update_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Routers server but before it is returned to user code.

        We recommend only using this `post_update_with_metadata`
        interceptor in new development instead of the `post_update` interceptor.
        When both interceptors are used, this `post_update_with_metadata` interceptor runs after the
        `post_update` interceptor. The (possibly modified) response returned by
        `post_update` will be passed to
        `post_update_with_metadata`.
        """
        return response, metadata

    def pre_update_named_set(
        self,
        request: compute.UpdateNamedSetRouterRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.UpdateNamedSetRouterRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_named_set

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Routers server.
        """
        return request, metadata

    def post_update_named_set(self, response: compute.Operation) -> compute.Operation:
        """Post-rpc interceptor for update_named_set

        DEPRECATED. Please use the `post_update_named_set_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Routers server but before
        it is returned to user code. This `post_update_named_set` interceptor runs
        before the `post_update_named_set_with_metadata` interceptor.
        """
        return response

    def post_update_named_set_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_named_set

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Routers server but before it is returned to user code.

        We recommend only using this `post_update_named_set_with_metadata`
        interceptor in new development instead of the `post_update_named_set` interceptor.
        When both interceptors are used, this `post_update_named_set_with_metadata` interceptor runs after the
        `post_update_named_set` interceptor. The (possibly modified) response returned by
        `post_update_named_set` will be passed to
        `post_update_named_set_with_metadata`.
        """
        return response, metadata

    def pre_update_route_policy(
        self,
        request: compute.UpdateRoutePolicyRouterRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.UpdateRoutePolicyRouterRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_route_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Routers server.
        """
        return request, metadata

    def post_update_route_policy(
        self, response: compute.Operation
    ) -> compute.Operation:
        """Post-rpc interceptor for update_route_policy

        DEPRECATED. Please use the `post_update_route_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Routers server but before
        it is returned to user code. This `post_update_route_policy` interceptor runs
        before the `post_update_route_policy_with_metadata` interceptor.
        """
        return response

    def post_update_route_policy_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_route_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Routers server but before it is returned to user code.

        We recommend only using this `post_update_route_policy_with_metadata`
        interceptor in new development instead of the `post_update_route_policy` interceptor.
        When both interceptors are used, this `post_update_route_policy_with_metadata` interceptor runs after the
        `post_update_route_policy` interceptor. The (possibly modified) response returned by
        `post_update_route_policy` will be passed to
        `post_update_route_policy_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class RoutersRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: RoutersRestInterceptor


class RoutersRestTransport(_BaseRoutersRestTransport):
    """REST backend synchronous transport for Routers.

    The Routers API.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "compute.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[RoutersRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        NOTE: This REST transport functionality is currently in a beta
        state (preview). We welcome your feedback via a GitHub issue in
        this library's repository. Thank you!

         Args:
             host (Optional[str]):
                  The hostname to connect to (default: 'compute.googleapis.com').
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
             interceptor (Optional[RoutersRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or RoutersRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _AggregatedList(
        _BaseRoutersRestTransport._BaseAggregatedList, RoutersRestStub
    ):
        def __hash__(self):
            return hash("RoutersRestTransport.AggregatedList")

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
            request: compute.AggregatedListRoutersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.RouterAggregatedList:
            r"""Call the aggregated list method over HTTP.

            Args:
                request (~.compute.AggregatedListRoutersRequest):
                    The request object. A request message for
                Routers.AggregatedList. See the method
                description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.RouterAggregatedList:
                    Contains a list of routers.
            """

            http_options = (
                _BaseRoutersRestTransport._BaseAggregatedList._get_http_options()
            )
            request, metadata = self._interceptor.pre_aggregated_list(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRoutersRestTransport._BaseAggregatedList,
                    "_BaseAggregatedList__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.compute_v1.RoutersClient.AggregatedList",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Routers",
                        "rpcName": "AggregatedList",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RoutersRestTransport._AggregatedList._get_response(
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
            resp = compute.RouterAggregatedList()
            pb_resp = compute.RouterAggregatedList.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_aggregated_list(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_aggregated_list_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.RouterAggregatedList.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.RoutersClient.aggregated_list",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Routers",
                        "rpcName": "AggregatedList",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _Delete(_BaseRoutersRestTransport._BaseDelete, RoutersRestStub):
        def __hash__(self):
            return hash("RoutersRestTransport.Delete")

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
            request: compute.DeleteRouterRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the delete method over HTTP.

            Args:
                request (~.compute.DeleteRouterRequest):
                    The request object. A request message for Routers.Delete.
                See the method description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource.

                Google Compute Engine has three Operation resources:

                - `Global </compute/docs/reference/rest/v1/globalOperations>`__
                - `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__

                You can use an operation resource to manage asynchronous
                API requests. For more information, readHandling API
                responses.

                Operations can be global, regional or zonal.

                ::

                   - For global operations, use the `globalOperations`
                   resource.
                   - For regional operations, use the
                   `regionOperations` resource.
                   - For zonal operations, use
                   the `zoneOperations` resource.

                For more information, read Global, Regional, and Zonal
                Resources.

                Note that completed Operation resources have a limited
                retention period.

            """

            http_options = _BaseRoutersRestTransport._BaseDelete._get_http_options()
            request, metadata = self._interceptor.pre_delete(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRoutersRestTransport._BaseDelete,
                    "_BaseDelete__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.compute_v1.RoutersClient.Delete",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Routers",
                        "rpcName": "Delete",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RoutersRestTransport._Delete._get_response(
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
            resp = compute.Operation()
            pb_resp = compute.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_delete(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.RoutersClient.delete",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Routers",
                        "rpcName": "Delete",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteNamedSet(
        _BaseRoutersRestTransport._BaseDeleteNamedSet, RoutersRestStub
    ):
        def __hash__(self):
            return hash("RoutersRestTransport.DeleteNamedSet")

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
            request: compute.DeleteNamedSetRouterRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the delete named set method over HTTP.

            Args:
                request (~.compute.DeleteNamedSetRouterRequest):
                    The request object. A request message for
                Routers.DeleteNamedSet. See the method
                description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource.

                Google Compute Engine has three Operation resources:

                - `Global </compute/docs/reference/rest/v1/globalOperations>`__
                - `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__

                You can use an operation resource to manage asynchronous
                API requests. For more information, readHandling API
                responses.

                Operations can be global, regional or zonal.

                ::

                   - For global operations, use the `globalOperations`
                   resource.
                   - For regional operations, use the
                   `regionOperations` resource.
                   - For zonal operations, use
                   the `zoneOperations` resource.

                For more information, read Global, Regional, and Zonal
                Resources.

                Note that completed Operation resources have a limited
                retention period.

            """

            http_options = (
                _BaseRoutersRestTransport._BaseDeleteNamedSet._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_named_set(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRoutersRestTransport._BaseDeleteNamedSet,
                    "_BaseDeleteNamedSet__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.compute_v1.RoutersClient.DeleteNamedSet",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Routers",
                        "rpcName": "DeleteNamedSet",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RoutersRestTransport._DeleteNamedSet._get_response(
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
            resp = compute.Operation()
            pb_resp = compute.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_delete_named_set(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_named_set_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.RoutersClient.delete_named_set",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Routers",
                        "rpcName": "DeleteNamedSet",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteRoutePolicy(
        _BaseRoutersRestTransport._BaseDeleteRoutePolicy, RoutersRestStub
    ):
        def __hash__(self):
            return hash("RoutersRestTransport.DeleteRoutePolicy")

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
            request: compute.DeleteRoutePolicyRouterRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the delete route policy method over HTTP.

            Args:
                request (~.compute.DeleteRoutePolicyRouterRequest):
                    The request object. A request message for
                Routers.DeleteRoutePolicy. See the
                method description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource.

                Google Compute Engine has three Operation resources:

                - `Global </compute/docs/reference/rest/v1/globalOperations>`__
                - `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__

                You can use an operation resource to manage asynchronous
                API requests. For more information, readHandling API
                responses.

                Operations can be global, regional or zonal.

                ::

                   - For global operations, use the `globalOperations`
                   resource.
                   - For regional operations, use the
                   `regionOperations` resource.
                   - For zonal operations, use
                   the `zoneOperations` resource.

                For more information, read Global, Regional, and Zonal
                Resources.

                Note that completed Operation resources have a limited
                retention period.

            """

            http_options = (
                _BaseRoutersRestTransport._BaseDeleteRoutePolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_route_policy(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRoutersRestTransport._BaseDeleteRoutePolicy,
                    "_BaseDeleteRoutePolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.compute_v1.RoutersClient.DeleteRoutePolicy",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Routers",
                        "rpcName": "DeleteRoutePolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RoutersRestTransport._DeleteRoutePolicy._get_response(
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
            resp = compute.Operation()
            pb_resp = compute.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_delete_route_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_route_policy_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.RoutersClient.delete_route_policy",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Routers",
                        "rpcName": "DeleteRoutePolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _Get(_BaseRoutersRestTransport._BaseGet, RoutersRestStub):
        def __hash__(self):
            return hash("RoutersRestTransport.Get")

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
            request: compute.GetRouterRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Router:
            r"""Call the get method over HTTP.

            Args:
                request (~.compute.GetRouterRequest):
                    The request object. A request message for Routers.Get.
                See the method description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Router:
                    Represents a Cloud Router resource.

                For more information about Cloud Router,
                read theCloud Router overview.

            """

            http_options = _BaseRoutersRestTransport._BaseGet._get_http_options()
            request, metadata = self._interceptor.pre_get(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRoutersRestTransport._BaseGet,
                    "_BaseGet__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.compute_v1.RoutersClient.Get",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Routers",
                        "rpcName": "Get",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RoutersRestTransport._Get._get_response(
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
            resp = compute.Router()
            pb_resp = compute.Router.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_with_metadata(resp, response_metadata)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Router.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.RoutersClient.get",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Routers",
                        "rpcName": "Get",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetNamedSet(_BaseRoutersRestTransport._BaseGetNamedSet, RoutersRestStub):
        def __hash__(self):
            return hash("RoutersRestTransport.GetNamedSet")

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
            request: compute.GetNamedSetRouterRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.RoutersGetNamedSetResponse:
            r"""Call the get named set method over HTTP.

            Args:
                request (~.compute.GetNamedSetRouterRequest):
                    The request object. A request message for
                Routers.GetNamedSet. See the method
                description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.RoutersGetNamedSetResponse:

            """

            http_options = (
                _BaseRoutersRestTransport._BaseGetNamedSet._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_named_set(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRoutersRestTransport._BaseGetNamedSet,
                    "_BaseGetNamedSet__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.compute_v1.RoutersClient.GetNamedSet",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Routers",
                        "rpcName": "GetNamedSet",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RoutersRestTransport._GetNamedSet._get_response(
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
            resp = compute.RoutersGetNamedSetResponse()
            pb_resp = compute.RoutersGetNamedSetResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_named_set(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_named_set_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.RoutersGetNamedSetResponse.to_json(
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
                    "Received response for google.cloud.compute_v1.RoutersClient.get_named_set",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Routers",
                        "rpcName": "GetNamedSet",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetNatIpInfo(_BaseRoutersRestTransport._BaseGetNatIpInfo, RoutersRestStub):
        def __hash__(self):
            return hash("RoutersRestTransport.GetNatIpInfo")

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
            request: compute.GetNatIpInfoRouterRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.NatIpInfoResponse:
            r"""Call the get nat ip info method over HTTP.

            Args:
                request (~.compute.GetNatIpInfoRouterRequest):
                    The request object. A request message for
                Routers.GetNatIpInfo. See the method
                description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.NatIpInfoResponse:

            """

            http_options = (
                _BaseRoutersRestTransport._BaseGetNatIpInfo._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_nat_ip_info(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRoutersRestTransport._BaseGetNatIpInfo,
                    "_BaseGetNatIpInfo__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.compute_v1.RoutersClient.GetNatIpInfo",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Routers",
                        "rpcName": "GetNatIpInfo",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RoutersRestTransport._GetNatIpInfo._get_response(
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
            resp = compute.NatIpInfoResponse()
            pb_resp = compute.NatIpInfoResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_nat_ip_info(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_nat_ip_info_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.NatIpInfoResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.RoutersClient.get_nat_ip_info",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Routers",
                        "rpcName": "GetNatIpInfo",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetNatMappingInfo(
        _BaseRoutersRestTransport._BaseGetNatMappingInfo, RoutersRestStub
    ):
        def __hash__(self):
            return hash("RoutersRestTransport.GetNatMappingInfo")

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
            request: compute.GetNatMappingInfoRoutersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.VmEndpointNatMappingsList:
            r"""Call the get nat mapping info method over HTTP.

            Args:
                request (~.compute.GetNatMappingInfoRoutersRequest):
                    The request object. A request message for
                Routers.GetNatMappingInfo. See the
                method description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.VmEndpointNatMappingsList:
                    Contains a list of
                VmEndpointNatMappings.

            """

            http_options = (
                _BaseRoutersRestTransport._BaseGetNatMappingInfo._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_nat_mapping_info(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRoutersRestTransport._BaseGetNatMappingInfo,
                    "_BaseGetNatMappingInfo__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.compute_v1.RoutersClient.GetNatMappingInfo",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Routers",
                        "rpcName": "GetNatMappingInfo",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RoutersRestTransport._GetNatMappingInfo._get_response(
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
            resp = compute.VmEndpointNatMappingsList()
            pb_resp = compute.VmEndpointNatMappingsList.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_nat_mapping_info(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_nat_mapping_info_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.VmEndpointNatMappingsList.to_json(
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
                    "Received response for google.cloud.compute_v1.RoutersClient.get_nat_mapping_info",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Routers",
                        "rpcName": "GetNatMappingInfo",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetRoutePolicy(
        _BaseRoutersRestTransport._BaseGetRoutePolicy, RoutersRestStub
    ):
        def __hash__(self):
            return hash("RoutersRestTransport.GetRoutePolicy")

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
            request: compute.GetRoutePolicyRouterRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.RoutersGetRoutePolicyResponse:
            r"""Call the get route policy method over HTTP.

            Args:
                request (~.compute.GetRoutePolicyRouterRequest):
                    The request object. A request message for
                Routers.GetRoutePolicy. See the method
                description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.RoutersGetRoutePolicyResponse:

            """

            http_options = (
                _BaseRoutersRestTransport._BaseGetRoutePolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_route_policy(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRoutersRestTransport._BaseGetRoutePolicy,
                    "_BaseGetRoutePolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.compute_v1.RoutersClient.GetRoutePolicy",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Routers",
                        "rpcName": "GetRoutePolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RoutersRestTransport._GetRoutePolicy._get_response(
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
            resp = compute.RoutersGetRoutePolicyResponse()
            pb_resp = compute.RoutersGetRoutePolicyResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_route_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_route_policy_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.RoutersGetRoutePolicyResponse.to_json(
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
                    "Received response for google.cloud.compute_v1.RoutersClient.get_route_policy",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Routers",
                        "rpcName": "GetRoutePolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetRouterStatus(
        _BaseRoutersRestTransport._BaseGetRouterStatus, RoutersRestStub
    ):
        def __hash__(self):
            return hash("RoutersRestTransport.GetRouterStatus")

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
            request: compute.GetRouterStatusRouterRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.RouterStatusResponse:
            r"""Call the get router status method over HTTP.

            Args:
                request (~.compute.GetRouterStatusRouterRequest):
                    The request object. A request message for
                Routers.GetRouterStatus. See the method
                description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.RouterStatusResponse:

            """

            http_options = (
                _BaseRoutersRestTransport._BaseGetRouterStatus._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_router_status(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRoutersRestTransport._BaseGetRouterStatus,
                    "_BaseGetRouterStatus__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.compute_v1.RoutersClient.GetRouterStatus",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Routers",
                        "rpcName": "GetRouterStatus",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RoutersRestTransport._GetRouterStatus._get_response(
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
            resp = compute.RouterStatusResponse()
            pb_resp = compute.RouterStatusResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_router_status(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_router_status_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.RouterStatusResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.RoutersClient.get_router_status",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Routers",
                        "rpcName": "GetRouterStatus",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _Insert(_BaseRoutersRestTransport._BaseInsert, RoutersRestStub):
        def __hash__(self):
            return hash("RoutersRestTransport.Insert")

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
            request: compute.InsertRouterRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the insert method over HTTP.

            Args:
                request (~.compute.InsertRouterRequest):
                    The request object. A request message for Routers.Insert.
                See the method description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource.

                Google Compute Engine has three Operation resources:

                - `Global </compute/docs/reference/rest/v1/globalOperations>`__
                - `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__

                You can use an operation resource to manage asynchronous
                API requests. For more information, readHandling API
                responses.

                Operations can be global, regional or zonal.

                ::

                   - For global operations, use the `globalOperations`
                   resource.
                   - For regional operations, use the
                   `regionOperations` resource.
                   - For zonal operations, use
                   the `zoneOperations` resource.

                For more information, read Global, Regional, and Zonal
                Resources.

                Note that completed Operation resources have a limited
                retention period.

            """

            http_options = _BaseRoutersRestTransport._BaseInsert._get_http_options()
            request, metadata = self._interceptor.pre_insert(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRoutersRestTransport._BaseInsert,
                    "_BaseInsert__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.compute_v1.RoutersClient.Insert",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Routers",
                        "rpcName": "Insert",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RoutersRestTransport._Insert._get_response(
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
            resp = compute.Operation()
            pb_resp = compute.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_insert(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_insert_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.RoutersClient.insert",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Routers",
                        "rpcName": "Insert",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _List(_BaseRoutersRestTransport._BaseList, RoutersRestStub):
        def __hash__(self):
            return hash("RoutersRestTransport.List")

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
            request: compute.ListRoutersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.RouterList:
            r"""Call the list method over HTTP.

            Args:
                request (~.compute.ListRoutersRequest):
                    The request object. A request message for Routers.List.
                See the method description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.RouterList:
                    Contains a list of Router resources.
            """

            http_options = _BaseRoutersRestTransport._BaseList._get_http_options()
            request, metadata = self._interceptor.pre_list(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRoutersRestTransport._BaseList,
                    "_BaseList__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.compute_v1.RoutersClient.List",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Routers",
                        "rpcName": "List",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RoutersRestTransport._List._get_response(
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
            resp = compute.RouterList()
            pb_resp = compute.RouterList.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_with_metadata(resp, response_metadata)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.RouterList.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.RoutersClient.list",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Routers",
                        "rpcName": "List",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListBgpRoutes(_BaseRoutersRestTransport._BaseListBgpRoutes, RoutersRestStub):
        def __hash__(self):
            return hash("RoutersRestTransport.ListBgpRoutes")

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
            request: compute.ListBgpRoutesRoutersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.RoutersListBgpRoutes:
            r"""Call the list bgp routes method over HTTP.

            Args:
                request (~.compute.ListBgpRoutesRoutersRequest):
                    The request object. A request message for
                Routers.ListBgpRoutes. See the method
                description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.RoutersListBgpRoutes:

            """

            http_options = (
                _BaseRoutersRestTransport._BaseListBgpRoutes._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_bgp_routes(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRoutersRestTransport._BaseListBgpRoutes,
                    "_BaseListBgpRoutes__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.compute_v1.RoutersClient.ListBgpRoutes",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Routers",
                        "rpcName": "ListBgpRoutes",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RoutersRestTransport._ListBgpRoutes._get_response(
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
            resp = compute.RoutersListBgpRoutes()
            pb_resp = compute.RoutersListBgpRoutes.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_bgp_routes(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_bgp_routes_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.RoutersListBgpRoutes.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.RoutersClient.list_bgp_routes",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Routers",
                        "rpcName": "ListBgpRoutes",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListNamedSets(_BaseRoutersRestTransport._BaseListNamedSets, RoutersRestStub):
        def __hash__(self):
            return hash("RoutersRestTransport.ListNamedSets")

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
            request: compute.ListNamedSetsRoutersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.RoutersListNamedSets:
            r"""Call the list named sets method over HTTP.

            Args:
                request (~.compute.ListNamedSetsRoutersRequest):
                    The request object. A request message for
                Routers.ListNamedSets. See the method
                description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.RoutersListNamedSets:

            """

            http_options = (
                _BaseRoutersRestTransport._BaseListNamedSets._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_named_sets(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRoutersRestTransport._BaseListNamedSets,
                    "_BaseListNamedSets__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.compute_v1.RoutersClient.ListNamedSets",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Routers",
                        "rpcName": "ListNamedSets",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RoutersRestTransport._ListNamedSets._get_response(
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
            resp = compute.RoutersListNamedSets()
            pb_resp = compute.RoutersListNamedSets.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_named_sets(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_named_sets_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.RoutersListNamedSets.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.RoutersClient.list_named_sets",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Routers",
                        "rpcName": "ListNamedSets",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListRoutePolicies(
        _BaseRoutersRestTransport._BaseListRoutePolicies, RoutersRestStub
    ):
        def __hash__(self):
            return hash("RoutersRestTransport.ListRoutePolicies")

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
            request: compute.ListRoutePoliciesRoutersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.RoutersListRoutePolicies:
            r"""Call the list route policies method over HTTP.

            Args:
                request (~.compute.ListRoutePoliciesRoutersRequest):
                    The request object. A request message for
                Routers.ListRoutePolicies. See the
                method description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.RoutersListRoutePolicies:

            """

            http_options = (
                _BaseRoutersRestTransport._BaseListRoutePolicies._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_route_policies(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRoutersRestTransport._BaseListRoutePolicies,
                    "_BaseListRoutePolicies__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.compute_v1.RoutersClient.ListRoutePolicies",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Routers",
                        "rpcName": "ListRoutePolicies",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RoutersRestTransport._ListRoutePolicies._get_response(
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
            resp = compute.RoutersListRoutePolicies()
            pb_resp = compute.RoutersListRoutePolicies.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_route_policies(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_route_policies_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.RoutersListRoutePolicies.to_json(
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
                    "Received response for google.cloud.compute_v1.RoutersClient.list_route_policies",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Routers",
                        "rpcName": "ListRoutePolicies",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _Patch(_BaseRoutersRestTransport._BasePatch, RoutersRestStub):
        def __hash__(self):
            return hash("RoutersRestTransport.Patch")

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
            request: compute.PatchRouterRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the patch method over HTTP.

            Args:
                request (~.compute.PatchRouterRequest):
                    The request object. A request message for Routers.Patch.
                See the method description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource.

                Google Compute Engine has three Operation resources:

                - `Global </compute/docs/reference/rest/v1/globalOperations>`__
                - `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__

                You can use an operation resource to manage asynchronous
                API requests. For more information, readHandling API
                responses.

                Operations can be global, regional or zonal.

                ::

                   - For global operations, use the `globalOperations`
                   resource.
                   - For regional operations, use the
                   `regionOperations` resource.
                   - For zonal operations, use
                   the `zoneOperations` resource.

                For more information, read Global, Regional, and Zonal
                Resources.

                Note that completed Operation resources have a limited
                retention period.

            """

            http_options = _BaseRoutersRestTransport._BasePatch._get_http_options()
            request, metadata = self._interceptor.pre_patch(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRoutersRestTransport._BasePatch,
                    "_BasePatch__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.compute_v1.RoutersClient.Patch",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Routers",
                        "rpcName": "Patch",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RoutersRestTransport._Patch._get_response(
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
            resp = compute.Operation()
            pb_resp = compute.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_patch(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_patch_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.RoutersClient.patch",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Routers",
                        "rpcName": "Patch",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _PatchNamedSet(_BaseRoutersRestTransport._BasePatchNamedSet, RoutersRestStub):
        def __hash__(self):
            return hash("RoutersRestTransport.PatchNamedSet")

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
            request: compute.PatchNamedSetRouterRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the patch named set method over HTTP.

            Args:
                request (~.compute.PatchNamedSetRouterRequest):
                    The request object. A request message for
                Routers.PatchNamedSet. See the method
                description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource.

                Google Compute Engine has three Operation resources:

                - `Global </compute/docs/reference/rest/v1/globalOperations>`__
                - `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__

                You can use an operation resource to manage asynchronous
                API requests. For more information, readHandling API
                responses.

                Operations can be global, regional or zonal.

                ::

                   - For global operations, use the `globalOperations`
                   resource.
                   - For regional operations, use the
                   `regionOperations` resource.
                   - For zonal operations, use
                   the `zoneOperations` resource.

                For more information, read Global, Regional, and Zonal
                Resources.

                Note that completed Operation resources have a limited
                retention period.

            """

            http_options = (
                _BaseRoutersRestTransport._BasePatchNamedSet._get_http_options()
            )
            request, metadata = self._interceptor.pre_patch_named_set(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRoutersRestTransport._BasePatchNamedSet,
                    "_BasePatchNamedSet__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.compute_v1.RoutersClient.PatchNamedSet",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Routers",
                        "rpcName": "PatchNamedSet",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RoutersRestTransport._PatchNamedSet._get_response(
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
            resp = compute.Operation()
            pb_resp = compute.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_patch_named_set(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_patch_named_set_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.RoutersClient.patch_named_set",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Routers",
                        "rpcName": "PatchNamedSet",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _PatchRoutePolicy(
        _BaseRoutersRestTransport._BasePatchRoutePolicy, RoutersRestStub
    ):
        def __hash__(self):
            return hash("RoutersRestTransport.PatchRoutePolicy")

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
            request: compute.PatchRoutePolicyRouterRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the patch route policy method over HTTP.

            Args:
                request (~.compute.PatchRoutePolicyRouterRequest):
                    The request object. A request message for
                Routers.PatchRoutePolicy. See the method
                description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource.

                Google Compute Engine has three Operation resources:

                - `Global </compute/docs/reference/rest/v1/globalOperations>`__
                - `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__

                You can use an operation resource to manage asynchronous
                API requests. For more information, readHandling API
                responses.

                Operations can be global, regional or zonal.

                ::

                   - For global operations, use the `globalOperations`
                   resource.
                   - For regional operations, use the
                   `regionOperations` resource.
                   - For zonal operations, use
                   the `zoneOperations` resource.

                For more information, read Global, Regional, and Zonal
                Resources.

                Note that completed Operation resources have a limited
                retention period.

            """

            http_options = (
                _BaseRoutersRestTransport._BasePatchRoutePolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_patch_route_policy(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRoutersRestTransport._BasePatchRoutePolicy,
                    "_BasePatchRoutePolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.compute_v1.RoutersClient.PatchRoutePolicy",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Routers",
                        "rpcName": "PatchRoutePolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RoutersRestTransport._PatchRoutePolicy._get_response(
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
            resp = compute.Operation()
            pb_resp = compute.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_patch_route_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_patch_route_policy_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.RoutersClient.patch_route_policy",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Routers",
                        "rpcName": "PatchRoutePolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _Preview(_BaseRoutersRestTransport._BasePreview, RoutersRestStub):
        def __hash__(self):
            return hash("RoutersRestTransport.Preview")

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
            request: compute.PreviewRouterRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.RoutersPreviewResponse:
            r"""Call the preview method over HTTP.

            Args:
                request (~.compute.PreviewRouterRequest):
                    The request object. A request message for
                Routers.Preview. See the method
                description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.RoutersPreviewResponse:

            """

            http_options = _BaseRoutersRestTransport._BasePreview._get_http_options()
            request, metadata = self._interceptor.pre_preview(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRoutersRestTransport._BasePreview,
                    "_BasePreview__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.compute_v1.RoutersClient.Preview",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Routers",
                        "rpcName": "Preview",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RoutersRestTransport._Preview._get_response(
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
            resp = compute.RoutersPreviewResponse()
            pb_resp = compute.RoutersPreviewResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_preview(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_preview_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.RoutersPreviewResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.RoutersClient.preview",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Routers",
                        "rpcName": "Preview",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _Update(_BaseRoutersRestTransport._BaseUpdate, RoutersRestStub):
        def __hash__(self):
            return hash("RoutersRestTransport.Update")

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
            request: compute.UpdateRouterRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the update method over HTTP.

            Args:
                request (~.compute.UpdateRouterRequest):
                    The request object. A request message for Routers.Update.
                See the method description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource.

                Google Compute Engine has three Operation resources:

                - `Global </compute/docs/reference/rest/v1/globalOperations>`__
                - `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__

                You can use an operation resource to manage asynchronous
                API requests. For more information, readHandling API
                responses.

                Operations can be global, regional or zonal.

                ::

                   - For global operations, use the `globalOperations`
                   resource.
                   - For regional operations, use the
                   `regionOperations` resource.
                   - For zonal operations, use
                   the `zoneOperations` resource.

                For more information, read Global, Regional, and Zonal
                Resources.

                Note that completed Operation resources have a limited
                retention period.

            """

            http_options = _BaseRoutersRestTransport._BaseUpdate._get_http_options()
            request, metadata = self._interceptor.pre_update(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRoutersRestTransport._BaseUpdate,
                    "_BaseUpdate__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.compute_v1.RoutersClient.Update",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Routers",
                        "rpcName": "Update",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RoutersRestTransport._Update._get_response(
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
            resp = compute.Operation()
            pb_resp = compute.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.RoutersClient.update",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Routers",
                        "rpcName": "Update",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateNamedSet(
        _BaseRoutersRestTransport._BaseUpdateNamedSet, RoutersRestStub
    ):
        def __hash__(self):
            return hash("RoutersRestTransport.UpdateNamedSet")

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
            request: compute.UpdateNamedSetRouterRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the update named set method over HTTP.

            Args:
                request (~.compute.UpdateNamedSetRouterRequest):
                    The request object. A request message for
                Routers.UpdateNamedSet. See the method
                description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource.

                Google Compute Engine has three Operation resources:

                - `Global </compute/docs/reference/rest/v1/globalOperations>`__
                - `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__

                You can use an operation resource to manage asynchronous
                API requests. For more information, readHandling API
                responses.

                Operations can be global, regional or zonal.

                ::

                   - For global operations, use the `globalOperations`
                   resource.
                   - For regional operations, use the
                   `regionOperations` resource.
                   - For zonal operations, use
                   the `zoneOperations` resource.

                For more information, read Global, Regional, and Zonal
                Resources.

                Note that completed Operation resources have a limited
                retention period.

            """

            http_options = (
                _BaseRoutersRestTransport._BaseUpdateNamedSet._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_named_set(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRoutersRestTransport._BaseUpdateNamedSet,
                    "_BaseUpdateNamedSet__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.compute_v1.RoutersClient.UpdateNamedSet",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Routers",
                        "rpcName": "UpdateNamedSet",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RoutersRestTransport._UpdateNamedSet._get_response(
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
            resp = compute.Operation()
            pb_resp = compute.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_named_set(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_named_set_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.RoutersClient.update_named_set",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Routers",
                        "rpcName": "UpdateNamedSet",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateRoutePolicy(
        _BaseRoutersRestTransport._BaseUpdateRoutePolicy, RoutersRestStub
    ):
        def __hash__(self):
            return hash("RoutersRestTransport.UpdateRoutePolicy")

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
            request: compute.UpdateRoutePolicyRouterRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the update route policy method over HTTP.

            Args:
                request (~.compute.UpdateRoutePolicyRouterRequest):
                    The request object. A request message for
                Routers.UpdateRoutePolicy. See the
                method description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource.

                Google Compute Engine has three Operation resources:

                - `Global </compute/docs/reference/rest/v1/globalOperations>`__
                - `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__

                You can use an operation resource to manage asynchronous
                API requests. For more information, readHandling API
                responses.

                Operations can be global, regional or zonal.

                ::

                   - For global operations, use the `globalOperations`
                   resource.
                   - For regional operations, use the
                   `regionOperations` resource.
                   - For zonal operations, use
                   the `zoneOperations` resource.

                For more information, read Global, Regional, and Zonal
                Resources.

                Note that completed Operation resources have a limited
                retention period.

            """

            http_options = (
                _BaseRoutersRestTransport._BaseUpdateRoutePolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_route_policy(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRoutersRestTransport._BaseUpdateRoutePolicy,
                    "_BaseUpdateRoutePolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.compute_v1.RoutersClient.UpdateRoutePolicy",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Routers",
                        "rpcName": "UpdateRoutePolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RoutersRestTransport._UpdateRoutePolicy._get_response(
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
            resp = compute.Operation()
            pb_resp = compute.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_route_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_route_policy_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.RoutersClient.update_route_policy",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Routers",
                        "rpcName": "UpdateRoutePolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def aggregated_list(
        self,
    ) -> Callable[[compute.AggregatedListRoutersRequest], compute.RouterAggregatedList]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._AggregatedList(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete(self) -> Callable[[compute.DeleteRouterRequest], compute.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._Delete(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_named_set(
        self,
    ) -> Callable[[compute.DeleteNamedSetRouterRequest], compute.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteNamedSet(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_route_policy(
        self,
    ) -> Callable[[compute.DeleteRoutePolicyRouterRequest], compute.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteRoutePolicy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get(self) -> Callable[[compute.GetRouterRequest], compute.Router]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._Get(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_named_set(
        self,
    ) -> Callable[
        [compute.GetNamedSetRouterRequest], compute.RoutersGetNamedSetResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetNamedSet(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_nat_ip_info(
        self,
    ) -> Callable[[compute.GetNatIpInfoRouterRequest], compute.NatIpInfoResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetNatIpInfo(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_nat_mapping_info(
        self,
    ) -> Callable[
        [compute.GetNatMappingInfoRoutersRequest], compute.VmEndpointNatMappingsList
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetNatMappingInfo(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_route_policy(
        self,
    ) -> Callable[
        [compute.GetRoutePolicyRouterRequest], compute.RoutersGetRoutePolicyResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetRoutePolicy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_router_status(
        self,
    ) -> Callable[[compute.GetRouterStatusRouterRequest], compute.RouterStatusResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetRouterStatus(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def insert(self) -> Callable[[compute.InsertRouterRequest], compute.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._Insert(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list(self) -> Callable[[compute.ListRoutersRequest], compute.RouterList]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._List(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_bgp_routes(
        self,
    ) -> Callable[[compute.ListBgpRoutesRoutersRequest], compute.RoutersListBgpRoutes]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListBgpRoutes(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_named_sets(
        self,
    ) -> Callable[[compute.ListNamedSetsRoutersRequest], compute.RoutersListNamedSets]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListNamedSets(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_route_policies(
        self,
    ) -> Callable[
        [compute.ListRoutePoliciesRoutersRequest], compute.RoutersListRoutePolicies
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListRoutePolicies(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def patch(self) -> Callable[[compute.PatchRouterRequest], compute.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._Patch(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def patch_named_set(
        self,
    ) -> Callable[[compute.PatchNamedSetRouterRequest], compute.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._PatchNamedSet(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def patch_route_policy(
        self,
    ) -> Callable[[compute.PatchRoutePolicyRouterRequest], compute.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._PatchRoutePolicy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def preview(
        self,
    ) -> Callable[[compute.PreviewRouterRequest], compute.RoutersPreviewResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._Preview(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update(self) -> Callable[[compute.UpdateRouterRequest], compute.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._Update(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_named_set(
        self,
    ) -> Callable[[compute.UpdateNamedSetRouterRequest], compute.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateNamedSet(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_route_policy(
        self,
    ) -> Callable[[compute.UpdateRoutePolicyRouterRequest], compute.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateRoutePolicy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("RoutersRestTransport",)
