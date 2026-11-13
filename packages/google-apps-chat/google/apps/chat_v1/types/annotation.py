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

from google.apps.chat_v1.types import attachment, reaction
from google.apps.chat_v1.types import user as gc_user

__protobuf__ = proto.module(
    package="google.chat.v1",
    manifest={
        "AnnotationType",
        "Annotation",
        "UserMentionMetadata",
        "SlashCommandMetadata",
        "RichLinkMetadata",
        "CustomEmojiMetadata",
        "DriveLinkData",
        "ChatSpaceLinkData",
        "MeetSpaceLinkData",
        "CalendarEventLinkData",
    },
)


class AnnotationType(proto.Enum):
    r"""Type of the annotation.

    Values:
        ANNOTATION_TYPE_UNSPECIFIED (0):
            Default value for the enum. Don't use.
        USER_MENTION (1):
            A user is mentioned.
        SLASH_COMMAND (2):
            A slash command is invoked.
        RICH_LINK (3):
            A rich link annotation.
        CUSTOM_EMOJI (4):
            A custom emoji annotation.
    """

    ANNOTATION_TYPE_UNSPECIFIED = 0
    USER_MENTION = 1
    SLASH_COMMAND = 2
    RICH_LINK = 3
    CUSTOM_EMOJI = 4


class Annotation(proto.Message):
    r"""Annotations can be associated with the plain-text body of the
    message or with chips that link to Google Workspace resources like
    Google Docs or Sheets with ``start_index`` and ``length`` of 0. To
    add basic formatting to a text message, see `Format text
    messages <https://developers.google.com/workspace/chat/format-messages>`__.

    Example plain-text message body:

    ::

       Hello @FooBot how are you!"

    The corresponding annotations metadata:

    ::

       "annotations":[{
         "type":"USER_MENTION",
         "startIndex":6,
         "length":7,
         "userMention": {
           "user": {
             "name":"users/{user}",
             "displayName":"FooBot",
             "avatarUrl":"https://goo.gl/aeDtrS",
             "type":"BOT"
           },
           "type":"MENTION"
          }
       }]

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        type_ (google.apps.chat_v1.types.AnnotationType):
            The type of this annotation.
        start_index (int):
            Start index (0-based, inclusive) in the
            plain-text message body this annotation
            corresponds to.

            This field is a member of `oneof`_ ``_start_index``.
        length (int):
            Length of the substring in the plain-text
            message body this annotation corresponds to. If
            not present, indicates a length of 0.
        user_mention (google.apps.chat_v1.types.UserMentionMetadata):
            The metadata of user mention.

            This field is a member of `oneof`_ ``metadata``.
        slash_command (google.apps.chat_v1.types.SlashCommandMetadata):
            The metadata for a slash command.

            This field is a member of `oneof`_ ``metadata``.
        rich_link_metadata (google.apps.chat_v1.types.RichLinkMetadata):
            The metadata for a rich link.

            This field is a member of `oneof`_ ``metadata``.
        custom_emoji_metadata (google.apps.chat_v1.types.CustomEmojiMetadata):
            The metadata for a custom emoji.

            This field is a member of `oneof`_ ``metadata``.
    """

    type_: "AnnotationType" = proto.Field(
        proto.ENUM,
        number=1,
        enum="AnnotationType",
    )
    start_index: int = proto.Field(
        proto.INT32,
        number=2,
        optional=True,
    )
    length: int = proto.Field(
        proto.INT32,
        number=3,
    )
    user_mention: "UserMentionMetadata" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="metadata",
        message="UserMentionMetadata",
    )
    slash_command: "SlashCommandMetadata" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="metadata",
        message="SlashCommandMetadata",
    )
    rich_link_metadata: "RichLinkMetadata" = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="metadata",
        message="RichLinkMetadata",
    )
    custom_emoji_metadata: "CustomEmojiMetadata" = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="metadata",
        message="CustomEmojiMetadata",
    )


