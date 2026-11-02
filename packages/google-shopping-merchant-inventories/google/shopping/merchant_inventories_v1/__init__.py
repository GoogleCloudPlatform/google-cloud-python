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

from google.shopping.merchant_inventories_v1 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.shopping.merchant_inventories_v1.services.local_inventory_service",
    "google.shopping.merchant_inventories_v1.services.regional_inventory_service",
    "google.shopping.merchant_inventories_v1.types.inventories_common",
    "google.shopping.merchant_inventories_v1.types.localinventory",
    "google.shopping.merchant_inventories_v1.types.regionalinventory",
}


from .services.local_inventory_service import (
    LocalInventoryServiceAsyncClient,
    LocalInventoryServiceClient,
)
from .services.regional_inventory_service import (
    RegionalInventoryServiceAsyncClient,
    RegionalInventoryServiceClient,
)
from .types.inventories_common import (
    InventoryLoyaltyProgram,
    LocalInventoryAttributes,
    RegionalInventoryAttributes,
)
from .types.localinventory import (
    DeleteLocalInventoryRequest,
    InsertLocalInventoryRequest,
    ListLocalInventoriesRequest,
    ListLocalInventoriesResponse,
    LocalInventory,
)
from .types.regionalinventory import (
    DeleteRegionalInventoryRequest,
    InsertRegionalInventoryRequest,
    ListRegionalInventoriesRequest,
    ListRegionalInventoriesResponse,
    RegionalInventory,
)

__all__ = (
    "LocalInventoryServiceAsyncClient",
    "RegionalInventoryServiceAsyncClient",
    "DeleteLocalInventoryRequest",
    "DeleteRegionalInventoryRequest",
    "InsertLocalInventoryRequest",
    "InsertRegionalInventoryRequest",
    "InventoryLoyaltyProgram",
    "ListLocalInventoriesRequest",
    "ListLocalInventoriesResponse",
    "ListRegionalInventoriesRequest",
    "ListRegionalInventoriesResponse",
    "LocalInventory",
    "LocalInventoryAttributes",
    "LocalInventoryServiceClient",
    "RegionalInventory",
    "RegionalInventoryAttributes",
    "RegionalInventoryServiceClient",
)

api_core.check_python_version("google.shopping.merchant_inventories_v1")
api_core.check_dependency_versions("google.shopping.merchant_inventories_v1")
