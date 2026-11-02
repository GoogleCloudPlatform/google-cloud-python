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

from google.cloud.securitycenter_v1beta1 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.securitycenter_v1beta1.services.security_center",
    "google.cloud.securitycenter_v1beta1.types.asset",
    "google.cloud.securitycenter_v1beta1.types.finding",
    "google.cloud.securitycenter_v1beta1.types.organization_settings",
    "google.cloud.securitycenter_v1beta1.types.run_asset_discovery_response",
    "google.cloud.securitycenter_v1beta1.types.security_marks",
    "google.cloud.securitycenter_v1beta1.types.securitycenter_service",
    "google.cloud.securitycenter_v1beta1.types.source",
}


from .services.security_center import SecurityCenterAsyncClient, SecurityCenterClient
from .types.asset import Asset
from .types.finding import Finding
from .types.organization_settings import OrganizationSettings
from .types.run_asset_discovery_response import RunAssetDiscoveryResponse
from .types.security_marks import SecurityMarks
from .types.securitycenter_service import (
    CreateFindingRequest,
    CreateSourceRequest,
    GetOrganizationSettingsRequest,
    GetSourceRequest,
    GroupAssetsRequest,
    GroupAssetsResponse,
    GroupFindingsRequest,
    GroupFindingsResponse,
    GroupResult,
    ListAssetsRequest,
    ListAssetsResponse,
    ListFindingsRequest,
    ListFindingsResponse,
    ListSourcesRequest,
    ListSourcesResponse,
    RunAssetDiscoveryRequest,
    SetFindingStateRequest,
    UpdateFindingRequest,
    UpdateOrganizationSettingsRequest,
    UpdateSecurityMarksRequest,
    UpdateSourceRequest,
)
from .types.source import Source

__all__ = (
    "SecurityCenterAsyncClient",
    "Asset",
    "CreateFindingRequest",
    "CreateSourceRequest",
    "Finding",
    "GetOrganizationSettingsRequest",
    "GetSourceRequest",
    "GroupAssetsRequest",
    "GroupAssetsResponse",
    "GroupFindingsRequest",
    "GroupFindingsResponse",
    "GroupResult",
    "ListAssetsRequest",
    "ListAssetsResponse",
    "ListFindingsRequest",
    "ListFindingsResponse",
    "ListSourcesRequest",
    "ListSourcesResponse",
    "OrganizationSettings",
    "RunAssetDiscoveryRequest",
    "RunAssetDiscoveryResponse",
    "SecurityCenterClient",
    "SecurityMarks",
    "SetFindingStateRequest",
    "Source",
    "UpdateFindingRequest",
    "UpdateOrganizationSettingsRequest",
    "UpdateSecurityMarksRequest",
    "UpdateSourceRequest",
)

api_core.check_python_version("google.cloud.securitycenter_v1beta1")
api_core.check_dependency_versions("google.cloud.securitycenter_v1beta1")
