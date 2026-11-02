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

from google.apps.chat_v1.types import membership as gc_membership
from google.apps.chat_v1.types import message as gc_message
from google.apps.chat_v1.types import reaction as gc_reaction
from google.apps.chat_v1.types import space as gc_space

__protobuf__ = proto.module(
    package="google.chat.v1",
    manifest={
        "MembershipCreatedEventData",
        "MembershipDeletedEventData",
        "MembershipUpdatedEventData",
        "MembershipBatchCreatedEventData",
        "MembershipBatchUpdatedEventData",
        "MembershipBatchDeletedEventData",
        "MessageCreatedEventData",
        "MessageUpdatedEventData",
        "MessageDeletedEventData",
        "MessageBatchCreatedEventData",
        "MessageBatchUpdatedEventData",
        "MessageBatchDeletedEventData",
        "SpaceUpdatedEventData",
        "SpaceBatchUpdatedEventData",
        "ReactionCreatedEventData",
        "ReactionDeletedEventData",
        "ReactionBatchCreatedEventData",
        "ReactionBatchDeletedEventData",
    },
)


class MembershipCreatedEventData(proto.Message):
    r"""Event payload for a new membership.

    Event type: ``google.workspace.chat.membership.v1.created``.

    Attributes:
        membership (google.apps.chat_v1.types.Membership):
            The new membership.
    """

    membership: gc_membership.Membership = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gc_membership.Membership,
    )


class MembershipDeletedEventData(proto.Message):
    r"""Event payload for a deleted membership.

    Event type: ``google.workspace.chat.membership.v1.deleted``

    Attributes:
        membership (google.apps.chat_v1.types.Membership):
            The deleted membership. Only the ``name`` and ``state``
            fields are populated.
    """

    membership: gc_membership.Membership = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gc_membership.Membership,
    )


class MembershipUpdatedEventData(proto.Message):
    r"""Event payload for an updated membership.

    Event type: ``google.workspace.chat.membership.v1.updated``

    Attributes:
        membership (google.apps.chat_v1.types.Membership):
            The updated membership.
    """

    membership: gc_membership.Membership = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gc_membership.Membership,
    )


class MembershipBatchCreatedEventData(proto.Message):
    r"""Event payload for multiple new memberships.

    Event type: ``google.workspace.chat.membership.v1.batchCreated``

    Attributes:
        memberships (MutableSequence[google.apps.chat_v1.types.MembershipCreatedEventData]):
            A list of new memberships.
    """

    memberships: MutableSequence["MembershipCreatedEventData"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="MembershipCreatedEventData",
    )


class MembershipBatchUpdatedEventData(proto.Message):
    r"""Event payload for multiple updated memberships.

    Event type: ``google.workspace.chat.membership.v1.batchUpdated``

    Attributes:
        memberships (MutableSequence[google.apps.chat_v1.types.MembershipUpdatedEventData]):
            A list of updated memberships.
    """

    memberships: MutableSequence["MembershipUpdatedEventData"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="MembershipUpdatedEventData",
    )


class MembershipBatchDeletedEventData(proto.Message):
    r"""Event payload for multiple deleted memberships.

    Event type: ``google.workspace.chat.membership.v1.batchDeleted``

    Attributes:
        memberships (MutableSequence[google.apps.chat_v1.types.MembershipDeletedEventData]):
            A list of deleted memberships.
    """

    memberships: MutableSequence["MembershipDeletedEventData"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="MembershipDeletedEventData",
    )


class MessageCreatedEventData(proto.Message):
    r"""Event payload for a new message.

    Event type: ``google.workspace.chat.message.v1.created``

    Attributes:
        message (google.apps.chat_v1.types.Message):
            The new message.
    """

    message: gc_message.Message = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gc_message.Message,
    )


class MessageUpdatedEventData(proto.Message):
    r"""Event payload for an updated message.

    Event type: ``google.workspace.chat.message.v1.updated``

    Attributes:
        message (google.apps.chat_v1.types.Message):
            The updated message.
    """

    message: gc_message.Message = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gc_message.Message,
    )


