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

from google.apps.chat_v1.types import user as gc_user

__protobuf__ = proto.module(
    package="google.chat.v1",
    manifest={
        "Reaction",
        "Emoji",
        "CustomEmoji",
        "EmojiReactionSummary",
        "CreateReactionRequest",
        "ListReactionsRequest",
        "ListReactionsResponse",
        "DeleteReactionRequest",
        "CreateCustomEmojiRequest",
        "GetCustomEmojiRequest",
        "ListCustomEmojisRequest",
        "ListCustomEmojisResponse",
        "DeleteCustomEmojiRequest",
    },
)


class Reaction(proto.Message):
    r"""A reaction to a message.

    Attributes:
        name (str):
            Identifier. The resource name of the reaction.

            Format:
            ``spaces/{space}/messages/{message}/reactions/{reaction}``
        user (google.apps.chat_v1.types.User):
            Output only. The user who created the
            reaction.
        emoji (google.apps.chat_v1.types.Emoji):
            Required. The emoji used in the reaction.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    user: gc_user.User = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gc_user.User,
    )
    emoji: "Emoji" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Emoji",
    )


class Emoji(proto.Message):
    r"""An emoji that is used as a reaction to a message.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        unicode (str):
            Optional. A basic emoji represented by a
            unicode string.

            This field is a member of `oneof`_ ``content``.
        custom_emoji (google.apps.chat_v1.types.CustomEmoji):
            A custom emoji.

            This field is a member of `oneof`_ ``content``.
    """

    unicode: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="content",
    )
    custom_emoji: "CustomEmoji" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="content",
        message="CustomEmoji",
    )


class CustomEmoji(proto.Message):
    r"""Represents a `custom
    emoji <https://support.google.com/chat/answer/12800149>`__.

    Attributes:
        name (str):
            Identifier. The resource name of the custom emoji, assigned
            by the server.

            Format: ``customEmojis/{customEmoji}``
        uid (str):
            Output only. Unique key for the custom emoji
            resource.
        emoji_name (str):
            Optional. Immutable. User-provided name for the custom
            emoji, which is unique within the organization.

            Required when the custom emoji is created, output only
            otherwise.

            Emoji names must start and end with colons, must be
            lowercase and can only contain alphanumeric characters,
            hyphens, and underscores. Hyphens and underscores should be
            used to separate words and cannot be used consecutively.

            Example: ``:valid-emoji-name:``
        temporary_image_uri (str):
            Output only. A temporary image URL for the
            custom emoji, valid for at least 10 minutes.
            Note that this is not populated in the response
            when the custom emoji is created.
        payload (google.apps.chat_v1.types.CustomEmoji.CustomEmojiPayload):
            Optional. Input only. Payload data.
            Required when the custom emoji is created.
    """

    class CustomEmojiPayload(proto.Message):
        r"""Payload data for the custom emoji.

        Attributes:
            file_content (bytes):
                Required. Input only. The image used for the
                custom emoji.
                The payload must be under 256 KB and the
                dimension of the image must be square and
                between 64 and 500 pixels. The restrictions are
                subject to change.
            filename (str):
                Required. Input only. The image file name.

                Supported file extensions: ``.png``, ``.jpg``, ``.gif``.
        """

        file_content: bytes = proto.Field(
            proto.BYTES,
            number=1,
        )
        filename: str = proto.Field(
            proto.STRING,
            number=2,
        )

    name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=1,
    )
    emoji_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    temporary_image_uri: str = proto.Field(
        proto.STRING,
        number=4,
    )
    payload: CustomEmojiPayload = proto.Field(
        proto.MESSAGE,
        number=5,
        message=CustomEmojiPayload,
    )


class EmojiReactionSummary(proto.Message):
    r"""The number of people who reacted to a message with a specific
    emoji.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        emoji (google.apps.chat_v1.types.Emoji):
            Output only. Emoji associated with the
            reactions.
        reaction_count (int):
            Output only. The total number of reactions
            using the associated emoji.

            This field is a member of `oneof`_ ``_reaction_count``.
    """

    emoji: "Emoji" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Emoji",
    )
    reaction_count: int = proto.Field(
        proto.INT32,
        number=2,
        optional=True,
    )


class CreateReactionRequest(proto.Message):
    r"""Creates a reaction to a message.

    Attributes:
        parent (str):
            Required. The message where the reaction is created.

            Format: ``spaces/{space}/messages/{message}``
        reaction (google.apps.chat_v1.types.Reaction):
            Required. The reaction to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    reaction: "Reaction" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Reaction",
    )


