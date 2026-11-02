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

import google.type.color_pb2 as color_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.apps.card.v1",
    manifest={
        "Card",
        "Widget",
        "TextParagraph",
        "Image",
        "Divider",
        "DecoratedText",
        "TextInput",
        "Suggestions",
        "ButtonList",
        "SelectionInput",
        "DateTimePicker",
        "OverflowMenu",
        "Button",
        "Icon",
        "MaterialIcon",
        "ImageCropStyle",
        "BorderStyle",
        "ImageComponent",
        "Grid",
        "Columns",
        "Carousel",
        "CollapseControl",
        "OnClick",
        "OpenLink",
        "Action",
        "Validation",
        "ChipList",
        "Chip",
    },
)


class Card(proto.Message):
    r"""A card interface displayed in a Google Chat message or Google
    Workspace add-on.

    Cards support a defined layout, interactive UI elements like
    buttons, and rich media like images. Use cards to present detailed
    information, gather information from users, and guide users to take
    a next step.

    `Card builder <https://addons.gsuite.google.com/uikit/builder>`__

    To learn how to build cards, see the following documentation:

    - For Google Chat apps, see `Design the components of a card or
      dialog <https://developers.google.com/workspace/chat/design-components-card-dialog>`__.
    - For Google Workspace add-ons, see `Card-based
      interfaces <https://developers.google.com/apps-script/add-ons/concepts/cards>`__.

    Note: You can add up to 100 widgets per card. Any widgets beyond
    this limit are ignored. This limit applies to both card messages and
    dialogs in Google Chat apps, and to cards in Google Workspace
    add-ons.

    **Example: Card message for a Google Chat app**

    |Example contact card|

    To create the sample card message in Google Chat, use the following
    JSON:

    ::

       {
         "cardsV2": [
           {
             "cardId": "unique-card-id",
             "card": {
               "header": {
                  "title": "Sasha",
                  "subtitle": "Software Engineer",
                  "imageUrl":
                  "https://developers.google.com/workspace/chat/images/quickstart-app-avatar.png",
                  "imageType": "CIRCLE",
                  "imageAltText": "Avatar for Sasha"
                },
                "sections": [
                  {
                    "header": "Contact Info",
                    "collapsible": true,
                    "uncollapsibleWidgetsCount": 1,
                    "widgets": [
                      {
                        "decoratedText": {
                          "startIcon": {
                            "knownIcon": "EMAIL"
                          },
                          "text": "sasha@example.com"
                        }
                      },
                      {
                        "decoratedText": {
                          "startIcon": {
                            "knownIcon": "PERSON"
                          },
                          "text": "<font color=\"#80e27e\">Online</font>"
                        }
                      },
                      {
                        "decoratedText": {
                          "startIcon": {
                            "knownIcon": "PHONE"
                          },
                          "text": "+1 (555) 555-1234"
                        }
                      },
                      {
                        "buttonList": {
                          "buttons": [
                            {
                              "text": "Share",
                              "onClick": {
                               "openLink": {
                                  "url": "https://example.com/share"
                                }
                              }
                            },
                            {
                              "text": "Edit",
                              "onClick": {
                                "action": {
                                  "function": "goToView",
                                  "parameters": [
                                    {
                                      "key": "viewType",
                                      "value": "EDIT"
                                    }
                                  ]
                                }
                              }
                            }
                          ]
                        }
                      }
                    ]
                  }
                ]
              }
           }
         ]
       }

    .. |Example contact card| image:: https://developers.google.com/workspace/chat/images/card_api_reference.png

    Attributes:
        header (google.apps.card_v1.types.Card.CardHeader):
            The header of the card. A header usually
            contains a leading image and a title. Headers
            always appear at the top of a card.
        sections (MutableSequence[google.apps.card_v1.types.Card.Section]):
            Contains a collection of widgets. Each section has its own,
            optional header. Sections are visually separated by a line
            divider. For an example in Google Chat apps, see `Define a
            section of a
            card <https://developers.google.com/workspace/chat/design-components-card-dialog#define_a_section_of_a_card>`__.
        section_divider_style (google.apps.card_v1.types.Card.DividerStyle):
            The divider style between the header,
            sections and footer.
        card_actions (MutableSequence[google.apps.card_v1.types.Card.CardAction]):
            The card's actions. Actions are added to the card's toolbar
            menu.

            `Google Workspace
            add-ons <https://developers.google.com/workspace/add-ons>`__:

            For example, the following JSON constructs a card action
            menu with ``Settings`` and ``Send Feedback`` options:

            ::

               "card_actions": [
                 {
                   "actionLabel": "Settings",
                   "onClick": {
                     "action": {
                       "functionName": "goToView",
                       "parameters": [
                         {
                           "key": "viewType",
                           "value": "SETTING"
                        }
                       ],
                       "loadIndicator": "LoadIndicator.SPINNER"
                     }
                   }
                 },
                 {
                   "actionLabel": "Send Feedback",
                   "onClick": {
                     "openLink": {
                       "url": "https://example.com/feedback"
                     }
                   }
                 }
               ]
        name (str):
            Name of the card. Used as a card identifier in card
            navigation.

            `Google Workspace
            add-ons <https://developers.google.com/workspace/add-ons>`__:
        fixed_footer (google.apps.card_v1.types.Card.CardFixedFooter):
            The fixed footer shown at the bottom of this card.

            Setting ``fixedFooter`` without specifying a
            ``primaryButton`` or a ``secondaryButton`` causes an error.
            For Chat apps, you can use fixed footers in
            `dialogs <https://developers.google.com/workspace/chat/dialogs>`__,
            but not `card
            messages <https://developers.google.com/workspace/chat/create-messages#create>`__.

            `Google Workspace add-ons and Chat
            apps <https://developers.google.com/workspace/extend>`__:
        display_style (google.apps.card_v1.types.Card.DisplayStyle):
            In Google Workspace add-ons, sets the display properties of
            the ``peekCardHeader``.

            `Google Workspace
            add-ons <https://developers.google.com/workspace/add-ons>`__:
        peek_card_header (google.apps.card_v1.types.Card.CardHeader):
            When displaying contextual content, the peek card header
            acts as a placeholder so that the user can navigate forward
            between the homepage cards and the contextual cards.

            `Google Workspace
            add-ons <https://developers.google.com/workspace/add-ons>`__:
    """

    class DividerStyle(proto.Enum):
        r"""The divider style of a card. Currently only used for dividers
        betweens card sections.

        `Google Workspace add-ons and Chat
        apps <https://developers.google.com/workspace/extend>`__:

        Values:
            DIVIDER_STYLE_UNSPECIFIED (0):
                Don't use. Unspecified.
            SOLID_DIVIDER (1):
                Default option. Render a solid divider.
            NO_DIVIDER (2):
                If set, no divider is rendered. This style
                completely removes the divider from the layout.
                The result is equivalent to not adding a divider
                at all.
        """

        DIVIDER_STYLE_UNSPECIFIED = 0
        SOLID_DIVIDER = 1
        NO_DIVIDER = 2

    class DisplayStyle(proto.Enum):
        r"""In Google Workspace add-ons, determines how a card is displayed.

        `Google Workspace
        add-ons <https://developers.google.com/workspace/add-ons>`__:

        Values:
            DISPLAY_STYLE_UNSPECIFIED (0):
                Don't use. Unspecified.
            PEEK (1):
                The header of the card appears at the bottom
                of the sidebar, partially covering the current
                top card of the stack. Clicking the header pops
                the card into the card stack. If the card has no
                header, a generated header is used instead.
            REPLACE (2):
                Default value. The card is shown by replacing
                the view of the top card in the card stack.
        """

        DISPLAY_STYLE_UNSPECIFIED = 0
        PEEK = 1
        REPLACE = 2

    class CardHeader(proto.Message):
        r"""Represents a card header. For an example in Google Chat apps, see
        `Add a
        header <https://developers.google.com/workspace/chat/design-components-card-dialog#add_a_header>`__.

        `Google Workspace add-ons and Chat
        apps <https://developers.google.com/workspace/extend>`__:

        Attributes:
            title (str):
                Required. The title of the card header.
                The header has a fixed height: if both a
                title and subtitle are specified, each takes up
                one line. If only the title is specified, it
                takes up both lines.
            subtitle (str):
                The subtitle of the card header. If specified, appears on
                its own line below the ``title``.
            image_type (google.apps.card_v1.types.Widget.ImageType):
                The shape used to crop the image.

                `Google Workspace add-ons and Chat
                apps <https://developers.google.com/workspace/extend>`__:
            image_url (str):
                The HTTPS URL of the image in the card
                header.
            image_alt_text (str):
                The alternative text of this image that's
                used for accessibility.
        """

        title: str = proto.Field(
            proto.STRING,
            number=1,
        )
        subtitle: str = proto.Field(
            proto.STRING,
            number=2,
        )
        image_type: "Widget.ImageType" = proto.Field(
            proto.ENUM,
            number=3,
            enum="Widget.ImageType",
        )
        image_url: str = proto.Field(
            proto.STRING,
            number=4,
        )
        image_alt_text: str = proto.Field(
            proto.STRING,
            number=5,
        )

    class Section(proto.Message):
        r"""A section contains a collection of widgets that are rendered
        vertically in the order that they're specified.

        `Google Workspace add-ons and Chat
        apps <https://developers.google.com/workspace/extend>`__:

        Attributes:
            header (str):
                Text that appears at the top of a section. Supports simple
                HTML formatted text. For more information about formatting
                text, see `Formatting text in Google Chat
                apps <https://developers.google.com/workspace/chat/format-messages#card-formatting>`__
                and `Formatting text in Google Workspace
                add-ons <https://developers.google.com/apps-script/add-ons/concepts/widgets#text_formatting>`__.
            widgets (MutableSequence[google.apps.card_v1.types.Widget]):
                All the widgets in the section.
                Must contain at least one widget.
            collapsible (bool):
                Indicates whether this section is collapsible.

                Collapsible sections hide some or all widgets, but users can
                expand the section to reveal the hidden widgets by clicking
                **Show more**. Users can hide the widgets again by clicking
                **Show less**.

                To determine which widgets are hidden, specify
                ``uncollapsibleWidgetsCount``.
            uncollapsible_widgets_count (int):
                The number of uncollapsible widgets which remain visible
                even when a section is collapsed.

                For example, when a section contains five widgets and the
                ``uncollapsibleWidgetsCount`` is set to ``2``, the first two
                widgets are always shown and the last three are collapsed by
                default. The ``uncollapsibleWidgetsCount`` is taken into
                account only when ``collapsible`` is ``true``.
            collapse_control (google.apps.card_v1.types.CollapseControl):
                Optional. Define the expand and collapse
                button of the section. This button will be shown
                only if the section is collapsible. If this
                field isn't set, the default button is used.
        """

        header: str = proto.Field(
            proto.STRING,
            number=1,
        )
        widgets: MutableSequence["Widget"] = proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="Widget",
        )
        collapsible: bool = proto.Field(
            proto.BOOL,
            number=5,
        )
        uncollapsible_widgets_count: int = proto.Field(
            proto.INT32,
            number=6,
        )
        collapse_control: "CollapseControl" = proto.Field(
            proto.MESSAGE,
            number=8,
            message="CollapseControl",
        )

    class CardAction(proto.Message):
        r"""A card action is the action associated with the card. For example,
        an invoice card might include actions such as delete invoice, email
        invoice, or open the invoice in a browser.

        `Google Workspace
        add-ons <https://developers.google.com/workspace/add-ons>`__:

        Attributes:
            action_label (str):
                The label that displays as the action menu
                item.
            on_click (google.apps.card_v1.types.OnClick):
                The ``onClick`` action for this action item.
        """

        action_label: str = proto.Field(
            proto.STRING,
            number=1,
        )
        on_click: "OnClick" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="OnClick",
        )

    class NestedWidget(proto.Message):
        r"""A list of widgets that can be displayed in a containing layout, such
        as a ``CarouselCard``. `Google Chat
        apps <https://developers.google.com/workspace/chat>`__:

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            text_paragraph (google.apps.card_v1.types.TextParagraph):
                A text paragraph widget.

                This field is a member of `oneof`_ ``data``.
            button_list (google.apps.card_v1.types.ButtonList):
                A button list widget.

                This field is a member of `oneof`_ ``data``.
            image (google.apps.card_v1.types.Image):
                An image widget.

                This field is a member of `oneof`_ ``data``.
        """

        text_paragraph: "TextParagraph" = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="data",
            message="TextParagraph",
        )
        button_list: "ButtonList" = proto.Field(
            proto.MESSAGE,
            number=3,
            oneof="data",
            message="ButtonList",
        )
        image: "Image" = proto.Field(
            proto.MESSAGE,
            number=10,
            oneof="data",
            message="Image",
        )

    class CardFixedFooter(proto.Message):
        r"""A persistent (sticky) footer that that appears at the bottom of the
        card.

        Setting ``fixedFooter`` without specifying a ``primaryButton`` or a
        ``secondaryButton`` causes an error.

        For Chat apps, you can use fixed footers in
        `dialogs <https://developers.google.com/workspace/chat/dialogs>`__,
        but not `card
        messages <https://developers.google.com/workspace/chat/create-messages#create>`__.
        For an example in Google Chat apps, see `Add a persistent
        footer <https://developers.google.com/workspace/chat/design-components-card-dialog#add_a_persistent_footer>`__.

        `Google Workspace add-ons and Chat
        apps <https://developers.google.com/workspace/extend>`__:

        Attributes:
            primary_button (google.apps.card_v1.types.Button):
                The primary button of the fixed footer. The
                button must be a text button with text and color
                set.
            secondary_button (google.apps.card_v1.types.Button):
                The secondary button of the fixed footer. The button must be
                a text button with text and color set. If
                ``secondaryButton`` is set, you must also set
                ``primaryButton``.
        """

        primary_button: "Button" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="Button",
        )
        secondary_button: "Button" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="Button",
        )

    header: CardHeader = proto.Field(
        proto.MESSAGE,
        number=1,
        message=CardHeader,
    )
    sections: MutableSequence[Section] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=Section,
    )
    section_divider_style: DividerStyle = proto.Field(
        proto.ENUM,
        number=9,
        enum=DividerStyle,
    )
    card_actions: MutableSequence[CardAction] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=CardAction,
    )
    name: str = proto.Field(
        proto.STRING,
        number=4,
    )
    fixed_footer: CardFixedFooter = proto.Field(
        proto.MESSAGE,
        number=5,
        message=CardFixedFooter,
    )
    display_style: DisplayStyle = proto.Field(
        proto.ENUM,
        number=6,
        enum=DisplayStyle,
    )
    peek_card_header: CardHeader = proto.Field(
        proto.MESSAGE,
        number=7,
        message=CardHeader,
    )


