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

from google.cloud.managedkafka_v1 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.managedkafka_v1.services.managed_kafka",
    "google.cloud.managedkafka_v1.services.managed_kafka_connect",
    "google.cloud.managedkafka_v1.types.managed_kafka",
    "google.cloud.managedkafka_v1.types.managed_kafka_connect",
    "google.cloud.managedkafka_v1.types.resources",
}


from .services.managed_kafka import ManagedKafkaAsyncClient, ManagedKafkaClient
from .services.managed_kafka_connect import (
    ManagedKafkaConnectAsyncClient,
    ManagedKafkaConnectClient,
)
from .types.managed_kafka import (
    AddAclEntryRequest,
    AddAclEntryResponse,
    CreateAclRequest,
    CreateClusterRequest,
    CreateTopicRequest,
    DeleteAclRequest,
    DeleteClusterRequest,
    DeleteConsumerGroupRequest,
    DeleteTopicRequest,
    GetAclRequest,
    GetClusterRequest,
    GetConsumerGroupRequest,
    GetTopicRequest,
    ListAclsRequest,
    ListAclsResponse,
    ListClustersRequest,
    ListClustersResponse,
    ListConsumerGroupsRequest,
    ListConsumerGroupsResponse,
    ListTopicsRequest,
    ListTopicsResponse,
    RemoveAclEntryRequest,
    RemoveAclEntryResponse,
    UpdateAclRequest,
    UpdateClusterRequest,
    UpdateConsumerGroupRequest,
    UpdateTopicRequest,
)
from .types.managed_kafka_connect import (
    CreateConnectClusterRequest,
    CreateConnectorRequest,
    DeleteConnectClusterRequest,
    DeleteConnectorRequest,
    GetConnectClusterRequest,
    GetConnectorRequest,
    ListConnectClustersRequest,
    ListConnectClustersResponse,
    ListConnectorsRequest,
    ListConnectorsResponse,
    PauseConnectorRequest,
    PauseConnectorResponse,
    RestartConnectorRequest,
    RestartConnectorResponse,
    ResumeConnectorRequest,
    ResumeConnectorResponse,
    StopConnectorRequest,
    StopConnectorResponse,
    UpdateConnectClusterRequest,
    UpdateConnectorRequest,
)
from .types.resources import (
    AccessConfig,
    Acl,
    AclEntry,
    CapacityConfig,
    Cluster,
    ConnectAccessConfig,
    ConnectCluster,
    ConnectGcpConfig,
    ConnectNetworkConfig,
    Connector,
    ConsumerGroup,
    ConsumerPartitionMetadata,
    ConsumerTopicMetadata,
    GcpConfig,
    NetworkConfig,
    OperationMetadata,
    RebalanceConfig,
    TaskRetryPolicy,
    TlsConfig,
    Topic,
    TrustConfig,
)

__all__ = (
    "ManagedKafkaAsyncClient",
    "ManagedKafkaConnectAsyncClient",
    "AccessConfig",
    "Acl",
    "AclEntry",
    "AddAclEntryRequest",
    "AddAclEntryResponse",
    "CapacityConfig",
    "Cluster",
    "ConnectAccessConfig",
    "ConnectCluster",
    "ConnectGcpConfig",
    "ConnectNetworkConfig",
    "Connector",
    "ConsumerGroup",
    "ConsumerPartitionMetadata",
    "ConsumerTopicMetadata",
    "CreateAclRequest",
    "CreateClusterRequest",
    "CreateConnectClusterRequest",
    "CreateConnectorRequest",
    "CreateTopicRequest",
    "DeleteAclRequest",
    "DeleteClusterRequest",
    "DeleteConnectClusterRequest",
    "DeleteConnectorRequest",
    "DeleteConsumerGroupRequest",
    "DeleteTopicRequest",
    "GcpConfig",
    "GetAclRequest",
    "GetClusterRequest",
    "GetConnectClusterRequest",
    "GetConnectorRequest",
    "GetConsumerGroupRequest",
    "GetTopicRequest",
    "ListAclsRequest",
    "ListAclsResponse",
    "ListClustersRequest",
    "ListClustersResponse",
    "ListConnectClustersRequest",
    "ListConnectClustersResponse",
    "ListConnectorsRequest",
    "ListConnectorsResponse",
    "ListConsumerGroupsRequest",
    "ListConsumerGroupsResponse",
    "ListTopicsRequest",
    "ListTopicsResponse",
    "ManagedKafkaClient",
    "ManagedKafkaConnectClient",
    "NetworkConfig",
    "OperationMetadata",
    "PauseConnectorRequest",
    "PauseConnectorResponse",
    "RebalanceConfig",
    "RemoveAclEntryRequest",
    "RemoveAclEntryResponse",
    "RestartConnectorRequest",
    "RestartConnectorResponse",
    "ResumeConnectorRequest",
    "ResumeConnectorResponse",
    "StopConnectorRequest",
    "StopConnectorResponse",
    "TaskRetryPolicy",
    "TlsConfig",
    "Topic",
    "TrustConfig",
    "UpdateAclRequest",
    "UpdateClusterRequest",
    "UpdateConnectClusterRequest",
    "UpdateConnectorRequest",
    "UpdateConsumerGroupRequest",
    "UpdateTopicRequest",
)

api_core.check_python_version("google.cloud.managedkafka_v1")
api_core.check_dependency_versions("google.cloud.managedkafka_v1")
