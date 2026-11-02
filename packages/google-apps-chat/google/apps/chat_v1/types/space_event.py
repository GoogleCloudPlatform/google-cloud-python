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

from google.apps.chat_v1.types import event_payload

__protobuf__ = proto.module(
    package="google.chat.v1",
    manifest={
        "SpaceEvent",
        "GetSpaceEventRequest",
        "ListSpaceEventsRequest",
        "ListSpaceEventsResponse",
    },
)


class SpaceEvent(proto.Message):
    r"""An event that represents a change or activity in a Google Chat
    space. To learn more, see `Work with events from Google
    Chat <https://developers.google.com/workspace/chat/events-overview>`__.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Resource name of the space event.

            Format: ``spaces/{space}/spaceEvents/{spaceEvent}``
        event_time (google.protobuf.timestamp_pb2.Timestamp):
            Time when the event occurred.
        event_type (str):
            Type of space event. Each event type has a batch version,
            which represents multiple instances of the event type that
            occur in a short period of time. For ``spaceEvents.list()``
            requests, omit batch event types in your query filter. By
            default, the server returns both event type and its batch
            version.

            Supported event types for
            `messages <https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces.messages>`__:

            ::

               * New message: `google.workspace.chat.message.v1.created`
               * Updated message: `google.workspace.chat.message.v1.updated`
               * Deleted message: `google.workspace.chat.message.v1.deleted`
               * Multiple new messages: `google.workspace.chat.message.v1.batchCreated`
               * Multiple updated messages:
               `google.workspace.chat.message.v1.batchUpdated`
               * Multiple deleted messages:
               `google.workspace.chat.message.v1.batchDeleted`

            Supported event types for
            `memberships <https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces.members>`__:

            - New membership:
              ``google.workspace.chat.membership.v1.created``
            - Updated membership:
              ``google.workspace.chat.membership.v1.updated``
            - Deleted membership:
              ``google.workspace.chat.membership.v1.deleted``
            - Multiple new memberships:
              ``google.workspace.chat.membership.v1.batchCreated``
            - Multiple updated memberships:
              ``google.workspace.chat.membership.v1.batchUpdated``
            - Multiple deleted memberships:
              ``google.workspace.chat.membership.v1.batchDeleted``

            Supported event types for
            `reactions <https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces.messages.reactions>`__:

            - New reaction:
              ``google.workspace.chat.reaction.v1.created``
            - Deleted reaction:
              ``google.workspace.chat.reaction.v1.deleted``
            - Multiple new reactions:
              ``google.workspace.chat.reaction.v1.batchCreated``
            - Multiple deleted reactions:
              ``google.workspace.chat.reaction.v1.batchDeleted``

            Supported event types about the
            `space <https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces>`__:

            - Updated space: ``google.workspace.chat.space.v1.updated``
            - Multiple space updates:
              ``google.workspace.chat.space.v1.batchUpdated``
        message_created_event_data (google.apps.chat_v1.types.MessageCreatedEventData):
            Event payload for a new message.

            Event type: ``google.workspace.chat.message.v1.created``

            This field is a member of `oneof`_ ``payload``.
        message_updated_event_data (google.apps.chat_v1.types.MessageUpdatedEventData):
            Event payload for an updated message.

            Event type: ``google.workspace.chat.message.v1.updated``

            This field is a member of `oneof`_ ``payload``.
        message_deleted_event_data (google.apps.chat_v1.types.MessageDeletedEventData):
            Event payload for a deleted message.

            Event type: ``google.workspace.chat.message.v1.deleted``

            This field is a member of `oneof`_ ``payload``.
        message_batch_created_event_data (google.apps.chat_v1.types.MessageBatchCreatedEventData):
            Event payload for multiple new messages.

            Event type:
            ``google.workspace.chat.message.v1.batchCreated``

            This field is a member of `oneof`_ ``payload``.
        message_batch_updated_event_data (google.apps.chat_v1.types.MessageBatchUpdatedEventData):
            Event payload for multiple updated messages.

            Event type:
            ``google.workspace.chat.message.v1.batchUpdated``

            This field is a member of `oneof`_ ``payload``.
        message_batch_deleted_event_data (google.apps.chat_v1.types.MessageBatchDeletedEventData):
            Event payload for multiple deleted messages.

            Event type:
            ``google.workspace.chat.message.v1.batchDeleted``

            This field is a member of `oneof`_ ``payload``.
        space_updated_event_data (google.apps.chat_v1.types.SpaceUpdatedEventData):
            Event payload for a space update.

            Event type: ``google.workspace.chat.space.v1.updated``

            This field is a member of `oneof`_ ``payload``.
        space_batch_updated_event_data (google.apps.chat_v1.types.SpaceBatchUpdatedEventData):
            Event payload for multiple updates to a space.

            Event type: ``google.workspace.chat.space.v1.batchUpdated``

            This field is a member of `oneof`_ ``payload``.
        membership_created_event_data (google.apps.chat_v1.types.MembershipCreatedEventData):
            Event payload for a new membership.

            Event type: ``google.workspace.chat.membership.v1.created``

            This field is a member of `oneof`_ ``payload``.
        membership_updated_event_data (google.apps.chat_v1.types.MembershipUpdatedEventData):
            Event payload for an updated membership.

            Event type: ``google.workspace.chat.membership.v1.updated``

            This field is a member of `oneof`_ ``payload``.
        membership_deleted_event_data (google.apps.chat_v1.types.MembershipDeletedEventData):
            Event payload for a deleted membership.

            Event type: ``google.workspace.chat.membership.v1.deleted``

            This field is a member of `oneof`_ ``payload``.
        membership_batch_created_event_data (google.apps.chat_v1.types.MembershipBatchCreatedEventData):
            Event payload for multiple new memberships.

            Event type:
            ``google.workspace.chat.membership.v1.batchCreated``

            This field is a member of `oneof`_ ``payload``.
        membership_batch_updated_event_data (google.apps.chat_v1.types.MembershipBatchUpdatedEventData):
            Event payload for multiple updated memberships.

            Event type:
            ``google.workspace.chat.membership.v1.batchUpdated``

            This field is a member of `oneof`_ ``payload``.
        membership_batch_deleted_event_data (google.apps.chat_v1.types.MembershipBatchDeletedEventData):
            Event payload for multiple deleted memberships.

            Event type:
            ``google.workspace.chat.membership.v1.batchDeleted``

            This field is a member of `oneof`_ ``payload``.
        reaction_created_event_data (google.apps.chat_v1.types.ReactionCreatedEventData):
            Event payload for a new reaction.

            Event type: ``google.workspace.chat.reaction.v1.created``

            This field is a member of `oneof`_ ``payload``.
        reaction_deleted_event_data (google.apps.chat_v1.types.ReactionDeletedEventData):
            Event payload for a deleted reaction.

            Event type: ``google.workspace.chat.reaction.v1.deleted``

            This field is a member of `oneof`_ ``payload``.
        reaction_batch_created_event_data (google.apps.chat_v1.types.ReactionBatchCreatedEventData):
            Event payload for multiple new reactions.

            Event type:
            ``google.workspace.chat.reaction.v1.batchCreated``

            This field is a member of `oneof`_ ``payload``.
        reaction_batch_deleted_event_data (google.apps.chat_v1.types.ReactionBatchDeletedEventData):
            Event payload for multiple deleted reactions.

            Event type:
            ``google.workspace.chat.reaction.v1.batchDeleted``

            This field is a member of `oneof`_ ``payload``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    event_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    event_type: str = proto.Field(
        proto.STRING,
        number=6,
    )
    message_created_event_data: event_payload.MessageCreatedEventData = proto.Field(
        proto.MESSAGE,
        number=12,
        oneof="payload",
        message=event_payload.MessageCreatedEventData,
    )
    message_updated_event_data: event_payload.MessageUpdatedEventData = proto.Field(
        proto.MESSAGE,
        number=13,
        oneof="payload",
        message=event_payload.MessageUpdatedEventData,
    )
    message_deleted_event_data: event_payload.MessageDeletedEventData = proto.Field(
        proto.MESSAGE,
        number=14,
        oneof="payload",
        message=event_payload.MessageDeletedEventData,
    )
    message_batch_created_event_data: event_payload.MessageBatchCreatedEventData = (
        proto.Field(
            proto.MESSAGE,
            number=26,
            oneof="payload",
            message=event_payload.MessageBatchCreatedEventData,
        )
    )
    message_batch_updated_event_data: event_payload.MessageBatchUpdatedEventData = (
        proto.Field(
            proto.MESSAGE,
            number=27,
            oneof="payload",
            message=event_payload.MessageBatchUpdatedEventData,
        )
    )
    message_batch_deleted_event_data: event_payload.MessageBatchDeletedEventData = (
        proto.Field(
            proto.MESSAGE,
            number=28,
            oneof="payload",
            message=event_payload.MessageBatchDeletedEventData,
        )
    )
    space_updated_event_data: event_payload.SpaceUpdatedEventData = proto.Field(
        proto.MESSAGE,
        number=15,
        oneof="payload",
        message=event_payload.SpaceUpdatedEventData,
    )
    space_batch_updated_event_data: event_payload.SpaceBatchUpdatedEventData = (
        proto.Field(
            proto.MESSAGE,
            number=29,
            oneof="payload",
            message=event_payload.SpaceBatchUpdatedEventData,
        )
    )
    membership_created_event_data: event_payload.MembershipCreatedEventData = (
        proto.Field(
            proto.MESSAGE,
            number=17,
            oneof="payload",
            message=event_payload.MembershipCreatedEventData,
        )
    )
    membership_updated_event_data: event_payload.MembershipUpdatedEventData = (
        proto.Field(
            proto.MESSAGE,
            number=18,
            oneof="payload",
            message=event_payload.MembershipUpdatedEventData,
        )
    )
    membership_deleted_event_data: event_payload.MembershipDeletedEventData = (
        proto.Field(
            proto.MESSAGE,
            number=219,
            oneof="payload",
            message=event_payload.MembershipDeletedEventData,
        )
    )
    membership_batch_created_event_data: event_payload.MembershipBatchCreatedEventData = proto.Field(
        proto.MESSAGE,
        number=31,
        oneof="payload",
        message=event_payload.MembershipBatchCreatedEventData,
    )
    membership_batch_updated_event_data: event_payload.MembershipBatchUpdatedEventData = proto.Field(
        proto.MESSAGE,
        number=32,
        oneof="payload",
        message=event_payload.MembershipBatchUpdatedEventData,
    )
    membership_batch_deleted_event_data: event_payload.MembershipBatchDeletedEventData = proto.Field(
        proto.MESSAGE,
        number=33,
        oneof="payload",
        message=event_payload.MembershipBatchDeletedEventData,
    )
    reaction_created_event_data: event_payload.ReactionCreatedEventData = proto.Field(
        proto.MESSAGE,
        number=21,
        oneof="payload",
        message=event_payload.ReactionCreatedEventData,
    )
    reaction_deleted_event_data: event_payload.ReactionDeletedEventData = proto.Field(
        proto.MESSAGE,
        number=22,
        oneof="payload",
        message=event_payload.ReactionDeletedEventData,
    )
    reaction_batch_created_event_data: event_payload.ReactionBatchCreatedEventData = (
        proto.Field(
            proto.MESSAGE,
            number=34,
            oneof="payload",
            message=event_payload.ReactionBatchCreatedEventData,
        )
    )
    reaction_batch_deleted_event_data: event_payload.ReactionBatchDeletedEventData = (
        proto.Field(
            proto.MESSAGE,
            number=35,
            oneof="payload",
            message=event_payload.ReactionBatchDeletedEventData,
        )
    )


class GetSpaceEventRequest(proto.Message):
    r"""Request message for getting a space event.

    Attributes:
        name (str):
            Required. The resource name of the space event.

            Format: ``spaces/{space}/spaceEvents/{spaceEvent}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListSpaceEventsRequest(proto.Message):
    r"""Request message for listing space events.

    Attributes:
        parent (str):
            Required. Resource name of the `Google Chat
            space <https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces>`__
            where the events occurred.

            Format: ``spaces/{space}``.
        page_size (int):
            Optional. The maximum number of space events returned. The
            service might return fewer than this value.

            Negative values return an ``INVALID_ARGUMENT`` error.
        page_token (str):
            Optional. A page token, received from a
            previous list space events call. Provide this to
            retrieve the subsequent page.

            When paginating, all other parameters provided
            to list space events must match the call that
            provided the page token. Passing different
            values to the other parameters might lead to
            unexpected results.
        filter (str):
            Required. A query filter.

            You must specify at least one event type (``event_type``)
            using the has ``:`` operator. To filter by multiple event
            types, use the ``OR`` operator. Omit batch event types in
            your filter. The request automatically returns any related
            batch events. For example, if you filter by new reactions
            (``google.workspace.chat.reaction.v1.created``), the server
            also returns batch new reactions events
            (``google.workspace.chat.reaction.v1.batchCreated``). For a
            list of supported event types, see the ```SpaceEvents``
            reference
            documentation <https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces.spaceEvents#SpaceEvent.FIELDS.event_type>`__.

            Optionally, you can also filter by start time
            (``start_time``) and end time (``end_time``):

            - ``start_time``: Exclusive timestamp from which to start
              listing space events. You can list events that occurred up
              to 28 days ago. If unspecified, lists space events from
              the past 28 days.
            - ``end_time``: Inclusive timestamp until which space events
              are listed. If unspecified, lists events up to the time of
              the request.

            To specify a start or end time, use the equals ``=``
            operator and format in
            `RFC-3339 <https://www.rfc-editor.org/rfc/rfc3339>`__. To
            filter by both ``start_time`` and ``end_time``, use the
            ``AND`` operator.

            For example, the following queries are valid:

            ::

               start_time="2023-08-23T19:20:33+00:00" AND
               end_time="2023-08-23T19:21:54+00:00"

            ::

               start_time="2023-08-23T19:20:33+00:00" AND
               (event_types:"google.workspace.chat.space.v1.updated" OR
               event_types:"google.workspace.chat.message.v1.created")

            The following queries are invalid:

            ::

               start_time="2023-08-23T19:20:33+00:00" OR
               end_time="2023-08-23T19:21:54+00:00"

            ::

               event_types:"google.workspace.chat.space.v1.updated" AND
               event_types:"google.workspace.chat.message.v1.created"

            Invalid queries are rejected by the server with an
            ``INVALID_ARGUMENT`` error.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=5,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=6,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=8,
    )


class ListSpaceEventsResponse(proto.Message):
    r"""Response message for listing space events.

    Attributes:
        space_events (MutableSequence[google.apps.chat_v1.types.SpaceEvent]):
            Results are returned in chronological order (oldest event
            first). Note: The ``permissionSettings`` field is not
            returned in the Space object for list requests.
        next_page_token (str):
            Continuation token used to fetch more events.
            If this field is omitted, there are no
            subsequent pages.
    """

    @property
    def raw_page(self):
        return self

    space_events: MutableSequence["SpaceEvent"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="SpaceEvent",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
