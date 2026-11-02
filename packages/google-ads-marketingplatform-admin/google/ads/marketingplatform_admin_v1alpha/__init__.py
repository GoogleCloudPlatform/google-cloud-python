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

from google.ads.marketingplatform_admin_v1alpha import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.ads.marketingplatform_admin_v1alpha.services.marketingplatform_admin_service",
    "google.ads.marketingplatform_admin_v1alpha.types.marketingplatform_admin",
    "google.ads.marketingplatform_admin_v1alpha.types.resources",
}


from .services.marketingplatform_admin_service import (
    MarketingplatformAdminServiceAsyncClient,
    MarketingplatformAdminServiceClient,
)
from .types.marketingplatform_admin import (
    CreateAdminAccessBindingRequest,
    CreateAnalyticsAccountLinkRequest,
    CreateUserGroupMemberRequest,
    CreateUserGroupRequest,
    DeleteAnalyticsAccountLinkRequest,
    DeleteUserGroupMemberRequest,
    DeleteUserGroupRequest,
    FindSalesPartnerManagedClientsRequest,
    FindSalesPartnerManagedClientsResponse,
    GetAdminAccessBindingRequest,
    GetOrganizationRequest,
    GetUserGroupMemberRequest,
    GetUserGroupRequest,
    ListAdminAccessBindingsRequest,
    ListAdminAccessBindingsResponse,
    ListAnalyticsAccountLinksRequest,
    ListAnalyticsAccountLinksResponse,
    ListOrganizationsRequest,
    ListOrganizationsResponse,
    ListUserGroupMembersRequest,
    ListUserGroupMembersResponse,
    ListUserGroupsRequest,
    ListUserGroupsResponse,
    ReportPropertyUsageRequest,
    ReportPropertyUsageResponse,
    SetPropertyServiceLevelRequest,
    SetPropertyServiceLevelResponse,
    UpdateAdminAccessBindingRequest,
    UpdateUserGroupMemberRequest,
    UpdateUserGroupRequest,
)
from .types.resources import (
    AdminAccessBinding,
    AnalyticsAccountLink,
    AnalyticsPropertyType,
    AnalyticsServiceLevel,
    LinkVerificationState,
    Organization,
    OrganizationRole,
    UserGroup,
    UserGroupMember,
)

__all__ = (
    "MarketingplatformAdminServiceAsyncClient",
    "AdminAccessBinding",
    "AnalyticsAccountLink",
    "AnalyticsPropertyType",
    "AnalyticsServiceLevel",
    "CreateAdminAccessBindingRequest",
    "CreateAnalyticsAccountLinkRequest",
    "CreateUserGroupMemberRequest",
    "CreateUserGroupRequest",
    "DeleteAnalyticsAccountLinkRequest",
    "DeleteUserGroupMemberRequest",
    "DeleteUserGroupRequest",
    "FindSalesPartnerManagedClientsRequest",
    "FindSalesPartnerManagedClientsResponse",
    "GetAdminAccessBindingRequest",
    "GetOrganizationRequest",
    "GetUserGroupMemberRequest",
    "GetUserGroupRequest",
    "LinkVerificationState",
    "ListAdminAccessBindingsRequest",
    "ListAdminAccessBindingsResponse",
    "ListAnalyticsAccountLinksRequest",
    "ListAnalyticsAccountLinksResponse",
    "ListOrganizationsRequest",
    "ListOrganizationsResponse",
    "ListUserGroupMembersRequest",
    "ListUserGroupMembersResponse",
    "ListUserGroupsRequest",
    "ListUserGroupsResponse",
    "MarketingplatformAdminServiceClient",
    "Organization",
    "OrganizationRole",
    "ReportPropertyUsageRequest",
    "ReportPropertyUsageResponse",
    "SetPropertyServiceLevelRequest",
    "SetPropertyServiceLevelResponse",
    "UpdateAdminAccessBindingRequest",
    "UpdateUserGroupMemberRequest",
    "UpdateUserGroupRequest",
    "UserGroup",
    "UserGroupMember",
)

api_core.check_python_version("google.ads.marketingplatform_admin_v1alpha")
api_core.check_dependency_versions("google.ads.marketingplatform_admin_v1alpha")
