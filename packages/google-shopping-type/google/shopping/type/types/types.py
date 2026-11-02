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

__protobuf__ = proto.module(
    package="google.shopping.type",
    manifest={
        "Weight",
        "Price",
        "CustomAttribute",
        "Destination",
        "ReportingContext",
        "Channel",
    },
)


class Weight(proto.Message):
    r"""The weight represented as the value in string and the unit.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        amount_micros (int):
            Required. The weight represented as a number
            in micros (1 million micros is an equivalent to
            one's currency standard unit, for example, 1 kg
            = 1000000 micros).
            This field can also be set as infinity by
            setting to -1. This field only support -1 and
            positive value.

            This field is a member of `oneof`_ ``_amount_micros``.
        unit (google.shopping.type.types.Weight.WeightUnit):
            Required. The weight unit.
            Acceptable values are: kg and lb
    """

    class WeightUnit(proto.Enum):
        r"""The weight unit.

        Values:
            WEIGHT_UNIT_UNSPECIFIED (0):
                unit unspecified
            POUND (1):
                lb unit.
            KILOGRAM (2):
                kg unit.
        """

        WEIGHT_UNIT_UNSPECIFIED = 0
        POUND = 1
        KILOGRAM = 2

    amount_micros: int = proto.Field(
        proto.INT64,
        number=1,
        optional=True,
    )
    unit: WeightUnit = proto.Field(
        proto.ENUM,
        number=2,
        enum=WeightUnit,
    )


class Price(proto.Message):
    r"""The price represented as a number and currency.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        amount_micros (int):
            The price represented as a number in micros
            (1 million micros is an equivalent to one's
            currency standard unit, for example, 1 USD =
            1000000 micros).

            This field is a member of `oneof`_ ``_amount_micros``.
        currency_code (str):
            The currency of the price using three-letter acronyms
            according to `ISO
            4217 <http://en.wikipedia.org/wiki/ISO_4217>`__.

            This field is a member of `oneof`_ ``_currency_code``.
    """

    amount_micros: int = proto.Field(
        proto.INT64,
        number=1,
        optional=True,
    )
    currency_code: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )


