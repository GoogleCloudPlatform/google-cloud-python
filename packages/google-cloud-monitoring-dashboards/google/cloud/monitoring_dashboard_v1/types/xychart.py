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

import google.protobuf.duration_pb2 as duration_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.monitoring_dashboard_v1.types import metrics

__protobuf__ = proto.module(
    package="google.monitoring.dashboard.v1",
    manifest={
        "XyChart",
        "ChartOptions",
    },
)


class XyChart(proto.Message):
    r"""A chart that displays data on a 2D (X and Y axes) plane.

    Attributes:
        data_sets (MutableSequence[google.cloud.monitoring_dashboard_v1.types.XyChart.DataSet]):
            Required. The data displayed in this chart.
        timeshift_duration (google.protobuf.duration_pb2.Duration):
            The duration used to display a comparison
            chart. A comparison chart simultaneously shows
            values from two similar-length time periods
            (e.g., week-over-week metrics).
            The duration must be positive, and it can only
            be applied to charts with data sets of LINE plot
            type.
        thresholds (MutableSequence[google.cloud.monitoring_dashboard_v1.types.Threshold]):
            Threshold lines drawn horizontally across the
            chart.
        x_axis (google.cloud.monitoring_dashboard_v1.types.XyChart.Axis):
            The properties applied to the x-axis.
        y_axis (google.cloud.monitoring_dashboard_v1.types.XyChart.Axis):
            The properties applied to the y-axis.
        y2_axis (google.cloud.monitoring_dashboard_v1.types.XyChart.Axis):
            The properties applied to the y2-axis.
        chart_options (google.cloud.monitoring_dashboard_v1.types.ChartOptions):
            Display options for the chart.
    """

    class DataSet(proto.Message):
        r"""Groups a time series query definition with charting options.

        Attributes:
            time_series_query (google.cloud.monitoring_dashboard_v1.types.TimeSeriesQuery):
                Required. Fields for querying time series
                data from the Stackdriver metrics API.
            plot_type (google.cloud.monitoring_dashboard_v1.types.XyChart.DataSet.PlotType):
                How this data should be plotted on the chart.
            legend_template (str):
                A template string for naming ``TimeSeries`` in the resulting
                data set. This should be a string with interpolations of the
                form ``${label_name}``, which will resolve to the label's
                value.
            min_alignment_period (google.protobuf.duration_pb2.Duration):
                Optional. The lower bound on data point frequency for this
                data set, implemented by specifying the minimum alignment
                period to use in a time series query For example, if the
                data is published once every 10 minutes, the
                ``min_alignment_period`` should be at least 10 minutes. It
                would not make sense to fetch and align data at one minute
                intervals.
            target_axis (google.cloud.monitoring_dashboard_v1.types.XyChart.DataSet.TargetAxis):
                Optional. The target axis to use for plotting
                the metric.
        """

        class PlotType(proto.Enum):
            r"""The types of plotting strategies for data sets.

            Values:
                PLOT_TYPE_UNSPECIFIED (0):
                    Plot type is unspecified. The view will default to ``LINE``.
                LINE (1):
                    The data is plotted as a set of lines (one
                    line per series).
                STACKED_AREA (2):
                    The data is plotted as a set of filled areas
                    (one area per series), with the areas stacked
                    vertically (the base of each area is the top of
                    its predecessor, and the base of the first area
                    is the x-axis). Since the areas do not overlap,
                    each is filled with a different opaque color.
                STACKED_BAR (3):
                    The data is plotted as a set of rectangular
                    boxes (one box per series), with the boxes
                    stacked vertically (the base of each box is the
                    top of its predecessor, and the base of the
                    first box is the x-axis). Since the boxes do not
                    overlap, each is filled with a different opaque
                    color.
                HEATMAP (4):
                    The data is plotted as a heatmap. The series being plotted
                    must have a ``DISTRIBUTION`` value type. The value of each
                    bucket in the distribution is displayed as a color. This
                    type is not currently available in the Stackdriver
                    Monitoring application.
            """

            PLOT_TYPE_UNSPECIFIED = 0
            LINE = 1
            STACKED_AREA = 2
            STACKED_BAR = 3
            HEATMAP = 4

        class TargetAxis(proto.Enum):
            r"""An axis identifier.

            Values:
                TARGET_AXIS_UNSPECIFIED (0):
                    The target axis was not specified. Defaults
                    to Y1.
                Y1 (1):
                    The y_axis (the right axis of chart).
                Y2 (2):
                    The y2_axis (the left axis of chart).
            """

            TARGET_AXIS_UNSPECIFIED = 0
            Y1 = 1
            Y2 = 2

        time_series_query: metrics.TimeSeriesQuery = proto.Field(
            proto.MESSAGE,
            number=1,
            message=metrics.TimeSeriesQuery,
        )
        plot_type: "XyChart.DataSet.PlotType" = proto.Field(
            proto.ENUM,
            number=2,
            enum="XyChart.DataSet.PlotType",
        )
        legend_template: str = proto.Field(
            proto.STRING,
            number=3,
        )
        min_alignment_period: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=4,
            message=duration_pb2.Duration,
        )
        target_axis: "XyChart.DataSet.TargetAxis" = proto.Field(
            proto.ENUM,
            number=5,
            enum="XyChart.DataSet.TargetAxis",
        )

    class Axis(proto.Message):
        r"""A chart axis.

        Attributes:
            label (str):
                The label of the axis.
            scale (google.cloud.monitoring_dashboard_v1.types.XyChart.Axis.Scale):
                The axis scale. By default, a linear scale is
                used.
        """

        class Scale(proto.Enum):
            r"""Types of scales used in axes.

            Values:
                SCALE_UNSPECIFIED (0):
                    Scale is unspecified. The view will default to ``LINEAR``.
                LINEAR (1):
                    Linear scale.
                LOG10 (2):
                    Logarithmic scale (base 10).
            """

            SCALE_UNSPECIFIED = 0
            LINEAR = 1
            LOG10 = 2

        label: str = proto.Field(
            proto.STRING,
            number=1,
        )
        scale: "XyChart.Axis.Scale" = proto.Field(
            proto.ENUM,
            number=2,
            enum="XyChart.Axis.Scale",
        )

    data_sets: MutableSequence[DataSet] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=DataSet,
    )
    timeshift_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=4,
        message=duration_pb2.Duration,
    )
    thresholds: MutableSequence[metrics.Threshold] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message=metrics.Threshold,
    )
    x_axis: Axis = proto.Field(
        proto.MESSAGE,
        number=6,
        message=Axis,
    )
    y_axis: Axis = proto.Field(
        proto.MESSAGE,
        number=7,
        message=Axis,
    )
    y2_axis: Axis = proto.Field(
        proto.MESSAGE,
        number=9,
        message=Axis,
    )
    chart_options: "ChartOptions" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="ChartOptions",
    )


class ChartOptions(proto.Message):
    r"""Options to control visual rendering of a chart.

    Attributes:
        mode (google.cloud.monitoring_dashboard_v1.types.ChartOptions.Mode):
            The chart mode.
    """

    class Mode(proto.Enum):
        r"""Chart mode options.

        Values:
            MODE_UNSPECIFIED (0):
                Mode is unspecified. The view will default to ``COLOR``.
            COLOR (1):
                The chart distinguishes data series using
                different color. Line colors may get reused when
                there are many lines in the chart.
            X_RAY (2):
                The chart uses the Stackdriver x-ray mode, in
                which each data set is plotted using the same
                semi-transparent color.
            STATS (3):
                The chart displays statistics such as
                average, median, 95th percentile, and more.
        """

        MODE_UNSPECIFIED = 0
        COLOR = 1
        X_RAY = 2
        STATS = 3

    mode: Mode = proto.Field(
        proto.ENUM,
        number=1,
        enum=Mode,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