class ListReactionsRequest(proto.Message):
    r"""Lists reactions to a message.

    Attributes:
        parent (str):
            Required. The message users reacted to.

            Format: ``spaces/{space}/messages/{message}``
        page_size (int):
            Optional. The maximum number of reactions
            returned. The service can return fewer reactions
            than this value. If unspecified, the default
            value is 25. The maximum value is 200; values
            above 200 are changed to 200.
        page_token (str):
            Optional. (If resuming from a previous
            query.)
            A page token received from a previous list
            reactions call. Provide this to retrieve the
            subsequent page.

            When paginating, the filter value should match
            the call that provided the page token. Passing a
            different value might lead to unexpected
            results.
        filter (str):
            Optional. A query filter.

            You can filter reactions by
            `emoji <https://developers.google.com/workspace/chat/api/reference/rest/v1/Emoji>`__
            (either ``emoji.unicode`` or ``emoji.custom_emoji.uid``) and
            `user <https://developers.google.com/workspace/chat/api/reference/rest/v1/User>`__
            (``user.name``).

            To filter reactions for multiple emojis or users, join
            similar fields with the ``OR`` operator, such as
            ``emoji.unicode = "🙂" OR emoji.unicode = "👍"`` and
            ``user.name = "users/AAAAAA" OR user.name = "users/BBBBBB"``.

            To filter reactions by emoji and user, use the ``AND``
            operator, such as
            ``emoji.unicode = "🙂" AND user.name = "users/AAAAAA"``.

            If your query uses both ``AND`` and ``OR``, group them with
            parentheses.

            For example, the following queries are valid:

            ::

               user.name = "users/{user}"
               emoji.unicode = "🙂"
               emoji.custom_emoji.uid = "{uid}"
               emoji.unicode = "🙂" OR emoji.unicode = "👍"
               emoji.unicode = "🙂" OR emoji.custom_emoji.uid = "{uid}"
               emoji.unicode = "🙂" AND user.name = "users/{user}"
               (emoji.unicode = "🙂" OR emoji.custom_emoji.uid = "{uid}")
               AND user.name = "users/{user}"

            The following queries are invalid:

            ::

               emoji.unicode = "🙂" AND emoji.unicode = "👍"
               emoji.unicode = "🙂" AND emoji.custom_emoji.uid = "{uid}"
               emoji.unicode = "🙂" OR user.name = "users/{user}"
               emoji.unicode = "🙂" OR emoji.custom_emoji.uid = "{uid}" OR
               user.name = "users/{user}"
               emoji.unicode = "🙂" OR emoji.custom_emoji.uid = "{uid}"
               AND user.name = "users/{user}"

            Invalid queries are rejected with an ``INVALID_ARGUMENT``
            error.
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


class ListReactionsResponse(proto.Message):
    r"""Response to a list reactions request.

    Attributes:
        reactions (MutableSequence[google.apps.chat_v1.types.Reaction]):
            List of reactions in the requested (or first)
            page.
        next_page_token (str):
            Continuation token to retrieve the next page
            of results. It's empty for the last page of
            results.
    """

    @property
    def raw_page(self):
        return self

    reactions: MutableSequence["Reaction"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Reaction",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DeleteReactionRequest(proto.Message):
    r"""Deletes a reaction to a message.

    Attributes:
        name (str):
            Required. Name of the reaction to delete.

            Format:
            ``spaces/{space}/messages/{message}/reactions/{reaction}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateCustomEmojiRequest(proto.Message):
    r"""A request to create a custom emoji.

    Attributes:
        custom_emoji (google.apps.chat_v1.types.CustomEmoji):
            Required. The custom emoji to create.
    """

    custom_emoji: "CustomEmoji" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="CustomEmoji",
    )


class GetCustomEmojiRequest(proto.Message):
    r"""A request to return a single custom emoji.

    Attributes:
        name (str):
            Required. Resource name of the custom emoji.

            Format: ``customEmojis/{customEmoji}``

            You can use the emoji name as an alias for
            ``{customEmoji}``. For example,
            ``customEmojis/:example-emoji:`` where ``:example-emoji:``
            is the emoji name for a custom emoji.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListCustomEmojisRequest(proto.Message):
    r"""A request to return a list of custom emojis.

    Attributes:
        page_size (int):
            Optional. The maximum number of custom emojis
            returned. The service can return fewer custom
            emojis than this value. If unspecified, the
            default value is 25. The maximum value is 200;
            values above 200 are changed to 200.
        page_token (str):
            Optional. (If resuming from a previous
            query.)
            A page token received from a previous list
            custom emoji call. Provide this to retrieve the
            subsequent page.

            When paginating, the filter value should match
            the call that provided the page token. Passing a
            different value might lead to unexpected
            results.
        filter (str):
            Optional. A query filter.

            Supports filtering by creator.

            To filter by creator, you must specify a valid value.
            Currently only ``creator("users/me")`` and
            ``NOT creator("users/me")`` are accepted to filter custom
            emojis by whether they were created by the calling user or
            not.

            For example, the following query returns custom emojis
            created by the caller:

            ::

               creator("users/me")

            Invalid queries are rejected with an ``INVALID_ARGUMENT``
            error.
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


class ListCustomEmojisResponse(proto.Message):
    r"""A response to list custom emojis.

    Attributes:
        custom_emojis (MutableSequence[google.apps.chat_v1.types.CustomEmoji]):
            Unordered list. List of custom emojis.
        next_page_token (str):
            A token that you can send as ``pageToken`` to retrieve the
            next page of results. If empty, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    custom_emojis: MutableSequence["CustomEmoji"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="CustomEmoji",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DeleteCustomEmojiRequest(proto.Message):
    r"""Request for deleting a custom emoji.

    Attributes:
        name (str):
            Required. Resource name of the custom emoji to delete.

            Format: ``customEmojis/{customEmoji}``

            You can use the emoji name as an alias for
            ``{customEmoji}``. For example,
            ``customEmojis/:example-emoji:`` where ``:example-emoji:``
            is the emoji name for a custom emoji.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