class UserMentionMetadata(proto.Message):
    r"""Annotation metadata for user mentions (@).

    Attributes:
        user (google.apps.chat_v1.types.User):
            The user mentioned.
        type_ (google.apps.chat_v1.types.UserMentionMetadata.Type):
            The type of user mention.
    """

    class Type(proto.Enum):
        r"""

        Values:
            TYPE_UNSPECIFIED (0):
                Default value for the enum. Don't use.
            ADD (1):
                Add user to space.
            MENTION (2):
                Mention user in space.
        """

        TYPE_UNSPECIFIED = 0
        ADD = 1
        MENTION = 2

    user: gc_user.User = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gc_user.User,
    )
    type_: Type = proto.Field(
        proto.ENUM,
        number=2,
        enum=Type,
    )


class SlashCommandMetadata(proto.Message):
    r"""Annotation metadata for slash commands (/).

    Attributes:
        bot (google.apps.chat_v1.types.User):
            The Chat app whose command was invoked.
        type_ (google.apps.chat_v1.types.SlashCommandMetadata.Type):
            The type of slash command.
        command_name (str):
            The name of the invoked slash command.
        command_id (int):
            The command ID of the invoked slash command.
        triggers_dialog (bool):
            Indicates whether the slash command is for a
            dialog.
    """

    class Type(proto.Enum):
        r"""

        Values:
            TYPE_UNSPECIFIED (0):
                Default value for the enum. Don't use.
            ADD (1):
                Add Chat app to space.
            INVOKE (2):
                Invoke slash command in space.
        """

        TYPE_UNSPECIFIED = 0
        ADD = 1
        INVOKE = 2

    bot: gc_user.User = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gc_user.User,
    )
    type_: Type = proto.Field(
        proto.ENUM,
        number=2,
        enum=Type,
    )
    command_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    command_id: int = proto.Field(
        proto.INT64,
        number=4,
    )
    triggers_dialog: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class RichLinkMetadata(proto.Message):
    r"""A rich link to a resource. Rich links can be associated with the
    plain-text body of the message or represent chips that link to
    Google Workspace resources like Google Docs or Sheets with
    ``start_index`` and ``length`` of 0.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        uri (str):
            The URI of this link.
        rich_link_type (google.apps.chat_v1.types.RichLinkMetadata.RichLinkType):
            The rich link type.
        drive_link_data (google.apps.chat_v1.types.DriveLinkData):
            Data for a drive link.

            This field is a member of `oneof`_ ``data``.
        chat_space_link_data (google.apps.chat_v1.types.ChatSpaceLinkData):
            Data for a chat space link.

            This field is a member of `oneof`_ ``data``.
        meet_space_link_data (google.apps.chat_v1.types.MeetSpaceLinkData):
            Data for a Meet space link.

            This field is a member of `oneof`_ ``data``.
        calendar_event_link_data (google.apps.chat_v1.types.CalendarEventLinkData):
            Data for a Calendar event link.

            This field is a member of `oneof`_ ``data``.
    """

    class RichLinkType(proto.Enum):
        r"""The rich link type. More types might be added in the future.

        Values:
            RICH_LINK_TYPE_UNSPECIFIED (0):
                Default value for the enum. Don't use.
            DRIVE_FILE (1):
                A Google Drive rich link type.
            CHAT_SPACE (2):
                A Chat space rich link type. For example, a
                space smart chip.
            GMAIL_MESSAGE (3):
                A Gmail message rich link type. Specifically, a Gmail chip
                from `Share to
                Chat <https://support.google.com/chat?p=chat_gmail>`__. The
                API only supports reading messages with GMAIL_MESSAGE rich
                links.
            MEET_SPACE (4):
                A Meet message rich link type. For example, a
                Meet chip.
            CALENDAR_EVENT (5):
                A Calendar message rich link type. For
                example, a Calendar chip.
        """

        RICH_LINK_TYPE_UNSPECIFIED = 0
        DRIVE_FILE = 1
        CHAT_SPACE = 2
        GMAIL_MESSAGE = 3
        MEET_SPACE = 4
        CALENDAR_EVENT = 5

    uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    rich_link_type: RichLinkType = proto.Field(
        proto.ENUM,
        number=2,
        enum=RichLinkType,
    )
    drive_link_data: "DriveLinkData" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="data",
        message="DriveLinkData",
    )
    chat_space_link_data: "ChatSpaceLinkData" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="data",
        message="ChatSpaceLinkData",
    )
    meet_space_link_data: "MeetSpaceLinkData" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="data",
        message="MeetSpaceLinkData",
    )
    calendar_event_link_data: "CalendarEventLinkData" = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="data",
        message="CalendarEventLinkData",
    )


