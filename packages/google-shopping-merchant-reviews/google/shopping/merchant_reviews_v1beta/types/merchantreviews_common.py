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

import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore
from google.shopping.type.types import types

__protobuf__ = proto.module(
    package="google.shopping.merchant.reviews.v1beta",
    manifest={
        "MerchantReviewAttributes",
        "MerchantReviewStatus",
    },
)


class MerchantReviewAttributes(proto.Message):
    r"""Attributes.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        merchant_id (str):
            Required. Must be unique and stable across
            all requests. In other words, if a request today
            and another 90 days ago refer to the same
            merchant, they must have the same id.

            This field is a member of `oneof`_ ``_merchant_id``.
        merchant_display_name (str):
            Optional. Human-readable display name for the
            merchant.

            This field is a member of `oneof`_ ``_merchant_display_name``.
        merchant_link (str):
            Optional. URL to the merchant's main website.
            Do not use a redirect URL for this value. In
            other words, the value should point directly to
            the merchant's site.

            This field is a member of `oneof`_ ``_merchant_link``.
        merchant_rating_link (str):
            Optional. URL to the landing page that hosts
            the reviews for this merchant. Do not use a
            redirect URL.

            This field is a member of `oneof`_ ``_merchant_rating_link``.
        min_rating (int):
            Optional. The minimum possible number for the
            rating. This should be the worst possible rating
            and should not be a value for no rating.

            This field is a member of `oneof`_ ``_min_rating``.
        max_rating (int):
            Optional. The maximum possible number for the
            rating. The value of the max rating must be
            greater than the value of the min rating.

            This field is a member of `oneof`_ ``_max_rating``.
        rating (float):
            Optional. The reviewer's overall rating of
            the merchant.

            This field is a member of `oneof`_ ``_rating``.
        title (str):
            Optional. The title of the review.

            This field is a member of `oneof`_ ``_title``.
        content (str):
            Required. This should be any freeform text
            provided by the user and should not be
            truncated. If multiple responses to different
            questions are provided, all responses should be
            included, with the minimal context for the
            responses to make sense. Context should not be
            provided if questions were left unanswered.

            This field is a member of `oneof`_ ``_content``.
        reviewer_id (str):
            Optional. A permanent, unique identifier for
            the author of the review in the publisher's
            system.

            This field is a member of `oneof`_ ``_reviewer_id``.
        reviewer_username (str):
            Optional. Display name of the review author.

            This field is a member of `oneof`_ ``_reviewer_username``.
        is_anonymous (bool):
            Optional. Set to true if the reviewer should
            remain anonymous.

            This field is a member of `oneof`_ ``_is_anonymous``.
        collection_method (google.shopping.merchant_reviews_v1beta.types.MerchantReviewAttributes.CollectionMethod):
            Optional. The method used to collect the
            review.

            This field is a member of `oneof`_ ``_collection_method``.
        review_time (google.protobuf.timestamp_pb2.Timestamp):
            Required. The timestamp indicating when the
            review was written.

            This field is a member of `oneof`_ ``_review_time``.
        review_language (str):
            Optional. The language of the review defined
            by BCP-47 language code.

            This field is a member of `oneof`_ ``_review_language``.
        review_country (str):
            Optional. The country where the reviewer made
            the order defined by ISO 3166-1 Alpha-2 Country
            Code.

            This field is a member of `oneof`_ ``_review_country``.
    """

    class CollectionMethod(proto.Enum):
        r"""The method used to collect the review.

        Values:
            COLLECTION_METHOD_UNSPECIFIED (0):
                Collection method unspecified.
            MERCHANT_UNSOLICITED (1):
                The user was not responding to a specific
                solicitation when they submitted the review.
            POINT_OF_SALE (2):
                The user submitted the review in response to
                a solicitation when the user placed an order.
            AFTER_FULFILLMENT (3):
                The user submitted the review in response to
                a solicitation after fulfillment of the user's
                order.
        """

        COLLECTION_METHOD_UNSPECIFIED = 0
        MERCHANT_UNSOLICITED = 1
        POINT_OF_SALE = 2
        AFTER_FULFILLMENT = 3

    merchant_id: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    merchant_display_name: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    merchant_link: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )
    merchant_rating_link: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )
    min_rating: int = proto.Field(
        proto.INT64,
        number=5,
        optional=True,
    )
    max_rating: int = proto.Field(
        proto.INT64,
        number=6,
        optional=True,
    )
    rating: float = proto.Field(
        proto.DOUBLE,
        number=7,
        optional=True,
    )
    title: str = proto.Field(
        proto.STRING,
        number=8,
        optional=True,
    )
    content: str = proto.Field(
        proto.STRING,
        number=9,
        optional=True,
    )
    reviewer_id: str = proto.Field(
        proto.STRING,
        number=10,
        optional=True,
    )
    reviewer_username: str = proto.Field(
        proto.STRING,
        number=11,
        optional=True,
    )
    is_anonymous: bool = proto.Field(
        proto.BOOL,
        number=12,
        optional=True,
    )
    collection_method: CollectionMethod = proto.Field(
        proto.ENUM,
        number=13,
        optional=True,
        enum=CollectionMethod,
    )
    review_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=14,
        optional=True,
        message=timestamp_pb2.Timestamp,
    )
    review_language: str = proto.Field(
        proto.STRING,
        number=15,
        optional=True,
    )
    review_country: str = proto.Field(
        proto.STRING,
        number=16,
        optional=True,
    )