class Widget(proto.Message):
    r"""Each card is made up of widgets.

    A widget is a composite object that can represent one of text,
    images, buttons, and other object types.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        text_paragraph (google.apps.card_v1.types.TextParagraph):
            Displays a text paragraph. Supports simple HTML formatted
            text. For more information about formatting text, see
            `Formatting text in Google Chat
            apps <https://developers.google.com/workspace/chat/format-messages#card-formatting>`__
            and `Formatting text in Google Workspace
            add-ons <https://developers.google.com/apps-script/add-ons/concepts/widgets#text_formatting>`__.

            For example, the following JSON creates a bolded text:

            ::

               "textParagraph": {
                 "text": "  <b>bold text</b>"
               }

            This field is a member of `oneof`_ ``data``.
        image (google.apps.card_v1.types.Image):
            Displays an image.

            For example, the following JSON creates an image with
            alternative text:

            ::

               "image": {
                 "imageUrl":
                 "https://developers.google.com/workspace/chat/images/quickstart-app-avatar.png",
                 "altText": "Chat app avatar"
               }

            This field is a member of `oneof`_ ``data``.
        decorated_text (google.apps.card_v1.types.DecoratedText):
            Displays a decorated text item.

            For example, the following JSON creates a decorated text
            widget showing email address:

            ::

               "decoratedText": {
                 "icon": {
                   "knownIcon": "EMAIL"
                 },
                 "topLabel": "Email Address",
                 "text": "sasha@example.com",
                 "bottomLabel": "This is a new Email address!",
                 "switchControl": {
                   "name": "has_send_welcome_email_to_sasha",
                   "selected": false,
                   "controlType": "CHECKBOX"
                 }
               }

            This field is a member of `oneof`_ ``data``.
        button_list (google.apps.card_v1.types.ButtonList):
            A list of buttons.

            For example, the following JSON creates two buttons. The
            first is a blue text button and the second is an image
            button that opens a link:

            ::

               "buttonList": {
                 "buttons": [
                   {
                     "text": "Edit",
                     "color": {
                       "red": 0,
                       "green": 0,
                       "blue": 1,
                     },
                     "disabled": true,
                   },
                   {
                     "icon": {
                       "knownIcon": "INVITE",
                       "altText": "check calendar"
                     },
                     "onClick": {
                       "openLink": {
                         "url": "https://example.com/calendar"
                       }
                     }
                   }
                 ]
               }

            This field is a member of `oneof`_ ``data``.
        text_input (google.apps.card_v1.types.TextInput):
            Displays a text box that users can type into.

            For example, the following JSON creates a text input for an
            email address:

            ::

               "textInput": {
                 "name": "mailing_address",
                 "label": "Mailing Address"
               }

            As another example, the following JSON creates a text input
            for a programming language with static suggestions:

            ::

               "textInput": {
                 "name": "preferred_programing_language",
                 "label": "Preferred Language",
                 "initialSuggestions": {
                   "items": [
                     {
                       "text": "C++"
                     },
                     {
                       "text": "Java"
                     },
                     {
                       "text": "JavaScript"
                     },
                     {
                       "text": "Python"
                     }
                   ]
                 }
               }

            This field is a member of `oneof`_ ``data``.
        selection_input (google.apps.card_v1.types.SelectionInput):
            Displays a selection control that lets users select items.
            Selection controls can be checkboxes, radio buttons,
            switches, or dropdown menus.

            For example, the following JSON creates a dropdown menu that
            lets users choose a size:

            ::

               "selectionInput": {
                 "name": "size",
                 "label": "Size"
                 "type": "DROPDOWN",
                 "items": [
                   {
                     "text": "S",
                     "value": "small",
                     "selected": false
                   },
                   {
                     "text": "M",
                     "value": "medium",
                     "selected": true
                   },
                   {
                     "text": "L",
                     "value": "large",
                     "selected": false
                   },
                   {
                     "text": "XL",
                     "value": "extra_large",
                     "selected": false
                   }
                 ]
               }

            This field is a member of `oneof`_ ``data``.
        date_time_picker (google.apps.card_v1.types.DateTimePicker):
            Displays a widget that lets users input a date, time, or
            date and time.

            For example, the following JSON creates a date time picker
            to schedule an appointment:

            ::

               "dateTimePicker": {
                 "name": "appointment_time",
                 "label": "Book your appointment at:",
                 "type": "DATE_AND_TIME",
                 "valueMsEpoch": 796435200000
               }

            This field is a member of `oneof`_ ``data``.
        divider (google.apps.card_v1.types.Divider):
            Displays a horizontal line divider between widgets.

            For example, the following JSON creates a divider:

            ::

               "divider": {
               }

            This field is a member of `oneof`_ ``data``.
        grid (google.apps.card_v1.types.Grid):
            Displays a grid with a collection of items.

            A grid supports any number of columns and items. The number
            of rows is determined by the upper bounds of the number
            items divided by the number of columns. A grid with 10 items
            and 2 columns has 5 rows. A grid with 11 items and 2 columns
            has 6 rows.

            `Google Workspace add-ons and Chat
            apps <https://developers.google.com/workspace/extend>`__:

            For example, the following JSON creates a 2 column grid with
            a single item:

            ::

               "grid": {
                 "title": "A fine collection of items",
                 "columnCount": 2,
                 "borderStyle": {
                   "type": "STROKE",
                   "cornerRadius": 4
                 },
                 "items": [
                   {
                     "image": {
                       "imageUri": "https://www.example.com/image.png",
                       "cropStyle": {
                         "type": "SQUARE"
                       },
                       "borderStyle": {
                         "type": "STROKE"
                       }
                     },
                     "title": "An item",
                     "textAlignment": "CENTER"
                   }
                 ],
                 "onClick": {
                   "openLink": {
                     "url": "https://www.example.com"
                   }
                 }
               }

            This field is a member of `oneof`_ ``data``.
        columns (google.apps.card_v1.types.Columns):
            Displays up to 2 columns.

            To include more than 2 columns, or to use rows, use the
            ``Grid`` widget.

            For example, the following JSON creates 2 columns that each
            contain text paragraphs:

            ::

               "columns": {
                 "columnItems": [
                   {
                     "horizontalSizeStyle": "FILL_AVAILABLE_SPACE",
                     "horizontalAlignment": "CENTER",
                     "verticalAlignment": "CENTER",
                     "widgets": [
                       {
                         "textParagraph": {
                           "text": "First column text paragraph"
                         }
                       }
                     ]
                   },
                   {
                     "horizontalSizeStyle": "FILL_AVAILABLE_SPACE",
                     "horizontalAlignment": "CENTER",
                     "verticalAlignment": "CENTER",
                     "widgets": [
                       {
                         "textParagraph": {
                           "text": "Second column text paragraph"
                         }
                       }
                     ]
                   }
                 ]
               }

            This field is a member of `oneof`_ ``data``.
        carousel (google.apps.card_v1.types.Carousel):
            A carousel contains a collection of nested widgets. For
            example, this is a JSON representation of a carousel that
            contains two text paragraphs.

            ::

               {
                 "widgets": [
                   {
                     "textParagraph": {
                       "text": "First text paragraph in the carousel."
                     }
                   },
                   {
                     "textParagraph": {
                       "text": "Second text paragraph in the carousel."
                     }
                   }
                 ]
               }

            This field is a member of `oneof`_ ``data``.
        chip_list (google.apps.card_v1.types.ChipList):
            A list of chips.

            For example, the following JSON creates two chips. The first
            is a text chip and the second is an icon chip that opens a
            link:

            ::

               "chipList": {
                 "chips": [
                   {
                     "text": "Edit",
                     "disabled": true,
                   },
                   {
                     "icon": {
                       "knownIcon": "INVITE",
                       "altText": "check calendar"
                     },
                     "onClick": {
                       "openLink": {
                         "url": "https://example.com/calendar"
                       }
                     }
                   }
                 ]
               }

            This field is a member of `oneof`_ ``data``.
        horizontal_alignment (google.apps.card_v1.types.Widget.HorizontalAlignment):
            Specifies whether widgets align to the left,
            right, or center of a column.
    """

    class ImageType(proto.Enum):
        r"""The shape used to crop the image.

        `Google Workspace add-ons and Chat
        apps <https://developers.google.com/workspace/extend>`__:

        Values:
            SQUARE (0):
                Default value. Applies a square mask to the
                image. For example, a 4x3 image becomes 3x3.
            CIRCLE (1):
                Applies a circular mask to the image. For
                example, a 4x3 image becomes a circle with a
                diameter of 3.
        """

        SQUARE = 0
        CIRCLE = 1

    class HorizontalAlignment(proto.Enum):
        r"""Specifies whether widgets align to the left, right, or center of a
        column.

        `Google Chat apps <https://developers.google.com/workspace/chat>`__:

        Values:
            HORIZONTAL_ALIGNMENT_UNSPECIFIED (0):
                Don't use. Unspecified.
            START (1):
                Default value. Aligns widgets to the start
                position of the column. For left-to-right
                layouts, aligns to the left. For right-to-left
                layouts, aligns to the right.
            CENTER (2):
                Aligns widgets to the center of the column.
            END (3):
                Aligns widgets to the end position of the
                column. For left-to-right layouts, aligns
                widgets to the right. For right-to-left layouts,
                aligns widgets to the left.
        """

        HORIZONTAL_ALIGNMENT_UNSPECIFIED = 0
        START = 1
        CENTER = 2
        END = 3

    class VerticalAlignment(proto.Enum):
        r"""Represents vertical alignment attribute.

        Values:
            VERTICAL_ALIGNMENT_UNSPECIFIED (0):
                Unspecified type. Do not use.
            TOP (1):
                Alignment to the top position.
            MIDDLE (2):
                Alignment to the middle position.
            BOTTOM (3):
                Alignment to the bottom position.
        """

        VERTICAL_ALIGNMENT_UNSPECIFIED = 0
        TOP = 1
        MIDDLE = 2
        BOTTOM = 3

    text_paragraph: "TextParagraph" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="data",
        message="TextParagraph",
    )
    image: "Image" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="data",
        message="Image",
    )
    decorated_text: "DecoratedText" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="data",
        message="DecoratedText",
    )
    button_list: "ButtonList" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="data",
        message="ButtonList",
    )
    text_input: "TextInput" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="data",
        message="TextInput",
    )
    selection_input: "SelectionInput" = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="data",
        message="SelectionInput",
    )
    date_time_picker: "DateTimePicker" = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="data",
        message="DateTimePicker",
    )
    divider: "Divider" = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="data",
        message="Divider",
    )
    grid: "Grid" = proto.Field(
        proto.MESSAGE,
        number=10,
        oneof="data",
        message="Grid",
    )
    columns: "Columns" = proto.Field(
        proto.MESSAGE,
        number=11,
        oneof="data",
        message="Columns",
    )
    carousel: "Carousel" = proto.Field(
        proto.MESSAGE,
        number=13,
        oneof="data",
        message="Carousel",
    )
    chip_list: "ChipList" = proto.Field(
        proto.MESSAGE,
        number=14,
        oneof="data",
        message="ChipList",
    )
    horizontal_alignment: HorizontalAlignment = proto.Field(
        proto.ENUM,
        number=8,
        enum=HorizontalAlignment,
    )


