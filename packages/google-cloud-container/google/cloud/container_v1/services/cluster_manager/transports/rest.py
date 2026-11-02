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
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.container_v1._compat import transcode_request
from google.cloud.container_v1.types import cluster_service

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseClusterManagerRestTransport

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


class ClusterManagerRestInterceptor:
    """Interceptor for ClusterManager.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the ClusterManagerRestTransport.

    .. code-block:: python
        class MyCustomClusterManagerInterceptor(ClusterManagerRestInterceptor):
            def pre_cancel_operation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_check_autopilot_compatibility(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_check_autopilot_compatibility(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_complete_control_plane_upgrade(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_complete_control_plane_upgrade(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_complete_ip_rotation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_complete_ip_rotation(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_complete_node_pool_upgrade(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_create_cluster(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_cluster(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_node_pool(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_node_pool(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_cluster(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_cluster(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_node_pool(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_node_pool(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_fetch_cluster_upgrade_info(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_fetch_cluster_upgrade_info(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_fetch_node_pool_upgrade_info(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_fetch_node_pool_upgrade_info(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_cluster(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_cluster(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_json_web_keys(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_json_web_keys(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_node_pool(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_node_pool(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_operation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_operation(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_server_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_server_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_clusters(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_clusters(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_node_pools(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_node_pools(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_operations(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_operations(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_usable_subnetworks(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_usable_subnetworks(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_rollback_node_pool_upgrade(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_rollback_node_pool_upgrade(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_set_addons_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_set_addons_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_set_labels(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_set_labels(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_set_legacy_abac(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_set_legacy_abac(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_set_locations(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_set_locations(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_set_logging_service(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_set_logging_service(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_set_maintenance_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_set_maintenance_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_set_master_auth(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_set_master_auth(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_set_monitoring_service(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_set_monitoring_service(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_set_network_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_set_network_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_set_node_pool_autoscaling(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_set_node_pool_autoscaling(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_set_node_pool_management(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_set_node_pool_management(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_set_node_pool_size(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_set_node_pool_size(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_start_ip_rotation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_start_ip_rotation(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_cluster(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_cluster(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_master(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_master(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_node_pool(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_node_pool(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = ClusterManagerRestTransport(interceptor=MyCustomClusterManagerInterceptor())
        client = ClusterManagerClient(transport=transport)


    """

    def pre_cancel_operation(
        self,
        request: cluster_service.CancelOperationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cluster_service.CancelOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ClusterManager server.
        """
        return request, metadata

    def pre_check_autopilot_compatibility(
        self,
        request: cluster_service.CheckAutopilotCompatibilityRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cluster_service.CheckAutopilotCompatibilityRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for check_autopilot_compatibility

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ClusterManager server.
        """
        return request, metadata

    def post_check_autopilot_compatibility(
        self, response: cluster_service.CheckAutopilotCompatibilityResponse
    ) -> cluster_service.CheckAutopilotCompatibilityResponse:
        """Post-rpc interceptor for check_autopilot_compatibility

        DEPRECATED. Please use the `post_check_autopilot_compatibility_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ClusterManager server but before
        it is returned to user code. This `post_check_autopilot_compatibility` interceptor runs
        before the `post_check_autopilot_compatibility_with_metadata` interceptor.
        """
        return response

    def post_check_autopilot_compatibility_with_metadata(
        self,
        response: cluster_service.CheckAutopilotCompatibilityResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cluster_service.CheckAutopilotCompatibilityResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for check_autopilot_compatibility

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ClusterManager server but before it is returned to user code.

        We recommend only using this `post_check_autopilot_compatibility_with_metadata`
        interceptor in new development instead of the `post_check_autopilot_compatibility` interceptor.
        When both interceptors are used, this `post_check_autopilot_compatibility_with_metadata` interceptor runs after the
        `post_check_autopilot_compatibility` interceptor. The (possibly modified) response returned by
        `post_check_autopilot_compatibility` will be passed to
        `post_check_autopilot_compatibility_with_metadata`.
        """
        return response, metadata

    def pre_complete_control_plane_upgrade(
        self,
        request: cluster_service.CompleteControlPlaneUpgradeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cluster_service.CompleteControlPlaneUpgradeRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for complete_control_plane_upgrade

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ClusterManager server.
        """
        return request, metadata

    def post_complete_control_plane_upgrade(
        self, response: cluster_service.Operation
    ) -> cluster_service.Operation:
        """Post-rpc interceptor for complete_control_plane_upgrade

        DEPRECATED. Please use the `post_complete_control_plane_upgrade_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ClusterManager server but before
        it is returned to user code. This `post_complete_control_plane_upgrade` interceptor runs
        before the `post_complete_control_plane_upgrade_with_metadata` interceptor.
        """
        return response

    def post_complete_control_plane_upgrade_with_metadata(
        self,
        response: cluster_service.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cluster_service.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for complete_control_plane_upgrade

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ClusterManager server but before it is returned to user code.

        We recommend only using this `post_complete_control_plane_upgrade_with_metadata`
        interceptor in new development instead of the `post_complete_control_plane_upgrade` interceptor.
        When both interceptors are used, this `post_complete_control_plane_upgrade_with_metadata` interceptor runs after the
        `post_complete_control_plane_upgrade` interceptor. The (possibly modified) response returned by
        `post_complete_control_plane_upgrade` will be passed to
        `post_complete_control_plane_upgrade_with_metadata`.
        """
        return response, metadata

    def pre_complete_ip_rotation(
        self,
        request: cluster_service.CompleteIPRotationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cluster_service.CompleteIPRotationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for complete_ip_rotation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ClusterManager server.
        """
        return request, metadata

    def post_complete_ip_rotation(
        self, response: cluster_service.Operation
    ) -> cluster_service.Operation:
        """Post-rpc interceptor for complete_ip_rotation

        DEPRECATED. Please use the `post_complete_ip_rotation_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ClusterManager server but before
        it is returned to user code. This `post_complete_ip_rotation` interceptor runs
        before the `post_complete_ip_rotation_with_metadata` interceptor.
        """
        return response

    def post_complete_ip_rotation_with_metadata(
        self,
        response: cluster_service.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cluster_service.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for complete_ip_rotation

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ClusterManager server but before it is returned to user code.

        We recommend only using this `post_complete_ip_rotation_with_metadata`
        interceptor in new development instead of the `post_complete_ip_rotation` interceptor.
        When both interceptors are used, this `post_complete_ip_rotation_with_metadata` interceptor runs after the
        `post_complete_ip_rotation` interceptor. The (possibly modified) response returned by
        `post_complete_ip_rotation` will be passed to
        `post_complete_ip_rotation_with_metadata`.
        """
        return response, metadata

    def pre_complete_node_pool_upgrade(
        self,
        request: cluster_service.CompleteNodePoolUpgradeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cluster_service.CompleteNodePoolUpgradeRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for complete_node_pool_upgrade

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ClusterManager server.
        """
        return request, metadata

    def pre_create_cluster(
        self,
        request: cluster_service.CreateClusterRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cluster_service.CreateClusterRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_cluster

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ClusterManager server.
        """
        return request, metadata

    def post_create_cluster(
        self, response: cluster_service.Operation
    ) -> cluster_service.Operation:
        """Post-rpc interceptor for create_cluster

        DEPRECATED. Please use the `post_create_cluster_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ClusterManager server but before
        it is returned to user code. This `post_create_cluster` interceptor runs
        before the `post_create_cluster_with_metadata` interceptor.
        """
        return response

    def post_create_cluster_with_metadata(
        self,
        response: cluster_service.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cluster_service.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_cluster

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ClusterManager server but before it is returned to user code.

        We recommend only using this `post_create_cluster_with_metadata`
        interceptor in new development instead of the `post_create_cluster` interceptor.
        When both interceptors are used, this `post_create_cluster_with_metadata` interceptor runs after the
        `post_create_cluster` interceptor. The (possibly modified) response returned by
        `post_create_cluster` will be passed to
        `post_create_cluster_with_metadata`.
        """
        return response, metadata

    def pre_create_node_pool(
        self,
        request: cluster_service.CreateNodePoolRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cluster_service.CreateNodePoolRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_node_pool

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ClusterManager server.
        """
        return request, metadata

    def post_create_node_pool(
        self, response: cluster_service.Operation
    ) -> cluster_service.Operation:
        """Post-rpc interceptor for create_node_pool

        DEPRECATED. Please use the `post_create_node_pool_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ClusterManager server but before
        it is returned to user code. This `post_create_node_pool` interceptor runs
        before the `post_create_node_pool_with_metadata` interceptor.
        """
        return response

    def post_create_node_pool_with_metadata(
        self,
        response: cluster_service.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cluster_service.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_node_pool

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ClusterManager server but before it is returned to user code.

        We recommend only using this `post_create_node_pool_with_metadata`
        interceptor in new development instead of the `post_create_node_pool` interceptor.
        When both interceptors are used, this `post_create_node_pool_with_metadata` interceptor runs after the
        `post_create_node_pool` interceptor. The (possibly modified) response returned by
        `post_create_node_pool` will be passed to
        `post_create_node_pool_with_metadata`.
        """
        return response, metadata

    def pre_delete_cluster(
        self,
        request: cluster_service.DeleteClusterRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cluster_service.DeleteClusterRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_cluster

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ClusterManager server.
        """
        return request, metadata

    def post_delete_cluster(
        self, response: cluster_service.Operation
    ) -> cluster_service.Operation:
        """Post-rpc interceptor for delete_cluster

        DEPRECATED. Please use the `post_delete_cluster_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ClusterManager server but before
        it is returned to user code. This `post_delete_cluster` interceptor runs
        before the `post_delete_cluster_with_metadata` interceptor.
        """
        return response

    def post_delete_cluster_with_metadata(
        self,
        response: cluster_service.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cluster_service.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_cluster

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ClusterManager server but before it is returned to user code.

        We recommend only using this `post_delete_cluster_with_metadata`
        interceptor in new development instead of the `post_delete_cluster` interceptor.
        When both interceptors are used, this `post_delete_cluster_with_metadata` interceptor runs after the
        `post_delete_cluster` interceptor. The (possibly modified) response returned by
        `post_delete_cluster` will be passed to
        `post_delete_cluster_with_metadata`.
        """
        return response, metadata

    def pre_delete_node_pool(
        self,
        request: cluster_service.DeleteNodePoolRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cluster_service.DeleteNodePoolRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_node_pool

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ClusterManager server.
        """
        return request, metadata

    def post_delete_node_pool(
        self, response: cluster_service.Operation
    ) -> cluster_service.Operation:
        """Post-rpc interceptor for delete_node_pool

        DEPRECATED. Please use the `post_delete_node_pool_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ClusterManager server but before
        it is returned to user code. This `post_delete_node_pool` interceptor runs
        before the `post_delete_node_pool_with_metadata` interceptor.
        """
        return response

    def post_delete_node_pool_with_metadata(
        self,
        response: cluster_service.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cluster_service.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_node_pool

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ClusterManager server but before it is returned to user code.

        We recommend only using this `post_delete_node_pool_with_metadata`
        interceptor in new development instead of the `post_delete_node_pool` interceptor.
        When both interceptors are used, this `post_delete_node_pool_with_metadata` interceptor runs after the
        `post_delete_node_pool` interceptor. The (possibly modified) response returned by
        `post_delete_node_pool` will be passed to
        `post_delete_node_pool_with_metadata`.
        """
        return response, metadata

    def pre_fetch_cluster_upgrade_info(
        self,
        request: cluster_service.FetchClusterUpgradeInfoRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cluster_service.FetchClusterUpgradeInfoRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for fetch_cluster_upgrade_info

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ClusterManager server.
        """
        return request, metadata

    def post_fetch_cluster_upgrade_info(
        self, response: cluster_service.ClusterUpgradeInfo
    ) -> cluster_service.ClusterUpgradeInfo:
        """Post-rpc interceptor for fetch_cluster_upgrade_info

        DEPRECATED. Please use the `post_fetch_cluster_upgrade_info_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ClusterManager server but before
        it is returned to user code. This `post_fetch_cluster_upgrade_info` interceptor runs
        before the `post_fetch_cluster_upgrade_info_with_metadata` interceptor.
        """
        return response

    def post_fetch_cluster_upgrade_info_with_metadata(
        self,
        response: cluster_service.ClusterUpgradeInfo,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cluster_service.ClusterUpgradeInfo, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for fetch_cluster_upgrade_info

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ClusterManager server but before it is returned to user code.

        We recommend only using this `post_fetch_cluster_upgrade_info_with_metadata`
        interceptor in new development instead of the `post_fetch_cluster_upgrade_info` interceptor.
        When both interceptors are used, this `post_fetch_cluster_upgrade_info_with_metadata` interceptor runs after the
        `post_fetch_cluster_upgrade_info` interceptor. The (possibly modified) response returned by
        `post_fetch_cluster_upgrade_info` will be passed to
        `post_fetch_cluster_upgrade_info_with_metadata`.
        """
        return response, metadata

    def pre_fetch_node_pool_upgrade_info(
        self,
        request: cluster_service.FetchNodePoolUpgradeInfoRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cluster_service.FetchNodePoolUpgradeInfoRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for fetch_node_pool_upgrade_info

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ClusterManager server.
        """
        return request, metadata

    def post_fetch_node_pool_upgrade_info(
        self, response: cluster_service.NodePoolUpgradeInfo
    ) -> cluster_service.NodePoolUpgradeInfo:
        """Post-rpc interceptor for fetch_node_pool_upgrade_info

        DEPRECATED. Please use the `post_fetch_node_pool_upgrade_info_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ClusterManager server but before
        it is returned to user code. This `post_fetch_node_pool_upgrade_info` interceptor runs
        before the `post_fetch_node_pool_upgrade_info_with_metadata` interceptor.
        """
        return response

    def post_fetch_node_pool_upgrade_info_with_metadata(
        self,
        response: cluster_service.NodePoolUpgradeInfo,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cluster_service.NodePoolUpgradeInfo, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for fetch_node_pool_upgrade_info

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ClusterManager server but before it is returned to user code.

        We recommend only using this `post_fetch_node_pool_upgrade_info_with_metadata`
        interceptor in new development instead of the `post_fetch_node_pool_upgrade_info` interceptor.
        When both interceptors are used, this `post_fetch_node_pool_upgrade_info_with_metadata` interceptor runs after the
        `post_fetch_node_pool_upgrade_info` interceptor. The (possibly modified) response returned by
        `post_fetch_node_pool_upgrade_info` will be passed to
        `post_fetch_node_pool_upgrade_info_with_metadata`.
        """
        return response, metadata

    def pre_get_cluster(
        self,
        request: cluster_service.GetClusterRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cluster_service.GetClusterRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_cluster

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ClusterManager server.
        """
        return request, metadata

    def post_get_cluster(
        self, response: cluster_service.Cluster
    ) -> cluster_service.Cluster:
        """Post-rpc interceptor for get_cluster

        DEPRECATED. Please use the `post_get_cluster_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ClusterManager server but before
        it is returned to user code. This `post_get_cluster` interceptor runs
        before the `post_get_cluster_with_metadata` interceptor.
        """
        return response

    def post_get_cluster_with_metadata(
        self,
        response: cluster_service.Cluster,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cluster_service.Cluster, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_cluster

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ClusterManager server but before it is returned to user code.

        We recommend only using this `post_get_cluster_with_metadata`
        interceptor in new development instead of the `post_get_cluster` interceptor.
        When both interceptors are used, this `post_get_cluster_with_metadata` interceptor runs after the
        `post_get_cluster` interceptor. The (possibly modified) response returned by
        `post_get_cluster` will be passed to
        `post_get_cluster_with_metadata`.
        """
        return response, metadata

    def pre_get_json_web_keys(
        self,
        request: cluster_service.GetJSONWebKeysRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cluster_service.GetJSONWebKeysRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_json_web_keys

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ClusterManager server.
        """
        return request, metadata

    def post_get_json_web_keys(
        self, response: cluster_service.GetJSONWebKeysResponse
    ) -> cluster_service.GetJSONWebKeysResponse:
        """Post-rpc interceptor for get_json_web_keys

        DEPRECATED. Please use the `post_get_json_web_keys_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ClusterManager server but before
        it is returned to user code. This `post_get_json_web_keys` interceptor runs
        before the `post_get_json_web_keys_with_metadata` interceptor.
        """
        return response

    def post_get_json_web_keys_with_metadata(
        self,
        response: cluster_service.GetJSONWebKeysResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cluster_service.GetJSONWebKeysResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_json_web_keys

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ClusterManager server but before it is returned to user code.

        We recommend only using this `post_get_json_web_keys_with_metadata`
        interceptor in new development instead of the `post_get_json_web_keys` interceptor.
        When both interceptors are used, this `post_get_json_web_keys_with_metadata` interceptor runs after the
        `post_get_json_web_keys` interceptor. The (possibly modified) response returned by
        `post_get_json_web_keys` will be passed to
        `post_get_json_web_keys_with_metadata`.
        """
        return response, metadata

    def pre_get_node_pool(
        self,
        request: cluster_service.GetNodePoolRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cluster_service.GetNodePoolRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_node_pool

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ClusterManager server.
        """
        return request, metadata

    def post_get_node_pool(
        self, response: cluster_service.NodePool
    ) -> cluster_service.NodePool:
        """Post-rpc interceptor for get_node_pool

        DEPRECATED. Please use the `post_get_node_pool_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ClusterManager server but before
        it is returned to user code. This `post_get_node_pool` interceptor runs
        before the `post_get_node_pool_with_metadata` interceptor.
        """
        return response

    def post_get_node_pool_with_metadata(
        self,
        response: cluster_service.NodePool,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cluster_service.NodePool, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_node_pool

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ClusterManager server but before it is returned to user code.

        We recommend only using this `post_get_node_pool_with_metadata`
        interceptor in new development instead of the `post_get_node_pool` interceptor.
        When both interceptors are used, this `post_get_node_pool_with_metadata` interceptor runs after the
        `post_get_node_pool` interceptor. The (possibly modified) response returned by
        `post_get_node_pool` will be passed to
        `post_get_node_pool_with_metadata`.
        """
        return response, metadata

    def pre_get_operation(
        self,
        request: cluster_service.GetOperationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cluster_service.GetOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ClusterManager server.
        """
        return request, metadata

    def post_get_operation(
        self, response: cluster_service.Operation
    ) -> cluster_service.Operation:
        """Post-rpc interceptor for get_operation

        DEPRECATED. Please use the `post_get_operation_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ClusterManager server but before
        it is returned to user code. This `post_get_operation` interceptor runs
        before the `post_get_operation_with_metadata` interceptor.
        """
        return response

    def post_get_operation_with_metadata(
        self,
        response: cluster_service.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cluster_service.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_operation

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ClusterManager server but before it is returned to user code.

        We recommend only using this `post_get_operation_with_metadata`
        interceptor in new development instead of the `post_get_operation` interceptor.
        When both interceptors are used, this `post_get_operation_with_metadata` interceptor runs after the
        `post_get_operation` interceptor. The (possibly modified) response returned by
        `post_get_operation` will be passed to
        `post_get_operation_with_metadata`.
        """
        return response, metadata

    def pre_get_server_config(
        self,
        request: cluster_service.GetServerConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cluster_service.GetServerConfigRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_server_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ClusterManager server.
        """
        return request, metadata

    def post_get_server_config(
        self, response: cluster_service.ServerConfig
    ) -> cluster_service.ServerConfig:
        """Post-rpc interceptor for get_server_config

        DEPRECATED. Please use the `post_get_server_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ClusterManager server but before
        it is returned to user code. This `post_get_server_config` interceptor runs
        before the `post_get_server_config_with_metadata` interceptor.
        """
        return response

    def post_get_server_config_with_metadata(
        self,
        response: cluster_service.ServerConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cluster_service.ServerConfig, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_server_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ClusterManager server but before it is returned to user code.

        We recommend only using this `post_get_server_config_with_metadata`
        interceptor in new development instead of the `post_get_server_config` interceptor.
        When both interceptors are used, this `post_get_server_config_with_metadata` interceptor runs after the
        `post_get_server_config` interceptor. The (possibly modified) response returned by
        `post_get_server_config` will be passed to
        `post_get_server_config_with_metadata`.
        """
        return response, metadata

    def pre_list_clusters(
        self,
        request: cluster_service.ListClustersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cluster_service.ListClustersRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_clusters

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ClusterManager server.
        """
        return request, metadata

    def post_list_clusters(
        self, response: cluster_service.ListClustersResponse
    ) -> cluster_service.ListClustersResponse:
        """Post-rpc interceptor for list_clusters

        DEPRECATED. Please use the `post_list_clusters_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ClusterManager server but before
        it is returned to user code. This `post_list_clusters` interceptor runs
        before the `post_list_clusters_with_metadata` interceptor.
        """
        return response

    def post_list_clusters_with_metadata(
        self,
        response: cluster_service.ListClustersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cluster_service.ListClustersResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_clusters

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ClusterManager server but before it is returned to user code.

        We recommend only using this `post_list_clusters_with_metadata`
        interceptor in new development instead of the `post_list_clusters` interceptor.
        When both interceptors are used, this `post_list_clusters_with_metadata` interceptor runs after the
        `post_list_clusters` interceptor. The (possibly modified) response returned by
        `post_list_clusters` will be passed to
        `post_list_clusters_with_metadata`.
        """
        return response, metadata

    def pre_list_node_pools(
        self,
        request: cluster_service.ListNodePoolsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cluster_service.ListNodePoolsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_node_pools

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ClusterManager server.
        """
        return request, metadata

    def post_list_node_pools(
        self, response: cluster_service.ListNodePoolsResponse
    ) -> cluster_service.ListNodePoolsResponse:
        """Post-rpc interceptor for list_node_pools

        DEPRECATED. Please use the `post_list_node_pools_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ClusterManager server but before
        it is returned to user code. This `post_list_node_pools` interceptor runs
        before the `post_list_node_pools_with_metadata` interceptor.
        """
        return response

    def post_list_node_pools_with_metadata(
        self,
        response: cluster_service.ListNodePoolsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cluster_service.ListNodePoolsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_node_pools

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ClusterManager server but before it is returned to user code.

        We recommend only using this `post_list_node_pools_with_metadata`
        interceptor in new development instead of the `post_list_node_pools` interceptor.
        When both interceptors are used, this `post_list_node_pools_with_metadata` interceptor runs after the
        `post_list_node_pools` interceptor. The (possibly modified) response returned by
        `post_list_node_pools` will be passed to
        `post_list_node_pools_with_metadata`.
        """
        return response, metadata

    def pre_list_operations(
        self,
        request: cluster_service.ListOperationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cluster_service.ListOperationsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_operations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ClusterManager server.
        """
        return request, metadata

    def post_list_operations(
        self, response: cluster_service.ListOperationsResponse
    ) -> cluster_service.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        DEPRECATED. Please use the `post_list_operations_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ClusterManager server but before
        it is returned to user code. This `post_list_operations` interceptor runs
        before the `post_list_operations_with_metadata` interceptor.
        """
        return response

    def post_list_operations_with_metadata(
        self,
        response: cluster_service.ListOperationsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cluster_service.ListOperationsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_operations

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ClusterManager server but before it is returned to user code.

        We recommend only using this `post_list_operations_with_metadata`
        interceptor in new development instead of the `post_list_operations` interceptor.
        When both interceptors are used, this `post_list_operations_with_metadata` interceptor runs after the
        `post_list_operations` interceptor. The (possibly modified) response returned by
        `post_list_operations` will be passed to
        `post_list_operations_with_metadata`.
        """
        return response, metadata

    def pre_list_usable_subnetworks(
        self,
        request: cluster_service.ListUsableSubnetworksRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cluster_service.ListUsableSubnetworksRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_usable_subnetworks

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ClusterManager server.
        """
        return request, metadata

    def post_list_usable_subnetworks(
        self, response: cluster_service.ListUsableSubnetworksResponse
    ) -> cluster_service.ListUsableSubnetworksResponse:
        """Post-rpc interceptor for list_usable_subnetworks

        DEPRECATED. Please use the `post_list_usable_subnetworks_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ClusterManager server but before
        it is returned to user code. This `post_list_usable_subnetworks` interceptor runs
        before the `post_list_usable_subnetworks_with_metadata` interceptor.
        """
        return response

    def post_list_usable_subnetworks_with_metadata(
        self,
        response: cluster_service.ListUsableSubnetworksResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cluster_service.ListUsableSubnetworksResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_usable_subnetworks

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ClusterManager server but before it is returned to user code.

        We recommend only using this `post_list_usable_subnetworks_with_metadata`
        interceptor in new development instead of the `post_list_usable_subnetworks` interceptor.
        When both interceptors are used, this `post_list_usable_subnetworks_with_metadata` interceptor runs after the
        `post_list_usable_subnetworks` interceptor. The (possibly modified) response returned by
        `post_list_usable_subnetworks` will be passed to
        `post_list_usable_subnetworks_with_metadata`.
        """
        return response, metadata

    def pre_rollback_node_pool_upgrade(
        self,
        request: cluster_service.RollbackNodePoolUpgradeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cluster_service.RollbackNodePoolUpgradeRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for rollback_node_pool_upgrade

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ClusterManager server.
        """
        return request, metadata

    def post_rollback_node_pool_upgrade(
        self, response: cluster_service.Operation
    ) -> cluster_service.Operation:
        """Post-rpc interceptor for rollback_node_pool_upgrade

        DEPRECATED. Please use the `post_rollback_node_pool_upgrade_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ClusterManager server but before
        it is returned to user code. This `post_rollback_node_pool_upgrade` interceptor runs
        before the `post_rollback_node_pool_upgrade_with_metadata` interceptor.
        """
        return response

    def post_rollback_node_pool_upgrade_with_metadata(
        self,
        response: cluster_service.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cluster_service.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for rollback_node_pool_upgrade

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ClusterManager server but before it is returned to user code.

        We recommend only using this `post_rollback_node_pool_upgrade_with_metadata`
        interceptor in new development instead of the `post_rollback_node_pool_upgrade` interceptor.
        When both interceptors are used, this `post_rollback_node_pool_upgrade_with_metadata` interceptor runs after the
        `post_rollback_node_pool_upgrade` interceptor. The (possibly modified) response returned by
        `post_rollback_node_pool_upgrade` will be passed to
        `post_rollback_node_pool_upgrade_with_metadata`.
        """
        return response, metadata

    def pre_set_addons_config(
        self,
        request: cluster_service.SetAddonsConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cluster_service.SetAddonsConfigRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for set_addons_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ClusterManager server.
        """
        return request, metadata

    def post_set_addons_config(
        self, response: cluster_service.Operation
    ) -> cluster_service.Operation:
        """Post-rpc interceptor for set_addons_config

        DEPRECATED. Please use the `post_set_addons_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ClusterManager server but before
        it is returned to user code. This `post_set_addons_config` interceptor runs
        before the `post_set_addons_config_with_metadata` interceptor.
        """
        return response

    def post_set_addons_config_with_metadata(
        self,
        response: cluster_service.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cluster_service.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for set_addons_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ClusterManager server but before it is returned to user code.

        We recommend only using this `post_set_addons_config_with_metadata`
        interceptor in new development instead of the `post_set_addons_config` interceptor.
        When both interceptors are used, this `post_set_addons_config_with_metadata` interceptor runs after the
        `post_set_addons_config` interceptor. The (possibly modified) response returned by
        `post_set_addons_config` will be passed to
        `post_set_addons_config_with_metadata`.
        """
        return response, metadata

    def pre_set_labels(
        self,
        request: cluster_service.SetLabelsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cluster_service.SetLabelsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for set_labels

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ClusterManager server.
        """
        return request, metadata

    def post_set_labels(
        self, response: cluster_service.Operation
    ) -> cluster_service.Operation:
        """Post-rpc interceptor for set_labels

        DEPRECATED. Please use the `post_set_labels_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ClusterManager server but before
        it is returned to user code. This `post_set_labels` interceptor runs
        before the `post_set_labels_with_metadata` interceptor.
        """
        return response

    def post_set_labels_with_metadata(
        self,
        response: cluster_service.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cluster_service.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for set_labels

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ClusterManager server but before it is returned to user code.

        We recommend only using this `post_set_labels_with_metadata`
        interceptor in new development instead of the `post_set_labels` interceptor.
        When both interceptors are used, this `post_set_labels_with_metadata` interceptor runs after the
        `post_set_labels` interceptor. The (possibly modified) response returned by
        `post_set_labels` will be passed to
        `post_set_labels_with_metadata`.
        """
        return response, metadata

    def pre_set_legacy_abac(
        self,
        request: cluster_service.SetLegacyAbacRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cluster_service.SetLegacyAbacRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for set_legacy_abac

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ClusterManager server.
        """
        return request, metadata

    def post_set_legacy_abac(
        self, response: cluster_service.Operation
    ) -> cluster_service.Operation:
        """Post-rpc interceptor for set_legacy_abac

        DEPRECATED. Please use the `post_set_legacy_abac_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ClusterManager server but before
        it is returned to user code. This `post_set_legacy_abac` interceptor runs
        before the `post_set_legacy_abac_with_metadata` interceptor.
        """
        return response

    def post_set_legacy_abac_with_metadata(
        self,
        response: cluster_service.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cluster_service.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for set_legacy_abac

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ClusterManager server but before it is returned to user code.

        We recommend only using this `post_set_legacy_abac_with_metadata`
        interceptor in new development instead of the `post_set_legacy_abac` interceptor.
        When both interceptors are used, this `post_set_legacy_abac_with_metadata` interceptor runs after the
        `post_set_legacy_abac` interceptor. The (possibly modified) response returned by
        `post_set_legacy_abac` will be passed to
        `post_set_legacy_abac_with_metadata`.
        """
        return response, metadata

    def pre_set_locations(
        self,
        request: cluster_service.SetLocationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cluster_service.SetLocationsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for set_locations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ClusterManager server.
        """
        return request, metadata

    def post_set_locations(
        self, response: cluster_service.Operation
    ) -> cluster_service.Operation:
        """Post-rpc interceptor for set_locations

        DEPRECATED. Please use the `post_set_locations_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ClusterManager server but before
        it is returned to user code. This `post_set_locations` interceptor runs
        before the `post_set_locations_with_metadata` interceptor.
        """
        return response

    def post_set_locations_with_metadata(
        self,
        response: cluster_service.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cluster_service.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for set_locations

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ClusterManager server but before it is returned to user code.

        We recommend only using this `post_set_locations_with_metadata`
        interceptor in new development instead of the `post_set_locations` interceptor.
        When both interceptors are used, this `post_set_locations_with_metadata` interceptor runs after the
        `post_set_locations` interceptor. The (possibly modified) response returned by
        `post_set_locations` will be passed to
        `post_set_locations_with_metadata`.
        """
        return response, metadata

    def pre_set_logging_service(
        self,
        request: cluster_service.SetLoggingServiceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cluster_service.SetLoggingServiceRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for set_logging_service

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ClusterManager server.
        """
        return request, metadata

    def post_set_logging_service(
        self, response: cluster_service.Operation
    ) -> cluster_service.Operation:
        """Post-rpc interceptor for set_logging_service

        DEPRECATED. Please use the `post_set_logging_service_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ClusterManager server but before
        it is returned to user code. This `post_set_logging_service` interceptor runs
        before the `post_set_logging_service_with_metadata` interceptor.
        """
        return response

    def post_set_logging_service_with_metadata(
        self,
        response: cluster_service.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cluster_service.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for set_logging_service

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ClusterManager server but before it is returned to user code.

        We recommend only using this `post_set_logging_service_with_metadata`
        interceptor in new development instead of the `post_set_logging_service` interceptor.
        When both interceptors are used, this `post_set_logging_service_with_metadata` interceptor runs after the
        `post_set_logging_service` interceptor. The (possibly modified) response returned by
        `post_set_logging_service` will be passed to
        `post_set_logging_service_with_metadata`.
        """
        return response, metadata

    def pre_set_maintenance_policy(
        self,
        request: cluster_service.SetMaintenancePolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cluster_service.SetMaintenancePolicyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for set_maintenance_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ClusterManager server.
        """
        return request, metadata

    def post_set_maintenance_policy(
        self, response: cluster_service.Operation
    ) -> cluster_service.Operation:
        """Post-rpc interceptor for set_maintenance_policy

        DEPRECATED. Please use the `post_set_maintenance_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ClusterManager server but before
        it is returned to user code. This `post_set_maintenance_policy` interceptor runs
        before the `post_set_maintenance_policy_with_metadata` interceptor.
        """
        return response

    def post_set_maintenance_policy_with_metadata(
        self,
        response: cluster_service.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cluster_service.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for set_maintenance_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ClusterManager server but before it is returned to user code.

        We recommend only using this `post_set_maintenance_policy_with_metadata`
        interceptor in new development instead of the `post_set_maintenance_policy` interceptor.
        When both interceptors are used, this `post_set_maintenance_policy_with_metadata` interceptor runs after the
        `post_set_maintenance_policy` interceptor. The (possibly modified) response returned by
        `post_set_maintenance_policy` will be passed to
        `post_set_maintenance_policy_with_metadata`.
        """
        return response, metadata

    def pre_set_master_auth(
        self,
        request: cluster_service.SetMasterAuthRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cluster_service.SetMasterAuthRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for set_master_auth

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ClusterManager server.
        """
        return request, metadata

    def post_set_master_auth(
        self, response: cluster_service.Operation
    ) -> cluster_service.Operation:
        """Post-rpc interceptor for set_master_auth

        DEPRECATED. Please use the `post_set_master_auth_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ClusterManager server but before
        it is returned to user code. This `post_set_master_auth` interceptor runs
        before the `post_set_master_auth_with_metadata` interceptor.
        """
        return response

    def post_set_master_auth_with_metadata(
        self,
        response: cluster_service.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cluster_service.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for set_master_auth

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ClusterManager server but before it is returned to user code.

        We recommend only using this `post_set_master_auth_with_metadata`
        interceptor in new development instead of the `post_set_master_auth` interceptor.
        When both interceptors are used, this `post_set_master_auth_with_metadata` interceptor runs after the
        `post_set_master_auth` interceptor. The (possibly modified) response returned by
        `post_set_master_auth` will be passed to
        `post_set_master_auth_with_metadata`.
        """
        return response, metadata

    def pre_set_monitoring_service(
        self,
        request: cluster_service.SetMonitoringServiceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cluster_service.SetMonitoringServiceRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for set_monitoring_service

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ClusterManager server.
        """
        return request, metadata

    def post_set_monitoring_service(
        self, response: cluster_service.Operation
    ) -> cluster_service.Operation:
        """Post-rpc interceptor for set_monitoring_service

        DEPRECATED. Please use the `post_set_monitoring_service_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ClusterManager server but before
        it is returned to user code. This `post_set_monitoring_service` interceptor runs
        before the `post_set_monitoring_service_with_metadata` interceptor.
        """
        return response

    def post_set_monitoring_service_with_metadata(
        self,
        response: cluster_service.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cluster_service.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for set_monitoring_service

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ClusterManager server but before it is returned to user code.

        We recommend only using this `post_set_monitoring_service_with_metadata`
        interceptor in new development instead of the `post_set_monitoring_service` interceptor.
        When both interceptors are used, this `post_set_monitoring_service_with_metadata` interceptor runs after the
        `post_set_monitoring_service` interceptor. The (possibly modified) response returned by
        `post_set_monitoring_service` will be passed to
        `post_set_monitoring_service_with_metadata`.
        """
        return response, metadata

    def pre_set_network_policy(
        self,
        request: cluster_service.SetNetworkPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cluster_service.SetNetworkPolicyRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for set_network_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ClusterManager server.
        """
        return request, metadata

    def post_set_network_policy(
        self, response: cluster_service.Operation
    ) -> cluster_service.Operation:
        """Post-rpc interceptor for set_network_policy

        DEPRECATED. Please use the `post_set_network_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ClusterManager server but before
        it is returned to user code. This `post_set_network_policy` interceptor runs
        before the `post_set_network_policy_with_metadata` interceptor.
        """
        return response

    def post_set_network_policy_with_metadata(
        self,
        response: cluster_service.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cluster_service.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for set_network_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ClusterManager server but before it is returned to user code.

        We recommend only using this `post_set_network_policy_with_metadata`
        interceptor in new development instead of the `post_set_network_policy` interceptor.
        When both interceptors are used, this `post_set_network_policy_with_metadata` interceptor runs after the
        `post_set_network_policy` interceptor. The (possibly modified) response returned by
        `post_set_network_policy` will be passed to
        `post_set_network_policy_with_metadata`.
        """
        return response, metadata

    def pre_set_node_pool_autoscaling(
        self,
        request: cluster_service.SetNodePoolAutoscalingRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cluster_service.SetNodePoolAutoscalingRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for set_node_pool_autoscaling

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ClusterManager server.
        """
        return request, metadata

    def post_set_node_pool_autoscaling(
        self, response: cluster_service.Operation
    ) -> cluster_service.Operation:
        """Post-rpc interceptor for set_node_pool_autoscaling

        DEPRECATED. Please use the `post_set_node_pool_autoscaling_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ClusterManager server but before
        it is returned to user code. This `post_set_node_pool_autoscaling` interceptor runs
        before the `post_set_node_pool_autoscaling_with_metadata` interceptor.
        """
        return response

    def post_set_node_pool_autoscaling_with_metadata(
        self,
        response: cluster_service.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cluster_service.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for set_node_pool_autoscaling

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ClusterManager server but before it is returned to user code.

        We recommend only using this `post_set_node_pool_autoscaling_with_metadata`
        interceptor in new development instead of the `post_set_node_pool_autoscaling` interceptor.
        When both interceptors are used, this `post_set_node_pool_autoscaling_with_metadata` interceptor runs after the
        `post_set_node_pool_autoscaling` interceptor. The (possibly modified) response returned by
        `post_set_node_pool_autoscaling` will be passed to
        `post_set_node_pool_autoscaling_with_metadata`.
        """
        return response, metadata

    def pre_set_node_pool_management(
        self,
        request: cluster_service.SetNodePoolManagementRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cluster_service.SetNodePoolManagementRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for set_node_pool_management

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ClusterManager server.
        """
        return request, metadata

    def post_set_node_pool_management(
        self, response: cluster_service.Operation
    ) -> cluster_service.Operation:
        """Post-rpc interceptor for set_node_pool_management

        DEPRECATED. Please use the `post_set_node_pool_management_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ClusterManager server but before
        it is returned to user code. This `post_set_node_pool_management` interceptor runs
        before the `post_set_node_pool_management_with_metadata` interceptor.
        """
        return response

    def post_set_node_pool_management_with_metadata(
        self,
        response: cluster_service.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cluster_service.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for set_node_pool_management

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ClusterManager server but before it is returned to user code.

        We recommend only using this `post_set_node_pool_management_with_metadata`
        interceptor in new development instead of the `post_set_node_pool_management` interceptor.
        When both interceptors are used, this `post_set_node_pool_management_with_metadata` interceptor runs after the
        `post_set_node_pool_management` interceptor. The (possibly modified) response returned by
        `post_set_node_pool_management` will be passed to
        `post_set_node_pool_management_with_metadata`.
        """
        return response, metadata

    def pre_set_node_pool_size(
        self,
        request: cluster_service.SetNodePoolSizeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cluster_service.SetNodePoolSizeRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for set_node_pool_size

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ClusterManager server.
        """
        return request, metadata

    def post_set_node_pool_size(
        self, response: cluster_service.Operation
    ) -> cluster_service.Operation:
        """Post-rpc interceptor for set_node_pool_size

        DEPRECATED. Please use the `post_set_node_pool_size_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ClusterManager server but before
        it is returned to user code. This `post_set_node_pool_size` interceptor runs
        before the `post_set_node_pool_size_with_metadata` interceptor.
        """
        return response

    def post_set_node_pool_size_with_metadata(
        self,
        response: cluster_service.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cluster_service.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for set_node_pool_size

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ClusterManager server but before it is returned to user code.

        We recommend only using this `post_set_node_pool_size_with_metadata`
        interceptor in new development instead of the `post_set_node_pool_size` interceptor.
        When both interceptors are used, this `post_set_node_pool_size_with_metadata` interceptor runs after the
        `post_set_node_pool_size` interceptor. The (possibly modified) response returned by
        `post_set_node_pool_size` will be passed to
        `post_set_node_pool_size_with_metadata`.
        """
        return response, metadata

    def pre_start_ip_rotation(
        self,
        request: cluster_service.StartIPRotationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cluster_service.StartIPRotationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for start_ip_rotation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ClusterManager server.
        """
        return request, metadata

    def post_start_ip_rotation(
        self, response: cluster_service.Operation
    ) -> cluster_service.Operation:
        """Post-rpc interceptor for start_ip_rotation

        DEPRECATED. Please use the `post_start_ip_rotation_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ClusterManager server but before
        it is returned to user code. This `post_start_ip_rotation` interceptor runs
        before the `post_start_ip_rotation_with_metadata` interceptor.
        """
        return response

    def post_start_ip_rotation_with_metadata(
        self,
        response: cluster_service.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cluster_service.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for start_ip_rotation

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ClusterManager server but before it is returned to user code.

        We recommend only using this `post_start_ip_rotation_with_metadata`
        interceptor in new development instead of the `post_start_ip_rotation` interceptor.
        When both interceptors are used, this `post_start_ip_rotation_with_metadata` interceptor runs after the
        `post_start_ip_rotation` interceptor. The (possibly modified) response returned by
        `post_start_ip_rotation` will be passed to
        `post_start_ip_rotation_with_metadata`.
        """
        return response, metadata

    def pre_update_cluster(
        self,
        request: cluster_service.UpdateClusterRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cluster_service.UpdateClusterRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_cluster

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ClusterManager server.
        """
        return request, metadata

    def post_update_cluster(
        self, response: cluster_service.Operation
    ) -> cluster_service.Operation:
        """Post-rpc interceptor for update_cluster

        DEPRECATED. Please use the `post_update_cluster_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ClusterManager server but before
        it is returned to user code. This `post_update_cluster` interceptor runs
        before the `post_update_cluster_with_metadata` interceptor.
        """
        return response

    def post_update_cluster_with_metadata(
        self,
        response: cluster_service.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cluster_service.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_cluster

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ClusterManager server but before it is returned to user code.

        We recommend only using this `post_update_cluster_with_metadata`
        interceptor in new development instead of the `post_update_cluster` interceptor.
        When both interceptors are used, this `post_update_cluster_with_metadata` interceptor runs after the
        `post_update_cluster` interceptor. The (possibly modified) response returned by
        `post_update_cluster` will be passed to
        `post_update_cluster_with_metadata`.
        """
        return response, metadata

    def pre_update_master(
        self,
        request: cluster_service.UpdateMasterRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cluster_service.UpdateMasterRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_master

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ClusterManager server.
        """
        return request, metadata

    def post_update_master(
        self, response: cluster_service.Operation
    ) -> cluster_service.Operation:
        """Post-rpc interceptor for update_master

        DEPRECATED. Please use the `post_update_master_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ClusterManager server but before
        it is returned to user code. This `post_update_master` interceptor runs
        before the `post_update_master_with_metadata` interceptor.
        """
        return response

    def post_update_master_with_metadata(
        self,
        response: cluster_service.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cluster_service.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_master

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ClusterManager server but before it is returned to user code.

        We recommend only using this `post_update_master_with_metadata`
        interceptor in new development instead of the `post_update_master` interceptor.
        When both interceptors are used, this `post_update_master_with_metadata` interceptor runs after the
        `post_update_master` interceptor. The (possibly modified) response returned by
        `post_update_master` will be passed to
        `post_update_master_with_metadata`.
        """
        return response, metadata

    def pre_update_node_pool(
        self,
        request: cluster_service.UpdateNodePoolRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cluster_service.UpdateNodePoolRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_node_pool

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ClusterManager server.
        """
        return request, metadata

    def post_update_node_pool(
        self, response: cluster_service.Operation
    ) -> cluster_service.Operation:
        """Post-rpc interceptor for update_node_pool

        DEPRECATED. Please use the `post_update_node_pool_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ClusterManager server but before
        it is returned to user code. This `post_update_node_pool` interceptor runs
        before the `post_update_node_pool_with_metadata` interceptor.
        """
        return response

    def post_update_node_pool_with_metadata(
        self,
        response: cluster_service.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cluster_service.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_node_pool

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ClusterManager server but before it is returned to user code.

        We recommend only using this `post_update_node_pool_with_metadata`
        interceptor in new development instead of the `post_update_node_pool` interceptor.
        When both interceptors are used, this `post_update_node_pool_with_metadata` interceptor runs after the
        `post_update_node_pool` interceptor. The (possibly modified) response returned by
        `post_update_node_pool` will be passed to
        `post_update_node_pool_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class ClusterManagerRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: ClusterManagerRestInterceptor


class ClusterManagerRestTransport(_BaseClusterManagerRestTransport):
    """REST backend synchronous transport for ClusterManager.

    Google Kubernetes Engine Cluster Manager v1

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "container.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[ClusterManagerRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'container.googleapis.com').
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
            interceptor (Optional[ClusterManagerRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or ClusterManagerRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _CancelOperation(
        _BaseClusterManagerRestTransport._BaseCancelOperation, ClusterManagerRestStub
    ):
        def __hash__(self):
            return hash("ClusterManagerRestTransport.CancelOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: cluster_service.CancelOperationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the cancel operation method over HTTP.

            Args:
                request (~.cluster_service.CancelOperationRequest):
                    The request object. CancelOperationRequest cancels a
                single operation.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseClusterManagerRestTransport._BaseCancelOperation._get_http_options()
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseClusterManagerRestTransport._BaseCancelOperation,
                    "_BaseCancelOperation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.container_v1.ClusterManagerClient.CancelOperation",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ClusterManagerRestTransport._CancelOperation._get_response(
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

    class _CheckAutopilotCompatibility(
        _BaseClusterManagerRestTransport._BaseCheckAutopilotCompatibility,
        ClusterManagerRestStub,
    ):
        def __hash__(self):
            return hash("ClusterManagerRestTransport.CheckAutopilotCompatibility")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: cluster_service.CheckAutopilotCompatibilityRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cluster_service.CheckAutopilotCompatibilityResponse:
            r"""Call the check autopilot
            compatibility method over HTTP.

                Args:
                    request (~.cluster_service.CheckAutopilotCompatibilityRequest):
                        The request object. CheckAutopilotCompatibilityRequest
                    requests getting the blockers for the
                    given operation in the cluster.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.cluster_service.CheckAutopilotCompatibilityResponse:
                        CheckAutopilotCompatibilityResponse
                    has a list of compatibility issues.

            """

            http_options = _BaseClusterManagerRestTransport._BaseCheckAutopilotCompatibility._get_http_options()
            request, metadata = self._interceptor.pre_check_autopilot_compatibility(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseClusterManagerRestTransport._BaseCheckAutopilotCompatibility,
                    "_BaseCheckAutopilotCompatibility__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.container_v1.ClusterManagerClient.CheckAutopilotCompatibility",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "CheckAutopilotCompatibility",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ClusterManagerRestTransport._CheckAutopilotCompatibility._get_response(
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
            resp = cluster_service.CheckAutopilotCompatibilityResponse()
            pb_resp = cluster_service.CheckAutopilotCompatibilityResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_check_autopilot_compatibility(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_check_autopilot_compatibility_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        cluster_service.CheckAutopilotCompatibilityResponse.to_json(
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
                    "Received response for google.container_v1.ClusterManagerClient.check_autopilot_compatibility",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "CheckAutopilotCompatibility",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CompleteControlPlaneUpgrade(
        _BaseClusterManagerRestTransport._BaseCompleteControlPlaneUpgrade,
        ClusterManagerRestStub,
    ):
        def __hash__(self):
            return hash("ClusterManagerRestTransport.CompleteControlPlaneUpgrade")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: cluster_service.CompleteControlPlaneUpgradeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cluster_service.Operation:
            r"""Call the complete control plane
            upgrade method over HTTP.

                Args:
                    request (~.cluster_service.CompleteControlPlaneUpgradeRequest):
                        The request object. CompleteControlPlaneUpgradeRequest
                    sets the name of target cluster to
                    complete upgrade.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.cluster_service.Operation:
                        This operation resource represents
                    operations that may have happened or are
                    happening on the cluster. All fields are
                    output only.

            """

            http_options = _BaseClusterManagerRestTransport._BaseCompleteControlPlaneUpgrade._get_http_options()
            request, metadata = self._interceptor.pre_complete_control_plane_upgrade(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseClusterManagerRestTransport._BaseCompleteControlPlaneUpgrade,
                    "_BaseCompleteControlPlaneUpgrade__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.container_v1.ClusterManagerClient.CompleteControlPlaneUpgrade",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "CompleteControlPlaneUpgrade",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ClusterManagerRestTransport._CompleteControlPlaneUpgrade._get_response(
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
            resp = cluster_service.Operation()
            pb_resp = cluster_service.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_complete_control_plane_upgrade(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_complete_control_plane_upgrade_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cluster_service.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.container_v1.ClusterManagerClient.complete_control_plane_upgrade",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "CompleteControlPlaneUpgrade",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CompleteIPRotation(
        _BaseClusterManagerRestTransport._BaseCompleteIPRotation, ClusterManagerRestStub
    ):
        def __hash__(self):
            return hash("ClusterManagerRestTransport.CompleteIPRotation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: cluster_service.CompleteIPRotationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cluster_service.Operation:
            r"""Call the complete ip rotation method over HTTP.

            Args:
                request (~.cluster_service.CompleteIPRotationRequest):
                    The request object. CompleteIPRotationRequest moves the
                cluster master back into single-IP mode.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cluster_service.Operation:
                    This operation resource represents
                operations that may have happened or are
                happening on the cluster. All fields are
                output only.

            """

            http_options = _BaseClusterManagerRestTransport._BaseCompleteIPRotation._get_http_options()
            request, metadata = self._interceptor.pre_complete_ip_rotation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseClusterManagerRestTransport._BaseCompleteIPRotation,
                    "_BaseCompleteIPRotation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.container_v1.ClusterManagerClient.CompleteIPRotation",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "CompleteIPRotation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ClusterManagerRestTransport._CompleteIPRotation._get_response(
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
            resp = cluster_service.Operation()
            pb_resp = cluster_service.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_complete_ip_rotation(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_complete_ip_rotation_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cluster_service.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.container_v1.ClusterManagerClient.complete_ip_rotation",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "CompleteIPRotation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CompleteNodePoolUpgrade(
        _BaseClusterManagerRestTransport._BaseCompleteNodePoolUpgrade,
        ClusterManagerRestStub,
    ):
        def __hash__(self):
            return hash("ClusterManagerRestTransport.CompleteNodePoolUpgrade")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: cluster_service.CompleteNodePoolUpgradeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the complete node pool
            upgrade method over HTTP.

                Args:
                    request (~.cluster_service.CompleteNodePoolUpgradeRequest):
                        The request object. CompleteNodePoolUpgradeRequest sets
                    the name of target node pool to complete
                    upgrade.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.
            """

            http_options = _BaseClusterManagerRestTransport._BaseCompleteNodePoolUpgrade._get_http_options()
            request, metadata = self._interceptor.pre_complete_node_pool_upgrade(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseClusterManagerRestTransport._BaseCompleteNodePoolUpgrade,
                    "_BaseCompleteNodePoolUpgrade__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.container_v1.ClusterManagerClient.CompleteNodePoolUpgrade",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "CompleteNodePoolUpgrade",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ClusterManagerRestTransport._CompleteNodePoolUpgrade._get_response(
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

    class _CreateCluster(
        _BaseClusterManagerRestTransport._BaseCreateCluster, ClusterManagerRestStub
    ):
        def __hash__(self):
            return hash("ClusterManagerRestTransport.CreateCluster")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: cluster_service.CreateClusterRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cluster_service.Operation:
            r"""Call the create cluster method over HTTP.

            Args:
                request (~.cluster_service.CreateClusterRequest):
                    The request object. CreateClusterRequest creates a
                cluster.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cluster_service.Operation:
                    This operation resource represents
                operations that may have happened or are
                happening on the cluster. All fields are
                output only.

            """

            http_options = (
                _BaseClusterManagerRestTransport._BaseCreateCluster._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_cluster(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseClusterManagerRestTransport._BaseCreateCluster,
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
                    f"Sending request for google.container_v1.ClusterManagerClient.CreateCluster",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "CreateCluster",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ClusterManagerRestTransport._CreateCluster._get_response(
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
            resp = cluster_service.Operation()
            pb_resp = cluster_service.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_cluster(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_cluster_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cluster_service.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.container_v1.ClusterManagerClient.create_cluster",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "CreateCluster",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateNodePool(
        _BaseClusterManagerRestTransport._BaseCreateNodePool, ClusterManagerRestStub
    ):
        def __hash__(self):
            return hash("ClusterManagerRestTransport.CreateNodePool")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: cluster_service.CreateNodePoolRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cluster_service.Operation:
            r"""Call the create node pool method over HTTP.

            Args:
                request (~.cluster_service.CreateNodePoolRequest):
                    The request object. CreateNodePoolRequest creates a node
                pool for a cluster.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cluster_service.Operation:
                    This operation resource represents
                operations that may have happened or are
                happening on the cluster. All fields are
                output only.

            """

            http_options = (
                _BaseClusterManagerRestTransport._BaseCreateNodePool._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_node_pool(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseClusterManagerRestTransport._BaseCreateNodePool,
                    "_BaseCreateNodePool__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.container_v1.ClusterManagerClient.CreateNodePool",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "CreateNodePool",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ClusterManagerRestTransport._CreateNodePool._get_response(
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
            resp = cluster_service.Operation()
            pb_resp = cluster_service.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_node_pool(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_node_pool_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cluster_service.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.container_v1.ClusterManagerClient.create_node_pool",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "CreateNodePool",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteCluster(
        _BaseClusterManagerRestTransport._BaseDeleteCluster, ClusterManagerRestStub
    ):
        def __hash__(self):
            return hash("ClusterManagerRestTransport.DeleteCluster")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: cluster_service.DeleteClusterRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cluster_service.Operation:
            r"""Call the delete cluster method over HTTP.

            Args:
                request (~.cluster_service.DeleteClusterRequest):
                    The request object. DeleteClusterRequest deletes a
                cluster.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cluster_service.Operation:
                    This operation resource represents
                operations that may have happened or are
                happening on the cluster. All fields are
                output only.

            """

            http_options = (
                _BaseClusterManagerRestTransport._BaseDeleteCluster._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_cluster(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseClusterManagerRestTransport._BaseDeleteCluster,
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
                    f"Sending request for google.container_v1.ClusterManagerClient.DeleteCluster",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "DeleteCluster",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ClusterManagerRestTransport._DeleteCluster._get_response(
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
            resp = cluster_service.Operation()
            pb_resp = cluster_service.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_delete_cluster(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_cluster_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cluster_service.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.container_v1.ClusterManagerClient.delete_cluster",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "DeleteCluster",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteNodePool(
        _BaseClusterManagerRestTransport._BaseDeleteNodePool, ClusterManagerRestStub
    ):
        def __hash__(self):
            return hash("ClusterManagerRestTransport.DeleteNodePool")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: cluster_service.DeleteNodePoolRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cluster_service.Operation:
            r"""Call the delete node pool method over HTTP.

            Args:
                request (~.cluster_service.DeleteNodePoolRequest):
                    The request object. DeleteNodePoolRequest deletes a node
                pool for a cluster.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cluster_service.Operation:
                    This operation resource represents
                operations that may have happened or are
                happening on the cluster. All fields are
                output only.

            """

            http_options = (
                _BaseClusterManagerRestTransport._BaseDeleteNodePool._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_node_pool(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseClusterManagerRestTransport._BaseDeleteNodePool,
                    "_BaseDeleteNodePool__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.container_v1.ClusterManagerClient.DeleteNodePool",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "DeleteNodePool",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ClusterManagerRestTransport._DeleteNodePool._get_response(
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
            resp = cluster_service.Operation()
            pb_resp = cluster_service.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_delete_node_pool(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_node_pool_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cluster_service.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.container_v1.ClusterManagerClient.delete_node_pool",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "DeleteNodePool",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _FetchClusterUpgradeInfo(
        _BaseClusterManagerRestTransport._BaseFetchClusterUpgradeInfo,
        ClusterManagerRestStub,
    ):
        def __hash__(self):
            return hash("ClusterManagerRestTransport.FetchClusterUpgradeInfo")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: cluster_service.FetchClusterUpgradeInfoRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cluster_service.ClusterUpgradeInfo:
            r"""Call the fetch cluster upgrade
            info method over HTTP.

                Args:
                    request (~.cluster_service.FetchClusterUpgradeInfoRequest):
                        The request object. FetchClusterUpgradeInfoRequest
                    fetches the upgrade information of a
                    cluster.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.cluster_service.ClusterUpgradeInfo:
                        ClusterUpgradeInfo contains the
                    upgrade information of a cluster.

            """

            http_options = _BaseClusterManagerRestTransport._BaseFetchClusterUpgradeInfo._get_http_options()
            request, metadata = self._interceptor.pre_fetch_cluster_upgrade_info(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseClusterManagerRestTransport._BaseFetchClusterUpgradeInfo,
                    "_BaseFetchClusterUpgradeInfo__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.container_v1.ClusterManagerClient.FetchClusterUpgradeInfo",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "FetchClusterUpgradeInfo",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ClusterManagerRestTransport._FetchClusterUpgradeInfo._get_response(
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
            resp = cluster_service.ClusterUpgradeInfo()
            pb_resp = cluster_service.ClusterUpgradeInfo.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_fetch_cluster_upgrade_info(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_fetch_cluster_upgrade_info_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cluster_service.ClusterUpgradeInfo.to_json(
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
                    "Received response for google.container_v1.ClusterManagerClient.fetch_cluster_upgrade_info",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "FetchClusterUpgradeInfo",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _FetchNodePoolUpgradeInfo(
        _BaseClusterManagerRestTransport._BaseFetchNodePoolUpgradeInfo,
        ClusterManagerRestStub,
    ):
        def __hash__(self):
            return hash("ClusterManagerRestTransport.FetchNodePoolUpgradeInfo")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: cluster_service.FetchNodePoolUpgradeInfoRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cluster_service.NodePoolUpgradeInfo:
            r"""Call the fetch node pool upgrade
            info method over HTTP.

                Args:
                    request (~.cluster_service.FetchNodePoolUpgradeInfoRequest):
                        The request object. FetchNodePoolUpgradeInfoRequest
                    fetches the upgrade information of a
                    node pool.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.cluster_service.NodePoolUpgradeInfo:
                        NodePoolUpgradeInfo contains the
                    upgrade information of a node pool.

            """

            http_options = _BaseClusterManagerRestTransport._BaseFetchNodePoolUpgradeInfo._get_http_options()
            request, metadata = self._interceptor.pre_fetch_node_pool_upgrade_info(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseClusterManagerRestTransport._BaseFetchNodePoolUpgradeInfo,
                    "_BaseFetchNodePoolUpgradeInfo__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.container_v1.ClusterManagerClient.FetchNodePoolUpgradeInfo",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "FetchNodePoolUpgradeInfo",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ClusterManagerRestTransport._FetchNodePoolUpgradeInfo._get_response(
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
            resp = cluster_service.NodePoolUpgradeInfo()
            pb_resp = cluster_service.NodePoolUpgradeInfo.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_fetch_node_pool_upgrade_info(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_fetch_node_pool_upgrade_info_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cluster_service.NodePoolUpgradeInfo.to_json(
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
                    "Received response for google.container_v1.ClusterManagerClient.fetch_node_pool_upgrade_info",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "FetchNodePoolUpgradeInfo",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetCluster(
        _BaseClusterManagerRestTransport._BaseGetCluster, ClusterManagerRestStub
    ):
        def __hash__(self):
            return hash("ClusterManagerRestTransport.GetCluster")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: cluster_service.GetClusterRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cluster_service.Cluster:
            r"""Call the get cluster method over HTTP.

            Args:
                request (~.cluster_service.GetClusterRequest):
                    The request object. GetClusterRequest gets the settings
                of a cluster.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cluster_service.Cluster:
                    A Google Kubernetes Engine cluster.
            """

            http_options = (
                _BaseClusterManagerRestTransport._BaseGetCluster._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_cluster(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseClusterManagerRestTransport._BaseGetCluster,
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
                    f"Sending request for google.container_v1.ClusterManagerClient.GetCluster",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "GetCluster",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ClusterManagerRestTransport._GetCluster._get_response(
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
            resp = cluster_service.Cluster()
            pb_resp = cluster_service.Cluster.pb(resp)

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
                    response_payload = cluster_service.Cluster.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.container_v1.ClusterManagerClient.get_cluster",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "GetCluster",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetJSONWebKeys(
        _BaseClusterManagerRestTransport._BaseGetJSONWebKeys, ClusterManagerRestStub
    ):
        def __hash__(self):
            return hash("ClusterManagerRestTransport.GetJSONWebKeys")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: cluster_service.GetJSONWebKeysRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cluster_service.GetJSONWebKeysResponse:
            r"""Call the get json web keys method over HTTP.

            Args:
                request (~.cluster_service.GetJSONWebKeysRequest):
                    The request object. GetJSONWebKeysRequest gets the public component of the
                keys used by the cluster to sign token requests. This
                will be the jwks_uri for the discover document returned
                by getOpenIDConfig. See the OpenID Connect Discovery 1.0
                specification for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cluster_service.GetJSONWebKeysResponse:
                    GetJSONWebKeysResponse is a valid
                JSON Web Key Set as specified in rfc
                7517

            """

            http_options = (
                _BaseClusterManagerRestTransport._BaseGetJSONWebKeys._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_json_web_keys(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseClusterManagerRestTransport._BaseGetJSONWebKeys,
                    "_BaseGetJSONWebKeys__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.container_v1.ClusterManagerClient.GetJSONWebKeys",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "GetJSONWebKeys",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ClusterManagerRestTransport._GetJSONWebKeys._get_response(
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
            resp = cluster_service.GetJSONWebKeysResponse()
            pb_resp = cluster_service.GetJSONWebKeysResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_json_web_keys(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_json_web_keys_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cluster_service.GetJSONWebKeysResponse.to_json(
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
                    "Received response for google.container_v1.ClusterManagerClient.get_json_web_keys",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "GetJSONWebKeys",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetNodePool(
        _BaseClusterManagerRestTransport._BaseGetNodePool, ClusterManagerRestStub
    ):
        def __hash__(self):
            return hash("ClusterManagerRestTransport.GetNodePool")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: cluster_service.GetNodePoolRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cluster_service.NodePool:
            r"""Call the get node pool method over HTTP.

            Args:
                request (~.cluster_service.GetNodePoolRequest):
                    The request object. GetNodePoolRequest retrieves a node
                pool for a cluster.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cluster_service.NodePool:
                    NodePool contains the name and
                configuration for a cluster's node pool.
                Node pools are a set of nodes (i.e.
                VM's), with a common configuration and
                specification, under the control of the
                cluster master. They may have a set of
                Kubernetes labels applied to them, which
                may be used to reference them during pod
                scheduling. They may also be resized up
                or down, to accommodate the workload.

            """

            http_options = (
                _BaseClusterManagerRestTransport._BaseGetNodePool._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_node_pool(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseClusterManagerRestTransport._BaseGetNodePool,
                    "_BaseGetNodePool__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.container_v1.ClusterManagerClient.GetNodePool",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "GetNodePool",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ClusterManagerRestTransport._GetNodePool._get_response(
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
            resp = cluster_service.NodePool()
            pb_resp = cluster_service.NodePool.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_node_pool(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_node_pool_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cluster_service.NodePool.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.container_v1.ClusterManagerClient.get_node_pool",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "GetNodePool",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetOperation(
        _BaseClusterManagerRestTransport._BaseGetOperation, ClusterManagerRestStub
    ):
        def __hash__(self):
            return hash("ClusterManagerRestTransport.GetOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: cluster_service.GetOperationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cluster_service.Operation:
            r"""Call the get operation method over HTTP.

            Args:
                request (~.cluster_service.GetOperationRequest):
                    The request object. GetOperationRequest gets a single
                operation.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cluster_service.Operation:
                    This operation resource represents
                operations that may have happened or are
                happening on the cluster. All fields are
                output only.

            """

            http_options = (
                _BaseClusterManagerRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseClusterManagerRestTransport._BaseGetOperation,
                    "_BaseGetOperation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.container_v1.ClusterManagerClient.GetOperation",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ClusterManagerRestTransport._GetOperation._get_response(
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
            resp = cluster_service.Operation()
            pb_resp = cluster_service.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_operation(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_operation_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cluster_service.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.container_v1.ClusterManagerClient.get_operation",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "GetOperation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetServerConfig(
        _BaseClusterManagerRestTransport._BaseGetServerConfig, ClusterManagerRestStub
    ):
        def __hash__(self):
            return hash("ClusterManagerRestTransport.GetServerConfig")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: cluster_service.GetServerConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cluster_service.ServerConfig:
            r"""Call the get server config method over HTTP.

            Args:
                request (~.cluster_service.GetServerConfigRequest):
                    The request object. Gets the current Kubernetes Engine
                service configuration.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cluster_service.ServerConfig:
                    Kubernetes Engine service
                configuration.

            """

            http_options = _BaseClusterManagerRestTransport._BaseGetServerConfig._get_http_options()
            request, metadata = self._interceptor.pre_get_server_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseClusterManagerRestTransport._BaseGetServerConfig,
                    "_BaseGetServerConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.container_v1.ClusterManagerClient.GetServerConfig",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "GetServerConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ClusterManagerRestTransport._GetServerConfig._get_response(
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
            resp = cluster_service.ServerConfig()
            pb_resp = cluster_service.ServerConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_server_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_server_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cluster_service.ServerConfig.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.container_v1.ClusterManagerClient.get_server_config",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "GetServerConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListClusters(
        _BaseClusterManagerRestTransport._BaseListClusters, ClusterManagerRestStub
    ):
        def __hash__(self):
            return hash("ClusterManagerRestTransport.ListClusters")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: cluster_service.ListClustersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cluster_service.ListClustersResponse:
            r"""Call the list clusters method over HTTP.

            Args:
                request (~.cluster_service.ListClustersRequest):
                    The request object. ListClustersRequest lists clusters.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cluster_service.ListClustersResponse:
                    ListClustersResponse is the result of
                ListClustersRequest.

            """

            http_options = (
                _BaseClusterManagerRestTransport._BaseListClusters._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_clusters(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseClusterManagerRestTransport._BaseListClusters,
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
                    f"Sending request for google.container_v1.ClusterManagerClient.ListClusters",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "ListClusters",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ClusterManagerRestTransport._ListClusters._get_response(
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
            resp = cluster_service.ListClustersResponse()
            pb_resp = cluster_service.ListClustersResponse.pb(resp)

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
                    response_payload = cluster_service.ListClustersResponse.to_json(
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
                    "Received response for google.container_v1.ClusterManagerClient.list_clusters",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "ListClusters",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListNodePools(
        _BaseClusterManagerRestTransport._BaseListNodePools, ClusterManagerRestStub
    ):
        def __hash__(self):
            return hash("ClusterManagerRestTransport.ListNodePools")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: cluster_service.ListNodePoolsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cluster_service.ListNodePoolsResponse:
            r"""Call the list node pools method over HTTP.

            Args:
                request (~.cluster_service.ListNodePoolsRequest):
                    The request object. ListNodePoolsRequest lists the node
                pool(s) for a cluster.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cluster_service.ListNodePoolsResponse:
                    ListNodePoolsResponse is the result
                of ListNodePoolsRequest.

            """

            http_options = (
                _BaseClusterManagerRestTransport._BaseListNodePools._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_node_pools(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseClusterManagerRestTransport._BaseListNodePools,
                    "_BaseListNodePools__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.container_v1.ClusterManagerClient.ListNodePools",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "ListNodePools",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ClusterManagerRestTransport._ListNodePools._get_response(
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
            resp = cluster_service.ListNodePoolsResponse()
            pb_resp = cluster_service.ListNodePoolsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_node_pools(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_node_pools_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cluster_service.ListNodePoolsResponse.to_json(
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
                    "Received response for google.container_v1.ClusterManagerClient.list_node_pools",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "ListNodePools",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListOperations(
        _BaseClusterManagerRestTransport._BaseListOperations, ClusterManagerRestStub
    ):
        def __hash__(self):
            return hash("ClusterManagerRestTransport.ListOperations")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: cluster_service.ListOperationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cluster_service.ListOperationsResponse:
            r"""Call the list operations method over HTTP.

            Args:
                request (~.cluster_service.ListOperationsRequest):
                    The request object. ListOperationsRequest lists
                operations.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cluster_service.ListOperationsResponse:
                    ListOperationsResponse is the result
                of ListOperationsRequest.

            """

            http_options = (
                _BaseClusterManagerRestTransport._BaseListOperations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseClusterManagerRestTransport._BaseListOperations,
                    "_BaseListOperations__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.container_v1.ClusterManagerClient.ListOperations",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ClusterManagerRestTransport._ListOperations._get_response(
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
            resp = cluster_service.ListOperationsResponse()
            pb_resp = cluster_service.ListOperationsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_operations(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_operations_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cluster_service.ListOperationsResponse.to_json(
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
                    "Received response for google.container_v1.ClusterManagerClient.list_operations",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "ListOperations",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListUsableSubnetworks(
        _BaseClusterManagerRestTransport._BaseListUsableSubnetworks,
        ClusterManagerRestStub,
    ):
        def __hash__(self):
            return hash("ClusterManagerRestTransport.ListUsableSubnetworks")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: cluster_service.ListUsableSubnetworksRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cluster_service.ListUsableSubnetworksResponse:
            r"""Call the list usable subnetworks method over HTTP.

            Args:
                request (~.cluster_service.ListUsableSubnetworksRequest):
                    The request object. ListUsableSubnetworksRequest requests
                the list of usable subnetworks available
                to a user for creating clusters.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cluster_service.ListUsableSubnetworksResponse:
                    ListUsableSubnetworksResponse is the
                response of
                ListUsableSubnetworksRequest.

            """

            http_options = _BaseClusterManagerRestTransport._BaseListUsableSubnetworks._get_http_options()
            request, metadata = self._interceptor.pre_list_usable_subnetworks(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseClusterManagerRestTransport._BaseListUsableSubnetworks,
                    "_BaseListUsableSubnetworks__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.container_v1.ClusterManagerClient.ListUsableSubnetworks",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "ListUsableSubnetworks",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ClusterManagerRestTransport._ListUsableSubnetworks._get_response(
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
            resp = cluster_service.ListUsableSubnetworksResponse()
            pb_resp = cluster_service.ListUsableSubnetworksResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_usable_subnetworks(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_usable_subnetworks_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        cluster_service.ListUsableSubnetworksResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.container_v1.ClusterManagerClient.list_usable_subnetworks",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "ListUsableSubnetworks",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RollbackNodePoolUpgrade(
        _BaseClusterManagerRestTransport._BaseRollbackNodePoolUpgrade,
        ClusterManagerRestStub,
    ):
        def __hash__(self):
            return hash("ClusterManagerRestTransport.RollbackNodePoolUpgrade")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: cluster_service.RollbackNodePoolUpgradeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cluster_service.Operation:
            r"""Call the rollback node pool
            upgrade method over HTTP.

                Args:
                    request (~.cluster_service.RollbackNodePoolUpgradeRequest):
                        The request object. RollbackNodePoolUpgradeRequest
                    rollbacks the previously Aborted or
                    Failed  NodePool upgrade. This will be
                    an no-op if the last upgrade
                    successfully  completed.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.cluster_service.Operation:
                        This operation resource represents
                    operations that may have happened or are
                    happening on the cluster. All fields are
                    output only.

            """

            http_options = _BaseClusterManagerRestTransport._BaseRollbackNodePoolUpgrade._get_http_options()
            request, metadata = self._interceptor.pre_rollback_node_pool_upgrade(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseClusterManagerRestTransport._BaseRollbackNodePoolUpgrade,
                    "_BaseRollbackNodePoolUpgrade__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.container_v1.ClusterManagerClient.RollbackNodePoolUpgrade",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "RollbackNodePoolUpgrade",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ClusterManagerRestTransport._RollbackNodePoolUpgrade._get_response(
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
            resp = cluster_service.Operation()
            pb_resp = cluster_service.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_rollback_node_pool_upgrade(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_rollback_node_pool_upgrade_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cluster_service.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.container_v1.ClusterManagerClient.rollback_node_pool_upgrade",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "RollbackNodePoolUpgrade",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SetAddonsConfig(
        _BaseClusterManagerRestTransport._BaseSetAddonsConfig, ClusterManagerRestStub
    ):
        def __hash__(self):
            return hash("ClusterManagerRestTransport.SetAddonsConfig")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: cluster_service.SetAddonsConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cluster_service.Operation:
            r"""Call the set addons config method over HTTP.

            Args:
                request (~.cluster_service.SetAddonsConfigRequest):
                    The request object. SetAddonsConfigRequest sets the
                addons associated with the cluster.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cluster_service.Operation:
                    This operation resource represents
                operations that may have happened or are
                happening on the cluster. All fields are
                output only.

            """

            http_options = _BaseClusterManagerRestTransport._BaseSetAddonsConfig._get_http_options()
            request, metadata = self._interceptor.pre_set_addons_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseClusterManagerRestTransport._BaseSetAddonsConfig,
                    "_BaseSetAddonsConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.container_v1.ClusterManagerClient.SetAddonsConfig",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "SetAddonsConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ClusterManagerRestTransport._SetAddonsConfig._get_response(
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
            resp = cluster_service.Operation()
            pb_resp = cluster_service.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_set_addons_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_set_addons_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cluster_service.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.container_v1.ClusterManagerClient.set_addons_config",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "SetAddonsConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SetLabels(
        _BaseClusterManagerRestTransport._BaseSetLabels, ClusterManagerRestStub
    ):
        def __hash__(self):
            return hash("ClusterManagerRestTransport.SetLabels")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: cluster_service.SetLabelsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cluster_service.Operation:
            r"""Call the set labels method over HTTP.

            Args:
                request (~.cluster_service.SetLabelsRequest):
                    The request object. SetLabelsRequest sets the Google
                Cloud Platform labels on a Google
                Container Engine cluster, which will in
                turn set them for Google Compute Engine
                resources used by that cluster
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cluster_service.Operation:
                    This operation resource represents
                operations that may have happened or are
                happening on the cluster. All fields are
                output only.

            """

            http_options = (
                _BaseClusterManagerRestTransport._BaseSetLabels._get_http_options()
            )
            request, metadata = self._interceptor.pre_set_labels(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseClusterManagerRestTransport._BaseSetLabels,
                    "_BaseSetLabels__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.container_v1.ClusterManagerClient.SetLabels",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "SetLabels",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ClusterManagerRestTransport._SetLabels._get_response(
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
            resp = cluster_service.Operation()
            pb_resp = cluster_service.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_set_labels(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_set_labels_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cluster_service.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.container_v1.ClusterManagerClient.set_labels",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "SetLabels",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SetLegacyAbac(
        _BaseClusterManagerRestTransport._BaseSetLegacyAbac, ClusterManagerRestStub
    ):
        def __hash__(self):
            return hash("ClusterManagerRestTransport.SetLegacyAbac")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: cluster_service.SetLegacyAbacRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cluster_service.Operation:
            r"""Call the set legacy abac method over HTTP.

            Args:
                request (~.cluster_service.SetLegacyAbacRequest):
                    The request object. SetLegacyAbacRequest enables or
                disables the ABAC authorization
                mechanism for a cluster.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cluster_service.Operation:
                    This operation resource represents
                operations that may have happened or are
                happening on the cluster. All fields are
                output only.

            """

            http_options = (
                _BaseClusterManagerRestTransport._BaseSetLegacyAbac._get_http_options()
            )
            request, metadata = self._interceptor.pre_set_legacy_abac(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseClusterManagerRestTransport._BaseSetLegacyAbac,
                    "_BaseSetLegacyAbac__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.container_v1.ClusterManagerClient.SetLegacyAbac",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "SetLegacyAbac",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ClusterManagerRestTransport._SetLegacyAbac._get_response(
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
            resp = cluster_service.Operation()
            pb_resp = cluster_service.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_set_legacy_abac(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_set_legacy_abac_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cluster_service.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.container_v1.ClusterManagerClient.set_legacy_abac",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "SetLegacyAbac",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SetLocations(
        _BaseClusterManagerRestTransport._BaseSetLocations, ClusterManagerRestStub
    ):
        def __hash__(self):
            return hash("ClusterManagerRestTransport.SetLocations")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: cluster_service.SetLocationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cluster_service.Operation:
            r"""Call the set locations method over HTTP.

            Args:
                request (~.cluster_service.SetLocationsRequest):
                    The request object. SetLocationsRequest sets the
                locations of the cluster.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cluster_service.Operation:
                    This operation resource represents
                operations that may have happened or are
                happening on the cluster. All fields are
                output only.

            """

            http_options = (
                _BaseClusterManagerRestTransport._BaseSetLocations._get_http_options()
            )
            request, metadata = self._interceptor.pre_set_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseClusterManagerRestTransport._BaseSetLocations,
                    "_BaseSetLocations__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.container_v1.ClusterManagerClient.SetLocations",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "SetLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ClusterManagerRestTransport._SetLocations._get_response(
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
            resp = cluster_service.Operation()
            pb_resp = cluster_service.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_set_locations(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_set_locations_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cluster_service.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.container_v1.ClusterManagerClient.set_locations",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "SetLocations",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SetLoggingService(
        _BaseClusterManagerRestTransport._BaseSetLoggingService, ClusterManagerRestStub
    ):
        def __hash__(self):
            return hash("ClusterManagerRestTransport.SetLoggingService")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: cluster_service.SetLoggingServiceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cluster_service.Operation:
            r"""Call the set logging service method over HTTP.

            Args:
                request (~.cluster_service.SetLoggingServiceRequest):
                    The request object. SetLoggingServiceRequest sets the
                logging service of a cluster.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cluster_service.Operation:
                    This operation resource represents
                operations that may have happened or are
                happening on the cluster. All fields are
                output only.

            """

            http_options = _BaseClusterManagerRestTransport._BaseSetLoggingService._get_http_options()
            request, metadata = self._interceptor.pre_set_logging_service(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseClusterManagerRestTransport._BaseSetLoggingService,
                    "_BaseSetLoggingService__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.container_v1.ClusterManagerClient.SetLoggingService",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "SetLoggingService",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ClusterManagerRestTransport._SetLoggingService._get_response(
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
            resp = cluster_service.Operation()
            pb_resp = cluster_service.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_set_logging_service(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_set_logging_service_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cluster_service.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.container_v1.ClusterManagerClient.set_logging_service",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "SetLoggingService",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SetMaintenancePolicy(
        _BaseClusterManagerRestTransport._BaseSetMaintenancePolicy,
        ClusterManagerRestStub,
    ):
        def __hash__(self):
            return hash("ClusterManagerRestTransport.SetMaintenancePolicy")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: cluster_service.SetMaintenancePolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cluster_service.Operation:
            r"""Call the set maintenance policy method over HTTP.

            Args:
                request (~.cluster_service.SetMaintenancePolicyRequest):
                    The request object. SetMaintenancePolicyRequest sets the
                maintenance policy for a cluster.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cluster_service.Operation:
                    This operation resource represents
                operations that may have happened or are
                happening on the cluster. All fields are
                output only.

            """

            http_options = _BaseClusterManagerRestTransport._BaseSetMaintenancePolicy._get_http_options()
            request, metadata = self._interceptor.pre_set_maintenance_policy(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseClusterManagerRestTransport._BaseSetMaintenancePolicy,
                    "_BaseSetMaintenancePolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.container_v1.ClusterManagerClient.SetMaintenancePolicy",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "SetMaintenancePolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ClusterManagerRestTransport._SetMaintenancePolicy._get_response(
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
            resp = cluster_service.Operation()
            pb_resp = cluster_service.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_set_maintenance_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_set_maintenance_policy_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cluster_service.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.container_v1.ClusterManagerClient.set_maintenance_policy",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "SetMaintenancePolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SetMasterAuth(
        _BaseClusterManagerRestTransport._BaseSetMasterAuth, ClusterManagerRestStub
    ):
        def __hash__(self):
            return hash("ClusterManagerRestTransport.SetMasterAuth")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: cluster_service.SetMasterAuthRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cluster_service.Operation:
            r"""Call the set master auth method over HTTP.

            Args:
                request (~.cluster_service.SetMasterAuthRequest):
                    The request object. SetMasterAuthRequest updates the
                admin password of a cluster.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cluster_service.Operation:
                    This operation resource represents
                operations that may have happened or are
                happening on the cluster. All fields are
                output only.

            """

            http_options = (
                _BaseClusterManagerRestTransport._BaseSetMasterAuth._get_http_options()
            )
            request, metadata = self._interceptor.pre_set_master_auth(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseClusterManagerRestTransport._BaseSetMasterAuth,
                    "_BaseSetMasterAuth__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.container_v1.ClusterManagerClient.SetMasterAuth",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "SetMasterAuth",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ClusterManagerRestTransport._SetMasterAuth._get_response(
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
            resp = cluster_service.Operation()
            pb_resp = cluster_service.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_set_master_auth(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_set_master_auth_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cluster_service.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.container_v1.ClusterManagerClient.set_master_auth",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "SetMasterAuth",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SetMonitoringService(
        _BaseClusterManagerRestTransport._BaseSetMonitoringService,
        ClusterManagerRestStub,
    ):
        def __hash__(self):
            return hash("ClusterManagerRestTransport.SetMonitoringService")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: cluster_service.SetMonitoringServiceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cluster_service.Operation:
            r"""Call the set monitoring service method over HTTP.

            Args:
                request (~.cluster_service.SetMonitoringServiceRequest):
                    The request object. SetMonitoringServiceRequest sets the
                monitoring service of a cluster.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cluster_service.Operation:
                    This operation resource represents
                operations that may have happened or are
                happening on the cluster. All fields are
                output only.

            """

            http_options = _BaseClusterManagerRestTransport._BaseSetMonitoringService._get_http_options()
            request, metadata = self._interceptor.pre_set_monitoring_service(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseClusterManagerRestTransport._BaseSetMonitoringService,
                    "_BaseSetMonitoringService__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.container_v1.ClusterManagerClient.SetMonitoringService",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "SetMonitoringService",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ClusterManagerRestTransport._SetMonitoringService._get_response(
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
            resp = cluster_service.Operation()
            pb_resp = cluster_service.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_set_monitoring_service(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_set_monitoring_service_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cluster_service.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.container_v1.ClusterManagerClient.set_monitoring_service",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "SetMonitoringService",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SetNetworkPolicy(
        _BaseClusterManagerRestTransport._BaseSetNetworkPolicy, ClusterManagerRestStub
    ):
        def __hash__(self):
            return hash("ClusterManagerRestTransport.SetNetworkPolicy")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: cluster_service.SetNetworkPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cluster_service.Operation:
            r"""Call the set network policy method over HTTP.

            Args:
                request (~.cluster_service.SetNetworkPolicyRequest):
                    The request object. SetNetworkPolicyRequest
                enables/disables network policy for a
                cluster.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cluster_service.Operation:
                    This operation resource represents
                operations that may have happened or are
                happening on the cluster. All fields are
                output only.

            """

            http_options = _BaseClusterManagerRestTransport._BaseSetNetworkPolicy._get_http_options()
            request, metadata = self._interceptor.pre_set_network_policy(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseClusterManagerRestTransport._BaseSetNetworkPolicy,
                    "_BaseSetNetworkPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.container_v1.ClusterManagerClient.SetNetworkPolicy",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "SetNetworkPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ClusterManagerRestTransport._SetNetworkPolicy._get_response(
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
            resp = cluster_service.Operation()
            pb_resp = cluster_service.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_set_network_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_set_network_policy_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cluster_service.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.container_v1.ClusterManagerClient.set_network_policy",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "SetNetworkPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SetNodePoolAutoscaling(
        _BaseClusterManagerRestTransport._BaseSetNodePoolAutoscaling,
        ClusterManagerRestStub,
    ):
        def __hash__(self):
            return hash("ClusterManagerRestTransport.SetNodePoolAutoscaling")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: cluster_service.SetNodePoolAutoscalingRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cluster_service.Operation:
            r"""Call the set node pool autoscaling method over HTTP.

            Args:
                request (~.cluster_service.SetNodePoolAutoscalingRequest):
                    The request object. SetNodePoolAutoscalingRequest sets
                the autoscaler settings of a node pool.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cluster_service.Operation:
                    This operation resource represents
                operations that may have happened or are
                happening on the cluster. All fields are
                output only.

            """

            http_options = _BaseClusterManagerRestTransport._BaseSetNodePoolAutoscaling._get_http_options()
            request, metadata = self._interceptor.pre_set_node_pool_autoscaling(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseClusterManagerRestTransport._BaseSetNodePoolAutoscaling,
                    "_BaseSetNodePoolAutoscaling__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.container_v1.ClusterManagerClient.SetNodePoolAutoscaling",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "SetNodePoolAutoscaling",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ClusterManagerRestTransport._SetNodePoolAutoscaling._get_response(
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
            resp = cluster_service.Operation()
            pb_resp = cluster_service.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_set_node_pool_autoscaling(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_set_node_pool_autoscaling_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cluster_service.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.container_v1.ClusterManagerClient.set_node_pool_autoscaling",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "SetNodePoolAutoscaling",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SetNodePoolManagement(
        _BaseClusterManagerRestTransport._BaseSetNodePoolManagement,
        ClusterManagerRestStub,
    ):
        def __hash__(self):
            return hash("ClusterManagerRestTransport.SetNodePoolManagement")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: cluster_service.SetNodePoolManagementRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cluster_service.Operation:
            r"""Call the set node pool management method over HTTP.

            Args:
                request (~.cluster_service.SetNodePoolManagementRequest):
                    The request object. SetNodePoolManagementRequest sets the
                node management properties of a node
                pool.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cluster_service.Operation:
                    This operation resource represents
                operations that may have happened or are
                happening on the cluster. All fields are
                output only.

            """

            http_options = _BaseClusterManagerRestTransport._BaseSetNodePoolManagement._get_http_options()
            request, metadata = self._interceptor.pre_set_node_pool_management(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseClusterManagerRestTransport._BaseSetNodePoolManagement,
                    "_BaseSetNodePoolManagement__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.container_v1.ClusterManagerClient.SetNodePoolManagement",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "SetNodePoolManagement",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ClusterManagerRestTransport._SetNodePoolManagement._get_response(
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
            resp = cluster_service.Operation()
            pb_resp = cluster_service.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_set_node_pool_management(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_set_node_pool_management_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cluster_service.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.container_v1.ClusterManagerClient.set_node_pool_management",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "SetNodePoolManagement",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SetNodePoolSize(
        _BaseClusterManagerRestTransport._BaseSetNodePoolSize, ClusterManagerRestStub
    ):
        def __hash__(self):
            return hash("ClusterManagerRestTransport.SetNodePoolSize")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: cluster_service.SetNodePoolSizeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cluster_service.Operation:
            r"""Call the set node pool size method over HTTP.

            Args:
                request (~.cluster_service.SetNodePoolSizeRequest):
                    The request object. SetNodePoolSizeRequest sets the size
                of a node pool.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cluster_service.Operation:
                    This operation resource represents
                operations that may have happened or are
                happening on the cluster. All fields are
                output only.

            """

            http_options = _BaseClusterManagerRestTransport._BaseSetNodePoolSize._get_http_options()
            request, metadata = self._interceptor.pre_set_node_pool_size(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseClusterManagerRestTransport._BaseSetNodePoolSize,
                    "_BaseSetNodePoolSize__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.container_v1.ClusterManagerClient.SetNodePoolSize",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "SetNodePoolSize",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ClusterManagerRestTransport._SetNodePoolSize._get_response(
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
            resp = cluster_service.Operation()
            pb_resp = cluster_service.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_set_node_pool_size(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_set_node_pool_size_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cluster_service.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.container_v1.ClusterManagerClient.set_node_pool_size",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "SetNodePoolSize",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _StartIPRotation(
        _BaseClusterManagerRestTransport._BaseStartIPRotation, ClusterManagerRestStub
    ):
        def __hash__(self):
            return hash("ClusterManagerRestTransport.StartIPRotation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: cluster_service.StartIPRotationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cluster_service.Operation:
            r"""Call the start ip rotation method over HTTP.

            Args:
                request (~.cluster_service.StartIPRotationRequest):
                    The request object. StartIPRotationRequest creates a new
                IP for the cluster and then performs a
                node upgrade on each node pool to point
                to the new IP.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cluster_service.Operation:
                    This operation resource represents
                operations that may have happened or are
                happening on the cluster. All fields are
                output only.

            """

            http_options = _BaseClusterManagerRestTransport._BaseStartIPRotation._get_http_options()
            request, metadata = self._interceptor.pre_start_ip_rotation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseClusterManagerRestTransport._BaseStartIPRotation,
                    "_BaseStartIPRotation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.container_v1.ClusterManagerClient.StartIPRotation",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "StartIPRotation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ClusterManagerRestTransport._StartIPRotation._get_response(
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
            resp = cluster_service.Operation()
            pb_resp = cluster_service.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_start_ip_rotation(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_start_ip_rotation_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cluster_service.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.container_v1.ClusterManagerClient.start_ip_rotation",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "StartIPRotation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateCluster(
        _BaseClusterManagerRestTransport._BaseUpdateCluster, ClusterManagerRestStub
    ):
        def __hash__(self):
            return hash("ClusterManagerRestTransport.UpdateCluster")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: cluster_service.UpdateClusterRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cluster_service.Operation:
            r"""Call the update cluster method over HTTP.

            Args:
                request (~.cluster_service.UpdateClusterRequest):
                    The request object. UpdateClusterRequest updates the
                settings of a cluster.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cluster_service.Operation:
                    This operation resource represents
                operations that may have happened or are
                happening on the cluster. All fields are
                output only.

            """

            http_options = (
                _BaseClusterManagerRestTransport._BaseUpdateCluster._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_cluster(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseClusterManagerRestTransport._BaseUpdateCluster,
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
                    f"Sending request for google.container_v1.ClusterManagerClient.UpdateCluster",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "UpdateCluster",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ClusterManagerRestTransport._UpdateCluster._get_response(
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
            resp = cluster_service.Operation()
            pb_resp = cluster_service.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_cluster(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_cluster_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cluster_service.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.container_v1.ClusterManagerClient.update_cluster",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "UpdateCluster",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateMaster(
        _BaseClusterManagerRestTransport._BaseUpdateMaster, ClusterManagerRestStub
    ):
        def __hash__(self):
            return hash("ClusterManagerRestTransport.UpdateMaster")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: cluster_service.UpdateMasterRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cluster_service.Operation:
            r"""Call the update master method over HTTP.

            Args:
                request (~.cluster_service.UpdateMasterRequest):
                    The request object. UpdateMasterRequest updates the
                master of the cluster.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cluster_service.Operation:
                    This operation resource represents
                operations that may have happened or are
                happening on the cluster. All fields are
                output only.

            """

            http_options = (
                _BaseClusterManagerRestTransport._BaseUpdateMaster._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_master(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseClusterManagerRestTransport._BaseUpdateMaster,
                    "_BaseUpdateMaster__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.container_v1.ClusterManagerClient.UpdateMaster",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "UpdateMaster",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ClusterManagerRestTransport._UpdateMaster._get_response(
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
            resp = cluster_service.Operation()
            pb_resp = cluster_service.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_master(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_master_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cluster_service.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.container_v1.ClusterManagerClient.update_master",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "UpdateMaster",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateNodePool(
        _BaseClusterManagerRestTransport._BaseUpdateNodePool, ClusterManagerRestStub
    ):
        def __hash__(self):
            return hash("ClusterManagerRestTransport.UpdateNodePool")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: cluster_service.UpdateNodePoolRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cluster_service.Operation:
            r"""Call the update node pool method over HTTP.

            Args:
                request (~.cluster_service.UpdateNodePoolRequest):
                    The request object. UpdateNodePoolRequests update a node
                pool's image and/or version.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cluster_service.Operation:
                    This operation resource represents
                operations that may have happened or are
                happening on the cluster. All fields are
                output only.

            """

            http_options = (
                _BaseClusterManagerRestTransport._BaseUpdateNodePool._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_node_pool(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseClusterManagerRestTransport._BaseUpdateNodePool,
                    "_BaseUpdateNodePool__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.container_v1.ClusterManagerClient.UpdateNodePool",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "UpdateNodePool",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ClusterManagerRestTransport._UpdateNodePool._get_response(
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
            resp = cluster_service.Operation()
            pb_resp = cluster_service.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_node_pool(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_node_pool_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cluster_service.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.container_v1.ClusterManagerClient.update_node_pool",
                    extra={
                        "serviceName": "google.container.v1.ClusterManager",
                        "rpcName": "UpdateNodePool",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def cancel_operation(
        self,
    ) -> Callable[[cluster_service.CancelOperationRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def check_autopilot_compatibility(
        self,
    ) -> Callable[
        [cluster_service.CheckAutopilotCompatibilityRequest],
        cluster_service.CheckAutopilotCompatibilityResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CheckAutopilotCompatibility(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def complete_control_plane_upgrade(
        self,
    ) -> Callable[
        [cluster_service.CompleteControlPlaneUpgradeRequest], cluster_service.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CompleteControlPlaneUpgrade(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def complete_ip_rotation(
        self,
    ) -> Callable[
        [cluster_service.CompleteIPRotationRequest], cluster_service.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CompleteIPRotation(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def complete_node_pool_upgrade(
        self,
    ) -> Callable[[cluster_service.CompleteNodePoolUpgradeRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CompleteNodePoolUpgrade(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_cluster(
        self,
    ) -> Callable[[cluster_service.CreateClusterRequest], cluster_service.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateCluster(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_node_pool(
        self,
    ) -> Callable[[cluster_service.CreateNodePoolRequest], cluster_service.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateNodePool(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_cluster(
        self,
    ) -> Callable[[cluster_service.DeleteClusterRequest], cluster_service.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteCluster(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_node_pool(
        self,
    ) -> Callable[[cluster_service.DeleteNodePoolRequest], cluster_service.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteNodePool(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def fetch_cluster_upgrade_info(
        self,
    ) -> Callable[
        [cluster_service.FetchClusterUpgradeInfoRequest],
        cluster_service.ClusterUpgradeInfo,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._FetchClusterUpgradeInfo(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def fetch_node_pool_upgrade_info(
        self,
    ) -> Callable[
        [cluster_service.FetchNodePoolUpgradeInfoRequest],
        cluster_service.NodePoolUpgradeInfo,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._FetchNodePoolUpgradeInfo(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_cluster(
        self,
    ) -> Callable[[cluster_service.GetClusterRequest], cluster_service.Cluster]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetCluster(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_json_web_keys(
        self,
    ) -> Callable[
        [cluster_service.GetJSONWebKeysRequest], cluster_service.GetJSONWebKeysResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetJSONWebKeys(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_node_pool(
        self,
    ) -> Callable[[cluster_service.GetNodePoolRequest], cluster_service.NodePool]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetNodePool(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_operation(
        self,
    ) -> Callable[[cluster_service.GetOperationRequest], cluster_service.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetOperation(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_server_config(
        self,
    ) -> Callable[
        [cluster_service.GetServerConfigRequest], cluster_service.ServerConfig
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetServerConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_clusters(
        self,
    ) -> Callable[
        [cluster_service.ListClustersRequest], cluster_service.ListClustersResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListClusters(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_node_pools(
        self,
    ) -> Callable[
        [cluster_service.ListNodePoolsRequest], cluster_service.ListNodePoolsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListNodePools(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_operations(
        self,
    ) -> Callable[
        [cluster_service.ListOperationsRequest], cluster_service.ListOperationsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListOperations(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_usable_subnetworks(
        self,
    ) -> Callable[
        [cluster_service.ListUsableSubnetworksRequest],
        cluster_service.ListUsableSubnetworksResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListUsableSubnetworks(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def rollback_node_pool_upgrade(
        self,
    ) -> Callable[
        [cluster_service.RollbackNodePoolUpgradeRequest], cluster_service.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RollbackNodePoolUpgrade(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def set_addons_config(
        self,
    ) -> Callable[[cluster_service.SetAddonsConfigRequest], cluster_service.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SetAddonsConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def set_labels(
        self,
    ) -> Callable[[cluster_service.SetLabelsRequest], cluster_service.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SetLabels(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def set_legacy_abac(
        self,
    ) -> Callable[[cluster_service.SetLegacyAbacRequest], cluster_service.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SetLegacyAbac(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def set_locations(
        self,
    ) -> Callable[[cluster_service.SetLocationsRequest], cluster_service.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SetLocations(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def set_logging_service(
        self,
    ) -> Callable[
        [cluster_service.SetLoggingServiceRequest], cluster_service.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SetLoggingService(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def set_maintenance_policy(
        self,
    ) -> Callable[
        [cluster_service.SetMaintenancePolicyRequest], cluster_service.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SetMaintenancePolicy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def set_master_auth(
        self,
    ) -> Callable[[cluster_service.SetMasterAuthRequest], cluster_service.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SetMasterAuth(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def set_monitoring_service(
        self,
    ) -> Callable[
        [cluster_service.SetMonitoringServiceRequest], cluster_service.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SetMonitoringService(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def set_network_policy(
        self,
    ) -> Callable[[cluster_service.SetNetworkPolicyRequest], cluster_service.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SetNetworkPolicy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def set_node_pool_autoscaling(
        self,
    ) -> Callable[
        [cluster_service.SetNodePoolAutoscalingRequest], cluster_service.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SetNodePoolAutoscaling(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def set_node_pool_management(
        self,
    ) -> Callable[
        [cluster_service.SetNodePoolManagementRequest], cluster_service.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SetNodePoolManagement(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def set_node_pool_size(
        self,
    ) -> Callable[[cluster_service.SetNodePoolSizeRequest], cluster_service.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SetNodePoolSize(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def start_ip_rotation(
        self,
    ) -> Callable[[cluster_service.StartIPRotationRequest], cluster_service.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._StartIPRotation(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_cluster(
        self,
    ) -> Callable[[cluster_service.UpdateClusterRequest], cluster_service.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateCluster(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_master(
        self,
    ) -> Callable[[cluster_service.UpdateMasterRequest], cluster_service.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateMaster(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_node_pool(
        self,
    ) -> Callable[[cluster_service.UpdateNodePoolRequest], cluster_service.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateNodePool(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("ClusterManagerRestTransport",)
