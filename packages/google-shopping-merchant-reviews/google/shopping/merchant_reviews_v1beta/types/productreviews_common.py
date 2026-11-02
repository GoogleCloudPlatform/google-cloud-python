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
        "ProductReviewAttributes",
        "ProductReviewStatus",
    },
)


class ProductReviewAttributes(proto.Message):
    r"""Attributes.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        aggregator_name (str):
            Optional. The name of the aggregator of the
            product reviews.
            A publisher may use a reviews aggregator to
            manage reviews and provide the feeds. This
            element indicates the use of an aggregator and
            contains information about the aggregator.

            This field is a member of `oneof`_ ``_aggregator_name``.
        subclient_name (str):
            Optional. The name of the subclient of the
            product reviews.
            The subclient is an identifier of the product
            review source. It should be equivalent to the
            directory provided in the file data source path.

            This field is a member of `oneof`_ ``_subclient_name``.
        publisher_name (str):
            Optional. The name of the publisher of the
            product reviews.
            The information about the publisher, which may
            be a retailer, manufacturer, reviews service
            company, or any entity that publishes product
            reviews.

            This field is a member of `oneof`_ ``_publisher_name``.
        publisher_favicon (str):
            Optional. A link to the company favicon of
            the publisher. The image dimensions should be
            favicon size: 16x16 pixels. The image format
            should be GIF, JPG or PNG.

            This field is a member of `oneof`_ ``_publisher_favicon``.
        reviewer_id (str):
            Optional. The author of the product review.

            A permanent, unique identifier for the author of
            the review in the publisher's system.

            This field is a member of `oneof`_ ``_reviewer_id``.
        reviewer_is_anonymous (bool):
            Optional. Set to true if the reviewer should
            remain anonymous.

            This field is a member of `oneof`_ ``_reviewer_is_anonymous``.
        reviewer_username (str):
            Optional. The name of the reviewer of the
            product review.

            This field is a member of `oneof`_ ``_reviewer_username``.
        review_language (str):
            Optional. The language of the review defined
            by BCP-47 language code.

            This field is a member of `oneof`_ ``_review_language``.
        review_country (str):
            Optional. The country of the review defined
            by ISO 3166-1 Alpha-2 Country Code.

            This field is a member of `oneof`_ ``_review_country``.
        review_time (google.protobuf.timestamp_pb2.Timestamp):
            Required. The timestamp indicating when the
            review was written.
        title (str):
            Optional. The title of the review.

            This field is a member of `oneof`_ ``_title``.
        content (str):
            Optional. The content of the review. If
            empty, the content might still get populated
            from pros and cons.

            This field is a member of `oneof`_ ``_content``.
        pros (MutableSequence[str]):
            Optional. Contains the advantages based on
            the opinion of the reviewer. Omit boilerplate
            text like "pro:" unless it was written by the
            reviewer.
        cons (MutableSequence[str]):
            Optional. Contains the disadvantages based on
            the opinion of the reviewer. Omit boilerplate
            text like "con:" unless it was written by the
            reviewer.
        review_link (google.shopping.merchant_reviews_v1beta.types.ProductReviewAttributes.ReviewLink):
            Optional. The URI of the review landing page.
        reviewer_image_links (MutableSequence[str]):
            Optional. A URI to an image of the reviewed
            product created by the review author. The URI
            does not have to end with an image file
            extension.
        min_rating (int):
            Optional. Contains the ratings associated
            with the review. The minimum possible number for
            the rating. This should be the worst possible
            rating and should not be a value for no rating.

            This field is a member of `oneof`_ ``_min_rating``.
        max_rating (int):
            Optional. The maximum possible number for the
            rating. The value of the max rating must be
            greater than the value of the min attribute.

            This field is a member of `oneof`_ ``_max_rating``.
        rating (float):
            Optional. The reviewer's overall rating of
            the product.

            This field is a member of `oneof`_ ``_rating``.
        product_names (MutableSequence[str]):
            Optional. Descriptive name of a product.
        product_links (MutableSequence[str]):
            Optional. The URI of the product. This URI can have the same
            value as the ``review_link`` element, if the review URI and
            the product URI are the same.
        asins (MutableSequence[str]):
            Optional. Contains ASINs (Amazon Standard
            Identification Numbers) associated with a
            product.
        gtins (MutableSequence[str]):
            Optional. Contains GTINs (global trade item
            numbers) associated with a product. Sub-types of
            GTINs (e.g. UPC, EAN, ISBN, JAN) are supported.
        mpns (MutableSequence[str]):
            Optional. Contains MPNs (manufacturer part
            numbers) associated with a product.
        skus (MutableSequence[str]):
            Optional. Contains SKUs (stock keeping units)
            associated with a product. Often this matches
            the product Offer Id in the product feed.
        brands (MutableSequence[str]):
            Optional. Contains brand names associated
            with a product.
        is_spam (bool):
            Optional. Indicates whether the review is
            marked as spam in the publisher's system.

            This field is a member of `oneof`_ ``_is_spam``.
        is_verified_purchase (bool):
            Optional. Indicates whether the reviewer's
            purchase is verified.

            This field is a member of `oneof`_ ``_is_verified_purchase``.
        is_incentivized_review (bool):
            Optional. Indicates whether the review is
            incentivized.

            This field is a member of `oneof`_ ``_is_incentivized_review``.
        collection_method (google.shopping.merchant_reviews_v1beta.types.ProductReviewAttributes.CollectionMethod):
            Optional. The method used to collect the
            review.
        transaction_id (str):
            Optional. A permanent, unique identifier for
            the transaction associated with the review in
            the publisher's system. This ID can be used to
            indicate that multiple reviews are associated
            with the same transaction.
    """

    class CollectionMethod(proto.Enum):
        r"""The method used to collect the review.

        Values:
            COLLECTION_METHOD_UNSPECIFIED (0):
                Collection method unspecified.
            UNSOLICITED (1):
                The user was not responding to a specific
                solicitation when they submitted the review.
            POST_FULFILLMENT (2):
                The user submitted the review in response to
                a solicitation after fulfillment of the user's
                order.
        """

        COLLECTION_METHOD_UNSPECIFIED = 0
        UNSOLICITED = 1
        POST_FULFILLMENT = 2

    class ReviewLink(proto.Message):
        r"""The URI of the review landing page.

        Attributes:
            type_ (google.shopping.merchant_reviews_v1beta.types.ProductReviewAttributes.ReviewLink.Type):
                Optional. Type of the review URI.
            link (str):
                Optional. The URI of the review landing page. For example:
                ``http://www.example.com/review_5.html``.
        """

        class Type(proto.Enum):
            r"""Type of the review URI.

            Values:
                TYPE_UNSPECIFIED (0):
                    Type unspecified.
                SINGLETON (1):
                    The review page contains only this single
                    review.
                GROUP (2):
                    The review page contains a group of reviews
                    including this review.
            """

            TYPE_UNSPECIFIED = 0
            SINGLETON = 1
            GROUP = 2

        type_: "ProductReviewAttributes.ReviewLink.Type" = proto.Field(
            proto.ENUM,
            number=1,
            enum="ProductReviewAttributes.ReviewLink.Type",
        )
        link: str = proto.Field(
            proto.STRING,
            number=2,
        )

    aggregator_name: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    subclient_name: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    publisher_name: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )
    publisher_favicon: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )
    reviewer_id: str = proto.Field(
        proto.STRING,
        number=5,
        optional=True,
    )
    reviewer_is_anonymous: bool = proto.Field(
        proto.BOOL,
        number=6,
        optional=True,
    )
    reviewer_username: str = proto.Field(
        proto.STRING,
        number=7,
        optional=True,
    )
    review_language: str = proto.Field(
        proto.STRING,
        number=8,
        optional=True,
    )
    review_country: str = proto.Field(
        proto.STRING,
        number=9,
        optional=True,
    )
    review_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10,
        message=timestamp_pb2.Timestamp,
    )
    title: str = proto.Field(
        proto.STRING,
        number=11,
        optional=True,
    )
    content: str = proto.Field(
        proto.STRING,
        number=12,
        optional=True,
    )
    pros: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=13,
    )
    cons: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=14,
    )
    review_link: ReviewLink = proto.Field(
        proto.MESSAGE,
        number=15,
        message=ReviewLink,
    )
    reviewer_image_links: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=16,
    )
    min_rating: int = proto.Field(
        proto.INT64,
        number=17,
        optional=True,
    )
    max_rating: int = proto.Field(
        proto.INT64,
        number=18,
        optional=True,
    )
    rating: float = proto.Field(
        proto.DOUBLE,
        number=19,
        optional=True,
    )
    product_names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=20,
    )
    product_links: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=21,
    )
    asins: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=22,
    )
    gtins: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=23,
    )
    mpns: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=24,
    )
    skus: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=25,
    )
    brands: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=26,
    )
    is_spam: bool = proto.Field(
        proto.BOOL,
        number=27,
        optional=True,
    )
    is_verified_purchase: bool = proto.Field(
        proto.BOOL,
        number=30,
        optional=True,
    )
    is_incentivized_review: bool = proto.Field(
        proto.BOOL,
        number=31,
        optional=True,
    )
    collection_method: CollectionMethod = proto.Field(
        proto.ENUM,
        number=28,
        enum=CollectionMethod,
    )
    transaction_id: str = proto.Field(
        proto.STRING,
        number=29,
    )


