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

import google.type.interval_pb2 as interval_pb2  # type: ignore
import proto  # type: ignore
from google.shopping.type.types import types

__protobuf__ = proto.module(
    package="google.shopping.merchant.inventories.v1",
    manifest={
        "LocalInventoryAttributes",
        "InventoryLoyaltyProgram",
        "RegionalInventoryAttributes",
    },
)


class LocalInventoryAttributes(proto.Message):
    r"""Local inventory attributes.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        price (google.shopping.type.types.Price):
            Optional. Price of the product at this store.
        sale_price (google.shopping.type.types.Price):
            Optional. Sale price of the product at this store. Mandatory
            if
            [``salePriceEffectiveDate``][LocalInventory.sale_price_effective_date]
            is defined.
        sale_price_effective_date (google.type.interval_pb2.Interval):
            Optional. The ``TimePeriod`` of the sale at this store.
        availability (google.shopping.merchant_inventories_v1.types.LocalInventoryAttributes.Availability):
            `Availability <https://support.google.com/merchants/answer/3061342>`__
            of the product at this store.

            This field is a member of `oneof`_ ``_availability``.
        quantity (int):
            Optional. Quantity of the product available
            at this store. Must be greater than or equal to
            zero.

            This field is a member of `oneof`_ ``_quantity``.
        pickup_method (google.shopping.merchant_inventories_v1.types.LocalInventoryAttributes.PickupMethod):
            Optional. Supported `pickup
            method <https://support.google.com/merchants/answer/3061342>`__
            for this product. Unless the value is ``"not supported"``,
            this field must be submitted together with ``pickupSla``.

            This field is a member of `oneof`_ ``_pickup_method``.
        pickup_sla (google.shopping.merchant_inventories_v1.types.LocalInventoryAttributes.PickupSla):
            Optional. Relative time period from the order date for an
            order for this product, from this store, to be ready for
            pickup. Must be submitted with ``pickupMethod``. See more
            details
            `here <https://support.google.com/merchants/answer/3061342>`__.

            This field is a member of `oneof`_ ``_pickup_sla``.
        instore_product_location (str):
            Optional. Location of the product inside the
            store. Maximum length is 20 bytes.

            This field is a member of `oneof`_ ``_instore_product_location``.
        local_shipping_label (str):
            Optional. Specifies a label associated with the shipping for
            the ``LocalInventory`` resource. Can be used to group local
            shipping services to this particular inventory item. For
            accepted field format, see the `Local
            delivery <https://support.google.com/merchants/answer/14819809#localdelivery>`__

            This field is a member of `oneof`_ ``_local_shipping_label``.
        loyalty_programs (MutableSequence[google.shopping.merchant_inventories_v1.types.InventoryLoyaltyProgram]):
            Optional. An optional list of loyalty programs containing
            applicable loyalty member prices for this product at this
            store.

            This field is used to show store-specific member prices on
            Local Inventory Ads (LIA).

            To use this, the loyalty program must be configured in
            Google Merchant Center. The benefits provided must match the
            merchant's website and be clear to members. This is only
            applicable for merchants in supported countries.

            See `Loyalty
            program <https://support.google.com/merchants/answer/12922446>`__
            for details on supported countries and loyalty program
            configuration. For local inventory specific details, see the
            `Local inventory data
            specification <https://support.google.com/merchants/answer/3061342>`__.
        custom_attributes (MutableSequence[google.shopping.type.types.CustomAttribute]):
            Optional. A list of custom (merchant-provided) attributes.
            It can also be used for submitting any attribute of the data
            specification in its generic form (for example,
            ``{ "name": "size type", "value": "regular" }``). This is
            useful for submitting attributes not explicitly exposed by
            the API. Maximum allowed number of characters for each
            custom attribute is 10240 (represents sum of characters for
            name and value). Maximum 2500 custom attributes can be set,
            with total size of 102.4kB. Underscores in custom attribute
            names are replaced by spaces upon insertion.
    """

    class Availability(proto.Enum):
        r"""`Availability <https://support.google.com/merchants/answer/3061342>`__
        of the product at this store.

        Values:
            LOCAL_INVENTORY_AVAILABILITY_UNSPECIFIED (0):
                Indicates that the availability is
                unspecified.
            IN_STOCK (1):
                Indicates that the product is in stock.
            LIMITED_AVAILABILITY (2):
                Indicates that the product is out of stock.
            ON_DISPLAY_TO_ORDER (3):
                Indicates that the product is on display to
                order.
            OUT_OF_STOCK (4):
                Indicates that the product is out of stock.
        """

        LOCAL_INVENTORY_AVAILABILITY_UNSPECIFIED = 0
        IN_STOCK = 1
        LIMITED_AVAILABILITY = 2
        ON_DISPLAY_TO_ORDER = 3
        OUT_OF_STOCK = 4

    class PickupMethod(proto.Enum):
        r"""Supported `pickup
        method <https://support.google.com/merchants/answer/3061342>`__ for
        this product. Unless the value is ``"not supported"``, this field
        must be submitted together with ``pickupSla``.

        Values:
            PICKUP_METHOD_UNSPECIFIED (0):
                Indicates that the pickup method is
                unspecified.
            BUY (1):
                Indicates that the pickup method is Buy.
            RESERVE (2):
                Indicates that the pickup method is Reserve.
            SHIP_TO_STORE (3):
                Indicates that the pickup method is Ship to
                store.
            NOT_SUPPORTED (4):
                Indicates that the pickup method is not
                supported.
        """

        PICKUP_METHOD_UNSPECIFIED = 0
        BUY = 1
        RESERVE = 2
        SHIP_TO_STORE = 3
        NOT_SUPPORTED = 4

    class PickupSla(proto.Enum):
        r"""Relative time period from the order date for an order for this
        product, from this store, to be ready for pickup. Must be submitted
        with ``pickupMethod``. See more details
        `here <https://support.google.com/merchants/answer/3061342>`__.

        Values:
            PICKUP_SLA_UNSPECIFIED (0):
                Indicates that the pickup SLA is unspecified.
            SAME_DAY (1):
                Indicates that the pickup SLA is same day.
            NEXT_DAY (2):
                Indicates that the pickup SLA is next day.
            TWO_DAY (3):
                Indicates that the pickup SLA is two days.
            THREE_DAY (4):
                Indicates that the pickup SLA is three days.
            FOUR_DAY (5):
                Indicates that the pickup SLA is four days.
            FIVE_DAY (6):
                Indicates that the pickup SLA is five days.
            SIX_DAY (7):
                Indicates that the pickup SLA is six days.
            SEVEN_DAY (8):
                Indicates that the pickup SLA is seven days.
            MULTI_WEEK (9):
                Indicates that the pickup SLA is multi-week.
        """

        PICKUP_SLA_UNSPECIFIED = 0
        SAME_DAY = 1
        NEXT_DAY = 2
        TWO_DAY = 3
        THREE_DAY = 4
        FOUR_DAY = 5
        FIVE_DAY = 6
        SIX_DAY = 7
        SEVEN_DAY = 8
        MULTI_WEEK = 9

    price: types.Price = proto.Field(
        proto.MESSAGE,
        number=1,
        message=types.Price,
    )
    sale_price: types.Price = proto.Field(
        proto.MESSAGE,
        number=2,
        message=types.Price,
    )
    sale_price_effective_date: interval_pb2.Interval = proto.Field(
        proto.MESSAGE,
        number=3,
        message=interval_pb2.Interval,
    )
    availability: Availability = proto.Field(
        proto.ENUM,
        number=4,
        optional=True,
        enum=Availability,
    )
    quantity: int = proto.Field(
        proto.INT64,
        number=5,
        optional=True,
    )
    pickup_method: PickupMethod = proto.Field(
        proto.ENUM,
        number=6,
        optional=True,
        enum=PickupMethod,
    )
    pickup_sla: PickupSla = proto.Field(
        proto.ENUM,
        number=7,
        optional=True,
        enum=PickupSla,
    )
    instore_product_location: str = proto.Field(
        proto.STRING,
        number=8,
        optional=True,
    )
    local_shipping_label: str = proto.Field(
        proto.STRING,
        number=9,
        optional=True,
    )
    loyalty_programs: MutableSequence["InventoryLoyaltyProgram"] = proto.RepeatedField(
        proto.MESSAGE,
        number=10,
        message="InventoryLoyaltyProgram",
    )
    custom_attributes: MutableSequence[types.CustomAttribute] = proto.RepeatedField(
        proto.MESSAGE,
        number=11,
        message=types.CustomAttribute,
    )


