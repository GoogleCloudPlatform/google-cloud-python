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

__protobuf__ = proto.module(
    package="google.cloud.commerce.consumer.procurement.v1alpha1",
    manifest={
        "LineItemChangeType",
        "LineItemChangeState",
        "LineItemChangeStateReasonType",
        "Order",
        "LineItem",
        "LineItemChange",
        "LineItemInfo",
        "Parameter",
        "Subscription",
    },
)


class LineItemChangeType(proto.Enum):
    r"""Type of a line item change.

    Values:
        LINE_ITEM_CHANGE_TYPE_UNSPECIFIED (0):
            Sentinel value. Do not use.
        LINE_ITEM_CHANGE_TYPE_CREATE (1):
            The change is to create a new line item.
        LINE_ITEM_CHANGE_TYPE_UPDATE (2):
            The change is to update an existing line
            item.
        LINE_ITEM_CHANGE_TYPE_CANCEL (3):
            The change is to cancel an existing line
            item.
        LINE_ITEM_CHANGE_TYPE_REVERT_CANCELLATION (4):
            The change is to revert a cancellation.
    """

    LINE_ITEM_CHANGE_TYPE_UNSPECIFIED = 0
    LINE_ITEM_CHANGE_TYPE_CREATE = 1
    LINE_ITEM_CHANGE_TYPE_UPDATE = 2
    LINE_ITEM_CHANGE_TYPE_CANCEL = 3
    LINE_ITEM_CHANGE_TYPE_REVERT_CANCELLATION = 4


class LineItemChangeState(proto.Enum):
    r"""State of a change.

    Values:
        LINE_ITEM_CHANGE_STATE_UNSPECIFIED (0):
            Sentinel value. Do not use.
        LINE_ITEM_CHANGE_STATE_PENDING_APPROVAL (1):
            Change is in this state when a change is
            initiated and waiting for partner approval.
        LINE_ITEM_CHANGE_STATE_APPROVED (2):
            Change is in this state after it's approved
            by the partner or auto-approved but before it
            takes effect. The change can be overwritten or
            cancelled depending on the new line item info
            property (pending Private Offer change cannot be
            cancelled and can only be overwritten by another
            Private Offer).
        LINE_ITEM_CHANGE_STATE_COMPLETED (3):
            Change is in this state after it's been
            activated.
        LINE_ITEM_CHANGE_STATE_REJECTED (4):
            Change is in this state if it was rejected by
            the partner.
        LINE_ITEM_CHANGE_STATE_ABANDONED (5):
            Change is in this state if it was abandoned
            by the user.
        LINE_ITEM_CHANGE_STATE_ACTIVATING (6):
            Change is in this state if it's currently
            being provisioned downstream. The change can't
            be overwritten or cancelled when it's in this
            state.
    """

    LINE_ITEM_CHANGE_STATE_UNSPECIFIED = 0
    LINE_ITEM_CHANGE_STATE_PENDING_APPROVAL = 1
    LINE_ITEM_CHANGE_STATE_APPROVED = 2
    LINE_ITEM_CHANGE_STATE_COMPLETED = 3
    LINE_ITEM_CHANGE_STATE_REJECTED = 4
    LINE_ITEM_CHANGE_STATE_ABANDONED = 5
    LINE_ITEM_CHANGE_STATE_ACTIVATING = 6


