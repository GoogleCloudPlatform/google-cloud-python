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

from google.shopping.merchant_lfp_v1 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.shopping.merchant_lfp_v1.services.lfp_inventory_service",
    "google.shopping.merchant_lfp_v1.services.lfp_merchant_state_service",
    "google.shopping.merchant_lfp_v1.services.lfp_sale_service",
    "google.shopping.merchant_lfp_v1.services.lfp_store_service",
    "google.shopping.merchant_lfp_v1.types.lfpinventory",
    "google.shopping.merchant_lfp_v1.types.lfpmerchantstate",
    "google.shopping.merchant_lfp_v1.types.lfpsale",
    "google.shopping.merchant_lfp_v1.types.lfpstore",
}


from .services.lfp_inventory_service import (
    LfpInventoryServiceAsyncClient,
    LfpInventoryServiceClient,
)
from .services.lfp_merchant_state_service import (
    LfpMerchantStateServiceAsyncClient,
    LfpMerchantStateServiceClient,
)
from .services.lfp_sale_service import LfpSaleServiceAsyncClient, LfpSaleServiceClient
from .services.lfp_store_service import (
    LfpStoreServiceAsyncClient,
    LfpStoreServiceClient,
)
from .types.lfpinventory import InsertLfpInventoryRequest, LfpInventory
from .types.lfpmerchantstate import GetLfpMerchantStateRequest, LfpMerchantState
from .types.lfpsale import InsertLfpSaleRequest, LfpSale
from .types.lfpstore import (
    DeleteLfpStoreRequest,
    GetLfpStoreRequest,
    InsertLfpStoreRequest,
    LfpStore,
    ListLfpStoresRequest,
    ListLfpStoresResponse,
)

__all__ = (
    "LfpInventoryServiceAsyncClient",
    "LfpMerchantStateServiceAsyncClient",
    "LfpSaleServiceAsyncClient",
    "LfpStoreServiceAsyncClient",
    "DeleteLfpStoreRequest",
    "GetLfpMerchantStateRequest",
    "GetLfpStoreRequest",
    "InsertLfpInventoryRequest",
    "InsertLfpSaleRequest",
    "InsertLfpStoreRequest",
    "LfpInventory",
    "LfpInventoryServiceClient",
    "LfpMerchantState",
    "LfpMerchantStateServiceClient",
    "LfpSale",
    "LfpSaleServiceClient",
    "LfpStore",
    "LfpStoreServiceClient",
    "ListLfpStoresRequest",
    "ListLfpStoresResponse",
)

api_core.check_python_version("google.shopping.merchant_lfp_v1")
api_core.check_dependency_versions("google.shopping.merchant_lfp_v1")
