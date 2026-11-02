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

from google.cloud.commerce_consumer_procurement_v1alpha1.types import order

__protobuf__ = proto.module(
    package="google.cloud.commerce.consumer.procurement.v1alpha1",
    manifest={
        "PlaceOrderRequest",
        "PlaceOrderMetadata",
        "GetOrderRequest",
        "ListOrdersRequest",
        "ListOrdersResponse",
    },
)


class PlaceOrderRequest(proto.Message):
    r"""Request message for
    [ConsumerProcurementService.PlaceOrder][google.cloud.commerce.consumer.procurement.v1alpha1.ConsumerProcurementService.PlaceOrder].

    Attributes:
        parent (str):
            Required. The resource name of the parent resource. This
            field has the form ``billingAccounts/{billing-account-id}``.
        display_name (str):
            Required. The user-specified name of the
            order being placed.
        line_item_info (MutableSequence[google.cloud.commerce_consumer_procurement_v1alpha1.types.LineItemInfo]):
            Optional. Places order for offer. Required
            when an offer-based order is being placed.
        request_id (str):
            Optional. A unique identifier for this request. The server
            will ignore subsequent requests that provide a duplicate
            request ID for at least 120 minutes after the first request.

            The request ID must be a valid
            `UUID <https://en.wikipedia.org/wiki/Universally_unique_identifier#Format>`__.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=6,
    )
    line_item_info: MutableSequence[order.LineItemInfo] = proto.RepeatedField(
        proto.MESSAGE,
        number=10,
        message=order.LineItemInfo,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=7,
    )


class PlaceOrderMetadata(proto.Message):
    r"""Message stored in the metadata field of the Operation returned by
    [ConsumerProcurementService.PlaceOrder][google.cloud.commerce.consumer.procurement.v1alpha1.ConsumerProcurementService.PlaceOrder].

    """


class GetOrderRequest(proto.Message):
    r"""Request message for
    [ConsumerProcurementService.GetOrder][google.cloud.commerce.consumer.procurement.v1alpha1.ConsumerProcurementService.GetOrder]

    Attributes:
        name (str):
            Required. The name of the order to retrieve.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListOrdersRequest(proto.Message):
    r"""Request message for
    [ConsumerProcurementService.ListOrders][google.cloud.commerce.consumer.procurement.v1alpha1.ConsumerProcurementService.ListOrders].

    Attributes:
        parent (str):
            Required. The parent resource to query for orders. This
            field has the form ``billingAccounts/{billing-account-id}``.
        page_size (int):
            The maximum number of entries requested.
            The default page size is 25 and the maximum page
            size is 200.
        page_token (str):
            The token for fetching the next page.
        filter (str):
            Filter that you can use to limit the list request.

            A query string that can match a selected set of attributes
            with string values. For example, ``display_name=abc``.
            Supported query attributes are

            - ``display_name``

            If the query contains special characters other than letters,
            underscore, or digits, the phrase must be quoted with double
            quotes. For example, ``display_name="foo:bar"``, where the
            display name needs to be quoted because it contains special
            character colon.

            Queries can be combined with ``OR``, and ``NOT`` to form
            more complex queries. You can also group them to force a
            desired evaluation order. For example,
            ``display_name=abc OR display_name=def``.
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
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListOrdersResponse(proto.Message):
    r"""Response message for
    [ConsumerProcurementService.ListOrders][google.cloud.commerce.consumer.procurement.v1alpha1.ConsumerProcurementService.ListOrders].

    Attributes:
        orders (MutableSequence[google.cloud.commerce_consumer_procurement_v1alpha1.types.Order]):
            The list of orders in this response.
        next_page_token (str):
            The token for fetching the next page.
    """

    @property
    def raw_page(self):
        return self

    orders: MutableSequence[order.Order] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=order.Order,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