class InventoryLoyaltyProgram(proto.Message):
    r"""A message that represents loyalty program.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        program_label (str):
            The label of the loyalty program. This is an
            internal label that uniquely identifies the
            relationship between a business entity and a
            loyalty program entity. The label must be
            provided if there are multiple loyalty programs
            available for the merchant, so that the system
            can associate the assets below (for example,
            price and points) with the correct business. The
            corresponding program must be linked to the
            Merchant Center account.

            This field is a member of `oneof`_ ``_program_label``.
        tier_label (str):
            The label of the tier within the loyalty
            program. Must match one of the labels within the
            program.

            This field is a member of `oneof`_ ``_tier_label``.
        price (google.shopping.type.types.Price):
            The price for members of the given tier, that
            is, the instant discount price. Must be smaller
            or equal to the regular price.

            This field is a member of `oneof`_ ``_price``.
        cashback_for_future_use (google.shopping.type.types.Price):
            The cashback that can be used for future
            purchases.

            This field is a member of `oneof`_ ``_cashback_for_future_use``.
        loyalty_points (int):
            The amount of loyalty points earned on a
            purchase.

            This field is a member of `oneof`_ ``_loyalty_points``.
        member_price_effective_interval (google.type.interval_pb2.Interval):
            A date range during which the item is
            eligible for member price. If not specified, the
            member price is always applicable. The date
            range is represented by a pair of ISO 8601 dates
            separated by a space, comma, or slash.

            This field is a member of `oneof`_ ``_member_price_effective_interval``.
        shipping_label (str):
            The label of the shipping benefit. If the
            field has value, this offer has loyalty shipping
            benefit. If the field value isn't provided, the
            item is not eligible for loyalty shipping for
            the given loyalty tier.

            This field is a member of `oneof`_ ``_shipping_label``.
    """

    program_label: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    tier_label: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    price: types.Price = proto.Field(
        proto.MESSAGE,
        number=3,
        optional=True,
        message=types.Price,
    )
    cashback_for_future_use: types.Price = proto.Field(
        proto.MESSAGE,
        number=4,
        optional=True,
        message=types.Price,
    )
    loyalty_points: int = proto.Field(
        proto.INT64,
        number=5,
        optional=True,
    )
    member_price_effective_interval: interval_pb2.Interval = proto.Field(
        proto.MESSAGE,
        number=6,
        optional=True,
        message=interval_pb2.Interval,
    )
    shipping_label: str = proto.Field(
        proto.STRING,
        number=7,
        optional=True,
    )


