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
from google.cloud.notebooks import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.notebooks_v1.services.managed_notebook_service.async_client import (
    ManagedNotebookServiceAsyncClient,
)
from google.cloud.notebooks_v1.services.managed_notebook_service.client import (
    ManagedNotebookServiceClient,
)
from google.cloud.notebooks_v1.services.notebook_service.async_client import (
    NotebookServiceAsyncClient,
)
from google.cloud.notebooks_v1.services.notebook_service.client import (
    NotebookServiceClient,
)
from google.cloud.notebooks_v1.types.diagnostic_config import DiagnosticConfig
from google.cloud.notebooks_v1.types.environment import (
    ContainerImage,
    Environment,
    VmImage,
)
from google.cloud.notebooks_v1.types.event import Event
from google.cloud.notebooks_v1.types.execution import Execution, ExecutionTemplate
from google.cloud.notebooks_v1.types.instance import Instance, ReservationAffinity
from google.cloud.notebooks_v1.types.instance_config import InstanceConfig
from google.cloud.notebooks_v1.types.managed_service import (
    CreateRuntimeRequest,
    DeleteRuntimeRequest,
    DiagnoseRuntimeRequest,
    GetRuntimeRequest,
    ListRuntimesRequest,
    ListRuntimesResponse,
    RefreshRuntimeTokenInternalRequest,
    RefreshRuntimeTokenInternalResponse,
    ReportRuntimeEventRequest,
    ResetRuntimeRequest,
    StartRuntimeRequest,
    StopRuntimeRequest,
    SwitchRuntimeRequest,
    UpdateRuntimeRequest,
    UpgradeRuntimeRequest,
)
from google.cloud.notebooks_v1.types.runtime import (
    EncryptionConfig,
    LocalDisk,
    LocalDiskInitializeParams,
    Runtime,
    RuntimeAcceleratorConfig,
    RuntimeAccessConfig,
    RuntimeMetrics,
    RuntimeShieldedInstanceConfig,
    RuntimeSoftwareConfig,
    VirtualMachine,
    VirtualMachineConfig,
)
from google.cloud.notebooks_v1.types.schedule import Schedule
from google.cloud.notebooks_v1.types.service import (
    CreateEnvironmentRequest,
    CreateExecutionRequest,
    CreateInstanceRequest,
    CreateScheduleRequest,
    DeleteEnvironmentRequest,
    DeleteExecutionRequest,
    DeleteInstanceRequest,
    DeleteScheduleRequest,
    DiagnoseInstanceRequest,
    GetEnvironmentRequest,
    GetExecutionRequest,
    GetInstanceHealthRequest,
    GetInstanceHealthResponse,
    GetInstanceRequest,
    GetScheduleRequest,
    IsInstanceUpgradeableRequest,
    IsInstanceUpgradeableResponse,
    ListEnvironmentsRequest,
    ListEnvironmentsResponse,
    ListExecutionsRequest,
    ListExecutionsResponse,
    ListInstancesRequest,
    ListInstancesResponse,
    ListSchedulesRequest,
    ListSchedulesResponse,
    OperationMetadata,
    RegisterInstanceRequest,
    ReportInstanceInfoRequest,
    ResetInstanceRequest,
    RollbackInstanceRequest,
    SetInstanceAcceleratorRequest,
    SetInstanceLabelsRequest,
    SetInstanceMachineTypeRequest,
    StartInstanceRequest,
    StopInstanceRequest,
    TriggerScheduleRequest,
    UpdateInstanceConfigRequest,
    UpdateInstanceMetadataItemsRequest,
    UpdateInstanceMetadataItemsResponse,
    UpdateShieldedInstanceConfigRequest,
    UpgradeInstanceInternalRequest,
    UpgradeInstanceRequest,
    UpgradeType,
)

__all__ = (
    "ManagedNotebookServiceClient",
    "ManagedNotebookServiceAsyncClient",
    "NotebookServiceClient",
    "NotebookServiceAsyncClient",
    "DiagnosticConfig",
    "ContainerImage",
    "Environment",
    "VmImage",
    "Event",
    "Execution",
    "ExecutionTemplate",
    "Instance",
    "ReservationAffinity",
    "InstanceConfig",
    "CreateRuntimeRequest",
    "DeleteRuntimeRequest",
    "DiagnoseRuntimeRequest",
    "GetRuntimeRequest",
    "ListRuntimesRequest",
    "ListRuntimesResponse",
    "RefreshRuntimeTokenInternalRequest",
    "RefreshRuntimeTokenInternalResponse",
    "ReportRuntimeEventRequest",
    "ResetRuntimeRequest",
    "StartRuntimeRequest",
    "StopRuntimeRequest",
    "SwitchRuntimeRequest",
    "UpdateRuntimeRequest",
    "UpgradeRuntimeRequest",
    "EncryptionConfig",
    "LocalDisk",
    "LocalDiskInitializeParams",
    "Runtime",
    "RuntimeAcceleratorConfig",
    "RuntimeAccessConfig",
    "RuntimeMetrics",
    "RuntimeShieldedInstanceConfig",
    "RuntimeSoftwareConfig",
    "VirtualMachine",
    "VirtualMachineConfig",
    "Schedule",
    "CreateEnvironmentRequest",
    "CreateExecutionRequest",
    "CreateInstanceRequest",
    "CreateScheduleRequest",
    "DeleteEnvironmentRequest",
    "DeleteExecutionRequest",
    "DeleteInstanceRequest",
    "DeleteScheduleRequest",
    "DiagnoseInstanceRequest",
    "GetEnvironmentRequest",
    "GetExecutionRequest",
    "GetInstanceHealthRequest",
    "GetInstanceHealthResponse",
    "GetInstanceRequest",
    "GetScheduleRequest",
    "IsInstanceUpgradeableRequest",
    "IsInstanceUpgradeableResponse",
    "ListEnvironmentsRequest",
    "ListEnvironmentsResponse",
    "ListExecutionsRequest",
    "ListExecutionsResponse",
    "ListInstancesRequest",
    "ListInstancesResponse",
    "ListSchedulesRequest",
    "ListSchedulesResponse",
    "OperationMetadata",
    "RegisterInstanceRequest",
    "ReportInstanceInfoRequest",
    "ResetInstanceRequest",
    "RollbackInstanceRequest",
    "SetInstanceAcceleratorRequest",
    "SetInstanceLabelsRequest",
    "SetInstanceMachineTypeRequest",
    "StartInstanceRequest",
    "StopInstanceRequest",
    "TriggerScheduleRequest",
    "UpdateInstanceConfigRequest",
    "UpdateInstanceMetadataItemsRequest",
    "UpdateInstanceMetadataItemsResponse",
    "UpdateShieldedInstanceConfigRequest",
    "UpgradeInstanceInternalRequest",
    "UpgradeInstanceRequest",
    "UpgradeType",
)