class TextParagraph(proto.Message):
    r"""A paragraph of text that supports formatting. For an example in
    Google Chat apps, see `Add a paragraph of formatted
    text <https://developers.google.com/workspace/chat/add-text-image-card-dialog#add_a_paragraph_of_formatted_text>`__.
    For more information about formatting text, see `Formatting text in
    Google Chat
    apps <https://developers.google.com/workspace/chat/format-messages#card-formatting>`__
    and `Formatting text in Google Workspace
    add-ons <https://developers.google.com/apps-script/add-ons/concepts/widgets#text_formatting>`__.

    `Google Workspace add-ons and Chat
    apps <https://developers.google.com/workspace/extend>`__:

    Attributes:
        text (str):
            The text that's shown in the widget.
        max_lines (int):
            The maximum number of lines of text that are displayed in
            the widget. If the text exceeds the specified maximum number
            of lines, the excess content is concealed behind a **show
            more** button. If the text is equal or shorter than the
            specified maximum number of lines, a **show more** button
            isn't displayed.

            The default value is 0, in which case all context is
            displayed. Negative values are ignored.
        text_syntax (google.apps.card_v1.types.TextParagraph.TextSyntax):
            The syntax of the text. If not set, the text is rendered as
            HTML.

            `Google Chat
            apps <https://developers.google.com/workspace/chat>`__:
    """

    class TextSyntax(proto.Enum):
        r"""Syntax to use for formatting text.

        `Google Chat apps <https://developers.google.com/workspace/chat>`__:

        Values:
            TEXT_SYNTAX_UNSPECIFIED (0):
                The text is rendered as HTML if unspecified.
            HTML (1):
                The text is rendered as HTML. This is the
                default value.
            MARKDOWN (2):
                The text is rendered as Markdown.
        """

        TEXT_SYNTAX_UNSPECIFIED = 0
        HTML = 1
        MARKDOWN = 2

    text: str = proto.Field(
        proto.STRING,
        number=1,
    )
    max_lines: int = proto.Field(
        proto.INT32,
        number=2,
    )
    text_syntax: TextSyntax = proto.Field(
        proto.ENUM,
        number=4,
        enum=TextSyntax,
    )


class Image(proto.Message):
    r"""An image that is specified by a URL and can have an ``onClick``
    action. For an example, see `Add an
    image <https://developers.google.com/workspace/chat/add-text-image-card-dialog#add_an_image>`__.

    `Google Workspace add-ons and Chat
    apps <https://developers.google.com/workspace/extend>`__:

    Attributes:
        image_url (str):
            The HTTPS URL that hosts the image.

            For example:

            ::

               https://developers.google.com/workspace/chat/images/quickstart-app-avatar.png
        on_click (google.apps.card_v1.types.OnClick):
            When a user clicks the image, the click
            triggers this action.
        alt_text (str):
            The alternative text of this image that's
            used for accessibility.
    """

    image_url: str = proto.Field(
        proto.STRING,
        number=1,
    )
    on_click: "OnClick" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="OnClick",
    )
    alt_text: str = proto.Field(
        proto.STRING,
        number=3,
    )


class Divider(proto.Message):
    r"""Displays a divider between widgets as a horizontal line. For an
    example in Google Chat apps, see `Add a horizontal divider between
    widgets <https://developers.google.com/workspace/chat/format-structure-card-dialog#add_a_horizontal_divider_between_widgets>`__.

    `Google Workspace add-ons and Chat
    apps <https://developers.google.com/workspace/extend>`__:

    For example, the following JSON creates a divider:

    ::

       "divider": {}

    """


class DecoratedText(proto.Message):
    r"""A widget that displays text with optional decorations such as a
    label above or below the text, an icon in front of the text, a
    selection widget, or a button after the text. For an example in
    Google Chat apps, see `Display text with decorative
    text <https://developers.google.com/workspace/chat/add-text-image-card-dialog#display_text_with_decorative_elements>`__.

    `Google Workspace add-ons and Chat
    apps <https://developers.google.com/workspace/extend>`__:

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        icon (google.apps.card_v1.types.Icon):
            Deprecated in favor of ``startIcon``.
        start_icon (google.apps.card_v1.types.Icon):
            The icon displayed in front of the text.
        start_icon_vertical_alignment (google.apps.card_v1.types.Widget.VerticalAlignment):
            Optional. Vertical alignment of the start icon. If not set,
            the icon will be vertically centered.

            `Google Chat
            apps <https://developers.google.com/workspace/chat>`__:
        top_label (str):
            The text that appears above ``text``. Always truncates.
        top_label_text (google.apps.card_v1.types.TextParagraph):
            ``TextParagraph`` equivalent of ``top_label``. Always
            truncates. Allows for more complex formatting than
            ``top_label``.

            `Google Chat
            apps <https://developers.google.com/workspace/chat>`__:
        text (str):
            Required. The primary text.

            Supports simple formatting. For more information about
            formatting text, see `Formatting text in Google Chat
            apps <https://developers.google.com/workspace/chat/format-messages#card-formatting>`__
            and `Formatting text in Google Workspace
            add-ons <https://developers.google.com/apps-script/add-ons/concepts/widgets#text_formatting>`__.
        content_text (google.apps.card_v1.types.TextParagraph):
            ``TextParagraph`` equivalent of ``text``. Allows for more
            complex formatting than ``text``.

            `Google Chat
            apps <https://developers.google.com/workspace/chat>`__:
        wrap_text (bool):
            The wrap text setting. If ``true``, the text wraps and
            displays on multiple lines. Otherwise, the text is
            truncated.

            Only applies to ``text``, not ``topLabel`` and
            ``bottomLabel``.
        bottom_label (str):
            The text that appears below ``text``. Always wraps.
        bottom_label_text (google.apps.card_v1.types.TextParagraph):
            ``TextParagraph`` equivalent of ``bottom_label``. Always
            wraps. Allows for more complex formatting than
            ``bottom_label``.

            `Google Chat
            apps <https://developers.google.com/workspace/chat>`__:
        on_click (google.apps.card_v1.types.OnClick):
            This action is triggered when users click ``topLabel`` or
            ``bottomLabel``.
        button (google.apps.card_v1.types.Button):
            A button that a user can click to trigger an
            action.

            This field is a member of `oneof`_ ``control``.
        switch_control (google.apps.card_v1.types.DecoratedText.SwitchControl):
            A switch widget that a user can click to
            change its state and trigger an action.

            This field is a member of `oneof`_ ``control``.
        end_icon (google.apps.card_v1.types.Icon):
            An icon displayed after the text.

            Supports
            `built-in <https://developers.google.com/workspace/chat/format-messages#builtinicons>`__
            and
            `custom <https://developers.google.com/workspace/chat/format-messages#customicons>`__
            icons.

            This field is a member of `oneof`_ ``control``.
    """

    class SwitchControl(proto.Message):
        r"""Either a toggle-style switch or a checkbox inside a
        ``decoratedText`` widget.

        `Google Workspace add-ons and Chat
        apps <https://developers.google.com/workspace/extend>`__:

        Only supported in the ``decoratedText`` widget.

        Attributes:
            name (str):
                The name by which the switch widget is identified in a form
                input event.

                For details about working with form inputs, see `Receive
                form
                data <https://developers.google.com/workspace/chat/read-form-data>`__.
            value (str):
                The value entered by a user, returned as part of a form
                input event.

                For details about working with form inputs, see `Receive
                form
                data <https://developers.google.com/workspace/chat/read-form-data>`__.
            selected (bool):
                When ``true``, the switch is selected.
            on_change_action (google.apps.card_v1.types.Action):
                The action to perform when the switch state
                is changed, such as what  function to run.
            control_type (google.apps.card_v1.types.DecoratedText.SwitchControl.ControlType):
                How the switch appears in the user interface.

                `Google Workspace add-ons and Chat
                apps <https://developers.google.com/workspace/extend>`__:
        """

        class ControlType(proto.Enum):
            r"""How the switch appears in the user interface.

            `Google Workspace add-ons and Chat
            apps <https://developers.google.com/workspace/extend>`__:

            Values:
                SWITCH (0):
                    A toggle-style switch.
                CHECKBOX (1):
                    Deprecated in favor of ``CHECK_BOX``.
                CHECK_BOX (2):
                    A checkbox.
            """

            SWITCH = 0
            CHECKBOX = 1
            CHECK_BOX = 2

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        value: str = proto.Field(
            proto.STRING,
            number=2,
        )
        selected: bool = proto.Field(
            proto.BOOL,
            number=3,
        )
        on_change_action: "Action" = proto.Field(
            proto.MESSAGE,
            number=4,
            message="Action",
        )
        control_type: "DecoratedText.SwitchControl.ControlType" = proto.Field(
            proto.ENUM,
            number=5,
            enum="DecoratedText.SwitchControl.ControlType",
        )

    icon: "Icon" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Icon",
    )
    start_icon: "Icon" = proto.Field(
        proto.MESSAGE,
        number=12,
        message="Icon",
    )
    start_icon_vertical_alignment: "Widget.VerticalAlignment" = proto.Field(
        proto.ENUM,
        number=13,
        enum="Widget.VerticalAlignment",
    )
    top_label: str = proto.Field(
        proto.STRING,
        number=3,
    )
    top_label_text: "TextParagraph" = proto.Field(
        proto.MESSAGE,
        number=17,
        message="TextParagraph",
    )
    text: str = proto.Field(
        proto.STRING,
        number=4,
    )
    content_text: "TextParagraph" = proto.Field(
        proto.MESSAGE,
        number=18,
        message="TextParagraph",
    )
    wrap_text: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    bottom_label: str = proto.Field(
        proto.STRING,
        number=6,
    )
    bottom_label_text: "TextParagraph" = proto.Field(
        proto.MESSAGE,
        number=19,
        message="TextParagraph",
    )
    on_click: "OnClick" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="OnClick",
    )
    button: "Button" = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="control",
        message="Button",
    )
    switch_control: SwitchControl = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="control",
        message=SwitchControl,
    )
    end_icon: "Icon" = proto.Field(
        proto.MESSAGE,
        number=11,
        oneof="control",
        message="Icon",
    )


