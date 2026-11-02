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
import google.type.interval_pb2 as interval_pb2  # type: ignore
import proto  # type: ignore
from google.shopping.type.types import types

__protobuf__ = proto.module(
    package="google.shopping.merchant.promotions.v1",
    manifest={
        "ProductApplicability",
        "StoreApplicability",
        "OfferType",
        "RedemptionChannel",
        "CouponValueType",
        "Attributes",
        "PromotionStatus",
    },
)


class ProductApplicability(proto.Enum):
    r"""Which product or list of products the promotion applies to.

    Values:
        PRODUCT_APPLICABILITY_UNSPECIFIED (0):
            Which products the promotion applies to is
            unknown.
        ALL_PRODUCTS (1):
            Applicable to all products.
        SPECIFIC_PRODUCTS (2):
            Applicable to only a single product or list
            of products.
    """

    PRODUCT_APPLICABILITY_UNSPECIFIED = 0
    ALL_PRODUCTS = 1
    SPECIFIC_PRODUCTS = 2


class StoreApplicability(proto.Enum):
    r"""Store codes or list of store codes the promotion applies to.
    Only for Local inventory ads promotions.

    Values:
        STORE_APPLICABILITY_UNSPECIFIED (0):
            Which store codes the promotion applies to is
            unknown.
        ALL_STORES (1):
            Promotion applies to all stores.
        SPECIFIC_STORES (2):
            Promotion applies to only the specified
            stores.
    """

    STORE_APPLICABILITY_UNSPECIFIED = 0
    ALL_STORES = 1
    SPECIFIC_STORES = 2


class OfferType(proto.Enum):
    r"""Offer type of a promotion.

    Values:
        OFFER_TYPE_UNSPECIFIED (0):
            Unknown offer type.
        NO_CODE (1):
            Offer type without a code.
        GENERIC_CODE (2):
            Offer type with a code. Generic redemption code for the
            promotion is required when ``offerType`` = ``GENERIC_CODE``.
    """

    OFFER_TYPE_UNSPECIFIED = 0
    NO_CODE = 1
    GENERIC_CODE = 2


class RedemptionChannel(proto.Enum):
    r"""Channel of a promotion.

    Values:
        REDEMPTION_CHANNEL_UNSPECIFIED (0):
            Indicates that the channel is unspecified.
        IN_STORE (1):
            Indicates that the channel is in store. This is same as
            ``local`` channel used for ``products``.
        ONLINE (2):
            Indicates that the channel is online.
    """

    REDEMPTION_CHANNEL_UNSPECIFIED = 0
    IN_STORE = 1
    ONLINE = 2


class CouponValueType(proto.Enum):
    r"""`Coupon value
    type <https://support.google.com/merchants/answer/13861986>`__ of a
    promotion.

    Values:
        COUPON_VALUE_TYPE_UNSPECIFIED (0):
            Indicates that the coupon value type is
            unspecified.
        MONEY_OFF (1):
            Money off coupon value type.
        PERCENT_OFF (2):
            Percent off coupon value type.
        BUY_M_GET_N_MONEY_OFF (3):
            Buy M quantity, get N money off coupon value type.
            ``minimum_purchase_quantity`` and
            ``get_this_quantity_discounted`` must be present.
            ``money_off_amount`` must also be present.
        BUY_M_GET_N_PERCENT_OFF (4):
            Buy M quantity, get N percent off coupon value type.
            ``minimum_purchase_quantity`` and
            ``get_this_quantity_discounted`` must be present.
            ``percent_off_percentage`` must also be present.
        BUY_M_GET_MONEY_OFF (5):
            Buy M quantity, get money off. ``minimum_purchase_quantity``
            and ``money_off_amount`` must be present.
        BUY_M_GET_PERCENT_OFF (6):
            Buy M quantity, get money off. ``minimum_purchase_quantity``
            and ``percent_off_percentage`` must be present.
        FREE_GIFT (7):
            Free gift with description only.
        FREE_GIFT_WITH_VALUE (8):
            Free gift with monetary value.
        FREE_GIFT_WITH_ITEM_ID (9):
            Free gift with item ID.
        FREE_SHIPPING_STANDARD (10):
            Standard free shipping coupon value type.
            Only available for online promotions.
        FREE_SHIPPING_OVERNIGHT (11):
            Overnight free shipping coupon value type.
            Only available for online promotions.
        FREE_SHIPPING_TWO_DAY (12):
            Two day free shipping coupon value type. Only
            available for online promotions.
    """

    COUPON_VALUE_TYPE_UNSPECIFIED = 0
    MONEY_OFF = 1
    PERCENT_OFF = 2
    BUY_M_GET_N_MONEY_OFF = 3
    BUY_M_GET_N_PERCENT_OFF = 4
    BUY_M_GET_MONEY_OFF = 5
    BUY_M_GET_PERCENT_OFF = 6
    FREE_GIFT = 7
    FREE_GIFT_WITH_VALUE = 8
    FREE_GIFT_WITH_ITEM_ID = 9
    FREE_SHIPPING_STANDARD = 10
    FREE_SHIPPING_OVERNIGHT = 11
    FREE_SHIPPING_TWO_DAY = 12


