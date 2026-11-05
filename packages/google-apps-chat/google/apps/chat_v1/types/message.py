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
from google.apps.card_v1.types import card as gac_card

from google.apps.chat_v1.types import action_status as gc_action_status
from google.apps.chat_v1.types import (
    annotation,
    contextual_addon,
    reaction,
    space_notification_setting,
    user,
)
from google.apps.chat_v1.types import attachment as gc_attachment
from google.apps.chat_v1.types import deletion_metadata as gc_deletion_metadata
from google.apps.chat_v1.types import markup_syntax as gc_markup_syntax
from google.apps.chat_v1.types import matched_url as gc_matched_url
from google.apps.chat_v1.types import slash_command as gc_slash_command
from google.apps.chat_v1.types import space as gc_space

__protobuf__ = proto.module(
    package="google.chat.v1",
    manifest={
        "Message",
        "AttachedGif",
        "QuotedMessageMetadata",
        "QuotedMessageSnapshot",
        "ForwardedMetadata",
        "Thread",
        "ActionResponse",
        "AccessoryWidget",
        "GetMessageRequest",
        "DeleteMessageRequest",
        "UpdateMessageRequest",
        "CreateMessageRequest",
        "CreateMessageNotificationOptions",
        "ListMessagesRequest",
        "ListMessagesResponse",
        "DialogAction",
        "Dialog",
        "CardWithId",
        "ReplaceMessageCardsRequest",
        "ReplaceMessageCardsResponse",
        "SearchMessagesRequest",
        "SearchMessagesResponse",
        "SearchMessageResult",
    },
)