class TextInput(proto.Message):
    r"""A field in which users can enter text. Supports suggestions and
    on-change actions. Supports form submission validation. When
    ``Action.all_widgets_are_required`` is set to ``true`` or this
    widget is specified in ``Action.required_widgets``, the submission
    action is blocked unless a value is entered. For an example in
    Google Chat apps, see `Add a field in which a user can enter
    text <https://developers.google.com/workspace/chat/design-interactive-card-dialog#add_a_field_in_which_a_user_can_enter_text>`__.

    Chat apps receive and can process the value of entered text during
    form input events. For details about working with form inputs, see
    `Receive form
    data <https://developers.google.com/workspace/chat/read-form-data>`__.

    When you need to collect undefined or abstract data from users, use
    a text input. To collect defined or enumerated data from users, use
    the [SelectionInput][google.apps.card.v1.SelectionInput] widget.

    `Google Workspace add-ons and Chat
    apps <https://developers.google.com/workspace/extend>`__:

    Attributes:
        name (str):
            The name by which the text input is identified in a form
            input event.

            For details about working with form inputs, see `Receive
            form
            data <https://developers.google.com/workspace/chat/read-form-data>`__.
        label (str):
            The text that appears above the text input field in the user
            interface.

            Specify text that helps the user enter the information your
            app needs. For example, if you are asking someone's name,
            but specifically need their surname, write ``surname``
            instead of ``name``.

            Required if ``hintText`` is unspecified. Otherwise,
            optional.
        hint_text (str):
            Text that appears below the text input field meant to assist
            users by prompting them to enter a certain value. This text
            is always visible.

            Required if ``label`` is unspecified. Otherwise, optional.
        value (str):
            The value entered by a user, returned as part of a form
            input event.

            For details about working with form inputs, see `Receive
            form
            data <https://developers.google.com/workspace/chat/read-form-data>`__.
        type_ (google.apps.card_v1.types.TextInput.Type):
            How a text input field appears in the user
            interface. For example, whether the field is
            single or multi-line.
        on_change_action (google.apps.card_v1.types.Action):
            What to do when a change occurs in the text input field. For
            example, a user adding to the field or deleting text.

            Examples of actions to take include running a custom
            function or opening a
            `dialog <https://developers.google.com/workspace/chat/dialogs>`__
            in Google Chat.
        initial_suggestions (google.apps.card_v1.types.Suggestions):
            Suggested values that users can enter. These values appear
            when users click inside the text input field. As users type,
            the suggested values dynamically filter to match what the
            users have typed.

            For example, a text input field for programming language
            might suggest Java, JavaScript, Python, and C++. When users
            start typing ``Jav``, the list of suggestions filters to
            show just ``Java`` and ``JavaScript``.

            Suggested values help guide users to enter values that your
            app can make sense of. When referring to JavaScript, some
            users might enter ``javascript`` and others ``java script``.
            Suggesting ``JavaScript`` can standardize how users interact
            with your app.

            When specified, ``TextInput.type`` is always
            ``SINGLE_LINE``, even if it's set to ``MULTIPLE_LINE``.

            `Google Workspace add-ons and Chat
            apps <https://developers.google.com/workspace/extend>`__:
        auto_complete_action (google.apps.card_v1.types.Action):
            Optional. Specify what action to take when the text input
            field provides suggestions to users who interact with it.

            If unspecified, the suggestions are set by
            ``initialSuggestions`` and are processed by the client.

            If specified, the app takes the action specified here, such
            as running a custom function.

            `Google Workspace
            add-ons <https://developers.google.com/workspace/add-ons>`__:
        validation (google.apps.card_v1.types.Validation):
            Specify the input format validation necessary for this text
            field.

            `Google Workspace add-ons and Chat
            apps <https://developers.google.com/workspace/extend>`__:
        placeholder_text (str):
            Text that appears in the text input field when the field is
            empty. Use this text to prompt users to enter a value. For
            example, ``Enter a number from 0 to 100``.

            `Google Chat
            apps <https://developers.google.com/workspace/chat>`__:
    """

    class Type(proto.Enum):
        r"""How a text input field appears in the user interface. For example,
        whether it's a single line input field, or a multi-line input. If
        ``initialSuggestions`` is specified, ``type`` is always
        ``SINGLE_LINE``, even if it's set to ``MULTIPLE_LINE``.

        `Google Workspace add-ons and Chat
        apps <https://developers.google.com/workspace/extend>`__:

        Values:
            SINGLE_LINE (0):
                The text input field has a fixed height of
                one line.
            MULTIPLE_LINE (1):
                The text input field has a fixed height of
                multiple lines.
        """

        SINGLE_LINE = 0
        MULTIPLE_LINE = 1

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    label: str = proto.Field(
        proto.STRING,
        number=2,
    )
    hint_text: str = proto.Field(
        proto.STRING,
        number=3,
    )
    value: str = proto.Field(
        proto.STRING,
        number=4,
    )
    type_: Type = proto.Field(
        proto.ENUM,
        number=5,
        enum=Type,
    )
    on_change_action: "Action" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="Action",
    )
    initial_suggestions: "Suggestions" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="Suggestions",
    )
    auto_complete_action: "Action" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="Action",
    )
    validation: "Validation" = proto.Field(
        proto.MESSAGE,
        number=11,
        message="Validation",
    )
    placeholder_text: str = proto.Field(
        proto.STRING,
        number=12,
    )


class Suggestions(proto.Message):
    r"""Suggested values that users can enter. These values appear when
    users click inside the text input field. As users type, the
    suggested values dynamically filter to match what the users have
    typed.

    For example, a text input field for programming language might
    suggest Java, JavaScript, Python, and C++. When users start typing
    ``Jav``, the list of suggestions filters to show ``Java`` and
    ``JavaScript``.

    Suggested values help guide users to enter values that your app can
    make sense of. When referring to JavaScript, some users might enter
    ``javascript`` and others ``java script``. Suggesting ``JavaScript``
    can standardize how users interact with your app.

    When specified, ``TextInput.type`` is always ``SINGLE_LINE``, even
    if it's set to ``MULTIPLE_LINE``.

    `Google Workspace add-ons and Chat
    apps <https://developers.google.com/workspace/extend>`__:

    Attributes:
        items (MutableSequence[google.apps.card_v1.types.Suggestions.SuggestionItem]):
            A list of suggestions used for autocomplete
            recommendations in text input fields.
    """

    class SuggestionItem(proto.Message):
        r"""One suggested value that users can enter in a text input field.

        `Google Workspace add-ons and Chat
        apps <https://developers.google.com/workspace/extend>`__:


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            text (str):
                The value of a suggested input to a text
                input field. This is equivalent to what users
                enter themselves.

                This field is a member of `oneof`_ ``content``.
        """

        text: str = proto.Field(
            proto.STRING,
            number=1,
            oneof="content",
        )

    items: MutableSequence[SuggestionItem] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=SuggestionItem,
    )


class ButtonList(proto.Message):
    r"""A list of buttons layed out horizontally. For an example in Google
    Chat apps, see `Add a
    button <https://developers.google.com/workspace/chat/design-interactive-card-dialog#add_a_button>`__.

    `Google Workspace add-ons and Chat
    apps <https://developers.google.com/workspace/extend>`__:

    Attributes:
        buttons (MutableSequence[google.apps.card_v1.types.Button]):
            An array of buttons.
    """

    buttons: MutableSequence["Button"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Button",
    )


class SelectionInput(proto.Message):
    r"""A widget that creates one or more UI items that users can select.
    Supports form submission validation for ``dropdown`` and
    ``multiselect`` menus only. When ``Action.all_widgets_are_required``
    is set to ``true`` or this widget is specified in
    ``Action.required_widgets``, the submission action is blocked unless
    a value is selected. For example, a dropdown menu or checkboxes. You
    can use this widget to collect data that can be predicted or
    enumerated. For an example in Google Chat apps, see `Add selectable
    UI
    elements </workspace/chat/design-interactive-card-dialog#add_selectable_ui_elements>`__.

    Chat apps can process the value of items that users select or input.
    For details about working with form inputs, see `Receive form
    data <https://developers.google.com/workspace/chat/read-form-data>`__.

    To collect undefined or abstract data from users, use the
    [TextInput][google.apps.card.v1.TextInput] widget.

    `Google Workspace add-ons and Chat
    apps <https://developers.google.com/workspace/extend>`__:

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Required. The name that identifies the selection input in a
            form input event.

            For details about working with form inputs, see `Receive
            form
            data <https://developers.google.com/workspace/chat/read-form-data>`__.
        label (str):
            The text that appears above the selection
            input field in the user interface.

            Specify text that helps the user enter the
            information your app needs. For example, if
            users are selecting the urgency of a work ticket
            from a drop-down menu, the label might be
            "Urgency" or "Select urgency".
        type_ (google.apps.card_v1.types.SelectionInput.SelectionType):
            The type of items that are displayed to users in a
            ``SelectionInput`` widget. Selection types support different
            types of interactions. For example, users can select one or
            more checkboxes, but they can only select one value from a
            dropdown menu.
        items (MutableSequence[google.apps.card_v1.types.SelectionInput.SelectionItem]):
            An array of selectable items. For example, an
            array of radio buttons or checkboxes. Supports
            up to 100 items.
        on_change_action (google.apps.card_v1.types.Action):
            If specified, the form is submitted when the selection
            changes. If not specified, you must specify a separate
            button that submits the form.

            For details about working with form inputs, see `Receive
            form
            data <https://developers.google.com/workspace/chat/read-form-data>`__.
        multi_select_max_selected_items (int):
            For multiselect menus, the maximum number of
            items that a user can select. Minimum value is 1
            item. If unspecified, defaults to 3 items.

            This field is a member of `oneof`_ ``_multi_select_max_selected_items``.
        multi_select_min_query_length (int):
            For multiselect menus, the number of text characters that a
            user inputs before the menu returns suggested selection
            items.

            If unset, the multiselect menu uses the following default
            values:

            - If the menu uses a static array of ``SelectionInput``
              items, defaults to 0 characters and immediately populates
              items from the array.
            - If the menu uses a dynamic data source
              (``multi_select_data_source``), defaults to 3 characters
              before querying the data source to return suggested items.
        external_data_source (google.apps.card_v1.types.Action):
            An external data source, such as a relational
            database.

            This field is a member of `oneof`_ ``multi_select_data_source``.
        platform_data_source (google.apps.card_v1.types.SelectionInput.PlatformDataSource):
            A data source from Google Workspace.

            This field is a member of `oneof`_ ``multi_select_data_source``.
    """

    class SelectionType(proto.Enum):
        r"""The format for the items that users can select. Different options
        support different types of interactions. For example, users can
        select multiple checkboxes, but can only select one item from a
        dropdown menu.

        Each selection input supports one type of selection. Mixing
        checkboxes and switches, for example, isn't supported.

        `Google Workspace add-ons and Chat
        apps <https://developers.google.com/workspace/extend>`__:

        Values:
            CHECK_BOX (0):
                A set of checkboxes. Users can select one or
                more checkboxes.
            RADIO_BUTTON (1):
                A set of radio buttons. Users can select one
                radio button.
            SWITCH (2):
                A set of switches. Users can turn on one or
                more switches.
            DROPDOWN (3):
                A dropdown menu. Users can select one item from the menu.

                For Google Chat apps, you can populate items using a dynamic
                data source and autosuggest items as users type in the menu.
                For example, users can start typing the name of a Google
                Chat space and the widget autosuggests the space. To
                dynamically populate items for a dropdown menu, use one of
                the following types of data sources:

                - Google Workspace data: Items are populated using data from
                  Google Workspace, such as Google Workspace users or Google
                  Chat spaces.
                - External data: Items are populated from an external data
                  source outside of Google Workspace.

                For examples of how to implement dropdown menus for Chat
                apps, see `Add a dropdown
                menu <https://developers.google.com/workspace/chat/design-interactive-card-dialog#dropdown-menu>`__
                and `Dynamically populate drop-down
                menus <https://developers.google.com/workspace/chat/design-interactive-card-dialog#dynamic-dropdown-menu>`__.

                `Google Workspace add-ons and Chat
                apps <https://developers.google.com/workspace/extend>`__:
            MULTI_SELECT (4):
                A menu with a text box. Users can type and select one or
                more items. For Google Workspace add-ons, you must populate
                items using a static array of ``SelectionItem`` objects.

                For Google Chat apps, you can also populate items using a
                dynamic data source and autosuggest items as users type in
                the menu. For example, users can start typing the name of a
                Google Chat space and the widget autosuggests the space. To
                dynamically populate items for a multiselect menu, use one
                of the following types of data sources:

                - Google Workspace data: Items are populated using data from
                  Google Workspace, such as Google Workspace users or Google
                  Chat spaces.
                - External data: Items are populated from an external data
                  source outside of Google Workspace.

                For examples of how to implement multiselect menus for Chat
                apps, see `Add a multiselect
                menu <https://developers.google.com/workspace/chat/design-interactive-card-dialog#multiselect-menu>`__.

                `Google Workspace add-ons and Chat
                apps <https://developers.google.com/workspace/extend>`__:
        """

        CHECK_BOX = 0
        RADIO_BUTTON = 1
        SWITCH = 2
        DROPDOWN = 3
        MULTI_SELECT = 4

    class SelectionItem(proto.Message):
        r"""An item that users can select in a selection input, such as a
        checkbox or switch. Supports up to 100 items.

        `Google Workspace add-ons and Chat
        apps <https://developers.google.com/workspace/extend>`__:


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            text (str):
                The text that identifies or describes the
                item to users.
            value (str):
                The value associated with this item. The client should use
                this as a form input value.

                For details about working with form inputs, see `Receive
                form
                data <https://developers.google.com/workspace/chat/read-form-data>`__.
            selected (bool):
                Whether the item is selected by default. If
                the selection input only accepts one value (such
                as for radio buttons or a dropdown menu), only
                set this field for one item.
            start_icon_uri (str):

                This field is a member of `oneof`_ ``start_icon``.
            bottom_text (str):
                For multiselect menus, a text description or label that's
                displayed below the item's ``text`` field.
        """

        text: str = proto.Field(
            proto.STRING,
            number=1,
        )
        value: str = proto.Field(
            proto.STRING,
            number=2,
        )
        selected: bool = proto.Field(
            proto.BOOL,
            number=3,
        )
        start_icon_uri: str = proto.Field(
            proto.STRING,
            number=4,
            oneof="start_icon",
        )
        bottom_text: str = proto.Field(
            proto.STRING,
            number=5,
        )

    class PlatformDataSource(proto.Message):
        r"""For a [``SelectionInput``][google.apps.card.v1.SelectionInput]
        widget that uses a multiselect menu, a data source from Google
        Workspace. Used to populate items in a multiselect menu.

        `Google Chat apps <https://developers.google.com/workspace/chat>`__:


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            common_data_source (google.apps.card_v1.types.SelectionInput.PlatformDataSource.CommonDataSource):
                A data source shared by all Google Workspace
                applications, such as users in a Google
                Workspace organization.

                This field is a member of `oneof`_ ``data_source``.
        """

        class CommonDataSource(proto.Enum):
            r"""A data source shared by all [Google Workspace applications]
            (https://developers.google.com/workspace/chat/api/reference/rest/v1/HostApp).

            `Google Chat apps <https://developers.google.com/workspace/chat>`__:

            Values:
                UNKNOWN (0):
                    Default value. Don't use.
                USER (1):
                    Google Workspace users. The user can only
                    view and select users from their Google
                    Workspace organization.
            """

            UNKNOWN = 0
            USER = 1

        common_data_source: "SelectionInput.PlatformDataSource.CommonDataSource" = (
            proto.Field(
                proto.ENUM,
                number=1,
                oneof="data_source",
                enum="SelectionInput.PlatformDataSource.CommonDataSource",
            )
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    label: str = proto.Field(
        proto.STRING,
        number=2,
    )
    type_: SelectionType = proto.Field(
        proto.ENUM,
        number=3,
        enum=SelectionType,
    )
    items: MutableSequence[SelectionItem] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=SelectionItem,
    )
    on_change_action: "Action" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="Action",
    )
    multi_select_max_selected_items: int = proto.Field(
        proto.INT32,
        number=6,
        optional=True,
    )
    multi_select_min_query_length: int = proto.Field(
        proto.INT32,
        number=7,
    )
    external_data_source: "Action" = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="multi_select_data_source",
        message="Action",
    )
    platform_data_source: PlatformDataSource = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="multi_select_data_source",
        message=PlatformDataSource,
    )