class ProductReviewStatus(proto.Message):
    r"""Product review status.

    Attributes:
        destination_statuses (MutableSequence[google.shopping.merchant_reviews_v1beta.types.ProductReviewStatus.ProductReviewDestinationStatus]):
            Output only. The intended destinations for
            the product review.
        item_level_issues (MutableSequence[google.shopping.merchant_reviews_v1beta.types.ProductReviewStatus.ProductReviewItemLevelIssue]):
            Output only. A list of all issues associated
            with the product review.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Date on which the item has been created, in
            `ISO 8601 <http://en.wikipedia.org/wiki/ISO_8601>`__ format.
        last_update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Date on which the item has been last updated,
            in `ISO 8601 <http://en.wikipedia.org/wiki/ISO_8601>`__
            format.
    """

    class ProductReviewDestinationStatus(proto.Message):
        r"""The destination status of the product review status.

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

    class ProductReviewItemLevelIssue(proto.Message):
        r"""The ItemLevelIssue of the product review status.

        Attributes:
            code (str):
                Output only. The error code of the issue.
            severity (google.shopping.merchant_reviews_v1beta.types.ProductReviewStatus.ProductReviewItemLevelIssue.Severity):
                Output only. How this issue affects serving
                of the product review.
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
            r"""How the issue affects the serving of the product review.

            Values:
                SEVERITY_UNSPECIFIED (0):
                    Not specified.
                NOT_IMPACTED (1):
                    This issue represents a warning and does not
                    have a direct affect on the product review.
                DISAPPROVED (2):
                    Issue disapproves the product review.
            """

            SEVERITY_UNSPECIFIED = 0
            NOT_IMPACTED = 1
            DISAPPROVED = 2

        code: str = proto.Field(
            proto.STRING,
            number=1,
        )
        severity: "ProductReviewStatus.ProductReviewItemLevelIssue.Severity" = (
            proto.Field(
                proto.ENUM,
                number=2,
                enum="ProductReviewStatus.ProductReviewItemLevelIssue.Severity",
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

    destination_statuses: MutableSequence[ProductReviewDestinationStatus] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=3,
            message=ProductReviewDestinationStatus,
        )
    )
    item_level_issues: MutableSequence[ProductReviewItemLevelIssue] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=4,
            message=ProductReviewItemLevelIssue,
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
