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
from google.cloud.edgecontainer import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.edgecontainer_v1.services.edge_container.async_client import (
    EdgeContainerAsyncClient,
)
from google.cloud.edgecontainer_v1.services.edge_container.client import (
    EdgeContainerClient,
)
from google.cloud.edgecontainer_v1.types.resources import (
    Authorization,
    ChannelConfig,
    Cluster,
    ClusterNetworking,
    ClusterUser,
    ConfigData,
    Fleet,
    KmsKeyState,
    LocationMetadata,
    Machine,
    MaintenanceExclusionWindow,
    MaintenancePolicy,
    MaintenanceWindow,
    NodePool,
    Quota,
    RecurringTimeWindow,
    ResourceState,
    ServerConfig,
    TimeWindow,
    Version,
    VpnConnection,
    ZoneMetadata,
)
from google.cloud.edgecontainer_v1.types.service import (
    CreateClusterRequest,
    CreateNodePoolRequest,
    CreateVpnConnectionRequest,
    DeleteClusterRequest,
    DeleteNodePoolRequest,
    DeleteVpnConnectionRequest,
    GenerateAccessTokenRequest,
    GenerateAccessTokenResponse,
    GenerateOfflineCredentialRequest,
    GenerateOfflineCredentialResponse,
    GetClusterRequest,
    GetMachineRequest,
    GetNodePoolRequest,
    GetServerConfigRequest,
    GetVpnConnectionRequest,
    ListClustersRequest,
    ListClustersResponse,
    ListMachinesRequest,
    ListMachinesResponse,
    ListNodePoolsRequest,
    ListNodePoolsResponse,
    ListVpnConnectionsRequest,
    ListVpnConnectionsResponse,
    OperationMetadata,
    UpdateClusterRequest,
    UpdateNodePoolRequest,
    UpgradeClusterRequest,
)

__all__ = (
    "EdgeContainerClient",
    "EdgeContainerAsyncClient",
    "Authorization",
    "ChannelConfig",
    "Cluster",
    "ClusterNetworking",
    "ClusterUser",
    "ConfigData",
    "Fleet",
    "LocationMetadata",
    "Machine",
    "MaintenanceExclusionWindow",
    "MaintenancePolicy",
    "MaintenanceWindow",
    "NodePool",
    "Quota",
    "RecurringTimeWindow",
    "ServerConfig",
    "TimeWindow",
    "Version",
    "VpnConnection",
    "ZoneMetadata",
    "KmsKeyState",
    "ResourceState",
    "CreateClusterRequest",
    "CreateNodePoolRequest",
    "CreateVpnConnectionRequest",
    "DeleteClusterRequest",
    "DeleteNodePoolRequest",
    "DeleteVpnConnectionRequest",
    "GenerateAccessTokenRequest",
    "GenerateAccessTokenResponse",
    "GenerateOfflineCredentialRequest",
    "GenerateOfflineCredentialResponse",
    "GetClusterRequest",
    "GetMachineRequest",
    "GetNodePoolRequest",
    "GetServerConfigRequest",
    "GetVpnConnectionRequest",
    "ListClustersRequest",
    "ListClustersResponse",
    "ListMachinesRequest",
    "ListMachinesResponse",
    "ListNodePoolsRequest",
    "ListNodePoolsResponse",
    "ListVpnConnectionsRequest",
    "ListVpnConnectionsResponse",
    "OperationMetadata",
    "UpdateClusterRequest",
    "UpdateNodePoolRequest",
    "UpgradeClusterRequest",
)
