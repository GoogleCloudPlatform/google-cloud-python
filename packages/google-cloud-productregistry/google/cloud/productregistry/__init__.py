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
from google.cloud.productregistry import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.productregistry_v1.services.cloud_product_registry_read_service.async_client import (
    CloudProductRegistryReadServiceAsyncClient,
)
from google.cloud.productregistry_v1.services.cloud_product_registry_read_service.client import (
    CloudProductRegistryReadServiceClient,
)
from google.cloud.productregistry_v1.types.cloud_product_registry_read_service import (
    GetLogicalProductRequest,
    GetLogicalProductVariantRequest,
    GetProductSuiteRequest,
    ListLogicalProductsRequest,
    ListLogicalProductsResponse,
    ListLogicalProductVariantsRequest,
    ListLogicalProductVariantsResponse,
    ListProductSuitesRequest,
    ListProductSuitesResponse,
    LookupEntityRequest,
    LookupEntityResponse,
)
from google.cloud.productregistry_v1.types.lifecycle_state import LifecycleState
from google.cloud.productregistry_v1.types.logical_product import LogicalProduct
from google.cloud.productregistry_v1.types.logical_product_variant import (
    LogicalProductVariant,
)
from google.cloud.productregistry_v1.types.product_suite import ProductSuite

__all__ = (
    "CloudProductRegistryReadServiceClient",
    "CloudProductRegistryReadServiceAsyncClient",
    "GetLogicalProductRequest",
    "GetLogicalProductVariantRequest",
    "GetProductSuiteRequest",
    "ListLogicalProductsRequest",
    "ListLogicalProductsResponse",
    "ListLogicalProductVariantsRequest",
    "ListLogicalProductVariantsResponse",
    "ListProductSuitesRequest",
    "ListProductSuitesResponse",
    "LookupEntityRequest",
    "LookupEntityResponse",
    "LifecycleState",
    "LogicalProduct",
    "LogicalProductVariant",
    "ProductSuite",
)