class Attributes(proto.Message):
    r"""Attributes.

    Attributes:
        product_applicability (google.shopping.merchant_promotions_v1.types.ProductApplicability):
            Required. Applicability of the promotion to either all
            products or `only specific
            products <https://support.google.com/merchants/answer/6396257?ref_topic=6396150&sjid=17642868584668136159-NC>`__.
        offer_type (google.shopping.merchant_promotions_v1.types.OfferType):
            Required.
            `Type <https://support.google.com/merchants/answer/13837405?ref_topic=13773355&sjid=17642868584668136159-NC>`__
            of the promotion. Use this attribute to indicate whether or
            not customers need a coupon code to redeem your promotion.
        generic_redemption_code (str):
            Optional. Generic redemption code for the promotion. To be
            used with the ``offerType`` field and must meet the `minimum
            requirements <https://support.google.com/merchants/answer/13837405?ref_topic=13773355&sjid=17642868584668136159-NC>`__.
        long_title (str):
            Required. `Long
            title <https://support.google.com/merchants/answer/13838102?ref_topic=13773355&sjid=17642868584668136159-NC>`__
            for the promotion.
        coupon_value_type (google.shopping.merchant_promotions_v1.types.CouponValueType):
            Required. The [coupon value type]
            (https://support.google.com/merchants/answer/13861986?ref_topic=13773355&sjid=17642868584668136159-NC)
            attribute to signal the type of promotion that you are
            running. Depending on type of the selected coupon value
            `some attributes are
            required <https://support.google.com/merchants/answer/6393006?ref_topic=7322920>`__.
        promotion_destinations (MutableSequence[google.shopping.type.types.Destination.DestinationEnum]):
            Required. The list of destinations (also known as `Marketing
            methods <https://support.google.com/merchants/answer/15130232>`__)
            where the promotion applies to. If you don't specify a
            destination by including a supported value in your data
            source, your promotion will display in Shopping ads and free
            listings by default.

            You may have previously submitted the following values as
            destinations for your products: Shopping Actions, Surfaces
            across Google, Local surfaces across Google. To represent
            these values use ``FREE_LISTINGS``, ``FREE_LOCAL_LISTINGS``,
            ``LOCAL_INVENTORY_ADS``. For more details see `Promotion
            destination <https://support.google.com/merchants/answer/13837465?sjid=5155774230887277618-NC>`__
        item_id_inclusion (MutableSequence[str]):
            Optional. Product filter by `item
            ID <https://support.google.com/merchants/answer/13861565?ref_topic=13773355&sjid=17642868584668136159-NC>`__
            for the promotion. The product filter attributes only
            applies when the products eligible for promotion product
            applicability ``product_applicability`` attribute is set to
            `specific_products <https://support.google.com/merchants/answer/13837299?ref_topic=13773355&sjid=17642868584668136159-NC>`__.
        brand_inclusion (MutableSequence[str]):
            Optional. Product filter by brand for the promotion. The
            product filter attributes only applies when the products
            eligible for promotion product applicability
            ``product_applicability`` attribute is set to
            `specific_products <https://support.google.com/merchants/answer/13837299?ref_topic=13773355&sjid=17642868584668136159-NC>`__.
        item_group_id_inclusion (MutableSequence[str]):
            Optional. Product filter by item group ID for the promotion.
            The product filter attributes only applies when the products
            eligible for promotion product applicability
            [product_applicability] attribute is set to
            `specific_products <https://support.google.com/merchants/answer/13837299?ref_topic=13773355&sjid=17642868584668136159-NC>`__.
        product_type_inclusion (MutableSequence[str]):
            Optional. Product filter by product type for the promotion.
            The product filter attributes only applies when the products
            eligible for promotion product applicability
            ``product_applicability`` attribute is set to
            `specific_products <https://support.google.com/merchants/answer/13837299?ref_topic=13773355&sjid=17642868584668136159-NC>`__.
        item_id_exclusion (MutableSequence[str]):
            Optional. Product filter by `item ID
            exclusion <https://support.google.com/merchants/answer/13863524?ref_topic=13773355&sjid=17642868584668136159-NC>`__
            for the promotion. The product filter attributes only
            applies when the products eligible for promotion product
            applicability ``product_applicability`` attribute is set to
            `specific_products <https://support.google.com/merchants/answer/13837299?ref_topic=13773355&sjid=17642868584668136159-NC>`__.
        brand_exclusion (MutableSequence[str]):
            Optional. Product filter by `brand
            exclusion <https://support.google.com/merchants/answer/13861679?ref_topic=13773355&sjid=17642868584668136159-NC>`__
            for the promotion. The product filter attributes only
            applies when the products eligible for promotion product
            applicability ``product_applicability`` attribute is set to
            `specific_products <https://support.google.com/merchants/answer/13837299?ref_topic=13773355&sjid=17642868584668136159-NC>`__.
        item_group_id_exclusion (MutableSequence[str]):
            Optional. Product filter by `item group
            ID <https://support.google.com/merchants/answer/13837298?ref_topic=13773355&sjid=17642868584668136159-NC>`__.
            The product filter attributes only applies when the products
            eligible for promotion product applicability
            ``product_applicability`` attribute is set to
            `specific_products <https://support.google.com/merchants/answer/13837299?ref_topic=13773355&sjid=17642868584668136159-NC>`__.
            exclusion for the promotion.
        product_type_exclusion (MutableSequence[str]):
            Optional. Product filter by `product type
            exclusion <https://support.google.com/merchants/answer/13863746?ref_topic=13773355&sjid=17642868584668136159-NC>`__
            for the promotion. The product filter attributes only
            applies when the products eligible for promotion product
            applicability ``product_applicability`` attribute is set to
            `specific_products <https://support.google.com/merchants/answer/13837299?ref_topic=13773355&sjid=17642868584668136159-NC>`__.
        minimum_purchase_amount (google.shopping.type.types.Price):
            Optional. `Minimum purchase
            amount <https://support.google.com/merchants/answer/13837705?ref_topic=13773355&sjid=17642868584668136159-NC>`__
            for the promotion.
        minimum_purchase_quantity (int):

        limit_quantity (int):
            Optional. `Maximum purchase
            quantity <https://support.google.com/merchants/answer/13861564?ref_topic=13773355&sjid=17642868584668136159-NC>`__
            for the promotion.
        limit_value (google.shopping.type.types.Price):
            Optional. `Maximum product
            price <https://support.google.com/merchants/answer/2906014>`__
            for promotion.
        percent_off (int):
            Optional. The `percentage
            discount <https://support.google.com/merchants/answer/13837404?sjid=17642868584668136159-NC>`__
            offered in the promotion.
        money_off_amount (google.shopping.type.types.Price):
            Optional. The `money off
            amount <https://support.google.com/merchants/answer/13838101?ref_topic=13773355&sjid=17642868584668136159-NC>`__
            offered in the promotion.
        get_this_quantity_discounted (int):
            Optional. The number of items discounted in the promotion.
            The attribute is set when ``couponValueType`` is equal to
            ``buy_m_get_n_money_off`` or ``buy_m_get_n_percent_off``.
        free_gift_value (google.shopping.type.types.Price):
            Optional. `Free gift
            value <https://support.google.com/merchants/answer/13844477?ref_topic=13773355&sjid=17642868584668136159-NC>`__
            for the promotion.
        free_gift_description (str):
            Optional. `Free gift
            description <https://support.google.com/merchants/answer/13847245?ref_topic=13773355&sjid=17642868584668136159-NC>`__
            for the promotion.
        free_gift_item_id (str):
            Optional. `Free gift item
            ID <https://support.google.com/merchants/answer/13857152?ref_topic=13773355&sjid=17642868584668136159-NC>`__
            for the promotion.
        promotion_effective_time_period (google.type.interval_pb2.Interval):
            Required. ``TimePeriod`` representation of the promotion's
            effective dates. This attribute specifies that the promotion
            can be tested on your online store during this time period.
        promotion_display_time_period (google.type.interval_pb2.Interval):
            Optional. ``TimePeriod`` representation of the promotion's
            display dates. This attribute specifies the date and time
            frame when the promotion will be live on Google.com and
            Shopping ads. If the display time period for promotion
            ``promotion_display_time_period`` attribute is not
            specified, the promotion effective time period
            ``promotion_effective_time_period`` determines the date and
            time frame when the promotion will be live on Google.com and
            Shopping ads.
        store_applicability (google.shopping.merchant_promotions_v1.types.StoreApplicability):
            Optional. Whether the promotion applies to `all stores, or
            only specified
            stores <https://support.google.com/merchants/answer/13857563?sjid=17642868584668136159-NC>`__.
            Local Inventory ads promotions throw an error if no store
            applicability is included. An ``INVALID_ARGUMENT`` error is
            thrown if ``store_applicability`` is set to ``ALL_STORES``
            and ``store_codes_inclusion`` or ``score_code_exclusion`` is
            set to a value.
        store_codes_inclusion (MutableSequence[str]):
            Optional. `Store codes to
            include <https://support.google.com/merchants/answer/13857470?ref_topic=13773355&sjid=17642868584668136159-NC>`__
            for the promotion. The store filter attributes only applies
            when the ``store_applicability`` attribute is set to
            `specific_stores <https://support.google.com/merchants/answer/13857563?ref_topic=13773355&sjid=17642868584668136159-NC>`__.

            Store code (the store ID from your Business Profile) of the
            physical store the product is sold in. See the `Local
            product inventory data
            specification <https://support.google.com/merchants/answer/3061342>`__
            for more information.
        store_codes_exclusion (MutableSequence[str]):
            Optional. `Store codes to
            exclude <https://support.google.com/merchants/answer/13859586?ref_topic=13773355&sjid=17642868584668136159-NC>`__
            for the promotion. The store filter attributes only applies
            when the ``store_applicability`` attribute is set to
            `specific_stores <https://support.google.com/merchants/answer/13857563?ref_topic=13773355&sjid=17642868584668136159-NC>`__.
        promotion_url (str):
            Optional. URL to the page on the merchant's site where the
            promotion shows. Local Inventory ads promotions throw an
            error if no ``promotion_url`` is included. URL is used to
            confirm that the promotion is valid and can be redeemed.
    """

    product_applicability: "ProductApplicability" = proto.Field(
        proto.ENUM,
        number=1,
        enum="ProductApplicability",
    )
    offer_type: "OfferType" = proto.Field(
        proto.ENUM,
        number=2,
        enum="OfferType",
    )
    generic_redemption_code: str = proto.Field(
        proto.STRING,
        number=3,
    )
    long_title: str = proto.Field(
        proto.STRING,
        number=4,
    )
    coupon_value_type: "CouponValueType" = proto.Field(
        proto.ENUM,
        number=5,
        enum="CouponValueType",
    )
    promotion_destinations: MutableSequence[types.Destination.DestinationEnum] = (
        proto.RepeatedField(
            proto.ENUM,
            number=6,
            enum=types.Destination.DestinationEnum,
        )
    )
    item_id_inclusion: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=7,
    )
    brand_inclusion: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=8,
    )
    item_group_id_inclusion: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=9,
    )
    product_type_inclusion: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=10,
    )
    item_id_exclusion: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=11,
    )
    brand_exclusion: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=12,
    )
    item_group_id_exclusion: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=13,
    )
    product_type_exclusion: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=14,
    )
    minimum_purchase_amount: types.Price = proto.Field(
        proto.MESSAGE,
        number=15,
        message=types.Price,
    )
    minimum_purchase_quantity: int = proto.Field(
        proto.INT64,
        number=16,
    )
    limit_quantity: int = proto.Field(
        proto.INT64,
        number=17,
    )
    limit_value: types.Price = proto.Field(
        proto.MESSAGE,
        number=18,
        message=types.Price,
    )
    percent_off: int = proto.Field(
        proto.INT64,
        number=19,
    )
    money_off_amount: types.Price = proto.Field(
        proto.MESSAGE,
        number=20,
        message=types.Price,
    )
    get_this_quantity_discounted: int = proto.Field(
        proto.INT64,
        number=21,
    )
    free_gift_value: types.Price = proto.Field(
        proto.MESSAGE,
        number=22,
        message=types.Price,
    )
    free_gift_description: str = proto.Field(
        proto.STRING,
        number=23,
    )
    free_gift_item_id: str = proto.Field(
        proto.STRING,
        number=24,
    )
    promotion_effective_time_period: interval_pb2.Interval = proto.Field(
        proto.MESSAGE,
        number=25,
        message=interval_pb2.Interval,
    )
    promotion_display_time_period: interval_pb2.Interval = proto.Field(
        proto.MESSAGE,
        number=26,
        message=interval_pb2.Interval,
    )
    store_applicability: "StoreApplicability" = proto.Field(
        proto.ENUM,
        number=28,
        enum="StoreApplicability",
    )
    store_codes_inclusion: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=29,
    )
    store_codes_exclusion: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=30,
    )
    promotion_url: str = proto.Field(
        proto.STRING,
        number=31,
    )