class DateTimePicker(proto.Message):
    r"""Lets users input a date, a time, or both a date and a time. Supports
    form submission validation. When ``Action.all_widgets_are_required``
    is set to ``true`` or this widget is specified in
    ``Action.required_widgets``, the submission action is blocked unless
    a value is selected. For an example in Google Chat apps, see `Let a
    user pick a date and
    time <https://developers.google.com/workspace/chat/design-interactive-card-dialog#let_a_user_pick_a_date_and_time>`__.

    Users can input text or use the picker to select dates and times. If
    users input an invalid date or time, the picker shows an error that
    prompts users to input the information correctly.

    `Google Workspace add-ons and Chat
    apps <https://developers.google.com/workspace/extend>`__:


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            The name by which the ``DateTimePicker`` is identified in a
            form input event.

            For details about working with form inputs, see `Receive
            form
            data <https://developers.google.com/workspace/chat/read-form-data>`__.
        label (str):
            The text that prompts users to input a date, a time, or a
            date and time. For example, if users are scheduling an
            appointment, use a label such as ``Appointment date`` or
            ``Appointment date and time``.
        type_ (google.apps.card_v1.types.DateTimePicker.DateTimePickerType):
            Whether the widget supports inputting a date,
            a time, or the date and time.
        value_ms_epoch (int):
            Optional. The default value displayed in the widget, in
            milliseconds since `Unix epoch
            time <https://en.wikipedia.org/wiki/Unix_time>`__.

            Specify the value based on the type of picker
            (``DateTimePickerType``):

            - ``DATE_AND_TIME``: a calendar date and time in UTC. For
              example, to represent January 1, 2023 at 12:00 PM UTC, use
              ``1672574400000``.
            - ``DATE_ONLY``: a calendar date at 00:00:00 UTC. For
              example, to represent January 1, 2023, use
              ``1672531200000``.
            - ``TIME_ONLY``: a time in UTC. For example, to represent
              12:00 PM, use ``43200000`` (or ``12 * 60 * 60 * 1000``).

            This field is a member of `oneof`_ ``_value_ms_epoch``.
        timezone_offset_date (int):
            The number representing the time zone offset from UTC, in
            minutes. If set, the ``value_ms_epoch`` is displayed in the
            specified time zone. If unset, the value defaults to the
            user's time zone setting.
        on_change_action (google.apps.card_v1.types.Action):
            Triggered when the user clicks **Save** or **Clear** from
            the ``DateTimePicker`` interface.
    """

    class DateTimePickerType(proto.Enum):
        r"""The format for the date and time in the ``DateTimePicker`` widget.
        Determines whether users can input a date, a time, or both a date
        and time.

        `Google Workspace add-ons and Chat
        apps <https://developers.google.com/workspace/extend>`__:

        Values:
            DATE_AND_TIME (0):
                Users input a date and time.
            DATE_ONLY (1):
                Users input a date.
            TIME_ONLY (2):
                Users input a time.
        """

        DATE_AND_TIME = 0
        DATE_ONLY = 1
        TIME_ONLY = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    label: str = proto.Field(
        proto.STRING,
        number=2,
    )
    type_: DateTimePickerType = proto.Field(
        proto.ENUM,
        number=3,
        enum=DateTimePickerType,
    )
    value_ms_epoch: int = proto.Field(
        proto.INT64,
        number=4,
        optional=True,
    )
    timezone_offset_date: int = proto.Field(
        proto.INT32,
        number=5,
    )
    on_change_action: "Action" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="Action",
    )


class OverflowMenu(proto.Message):
    r"""A widget that presents a pop-up menu with one or more actions that
    users can invoke. For example, showing non-primary actions in a
    card. You can use this widget when actions don't fit in the
    available space. To use, specify this widget in the ``OnClick``
    action of widgets that support it. For example, in a ``Button``.

    `Google Workspace add-ons and Chat
    apps <https://developers.google.com/workspace/extend>`__:

    Attributes:
        items (MutableSequence[google.apps.card_v1.types.OverflowMenu.OverflowMenuItem]):
            Required. The list of menu options.
    """

    class OverflowMenuItem(proto.Message):
        r"""An option that users can invoke in an overflow menu.

        `Google Workspace add-ons and Chat
        apps <https://developers.google.com/workspace/extend>`__:

        Attributes:
            start_icon (google.apps.card_v1.types.Icon):
                The icon displayed in front of the text.
            text (str):
                Required. The text that identifies or
                describes the item to users.
            on_click (google.apps.card_v1.types.OnClick):
                Required. The action invoked when a menu option is selected.
                This ``OnClick`` cannot contain an ``OverflowMenu``, any
                specified ``OverflowMenu`` is dropped and the menu item
                disabled.
            disabled (bool):
                Whether the menu option is disabled.
                Defaults to false.
        """

        start_icon: "Icon" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="Icon",
        )
        text: str = proto.Field(
            proto.STRING,
            number=2,
        )
        on_click: "OnClick" = proto.Field(
            proto.MESSAGE,
            number=3,
            message="OnClick",
        )
        disabled: bool = proto.Field(
            proto.BOOL,
            number=4,
        )

    items: MutableSequence[OverflowMenuItem] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=OverflowMenuItem,
    )


class Button(proto.Message):
    r"""A text, icon, or text and icon button that users can click. For an
    example in Google Chat apps, see `Add a
    button <https://developers.google.com/workspace/chat/design-interactive-card-dialog#add_a_button>`__.

    To make an image a clickable button, specify an
    [``Image``][google.apps.card.v1.Image] (not an
    [``ImageComponent``][google.apps.card.v1.ImageComponent]) and set an
    ``onClick`` action.

    `Google Workspace add-ons and Chat
    apps <https://developers.google.com/workspace/extend>`__:

    Attributes:
        text (str):
            The text displayed inside the button.
        icon (google.apps.card_v1.types.Icon):
            An icon displayed inside the button. If both ``icon`` and
            ``text`` are set, then the icon appears before the text.
        color (google.type.color_pb2.Color):
            Optional. The color of the button. If set, the button
            ``type`` is set to ``FILLED`` and the color of ``text`` and
            ``icon`` fields are set to a contrasting color for
            readability. For example, if the button color is set to
            blue, any text or icons in the button are set to white.

            To set the button color, specify a value for the ``red``,
            ``green``, and ``blue`` fields. The value must be a float
            number between 0 and 1 based on the RGB color value, where
            ``0`` (0/255) represents the absence of color and ``1``
            (255/255) represents the maximum intensity of the color.

            For example, the following sets the color to red at its
            maximum intensity:

            ::

               "color": {
                  "red": 1,
                  "green": 0,
                  "blue": 0,
               }

            The ``alpha`` field is unavailable for button color. If
            specified, this field is ignored.
        on_click (google.apps.card_v1.types.OnClick):
            Required. The action to perform when a user
            clicks the button, such as opening a hyperlink
            or running a custom function.
        disabled (bool):
            If ``true``, the button is displayed in an inactive state
            and doesn't respond to user actions.
        alt_text (str):
            The alternative text that's used for
            accessibility.
            Set descriptive text that lets users know what
            the button does. For example, if a button opens
            a hyperlink, you might write: "Opens a new
            browser tab and navigates to the Google Chat
            developer documentation at
            https://developers.google.com/workspace/chat".
        type_ (google.apps.card_v1.types.Button.Type):
            Optional. The type of a button. If unset, button type
            defaults to ``OUTLINED``. If the ``color`` field is set, the
            button type is forced to ``FILLED`` and any value set for
            this field is ignored.
    """

    class Type(proto.Enum):
        r"""Optional. The
        `type <https://m3.material.io/components/all-buttons#9134ac95-678e-49ae-a50a-e71948011b05>`__
        of a button. If ``color`` field is set, the ``type`` is forced to
        ``FILLED``.

        `Google Chat apps <https://developers.google.com/workspace/chat>`__:

        Values:
            TYPE_UNSPECIFIED (0):
                Don't use. Unspecified.
            OUTLINED (1):
                Outlined buttons are medium-emphasis buttons.
                They usually contain actions that are important,
                but aren’t the primary action in a Chat app or
                an add-on.
            FILLED (2):
                A filled button has a container with a solid
                color. It has the most visual impact and is
                recommended for the important and primary action
                in a Chat app or an add-on.
            FILLED_TONAL (3):
                A filled tonal button is an alternative
                middle ground between filled and outlined
                buttons. They’re useful in contexts where a
                lower-priority button requires slightly more
                emphasis than an outline button would give.
            BORDERLESS (4):
                A button does not have an invisible container
                in its default state. It is often used for the
                lowest priority actions, especially when
                presenting multiple options.
        """

        TYPE_UNSPECIFIED = 0
        OUTLINED = 1
        FILLED = 2
        FILLED_TONAL = 3
        BORDERLESS = 4

    text: str = proto.Field(
        proto.STRING,
        number=1,
    )
    icon: "Icon" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Icon",
    )
    color: color_pb2.Color = proto.Field(
        proto.MESSAGE,
        number=3,
        message=color_pb2.Color,
    )
    on_click: "OnClick" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="OnClick",
    )
    disabled: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    alt_text: str = proto.Field(
        proto.STRING,
        number=6,
    )
    type_: Type = proto.Field(
        proto.ENUM,
        number=7,
        enum=Type,
    )


