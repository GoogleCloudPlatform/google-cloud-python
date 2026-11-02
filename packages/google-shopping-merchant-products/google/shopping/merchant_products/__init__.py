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
from google.shopping.merchant_products import gapic_version as package_version

__version__ = package_version.__version__


from google.shopping.merchant_products_v1.services.product_inputs_service.async_client import (
    ProductInputsServiceAsyncClient,
)
from google.shopping.merchant_products_v1.services.product_inputs_service.client import (
    ProductInputsServiceClient,
)
from google.shopping.merchant_products_v1.services.products_service.async_client import (
    ProductsServiceAsyncClient,
)
from google.shopping.merchant_products_v1.services.products_service.client import (
    ProductsServiceClient,
)
from google.shopping.merchant_products_v1.types.productinputs import (
    DeleteProductInputRequest,
    InsertProductInputRequest,
    ProductInput,
    UpdateProductInputRequest,
)
from google.shopping.merchant_products_v1.types.products import (
    GetProductRequest,
    ListProductsRequest,
    ListProductsResponse,
    Product,
)
from google.shopping.merchant_products_v1.types.products_common import (
    AgeGroup,
    AutomatedDiscounts,
    Availability,
    CarrierTransitTimeOption,
    CertificationAuthority,
    CertificationName,
    CloudExportAdditionalProperties,
    Condition,
    CreditType,
    DigitalSourceType,
    EnergyEfficiencyClass,
    FreeShippingThreshold,
    Gender,
    HandlingCutoffTime,
    LoyaltyPoints,
    LoyaltyProgram,
    Pause,
    PickupCost,
    PickupMethod,
    PickupSla,
    ProductAttributes,
    ProductCertification,
    ProductDetail,
    ProductDimension,
    ProductInstallment,
    ProductMinimumOrderValue,
    ProductStatus,
    ProductSustainabilityIncentive,
    ProductWeight,
    Shipping,
    ShippingDimension,
    ShippingWeight,
    SizeSystem,
    SizeType,
    StructuredDescription,
    StructuredTitle,
    SubscriptionCost,
    SubscriptionPeriod,
    UnitPricingBaseMeasure,
    UnitPricingMeasure,
)

__all__ = (
    "ProductInputsServiceClient",
    "ProductInputsServiceAsyncClient",
    "ProductsServiceClient",
    "ProductsServiceAsyncClient",
    "DeleteProductInputRequest",
    "InsertProductInputRequest",
    "ProductInput",
    "UpdateProductInputRequest",
    "GetProductRequest",
    "ListProductsRequest",
    "ListProductsResponse",
    "Product",
    "AutomatedDiscounts",
    "CloudExportAdditionalProperties",
    "FreeShippingThreshold",
    "HandlingCutoffTime",
    "LoyaltyPoints",
    "LoyaltyProgram",
    "PickupCost",
    "ProductAttributes",
    "ProductCertification",
    "ProductDetail",
    "ProductDimension",
    "ProductInstallment",
    "ProductMinimumOrderValue",
    "ProductStatus",
    "ProductSustainabilityIncentive",
    "ProductWeight",
    "Shipping",
    "ShippingDimension",
    "ShippingWeight",
    "StructuredDescription",
    "StructuredTitle",
    "SubscriptionCost",
    "UnitPricingBaseMeasure",
    "UnitPricingMeasure",
    "AgeGroup",
    "Availability",
    "CarrierTransitTimeOption",
    "CertificationAuthority",
    "CertificationName",
    "Condition",
    "CreditType",
    "DigitalSourceType",
    "EnergyEfficiencyClass",
    "Gender",
    "Pause",
    "PickupMethod",
    "PickupSla",
    "SizeSystem",
    "SizeType",
    "SubscriptionPeriod",
)
