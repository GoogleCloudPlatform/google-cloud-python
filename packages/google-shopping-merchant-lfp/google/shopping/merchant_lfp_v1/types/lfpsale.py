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
        "LfpSale",
        "InsertLfpSaleRequest",
    },
)


class LfpSale(proto.Message):
    r"""A sale for the merchant.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Output only. Identifier. The name of the ``LfpSale``
            resource. Format: ``accounts/{account}/lfpSales/{sale}``
        target_account (int):
            Required. The Merchant Center ID of the
            merchant to submit the sale for.
        store_code (str):
            Required. The identifier of the merchant's store. Either a
            ``storeCode`` inserted through the API or the code of the
            store in the Business Profile.
        offer_id (str):
            Required. A unique identifier for the product. If both
            inventories and sales are submitted for a merchant, this id
            should match for the same product.

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
            Required. The Global Trade Item Number of the
            sold product.
        price (google.shopping.type.types.Price):
            Required. The unit price of the product.
        quantity (int):
            Required. The relative change of the
            available quantity. Negative for items returned.
        sale_time (google.protobuf.timestamp_pb2.Timestamp):
            Required. The timestamp for the sale.
        uid (str):
            Output only. System generated globally unique ID for the
            ``LfpSale``.

            This field is a member of `oneof`_ ``_uid``.
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
    )
    price: types.Price = proto.Field(
        proto.MESSAGE,
        number=8,
        message=types.Price,
    )
    quantity: int = proto.Field(
        proto.INT64,
        number=9,
    )
    sale_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10,
        message=timestamp_pb2.Timestamp,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=11,
        optional=True,
    )
    feed_label: str = proto.Field(
        proto.STRING,
        number=12,
        optional=True,
    )


class InsertLfpSaleRequest(proto.Message):
    r"""Request message for the InsertLfpSale method.

    Attributes:
        parent (str):
            Required. The LFP provider account. Format:
            ``accounts/{lfp_partner}``
        lfp_sale (google.shopping.merchant_lfp_v1.types.LfpSale):
            Required. The sale to insert.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    lfp_sale: "LfpSale" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="LfpSale",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
