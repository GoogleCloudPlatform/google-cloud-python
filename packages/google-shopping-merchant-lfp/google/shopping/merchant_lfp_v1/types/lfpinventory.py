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
    package="google.shopping.merchant.lfp.v1",
    manifest={
        "LfpInventory",
        "InsertLfpInventoryRequest",
    },
)


class LfpInventory(proto.Message):
    r"""Local Inventory for the merchant.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Output only. Identifier. The name for the ``LfpInventory``
            resource. Format:
            ``accounts/{account}/lfpInventories/{target_merchant}~{store_code}~{offer}``
        target_account (int):
            Required. The Merchant Center ID of the
            merchant to submit the inventory for.
        store_code (str):
            Required. The identifier of the merchant's store. Either the
            store code inserted through ``InsertLfpStore`` or the store
            code in the Business Profile.
        offer_id (str):
            Required. Immutable. A unique identifier for the product. If
            both inventories and sales are submitted for a merchant,
            this id should match for the same product.

            **Note**: if the merchant sells the same product new and
            used, they should have different IDs.
        region_code (str):
            Required. The `CLDR territory
            code <https://github.com/unicode-org/cldr/blob/latest/common/main/en.xml>`__
            for the country where the product is sold.
        content_language (str):
            Required. The two-letter ISO 639-1 language
            code for the item.
        gtin (str):
            Optional. The Global Trade Item Number of the
            product.

            This field is a member of `oneof`_ ``_gtin``.
        price (google.shopping.type.types.Price):
            Optional. The current price of the product.
        availability (str):
            Required. Availability of the product at this store. For
            accepted attribute values, see the `local product inventory
            data
            specification <https://support.google.com/merchants/answer/3061342>`__
        quantity (int):
            Optional. Quantity of the product available
            at this store. Must be greater than or equal to
            zero.

            This field is a member of `oneof`_ ``_quantity``.
        collection_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. The time when the inventory is
            collected. If not set, it will be set to the
            time when the inventory is submitted.
        pickup_method (str):
            Optional. Supported pickup method for this offer. Unless the
            value is "not supported", this field must be submitted
            together with ``pickupSla``. For accepted attribute values,
            see the `local product inventory data
            specification <https://support.google.com/merchants/answer/3061342>`__.

            This field is a member of `oneof`_ ``_pickup_method``.
        pickup_sla (str):
            Optional. Expected date that an order will be ready for
            pickup relative to the order date. Must be submitted
            together with ``pickupMethod``. For accepted attribute
            values, see the `local product inventory data
            specification <https://support.google.com/merchants/answer/3061342>`__.

            This field is a member of `oneof`_ ``_pickup_sla``.
        feed_label (str):
            Optional. The `feed
            label <https://developers.google.com/shopping-content/guides/products/feed-labels>`__
            for the product. If this is not set, it will default to
            ``regionCode``.

            This field is a member of `oneof`_ ``_feed_label``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    target_account: int = proto.Field(
        proto.INT64,
        number=2,
    )
    store_code: str = proto.Field(
        proto.STRING,
        number=3,
    )
    offer_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    region_code: str = proto.Field(
        proto.STRING,
        number=5,
    )
    content_language: str = proto.Field(
        proto.STRING,
        number=6,
    )
    gtin: str = proto.Field(
        proto.STRING,
        number=7,
        optional=True,
    )
    price: types.Price = proto.Field(
        proto.MESSAGE,
        number=8,
        message=types.Price,
    )
    availability: str = proto.Field(
        proto.STRING,
        number=9,
    )
    quantity: int = proto.Field(
        proto.INT64,
        number=10,
        optional=True,
    )
    collection_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=11,
        message=timestamp_pb2.Timestamp,
    )
    pickup_method: str = proto.Field(
        proto.STRING,
        number=12,
        optional=True,
    )
    pickup_sla: str = proto.Field(
        proto.STRING,
        number=13,
        optional=True,
    )
    feed_label: str = proto.Field(
        proto.STRING,
        number=14,
        optional=True,
    )


class InsertLfpInventoryRequest(proto.Message):
    r"""Request message for the ``InsertLfpInventory`` method.

    Attributes:
        parent (str):
            Required. The LFP provider account. Format:
            ``accounts/{account}``
        lfp_inventory (google.shopping.merchant_lfp_v1.types.LfpInventory):
            Required. The inventory to insert.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    lfp_inventory: "LfpInventory" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="LfpInventory",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
