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

from google.cloud.chronicle_v1.types import dashboard_query as gcc_dashboard_query

__protobuf__ = proto.module(
    package="google.cloud.chronicle.v1",
    manifest={
        "TileType",
        "RenderType",
        "AxisType",
        "SeriesType",
        "SeriesStackStrategy",
        "ToolTipTrigger",
        "LegendOrient",
        "LegendAlign",
        "ButtonStyle",
        "PlotMode",
        "PointSizeType",
        "MetricFormat",
        "MetricDisplayTrend",
        "MetricTrendType",
        "VisualMapType",
        "DashboardChart",
        "Button",
        "Markdown",
        "GetDashboardChartRequest",
        "BatchGetDashboardChartsRequest",
        "BatchGetDashboardChartsResponse",
    },
)


class TileType(proto.Enum):
    r"""TileType indicates what type of chart tile it is i.e.,
    visualization chart, button or text.

    Values:
        TILE_TYPE_UNSPECIFIED (0):
            Defaults to VISUALIZATION.
        TILE_TYPE_VISUALIZATION (1):
            Visualization i.e., bar charts, pie charts
            etc.
        TILE_TYPE_BUTTON (2):
            Button with hyperlink.
        TILE_TYPE_MARKDOWN (3):
            Markdown tile.
    """

    TILE_TYPE_UNSPECIFIED = 0
    TILE_TYPE_VISUALIZATION = 1
    TILE_TYPE_BUTTON = 2
    TILE_TYPE_MARKDOWN = 3


class RenderType(proto.Enum):
    r"""Render type of the data in the chart.

    Values:
        RENDER_TYPE_UNSPECIFIED (0):
            Defaults to Unspecified.
        RENDER_TYPE_TEXT (1):
            Text render type.
        RENDER_TYPE_ICON (2):
            Icon render type.
        RENDER_TYPE_ICON_AND_TEXT (3):
            Icon and text render type.
    """

    RENDER_TYPE_UNSPECIFIED = 0
    RENDER_TYPE_TEXT = 1
    RENDER_TYPE_ICON = 2
    RENDER_TYPE_ICON_AND_TEXT = 3


class AxisType(proto.Enum):
    r"""

    Values:
        AXIS_TYPE_UNSPECIFIED (0):
            No description available.
        VALUE (1):
            No description available.
        CATEGORY (2):
            No description available.
        TIME (3):
            No description available.
        LOG (4):
            No description available.
    """

    AXIS_TYPE_UNSPECIFIED = 0
    VALUE = 1
    CATEGORY = 2
    TIME = 3
    LOG = 4


class SeriesType(proto.Enum):
    r"""

    Values:
        SERIES_TYPE_UNSPECIFIED (0):
            No description available.
        LINE (1):
            No description available.
        BAR (2):
            No description available.
        PIE (3):
            No description available.
        TEXT (4):
            No description available.
        MAP (5):
            Represents map chart type.
        GAUGE (6):
            Represents gauge chart type.
        SCATTERPLOT (7):
            Represents scatterplot chart type.
    """

    SERIES_TYPE_UNSPECIFIED = 0
    LINE = 1
    BAR = 2
    PIE = 3
    TEXT = 4
    MAP = 5
    GAUGE = 6
    SCATTERPLOT = 7


class SeriesStackStrategy(proto.Enum):
    r"""

    Values:
        SERIES_STACK_STRATEGY_UNSPECIFIED (0):
            No description available.
        SAMESIGN (1):
            No description available.
        ALL (2):
            No description available.
        POSITIVE (3):
            No description available.
        NEGATIVE (4):
            No description available.
    """

    SERIES_STACK_STRATEGY_UNSPECIFIED = 0
    SAMESIGN = 1
    ALL = 2
    POSITIVE = 3
    NEGATIVE = 4


class ToolTipTrigger(proto.Enum):
    r"""

    Values:
        TOOLTIP_TRIGGER_UNSPECIFIED (0):
            No description available.
        TOOLTIP_TRIGGER_NONE (1):
            No description available.
        TOOLTIP_TRIGGER_ITEM (2):
            No description available.
        TOOLTIP_TRIGGER_AXIS (3):
            No description available.
    """

    TOOLTIP_TRIGGER_UNSPECIFIED = 0
    TOOLTIP_TRIGGER_NONE = 1
    TOOLTIP_TRIGGER_ITEM = 2
    TOOLTIP_TRIGGER_AXIS = 3


class LegendOrient(proto.Enum):
    r"""

    Values:
        LEGEND_ORIENT_UNSPECIFIED (0):
            No description available.
        VERTICAL (1):
            No description available.
        HORIZONTAL (2):
            No description available.
    """

    LEGEND_ORIENT_UNSPECIFIED = 0
    VERTICAL = 1
    HORIZONTAL = 2


class LegendAlign(proto.Enum):
    r"""

    Values:
        LEGEND_ALIGN_UNSPECIFIED (0):
            No description available.
        AUTO (1):
            No description available.
        LEFT (2):
            No description available.
        RIGHT (3):
            No description available.
    """

    LEGEND_ALIGN_UNSPECIFIED = 0
    AUTO = 1
    LEFT = 2
    RIGHT = 3


class ButtonStyle(proto.Enum):
    r"""

    Values:
        BUTTON_STYLE_UNSPECIFIED (0):
            No description available.
        BUTTON_STYLE_FILLED (1):
            No description available.
        BUTTON_STYLE_OUTLINED (2):
            No description available.
        BUTTON_STYLE_TRANSPARENT (3):
            No description available.
    """

    BUTTON_STYLE_UNSPECIFIED = 0
    BUTTON_STYLE_FILLED = 1
    BUTTON_STYLE_OUTLINED = 2
    BUTTON_STYLE_TRANSPARENT = 3


