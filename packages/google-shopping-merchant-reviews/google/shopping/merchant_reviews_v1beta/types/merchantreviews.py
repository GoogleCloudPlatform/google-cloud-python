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

from google.shopping.merchant_reviews_v1beta.types import merchantreviews_common

__protobuf__ = proto.module(
    package="google.shopping.merchant.reviews.v1beta",
    manifest={
        "GetMerchantReviewRequest",
        "DeleteMerchantReviewRequest",
        "ListMerchantReviewsRequest",
        "InsertMerchantReviewRequest",
        "ListMerchantReviewsResponse",
        "MerchantReview",
    },
)


class GetMerchantReviewRequest(proto.Message):
    r"""Request message for the ``GetMerchantReview`` method.

    Attributes:
        name (str):
            Required. The ID of the merchant review.
            Format:
            accounts/{account}/merchantReviews/{merchantReview}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteMerchantReviewRequest(proto.Message):
    r"""Request message for the ``DeleteMerchantReview`` method.

    Attributes:
        name (str):
            Required. The ID of the merchant review.
            Format:
            accounts/{account}/merchantReviews/{merchantReview}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListMerchantReviewsRequest(proto.Message):
    r"""Request message for the ``ListMerchantsReview`` method.

    Attributes:
        parent (str):
            Required. The account to list merchant
            reviews for. Format: accounts/{account}
        page_size (int):
            Optional. The maximum number of merchant
            reviews to return. The service can return fewer
            than this value. The maximum value is 1000;
            values above 1000 are coerced to 1000. If
            unspecified, the maximum number of reviews is
            returned.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListMerchantReviews`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListMerchantReviews`` must match the call that provided
            the page token.
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


class InsertMerchantReviewRequest(proto.Message):
    r"""Request message for the ``InsertMerchantReview`` method.

    Attributes:
        parent (str):
            Required. The account where the merchant
            review will be inserted. Format:
            accounts/{account}
        merchant_review (google.shopping.merchant_reviews_v1beta.types.MerchantReview):
            Required. The merchant review to insert.
        data_source (str):
            Required. The data source of the
            `merchantreview <https://support.google.com/merchants/answer/7045996?sjid=5253581244217581976-EU>`__
            Format: ``accounts/{account}/dataSources/{datasource}``.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    merchant_review: "MerchantReview" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="MerchantReview",
    )
    data_source: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListMerchantReviewsResponse(proto.Message):
    r"""Response message for the ``ListMerchantsReview`` method.

    Attributes:
        merchant_reviews (MutableSequence[google.shopping.merchant_reviews_v1beta.types.MerchantReview]):
            The merchant review.
        next_page_token (str):
            The token to retrieve the next page of
            results.
    """

    @property
    def raw_page(self):
        return self

    merchant_reviews: MutableSequence["MerchantReview"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="MerchantReview",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class MerchantReview(proto.Message):
    r"""A review for a merchant. For more information, see `Introduction to
    Merchant Review
    Feeds <https://developers.google.com/merchant-review-feeds>`__

    Attributes:
        name (str):
            Identifier. The name of the merchant review. Format:
            ``"{merchantreview.name=accounts/{account}/merchantReviews/{merchantReview}}"``
        merchant_review_id (str):
            Required. The user provided merchant review
            ID to uniquely identify the merchant review.
        merchant_review_attributes (google.shopping.merchant_reviews_v1beta.types.MerchantReviewAttributes):
            Optional. A list of merchant review
            attributes.
        custom_attributes (MutableSequence[google.shopping.type.types.CustomAttribute]):
            Optional. A list of custom (merchant-provided) attributes.
            It can also be used for submitting any attribute of the data
            specification in its generic form (for example,
            ``{ "name": "size type", "value": "regular" }``). This is
            useful for submitting attributes not explicitly exposed by
            the API, such as experimental attributes. Maximum allowed
            number of characters for each custom attribute is 10240
            (represents sum of characters for name and value). Maximum
            2500 custom attributes can be set per product, with total
            size of 102.4kB. Underscores in custom attribute names are
            replaced by spaces upon insertion.
        data_source (str):
            Output only. The primary data source of the
            merchant review.
        merchant_review_status (google.shopping.merchant_reviews_v1beta.types.MerchantReviewStatus):
            Output only. The status of a merchant review,
            data validation issues, that is, information
            about a merchant review computed asynchronously.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    merchant_review_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    merchant_review_attributes: merchantreviews_common.MerchantReviewAttributes = (
        proto.Field(
            proto.MESSAGE,
            number=3,
            message=merchantreviews_common.MerchantReviewAttributes,
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
    merchant_review_status: merchantreviews_common.MerchantReviewStatus = proto.Field(
        proto.MESSAGE,
        number=6,
        message=merchantreviews_common.MerchantReviewStatus,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
