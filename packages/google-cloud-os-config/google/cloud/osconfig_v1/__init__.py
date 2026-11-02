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

from google.cloud.osconfig_v1 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.osconfig_v1.services.os_config_service",
    "google.cloud.osconfig_v1.services.os_config_zonal_service",
    "google.cloud.osconfig_v1.types.inventory",
    "google.cloud.osconfig_v1.types.os_policy",
    "google.cloud.osconfig_v1.types.os_policy_assignment_reports",
    "google.cloud.osconfig_v1.types.os_policy_assignments",
    "google.cloud.osconfig_v1.types.osconfig_common",
    "google.cloud.osconfig_v1.types.osconfig_service",
    "google.cloud.osconfig_v1.types.osconfig_zonal_service",
    "google.cloud.osconfig_v1.types.patch_deployments",
    "google.cloud.osconfig_v1.types.patch_jobs",
    "google.cloud.osconfig_v1.types.vulnerability",
}


from .services.os_config_service import (
    OsConfigServiceAsyncClient,
    OsConfigServiceClient,
)
from .services.os_config_zonal_service import (
    OsConfigZonalServiceAsyncClient,
    OsConfigZonalServiceClient,
)
from .types.inventory import (
    GetInventoryRequest,
    Inventory,
    InventoryView,
    ListInventoriesRequest,
    ListInventoriesResponse,
)
from .types.os_policy import OSPolicy
from .types.os_policy_assignment_reports import (
    GetOSPolicyAssignmentReportRequest,
    ListOSPolicyAssignmentReportsRequest,
    ListOSPolicyAssignmentReportsResponse,
    OSPolicyAssignmentReport,
)
from .types.os_policy_assignments import (
    CreateOSPolicyAssignmentRequest,
    DeleteOSPolicyAssignmentRequest,
    GetOSPolicyAssignmentRequest,
    ListOSPolicyAssignmentRevisionsRequest,
    ListOSPolicyAssignmentRevisionsResponse,
    ListOSPolicyAssignmentsRequest,
    ListOSPolicyAssignmentsResponse,
    OSPolicyAssignment,
    OSPolicyAssignmentOperationMetadata,
    UpdateOSPolicyAssignmentRequest,
)
from .types.osconfig_common import FixedOrPercent
from .types.patch_deployments import (
    CreatePatchDeploymentRequest,
    DeletePatchDeploymentRequest,
    GetPatchDeploymentRequest,
    ListPatchDeploymentsRequest,
    ListPatchDeploymentsResponse,
    MonthlySchedule,
    OneTimeSchedule,
    PatchDeployment,
    PausePatchDeploymentRequest,
    RecurringSchedule,
    ResumePatchDeploymentRequest,
    UpdatePatchDeploymentRequest,
    WeekDayOfMonth,
    WeeklySchedule,
)
from .types.patch_jobs import (
    AptSettings,
    CancelPatchJobRequest,
    ExecStep,
    ExecStepConfig,
    ExecutePatchJobRequest,
    GcsObject,
    GetPatchJobRequest,
    GooSettings,
    Instance,
    ListPatchJobInstanceDetailsRequest,
    ListPatchJobInstanceDetailsResponse,
    ListPatchJobsRequest,
    ListPatchJobsResponse,
    PatchConfig,
    PatchInstanceFilter,
    PatchJob,
    PatchJobInstanceDetails,
    PatchRollout,
    WindowsUpdateSettings,
    YumSettings,
    ZypperSettings,
)
from .types.vulnerability import (
    CVSSv3,
    GetVulnerabilityReportRequest,
    ListVulnerabilityReportsRequest,
    ListVulnerabilityReportsResponse,
    VulnerabilityReport,
)

__all__ = (
    "OsConfigServiceAsyncClient",
    "OsConfigZonalServiceAsyncClient",
    "AptSettings",
    "CVSSv3",
    "CancelPatchJobRequest",
    "CreateOSPolicyAssignmentRequest",
    "CreatePatchDeploymentRequest",
    "DeleteOSPolicyAssignmentRequest",
    "DeletePatchDeploymentRequest",
    "ExecStep",
    "ExecStepConfig",
    "ExecutePatchJobRequest",
    "FixedOrPercent",
    "GcsObject",
    "GetInventoryRequest",
    "GetOSPolicyAssignmentReportRequest",
    "GetOSPolicyAssignmentRequest",
    "GetPatchDeploymentRequest",
    "GetPatchJobRequest",
    "GetVulnerabilityReportRequest",
    "GooSettings",
    "Instance",
    "Inventory",
    "InventoryView",
    "ListInventoriesRequest",
    "ListInventoriesResponse",
    "ListOSPolicyAssignmentReportsRequest",
    "ListOSPolicyAssignmentReportsResponse",
    "ListOSPolicyAssignmentRevisionsRequest",
    "ListOSPolicyAssignmentRevisionsResponse",
    "ListOSPolicyAssignmentsRequest",
    "ListOSPolicyAssignmentsResponse",
    "ListPatchDeploymentsRequest",
    "ListPatchDeploymentsResponse",
    "ListPatchJobInstanceDetailsRequest",
    "ListPatchJobInstanceDetailsResponse",
    "ListPatchJobsRequest",
    "ListPatchJobsResponse",
    "ListVulnerabilityReportsRequest",
    "ListVulnerabilityReportsResponse",
    "MonthlySchedule",
    "OSPolicy",
    "OSPolicyAssignment",
    "OSPolicyAssignmentOperationMetadata",
    "OSPolicyAssignmentReport",
    "OneTimeSchedule",
    "OsConfigServiceClient",
    "OsConfigZonalServiceClient",
    "PatchConfig",
    "PatchDeployment",
    "PatchInstanceFilter",
    "PatchJob",
    "PatchJobInstanceDetails",
    "PatchRollout",
    "PausePatchDeploymentRequest",
    "RecurringSchedule",
    "ResumePatchDeploymentRequest",
    "UpdateOSPolicyAssignmentRequest",
    "UpdatePatchDeploymentRequest",
    "VulnerabilityReport",
    "WeekDayOfMonth",
    "WeeklySchedule",
    "WindowsUpdateSettings",
    "YumSettings",
    "ZypperSettings",
)

api_core.check_python_version("google.cloud.osconfig_v1")
api_core.check_dependency_versions("google.cloud.osconfig_v1")