class Message(proto.Message):
    r"""A message in a Google Chat space.

    Attributes:
        name (str):
            Identifier. Resource name of the message.

            Format: ``spaces/{space}/messages/{message}``

            Where ``{space}`` is the ID of the space where the message
            is posted and ``{message}`` is a system-assigned ID for the
            message. For example,
            ``spaces/AAAAAAAAAAA/messages/BBBBBBBBBBB.BBBBBBBBBBB``.

            If you set a custom ID when you create a message, you can
            use this ID to specify the message in a request by replacing
            ``{message}`` with the value from the
            ``clientAssignedMessageId`` field. For example,
            ``spaces/AAAAAAAAAAA/messages/client-custom-name``. For
            details, see `Name a
            message <https://developers.google.com/workspace/chat/create-messages#name_a_created_message>`__.
        sender (google.apps.chat_v1.types.User):
            Output only. The user who created the message. If your Chat
            app `authenticates as a
            user <https://developers.google.com/workspace/chat/authenticate-authorize-chat-user>`__,
            the output only populates the
            `user <https://developers.google.com/workspace/chat/api/reference/rest/v1/User>`__
            ``name`` and ``type`` fields for both internal and external
            users, unless they are members of the space or have a prior
            affinity, like a direct message (DM) conversation, with the
            calling user.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. Immutable. For spaces created in
            Chat, the time at which the message was created.
            This field is output only, except when used in
            import mode spaces.

            For import mode spaces, set this field to the
            historical timestamp at which the message was
            created in the source in order to preserve the
            original creation time.
        last_update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which the message
            was last edited by a user. If the message has
            never been edited, this field is empty.
        delete_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which the message
            was deleted in Google Chat. If the message is
            never deleted, this field is empty.
        text (str):
            Optional. Plain-text body of the message. The first link to
            an image, video, or web page generates a `preview
            chip <https://developers.google.com/workspace/chat/preview-links>`__.
            You can also `@mention a Google Chat
            user <https://developers.google.com/workspace/chat/format-messages#messages-@mention>`__,
            or everyone in the space.

            To learn about creating text messages, see `Send a
            message <https://developers.google.com/workspace/chat/create-messages>`__.
        formatted_text (str):
            Output only. Contains the message ``text`` with markups
            added to communicate formatting. This field might not
            capture all formatting visible in the UI, but includes the
            following:

            - `Markup
              syntax <https://developers.google.com/workspace/chat/format-messages>`__
              for bold, italic, strikethrough, monospace, monospace
              block, bulleted list, and block quote.

            - `User
              mentions <https://developers.google.com/workspace/chat/format-messages#messages-@mention>`__
              using the format ``<users/{user}>``.

            - Custom hyperlinks using the format
              ``<{url}|{rendered_text}>`` where the first string is the
              URL and the second is the rendered text—for example,
              ``<http://example.com|custom text>``.

            - Custom emoji using the format ``:{emoji_name}:``—for
              example, ``:smile:``. This doesn't apply to Unicode emoji,
              such as ``U+1F600`` for a grinning face emoji.

            - Bullet list items using asterisks (``*``)—for example,
              ``* item``.

            For more information, see `View text formatting sent in a
            message <https://developers.google.com/workspace/chat/format-messages#view_text_formatting_sent_in_a_message>`__
        cards (MutableSequence[google.apps.chat_v1.types.ContextualAddOnMarkup.Card]):
            Deprecated: Use ``cards_v2`` instead.

            Rich, formatted, and interactive cards that you can use to
            display UI elements such as: formatted texts, buttons, and
            clickable images. Cards are normally displayed below the
            plain-text body of the message. ``cards`` and ``cards_v2``
            can have a maximum size of 32 KB.
        cards_v2 (MutableSequence[google.apps.chat_v1.types.CardWithId]):
            Optional. An array of
            `cards <https://developers.google.com/workspace/chat/api/reference/rest/v1/cards>`__.

            Chat apps can create cards with `app
            authentication <https://developers.google.com/workspace/chat/authenticate-authorize-chat-app>`__.
            As part of the `Developer Preview
            Program <https://developers.google.com/workspace/preview>`__,
            if your Chat app `authenticates as a
            user <https://developers.google.com/workspace/chat/authenticate-authorize-chat-user>`__,
            it can create card messages. If your Chat app is not part of
            Developer Preview Program, it can't create cards with user
            authentication.

            To learn how to create a message that contains cards, see
            `Send a
            message <https://developers.google.com/workspace/chat/create-messages>`__.

            `Card
            builder <https://addons.gsuite.google.com/uikit/builder>`__
        annotations (MutableSequence[google.apps.chat_v1.types.Annotation]):
            Output only. Annotations can be associated with the
            plain-text body of the message or with chips that link to
            Google Workspace resources like Google Docs or Sheets with
            ``start_index`` and ``length`` of 0.
        thread (google.apps.chat_v1.types.Thread):
            The thread the message belongs to. For example usage, see
            `Start or reply to a message
            thread <https://developers.google.com/workspace/chat/create-messages#create-message-thread>`__.
        space (google.apps.chat_v1.types.Space):
            Output only. If your Chat app `authenticates as a
            user <https://developers.google.com/workspace/chat/authenticate-authorize-chat-user>`__,
            the output only populates the
            `space <https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces>`__
            ``name``.
        fallback_text (str):
            Optional. A plain-text description of the
            message's cards, used when the actual cards
            can't be displayed—for example, mobile
            notifications.
        action_response (google.apps.chat_v1.types.ActionResponse):
            Input only. Parameters that a Chat app can
            use to configure how its response is posted.
        argument_text (str):
            Output only. Plain-text body of the message
            with all Chat app mentions stripped out.
        slash_command (google.apps.chat_v1.types.SlashCommand):
            Output only. Slash command information, if
            applicable.
        attachment (MutableSequence[google.apps.chat_v1.types.Attachment]):
            Optional. User-uploaded attachment.
        matched_url (google.apps.chat_v1.types.MatchedUrl):
            Output only. A URL in the Chat message ``text`` field that
            matches a link preview pattern. For more information, see
            `Preview
            links <https://developers.google.com/workspace/chat/preview-links>`__.
        thread_reply (bool):
            Output only. When ``true``, the message is a response in a
            reply thread. When ``false``, the message is visible in the
            space's top-level conversation as either the first message
            of a thread or a message with no threaded replies.

            If the space doesn't support reply in threads, this field is
            always ``false``.
        silent (bool):
            Output only. Whether this is a silent
            message. Silent messages are messages where Chat
            suppresses push notifications for recipients.
        client_assigned_message_id (str):
            Optional. A custom ID for the message. You can use field to
            identify a message, or to get, delete, or update a message.
            To set a custom ID, specify the
            ```messageId`` <https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces.messages/create#body.QUERY_PARAMETERS.message_id>`__
            field when you create the message. For details, see `Name a
            message <https://developers.google.com/workspace/chat/create-messages#name_a_created_message>`__.
        emoji_reaction_summaries (MutableSequence[google.apps.chat_v1.types.EmojiReactionSummary]):
            Output only. The list of emoji reaction
            summaries on the message.
        private_message_viewer (google.apps.chat_v1.types.User):
            Optional. Immutable. Input for creating a message, otherwise
            output only. The user that can view the message. When set,
            the message is private and only visible to the specified
            user and the Chat app. To include this field in your
            request, you must call the Chat API using `app
            authentication <https://developers.google.com/workspace/chat/authenticate-authorize-chat-app>`__
            and omit the following:

            - `Attachments <https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces.messages.attachments>`__

            For details, see `Send a message
            privately <https://developers.google.com/workspace/chat/create-messages#private>`__.
        deletion_metadata (google.apps.chat_v1.types.DeletionMetadata):
            Output only. Information about a deleted message. A message
            is deleted when ``delete_time`` is set.
        quoted_message_metadata (google.apps.chat_v1.types.QuotedMessageMetadata):
            Optional. Information about a message that another message
            quotes.

            When you create a message, you can quote messages within the
            same thread, or quote a root message to create a new root
            message. However, you can't quote a message reply from a
            different thread.

            When you update a message, you can't add or replace the
            ``quotedMessageMetadata`` field, but you can remove it.

            For example usage, see `Quote another
            message <https://developers.google.com/workspace/chat/create-messages#quote-a-message>`__.
        attached_gifs (MutableSequence[google.apps.chat_v1.types.AttachedGif]):
            Output only. GIF images that are attached to
            the message.
        accessory_widgets (MutableSequence[google.apps.chat_v1.types.AccessoryWidget]):
            Optional. One or more interactive widgets that appear at the
            bottom of a message. You can add accessory widgets to
            messages that contain text, cards, or both text and cards.
            Not supported for messages that contain dialogs. For
            details, see `Add interactive widgets at the bottom of a
            message <https://developers.google.com/workspace/chat/create-messages#add-accessory-widgets>`__.

            Creating a message with accessory widgets requires [app
            authentication]
            (https://developers.google.com/workspace/chat/authenticate-authorize-chat-app).
        markup_syntax (google.apps.chat_v1.types.MarkupSyntax):
            Optional. Specifies how the server interprets the message
            ``text`` field content.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    sender: user.User = proto.Field(
        proto.MESSAGE,
        number=2,
        message=user.User,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    last_update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=23,
        message=timestamp_pb2.Timestamp,
    )
    delete_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=26,
        message=timestamp_pb2.Timestamp,
    )
    text: str = proto.Field(
        proto.STRING,
        number=4,
    )
    formatted_text: str = proto.Field(
        proto.STRING,
        number=43,
    )
    cards: MutableSequence[contextual_addon.ContextualAddOnMarkup.Card] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=5,
            message=contextual_addon.ContextualAddOnMarkup.Card,
        )
    )
    cards_v2: MutableSequence["CardWithId"] = proto.RepeatedField(
        proto.MESSAGE,
        number=22,
        message="CardWithId",
    )
    annotations: MutableSequence[annotation.Annotation] = proto.RepeatedField(
        proto.MESSAGE,
        number=10,
        message=annotation.Annotation,
    )
    thread: "Thread" = proto.Field(
        proto.MESSAGE,
        number=11,
        message="Thread",
    )
    space: gc_space.Space = proto.Field(
        proto.MESSAGE,
        number=12,
        message=gc_space.Space,
    )
    fallback_text: str = proto.Field(
        proto.STRING,
        number=13,
    )
    action_response: "ActionResponse" = proto.Field(
        proto.MESSAGE,
        number=14,
        message="ActionResponse",
    )
    argument_text: str = proto.Field(
        proto.STRING,
        number=15,
    )
    slash_command: gc_slash_command.SlashCommand = proto.Field(
        proto.MESSAGE,
        number=17,
        message=gc_slash_command.SlashCommand,
    )
    attachment: MutableSequence[gc_attachment.Attachment] = proto.RepeatedField(
        proto.MESSAGE,
        number=18,
        message=gc_attachment.Attachment,
    )
    matched_url: gc_matched_url.MatchedUrl = proto.Field(
        proto.MESSAGE,
        number=20,
        message=gc_matched_url.MatchedUrl,
    )
    thread_reply: bool = proto.Field(
        proto.BOOL,
        number=25,
    )
    silent: bool = proto.Field(
        proto.BOOL,
        number=46,
    )
    client_assigned_message_id: str = proto.Field(
        proto.STRING,
        number=32,
    )
    emoji_reaction_summaries: MutableSequence[reaction.EmojiReactionSummary] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=33,
            message=reaction.EmojiReactionSummary,
        )
    )
    private_message_viewer: user.User = proto.Field(
        proto.MESSAGE,
        number=36,
        message=user.User,
    )
    deletion_metadata: gc_deletion_metadata.DeletionMetadata = proto.Field(
        proto.MESSAGE,
        number=38,
        message=gc_deletion_metadata.DeletionMetadata,
    )
    quoted_message_metadata: "QuotedMessageMetadata" = proto.Field(
        proto.MESSAGE,
        number=39,
        message="QuotedMessageMetadata",
    )
    attached_gifs: MutableSequence["AttachedGif"] = proto.RepeatedField(
        proto.MESSAGE,
        number=42,
        message="AttachedGif",
    )
    accessory_widgets: MutableSequence["AccessoryWidget"] = proto.RepeatedField(
        proto.MESSAGE,
        number=44,
        message="AccessoryWidget",
    )
    markup_syntax: gc_markup_syntax.MarkupSyntax = proto.Field(
        proto.ENUM,
        number=47,
        enum=gc_markup_syntax.MarkupSyntax,
    )


class AttachedGif(proto.Message):
    r"""A GIF image that's specified by a URL.

    Attributes:
        uri (str):
            Output only. The URL that hosts the GIF
            image.
    """

    uri: str = proto.Field(
        proto.STRING,
        number=1,
    )


class QuotedMessageMetadata(proto.Message):
    r"""Information about a message that another message quotes.

    When you update a message, you can't add or replace the
    ``quotedMessageMetadata`` field, but you can remove it.

    For example usage, see `Quote another
    message <https://developers.google.com/workspace/chat/create-messages#quote-a-message>`__.

    Attributes:
        name (str):
            Required. Resource name of the message that is quoted.

            Format: ``spaces/{space}/messages/{message}``
        last_update_time (google.protobuf.timestamp_pb2.Timestamp):
            Required. The timestamp when the quoted message was created
            or when the quoted message was last updated.

            If the message was edited, use this field,
            ``last_update_time``. If the message was never edited, use
            ``create_time``.

            If ``last_update_time`` doesn't match the latest version of
            the quoted message, the request fails.
        quote_type (google.apps.chat_v1.types.QuotedMessageMetadata.QuoteType):
            Optional. Specifies the quote type. If not
            set, defaults to REPLY in the message read/write
            path for backward compatibility.
        quoted_message_snapshot (google.apps.chat_v1.types.QuotedMessageSnapshot):
            Output only. A snapshot of the quoted
            message's content.
        forwarded_metadata (google.apps.chat_v1.types.ForwardedMetadata):
            Output only. Metadata about the source space
            of the quoted message. Populated only for
            FORWARD quote type.
    """

    class QuoteType(proto.Enum):
        r"""The quote type of the quoted message.

        Values:
            QUOTE_TYPE_UNSPECIFIED (0):
                Reserved. This value is unused.
            REPLY (1):
                When ``quote_type`` is ``REPLY``, you can do the following:

                - If you're replying in a thread, you can quote another
                  message in that thread.

                - If you're creating a root message, you can quote another
                  root message in that space.
            FORWARD (2):
                When ``quote_type`` is ``FORWARD``, you can quote a:

                - Message from a different space.

                - Message reply from a different thread in the same space.
        """

        QUOTE_TYPE_UNSPECIFIED = 0
        REPLY = 1
        FORWARD = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    last_update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    quote_type: QuoteType = proto.Field(
        proto.ENUM,
        number=4,
        enum=QuoteType,
    )
    quoted_message_snapshot: "QuotedMessageSnapshot" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="QuotedMessageSnapshot",
    )
    forwarded_metadata: "ForwardedMetadata" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="ForwardedMetadata",
    )


class QuotedMessageSnapshot(proto.Message):
    r"""Provides a snapshot of the content of the quoted message at
    the time of quoting or forwarding

    Attributes:
        sender (str):
            Output only. The quoted message's author
            name. Populated for both REPLY & FORWARD quote
            types.
        text (str):
            Output only. Snapshot of the quoted message's
            text content.
        formatted_text (str):
            Output only. Contains the quoted message ``text`` with
            markups added to support rich formatting like
            hyperlinks,custom emojis, markup, etc. Populated only for
            FORWARD quote type.
        annotations (MutableSequence[google.apps.chat_v1.types.Annotation]):
            Output only. Annotations parsed from the text
            body of the quoted message. Populated only for
            FORWARD quote type.
        attachments (MutableSequence[google.apps.chat_v1.types.Attachment]):
            Output only. Attachments that were part of
            the quoted message. These are copies of the
            quoted message's attachment metadata. Populated
            only for FORWARD quote type.
    """

    sender: str = proto.Field(
        proto.STRING,
        number=1,
    )
    text: str = proto.Field(
        proto.STRING,
        number=2,
    )
    formatted_text: str = proto.Field(
        proto.STRING,
        number=3,
    )
    annotations: MutableSequence[annotation.Annotation] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=annotation.Annotation,
    )
    attachments: MutableSequence[gc_attachment.Attachment] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message=gc_attachment.Attachment,
    )


class ForwardedMetadata(proto.Message):
    r"""Metadata about the source space from which a message was
    forwarded.

    Attributes:
        space (str):
            Output only. The resource name of the source
            space. Format: spaces/{space}
        space_display_name (str):
            Output only. The display name of the source space or DM at
            the time of forwarding. For ``SPACE``, this is the space
            name. For ``DIRECT_MESSAGE``, this is the other
            participant's name (e.g., "User A"). For ``GROUP_CHAT``,
            this is a generated name based on members' first names,
            limited to 5 including the creator (e.g., "User A, User B").
    """

    space: str = proto.Field(
        proto.STRING,
        number=1,
    )
    space_display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )


class Thread(proto.Message):
    r"""A thread in a Google Chat space. For example usage, see `Start or
    reply to a message
    thread <https://developers.google.com/workspace/chat/create-messages#create-message-thread>`__.

    If you specify a thread when creating a message, you can set the
    ```messageReplyOption`` <https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces.messages/create#messagereplyoption>`__
    field to determine what happens if no matching thread is found.

    Attributes:
        name (str):
            Identifier. Resource name of the thread.

            Example: ``spaces/{space}/threads/{thread}``
        thread_key (str):
            Optional. Input for creating or updating a thread.
            Otherwise, output only. ID for the thread. Supports up to
            4000 characters.

            This ID is unique to the Chat app that sets it. For example,
            if multiple Chat apps create a message using the same thread
            key, the messages are posted in different threads. To reply
            in a thread created by a person or another Chat app, specify
            the thread ``name`` field instead.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    thread_key: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ActionResponse(proto.Message):
    r"""Parameters that a Chat app can use to configure how its
    response is posted.

    Attributes:
        type_ (google.apps.chat_v1.types.ActionResponse.ResponseType):
            Input only. The type of Chat app response.
        url (str):
            Input only. URL for users to authenticate or configure.
            (Only for ``REQUEST_CONFIG`` response types.)
        dialog_action (google.apps.chat_v1.types.DialogAction):
            Input only. A response to an interaction event related to a
            `dialog <https://developers.google.com/workspace/chat/dialogs>`__.
            Must be accompanied by ``ResponseType.Dialog``.
        updated_widget (google.apps.chat_v1.types.ActionResponse.UpdatedWidget):
            Input only. The response of the updated
            widget.
    """

    class ResponseType(proto.Enum):
        r"""The type of Chat app response.

        Values:
            TYPE_UNSPECIFIED (0):
                Default type that's handled as ``NEW_MESSAGE``.
            NEW_MESSAGE (1):
                Post as a new message in the topic.
            UPDATE_MESSAGE (2):
                Update the Chat app's message. This is only permitted on a
                ``CARD_CLICKED`` event where the message sender type is
                ``BOT``.
            UPDATE_USER_MESSAGE_CARDS (6):
                Update the cards on a user's message. This is only permitted
                as a response to a ``MESSAGE`` event with a matched url, or
                a ``CARD_CLICKED`` event where the message sender type is
                ``HUMAN``. Text is ignored.
            REQUEST_CONFIG (3):
                Privately ask the user for additional
                authentication or configuration.
            DIALOG (4):
                Presents a
                `dialog <https://developers.google.com/workspace/chat/dialogs>`__.
            UPDATE_WIDGET (7):
                Widget text autocomplete options query.
        """

        TYPE_UNSPECIFIED = 0
        NEW_MESSAGE = 1
        UPDATE_MESSAGE = 2
        UPDATE_USER_MESSAGE_CARDS = 6
        REQUEST_CONFIG = 3
        DIALOG = 4
        UPDATE_WIDGET = 7

    class SelectionItems(proto.Message):
        r"""List of widget autocomplete results.

        Attributes:
            items (MutableSequence[google.apps.card_v1.types.SelectionInput.SelectionItem]):
                An array of the SelectionItem objects.
        """

        items: MutableSequence[gac_card.SelectionInput.SelectionItem] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=1,
                message=gac_card.SelectionInput.SelectionItem,
            )
        )

    class UpdatedWidget(proto.Message):
        r"""For ``selectionInput`` widgets, returns autocomplete suggestions for
        a multiselect menu.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            suggestions (google.apps.chat_v1.types.ActionResponse.SelectionItems):
                List of widget autocomplete results

                This field is a member of `oneof`_ ``updated_widget``.
            widget (str):
                The ID of the updated widget. The ID must
                match the one for the widget that triggered the
                update request.
        """

        suggestions: "ActionResponse.SelectionItems" = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="updated_widget",
            message="ActionResponse.SelectionItems",
        )
        widget: str = proto.Field(
            proto.STRING,
            number=2,
        )

    type_: ResponseType = proto.Field(
        proto.ENUM,
        number=1,
        enum=ResponseType,
    )
    url: str = proto.Field(
        proto.STRING,
        number=2,
    )
    dialog_action: "DialogAction" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="DialogAction",
    )
    updated_widget: UpdatedWidget = proto.Field(
        proto.MESSAGE,
        number=4,
        message=UpdatedWidget,
    )


