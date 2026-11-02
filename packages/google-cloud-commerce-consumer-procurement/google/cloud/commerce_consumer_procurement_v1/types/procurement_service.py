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

from google.cloud.commerce_consumer_procurement_v1.types import order

__protobuf__ = proto.module(
    package="google.cloud.commerce.consumer.procurement.v1",
    manifest={
        "AutoRenewalBehavior",
        "PlaceOrderRequest",
        "PlaceOrderMetadata",
        "GetOrderRequest",
        "ListOrdersRequest",
        "ListOrdersResponse",
        "ModifyOrderRequest",
        "ModifyOrderMetadata",
        "CancelOrderRequest",
        "CancelOrderMetadata",
    },
)


class AutoRenewalBehavior(proto.Enum):
    r"""Indicates the auto renewal behavior customer specifies on
    subscription.

    Values:
        AUTO_RENEWAL_BEHAVIOR_UNSPECIFIED (0):
            If unspecified, the auto renewal behavior
            will follow the default config.
        AUTO_RENEWAL_BEHAVIOR_ENABLE (1):
            Auto Renewal will be enabled on subscription.
        AUTO_RENEWAL_BEHAVIOR_DISABLE (2):
            Auto Renewal will be disabled on
            subscription.
    """

    AUTO_RENEWAL_BEHAVIOR_UNSPECIFIED = 0
    AUTO_RENEWAL_BEHAVIOR_ENABLE = 1
    AUTO_RENEWAL_BEHAVIOR_DISABLE = 2


class PlaceOrderRequest(proto.Message):
    r"""Request message for
    [ConsumerProcurementService.PlaceOrder][google.cloud.commerce.consumer.procurement.v1.ConsumerProcurementService.PlaceOrder].

    Attributes:
        parent (str):
            Required. The resource name of the parent resource. This
            field has the form ``billingAccounts/{billing-account-id}``.
        display_name (str):
            Required. The user-specified name of the
            order being placed.
        line_item_info (MutableSequence[google.cloud.commerce_consumer_procurement_v1.types.LineItemInfo]):
            Optional. Places order for offer. Required
            when an offer-based order is being placed.
        request_id (str):
            Optional. A unique identifier for this request. The server
            will ignore subsequent requests that provide a duplicate
            request ID for at least 24 hours after the first request.

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
    [ConsumerProcurementService.PlaceOrder][google.cloud.commerce.consumer.procurement.v1.ConsumerProcurementService.PlaceOrder].

    """


