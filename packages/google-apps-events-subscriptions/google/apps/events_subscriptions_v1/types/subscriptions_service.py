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

from google.apps.events_subscriptions_v1.types import subscription_resource

__protobuf__ = proto.module(
    package="google.apps.events.subscriptions.v1",
    manifest={
        "CreateSubscriptionRequest",
        "DeleteSubscriptionRequest",
        "GetSubscriptionRequest",
        "UpdateSubscriptionRequest",
        "ReactivateSubscriptionRequest",
        "ListSubscriptionsRequest",
        "ListSubscriptionsResponse",
        "UpdateSubscriptionMetadata",
        "CreateSubscriptionMetadata",
        "DeleteSubscriptionMetadata",
        "ReactivateSubscriptionMetadata",
    },
)


class CreateSubscriptionRequest(proto.Message):
    r"""The request message for
    [SubscriptionsService.CreateSubscription][google.apps.events.subscriptions.v1.SubscriptionsService.CreateSubscription].

    Attributes:
        subscription (google.apps.events_subscriptions_v1.types.Subscription):
            Required. The subscription resource to
            create.
        validate_only (bool):
            Optional. If set to ``true``, validates and previews the
            request, but doesn't create the subscription.
    """

    subscription: subscription_resource.Subscription = proto.Field(
        proto.MESSAGE,
        number=1,
        message=subscription_resource.Subscription,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class DeleteSubscriptionRequest(proto.Message):
    r"""The request message for
    [SubscriptionsService.DeleteSubscription][google.apps.events.subscriptions.v1.SubscriptionsService.DeleteSubscription].

    Attributes:
        name (str):
            Required. Resource name of the subscription to delete.

            Format: ``subscriptions/{subscription}``
        validate_only (bool):
            Optional. If set to ``true``, validates and previews the
            request, but doesn't delete the subscription.
        allow_missing (bool):
            Optional. If set to ``true`` and the subscription isn't
            found, the request succeeds but doesn't delete the
            subscription.
        etag (str):
            Optional. Etag of the subscription.

            If present, it must match with the server's etag. Otherwise,
            request fails with the status ``ABORTED``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    allow_missing: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=4,
    )


class GetSubscriptionRequest(proto.Message):
    r"""The request message for
    [SubscriptionsService.GetSubscription][google.apps.events.subscriptions.v1.SubscriptionsService.GetSubscription].

    Attributes:
        name (str):
            Required. Resource name of the subscription.

            Format: ``subscriptions/{subscription}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateSubscriptionRequest(proto.Message):
    r"""The request message for
    [SubscriptionsService.UpdateSubscription][google.apps.events.subscriptions.v1.SubscriptionsService.UpdateSubscription].

    Attributes:
        subscription (google.apps.events_subscriptions_v1.types.Subscription):
            Required. The subscription to update.

            The subscription's ``name`` field is used to identify the
            subscription to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Required. The field to update.

            You can update one of the following fields in a
            subscription:

            - [``expire_time``][google.apps.events.subscriptions.v1.Subscription.expire_time]:
              The timestamp when the subscription expires.
            - [``ttl``][google.apps.events.subscriptions.v1.Subscription.ttl]:
              The time-to-live (TTL) or duration of the subscription.
        validate_only (bool):
            Optional. If set to ``true``, validates and previews the
            request, but doesn't update the subscription.
    """

    subscription: subscription_resource.Subscription = proto.Field(
        proto.MESSAGE,
        number=1,
        message=subscription_resource.Subscription,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class ReactivateSubscriptionRequest(proto.Message):
    r"""The request message for
    [SubscriptionsService.ReactivateSubscription][google.apps.events.subscriptions.v1.SubscriptionsService.ReactivateSubscription].

    Attributes:
        name (str):
            Required. Resource name of the subscription.

            Format: ``subscriptions/{subscription}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListSubscriptionsRequest(proto.Message):
    r"""The request message for
    [SubscriptionsService.ListSubscriptions][google.apps.events.subscriptions.v1.SubscriptionsService.ListSubscriptions].

    Attributes:
        page_size (int):
            Optional. The maximum number of subscriptions to return. The
            service might return fewer than this value.

            If unspecified or set to ``0``, up to 50 subscriptions are
            returned.

            The maximum value is 100. If you specify a value more than
            100, the system only returns 100 subscriptions.
        page_token (str):
            Optional. A page token, received from a
            previous list subscriptions call. Provide this
            parameter to retrieve the subsequent page.

            When paginating, the filter value should match
            the call that provided the page token. Passing a
            different value might lead to unexpected
            results.
        filter (str):
            Required. A query filter.

            You can filter subscriptions by event type (``event_types``)
            and target resource (``target_resource``).

            You must specify at least one event type in your query. To
            filter for multiple event types, use the ``OR`` operator.

            To filter by both event type and target resource, use the
            ``AND`` operator and specify the full resource name, such as
            ``//chat.googleapis.com/spaces/{space}``.

            For example, the following queries are valid:

            ::

               event_types:"google.workspace.chat.membership.v1.updated" OR
                 event_types:"google.workspace.chat.message.v1.created"

               event_types:"google.workspace.chat.message.v1.created" AND
                 target_resource="//chat.googleapis.com/spaces/{space}"

               ( event_types:"google.workspace.chat.membership.v1.updated" OR
                 event_types:"google.workspace.chat.message.v1.created" ) AND
                 target_resource="//chat.googleapis.com/spaces/{space}"

            The server rejects invalid queries with an
            ``INVALID_ARGUMENT`` error.
    """

    page_size: int = proto.Field(
        proto.INT32,
        number=1,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListSubscriptionsResponse(proto.Message):
    r"""The response message for
    [SubscriptionsService.ListSubscriptions][google.apps.events.subscriptions.v1.SubscriptionsService.ListSubscriptions].

    Attributes:
        subscriptions (MutableSequence[google.apps.events_subscriptions_v1.types.Subscription]):
            List of subscriptions.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    subscriptions: MutableSequence[subscription_resource.Subscription] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=subscription_resource.Subscription,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class UpdateSubscriptionMetadata(proto.Message):
    r"""Metadata for UpdateSubscription LRO."""


class CreateSubscriptionMetadata(proto.Message):
    r"""Metadata for CreateSubscription LRO."""


class DeleteSubscriptionMetadata(proto.Message):
    r"""Metadata for DeleteSubscription LRO."""


class ReactivateSubscriptionMetadata(proto.Message):
    r"""Metadata for ReactivateSubscription LRO."""


__all__ = tuple(sorted(__protobuf__.manifest))