class AccessoryWidget(proto.Message):
    r"""One or more interactive widgets that appear at the bottom of a
    message. For details, see `Add interactive widgets at the bottom of
    a
    message <https://developers.google.com/workspace/chat/create-messages#add-accessory-widgets>`__.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        button_list (google.apps.card_v1.types.ButtonList):
            A list of buttons.

            This field is a member of `oneof`_ ``action``.
    """

    button_list: gac_card.ButtonList = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="action",
        message=gac_card.ButtonList,
    )


class GetMessageRequest(proto.Message):
    r"""Request to get a message.

    Attributes:
        name (str):
            Required. Resource name of the message.

            Format: ``spaces/{space}/messages/{message}``

            If you've set a custom ID for your message, you can use the
            value from the ``clientAssignedMessageId`` field for
            ``{message}``. For details, see [Name a message]
            (https://developers.google.com/workspace/chat/create-messages#name_a_created_message).
        markup_syntax (google.apps.chat_v1.types.MarkupSyntax):
            Optional. Specifies the desired output syntax for the Chat
            message ``formatted_text`` field.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    markup_syntax: gc_markup_syntax.MarkupSyntax = proto.Field(
        proto.ENUM,
        number=3,
        enum=gc_markup_syntax.MarkupSyntax,
    )


class DeleteMessageRequest(proto.Message):
    r"""Request to delete a message.

    Attributes:
        name (str):
            Required. Resource name of the message.

            Format: ``spaces/{space}/messages/{message}``

            If you've set a custom ID for your message, you can use the
            value from the ``clientAssignedMessageId`` field for
            ``{message}``. For details, see [Name a message]
            (https://developers.google.com/workspace/chat/create-messages#name_a_created_message).
        force (bool):
            Optional. When ``true``, deleting a message also deletes its
            threaded replies. When ``false``, if a message has threaded
            replies, deletion fails.

            Only applies when `authenticating as a
            user <https://developers.google.com/workspace/chat/authenticate-authorize-chat-user>`__.
            Has no effect when [authenticating as a Chat app]
            (https://developers.google.com/workspace/chat/authenticate-authorize-chat-app).
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class UpdateMessageRequest(proto.Message):
    r"""Request to update a message.

    Attributes:
        message (google.apps.chat_v1.types.Message):
            Required. Message with fields updated.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The field paths to update. Separate multiple
            values with commas or use ``*`` to update all field paths.

            Currently supported field paths:

            - ``text``

            - ``attachment``

            - ``cards`` (Requires `app
              authentication </chat/api/guides/auth/service-accounts>`__.)

            - ``cards_v2`` (Requires `app
              authentication </chat/api/guides/auth/service-accounts>`__.)

            - ``accessory_widgets`` (Requires `app
              authentication </chat/api/guides/auth/service-accounts>`__.)

            - ``quoted_message_metadata`` (Only allows removal of the
              quoted message.)
        allow_missing (bool):
            Optional. If ``true`` and the message isn't found, a new
            message is created and ``updateMask`` is ignored. The
            specified message ID must be
            `client-assigned <https://developers.google.com/workspace/chat/create-messages#name_a_created_message>`__
            or the request fails.
    """

    message: "Message" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Message",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )
    allow_missing: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class CreateMessageRequest(proto.Message):
    r"""Creates a message.

    Attributes:
        parent (str):
            Required. The resource name of the space in which to create
            a message.

            Format: ``spaces/{space}``
        message (google.apps.chat_v1.types.Message):
            Required. Message body.
        thread_key (str):
            Optional. Deprecated: Use
            [thread.thread_key][google.chat.v1.Thread.thread_key]
            instead. ID for the thread. Supports up to 4000 characters.
            To start or add to a thread, create a message and specify a
            ``threadKey`` or the
            [thread.name][google.chat.v1.Thread.name]. For example
            usage, see `Start or reply to a message
            thread <https://developers.google.com/workspace/chat/create-messages#create-message-thread>`__.
        request_id (str):
            Optional. A unique ID for this request. A random UUID is
            recommended. Specifying a request ID makes the request
            idempotent, which ensures that multiple identical requests
            with the same request ID result in only a single message
            being created. Subsequent requests with the same request ID
            return the existing message and do not update the message,
            even if the requested details differ from the current state.

            To use this field effectively:

            - Ensure that subsequent requests are identical and use the
              same authentication credentials as the original request.
            - If a message was already created with the provided request
              ID, the request returns that message. Note that the
              returned message might not be fully populated; the API
              echoes the message in your request with the
              system-assigned resource names populated. To retrieve the
              latest metadata for the message, call ``GetMessage``.
            - Reusing an existing request ID with a different
              authenticated user results in an error.
        message_reply_option (google.apps.chat_v1.types.CreateMessageRequest.MessageReplyOption):
            Optional. Specifies whether a message starts a thread or
            replies to one. Only supported in named spaces.

            When `responding to user
            interactions <https://developers.google.com/workspace/chat/receive-respond-interactions>`__,
            this field is ignored. For interactions within a thread, the
            reply is created in the same thread. Otherwise, the reply is
            created as a new thread.
        message_id (str):
            Optional. A custom ID for a message. Lets Chat apps get,
            update, or delete a message without needing to store the
            system-assigned ID in the message's resource name
            (represented in the message ``name`` field).

            The value for this field must meet the following
            requirements:

            - Begins with ``client-``. For example,
              ``client-custom-name`` is a valid custom ID, but
              ``custom-name`` is not.
            - Contains up to 63 characters and only lowercase letters,
              numbers, and hyphens.
            - Is unique within a space. A Chat app can't use the same
              custom ID for different messages.

            For details, see `Name a
            message <https://developers.google.com/workspace/chat/create-messages#name_a_created_message>`__.
        create_message_notification_options (google.apps.chat_v1.types.CreateMessageNotificationOptions):
            Optional. Controls the notification behavior when the
            message is posted. To learn more, see `Force notifications
            or send silent
            messages <https://developer.google.com/workspace/chat/create-messages#force-notify-silent>`__.
    """

    class MessageReplyOption(proto.Enum):
        r"""Specifies how to reply to a message.
        More states might be added in the future.

        Values:
            MESSAGE_REPLY_OPTION_UNSPECIFIED (0):
                Default. Starts a new thread. Using this option ignores any
                [thread ID][google.chat.v1.Thread.name] or
                [``thread_key``][google.chat.v1.Thread.thread_key] that's
                included.
            REPLY_MESSAGE_FALLBACK_TO_NEW_THREAD (1):
                Creates the message as a reply to the thread specified by
                [thread ID][google.chat.v1.Thread.name] or
                [``thread_key``][google.chat.v1.Thread.thread_key]. If it
                fails, the message starts a new thread instead.
            REPLY_MESSAGE_OR_FAIL (2):
                Creates the message as a reply to the thread specified by
                [thread ID][google.chat.v1.Thread.name] or
                [``thread_key``][google.chat.v1.Thread.thread_key]. If a new
                ``thread_key`` is used, a new thread is created. If the
                message creation fails, a ``NOT_FOUND`` error is returned
                instead.
        """

        MESSAGE_REPLY_OPTION_UNSPECIFIED = 0
        REPLY_MESSAGE_FALLBACK_TO_NEW_THREAD = 1
        REPLY_MESSAGE_OR_FAIL = 2

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    message: "Message" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="Message",
    )
    thread_key: str = proto.Field(
        proto.STRING,
        number=6,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=7,
    )
    message_reply_option: MessageReplyOption = proto.Field(
        proto.ENUM,
        number=8,
        enum=MessageReplyOption,
    )
    message_id: str = proto.Field(
        proto.STRING,
        number=9,
    )
    create_message_notification_options: "CreateMessageNotificationOptions" = (
        proto.Field(
            proto.MESSAGE,
            number=10,
            message="CreateMessageNotificationOptions",
        )
    )


class CreateMessageNotificationOptions(proto.Message):
    r"""Options for the notification behavior when the message is
    posted.

    Attributes:
        notification_type (google.apps.chat_v1.types.CreateMessageNotificationOptions.NotificationType):
            The notification type for the message.
    """

    class NotificationType(proto.Enum):
        r"""The notification types options for the message.

        Values:
            NOTIFICATION_TYPE_NONE (0):
                Default behavior. Notification behavior is
                similar to when the human user sends the message
                using the Chat UI: no notification is sent to
                the human sender.
            NOTIFICATION_TYPE_FORCE_NOTIFY (2):
                Force notify recipients. This bypasses users' space
                notification settings and `Chat Do Not Disturb
                settings <https://support.google.com/chat/answer/9093489>`__.
                This option does not bypass device-level Do Not Disturb
                settings.

                Requires [app authentication]
                (https://developers.google.com/workspace/chat/authenticate-authorize-chat-app).
            NOTIFICATION_TYPE_SILENT (3):
                Do not notify recipients, and do not mark the message as
                unread. This behaves similarly to the user muting the
                conversation or enabling `Chat Do Not
                Disturb <https://support.google.com/chat/answer/9093489>`__.

                Requires [app authentication]
                (https://developers.google.com/workspace/chat/authenticate-authorize-chat-app).
        """

        NOTIFICATION_TYPE_NONE = 0
        NOTIFICATION_TYPE_FORCE_NOTIFY = 2
        NOTIFICATION_TYPE_SILENT = 3

    notification_type: NotificationType = proto.Field(
        proto.ENUM,
        number=1,
        enum=NotificationType,
    )


class ListMessagesRequest(proto.Message):
    r"""Lists messages in the specified space, that the user is a
    member of.

    Attributes:
        parent (str):
            Required. The resource name of the space to list messages
            from.

            Format: ``spaces/{space}``
        page_size (int):
            Optional. The maximum number of messages returned. The
            service might return fewer messages than this value.

            If unspecified, at most 25 are returned.

            The maximum value is 1000. If you use a value more than
            1000, it's automatically changed to 1000.

            Negative values return an ``INVALID_ARGUMENT`` error.
        page_token (str):
            Optional. A page token received from a
            previous list messages call. Provide this
            parameter to retrieve the subsequent page.

            When paginating, all other parameters provided
            should match the call that provided the page
            token. Passing different values to the other
            parameters might lead to unexpected results.
        filter (str):
            Optional. A query filter.

            You can filter messages by date (``create_time``) and thread
            (``thread.name``).

            To filter messages by the date they were created, specify
            the ``create_time`` with a timestamp in
            `RFC-3339 <https://www.rfc-editor.org/rfc/rfc3339>`__ format
            and double quotation marks. For example,
            ``"2023-04-21T11:30:00-04:00"``. You can use the greater
            than operator ``>`` to list messages that were created after
            a timestamp, or the less than operator ``<`` to list
            messages that were created before a timestamp. To filter
            messages within a time interval, use the ``AND`` operator
            between two timestamps.

            To filter by thread, specify the ``thread.name``, formatted
            as ``spaces/{space}/threads/{thread}``. You can only specify
            one ``thread.name`` per query.

            To filter by both thread and date, use the ``AND`` operator
            in your query.

            For example, the following queries are valid:

            ::

               create_time > "2012-04-21T11:30:00-04:00"

               create_time > "2012-04-21T11:30:00-04:00" AND
                 thread.name = spaces/AAAAAAAAAAA/threads/123

               create_time > "2012-04-21T11:30:00+00:00" AND

               create_time < "2013-01-01T00:00:00+00:00" AND
                 thread.name = spaces/AAAAAAAAAAA/threads/123

               thread.name = spaces/AAAAAAAAAAA/threads/123

            Invalid queries are rejected by the server with an
            ``INVALID_ARGUMENT`` error.
        order_by (str):
            Optional. How the list of messages is ordered. Specify a
            value to order by an ordering operation. Valid ordering
            operation values are as follows:

            - ``ASC`` for ascending.

            - ``DESC`` for descending.

            The default ordering is ``create_time ASC``.
        show_deleted (bool):
            Optional. Whether to include deleted
            messages. Deleted messages include deleted time
            and metadata about their deletion, but message
            content is unavailable.
        markup_syntax (google.apps.chat_v1.types.MarkupSyntax):
            Optional. Specifies the desired output syntax for the Chat
            message ``formatted_text`` field.
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
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )
    show_deleted: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    markup_syntax: gc_markup_syntax.MarkupSyntax = proto.Field(
        proto.ENUM,
        number=9,
        enum=gc_markup_syntax.MarkupSyntax,
    )


class ListMessagesResponse(proto.Message):
    r"""Response message for listing messages.

    Attributes:
        messages (MutableSequence[google.apps.chat_v1.types.Message]):
            List of messages.
        next_page_token (str):
            You can send a token as ``pageToken`` to retrieve the next
            page of results. If empty, there are no subsequent pages.
    """

    @property
    def raw_page(self):
        return self

    messages: MutableSequence["Message"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Message",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DialogAction(proto.Message):
    r"""Contains a
    `dialog <https://developers.google.com/workspace/chat/dialogs>`__
    and request status code.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        dialog (google.apps.chat_v1.types.Dialog):
            Input only.
            `Dialog <https://developers.google.com/workspace/chat/dialogs>`__
            for the request.

            This field is a member of `oneof`_ ``action``.
        action_status (google.apps.chat_v1.types.ActionStatus):
            Input only. Status for a request to either invoke or submit
            a
            `dialog <https://developers.google.com/workspace/chat/dialogs>`__.
            Displays a status and message to users, if necessary. For
            example, in case of an error or success.
    """

    dialog: "Dialog" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="action",
        message="Dialog",
    )
    action_status: gc_action_status.ActionStatus = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gc_action_status.ActionStatus,
    )


class Dialog(proto.Message):
    r"""Wrapper around the card body of the dialog.

    Attributes:
        body (google.apps.card_v1.types.Card):
            Input only. Body of the dialog, which is rendered in a
            modal. Google Chat apps don't support the following card
            entities: ``DateTimePicker``, ``OnChangeAction``.
    """

    body: gac_card.Card = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gac_card.Card,
    )


class CardWithId(proto.Message):
    r"""A
    `card <https://developers.google.com/workspace/chat/api/reference/rest/v1/cards>`__
    in a Google Chat message.

    Chat apps can create cards with `app
    authentication <https://developers.google.com/workspace/chat/authenticate-authorize-chat-app>`__.
    As part of the `Developer Preview
    Program <https://developers.google.com/workspace/preview>`__, if
    your Chat app `authenticates as a
    user <https://developers.google.com/workspace/chat/authenticate-authorize-chat-user>`__,
    it can create card messages. If your Chat app is not part of
    Developer Preview Program, it can't create cards with user
    authentication.

    To learn how to create a message that contains cards, see `Send a
    message <https://developers.google.com/workspace/chat/create-messages>`__.

    `Card builder <https://addons.gsuite.google.com/uikit/builder>`__

    Attributes:
        card_id (str):
            Required if the message contains multiple
            cards. A unique identifier for a card in a
            message.
        card (google.apps.card_v1.types.Card):
            A card. Maximum size is 32 KB.
        owner_user (google.apps.chat_v1.types.User):
            Output only. The app that owns the card.
    """

    card_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    card: gac_card.Card = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gac_card.Card,
    )
    owner_user: user.User = proto.Field(
        proto.MESSAGE,
        number=3,
        message=user.User,
    )


class ReplaceMessageCardsRequest(proto.Message):
    r"""Request message for ReplaceMessageCards API method.

    Attributes:
        name (str):
            Required. The resource name of the message.

            Format: ``spaces/{space}/messages/{message}``
        cards_v2 (MutableSequence[google.apps.chat_v1.types.CardWithId]):
            Optional. An array of
            `cards <https://developers.google.com/workspace/chat/api/reference/rest/v1/cards>`__
            to be included in the message. These cards will replace the
            existing cards of the message. If empty, the original cards
            included in the message will be cleared.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    cards_v2: MutableSequence["CardWithId"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="CardWithId",
    )


class ReplaceMessageCardsResponse(proto.Message):
    r"""Response message for ReplaceMessageCards API."""


class SearchMessagesRequest(proto.Message):
    r"""Request message for searching messages.

    Attributes:
        parent (str):
            Required. The resource name of the space to search within.

            To search across all spaces the user has access to, set this
            field to ``spaces/-``. Using any other value for ``parent``
            results in an ``INVALID_ARGUMENT`` error.

            To limit the search to one or more spaces, use
            ``space.name`` or ``space.display_name`` in the ``filter``.
        filter (str):
            Required. A search query.

            The query can specify one or more search keywords, which are
            used to filter the results,

            You can also filter the results using the following message
            fields:

            - ``create_time``: Accepts a timestamp in
              `RFC-3339 <https://www.rfc-editor.org/rfc/rfc3339>`__
              format and the supported comparison operators are: ``<``
              and ``>=``.
            - ``sender.name``: The resource name of the sender
              (``users/{user}``). Only supports ``=``. You can use the
              e-mail as an alias for ``{user}``. For example,
              ``users/example@gmail.com``, where ``example@gmail.com``
              is the e-mail of the Google Chat user.
            - ``space.name``: The resource name of the space where the
              message is posted. (``spaces/{space}``). Only supports
              ``=``. If this filter is not set, the search is performed
              across all direct messages and spaces the user has access
              to as a space member.
            - ``space.display_name``: Supports the operator ``:`` (has)
              and filters spaces based on a partial match of their
              display name. Results are limited to the top five space
              matches. For example, ``space.display_name:Project``
              searches for messages in the top five spaces that contain
              the word "Project" in their display names.
            - ``space.space_type``: The type of the space. Only supports
              ``=``. For example, ``space.space_type="DIRECT_MESSAGE"``
              returns only messages from direct messages. The possible
              values are ``DIRECT_MESSAGE``, ``GROUP_CHAT``, and
              ``SPACE``.
            - ``attachment``: Supports the operator ``:*`` (has any) to
              check for the presence of attachments. If ``attachment:*``
              is specified, only messages that have at least one
              attachment are returned.
            - ``annotations.user_mentions.user.name``: The resource name
              of the mentioned user (``users/{user}``). Only supports
              ``:`` (has). For example:
              ``annotations.user_mentions.user.name:"users/1234567890"``
              returns only messages that contain a mention to the
              specified user. Alternatively, the alias ``me`` can be
              used to filter for messages that mention the caller user,
              for example:
              ``annotations.user_mentions.user.name:users/me``. You can
              also use the e-mail as an alias for ``{user}``, for
              example, ``users/example@gmail.com``.

            For advanced filtering, the following functions are also
            available:

            - ``has_link()``: Returns only messages that have at least
              one hyperlink in the message text.
            - ``is_unread()``: Filters out messages that have been read
              by the calling user.

            Using the ``space.display_name`` or the ``space.space_type``
            filters requires that the calling credentials include one of
            the following `authorization
            scopes <https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes>`__:

            - ``https://www.googleapis.com/auth/chat.spaces.readonly``
            - ``https://www.googleapis.com/auth/chat.spaces``

            Using the ``is_unread()`` filter requires that the calling
            credentials include one of the following `authorization
            scopes <https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes>`__:

            - ``https://www.googleapis.com/auth/chat.users.readstate.readonly``
            - ``https://www.googleapis.com/auth/chat.users.readstate``

            Across different fields, only ``AND`` operators are
            supported. A valid example is
            ``sender.name = "users/1234567890" AND is_unread()``. The
            word ``AND`` is optional and is implied if omitted. For
            example, ``sender.name = "users/1234567890" is_unread()`` is
            valid and is equivalent to the previous example. An invalid
            example is
            ``sender.name = "users/1234567890" OR is_unread()`` because
            ``OR`` is not supported between different fields.

            Among the same field:

            - ``create_time`` supports only ``AND``, and can only be
              used to represent an interval, such as
              ``create_time >= "2022-01-01T00:00:00+00:00" AND create_time < "2023-01-01T00:00:00+00:00"``.
            - ``sender.name`` supports only the ``OR`` operator, for
              example:
              ``sender.name = "users/1234567890" OR sender.name = "users/0987654321"``.
            - ``space.name`` supports only the ``OR`` operator, for
              example:
              ``space.name = "spaces/ABCDEFGH" OR space.name = "spaces/QWERTYUI"``.
            - ``space.display_name`` supports the operators ``AND`` and
              ``OR``, but not a mix of both. For example:
              ``space.display_name:Project AND space.display_name:Tasks``
              returns messages that are in spaces with display names
              containing both ``Project`` and ``Tasks``, whereas
              ``space.display_name:Project OR space.display_name:Tasks``
              returns messages that are in spaces with display names
              containing either ``Project`` or ``Tasks`` or both.
            - ``space.space_type`` supports only the ``OR`` operator,
              for example:
              ``space.space_type = "DIRECT_MESSAGE" OR space.space_type = "GROUP_CHAT"``.
            - ``annotations.user_mentions.user.name`` supports the
              operators ``AND`` and ``OR``, but not a mix of both. For
              example:
              ``annotations.user_mentions.user.name:"users/1234567890" AND annotations.user_mentions.user.name:"users/0987654321"``
              returns only messages that mentions both users, whereas
              ``annotations.user_mentions.user.name:"users/1234567890" OR annotations.user_mentions.user.name:"users/0987654321"``
              returns messages that mention either user or both.

            Parentheses are required to disambiguate operator precedence
            when combining ``AND`` and ``OR`` operators in the same
            query. For example:
            ``(sender.name="users/me" OR sender.name="users/123456") AND is_unread()``.
            Otherwise, parentheses are optional.

            The following example queries are valid:

            ::

               "Pending reports" AND create_time >= "2023-01-01T00:00:00Z"

               sender.name = "users/example@gmail.com"

               annotations.user_mentions.user.name:"users/0987654321"

               attachment:* AND space.name = "spaces/ABCDEFGH"

               tasks AND is_unread() AND sender.name = "users/1234567890"

               "things to do" "urgent"

               (sender.name = "users/1234567890")
               AND (create_time < "2023-05-01T00:00:00Z")

               tasks AND space.name = "spaces/ABCDEFGH" AND has_link()

               "project one" is_unread()

               space.display_name:Project tasks

            The maximum query length is 1,000 characters.

            Invalid queries are rejected by the server with an
            ``INVALID_ARGUMENT`` error.
        page_size (int):
            Optional. The maximum number of results to
            return. The service may return fewer than this
            value.

            If unspecified, at most 25 are returned.

            The maximum value is 100. If you use a value
            more than 100, it's automatically changed to
            100.
        page_token (str):
            Optional. A token, received from the previous
            search messages call. Provide this parameter to
            retrieve the subsequent page.

            When paginating, all other parameters provided
            should match the call that provided the page
            token. Passing different values to the other
            parameters might lead to unexpected results.
        order_by (str):
            Optional. How the results list is ordered.

            Supported attributes to order by are:

            - ``create_time``: Sorts the results by the time of the
              message creation. Default value.
            - ``relevance``: Sorts the results by relevance. `Developer
              Preview <https://developers.google.com/workspace/preview>`__.

            The default ordering is ``create_time desc``. Only a single
            order per query (``create_time`` or ``relevance``) is
            supported. Only descending order (``desc``) is supported,
            and it must be specified after the order attribute.
        markup_syntax (google.apps.chat_v1.types.MarkupSyntax):
            Optional. Specifies the desired output syntax for the Chat
            message ``formatted_text`` field.
        view (google.apps.chat_v1.types.SearchMessagesRequest.SearchMessagesView):
            Optional. Specifies what kind of search results view to
            return. The default is ``SEARCH_MESSAGES_VIEW_BASIC``.
    """

    class SearchMessagesView(proto.Enum):
        r"""The kinds of view that are supported for partial search
        results.

        Values:
            SEARCH_MESSAGES_VIEW_UNSPECIFIED (0):
                The default / unset value.
                The API will default to the BASIC view.
            SEARCH_MESSAGES_VIEW_BASIC (1):
                Includes only the matched messages in the
                results, but no additional metadata. This is the
                default value.
            SEARCH_MESSAGES_VIEW_FULL (2):
                Includes everything in the results: the
                matched messages and additional metadata.
        """

        SEARCH_MESSAGES_VIEW_UNSPECIFIED = 0
        SEARCH_MESSAGES_VIEW_BASIC = 1
        SEARCH_MESSAGES_VIEW_FULL = 2

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
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )
    markup_syntax: gc_markup_syntax.MarkupSyntax = proto.Field(
        proto.ENUM,
        number=6,
        enum=gc_markup_syntax.MarkupSyntax,
    )
    view: SearchMessagesView = proto.Field(
        proto.ENUM,
        number=7,
        enum=SearchMessagesView,
    )


