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

import google.protobuf.duration_pb2 as duration_pb2  # type: ignore
import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.apps.events.subscriptions.v1",
    manifest={
        "Subscription",
        "PayloadOptions",
        "NotificationEndpoint",
    },
)


class Subscription(proto.Message):
    r"""A subscription to receive events about a Google Workspace resource.
    To learn more about subscriptions, see the `Google Workspace Events
    API overview <https://developers.google.com/workspace/events>`__.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        expire_time (google.protobuf.timestamp_pb2.Timestamp):
            Non-empty default. The timestamp in UTC when
            the subscription expires. Always displayed on
            output, regardless of what was used on input.

            This field is a member of `oneof`_ ``expiration``.
        ttl (google.protobuf.duration_pb2.Duration):
            Input only. The time-to-live (TTL) or duration for the
            subscription. If unspecified or set to ``0``, uses the
            maximum possible duration.

            This field is a member of `oneof`_ ``expiration``.
        name (str):
            Optional. Immutable. Identifier. Resource name of the
            subscription.

            Format: ``subscriptions/{subscription}``
        uid (str):
            Output only. System-assigned unique
            identifier for the subscription.
        target_resource (str):
            Required. Immutable. The Google Workspace resource that's
            monitored for events, formatted as the `full resource
            name <https://google.aip.dev/122#full-resource-names>`__. To
            learn about target resources and the events that they
            support, see `Supported Google Workspace
            events <https://developers.google.com/workspace/events#supported-events>`__.

            A user can only authorize your app to create one
            subscription for a given target resource. If your app tries
            to create another subscription with the same user
            credentials, the request returns an ``ALREADY_EXISTS``
            error.
        event_types (MutableSequence[str]):
            Required. Immutable. Unordered list. Input for creating a
            subscription. Otherwise, output only. One or more types of
            events to receive about the target resource. Formatted
            according to the CloudEvents specification.

            The supported event types depend on the target resource of
            your subscription. For details, see `Supported Google
            Workspace
            events <https://developers.google.com/workspace/events/guides#supported-events>`__.

            By default, you also receive events about the `lifecycle of
            your
            subscription <https://developers.google.com/workspace/events/guides/events-lifecycle>`__.
            You don't need to specify lifecycle events for this field.

            If you specify an event type that doesn't exist for the
            target resource, the request returns an HTTP
            ``400 Bad Request`` status code.
        payload_options (google.apps.events_subscriptions_v1.types.PayloadOptions):
            Optional. Options about what data to include
            in the event payload. Only supported for Google
            Chat events.
        notification_endpoint (google.apps.events_subscriptions_v1.types.NotificationEndpoint):
            Required. Immutable. The endpoint where the
            subscription delivers events, such as a Pub/Sub
            topic.
        state (google.apps.events_subscriptions_v1.types.Subscription.State):
            Output only. The state of the subscription.
            Determines whether the subscription can receive
            events and deliver them to the notification
            endpoint.
        suspension_reason (google.apps.events_subscriptions_v1.types.Subscription.ErrorType):
            Output only. The error that suspended the subscription.

            To reactivate the subscription, resolve the error and call
            the
            [``ReactivateSubscription``][google.apps.events.subscriptions.v1.SubscriptionsService.ReactivateSubscription]
            method.
        authority (str):
            Output only. The user who authorized the creation of the
            subscription.

            Format: ``users/{user}``

            For Google Workspace users, the ``{user}`` value is the
            ```user.id`` <https://developers.google.com/admin-sdk/directory/reference/rest/v1/users#User.FIELDS.ids>`__
            field from the Directory API.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the subscription
            is created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last time that the
            subscription is updated.
        reconciling (bool):
            Output only. If ``true``, the subscription is in the process
            of being updated.
        etag (str):
            Optional. This checksum is computed by the
            server based on the value of other fields, and
            might be sent on update requests to ensure the
            client has an up-to-date value before
            proceeding.
    """

    class State(proto.Enum):
        r"""Possible states for the subscription.

        Values:
            STATE_UNSPECIFIED (0):
                Default value. This value is unused.
            ACTIVE (1):
                The subscription is active and can receive
                and deliver events to its notification endpoint.
            SUSPENDED (2):
                The subscription is unable to receive events due to an
                error. To identify the error, see the
                [``suspension_reason``][google.apps.events.subscriptions.v1.Subscription.suspension_reason]
                field.
            DELETED (3):
                The subscription is deleted.
        """

        STATE_UNSPECIFIED = 0
        ACTIVE = 1
        SUSPENDED = 2
        DELETED = 3

    class ErrorType(proto.Enum):
        r"""Possible errors for a subscription.

        Values:
            ERROR_TYPE_UNSPECIFIED (0):
                Default value. This value is unused.
            USER_SCOPE_REVOKED (1):
                The authorizing user has revoked the grant of one or more
                OAuth scopes. To learn more about authorization for Google
                Workspace, see `Configure the OAuth consent
                screen <https://developers.google.com/workspace/guides/configure-oauth-consent#choose-scopes>`__.
            RESOURCE_DELETED (2):
                The target resource for the subscription no
                longer exists.
            USER_AUTHORIZATION_FAILURE (3):
                The user that authorized the creation of the
                subscription no longer has access to the
                subscription's target resource.
            ENDPOINT_PERMISSION_DENIED (4):
                The Google Workspace application doesn't have
                access to deliver events to your subscription's
                notification endpoint.
            ENDPOINT_NOT_FOUND (6):
                The subscription's notification endpoint
                doesn't exist, or the endpoint can't be found in
                the Google Cloud project where you created the
                subscription.
            ENDPOINT_RESOURCE_EXHAUSTED (7):
                The subscription's notification endpoint
                failed to receive events due to insufficient
                quota or reaching rate limiting.
            OTHER (5):
                An unidentified error has occurred.
        """

        ERROR_TYPE_UNSPECIFIED = 0
        USER_SCOPE_REVOKED = 1
        RESOURCE_DELETED = 2
        USER_AUTHORIZATION_FAILURE = 3
        ENDPOINT_PERMISSION_DENIED = 4
        ENDPOINT_NOT_FOUND = 6
        ENDPOINT_RESOURCE_EXHAUSTED = 7
        OTHER = 5

    expire_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=13,
        oneof="expiration",
        message=timestamp_pb2.Timestamp,
    )
    ttl: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=14,
        oneof="expiration",
        message=duration_pb2.Duration,
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=2,
    )
    target_resource: str = proto.Field(
        proto.STRING,
        number=4,
    )
    event_types: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )
    payload_options: "PayloadOptions" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="PayloadOptions",
    )
    notification_endpoint: "NotificationEndpoint" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="NotificationEndpoint",
    )
    state: State = proto.Field(
        proto.ENUM,
        number=8,
        enum=State,
    )
    suspension_reason: ErrorType = proto.Field(
        proto.ENUM,
        number=18,
        enum=ErrorType,
    )
    authority: str = proto.Field(
        proto.STRING,
        number=10,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=11,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=12,
        message=timestamp_pb2.Timestamp,
    )
    reconciling: bool = proto.Field(
        proto.BOOL,
        number=15,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=17,
    )


