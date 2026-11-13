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

from google.cloud.vmwareengine_v1._compat import transcode_request
from google.cloud.vmwareengine_v1.types import vmwareengine, vmwareengine_resources

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseVmwareEngineRestTransport

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


class VmwareEngineRestInterceptor:
    """Interceptor for VmwareEngine.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the VmwareEngineRestTransport.

    .. code-block:: python
        class MyCustomVmwareEngineInterceptor(VmwareEngineRestInterceptor):
            def pre_create_cluster(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_cluster(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_external_access_rule(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_external_access_rule(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_external_address(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_external_address(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_hcx_activation_key(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_hcx_activation_key(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_logging_server(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_logging_server(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_management_dns_zone_binding(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_management_dns_zone_binding(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_network_peering(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_network_peering(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_network_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_network_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_private_cloud(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_private_cloud(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_private_connection(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_private_connection(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_vmware_engine_network(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_vmware_engine_network(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_cluster(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_cluster(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_external_access_rule(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_external_access_rule(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_external_address(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_external_address(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_logging_server(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_logging_server(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_management_dns_zone_binding(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_management_dns_zone_binding(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_network_peering(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_network_peering(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_network_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_network_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_private_cloud(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_private_cloud(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_private_connection(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_private_connection(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_vmware_engine_network(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_vmware_engine_network(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_fetch_network_policy_external_addresses(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_fetch_network_policy_external_addresses(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_cluster(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_cluster(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_dns_bind_permission(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_dns_bind_permission(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_dns_forwarding(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_dns_forwarding(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_external_access_rule(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_external_access_rule(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_external_address(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_external_address(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_hcx_activation_key(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_hcx_activation_key(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_logging_server(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_logging_server(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_management_dns_zone_binding(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_management_dns_zone_binding(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_network_peering(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_network_peering(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_network_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_network_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_node(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_node(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_node_type(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_node_type(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_private_cloud(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_private_cloud(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_private_connection(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_private_connection(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_subnet(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_subnet(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_vmware_engine_network(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_vmware_engine_network(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_grant_dns_bind_permission(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_grant_dns_bind_permission(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_clusters(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_clusters(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_external_access_rules(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_external_access_rules(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_external_addresses(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_external_addresses(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_hcx_activation_keys(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_hcx_activation_keys(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_logging_servers(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_logging_servers(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_management_dns_zone_bindings(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_management_dns_zone_bindings(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_network_peerings(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_network_peerings(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_network_policies(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_network_policies(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_nodes(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_nodes(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_node_types(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_node_types(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_peering_routes(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_peering_routes(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_private_clouds(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_private_clouds(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_private_connection_peering_routes(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_private_connection_peering_routes(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_private_connections(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_private_connections(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_subnets(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_subnets(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_vmware_engine_networks(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_vmware_engine_networks(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_repair_management_dns_zone_binding(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_repair_management_dns_zone_binding(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_reset_nsx_credentials(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_reset_nsx_credentials(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_reset_vcenter_credentials(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_reset_vcenter_credentials(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_revoke_dns_bind_permission(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_revoke_dns_bind_permission(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_show_nsx_credentials(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_show_nsx_credentials(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_show_vcenter_credentials(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_show_vcenter_credentials(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_undelete_private_cloud(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_undelete_private_cloud(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_cluster(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_cluster(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_dns_forwarding(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_dns_forwarding(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_external_access_rule(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_external_access_rule(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_external_address(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_external_address(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_logging_server(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_logging_server(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_management_dns_zone_binding(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_management_dns_zone_binding(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_network_peering(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_network_peering(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_network_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_network_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_private_cloud(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_private_cloud(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_private_connection(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_private_connection(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_subnet(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_subnet(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_vmware_engine_network(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_vmware_engine_network(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = VmwareEngineRestTransport(interceptor=MyCustomVmwareEngineInterceptor())
        client = VmwareEngineClient(transport=transport)


    """

    def pre_create_cluster(
        self,
        request: vmwareengine.CreateClusterRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.CreateClusterRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_cluster

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_create_cluster(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_cluster

        DEPRECATED. Please use the `post_create_cluster_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_create_cluster` interceptor runs
        before the `post_create_cluster_with_metadata` interceptor.
        """
        return response

    def post_create_cluster_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_cluster

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_create_cluster_with_metadata`
        interceptor in new development instead of the `post_create_cluster` interceptor.
        When both interceptors are used, this `post_create_cluster_with_metadata` interceptor runs after the
        `post_create_cluster` interceptor. The (possibly modified) response returned by
        `post_create_cluster` will be passed to
        `post_create_cluster_with_metadata`.
        """
        return response, metadata

    def pre_create_external_access_rule(
        self,
        request: vmwareengine.CreateExternalAccessRuleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.CreateExternalAccessRuleRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_external_access_rule

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_create_external_access_rule(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_external_access_rule

        DEPRECATED. Please use the `post_create_external_access_rule_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_create_external_access_rule` interceptor runs
        before the `post_create_external_access_rule_with_metadata` interceptor.
        """
        return response

    def post_create_external_access_rule_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_external_access_rule

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_create_external_access_rule_with_metadata`
        interceptor in new development instead of the `post_create_external_access_rule` interceptor.
        When both interceptors are used, this `post_create_external_access_rule_with_metadata` interceptor runs after the
        `post_create_external_access_rule` interceptor. The (possibly modified) response returned by
        `post_create_external_access_rule` will be passed to
        `post_create_external_access_rule_with_metadata`.
        """
        return response, metadata

    def pre_create_external_address(
        self,
        request: vmwareengine.CreateExternalAddressRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.CreateExternalAddressRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_external_address

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_create_external_address(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_external_address

        DEPRECATED. Please use the `post_create_external_address_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_create_external_address` interceptor runs
        before the `post_create_external_address_with_metadata` interceptor.
        """
        return response

    def post_create_external_address_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_external_address

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_create_external_address_with_metadata`
        interceptor in new development instead of the `post_create_external_address` interceptor.
        When both interceptors are used, this `post_create_external_address_with_metadata` interceptor runs after the
        `post_create_external_address` interceptor. The (possibly modified) response returned by
        `post_create_external_address` will be passed to
        `post_create_external_address_with_metadata`.
        """
        return response, metadata

    def pre_create_hcx_activation_key(
        self,
        request: vmwareengine.CreateHcxActivationKeyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.CreateHcxActivationKeyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_hcx_activation_key

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_create_hcx_activation_key(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_hcx_activation_key

        DEPRECATED. Please use the `post_create_hcx_activation_key_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_create_hcx_activation_key` interceptor runs
        before the `post_create_hcx_activation_key_with_metadata` interceptor.
        """
        return response

    def post_create_hcx_activation_key_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_hcx_activation_key

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_create_hcx_activation_key_with_metadata`
        interceptor in new development instead of the `post_create_hcx_activation_key` interceptor.
        When both interceptors are used, this `post_create_hcx_activation_key_with_metadata` interceptor runs after the
        `post_create_hcx_activation_key` interceptor. The (possibly modified) response returned by
        `post_create_hcx_activation_key` will be passed to
        `post_create_hcx_activation_key_with_metadata`.
        """
        return response, metadata

    def pre_create_logging_server(
        self,
        request: vmwareengine.CreateLoggingServerRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.CreateLoggingServerRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_logging_server

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_create_logging_server(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_logging_server

        DEPRECATED. Please use the `post_create_logging_server_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_create_logging_server` interceptor runs
        before the `post_create_logging_server_with_metadata` interceptor.
        """
        return response

    def post_create_logging_server_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_logging_server

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_create_logging_server_with_metadata`
        interceptor in new development instead of the `post_create_logging_server` interceptor.
        When both interceptors are used, this `post_create_logging_server_with_metadata` interceptor runs after the
        `post_create_logging_server` interceptor. The (possibly modified) response returned by
        `post_create_logging_server` will be passed to
        `post_create_logging_server_with_metadata`.
        """
        return response, metadata

    def pre_create_management_dns_zone_binding(
        self,
        request: vmwareengine.CreateManagementDnsZoneBindingRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.CreateManagementDnsZoneBindingRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_management_dns_zone_binding

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_create_management_dns_zone_binding(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_management_dns_zone_binding

        DEPRECATED. Please use the `post_create_management_dns_zone_binding_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_create_management_dns_zone_binding` interceptor runs
        before the `post_create_management_dns_zone_binding_with_metadata` interceptor.
        """
        return response

    def post_create_management_dns_zone_binding_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_management_dns_zone_binding

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_create_management_dns_zone_binding_with_metadata`
        interceptor in new development instead of the `post_create_management_dns_zone_binding` interceptor.
        When both interceptors are used, this `post_create_management_dns_zone_binding_with_metadata` interceptor runs after the
        `post_create_management_dns_zone_binding` interceptor. The (possibly modified) response returned by
        `post_create_management_dns_zone_binding` will be passed to
        `post_create_management_dns_zone_binding_with_metadata`.
        """
        return response, metadata

    def pre_create_network_peering(
        self,
        request: vmwareengine.CreateNetworkPeeringRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.CreateNetworkPeeringRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_network_peering

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_create_network_peering(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_network_peering

        DEPRECATED. Please use the `post_create_network_peering_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_create_network_peering` interceptor runs
        before the `post_create_network_peering_with_metadata` interceptor.
        """
        return response

    def post_create_network_peering_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_network_peering

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_create_network_peering_with_metadata`
        interceptor in new development instead of the `post_create_network_peering` interceptor.
        When both interceptors are used, this `post_create_network_peering_with_metadata` interceptor runs after the
        `post_create_network_peering` interceptor. The (possibly modified) response returned by
        `post_create_network_peering` will be passed to
        `post_create_network_peering_with_metadata`.
        """
        return response, metadata

    def pre_create_network_policy(
        self,
        request: vmwareengine.CreateNetworkPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.CreateNetworkPolicyRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_network_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_create_network_policy(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_network_policy

        DEPRECATED. Please use the `post_create_network_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_create_network_policy` interceptor runs
        before the `post_create_network_policy_with_metadata` interceptor.
        """
        return response

    def post_create_network_policy_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_network_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_create_network_policy_with_metadata`
        interceptor in new development instead of the `post_create_network_policy` interceptor.
        When both interceptors are used, this `post_create_network_policy_with_metadata` interceptor runs after the
        `post_create_network_policy` interceptor. The (possibly modified) response returned by
        `post_create_network_policy` will be passed to
        `post_create_network_policy_with_metadata`.
        """
        return response, metadata

    def pre_create_private_cloud(
        self,
        request: vmwareengine.CreatePrivateCloudRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.CreatePrivateCloudRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_private_cloud

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_create_private_cloud(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_private_cloud

        DEPRECATED. Please use the `post_create_private_cloud_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_create_private_cloud` interceptor runs
        before the `post_create_private_cloud_with_metadata` interceptor.
        """
        return response

    def post_create_private_cloud_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_private_cloud

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_create_private_cloud_with_metadata`
        interceptor in new development instead of the `post_create_private_cloud` interceptor.
        When both interceptors are used, this `post_create_private_cloud_with_metadata` interceptor runs after the
        `post_create_private_cloud` interceptor. The (possibly modified) response returned by
        `post_create_private_cloud` will be passed to
        `post_create_private_cloud_with_metadata`.
        """
        return response, metadata

    def pre_create_private_connection(
        self,
        request: vmwareengine.CreatePrivateConnectionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.CreatePrivateConnectionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_private_connection

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_create_private_connection(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_private_connection

        DEPRECATED. Please use the `post_create_private_connection_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_create_private_connection` interceptor runs
        before the `post_create_private_connection_with_metadata` interceptor.
        """
        return response

    def post_create_private_connection_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_private_connection

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_create_private_connection_with_metadata`
        interceptor in new development instead of the `post_create_private_connection` interceptor.
        When both interceptors are used, this `post_create_private_connection_with_metadata` interceptor runs after the
        `post_create_private_connection` interceptor. The (possibly modified) response returned by
        `post_create_private_connection` will be passed to
        `post_create_private_connection_with_metadata`.
        """
        return response, metadata

    def pre_create_vmware_engine_network(
        self,
        request: vmwareengine.CreateVmwareEngineNetworkRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.CreateVmwareEngineNetworkRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_vmware_engine_network

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_create_vmware_engine_network(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_vmware_engine_network

        DEPRECATED. Please use the `post_create_vmware_engine_network_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_create_vmware_engine_network` interceptor runs
        before the `post_create_vmware_engine_network_with_metadata` interceptor.
        """
        return response

    def post_create_vmware_engine_network_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_vmware_engine_network

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_create_vmware_engine_network_with_metadata`
        interceptor in new development instead of the `post_create_vmware_engine_network` interceptor.
        When both interceptors are used, this `post_create_vmware_engine_network_with_metadata` interceptor runs after the
        `post_create_vmware_engine_network` interceptor. The (possibly modified) response returned by
        `post_create_vmware_engine_network` will be passed to
        `post_create_vmware_engine_network_with_metadata`.
        """
        return response, metadata

    def pre_delete_cluster(
        self,
        request: vmwareengine.DeleteClusterRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.DeleteClusterRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_cluster

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_delete_cluster(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_cluster

        DEPRECATED. Please use the `post_delete_cluster_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_delete_cluster` interceptor runs
        before the `post_delete_cluster_with_metadata` interceptor.
        """
        return response

    def post_delete_cluster_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_cluster

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_delete_cluster_with_metadata`
        interceptor in new development instead of the `post_delete_cluster` interceptor.
        When both interceptors are used, this `post_delete_cluster_with_metadata` interceptor runs after the
        `post_delete_cluster` interceptor. The (possibly modified) response returned by
        `post_delete_cluster` will be passed to
        `post_delete_cluster_with_metadata`.
        """
        return response, metadata

    def pre_delete_external_access_rule(
        self,
        request: vmwareengine.DeleteExternalAccessRuleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.DeleteExternalAccessRuleRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_external_access_rule

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_delete_external_access_rule(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_external_access_rule

        DEPRECATED. Please use the `post_delete_external_access_rule_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_delete_external_access_rule` interceptor runs
        before the `post_delete_external_access_rule_with_metadata` interceptor.
        """
        return response

    def post_delete_external_access_rule_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_external_access_rule

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_delete_external_access_rule_with_metadata`
        interceptor in new development instead of the `post_delete_external_access_rule` interceptor.
        When both interceptors are used, this `post_delete_external_access_rule_with_metadata` interceptor runs after the
        `post_delete_external_access_rule` interceptor. The (possibly modified) response returned by
        `post_delete_external_access_rule` will be passed to
        `post_delete_external_access_rule_with_metadata`.
        """
        return response, metadata

    def pre_delete_external_address(
        self,
        request: vmwareengine.DeleteExternalAddressRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.DeleteExternalAddressRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_external_address

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_delete_external_address(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_external_address

        DEPRECATED. Please use the `post_delete_external_address_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_delete_external_address` interceptor runs
        before the `post_delete_external_address_with_metadata` interceptor.
        """
        return response

    def post_delete_external_address_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_external_address

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_delete_external_address_with_metadata`
        interceptor in new development instead of the `post_delete_external_address` interceptor.
        When both interceptors are used, this `post_delete_external_address_with_metadata` interceptor runs after the
        `post_delete_external_address` interceptor. The (possibly modified) response returned by
        `post_delete_external_address` will be passed to
        `post_delete_external_address_with_metadata`.
        """
        return response, metadata

    def pre_delete_logging_server(
        self,
        request: vmwareengine.DeleteLoggingServerRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.DeleteLoggingServerRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_logging_server

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_delete_logging_server(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_logging_server

        DEPRECATED. Please use the `post_delete_logging_server_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_delete_logging_server` interceptor runs
        before the `post_delete_logging_server_with_metadata` interceptor.
        """
        return response

    def post_delete_logging_server_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_logging_server

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_delete_logging_server_with_metadata`
        interceptor in new development instead of the `post_delete_logging_server` interceptor.
        When both interceptors are used, this `post_delete_logging_server_with_metadata` interceptor runs after the
        `post_delete_logging_server` interceptor. The (possibly modified) response returned by
        `post_delete_logging_server` will be passed to
        `post_delete_logging_server_with_metadata`.
        """
        return response, metadata

    def pre_delete_management_dns_zone_binding(
        self,
        request: vmwareengine.DeleteManagementDnsZoneBindingRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.DeleteManagementDnsZoneBindingRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_management_dns_zone_binding

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_delete_management_dns_zone_binding(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_management_dns_zone_binding

        DEPRECATED. Please use the `post_delete_management_dns_zone_binding_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_delete_management_dns_zone_binding` interceptor runs
        before the `post_delete_management_dns_zone_binding_with_metadata` interceptor.
        """
        return response

    def post_delete_management_dns_zone_binding_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_management_dns_zone_binding

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_delete_management_dns_zone_binding_with_metadata`
        interceptor in new development instead of the `post_delete_management_dns_zone_binding` interceptor.
        When both interceptors are used, this `post_delete_management_dns_zone_binding_with_metadata` interceptor runs after the
        `post_delete_management_dns_zone_binding` interceptor. The (possibly modified) response returned by
        `post_delete_management_dns_zone_binding` will be passed to
        `post_delete_management_dns_zone_binding_with_metadata`.
        """
        return response, metadata

    def pre_delete_network_peering(
        self,
        request: vmwareengine.DeleteNetworkPeeringRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.DeleteNetworkPeeringRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_network_peering

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_delete_network_peering(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_network_peering

        DEPRECATED. Please use the `post_delete_network_peering_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_delete_network_peering` interceptor runs
        before the `post_delete_network_peering_with_metadata` interceptor.
        """
        return response

    def post_delete_network_peering_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_network_peering

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_delete_network_peering_with_metadata`
        interceptor in new development instead of the `post_delete_network_peering` interceptor.
        When both interceptors are used, this `post_delete_network_peering_with_metadata` interceptor runs after the
        `post_delete_network_peering` interceptor. The (possibly modified) response returned by
        `post_delete_network_peering` will be passed to
        `post_delete_network_peering_with_metadata`.
        """
        return response, metadata

    def pre_delete_network_policy(
        self,
        request: vmwareengine.DeleteNetworkPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.DeleteNetworkPolicyRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_network_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_delete_network_policy(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_network_policy

        DEPRECATED. Please use the `post_delete_network_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_delete_network_policy` interceptor runs
        before the `post_delete_network_policy_with_metadata` interceptor.
        """
        return response

    def post_delete_network_policy_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_network_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_delete_network_policy_with_metadata`
        interceptor in new development instead of the `post_delete_network_policy` interceptor.
        When both interceptors are used, this `post_delete_network_policy_with_metadata` interceptor runs after the
        `post_delete_network_policy` interceptor. The (possibly modified) response returned by
        `post_delete_network_policy` will be passed to
        `post_delete_network_policy_with_metadata`.
        """
        return response, metadata

    def pre_delete_private_cloud(
        self,
        request: vmwareengine.DeletePrivateCloudRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.DeletePrivateCloudRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_private_cloud

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_delete_private_cloud(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_private_cloud

        DEPRECATED. Please use the `post_delete_private_cloud_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_delete_private_cloud` interceptor runs
        before the `post_delete_private_cloud_with_metadata` interceptor.
        """
        return response

    def post_delete_private_cloud_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_private_cloud

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_delete_private_cloud_with_metadata`
        interceptor in new development instead of the `post_delete_private_cloud` interceptor.
        When both interceptors are used, this `post_delete_private_cloud_with_metadata` interceptor runs after the
        `post_delete_private_cloud` interceptor. The (possibly modified) response returned by
        `post_delete_private_cloud` will be passed to
        `post_delete_private_cloud_with_metadata`.
        """
        return response, metadata

    def pre_delete_private_connection(
        self,
        request: vmwareengine.DeletePrivateConnectionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.DeletePrivateConnectionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_private_connection

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_delete_private_connection(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_private_connection

        DEPRECATED. Please use the `post_delete_private_connection_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_delete_private_connection` interceptor runs
        before the `post_delete_private_connection_with_metadata` interceptor.
        """
        return response

    def post_delete_private_connection_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_private_connection

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_delete_private_connection_with_metadata`
        interceptor in new development instead of the `post_delete_private_connection` interceptor.
        When both interceptors are used, this `post_delete_private_connection_with_metadata` interceptor runs after the
        `post_delete_private_connection` interceptor. The (possibly modified) response returned by
        `post_delete_private_connection` will be passed to
        `post_delete_private_connection_with_metadata`.
        """
        return response, metadata

    def pre_delete_vmware_engine_network(
        self,
        request: vmwareengine.DeleteVmwareEngineNetworkRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.DeleteVmwareEngineNetworkRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_vmware_engine_network

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_delete_vmware_engine_network(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_vmware_engine_network

        DEPRECATED. Please use the `post_delete_vmware_engine_network_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_delete_vmware_engine_network` interceptor runs
        before the `post_delete_vmware_engine_network_with_metadata` interceptor.
        """
        return response

    def post_delete_vmware_engine_network_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_vmware_engine_network

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_delete_vmware_engine_network_with_metadata`
        interceptor in new development instead of the `post_delete_vmware_engine_network` interceptor.
        When both interceptors are used, this `post_delete_vmware_engine_network_with_metadata` interceptor runs after the
        `post_delete_vmware_engine_network` interceptor. The (possibly modified) response returned by
        `post_delete_vmware_engine_network` will be passed to
        `post_delete_vmware_engine_network_with_metadata`.
        """
        return response, metadata

    def pre_fetch_network_policy_external_addresses(
        self,
        request: vmwareengine.FetchNetworkPolicyExternalAddressesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.FetchNetworkPolicyExternalAddressesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for fetch_network_policy_external_addresses

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_fetch_network_policy_external_addresses(
        self, response: vmwareengine.FetchNetworkPolicyExternalAddressesResponse
    ) -> vmwareengine.FetchNetworkPolicyExternalAddressesResponse:
        """Post-rpc interceptor for fetch_network_policy_external_addresses

        DEPRECATED. Please use the `post_fetch_network_policy_external_addresses_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_fetch_network_policy_external_addresses` interceptor runs
        before the `post_fetch_network_policy_external_addresses_with_metadata` interceptor.
        """
        return response

    def post_fetch_network_policy_external_addresses_with_metadata(
        self,
        response: vmwareengine.FetchNetworkPolicyExternalAddressesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.FetchNetworkPolicyExternalAddressesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for fetch_network_policy_external_addresses

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_fetch_network_policy_external_addresses_with_metadata`
        interceptor in new development instead of the `post_fetch_network_policy_external_addresses` interceptor.
        When both interceptors are used, this `post_fetch_network_policy_external_addresses_with_metadata` interceptor runs after the
        `post_fetch_network_policy_external_addresses` interceptor. The (possibly modified) response returned by
        `post_fetch_network_policy_external_addresses` will be passed to
        `post_fetch_network_policy_external_addresses_with_metadata`.
        """
        return response, metadata

    def pre_get_cluster(
        self,
        request: vmwareengine.GetClusterRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[vmwareengine.GetClusterRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_cluster

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_get_cluster(
        self, response: vmwareengine_resources.Cluster
    ) -> vmwareengine_resources.Cluster:
        """Post-rpc interceptor for get_cluster

        DEPRECATED. Please use the `post_get_cluster_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_get_cluster` interceptor runs
        before the `post_get_cluster_with_metadata` interceptor.
        """
        return response

    def post_get_cluster_with_metadata(
        self,
        response: vmwareengine_resources.Cluster,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[vmwareengine_resources.Cluster, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_cluster

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_get_cluster_with_metadata`
        interceptor in new development instead of the `post_get_cluster` interceptor.
        When both interceptors are used, this `post_get_cluster_with_metadata` interceptor runs after the
        `post_get_cluster` interceptor. The (possibly modified) response returned by
        `post_get_cluster` will be passed to
        `post_get_cluster_with_metadata`.
        """
        return response, metadata

    def pre_get_dns_bind_permission(
        self,
        request: vmwareengine.GetDnsBindPermissionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.GetDnsBindPermissionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_dns_bind_permission

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_get_dns_bind_permission(
        self, response: vmwareengine_resources.DnsBindPermission
    ) -> vmwareengine_resources.DnsBindPermission:
        """Post-rpc interceptor for get_dns_bind_permission

        DEPRECATED. Please use the `post_get_dns_bind_permission_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_get_dns_bind_permission` interceptor runs
        before the `post_get_dns_bind_permission_with_metadata` interceptor.
        """
        return response

    def post_get_dns_bind_permission_with_metadata(
        self,
        response: vmwareengine_resources.DnsBindPermission,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine_resources.DnsBindPermission,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_dns_bind_permission

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_get_dns_bind_permission_with_metadata`
        interceptor in new development instead of the `post_get_dns_bind_permission` interceptor.
        When both interceptors are used, this `post_get_dns_bind_permission_with_metadata` interceptor runs after the
        `post_get_dns_bind_permission` interceptor. The (possibly modified) response returned by
        `post_get_dns_bind_permission` will be passed to
        `post_get_dns_bind_permission_with_metadata`.
        """
        return response, metadata

    def pre_get_dns_forwarding(
        self,
        request: vmwareengine.GetDnsForwardingRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.GetDnsForwardingRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_dns_forwarding

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_get_dns_forwarding(
        self, response: vmwareengine_resources.DnsForwarding
    ) -> vmwareengine_resources.DnsForwarding:
        """Post-rpc interceptor for get_dns_forwarding

        DEPRECATED. Please use the `post_get_dns_forwarding_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_get_dns_forwarding` interceptor runs
        before the `post_get_dns_forwarding_with_metadata` interceptor.
        """
        return response

    def post_get_dns_forwarding_with_metadata(
        self,
        response: vmwareengine_resources.DnsForwarding,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine_resources.DnsForwarding, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_dns_forwarding

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_get_dns_forwarding_with_metadata`
        interceptor in new development instead of the `post_get_dns_forwarding` interceptor.
        When both interceptors are used, this `post_get_dns_forwarding_with_metadata` interceptor runs after the
        `post_get_dns_forwarding` interceptor. The (possibly modified) response returned by
        `post_get_dns_forwarding` will be passed to
        `post_get_dns_forwarding_with_metadata`.
        """
        return response, metadata

    def pre_get_external_access_rule(
        self,
        request: vmwareengine.GetExternalAccessRuleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.GetExternalAccessRuleRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_external_access_rule

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_get_external_access_rule(
        self, response: vmwareengine_resources.ExternalAccessRule
    ) -> vmwareengine_resources.ExternalAccessRule:
        """Post-rpc interceptor for get_external_access_rule

        DEPRECATED. Please use the `post_get_external_access_rule_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_get_external_access_rule` interceptor runs
        before the `post_get_external_access_rule_with_metadata` interceptor.
        """
        return response

    def post_get_external_access_rule_with_metadata(
        self,
        response: vmwareengine_resources.ExternalAccessRule,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine_resources.ExternalAccessRule,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_external_access_rule

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_get_external_access_rule_with_metadata`
        interceptor in new development instead of the `post_get_external_access_rule` interceptor.
        When both interceptors are used, this `post_get_external_access_rule_with_metadata` interceptor runs after the
        `post_get_external_access_rule` interceptor. The (possibly modified) response returned by
        `post_get_external_access_rule` will be passed to
        `post_get_external_access_rule_with_metadata`.
        """
        return response, metadata

    def pre_get_external_address(
        self,
        request: vmwareengine.GetExternalAddressRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.GetExternalAddressRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_external_address

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_get_external_address(
        self, response: vmwareengine_resources.ExternalAddress
    ) -> vmwareengine_resources.ExternalAddress:
        """Post-rpc interceptor for get_external_address

        DEPRECATED. Please use the `post_get_external_address_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_get_external_address` interceptor runs
        before the `post_get_external_address_with_metadata` interceptor.
        """
        return response

    def post_get_external_address_with_metadata(
        self,
        response: vmwareengine_resources.ExternalAddress,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine_resources.ExternalAddress, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_external_address

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_get_external_address_with_metadata`
        interceptor in new development instead of the `post_get_external_address` interceptor.
        When both interceptors are used, this `post_get_external_address_with_metadata` interceptor runs after the
        `post_get_external_address` interceptor. The (possibly modified) response returned by
        `post_get_external_address` will be passed to
        `post_get_external_address_with_metadata`.
        """
        return response, metadata

    def pre_get_hcx_activation_key(
        self,
        request: vmwareengine.GetHcxActivationKeyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.GetHcxActivationKeyRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_hcx_activation_key

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_get_hcx_activation_key(
        self, response: vmwareengine_resources.HcxActivationKey
    ) -> vmwareengine_resources.HcxActivationKey:
        """Post-rpc interceptor for get_hcx_activation_key

        DEPRECATED. Please use the `post_get_hcx_activation_key_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_get_hcx_activation_key` interceptor runs
        before the `post_get_hcx_activation_key_with_metadata` interceptor.
        """
        return response

    def post_get_hcx_activation_key_with_metadata(
        self,
        response: vmwareengine_resources.HcxActivationKey,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine_resources.HcxActivationKey, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_hcx_activation_key

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_get_hcx_activation_key_with_metadata`
        interceptor in new development instead of the `post_get_hcx_activation_key` interceptor.
        When both interceptors are used, this `post_get_hcx_activation_key_with_metadata` interceptor runs after the
        `post_get_hcx_activation_key` interceptor. The (possibly modified) response returned by
        `post_get_hcx_activation_key` will be passed to
        `post_get_hcx_activation_key_with_metadata`.
        """
        return response, metadata

    def pre_get_logging_server(
        self,
        request: vmwareengine.GetLoggingServerRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.GetLoggingServerRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_logging_server

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_get_logging_server(
        self, response: vmwareengine_resources.LoggingServer
    ) -> vmwareengine_resources.LoggingServer:
        """Post-rpc interceptor for get_logging_server

        DEPRECATED. Please use the `post_get_logging_server_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_get_logging_server` interceptor runs
        before the `post_get_logging_server_with_metadata` interceptor.
        """
        return response

    def post_get_logging_server_with_metadata(
        self,
        response: vmwareengine_resources.LoggingServer,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine_resources.LoggingServer, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_logging_server

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_get_logging_server_with_metadata`
        interceptor in new development instead of the `post_get_logging_server` interceptor.
        When both interceptors are used, this `post_get_logging_server_with_metadata` interceptor runs after the
        `post_get_logging_server` interceptor. The (possibly modified) response returned by
        `post_get_logging_server` will be passed to
        `post_get_logging_server_with_metadata`.
        """
        return response, metadata

    def pre_get_management_dns_zone_binding(
        self,
        request: vmwareengine.GetManagementDnsZoneBindingRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.GetManagementDnsZoneBindingRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_management_dns_zone_binding

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_get_management_dns_zone_binding(
        self, response: vmwareengine_resources.ManagementDnsZoneBinding
    ) -> vmwareengine_resources.ManagementDnsZoneBinding:
        """Post-rpc interceptor for get_management_dns_zone_binding

        DEPRECATED. Please use the `post_get_management_dns_zone_binding_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_get_management_dns_zone_binding` interceptor runs
        before the `post_get_management_dns_zone_binding_with_metadata` interceptor.
        """
        return response

    def post_get_management_dns_zone_binding_with_metadata(
        self,
        response: vmwareengine_resources.ManagementDnsZoneBinding,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine_resources.ManagementDnsZoneBinding,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_management_dns_zone_binding

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_get_management_dns_zone_binding_with_metadata`
        interceptor in new development instead of the `post_get_management_dns_zone_binding` interceptor.
        When both interceptors are used, this `post_get_management_dns_zone_binding_with_metadata` interceptor runs after the
        `post_get_management_dns_zone_binding` interceptor. The (possibly modified) response returned by
        `post_get_management_dns_zone_binding` will be passed to
        `post_get_management_dns_zone_binding_with_metadata`.
        """
        return response, metadata

    def pre_get_network_peering(
        self,
        request: vmwareengine.GetNetworkPeeringRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.GetNetworkPeeringRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_network_peering

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_get_network_peering(
        self, response: vmwareengine_resources.NetworkPeering
    ) -> vmwareengine_resources.NetworkPeering:
        """Post-rpc interceptor for get_network_peering

        DEPRECATED. Please use the `post_get_network_peering_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_get_network_peering` interceptor runs
        before the `post_get_network_peering_with_metadata` interceptor.
        """
        return response

    def post_get_network_peering_with_metadata(
        self,
        response: vmwareengine_resources.NetworkPeering,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine_resources.NetworkPeering, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_network_peering

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_get_network_peering_with_metadata`
        interceptor in new development instead of the `post_get_network_peering` interceptor.
        When both interceptors are used, this `post_get_network_peering_with_metadata` interceptor runs after the
        `post_get_network_peering` interceptor. The (possibly modified) response returned by
        `post_get_network_peering` will be passed to
        `post_get_network_peering_with_metadata`.
        """
        return response, metadata

    def pre_get_network_policy(
        self,
        request: vmwareengine.GetNetworkPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.GetNetworkPolicyRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_network_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_get_network_policy(
        self, response: vmwareengine_resources.NetworkPolicy
    ) -> vmwareengine_resources.NetworkPolicy:
        """Post-rpc interceptor for get_network_policy

        DEPRECATED. Please use the `post_get_network_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_get_network_policy` interceptor runs
        before the `post_get_network_policy_with_metadata` interceptor.
        """
        return response

    def post_get_network_policy_with_metadata(
        self,
        response: vmwareengine_resources.NetworkPolicy,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine_resources.NetworkPolicy, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_network_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_get_network_policy_with_metadata`
        interceptor in new development instead of the `post_get_network_policy` interceptor.
        When both interceptors are used, this `post_get_network_policy_with_metadata` interceptor runs after the
        `post_get_network_policy` interceptor. The (possibly modified) response returned by
        `post_get_network_policy` will be passed to
        `post_get_network_policy_with_metadata`.
        """
        return response, metadata

    def pre_get_node(
        self,
        request: vmwareengine.GetNodeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[vmwareengine.GetNodeRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_node

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_get_node(
        self, response: vmwareengine_resources.Node
    ) -> vmwareengine_resources.Node:
        """Post-rpc interceptor for get_node

        DEPRECATED. Please use the `post_get_node_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_get_node` interceptor runs
        before the `post_get_node_with_metadata` interceptor.
        """
        return response

    def post_get_node_with_metadata(
        self,
        response: vmwareengine_resources.Node,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[vmwareengine_resources.Node, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_node

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_get_node_with_metadata`
        interceptor in new development instead of the `post_get_node` interceptor.
        When both interceptors are used, this `post_get_node_with_metadata` interceptor runs after the
        `post_get_node` interceptor. The (possibly modified) response returned by
        `post_get_node` will be passed to
        `post_get_node_with_metadata`.
        """
        return response, metadata

    def pre_get_node_type(
        self,
        request: vmwareengine.GetNodeTypeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.GetNodeTypeRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_node_type

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_get_node_type(
        self, response: vmwareengine_resources.NodeType
    ) -> vmwareengine_resources.NodeType:
        """Post-rpc interceptor for get_node_type

        DEPRECATED. Please use the `post_get_node_type_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_get_node_type` interceptor runs
        before the `post_get_node_type_with_metadata` interceptor.
        """
        return response

    def post_get_node_type_with_metadata(
        self,
        response: vmwareengine_resources.NodeType,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine_resources.NodeType, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_node_type

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_get_node_type_with_metadata`
        interceptor in new development instead of the `post_get_node_type` interceptor.
        When both interceptors are used, this `post_get_node_type_with_metadata` interceptor runs after the
        `post_get_node_type` interceptor. The (possibly modified) response returned by
        `post_get_node_type` will be passed to
        `post_get_node_type_with_metadata`.
        """
        return response, metadata

    def pre_get_private_cloud(
        self,
        request: vmwareengine.GetPrivateCloudRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.GetPrivateCloudRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_private_cloud

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_get_private_cloud(
        self, response: vmwareengine_resources.PrivateCloud
    ) -> vmwareengine_resources.PrivateCloud:
        """Post-rpc interceptor for get_private_cloud

        DEPRECATED. Please use the `post_get_private_cloud_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_get_private_cloud` interceptor runs
        before the `post_get_private_cloud_with_metadata` interceptor.
        """
        return response

    def post_get_private_cloud_with_metadata(
        self,
        response: vmwareengine_resources.PrivateCloud,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine_resources.PrivateCloud, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_private_cloud

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_get_private_cloud_with_metadata`
        interceptor in new development instead of the `post_get_private_cloud` interceptor.
        When both interceptors are used, this `post_get_private_cloud_with_metadata` interceptor runs after the
        `post_get_private_cloud` interceptor. The (possibly modified) response returned by
        `post_get_private_cloud` will be passed to
        `post_get_private_cloud_with_metadata`.
        """
        return response, metadata

    def pre_get_private_connection(
        self,
        request: vmwareengine.GetPrivateConnectionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.GetPrivateConnectionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_private_connection

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_get_private_connection(
        self, response: vmwareengine_resources.PrivateConnection
    ) -> vmwareengine_resources.PrivateConnection:
        """Post-rpc interceptor for get_private_connection

        DEPRECATED. Please use the `post_get_private_connection_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_get_private_connection` interceptor runs
        before the `post_get_private_connection_with_metadata` interceptor.
        """
        return response

    def post_get_private_connection_with_metadata(
        self,
        response: vmwareengine_resources.PrivateConnection,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine_resources.PrivateConnection,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_private_connection

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_get_private_connection_with_metadata`
        interceptor in new development instead of the `post_get_private_connection` interceptor.
        When both interceptors are used, this `post_get_private_connection_with_metadata` interceptor runs after the
        `post_get_private_connection` interceptor. The (possibly modified) response returned by
        `post_get_private_connection` will be passed to
        `post_get_private_connection_with_metadata`.
        """
        return response, metadata

    def pre_get_subnet(
        self,
        request: vmwareengine.GetSubnetRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[vmwareengine.GetSubnetRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_subnet

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_get_subnet(
        self, response: vmwareengine_resources.Subnet
    ) -> vmwareengine_resources.Subnet:
        """Post-rpc interceptor for get_subnet

        DEPRECATED. Please use the `post_get_subnet_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_get_subnet` interceptor runs
        before the `post_get_subnet_with_metadata` interceptor.
        """
        return response

    def post_get_subnet_with_metadata(
        self,
        response: vmwareengine_resources.Subnet,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[vmwareengine_resources.Subnet, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_subnet

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_get_subnet_with_metadata`
        interceptor in new development instead of the `post_get_subnet` interceptor.
        When both interceptors are used, this `post_get_subnet_with_metadata` interceptor runs after the
        `post_get_subnet` interceptor. The (possibly modified) response returned by
        `post_get_subnet` will be passed to
        `post_get_subnet_with_metadata`.
        """
        return response, metadata

    def pre_get_vmware_engine_network(
        self,
        request: vmwareengine.GetVmwareEngineNetworkRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.GetVmwareEngineNetworkRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_vmware_engine_network

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_get_vmware_engine_network(
        self, response: vmwareengine_resources.VmwareEngineNetwork
    ) -> vmwareengine_resources.VmwareEngineNetwork:
        """Post-rpc interceptor for get_vmware_engine_network

        DEPRECATED. Please use the `post_get_vmware_engine_network_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_get_vmware_engine_network` interceptor runs
        before the `post_get_vmware_engine_network_with_metadata` interceptor.
        """
        return response

    def post_get_vmware_engine_network_with_metadata(
        self,
        response: vmwareengine_resources.VmwareEngineNetwork,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine_resources.VmwareEngineNetwork,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_vmware_engine_network

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_get_vmware_engine_network_with_metadata`
        interceptor in new development instead of the `post_get_vmware_engine_network` interceptor.
        When both interceptors are used, this `post_get_vmware_engine_network_with_metadata` interceptor runs after the
        `post_get_vmware_engine_network` interceptor. The (possibly modified) response returned by
        `post_get_vmware_engine_network` will be passed to
        `post_get_vmware_engine_network_with_metadata`.
        """
        return response, metadata

    def pre_grant_dns_bind_permission(
        self,
        request: vmwareengine.GrantDnsBindPermissionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.GrantDnsBindPermissionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for grant_dns_bind_permission

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_grant_dns_bind_permission(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for grant_dns_bind_permission

        DEPRECATED. Please use the `post_grant_dns_bind_permission_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_grant_dns_bind_permission` interceptor runs
        before the `post_grant_dns_bind_permission_with_metadata` interceptor.
        """
        return response

    def post_grant_dns_bind_permission_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for grant_dns_bind_permission

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_grant_dns_bind_permission_with_metadata`
        interceptor in new development instead of the `post_grant_dns_bind_permission` interceptor.
        When both interceptors are used, this `post_grant_dns_bind_permission_with_metadata` interceptor runs after the
        `post_grant_dns_bind_permission` interceptor. The (possibly modified) response returned by
        `post_grant_dns_bind_permission` will be passed to
        `post_grant_dns_bind_permission_with_metadata`.
        """
        return response, metadata

    def pre_list_clusters(
        self,
        request: vmwareengine.ListClustersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.ListClustersRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_clusters

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_list_clusters(
        self, response: vmwareengine.ListClustersResponse
    ) -> vmwareengine.ListClustersResponse:
        """Post-rpc interceptor for list_clusters

        DEPRECATED. Please use the `post_list_clusters_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_list_clusters` interceptor runs
        before the `post_list_clusters_with_metadata` interceptor.
        """
        return response

    def post_list_clusters_with_metadata(
        self,
        response: vmwareengine.ListClustersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.ListClustersResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_clusters

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_list_clusters_with_metadata`
        interceptor in new development instead of the `post_list_clusters` interceptor.
        When both interceptors are used, this `post_list_clusters_with_metadata` interceptor runs after the
        `post_list_clusters` interceptor. The (possibly modified) response returned by
        `post_list_clusters` will be passed to
        `post_list_clusters_with_metadata`.
        """
        return response, metadata

    def pre_list_external_access_rules(
        self,
        request: vmwareengine.ListExternalAccessRulesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.ListExternalAccessRulesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_external_access_rules

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_list_external_access_rules(
        self, response: vmwareengine.ListExternalAccessRulesResponse
    ) -> vmwareengine.ListExternalAccessRulesResponse:
        """Post-rpc interceptor for list_external_access_rules

        DEPRECATED. Please use the `post_list_external_access_rules_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_list_external_access_rules` interceptor runs
        before the `post_list_external_access_rules_with_metadata` interceptor.
        """
        return response

    def post_list_external_access_rules_with_metadata(
        self,
        response: vmwareengine.ListExternalAccessRulesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.ListExternalAccessRulesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_external_access_rules

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_list_external_access_rules_with_metadata`
        interceptor in new development instead of the `post_list_external_access_rules` interceptor.
        When both interceptors are used, this `post_list_external_access_rules_with_metadata` interceptor runs after the
        `post_list_external_access_rules` interceptor. The (possibly modified) response returned by
        `post_list_external_access_rules` will be passed to
        `post_list_external_access_rules_with_metadata`.
        """
        return response, metadata

    def pre_list_external_addresses(
        self,
        request: vmwareengine.ListExternalAddressesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.ListExternalAddressesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_external_addresses

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_list_external_addresses(
        self, response: vmwareengine.ListExternalAddressesResponse
    ) -> vmwareengine.ListExternalAddressesResponse:
        """Post-rpc interceptor for list_external_addresses

        DEPRECATED. Please use the `post_list_external_addresses_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_list_external_addresses` interceptor runs
        before the `post_list_external_addresses_with_metadata` interceptor.
        """
        return response

    def post_list_external_addresses_with_metadata(
        self,
        response: vmwareengine.ListExternalAddressesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.ListExternalAddressesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_external_addresses

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_list_external_addresses_with_metadata`
        interceptor in new development instead of the `post_list_external_addresses` interceptor.
        When both interceptors are used, this `post_list_external_addresses_with_metadata` interceptor runs after the
        `post_list_external_addresses` interceptor. The (possibly modified) response returned by
        `post_list_external_addresses` will be passed to
        `post_list_external_addresses_with_metadata`.
        """
        return response, metadata

    def pre_list_hcx_activation_keys(
        self,
        request: vmwareengine.ListHcxActivationKeysRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.ListHcxActivationKeysRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_hcx_activation_keys

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_list_hcx_activation_keys(
        self, response: vmwareengine.ListHcxActivationKeysResponse
    ) -> vmwareengine.ListHcxActivationKeysResponse:
        """Post-rpc interceptor for list_hcx_activation_keys

        DEPRECATED. Please use the `post_list_hcx_activation_keys_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_list_hcx_activation_keys` interceptor runs
        before the `post_list_hcx_activation_keys_with_metadata` interceptor.
        """
        return response

    def post_list_hcx_activation_keys_with_metadata(
        self,
        response: vmwareengine.ListHcxActivationKeysResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.ListHcxActivationKeysResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_hcx_activation_keys

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_list_hcx_activation_keys_with_metadata`
        interceptor in new development instead of the `post_list_hcx_activation_keys` interceptor.
        When both interceptors are used, this `post_list_hcx_activation_keys_with_metadata` interceptor runs after the
        `post_list_hcx_activation_keys` interceptor. The (possibly modified) response returned by
        `post_list_hcx_activation_keys` will be passed to
        `post_list_hcx_activation_keys_with_metadata`.
        """
        return response, metadata

    def pre_list_logging_servers(
        self,
        request: vmwareengine.ListLoggingServersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.ListLoggingServersRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_logging_servers

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_list_logging_servers(
        self, response: vmwareengine.ListLoggingServersResponse
    ) -> vmwareengine.ListLoggingServersResponse:
        """Post-rpc interceptor for list_logging_servers

        DEPRECATED. Please use the `post_list_logging_servers_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_list_logging_servers` interceptor runs
        before the `post_list_logging_servers_with_metadata` interceptor.
        """
        return response

    def post_list_logging_servers_with_metadata(
        self,
        response: vmwareengine.ListLoggingServersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.ListLoggingServersResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_logging_servers

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_list_logging_servers_with_metadata`
        interceptor in new development instead of the `post_list_logging_servers` interceptor.
        When both interceptors are used, this `post_list_logging_servers_with_metadata` interceptor runs after the
        `post_list_logging_servers` interceptor. The (possibly modified) response returned by
        `post_list_logging_servers` will be passed to
        `post_list_logging_servers_with_metadata`.
        """
        return response, metadata

    def pre_list_management_dns_zone_bindings(
        self,
        request: vmwareengine.ListManagementDnsZoneBindingsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.ListManagementDnsZoneBindingsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_management_dns_zone_bindings

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_list_management_dns_zone_bindings(
        self, response: vmwareengine.ListManagementDnsZoneBindingsResponse
    ) -> vmwareengine.ListManagementDnsZoneBindingsResponse:
        """Post-rpc interceptor for list_management_dns_zone_bindings

        DEPRECATED. Please use the `post_list_management_dns_zone_bindings_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_list_management_dns_zone_bindings` interceptor runs
        before the `post_list_management_dns_zone_bindings_with_metadata` interceptor.
        """
        return response

    def post_list_management_dns_zone_bindings_with_metadata(
        self,
        response: vmwareengine.ListManagementDnsZoneBindingsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.ListManagementDnsZoneBindingsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_management_dns_zone_bindings

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_list_management_dns_zone_bindings_with_metadata`
        interceptor in new development instead of the `post_list_management_dns_zone_bindings` interceptor.
        When both interceptors are used, this `post_list_management_dns_zone_bindings_with_metadata` interceptor runs after the
        `post_list_management_dns_zone_bindings` interceptor. The (possibly modified) response returned by
        `post_list_management_dns_zone_bindings` will be passed to
        `post_list_management_dns_zone_bindings_with_metadata`.
        """
        return response, metadata

    def pre_list_network_peerings(
        self,
        request: vmwareengine.ListNetworkPeeringsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.ListNetworkPeeringsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_network_peerings

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_list_network_peerings(
        self, response: vmwareengine.ListNetworkPeeringsResponse
    ) -> vmwareengine.ListNetworkPeeringsResponse:
        """Post-rpc interceptor for list_network_peerings

        DEPRECATED. Please use the `post_list_network_peerings_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_list_network_peerings` interceptor runs
        before the `post_list_network_peerings_with_metadata` interceptor.
        """
        return response

    def post_list_network_peerings_with_metadata(
        self,
        response: vmwareengine.ListNetworkPeeringsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.ListNetworkPeeringsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_network_peerings

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_list_network_peerings_with_metadata`
        interceptor in new development instead of the `post_list_network_peerings` interceptor.
        When both interceptors are used, this `post_list_network_peerings_with_metadata` interceptor runs after the
        `post_list_network_peerings` interceptor. The (possibly modified) response returned by
        `post_list_network_peerings` will be passed to
        `post_list_network_peerings_with_metadata`.
        """
        return response, metadata

    def pre_list_network_policies(
        self,
        request: vmwareengine.ListNetworkPoliciesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.ListNetworkPoliciesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_network_policies

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_list_network_policies(
        self, response: vmwareengine.ListNetworkPoliciesResponse
    ) -> vmwareengine.ListNetworkPoliciesResponse:
        """Post-rpc interceptor for list_network_policies

        DEPRECATED. Please use the `post_list_network_policies_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_list_network_policies` interceptor runs
        before the `post_list_network_policies_with_metadata` interceptor.
        """
        return response

    def post_list_network_policies_with_metadata(
        self,
        response: vmwareengine.ListNetworkPoliciesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.ListNetworkPoliciesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_network_policies

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_list_network_policies_with_metadata`
        interceptor in new development instead of the `post_list_network_policies` interceptor.
        When both interceptors are used, this `post_list_network_policies_with_metadata` interceptor runs after the
        `post_list_network_policies` interceptor. The (possibly modified) response returned by
        `post_list_network_policies` will be passed to
        `post_list_network_policies_with_metadata`.
        """
        return response, metadata

    def pre_list_nodes(
        self,
        request: vmwareengine.ListNodesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[vmwareengine.ListNodesRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_nodes

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_list_nodes(
        self, response: vmwareengine.ListNodesResponse
    ) -> vmwareengine.ListNodesResponse:
        """Post-rpc interceptor for list_nodes

        DEPRECATED. Please use the `post_list_nodes_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_list_nodes` interceptor runs
        before the `post_list_nodes_with_metadata` interceptor.
        """
        return response

    def post_list_nodes_with_metadata(
        self,
        response: vmwareengine.ListNodesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[vmwareengine.ListNodesResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_nodes

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_list_nodes_with_metadata`
        interceptor in new development instead of the `post_list_nodes` interceptor.
        When both interceptors are used, this `post_list_nodes_with_metadata` interceptor runs after the
        `post_list_nodes` interceptor. The (possibly modified) response returned by
        `post_list_nodes` will be passed to
        `post_list_nodes_with_metadata`.
        """
        return response, metadata

    def pre_list_node_types(
        self,
        request: vmwareengine.ListNodeTypesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.ListNodeTypesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_node_types

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_list_node_types(
        self, response: vmwareengine.ListNodeTypesResponse
    ) -> vmwareengine.ListNodeTypesResponse:
        """Post-rpc interceptor for list_node_types

        DEPRECATED. Please use the `post_list_node_types_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_list_node_types` interceptor runs
        before the `post_list_node_types_with_metadata` interceptor.
        """
        return response

    def post_list_node_types_with_metadata(
        self,
        response: vmwareengine.ListNodeTypesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.ListNodeTypesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_node_types

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_list_node_types_with_metadata`
        interceptor in new development instead of the `post_list_node_types` interceptor.
        When both interceptors are used, this `post_list_node_types_with_metadata` interceptor runs after the
        `post_list_node_types` interceptor. The (possibly modified) response returned by
        `post_list_node_types` will be passed to
        `post_list_node_types_with_metadata`.
        """
        return response, metadata

    def pre_list_peering_routes(
        self,
        request: vmwareengine.ListPeeringRoutesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.ListPeeringRoutesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_peering_routes

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_list_peering_routes(
        self, response: vmwareengine.ListPeeringRoutesResponse
    ) -> vmwareengine.ListPeeringRoutesResponse:
        """Post-rpc interceptor for list_peering_routes

        DEPRECATED. Please use the `post_list_peering_routes_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_list_peering_routes` interceptor runs
        before the `post_list_peering_routes_with_metadata` interceptor.
        """
        return response

    def post_list_peering_routes_with_metadata(
        self,
        response: vmwareengine.ListPeeringRoutesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.ListPeeringRoutesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_peering_routes

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_list_peering_routes_with_metadata`
        interceptor in new development instead of the `post_list_peering_routes` interceptor.
        When both interceptors are used, this `post_list_peering_routes_with_metadata` interceptor runs after the
        `post_list_peering_routes` interceptor. The (possibly modified) response returned by
        `post_list_peering_routes` will be passed to
        `post_list_peering_routes_with_metadata`.
        """
        return response, metadata

    def pre_list_private_clouds(
        self,
        request: vmwareengine.ListPrivateCloudsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.ListPrivateCloudsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_private_clouds

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_list_private_clouds(
        self, response: vmwareengine.ListPrivateCloudsResponse
    ) -> vmwareengine.ListPrivateCloudsResponse:
        """Post-rpc interceptor for list_private_clouds

        DEPRECATED. Please use the `post_list_private_clouds_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_list_private_clouds` interceptor runs
        before the `post_list_private_clouds_with_metadata` interceptor.
        """
        return response

    def post_list_private_clouds_with_metadata(
        self,
        response: vmwareengine.ListPrivateCloudsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.ListPrivateCloudsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_private_clouds

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_list_private_clouds_with_metadata`
        interceptor in new development instead of the `post_list_private_clouds` interceptor.
        When both interceptors are used, this `post_list_private_clouds_with_metadata` interceptor runs after the
        `post_list_private_clouds` interceptor. The (possibly modified) response returned by
        `post_list_private_clouds` will be passed to
        `post_list_private_clouds_with_metadata`.
        """
        return response, metadata

    def pre_list_private_connection_peering_routes(
        self,
        request: vmwareengine.ListPrivateConnectionPeeringRoutesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.ListPrivateConnectionPeeringRoutesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_private_connection_peering_routes

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_list_private_connection_peering_routes(
        self, response: vmwareengine.ListPrivateConnectionPeeringRoutesResponse
    ) -> vmwareengine.ListPrivateConnectionPeeringRoutesResponse:
        """Post-rpc interceptor for list_private_connection_peering_routes

        DEPRECATED. Please use the `post_list_private_connection_peering_routes_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_list_private_connection_peering_routes` interceptor runs
        before the `post_list_private_connection_peering_routes_with_metadata` interceptor.
        """
        return response

    def post_list_private_connection_peering_routes_with_metadata(
        self,
        response: vmwareengine.ListPrivateConnectionPeeringRoutesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.ListPrivateConnectionPeeringRoutesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_private_connection_peering_routes

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_list_private_connection_peering_routes_with_metadata`
        interceptor in new development instead of the `post_list_private_connection_peering_routes` interceptor.
        When both interceptors are used, this `post_list_private_connection_peering_routes_with_metadata` interceptor runs after the
        `post_list_private_connection_peering_routes` interceptor. The (possibly modified) response returned by
        `post_list_private_connection_peering_routes` will be passed to
        `post_list_private_connection_peering_routes_with_metadata`.
        """
        return response, metadata

    def pre_list_private_connections(
        self,
        request: vmwareengine.ListPrivateConnectionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.ListPrivateConnectionsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_private_connections

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_list_private_connections(
        self, response: vmwareengine.ListPrivateConnectionsResponse
    ) -> vmwareengine.ListPrivateConnectionsResponse:
        """Post-rpc interceptor for list_private_connections

        DEPRECATED. Please use the `post_list_private_connections_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_list_private_connections` interceptor runs
        before the `post_list_private_connections_with_metadata` interceptor.
        """
        return response

    def post_list_private_connections_with_metadata(
        self,
        response: vmwareengine.ListPrivateConnectionsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.ListPrivateConnectionsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_private_connections

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_list_private_connections_with_metadata`
        interceptor in new development instead of the `post_list_private_connections` interceptor.
        When both interceptors are used, this `post_list_private_connections_with_metadata` interceptor runs after the
        `post_list_private_connections` interceptor. The (possibly modified) response returned by
        `post_list_private_connections` will be passed to
        `post_list_private_connections_with_metadata`.
        """
        return response, metadata

    def pre_list_subnets(
        self,
        request: vmwareengine.ListSubnetsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.ListSubnetsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_subnets

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_list_subnets(
        self, response: vmwareengine.ListSubnetsResponse
    ) -> vmwareengine.ListSubnetsResponse:
        """Post-rpc interceptor for list_subnets

        DEPRECATED. Please use the `post_list_subnets_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_list_subnets` interceptor runs
        before the `post_list_subnets_with_metadata` interceptor.
        """
        return response

    def post_list_subnets_with_metadata(
        self,
        response: vmwareengine.ListSubnetsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.ListSubnetsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_subnets

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_list_subnets_with_metadata`
        interceptor in new development instead of the `post_list_subnets` interceptor.
        When both interceptors are used, this `post_list_subnets_with_metadata` interceptor runs after the
        `post_list_subnets` interceptor. The (possibly modified) response returned by
        `post_list_subnets` will be passed to
        `post_list_subnets_with_metadata`.
        """
        return response, metadata

    def pre_list_vmware_engine_networks(
        self,
        request: vmwareengine.ListVmwareEngineNetworksRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.ListVmwareEngineNetworksRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_vmware_engine_networks

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_list_vmware_engine_networks(
        self, response: vmwareengine.ListVmwareEngineNetworksResponse
    ) -> vmwareengine.ListVmwareEngineNetworksResponse:
        """Post-rpc interceptor for list_vmware_engine_networks

        DEPRECATED. Please use the `post_list_vmware_engine_networks_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_list_vmware_engine_networks` interceptor runs
        before the `post_list_vmware_engine_networks_with_metadata` interceptor.
        """
        return response

    def post_list_vmware_engine_networks_with_metadata(
        self,
        response: vmwareengine.ListVmwareEngineNetworksResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.ListVmwareEngineNetworksResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_vmware_engine_networks

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_list_vmware_engine_networks_with_metadata`
        interceptor in new development instead of the `post_list_vmware_engine_networks` interceptor.
        When both interceptors are used, this `post_list_vmware_engine_networks_with_metadata` interceptor runs after the
        `post_list_vmware_engine_networks` interceptor. The (possibly modified) response returned by
        `post_list_vmware_engine_networks` will be passed to
        `post_list_vmware_engine_networks_with_metadata`.
        """
        return response, metadata

    def pre_repair_management_dns_zone_binding(
        self,
        request: vmwareengine.RepairManagementDnsZoneBindingRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.RepairManagementDnsZoneBindingRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for repair_management_dns_zone_binding

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_repair_management_dns_zone_binding(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for repair_management_dns_zone_binding

        DEPRECATED. Please use the `post_repair_management_dns_zone_binding_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_repair_management_dns_zone_binding` interceptor runs
        before the `post_repair_management_dns_zone_binding_with_metadata` interceptor.
        """
        return response

    def post_repair_management_dns_zone_binding_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for repair_management_dns_zone_binding

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_repair_management_dns_zone_binding_with_metadata`
        interceptor in new development instead of the `post_repair_management_dns_zone_binding` interceptor.
        When both interceptors are used, this `post_repair_management_dns_zone_binding_with_metadata` interceptor runs after the
        `post_repair_management_dns_zone_binding` interceptor. The (possibly modified) response returned by
        `post_repair_management_dns_zone_binding` will be passed to
        `post_repair_management_dns_zone_binding_with_metadata`.
        """
        return response, metadata

    def pre_reset_nsx_credentials(
        self,
        request: vmwareengine.ResetNsxCredentialsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.ResetNsxCredentialsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for reset_nsx_credentials

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_reset_nsx_credentials(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for reset_nsx_credentials

        DEPRECATED. Please use the `post_reset_nsx_credentials_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_reset_nsx_credentials` interceptor runs
        before the `post_reset_nsx_credentials_with_metadata` interceptor.
        """
        return response

    def post_reset_nsx_credentials_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for reset_nsx_credentials

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_reset_nsx_credentials_with_metadata`
        interceptor in new development instead of the `post_reset_nsx_credentials` interceptor.
        When both interceptors are used, this `post_reset_nsx_credentials_with_metadata` interceptor runs after the
        `post_reset_nsx_credentials` interceptor. The (possibly modified) response returned by
        `post_reset_nsx_credentials` will be passed to
        `post_reset_nsx_credentials_with_metadata`.
        """
        return response, metadata

    def pre_reset_vcenter_credentials(
        self,
        request: vmwareengine.ResetVcenterCredentialsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.ResetVcenterCredentialsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for reset_vcenter_credentials

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_reset_vcenter_credentials(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for reset_vcenter_credentials

        DEPRECATED. Please use the `post_reset_vcenter_credentials_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_reset_vcenter_credentials` interceptor runs
        before the `post_reset_vcenter_credentials_with_metadata` interceptor.
        """
        return response

    def post_reset_vcenter_credentials_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for reset_vcenter_credentials

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_reset_vcenter_credentials_with_metadata`
        interceptor in new development instead of the `post_reset_vcenter_credentials` interceptor.
        When both interceptors are used, this `post_reset_vcenter_credentials_with_metadata` interceptor runs after the
        `post_reset_vcenter_credentials` interceptor. The (possibly modified) response returned by
        `post_reset_vcenter_credentials` will be passed to
        `post_reset_vcenter_credentials_with_metadata`.
        """
        return response, metadata

    def pre_revoke_dns_bind_permission(
        self,
        request: vmwareengine.RevokeDnsBindPermissionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.RevokeDnsBindPermissionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for revoke_dns_bind_permission

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_revoke_dns_bind_permission(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for revoke_dns_bind_permission

        DEPRECATED. Please use the `post_revoke_dns_bind_permission_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_revoke_dns_bind_permission` interceptor runs
        before the `post_revoke_dns_bind_permission_with_metadata` interceptor.
        """
        return response

    def post_revoke_dns_bind_permission_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for revoke_dns_bind_permission

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_revoke_dns_bind_permission_with_metadata`
        interceptor in new development instead of the `post_revoke_dns_bind_permission` interceptor.
        When both interceptors are used, this `post_revoke_dns_bind_permission_with_metadata` interceptor runs after the
        `post_revoke_dns_bind_permission` interceptor. The (possibly modified) response returned by
        `post_revoke_dns_bind_permission` will be passed to
        `post_revoke_dns_bind_permission_with_metadata`.
        """
        return response, metadata

    def pre_show_nsx_credentials(
        self,
        request: vmwareengine.ShowNsxCredentialsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.ShowNsxCredentialsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for show_nsx_credentials

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_show_nsx_credentials(
        self, response: vmwareengine_resources.Credentials
    ) -> vmwareengine_resources.Credentials:
        """Post-rpc interceptor for show_nsx_credentials

        DEPRECATED. Please use the `post_show_nsx_credentials_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_show_nsx_credentials` interceptor runs
        before the `post_show_nsx_credentials_with_metadata` interceptor.
        """
        return response

    def post_show_nsx_credentials_with_metadata(
        self,
        response: vmwareengine_resources.Credentials,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine_resources.Credentials, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for show_nsx_credentials

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_show_nsx_credentials_with_metadata`
        interceptor in new development instead of the `post_show_nsx_credentials` interceptor.
        When both interceptors are used, this `post_show_nsx_credentials_with_metadata` interceptor runs after the
        `post_show_nsx_credentials` interceptor. The (possibly modified) response returned by
        `post_show_nsx_credentials` will be passed to
        `post_show_nsx_credentials_with_metadata`.
        """
        return response, metadata

    def pre_show_vcenter_credentials(
        self,
        request: vmwareengine.ShowVcenterCredentialsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.ShowVcenterCredentialsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for show_vcenter_credentials

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_show_vcenter_credentials(
        self, response: vmwareengine_resources.Credentials
    ) -> vmwareengine_resources.Credentials:
        """Post-rpc interceptor for show_vcenter_credentials

        DEPRECATED. Please use the `post_show_vcenter_credentials_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_show_vcenter_credentials` interceptor runs
        before the `post_show_vcenter_credentials_with_metadata` interceptor.
        """
        return response

    def post_show_vcenter_credentials_with_metadata(
        self,
        response: vmwareengine_resources.Credentials,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine_resources.Credentials, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for show_vcenter_credentials

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_show_vcenter_credentials_with_metadata`
        interceptor in new development instead of the `post_show_vcenter_credentials` interceptor.
        When both interceptors are used, this `post_show_vcenter_credentials_with_metadata` interceptor runs after the
        `post_show_vcenter_credentials` interceptor. The (possibly modified) response returned by
        `post_show_vcenter_credentials` will be passed to
        `post_show_vcenter_credentials_with_metadata`.
        """
        return response, metadata

    def pre_undelete_private_cloud(
        self,
        request: vmwareengine.UndeletePrivateCloudRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.UndeletePrivateCloudRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for undelete_private_cloud

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_undelete_private_cloud(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for undelete_private_cloud

        DEPRECATED. Please use the `post_undelete_private_cloud_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_undelete_private_cloud` interceptor runs
        before the `post_undelete_private_cloud_with_metadata` interceptor.
        """
        return response

    def post_undelete_private_cloud_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for undelete_private_cloud

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_undelete_private_cloud_with_metadata`
        interceptor in new development instead of the `post_undelete_private_cloud` interceptor.
        When both interceptors are used, this `post_undelete_private_cloud_with_metadata` interceptor runs after the
        `post_undelete_private_cloud` interceptor. The (possibly modified) response returned by
        `post_undelete_private_cloud` will be passed to
        `post_undelete_private_cloud_with_metadata`.
        """
        return response, metadata

    def pre_update_cluster(
        self,
        request: vmwareengine.UpdateClusterRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.UpdateClusterRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_cluster

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_update_cluster(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_cluster

        DEPRECATED. Please use the `post_update_cluster_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_update_cluster` interceptor runs
        before the `post_update_cluster_with_metadata` interceptor.
        """
        return response

    def post_update_cluster_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_cluster

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_update_cluster_with_metadata`
        interceptor in new development instead of the `post_update_cluster` interceptor.
        When both interceptors are used, this `post_update_cluster_with_metadata` interceptor runs after the
        `post_update_cluster` interceptor. The (possibly modified) response returned by
        `post_update_cluster` will be passed to
        `post_update_cluster_with_metadata`.
        """
        return response, metadata

    def pre_update_dns_forwarding(
        self,
        request: vmwareengine.UpdateDnsForwardingRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.UpdateDnsForwardingRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_dns_forwarding

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_update_dns_forwarding(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_dns_forwarding

        DEPRECATED. Please use the `post_update_dns_forwarding_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_update_dns_forwarding` interceptor runs
        before the `post_update_dns_forwarding_with_metadata` interceptor.
        """
        return response

    def post_update_dns_forwarding_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_dns_forwarding

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_update_dns_forwarding_with_metadata`
        interceptor in new development instead of the `post_update_dns_forwarding` interceptor.
        When both interceptors are used, this `post_update_dns_forwarding_with_metadata` interceptor runs after the
        `post_update_dns_forwarding` interceptor. The (possibly modified) response returned by
        `post_update_dns_forwarding` will be passed to
        `post_update_dns_forwarding_with_metadata`.
        """
        return response, metadata

    def pre_update_external_access_rule(
        self,
        request: vmwareengine.UpdateExternalAccessRuleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.UpdateExternalAccessRuleRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_external_access_rule

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_update_external_access_rule(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_external_access_rule

        DEPRECATED. Please use the `post_update_external_access_rule_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_update_external_access_rule` interceptor runs
        before the `post_update_external_access_rule_with_metadata` interceptor.
        """
        return response

    def post_update_external_access_rule_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_external_access_rule

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_update_external_access_rule_with_metadata`
        interceptor in new development instead of the `post_update_external_access_rule` interceptor.
        When both interceptors are used, this `post_update_external_access_rule_with_metadata` interceptor runs after the
        `post_update_external_access_rule` interceptor. The (possibly modified) response returned by
        `post_update_external_access_rule` will be passed to
        `post_update_external_access_rule_with_metadata`.
        """
        return response, metadata

    def pre_update_external_address(
        self,
        request: vmwareengine.UpdateExternalAddressRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.UpdateExternalAddressRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_external_address

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_update_external_address(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_external_address

        DEPRECATED. Please use the `post_update_external_address_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_update_external_address` interceptor runs
        before the `post_update_external_address_with_metadata` interceptor.
        """
        return response

    def post_update_external_address_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_external_address

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_update_external_address_with_metadata`
        interceptor in new development instead of the `post_update_external_address` interceptor.
        When both interceptors are used, this `post_update_external_address_with_metadata` interceptor runs after the
        `post_update_external_address` interceptor. The (possibly modified) response returned by
        `post_update_external_address` will be passed to
        `post_update_external_address_with_metadata`.
        """
        return response, metadata

    def pre_update_logging_server(
        self,
        request: vmwareengine.UpdateLoggingServerRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.UpdateLoggingServerRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_logging_server

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_update_logging_server(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_logging_server

        DEPRECATED. Please use the `post_update_logging_server_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_update_logging_server` interceptor runs
        before the `post_update_logging_server_with_metadata` interceptor.
        """
        return response

    def post_update_logging_server_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_logging_server

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_update_logging_server_with_metadata`
        interceptor in new development instead of the `post_update_logging_server` interceptor.
        When both interceptors are used, this `post_update_logging_server_with_metadata` interceptor runs after the
        `post_update_logging_server` interceptor. The (possibly modified) response returned by
        `post_update_logging_server` will be passed to
        `post_update_logging_server_with_metadata`.
        """
        return response, metadata

    def pre_update_management_dns_zone_binding(
        self,
        request: vmwareengine.UpdateManagementDnsZoneBindingRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.UpdateManagementDnsZoneBindingRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_management_dns_zone_binding

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_update_management_dns_zone_binding(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_management_dns_zone_binding

        DEPRECATED. Please use the `post_update_management_dns_zone_binding_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_update_management_dns_zone_binding` interceptor runs
        before the `post_update_management_dns_zone_binding_with_metadata` interceptor.
        """
        return response

    def post_update_management_dns_zone_binding_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_management_dns_zone_binding

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_update_management_dns_zone_binding_with_metadata`
        interceptor in new development instead of the `post_update_management_dns_zone_binding` interceptor.
        When both interceptors are used, this `post_update_management_dns_zone_binding_with_metadata` interceptor runs after the
        `post_update_management_dns_zone_binding` interceptor. The (possibly modified) response returned by
        `post_update_management_dns_zone_binding` will be passed to
        `post_update_management_dns_zone_binding_with_metadata`.
        """
        return response, metadata

    def pre_update_network_peering(
        self,
        request: vmwareengine.UpdateNetworkPeeringRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.UpdateNetworkPeeringRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_network_peering

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_update_network_peering(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_network_peering

        DEPRECATED. Please use the `post_update_network_peering_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_update_network_peering` interceptor runs
        before the `post_update_network_peering_with_metadata` interceptor.
        """
        return response

    def post_update_network_peering_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_network_peering

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_update_network_peering_with_metadata`
        interceptor in new development instead of the `post_update_network_peering` interceptor.
        When both interceptors are used, this `post_update_network_peering_with_metadata` interceptor runs after the
        `post_update_network_peering` interceptor. The (possibly modified) response returned by
        `post_update_network_peering` will be passed to
        `post_update_network_peering_with_metadata`.
        """
        return response, metadata

    def pre_update_network_policy(
        self,
        request: vmwareengine.UpdateNetworkPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.UpdateNetworkPolicyRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_network_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_update_network_policy(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_network_policy

        DEPRECATED. Please use the `post_update_network_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_update_network_policy` interceptor runs
        before the `post_update_network_policy_with_metadata` interceptor.
        """
        return response

    def post_update_network_policy_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_network_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_update_network_policy_with_metadata`
        interceptor in new development instead of the `post_update_network_policy` interceptor.
        When both interceptors are used, this `post_update_network_policy_with_metadata` interceptor runs after the
        `post_update_network_policy` interceptor. The (possibly modified) response returned by
        `post_update_network_policy` will be passed to
        `post_update_network_policy_with_metadata`.
        """
        return response, metadata

    def pre_update_private_cloud(
        self,
        request: vmwareengine.UpdatePrivateCloudRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.UpdatePrivateCloudRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_private_cloud

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_update_private_cloud(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_private_cloud

        DEPRECATED. Please use the `post_update_private_cloud_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_update_private_cloud` interceptor runs
        before the `post_update_private_cloud_with_metadata` interceptor.
        """
        return response

    def post_update_private_cloud_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_private_cloud

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_update_private_cloud_with_metadata`
        interceptor in new development instead of the `post_update_private_cloud` interceptor.
        When both interceptors are used, this `post_update_private_cloud_with_metadata` interceptor runs after the
        `post_update_private_cloud` interceptor. The (possibly modified) response returned by
        `post_update_private_cloud` will be passed to
        `post_update_private_cloud_with_metadata`.
        """
        return response, metadata

    def pre_update_private_connection(
        self,
        request: vmwareengine.UpdatePrivateConnectionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.UpdatePrivateConnectionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_private_connection

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_update_private_connection(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_private_connection

        DEPRECATED. Please use the `post_update_private_connection_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_update_private_connection` interceptor runs
        before the `post_update_private_connection_with_metadata` interceptor.
        """
        return response

    def post_update_private_connection_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_private_connection

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_update_private_connection_with_metadata`
        interceptor in new development instead of the `post_update_private_connection` interceptor.
        When both interceptors are used, this `post_update_private_connection_with_metadata` interceptor runs after the
        `post_update_private_connection` interceptor. The (possibly modified) response returned by
        `post_update_private_connection` will be passed to
        `post_update_private_connection_with_metadata`.
        """
        return response, metadata

    def pre_update_subnet(
        self,
        request: vmwareengine.UpdateSubnetRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.UpdateSubnetRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_subnet

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_update_subnet(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_subnet

        DEPRECATED. Please use the `post_update_subnet_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_update_subnet` interceptor runs
        before the `post_update_subnet_with_metadata` interceptor.
        """
        return response

    def post_update_subnet_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_subnet

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_update_subnet_with_metadata`
        interceptor in new development instead of the `post_update_subnet` interceptor.
        When both interceptors are used, this `post_update_subnet_with_metadata` interceptor runs after the
        `post_update_subnet` interceptor. The (possibly modified) response returned by
        `post_update_subnet` will be passed to
        `post_update_subnet_with_metadata`.
        """
        return response, metadata

    def pre_update_vmware_engine_network(
        self,
        request: vmwareengine.UpdateVmwareEngineNetworkRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmwareengine.UpdateVmwareEngineNetworkRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_vmware_engine_network

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_update_vmware_engine_network(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_vmware_engine_network

        DEPRECATED. Please use the `post_update_vmware_engine_network_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code. This `post_update_vmware_engine_network` interceptor runs
        before the `post_update_vmware_engine_network_with_metadata` interceptor.
        """
        return response

    def post_update_vmware_engine_network_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_vmware_engine_network

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmwareEngine server but before it is returned to user code.

        We recommend only using this `post_update_vmware_engine_network_with_metadata`
        interceptor in new development instead of the `post_update_vmware_engine_network` interceptor.
        When both interceptors are used, this `post_update_vmware_engine_network_with_metadata` interceptor runs after the
        `post_update_vmware_engine_network` interceptor. The (possibly modified) response returned by
        `post_update_vmware_engine_network` will be passed to
        `post_update_vmware_engine_network_with_metadata`.
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
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the VmwareEngine server but before
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
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the VmwareEngine server but before
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
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_get_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for get_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the VmwareEngine server but before
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
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_set_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for set_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the VmwareEngine server but before
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
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_test_iam_permissions(
        self, response: iam_policy_pb2.TestIamPermissionsResponse
    ) -> iam_policy_pb2.TestIamPermissionsResponse:
        """Post-rpc interceptor for test_iam_permissions

        Override in a subclass to manipulate the response
        after it is returned by the VmwareEngine server but before
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
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_delete_operation(self, response: None) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the VmwareEngine server but before
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
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the VmwareEngine server but before
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
        before they are sent to the VmwareEngine server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the VmwareEngine server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class VmwareEngineRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: VmwareEngineRestInterceptor


class VmwareEngineRestTransport(_BaseVmwareEngineRestTransport):
    """REST backend synchronous transport for VmwareEngine.

    VMwareEngine manages VMware's private clusters in the Cloud.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "vmwareengine.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[VmwareEngineRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'vmwareengine.googleapis.com').
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
            interceptor (Optional[VmwareEngineRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or VmwareEngineRestInterceptor()
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

    class _CreateCluster(
        _BaseVmwareEngineRestTransport._BaseCreateCluster, VmwareEngineRestStub
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.CreateCluster")

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
            request: vmwareengine.CreateClusterRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create cluster method over HTTP.

            Args:
                request (~.vmwareengine.CreateClusterRequest):
                    The request object. Request message for
                [VmwareEngine.CreateCluster][google.cloud.vmwareengine.v1.VmwareEngine.CreateCluster]
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
                _BaseVmwareEngineRestTransport._BaseCreateCluster._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_cluster(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseCreateCluster,
                    "_BaseCreateCluster__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.CreateCluster",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "CreateCluster",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._CreateCluster._get_response(
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

            resp = self._interceptor.post_create_cluster(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_cluster_with_metadata(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.create_cluster",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "CreateCluster",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateExternalAccessRule(
        _BaseVmwareEngineRestTransport._BaseCreateExternalAccessRule,
        VmwareEngineRestStub,
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.CreateExternalAccessRule")

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
            request: vmwareengine.CreateExternalAccessRuleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create external access
            rule method over HTTP.

                Args:
                    request (~.vmwareengine.CreateExternalAccessRuleRequest):
                        The request object. Request message for
                    [VmwareEngine.CreateExternalAccessRule][google.cloud.vmwareengine.v1.VmwareEngine.CreateExternalAccessRule]
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

            http_options = _BaseVmwareEngineRestTransport._BaseCreateExternalAccessRule._get_http_options()
            request, metadata = self._interceptor.pre_create_external_access_rule(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseCreateExternalAccessRule,
                    "_BaseCreateExternalAccessRule__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.CreateExternalAccessRule",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "CreateExternalAccessRule",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                VmwareEngineRestTransport._CreateExternalAccessRule._get_response(
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

            resp = self._interceptor.post_create_external_access_rule(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_external_access_rule_with_metadata(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.create_external_access_rule",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "CreateExternalAccessRule",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateExternalAddress(
        _BaseVmwareEngineRestTransport._BaseCreateExternalAddress, VmwareEngineRestStub
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.CreateExternalAddress")

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
            request: vmwareengine.CreateExternalAddressRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create external address method over HTTP.

            Args:
                request (~.vmwareengine.CreateExternalAddressRequest):
                    The request object. Request message for
                [VmwareEngine.CreateExternalAddress][google.cloud.vmwareengine.v1.VmwareEngine.CreateExternalAddress]
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

            http_options = _BaseVmwareEngineRestTransport._BaseCreateExternalAddress._get_http_options()
            request, metadata = self._interceptor.pre_create_external_address(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseCreateExternalAddress,
                    "_BaseCreateExternalAddress__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.CreateExternalAddress",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "CreateExternalAddress",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._CreateExternalAddress._get_response(
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

            resp = self._interceptor.post_create_external_address(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_external_address_with_metadata(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.create_external_address",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "CreateExternalAddress",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateHcxActivationKey(
        _BaseVmwareEngineRestTransport._BaseCreateHcxActivationKey, VmwareEngineRestStub
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.CreateHcxActivationKey")

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
            request: vmwareengine.CreateHcxActivationKeyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create hcx activation key method over HTTP.

            Args:
                request (~.vmwareengine.CreateHcxActivationKeyRequest):
                    The request object. Request message for
                [VmwareEngine.CreateHcxActivationKey][google.cloud.vmwareengine.v1.VmwareEngine.CreateHcxActivationKey]
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

            http_options = _BaseVmwareEngineRestTransport._BaseCreateHcxActivationKey._get_http_options()
            request, metadata = self._interceptor.pre_create_hcx_activation_key(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseCreateHcxActivationKey,
                    "_BaseCreateHcxActivationKey__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.CreateHcxActivationKey",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "CreateHcxActivationKey",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._CreateHcxActivationKey._get_response(
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

            resp = self._interceptor.post_create_hcx_activation_key(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_hcx_activation_key_with_metadata(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.create_hcx_activation_key",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "CreateHcxActivationKey",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateLoggingServer(
        _BaseVmwareEngineRestTransport._BaseCreateLoggingServer, VmwareEngineRestStub
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.CreateLoggingServer")

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
            request: vmwareengine.CreateLoggingServerRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create logging server method over HTTP.

            Args:
                request (~.vmwareengine.CreateLoggingServerRequest):
                    The request object. Request message for
                [VmwareEngine.CreateLoggingServer][google.cloud.vmwareengine.v1.VmwareEngine.CreateLoggingServer]
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

            http_options = _BaseVmwareEngineRestTransport._BaseCreateLoggingServer._get_http_options()
            request, metadata = self._interceptor.pre_create_logging_server(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseCreateLoggingServer,
                    "_BaseCreateLoggingServer__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.CreateLoggingServer",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "CreateLoggingServer",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._CreateLoggingServer._get_response(
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

            resp = self._interceptor.post_create_logging_server(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_logging_server_with_metadata(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.create_logging_server",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "CreateLoggingServer",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateManagementDnsZoneBinding(
        _BaseVmwareEngineRestTransport._BaseCreateManagementDnsZoneBinding,
        VmwareEngineRestStub,
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.CreateManagementDnsZoneBinding")

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
            request: vmwareengine.CreateManagementDnsZoneBindingRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create management dns
            zone binding method over HTTP.

                Args:
                    request (~.vmwareengine.CreateManagementDnsZoneBindingRequest):
                        The request object. Request message for
                    [VmwareEngine.CreateManagementDnsZoneBindings][]
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

            http_options = _BaseVmwareEngineRestTransport._BaseCreateManagementDnsZoneBinding._get_http_options()
            request, metadata = (
                self._interceptor.pre_create_management_dns_zone_binding(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseCreateManagementDnsZoneBinding,
                    "_BaseCreateManagementDnsZoneBinding__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.CreateManagementDnsZoneBinding",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "CreateManagementDnsZoneBinding",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                VmwareEngineRestTransport._CreateManagementDnsZoneBinding._get_response(
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

            resp = self._interceptor.post_create_management_dns_zone_binding(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_create_management_dns_zone_binding_with_metadata(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.create_management_dns_zone_binding",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "CreateManagementDnsZoneBinding",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateNetworkPeering(
        _BaseVmwareEngineRestTransport._BaseCreateNetworkPeering, VmwareEngineRestStub
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.CreateNetworkPeering")

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
            request: vmwareengine.CreateNetworkPeeringRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create network peering method over HTTP.

            Args:
                request (~.vmwareengine.CreateNetworkPeeringRequest):
                    The request object. Request message for
                [VmwareEngine.CreateNetworkPeering][google.cloud.vmwareengine.v1.VmwareEngine.CreateNetworkPeering]
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

            http_options = _BaseVmwareEngineRestTransport._BaseCreateNetworkPeering._get_http_options()
            request, metadata = self._interceptor.pre_create_network_peering(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseCreateNetworkPeering,
                    "_BaseCreateNetworkPeering__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.CreateNetworkPeering",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "CreateNetworkPeering",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._CreateNetworkPeering._get_response(
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

            resp = self._interceptor.post_create_network_peering(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_network_peering_with_metadata(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.create_network_peering",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "CreateNetworkPeering",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateNetworkPolicy(
        _BaseVmwareEngineRestTransport._BaseCreateNetworkPolicy, VmwareEngineRestStub
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.CreateNetworkPolicy")

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
            request: vmwareengine.CreateNetworkPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create network policy method over HTTP.

            Args:
                request (~.vmwareengine.CreateNetworkPolicyRequest):
                    The request object. Request message for
                [VmwareEngine.CreateNetworkPolicy][google.cloud.vmwareengine.v1.VmwareEngine.CreateNetworkPolicy]
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

            http_options = _BaseVmwareEngineRestTransport._BaseCreateNetworkPolicy._get_http_options()
            request, metadata = self._interceptor.pre_create_network_policy(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseCreateNetworkPolicy,
                    "_BaseCreateNetworkPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.CreateNetworkPolicy",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "CreateNetworkPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._CreateNetworkPolicy._get_response(
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

            resp = self._interceptor.post_create_network_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_network_policy_with_metadata(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.create_network_policy",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "CreateNetworkPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreatePrivateCloud(
        _BaseVmwareEngineRestTransport._BaseCreatePrivateCloud, VmwareEngineRestStub
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.CreatePrivateCloud")

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
            request: vmwareengine.CreatePrivateCloudRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create private cloud method over HTTP.

            Args:
                request (~.vmwareengine.CreatePrivateCloudRequest):
                    The request object. Request message for
                [VmwareEngine.CreatePrivateCloud][google.cloud.vmwareengine.v1.VmwareEngine.CreatePrivateCloud]
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

            http_options = _BaseVmwareEngineRestTransport._BaseCreatePrivateCloud._get_http_options()
            request, metadata = self._interceptor.pre_create_private_cloud(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseCreatePrivateCloud,
                    "_BaseCreatePrivateCloud__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.CreatePrivateCloud",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "CreatePrivateCloud",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._CreatePrivateCloud._get_response(
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

            resp = self._interceptor.post_create_private_cloud(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_private_cloud_with_metadata(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.create_private_cloud",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "CreatePrivateCloud",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreatePrivateConnection(
        _BaseVmwareEngineRestTransport._BaseCreatePrivateConnection,
        VmwareEngineRestStub,
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.CreatePrivateConnection")

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
            request: vmwareengine.CreatePrivateConnectionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create private connection method over HTTP.

            Args:
                request (~.vmwareengine.CreatePrivateConnectionRequest):
                    The request object. Request message for
                [VmwareEngine.CreatePrivateConnection][google.cloud.vmwareengine.v1.VmwareEngine.CreatePrivateConnection]
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

            http_options = _BaseVmwareEngineRestTransport._BaseCreatePrivateConnection._get_http_options()
            request, metadata = self._interceptor.pre_create_private_connection(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseCreatePrivateConnection,
                    "_BaseCreatePrivateConnection__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.CreatePrivateConnection",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "CreatePrivateConnection",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._CreatePrivateConnection._get_response(
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

            resp = self._interceptor.post_create_private_connection(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_private_connection_with_metadata(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.create_private_connection",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "CreatePrivateConnection",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateVmwareEngineNetwork(
        _BaseVmwareEngineRestTransport._BaseCreateVmwareEngineNetwork,
        VmwareEngineRestStub,
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.CreateVmwareEngineNetwork")

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
            request: vmwareengine.CreateVmwareEngineNetworkRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create vmware engine
            network method over HTTP.

                Args:
                    request (~.vmwareengine.CreateVmwareEngineNetworkRequest):
                        The request object. Request message for
                    [VmwareEngine.CreateVmwareEngineNetwork][google.cloud.vmwareengine.v1.VmwareEngine.CreateVmwareEngineNetwork]
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

            http_options = _BaseVmwareEngineRestTransport._BaseCreateVmwareEngineNetwork._get_http_options()
            request, metadata = self._interceptor.pre_create_vmware_engine_network(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseCreateVmwareEngineNetwork,
                    "_BaseCreateVmwareEngineNetwork__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.CreateVmwareEngineNetwork",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "CreateVmwareEngineNetwork",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                VmwareEngineRestTransport._CreateVmwareEngineNetwork._get_response(
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

            resp = self._interceptor.post_create_vmware_engine_network(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_vmware_engine_network_with_metadata(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.create_vmware_engine_network",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "CreateVmwareEngineNetwork",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteCluster(
        _BaseVmwareEngineRestTransport._BaseDeleteCluster, VmwareEngineRestStub
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.DeleteCluster")

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
            request: vmwareengine.DeleteClusterRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete cluster method over HTTP.

            Args:
                request (~.vmwareengine.DeleteClusterRequest):
                    The request object. Request message for
                [VmwareEngine.DeleteCluster][google.cloud.vmwareengine.v1.VmwareEngine.DeleteCluster]
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
                _BaseVmwareEngineRestTransport._BaseDeleteCluster._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_cluster(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseDeleteCluster,
                    "_BaseDeleteCluster__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.DeleteCluster",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "DeleteCluster",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._DeleteCluster._get_response(
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

            resp = self._interceptor.post_delete_cluster(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_cluster_with_metadata(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.delete_cluster",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "DeleteCluster",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteExternalAccessRule(
        _BaseVmwareEngineRestTransport._BaseDeleteExternalAccessRule,
        VmwareEngineRestStub,
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.DeleteExternalAccessRule")

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
            request: vmwareengine.DeleteExternalAccessRuleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete external access
            rule method over HTTP.

                Args:
                    request (~.vmwareengine.DeleteExternalAccessRuleRequest):
                        The request object. Request message for
                    [VmwareEngine.DeleteExternalAccessRule][google.cloud.vmwareengine.v1.VmwareEngine.DeleteExternalAccessRule]
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

            http_options = _BaseVmwareEngineRestTransport._BaseDeleteExternalAccessRule._get_http_options()
            request, metadata = self._interceptor.pre_delete_external_access_rule(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseDeleteExternalAccessRule,
                    "_BaseDeleteExternalAccessRule__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.DeleteExternalAccessRule",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "DeleteExternalAccessRule",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                VmwareEngineRestTransport._DeleteExternalAccessRule._get_response(
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

            resp = self._interceptor.post_delete_external_access_rule(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_external_access_rule_with_metadata(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.delete_external_access_rule",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "DeleteExternalAccessRule",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteExternalAddress(
        _BaseVmwareEngineRestTransport._BaseDeleteExternalAddress, VmwareEngineRestStub
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.DeleteExternalAddress")

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
            request: vmwareengine.DeleteExternalAddressRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete external address method over HTTP.

            Args:
                request (~.vmwareengine.DeleteExternalAddressRequest):
                    The request object. Request message for
                [VmwareEngine.DeleteExternalAddress][google.cloud.vmwareengine.v1.VmwareEngine.DeleteExternalAddress]
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

            http_options = _BaseVmwareEngineRestTransport._BaseDeleteExternalAddress._get_http_options()
            request, metadata = self._interceptor.pre_delete_external_address(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseDeleteExternalAddress,
                    "_BaseDeleteExternalAddress__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.DeleteExternalAddress",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "DeleteExternalAddress",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._DeleteExternalAddress._get_response(
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

            resp = self._interceptor.post_delete_external_address(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_external_address_with_metadata(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.delete_external_address",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "DeleteExternalAddress",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteLoggingServer(
        _BaseVmwareEngineRestTransport._BaseDeleteLoggingServer, VmwareEngineRestStub
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.DeleteLoggingServer")

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
            request: vmwareengine.DeleteLoggingServerRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete logging server method over HTTP.

            Args:
                request (~.vmwareengine.DeleteLoggingServerRequest):
                    The request object. Request message for
                [VmwareEngine.DeleteLoggingServer][google.cloud.vmwareengine.v1.VmwareEngine.DeleteLoggingServer]
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

            http_options = _BaseVmwareEngineRestTransport._BaseDeleteLoggingServer._get_http_options()
            request, metadata = self._interceptor.pre_delete_logging_server(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseDeleteLoggingServer,
                    "_BaseDeleteLoggingServer__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.DeleteLoggingServer",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "DeleteLoggingServer",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._DeleteLoggingServer._get_response(
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

            resp = self._interceptor.post_delete_logging_server(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_logging_server_with_metadata(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.delete_logging_server",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "DeleteLoggingServer",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteManagementDnsZoneBinding(
        _BaseVmwareEngineRestTransport._BaseDeleteManagementDnsZoneBinding,
        VmwareEngineRestStub,
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.DeleteManagementDnsZoneBinding")

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
            request: vmwareengine.DeleteManagementDnsZoneBindingRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete management dns
            zone binding method over HTTP.

                Args:
                    request (~.vmwareengine.DeleteManagementDnsZoneBindingRequest):
                        The request object. Request message for
                    [VmwareEngine.DeleteManagementDnsZoneBinding][google.cloud.vmwareengine.v1.VmwareEngine.DeleteManagementDnsZoneBinding]
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

            http_options = _BaseVmwareEngineRestTransport._BaseDeleteManagementDnsZoneBinding._get_http_options()
            request, metadata = (
                self._interceptor.pre_delete_management_dns_zone_binding(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseDeleteManagementDnsZoneBinding,
                    "_BaseDeleteManagementDnsZoneBinding__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.DeleteManagementDnsZoneBinding",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "DeleteManagementDnsZoneBinding",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                VmwareEngineRestTransport._DeleteManagementDnsZoneBinding._get_response(
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

            resp = self._interceptor.post_delete_management_dns_zone_binding(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_delete_management_dns_zone_binding_with_metadata(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.delete_management_dns_zone_binding",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "DeleteManagementDnsZoneBinding",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteNetworkPeering(
        _BaseVmwareEngineRestTransport._BaseDeleteNetworkPeering, VmwareEngineRestStub
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.DeleteNetworkPeering")

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
            request: vmwareengine.DeleteNetworkPeeringRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete network peering method over HTTP.

            Args:
                request (~.vmwareengine.DeleteNetworkPeeringRequest):
                    The request object. Request message for
                [VmwareEngine.DeleteNetworkPeering][google.cloud.vmwareengine.v1.VmwareEngine.DeleteNetworkPeering]
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

            http_options = _BaseVmwareEngineRestTransport._BaseDeleteNetworkPeering._get_http_options()
            request, metadata = self._interceptor.pre_delete_network_peering(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseDeleteNetworkPeering,
                    "_BaseDeleteNetworkPeering__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.DeleteNetworkPeering",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "DeleteNetworkPeering",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._DeleteNetworkPeering._get_response(
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

            resp = self._interceptor.post_delete_network_peering(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_network_peering_with_metadata(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.delete_network_peering",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "DeleteNetworkPeering",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteNetworkPolicy(
        _BaseVmwareEngineRestTransport._BaseDeleteNetworkPolicy, VmwareEngineRestStub
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.DeleteNetworkPolicy")

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
            request: vmwareengine.DeleteNetworkPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete network policy method over HTTP.

            Args:
                request (~.vmwareengine.DeleteNetworkPolicyRequest):
                    The request object. Request message for
                [VmwareEngine.DeleteNetworkPolicy][google.cloud.vmwareengine.v1.VmwareEngine.DeleteNetworkPolicy]
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

            http_options = _BaseVmwareEngineRestTransport._BaseDeleteNetworkPolicy._get_http_options()
            request, metadata = self._interceptor.pre_delete_network_policy(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseDeleteNetworkPolicy,
                    "_BaseDeleteNetworkPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.DeleteNetworkPolicy",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "DeleteNetworkPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._DeleteNetworkPolicy._get_response(
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

            resp = self._interceptor.post_delete_network_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_network_policy_with_metadata(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.delete_network_policy",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "DeleteNetworkPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeletePrivateCloud(
        _BaseVmwareEngineRestTransport._BaseDeletePrivateCloud, VmwareEngineRestStub
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.DeletePrivateCloud")

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
            request: vmwareengine.DeletePrivateCloudRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete private cloud method over HTTP.

            Args:
                request (~.vmwareengine.DeletePrivateCloudRequest):
                    The request object. Request message for
                [VmwareEngine.DeletePrivateCloud][google.cloud.vmwareengine.v1.VmwareEngine.DeletePrivateCloud]
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

            http_options = _BaseVmwareEngineRestTransport._BaseDeletePrivateCloud._get_http_options()
            request, metadata = self._interceptor.pre_delete_private_cloud(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseDeletePrivateCloud,
                    "_BaseDeletePrivateCloud__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.DeletePrivateCloud",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "DeletePrivateCloud",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._DeletePrivateCloud._get_response(
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

            resp = self._interceptor.post_delete_private_cloud(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_private_cloud_with_metadata(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.delete_private_cloud",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "DeletePrivateCloud",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeletePrivateConnection(
        _BaseVmwareEngineRestTransport._BaseDeletePrivateConnection,
        VmwareEngineRestStub,
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.DeletePrivateConnection")

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
            request: vmwareengine.DeletePrivateConnectionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete private connection method over HTTP.

            Args:
                request (~.vmwareengine.DeletePrivateConnectionRequest):
                    The request object. Request message for
                [VmwareEngine.DeletePrivateConnection][google.cloud.vmwareengine.v1.VmwareEngine.DeletePrivateConnection]
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

            http_options = _BaseVmwareEngineRestTransport._BaseDeletePrivateConnection._get_http_options()
            request, metadata = self._interceptor.pre_delete_private_connection(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseDeletePrivateConnection,
                    "_BaseDeletePrivateConnection__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.DeletePrivateConnection",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "DeletePrivateConnection",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._DeletePrivateConnection._get_response(
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

            resp = self._interceptor.post_delete_private_connection(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_private_connection_with_metadata(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.delete_private_connection",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "DeletePrivateConnection",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteVmwareEngineNetwork(
        _BaseVmwareEngineRestTransport._BaseDeleteVmwareEngineNetwork,
        VmwareEngineRestStub,
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.DeleteVmwareEngineNetwork")

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
            request: vmwareengine.DeleteVmwareEngineNetworkRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete vmware engine
            network method over HTTP.

                Args:
                    request (~.vmwareengine.DeleteVmwareEngineNetworkRequest):
                        The request object. Request message for
                    [VmwareEngine.DeleteVmwareEngineNetwork][google.cloud.vmwareengine.v1.VmwareEngine.DeleteVmwareEngineNetwork]
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

            http_options = _BaseVmwareEngineRestTransport._BaseDeleteVmwareEngineNetwork._get_http_options()
            request, metadata = self._interceptor.pre_delete_vmware_engine_network(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseDeleteVmwareEngineNetwork,
                    "_BaseDeleteVmwareEngineNetwork__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.DeleteVmwareEngineNetwork",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "DeleteVmwareEngineNetwork",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                VmwareEngineRestTransport._DeleteVmwareEngineNetwork._get_response(
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

            resp = self._interceptor.post_delete_vmware_engine_network(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_vmware_engine_network_with_metadata(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.delete_vmware_engine_network",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "DeleteVmwareEngineNetwork",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _FetchNetworkPolicyExternalAddresses(
        _BaseVmwareEngineRestTransport._BaseFetchNetworkPolicyExternalAddresses,
        VmwareEngineRestStub,
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.FetchNetworkPolicyExternalAddresses")

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
            request: vmwareengine.FetchNetworkPolicyExternalAddressesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> vmwareengine.FetchNetworkPolicyExternalAddressesResponse:
            r"""Call the fetch network policy
            external addresses method over HTTP.

                Args:
                    request (~.vmwareengine.FetchNetworkPolicyExternalAddressesRequest):
                        The request object. Request message for
                    [VmwareEngine.FetchNetworkPolicyExternalAddresses][google.cloud.vmwareengine.v1.VmwareEngine.FetchNetworkPolicyExternalAddresses]
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.vmwareengine.FetchNetworkPolicyExternalAddressesResponse:
                        Response message for
                    [VmwareEngine.FetchNetworkPolicyExternalAddresses][google.cloud.vmwareengine.v1.VmwareEngine.FetchNetworkPolicyExternalAddresses]

            """

            http_options = _BaseVmwareEngineRestTransport._BaseFetchNetworkPolicyExternalAddresses._get_http_options()
            request, metadata = (
                self._interceptor.pre_fetch_network_policy_external_addresses(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseFetchNetworkPolicyExternalAddresses,
                    "_BaseFetchNetworkPolicyExternalAddresses__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.FetchNetworkPolicyExternalAddresses",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "FetchNetworkPolicyExternalAddresses",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._FetchNetworkPolicyExternalAddresses._get_response(
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
            resp = vmwareengine.FetchNetworkPolicyExternalAddressesResponse()
            pb_resp = vmwareengine.FetchNetworkPolicyExternalAddressesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_fetch_network_policy_external_addresses(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_fetch_network_policy_external_addresses_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = vmwareengine.FetchNetworkPolicyExternalAddressesResponse.to_json(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.fetch_network_policy_external_addresses",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "FetchNetworkPolicyExternalAddresses",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetCluster(
        _BaseVmwareEngineRestTransport._BaseGetCluster, VmwareEngineRestStub
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.GetCluster")

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
            request: vmwareengine.GetClusterRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> vmwareengine_resources.Cluster:
            r"""Call the get cluster method over HTTP.

            Args:
                request (~.vmwareengine.GetClusterRequest):
                    The request object. Request message for
                [VmwareEngine.GetCluster][google.cloud.vmwareengine.v1.VmwareEngine.GetCluster]
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.vmwareengine_resources.Cluster:
                    A cluster in a private cloud.
            """

            http_options = (
                _BaseVmwareEngineRestTransport._BaseGetCluster._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_cluster(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseGetCluster,
                    "_BaseGetCluster__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.GetCluster",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "GetCluster",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._GetCluster._get_response(
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
            resp = vmwareengine_resources.Cluster()
            pb_resp = vmwareengine_resources.Cluster.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_cluster(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_cluster_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = vmwareengine_resources.Cluster.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.get_cluster",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "GetCluster",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetDnsBindPermission(
        _BaseVmwareEngineRestTransport._BaseGetDnsBindPermission, VmwareEngineRestStub
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.GetDnsBindPermission")

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
            request: vmwareengine.GetDnsBindPermissionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> vmwareengine_resources.DnsBindPermission:
            r"""Call the get dns bind permission method over HTTP.

            Args:
                request (~.vmwareengine.GetDnsBindPermissionRequest):
                    The request object. Request message for
                [VmwareEngine.GetDnsBindPermission][google.cloud.vmwareengine.v1.VmwareEngine.GetDnsBindPermission]
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.vmwareengine_resources.DnsBindPermission:
                    DnsBindPermission resource that
                contains the accounts having the
                consumer DNS bind permission on the
                corresponding intranet VPC of the
                consumer project.

            """

            http_options = _BaseVmwareEngineRestTransport._BaseGetDnsBindPermission._get_http_options()
            request, metadata = self._interceptor.pre_get_dns_bind_permission(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseGetDnsBindPermission,
                    "_BaseGetDnsBindPermission__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.GetDnsBindPermission",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "GetDnsBindPermission",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._GetDnsBindPermission._get_response(
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
            resp = vmwareengine_resources.DnsBindPermission()
            pb_resp = vmwareengine_resources.DnsBindPermission.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_dns_bind_permission(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_dns_bind_permission_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = vmwareengine_resources.DnsBindPermission.to_json(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.get_dns_bind_permission",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "GetDnsBindPermission",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetDnsForwarding(
        _BaseVmwareEngineRestTransport._BaseGetDnsForwarding, VmwareEngineRestStub
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.GetDnsForwarding")

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
            request: vmwareengine.GetDnsForwardingRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> vmwareengine_resources.DnsForwarding:
            r"""Call the get dns forwarding method over HTTP.

            Args:
                request (~.vmwareengine.GetDnsForwardingRequest):
                    The request object. Request message for
                [VmwareEngine.GetDnsForwarding][google.cloud.vmwareengine.v1.VmwareEngine.GetDnsForwarding]
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.vmwareengine_resources.DnsForwarding:
                    DNS forwarding config.
                This config defines a list of domain to
                name server mappings, and is attached to
                the private cloud for custom domain
                resolution.

            """

            http_options = (
                _BaseVmwareEngineRestTransport._BaseGetDnsForwarding._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_dns_forwarding(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseGetDnsForwarding,
                    "_BaseGetDnsForwarding__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.GetDnsForwarding",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "GetDnsForwarding",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._GetDnsForwarding._get_response(
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
            resp = vmwareengine_resources.DnsForwarding()
            pb_resp = vmwareengine_resources.DnsForwarding.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_dns_forwarding(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_dns_forwarding_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = vmwareengine_resources.DnsForwarding.to_json(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.get_dns_forwarding",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "GetDnsForwarding",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetExternalAccessRule(
        _BaseVmwareEngineRestTransport._BaseGetExternalAccessRule, VmwareEngineRestStub
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.GetExternalAccessRule")

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
            request: vmwareengine.GetExternalAccessRuleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> vmwareengine_resources.ExternalAccessRule:
            r"""Call the get external access rule method over HTTP.

            Args:
                request (~.vmwareengine.GetExternalAccessRuleRequest):
                    The request object. Request message for
                [VmwareEngine.GetExternalAccessRule][google.cloud.vmwareengine.v1.VmwareEngine.GetExternalAccessRule]
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.vmwareengine_resources.ExternalAccessRule:
                    External access firewall rules for filtering incoming
                traffic destined to ``ExternalAddress`` resources.

            """

            http_options = _BaseVmwareEngineRestTransport._BaseGetExternalAccessRule._get_http_options()
            request, metadata = self._interceptor.pre_get_external_access_rule(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseGetExternalAccessRule,
                    "_BaseGetExternalAccessRule__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.GetExternalAccessRule",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "GetExternalAccessRule",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._GetExternalAccessRule._get_response(
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
            resp = vmwareengine_resources.ExternalAccessRule()
            pb_resp = vmwareengine_resources.ExternalAccessRule.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_external_access_rule(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_external_access_rule_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        vmwareengine_resources.ExternalAccessRule.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.get_external_access_rule",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "GetExternalAccessRule",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetExternalAddress(
        _BaseVmwareEngineRestTransport._BaseGetExternalAddress, VmwareEngineRestStub
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.GetExternalAddress")

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
            request: vmwareengine.GetExternalAddressRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> vmwareengine_resources.ExternalAddress:
            r"""Call the get external address method over HTTP.

            Args:
                request (~.vmwareengine.GetExternalAddressRequest):
                    The request object. Request message for
                [VmwareEngine.GetExternalAddress][google.cloud.vmwareengine.v1.VmwareEngine.GetExternalAddress]
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.vmwareengine_resources.ExternalAddress:
                    Represents an allocated external IP
                address and its corresponding internal
                IP address in a private cloud.

            """

            http_options = _BaseVmwareEngineRestTransport._BaseGetExternalAddress._get_http_options()
            request, metadata = self._interceptor.pre_get_external_address(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseGetExternalAddress,
                    "_BaseGetExternalAddress__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.GetExternalAddress",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "GetExternalAddress",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._GetExternalAddress._get_response(
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
            resp = vmwareengine_resources.ExternalAddress()
            pb_resp = vmwareengine_resources.ExternalAddress.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_external_address(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_external_address_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = vmwareengine_resources.ExternalAddress.to_json(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.get_external_address",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "GetExternalAddress",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetHcxActivationKey(
        _BaseVmwareEngineRestTransport._BaseGetHcxActivationKey, VmwareEngineRestStub
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.GetHcxActivationKey")

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
            request: vmwareengine.GetHcxActivationKeyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> vmwareengine_resources.HcxActivationKey:
            r"""Call the get hcx activation key method over HTTP.

            Args:
                request (~.vmwareengine.GetHcxActivationKeyRequest):
                    The request object. Request message for
                [VmwareEngine.GetHcxActivationKeys][]
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.vmwareengine_resources.HcxActivationKey:
                    HCX activation key. A default key is created during
                private cloud provisioning, but this behavior is subject
                to change and you should always verify active keys. Use
                [VmwareEngine.ListHcxActivationKeys][google.cloud.vmwareengine.v1.VmwareEngine.ListHcxActivationKeys]
                to retrieve existing keys and
                [VmwareEngine.CreateHcxActivationKey][google.cloud.vmwareengine.v1.VmwareEngine.CreateHcxActivationKey]
                to create new ones.

            """

            http_options = _BaseVmwareEngineRestTransport._BaseGetHcxActivationKey._get_http_options()
            request, metadata = self._interceptor.pre_get_hcx_activation_key(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseGetHcxActivationKey,
                    "_BaseGetHcxActivationKey__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.GetHcxActivationKey",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "GetHcxActivationKey",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._GetHcxActivationKey._get_response(
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
            resp = vmwareengine_resources.HcxActivationKey()
            pb_resp = vmwareengine_resources.HcxActivationKey.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_hcx_activation_key(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_hcx_activation_key_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = vmwareengine_resources.HcxActivationKey.to_json(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.get_hcx_activation_key",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "GetHcxActivationKey",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetLoggingServer(
        _BaseVmwareEngineRestTransport._BaseGetLoggingServer, VmwareEngineRestStub
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.GetLoggingServer")

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
            request: vmwareengine.GetLoggingServerRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> vmwareengine_resources.LoggingServer:
            r"""Call the get logging server method over HTTP.

            Args:
                request (~.vmwareengine.GetLoggingServerRequest):
                    The request object. Request message for
                [VmwareEngine.GetLoggingServer][google.cloud.vmwareengine.v1.VmwareEngine.GetLoggingServer]
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.vmwareengine_resources.LoggingServer:
                    Logging server to receive vCenter or
                ESXi logs.

            """

            http_options = (
                _BaseVmwareEngineRestTransport._BaseGetLoggingServer._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_logging_server(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseGetLoggingServer,
                    "_BaseGetLoggingServer__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.GetLoggingServer",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "GetLoggingServer",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._GetLoggingServer._get_response(
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
            resp = vmwareengine_resources.LoggingServer()
            pb_resp = vmwareengine_resources.LoggingServer.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_logging_server(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_logging_server_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = vmwareengine_resources.LoggingServer.to_json(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.get_logging_server",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "GetLoggingServer",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetManagementDnsZoneBinding(
        _BaseVmwareEngineRestTransport._BaseGetManagementDnsZoneBinding,
        VmwareEngineRestStub,
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.GetManagementDnsZoneBinding")

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
            request: vmwareengine.GetManagementDnsZoneBindingRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> vmwareengine_resources.ManagementDnsZoneBinding:
            r"""Call the get management dns zone
            binding method over HTTP.

                Args:
                    request (~.vmwareengine.GetManagementDnsZoneBindingRequest):
                        The request object. Request message for
                    [VmwareEngine.GetManagementDnsZoneBinding][google.cloud.vmwareengine.v1.VmwareEngine.GetManagementDnsZoneBinding]
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.vmwareengine_resources.ManagementDnsZoneBinding:
                        Represents a binding between a
                    network and the management DNS zone. A
                    management DNS zone is the Cloud DNS
                    cross-project binding zone that VMware
                    Engine creates for each private cloud.
                    It contains FQDNs and corresponding IP
                    addresses for the private cloud's ESXi
                    hosts and management VM appliances like
                    vCenter and NSX Manager.

            """

            http_options = _BaseVmwareEngineRestTransport._BaseGetManagementDnsZoneBinding._get_http_options()
            request, metadata = self._interceptor.pre_get_management_dns_zone_binding(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseGetManagementDnsZoneBinding,
                    "_BaseGetManagementDnsZoneBinding__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.GetManagementDnsZoneBinding",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "GetManagementDnsZoneBinding",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                VmwareEngineRestTransport._GetManagementDnsZoneBinding._get_response(
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
            resp = vmwareengine_resources.ManagementDnsZoneBinding()
            pb_resp = vmwareengine_resources.ManagementDnsZoneBinding.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_management_dns_zone_binding(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_get_management_dns_zone_binding_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        vmwareengine_resources.ManagementDnsZoneBinding.to_json(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.get_management_dns_zone_binding",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "GetManagementDnsZoneBinding",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetNetworkPeering(
        _BaseVmwareEngineRestTransport._BaseGetNetworkPeering, VmwareEngineRestStub
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.GetNetworkPeering")

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
            request: vmwareengine.GetNetworkPeeringRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> vmwareengine_resources.NetworkPeering:
            r"""Call the get network peering method over HTTP.

            Args:
                request (~.vmwareengine.GetNetworkPeeringRequest):
                    The request object. Request message for
                [VmwareEngine.GetNetworkPeering][google.cloud.vmwareengine.v1.VmwareEngine.GetNetworkPeering]
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.vmwareengine_resources.NetworkPeering:
                    Details of a network peering.
            """

            http_options = _BaseVmwareEngineRestTransport._BaseGetNetworkPeering._get_http_options()
            request, metadata = self._interceptor.pre_get_network_peering(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseGetNetworkPeering,
                    "_BaseGetNetworkPeering__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.GetNetworkPeering",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "GetNetworkPeering",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._GetNetworkPeering._get_response(
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
            resp = vmwareengine_resources.NetworkPeering()
            pb_resp = vmwareengine_resources.NetworkPeering.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_network_peering(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_network_peering_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = vmwareengine_resources.NetworkPeering.to_json(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.get_network_peering",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "GetNetworkPeering",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetNetworkPolicy(
        _BaseVmwareEngineRestTransport._BaseGetNetworkPolicy, VmwareEngineRestStub
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.GetNetworkPolicy")

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
            request: vmwareengine.GetNetworkPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> vmwareengine_resources.NetworkPolicy:
            r"""Call the get network policy method over HTTP.

            Args:
                request (~.vmwareengine.GetNetworkPolicyRequest):
                    The request object. Request message for
                [VmwareEngine.GetNetworkPolicy][google.cloud.vmwareengine.v1.VmwareEngine.GetNetworkPolicy]
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.vmwareengine_resources.NetworkPolicy:
                    Represents a network policy resource.
                Network policies are regional resources.
                You can use a network policy to enable
                or disable internet access and external
                IP access. Network policies are
                associated with a VMware Engine network,
                which might span across regions. For a
                given region, a network policy applies
                to all private clouds in the VMware
                Engine network associated with the
                policy.

            """

            http_options = (
                _BaseVmwareEngineRestTransport._BaseGetNetworkPolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_network_policy(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseGetNetworkPolicy,
                    "_BaseGetNetworkPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.GetNetworkPolicy",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "GetNetworkPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._GetNetworkPolicy._get_response(
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
            resp = vmwareengine_resources.NetworkPolicy()
            pb_resp = vmwareengine_resources.NetworkPolicy.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_network_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_network_policy_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = vmwareengine_resources.NetworkPolicy.to_json(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.get_network_policy",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "GetNetworkPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetNode(_BaseVmwareEngineRestTransport._BaseGetNode, VmwareEngineRestStub):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.GetNode")

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
            request: vmwareengine.GetNodeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> vmwareengine_resources.Node:
            r"""Call the get node method over HTTP.

            Args:
                request (~.vmwareengine.GetNodeRequest):
                    The request object. Request message for
                [VmwareEngine.GetNode][google.cloud.vmwareengine.v1.VmwareEngine.GetNode]
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.vmwareengine_resources.Node:
                    Node in a cluster.
            """

            http_options = (
                _BaseVmwareEngineRestTransport._BaseGetNode._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_node(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseGetNode,
                    "_BaseGetNode__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.GetNode",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "GetNode",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._GetNode._get_response(
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
            resp = vmwareengine_resources.Node()
            pb_resp = vmwareengine_resources.Node.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_node(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_node_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = vmwareengine_resources.Node.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.get_node",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "GetNode",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetNodeType(
        _BaseVmwareEngineRestTransport._BaseGetNodeType, VmwareEngineRestStub
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.GetNodeType")

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
            request: vmwareengine.GetNodeTypeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> vmwareengine_resources.NodeType:
            r"""Call the get node type method over HTTP.

            Args:
                request (~.vmwareengine.GetNodeTypeRequest):
                    The request object. Request message for
                [VmwareEngine.GetNodeType][google.cloud.vmwareengine.v1.VmwareEngine.GetNodeType]
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.vmwareengine_resources.NodeType:
                    Describes node type.
            """

            http_options = (
                _BaseVmwareEngineRestTransport._BaseGetNodeType._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_node_type(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseGetNodeType,
                    "_BaseGetNodeType__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.GetNodeType",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "GetNodeType",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._GetNodeType._get_response(
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
            resp = vmwareengine_resources.NodeType()
            pb_resp = vmwareengine_resources.NodeType.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_node_type(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_node_type_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = vmwareengine_resources.NodeType.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.get_node_type",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "GetNodeType",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetPrivateCloud(
        _BaseVmwareEngineRestTransport._BaseGetPrivateCloud, VmwareEngineRestStub
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.GetPrivateCloud")

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
            request: vmwareengine.GetPrivateCloudRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> vmwareengine_resources.PrivateCloud:
            r"""Call the get private cloud method over HTTP.

            Args:
                request (~.vmwareengine.GetPrivateCloudRequest):
                    The request object. Request message for
                [VmwareEngine.GetPrivateCloud][google.cloud.vmwareengine.v1.VmwareEngine.GetPrivateCloud]
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.vmwareengine_resources.PrivateCloud:
                    Represents a private cloud resource. Private clouds of
                type ``STANDARD`` and ``TIME_LIMITED`` are zonal
                resources, ``STRETCHED`` private clouds are regional.

            """

            http_options = (
                _BaseVmwareEngineRestTransport._BaseGetPrivateCloud._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_private_cloud(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseGetPrivateCloud,
                    "_BaseGetPrivateCloud__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.GetPrivateCloud",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "GetPrivateCloud",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._GetPrivateCloud._get_response(
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
            resp = vmwareengine_resources.PrivateCloud()
            pb_resp = vmwareengine_resources.PrivateCloud.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_private_cloud(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_private_cloud_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = vmwareengine_resources.PrivateCloud.to_json(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.get_private_cloud",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "GetPrivateCloud",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetPrivateConnection(
        _BaseVmwareEngineRestTransport._BaseGetPrivateConnection, VmwareEngineRestStub
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.GetPrivateConnection")

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
            request: vmwareengine.GetPrivateConnectionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> vmwareengine_resources.PrivateConnection:
            r"""Call the get private connection method over HTTP.

            Args:
                request (~.vmwareengine.GetPrivateConnectionRequest):
                    The request object. Request message for
                [VmwareEngine.GetPrivateConnection][google.cloud.vmwareengine.v1.VmwareEngine.GetPrivateConnection]
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.vmwareengine_resources.PrivateConnection:
                    Private connection resource that
                provides connectivity for VMware Engine
                private clouds.

            """

            http_options = _BaseVmwareEngineRestTransport._BaseGetPrivateConnection._get_http_options()
            request, metadata = self._interceptor.pre_get_private_connection(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseGetPrivateConnection,
                    "_BaseGetPrivateConnection__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.GetPrivateConnection",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "GetPrivateConnection",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._GetPrivateConnection._get_response(
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
            resp = vmwareengine_resources.PrivateConnection()
            pb_resp = vmwareengine_resources.PrivateConnection.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_private_connection(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_private_connection_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = vmwareengine_resources.PrivateConnection.to_json(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.get_private_connection",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "GetPrivateConnection",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetSubnet(
        _BaseVmwareEngineRestTransport._BaseGetSubnet, VmwareEngineRestStub
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.GetSubnet")

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
            request: vmwareengine.GetSubnetRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> vmwareengine_resources.Subnet:
            r"""Call the get subnet method over HTTP.

            Args:
                request (~.vmwareengine.GetSubnetRequest):
                    The request object. Request message for
                [VmwareEngine.GetSubnet][google.cloud.vmwareengine.v1.VmwareEngine.GetSubnet]
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.vmwareengine_resources.Subnet:
                    Subnet in a private cloud. Either ``management`` subnets
                (such as vMotion) that are read-only, or
                ``userDefined``, which can also be updated.

            """

            http_options = (
                _BaseVmwareEngineRestTransport._BaseGetSubnet._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_subnet(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseGetSubnet,
                    "_BaseGetSubnet__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.GetSubnet",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "GetSubnet",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._GetSubnet._get_response(
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
            resp = vmwareengine_resources.Subnet()
            pb_resp = vmwareengine_resources.Subnet.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_subnet(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_subnet_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = vmwareengine_resources.Subnet.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.get_subnet",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "GetSubnet",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetVmwareEngineNetwork(
        _BaseVmwareEngineRestTransport._BaseGetVmwareEngineNetwork, VmwareEngineRestStub
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.GetVmwareEngineNetwork")

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
            request: vmwareengine.GetVmwareEngineNetworkRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> vmwareengine_resources.VmwareEngineNetwork:
            r"""Call the get vmware engine network method over HTTP.

            Args:
                request (~.vmwareengine.GetVmwareEngineNetworkRequest):
                    The request object. Request message for
                [VmwareEngine.GetVmwareEngineNetwork][google.cloud.vmwareengine.v1.VmwareEngine.GetVmwareEngineNetwork]
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.vmwareengine_resources.VmwareEngineNetwork:
                    VMware Engine network resource that
                provides connectivity for VMware Engine
                private clouds.

            """

            http_options = _BaseVmwareEngineRestTransport._BaseGetVmwareEngineNetwork._get_http_options()
            request, metadata = self._interceptor.pre_get_vmware_engine_network(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseGetVmwareEngineNetwork,
                    "_BaseGetVmwareEngineNetwork__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.GetVmwareEngineNetwork",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "GetVmwareEngineNetwork",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._GetVmwareEngineNetwork._get_response(
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
            resp = vmwareengine_resources.VmwareEngineNetwork()
            pb_resp = vmwareengine_resources.VmwareEngineNetwork.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_vmware_engine_network(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_vmware_engine_network_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        vmwareengine_resources.VmwareEngineNetwork.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.get_vmware_engine_network",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "GetVmwareEngineNetwork",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GrantDnsBindPermission(
        _BaseVmwareEngineRestTransport._BaseGrantDnsBindPermission, VmwareEngineRestStub
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.GrantDnsBindPermission")

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
            request: vmwareengine.GrantDnsBindPermissionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the grant dns bind permission method over HTTP.

            Args:
                request (~.vmwareengine.GrantDnsBindPermissionRequest):
                    The request object. Request message for
                [VmwareEngine.GrantDnsBindPermission][google.cloud.vmwareengine.v1.VmwareEngine.GrantDnsBindPermission]
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

            http_options = _BaseVmwareEngineRestTransport._BaseGrantDnsBindPermission._get_http_options()
            request, metadata = self._interceptor.pre_grant_dns_bind_permission(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseGrantDnsBindPermission,
                    "_BaseGrantDnsBindPermission__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.GrantDnsBindPermission",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "GrantDnsBindPermission",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._GrantDnsBindPermission._get_response(
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

            resp = self._interceptor.post_grant_dns_bind_permission(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_grant_dns_bind_permission_with_metadata(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.grant_dns_bind_permission",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "GrantDnsBindPermission",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListClusters(
        _BaseVmwareEngineRestTransport._BaseListClusters, VmwareEngineRestStub
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.ListClusters")

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
            request: vmwareengine.ListClustersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> vmwareengine.ListClustersResponse:
            r"""Call the list clusters method over HTTP.

            Args:
                request (~.vmwareengine.ListClustersRequest):
                    The request object. Request message for
                [VmwareEngine.ListClusters][google.cloud.vmwareengine.v1.VmwareEngine.ListClusters]
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.vmwareengine.ListClustersResponse:
                    Response message for
                [VmwareEngine.ListClusters][google.cloud.vmwareengine.v1.VmwareEngine.ListClusters]

            """

            http_options = (
                _BaseVmwareEngineRestTransport._BaseListClusters._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_clusters(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseListClusters,
                    "_BaseListClusters__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.ListClusters",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "ListClusters",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._ListClusters._get_response(
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
            resp = vmwareengine.ListClustersResponse()
            pb_resp = vmwareengine.ListClustersResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_clusters(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_clusters_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = vmwareengine.ListClustersResponse.to_json(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.list_clusters",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "ListClusters",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListExternalAccessRules(
        _BaseVmwareEngineRestTransport._BaseListExternalAccessRules,
        VmwareEngineRestStub,
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.ListExternalAccessRules")

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
            request: vmwareengine.ListExternalAccessRulesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> vmwareengine.ListExternalAccessRulesResponse:
            r"""Call the list external access
            rules method over HTTP.

                Args:
                    request (~.vmwareengine.ListExternalAccessRulesRequest):
                        The request object. Request message for
                    [VmwareEngine.ListExternalAccessRules][google.cloud.vmwareengine.v1.VmwareEngine.ListExternalAccessRules]
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.vmwareengine.ListExternalAccessRulesResponse:
                        Response message for
                    [VmwareEngine.ListExternalAccessRules][google.cloud.vmwareengine.v1.VmwareEngine.ListExternalAccessRules]

            """

            http_options = _BaseVmwareEngineRestTransport._BaseListExternalAccessRules._get_http_options()
            request, metadata = self._interceptor.pre_list_external_access_rules(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseListExternalAccessRules,
                    "_BaseListExternalAccessRules__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.ListExternalAccessRules",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "ListExternalAccessRules",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._ListExternalAccessRules._get_response(
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
            resp = vmwareengine.ListExternalAccessRulesResponse()
            pb_resp = vmwareengine.ListExternalAccessRulesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_external_access_rules(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_external_access_rules_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        vmwareengine.ListExternalAccessRulesResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.list_external_access_rules",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "ListExternalAccessRules",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListExternalAddresses(
        _BaseVmwareEngineRestTransport._BaseListExternalAddresses, VmwareEngineRestStub
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.ListExternalAddresses")

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
            request: vmwareengine.ListExternalAddressesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> vmwareengine.ListExternalAddressesResponse:
            r"""Call the list external addresses method over HTTP.

            Args:
                request (~.vmwareengine.ListExternalAddressesRequest):
                    The request object. Request message for
                [VmwareEngine.ListExternalAddresses][google.cloud.vmwareengine.v1.VmwareEngine.ListExternalAddresses]
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.vmwareengine.ListExternalAddressesResponse:
                    Response message for
                [VmwareEngine.ListExternalAddresses][google.cloud.vmwareengine.v1.VmwareEngine.ListExternalAddresses]

            """

            http_options = _BaseVmwareEngineRestTransport._BaseListExternalAddresses._get_http_options()
            request, metadata = self._interceptor.pre_list_external_addresses(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseListExternalAddresses,
                    "_BaseListExternalAddresses__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.ListExternalAddresses",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "ListExternalAddresses",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._ListExternalAddresses._get_response(
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
            resp = vmwareengine.ListExternalAddressesResponse()
            pb_resp = vmwareengine.ListExternalAddressesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_external_addresses(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_external_addresses_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        vmwareengine.ListExternalAddressesResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.list_external_addresses",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "ListExternalAddresses",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListHcxActivationKeys(
        _BaseVmwareEngineRestTransport._BaseListHcxActivationKeys, VmwareEngineRestStub
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.ListHcxActivationKeys")

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
            request: vmwareengine.ListHcxActivationKeysRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> vmwareengine.ListHcxActivationKeysResponse:
            r"""Call the list hcx activation keys method over HTTP.

            Args:
                request (~.vmwareengine.ListHcxActivationKeysRequest):
                    The request object. Request message for
                [VmwareEngine.ListHcxActivationKeys][google.cloud.vmwareengine.v1.VmwareEngine.ListHcxActivationKeys]
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.vmwareengine.ListHcxActivationKeysResponse:
                    Response message for
                [VmwareEngine.ListHcxActivationKeys][google.cloud.vmwareengine.v1.VmwareEngine.ListHcxActivationKeys]

            """

            http_options = _BaseVmwareEngineRestTransport._BaseListHcxActivationKeys._get_http_options()
            request, metadata = self._interceptor.pre_list_hcx_activation_keys(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseListHcxActivationKeys,
                    "_BaseListHcxActivationKeys__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.ListHcxActivationKeys",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "ListHcxActivationKeys",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._ListHcxActivationKeys._get_response(
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
            resp = vmwareengine.ListHcxActivationKeysResponse()
            pb_resp = vmwareengine.ListHcxActivationKeysResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_hcx_activation_keys(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_hcx_activation_keys_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        vmwareengine.ListHcxActivationKeysResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.list_hcx_activation_keys",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "ListHcxActivationKeys",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListLoggingServers(
        _BaseVmwareEngineRestTransport._BaseListLoggingServers, VmwareEngineRestStub
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.ListLoggingServers")

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
            request: vmwareengine.ListLoggingServersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> vmwareengine.ListLoggingServersResponse:
            r"""Call the list logging servers method over HTTP.

            Args:
                request (~.vmwareengine.ListLoggingServersRequest):
                    The request object. Request message for
                [VmwareEngine.ListLoggingServers][google.cloud.vmwareengine.v1.VmwareEngine.ListLoggingServers]
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.vmwareengine.ListLoggingServersResponse:
                    Response message for
                [VmwareEngine.ListLoggingServers][google.cloud.vmwareengine.v1.VmwareEngine.ListLoggingServers]

            """

            http_options = _BaseVmwareEngineRestTransport._BaseListLoggingServers._get_http_options()
            request, metadata = self._interceptor.pre_list_logging_servers(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseListLoggingServers,
                    "_BaseListLoggingServers__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.ListLoggingServers",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "ListLoggingServers",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._ListLoggingServers._get_response(
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
            resp = vmwareengine.ListLoggingServersResponse()
            pb_resp = vmwareengine.ListLoggingServersResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_logging_servers(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_logging_servers_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = vmwareengine.ListLoggingServersResponse.to_json(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.list_logging_servers",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "ListLoggingServers",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListManagementDnsZoneBindings(
        _BaseVmwareEngineRestTransport._BaseListManagementDnsZoneBindings,
        VmwareEngineRestStub,
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.ListManagementDnsZoneBindings")

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
            request: vmwareengine.ListManagementDnsZoneBindingsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> vmwareengine.ListManagementDnsZoneBindingsResponse:
            r"""Call the list management dns zone
            bindings method over HTTP.

                Args:
                    request (~.vmwareengine.ListManagementDnsZoneBindingsRequest):
                        The request object. Request message for
                    [VmwareEngine.ListManagementDnsZoneBindings][google.cloud.vmwareengine.v1.VmwareEngine.ListManagementDnsZoneBindings]
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.vmwareengine.ListManagementDnsZoneBindingsResponse:
                        Response message for
                    [VmwareEngine.ListManagementDnsZoneBindings][google.cloud.vmwareengine.v1.VmwareEngine.ListManagementDnsZoneBindings]

            """

            http_options = _BaseVmwareEngineRestTransport._BaseListManagementDnsZoneBindings._get_http_options()
            request, metadata = self._interceptor.pre_list_management_dns_zone_bindings(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseListManagementDnsZoneBindings,
                    "_BaseListManagementDnsZoneBindings__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.ListManagementDnsZoneBindings",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "ListManagementDnsZoneBindings",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                VmwareEngineRestTransport._ListManagementDnsZoneBindings._get_response(
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
            resp = vmwareengine.ListManagementDnsZoneBindingsResponse()
            pb_resp = vmwareengine.ListManagementDnsZoneBindingsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_management_dns_zone_bindings(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_list_management_dns_zone_bindings_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        vmwareengine.ListManagementDnsZoneBindingsResponse.to_json(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.list_management_dns_zone_bindings",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "ListManagementDnsZoneBindings",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListNetworkPeerings(
        _BaseVmwareEngineRestTransport._BaseListNetworkPeerings, VmwareEngineRestStub
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.ListNetworkPeerings")

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
            request: vmwareengine.ListNetworkPeeringsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> vmwareengine.ListNetworkPeeringsResponse:
            r"""Call the list network peerings method over HTTP.

            Args:
                request (~.vmwareengine.ListNetworkPeeringsRequest):
                    The request object. Request message for
                [VmwareEngine.ListNetworkPeerings][google.cloud.vmwareengine.v1.VmwareEngine.ListNetworkPeerings]
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.vmwareengine.ListNetworkPeeringsResponse:
                    Response message for
                [VmwareEngine.ListNetworkPeerings][google.cloud.vmwareengine.v1.VmwareEngine.ListNetworkPeerings]

            """

            http_options = _BaseVmwareEngineRestTransport._BaseListNetworkPeerings._get_http_options()
            request, metadata = self._interceptor.pre_list_network_peerings(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseListNetworkPeerings,
                    "_BaseListNetworkPeerings__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.ListNetworkPeerings",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "ListNetworkPeerings",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._ListNetworkPeerings._get_response(
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
            resp = vmwareengine.ListNetworkPeeringsResponse()
            pb_resp = vmwareengine.ListNetworkPeeringsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_network_peerings(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_network_peerings_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = vmwareengine.ListNetworkPeeringsResponse.to_json(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.list_network_peerings",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "ListNetworkPeerings",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListNetworkPolicies(
        _BaseVmwareEngineRestTransport._BaseListNetworkPolicies, VmwareEngineRestStub
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.ListNetworkPolicies")

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
            request: vmwareengine.ListNetworkPoliciesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> vmwareengine.ListNetworkPoliciesResponse:
            r"""Call the list network policies method over HTTP.

            Args:
                request (~.vmwareengine.ListNetworkPoliciesRequest):
                    The request object. Request message for
                [VmwareEngine.ListNetworkPolicies][google.cloud.vmwareengine.v1.VmwareEngine.ListNetworkPolicies]
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.vmwareengine.ListNetworkPoliciesResponse:
                    Response message for
                [VmwareEngine.ListNetworkPolicies][google.cloud.vmwareengine.v1.VmwareEngine.ListNetworkPolicies]

            """

            http_options = _BaseVmwareEngineRestTransport._BaseListNetworkPolicies._get_http_options()
            request, metadata = self._interceptor.pre_list_network_policies(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseListNetworkPolicies,
                    "_BaseListNetworkPolicies__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.ListNetworkPolicies",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "ListNetworkPolicies",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._ListNetworkPolicies._get_response(
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
            resp = vmwareengine.ListNetworkPoliciesResponse()
            pb_resp = vmwareengine.ListNetworkPoliciesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_network_policies(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_network_policies_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = vmwareengine.ListNetworkPoliciesResponse.to_json(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.list_network_policies",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "ListNetworkPolicies",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListNodes(
        _BaseVmwareEngineRestTransport._BaseListNodes, VmwareEngineRestStub
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.ListNodes")

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
            request: vmwareengine.ListNodesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> vmwareengine.ListNodesResponse:
            r"""Call the list nodes method over HTTP.

            Args:
                request (~.vmwareengine.ListNodesRequest):
                    The request object. Request message for
                [VmwareEngine.ListNodes][google.cloud.vmwareengine.v1.VmwareEngine.ListNodes]
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.vmwareengine.ListNodesResponse:
                    Response message for
                [VmwareEngine.ListNodes][google.cloud.vmwareengine.v1.VmwareEngine.ListNodes]

            """

            http_options = (
                _BaseVmwareEngineRestTransport._BaseListNodes._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_nodes(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseListNodes,
                    "_BaseListNodes__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.ListNodes",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "ListNodes",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._ListNodes._get_response(
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
            resp = vmwareengine.ListNodesResponse()
            pb_resp = vmwareengine.ListNodesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_nodes(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_nodes_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = vmwareengine.ListNodesResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.list_nodes",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "ListNodes",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListNodeTypes(
        _BaseVmwareEngineRestTransport._BaseListNodeTypes, VmwareEngineRestStub
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.ListNodeTypes")

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
            request: vmwareengine.ListNodeTypesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> vmwareengine.ListNodeTypesResponse:
            r"""Call the list node types method over HTTP.

            Args:
                request (~.vmwareengine.ListNodeTypesRequest):
                    The request object. Request message for
                [VmwareEngine.ListNodeTypes][google.cloud.vmwareengine.v1.VmwareEngine.ListNodeTypes]
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.vmwareengine.ListNodeTypesResponse:
                    Response message for
                [VmwareEngine.ListNodeTypes][google.cloud.vmwareengine.v1.VmwareEngine.ListNodeTypes]

            """

            http_options = (
                _BaseVmwareEngineRestTransport._BaseListNodeTypes._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_node_types(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseListNodeTypes,
                    "_BaseListNodeTypes__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.ListNodeTypes",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "ListNodeTypes",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._ListNodeTypes._get_response(
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
            resp = vmwareengine.ListNodeTypesResponse()
            pb_resp = vmwareengine.ListNodeTypesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_node_types(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_node_types_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = vmwareengine.ListNodeTypesResponse.to_json(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.list_node_types",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "ListNodeTypes",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListPeeringRoutes(
        _BaseVmwareEngineRestTransport._BaseListPeeringRoutes, VmwareEngineRestStub
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.ListPeeringRoutes")

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
            request: vmwareengine.ListPeeringRoutesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> vmwareengine.ListPeeringRoutesResponse:
            r"""Call the list peering routes method over HTTP.

            Args:
                request (~.vmwareengine.ListPeeringRoutesRequest):
                    The request object. Request message for
                [VmwareEngine.ListPeeringRoutes][google.cloud.vmwareengine.v1.VmwareEngine.ListPeeringRoutes]
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.vmwareengine.ListPeeringRoutesResponse:
                    Response message for
                [VmwareEngine.ListPeeringRoutes][google.cloud.vmwareengine.v1.VmwareEngine.ListPeeringRoutes]

            """

            http_options = _BaseVmwareEngineRestTransport._BaseListPeeringRoutes._get_http_options()
            request, metadata = self._interceptor.pre_list_peering_routes(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseListPeeringRoutes,
                    "_BaseListPeeringRoutes__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.ListPeeringRoutes",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "ListPeeringRoutes",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._ListPeeringRoutes._get_response(
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
            resp = vmwareengine.ListPeeringRoutesResponse()
            pb_resp = vmwareengine.ListPeeringRoutesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_peering_routes(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_peering_routes_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = vmwareengine.ListPeeringRoutesResponse.to_json(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.list_peering_routes",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "ListPeeringRoutes",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListPrivateClouds(
        _BaseVmwareEngineRestTransport._BaseListPrivateClouds, VmwareEngineRestStub
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.ListPrivateClouds")

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
            request: vmwareengine.ListPrivateCloudsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> vmwareengine.ListPrivateCloudsResponse:
            r"""Call the list private clouds method over HTTP.

            Args:
                request (~.vmwareengine.ListPrivateCloudsRequest):
                    The request object. Request message for
                [VmwareEngine.ListPrivateClouds][google.cloud.vmwareengine.v1.VmwareEngine.ListPrivateClouds]
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.vmwareengine.ListPrivateCloudsResponse:
                    Response message for
                [VmwareEngine.ListPrivateClouds][google.cloud.vmwareengine.v1.VmwareEngine.ListPrivateClouds]

            """

            http_options = _BaseVmwareEngineRestTransport._BaseListPrivateClouds._get_http_options()
            request, metadata = self._interceptor.pre_list_private_clouds(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseListPrivateClouds,
                    "_BaseListPrivateClouds__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.ListPrivateClouds",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "ListPrivateClouds",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._ListPrivateClouds._get_response(
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
            resp = vmwareengine.ListPrivateCloudsResponse()
            pb_resp = vmwareengine.ListPrivateCloudsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_private_clouds(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_private_clouds_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = vmwareengine.ListPrivateCloudsResponse.to_json(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.list_private_clouds",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "ListPrivateClouds",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListPrivateConnectionPeeringRoutes(
        _BaseVmwareEngineRestTransport._BaseListPrivateConnectionPeeringRoutes,
        VmwareEngineRestStub,
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.ListPrivateConnectionPeeringRoutes")

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
            request: vmwareengine.ListPrivateConnectionPeeringRoutesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> vmwareengine.ListPrivateConnectionPeeringRoutesResponse:
            r"""Call the list private connection
            peering routes method over HTTP.

                Args:
                    request (~.vmwareengine.ListPrivateConnectionPeeringRoutesRequest):
                        The request object. Request message for
                    [VmwareEngine.ListPrivateConnectionPeeringRoutes][google.cloud.vmwareengine.v1.VmwareEngine.ListPrivateConnectionPeeringRoutes]
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.vmwareengine.ListPrivateConnectionPeeringRoutesResponse:
                        Response message for
                    [VmwareEngine.ListPrivateConnectionPeeringRoutes][google.cloud.vmwareengine.v1.VmwareEngine.ListPrivateConnectionPeeringRoutes]

            """

            http_options = _BaseVmwareEngineRestTransport._BaseListPrivateConnectionPeeringRoutes._get_http_options()
            request, metadata = (
                self._interceptor.pre_list_private_connection_peering_routes(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseListPrivateConnectionPeeringRoutes,
                    "_BaseListPrivateConnectionPeeringRoutes__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.ListPrivateConnectionPeeringRoutes",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "ListPrivateConnectionPeeringRoutes",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._ListPrivateConnectionPeeringRoutes._get_response(
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
            resp = vmwareengine.ListPrivateConnectionPeeringRoutesResponse()
            pb_resp = vmwareengine.ListPrivateConnectionPeeringRoutesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_private_connection_peering_routes(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_list_private_connection_peering_routes_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        vmwareengine.ListPrivateConnectionPeeringRoutesResponse.to_json(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.list_private_connection_peering_routes",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "ListPrivateConnectionPeeringRoutes",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListPrivateConnections(
        _BaseVmwareEngineRestTransport._BaseListPrivateConnections, VmwareEngineRestStub
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.ListPrivateConnections")

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
            request: vmwareengine.ListPrivateConnectionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> vmwareengine.ListPrivateConnectionsResponse:
            r"""Call the list private connections method over HTTP.

            Args:
                request (~.vmwareengine.ListPrivateConnectionsRequest):
                    The request object. Request message for
                [VmwareEngine.ListPrivateConnections][google.cloud.vmwareengine.v1.VmwareEngine.ListPrivateConnections]
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.vmwareengine.ListPrivateConnectionsResponse:
                    Response message for
                [VmwareEngine.ListPrivateConnections][google.cloud.vmwareengine.v1.VmwareEngine.ListPrivateConnections]

            """

            http_options = _BaseVmwareEngineRestTransport._BaseListPrivateConnections._get_http_options()
            request, metadata = self._interceptor.pre_list_private_connections(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseListPrivateConnections,
                    "_BaseListPrivateConnections__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.ListPrivateConnections",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "ListPrivateConnections",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._ListPrivateConnections._get_response(
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
            resp = vmwareengine.ListPrivateConnectionsResponse()
            pb_resp = vmwareengine.ListPrivateConnectionsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_private_connections(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_private_connections_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        vmwareengine.ListPrivateConnectionsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.list_private_connections",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "ListPrivateConnections",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListSubnets(
        _BaseVmwareEngineRestTransport._BaseListSubnets, VmwareEngineRestStub
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.ListSubnets")

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
            request: vmwareengine.ListSubnetsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> vmwareengine.ListSubnetsResponse:
            r"""Call the list subnets method over HTTP.

            Args:
                request (~.vmwareengine.ListSubnetsRequest):
                    The request object. Request message for
                [VmwareEngine.ListSubnets][google.cloud.vmwareengine.v1.VmwareEngine.ListSubnets]
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.vmwareengine.ListSubnetsResponse:
                    Response message for
                [VmwareEngine.ListSubnets][google.cloud.vmwareengine.v1.VmwareEngine.ListSubnets]

            """

            http_options = (
                _BaseVmwareEngineRestTransport._BaseListSubnets._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_subnets(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseListSubnets,
                    "_BaseListSubnets__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.ListSubnets",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "ListSubnets",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._ListSubnets._get_response(
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
            resp = vmwareengine.ListSubnetsResponse()
            pb_resp = vmwareengine.ListSubnetsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_subnets(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_subnets_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = vmwareengine.ListSubnetsResponse.to_json(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.list_subnets",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "ListSubnets",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListVmwareEngineNetworks(
        _BaseVmwareEngineRestTransport._BaseListVmwareEngineNetworks,
        VmwareEngineRestStub,
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.ListVmwareEngineNetworks")

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
            request: vmwareengine.ListVmwareEngineNetworksRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> vmwareengine.ListVmwareEngineNetworksResponse:
            r"""Call the list vmware engine
            networks method over HTTP.

                Args:
                    request (~.vmwareengine.ListVmwareEngineNetworksRequest):
                        The request object. Request message for
                    [VmwareEngine.ListVmwareEngineNetworks][google.cloud.vmwareengine.v1.VmwareEngine.ListVmwareEngineNetworks]
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.vmwareengine.ListVmwareEngineNetworksResponse:
                        Response message for
                    [VmwareEngine.ListVmwareEngineNetworks][google.cloud.vmwareengine.v1.VmwareEngine.ListVmwareEngineNetworks]

            """

            http_options = _BaseVmwareEngineRestTransport._BaseListVmwareEngineNetworks._get_http_options()
            request, metadata = self._interceptor.pre_list_vmware_engine_networks(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseListVmwareEngineNetworks,
                    "_BaseListVmwareEngineNetworks__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.ListVmwareEngineNetworks",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "ListVmwareEngineNetworks",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                VmwareEngineRestTransport._ListVmwareEngineNetworks._get_response(
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
            resp = vmwareengine.ListVmwareEngineNetworksResponse()
            pb_resp = vmwareengine.ListVmwareEngineNetworksResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_vmware_engine_networks(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_vmware_engine_networks_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        vmwareengine.ListVmwareEngineNetworksResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.list_vmware_engine_networks",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "ListVmwareEngineNetworks",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RepairManagementDnsZoneBinding(
        _BaseVmwareEngineRestTransport._BaseRepairManagementDnsZoneBinding,
        VmwareEngineRestStub,
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.RepairManagementDnsZoneBinding")

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
            request: vmwareengine.RepairManagementDnsZoneBindingRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the repair management dns
            zone binding method over HTTP.

                Args:
                    request (~.vmwareengine.RepairManagementDnsZoneBindingRequest):
                        The request object. Request message for
                    [VmwareEngine.RepairManagementDnsZoneBindings][]
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

            http_options = _BaseVmwareEngineRestTransport._BaseRepairManagementDnsZoneBinding._get_http_options()
            request, metadata = (
                self._interceptor.pre_repair_management_dns_zone_binding(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseRepairManagementDnsZoneBinding,
                    "_BaseRepairManagementDnsZoneBinding__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.RepairManagementDnsZoneBinding",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "RepairManagementDnsZoneBinding",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                VmwareEngineRestTransport._RepairManagementDnsZoneBinding._get_response(
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

            resp = self._interceptor.post_repair_management_dns_zone_binding(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_repair_management_dns_zone_binding_with_metadata(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.repair_management_dns_zone_binding",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "RepairManagementDnsZoneBinding",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ResetNsxCredentials(
        _BaseVmwareEngineRestTransport._BaseResetNsxCredentials, VmwareEngineRestStub
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.ResetNsxCredentials")

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
            request: vmwareengine.ResetNsxCredentialsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the reset nsx credentials method over HTTP.

            Args:
                request (~.vmwareengine.ResetNsxCredentialsRequest):
                    The request object. Request message for
                [VmwareEngine.ResetNsxCredentials][google.cloud.vmwareengine.v1.VmwareEngine.ResetNsxCredentials]
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

            http_options = _BaseVmwareEngineRestTransport._BaseResetNsxCredentials._get_http_options()
            request, metadata = self._interceptor.pre_reset_nsx_credentials(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseResetNsxCredentials,
                    "_BaseResetNsxCredentials__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.ResetNsxCredentials",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "ResetNsxCredentials",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._ResetNsxCredentials._get_response(
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

            resp = self._interceptor.post_reset_nsx_credentials(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_reset_nsx_credentials_with_metadata(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.reset_nsx_credentials",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "ResetNsxCredentials",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ResetVcenterCredentials(
        _BaseVmwareEngineRestTransport._BaseResetVcenterCredentials,
        VmwareEngineRestStub,
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.ResetVcenterCredentials")

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
            request: vmwareengine.ResetVcenterCredentialsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the reset vcenter credentials method over HTTP.

            Args:
                request (~.vmwareengine.ResetVcenterCredentialsRequest):
                    The request object. Request message for
                [VmwareEngine.ResetVcenterCredentials][google.cloud.vmwareengine.v1.VmwareEngine.ResetVcenterCredentials]
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

            http_options = _BaseVmwareEngineRestTransport._BaseResetVcenterCredentials._get_http_options()
            request, metadata = self._interceptor.pre_reset_vcenter_credentials(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseResetVcenterCredentials,
                    "_BaseResetVcenterCredentials__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.ResetVcenterCredentials",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "ResetVcenterCredentials",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._ResetVcenterCredentials._get_response(
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

            resp = self._interceptor.post_reset_vcenter_credentials(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_reset_vcenter_credentials_with_metadata(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.reset_vcenter_credentials",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "ResetVcenterCredentials",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RevokeDnsBindPermission(
        _BaseVmwareEngineRestTransport._BaseRevokeDnsBindPermission,
        VmwareEngineRestStub,
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.RevokeDnsBindPermission")

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
            request: vmwareengine.RevokeDnsBindPermissionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the revoke dns bind
            permission method over HTTP.

                Args:
                    request (~.vmwareengine.RevokeDnsBindPermissionRequest):
                        The request object. Request message for
                    [VmwareEngine.RevokeDnsBindPermission][google.cloud.vmwareengine.v1.VmwareEngine.RevokeDnsBindPermission]
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

            http_options = _BaseVmwareEngineRestTransport._BaseRevokeDnsBindPermission._get_http_options()
            request, metadata = self._interceptor.pre_revoke_dns_bind_permission(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseRevokeDnsBindPermission,
                    "_BaseRevokeDnsBindPermission__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.RevokeDnsBindPermission",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "RevokeDnsBindPermission",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._RevokeDnsBindPermission._get_response(
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

            resp = self._interceptor.post_revoke_dns_bind_permission(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_revoke_dns_bind_permission_with_metadata(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.revoke_dns_bind_permission",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "RevokeDnsBindPermission",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ShowNsxCredentials(
        _BaseVmwareEngineRestTransport._BaseShowNsxCredentials, VmwareEngineRestStub
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.ShowNsxCredentials")

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
            request: vmwareengine.ShowNsxCredentialsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> vmwareengine_resources.Credentials:
            r"""Call the show nsx credentials method over HTTP.

            Args:
                request (~.vmwareengine.ShowNsxCredentialsRequest):
                    The request object. Request message for
                [VmwareEngine.ShowNsxCredentials][google.cloud.vmwareengine.v1.VmwareEngine.ShowNsxCredentials]
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.vmwareengine_resources.Credentials:
                    Credentials for a private cloud.
            """

            http_options = _BaseVmwareEngineRestTransport._BaseShowNsxCredentials._get_http_options()
            request, metadata = self._interceptor.pre_show_nsx_credentials(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseShowNsxCredentials,
                    "_BaseShowNsxCredentials__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.ShowNsxCredentials",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "ShowNsxCredentials",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._ShowNsxCredentials._get_response(
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
            resp = vmwareengine_resources.Credentials()
            pb_resp = vmwareengine_resources.Credentials.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_show_nsx_credentials(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_show_nsx_credentials_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = vmwareengine_resources.Credentials.to_json(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.show_nsx_credentials",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "ShowNsxCredentials",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ShowVcenterCredentials(
        _BaseVmwareEngineRestTransport._BaseShowVcenterCredentials, VmwareEngineRestStub
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.ShowVcenterCredentials")

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
            request: vmwareengine.ShowVcenterCredentialsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> vmwareengine_resources.Credentials:
            r"""Call the show vcenter credentials method over HTTP.

            Args:
                request (~.vmwareengine.ShowVcenterCredentialsRequest):
                    The request object. Request message for
                [VmwareEngine.ShowVcenterCredentials][google.cloud.vmwareengine.v1.VmwareEngine.ShowVcenterCredentials]
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.vmwareengine_resources.Credentials:
                    Credentials for a private cloud.
            """

            http_options = _BaseVmwareEngineRestTransport._BaseShowVcenterCredentials._get_http_options()
            request, metadata = self._interceptor.pre_show_vcenter_credentials(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseShowVcenterCredentials,
                    "_BaseShowVcenterCredentials__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.ShowVcenterCredentials",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "ShowVcenterCredentials",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._ShowVcenterCredentials._get_response(
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
            resp = vmwareengine_resources.Credentials()
            pb_resp = vmwareengine_resources.Credentials.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_show_vcenter_credentials(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_show_vcenter_credentials_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = vmwareengine_resources.Credentials.to_json(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.show_vcenter_credentials",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "ShowVcenterCredentials",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UndeletePrivateCloud(
        _BaseVmwareEngineRestTransport._BaseUndeletePrivateCloud, VmwareEngineRestStub
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.UndeletePrivateCloud")

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
            request: vmwareengine.UndeletePrivateCloudRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the undelete private cloud method over HTTP.

            Args:
                request (~.vmwareengine.UndeletePrivateCloudRequest):
                    The request object. Request message for
                [VmwareEngine.UndeletePrivateCloud][google.cloud.vmwareengine.v1.VmwareEngine.UndeletePrivateCloud]
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

            http_options = _BaseVmwareEngineRestTransport._BaseUndeletePrivateCloud._get_http_options()
            request, metadata = self._interceptor.pre_undelete_private_cloud(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseUndeletePrivateCloud,
                    "_BaseUndeletePrivateCloud__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.UndeletePrivateCloud",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "UndeletePrivateCloud",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._UndeletePrivateCloud._get_response(
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

            resp = self._interceptor.post_undelete_private_cloud(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_undelete_private_cloud_with_metadata(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.undelete_private_cloud",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "UndeletePrivateCloud",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateCluster(
        _BaseVmwareEngineRestTransport._BaseUpdateCluster, VmwareEngineRestStub
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.UpdateCluster")

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
            request: vmwareengine.UpdateClusterRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update cluster method over HTTP.

            Args:
                request (~.vmwareengine.UpdateClusterRequest):
                    The request object. Request message for
                [VmwareEngine.UpdateCluster][google.cloud.vmwareengine.v1.VmwareEngine.UpdateCluster]
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
                _BaseVmwareEngineRestTransport._BaseUpdateCluster._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_cluster(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseUpdateCluster,
                    "_BaseUpdateCluster__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.UpdateCluster",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "UpdateCluster",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._UpdateCluster._get_response(
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

            resp = self._interceptor.post_update_cluster(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_cluster_with_metadata(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.update_cluster",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "UpdateCluster",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateDnsForwarding(
        _BaseVmwareEngineRestTransport._BaseUpdateDnsForwarding, VmwareEngineRestStub
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.UpdateDnsForwarding")

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
            request: vmwareengine.UpdateDnsForwardingRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update dns forwarding method over HTTP.

            Args:
                request (~.vmwareengine.UpdateDnsForwardingRequest):
                    The request object. Request message for
                [VmwareEngine.UpdateDnsForwarding][google.cloud.vmwareengine.v1.VmwareEngine.UpdateDnsForwarding]
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

            http_options = _BaseVmwareEngineRestTransport._BaseUpdateDnsForwarding._get_http_options()
            request, metadata = self._interceptor.pre_update_dns_forwarding(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseUpdateDnsForwarding,
                    "_BaseUpdateDnsForwarding__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.UpdateDnsForwarding",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "UpdateDnsForwarding",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._UpdateDnsForwarding._get_response(
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

            resp = self._interceptor.post_update_dns_forwarding(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_dns_forwarding_with_metadata(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.update_dns_forwarding",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "UpdateDnsForwarding",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateExternalAccessRule(
        _BaseVmwareEngineRestTransport._BaseUpdateExternalAccessRule,
        VmwareEngineRestStub,
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.UpdateExternalAccessRule")

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
            request: vmwareengine.UpdateExternalAccessRuleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update external access
            rule method over HTTP.

                Args:
                    request (~.vmwareengine.UpdateExternalAccessRuleRequest):
                        The request object. Request message for
                    [VmwareEngine.UpdateExternalAccessRule][google.cloud.vmwareengine.v1.VmwareEngine.UpdateExternalAccessRule]
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

            http_options = _BaseVmwareEngineRestTransport._BaseUpdateExternalAccessRule._get_http_options()
            request, metadata = self._interceptor.pre_update_external_access_rule(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseUpdateExternalAccessRule,
                    "_BaseUpdateExternalAccessRule__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.UpdateExternalAccessRule",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "UpdateExternalAccessRule",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                VmwareEngineRestTransport._UpdateExternalAccessRule._get_response(
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

            resp = self._interceptor.post_update_external_access_rule(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_external_access_rule_with_metadata(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.update_external_access_rule",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "UpdateExternalAccessRule",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateExternalAddress(
        _BaseVmwareEngineRestTransport._BaseUpdateExternalAddress, VmwareEngineRestStub
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.UpdateExternalAddress")

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
            request: vmwareengine.UpdateExternalAddressRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update external address method over HTTP.

            Args:
                request (~.vmwareengine.UpdateExternalAddressRequest):
                    The request object. Request message for
                [VmwareEngine.UpdateExternalAddress][google.cloud.vmwareengine.v1.VmwareEngine.UpdateExternalAddress]
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

            http_options = _BaseVmwareEngineRestTransport._BaseUpdateExternalAddress._get_http_options()
            request, metadata = self._interceptor.pre_update_external_address(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseUpdateExternalAddress,
                    "_BaseUpdateExternalAddress__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.UpdateExternalAddress",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "UpdateExternalAddress",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._UpdateExternalAddress._get_response(
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

            resp = self._interceptor.post_update_external_address(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_external_address_with_metadata(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.update_external_address",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "UpdateExternalAddress",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateLoggingServer(
        _BaseVmwareEngineRestTransport._BaseUpdateLoggingServer, VmwareEngineRestStub
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.UpdateLoggingServer")

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
            request: vmwareengine.UpdateLoggingServerRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update logging server method over HTTP.

            Args:
                request (~.vmwareengine.UpdateLoggingServerRequest):
                    The request object. Request message for
                [VmwareEngine.UpdateLoggingServer][google.cloud.vmwareengine.v1.VmwareEngine.UpdateLoggingServer]
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

            http_options = _BaseVmwareEngineRestTransport._BaseUpdateLoggingServer._get_http_options()
            request, metadata = self._interceptor.pre_update_logging_server(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseUpdateLoggingServer,
                    "_BaseUpdateLoggingServer__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.UpdateLoggingServer",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "UpdateLoggingServer",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._UpdateLoggingServer._get_response(
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

            resp = self._interceptor.post_update_logging_server(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_logging_server_with_metadata(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.update_logging_server",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "UpdateLoggingServer",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateManagementDnsZoneBinding(
        _BaseVmwareEngineRestTransport._BaseUpdateManagementDnsZoneBinding,
        VmwareEngineRestStub,
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.UpdateManagementDnsZoneBinding")

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
            request: vmwareengine.UpdateManagementDnsZoneBindingRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update management dns
            zone binding method over HTTP.

                Args:
                    request (~.vmwareengine.UpdateManagementDnsZoneBindingRequest):
                        The request object. Request message for
                    [VmwareEngine.UpdateManagementDnsZoneBinding][google.cloud.vmwareengine.v1.VmwareEngine.UpdateManagementDnsZoneBinding]
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

            http_options = _BaseVmwareEngineRestTransport._BaseUpdateManagementDnsZoneBinding._get_http_options()
            request, metadata = (
                self._interceptor.pre_update_management_dns_zone_binding(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseUpdateManagementDnsZoneBinding,
                    "_BaseUpdateManagementDnsZoneBinding__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.UpdateManagementDnsZoneBinding",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "UpdateManagementDnsZoneBinding",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                VmwareEngineRestTransport._UpdateManagementDnsZoneBinding._get_response(
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

            resp = self._interceptor.post_update_management_dns_zone_binding(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_update_management_dns_zone_binding_with_metadata(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.update_management_dns_zone_binding",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "UpdateManagementDnsZoneBinding",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateNetworkPeering(
        _BaseVmwareEngineRestTransport._BaseUpdateNetworkPeering, VmwareEngineRestStub
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.UpdateNetworkPeering")

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
            request: vmwareengine.UpdateNetworkPeeringRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update network peering method over HTTP.

            Args:
                request (~.vmwareengine.UpdateNetworkPeeringRequest):
                    The request object. Request message for
                [VmwareEngine.UpdateNetworkPeering][google.cloud.vmwareengine.v1.VmwareEngine.UpdateNetworkPeering]
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

            http_options = _BaseVmwareEngineRestTransport._BaseUpdateNetworkPeering._get_http_options()
            request, metadata = self._interceptor.pre_update_network_peering(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseUpdateNetworkPeering,
                    "_BaseUpdateNetworkPeering__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.UpdateNetworkPeering",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "UpdateNetworkPeering",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._UpdateNetworkPeering._get_response(
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

            resp = self._interceptor.post_update_network_peering(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_network_peering_with_metadata(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.update_network_peering",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "UpdateNetworkPeering",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateNetworkPolicy(
        _BaseVmwareEngineRestTransport._BaseUpdateNetworkPolicy, VmwareEngineRestStub
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.UpdateNetworkPolicy")

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
            request: vmwareengine.UpdateNetworkPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update network policy method over HTTP.

            Args:
                request (~.vmwareengine.UpdateNetworkPolicyRequest):
                    The request object. Request message for
                [VmwareEngine.UpdateNetworkPolicy][google.cloud.vmwareengine.v1.VmwareEngine.UpdateNetworkPolicy]
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

            http_options = _BaseVmwareEngineRestTransport._BaseUpdateNetworkPolicy._get_http_options()
            request, metadata = self._interceptor.pre_update_network_policy(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseUpdateNetworkPolicy,
                    "_BaseUpdateNetworkPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.UpdateNetworkPolicy",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "UpdateNetworkPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._UpdateNetworkPolicy._get_response(
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

            resp = self._interceptor.post_update_network_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_network_policy_with_metadata(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.update_network_policy",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "UpdateNetworkPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdatePrivateCloud(
        _BaseVmwareEngineRestTransport._BaseUpdatePrivateCloud, VmwareEngineRestStub
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.UpdatePrivateCloud")

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
            request: vmwareengine.UpdatePrivateCloudRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update private cloud method over HTTP.

            Args:
                request (~.vmwareengine.UpdatePrivateCloudRequest):
                    The request object. Request message for
                [VmwareEngine.UpdatePrivateCloud][google.cloud.vmwareengine.v1.VmwareEngine.UpdatePrivateCloud]
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

            http_options = _BaseVmwareEngineRestTransport._BaseUpdatePrivateCloud._get_http_options()
            request, metadata = self._interceptor.pre_update_private_cloud(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseUpdatePrivateCloud,
                    "_BaseUpdatePrivateCloud__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.UpdatePrivateCloud",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "UpdatePrivateCloud",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._UpdatePrivateCloud._get_response(
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

            resp = self._interceptor.post_update_private_cloud(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_private_cloud_with_metadata(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.update_private_cloud",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "UpdatePrivateCloud",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdatePrivateConnection(
        _BaseVmwareEngineRestTransport._BaseUpdatePrivateConnection,
        VmwareEngineRestStub,
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.UpdatePrivateConnection")

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
            request: vmwareengine.UpdatePrivateConnectionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update private connection method over HTTP.

            Args:
                request (~.vmwareengine.UpdatePrivateConnectionRequest):
                    The request object. Request message for
                [VmwareEngine.UpdatePrivateConnection][google.cloud.vmwareengine.v1.VmwareEngine.UpdatePrivateConnection]
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

            http_options = _BaseVmwareEngineRestTransport._BaseUpdatePrivateConnection._get_http_options()
            request, metadata = self._interceptor.pre_update_private_connection(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseUpdatePrivateConnection,
                    "_BaseUpdatePrivateConnection__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.UpdatePrivateConnection",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "UpdatePrivateConnection",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._UpdatePrivateConnection._get_response(
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

            resp = self._interceptor.post_update_private_connection(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_private_connection_with_metadata(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.update_private_connection",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "UpdatePrivateConnection",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateSubnet(
        _BaseVmwareEngineRestTransport._BaseUpdateSubnet, VmwareEngineRestStub
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.UpdateSubnet")

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
            request: vmwareengine.UpdateSubnetRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update subnet method over HTTP.

            Args:
                request (~.vmwareengine.UpdateSubnetRequest):
                    The request object. Request message for
                [VmwareEngine.UpdateSubnet][google.cloud.vmwareengine.v1.VmwareEngine.UpdateSubnet]
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
                _BaseVmwareEngineRestTransport._BaseUpdateSubnet._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_subnet(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseUpdateSubnet,
                    "_BaseUpdateSubnet__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.UpdateSubnet",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "UpdateSubnet",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._UpdateSubnet._get_response(
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

            resp = self._interceptor.post_update_subnet(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_subnet_with_metadata(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.update_subnet",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "UpdateSubnet",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateVmwareEngineNetwork(
        _BaseVmwareEngineRestTransport._BaseUpdateVmwareEngineNetwork,
        VmwareEngineRestStub,
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.UpdateVmwareEngineNetwork")

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
            request: vmwareengine.UpdateVmwareEngineNetworkRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update vmware engine
            network method over HTTP.

                Args:
                    request (~.vmwareengine.UpdateVmwareEngineNetworkRequest):
                        The request object. Request message for
                    [VmwareEngine.UpdateVmwareEngineNetwork][google.cloud.vmwareengine.v1.VmwareEngine.UpdateVmwareEngineNetwork]
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

            http_options = _BaseVmwareEngineRestTransport._BaseUpdateVmwareEngineNetwork._get_http_options()
            request, metadata = self._interceptor.pre_update_vmware_engine_network(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseUpdateVmwareEngineNetwork,
                    "_BaseUpdateVmwareEngineNetwork__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.UpdateVmwareEngineNetwork",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "UpdateVmwareEngineNetwork",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                VmwareEngineRestTransport._UpdateVmwareEngineNetwork._get_response(
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

            resp = self._interceptor.post_update_vmware_engine_network(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_vmware_engine_network_with_metadata(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineClient.update_vmware_engine_network",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "UpdateVmwareEngineNetwork",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_cluster(
        self,
    ) -> Callable[[vmwareengine.CreateClusterRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateCluster(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_external_access_rule(
        self,
    ) -> Callable[
        [vmwareengine.CreateExternalAccessRuleRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateExternalAccessRule(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_external_address(
        self,
    ) -> Callable[
        [vmwareengine.CreateExternalAddressRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateExternalAddress(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_hcx_activation_key(
        self,
    ) -> Callable[
        [vmwareengine.CreateHcxActivationKeyRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateHcxActivationKey(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_logging_server(
        self,
    ) -> Callable[[vmwareengine.CreateLoggingServerRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateLoggingServer(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_management_dns_zone_binding(
        self,
    ) -> Callable[
        [vmwareengine.CreateManagementDnsZoneBindingRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateManagementDnsZoneBinding(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_network_peering(
        self,
    ) -> Callable[[vmwareengine.CreateNetworkPeeringRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateNetworkPeering(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_network_policy(
        self,
    ) -> Callable[[vmwareengine.CreateNetworkPolicyRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateNetworkPolicy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_private_cloud(
        self,
    ) -> Callable[[vmwareengine.CreatePrivateCloudRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreatePrivateCloud(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_private_connection(
        self,
    ) -> Callable[
        [vmwareengine.CreatePrivateConnectionRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreatePrivateConnection(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_vmware_engine_network(
        self,
    ) -> Callable[
        [vmwareengine.CreateVmwareEngineNetworkRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateVmwareEngineNetwork(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_cluster(
        self,
    ) -> Callable[[vmwareengine.DeleteClusterRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteCluster(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_external_access_rule(
        self,
    ) -> Callable[
        [vmwareengine.DeleteExternalAccessRuleRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteExternalAccessRule(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_external_address(
        self,
    ) -> Callable[
        [vmwareengine.DeleteExternalAddressRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteExternalAddress(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_logging_server(
        self,
    ) -> Callable[[vmwareengine.DeleteLoggingServerRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteLoggingServer(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_management_dns_zone_binding(
        self,
    ) -> Callable[
        [vmwareengine.DeleteManagementDnsZoneBindingRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteManagementDnsZoneBinding(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_network_peering(
        self,
    ) -> Callable[[vmwareengine.DeleteNetworkPeeringRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteNetworkPeering(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_network_policy(
        self,
    ) -> Callable[[vmwareengine.DeleteNetworkPolicyRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteNetworkPolicy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_private_cloud(
        self,
    ) -> Callable[[vmwareengine.DeletePrivateCloudRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeletePrivateCloud(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_private_connection(
        self,
    ) -> Callable[
        [vmwareengine.DeletePrivateConnectionRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeletePrivateConnection(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_vmware_engine_network(
        self,
    ) -> Callable[
        [vmwareengine.DeleteVmwareEngineNetworkRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteVmwareEngineNetwork(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def fetch_network_policy_external_addresses(
        self,
    ) -> Callable[
        [vmwareengine.FetchNetworkPolicyExternalAddressesRequest],
        vmwareengine.FetchNetworkPolicyExternalAddressesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._FetchNetworkPolicyExternalAddresses(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_cluster(
        self,
    ) -> Callable[[vmwareengine.GetClusterRequest], vmwareengine_resources.Cluster]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetCluster(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_dns_bind_permission(
        self,
    ) -> Callable[
        [vmwareengine.GetDnsBindPermissionRequest],
        vmwareengine_resources.DnsBindPermission,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetDnsBindPermission(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_dns_forwarding(
        self,
    ) -> Callable[
        [vmwareengine.GetDnsForwardingRequest], vmwareengine_resources.DnsForwarding
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetDnsForwarding(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_external_access_rule(
        self,
    ) -> Callable[
        [vmwareengine.GetExternalAccessRuleRequest],
        vmwareengine_resources.ExternalAccessRule,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetExternalAccessRule(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_external_address(
        self,
    ) -> Callable[
        [vmwareengine.GetExternalAddressRequest], vmwareengine_resources.ExternalAddress
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetExternalAddress(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_hcx_activation_key(
        self,
    ) -> Callable[
        [vmwareengine.GetHcxActivationKeyRequest],
        vmwareengine_resources.HcxActivationKey,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetHcxActivationKey(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_logging_server(
        self,
    ) -> Callable[
        [vmwareengine.GetLoggingServerRequest], vmwareengine_resources.LoggingServer
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetLoggingServer(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_management_dns_zone_binding(
        self,
    ) -> Callable[
        [vmwareengine.GetManagementDnsZoneBindingRequest],
        vmwareengine_resources.ManagementDnsZoneBinding,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetManagementDnsZoneBinding(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_network_peering(
        self,
    ) -> Callable[
        [vmwareengine.GetNetworkPeeringRequest], vmwareengine_resources.NetworkPeering
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetNetworkPeering(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_network_policy(
        self,
    ) -> Callable[
        [vmwareengine.GetNetworkPolicyRequest], vmwareengine_resources.NetworkPolicy
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetNetworkPolicy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_node(
        self,
    ) -> Callable[[vmwareengine.GetNodeRequest], vmwareengine_resources.Node]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetNode(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_node_type(
        self,
    ) -> Callable[[vmwareengine.GetNodeTypeRequest], vmwareengine_resources.NodeType]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetNodeType(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_private_cloud(
        self,
    ) -> Callable[
        [vmwareengine.GetPrivateCloudRequest], vmwareengine_resources.PrivateCloud
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetPrivateCloud(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_private_connection(
        self,
    ) -> Callable[
        [vmwareengine.GetPrivateConnectionRequest],
        vmwareengine_resources.PrivateConnection,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetPrivateConnection(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_subnet(
        self,
    ) -> Callable[[vmwareengine.GetSubnetRequest], vmwareengine_resources.Subnet]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetSubnet(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_vmware_engine_network(
        self,
    ) -> Callable[
        [vmwareengine.GetVmwareEngineNetworkRequest],
        vmwareengine_resources.VmwareEngineNetwork,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetVmwareEngineNetwork(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def grant_dns_bind_permission(
        self,
    ) -> Callable[
        [vmwareengine.GrantDnsBindPermissionRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GrantDnsBindPermission(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_clusters(
        self,
    ) -> Callable[
        [vmwareengine.ListClustersRequest], vmwareengine.ListClustersResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListClusters(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_external_access_rules(
        self,
    ) -> Callable[
        [vmwareengine.ListExternalAccessRulesRequest],
        vmwareengine.ListExternalAccessRulesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListExternalAccessRules(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_external_addresses(
        self,
    ) -> Callable[
        [vmwareengine.ListExternalAddressesRequest],
        vmwareengine.ListExternalAddressesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListExternalAddresses(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_hcx_activation_keys(
        self,
    ) -> Callable[
        [vmwareengine.ListHcxActivationKeysRequest],
        vmwareengine.ListHcxActivationKeysResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListHcxActivationKeys(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_logging_servers(
        self,
    ) -> Callable[
        [vmwareengine.ListLoggingServersRequest],
        vmwareengine.ListLoggingServersResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListLoggingServers(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_management_dns_zone_bindings(
        self,
    ) -> Callable[
        [vmwareengine.ListManagementDnsZoneBindingsRequest],
        vmwareengine.ListManagementDnsZoneBindingsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListManagementDnsZoneBindings(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_network_peerings(
        self,
    ) -> Callable[
        [vmwareengine.ListNetworkPeeringsRequest],
        vmwareengine.ListNetworkPeeringsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListNetworkPeerings(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_network_policies(
        self,
    ) -> Callable[
        [vmwareengine.ListNetworkPoliciesRequest],
        vmwareengine.ListNetworkPoliciesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListNetworkPolicies(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_nodes(
        self,
    ) -> Callable[[vmwareengine.ListNodesRequest], vmwareengine.ListNodesResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListNodes(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_node_types(
        self,
    ) -> Callable[
        [vmwareengine.ListNodeTypesRequest], vmwareengine.ListNodeTypesResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListNodeTypes(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_peering_routes(
        self,
    ) -> Callable[
        [vmwareengine.ListPeeringRoutesRequest], vmwareengine.ListPeeringRoutesResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListPeeringRoutes(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_private_clouds(
        self,
    ) -> Callable[
        [vmwareengine.ListPrivateCloudsRequest], vmwareengine.ListPrivateCloudsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListPrivateClouds(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_private_connection_peering_routes(
        self,
    ) -> Callable[
        [vmwareengine.ListPrivateConnectionPeeringRoutesRequest],
        vmwareengine.ListPrivateConnectionPeeringRoutesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListPrivateConnectionPeeringRoutes(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_private_connections(
        self,
    ) -> Callable[
        [vmwareengine.ListPrivateConnectionsRequest],
        vmwareengine.ListPrivateConnectionsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListPrivateConnections(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_subnets(
        self,
    ) -> Callable[[vmwareengine.ListSubnetsRequest], vmwareengine.ListSubnetsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListSubnets(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_vmware_engine_networks(
        self,
    ) -> Callable[
        [vmwareengine.ListVmwareEngineNetworksRequest],
        vmwareengine.ListVmwareEngineNetworksResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListVmwareEngineNetworks(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def repair_management_dns_zone_binding(
        self,
    ) -> Callable[
        [vmwareengine.RepairManagementDnsZoneBindingRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RepairManagementDnsZoneBinding(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def reset_nsx_credentials(
        self,
    ) -> Callable[[vmwareengine.ResetNsxCredentialsRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ResetNsxCredentials(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def reset_vcenter_credentials(
        self,
    ) -> Callable[
        [vmwareengine.ResetVcenterCredentialsRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ResetVcenterCredentials(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def revoke_dns_bind_permission(
        self,
    ) -> Callable[
        [vmwareengine.RevokeDnsBindPermissionRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RevokeDnsBindPermission(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def show_nsx_credentials(
        self,
    ) -> Callable[
        [vmwareengine.ShowNsxCredentialsRequest], vmwareengine_resources.Credentials
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ShowNsxCredentials(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def show_vcenter_credentials(
        self,
    ) -> Callable[
        [vmwareengine.ShowVcenterCredentialsRequest], vmwareengine_resources.Credentials
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ShowVcenterCredentials(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def undelete_private_cloud(
        self,
    ) -> Callable[[vmwareengine.UndeletePrivateCloudRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UndeletePrivateCloud(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_cluster(
        self,
    ) -> Callable[[vmwareengine.UpdateClusterRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateCluster(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_dns_forwarding(
        self,
    ) -> Callable[[vmwareengine.UpdateDnsForwardingRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateDnsForwarding(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_external_access_rule(
        self,
    ) -> Callable[
        [vmwareengine.UpdateExternalAccessRuleRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateExternalAccessRule(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_external_address(
        self,
    ) -> Callable[
        [vmwareengine.UpdateExternalAddressRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateExternalAddress(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_logging_server(
        self,
    ) -> Callable[[vmwareengine.UpdateLoggingServerRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateLoggingServer(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_management_dns_zone_binding(
        self,
    ) -> Callable[
        [vmwareengine.UpdateManagementDnsZoneBindingRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateManagementDnsZoneBinding(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_network_peering(
        self,
    ) -> Callable[[vmwareengine.UpdateNetworkPeeringRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateNetworkPeering(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_network_policy(
        self,
    ) -> Callable[[vmwareengine.UpdateNetworkPolicyRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateNetworkPolicy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_private_cloud(
        self,
    ) -> Callable[[vmwareengine.UpdatePrivateCloudRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdatePrivateCloud(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_private_connection(
        self,
    ) -> Callable[
        [vmwareengine.UpdatePrivateConnectionRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdatePrivateConnection(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_subnet(
        self,
    ) -> Callable[[vmwareengine.UpdateSubnetRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateSubnet(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_vmware_engine_network(
        self,
    ) -> Callable[
        [vmwareengine.UpdateVmwareEngineNetworkRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateVmwareEngineNetwork(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(
        _BaseVmwareEngineRestTransport._BaseGetLocation, VmwareEngineRestStub
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.GetLocation")

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
                _BaseVmwareEngineRestTransport._BaseGetLocation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseGetLocation,
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._GetLocation._get_response(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
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
        _BaseVmwareEngineRestTransport._BaseListLocations, VmwareEngineRestStub
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.ListLocations")

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
                _BaseVmwareEngineRestTransport._BaseListLocations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseListLocations,
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._ListLocations._get_response(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
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
        _BaseVmwareEngineRestTransport._BaseGetIamPolicy, VmwareEngineRestStub
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.GetIamPolicy")

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
                _BaseVmwareEngineRestTransport._BaseGetIamPolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseGetIamPolicy,
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.GetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "GetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._GetIamPolicy._get_response(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineAsyncClient.GetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
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
        _BaseVmwareEngineRestTransport._BaseSetIamPolicy, VmwareEngineRestStub
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.SetIamPolicy")

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
                _BaseVmwareEngineRestTransport._BaseSetIamPolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_set_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseSetIamPolicy,
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.SetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "SetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._SetIamPolicy._get_response(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineAsyncClient.SetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
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
        _BaseVmwareEngineRestTransport._BaseTestIamPermissions, VmwareEngineRestStub
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.TestIamPermissions")

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

            http_options = _BaseVmwareEngineRestTransport._BaseTestIamPermissions._get_http_options()
            request, metadata = self._interceptor.pre_test_iam_permissions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseTestIamPermissions,
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.TestIamPermissions",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "TestIamPermissions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._TestIamPermissions._get_response(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineAsyncClient.TestIamPermissions",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "TestIamPermissions",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def delete_operation(self):
        return self._DeleteOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _DeleteOperation(
        _BaseVmwareEngineRestTransport._BaseDeleteOperation, VmwareEngineRestStub
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.DeleteOperation")

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

            http_options = (
                _BaseVmwareEngineRestTransport._BaseDeleteOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseDeleteOperation,
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.DeleteOperation",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "DeleteOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._DeleteOperation._get_response(
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
        _BaseVmwareEngineRestTransport._BaseGetOperation, VmwareEngineRestStub
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.GetOperation")

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
                _BaseVmwareEngineRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
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
        _BaseVmwareEngineRestTransport._BaseListOperations, VmwareEngineRestStub
    ):
        def __hash__(self):
            return hash("VmwareEngineRestTransport.ListOperations")

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

            http_options = (
                _BaseVmwareEngineRestTransport._BaseListOperations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmwareEngineRestTransport._BaseListOperations,
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
                    f"Sending request for google.cloud.vmwareengine_v1.VmwareEngineClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmwareEngineRestTransport._ListOperations._get_response(
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
                    "Received response for google.cloud.vmwareengine_v1.VmwareEngineAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
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


__all__ = ("VmwareEngineRestTransport",)
