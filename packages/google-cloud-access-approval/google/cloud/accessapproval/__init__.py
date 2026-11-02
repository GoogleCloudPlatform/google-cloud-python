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
from google.cloud.accessapproval import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.accessapproval_v1.services.access_approval.async_client import (
    AccessApprovalAsyncClient,
)
from google.cloud.accessapproval_v1.services.access_approval.client import (
    AccessApprovalClient,
)
from google.cloud.accessapproval_v1.types.accessapproval import (
    AccessApprovalServiceAccount,
    AccessApprovalSettings,
    AccessLocations,
    AccessReason,
    ApprovalRequest,
    ApproveApprovalRequestMessage,
    ApproveDecision,
    DeleteAccessApprovalSettingsMessage,
    DismissApprovalRequestMessage,
    DismissDecision,
    EnrolledService,
    EnrollmentLevel,
    GetAccessApprovalServiceAccountMessage,
    GetAccessApprovalSettingsMessage,
    GetApprovalRequestMessage,
    InvalidateApprovalRequestMessage,
    ListApprovalRequestsMessage,
    ListApprovalRequestsResponse,
    ResourceProperties,
    SignatureInfo,
    UpdateAccessApprovalSettingsMessage,
)

__all__ = (
    "AccessApprovalClient",
    "AccessApprovalAsyncClient",
    "AccessApprovalServiceAccount",
    "AccessApprovalSettings",
    "AccessLocations",
    "AccessReason",
    "ApprovalRequest",
    "ApproveApprovalRequestMessage",
    "ApproveDecision",
    "DeleteAccessApprovalSettingsMessage",
    "DismissApprovalRequestMessage",
    "DismissDecision",
    "EnrolledService",
    "GetAccessApprovalServiceAccountMessage",
    "GetAccessApprovalSettingsMessage",
    "GetApprovalRequestMessage",
    "InvalidateApprovalRequestMessage",
    "ListApprovalRequestsMessage",
    "ListApprovalRequestsResponse",
    "ResourceProperties",
    "SignatureInfo",
    "UpdateAccessApprovalSettingsMessage",
    "EnrollmentLevel",
)
