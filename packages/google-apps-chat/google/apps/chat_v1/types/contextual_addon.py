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

from google.apps.chat_v1.types import widgets as gc_widgets

__protobuf__ = proto.module(
    package="google.chat.v1",
    manifest={
        "ContextualAddOnMarkup",
    },
)


class ContextualAddOnMarkup(proto.Message):
    r"""The markup for developers to specify the contents of a
    contextual AddOn.

    """

    class Card(proto.Message):
        r"""A card is a UI element that can contain UI widgets such as
        text and images.

        Attributes:
            header (google.apps.chat_v1.types.ContextualAddOnMarkup.Card.CardHeader):
                The header of the card. A header usually
                contains a title and an image.
            sections (MutableSequence[google.apps.chat_v1.types.ContextualAddOnMarkup.Card.Section]):
                Sections are separated by a line divider.
            card_actions (MutableSequence[google.apps.chat_v1.types.ContextualAddOnMarkup.Card.CardAction]):
                The actions of this card.
            name (str):
                Name of the card.
        """

        class CardHeader(proto.Message):
            r"""

            Attributes:
                title (str):
                    The title must be specified. The header has a
                    fixed height: if both a title and subtitle is
                    specified, each takes up one line. If only the
                    title is specified, it takes up both lines.
                subtitle (str):
                    The subtitle of the card header.
                image_style (google.apps.chat_v1.types.ContextualAddOnMarkup.Card.CardHeader.ImageStyle):
                    The image's type (for example, square border
                    or circular border).
                image_url (str):
                    The URL of the image in the card header.
            """

            class ImageStyle(proto.Enum):
                r"""

                Values:
                    IMAGE_STYLE_UNSPECIFIED (0):
                        No description available.
                    IMAGE (1):
                        Square border.
                    AVATAR (2):
                        Circular border.
                """

                IMAGE_STYLE_UNSPECIFIED = 0
                IMAGE = 1
                AVATAR = 2

            title: str = proto.Field(
                proto.STRING,
                number=1,
            )
            subtitle: str = proto.Field(
                proto.STRING,
                number=2,
            )
            image_style: "ContextualAddOnMarkup.Card.CardHeader.ImageStyle" = (
                proto.Field(
                    proto.ENUM,
                    number=3,
                    enum="ContextualAddOnMarkup.Card.CardHeader.ImageStyle",
                )
            )
            image_url: str = proto.Field(
                proto.STRING,
                number=4,
            )

        class Section(proto.Message):
            r"""A section contains a collection of widgets that are rendered
            (vertically) in the order that they are specified. Across all
            platforms, cards have a narrow fixed width, so
            there's currently no need for layout properties (for example,
            float).

            Attributes:
                header (str):
                    The header of the section. Formatted text is supported. For
                    more information about formatting text, see `Formatting text
                    in Google Chat
                    apps <https://developers.google.com/workspace/chat/format-messages#card-formatting>`__
                    and `Formatting text in Google Workspace
                    Add-ons <https://developers.google.com/apps-script/add-ons/concepts/widgets#text_formatting>`__.
                widgets (MutableSequence[google.apps.chat_v1.types.WidgetMarkup]):
                    A section must contain at least one widget.
            """

            header: str = proto.Field(
                proto.STRING,
                number=1,
            )
            widgets: MutableSequence[gc_widgets.WidgetMarkup] = proto.RepeatedField(
                proto.MESSAGE,
                number=2,
                message=gc_widgets.WidgetMarkup,
            )

        class CardAction(proto.Message):
            r"""A card action is
            the action associated with the card. For an invoice card, a
            typical action would be: delete invoice, email invoice or open
            the invoice in browser.

            Not supported by Google Chat apps.

            Attributes:
                action_label (str):
                    The label used to be displayed in the action
                    menu item.
                on_click (google.apps.chat_v1.types.WidgetMarkup.OnClick):
                    The onclick action for this action item.
            """

            action_label: str = proto.Field(
                proto.STRING,
                number=1,
            )
            on_click: gc_widgets.WidgetMarkup.OnClick = proto.Field(
                proto.MESSAGE,
                number=2,
                message=gc_widgets.WidgetMarkup.OnClick,
            )

        header: "ContextualAddOnMarkup.Card.CardHeader" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="ContextualAddOnMarkup.Card.CardHeader",
        )
        sections: MutableSequence["ContextualAddOnMarkup.Card.Section"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=2,
                message="ContextualAddOnMarkup.Card.Section",
            )
        )
        card_actions: MutableSequence["ContextualAddOnMarkup.Card.CardAction"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=3,
                message="ContextualAddOnMarkup.Card.CardAction",
            )
        )
        name: str = proto.Field(
            proto.STRING,
            number=4,
        )


__all__ = tuple(sorted(__protobuf__.manifest))