class LineItemChangeStateReasonType(proto.Enum):
    r"""Predefined types for line item change state reason.

    Values:
        LINE_ITEM_CHANGE_STATE_REASON_TYPE_UNSPECIFIED (0):
            Default value, indicating there's no
            predefined type for change state reason.
        LINE_ITEM_CHANGE_STATE_REASON_TYPE_EXPIRED (1):
            Change is in current state due to term
            expiration.
        LINE_ITEM_CHANGE_STATE_REASON_TYPE_USER_CANCELLED (2):
            Change is in current state due to
            user-initiated cancellation.
        LINE_ITEM_CHANGE_STATE_REASON_TYPE_SYSTEM_CANCELLED (3):
            Change is in current state due to
            system-initiated cancellation.
    """

    LINE_ITEM_CHANGE_STATE_REASON_TYPE_UNSPECIFIED = 0
    LINE_ITEM_CHANGE_STATE_REASON_TYPE_EXPIRED = 1
    LINE_ITEM_CHANGE_STATE_REASON_TYPE_USER_CANCELLED = 2
    LINE_ITEM_CHANGE_STATE_REASON_TYPE_SYSTEM_CANCELLED = 3


class Order(proto.Message):
    r"""Represents a purchase made by a customer on Cloud
    Marketplace. Creating an order makes sure that both the Google
    backend systems as well as external service provider's systems
    (if needed) allow use of purchased products and ensures the
    appropriate billing events occur.

    An Order can be made against one Product with multiple add-ons
    (optional) or one Quote which might reference multiple products.

    Customers typically choose a price plan for each Product
    purchased when they create an order and can change their plan
    later, if the product allows.

    Attributes:
        name (str):
            Output only. The resource name of the order. Has the form
            ``billingAccounts/{billing_account}/orders/{order}``.
        display_name (str):
            Required. The user-specified name of the
            order.
        line_items (MutableSequence[google.cloud.commerce_consumer_procurement_v1alpha1.types.LineItem]):
            Output only. The items being purchased.
        cancelled_line_items (MutableSequence[google.cloud.commerce_consumer_procurement_v1alpha1.types.LineItem]):
            Output only. Line items that were cancelled.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The creation timestamp.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last update timestamp.
        etag (str):
            The weak etag of the order.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=10,
    )
    line_items: MutableSequence["LineItem"] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message="LineItem",
    )
    cancelled_line_items: MutableSequence["LineItem"] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message="LineItem",
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=11,
    )


class LineItem(proto.Message):
    r"""A single item within an order.

    Attributes:
        line_item_id (str):
            Output only. Line item ID.
        line_item_info (google.cloud.commerce_consumer_procurement_v1alpha1.types.LineItemInfo):
            Output only. Current state and information of
            this item. It tells what, e.g. which offer, is
            currently effective.
        pending_change (google.cloud.commerce_consumer_procurement_v1alpha1.types.LineItemChange):
            Output only. A change made on the item which
            is pending and not yet effective. Absence of
            this field indicates the line item is not
            undergoing a change.
        change_history (MutableSequence[google.cloud.commerce_consumer_procurement_v1alpha1.types.LineItemChange]):
            Output only. Changes made on the item that
            are not pending anymore which might be because
            they already took effect, were reverted by the
            customer, or were rejected by the partner. No
            more operations are allowed on these changes.
    """

    line_item_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    line_item_info: "LineItemInfo" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="LineItemInfo",
    )
    pending_change: "LineItemChange" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="LineItemChange",
    )
    change_history: MutableSequence["LineItemChange"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="LineItemChange",
    )


class LineItemChange(proto.Message):
    r"""A change made on a line item.

    Attributes:
        change_id (str):
            Output only. Change ID. All changes made within one order
            update operation have the same change_id.
        change_type (google.cloud.commerce_consumer_procurement_v1alpha1.types.LineItemChangeType):
            Required. Type of the change to make.
        old_line_item_info (google.cloud.commerce_consumer_procurement_v1alpha1.types.LineItemInfo):
            Output only. Line item info before the
            change.
        new_line_item_info (google.cloud.commerce_consumer_procurement_v1alpha1.types.LineItemInfo):
            Line item info after the change.
        change_state (google.cloud.commerce_consumer_procurement_v1alpha1.types.LineItemChangeState):
            Output only. State of the change.
        state_reason (str):
            Output only. Provider-supplied message explaining the
            LineItemChange's state. Mainly used to communicate progress
            and ETA for provisioning in the case of
            ``PENDING_APPROVAL``, and to explain why the change request
            was denied or canceled in the case of ``REJECTED`` and
            ``CANCELED`` states.
        change_state_reason_type (google.cloud.commerce_consumer_procurement_v1alpha1.types.LineItemChangeStateReasonType):
            Output only. Predefined enum types for why this line item
            change is in current state. For example, a line item
            change's state could be ``LINE_ITEM_CHANGE_STATE_COMPLETED``
            because of end-of-term expiration, immediate cancellation
            initiated by the user, or system-initiated cancellation.
        change_effective_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. A time at which the change
            became or will become (in case of pending
            change) effective.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when change was
            initiated.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when change was
            updated, e.g. approved/rejected by partners or
            cancelled by the user.
    """

    change_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    change_type: "LineItemChangeType" = proto.Field(
        proto.ENUM,
        number=2,
        enum="LineItemChangeType",
    )
    old_line_item_info: "LineItemInfo" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="LineItemInfo",
    )
    new_line_item_info: "LineItemInfo" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="LineItemInfo",
    )
    change_state: "LineItemChangeState" = proto.Field(
        proto.ENUM,
        number=5,
        enum="LineItemChangeState",
    )
    state_reason: str = proto.Field(
        proto.STRING,
        number=6,
    )
    change_state_reason_type: "LineItemChangeStateReasonType" = proto.Field(
        proto.ENUM,
        number=10,
        enum="LineItemChangeStateReasonType",
    )
    change_effective_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )


class LineItemInfo(proto.Message):
    r"""Line item information.

    Attributes:
        offer (str):
            Optional. The name of the offer can have either of these
            formats: 'billingAccounts/{billing_account}/offers/{offer}',
            or 'services/{service}/standardOffers/{offer}'.
        parameters (MutableSequence[google.cloud.commerce_consumer_procurement_v1alpha1.types.Parameter]):
            Optional. User-provided parameters.
        subscription (google.cloud.commerce_consumer_procurement_v1alpha1.types.Subscription):
            Output only. Information about the
            subscription created, if applicable.
    """

    offer: str = proto.Field(
        proto.STRING,
        number=13,
    )
    parameters: MutableSequence["Parameter"] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message="Parameter",
    )
    subscription: "Subscription" = proto.Field(
        proto.MESSAGE,
        number=10,
        message="Subscription",
    )


class Parameter(proto.Message):
    r"""User-provided Parameters.

    Attributes:
        name (str):
            Name of the parameter.
        value (google.cloud.commerce_consumer_procurement_v1alpha1.types.Parameter.Value):
            Value of parameter.
    """

    class Value(proto.Message):
        r"""

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            int64_value (int):
                Represents an int64 value.

                This field is a member of `oneof`_ ``kind``.
            string_value (str):
                Represents a string value.

                This field is a member of `oneof`_ ``kind``.
            double_value (float):
                Represents a double value.

                This field is a member of `oneof`_ ``kind``.
        """

        int64_value: int = proto.Field(
            proto.INT64,
            number=3,
            oneof="kind",
        )
        string_value: str = proto.Field(
            proto.STRING,
            number=4,
            oneof="kind",
        )
        double_value: float = proto.Field(
            proto.DOUBLE,
            number=5,
            oneof="kind",
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    value: Value = proto.Field(
        proto.MESSAGE,
        number=2,
        message=Value,
    )


class Subscription(proto.Message):
    r"""Subscription information.

    Attributes:
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            The timestamp when the subscription begins,
            if applicable.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            The timestamp when the subscription ends, if
            applicable.
        auto_renewal_enabled (bool):
            Whether auto renewal is enabled by user
            choice on current subscription. This field
            indicates order/subscription status after
            pending plan change is cancelled or rejected.
    """

    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    auto_renewal_enabled: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