class PayloadOptions(proto.Message):
    r"""Options about what data to include in the event payload. Only
    supported for Google Chat events.

    Attributes:
        include_resource (bool):
            Optional. Whether the event payload includes data about the
            resource that changed. For example, for an event where a
            Google Chat message was created, whether the payload
            contains data about the
            ```Message`` <https://developers.google.com/chat/api/reference/rest/v1/spaces.messages>`__
            resource. If false, the event payload only includes the name
            of the changed resource.
        field_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. If ``include_resource`` is set to ``true``, the
            list of fields to include in the event payload. Separate
            fields with a comma. For example, to include a Google Chat
            message's sender and create time, enter
            ``message.sender,message.createTime``. If omitted, the
            payload includes all fields for the resource.

            If you specify a field that doesn't exist for the resource,
            the system ignores the field.
    """

    include_resource: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    field_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class NotificationEndpoint(proto.Message):
    r"""The endpoint where the subscription delivers events.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        pubsub_topic (str):
            Immutable. The Cloud Pub/Sub topic that receives events for
            the subscription.

            Format: ``projects/{project}/topics/{topic}``

            You must create the topic in the same Google Cloud project
            where you create this subscription.

            When the topic receives events, the events are encoded as
            Cloud Pub/Sub messages. For details, see the `Google Cloud
            Pub/Sub Protocol Binding for
            CloudEvents <https://github.com/googleapis/google-cloudevents/blob/main/docs/spec/pubsub.md>`__.

            This field is a member of `oneof`_ ``endpoint``.
    """

    pubsub_topic: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="endpoint",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
