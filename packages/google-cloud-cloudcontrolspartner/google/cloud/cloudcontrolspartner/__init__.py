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
from google.cloud.cloudcontrolspartner import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.cloudcontrolspartner_v1.services.cloud_controls_partner_core.async_client import (
    CloudControlsPartnerCoreAsyncClient,
)
from google.cloud.cloudcontrolspartner_v1.services.cloud_controls_partner_core.client import (
    CloudControlsPartnerCoreClient,
)
from google.cloud.cloudcontrolspartner_v1.services.cloud_controls_partner_monitoring.async_client import (
    CloudControlsPartnerMonitoringAsyncClient,
)
from google.cloud.cloudcontrolspartner_v1.services.cloud_controls_partner_monitoring.client import (
    CloudControlsPartnerMonitoringClient,
)
from google.cloud.cloudcontrolspartner_v1.types.access_approval_requests import (
    AccessApprovalRequest,
    AccessReason,
    ListAccessApprovalRequestsRequest,
    ListAccessApprovalRequestsResponse,
)
from google.cloud.cloudcontrolspartner_v1.types.completion_state import CompletionState
from google.cloud.cloudcontrolspartner_v1.types.core import OperationMetadata
from google.cloud.cloudcontrolspartner_v1.types.customer_workloads import (
    GetWorkloadRequest,
    ListWorkloadsRequest,
    ListWorkloadsResponse,
    Workload,
    WorkloadOnboardingState,
    WorkloadOnboardingStep,
)
from google.cloud.cloudcontrolspartner_v1.types.customers import (
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
from google.cloud.cloudcontrolspartner_v1.types.ekm_connections import (
    EkmConnection,
    EkmConnections,
    GetEkmConnectionsRequest,
)
from google.cloud.cloudcontrolspartner_v1.types.partner_permissions import (
    GetPartnerPermissionsRequest,
    PartnerPermissions,
)
from google.cloud.cloudcontrolspartner_v1.types.partners import (
    EkmMetadata,
    GetPartnerRequest,
    Partner,
    Sku,
)
from google.cloud.cloudcontrolspartner_v1.types.violations import (
    GetViolationRequest,
    ListViolationsRequest,
    ListViolationsResponse,
    Violation,
)

__all__ = (
    "CloudControlsPartnerCoreClient",
    "CloudControlsPartnerCoreAsyncClient",
    "CloudControlsPartnerMonitoringClient",
    "CloudControlsPartnerMonitoringAsyncClient",
    "AccessApprovalRequest",
    "AccessReason",
    "ListAccessApprovalRequestsRequest",
    "ListAccessApprovalRequestsResponse",
    "CompletionState",
    "OperationMetadata",
    "GetWorkloadRequest",
    "ListWorkloadsRequest",
    "ListWorkloadsResponse",
    "Workload",
    "WorkloadOnboardingState",
    "WorkloadOnboardingStep",
    "CreateCustomerRequest",
    "Customer",
    "CustomerOnboardingState",
    "CustomerOnboardingStep",
    "DeleteCustomerRequest",
    "GetCustomerRequest",
    "ListCustomersRequest",
    "ListCustomersResponse",
    "UpdateCustomerRequest",
    "EkmConnection",
    "EkmConnections",
    "GetEkmConnectionsRequest",
    "GetPartnerPermissionsRequest",
    "PartnerPermissions",
    "EkmMetadata",
    "GetPartnerRequest",
    "Partner",
    "Sku",
    "GetViolationRequest",
    "ListViolationsRequest",
    "ListViolationsResponse",
    "Violation",
)
