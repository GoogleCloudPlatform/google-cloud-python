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
from google.cloud.privilegedaccessmanager import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.privilegedaccessmanager_v1.services.privileged_access_manager.async_client import (
    PrivilegedAccessManagerAsyncClient,
)
from google.cloud.privilegedaccessmanager_v1.services.privileged_access_manager.client import (
    PrivilegedAccessManagerClient,
)
from google.cloud.privilegedaccessmanager_v1.types.privilegedaccessmanager import (
    AccessControlEntry,
    ApprovalWorkflow,
    ApproveGrantRequest,
    CheckOnboardingStatusRequest,
    CheckOnboardingStatusResponse,
    CreateEntitlementRequest,
    CreateGrantRequest,
    DeleteEntitlementRequest,
    DenyGrantRequest,
    Entitlement,
    GetEntitlementRequest,
    GetGrantRequest,
    Grant,
    Justification,
    ListEntitlementsRequest,
    ListEntitlementsResponse,
    ListGrantsRequest,
    ListGrantsResponse,
    ManualApprovals,
    OperationMetadata,
    PrivilegedAccess,
    RevokeGrantRequest,
    SearchEntitlementsRequest,
    SearchEntitlementsResponse,
    SearchGrantsRequest,
    SearchGrantsResponse,
    UpdateEntitlementRequest,
)

__all__ = (
    "PrivilegedAccessManagerClient",
    "PrivilegedAccessManagerAsyncClient",
    "AccessControlEntry",
    "ApprovalWorkflow",
    "ApproveGrantRequest",
    "CheckOnboardingStatusRequest",
    "CheckOnboardingStatusResponse",
    "CreateEntitlementRequest",
    "CreateGrantRequest",
    "DeleteEntitlementRequest",
    "DenyGrantRequest",
    "Entitlement",
    "GetEntitlementRequest",
    "GetGrantRequest",
    "Grant",
    "Justification",
    "ListEntitlementsRequest",
    "ListEntitlementsResponse",
    "ListGrantsRequest",
    "ListGrantsResponse",
    "ManualApprovals",
    "OperationMetadata",
    "PrivilegedAccess",
    "RevokeGrantRequest",
    "SearchEntitlementsRequest",
    "SearchEntitlementsResponse",
    "SearchGrantsRequest",
    "SearchGrantsResponse",
    "UpdateEntitlementRequest",
)
