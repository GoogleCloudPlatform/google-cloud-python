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

from google.apps.chat_v1.types import reaction

__protobuf__ = proto.module(
    package="google.chat.v1",
    manifest={
        "Availability",
        "CustomStatus",
        "DoNotDisturbMetadata",
        "GetAvailabilityRequest",
        "UpdateAvailabilityRequest",
        "MarkAsActiveRequest",
        "MarkAsAwayRequest",
        "MarkAsDoNotDisturbRequest",
    },
)


class Availability(proto.Message):
    r"""Represents a user's current availability information in
    Google Chat, including their state (for example, Active, Away,
    Do Not Disturb) and any custom status.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. Resource name of the user's availability.

            Format: ``users/{user}/availability``

            ``{user}`` is the id for the Person in the People API or
            Admin SDK directory API. For example, ``users/123456789``.

            The user's email address or ``me`` can also be used as an
            alias to refer to the caller. For example,
            ``users/user@example.com`` or ``users/me``.
        state (google.apps.chat_v1.types.Availability.State):
            Output only. The user's current availability
            state.
        do_not_disturb_metadata (google.apps.chat_v1.types.DoNotDisturbMetadata):
            Output only. Metadata if the user state is set to
            DO_NOT_DISTURB.

            This field is a member of `oneof`_ ``state_metadata``.
        custom_status (google.apps.chat_v1.types.CustomStatus):
            Optional. The user's custom status.
    """

    class State(proto.Enum):
        r"""Represents the current availability state of the user.

        Values:
            STATE_UNSPECIFIED (0):
                Default value. The state is unspecified.
            ACTIVE (1):
                The user is currently active, based on recent
                activity.
            IDLE (2):
                The user is currently idle. This state
                indicates a period of inactivity after being
                ACTIVE, before potentially transitioning to
                AWAY.
            AWAY (3):
                The user is currently away. This can be either automatically
                set after a period of inactivity in ACTIVE or IDLE state, or
                it can be manually set by the user. When manually set via
                ``MarkAsAway``, this state persists regardless of user
                activity.
            DO_NOT_DISTURB (4):
                The user is in Do Not Disturb state, which is
                manually set.
        """

        STATE_UNSPECIFIED = 0
        ACTIVE = 1
        IDLE = 2
        AWAY = 3
        DO_NOT_DISTURB = 4

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=2,
        enum=State,
    )
    do_not_disturb_metadata: "DoNotDisturbMetadata" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="state_metadata",
        message="DoNotDisturbMetadata",
    )
    custom_status: "CustomStatus" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="CustomStatus",
    )


class CustomStatus(proto.Message):
    r"""Represents a user's custom status in Google Chat.
    This includes a short text message with an optional emoji that a
    user sets to give more context about their availability.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        text (str):
            Required. The text of the custom status. This
            will be a string with maximum length of 64.
        emoji (google.apps.chat_v1.types.Emoji):
            Required. The emoji of the custom status.
            Only Unicode emojis are supported; custom emojis
            are not supported.
        expire_time (google.protobuf.timestamp_pb2.Timestamp):
            The timestamp when the custom status expires.

            This field is a member of `oneof`_ ``expiration``.
        ttl (google.protobuf.duration_pb2.Duration):
            Input only. The time-to-live duration after
            which the custom status expires.

            This field is a member of `oneof`_ ``expiration``.
    """

    text: str = proto.Field(
        proto.STRING,
        number=1,
    )
    emoji: reaction.Emoji = proto.Field(
        proto.MESSAGE,
        number=2,
        message=reaction.Emoji,
    )
    expire_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="expiration",
        message=timestamp_pb2.Timestamp,
    )
    ttl: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="expiration",
        message=duration_pb2.Duration,
    )


class DoNotDisturbMetadata(proto.Message):
    r"""Metadata associated with the ``DO_NOT_DISTURB`` availability state,
    specifying when the state is set to expire.

    Attributes:
        expiration_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp until which the user should be marked
            as DO_NOT_DISTURB. This can be maximum of 1 year in the
            future.
    """

    expiration_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )


class GetAvailabilityRequest(proto.Message):
    r"""Request message for the ``GetAvailability`` method.

    Attributes:
        name (str):
            Required. The resource name of the availability to retrieve.

            Format: users/{user}/availability

            ``{user}`` is the id for the Person in the People API or
            Admin SDK directory API. For example, ``users/123456789``.

            The user's email address or ``me`` can also be used as an
            alias to refer to the caller. For example,
            ``users/user@example.com`` or ``users/me``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateAvailabilityRequest(proto.Message):
    r"""Request message for the ``UpdateAvailability`` method.

    Attributes:
        availability (google.apps.chat_v1.types.Availability):
            Required. The availability to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The list of fields to update. The only field that
            can be updated is ``custom_status``.
    """

    availability: "Availability" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Availability",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class MarkAsActiveRequest(proto.Message):
    r"""Request message for the ``MarkAsActive`` method.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Required. The resource name of the availability to mark as
            active. Format: users/{user}/availability

            ``{user}`` is the id for the Person in the People API or
            Admin SDK directory API. For example, ``users/123456789``.

            The user's email address or ``me`` can also be used as an
            alias to refer to the caller. For example,
            ``users/user@example.com`` or ``users/me``.
        expire_time (google.protobuf.timestamp_pb2.Timestamp):
            The absolute timestamp when the ACTIVE state
            expires.

            This field is a member of `oneof`_ ``expiration``.
        ttl (google.protobuf.duration_pb2.Duration):
            The duration from the current time until the
            ACTIVE state expires. Using a short TTL can
            effectively reset the user's state to be based
            on activity after this brief duration.

            This field is a member of `oneof`_ ``expiration``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    expire_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="expiration",
        message=timestamp_pb2.Timestamp,
    )
    ttl: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="expiration",
        message=duration_pb2.Duration,
    )


class MarkAsAwayRequest(proto.Message):
    r"""Request message for the ``MarkAsAway`` method.

    Attributes:
        name (str):
            Required. The resource name of the availability to mark as
            away. Format: users/{user}/availability

            ``{user}`` is the id for the Person in the People API or
            Admin SDK directory API. For example, ``users/123456789``.

            The user's email address or ``me`` can also be used as an
            alias to refer to the caller. For example,
            ``users/user@example.com`` or ``users/me``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class MarkAsDoNotDisturbRequest(proto.Message):
    r"""Request message for the ``MarkAsDoNotDisturb`` method.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Required. The resource name of the availability to mark as
            Do Not Disturb. Format: users/{user}/availability

            ``{user}`` is the id for the Person in the People API or
            Admin SDK directory API. For example, ``users/123456789``.

            The user's email address or ``me`` can also be used as an
            alias to refer to the caller. For example,
            ``users/user@example.com`` or ``users/me``.
        expire_time (google.protobuf.timestamp_pb2.Timestamp):
            The absolute timestamp when the DND state
            expires.

            This field is a member of `oneof`_ ``expiration``.
        ttl (google.protobuf.duration_pb2.Duration):
            The duration from the current time until the
            DND state expires.

            This field is a member of `oneof`_ ``expiration``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    expire_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="expiration",
        message=timestamp_pb2.Timestamp,
    )
    ttl: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="expiration",
        message=duration_pb2.Duration,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
