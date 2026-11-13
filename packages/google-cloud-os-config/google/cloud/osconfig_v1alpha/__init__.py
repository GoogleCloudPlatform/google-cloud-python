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

from google.cloud.osconfig_v1alpha import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.osconfig_v1alpha.services.os_config_zonal_service",
    "google.cloud.osconfig_v1alpha.types.config_common",
    "google.cloud.osconfig_v1alpha.types.instance_os_policies_compliance",
    "google.cloud.osconfig_v1alpha.types.inventory",
    "google.cloud.osconfig_v1alpha.types.os_policy",
    "google.cloud.osconfig_v1alpha.types.os_policy_assignment_reports",
    "google.cloud.osconfig_v1alpha.types.os_policy_assignments",
    "google.cloud.osconfig_v1alpha.types.osconfig_common",
    "google.cloud.osconfig_v1alpha.types.osconfig_zonal_service",
    "google.cloud.osconfig_v1alpha.types.vulnerability",
}


from .services.os_config_zonal_service import (
    OsConfigZonalServiceAsyncClient,
    OsConfigZonalServiceClient,
)
from .types.config_common import (
    OSPolicyComplianceState,
    OSPolicyResourceCompliance,
    OSPolicyResourceConfigStep,
)
from .types.instance_os_policies_compliance import (
    GetInstanceOSPoliciesComplianceRequest,
    InstanceOSPoliciesCompliance,
    ListInstanceOSPoliciesCompliancesRequest,
    ListInstanceOSPoliciesCompliancesResponse,
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
from .types.vulnerability import (
    CVSSv3,
    GetVulnerabilityReportRequest,
    ListVulnerabilityReportsRequest,
    ListVulnerabilityReportsResponse,
    VulnerabilityReport,
)

__all__ = (
    "OsConfigZonalServiceAsyncClient",
    "CVSSv3",
    "CreateOSPolicyAssignmentRequest",
    "DeleteOSPolicyAssignmentRequest",
    "FixedOrPercent",
    "GetInstanceOSPoliciesComplianceRequest",
    "GetInventoryRequest",
    "GetOSPolicyAssignmentReportRequest",
    "GetOSPolicyAssignmentRequest",
    "GetVulnerabilityReportRequest",
    "InstanceOSPoliciesCompliance",
    "Inventory",
    "InventoryView",
    "ListInstanceOSPoliciesCompliancesRequest",
    "ListInstanceOSPoliciesCompliancesResponse",
    "ListInventoriesRequest",
    "ListInventoriesResponse",
    "ListOSPolicyAssignmentReportsRequest",
    "ListOSPolicyAssignmentReportsResponse",
    "ListOSPolicyAssignmentRevisionsRequest",
    "ListOSPolicyAssignmentRevisionsResponse",
    "ListOSPolicyAssignmentsRequest",
    "ListOSPolicyAssignmentsResponse",
    "ListVulnerabilityReportsRequest",
    "ListVulnerabilityReportsResponse",
    "OSPolicy",
    "OSPolicyAssignment",
    "OSPolicyAssignmentOperationMetadata",
    "OSPolicyAssignmentReport",
    "OSPolicyComplianceState",
    "OSPolicyResourceCompliance",
    "OSPolicyResourceConfigStep",
    "OsConfigZonalServiceClient",
    "UpdateOSPolicyAssignmentRequest",
    "VulnerabilityReport",
)

api_core.check_python_version("google.cloud.osconfig_v1alpha")
api_core.check_dependency_versions("google.cloud.osconfig_v1alpha")
