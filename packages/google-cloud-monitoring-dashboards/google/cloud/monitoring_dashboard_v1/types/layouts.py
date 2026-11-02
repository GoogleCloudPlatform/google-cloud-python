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

from google.cloud.monitoring_dashboard_v1.types import widget as gmd_widget

__protobuf__ = proto.module(
    package="google.monitoring.dashboard.v1",
    manifest={
        "GridLayout",
        "MosaicLayout",
        "RowLayout",
        "ColumnLayout",
    },
)


class GridLayout(proto.Message):
    r"""A basic layout divides the available space into vertical
    columns of equal width and arranges a list of widgets using a
    row-first strategy.

    Attributes:
        columns (int):
            The number of columns into which the view's
            width is divided. If omitted or set to zero, a
            system default will be used while rendering.
        widgets (MutableSequence[google.cloud.monitoring_dashboard_v1.types.Widget]):
            The informational elements that are arranged
            into the columns row-first.
    """

    columns: int = proto.Field(
        proto.INT64,
        number=1,
    )
    widgets: MutableSequence[gmd_widget.Widget] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=gmd_widget.Widget,
    )


class MosaicLayout(proto.Message):
    r"""A mosaic layout divides the available space into a grid of blocks,
    and overlays the grid with tiles. Unlike ``GridLayout``, tiles may
    span multiple grid blocks and can be placed at arbitrary locations
    in the grid.

    Attributes:
        columns (int):
            The number of columns in the mosaic grid. The
            number of columns must be between 1 and 12,
            inclusive.
        tiles (MutableSequence[google.cloud.monitoring_dashboard_v1.types.MosaicLayout.Tile]):
            The tiles to display.
    """

    class Tile(proto.Message):
        r"""A single tile in the mosaic. The placement and size of the
        tile are configurable.

        Attributes:
            x_pos (int):
                The zero-indexed position of the tile in grid blocks
                relative to the left edge of the grid. Tiles must be
                contained within the specified number of columns. ``x_pos``
                cannot be negative.
            y_pos (int):
                The zero-indexed position of the tile in grid blocks
                relative to the top edge of the grid. ``y_pos`` cannot be
                negative.
            width (int):
                The width of the tile, measured in grid
                blocks. Tiles must have a minimum width of 1.
            height (int):
                The height of the tile, measured in grid
                blocks. Tiles must have a minimum height of 1.
            widget (google.cloud.monitoring_dashboard_v1.types.Widget):
                The informational widget contained in the tile. For example
                an ``XyChart``.
        """

        x_pos: int = proto.Field(
            proto.INT32,
            number=1,
        )
        y_pos: int = proto.Field(
            proto.INT32,
            number=2,
        )
        width: int = proto.Field(
            proto.INT32,
            number=3,
        )
        height: int = proto.Field(
            proto.INT32,
            number=4,
        )
        widget: gmd_widget.Widget = proto.Field(
            proto.MESSAGE,
            number=5,
            message=gmd_widget.Widget,
        )

    columns: int = proto.Field(
        proto.INT32,
        number=1,
    )
    tiles: MutableSequence[Tile] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=Tile,
    )


class RowLayout(proto.Message):
    r"""A simplified layout that divides the available space into
    rows and arranges a set of widgets horizontally in each row.

    Attributes:
        rows (MutableSequence[google.cloud.monitoring_dashboard_v1.types.RowLayout.Row]):
            The rows of content to display.
    """

    class Row(proto.Message):
        r"""Defines the layout properties and content for a row.

        Attributes:
            weight (int):
                The relative weight of this row. The row
                weight is used to adjust the height of rows on
                the screen (relative to peers). Greater the
                weight, greater the height of the row on the
                screen. If omitted, a value of 1 is used while
                rendering.
            widgets (MutableSequence[google.cloud.monitoring_dashboard_v1.types.Widget]):
                The display widgets arranged horizontally in
                this row.
        """

        weight: int = proto.Field(
            proto.INT64,
            number=1,
        )
        widgets: MutableSequence[gmd_widget.Widget] = proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message=gmd_widget.Widget,
        )

    rows: MutableSequence[Row] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=Row,
    )


class ColumnLayout(proto.Message):
    r"""A simplified layout that divides the available space into
    vertical columns and arranges a set of widgets vertically in
    each column.

    Attributes:
        columns (MutableSequence[google.cloud.monitoring_dashboard_v1.types.ColumnLayout.Column]):
            The columns of content to display.
    """

    class Column(proto.Message):
        r"""Defines the layout properties and content for a column.

        Attributes:
            weight (int):
                The relative weight of this column. The
                column weight is used to adjust the width of
                columns on the screen (relative to peers).
                Greater the weight, greater the width of the
                column on the screen. If omitted, a value of 1
                is used while rendering.
            widgets (MutableSequence[google.cloud.monitoring_dashboard_v1.types.Widget]):
                The display widgets arranged vertically in
                this column.
        """

        weight: int = proto.Field(
            proto.INT64,
            number=1,
        )
        widgets: MutableSequence[gmd_widget.Widget] = proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message=gmd_widget.Widget,
        )

    columns: MutableSequence[Column] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=Column,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
