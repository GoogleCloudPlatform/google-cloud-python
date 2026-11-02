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
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.devicesandservices.health.v4",
    manifest={
        "CreateSubscriberRequest",
        "ListSubscribersRequest",
        "ListSubscribersResponse",
        "UpdateSubscriberRequest",
        "DeleteSubscriberRequest",
        "CreateSubscriptionRequest",
        "ListSubscriptionsRequest",
        "ListSubscriptionsResponse",
        "UpdateSubscriptionRequest",
        "DeleteSubscriptionRequest",
        "Subscriber",
        "Subscription",
        "SubscriberConfig",
        "EndpointAuthorization",
        "CreateSubscriberPayload",
        "CreateSubscriptionPayload",
        "CreateSubscriberMetadata",
        "UpdateSubscriberMetadata",
        "DeleteSubscriberMetadata",
    },
)


class CreateSubscriberRequest(proto.Message):
    r"""-- Messages --
    Request message for CreateSubscriber.

    Attributes:
        parent (str):
            Required. The parent resource where this subscriber will be
            created. Format: projects/{project_number} Example:
            projects/1234567890
        subscriber (google.devicesandservices.health_v4.types.CreateSubscriberPayload):
            Required. The subscriber to create.
        subscriber_id (str):
            Optional. The ID to use for the subscriber, which will
            become the final component of the subscriber's resource
            name.

            This value should be 4-36 characters, and valid characters
            are /`a-z <[a-z0-9-]{2,34}[a-z0-9]>`__/.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    subscriber: "CreateSubscriberPayload" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="CreateSubscriberPayload",
    )
    subscriber_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListSubscribersRequest(proto.Message):
    r"""Request message for ListSubscribers.

    Attributes:
        parent (str):
            Required. The parent, which owns this
            collection of subscribers. Format:
            projects/{project}
        page_size (int):
            Optional. The maximum number of subscribers
            to return. The service may return fewer than
            this value. If unspecified, at most 50
            subscribers will be returned. The maximum value
            is 1000; values above 1000 will be coerced to
            1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListSubscribers`` call. Provide this to retrieve the
            subsequent page. When paginating, all other parameters
            provided to ``ListSubscribers`` must match the call that
            provided the page token.
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


class ListSubscribersResponse(proto.Message):
    r"""Response message for ListSubscribers.

    Attributes:
        subscribers (MutableSequence[google.devicesandservices.health_v4.types.Subscriber]):
            Subscribers from the specified project.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        total_size (int):
            The total number of subscribers matching the
            request.
    """

    @property
    def raw_page(self):
        return self

    subscribers: MutableSequence["Subscriber"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Subscriber",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    total_size: int = proto.Field(
        proto.INT32,
        number=3,
    )


class UpdateSubscriberRequest(proto.Message):
    r"""Request message for UpdateSubscriber.

    Attributes:
        subscriber (google.devicesandservices.health_v4.types.Subscriber):
            Required. The subscriber resource to update. Its 'name'
            field is mapped to the URI, and the value of the 'name'
            field should be of the form:
            "projects/{project}/subscribers/{subscriber_id}". The
            remaining fields of the Subscriber object represent the new
            values for the corresponding fields in the existing
            subscriber resource.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. A field mask that specifies which fields of the
            Subscriber message are to be updated. This allows for
            partial updates. Supported fields:

            - endpoint_uri
            - subscriber_configs
            - endpoint_authorization
    """

    subscriber: "Subscriber" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Subscriber",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteSubscriberRequest(proto.Message):
    r"""Request message for DeleteSubscriber.

    Attributes:
        name (str):
            Required. The name of the subscriber to delete. Format:
            projects/{project}/subscribers/{subscriber} Example:
            projects/my-project/subscribers/my-subscriber-123 The
            {subscriber} ID is user-settable (4-36 characters, matching
            /`a-z <[a-z0-9-]{2,34}[a-z0-9]>`__/) or system-generated if
            not provided during creation.
        force (bool):
            Optional. If set to true, any child resources
            (e.g., subscriptions) will also be deleted. If
            false (default) and child resources exist, the
            request will fail.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class CreateSubscriptionRequest(proto.Message):
    r"""Request message for CreateSubscription.

    Attributes:
        parent (str):
            Required. The parent subscriber. Format:
            projects/{project}/subscribers/{subscriber} The {subscriber}
            ID is user-settable (4-36 characters, matching
            /`a-z <[a-z0-9-]{2,34}[a-z0-9]>`__/) if provided during
            creation, or system-generated otherwise.
        subscription_id (str):
            Optional. The {subscription_id} is user-settable (4-36
            chars, matching /`a-z <[a-z0-9-]{2,34}[a-z0-9]>`__/) or
            system-generated otherwise. If provided, the ID must be
            unique within the parent subscriber.
        subscription (google.devicesandservices.health_v4.types.CreateSubscriptionPayload):
            Required. The subscription to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    subscription_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    subscription: "CreateSubscriptionPayload" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="CreateSubscriptionPayload",
    )


