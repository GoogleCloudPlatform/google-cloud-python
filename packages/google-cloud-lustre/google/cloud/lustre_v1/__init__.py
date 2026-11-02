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

from google.cloud.lustre_v1 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.lustre_v1.services.lustre",
    "google.cloud.lustre_v1.types.directory_policy",
    "google.cloud.lustre_v1.types.instance",
    "google.cloud.lustre_v1.types.lustre",
    "google.cloud.lustre_v1.types.mirror",
    "google.cloud.lustre_v1.types.transfer",
}


from .services.lustre import LustreAsyncClient, LustreClient
from .types.directory_policy import (
    CreateDirectoryPolicyRequest,
    DeleteDirectoryPolicyRequest,
    DirectoryPolicy,
    GetDirectoryPolicyRequest,
    ListDirectoryPoliciesRequest,
    ListDirectoryPoliciesResponse,
)
from .types.instance import (
    AccessRulesOptions,
    CreateInstanceRequest,
    DeleteInstanceRequest,
    DynamicTierOptions,
    GetInstanceRequest,
    Instance,
    ListInstancesRequest,
    ListInstancesResponse,
    MaintenancePolicy,
    MaintenanceSchedule,
    OperationMetadata,
    RescheduleMaintenanceRequest,
    UpdateInstanceRequest,
)
from .types.mirror import (
    CreateMirrorMetadata,
    CreateMirrorRequest,
    DeleteMirrorRequest,
    GetMirrorRequest,
    ListMirrorsRequest,
    ListMirrorsResponse,
    Mirror,
    UpdateMirrorRequest,
)
from .types.transfer import (
    ErrorLogEntry,
    ErrorSummary,
    ExportDataMetadata,
    ExportDataRequest,
    ExportDataResponse,
    GcsPath,
    ImportDataMetadata,
    ImportDataRequest,
    ImportDataResponse,
    LustrePath,
    TransferCounters,
    TransferOperationMetadata,
    TransferType,
)

__all__ = (
    "LustreAsyncClient",
    "AccessRulesOptions",
    "CreateDirectoryPolicyRequest",
    "CreateInstanceRequest",
    "CreateMirrorMetadata",
    "CreateMirrorRequest",
    "DeleteDirectoryPolicyRequest",
    "DeleteInstanceRequest",
    "DeleteMirrorRequest",
    "DirectoryPolicy",
    "DynamicTierOptions",
    "ErrorLogEntry",
    "ErrorSummary",
    "ExportDataMetadata",
    "ExportDataRequest",
    "ExportDataResponse",
    "GcsPath",
    "GetDirectoryPolicyRequest",
    "GetInstanceRequest",
    "GetMirrorRequest",
    "ImportDataMetadata",
    "ImportDataRequest",
    "ImportDataResponse",
    "Instance",
    "ListDirectoryPoliciesRequest",
    "ListDirectoryPoliciesResponse",
    "ListInstancesRequest",
    "ListInstancesResponse",
    "ListMirrorsRequest",
    "ListMirrorsResponse",
    "LustreClient",
    "LustrePath",
    "MaintenancePolicy",
    "MaintenanceSchedule",
    "Mirror",
    "OperationMetadata",
    "RescheduleMaintenanceRequest",
    "TransferCounters",
    "TransferOperationMetadata",
    "TransferType",
    "UpdateInstanceRequest",
    "UpdateMirrorRequest",
)

api_core.check_python_version("google.cloud.lustre_v1")
api_core.check_dependency_versions("google.cloud.lustre_v1")
