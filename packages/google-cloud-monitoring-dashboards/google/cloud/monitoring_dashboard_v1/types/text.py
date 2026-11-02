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
    package="google.monitoring.dashboard.v1",
    manifest={
        "Text",
    },
)


class Text(proto.Message):
    r"""A widget that displays textual content.

    Attributes:
        content (str):
            The text content to be displayed.
        format_ (google.cloud.monitoring_dashboard_v1.types.Text.Format):
            How the text content is formatted.
        style (google.cloud.monitoring_dashboard_v1.types.Text.TextStyle):
            How the text is styled
    """

    class Format(proto.Enum):
        r"""The format type of the text content.

        Values:
            FORMAT_UNSPECIFIED (0):
                Format is unspecified. Defaults to MARKDOWN.
            MARKDOWN (1):
                The text contains Markdown formatting.
            RAW (2):
                The text contains no special formatting.
        """

        FORMAT_UNSPECIFIED = 0
        MARKDOWN = 1
        RAW = 2

    class TextStyle(proto.Message):
        r"""Properties that determine how the title and content are
        styled

        Attributes:
            background_color (str):
                The background color as a hex string.
                "#RRGGBB" or "#RGB".
            text_color (str):
                The text color as a hex string. "#RRGGBB" or
                "#RGB".
            horizontal_alignment (google.cloud.monitoring_dashboard_v1.types.Text.TextStyle.HorizontalAlignment):
                The horizontal alignment of both the title
                and content
            vertical_alignment (google.cloud.monitoring_dashboard_v1.types.Text.TextStyle.VerticalAlignment):
                The vertical alignment of both the title and
                content
            padding (google.cloud.monitoring_dashboard_v1.types.Text.TextStyle.PaddingSize):
                The amount of padding around the widget
            font_size (google.cloud.monitoring_dashboard_v1.types.Text.TextStyle.FontSize):
                Font sizes for both the title and content.
                The title will still be larger relative to the
                content.
            pointer_location (google.cloud.monitoring_dashboard_v1.types.Text.TextStyle.PointerLocation):
                The pointer location for this widget (also
                sometimes called a "tail")
        """

        class HorizontalAlignment(proto.Enum):
            r"""The horizontal alignment of both the title and content on a
            text widget

            Values:
                HORIZONTAL_ALIGNMENT_UNSPECIFIED (0):
                    No horizontal alignment specified, will default to H_LEFT
                H_LEFT (1):
                    Left-align
                H_CENTER (2):
                    Center-align
                H_RIGHT (3):
                    Right-align
            """

            HORIZONTAL_ALIGNMENT_UNSPECIFIED = 0
            H_LEFT = 1
            H_CENTER = 2
            H_RIGHT = 3

        class VerticalAlignment(proto.Enum):
            r"""The vertical alignment of both the title and content on a
            text widget

            Values:
                VERTICAL_ALIGNMENT_UNSPECIFIED (0):
                    No vertical alignment specified, will default to V_TOP
                V_TOP (1):
                    Top-align
                V_CENTER (2):
                    Center-align
                V_BOTTOM (3):
                    Bottom-align
            """

            VERTICAL_ALIGNMENT_UNSPECIFIED = 0
            V_TOP = 1
            V_CENTER = 2
            V_BOTTOM = 3

        class PaddingSize(proto.Enum):
            r"""Specifies padding size around a text widget

            Values:
                PADDING_SIZE_UNSPECIFIED (0):
                    No padding size specified, will default to P_EXTRA_SMALL
                P_EXTRA_SMALL (1):
                    Extra small padding
                P_SMALL (2):
                    Small padding
                P_MEDIUM (3):
                    Medium padding
                P_LARGE (4):
                    Large padding
                P_EXTRA_LARGE (5):
                    Extra large padding
            """

            PADDING_SIZE_UNSPECIFIED = 0
            P_EXTRA_SMALL = 1
            P_SMALL = 2
            P_MEDIUM = 3
            P_LARGE = 4
            P_EXTRA_LARGE = 5

        class FontSize(proto.Enum):
            r"""Specifies a font size for the title and content of a text
            widget

            Values:
                FONT_SIZE_UNSPECIFIED (0):
                    No font size specified, will default to FS_LARGE
                FS_EXTRA_SMALL (1):
                    Extra small font size
                FS_SMALL (2):
                    Small font size
                FS_MEDIUM (3):
                    Medium font size
                FS_LARGE (4):
                    Large font size
                FS_EXTRA_LARGE (5):
                    Extra large font size
            """

            FONT_SIZE_UNSPECIFIED = 0
            FS_EXTRA_SMALL = 1
            FS_SMALL = 2
            FS_MEDIUM = 3
            FS_LARGE = 4
            FS_EXTRA_LARGE = 5

        class PointerLocation(proto.Enum):
            r"""Specifies where a visual pointer is placed on a text widget
            (also sometimes called a "tail")

            Values:
                POINTER_LOCATION_UNSPECIFIED (0):
                    No visual pointer
                PL_TOP (1):
                    Placed in the middle of the top of the widget
                PL_RIGHT (2):
                    Placed in the middle of the right side of the
                    widget
                PL_BOTTOM (3):
                    Placed in the middle of the bottom of the
                    widget
                PL_LEFT (4):
                    Placed in the middle of the left side of the
                    widget
                PL_TOP_LEFT (5):
                    Placed on the left side of the top of the
                    widget
                PL_TOP_RIGHT (6):
                    Placed on the right side of the top of the
                    widget
                PL_RIGHT_TOP (7):
                    Placed on the top of the right side of the
                    widget
                PL_RIGHT_BOTTOM (8):
                    Placed on the bottom of the right side of the
                    widget
                PL_BOTTOM_RIGHT (9):
                    Placed on the right side of the bottom of the
                    widget
                PL_BOTTOM_LEFT (10):
                    Placed on the left side of the bottom of the
                    widget
                PL_LEFT_BOTTOM (11):
                    Placed on the bottom of the left side of the
                    widget
                PL_LEFT_TOP (12):
                    Placed on the top of the left side of the
                    widget
            """

            POINTER_LOCATION_UNSPECIFIED = 0
            PL_TOP = 1
            PL_RIGHT = 2
            PL_BOTTOM = 3
            PL_LEFT = 4
            PL_TOP_LEFT = 5
            PL_TOP_RIGHT = 6
            PL_RIGHT_TOP = 7
            PL_RIGHT_BOTTOM = 8
            PL_BOTTOM_RIGHT = 9
            PL_BOTTOM_LEFT = 10
            PL_LEFT_BOTTOM = 11
            PL_LEFT_TOP = 12

        background_color: str = proto.Field(
            proto.STRING,
            number=1,
        )
        text_color: str = proto.Field(
            proto.STRING,
            number=2,
        )
        horizontal_alignment: "Text.TextStyle.HorizontalAlignment" = proto.Field(
            proto.ENUM,
            number=3,
            enum="Text.TextStyle.HorizontalAlignment",
        )
        vertical_alignment: "Text.TextStyle.VerticalAlignment" = proto.Field(
            proto.ENUM,
            number=4,
            enum="Text.TextStyle.VerticalAlignment",
        )
        padding: "Text.TextStyle.PaddingSize" = proto.Field(
            proto.ENUM,
            number=5,
            enum="Text.TextStyle.PaddingSize",
        )
        font_size: "Text.TextStyle.FontSize" = proto.Field(
            proto.ENUM,
            number=6,
            enum="Text.TextStyle.FontSize",
        )
        pointer_location: "Text.TextStyle.PointerLocation" = proto.Field(
            proto.ENUM,
            number=7,
            enum="Text.TextStyle.PointerLocation",
        )

    content: str = proto.Field(
        proto.STRING,
        number=1,
    )
    format_: Format = proto.Field(
        proto.ENUM,
        number=2,
        enum=Format,
    )
    style: TextStyle = proto.Field(
        proto.MESSAGE,
        number=3,
        message=TextStyle,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
