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
import google.api_core as api_core

from google.cloud.edgecontainer_v1 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.edgecontainer_v1.services.edge_container",
    "google.cloud.edgecontainer_v1.types.resources",
    "google.cloud.edgecontainer_v1.types.service",
}


from .services.edge_container import EdgeContainerAsyncClient, EdgeContainerClient
from .types.resources import (
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
from .types.service import (
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
    "EdgeContainerAsyncClient",
    "Authorization",
    "ChannelConfig",
    "Cluster",
    "ClusterNetworking",
    "ClusterUser",
    "ConfigData",
    "CreateClusterRequest",
    "CreateNodePoolRequest",
    "CreateVpnConnectionRequest",
    "DeleteClusterRequest",
    "DeleteNodePoolRequest",
    "DeleteVpnConnectionRequest",
    "EdgeContainerClient",
    "Fleet",
    "GenerateAccessTokenRequest",
    "GenerateAccessTokenResponse",
    "GenerateOfflineCredentialRequest",
    "GenerateOfflineCredentialResponse",
    "GetClusterRequest",
    "GetMachineRequest",
    "GetNodePoolRequest",
    "GetServerConfigRequest",
    "GetVpnConnectionRequest",
    "KmsKeyState",
    "ListClustersRequest",
    "ListClustersResponse",
    "ListMachinesRequest",
    "ListMachinesResponse",
    "ListNodePoolsRequest",
    "ListNodePoolsResponse",
    "ListVpnConnectionsRequest",
    "ListVpnConnectionsResponse",
    "LocationMetadata",
    "Machine",
    "MaintenanceExclusionWindow",
    "MaintenancePolicy",
    "MaintenanceWindow",
    "NodePool",
    "OperationMetadata",
    "Quota",
    "RecurringTimeWindow",
    "ResourceState",
    "ServerConfig",
    "TimeWindow",
    "UpdateClusterRequest",
    "UpdateNodePoolRequest",
    "UpgradeClusterRequest",
    "Version",
    "VpnConnection",
    "ZoneMetadata",
)

api_core.check_python_version("google.cloud.edgecontainer_v1")
api_core.check_dependency_versions("google.cloud.edgecontainer_v1")
