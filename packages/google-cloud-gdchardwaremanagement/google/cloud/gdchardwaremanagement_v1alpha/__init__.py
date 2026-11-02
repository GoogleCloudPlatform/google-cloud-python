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

from google.cloud.gdchardwaremanagement_v1alpha import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management",
    "google.cloud.gdchardwaremanagement_v1alpha.types.resources",
    "google.cloud.gdchardwaremanagement_v1alpha.types.service",
}


from .services.gdc_hardware_management import (
    GDCHardwareManagementAsyncClient,
    GDCHardwareManagementClient,
)
from .types.resources import (
    ChangeLogEntry,
    Comment,
    Contact,
    Dimensions,
    Entity,
    Hardware,
    HardwareConfig,
    HardwareGroup,
    HardwareInstallationInfo,
    HardwareLocation,
    HardwarePhysicalInfo,
    Order,
    OrganizationContact,
    PowerSupply,
    RackSpace,
    Site,
    Sku,
    SkuConfig,
    SkuInstance,
    Subnet,
    SubscriptionConfig,
    TimePeriod,
    Zone,
    ZoneNetworkConfig,
)
from .types.service import (
    CancelOrderRequest,
    CreateCommentRequest,
    CreateHardwareGroupRequest,
    CreateHardwareRequest,
    CreateOrderRequest,
    CreateSiteRequest,
    CreateZoneRequest,
    DeleteHardwareGroupRequest,
    DeleteHardwareRequest,
    DeleteOrderRequest,
    DeleteSiteRequest,
    DeleteZoneRequest,
    GetChangeLogEntryRequest,
    GetCommentRequest,
    GetHardwareGroupRequest,
    GetHardwareRequest,
    GetOrderRequest,
    GetSiteRequest,
    GetSkuRequest,
    GetZoneRequest,
    ListChangeLogEntriesRequest,
    ListChangeLogEntriesResponse,
    ListCommentsRequest,
    ListCommentsResponse,
    ListHardwareGroupsRequest,
    ListHardwareGroupsResponse,
    ListHardwareRequest,
    ListHardwareResponse,
    ListOrdersRequest,
    ListOrdersResponse,
    ListSitesRequest,
    ListSitesResponse,
    ListSkusRequest,
    ListSkusResponse,
    ListZonesRequest,
    ListZonesResponse,
    OperationMetadata,
    RecordActionOnCommentRequest,
    RequestOrderDateChangeRequest,
    SignalZoneStateRequest,
    SubmitOrderRequest,
    UpdateHardwareGroupRequest,
    UpdateHardwareRequest,
    UpdateOrderRequest,
    UpdateSiteRequest,
    UpdateZoneRequest,
)

__all__ = (
    "GDCHardwareManagementAsyncClient",
    "CancelOrderRequest",
    "ChangeLogEntry",
    "Comment",
    "Contact",
    "CreateCommentRequest",
    "CreateHardwareGroupRequest",
    "CreateHardwareRequest",
    "CreateOrderRequest",
    "CreateSiteRequest",
    "CreateZoneRequest",
    "DeleteHardwareGroupRequest",
    "DeleteHardwareRequest",
    "DeleteOrderRequest",
    "DeleteSiteRequest",
    "DeleteZoneRequest",
    "Dimensions",
    "Entity",
    "GDCHardwareManagementClient",
    "GetChangeLogEntryRequest",
    "GetCommentRequest",
    "GetHardwareGroupRequest",
    "GetHardwareRequest",
    "GetOrderRequest",
    "GetSiteRequest",
    "GetSkuRequest",
    "GetZoneRequest",
    "Hardware",
    "HardwareConfig",
    "HardwareGroup",
    "HardwareInstallationInfo",
    "HardwareLocation",
    "HardwarePhysicalInfo",
    "ListChangeLogEntriesRequest",
    "ListChangeLogEntriesResponse",
    "ListCommentsRequest",
    "ListCommentsResponse",
    "ListHardwareGroupsRequest",
    "ListHardwareGroupsResponse",
    "ListHardwareRequest",
    "ListHardwareResponse",
    "ListOrdersRequest",
    "ListOrdersResponse",
    "ListSitesRequest",
    "ListSitesResponse",
    "ListSkusRequest",
    "ListSkusResponse",
    "ListZonesRequest",
    "ListZonesResponse",
    "OperationMetadata",
    "Order",
    "OrganizationContact",
    "PowerSupply",
    "RackSpace",
    "RecordActionOnCommentRequest",
    "RequestOrderDateChangeRequest",
    "SignalZoneStateRequest",
    "Site",
    "Sku",
    "SkuConfig",
    "SkuInstance",
    "SubmitOrderRequest",
    "Subnet",
    "SubscriptionConfig",
    "TimePeriod",
    "UpdateHardwareGroupRequest",
    "UpdateHardwareRequest",
    "UpdateOrderRequest",
    "UpdateSiteRequest",
    "UpdateZoneRequest",
    "Zone",
    "ZoneNetworkConfig",
)

api_core.check_python_version("google.cloud.gdchardwaremanagement_v1alpha")
api_core.check_dependency_versions("google.cloud.gdchardwaremanagement_v1alpha")
