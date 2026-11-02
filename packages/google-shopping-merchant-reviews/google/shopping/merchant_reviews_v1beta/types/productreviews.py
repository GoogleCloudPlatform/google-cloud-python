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
from __future__ import annotations

from typing import MutableMapping, MutableSequence

import proto  # type: ignore
from google.shopping.type.types import types

from google.shopping.merchant_reviews_v1beta.types import productreviews_common

__protobuf__ = proto.module(
    package="google.shopping.merchant.reviews.v1beta",
    manifest={
        "GetProductReviewRequest",
        "DeleteProductReviewRequest",
        "ListProductReviewsRequest",
        "InsertProductReviewRequest",
        "ListProductReviewsResponse",
        "ProductReview",
    },
)


class GetProductReviewRequest(proto.Message):
    r"""Request message for the GetProductReview method.

    Attributes:
        name (str):
            Required. The ID of the merchant review.
            Format:
            accounts/{account}/productReviews/{productReview}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteProductReviewRequest(proto.Message):
    r"""Request message for the ``DeleteProductReview`` method.

    Attributes:
        name (str):
            Required. The ID of the Product review.
            Format:
            accounts/{account}/productReviews/{productReview}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListProductReviewsRequest(proto.Message):
    r"""Request message for the ListProductReviews method.

    Attributes:
        parent (str):
            Required. The account to list product reviews
            for. Format: accounts/{account}
        page_size (int):
            Optional. The maximum number of products to
            return. The service may return fewer than this
            value.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListProductReviews`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListProductReviews`` must match the call that provided the
            page token.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class InsertProductReviewRequest(proto.Message):
    r"""Request message for the ``InsertProductReview`` method.

    Attributes:
        parent (str):
            Required. The account where the product
            review will be inserted. Format:
            accounts/{account}
        product_review (google.shopping.merchant_reviews_v1beta.types.ProductReview):
            Required. The product review to insert.
        data_source (str):
            Required. Format:
            ``accounts/{account}/dataSources/{datasource}``.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    product_review: "ProductReview" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ProductReview",
    )
    data_source: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListProductReviewsResponse(proto.Message):
    r"""response message for the ListProductReviews method.

    Attributes:
        product_reviews (MutableSequence[google.shopping.merchant_reviews_v1beta.types.ProductReview]):
            The product review.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    product_reviews: MutableSequence["ProductReview"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ProductReview",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ProductReview(proto.Message):
    r"""A review for a product. For more information, see `Introduction to
    Product Review
    Feeds <https://developers.google.com/product-review-feeds>`__

    Attributes:
        name (str):
            Identifier. The name of the product review. Format:
            ``"{productreview.name=accounts/{account}/productReviews/{productReview}}"``
        product_review_id (str):
            Required. The permanent, unique identifier
            for the product review in the publisher’s
            system.
        product_review_attributes (google.shopping.merchant_reviews_v1beta.types.ProductReviewAttributes):
            Optional. A list of product review
            attributes.
        custom_attributes (MutableSequence[google.shopping.type.types.CustomAttribute]):
            Optional. A list of custom
            (merchant-provided) attributes.
        data_source (str):
            Output only. The primary data source of the
            product review.
        product_review_status (google.shopping.merchant_reviews_v1beta.types.ProductReviewStatus):
            Output only. The status of a product review,
            data validation issues, that is, information
            about a product review computed asynchronously.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    product_review_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    product_review_attributes: productreviews_common.ProductReviewAttributes = (
        proto.Field(
            proto.MESSAGE,
            number=3,
            message=productreviews_common.ProductReviewAttributes,
        )
    )
    custom_attributes: MutableSequence[types.CustomAttribute] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=types.CustomAttribute,
    )
    data_source: str = proto.Field(
        proto.STRING,
        number=5,
    )
    product_review_status: productreviews_common.ProductReviewStatus = proto.Field(
        proto.MESSAGE,
        number=6,
        message=productreviews_common.ProductReviewStatus,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
