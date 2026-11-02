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

from google.ads.datamanager_v1.types import item_parameter

__protobuf__ = proto.module(
    package="google.ads.datamanager.v1",
    manifest={
        "CartData",
        "Item",
        "ItemCustomVariable",
    },
)


class CartData(proto.Message):
    r"""The cart data associated with the event.

    Attributes:
        merchant_id (str):
            Optional. The Merchant Center ID associated
            with the items.
        merchant_feed_label (str):
            Optional. The Merchant Center feed label
            associated with the feed of the items.
        merchant_feed_language_code (str):
            Optional. The language code in ISO 639-1
            associated with the Merchant Center feed of the
            items.where your items are uploaded.
        transaction_discount (float):
            Optional. The sum of all discounts associated
            with the transaction.
        items (MutableSequence[google.ads.datamanager_v1.types.Item]):
            Optional. The list of items associated with
            the event.
        coupon_codes (MutableSequence[str]):
            Optional. The list of coupon codes that were
            applied to the cart. Cart-level and item-level
            coupon codes are independent.

            If the event is for a Google Analytics
            destination, only provide a single coupon code.
            Google Analytics ignores additional coupon
            codes.
    """

    merchant_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    merchant_feed_label: str = proto.Field(
        proto.STRING,
        number=2,
    )
    merchant_feed_language_code: str = proto.Field(
        proto.STRING,
        number=3,
    )
    transaction_discount: float = proto.Field(
        proto.DOUBLE,
        number=4,
    )
    items: MutableSequence["Item"] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message="Item",
    )
    coupon_codes: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )


class Item(proto.Message):
    r"""Represents an item in the cart associated with the event.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        merchant_product_id (str):
            Optional. The product ID within the Merchant
            Center account.
        quantity (int):
            Optional. The number of this item associated
            with the event.
        unit_price (float):
            Optional. The unit price excluding tax,
            shipping, and any transaction level discounts.
        item_id (str):
            Optional. A unique identifier to reference
            the item.
        additional_item_parameters (MutableSequence[google.ads.datamanager_v1.types.ItemParameter]):
            Optional. A bucket of any `event parameters related to an
            item <https://developers.google.com/analytics/devguides/collection/protocol/ga4/reference/events>`__
            to be included within the event that were not already
            specified using other structured fields.
        merchant_id (str):
            Optional. The Merchant Center ID associated
            with the item. For Store Sales events this will
            override the value set at the cart level.  This
            field is ignored for other events.
        merchant_feed_label (str):
            Optional. The feed label of the Merchant
            Center feed. If countries are still being used,
            the 2-letter country code in ISO-3166-1 alpha-2
            can be used instead. For Store Sales events this
            will override the value set at the cart level.
            This field is ignored for other events.
        merchant_feed_language_code (str):
            Optional. The language code in ISO 639-1
            associated with the Merchant Center feed where
            your items are uploaded.
        conversion_value (float):
            Optional. The conversion value associated
            with this item within the event, for cases where
            the conversion value is different for each item.

            This field is a member of `oneof`_ ``_conversion_value``.
        custom_variables (MutableSequence[google.ads.datamanager_v1.types.ItemCustomVariable]):
            Optional. Additional key/value pair
            information to send to the conversion containers
            (conversion action or Floodlight activity), when
            tracking per-item
             conversions.
    """

    merchant_product_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    quantity: int = proto.Field(
        proto.INT64,
        number=2,
    )
    unit_price: float = proto.Field(
        proto.DOUBLE,
        number=3,
    )
    item_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    additional_item_parameters: MutableSequence[item_parameter.ItemParameter] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=5,
            message=item_parameter.ItemParameter,
        )
    )
    merchant_id: str = proto.Field(
        proto.STRING,
        number=6,
    )
    merchant_feed_label: str = proto.Field(
        proto.STRING,
        number=7,
    )
    merchant_feed_language_code: str = proto.Field(
        proto.STRING,
        number=8,
    )
    conversion_value: float = proto.Field(
        proto.DOUBLE,
        number=9,
        optional=True,
    )
    custom_variables: MutableSequence["ItemCustomVariable"] = proto.RepeatedField(
        proto.MESSAGE,
        number=10,
        message="ItemCustomVariable",
    )


class ItemCustomVariable(proto.Message):
    r"""Item-level custom variable for ads conversions.

    Attributes:
        variable (str):
            Optional. The name of the custom variable to
            set. If the variable is not found for the given
            destination, it will be ignored.
        value (str):
            Optional. The value to store for the custom
            variable.
        destination_references (MutableSequence[str]):
            Optional. Reference string used to determine which of the
            [Event.destination_references][google.ads.datamanager.v1.Event.destination_references]
            the custom variable should be sent to. If empty, the
            [Event.destination_references][google.ads.datamanager.v1.Event.destination_references]
            will be used.
    """

    variable: str = proto.Field(
        proto.STRING,
        number=1,
    )
    value: str = proto.Field(
        proto.STRING,
        number=2,
    )
    destination_references: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
