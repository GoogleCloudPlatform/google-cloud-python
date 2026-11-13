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

from google.cloud.network_management_v1 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.network_management_v1.services.organization_vpc_flow_logs_service",
    "google.cloud.network_management_v1.services.reachability_service",
    "google.cloud.network_management_v1.services.vpc_flow_logs_service",
    "google.cloud.network_management_v1.types.connectivity_test",
    "google.cloud.network_management_v1.types.reachability",
    "google.cloud.network_management_v1.types.trace",
    "google.cloud.network_management_v1.types.vpc_flow_logs",
    "google.cloud.network_management_v1.types.vpc_flow_logs_config",
}


from .services.organization_vpc_flow_logs_service import (
    OrganizationVpcFlowLogsServiceAsyncClient,
    OrganizationVpcFlowLogsServiceClient,
)
from .services.reachability_service import (
    ReachabilityServiceAsyncClient,
    ReachabilityServiceClient,
)
from .services.vpc_flow_logs_service import (
    VpcFlowLogsServiceAsyncClient,
    VpcFlowLogsServiceClient,
)
from .types.connectivity_test import (
    ConnectivityTest,
    Endpoint,
    LatencyDistribution,
    LatencyPercentile,
    ProbingDetails,
    ReachabilityDetails,
)
from .types.reachability import (
    CreateConnectivityTestRequest,
    DeleteConnectivityTestRequest,
    GetConnectivityTestRequest,
    ListConnectivityTestsRequest,
    ListConnectivityTestsResponse,
    OperationMetadata,
    RerunConnectivityTestRequest,
    UpdateConnectivityTestRequest,
)
from .types.trace import (
    AbortInfo,
    AppEngineVersionInfo,
    CloudFunctionInfo,
    CloudRunJobInfo,
    CloudRunRevisionInfo,
    CloudSQLInstanceInfo,
    DeliverInfo,
    DirectVpcEgressConnectionInfo,
    DropInfo,
    EndpointInfo,
    FirewallInfo,
    ForwardInfo,
    ForwardingRuleInfo,
    GKEMasterInfo,
    GkeNetworkPolicyInfo,
    GkeNetworkPolicySkippedInfo,
    GkePodInfo,
    GoogleServiceInfo,
    HybridSubnetInfo,
    InstanceInfo,
    InterconnectAttachmentInfo,
    IpMasqueradingSkippedInfo,
    LoadBalancerBackend,
    LoadBalancerBackendInfo,
    LoadBalancerInfo,
    LoadBalancerType,
    NatInfo,
    NetworkInfo,
    NgfwPacketInspectionInfo,
    PrivateConnectionInfo,
    ProxyConnectionInfo,
    RedisClusterInfo,
    RedisInstanceInfo,
    RouteInfo,
    ServerlessExternalConnectionInfo,
    ServerlessNegInfo,
    Step,
    StorageBucketInfo,
    Trace,
    VpcConnectorInfo,
    VpnGatewayInfo,
    VpnTunnelInfo,
)
from .types.vpc_flow_logs import (
    CreateVpcFlowLogsConfigRequest,
    DeleteVpcFlowLogsConfigRequest,
    GetVpcFlowLogsConfigRequest,
    ListVpcFlowLogsConfigsRequest,
    ListVpcFlowLogsConfigsResponse,
    QueryOrgVpcFlowLogsConfigsRequest,
    QueryOrgVpcFlowLogsConfigsResponse,
    ShowEffectiveFlowLogsConfigsRequest,
    ShowEffectiveFlowLogsConfigsResponse,
    UpdateVpcFlowLogsConfigRequest,
)
from .types.vpc_flow_logs_config import EffectiveVpcFlowLogsConfig, VpcFlowLogsConfig

__all__ = (
    "OrganizationVpcFlowLogsServiceAsyncClient",
    "ReachabilityServiceAsyncClient",
    "VpcFlowLogsServiceAsyncClient",
    "AbortInfo",
    "AppEngineVersionInfo",
    "CloudFunctionInfo",
    "CloudRunJobInfo",
    "CloudRunRevisionInfo",
    "CloudSQLInstanceInfo",
    "ConnectivityTest",
    "CreateConnectivityTestRequest",
    "CreateVpcFlowLogsConfigRequest",
    "DeleteConnectivityTestRequest",
    "DeleteVpcFlowLogsConfigRequest",
    "DeliverInfo",
    "DirectVpcEgressConnectionInfo",
    "DropInfo",
    "EffectiveVpcFlowLogsConfig",
    "Endpoint",
    "EndpointInfo",
    "FirewallInfo",
    "ForwardInfo",
    "ForwardingRuleInfo",
    "GKEMasterInfo",
    "GetConnectivityTestRequest",
    "GetVpcFlowLogsConfigRequest",
    "GkeNetworkPolicyInfo",
    "GkeNetworkPolicySkippedInfo",
    "GkePodInfo",
    "GoogleServiceInfo",
    "HybridSubnetInfo",
    "InstanceInfo",
    "InterconnectAttachmentInfo",
    "IpMasqueradingSkippedInfo",
    "LatencyDistribution",
    "LatencyPercentile",
    "ListConnectivityTestsRequest",
    "ListConnectivityTestsResponse",
    "ListVpcFlowLogsConfigsRequest",
    "ListVpcFlowLogsConfigsResponse",
    "LoadBalancerBackend",
    "LoadBalancerBackendInfo",
    "LoadBalancerInfo",
    "LoadBalancerType",
    "NatInfo",
    "NetworkInfo",
    "NgfwPacketInspectionInfo",
    "OperationMetadata",
    "OrganizationVpcFlowLogsServiceClient",
    "PrivateConnectionInfo",
    "ProbingDetails",
    "ProxyConnectionInfo",
    "QueryOrgVpcFlowLogsConfigsRequest",
    "QueryOrgVpcFlowLogsConfigsResponse",
    "ReachabilityDetails",
    "ReachabilityServiceClient",
    "RedisClusterInfo",
    "RedisInstanceInfo",
    "RerunConnectivityTestRequest",
    "RouteInfo",
    "ServerlessExternalConnectionInfo",
    "ServerlessNegInfo",
    "ShowEffectiveFlowLogsConfigsRequest",
    "ShowEffectiveFlowLogsConfigsResponse",
    "Step",
    "StorageBucketInfo",
    "Trace",
    "UpdateConnectivityTestRequest",
    "UpdateVpcFlowLogsConfigRequest",
    "VpcConnectorInfo",
    "VpcFlowLogsConfig",
    "VpcFlowLogsServiceClient",
    "VpnGatewayInfo",
    "VpnTunnelInfo",
)

api_core.check_python_version("google.cloud.network_management_v1")
api_core.check_dependency_versions("google.cloud.network_management_v1")