class MessageDeletedEventData(proto.Message):
    r"""Event payload for a deleted message.

    Event type: ``google.workspace.chat.message.v1.deleted``

    Attributes:
        message (google.apps.chat_v1.types.Message):
            The deleted message. Only the ``name``, ``createTime``, and
            ``deletionMetadata`` fields are populated.
    """

    message: gc_message.Message = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gc_message.Message,
    )


class MessageBatchCreatedEventData(proto.Message):
    r"""Event payload for multiple new messages.

    Event type: ``google.workspace.chat.message.v1.batchCreated``

    Attributes:
        messages (MutableSequence[google.apps.chat_v1.types.MessageCreatedEventData]):
            A list of new messages.
    """

    messages: MutableSequence["MessageCreatedEventData"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="MessageCreatedEventData",
    )


class MessageBatchUpdatedEventData(proto.Message):
    r"""Event payload for multiple updated messages.

    Event type: ``google.workspace.chat.message.v1.batchUpdated``

    Attributes:
        messages (MutableSequence[google.apps.chat_v1.types.MessageUpdatedEventData]):
            A list of updated messages.
    """

    messages: MutableSequence["MessageUpdatedEventData"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="MessageUpdatedEventData",
    )


class MessageBatchDeletedEventData(proto.Message):
    r"""Event payload for multiple deleted messages.

    Event type: ``google.workspace.chat.message.v1.batchDeleted``

    Attributes:
        messages (MutableSequence[google.apps.chat_v1.types.MessageDeletedEventData]):
            A list of deleted messages.
    """

    messages: MutableSequence["MessageDeletedEventData"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="MessageDeletedEventData",
    )


class SpaceUpdatedEventData(proto.Message):
    r"""Event payload for an updated space.

    Event type: ``google.workspace.chat.space.v1.updated``

    Attributes:
        space (google.apps.chat_v1.types.Space):
            The updated space.
    """

    space: gc_space.Space = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gc_space.Space,
    )


class SpaceBatchUpdatedEventData(proto.Message):
    r"""Event payload for multiple updates to a space.

    Event type: ``google.workspace.chat.space.v1.batchUpdated``

    Attributes:
        spaces (MutableSequence[google.apps.chat_v1.types.SpaceUpdatedEventData]):
            A list of updated spaces.
    """

    spaces: MutableSequence["SpaceUpdatedEventData"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="SpaceUpdatedEventData",
    )


class ReactionCreatedEventData(proto.Message):
    r"""Event payload for a new reaction.

    Event type: ``google.workspace.chat.reaction.v1.created``

    Attributes:
        reaction (google.apps.chat_v1.types.Reaction):
            The new reaction.
    """

    reaction: gc_reaction.Reaction = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gc_reaction.Reaction,
    )


class ReactionDeletedEventData(proto.Message):
    r"""Event payload for a deleted reaction.

    Type: ``google.workspace.chat.reaction.v1.deleted``

    Attributes:
        reaction (google.apps.chat_v1.types.Reaction):
            The deleted reaction.
    """

    reaction: gc_reaction.Reaction = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gc_reaction.Reaction,
    )


class ReactionBatchCreatedEventData(proto.Message):
    r"""Event payload for multiple new reactions.

    Event type: ``google.workspace.chat.reaction.v1.batchCreated``

    Attributes:
        reactions (MutableSequence[google.apps.chat_v1.types.ReactionCreatedEventData]):
            A list of new reactions.
    """

    reactions: MutableSequence["ReactionCreatedEventData"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ReactionCreatedEventData",
    )


class ReactionBatchDeletedEventData(proto.Message):
    r"""Event payload for multiple deleted reactions.

    Event type: ``google.workspace.chat.reaction.v1.batchDeleted``

    Attributes:
        reactions (MutableSequence[google.apps.chat_v1.types.ReactionDeletedEventData]):
            A list of deleted reactions.
    """

    reactions: MutableSequence["ReactionDeletedEventData"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ReactionDeletedEventData",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
