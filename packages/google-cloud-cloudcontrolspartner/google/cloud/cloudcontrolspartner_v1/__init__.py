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

from google.cloud.cloudcontrolspartner_v1 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.cloudcontrolspartner_v1.services.cloud_controls_partner_core",
    "google.cloud.cloudcontrolspartner_v1.services.cloud_controls_partner_monitoring",
    "google.cloud.cloudcontrolspartner_v1.types.access_approval_requests",
    "google.cloud.cloudcontrolspartner_v1.types.completion_state",
    "google.cloud.cloudcontrolspartner_v1.types.core",
    "google.cloud.cloudcontrolspartner_v1.types.customer_workloads",
    "google.cloud.cloudcontrolspartner_v1.types.customers",
    "google.cloud.cloudcontrolspartner_v1.types.ekm_connections",
    "google.cloud.cloudcontrolspartner_v1.types.monitoring",
    "google.cloud.cloudcontrolspartner_v1.types.partner_permissions",
    "google.cloud.cloudcontrolspartner_v1.types.partners",
    "google.cloud.cloudcontrolspartner_v1.types.violations",
}


from .services.cloud_controls_partner_core import (
    CloudControlsPartnerCoreAsyncClient,
    CloudControlsPartnerCoreClient,
)
from .services.cloud_controls_partner_monitoring import (
    CloudControlsPartnerMonitoringAsyncClient,
    CloudControlsPartnerMonitoringClient,
)
from .types.access_approval_requests import (
    AccessApprovalRequest,
    AccessReason,
    ListAccessApprovalRequestsRequest,
    ListAccessApprovalRequestsResponse,
)
from .types.completion_state import CompletionState
from .types.core import OperationMetadata
from .types.customer_workloads import (
    GetWorkloadRequest,
    ListWorkloadsRequest,
    ListWorkloadsResponse,
    Workload,
    WorkloadOnboardingState,
    WorkloadOnboardingStep,
)
from .types.customers import (
    CreateCustomerRequest,
    Customer,
    CustomerOnboardingState,
    CustomerOnboardingStep,
    DeleteCustomerRequest,
    GetCustomerRequest,
    ListCustomersRequest,
    ListCustomersResponse,
    UpdateCustomerRequest,
)
from .types.ekm_connections import (
    EkmConnection,
    EkmConnections,
    GetEkmConnectionsRequest,
)
from .types.partner_permissions import GetPartnerPermissionsRequest, PartnerPermissions
from .types.partners import EkmMetadata, GetPartnerRequest, Partner, Sku
from .types.violations import (
    GetViolationRequest,
    ListViolationsRequest,
    ListViolationsResponse,
    Violation,
)

__all__ = (
    "CloudControlsPartnerCoreAsyncClient",
    "CloudControlsPartnerMonitoringAsyncClient",
    "AccessApprovalRequest",
    "AccessReason",
    "CloudControlsPartnerCoreClient",
    "CloudControlsPartnerMonitoringClient",
    "CompletionState",
    "CreateCustomerRequest",
    "Customer",
    "CustomerOnboardingState",
    "CustomerOnboardingStep",
    "DeleteCustomerRequest",
    "EkmConnection",
    "EkmConnections",
    "EkmMetadata",
    "GetCustomerRequest",
    "GetEkmConnectionsRequest",
    "GetPartnerPermissionsRequest",
    "GetPartnerRequest",
    "GetViolationRequest",
    "GetWorkloadRequest",
    "ListAccessApprovalRequestsRequest",
    "ListAccessApprovalRequestsResponse",
    "ListCustomersRequest",
    "ListCustomersResponse",
    "ListViolationsRequest",
    "ListViolationsResponse",
    "ListWorkloadsRequest",
    "ListWorkloadsResponse",
    "OperationMetadata",
    "Partner",
    "PartnerPermissions",
    "Sku",
    "UpdateCustomerRequest",
    "Violation",
    "Workload",
    "WorkloadOnboardingState",
    "WorkloadOnboardingStep",
)

api_core.check_python_version("google.cloud.cloudcontrolspartner_v1")
api_core.check_dependency_versions("google.cloud.cloudcontrolspartner_v1")