class Icon(proto.Message):
    r"""An icon displayed in a widget on a card. For an example in Google
    Chat apps, see `Add an
    icon <https://developers.google.com/workspace/chat/add-text-image-card-dialog#add_an_icon>`__.

    Supports
    `built-in <https://developers.google.com/workspace/chat/format-messages#builtinicons>`__
    and
    `custom <https://developers.google.com/workspace/chat/format-messages#customicons>`__
    icons.

    `Google Workspace add-ons and Chat
    apps <https://developers.google.com/workspace/extend>`__:

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        known_icon (str):
            Display one of the built-in icons provided by Google
            Workspace.

            For example, to display an airplane icon, specify
            ``AIRPLANE``. For a bus, specify ``BUS``.

            For a full list of supported icons, see `built-in
            icons <https://developers.google.com/workspace/chat/format-messages#builtinicons>`__.

            This field is a member of `oneof`_ ``icons``.
        icon_url (str):
            Display a custom icon hosted at an HTTPS URL.

            For example:

            ::

               "iconUrl":
               "https://developers.google.com/workspace/chat/images/quickstart-app-avatar.png"

            Supported file types include ``.png`` and ``.jpg``.

            This field is a member of `oneof`_ ``icons``.
        material_icon (google.apps.card_v1.types.MaterialIcon):
            Display one of the `Google Material
            Icons <https://fonts.google.com/icons>`__.

            For example, to display a `checkbox
            icon <https://fonts.google.com/icons?selected=Material%20Symbols%20Outlined%3Acheck_box%3AFILL%400%3Bwght%40400%3BGRAD%400%3Bopsz%4048>`__,
            use

            ::

               "material_icon": {
                 "name": "check_box"
               }

            `Google Chat
            apps <https://developers.google.com/workspace/chat>`__:

            This field is a member of `oneof`_ ``icons``.
        alt_text (str):
            Optional. A description of the icon used for accessibility.
            If unspecified, the default value ``Button`` is provided. As
            a best practice, you should set a helpful description for
            what the icon displays, and if applicable, what it does. For
            example, ``A user's account portrait``, or
            ``Opens a new browser tab and navigates to the Google Chat developer documentation at https://developers.google.com/workspace/chat``.

            If the icon is set in a
            [``Button``][google.apps.card.v1.Button], the ``altText``
            appears as helper text when the user hovers over the button.
            However, if the button also sets ``text``, the icon's
            ``altText`` is ignored.
        image_type (google.apps.card_v1.types.Widget.ImageType):
            The crop style applied to the image. In some cases, applying
            a ``CIRCLE`` crop causes the image to be drawn larger than a
            built-in icon.
    """

    known_icon: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="icons",
    )
    icon_url: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="icons",
    )
    material_icon: "MaterialIcon" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="icons",
        message="MaterialIcon",
    )
    alt_text: str = proto.Field(
        proto.STRING,
        number=3,
    )
    image_type: "Widget.ImageType" = proto.Field(
        proto.ENUM,
        number=4,
        enum="Widget.ImageType",
    )


