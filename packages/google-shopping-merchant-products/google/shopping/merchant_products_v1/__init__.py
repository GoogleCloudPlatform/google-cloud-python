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

from google.shopping.merchant_products_v1 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.shopping.merchant_products_v1.services.product_inputs_service",
    "google.shopping.merchant_products_v1.services.products_service",
    "google.shopping.merchant_products_v1.types.productinputs",
    "google.shopping.merchant_products_v1.types.products",
    "google.shopping.merchant_products_v1.types.products_common",
}


from .services.product_inputs_service import (
    ProductInputsServiceAsyncClient,
    ProductInputsServiceClient,
)
from .services.products_service import ProductsServiceAsyncClient, ProductsServiceClient
from .types.productinputs import (
    DeleteProductInputRequest,
    InsertProductInputRequest,
    ProductInput,
    UpdateProductInputRequest,
)
from .types.products import (
    GetProductRequest,
    ListProductsRequest,
    ListProductsResponse,
    Product,
)
from .types.products_common import (
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
    "ProductInputsServiceAsyncClient",
    "ProductsServiceAsyncClient",
    "AgeGroup",
    "AutomatedDiscounts",
    "Availability",
    "CarrierTransitTimeOption",
    "CertificationAuthority",
    "CertificationName",
    "CloudExportAdditionalProperties",
    "Condition",
    "CreditType",
    "DeleteProductInputRequest",
    "DigitalSourceType",
    "EnergyEfficiencyClass",
    "FreeShippingThreshold",
    "Gender",
    "GetProductRequest",
    "HandlingCutoffTime",
    "InsertProductInputRequest",
    "ListProductsRequest",
    "ListProductsResponse",
    "LoyaltyPoints",
    "LoyaltyProgram",
    "Pause",
    "PickupCost",
    "PickupMethod",
    "PickupSla",
    "Product",
    "ProductAttributes",
    "ProductCertification",
    "ProductDetail",
    "ProductDimension",
    "ProductInput",
    "ProductInputsServiceClient",
    "ProductInstallment",
    "ProductMinimumOrderValue",
    "ProductStatus",
    "ProductSustainabilityIncentive",
    "ProductWeight",
    "ProductsServiceClient",
    "Shipping",
    "ShippingDimension",
    "ShippingWeight",
    "SizeSystem",
    "SizeType",
    "StructuredDescription",
    "StructuredTitle",
    "SubscriptionCost",
    "SubscriptionPeriod",
    "UnitPricingBaseMeasure",
    "UnitPricingMeasure",
    "UpdateProductInputRequest",
)

api_core.check_python_version("google.shopping.merchant_products_v1")
api_core.check_dependency_versions("google.shopping.merchant_products_v1")
