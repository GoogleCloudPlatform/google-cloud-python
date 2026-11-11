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
from google.shopping.merchant_reviews import gapic_version as package_version

__version__ = package_version.__version__


from google.shopping.merchant_reviews_v1.services.product_reviews_service.async_client import (
    ProductReviewsServiceAsyncClient,
)
from google.shopping.merchant_reviews_v1.services.product_reviews_service.client import (
    ProductReviewsServiceClient,
)
from google.shopping.merchant_reviews_v1.types.productreviews import (
    DeleteProductReviewRequest,
    GetProductReviewRequest,
    InsertProductReviewRequest,
    ListProductReviewsRequest,
    ListProductReviewsResponse,
    ProductReview,
)
from google.shopping.merchant_reviews_v1.types.productreviews_common import (
    ProductReviewAttributes,
    ProductReviewStatus,
)

__all__ = (
    "ProductReviewsServiceClient",
    "ProductReviewsServiceAsyncClient",
    "DeleteProductReviewRequest",
    "GetProductReviewRequest",
    "InsertProductReviewRequest",
    "ListProductReviewsRequest",
    "ListProductReviewsResponse",
    "ProductReview",
    "ProductReviewAttributes",
    "ProductReviewStatus",
)