class PlotMode(proto.Enum):
    r"""Plot mode for the map.

    Values:
        PLOT_MODE_UNSPECIFIED (0):
            Plot mode is not specified.
        PLOT_MODE_POINTS (1):
            Plot mode is points.
        PLOT_MODE_HEATMAP (2):
            Plot mode is heatmap.
        PLOT_MODE_BOTH (3):
            Plot mode is both points and heatmap.
    """

    PLOT_MODE_UNSPECIFIED = 0
    PLOT_MODE_POINTS = 1
    PLOT_MODE_HEATMAP = 2
    PLOT_MODE_BOTH = 3


class PointSizeType(proto.Enum):
    r"""Point size type for the map.

    Values:
        POINT_SIZE_TYPE_UNSPECIFIED (0):
            Point size is not specified.
        POINT_SIZE_TYPE_FIXED (1):
            Point size is fixed.
        POINT_SIZE_TYPE_PROPORTIONAL_TO_SIZE (2):
            Point size is proportional to the size of the
            data point.
    """

    POINT_SIZE_TYPE_UNSPECIFIED = 0
    POINT_SIZE_TYPE_FIXED = 1
    POINT_SIZE_TYPE_PROPORTIONAL_TO_SIZE = 2


class MetricFormat(proto.Enum):
    r"""Metric format to be displayed for the metric charts.

    Values:
        METRIC_FORMAT_UNSPECIFIED (0):
            Metric format is not specified.
        METRIC_FORMAT_NUMBER (1):
            Metric format in number
        METRIC_FORMAT_PLAIN_TEXT (2):
            Metric format in plain text
    """

    METRIC_FORMAT_UNSPECIFIED = 0
    METRIC_FORMAT_NUMBER = 1
    METRIC_FORMAT_PLAIN_TEXT = 2


class MetricDisplayTrend(proto.Enum):
    r"""Trend to be displayed for the metric charts as.

    Values:
        METRIC_DISPLAY_TREND_UNSPECIFIED (0):
            Trend is not specified.
        METRIC_DISPLAY_TREND_ABSOLUTE_VALUE (2):
            Trend data in absolute value
        METRIC_DISPLAY_TREND_PERCENTAGE (3):
            Trend data in percentage
        METRIC_DISPLAY_TREND_ABSOLUTE_VALUE_AND_PERCENTAGE (4):
            Trend data in both absolute value and
            percentage
    """

    METRIC_DISPLAY_TREND_UNSPECIFIED = 0
    METRIC_DISPLAY_TREND_ABSOLUTE_VALUE = 2
    METRIC_DISPLAY_TREND_PERCENTAGE = 3
    METRIC_DISPLAY_TREND_ABSOLUTE_VALUE_AND_PERCENTAGE = 4


class MetricTrendType(proto.Enum):
    r"""Trend to be displayed for the metric charts as.

    Values:
        METRIC_TREND_TYPE_UNSPECIFIED (0):
            Trend type is not specified.
        METRIC_TREND_TYPE_REGULAR (1):
            The trend type is regular(green for positive
            delta)
        METRIC_TREND_TYPE_INVERSE (2):
            The trend type is inverse(red for positive
            delta)
    """

    METRIC_TREND_TYPE_UNSPECIFIED = 0
    METRIC_TREND_TYPE_REGULAR = 1
    METRIC_TREND_TYPE_INVERSE = 2


class VisualMapType(proto.Enum):
    r"""Visual map for various charts. More info:

    https://echarts.apache.org/en/option.html#visualMap

    Values:
        VISUAL_MAP_TYPE_UNSPECIFIED (0):
            Visual map type is not specified
        CONTINUOUS (1):
            Continuous visual map
        PIECEWISE (2):
            Piecewise visual map
    """

    VISUAL_MAP_TYPE_UNSPECIFIED = 0
    CONTINUOUS = 1
    PIECEWISE = 2


