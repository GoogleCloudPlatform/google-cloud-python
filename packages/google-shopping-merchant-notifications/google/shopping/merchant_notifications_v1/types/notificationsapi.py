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

import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.shopping.merchant.notifications.v1",
    manifest={
        "GetNotificationSubscriptionRequest",
        "CreateNotificationSubscriptionRequest",
        "UpdateNotificationSubscriptionRequest",
        "DeleteNotificationSubscriptionRequest",
        "ListNotificationSubscriptionsRequest",
        "ListNotificationSubscriptionsResponse",
        "NotificationSubscription",
        "GetNotificationSubscriptionHealthMetricsRequest",
        "NotificationSubscriptionHealthMetrics",
    },
)


class GetNotificationSubscriptionRequest(proto.Message):
    r"""Request message for the GetNotificationSubscription method.

    Attributes:
        name (str):
            Required. The ``name`` of the notification subscription.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateNotificationSubscriptionRequest(proto.Message):
    r"""Request message for the CreateNotificationSubscription
    method.

    Attributes:
        parent (str):
            Required. The merchant account that owns the new
            notification subscription. Format: ``accounts/{account}``
        notification_subscription (google.shopping.merchant_notifications_v1.types.NotificationSubscription):
            Required. The notification subscription to
            create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    notification_subscription: "NotificationSubscription" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="NotificationSubscription",
    )


class UpdateNotificationSubscriptionRequest(proto.Message):
    r"""Request message for the UpdateNotificationSubscription
    method.

    Attributes:
        notification_subscription (google.shopping.merchant_notifications_v1.types.NotificationSubscription):
            Required. The new version of the notification
            subscription that should be updated.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            List of fields being updated.
    """

    notification_subscription: "NotificationSubscription" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="NotificationSubscription",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteNotificationSubscriptionRequest(proto.Message):
    r"""Request message for the DeleteNotificationSubscription
    method.

    Attributes:
        name (str):
            Required. The name of the notification
            subscription to be deleted.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListNotificationSubscriptionsRequest(proto.Message):
    r"""Request message for the ListNotificationSubscription method.

    Attributes:
        parent (str):
            Required. The merchant account who owns the notification
            subscriptions. Format: ``accounts/{account}``
        page_size (int):
            The maximum number of notification subscriptions to return
            in a page. The default value for ``page_size`` is 100. The
            maximum value is ``200``. Values above ``200`` will be
            coerced to ``200``.
        page_token (str):
            Token (if provided) to retrieve the
            subsequent page. All other parameters must match
            the original call that provided the page token.
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


class ListNotificationSubscriptionsResponse(proto.Message):
    r"""Response message for the ListNotificationSubscription method.

    Attributes:
        notification_subscriptions (MutableSequence[google.shopping.merchant_notifications_v1.types.NotificationSubscription]):
            The list of notification subscriptions
            requested by the merchant.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    notification_subscriptions: MutableSequence["NotificationSubscription"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="NotificationSubscription",
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class NotificationSubscription(proto.Message):
    r"""Represents a notification subscription owned by a Merchant
    account.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        all_managed_accounts (bool):
            If this value is true, the requesting account
            is notified of the specified event for all
            managed accounts (can be subaccounts or other
            linked accounts) including newly added accounts
            on a daily basis.

            This field is a member of `oneof`_ ``interested_in``.
        target_account (str):
            The ``name`` of the account you want to receive
            notifications for. Format: ``accounts/{account}``

            This field is a member of `oneof`_ ``interested_in``.
        name (str):
            Output only. The ``name`` of the notification configuration.
            Generated by the Content API upon creation of a new
            ``NotificationSubscription``. The ``account`` represents the
            merchant ID of the merchant that owns the configuration.
            Format:
            ``accounts/{account}/notificationsubscriptions/{notification_subscription}``
        registered_event (google.shopping.merchant_notifications_v1.types.NotificationSubscription.NotificationEventType):
            The event that the merchant wants to be
            notified about.
        call_back_uri (str):
            URL to be used to push the notification to
            the merchant.
    """

    class NotificationEventType(proto.Enum):
        r"""Represents the event type that the merchant is interested in
        receiving notifications for.

        Values:
            NOTIFICATION_EVENT_TYPE_UNSPECIFIED (0):
                Notifications event type is unspecified.
            PRODUCT_STATUS_CHANGE (1):
                Notification of product status changes, for
                example when product becomes disapproved.
        """

        NOTIFICATION_EVENT_TYPE_UNSPECIFIED = 0
        PRODUCT_STATUS_CHANGE = 1

    all_managed_accounts: bool = proto.Field(
        proto.BOOL,
        number=3,
        oneof="interested_in",
    )
    target_account: str = proto.Field(
        proto.STRING,
        number=4,
        oneof="interested_in",
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    registered_event: NotificationEventType = proto.Field(
        proto.ENUM,
        number=2,
        enum=NotificationEventType,
    )
    call_back_uri: str = proto.Field(
        proto.STRING,
        number=5,
    )


class GetNotificationSubscriptionHealthMetricsRequest(proto.Message):
    r"""Request for notification subscription health metrics.

    Attributes:
        name (str):
            Required. The ``name`` of the notification subscription for
            which metrics are retrieved. Format:
            ``accounts/{account}/notificationsubscriptions/{notification_subscription}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class NotificationSubscriptionHealthMetrics(proto.Message):
    r"""Represents a notification subscription health metrics.

    Attributes:
        name (str):
            Output only. Identifier. The name of the
            notification configuration. Generated by the
            Content API upon creation of a new
            NotificationSubscription. The account represents
            the merchant ID of the merchant that owns the
            configuration.
        acknowledged_messages_count (int):
            The number of retained acknowledged messages
            for the last 24 hours
        undelivered_messages_count (int):
            The number of unacknowledged messages for the
            last 7 days, we will attempt to re-deliver the
            unacknowledged message later and once
            successfully delivered it will not be counted
            within unacknowledged messages (the number of
            unacknowledged messages should gradually
            decrease to zero once the issue is fixed).
        oldest_unacknowledged_message_waiting_time (int):
            The time since the oldest unacknowledged
            message was sent in seconds
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    acknowledged_messages_count: int = proto.Field(
        proto.INT64,
        number=2,
    )
    undelivered_messages_count: int = proto.Field(
        proto.INT64,
        number=3,
    )
    oldest_unacknowledged_message_waiting_time: int = proto.Field(
        proto.INT64,
        number=4,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