class SearchMessagesResponse(proto.Message):
    r"""Response message for searching messages.

    Attributes:
        results (MutableSequence[google.apps.chat_v1.types.SearchMessageResult]):
            The list of search results that matched the
            query.
        next_page_token (str):
            A token that can be used to retrieve the next
            page. If this field is empty, there are no
            subsequent pages.
    """

    @property
    def raw_page(self):
        return self

    results: MutableSequence["SearchMessageResult"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="SearchMessageResult",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class SearchMessageResult(proto.Message):
    r"""A single result item from a message search.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        message (google.apps.chat_v1.types.Message):
            The matched message.
        read (bool):
            Indicates if the matched message is read by the calling
            user.

            Only returned if the request view is
            ``SEARCH_MESSAGES_VIEW_FULL`` and the calling credentials
            include one of the following `authorization
            scopes <https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes>`__:

            - ``https://www.googleapis.com/auth/chat.users.readstate.readonly``
            - ``https://www.googleapis.com/auth/chat.users.readstate``

            This field is a member of `oneof`_ ``_read``.
        space_mute_setting (google.apps.chat_v1.types.SpaceNotificationSetting.MuteSetting):
            The mute setting of the calling user for the space where the
            message is posted. The caller app can use this information
            to decide how to process the message depending on whether
            the space is muted for the user or not.

            Only returned if the request view is
            ``SEARCH_MESSAGES_VIEW_FULL`` and the calling credentials
            include the following `authorization
            scope <https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes>`__:

            - ``https://www.googleapis.com/auth/chat.users.spacesettings``
    """

    message: "Message" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Message",
    )
    read: bool = proto.Field(
        proto.BOOL,
        number=3,
        optional=True,
    )
    space_mute_setting: space_notification_setting.SpaceNotificationSetting.MuteSetting = proto.Field(
        proto.ENUM,
        number=4,
        enum=space_notification_setting.SpaceNotificationSetting.MuteSetting,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