class MaterialIcon(proto.Message):
    r"""A `Google Material Icon <https://fonts.google.com/icons>`__, which
    includes over 2500+ options.

    For example, to display a `checkbox
    icon <https://fonts.google.com/icons?selected=Material%20Symbols%20Outlined%3Acheck_box%3AFILL%400%3Bwght%40400%3BGRAD%400%3Bopsz%4048>`__
    with customized weight and grade, write the following:

    ::

       {
         "name": "check_box",
         "fill": true,
         "weight": 300,
         "grade": -25
       }

    `Google Chat apps <https://developers.google.com/workspace/chat>`__:

    Attributes:
        name (str):
            The icon name defined in the `Google Material
            Icon <https://fonts.google.com/icons>`__, for example,
            ``check_box``. Any invalid names are abandoned and replaced
            with empty string and results in the icon failing to render.
        fill (bool):
            Whether the icon renders as filled. Default value is false.

            To preview different icon settings, go to `Google Font
            Icons <https://fonts.google.com/icons>`__ and adjust the
            settings under **Customize**.
        weight (int):
            The stroke weight of the icon. Choose from {100, 200, 300,
            400, 500, 600, 700}. If absent, default value is 400. If any
            other value is specified, the default value is used.

            To preview different icon settings, go to `Google Font
            Icons <https://fonts.google.com/icons>`__ and adjust the
            settings under **Customize**.
        grade (int):
            Weight and grade affect a symbol’s thickness. Adjustments to
            grade are more granular than adjustments to weight and have
            a small impact on the size of the symbol. Choose from {-25,
            0, 200}. If absent, default value is 0. If any other value
            is specified, the default value is used.

            To preview different icon settings, go to `Google Font
            Icons <https://fonts.google.com/icons>`__ and adjust the
            settings under **Customize**.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    fill: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    weight: int = proto.Field(
        proto.INT32,
        number=3,
    )
    grade: int = proto.Field(
        proto.INT32,
        number=4,
    )


class ImageCropStyle(proto.Message):
    r"""Represents the crop style applied to an image.

    `Google Workspace add-ons and Chat
    apps <https://developers.google.com/workspace/extend>`__:

    For example, here's how to apply a 16:9 aspect ratio:

    ::

       cropStyle {
        "type": "RECTANGLE_CUSTOM",
        "aspectRatio": 16/9
       }

    Attributes:
        type_ (google.apps.card_v1.types.ImageCropStyle.ImageCropType):
            The crop type.
        aspect_ratio (float):
            The aspect ratio to use if the crop type is
            ``RECTANGLE_CUSTOM``.

            For example, here's how to apply a 16:9 aspect ratio:

            ::

               cropStyle {
                "type": "RECTANGLE_CUSTOM",
                "aspectRatio": 16/9
               }
    """

    class ImageCropType(proto.Enum):
        r"""Represents the crop style applied to an image.

        `Google Workspace add-ons and Chat
        apps <https://developers.google.com/workspace/extend>`__:

        Values:
            IMAGE_CROP_TYPE_UNSPECIFIED (0):
                Don't use. Unspecified.
            SQUARE (1):
                Default value. Applies a square crop.
            CIRCLE (2):
                Applies a circular crop.
            RECTANGLE_CUSTOM (3):
                Applies a rectangular crop with a custom aspect ratio. Set
                the custom aspect ratio with ``aspectRatio``.
            RECTANGLE_4_3 (4):
                Applies a rectangular crop with a 4:3 aspect
                ratio.
        """

        IMAGE_CROP_TYPE_UNSPECIFIED = 0
        SQUARE = 1
        CIRCLE = 2
        RECTANGLE_CUSTOM = 3
        RECTANGLE_4_3 = 4

    type_: ImageCropType = proto.Field(
        proto.ENUM,
        number=1,
        enum=ImageCropType,
    )
    aspect_ratio: float = proto.Field(
        proto.DOUBLE,
        number=2,
    )


class BorderStyle(proto.Message):
    r"""The style options for the border of a card or widget, including the
    border type and color.

    `Google Workspace add-ons and Chat
    apps <https://developers.google.com/workspace/extend>`__:

    Attributes:
        type_ (google.apps.card_v1.types.BorderStyle.BorderType):
            The border type.
        stroke_color (google.type.color_pb2.Color):
            The colors to use when the type is ``BORDER_TYPE_STROKE``.

            To set the stroke color, specify a value for the ``red``,
            ``green``, and ``blue`` fields. The value must be a float
            number between 0 and 1 based on the RGB color value, where
            ``0`` (0/255) represents the absence of color and ``1``
            (255/255) represents the maximum intensity of the color.

            For example, the following sets the color to red at its
            maximum intensity:

            ::

               "color": {
                  "red": 1,
                  "green": 0,
                  "blue": 0,
               }

            The ``alpha`` field is unavailable for stroke color. If
            specified, this field is ignored.
        corner_radius (int):
            The corner radius for the border.
    """

    class BorderType(proto.Enum):
        r"""Represents the border types applied to widgets.

        `Google Workspace add-ons and Chat
        apps <https://developers.google.com/workspace/extend>`__:

        Values:
            BORDER_TYPE_UNSPECIFIED (0):
                Don't use. Unspecified.
            NO_BORDER (1):
                No border.
            STROKE (2):
                Default value. Outline.
        """

        BORDER_TYPE_UNSPECIFIED = 0
        NO_BORDER = 1
        STROKE = 2

    type_: BorderType = proto.Field(
        proto.ENUM,
        number=1,
        enum=BorderType,
    )
    stroke_color: color_pb2.Color = proto.Field(
        proto.MESSAGE,
        number=2,
        message=color_pb2.Color,
    )
    corner_radius: int = proto.Field(
        proto.INT32,
        number=3,
    )


class ImageComponent(proto.Message):
    r"""Represents an image.

    `Google Workspace add-ons and Chat
    apps <https://developers.google.com/workspace/extend>`__:

    Attributes:
        image_uri (str):
            The image URL.
        alt_text (str):
            The accessibility label for the image.
        crop_style (google.apps.card_v1.types.ImageCropStyle):
            The crop style to apply to the image.
        border_style (google.apps.card_v1.types.BorderStyle):
            The border style to apply to the image.
    """

    image_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    alt_text: str = proto.Field(
        proto.STRING,
        number=2,
    )
    crop_style: "ImageCropStyle" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="ImageCropStyle",
    )
    border_style: "BorderStyle" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="BorderStyle",
    )


class Grid(proto.Message):
    r"""Displays a grid with a collection of items. Items can only include
    text or images. For responsive columns, or to include more than text
    or images, use [``Columns``][google.apps.card.v1.Columns]. For an
    example in Google Chat apps, see `Display a Grid with a collection
    of
    items <https://developers.google.com/workspace/chat/format-structure-card-dialog#display_a_grid_with_a_collection_of_items>`__.

    A grid supports any number of columns and items. The number of rows
    is determined by items divided by columns. A grid with 10 items and
    2 columns has 5 rows. A grid with 11 items and 2 columns has 6 rows.

    `Google Workspace add-ons and Chat
    apps <https://developers.google.com/workspace/extend>`__:

    For example, the following JSON creates a 2 column grid with a
    single item:

    ::

       "grid": {
         "title": "A fine collection of items",
         "columnCount": 2,
         "borderStyle": {
           "type": "STROKE",
           "cornerRadius": 4
         },
         "items": [
           {
             "image": {
               "imageUri": "https://www.example.com/image.png",
               "cropStyle": {
                 "type": "SQUARE"
               },
               "borderStyle": {
                 "type": "STROKE"
               }
             },
             "title": "An item",
             "textAlignment": "CENTER"
           }
         ],
         "onClick": {
           "openLink": {
             "url": "https://www.example.com"
           }
         }
       }

    Attributes:
        title (str):
            The text that displays in the grid header.
        items (MutableSequence[google.apps.card_v1.types.Grid.GridItem]):
            The items to display in the grid.
        border_style (google.apps.card_v1.types.BorderStyle):
            The border style to apply to each grid item.
        column_count (int):
            The number of columns to display in the grid.
            A default value is used if this field isn't
            specified, and that default value is different
            depending on where the grid is shown (dialog
            versus companion).
        on_click (google.apps.card_v1.types.OnClick):
            This callback is reused by each individual
            grid item, but with the item's identifier and
            index in the items list added to the callback's
            parameters.
    """

    class GridItem(proto.Message):
        r"""Represents an item in a grid layout. Items can contain text, an
        image, or both text and an image.

        `Google Workspace add-ons and Chat
        apps <https://developers.google.com/workspace/extend>`__:

        Attributes:
            id (str):
                A user-specified identifier for this grid item. This
                identifier is returned in the parent grid's ``onClick``
                callback parameters.
            image (google.apps.card_v1.types.ImageComponent):
                The image that displays in the grid item.
            title (str):
                The grid item's title.
            subtitle (str):
                The grid item's subtitle.
            layout (google.apps.card_v1.types.Grid.GridItem.GridItemLayout):
                The layout to use for the grid item.
        """

        class GridItemLayout(proto.Enum):
            r"""Represents the various layout options available for a grid item.

            `Google Workspace add-ons and Chat
            apps <https://developers.google.com/workspace/extend>`__:

            Values:
                GRID_ITEM_LAYOUT_UNSPECIFIED (0):
                    Don't use. Unspecified.
                TEXT_BELOW (1):
                    The title and subtitle are shown below the
                    grid item's image.
                TEXT_ABOVE (2):
                    The title and subtitle are shown above the
                    grid item's image.
            """

            GRID_ITEM_LAYOUT_UNSPECIFIED = 0
            TEXT_BELOW = 1
            TEXT_ABOVE = 2

        id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        image: "ImageComponent" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="ImageComponent",
        )
        title: str = proto.Field(
            proto.STRING,
            number=3,
        )
        subtitle: str = proto.Field(
            proto.STRING,
            number=4,
        )
        layout: "Grid.GridItem.GridItemLayout" = proto.Field(
            proto.ENUM,
            number=9,
            enum="Grid.GridItem.GridItemLayout",
        )

    title: str = proto.Field(
        proto.STRING,
        number=1,
    )
    items: MutableSequence[GridItem] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=GridItem,
    )
    border_style: "BorderStyle" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="BorderStyle",
    )
    column_count: int = proto.Field(
        proto.INT32,
        number=4,
    )
    on_click: "OnClick" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="OnClick",
    )


class Columns(proto.Message):
    r"""The ``Columns`` widget displays up to 2 columns in a card or dialog.
    You can add widgets to each column; the widgets appear in the order
    that they are specified. For an example in Google Chat apps, see
    `Display cards and dialogs in
    columns <https://developers.google.com/workspace/chat/format-structure-card-dialog#display_cards_and_dialogs_in_columns>`__.

    The height of each column is determined by the taller column. For
    example, if the first column is taller than the second column, both
    columns have the height of the first column. Because each column can
    contain a different number of widgets, you can't define rows or
    align widgets between the columns.

    Columns are displayed side-by-side. You can customize the width of
    each column using the ``HorizontalSizeStyle`` field. If the user's
    screen width is too narrow, the second column wraps below the first:

    - On web, the second column wraps if the screen width is less than
      or equal to 480 pixels.
    - On iOS devices, the second column wraps if the screen width is
      less than or equal to 300 pt.
    - On Android devices, the second column wraps if the screen width is
      less than or equal to 320 dp.

    To include more than two columns, or to use rows, use the
    [``Grid``][google.apps.card.v1.Grid] widget.

    `Google Workspace add-ons and Chat
    apps <https://developers.google.com/workspace/extend>`__: The add-on
    UIs that support columns include:

    - The dialog displayed when users open the add-on from an email
      draft.
    - The dialog displayed when users open the add-on from the **Add
      attachment** menu in a Google Calendar event.

    Attributes:
        column_items (MutableSequence[google.apps.card_v1.types.Columns.Column]):
            An array of columns. You can include up to 2
            columns in a card or dialog.
    """

    class Column(proto.Message):
        r"""A column.

        `Google Workspace add-ons and Chat
        apps <https://developers.google.com/workspace/extend>`__

        Attributes:
            horizontal_size_style (google.apps.card_v1.types.Columns.Column.HorizontalSizeStyle):
                Specifies how a column fills the width of the
                card.
            horizontal_alignment (google.apps.card_v1.types.Widget.HorizontalAlignment):
                Specifies whether widgets align to the left,
                right, or center of a column.
            vertical_alignment (google.apps.card_v1.types.Columns.Column.VerticalAlignment):
                Specifies whether widgets align to the top,
                bottom, or center of a column.
            widgets (MutableSequence[google.apps.card_v1.types.Columns.Column.Widgets]):
                An array of widgets included in a column.
                Widgets appear in the order that they are
                specified.
        """

        class HorizontalSizeStyle(proto.Enum):
            r"""Specifies how a column fills the width of the card. The width of
            each column depends on both the ``HorizontalSizeStyle`` and the
            width of the widgets within the column.

            `Google Workspace add-ons and Chat
            apps <https://developers.google.com/workspace/extend>`__

            Values:
                HORIZONTAL_SIZE_STYLE_UNSPECIFIED (0):
                    Don't use. Unspecified.
                FILL_AVAILABLE_SPACE (1):
                    Default value. Column fills the available space, up to 70%
                    of the card's width. If both columns are set to
                    ``FILL_AVAILABLE_SPACE``, each column fills 50% of the
                    space.
                FILL_MINIMUM_SPACE (2):
                    Column fills the least amount of space
                    possible and no more than 30% of the card's
                    width.
            """

            HORIZONTAL_SIZE_STYLE_UNSPECIFIED = 0
            FILL_AVAILABLE_SPACE = 1
            FILL_MINIMUM_SPACE = 2

        class VerticalAlignment(proto.Enum):
            r"""Specifies whether widgets align to the top, bottom, or center of a
            column.

            `Google Workspace add-ons and Chat
            apps <https://developers.google.com/workspace/extend>`__

            Values:
                VERTICAL_ALIGNMENT_UNSPECIFIED (0):
                    Don't use. Unspecified.
                CENTER (1):
                    Default value. Aligns widgets to the center
                    of a column.
                TOP (2):
                    Aligns widgets to the top of a column.
                BOTTOM (3):
                    Aligns widgets to the bottom of a column.
            """

            VERTICAL_ALIGNMENT_UNSPECIFIED = 0
            CENTER = 1
            TOP = 2
            BOTTOM = 3

        class Widgets(proto.Message):
            r"""The supported widgets that you can include in a column.

            `Google Workspace add-ons and Chat
            apps <https://developers.google.com/workspace/extend>`__

            This message has `oneof`_ fields (mutually exclusive fields).
            For each oneof, at most one member field can be set at the same time.
            Setting any member of the oneof automatically clears all other
            members.

            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                text_paragraph (google.apps.card_v1.types.TextParagraph):
                    [TextParagraph][google.apps.card.v1.TextParagraph] widget.

                    This field is a member of `oneof`_ ``data``.
                image (google.apps.card_v1.types.Image):
                    [Image][google.apps.card.v1.Image] widget.

                    This field is a member of `oneof`_ ``data``.
                decorated_text (google.apps.card_v1.types.DecoratedText):
                    [DecoratedText][google.apps.card.v1.DecoratedText] widget.

                    This field is a member of `oneof`_ ``data``.
                button_list (google.apps.card_v1.types.ButtonList):
                    [ButtonList][google.apps.card.v1.ButtonList] widget.

                    This field is a member of `oneof`_ ``data``.
                text_input (google.apps.card_v1.types.TextInput):
                    [TextInput][google.apps.card.v1.TextInput] widget.

                    This field is a member of `oneof`_ ``data``.
                selection_input (google.apps.card_v1.types.SelectionInput):
                    [SelectionInput][google.apps.card.v1.SelectionInput] widget.

                    This field is a member of `oneof`_ ``data``.
                date_time_picker (google.apps.card_v1.types.DateTimePicker):
                    [DateTimePicker][google.apps.card.v1.DateTimePicker] widget.

                    This field is a member of `oneof`_ ``data``.
                chip_list (google.apps.card_v1.types.ChipList):
                    [ChipList][google.apps.card.v1.ChipList] widget.

                    This field is a member of `oneof`_ ``data``.
            """

            text_paragraph: "TextParagraph" = proto.Field(
                proto.MESSAGE,
                number=1,
                oneof="data",
                message="TextParagraph",
            )
            image: "Image" = proto.Field(
                proto.MESSAGE,
                number=2,
                oneof="data",
                message="Image",
            )
            decorated_text: "DecoratedText" = proto.Field(
                proto.MESSAGE,
                number=3,
                oneof="data",
                message="DecoratedText",
            )
            button_list: "ButtonList" = proto.Field(
                proto.MESSAGE,
                number=4,
                oneof="data",
                message="ButtonList",
            )
            text_input: "TextInput" = proto.Field(
                proto.MESSAGE,
                number=5,
                oneof="data",
                message="TextInput",
            )
            selection_input: "SelectionInput" = proto.Field(
                proto.MESSAGE,
                number=6,
                oneof="data",
                message="SelectionInput",
            )
            date_time_picker: "DateTimePicker" = proto.Field(
                proto.MESSAGE,
                number=7,
                oneof="data",
                message="DateTimePicker",
            )
            chip_list: "ChipList" = proto.Field(
                proto.MESSAGE,
                number=8,
                oneof="data",
                message="ChipList",
            )

        horizontal_size_style: "Columns.Column.HorizontalSizeStyle" = proto.Field(
            proto.ENUM,
            number=1,
            enum="Columns.Column.HorizontalSizeStyle",
        )
        horizontal_alignment: "Widget.HorizontalAlignment" = proto.Field(
            proto.ENUM,
            number=2,
            enum="Widget.HorizontalAlignment",
        )
        vertical_alignment: "Columns.Column.VerticalAlignment" = proto.Field(
            proto.ENUM,
            number=3,
            enum="Columns.Column.VerticalAlignment",
        )
        widgets: MutableSequence["Columns.Column.Widgets"] = proto.RepeatedField(
            proto.MESSAGE,
            number=4,
            message="Columns.Column.Widgets",
        )

    column_items: MutableSequence[Column] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=Column,
    )


class Carousel(proto.Message):
    r"""A carousel, also known as a slider, rotates and displays a list of
    widgets in a slideshow format, with buttons navigating to the
    previous or next widget.

    For example, this is a JSON representation of a carousel that
    contains three text paragraph widgets.

    ::

       {
         "carouselCards": [
           {
             "widgets": [
               {
                 "textParagraph": {
                   "text": "First text paragraph in carousel",
                 }
               }
             ]
           },
           {
             "widgets": [
               {
                 "textParagraph": {
                   "text": "Second text paragraph in carousel",
                 }
               }
             ]
           },
           {
             "widgets": [
               {
                 "textParagraph": {
                   "text": "Third text paragraph in carousel",
                 }
               }
             ]
           }
         ]
       }

    `Google Chat apps <https://developers.google.com/workspace/chat>`__:

    Attributes:
        carousel_cards (MutableSequence[google.apps.card_v1.types.Carousel.CarouselCard]):
            A list of cards included in the carousel.
    """

    class CarouselCard(proto.Message):
        r"""A card that can be displayed as a carousel item. `Google Chat
        apps <https://developers.google.com/workspace/chat>`__:

        Attributes:
            widgets (MutableSequence[google.apps.card_v1.types.Card.NestedWidget]):
                A list of widgets displayed in the carousel
                card. The widgets are displayed in the order
                that they are specified.
            footer_widgets (MutableSequence[google.apps.card_v1.types.Card.NestedWidget]):
                A list of widgets displayed at the bottom of
                the carousel card. The widgets are displayed in
                the order that they are specified.
        """

        widgets: MutableSequence["Card.NestedWidget"] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="Card.NestedWidget",
        )
        footer_widgets: MutableSequence["Card.NestedWidget"] = proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="Card.NestedWidget",
        )

    carousel_cards: MutableSequence[CarouselCard] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=CarouselCard,
    )


class CollapseControl(proto.Message):
    r"""Represent an expand and collapse control.

    `Google Workspace add-ons and Chat
    apps <https://developers.google.com/workspace/extend>`__:

    Attributes:
        horizontal_alignment (google.apps.card_v1.types.Widget.HorizontalAlignment):
            The horizontal alignment of the expand and
            collapse button.
        expand_button (google.apps.card_v1.types.Button):
            Optional. Define a customizable button to expand the
            section. Both expand_button and collapse_button field must
            be set. Only one field set will not take into effect. If
            this field isn't set, the default button is used.
        collapse_button (google.apps.card_v1.types.Button):
            Optional. Define a customizable button to collapse the
            section. Both expand_button and collapse_button field must
            be set. Only one field set will not take into effect. If
            this field isn't set, the default button is used.
    """

    horizontal_alignment: "Widget.HorizontalAlignment" = proto.Field(
        proto.ENUM,
        number=1,
        enum="Widget.HorizontalAlignment",
    )
    expand_button: "Button" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Button",
    )
    collapse_button: "Button" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Button",
    )


class OnClick(proto.Message):
    r"""Represents how to respond when users click an interactive element on
    a card, such as a button.

    `Google Workspace add-ons and Chat
    apps <https://developers.google.com/workspace/extend>`__:

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        action (google.apps.card_v1.types.Action):
            If specified, an action is triggered by this ``onClick``.

            This field is a member of `oneof`_ ``data``.
        open_link (google.apps.card_v1.types.OpenLink):
            If specified, this ``onClick`` triggers an open link action.

            This field is a member of `oneof`_ ``data``.
        open_dynamic_link_action (google.apps.card_v1.types.Action):
            An add-on triggers this action when the action needs to open
            a link. This differs from the ``open_link`` above in that
            this needs to talk to server to get the link. Thus some
            preparation work is required for web client to do before the
            open link action response comes back.

            `Google Workspace
            add-ons <https://developers.google.com/workspace/add-ons>`__:

            This field is a member of `oneof`_ ``data``.
        card (google.apps.card_v1.types.Card):
            A new card is pushed to the card stack after clicking if
            specified.

            `Google Workspace
            add-ons <https://developers.google.com/workspace/add-ons>`__:

            This field is a member of `oneof`_ ``data``.
        overflow_menu (google.apps.card_v1.types.OverflowMenu):
            If specified, this ``onClick`` opens an overflow menu.

            This field is a member of `oneof`_ ``data``.
    """

    action: "Action" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="data",
        message="Action",
    )
    open_link: "OpenLink" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="data",
        message="OpenLink",
    )
    open_dynamic_link_action: "Action" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="data",
        message="Action",
    )
    card: "Card" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="data",
        message="Card",
    )
    overflow_menu: "OverflowMenu" = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="data",
        message="OverflowMenu",
    )


class OpenLink(proto.Message):
    r"""Represents an ``onClick`` event that opens a hyperlink.

    `Google Workspace add-ons and Chat
    apps <https://developers.google.com/workspace/extend>`__:

    Attributes:
        url (str):
            The URL to open.
        open_as (google.apps.card_v1.types.OpenLink.OpenAs):
            How to open a link.

            `Google Workspace
            add-ons <https://developers.google.com/workspace/add-ons>`__:
        on_close (google.apps.card_v1.types.OpenLink.OnClose):
            Whether the client forgets about a link after opening it, or
            observes it until the window closes.

            `Google Workspace
            add-ons <https://developers.google.com/workspace/add-ons>`__:
    """

    class OpenAs(proto.Enum):
        r"""When an ``OnClick`` action opens a link, then the client can either
        open it as a full-size window (if that's the frame used by the
        client), or an overlay (such as a pop-up). The implementation
        depends on the client platform capabilities, and the value selected
        might be ignored if the client doesn't support it. ``FULL_SIZE`` is
        supported by all clients.

        `Google Workspace
        add-ons <https://developers.google.com/workspace/add-ons>`__:

        Values:
            FULL_SIZE (0):
                The link opens as a full-size window (if
                that's the frame used by the client).
            OVERLAY (1):
                The link opens as an overlay, such as a
                pop-up.
        """

        FULL_SIZE = 0
        OVERLAY = 1

    class OnClose(proto.Enum):
        r"""What the client does when a link opened by an ``OnClick`` action is
        closed.

        Implementation depends on client platform capabilities. For example,
        a web browser might open a link in a pop-up window with an
        ``OnClose`` handler.

        If both ``OnOpen`` and ``OnClose`` handlers are set, and the client
        platform can't support both values, ``OnClose`` takes precedence.

        `Google Workspace
        add-ons <https://developers.google.com/workspace/add-ons>`__:

        Values:
            NOTHING (0):
                Default value. The card doesn't reload;
                nothing happens.
            RELOAD (1):
                Reloads the card after the child window closes.

                If used in conjunction with
                ```OpenAs.OVERLAY`` <https://developers.google.com/workspace/add-ons/reference/rpc/google.apps.card.v1#openas>`__,
                the child window acts as a modal dialog and the parent card
                is blocked until the child window closes.
        """

        NOTHING = 0
        RELOAD = 1

    url: str = proto.Field(
        proto.STRING,
        number=1,
    )
    open_as: OpenAs = proto.Field(
        proto.ENUM,
        number=2,
        enum=OpenAs,
    )
    on_close: OnClose = proto.Field(
        proto.ENUM,
        number=3,
        enum=OnClose,
    )


class Action(proto.Message):
    r"""An action that describes the behavior when the form is submitted.
    For example, you can invoke an Apps Script script to handle the
    form. If the action is triggered, the form values are sent to the
    server.

    `Google Workspace add-ons and Chat
    apps <https://developers.google.com/workspace/extend>`__:

    Attributes:
        function (str):
            A custom function to invoke when the containing element is
            clicked or otherwise activated.

            For example usage, see `Read form
            data <https://developers.google.com/workspace/chat/read-form-data>`__.
        parameters (MutableSequence[google.apps.card_v1.types.Action.ActionParameter]):
            List of action parameters.
        load_indicator (google.apps.card_v1.types.Action.LoadIndicator):
            Specifies the loading indicator that the
            action displays while making the call to the
            action.
        persist_values (bool):
            Indicates whether form values persist after the action. The
            default value is ``false``.

            If ``true``, form values remain after the action is
            triggered. To let the user make changes while the action is
            being processed, set
            ```LoadIndicator`` <https://developers.google.com/workspace/add-ons/reference/rpc/google.apps.card.v1#loadindicator>`__
            to ``NONE``. For `card
            messages <https://developers.google.com/workspace/chat/api/guides/v1/messages/create#create>`__
            in Chat apps, you must also set the action's
            ```ResponseType`` <https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces.messages#responsetype>`__
            to ``UPDATE_MESSAGE`` and use the same
            ```card_id`` <https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces.messages#CardWithId>`__
            from the card that contained the action.

            If ``false``, the form values are cleared when the action is
            triggered. To prevent the user from making changes while the
            action is being processed, set
            ```LoadIndicator`` <https://developers.google.com/workspace/add-ons/reference/rpc/google.apps.card.v1#loadindicator>`__
            to ``SPINNER``.
        interaction (google.apps.card_v1.types.Action.Interaction):
            Optional. Required when opening a
            `dialog <https://developers.google.com/workspace/chat/dialogs>`__.

            What to do in response to an interaction with a user, such
            as a user clicking a button in a card message.

            If unspecified, the app responds by executing an
            ``action``—like opening a link or running a function—as
            normal.

            By specifying an ``interaction``, the app can respond in
            special interactive ways. For example, by setting
            ``interaction`` to ``OPEN_DIALOG``, the app can open a
            `dialog <https://developers.google.com/workspace/chat/dialogs>`__.
            When specified, a loading indicator isn't shown. If
            specified for an add-on, the entire card is stripped and
            nothing is shown in the client.

            `Google Chat
            apps <https://developers.google.com/workspace/chat>`__:
        required_widgets (MutableSequence[str]):
            Optional. Fill this list with the names of widgets that this
            Action needs for a valid submission.

            If the widgets listed here don't have a value when this
            Action is invoked, the form submission is aborted.

            `Google Workspace add-ons and Chat
            apps <https://developers.google.com/workspace/extend>`__:
        all_widgets_are_required (bool):
            Optional. If this is true, then all widgets are considered
            required by this action.

            `Google Workspace add-ons and Chat
            apps <https://developers.google.com/workspace/extend>`__:
    """

    class LoadIndicator(proto.Enum):
        r"""Specifies the loading indicator that the action displays while
        making the call to the action.

        `Google Workspace add-ons and Chat
        apps <https://developers.google.com/workspace/extend>`__:

        Values:
            SPINNER (0):
                Displays a spinner to indicate that content
                is loading.
            NONE (1):
                Nothing is displayed.
        """

        SPINNER = 0
        NONE = 1

    class Interaction(proto.Enum):
        r"""Optional. Required when opening a
        `dialog <https://developers.google.com/workspace/chat/dialogs>`__.

        What to do in response to an interaction with a user, such as a user
        clicking a button in a card message.

        If unspecified, the app responds by executing an ``action``—like
        opening a link or running a function—as normal.

        By specifying an ``interaction``, the app can respond in special
        interactive ways. For example, by setting ``interaction`` to
        ``OPEN_DIALOG``, the app can open a
        `dialog <https://developers.google.com/workspace/chat/dialogs>`__.

        When specified, a loading indicator isn't shown. If specified for an
        add-on, the entire card is stripped and nothing is shown in the
        client.

        `Google Chat apps <https://developers.google.com/workspace/chat>`__:

        Values:
            INTERACTION_UNSPECIFIED (0):
                Default value. The ``action`` executes as normal.
            OPEN_DIALOG (1):
                Opens a
                `dialog <https://developers.google.com/workspace/chat/dialogs>`__,
                a windowed, card-based interface that Chat apps use to
                interact with users.

                Only supported by Chat apps in response to button-clicks on
                card messages. If specified for an add-on, the entire card
                is stripped and nothing is shown in the client.

                `Google Chat
                apps <https://developers.google.com/workspace/chat>`__:
        """

        INTERACTION_UNSPECIFIED = 0
        OPEN_DIALOG = 1

    class ActionParameter(proto.Message):
        r"""List of string parameters to supply when the action method is
        invoked. For example, consider three snooze buttons: snooze now,
        snooze one day, or snooze next week. You might use
        ``action method = snooze()``, passing the snooze type and snooze
        time in the list of string parameters.

        To learn more, see
        ```CommonEventObject`` <https://developers.google.com/workspace/chat/api/reference/rest/v1/Event#commoneventobject>`__.

        `Google Workspace add-ons and Chat
        apps <https://developers.google.com/workspace/extend>`__:

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

    function: str = proto.Field(
        proto.STRING,
        number=1,
    )
    parameters: MutableSequence[ActionParameter] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=ActionParameter,
    )
    load_indicator: LoadIndicator = proto.Field(
        proto.ENUM,
        number=3,
        enum=LoadIndicator,
    )
    persist_values: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    interaction: Interaction = proto.Field(
        proto.ENUM,
        number=5,
        enum=Interaction,
    )
    required_widgets: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )
    all_widgets_are_required: bool = proto.Field(
        proto.BOOL,
        number=7,
    )


