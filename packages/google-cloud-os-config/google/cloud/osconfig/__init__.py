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
from google.cloud.osconfig import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.osconfig_v1.services.os_config_service.async_client import (
    OsConfigServiceAsyncClient,
)
from google.cloud.osconfig_v1.services.os_config_service.client import (
    OsConfigServiceClient,
)
from google.cloud.osconfig_v1.services.os_config_zonal_service.async_client import (
    OsConfigZonalServiceAsyncClient,
)
from google.cloud.osconfig_v1.services.os_config_zonal_service.client import (
    OsConfigZonalServiceClient,
)
from google.cloud.osconfig_v1.types.inventory import (
    GetInventoryRequest,
    Inventory,
    InventoryView,
    ListInventoriesRequest,
    ListInventoriesResponse,
)
from google.cloud.osconfig_v1.types.os_policy import OSPolicy
from google.cloud.osconfig_v1.types.os_policy_assignment_reports import (
    GetOSPolicyAssignmentReportRequest,
    ListOSPolicyAssignmentReportsRequest,
    ListOSPolicyAssignmentReportsResponse,
    OSPolicyAssignmentReport,
)
from google.cloud.osconfig_v1.types.os_policy_assignments import (
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
from google.cloud.osconfig_v1.types.osconfig_common import FixedOrPercent
from google.cloud.osconfig_v1.types.patch_deployments import (
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
from google.cloud.osconfig_v1.types.patch_jobs import (
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
from google.cloud.osconfig_v1.types.vulnerability import (
    CVSSv3,
    GetVulnerabilityReportRequest,
    ListVulnerabilityReportsRequest,
    ListVulnerabilityReportsResponse,
    VulnerabilityReport,
)

__all__ = (
    "OsConfigServiceClient",
    "OsConfigServiceAsyncClient",
    "OsConfigZonalServiceClient",
    "OsConfigZonalServiceAsyncClient",
    "GetInventoryRequest",
    "Inventory",
    "ListInventoriesRequest",
    "ListInventoriesResponse",
    "InventoryView",
    "OSPolicy",
    "GetOSPolicyAssignmentReportRequest",
    "ListOSPolicyAssignmentReportsRequest",
    "ListOSPolicyAssignmentReportsResponse",
    "OSPolicyAssignmentReport",
    "CreateOSPolicyAssignmentRequest",
    "DeleteOSPolicyAssignmentRequest",
    "GetOSPolicyAssignmentRequest",
    "ListOSPolicyAssignmentRevisionsRequest",
    "ListOSPolicyAssignmentRevisionsResponse",
    "ListOSPolicyAssignmentsRequest",
    "ListOSPolicyAssignmentsResponse",
    "OSPolicyAssignment",
    "OSPolicyAssignmentOperationMetadata",
    "UpdateOSPolicyAssignmentRequest",
    "FixedOrPercent",
    "CreatePatchDeploymentRequest",
    "DeletePatchDeploymentRequest",
    "GetPatchDeploymentRequest",
    "ListPatchDeploymentsRequest",
    "ListPatchDeploymentsResponse",
    "MonthlySchedule",
    "OneTimeSchedule",
    "PatchDeployment",
    "PausePatchDeploymentRequest",
    "RecurringSchedule",
    "ResumePatchDeploymentRequest",
    "UpdatePatchDeploymentRequest",
    "WeekDayOfMonth",
    "WeeklySchedule",
    "AptSettings",
    "CancelPatchJobRequest",
    "ExecStep",
    "ExecStepConfig",
    "ExecutePatchJobRequest",
    "GcsObject",
    "GetPatchJobRequest",
    "GooSettings",
    "Instance",
    "ListPatchJobInstanceDetailsRequest",
    "ListPatchJobInstanceDetailsResponse",
    "ListPatchJobsRequest",
    "ListPatchJobsResponse",
    "PatchConfig",
    "PatchInstanceFilter",
    "PatchJob",
    "PatchJobInstanceDetails",
    "PatchRollout",
    "WindowsUpdateSettings",
    "YumSettings",
    "ZypperSettings",
    "CVSSv3",
    "GetVulnerabilityReportRequest",
    "ListVulnerabilityReportsRequest",
    "ListVulnerabilityReportsResponse",
    "VulnerabilityReport",
)
