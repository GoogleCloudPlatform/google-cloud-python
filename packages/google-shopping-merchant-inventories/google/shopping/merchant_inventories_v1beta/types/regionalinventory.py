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
        "RegionalInventory",
        "ListRegionalInventoriesRequest",
        "ListRegionalInventoriesResponse",
        "InsertRegionalInventoryRequest",
        "DeleteRegionalInventoryRequest",
    },
)


class RegionalInventory(proto.Message):
    r"""Regional inventory information for the product. Represents specific
    information like price and availability for a given product in a
    specific
    [``region``][google.shopping.merchant.inventories.v1beta.RegionalInventory.region].
    For a list of all accepted attribute values, see the `regional
    product inventory data
    specification <https://support.google.com/merchants/answer/9698880>`__.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Output only. The name of the ``RegionalInventory`` resource.
            Format:
            ``{regional_inventory.name=accounts/{account}/products/{product}/regionalInventories/{region}``
        account (int):
            Output only. The account that owns the
            product. This field will be ignored if set by
            the client.
        region (str):
            Required. Immutable. ID of the region for this
            ``RegionalInventory`` resource. See the `Regional
            availability and
            pricing <https://support.google.com/merchants/answer/9698880>`__
            for more details.
        price (google.shopping.type.types.Price):
            Price of the product in this region.
        sale_price (google.shopping.type.types.Price):
            Sale price of the product in this region. Mandatory if
            [``salePriceEffectiveDate``][google.shopping.merchant.inventories.v1beta.RegionalInventory.sale_price_effective_date]
            is defined.
        sale_price_effective_date (google.type.interval_pb2.Interval):
            The ``TimePeriod`` of the sale price in this region.
        availability (str):
            Availability of the product in this region. For accepted
            attribute values, see the `regional product inventory data
            specification <https://support.google.com/merchants/answer/3061342>`__

            This field is a member of `oneof`_ ``_availability``.
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
    region: str = proto.Field(
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
    custom_attributes: MutableSequence[types.CustomAttribute] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message=types.CustomAttribute,
    )


class ListRegionalInventoriesRequest(proto.Message):
    r"""Request message for the ``ListRegionalInventories`` method.

    Attributes:
        parent (str):
            Required. The ``name`` of the parent product to list
            ``RegionalInventory`` resources for. Format:
            ``accounts/{account}/products/{product}``
        page_size (int):
            The maximum number of ``RegionalInventory`` resources for
            the given product to return. The service returns fewer than
            this value if the number of inventories for the given
            product is less that than the ``pageSize``. The default
            value is 25000. The maximum value is 100000; If a value
            higher than the maximum is specified, then the ``pageSize``
            will default to the maximum.
        page_token (str):
            A page token, received from a previous
            ``ListRegionalInventories`` call. Provide the page token to
            retrieve the subsequent page.

            When paginating, all other parameters provided to
            ``ListRegionalInventories`` must match the call that
            provided the page token. The token returned as
            [nextPageToken][google.shopping.merchant.inventories.v1beta.ListRegionalInventoriesResponse.next_page_token]
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


class ListRegionalInventoriesResponse(proto.Message):
    r"""Response message for the ``ListRegionalInventories`` method.

    Attributes:
        regional_inventories (MutableSequence[google.shopping.merchant_inventories_v1beta.types.RegionalInventory]):
            The ``RegionalInventory`` resources for the given product
            from the specified account.
        next_page_token (str):
            A token, which can be sent as ``pageToken`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    regional_inventories: MutableSequence["RegionalInventory"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="RegionalInventory",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class InsertRegionalInventoryRequest(proto.Message):
    r"""Request message for the ``InsertRegionalInventory`` method.

    Attributes:
        parent (str):
            Required. The account and product where this inventory will
            be inserted. Format:
            ``accounts/{account}/products/{product}``
        regional_inventory (google.shopping.merchant_inventories_v1beta.types.RegionalInventory):
            Required. Regional inventory information to add to the
            product. If the product already has a ``RegionalInventory``
            resource for the same ``region``, full replacement of the
            ``RegionalInventory`` resource is performed.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    regional_inventory: "RegionalInventory" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="RegionalInventory",
    )


class DeleteRegionalInventoryRequest(proto.Message):
    r"""Request message for the ``DeleteRegionalInventory`` method.

    Attributes:
        name (str):
            Required. The name of the ``RegionalInventory`` resource to
            delete. Format:
            ``accounts/{account}/products/{product}/regionalInventories/{region}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
