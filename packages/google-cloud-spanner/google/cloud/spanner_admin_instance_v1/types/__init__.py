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
from .common import (
    FulfillmentPeriod,
    OperationProgress,
    ReplicaSelection,
)
from .spanner_instance_admin import (
    AutoscalingConfig,
    CreateInstanceConfigMetadata,
    CreateInstanceConfigRequest,
    CreateInstanceMetadata,
    CreateInstancePartitionMetadata,
    CreateInstancePartitionRequest,
    CreateInstanceRequest,
    DeleteInstanceConfigRequest,
    DeleteInstancePartitionRequest,
    DeleteInstanceRequest,
    FreeInstanceMetadata,
    GetInstanceConfigRequest,
    GetInstancePartitionRequest,
    GetInstanceRequest,
    Instance,
    InstanceConfig,
    InstancePartition,
    ListInstanceConfigOperationsRequest,
    ListInstanceConfigOperationsResponse,
    ListInstanceConfigsRequest,
    ListInstanceConfigsResponse,
    ListInstancePartitionOperationsRequest,
    ListInstancePartitionOperationsResponse,
    ListInstancePartitionsRequest,
    ListInstancePartitionsResponse,
    ListInstancesRequest,
    ListInstancesResponse,
    MoveInstanceMetadata,
    MoveInstanceRequest,
    MoveInstanceResponse,
    ReplicaComputeCapacity,
    ReplicaInfo,
    UpdateInstanceConfigMetadata,
    UpdateInstanceConfigRequest,
    UpdateInstanceMetadata,
    UpdateInstancePartitionMetadata,
    UpdateInstancePartitionRequest,
    UpdateInstanceRequest,
)

__all__ = (
    "OperationProgress",
    "ReplicaSelection",
    "FulfillmentPeriod",
    "AutoscalingConfig",
    "CreateInstanceConfigMetadata",
    "CreateInstanceConfigRequest",
    "CreateInstanceMetadata",
    "CreateInstancePartitionMetadata",
    "CreateInstancePartitionRequest",
    "CreateInstanceRequest",
    "DeleteInstanceConfigRequest",
    "DeleteInstancePartitionRequest",
    "DeleteInstanceRequest",
    "FreeInstanceMetadata",
    "GetInstanceConfigRequest",
    "GetInstancePartitionRequest",
    "GetInstanceRequest",
    "Instance",
    "InstanceConfig",
    "InstancePartition",
    "ListInstanceConfigOperationsRequest",
    "ListInstanceConfigOperationsResponse",
    "ListInstanceConfigsRequest",
    "ListInstanceConfigsResponse",
    "ListInstancePartitionOperationsRequest",
    "ListInstancePartitionOperationsResponse",
    "ListInstancePartitionsRequest",
    "ListInstancePartitionsResponse",
    "ListInstancesRequest",
    "ListInstancesResponse",
    "MoveInstanceMetadata",
    "MoveInstanceRequest",
    "MoveInstanceResponse",
    "ReplicaComputeCapacity",
    "ReplicaInfo",
    "UpdateInstanceConfigMetadata",
    "UpdateInstanceConfigRequest",
    "UpdateInstanceMetadata",
    "UpdateInstancePartitionMetadata",
    "UpdateInstancePartitionRequest",
    "UpdateInstanceRequest",
)
