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
from google.shopping.type.types import types

__protobuf__ = proto.module(
    package="google.shopping.merchant.notifications.v1beta",
    manifest={
        "Resource",
        "Attribute",
        "GetNotificationSubscriptionRequest",
        "CreateNotificationSubscriptionRequest",
        "UpdateNotificationSubscriptionRequest",
        "DeleteNotificationSubscriptionRequest",
        "ListNotificationSubscriptionsRequest",
        "ListNotificationSubscriptionsResponse",
        "NotificationSubscription",
        "ProductChange",
        "ProductStatusChangeMessage",
    },
)


class Resource(proto.Enum):
    r"""Enum to specify the resource that is being changed to notify
    the merchant about.

    Values:
        RESOURCE_UNSPECIFIED (0):
            Unspecified resource
        PRODUCT (1):
            Resource type : product
    """

    RESOURCE_UNSPECIFIED = 0
    PRODUCT = 1


class Attribute(proto.Enum):
    r"""Enum to specify the attribute in the resource that is being
    changed to notify the merchant about.

    Values:
        ATTRIBUTE_UNSPECIFIED (0):
            Unspecified attribute
        STATUS (1):
            Status of the changed entity
    """

    ATTRIBUTE_UNSPECIFIED = 0
    STATUS = 1


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
        notification_subscription (google.shopping.merchant_notifications_v1beta.types.NotificationSubscription):
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
        notification_subscription (google.shopping.merchant_notifications_v1beta.types.NotificationSubscription):
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
        notification_subscriptions (MutableSequence[google.shopping.merchant_notifications_v1beta.types.NotificationSubscription]):
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
        registered_event (google.shopping.merchant_notifications_v1beta.types.NotificationSubscription.NotificationEventType):
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


class ProductChange(proto.Message):
    r"""The change that happened to the product including old value,
    new value, country code as the region code and reporting
    context.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        old_value (str):
            The old value of the changed resource or
            attribute.

            This field is a member of `oneof`_ ``_old_value``.
        new_value (str):
            The new value of the changed resource or
            attribute.

            This field is a member of `oneof`_ ``_new_value``.
        region_code (str):
            Countries that have the change (if
            applicable)

            This field is a member of `oneof`_ ``_region_code``.
        reporting_context (google.shopping.type.types.ReportingContext.ReportingContextEnum):
            Reporting contexts that have the change (if
            applicable)

            This field is a member of `oneof`_ ``_reporting_context``.
    """

    old_value: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    new_value: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    region_code: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )
    reporting_context: types.ReportingContext.ReportingContextEnum = proto.Field(
        proto.ENUM,
        number=4,
        optional=True,
        enum=types.ReportingContext.ReportingContextEnum,
    )


class ProductStatusChangeMessage(proto.Message):
    r"""The message that the merchant will receive to notify about
    product status change event


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        account (str):
            The target account that owns the entity that changed. Format
            : ``accounts/{merchant_id}``

            This field is a member of `oneof`_ ``_account``.
        managing_account (str):
            The account that manages the merchant's account. can be the
            same as merchant id if it is standalone account. Format :
            ``accounts/{service_provider_id}``

            This field is a member of `oneof`_ ``_managing_account``.
        resource_type (google.shopping.merchant_notifications_v1beta.types.Resource):
            The resource that changed, in this case it will always be
            ``Product``.

            This field is a member of `oneof`_ ``_resource_type``.
        attribute (google.shopping.merchant_notifications_v1beta.types.Attribute):
            The attribute in the resource that changed, in this case it
            will be always ``Status``.

            This field is a member of `oneof`_ ``_attribute``.
        changes (MutableSequence[google.shopping.merchant_notifications_v1beta.types.ProductChange]):
            A message to describe the change that
            happened to the product
        resource_id (str):
            The product id.

            This field is a member of `oneof`_ ``_resource_id``.
        resource (str):
            The product name. Format:
            ``{product.name=accounts/{account}/products/{product}}``

            This field is a member of `oneof`_ ``_resource``.
    """

    account: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    managing_account: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    resource_type: "Resource" = proto.Field(
        proto.ENUM,
        number=3,
        optional=True,
        enum="Resource",
    )
    attribute: "Attribute" = proto.Field(
        proto.ENUM,
        number=4,
        optional=True,
        enum="Attribute",
    )
    changes: MutableSequence["ProductChange"] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message="ProductChange",
    )
    resource_id: str = proto.Field(
        proto.STRING,
        number=6,
        optional=True,
    )
    resource: str = proto.Field(
        proto.STRING,
        number=7,
        optional=True,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
