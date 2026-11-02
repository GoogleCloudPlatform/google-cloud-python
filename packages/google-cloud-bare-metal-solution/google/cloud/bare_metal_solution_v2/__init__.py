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

from google.cloud.bare_metal_solution_v2 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.bare_metal_solution_v2.services.bare_metal_solution",
    "google.cloud.bare_metal_solution_v2.types.baremetalsolution",
    "google.cloud.bare_metal_solution_v2.types.common",
    "google.cloud.bare_metal_solution_v2.types.instance",
    "google.cloud.bare_metal_solution_v2.types.lun",
    "google.cloud.bare_metal_solution_v2.types.network",
    "google.cloud.bare_metal_solution_v2.types.nfs_share",
    "google.cloud.bare_metal_solution_v2.types.osimage",
    "google.cloud.bare_metal_solution_v2.types.provisioning",
    "google.cloud.bare_metal_solution_v2.types.ssh_key",
    "google.cloud.bare_metal_solution_v2.types.volume",
    "google.cloud.bare_metal_solution_v2.types.volume_snapshot",
}


from .services.bare_metal_solution import (
    BareMetalSolutionAsyncClient,
    BareMetalSolutionClient,
)
from .types.baremetalsolution import OperationMetadata, ResetInstanceResponse
from .types.common import VolumePerformanceTier, WorkloadProfile
from .types.instance import (
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
from .types.lun import (
    EvictLunRequest,
    GetLunRequest,
    ListLunsRequest,
    ListLunsResponse,
    Lun,
)
from .types.network import (
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
from .types.nfs_share import (
    CreateNfsShareRequest,
    DeleteNfsShareRequest,
    GetNfsShareRequest,
    ListNfsSharesRequest,
    ListNfsSharesResponse,
    NfsShare,
    RenameNfsShareRequest,
    UpdateNfsShareRequest,
)
from .types.osimage import ListOSImagesRequest, ListOSImagesResponse, OSImage
from .types.provisioning import (
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
from .types.ssh_key import (
    CreateSSHKeyRequest,
    DeleteSSHKeyRequest,
    ListSSHKeysRequest,
    ListSSHKeysResponse,
    SSHKey,
)
from .types.volume import (
    EvictVolumeRequest,
    GetVolumeRequest,
    ListVolumesRequest,
    ListVolumesResponse,
    RenameVolumeRequest,
    ResizeVolumeRequest,
    UpdateVolumeRequest,
    Volume,
)
from .types.volume_snapshot import (
    CreateVolumeSnapshotRequest,
    DeleteVolumeSnapshotRequest,
    GetVolumeSnapshotRequest,
    ListVolumeSnapshotsRequest,
    ListVolumeSnapshotsResponse,
    RestoreVolumeSnapshotRequest,
    VolumeSnapshot,
)

__all__ = (
    "BareMetalSolutionAsyncClient",
    "BareMetalSolutionClient",
    "CreateNfsShareRequest",
    "CreateProvisioningConfigRequest",
    "CreateSSHKeyRequest",
    "CreateVolumeSnapshotRequest",
    "DeleteNfsShareRequest",
    "DeleteSSHKeyRequest",
    "DeleteVolumeSnapshotRequest",
    "DetachLunRequest",
    "DisableInteractiveSerialConsoleRequest",
    "DisableInteractiveSerialConsoleResponse",
    "EnableInteractiveSerialConsoleRequest",
    "EnableInteractiveSerialConsoleResponse",
    "EvictLunRequest",
    "EvictVolumeRequest",
    "GetInstanceRequest",
    "GetLunRequest",
    "GetNetworkRequest",
    "GetNfsShareRequest",
    "GetProvisioningConfigRequest",
    "GetVolumeRequest",
    "GetVolumeSnapshotRequest",
    "Instance",
    "InstanceConfig",
    "InstanceQuota",
    "ListInstancesRequest",
    "ListInstancesResponse",
    "ListLunsRequest",
    "ListLunsResponse",
    "ListNetworkUsageRequest",
    "ListNetworkUsageResponse",
    "ListNetworksRequest",
    "ListNetworksResponse",
    "ListNfsSharesRequest",
    "ListNfsSharesResponse",
    "ListOSImagesRequest",
    "ListOSImagesResponse",
    "ListProvisioningQuotasRequest",
    "ListProvisioningQuotasResponse",
    "ListSSHKeysRequest",
    "ListSSHKeysResponse",
    "ListVolumeSnapshotsRequest",
    "ListVolumeSnapshotsResponse",
    "ListVolumesRequest",
    "ListVolumesResponse",
    "LogicalInterface",
    "Lun",
    "Network",
    "NetworkAddressReservation",
    "NetworkConfig",
    "NetworkMountPoint",
    "NetworkUsage",
    "NfsShare",
    "OSImage",
    "OperationMetadata",
    "ProvisioningConfig",
    "ProvisioningQuota",
    "RenameInstanceRequest",
    "RenameNetworkRequest",
    "RenameNfsShareRequest",
    "RenameVolumeRequest",
    "ResetInstanceRequest",
    "ResetInstanceResponse",
    "ResizeVolumeRequest",
    "RestoreVolumeSnapshotRequest",
    "SSHKey",
    "ServerNetworkTemplate",
    "StartInstanceRequest",
    "StartInstanceResponse",
    "StopInstanceRequest",
    "StopInstanceResponse",
    "SubmitProvisioningConfigRequest",
    "SubmitProvisioningConfigResponse",
    "UpdateInstanceRequest",
    "UpdateNetworkRequest",
    "UpdateNfsShareRequest",
    "UpdateProvisioningConfigRequest",
    "UpdateVolumeRequest",
    "VRF",
    "Volume",
    "VolumeConfig",
    "VolumePerformanceTier",
    "VolumeSnapshot",
    "WorkloadProfile",
)

api_core.check_python_version("google.cloud.bare_metal_solution_v2")
api_core.check_dependency_versions("google.cloud.bare_metal_solution_v2")
