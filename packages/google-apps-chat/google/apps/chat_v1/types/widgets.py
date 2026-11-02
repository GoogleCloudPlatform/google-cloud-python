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

__protobuf__ = proto.module(
    package="google.chat.v1",
    manifest={
        "WidgetMarkup",
    },
)


class WidgetMarkup(proto.Message):
    r"""A widget is a UI element that presents text and images.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        text_paragraph (google.apps.chat_v1.types.WidgetMarkup.TextParagraph):
            Display a text paragraph in this widget.

            This field is a member of `oneof`_ ``data``.
        image (google.apps.chat_v1.types.WidgetMarkup.Image):
            Display an image in this widget.

            This field is a member of `oneof`_ ``data``.
        key_value (google.apps.chat_v1.types.WidgetMarkup.KeyValue):
            Display a key value item in this widget.

            This field is a member of `oneof`_ ``data``.
        buttons (MutableSequence[google.apps.chat_v1.types.WidgetMarkup.Button]):
            A list of buttons. Buttons is also ``oneof data`` and only
            one of these fields should be set.
    """

    class Icon(proto.Enum):
        r"""The set of supported icons.

        Values:
            ICON_UNSPECIFIED (0):
                No description available.
            AIRPLANE (1):
                No description available.
            BOOKMARK (26):
                No description available.
            BUS (25):
                No description available.
            CAR (9):
                No description available.
            CLOCK (2):
                No description available.
            CONFIRMATION_NUMBER_ICON (12):
                No description available.
            DOLLAR (14):
                No description available.
            DESCRIPTION (27):
                No description available.
            EMAIL (10):
                No description available.
            EVENT_PERFORMER (20):
                No description available.
            EVENT_SEAT (21):
                No description available.
            FLIGHT_ARRIVAL (16):
                No description available.
            FLIGHT_DEPARTURE (15):
                No description available.
            HOTEL (6):
                No description available.
            HOTEL_ROOM_TYPE (17):
                No description available.
            INVITE (19):
                No description available.
            MAP_PIN (3):
                No description available.
            MEMBERSHIP (24):
                No description available.
            MULTIPLE_PEOPLE (18):
                No description available.
            OFFER (30):
                No description available.
            PERSON (11):
                No description available.
            PHONE (13):
                No description available.
            RESTAURANT_ICON (7):
                No description available.
            SHOPPING_CART (8):
                No description available.
            STAR (5):
                No description available.
            STORE (22):
                No description available.
            TICKET (4):
                No description available.
            TRAIN (23):
                No description available.
            VIDEO_CAMERA (28):
                No description available.
            VIDEO_PLAY (29):
                No description available.
        """

        ICON_UNSPECIFIED = 0
        AIRPLANE = 1
        BOOKMARK = 26
        BUS = 25
        CAR = 9
        CLOCK = 2
        CONFIRMATION_NUMBER_ICON = 12
        DOLLAR = 14
        DESCRIPTION = 27
        EMAIL = 10
        EVENT_PERFORMER = 20
        EVENT_SEAT = 21
        FLIGHT_ARRIVAL = 16
        FLIGHT_DEPARTURE = 15
        HOTEL = 6
        HOTEL_ROOM_TYPE = 17
        INVITE = 19
        MAP_PIN = 3
        MEMBERSHIP = 24
        MULTIPLE_PEOPLE = 18
        OFFER = 30
        PERSON = 11
        PHONE = 13
        RESTAURANT_ICON = 7
        SHOPPING_CART = 8
        STAR = 5
        STORE = 22
        TICKET = 4
        TRAIN = 23
        VIDEO_CAMERA = 28
        VIDEO_PLAY = 29

    class TextParagraph(proto.Message):
        r"""A paragraph of text. Formatted text supported. For more information
        about formatting text, see `Formatting text in Google Chat
        apps <https://developers.google.com/workspace/chat/format-messages#card-formatting>`__
        and `Formatting text in Google Workspace
        Add-ons <https://developers.google.com/apps-script/add-ons/concepts/widgets#text_formatting>`__.

        Attributes:
            text (str):

        """

        text: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class Button(proto.Message):
        r"""A button. Can be a text button or an image button.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            text_button (google.apps.chat_v1.types.WidgetMarkup.TextButton):
                A button with text and ``onclick`` action.

                This field is a member of `oneof`_ ``type``.
            image_button (google.apps.chat_v1.types.WidgetMarkup.ImageButton):
                A button with image and ``onclick`` action.

                This field is a member of `oneof`_ ``type``.
        """

        text_button: "WidgetMarkup.TextButton" = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="type",
            message="WidgetMarkup.TextButton",
        )
        image_button: "WidgetMarkup.ImageButton" = proto.Field(
            proto.MESSAGE,
            number=2,
            oneof="type",
            message="WidgetMarkup.ImageButton",
        )

    class TextButton(proto.Message):
        r"""A button with text and ``onclick`` action.

        Attributes:
            text (str):
                The text of the button.
            on_click (google.apps.chat_v1.types.WidgetMarkup.OnClick):
                The ``onclick`` action of the button.
        """

        text: str = proto.Field(
            proto.STRING,
            number=1,
        )
        on_click: "WidgetMarkup.OnClick" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="WidgetMarkup.OnClick",
        )

    class KeyValue(proto.Message):
        r"""A UI element contains a key (label) and a value (content). This
        element can also contain some actions such as ``onclick`` button.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            icon (google.apps.chat_v1.types.WidgetMarkup.Icon):
                An enum value that's replaced by the Chat API
                with the corresponding icon image.

                This field is a member of `oneof`_ ``icons``.
            icon_url (str):
                The icon specified by a URL.

                This field is a member of `oneof`_ ``icons``.
            top_label (str):
                The text of the top label. Formatted text supported. For
                more information about formatting text, see `Formatting text
                in Google Chat
                apps <https://developers.google.com/workspace/chat/format-messages#card-formatting>`__
                and `Formatting text in Google Workspace
                Add-ons <https://developers.google.com/apps-script/add-ons/concepts/widgets#text_formatting>`__.
            content (str):
                The text of the content. Formatted text supported and always
                required. For more information about formatting text, see
                `Formatting text in Google Chat
                apps <https://developers.google.com/workspace/chat/format-messages#card-formatting>`__
                and `Formatting text in Google Workspace
                Add-ons <https://developers.google.com/apps-script/add-ons/concepts/widgets#text_formatting>`__.
            content_multiline (bool):
                If the content should be multiline.
            bottom_label (str):
                The text of the bottom label. Formatted text supported. For
                more information about formatting text, see `Formatting text
                in Google Chat
                apps <https://developers.google.com/workspace/chat/format-messages#card-formatting>`__
                and `Formatting text in Google Workspace
                Add-ons <https://developers.google.com/apps-script/add-ons/concepts/widgets#text_formatting>`__.
            on_click (google.apps.chat_v1.types.WidgetMarkup.OnClick):
                The ``onclick`` action. Only the top label, bottom label,
                and content region are clickable.
            button (google.apps.chat_v1.types.WidgetMarkup.Button):
                A button that can be clicked to trigger an
                action.

                This field is a member of `oneof`_ ``control``.
        """

        icon: "WidgetMarkup.Icon" = proto.Field(
            proto.ENUM,
            number=1,
            oneof="icons",
            enum="WidgetMarkup.Icon",
        )
        icon_url: str = proto.Field(
            proto.STRING,
            number=2,
            oneof="icons",
        )
        top_label: str = proto.Field(
            proto.STRING,
            number=3,
        )
        content: str = proto.Field(
            proto.STRING,
            number=4,
        )
        content_multiline: bool = proto.Field(
            proto.BOOL,
            number=9,
        )
        bottom_label: str = proto.Field(
            proto.STRING,
            number=5,
        )
        on_click: "WidgetMarkup.OnClick" = proto.Field(
            proto.MESSAGE,
            number=6,
            message="WidgetMarkup.OnClick",
        )
        button: "WidgetMarkup.Button" = proto.Field(
            proto.MESSAGE,
            number=7,
            oneof="control",
            message="WidgetMarkup.Button",
        )

    class Image(proto.Message):
        r"""An image that's specified by a URL and can have an ``onclick``
        action.

        Attributes:
            image_url (str):
                The URL of the image.
            on_click (google.apps.chat_v1.types.WidgetMarkup.OnClick):
                The ``onclick`` action.
            aspect_ratio (float):
                The aspect ratio of this image (width and
                height). This field lets you reserve the right
                height for the image while waiting for it to
                load. It's not meant to override the built-in
                aspect ratio of the image. If unset, the server
                fills it by prefetching the image.
        """

        image_url: str = proto.Field(
            proto.STRING,
            number=1,
        )
        on_click: "WidgetMarkup.OnClick" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="WidgetMarkup.OnClick",
        )
        aspect_ratio: float = proto.Field(
            proto.DOUBLE,
            number=3,
        )

    class ImageButton(proto.Message):
        r"""An image button with an ``onclick`` action.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            icon (google.apps.chat_v1.types.WidgetMarkup.Icon):
                The icon specified by an ``enum`` that indices to an icon
                provided by Chat API.

                This field is a member of `oneof`_ ``icons``.
            icon_url (str):
                The icon specified by a URL.

                This field is a member of `oneof`_ ``icons``.
            on_click (google.apps.chat_v1.types.WidgetMarkup.OnClick):
                The ``onclick`` action.
            name (str):
                The name of this ``image_button`` that's used for
                accessibility. Default value is provided if this name isn't
                specified.
        """

        icon: "WidgetMarkup.Icon" = proto.Field(
            proto.ENUM,
            number=1,
            oneof="icons",
            enum="WidgetMarkup.Icon",
        )
        icon_url: str = proto.Field(
            proto.STRING,
            number=3,
            oneof="icons",
        )
        on_click: "WidgetMarkup.OnClick" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="WidgetMarkup.OnClick",
        )
        name: str = proto.Field(
            proto.STRING,
            number=4,
        )

    class OnClick(proto.Message):
        r"""An ``onclick`` action (for example, open a link).

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            action (google.apps.chat_v1.types.WidgetMarkup.FormAction):
                A form action is triggered by this ``onclick`` action if
                specified.

                This field is a member of `oneof`_ ``data``.
            open_link (google.apps.chat_v1.types.WidgetMarkup.OpenLink):
                This ``onclick`` action triggers an open link action if
                specified.

                This field is a member of `oneof`_ ``data``.
        """

        action: "WidgetMarkup.FormAction" = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="data",
            message="WidgetMarkup.FormAction",
        )
        open_link: "WidgetMarkup.OpenLink" = proto.Field(
            proto.MESSAGE,
            number=2,
            oneof="data",
            message="WidgetMarkup.OpenLink",
        )

    class OpenLink(proto.Message):
        r"""A link that opens a new window.

        Attributes:
            url (str):
                The URL to open.
        """

        url: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class FormAction(proto.Message):
        r"""A form action describes the behavior when the form is
        submitted. For example, you can invoke Apps Script to handle the
        form.

        Attributes:
            action_method_name (str):
                The method name is used to identify which
                part of the form triggered the form submission.
                This information is echoed back to the Chat app
                as part of the card click event. You can use the
                same method name for several elements that
                trigger a common behavior.
            parameters (MutableSequence[google.apps.chat_v1.types.WidgetMarkup.FormAction.ActionParameter]):
                List of action parameters.
        """

        class ActionParameter(proto.Message):
            r"""List of string parameters to supply when the action method is
            invoked. For example, consider three snooze buttons: snooze now,
            snooze one day, snooze next week. You might use
            ``action method = snooze()``, passing the snooze type and snooze
            time in the list of string parameters.

            Attributes:
                key (str):
                    The name of the parameter for the action
                    script.
                value (str):
                    The value of the parameter.
            """

            key: str = proto.Field(
                proto.STRING,
                number=1,
            )
            value: str = proto.Field(
                proto.STRING,
                number=2,
            )

        action_method_name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        parameters: MutableSequence["WidgetMarkup.FormAction.ActionParameter"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=2,
                message="WidgetMarkup.FormAction.ActionParameter",
            )
        )

    text_paragraph: TextParagraph = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="data",
        message=TextParagraph,
    )
    image: Image = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="data",
        message=Image,
    )
    key_value: KeyValue = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="data",
        message=KeyValue,
    )
    buttons: MutableSequence[Button] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message=Button,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