class PromotionStatus(proto.Message):
    r"""The status of the promotion.

    Attributes:
        destination_statuses (MutableSequence[google.shopping.merchant_promotions_v1.types.PromotionStatus.DestinationStatus]):
            Output only. The intended destinations for
            the promotion.
        item_level_issues (MutableSequence[google.shopping.merchant_promotions_v1.types.PromotionStatus.ItemLevelIssue]):
            Output only. A list of issues associated with
            the promotion.
        creation_date (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Date on which the promotion has been created in
            `ISO 8601 <http://en.wikipedia.org/wiki/ISO_8601>`__ format:
            Date, time, and offset, for example
            ``2020-01-02T09:00:00+01:00`` or ``2020-01-02T09:00:00Z``
        last_update_date (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Date on which the promotion status has been
            last updated in `ISO
            8601 <http://en.wikipedia.org/wiki/ISO_8601>`__ format:
            Date, time, and offset, for example
            ``2020-01-02T09:00:00+01:00`` or ``2020-01-02T09:00:00Z``
    """

    class DestinationStatus(proto.Message):
        r"""The status for the specified destination.

        Attributes:
            reporting_context (google.shopping.type.types.ReportingContext.ReportingContextEnum):
                Output only. The name of the promotion
                destination.
            status (google.shopping.merchant_promotions_v1.types.PromotionStatus.DestinationStatus.State):
                Output only. The status for the specified
                destination.
        """

        class State(proto.Enum):
            r"""The current state of the promotion.

            Values:
                STATE_UNSPECIFIED (0):
                    Unknown promotion state.
                IN_REVIEW (1):
                    The promotion is under review.
                REJECTED (2):
                    The promotion is disapproved.
                LIVE (3):
                    The promotion is approved and active.
                STOPPED (4):
                    The promotion is stopped by merchant.
                EXPIRED (5):
                    The promotion is no longer active.
                PENDING (6):
                    The promotion is not stopped, and all reviews
                    are approved, but the active date is in the
                    future.
            """

            STATE_UNSPECIFIED = 0
            IN_REVIEW = 1
            REJECTED = 2
            LIVE = 3
            STOPPED = 4
            EXPIRED = 5
            PENDING = 6

        reporting_context: types.ReportingContext.ReportingContextEnum = proto.Field(
            proto.ENUM,
            number=1,
            enum=types.ReportingContext.ReportingContextEnum,
        )
        status: "PromotionStatus.DestinationStatus.State" = proto.Field(
            proto.ENUM,
            number=2,
            enum="PromotionStatus.DestinationStatus.State",
        )

    class ItemLevelIssue(proto.Message):
        r"""The issue associated with the promotion.

        Attributes:
            code (str):
                Output only. The error code of the issue.
            severity (google.shopping.merchant_promotions_v1.types.PromotionStatus.ItemLevelIssue.Severity):
                Output only. How this issue affects serving
                of the promotion.
            resolution (str):
                Output only. Whether the issue can be
                resolved by the merchant.
            attribute (str):
                Output only. The attribute's name, if the
                issue is caused by a single attribute.
            reporting_context (google.shopping.type.types.ReportingContext.ReportingContextEnum):
                Output only. The destination the issue
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
            applicable_countries (MutableSequence[str]):
                Output only. List of country codes (ISO
                3166-1 alpha-2) where issue applies to the
                offer.
        """

        class Severity(proto.Enum):
            r"""The severity of the issue.

            Values:
                SEVERITY_UNSPECIFIED (0):
                    Not specified.
                NOT_IMPACTED (1):
                    This issue represents a warning and does not
                    have a direct affect on the promotion.
                DEMOTED (2):
                    The promotion is demoted and most likely have
                    limited performance in search results
                DISAPPROVED (3):
                    Issue disapproves the promotion.
            """

            SEVERITY_UNSPECIFIED = 0
            NOT_IMPACTED = 1
            DEMOTED = 2
            DISAPPROVED = 3

        code: str = proto.Field(
            proto.STRING,
            number=1,
        )
        severity: "PromotionStatus.ItemLevelIssue.Severity" = proto.Field(
            proto.ENUM,
            number=2,
            enum="PromotionStatus.ItemLevelIssue.Severity",
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
        applicable_countries: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=9,
        )

    destination_statuses: MutableSequence[DestinationStatus] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=DestinationStatus,
    )
    item_level_issues: MutableSequence[ItemLevelIssue] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=ItemLevelIssue,
    )
    creation_date: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    last_update_date: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