class GetOrderRequest(proto.Message):
    r"""Request message for
    [ConsumerProcurementService.GetOrder][google.cloud.commerce.consumer.procurement.v1.ConsumerProcurementService.GetOrder]

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
    [ConsumerProcurementService.ListOrders][google.cloud.commerce.consumer.procurement.v1.ConsumerProcurementService.ListOrders].

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
    [ConsumerProcurementService.ListOrders][google.cloud.commerce.consumer.procurement.v1.ConsumerProcurementService.ListOrders].

    Attributes:
        orders (MutableSequence[google.cloud.commerce_consumer_procurement_v1.types.Order]):
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


class ModifyOrderRequest(proto.Message):
    r"""Request message for
    [ConsumerProcurementService.ModifyOrder][google.cloud.commerce.consumer.procurement.v1.ConsumerProcurementService.ModifyOrder].

    Attributes:
        name (str):
            Required. Name of the order to update.
        modifications (MutableSequence[google.cloud.commerce_consumer_procurement_v1.types.ModifyOrderRequest.Modification]):
            Optional. Modifications for an existing Order
            created by an Offer. Required when Offer based
            Order is being modified, except for when going
            from an offer to a public plan.
        display_name (str):
            Optional. Updated display name of the order,
            leave as empty if you do not want to update
            current display name.
        etag (str):
            Optional. The weak etag, which can be
            optionally populated, of the order that this
            modify request is based on. Validation checking
            will only happen if the invoker supplies this
            field.
    """

    class Modification(proto.Message):
        r"""Modifications to make on the order.

        Attributes:
            line_item_id (str):
                Required. ID of the existing line item to make change to.
                Required when change type is
                [LineItemChangeType.LINE_ITEM_CHANGE_TYPE_UPDATE] or
                [LineItemChangeType.LINE_ITEM_CHANGE_TYPE_CANCEL].
            change_type (google.cloud.commerce_consumer_procurement_v1.types.LineItemChangeType):
                Required. Type of change to make.
            new_line_item_info (google.cloud.commerce_consumer_procurement_v1.types.LineItemInfo):
                Optional. The line item to update to. Required when
                change_type is
                [LineItemChangeType.LINE_ITEM_CHANGE_TYPE_CREATE] or
                [LineItemChangeType.LINE_ITEM_CHANGE_TYPE_UPDATE].
            auto_renewal_behavior (google.cloud.commerce_consumer_procurement_v1.types.AutoRenewalBehavior):
                Optional. Auto renewal behavior of the subscription for the
                update. Applied when change_type is
                [LineItemChangeType.LINE_ITEM_CHANGE_TYPE_UPDATE]. Follows
                plan default config when this field is not specified.
        """

        line_item_id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        change_type: order.LineItemChangeType = proto.Field(
            proto.ENUM,
            number=2,
            enum=order.LineItemChangeType,
        )
        new_line_item_info: order.LineItemInfo = proto.Field(
            proto.MESSAGE,
            number=3,
            message=order.LineItemInfo,
        )
        auto_renewal_behavior: "AutoRenewalBehavior" = proto.Field(
            proto.ENUM,
            number=4,
            enum="AutoRenewalBehavior",
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    modifications: MutableSequence[Modification] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message=Modification,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=5,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ModifyOrderMetadata(proto.Message):
    r"""Message stored in the metadata field of the Operation returned by
    [ConsumerProcurementService.ModifyOrder][google.cloud.commerce.consumer.procurement.v1.ConsumerProcurementService.ModifyOrder].

    """


class CancelOrderRequest(proto.Message):
    r"""Request message for
    [ConsumerProcurementService.CancelOrder][google.cloud.commerce.consumer.procurement.v1.ConsumerProcurementService.CancelOrder].

    Attributes:
        name (str):
            Required. The resource name of the order.
        etag (str):
            Optional. The weak etag, which can be
            optionally populated, of the order that this
            cancel request is based on. Validation checking
            will only happen if the invoker supplies this
            field.
        cancellation_policy (google.cloud.commerce_consumer_procurement_v1.types.CancelOrderRequest.CancellationPolicy):
            Optional. Cancellation policy of this
            request.
    """

    class CancellationPolicy(proto.Enum):
        r"""Indicates the cancellation policy the customer uses to cancel
        the order.

        Values:
            CANCELLATION_POLICY_UNSPECIFIED (0):
                If unspecified, cancellation will try to
                cancel the order, if order cannot be immediately
                cancelled, auto renewal will be turned off.
                However, caller should avoid using the value as
                it will yield a non-deterministic result. This
                is still supported mainly to maintain existing
                integrated usages and ensure backwards
                compatibility.
            CANCELLATION_POLICY_CANCEL_IMMEDIATELY (1):
                Request will cancel the whole order
                immediately, if order cannot be immediately
                cancelled, the request will fail.
            CANCELLATION_POLICY_CANCEL_AT_TERM_END (2):
                Request will cancel the auto renewal, if
                order is not subscription based, the request
                will fail.
        """

        CANCELLATION_POLICY_UNSPECIFIED = 0
        CANCELLATION_POLICY_CANCEL_IMMEDIATELY = 1
        CANCELLATION_POLICY_CANCEL_AT_TERM_END = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=2,
    )
    cancellation_policy: CancellationPolicy = proto.Field(
        proto.ENUM,
        number=3,
        enum=CancellationPolicy,
    )


class CancelOrderMetadata(proto.Message):
    r"""Message stored in the metadata field of the Operation returned by
    [ConsumerProcurementService.CancelOrder][google.cloud.commerce.consumer.procurement.v1.ConsumerProcurementService.CancelOrder].

    """


__all__ = tuple(sorted(__protobuf__.manifest))
