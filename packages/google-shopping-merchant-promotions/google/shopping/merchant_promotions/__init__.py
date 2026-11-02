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
from google.shopping.merchant_promotions import gapic_version as package_version

__version__ = package_version.__version__


from google.shopping.merchant_promotions_v1.services.promotions_service.async_client import (
    PromotionsServiceAsyncClient,
)
from google.shopping.merchant_promotions_v1.services.promotions_service.client import (
    PromotionsServiceClient,
)
from google.shopping.merchant_promotions_v1.types.promotions import (
    GetPromotionRequest,
    InsertPromotionRequest,
    ListPromotionsRequest,
    ListPromotionsResponse,
    Promotion,
)
from google.shopping.merchant_promotions_v1.types.promotions_common import (
    Attributes,
    CouponValueType,
    OfferType,
    ProductApplicability,
    PromotionStatus,
    RedemptionChannel,
    StoreApplicability,
)

__all__ = (
    "PromotionsServiceClient",
    "PromotionsServiceAsyncClient",
    "GetPromotionRequest",
    "InsertPromotionRequest",
    "ListPromotionsRequest",
    "ListPromotionsResponse",
    "Promotion",
    "Attributes",
    "PromotionStatus",
    "CouponValueType",
    "OfferType",
    "ProductApplicability",
    "RedemptionChannel",
    "StoreApplicability",
)