class ListSubscriptionsRequest(proto.Message):
    r"""Request message for ListSubscriptions.

    Attributes:
        parent (str):
            Required. The parent subscriber. Format:
            projects/{project}/subscribers/{subscriber} The {subscriber}
            ID is user-settable (4-36 characters, matching
            /`a-z <[a-z0-9-]{2,34}[a-z0-9]>`__/) if provided during
            creation, or system-generated otherwise.
        filter (str):
            Optional. A filter to apply to the list of subscriptions.
            The filter syntax is described in
            https://google.aip.dev/160. The filter can be applied to the
            following fields:

            - ``user``
            - ``data_type``

            The ``user`` identifier (e.g., ``user1`` in ``users/user1``)
            refers to the public ``health_user_id``

            Example: user = "users/user1" Example: user = "users/user1"
            OR user = "users/user2" Example: user = "users/user1" AND
            (data_type = "sleep" OR data_type = "weight")
        page_size (int):
            Optional. The maximum number of subscriptions
            to return. The service may return fewer than
            this value. If unspecified, at most 50
            subscriptions will be returned. The maximum
            value is 1000; values above 1000 will be coerced
            to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListSubscriptions`` call. Provide this to retrieve the
            subsequent page. When paginating, all other parameters
            provided to ``ListSubscriptions`` must match the call that
            provided the page token.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListSubscriptionsResponse(proto.Message):
    r"""Response message for ListSubscriptions.

    Attributes:
        subscriptions (MutableSequence[google.devicesandservices.health_v4.types.Subscription]):
            The subscriptions from the specified
            subscriber.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    subscriptions: MutableSequence["Subscription"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Subscription",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class UpdateSubscriptionRequest(proto.Message):
    r"""Request message for UpdateSubscription.

    Attributes:
        subscription (google.devicesandservices.health_v4.types.Subscription):
            Required. The subscription to update. The subscription's
            ``name`` field is used to identify the subscription to
            update. Format:
            projects/{project}/subscribers/{subscriber}/subscriptions/{subscription}
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update.
    """

    subscription: "Subscription" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Subscription",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteSubscriptionRequest(proto.Message):
    r"""Request message for DeleteSubscription.

    Attributes:
        name (str):
            Required. The resource name of the subscription to delete.
            Format:
            ``projects/{project}/subscribers/{subscriber}/subscriptions/{subscription}``
            Example:
            ``projects/my-project/subscribers/my-subscriber-123/subscriptions/my-subscription-456``
            The {subscriber} ID is user-settable (4-36 characters,
            matching /`a-z <[a-z0-9-]{2,34}[a-z0-9]>`__/) if provided
            during creation, or system-generated otherwise. The
            {subscription} ID is user-settable (4-36 characters,
            matching /`a-z <[a-z0-9-]{2,34}[a-z0-9]>`__/) or
            system-generated if not provided during creation.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class Subscriber(proto.Message):
    r"""-- Resource Messages --
    A subscriber receives notifications from Google Health API.

    Attributes:
        name (str):
            Identifier. The resource name of the Subscriber. Format:
            projects/{project}/subscribers/{subscriber} The {project} ID
            is a Google Cloud Project ID or Project Number. The
            {subscriber} ID is user-settable (4-36 characters, matching
            /`a-z <[a-z0-9-]{2,34}[a-z0-9]>`__/) if provided during
            creation, or system-generated otherwise (e.g., a UUID).
            Example (User-settable subscriber ID):
            projects/my-project/subscribers/my-sub-123 Example
            (System-generated subscriber ID):
            projects/my-project/subscribers/a1b2c3d4-e5f6-7890-1234-567890abcdef
        endpoint_uri (str):
            Required. The full HTTPS URI where update
            notifications will be sent. The URI must be a
            valid URL and use HTTPS as the scheme. This
            endpoint will be verified during
            CreateSubscriber and UpdateSubscriber calls. See
            RPC documentation for verification details.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which the subscriber
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which the subscriber
            was last updated.
        subscriber_configs (MutableSequence[google.devicesandservices.health_v4.types.SubscriberConfig]):
            Optional. Configuration for the subscriber.
        endpoint_authorization (google.devicesandservices.health_v4.types.EndpointAuthorization):
            Required. Authorization mechanism for a
            subscriber endpoint. This is required to ensure
            the endpoint can be verified.
        state (google.devicesandservices.health_v4.types.Subscriber.State):
            Output only. The state of the subscriber.
    """

    class State(proto.Enum):
        r"""The state of the subscriber.

        Values:
            STATE_UNSPECIFIED (0):
                Represents an unspecified subscriber state.
            UNVERIFIED (1):
                Represents an unverified subscriber. This is the initial
                state of the subscriber when it is created. The backend will
                verify the subscriber's endpoint_uri.
            ACTIVE (2):
                Represents an active subscriber. The endpoint
                has been verified.
            INACTIVE (3):
                Represents an inactive subscriber.
        """

        STATE_UNSPECIFIED = 0
        UNVERIFIED = 1
        ACTIVE = 2
        INACTIVE = 3

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    endpoint_uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    subscriber_configs: MutableSequence["SubscriberConfig"] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message="SubscriberConfig",
    )
    endpoint_authorization: "EndpointAuthorization" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="EndpointAuthorization",
    )
    state: State = proto.Field(
        proto.ENUM,
        number=6,
        enum=State,
    )


class Subscription(proto.Message):
    r"""A subscription to a data collection for a specific user, to
    be delivered to a subscriber.

    Attributes:
        name (str):
            Identifier. The resource name of the Subscription. Format:
            ``projects/{project}/subscribers/{subscriber}/subscriptions/{subscription}``
            Example:
            ``projects/my-project/subscribers/my-subscriber-123/subscriptions/my-subscription-456``
            The {project} ID is mandatory (6-30 characters, matching
            /[a-z][a-z0-9-]{6,30}/) The {subscriber} ID is user-settable
            (4-36 characters, matching
            /`a-z <[a-z0-9-]{2,34}[a-z0-9]>`__/) if provided during
            creation, or system-generated otherwise. The {subscription}
            ID is user-settable (4-36 chars, matching
            /`a-z <[a-z0-9-]{2,34}[a-z0-9]>`__/) or system-generated
            otherwise.
        data_types (MutableSequence[str]):
            Optional. Data types subscribed to. A subscriber will only
            receive notifications for data types that are declared here.
            A subscription can only subscribe to the data types of the
            subscriber. The values should be in the format
            "users/{health_user_id}/dataTypes/{data_type}" where
            ``{data_type}`` is one of "altitude", "distance", "floors",
            "sleep", "steps", "weight".
        user (str):
            Immutable. The resource name of the user for whom this
            subscription is active. Format: ``users/{user}`` where
            ``{user}`` is the public ``healthUserId`` as returned by the
            ``GetIdentity`` action in the profile PAPI (see
            ``google.devicesandservices.health.v4main.HealthProfileService.GetIdentity``).
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    data_types: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    user: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SubscriberConfig(proto.Message):
    r"""Configuration for a subscriber.
    A notification is sent to a subscription ONLY if the subscriber
    has a config for the data type.

    Attributes:
        data_types (MutableSequence[str]):
            Required. See `Google Health API data
            types <https://developers.google.com/health/data-types>`__
            for the list of supported data types. Values should be in
            kebab-case.
        subscription_create_policy (google.devicesandservices.health_v4.types.SubscriberConfig.SubscriptionCreatePolicy):
            Required. Policy for subscription creation.
    """

    class SubscriptionCreatePolicy(proto.Enum):
        r"""Policy for subscription creation.

        Values:
            SUBSCRIPTION_CREATE_POLICY_UNSPECIFIED (0):
                Represents an unspecified policy.
            AUTOMATIC (1):
                When using ``AUTOMATIC``, individual subscriptions are not
                created or stored. Instead, eligibility for notifications is
                computed dynamically. When a data update occurs for a given
                data type, notifications are sent to all subscribers with an
                ``AUTOMATIC`` policy for that data type, provided the user
                has granted the necessary consents.

                This means you do not need to call ``CreateSubscription``
                for each user; notifications are managed automatically based
                on user consents. As ``Subscription`` resources are not
                stored, they cannot be retrieved or managed through
                ``GetSubscription``, ``ListSubscriptions``,
                ``UpdateSubscription``, or ``DeleteSubscription``.
            MANUAL (2):
                Requires subscriptions to be created manually
                for new users. The developer needs to call
                CreateSubscription for new users.
        """

        SUBSCRIPTION_CREATE_POLICY_UNSPECIFIED = 0
        AUTOMATIC = 1
        MANUAL = 2

    data_types: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    subscription_create_policy: SubscriptionCreatePolicy = proto.Field(
        proto.ENUM,
        number=2,
        enum=SubscriptionCreatePolicy,
    )


class EndpointAuthorization(proto.Message):
    r"""Authorization mechanism for a subscriber endpoint. For all requests
    sent by the Webhooks service, the JSON payload is cryptographically
    signed. The signature is delivered in the
    ``GOOGLE-HEALTH-API-SIGNATURE`` HTTP header. This is an ECDSA (NIST
    P256) signature of the JSON payload. Clients must verify this
    signature using Google Health API's public key to confirm the
    payload was sent by the Health API.

    Attributes:
        secret (str):
            Required. Input only. Provides a client-provided secret that
            will be sent with each notification to the subscriber
            endpoint using the "Authorization" header. The value must
            include the authorization scheme, e.g., "Bearer " or "Basic
            ", as it will be used as the full Authorization header
            value. This secret is used by the API to test the endpoint
            during ``CreateSubscriber`` and ``UpdateSubscriber`` calls,
            and will be sent in the ``Authorization`` header for all
            subsequent webhook notifications to this endpoint.
        secret_set (bool):
            Output only. Whether the secret is set.
    """

    secret: str = proto.Field(
        proto.STRING,
        number=1,
    )
    secret_set: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class CreateSubscriberPayload(proto.Message):
    r"""Payload for creating a subscriber.

    Attributes:
        endpoint_uri (str):
            Required. The full HTTPS URI where update notifications will
            be sent. The URI must be a valid URL and use HTTPS as the
            scheme. This endpoint will be verified during the
            ``CreateSubscriber`` call. See CreateSubscriber RPC
            documentation for verification details.
        subscriber_configs (MutableSequence[google.devicesandservices.health_v4.types.SubscriberConfig]):
            Optional. Configuration for the subscriber.
        endpoint_authorization (google.devicesandservices.health_v4.types.EndpointAuthorization):
            Required. Authorization mechanism for the subscriber
            endpoint. The ``secret`` within this message is crucial for
            endpoint verification and for securing webhook
            notifications.
    """

    endpoint_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    subscriber_configs: MutableSequence["SubscriberConfig"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="SubscriberConfig",
    )
    endpoint_authorization: "EndpointAuthorization" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="EndpointAuthorization",
    )


class CreateSubscriptionPayload(proto.Message):
    r"""Payload for creating a subscription.

    Attributes:
        data_types (MutableSequence[str]):
            Optional. Data types subscribed to.
        user (str):
            Required. Immutable. The resource name of the user for whom
            this subscription is active. Format: ``users/{user}`` where
            ``{user}`` is the public ``healthUserId`` as returned by the
            ``GetIdentity`` action in the profile PAPI (see
            ``google.devicesandservices.health.v4main.HealthProfileService.GetIdentity``).
    """

    data_types: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    user: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreateSubscriberMetadata(proto.Message):
    r"""Represents metadata for creating a subscriber."""


class UpdateSubscriberMetadata(proto.Message):
    r"""Represents metadata for updating a subscriber."""


class DeleteSubscriberMetadata(proto.Message):
    r"""Represents metadata for deleting a subscriber."""


__all__ = tuple(sorted(__protobuf__.manifest))