class Validation(proto.Message):
    r"""Represents the necessary data for validating the widget it's
    attached to.

    `Google Workspace add-ons and Chat
    apps <https://developers.google.com/workspace/extend>`__:

    Attributes:
        character_limit (int):
            Specify the character limit for text input widgets. Note
            that this is only used for text input and is ignored for
            other widgets.

            `Google Workspace add-ons and Chat
            apps <https://developers.google.com/workspace/extend>`__:
        input_type (google.apps.card_v1.types.Validation.InputType):
            Specify the type of the input widgets.

            `Google Workspace add-ons and Chat
            apps <https://developers.google.com/workspace/extend>`__:
    """

    class InputType(proto.Enum):
        r"""The type of the input widget.

        Values:
            INPUT_TYPE_UNSPECIFIED (0):
                Unspecified type. Do not use.
            TEXT (1):
                Regular text that accepts all characters.
            INTEGER (2):
                An integer value.
            FLOAT (3):
                A float value.
            EMAIL (4):
                An email address.
            EMOJI_PICKER (5):
                A emoji selected from system-provided emoji
                picker.
        """

        INPUT_TYPE_UNSPECIFIED = 0
        TEXT = 1
        INTEGER = 2
        FLOAT = 3
        EMAIL = 4
        EMOJI_PICKER = 5

    character_limit: int = proto.Field(
        proto.INT32,
        number=1,
    )
    input_type: InputType = proto.Field(
        proto.ENUM,
        number=2,
        enum=InputType,
    )


class ChipList(proto.Message):
    r"""A list of chips layed out horizontally, which can either scroll
    horizontally or wrap to the next line.

    `Google Workspace add-ons and Chat
    apps <https://developers.google.com/workspace/extend>`__:

    Attributes:
        layout (google.apps.card_v1.types.ChipList.Layout):
            Specified chip list layout.
        chips (MutableSequence[google.apps.card_v1.types.Chip]):
            An array of chips.
    """

    class Layout(proto.Enum):
        r"""The chip list layout.

        Values:
            LAYOUT_UNSPECIFIED (0):
                Don't use. Unspecified.
            WRAPPED (1):
                Default value. The chip list wraps to the
                next line if there isn't enough horizontal
                space.
            HORIZONTAL_SCROLLABLE (2):
                The chips scroll horizontally if they don't
                fit in the available space.
        """

        LAYOUT_UNSPECIFIED = 0
        WRAPPED = 1
        HORIZONTAL_SCROLLABLE = 2

    layout: Layout = proto.Field(
        proto.ENUM,
        number=1,
        enum=Layout,
    )
    chips: MutableSequence["Chip"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="Chip",
    )


class Chip(proto.Message):
    r"""A text, icon, or text and icon chip that users can click.

    `Google Workspace add-ons and Chat
    apps <https://developers.google.com/workspace/extend>`__:

    Attributes:
        icon (google.apps.card_v1.types.Icon):
            The icon image. If both ``icon`` and ``text`` are set, then
            the icon appears before the text.
        label (str):
            The text displayed inside the chip.
        on_click (google.apps.card_v1.types.OnClick):
            Optional. The action to perform when a user
            clicks the chip, such as opening a hyperlink or
            running a custom function.
        enabled (bool):
            Whether the chip is in an active state and responds to user
            actions. Defaults to ``true``. Deprecated. Use ``disabled``
            instead.
        disabled (bool):
            Whether the chip is in an inactive state and ignores user
            actions. Defaults to ``false``.
        alt_text (str):
            The alternative text that's used for
            accessibility.
            Set descriptive text that lets users know what
            the chip does. For example, if a chip opens a
            hyperlink, write: "Opens a new browser tab and
            navigates to the Google Chat developer
            documentation at
            https://developers.google.com/workspace/chat".
    """

    icon: "Icon" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Icon",
    )
    label: str = proto.Field(
        proto.STRING,
        number=2,
    )
    on_click: "OnClick" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="OnClick",
    )
    enabled: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    disabled: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    alt_text: str = proto.Field(
        proto.STRING,
        number=5,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