class DashboardChart(proto.Message):
    r"""DashboardChart resource.

    Attributes:
        name (str):
            Output only. Name of the dashboardChart.
        display_name (str):
            Required. Display name/Title of the
            dashboardChart visible to users.
        description (str):
            Optional. Description of the dashboardChart.
        native_dashboard (str):
            Output only. NativeDashboard this chart
            belongs to.
        tile_type (google.cloud.chronicle_v1.types.TileType):
            Optional. Type of tile i.e., visualization,
            button or text.
        chart_datasource (google.cloud.chronicle_v1.types.DashboardChart.ChartDatasource):
            Optional. Query and datasource used in the
            chart. Should be empty for Button Tiles.
        visualization (google.cloud.chronicle_v1.types.DashboardChart.Visualization):
            Required. Depending on tile_type one of below fields will be
            required.
        etag (str):
            Optional. This checksum is computed by the
            server based on the value of other fields, and
            may be sent on update and delete requests to
            ensure the client has an up-to-date value before
            proceeding.
        drill_down_config (google.cloud.chronicle_v1.types.DashboardChart.DrillDownConfig):
            Optional. Drill down configuration.
        tokens (MutableSequence[str]):
            Optional. List of Advanced Filter tokens used
            in this chart's query (e.g., "hostname", "ip").
            This allows the UI to identify dependencies
            without parsing the query text. The tokens are
            stored without the wrapping '$' characters.
            The number of tokens are not expected to be more
            than 10.
    """

    class ChartDatasource(proto.Message):
        r"""Datasource of the chart including the query reference and
        source name.

        Attributes:
            dashboard_query (str):
                Reference to dashboard query resource used in
                the chart.
            data_sources (MutableSequence[google.cloud.chronicle_v1.types.DataSource]):
                Name of the datasource used in the chart.
        """

        dashboard_query: str = proto.Field(
            proto.STRING,
            number=1,
        )
        data_sources: MutableSequence[gcc_dashboard_query.DataSource] = (
            proto.RepeatedField(
                proto.ENUM,
                number=3,
                enum=gcc_dashboard_query.DataSource,
            )
        )

    class Visualization(proto.Message):
        r"""Visualization config for a chart.
        https://echarts.apache.org/en/option.html#series

        Attributes:
            x_axes (MutableSequence[google.cloud.chronicle_v1.types.DashboardChart.Visualization.Axis]):

            y_axes (MutableSequence[google.cloud.chronicle_v1.types.DashboardChart.Visualization.Axis]):

            series (MutableSequence[google.cloud.chronicle_v1.types.DashboardChart.Visualization.Series]):

            tooltip (google.cloud.chronicle_v1.types.DashboardChart.Visualization.Tooltip):

            legends (MutableSequence[google.cloud.chronicle_v1.types.DashboardChart.Visualization.Legend]):

            column_defs (MutableSequence[google.cloud.chronicle_v1.types.DashboardChart.Visualization.ColumnDef]):
                Column Definition to represent chart as a
                table.
            table_config (google.cloud.chronicle_v1.types.DashboardChart.Visualization.TableConfig):
                Optional. Configuration for table appearance.
            button (google.cloud.chronicle_v1.types.Button):
                Button config for a chart if tileType is TILE_TYPE_BUTTON.
            markdown (google.cloud.chronicle_v1.types.Markdown):
                Optional. Markdown config for a chart if tileType is
                TILE_TYPE_MARKDOWN.
            series_column (MutableSequence[str]):
                Optional. Selected column for series
            grouping_type (str):
                Optional. Selected grouping type for series
            google_maps_config (google.cloud.chronicle_v1.types.DashboardChart.Visualization.GoogleMapsConfig):
                Optional. Google Maps config for a chart if
                type is GOOGLE MAPS.
            threshold_coloring_enabled (bool):
                Optional. Whether threshold coloring is
                enabled for the chart. If it's enabled, the
                chart will be colored based on the values stored
                in VisualMap below.
            visual_maps (MutableSequence[google.cloud.chronicle_v1.types.DashboardChart.Visualization.VisualMap]):
                Optional. Visual maps for the chart.
        """

        class Axis(proto.Message):
            r"""

            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                axis_type (google.cloud.chronicle_v1.types.AxisType):

                display_name (str):

                min_ (int):
                    Minimum value to be rendered in ECharts as
                    per
                    https://echarts.apache.org/en/option.html#xAxis.min

                    This field is a member of `oneof`_ ``_min``.
                max_ (int):
                    Maximum value to be rendered in ECharts as
                    per
                    https://echarts.apache.org/en/option.html#xAxis.max

                    This field is a member of `oneof`_ ``_max``.
            """

            axis_type: "AxisType" = proto.Field(
                proto.ENUM,
                number=4,
                enum="AxisType",
            )
            display_name: str = proto.Field(
                proto.STRING,
                number=5,
            )
            min_: int = proto.Field(
                proto.INT32,
                number=6,
                optional=True,
            )
            max_: int = proto.Field(
                proto.INT32,
                number=7,
                optional=True,
            )

        class Series(proto.Message):
            r"""

            Attributes:
                series_type (google.cloud.chronicle_v1.types.SeriesType):

                series_name (str):
                    user specified series label
                show_symbol (bool):

                show_background (bool):

                stack (str):

                series_stack_strategy (google.cloud.chronicle_v1.types.SeriesStackStrategy):

                encode (google.cloud.chronicle_v1.types.DashboardChart.Visualization.Series.Encode):

                label (str):

                field (str):

                data_label (google.cloud.chronicle_v1.types.DashboardChart.Visualization.Series.DataLabel):
                    Optional. Data label config for a series.
                    Displays data vaule in the chart
                radius (MutableSequence[str]):
                    Optional. Used to make a pie chart into a
                    douhnut chart
                item_style (google.cloud.chronicle_v1.types.DashboardChart.Visualization.Series.ItemStyle):
                    Optional. Custom styling for chart
                series_unique_value (str):
                    Optional. Series unique value from the query
                    result
                area_style (google.cloud.chronicle_v1.types.DashboardChart.Visualization.Series.AreaStyle):
                    Optional. Custom styling for area chart
                item_colors (google.cloud.chronicle_v1.types.DashboardChart.Visualization.Series.ItemColors):
                    Optional. Field to be saved for retrieving
                    slice colors for the chart
                gauge_config (google.cloud.chronicle_v1.types.DashboardChart.Visualization.Series.GaugeConfig):
                    Optional. Field to be saved for retrieving
                    gauge config for gauge chart
                metric_trend_config (google.cloud.chronicle_v1.types.DashboardChart.Visualization.Series.MetricTrendConfig):
                    Optional. Fields to capture trend config for
                    metric charts
            """

            class Encode(proto.Message):
                r"""

                Attributes:
                    x (str):

                    y (str):

                    value (str):
                        For some type of series that are not in any
                        coordinate system, like 'pie'
                    item_name (str):
                        This is useful in charts like 'pie', where
                        data item name can be displayed in legend.
                """

                x: str = proto.Field(
                    proto.STRING,
                    number=1,
                )
                y: str = proto.Field(
                    proto.STRING,
                    number=2,
                )
                value: str = proto.Field(
                    proto.STRING,
                    number=3,
                )
                item_name: str = proto.Field(
                    proto.STRING,
                    number=4,
                )

            class DataLabel(proto.Message):
                r"""Data label config for a series.

                Attributes:
                    show (bool):
                        Optional. Whether to show data label.
                """

                show: bool = proto.Field(
                    proto.BOOL,
                    number=1,
                )

            class ItemStyle(proto.Message):
                r"""Custom styling for chart

                Attributes:
                    border_width (int):
                        Optional. Used to add border width
                    border_color (str):
                        Optional. Used to add border color
                    color (str):
                        Optional. Used to add color
                """

                border_width: int = proto.Field(
                    proto.INT32,
                    number=1,
                )
                border_color: str = proto.Field(
                    proto.STRING,
                    number=2,
                )
                color: str = proto.Field(
                    proto.STRING,
                    number=3,
                )

            class AreaStyle(proto.Message):
                r"""Custom styling for area chart

                Attributes:
                    color (str):
                        Optional. Used to add color
                    origin (str):
                        Optional. Used to add origin
                    shadow_blur (int):
                        Optional. Used to add shadow blur
                    shadow_color (str):
                        Optional. Used to add shadow color
                    shadow_offset_x (int):
                        Optional. Used to add shadow offsetX
                    shadow_offset_y (int):
                        Optional. Used to add shadow offsetY
                    opacity (int):
                        Optional. Used to add opacity
                """

                color: str = proto.Field(
                    proto.STRING,
                    number=1,
                )
                origin: str = proto.Field(
                    proto.STRING,
                    number=2,
                )
                shadow_blur: int = proto.Field(
                    proto.INT32,
                    number=3,
                )
                shadow_color: str = proto.Field(
                    proto.STRING,
                    number=4,
                )
                shadow_offset_x: int = proto.Field(
                    proto.INT32,
                    number=5,
                )
                shadow_offset_y: int = proto.Field(
                    proto.INT32,
                    number=6,
                )
                opacity: int = proto.Field(
                    proto.INT32,
                    number=7,
                )

            class UserSelectedValues(proto.Message):
                r"""User selected color and label for the slice of the chart

                Attributes:
                    color (str):
                        Optional. User specified color of a pie slice
                    label (str):
                        Optional. User specified label for a pie
                        slice
                """

                color: str = proto.Field(
                    proto.STRING,
                    number=1,
                )
                label: str = proto.Field(
                    proto.STRING,
                    number=2,
                )

            class ChartSliceColor(proto.Message):
                r"""Slice containing the key and value for a slice in the chart

                Attributes:
                    key (str):
                        Optional. Key for the slice
                    value (google.cloud.chronicle_v1.types.DashboardChart.Visualization.Series.UserSelectedValues):
                        Optional. Value for the slice
                """

                key: str = proto.Field(
                    proto.STRING,
                    number=1,
                )
                value: "DashboardChart.Visualization.Series.UserSelectedValues" = proto.Field(
                    proto.MESSAGE,
                    number=2,
                    message="DashboardChart.Visualization.Series.UserSelectedValues",
                )

            class ItemColors(proto.Message):
                r"""Field to be saved for retrieving slice colors for the chart

                Attributes:
                    colors (MutableSequence[google.cloud.chronicle_v1.types.DashboardChart.Visualization.Series.ChartSliceColor]):
                        Optional. Slice colors array
                """

                colors: MutableSequence[
                    "DashboardChart.Visualization.Series.ChartSliceColor"
                ] = proto.RepeatedField(
                    proto.MESSAGE,
                    number=1,
                    message="DashboardChart.Visualization.Series.ChartSliceColor",
                )

            class GaugeValue(proto.Message):
                r"""Field to be saved for retrieving value and color for gauge
                chart

                Attributes:
                    value (int):
                        Optional. Value for gauge chart
                    color (str):
                        Optional. Color for gauge chart
                """

                value: int = proto.Field(
                    proto.INT32,
                    number=1,
                )
                color: str = proto.Field(
                    proto.STRING,
                    number=2,
                )

            class GaugeConfig(proto.Message):
                r"""Field to be saved for retrieving value and color for gauge
                chart

                Attributes:
                    base_value (google.cloud.chronicle_v1.types.DashboardChart.Visualization.Series.GaugeValue):
                        Optional. Base value for gauge chart
                    limit_value (google.cloud.chronicle_v1.types.DashboardChart.Visualization.Series.GaugeValue):
                        Optional. Limit value for gauge chart
                    threshold_values (MutableSequence[google.cloud.chronicle_v1.types.DashboardChart.Visualization.Series.GaugeValue]):
                        Optional. Threshold values for gauge chart
                """

                base_value: "DashboardChart.Visualization.Series.GaugeValue" = (
                    proto.Field(
                        proto.MESSAGE,
                        number=1,
                        message="DashboardChart.Visualization.Series.GaugeValue",
                    )
                )
                limit_value: "DashboardChart.Visualization.Series.GaugeValue" = (
                    proto.Field(
                        proto.MESSAGE,
                        number=2,
                        message="DashboardChart.Visualization.Series.GaugeValue",
                    )
                )
                threshold_values: MutableSequence[
                    "DashboardChart.Visualization.Series.GaugeValue"
                ] = proto.RepeatedField(
                    proto.MESSAGE,
                    number=3,
                    message="DashboardChart.Visualization.Series.GaugeValue",
                )

            class MetricTrendConfig(proto.Message):
                r"""Metric trend config for displaying trend value in Metrics
                chart

                Attributes:
                    metric_format (google.cloud.chronicle_v1.types.MetricFormat):
                        Optional. Metric chart configuration to
                        display metric trend
                    show_metric_trend (bool):
                        Optional. Metric chart configuration to
                        toggle the trend value display
                    metric_display_trend (google.cloud.chronicle_v1.types.MetricDisplayTrend):
                        Optional. Metric chart configuration to
                        display the trend value
                    metric_trend_type (google.cloud.chronicle_v1.types.MetricTrendType):
                        Optional. Metric chart configuration to
                        display trend type whether regular or inverse
                """

                metric_format: "MetricFormat" = proto.Field(
                    proto.ENUM,
                    number=1,
                    enum="MetricFormat",
                )
                show_metric_trend: bool = proto.Field(
                    proto.BOOL,
                    number=5,
                )
                metric_display_trend: "MetricDisplayTrend" = proto.Field(
                    proto.ENUM,
                    number=3,
                    enum="MetricDisplayTrend",
                )
                metric_trend_type: "MetricTrendType" = proto.Field(
                    proto.ENUM,
                    number=4,
                    enum="MetricTrendType",
                )

            series_type: "SeriesType" = proto.Field(
                proto.ENUM,
                number=8,
                enum="SeriesType",
            )
            series_name: str = proto.Field(
                proto.STRING,
                number=2,
            )
            show_symbol: bool = proto.Field(
                proto.BOOL,
                number=4,
            )
            show_background: bool = proto.Field(
                proto.BOOL,
                number=5,
            )
            stack: str = proto.Field(
                proto.STRING,
                number=6,
            )
            series_stack_strategy: "SeriesStackStrategy" = proto.Field(
                proto.ENUM,
                number=9,
                enum="SeriesStackStrategy",
            )
            encode: "DashboardChart.Visualization.Series.Encode" = proto.Field(
                proto.MESSAGE,
                number=10,
                message="DashboardChart.Visualization.Series.Encode",
            )
            label: str = proto.Field(
                proto.STRING,
                number=11,
            )
            field: str = proto.Field(
                proto.STRING,
                number=12,
            )
            data_label: "DashboardChart.Visualization.Series.DataLabel" = proto.Field(
                proto.MESSAGE,
                number=13,
                message="DashboardChart.Visualization.Series.DataLabel",
            )
            radius: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=14,
            )
            item_style: "DashboardChart.Visualization.Series.ItemStyle" = proto.Field(
                proto.MESSAGE,
                number=15,
                message="DashboardChart.Visualization.Series.ItemStyle",
            )
            series_unique_value: str = proto.Field(
                proto.STRING,
                number=16,
            )
            area_style: "DashboardChart.Visualization.Series.AreaStyle" = proto.Field(
                proto.MESSAGE,
                number=17,
                message="DashboardChart.Visualization.Series.AreaStyle",
            )
            item_colors: "DashboardChart.Visualization.Series.ItemColors" = proto.Field(
                proto.MESSAGE,
                number=18,
                message="DashboardChart.Visualization.Series.ItemColors",
            )
            gauge_config: "DashboardChart.Visualization.Series.GaugeConfig" = (
                proto.Field(
                    proto.MESSAGE,
                    number=19,
                    message="DashboardChart.Visualization.Series.GaugeConfig",
                )
            )
            metric_trend_config: "DashboardChart.Visualization.Series.MetricTrendConfig" = proto.Field(
                proto.MESSAGE,
                number=20,
                message="DashboardChart.Visualization.Series.MetricTrendConfig",
            )

        class Tooltip(proto.Message):
            r"""

            Attributes:
                show (bool):

                tooltip_trigger (google.cloud.chronicle_v1.types.ToolTipTrigger):

            """

            show: bool = proto.Field(
                proto.BOOL,
                number=1,
            )
            tooltip_trigger: "ToolTipTrigger" = proto.Field(
                proto.ENUM,
                number=3,
                enum="ToolTipTrigger",
            )

        class Legend(proto.Message):
            r"""

            Attributes:
                id (str):

                show (bool):

                z_level (int):

                z (int):

                left (int):

                top (int):

                right (int):

                bottom (int):

                legend_orient (google.cloud.chronicle_v1.types.LegendOrient):

                legend_align (google.cloud.chronicle_v1.types.LegendAlign):

                padding (MutableSequence[int]):

            """

            id: str = proto.Field(
                proto.STRING,
                number=1,
            )
            show: bool = proto.Field(
                proto.BOOL,
                number=2,
            )
            z_level: int = proto.Field(
                proto.INT32,
                number=3,
            )
            z: int = proto.Field(
                proto.INT32,
                number=4,
            )
            left: int = proto.Field(
                proto.INT32,
                number=5,
            )
            top: int = proto.Field(
                proto.INT32,
                number=6,
            )
            right: int = proto.Field(
                proto.INT32,
                number=7,
            )
            bottom: int = proto.Field(
                proto.INT32,
                number=8,
            )
            legend_orient: "LegendOrient" = proto.Field(
                proto.ENUM,
                number=12,
                enum="LegendOrient",
            )
            legend_align: "LegendAlign" = proto.Field(
                proto.ENUM,
                number=13,
                enum="LegendAlign",
            )
            padding: MutableSequence[int] = proto.RepeatedField(
                proto.INT32,
                number=11,
            )

        class ColumnDef(proto.Message):
            r"""Column Definition.

            Attributes:
                field (str):
                    Field key in data.
                header (str):
                    Header name for column.
            """

            field: str = proto.Field(
                proto.STRING,
                number=1,
            )
            header: str = proto.Field(
                proto.STRING,
                number=2,
            )

        class ColumnRenderTypeSettings(proto.Message):
            r"""Column render type settings. This is used to determine the
            data render type of the column in the table.

            Attributes:
                field (str):
                    Optional. Field key in data.
                column_render_type (google.cloud.chronicle_v1.types.RenderType):
                    Optional. Column render type.
            """

            field: str = proto.Field(
                proto.STRING,
                number=1,
            )
            column_render_type: "RenderType" = proto.Field(
                proto.ENUM,
                number=2,
                enum="RenderType",
            )

        class ColumnTooltipSettings(proto.Message):
            r"""Settings for tooltip for column header and cell.

            Attributes:
                field (str):
                    Required. Field key in data.
                header_tooltip_text (str):
                    Optional. Column header tooltip text.
                cell_tooltip_text (str):
                    Optional. Column cell tooltip text.
            """

            field: str = proto.Field(
                proto.STRING,
                number=1,
            )
            header_tooltip_text: str = proto.Field(
                proto.STRING,
                number=2,
            )
            cell_tooltip_text: str = proto.Field(
                proto.STRING,
                number=3,
            )

        class TableConfig(proto.Message):
            r"""Configuration for table appearance.

            Attributes:
                enable_text_wrap (bool):
                    Optional. Whether to show the table.
                column_render_type_settings (MutableSequence[google.cloud.chronicle_v1.types.DashboardChart.Visualization.ColumnRenderTypeSettings]):
                    Optional. Column render type settings.
                column_tooltip_settings (MutableSequence[google.cloud.chronicle_v1.types.DashboardChart.Visualization.ColumnTooltipSettings]):
                    Optional. Settings for tooltip for column
                    header and cell.
            """

            enable_text_wrap: bool = proto.Field(
                proto.BOOL,
                number=1,
            )
            column_render_type_settings: MutableSequence[
                "DashboardChart.Visualization.ColumnRenderTypeSettings"
            ] = proto.RepeatedField(
                proto.MESSAGE,
                number=2,
                message="DashboardChart.Visualization.ColumnRenderTypeSettings",
            )
            column_tooltip_settings: MutableSequence[
                "DashboardChart.Visualization.ColumnTooltipSettings"
            ] = proto.RepeatedField(
                proto.MESSAGE,
                number=3,
                message="DashboardChart.Visualization.ColumnTooltipSettings",
            )

        class GoogleMapsConfig(proto.Message):
            r"""Google Maps config for a chart if chart type is map.

            Attributes:
                data_settings (google.cloud.chronicle_v1.types.DashboardChart.Visualization.GoogleMapsConfig.DataSettings):
                    Optional. Data settings for the map.
                plot_mode (google.cloud.chronicle_v1.types.PlotMode):
                    Optional. Plot mode for the map. This is used
                    to determine whether to show points, heatmap or
                    both.
                map_position (google.cloud.chronicle_v1.types.DashboardChart.Visualization.GoogleMapsConfig.MapPosition):
                    Optional. Map position settings for the map.
                point_settings (google.cloud.chronicle_v1.types.DashboardChart.Visualization.GoogleMapsConfig.PointSettings):
                    Optional. Point settings for the map.
            """

            class DataSettings(proto.Message):
                r"""Data settings for the map.

                Attributes:
                    latitude_column (str):
                        Optional. Latitude column.
                    longitude_column (str):
                        Optional. Longitude column.
                    count_column (str):
                        Optional. Field to count.
                """

                latitude_column: str = proto.Field(
                    proto.STRING,
                    number=1,
                )
                longitude_column: str = proto.Field(
                    proto.STRING,
                    number=2,
                )
                count_column: str = proto.Field(
                    proto.STRING,
                    number=3,
                )

            class MapPosition(proto.Message):
                r"""Map position settings for the map.

                Attributes:
                    fit_data (bool):
                        Optional. Whether to fit the map to the data.
                        If true, the map will be resized to fit the
                        data. If false, langitude and longitude will be
                        used to set the map size.
                    latitude_value (float):
                        Optional. Latitude of the map.
                    longitude_value (float):
                        Optional. Longitude of the map.
                    zoom_scale_value (float):
                        Optional. Scale of the map.
                """

                fit_data: bool = proto.Field(
                    proto.BOOL,
                    number=1,
                )
                latitude_value: float = proto.Field(
                    proto.DOUBLE,
                    number=5,
                )
                longitude_value: float = proto.Field(
                    proto.DOUBLE,
                    number=6,
                )
                zoom_scale_value: float = proto.Field(
                    proto.DOUBLE,
                    number=7,
                )

            class PointSettings(proto.Message):
                r"""Point settings for the map.

                Attributes:
                    point_size_type (google.cloud.chronicle_v1.types.PointSizeType):
                        Optional. Point size type for the map. This
                        is used to determine the size of the points on
                        the map.
                    color (str):
                        Optional. Color for the point on the map.
                """

                point_size_type: "PointSizeType" = proto.Field(
                    proto.ENUM,
                    number=1,
                    enum="PointSizeType",
                )
                color: str = proto.Field(
                    proto.STRING,
                    number=2,
                )

            data_settings: "DashboardChart.Visualization.GoogleMapsConfig.DataSettings" = proto.Field(
                proto.MESSAGE,
                number=1,
                message="DashboardChart.Visualization.GoogleMapsConfig.DataSettings",
            )
            plot_mode: "PlotMode" = proto.Field(
                proto.ENUM,
                number=2,
                enum="PlotMode",
            )
            map_position: "DashboardChart.Visualization.GoogleMapsConfig.MapPosition" = proto.Field(
                proto.MESSAGE,
                number=3,
                message="DashboardChart.Visualization.GoogleMapsConfig.MapPosition",
            )
            point_settings: "DashboardChart.Visualization.GoogleMapsConfig.PointSettings" = proto.Field(
                proto.MESSAGE,
                number=4,
                message="DashboardChart.Visualization.GoogleMapsConfig.PointSettings",
            )

        class VisualMap(proto.Message):
            r"""Conveys what range of values should be rendered in what color. This
            field is used when threshold_coloring_enabled is true.

            Attributes:
                visual_map_type (google.cloud.chronicle_v1.types.VisualMapType):
                    Optional. Contains one of the valid visual
                    map types such as 'continuous' or 'piecewise'.
                pieces (MutableSequence[google.cloud.chronicle_v1.types.DashboardChart.Visualization.VisualMap.VisualMapPiece]):
                    Optional. Pieces of the visual map.
            """

            class VisualMapPiece(proto.Message):
                r"""An ECharts visual map of type 'piecewise' contain many
                pieces. Each piece has a min, max, and color with which it's
                rendered.


                .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

                Attributes:
                    min_ (int):
                        Optional. Minimum value for the piece.

                        This field is a member of `oneof`_ ``_min``.
                    max_ (int):
                        Optional. Minimum value for the piece.

                        This field is a member of `oneof`_ ``_max``.
                    color (str):
                        Optional. Color to render the piece in when
                        the value is between min and max.
                    label (str):
                        Optional. Label used in visual map
                        controller.
                """

                min_: int = proto.Field(
                    proto.INT64,
                    number=1,
                    optional=True,
                )
                max_: int = proto.Field(
                    proto.INT64,
                    number=2,
                    optional=True,
                )
                color: str = proto.Field(
                    proto.STRING,
                    number=3,
                )
                label: str = proto.Field(
                    proto.STRING,
                    number=4,
                )

            visual_map_type: "VisualMapType" = proto.Field(
                proto.ENUM,
                number=1,
                enum="VisualMapType",
            )
            pieces: MutableSequence[
                "DashboardChart.Visualization.VisualMap.VisualMapPiece"
            ] = proto.RepeatedField(
                proto.MESSAGE,
                number=2,
                message="DashboardChart.Visualization.VisualMap.VisualMapPiece",
            )

        x_axes: MutableSequence["DashboardChart.Visualization.Axis"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=7,
                message="DashboardChart.Visualization.Axis",
            )
        )
        y_axes: MutableSequence["DashboardChart.Visualization.Axis"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=8,
                message="DashboardChart.Visualization.Axis",
            )
        )
        series: MutableSequence["DashboardChart.Visualization.Series"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=3,
                message="DashboardChart.Visualization.Series",
            )
        )
        tooltip: "DashboardChart.Visualization.Tooltip" = proto.Field(
            proto.MESSAGE,
            number=4,
            message="DashboardChart.Visualization.Tooltip",
        )
        legends: MutableSequence["DashboardChart.Visualization.Legend"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=9,
                message="DashboardChart.Visualization.Legend",
            )
        )
        column_defs: MutableSequence["DashboardChart.Visualization.ColumnDef"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=10,
                message="DashboardChart.Visualization.ColumnDef",
            )
        )
        table_config: "DashboardChart.Visualization.TableConfig" = proto.Field(
            proto.MESSAGE,
            number=18,
            message="DashboardChart.Visualization.TableConfig",
        )
        button: "Button" = proto.Field(
            proto.MESSAGE,
            number=11,
            message="Button",
        )
        markdown: "Markdown" = proto.Field(
            proto.MESSAGE,
            number=17,
            message="Markdown",
        )
        series_column: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=12,
        )
        grouping_type: str = proto.Field(
            proto.STRING,
            number=13,
        )
        google_maps_config: "DashboardChart.Visualization.GoogleMapsConfig" = (
            proto.Field(
                proto.MESSAGE,
                number=14,
                message="DashboardChart.Visualization.GoogleMapsConfig",
            )
        )
        threshold_coloring_enabled: bool = proto.Field(
            proto.BOOL,
            number=15,
        )
        visual_maps: MutableSequence["DashboardChart.Visualization.VisualMap"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=16,
                message="DashboardChart.Visualization.VisualMap",
            )
        )

    class DrillDownConfig(proto.Message):
        r"""Drill down configuration.

        Attributes:
            left_drill_downs (MutableSequence[google.cloud.chronicle_v1.types.DashboardChart.DrillDownConfig.DrillDown]):
                Required. Left click drill downs.
            right_drill_downs (MutableSequence[google.cloud.chronicle_v1.types.DashboardChart.DrillDownConfig.DrillDown]):
                Required. Right click drill downs.
        """

        class DrillDown(proto.Message):
            r"""Drill down config.

            This message has `oneof`_ fields (mutually exclusive fields).
            For each oneof, at most one member field can be set at the same time.
            Setting any member of the oneof automatically clears all other
            members.

            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                default_settings (google.cloud.chronicle_v1.types.DashboardChart.DrillDownConfig.DrillDown.DefaultDrillDownSettings):
                    Default drill down settings.

                    This field is a member of `oneof`_ ``settings``.
                custom_settings (google.cloud.chronicle_v1.types.DashboardChart.DrillDownConfig.DrillDown.CustomDrillDownSettings):
                    Custom drill down settings.

                    This field is a member of `oneof`_ ``settings``.
                id (str):
                    Required. ID of the drill down.
                display_name (str):
                    Required. Display name of the drill down.
            """

            class DefaultDrillDownSettings(proto.Message):
                r"""Default drill down settings.

                Attributes:
                    enabled (bool):
                        Required. Whether the default drill down is
                        enabled.
                """

                enabled: bool = proto.Field(
                    proto.BOOL,
                    number=1,
                )

            class CustomDrillDownSettings(proto.Message):
                r"""Custom drill down settings.

                This message has `oneof`_ fields (mutually exclusive fields).
                For each oneof, at most one member field can be set at the same time.
                Setting any member of the oneof automatically clears all other
                members.

                .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

                Attributes:
                    query (google.cloud.chronicle_v1.types.DashboardChart.DrillDownConfig.DrillDown.CustomDrillDownSettings.DrillDownQuery):
                        Drill down query action config.

                        This field is a member of `oneof`_ ``action``.
                    filter (google.cloud.chronicle_v1.types.DashboardChart.DrillDownConfig.DrillDown.CustomDrillDownSettings.DrillDownFilter):
                        Drill down filter action config.

                        This field is a member of `oneof`_ ``action``.
                    external_link (google.cloud.chronicle_v1.types.DashboardChart.DrillDownConfig.DrillDown.CustomDrillDownSettings.DrillDownExternalLink):
                        Drill down external link action config.

                        This field is a member of `oneof`_ ``action``.
                    new_tab (bool):
                        Required. Whether to open the drill down
                        action in a new tab.
                    left_click_column (str):
                        Optional. Table chart column name to
                        associate the custom drill down action on left
                        click.
                """

                class DrillDownQuery(proto.Message):
                    r"""Drill down query config.

                    Attributes:
                        query (str):
                            Required. Search query to be executed on
                            drill down.
                    """

                    query: str = proto.Field(
                        proto.STRING,
                        number=1,
                    )

                class DrillDownFilter(proto.Message):
                    r"""Drill down filter config.

                    Attributes:
                        dashboard_filters (MutableSequence[google.cloud.chronicle_v1.types.DashboardChart.DrillDownConfig.DrillDown.CustomDrillDownSettings.DrillDownFilter.DrillDownDashboardFilter]):
                            Required. Dashboard filters to be applied on
                            drill down.
                    """

                    class DrillDownDashboardFilter(proto.Message):
                        r"""Drill down dashboard filter config.

                        Attributes:
                            dashboard_filter_id (str):
                                Required. ID of the dashboard filter.
                            filter_operator_and_values (MutableSequence[google.cloud.chronicle_v1.types.FilterOperatorAndValues]):
                                Required. Filter operator and field values
                                for the dashboard filter.
                        """

                        dashboard_filter_id: str = proto.Field(
                            proto.STRING,
                            number=1,
                        )
                        filter_operator_and_values: MutableSequence[
                            gcc_dashboard_query.FilterOperatorAndValues
                        ] = proto.RepeatedField(
                            proto.MESSAGE,
                            number=2,
                            message=gcc_dashboard_query.FilterOperatorAndValues,
                        )

                    dashboard_filters: MutableSequence[
                        "DashboardChart.DrillDownConfig.DrillDown.CustomDrillDownSettings.DrillDownFilter.DrillDownDashboardFilter"
                    ] = proto.RepeatedField(
                        proto.MESSAGE,
                        number=1,
                        message="DashboardChart.DrillDownConfig.DrillDown.CustomDrillDownSettings.DrillDownFilter.DrillDownDashboardFilter",
                    )

                class DrillDownExternalLink(proto.Message):
                    r"""Drill down external link config.

                    Attributes:
                        link (str):
                            Required. External link the drill down action
                            should redirect to.
                        description (str):
                            Optional. Description of the external link.
                    """

                    link: str = proto.Field(
                        proto.STRING,
                        number=1,
                    )
                    description: str = proto.Field(
                        proto.STRING,
                        number=2,
                    )

                query: "DashboardChart.DrillDownConfig.DrillDown.CustomDrillDownSettings.DrillDownQuery" = proto.Field(
                    proto.MESSAGE,
                    number=3,
                    oneof="action",
                    message="DashboardChart.DrillDownConfig.DrillDown.CustomDrillDownSettings.DrillDownQuery",
                )
                filter: "DashboardChart.DrillDownConfig.DrillDown.CustomDrillDownSettings.DrillDownFilter" = proto.Field(
                    proto.MESSAGE,
                    number=4,
                    oneof="action",
                    message="DashboardChart.DrillDownConfig.DrillDown.CustomDrillDownSettings.DrillDownFilter",
                )
                external_link: "DashboardChart.DrillDownConfig.DrillDown.CustomDrillDownSettings.DrillDownExternalLink" = proto.Field(
                    proto.MESSAGE,
                    number=5,
                    oneof="action",
                    message="DashboardChart.DrillDownConfig.DrillDown.CustomDrillDownSettings.DrillDownExternalLink",
                )
                new_tab: bool = proto.Field(
                    proto.BOOL,
                    number=1,
                )
                left_click_column: str = proto.Field(
                    proto.STRING,
                    number=2,
                )

            default_settings: "DashboardChart.DrillDownConfig.DrillDown.DefaultDrillDownSettings" = proto.Field(
                proto.MESSAGE,
                number=3,
                oneof="settings",
                message="DashboardChart.DrillDownConfig.DrillDown.DefaultDrillDownSettings",
            )
            custom_settings: "DashboardChart.DrillDownConfig.DrillDown.CustomDrillDownSettings" = proto.Field(
                proto.MESSAGE,
                number=4,
                oneof="settings",
                message="DashboardChart.DrillDownConfig.DrillDown.CustomDrillDownSettings",
            )
            id: str = proto.Field(
                proto.STRING,
                number=1,
            )
            display_name: str = proto.Field(
                proto.STRING,
                number=2,
            )

        left_drill_downs: MutableSequence[
            "DashboardChart.DrillDownConfig.DrillDown"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="DashboardChart.DrillDownConfig.DrillDown",
        )
        right_drill_downs: MutableSequence[
            "DashboardChart.DrillDownConfig.DrillDown"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="DashboardChart.DrillDownConfig.DrillDown",
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    native_dashboard: str = proto.Field(
        proto.STRING,
        number=4,
    )
    tile_type: "TileType" = proto.Field(
        proto.ENUM,
        number=7,
        enum="TileType",
    )
    chart_datasource: ChartDatasource = proto.Field(
        proto.MESSAGE,
        number=5,
        message=ChartDatasource,
    )
    visualization: Visualization = proto.Field(
        proto.MESSAGE,
        number=6,
        message=Visualization,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=8,
    )
    drill_down_config: DrillDownConfig = proto.Field(
        proto.MESSAGE,
        number=9,
        message=DrillDownConfig,
    )
    tokens: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=10,
    )


