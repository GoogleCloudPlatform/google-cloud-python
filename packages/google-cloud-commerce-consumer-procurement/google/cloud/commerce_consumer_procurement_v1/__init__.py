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

from google.cloud.commerce_consumer_procurement_v1 import (
    gapic_version as package_version,
)

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.commerce_consumer_procurement_v1.services.consumer_procurement_service",
    "google.cloud.commerce_consumer_procurement_v1.services.license_management_service",
    "google.cloud.commerce_consumer_procurement_v1.types.license_management_service",
    "google.cloud.commerce_consumer_procurement_v1.types.order",
    "google.cloud.commerce_consumer_procurement_v1.types.procurement_service",
}


from .services.consumer_procurement_service import (
    ConsumerProcurementServiceAsyncClient,
    ConsumerProcurementServiceClient,
)
from .services.license_management_service import (
    LicenseManagementServiceAsyncClient,
    LicenseManagementServiceClient,
)
from .types.license_management_service import (
    AssignmentProtocol,
    AssignRequest,
    AssignResponse,
    EnumerateLicensedUsersRequest,
    EnumerateLicensedUsersResponse,
    GetLicensePoolRequest,
    LicensedUser,
    LicensePool,
    UnassignRequest,
    UnassignResponse,
    UpdateLicensePoolRequest,
)
from .types.order import (
    LineItem,
    LineItemChange,
    LineItemChangeState,
    LineItemChangeStateReasonType,
    LineItemChangeType,
    LineItemInfo,
    Order,
    Parameter,
    Subscription,
)
from .types.procurement_service import (
    AutoRenewalBehavior,
    CancelOrderMetadata,
    CancelOrderRequest,
    GetOrderRequest,
    ListOrdersRequest,
    ListOrdersResponse,
    ModifyOrderMetadata,
    ModifyOrderRequest,
    PlaceOrderMetadata,
    PlaceOrderRequest,
)

__all__ = (
    "ConsumerProcurementServiceAsyncClient",
    "LicenseManagementServiceAsyncClient",
    "AssignRequest",
    "AssignResponse",
    "AssignmentProtocol",
    "AutoRenewalBehavior",
    "CancelOrderMetadata",
    "CancelOrderRequest",
    "ConsumerProcurementServiceClient",
    "EnumerateLicensedUsersRequest",
    "EnumerateLicensedUsersResponse",
    "GetLicensePoolRequest",
    "GetOrderRequest",
    "LicenseManagementServiceClient",
    "LicensePool",
    "LicensedUser",
    "LineItem",
    "LineItemChange",
    "LineItemChangeState",
    "LineItemChangeStateReasonType",
    "LineItemChangeType",
    "LineItemInfo",
    "ListOrdersRequest",
    "ListOrdersResponse",
    "ModifyOrderMetadata",
    "ModifyOrderRequest",
    "Order",
    "Parameter",
    "PlaceOrderMetadata",
    "PlaceOrderRequest",
    "Subscription",
    "UnassignRequest",
    "UnassignResponse",
    "UpdateLicensePoolRequest",
)

api_core.check_python_version("google.cloud.commerce_consumer_procurement_v1")
api_core.check_dependency_versions("google.cloud.commerce_consumer_procurement_v1")
