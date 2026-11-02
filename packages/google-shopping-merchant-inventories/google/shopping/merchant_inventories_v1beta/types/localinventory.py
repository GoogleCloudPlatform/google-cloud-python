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
    package="google.shopping.merchant.inventories.v1beta",
    manifest={
        "LocalInventory",
        "ListLocalInventoriesRequest",
        "ListLocalInventoriesResponse",
        "InsertLocalInventoryRequest",
        "DeleteLocalInventoryRequest",
    },
)


class LocalInventory(proto.Message):
    r"""Local inventory information for the product. Represents in-store
    information for a specific product at the store specified by
    [``storeCode``][google.shopping.merchant.inventories.v1beta.LocalInventory.store_code].
    For a list of all accepted attribute values, see the `local product
    inventory data
    specification <https://support.google.com/merchants/answer/3061342>`__.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Output only. The name of the ``LocalInventory`` resource.
            Format:
            ``accounts/{account}/products/{product}/localInventories/{store_code}``
        account (int):
            Output only. The account that owns the
            product. This field will be ignored if set by
            the client.
        store_code (str):
            Required. Immutable. Store code (the store ID from your
            Business Profile) of the physical store the product is sold
            in. See the `Local product inventory data
            specification <https://support.google.com/merchants/answer/3061342>`__
            for more information.
        price (google.shopping.type.types.Price):
            Price of the product at this store.
        sale_price (google.shopping.type.types.Price):
            Sale price of the product at this store. Mandatory if
            [``salePriceEffectiveDate``][google.shopping.merchant.inventories.v1beta.LocalInventory.sale_price_effective_date]
            is defined.
        sale_price_effective_date (google.type.interval_pb2.Interval):
            The ``TimePeriod`` of the sale at this store.
        availability (str):
            Availability of the product at this store. For accepted
            attribute values, see the `local product inventory data
            specification <https://support.google.com/merchants/answer/3061342>`__

            This field is a member of `oneof`_ ``_availability``.
        quantity (int):
            Quantity of the product available at this
            store. Must be greater than or equal to zero.

            This field is a member of `oneof`_ ``_quantity``.
        pickup_method (str):
            Supported pickup method for this product. Unless the value
            is ``"not supported"``, this field must be submitted
            together with ``pickupSla``. For accepted attribute values,
            see the `local product inventory data
            specification <https://support.google.com/merchants/answer/3061342>`__

            This field is a member of `oneof`_ ``_pickup_method``.
        pickup_sla (str):
            Relative time period from the order date for an order for
            this product, from this store, to be ready for pickup. Must
            be submitted with ``pickupMethod``. For accepted attribute
            values, see the `local product inventory data
            specification <https://support.google.com/merchants/answer/3061342>`__

            This field is a member of `oneof`_ ``_pickup_sla``.
        instore_product_location (str):
            Location of the product inside the store.
            Maximum length is 20 bytes.

            This field is a member of `oneof`_ ``_instore_product_location``.
        custom_attributes (MutableSequence[google.shopping.type.types.CustomAttribute]):
            A list of custom (merchant-provided) attributes. You can
            also use ``CustomAttribute`` to submit any attribute of the
            data specification in its generic form.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    account: int = proto.Field(
        proto.INT64,
        number=2,
    )
    store_code: str = proto.Field(
        proto.STRING,
        number=3,
    )
    price: types.Price = proto.Field(
        proto.MESSAGE,
        number=4,
        message=types.Price,
    )
    sale_price: types.Price = proto.Field(
        proto.MESSAGE,
        number=5,
        message=types.Price,
    )
    sale_price_effective_date: interval_pb2.Interval = proto.Field(
        proto.MESSAGE,
        number=6,
        message=interval_pb2.Interval,
    )
    availability: str = proto.Field(
        proto.STRING,
        number=7,
        optional=True,
    )
    quantity: int = proto.Field(
        proto.INT64,
        number=8,
        optional=True,
    )
    pickup_method: str = proto.Field(
        proto.STRING,
        number=9,
        optional=True,
    )
    pickup_sla: str = proto.Field(
        proto.STRING,
        number=10,
        optional=True,
    )
    instore_product_location: str = proto.Field(
        proto.STRING,
        number=11,
        optional=True,
    )
    custom_attributes: MutableSequence[types.CustomAttribute] = proto.RepeatedField(
        proto.MESSAGE,
        number=12,
        message=types.CustomAttribute,
    )


class ListLocalInventoriesRequest(proto.Message):
    r"""Request message for the ``ListLocalInventories`` method.

    Attributes:
        parent (str):
            Required. The ``name`` of the parent product to list local
            inventories for. Format:
            ``accounts/{account}/products/{product}``
        page_size (int):
            The maximum number of ``LocalInventory`` resources for the
            given product to return. The service returns fewer than this
            value if the number of inventories for the given product is
            less that than the ``pageSize``. The default value is 25000.
            The maximum value is 25000; If a value higher than the
            maximum is specified, then the ``pageSize`` will default to
            the maximum
        page_token (str):
            A page token, received from a previous
            ``ListLocalInventories`` call. Provide the page token to
            retrieve the subsequent page.

            When paginating, all other parameters provided to
            ``ListLocalInventories`` must match the call that provided
            the page token. The token returned as
            [nextPageToken][google.shopping.merchant.inventories.v1beta.ListLocalInventoriesResponse.next_page_token]
            in the response to the previous request.
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


class ListLocalInventoriesResponse(proto.Message):
    r"""Response message for the ``ListLocalInventories`` method.

    Attributes:
        local_inventories (MutableSequence[google.shopping.merchant_inventories_v1beta.types.LocalInventory]):
            The ``LocalInventory`` resources for the given product from
            the specified account.
        next_page_token (str):
            A token, which can be sent as ``pageToken`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    local_inventories: MutableSequence["LocalInventory"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="LocalInventory",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class InsertLocalInventoryRequest(proto.Message):
    r"""Request message for the ``InsertLocalInventory`` method.

    Attributes:
        parent (str):
            Required. The account and product where this inventory will
            be inserted. Format:
            ``accounts/{account}/products/{product}``
        local_inventory (google.shopping.merchant_inventories_v1beta.types.LocalInventory):
            Required. Local inventory information of the product. If the
            product already has a ``LocalInventory`` resource for the
            same ``storeCode``, full replacement of the
            ``LocalInventory`` resource is performed.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    local_inventory: "LocalInventory" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="LocalInventory",
    )


class DeleteLocalInventoryRequest(proto.Message):
    r"""Request message for the ``DeleteLocalInventory`` method.

    Attributes:
        name (str):
            Required. The name of the local inventory for the given
            product to delete. Format:
            ``accounts/{account}/products/{product}/localInventories/{store_code}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
