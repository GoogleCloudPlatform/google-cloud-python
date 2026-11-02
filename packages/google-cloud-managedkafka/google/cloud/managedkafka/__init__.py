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
from google.cloud.managedkafka import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.managedkafka_v1.services.managed_kafka.async_client import (
    ManagedKafkaAsyncClient,
)
from google.cloud.managedkafka_v1.services.managed_kafka.client import (
    ManagedKafkaClient,
)
from google.cloud.managedkafka_v1.services.managed_kafka_connect.async_client import (
    ManagedKafkaConnectAsyncClient,
)
from google.cloud.managedkafka_v1.services.managed_kafka_connect.client import (
    ManagedKafkaConnectClient,
)
from google.cloud.managedkafka_v1.types.managed_kafka import (
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
from google.cloud.managedkafka_v1.types.managed_kafka_connect import (
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
from google.cloud.managedkafka_v1.types.resources import (
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
    "ManagedKafkaClient",
    "ManagedKafkaAsyncClient",
    "ManagedKafkaConnectClient",
    "ManagedKafkaConnectAsyncClient",
    "AddAclEntryRequest",
    "AddAclEntryResponse",
    "CreateAclRequest",
    "CreateClusterRequest",
    "CreateTopicRequest",
    "DeleteAclRequest",
    "DeleteClusterRequest",
    "DeleteConsumerGroupRequest",
    "DeleteTopicRequest",
    "GetAclRequest",
    "GetClusterRequest",
    "GetConsumerGroupRequest",
    "GetTopicRequest",
    "ListAclsRequest",
    "ListAclsResponse",
    "ListClustersRequest",
    "ListClustersResponse",
    "ListConsumerGroupsRequest",
    "ListConsumerGroupsResponse",
    "ListTopicsRequest",
    "ListTopicsResponse",
    "RemoveAclEntryRequest",
    "RemoveAclEntryResponse",
    "UpdateAclRequest",
    "UpdateClusterRequest",
    "UpdateConsumerGroupRequest",
    "UpdateTopicRequest",
    "CreateConnectClusterRequest",
    "CreateConnectorRequest",
    "DeleteConnectClusterRequest",
    "DeleteConnectorRequest",
    "GetConnectClusterRequest",
    "GetConnectorRequest",
    "ListConnectClustersRequest",
    "ListConnectClustersResponse",
    "ListConnectorsRequest",
    "ListConnectorsResponse",
    "PauseConnectorRequest",
    "PauseConnectorResponse",
    "RestartConnectorRequest",
    "RestartConnectorResponse",
    "ResumeConnectorRequest",
    "ResumeConnectorResponse",
    "StopConnectorRequest",
    "StopConnectorResponse",
    "UpdateConnectClusterRequest",
    "UpdateConnectorRequest",
    "AccessConfig",
    "Acl",
    "AclEntry",
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
    "GcpConfig",
    "NetworkConfig",
    "OperationMetadata",
    "RebalanceConfig",
    "TaskRetryPolicy",
    "TlsConfig",
    "Topic",
    "TrustConfig",
)