class CustomAttribute(proto.Message):
    r"""A message that represents custom attributes. Exactly one of
    ``value`` or ``group_values`` must not be empty.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            The name of the attribute.

            This field is a member of `oneof`_ ``_name``.
        value (str):
            The value of the attribute. If ``value`` is not empty,
            ``group_values`` must be empty.

            This field is a member of `oneof`_ ``_value``.
        group_values (MutableSequence[google.shopping.type.types.CustomAttribute]):
            Subattributes within this attribute group. If
            ``group_values`` is not empty, ``value`` must be empty.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    value: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    group_values: MutableSequence["CustomAttribute"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="CustomAttribute",
    )


class Destination(proto.Message):
    r"""Destinations available for a product.

    Destinations are used in Merchant Center to allow you to control
    where the products from your data feed should be displayed.

    """

    class DestinationEnum(proto.Enum):
        r"""Destination values.

        Values:
            DESTINATION_ENUM_UNSPECIFIED (0):
                Not specified.
            SHOPPING_ADS (1):
                `Shopping
                ads <https://support.google.com/google-ads/answer/2454022>`__.
            DISPLAY_ADS (2):
                `Display
                ads <https://support.google.com/merchants/answer/6069387>`__.
            LOCAL_INVENTORY_ADS (3):
                `Local inventory
                ads <https://support.google.com/merchants/answer/3057972>`__.
            FREE_LISTINGS (4):
                `Free
                listings <https://support.google.com/merchants/answer/9199328>`__.
            FREE_LOCAL_LISTINGS (5):
                `Free local product
                listings <https://support.google.com/merchants/answer/9825611>`__.
            YOUTUBE_SHOPPING (6):
                `YouTube
                Shopping <https://support.google.com/merchants/answer/12362804>`__.
            YOUTUBE_SHOPPING_CHECKOUT (7):
                Youtube shopping checkout.
            YOUTUBE_AFFILIATE (8):
                `Youtube
                Affiliate <https://support.google.com/youtube/answer/13376398>`__.
            FREE_VEHICLE_LISTINGS (9):
                `Free vehicle
                listings <https://support.google.com/merchants/answer/11189169>`__.
            VEHICLE_ADS (10):
                `Vehicle
                ads <https://support.google.com/merchants/answer/11189169>`__.
            CLOUD_RETAIL (11):
                `Cloud
                retail <https://cloud.google.com/solutions/retail>`__.
            LOCAL_CLOUD_RETAIL (12):
                `Local cloud
                retail <https://cloud.google.com/solutions/retail>`__.
        """

        DESTINATION_ENUM_UNSPECIFIED = 0
        SHOPPING_ADS = 1
        DISPLAY_ADS = 2
        LOCAL_INVENTORY_ADS = 3
        FREE_LISTINGS = 4
        FREE_LOCAL_LISTINGS = 5
        YOUTUBE_SHOPPING = 6
        YOUTUBE_SHOPPING_CHECKOUT = 7
        YOUTUBE_AFFILIATE = 8
        FREE_VEHICLE_LISTINGS = 9
        VEHICLE_ADS = 10
        CLOUD_RETAIL = 11
        LOCAL_CLOUD_RETAIL = 12


class ReportingContext(proto.Message):
    r"""Reporting contexts that your account and product issues apply to.

    Reporting contexts are groups of surfaces and formats for product
    results on Google. They can represent the entire destination (for
    example, `Shopping
    ads <https://support.google.com/merchants/answer/6149970>`__) or a
    subset of formats within a destination (for example, `Demand Gen
    ads <https://support.google.com/merchants/answer/13389785>`__).

    """

    class ReportingContextEnum(proto.Enum):
        r"""Reporting context values.

        Values:
            REPORTING_CONTEXT_ENUM_UNSPECIFIED (0):
                Not specified.
            SHOPPING_ADS (1):
                `Shopping
                ads <https://support.google.com/merchants/answer/6149970>`__.
            DISCOVERY_ADS (2):
                Deprecated: Use ``DEMAND_GEN_ADS`` instead. `Discovery and
                Demand Gen
                ads <https://support.google.com/merchants/answer/13389785>`__.
            DEMAND_GEN_ADS (13):
                `Demand Gen
                ads <https://support.google.com/merchants/answer/13389785>`__.
            DEMAND_GEN_ADS_DISCOVER_SURFACE (14):
                `Demand Gen ads on Discover
                surface <https://support.google.com/merchants/answer/13389785>`__.
            VIDEO_ADS (3):
                `Video
                ads <https://support.google.com/google-ads/answer/6340491>`__.
            DISPLAY_ADS (4):
                `Display
                ads <https://support.google.com/merchants/answer/6069387>`__.
            LOCAL_INVENTORY_ADS (5):
                `Local inventory
                ads <https://support.google.com/merchants/answer/3271956>`__.
            VEHICLE_INVENTORY_ADS (6):
                `Vehicle inventory
                ads <https://support.google.com/merchants/answer/11544533>`__.
            FREE_LISTINGS (7):
                `Free product
                listings <https://support.google.com/merchants/answer/9199328>`__.
            FREE_LISTINGS_UCP_CHECKOUT (19):
                `Free product listings on UCP
                checkout <https://developers.google.com/merchant/ucp>`__.
            FREE_LOCAL_LISTINGS (8):
                `Free local product
                listings <https://support.google.com/merchants/answer/9825611>`__.
            FREE_LOCAL_VEHICLE_LISTINGS (9):
                `Free local vehicle
                listings <https://support.google.com/merchants/answer/11544533>`__.
            YOUTUBE_AFFILIATE (18):
                `Youtube
                Affiliate <https://support.google.com/youtube/answer/13376398>`__.
            YOUTUBE_SHOPPING (10):
                `YouTube
                Shopping <https://support.google.com/merchants/answer/13478370>`__.
            CLOUD_RETAIL (11):
                `Cloud
                retail <https://cloud.google.com/solutions/retail>`__.
            LOCAL_CLOUD_RETAIL (12):
                `Local cloud
                retail <https://cloud.google.com/solutions/retail>`__.
            PRODUCT_REVIEWS (15):
                `Product
                Reviews <https://support.google.com/merchants/answer/14620732>`__.
            MERCHANT_REVIEWS (16):
                `Merchant
                Reviews <https://developers.google.com/merchant-review-feeds>`__.
            YOUTUBE_CHECKOUT (17):
                YouTube Checkout
                .
        """

        REPORTING_CONTEXT_ENUM_UNSPECIFIED = 0
        SHOPPING_ADS = 1
        DISCOVERY_ADS = 2
        DEMAND_GEN_ADS = 13
        DEMAND_GEN_ADS_DISCOVER_SURFACE = 14
        VIDEO_ADS = 3
        DISPLAY_ADS = 4
        LOCAL_INVENTORY_ADS = 5
        VEHICLE_INVENTORY_ADS = 6
        FREE_LISTINGS = 7
        FREE_LISTINGS_UCP_CHECKOUT = 19
        FREE_LOCAL_LISTINGS = 8
        FREE_LOCAL_VEHICLE_LISTINGS = 9
        YOUTUBE_AFFILIATE = 18
        YOUTUBE_SHOPPING = 10
        CLOUD_RETAIL = 11
        LOCAL_CLOUD_RETAIL = 12
        PRODUCT_REVIEWS = 15
        MERCHANT_REVIEWS = 16
        YOUTUBE_CHECKOUT = 17


class Channel(proto.Message):
    r"""`Channel <https://support.google.com/merchants/answer/7361332>`__ of
    a product.

    Channel is used to distinguish between online and local products.

    """

    class ChannelEnum(proto.Enum):
        r"""Channel values.

        Values:
            CHANNEL_ENUM_UNSPECIFIED (0):
                Not specified.
            ONLINE (1):
                Online product.
            LOCAL (2):
                Local product.
        """

        CHANNEL_ENUM_UNSPECIFIED = 0
        ONLINE = 1
        LOCAL = 2


__all__ = tuple(sorted(__protobuf__.manifest))
