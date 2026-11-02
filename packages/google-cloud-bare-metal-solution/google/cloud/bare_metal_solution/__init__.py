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
from google.cloud.bare_metal_solution import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.bare_metal_solution_v2.services.bare_metal_solution.async_client import (
    BareMetalSolutionAsyncClient,
)
from google.cloud.bare_metal_solution_v2.services.bare_metal_solution.client import (
    BareMetalSolutionClient,
)
from google.cloud.bare_metal_solution_v2.types.baremetalsolution import (
    OperationMetadata,
    ResetInstanceResponse,
)
from google.cloud.bare_metal_solution_v2.types.common import (
    VolumePerformanceTier,
    WorkloadProfile,
)
from google.cloud.bare_metal_solution_v2.types.instance import (
    DetachLunRequest,
    DisableInteractiveSerialConsoleRequest,
    DisableInteractiveSerialConsoleResponse,
    EnableInteractiveSerialConsoleRequest,
    EnableInteractiveSerialConsoleResponse,
    GetInstanceRequest,
    Instance,
    ListInstancesRequest,
    ListInstancesResponse,
    RenameInstanceRequest,
    ResetInstanceRequest,
    ServerNetworkTemplate,
    StartInstanceRequest,
    StartInstanceResponse,
    StopInstanceRequest,
    StopInstanceResponse,
    UpdateInstanceRequest,
)
from google.cloud.bare_metal_solution_v2.types.lun import (
    EvictLunRequest,
    GetLunRequest,
    ListLunsRequest,
    ListLunsResponse,
    Lun,
)
from google.cloud.bare_metal_solution_v2.types.network import (
    VRF,
    GetNetworkRequest,
    ListNetworksRequest,
    ListNetworksResponse,
    ListNetworkUsageRequest,
    ListNetworkUsageResponse,
    LogicalInterface,
    Network,
    NetworkAddressReservation,
    NetworkMountPoint,
    NetworkUsage,
    RenameNetworkRequest,
    UpdateNetworkRequest,
)
from google.cloud.bare_metal_solution_v2.types.nfs_share import (
    CreateNfsShareRequest,
    DeleteNfsShareRequest,
    GetNfsShareRequest,
    ListNfsSharesRequest,
    ListNfsSharesResponse,
    NfsShare,
    RenameNfsShareRequest,
    UpdateNfsShareRequest,
)
from google.cloud.bare_metal_solution_v2.types.osimage import (
    ListOSImagesRequest,
    ListOSImagesResponse,
    OSImage,
)
from google.cloud.bare_metal_solution_v2.types.provisioning import (
    CreateProvisioningConfigRequest,
    GetProvisioningConfigRequest,
    InstanceConfig,
    InstanceQuota,
    ListProvisioningQuotasRequest,
    ListProvisioningQuotasResponse,
    NetworkConfig,
    ProvisioningConfig,
    ProvisioningQuota,
    SubmitProvisioningConfigRequest,
    SubmitProvisioningConfigResponse,
    UpdateProvisioningConfigRequest,
    VolumeConfig,
)
from google.cloud.bare_metal_solution_v2.types.ssh_key import (
    CreateSSHKeyRequest,
    DeleteSSHKeyRequest,
    ListSSHKeysRequest,
    ListSSHKeysResponse,
    SSHKey,
)
from google.cloud.bare_metal_solution_v2.types.volume import (
    EvictVolumeRequest,
    GetVolumeRequest,
    ListVolumesRequest,
    ListVolumesResponse,
    RenameVolumeRequest,
    ResizeVolumeRequest,
    UpdateVolumeRequest,
    Volume,
)
from google.cloud.bare_metal_solution_v2.types.volume_snapshot import (
    CreateVolumeSnapshotRequest,
    DeleteVolumeSnapshotRequest,
    GetVolumeSnapshotRequest,
    ListVolumeSnapshotsRequest,
    ListVolumeSnapshotsResponse,
    RestoreVolumeSnapshotRequest,
    VolumeSnapshot,
)

__all__ = (
    "BareMetalSolutionClient",
    "BareMetalSolutionAsyncClient",
    "OperationMetadata",
    "ResetInstanceResponse",
    "VolumePerformanceTier",
    "WorkloadProfile",
    "DetachLunRequest",
    "DisableInteractiveSerialConsoleRequest",
    "DisableInteractiveSerialConsoleResponse",
    "EnableInteractiveSerialConsoleRequest",
    "EnableInteractiveSerialConsoleResponse",
    "GetInstanceRequest",
    "Instance",
    "ListInstancesRequest",
    "ListInstancesResponse",
    "RenameInstanceRequest",
    "ResetInstanceRequest",
    "ServerNetworkTemplate",
    "StartInstanceRequest",
    "StartInstanceResponse",
    "StopInstanceRequest",
    "StopInstanceResponse",
    "UpdateInstanceRequest",
    "EvictLunRequest",
    "GetLunRequest",
    "ListLunsRequest",
    "ListLunsResponse",
    "Lun",
    "GetNetworkRequest",
    "ListNetworksRequest",
    "ListNetworksResponse",
    "ListNetworkUsageRequest",
    "ListNetworkUsageResponse",
    "LogicalInterface",
    "Network",
    "NetworkAddressReservation",
    "NetworkMountPoint",
    "NetworkUsage",
    "RenameNetworkRequest",
    "UpdateNetworkRequest",
    "VRF",
    "CreateNfsShareRequest",
    "DeleteNfsShareRequest",
    "GetNfsShareRequest",
    "ListNfsSharesRequest",
    "ListNfsSharesResponse",
    "NfsShare",
    "RenameNfsShareRequest",
    "UpdateNfsShareRequest",
    "ListOSImagesRequest",
    "ListOSImagesResponse",
    "OSImage",
    "CreateProvisioningConfigRequest",
    "GetProvisioningConfigRequest",
    "InstanceConfig",
    "InstanceQuota",
    "ListProvisioningQuotasRequest",
    "ListProvisioningQuotasResponse",
    "NetworkConfig",
    "ProvisioningConfig",
    "ProvisioningQuota",
    "SubmitProvisioningConfigRequest",
    "SubmitProvisioningConfigResponse",
    "UpdateProvisioningConfigRequest",
    "VolumeConfig",
    "CreateSSHKeyRequest",
    "DeleteSSHKeyRequest",
    "ListSSHKeysRequest",
    "ListSSHKeysResponse",
    "SSHKey",
    "EvictVolumeRequest",
    "GetVolumeRequest",
    "ListVolumesRequest",
    "ListVolumesResponse",
    "RenameVolumeRequest",
    "ResizeVolumeRequest",
    "UpdateVolumeRequest",
    "Volume",
    "CreateVolumeSnapshotRequest",
    "DeleteVolumeSnapshotRequest",
    "GetVolumeSnapshotRequest",
    "ListVolumeSnapshotsRequest",
    "ListVolumeSnapshotsResponse",
    "RestoreVolumeSnapshotRequest",
    "VolumeSnapshot",
)