class MerchantReviewStatus(proto.Message):
    r"""The status of a merchant review, data validation issues, that
    is, information about a merchant review computed asynchronously.

    Attributes:
        destination_statuses (MutableSequence[google.shopping.merchant_reviews_v1beta.types.MerchantReviewStatus.MerchantReviewDestinationStatus]):
            Output only. The intended destinations for
            the merchant review.
        item_level_issues (MutableSequence[google.shopping.merchant_reviews_v1beta.types.MerchantReviewStatus.MerchantReviewItemLevelIssue]):
            Output only. A list of all issues associated
            with the merchant review.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Date on which the item has been created, in
            `ISO 8601 <http://en.wikipedia.org/wiki/ISO_8601>`__ format.
        last_update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Date on which the item has been last updated,
            in `ISO 8601 <http://en.wikipedia.org/wiki/ISO_8601>`__
            format.
    """

    class MerchantReviewDestinationStatus(proto.Message):
        r"""The destination status of the merchant review status.

        Attributes:
            reporting_context (google.shopping.type.types.ReportingContext.ReportingContextEnum):
                Output only. The name of the reporting
                context.
        """

        reporting_context: types.ReportingContext.ReportingContextEnum = proto.Field(
            proto.ENUM,
            number=1,
            enum=types.ReportingContext.ReportingContextEnum,
        )

    class MerchantReviewItemLevelIssue(proto.Message):
        r"""The ItemLevelIssue of the merchant review status.

        Attributes:
            code (str):
                Output only. The error code of the issue.
            severity (google.shopping.merchant_reviews_v1beta.types.MerchantReviewStatus.MerchantReviewItemLevelIssue.Severity):
                Output only. How this issue affects serving
                of the merchant review.
            resolution (str):
                Output only. Whether the issue can be
                resolved by the merchant.
            attribute (str):
                Output only. The attribute's name, if the
                issue is caused by a single attribute.
            reporting_context (google.shopping.type.types.ReportingContext.ReportingContextEnum):
                Output only. The reporting context the issue
                applies to.
            description (str):
                Output only. A short issue description in
                English.
            detail (str):
                Output only. A detailed issue description in
                English.
            documentation (str):
                Output only. The URL of a web page to help
                with resolving this issue.
        """

        class Severity(proto.Enum):
            r"""How the issue affects the serving of the merchant review.

            Values:
                SEVERITY_UNSPECIFIED (0):
                    Not specified.
                NOT_IMPACTED (1):
                    This issue represents a warning and does not
                    have a direct affect on the merchant review.
                DISAPPROVED (2):
                    Issue disapproves the merchant review.
            """

            SEVERITY_UNSPECIFIED = 0
            NOT_IMPACTED = 1
            DISAPPROVED = 2

        code: str = proto.Field(
            proto.STRING,
            number=1,
        )
        severity: "MerchantReviewStatus.MerchantReviewItemLevelIssue.Severity" = (
            proto.Field(
                proto.ENUM,
                number=2,
                enum="MerchantReviewStatus.MerchantReviewItemLevelIssue.Severity",
            )
        )
        resolution: str = proto.Field(
            proto.STRING,
            number=3,
        )
        attribute: str = proto.Field(
            proto.STRING,
            number=4,
        )
        reporting_context: types.ReportingContext.ReportingContextEnum = proto.Field(
            proto.ENUM,
            number=5,
            enum=types.ReportingContext.ReportingContextEnum,
        )
        description: str = proto.Field(
            proto.STRING,
            number=6,
        )
        detail: str = proto.Field(
            proto.STRING,
            number=7,
        )
        documentation: str = proto.Field(
            proto.STRING,
            number=8,
        )

    destination_statuses: MutableSequence[MerchantReviewDestinationStatus] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=3,
            message=MerchantReviewDestinationStatus,
        )
    )
    item_level_issues: MutableSequence[MerchantReviewItemLevelIssue] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=4,
            message=MerchantReviewItemLevelIssue,
        )
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    last_update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
