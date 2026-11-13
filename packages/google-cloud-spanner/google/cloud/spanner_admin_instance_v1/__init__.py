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

from google.cloud.spanner_admin_instance_v1 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.spanner_admin_instance_v1.services.instance_admin",
    "google.cloud.spanner_admin_instance_v1.types.common",
    "google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin",
}


from .services.instance_admin import InstanceAdminAsyncClient, InstanceAdminClient
from .types.common import FulfillmentPeriod, OperationProgress, ReplicaSelection
from .types.spanner_instance_admin import (
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
    "InstanceAdminAsyncClient",
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
    "FulfillmentPeriod",
    "GetInstanceConfigRequest",
    "GetInstancePartitionRequest",
    "GetInstanceRequest",
    "Instance",
    "InstanceAdminClient",
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
    "OperationProgress",
    "ReplicaComputeCapacity",
    "ReplicaInfo",
    "ReplicaSelection",
    "UpdateInstanceConfigMetadata",
    "UpdateInstanceConfigRequest",
    "UpdateInstanceMetadata",
    "UpdateInstancePartitionMetadata",
    "UpdateInstancePartitionRequest",
    "UpdateInstanceRequest",
)

api_core.check_python_version("google.cloud.spanner_admin_instance_v1")
api_core.check_dependency_versions("google.cloud.spanner_admin_instance_v1")