class Button(proto.Message):
    r"""Button config for a chart.

    Attributes:
        label (str):

        hyperlink (str):

        description (str):

        new_tab (bool):
            Optional. Whether to open the link in a new
            tab.
        properties (google.cloud.chronicle_v1.types.Button.Properties):

    """

    class Properties(proto.Message):
        r"""

        Attributes:
            color (str):

            button_style (google.cloud.chronicle_v1.types.ButtonStyle):

        """

        color: str = proto.Field(
            proto.STRING,
            number=1,
        )
        button_style: "ButtonStyle" = proto.Field(
            proto.ENUM,
            number=2,
            enum="ButtonStyle",
        )

    label: str = proto.Field(
        proto.STRING,
        number=1,
    )
    hyperlink: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    new_tab: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    properties: Properties = proto.Field(
        proto.MESSAGE,
        number=5,
        message=Properties,
    )


class Markdown(proto.Message):
    r"""Markdown config for a dashboard tile.

    Attributes:
        content (str):
            Required. Markdown content.
        properties (google.cloud.chronicle_v1.types.Markdown.MarkdownProperties):
            Optional. Properties for the markdown.
    """

    class MarkdownProperties(proto.Message):
        r"""Properties for the markdown.

        Attributes:
            background_color (str):
                Optional. Background color of the markdown.
        """

        background_color: str = proto.Field(
            proto.STRING,
            number=3,
        )

    content: str = proto.Field(
        proto.STRING,
        number=1,
    )
    properties: MarkdownProperties = proto.Field(
        proto.MESSAGE,
        number=2,
        message=MarkdownProperties,
    )


class GetDashboardChartRequest(proto.Message):
    r"""Request message to get a dashboard chart.

    Attributes:
        name (str):
            Required. The name of the dashboardChart to
            retrieve. Format:

            projects/{project}/locations/{location}/instances/{instance}/dashboardCharts/{chart}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class BatchGetDashboardChartsRequest(proto.Message):
    r"""Request message to get dashboard charts in batch.

    Attributes:
        parent (str):
            Required. The parent resource shared by all dashboard charts
            being retrieved. Format:
            projects/{project}/locations/{location}/instances/{instance}
            If this is set, the parent of all of the dashboard charts
            specified in ``names`` must match this field.
        names (MutableSequence[str]):
            Required. The names of the dashboard charts
            to get.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchGetDashboardChartsResponse(proto.Message):
    r"""Response message for getting dashboard charts in batch.

    Attributes:
        dashboard_charts (MutableSequence[google.cloud.chronicle_v1.types.DashboardChart]):
            The dashboardCharts from the specified
            chronicle instance.
    """

    dashboard_charts: MutableSequence["DashboardChart"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="DashboardChart",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
