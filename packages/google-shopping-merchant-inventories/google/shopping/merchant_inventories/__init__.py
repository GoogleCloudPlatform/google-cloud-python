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
from google.shopping.merchant_inventories import gapic_version as package_version

__version__ = package_version.__version__


from google.shopping.merchant_inventories_v1.services.local_inventory_service.async_client import (
    LocalInventoryServiceAsyncClient,
)
from google.shopping.merchant_inventories_v1.services.local_inventory_service.client import (
    LocalInventoryServiceClient,
)
from google.shopping.merchant_inventories_v1.services.regional_inventory_service.async_client import (
    RegionalInventoryServiceAsyncClient,
)
from google.shopping.merchant_inventories_v1.services.regional_inventory_service.client import (
    RegionalInventoryServiceClient,
)
from google.shopping.merchant_inventories_v1.types.inventories_common import (
    InventoryLoyaltyProgram,
    LocalInventoryAttributes,
    RegionalInventoryAttributes,
)
from google.shopping.merchant_inventories_v1.types.localinventory import (
    DeleteLocalInventoryRequest,
    InsertLocalInventoryRequest,
    ListLocalInventoriesRequest,
    ListLocalInventoriesResponse,
    LocalInventory,
)
from google.shopping.merchant_inventories_v1.types.regionalinventory import (
    DeleteRegionalInventoryRequest,
    InsertRegionalInventoryRequest,
    ListRegionalInventoriesRequest,
    ListRegionalInventoriesResponse,
    RegionalInventory,
)

__all__ = (
    "LocalInventoryServiceClient",
    "LocalInventoryServiceAsyncClient",
    "RegionalInventoryServiceClient",
    "RegionalInventoryServiceAsyncClient",
    "InventoryLoyaltyProgram",
    "LocalInventoryAttributes",
    "RegionalInventoryAttributes",
    "DeleteLocalInventoryRequest",
    "InsertLocalInventoryRequest",
    "ListLocalInventoriesRequest",
    "ListLocalInventoriesResponse",
    "LocalInventory",
    "DeleteRegionalInventoryRequest",
    "InsertRegionalInventoryRequest",
    "ListRegionalInventoriesRequest",
    "ListRegionalInventoriesResponse",
    "RegionalInventory",
)