class RegionalInventoryAttributes(proto.Message):
    r"""Regional inventory attributes.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        price (google.shopping.type.types.Price):
            Optional. Price of the product in this
            region.
        sale_price (google.shopping.type.types.Price):
            Optional. Sale price of the product in this region.
            Mandatory if
            [``salePriceEffectiveDate``][RegionalInventory.sale_price_effective_date]
            is defined.
        sale_price_effective_date (google.type.interval_pb2.Interval):
            Optional. The ``TimePeriod`` of the sale price in this
            region.
        availability (google.shopping.merchant_inventories_v1.types.RegionalInventoryAttributes.Availability):
            Optional.
            `Availability <https://support.google.com/merchants/answer/14644124>`__
            of the product in this region.

            This field is a member of `oneof`_ ``_availability``.
        loyalty_programs (MutableSequence[google.shopping.merchant_inventories_v1.types.InventoryLoyaltyProgram]):
            Optional. An optional list of loyalty programs containing
            applicable loyalty member prices for this product in this
            region.

            This field is used to show region-specific member prices on
            Product Listing Ads (PLA).

            To use this, the loyalty program must be configured in
            Google Merchant Center, and the merchant must be using the
            Regional Availability and Pricing (RAAP) feature. The
            benefits provided must match the merchant's website and be
            clear to members. This is only applicable for merchants in
            supported countries.

            See `Loyalty
            program <https://support.google.com/merchants/answer/12922446>`__
            for details on supported countries and loyalty program
            configuration. Also see `Regional availability and
            pricing <https://support.google.com/merchants/answer/14644124>`__
            and `How to set up regional member
            pricing <https://support.google.com/merchants/answer/16388178>`__
            for more information.
    """

    class Availability(proto.Enum):
        r"""`Availability <https://support.google.com/merchants/answer/14644124>`__
        of the product in this region.

        Values:
            REGIONAL_INVENTORY_AVAILABILITY_UNSPECIFIED (0):
                Indicates that the availability is
                unspecified.
            IN_STOCK (1):
                Indicates that the product is in stock.
            OUT_OF_STOCK (2):
                Indicates that the product is out of stock.
        """

        REGIONAL_INVENTORY_AVAILABILITY_UNSPECIFIED = 0
        IN_STOCK = 1
        OUT_OF_STOCK = 2

    price: types.Price = proto.Field(
        proto.MESSAGE,
        number=1,
        message=types.Price,
    )
    sale_price: types.Price = proto.Field(
        proto.MESSAGE,
        number=2,
        message=types.Price,
    )
    sale_price_effective_date: interval_pb2.Interval = proto.Field(
        proto.MESSAGE,
        number=3,
        message=interval_pb2.Interval,
    )
    availability: Availability = proto.Field(
        proto.ENUM,
        number=4,
        optional=True,
        enum=Availability,
    )
    loyalty_programs: MutableSequence["InventoryLoyaltyProgram"] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message="InventoryLoyaltyProgram",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