class CustomEmojiMetadata(proto.Message):
    r"""Annotation metadata for custom emoji.

    Attributes:
        custom_emoji (google.apps.chat_v1.types.CustomEmoji):
            The custom emoji.
    """

    custom_emoji: reaction.CustomEmoji = proto.Field(
        proto.MESSAGE,
        number=1,
        message=reaction.CustomEmoji,
    )


class DriveLinkData(proto.Message):
    r"""Data for Google Drive links.

    Attributes:
        drive_data_ref (google.apps.chat_v1.types.DriveDataRef):
            A
            `DriveDataRef <https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces.messages.attachments#drivedataref>`__
            which references a Google Drive file.
        mime_type (str):
            The mime type of the linked Google Drive
            resource.
    """

    drive_data_ref: attachment.DriveDataRef = proto.Field(
        proto.MESSAGE,
        number=1,
        message=attachment.DriveDataRef,
    )
    mime_type: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ChatSpaceLinkData(proto.Message):
    r"""Data for Chat space links.

    Attributes:
        space (str):
            The space of the linked Chat space resource.

            Format: ``spaces/{space}``
        thread (str):
            The thread of the linked Chat space resource.

            Format: ``spaces/{space}/threads/{thread}``
        message (str):
            The message of the linked Chat space resource.

            Format: ``spaces/{space}/messages/{message}``
    """

    space: str = proto.Field(
        proto.STRING,
        number=1,
    )
    thread: str = proto.Field(
        proto.STRING,
        number=2,
    )
    message: str = proto.Field(
        proto.STRING,
        number=3,
    )


class MeetSpaceLinkData(proto.Message):
    r"""Data for Meet space links.

    Attributes:
        meeting_code (str):
            Meeting code of the linked Meet space.
        type_ (google.apps.chat_v1.types.MeetSpaceLinkData.Type):
            Indicates the type of the Meet space.
        huddle_status (google.apps.chat_v1.types.MeetSpaceLinkData.HuddleStatus):
            Optional. Output only. If the Meet is a
            Huddle, indicates the status of the huddle.
            Otherwise, this is unset.
    """

    class Type(proto.Enum):
        r"""The type of the Meet space.

        Values:
            TYPE_UNSPECIFIED (0):
                Default value for the enum. Don't use.
            MEETING (1):
                The Meet space is a meeting.
            HUDDLE (2):
                The Meet space is a huddle.
        """

        TYPE_UNSPECIFIED = 0
        MEETING = 1
        HUDDLE = 2

    class HuddleStatus(proto.Enum):
        r"""The status of the huddle

        Values:
            HUDDLE_STATUS_UNSPECIFIED (0):
                Default value for the enum. Don't use.
            STARTED (1):
                The huddle has started.
            ENDED (2):
                The huddle has ended. In this case the Meet
                space URI and identifiers will no longer be
                valid.
            MISSED (3):
                The huddle has been missed. In this case the
                Meet space URI and identifiers will no longer be
                valid.
        """

        HUDDLE_STATUS_UNSPECIFIED = 0
        STARTED = 1
        ENDED = 2
        MISSED = 3

    meeting_code: str = proto.Field(
        proto.STRING,
        number=1,
    )
    type_: Type = proto.Field(
        proto.ENUM,
        number=2,
        enum=Type,
    )
    huddle_status: HuddleStatus = proto.Field(
        proto.ENUM,
        number=3,
        enum=HuddleStatus,
    )


class CalendarEventLinkData(proto.Message):
    r"""Data for Calendar event links.

    Attributes:
        calendar_id (str):
            The `Calendar
            identifier <https://developers.google.com/workspace/calendar/api/v3/reference/calendars>`__
            of the linked Calendar.
        event_id (str):
            The `Event
            identifier <https://developers.google.com/workspace/calendar/api/v3/reference/events>`__
            of the linked Calendar event.
    """

    calendar_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    event_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
