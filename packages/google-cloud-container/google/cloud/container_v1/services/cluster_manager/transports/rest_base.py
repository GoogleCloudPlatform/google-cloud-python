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
import json  # type: ignore
import re
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Union

import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
from google.api_core import gapic_v1, path_template
from google.protobuf import json_format

from google.cloud.container_v1.types import cluster_service

from .base import DEFAULT_CLIENT_INFO, ClusterManagerTransport


class _BaseClusterManagerRestTransport(ClusterManagerTransport):
    """Base REST backend transport for ClusterManager.

    Note: This class is not meant to be used directly. Use its sync and
    async sub-classes instead.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "container.googleapis.com",
        credentials: Optional[Any] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.
        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'container.googleapis.com').
            credentials (Optional[Any]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
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
        """
        # Run the base constructor
        maybe_url_match = re.match("^(?P<scheme>http(?:s)?://)?(?P<host>.*)$", host)
        if maybe_url_match is None:
            raise ValueError(
                f"Unexpected hostname structure: {host}"
            )  # pragma: NO COVER

        url_match_items = maybe_url_match.groupdict()

        host = f"{url_scheme}://{host}" if not url_match_items["scheme"] else host

        super().__init__(
            host=host,
            credentials=credentials,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
            api_audience=api_audience,
        )

    class _BaseCancelOperation:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1/{name=projects/*/locations/*/operations/*}:cancel",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1/projects/{project_id}/zones/{zone}/operations/{operation_id}:cancel",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseCheckAutopilotCompatibility:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{name=projects/*/locations/*/clusters/*}:checkAutopilotCompatibility",
                },
            ]
            return http_options

    class _BaseCompleteControlPlaneUpgrade:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1/{name=projects/*/locations/*/clusters/*}:completeControlPlaneUpgrade",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1/{name=projects/*/zones/*/clusters/*}:completeControlPlaneUpgrade",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseCompleteIPRotation:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1/{name=projects/*/locations/*/clusters/*}:completeIpRotation",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1/projects/{project_id}/zones/{zone}/clusters/{cluster_id}:completeIpRotation",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseCompleteNodePoolUpgrade:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1/{name=projects/*/locations/*/clusters/*/nodePools/*}:completeUpgrade",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseCreateCluster:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1/{parent=projects/*/locations/*}/clusters",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1/projects/{project_id}/zones/{zone}/clusters",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseCreateNodePool:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1/{parent=projects/*/locations/*/clusters/*}/nodePools",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1/projects/{project_id}/zones/{zone}/clusters/{cluster_id}/nodePools",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseDeleteCluster:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "delete",
                    "uri": "/v1/{name=projects/*/locations/*/clusters/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1/projects/{project_id}/zones/{zone}/clusters/{cluster_id}",
                },
            ]
            return http_options

    class _BaseDeleteNodePool:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "delete",
                    "uri": "/v1/{name=projects/*/locations/*/clusters/*/nodePools/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1/projects/{project_id}/zones/{zone}/clusters/{cluster_id}/nodePools/{node_pool_id}",
                },
            ]
            return http_options

    class _BaseFetchClusterUpgradeInfo:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{name=projects/*/locations/*/clusters/*}:fetchClusterUpgradeInfo",
                },
                {
                    "method": "get",
                    "uri": "/v1/{name=projects/*/zones/*/clusters/*}:fetchClusterUpgradeInfo",
                },
            ]
            return http_options

    class _BaseFetchNodePoolUpgradeInfo:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{name=projects/*/locations/*/clusters/*/nodePools/*}:fetchNodePoolUpgradeInfo",
                },
                {
                    "method": "get",
                    "uri": "/v1/{name=projects/*/zones/*/clusters/*/nodePools/*}:fetchNodePoolUpgradeInfo",
                },
            ]
            return http_options

    class _BaseGetCluster:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{name=projects/*/locations/*/clusters/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1/projects/{project_id}/zones/{zone}/clusters/{cluster_id}",
                },
            ]
            return http_options

    class _BaseGetJSONWebKeys:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{parent=projects/*/locations/*/clusters/*}/jwks",
                },
            ]
            return http_options

    class _BaseGetNodePool:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{name=projects/*/locations/*/clusters/*/nodePools/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1/projects/{project_id}/zones/{zone}/clusters/{cluster_id}/nodePools/{node_pool_id}",
                },
            ]
            return http_options

    class _BaseGetOperation:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{name=projects/*/locations/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1/projects/{project_id}/zones/{zone}/operations/{operation_id}",
                },
            ]
            return http_options

    class _BaseGetServerConfig:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{name=projects/*/locations/*}/serverConfig",
                },
                {
                    "method": "get",
                    "uri": "/v1/projects/{project_id}/zones/{zone}/serverconfig",
                },
            ]
            return http_options

    class _BaseListClusters:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{parent=projects/*/locations/*}/clusters",
                },
                {
                    "method": "get",
                    "uri": "/v1/projects/{project_id}/zones/{zone}/clusters",
                },
            ]
            return http_options

    class _BaseListNodePools:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{parent=projects/*/locations/*/clusters/*}/nodePools",
                },
                {
                    "method": "get",
                    "uri": "/v1/projects/{project_id}/zones/{zone}/clusters/{cluster_id}/nodePools",
                },
            ]
            return http_options

    class _BaseListOperations:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{parent=projects/*/locations/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1/projects/{project_id}/zones/{zone}/operations",
                },
            ]
            return http_options

    class _BaseListUsableSubnetworks:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{parent=projects/*}/aggregated/usableSubnetworks",
                },
            ]
            return http_options

    class _BaseRollbackNodePoolUpgrade:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1/{name=projects/*/locations/*/clusters/*/nodePools/*}:rollback",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1/projects/{project_id}/zones/{zone}/clusters/{cluster_id}/nodePools/{node_pool_id}:rollback",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseSetAddonsConfig:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1/{name=projects/*/locations/*/clusters/*}:setAddons",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1/projects/{project_id}/zones/{zone}/clusters/{cluster_id}/addons",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseSetLabels:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1/{name=projects/*/locations/*/clusters/*}:setResourceLabels",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1/projects/{project_id}/zones/{zone}/clusters/{cluster_id}/resourceLabels",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseSetLegacyAbac:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1/{name=projects/*/locations/*/clusters/*}:setLegacyAbac",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1/projects/{project_id}/zones/{zone}/clusters/{cluster_id}/legacyAbac",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseSetLocations:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1/{name=projects/*/locations/*/clusters/*}:setLocations",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1/projects/{project_id}/zones/{zone}/clusters/{cluster_id}/locations",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseSetLoggingService:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1/{name=projects/*/locations/*/clusters/*}:setLogging",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1/projects/{project_id}/zones/{zone}/clusters/{cluster_id}/logging",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseSetMaintenancePolicy:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1/{name=projects/*/locations/*/clusters/*}:setMaintenancePolicy",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1/projects/{project_id}/zones/{zone}/clusters/{cluster_id}:setMaintenancePolicy",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseSetMasterAuth:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1/{name=projects/*/locations/*/clusters/*}:setMasterAuth",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1/projects/{project_id}/zones/{zone}/clusters/{cluster_id}:setMasterAuth",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseSetMonitoringService:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1/{name=projects/*/locations/*/clusters/*}:setMonitoring",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1/projects/{project_id}/zones/{zone}/clusters/{cluster_id}/monitoring",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseSetNetworkPolicy:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1/{name=projects/*/locations/*/clusters/*}:setNetworkPolicy",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1/projects/{project_id}/zones/{zone}/clusters/{cluster_id}:setNetworkPolicy",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseSetNodePoolAutoscaling:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1/{name=projects/*/locations/*/clusters/*/nodePools/*}:setAutoscaling",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1/projects/{project_id}/zones/{zone}/clusters/{cluster_id}/nodePools/{node_pool_id}/autoscaling",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseSetNodePoolManagement:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1/{name=projects/*/locations/*/clusters/*/nodePools/*}:setManagement",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1/projects/{project_id}/zones/{zone}/clusters/{cluster_id}/nodePools/{node_pool_id}/setManagement",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseSetNodePoolSize:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1/{name=projects/*/locations/*/clusters/*/nodePools/*}:setSize",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1/projects/{project_id}/zones/{zone}/clusters/{cluster_id}/nodePools/{node_pool_id}/setSize",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseStartIPRotation:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1/{name=projects/*/locations/*/clusters/*}:startIpRotation",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1/projects/{project_id}/zones/{zone}/clusters/{cluster_id}:startIpRotation",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseUpdateCluster:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "put",
                    "uri": "/v1/{name=projects/*/locations/*/clusters/*}",
                    "body": "*",
                },
                {
                    "method": "put",
                    "uri": "/v1/projects/{project_id}/zones/{zone}/clusters/{cluster_id}",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseUpdateMaster:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1/{name=projects/*/locations/*/clusters/*}:updateMaster",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1/projects/{project_id}/zones/{zone}/clusters/{cluster_id}/master",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseUpdateNodePool:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "put",
                    "uri": "/v1/{name=projects/*/locations/*/clusters/*/nodePools/*}",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1/projects/{project_id}/zones/{zone}/clusters/{cluster_id}/nodePools/{node_pool_id}/update",
                    "body": "*",
                },
            ]
            return http_options


__all__ = ("_BaseClusterManagerRestTransport",)
