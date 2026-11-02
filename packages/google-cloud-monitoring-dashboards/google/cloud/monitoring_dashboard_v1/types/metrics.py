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

from google.cloud.monitoring_dashboard_v1.types import common

__protobuf__ = proto.module(
    package="google.monitoring.dashboard.v1",
    manifest={
        "SparkChartType",
        "TimeSeriesQuery",
        "TimeSeriesFilter",
        "TimeSeriesFilterRatio",
        "Threshold",
    },
)


class SparkChartType(proto.Enum):
    r"""Defines the possible types of spark chart supported by the
    ``Scorecard``.

    Values:
        SPARK_CHART_TYPE_UNSPECIFIED (0):
            Not allowed in well-formed requests.
        SPARK_LINE (1):
            The sparkline will be rendered as a small
            line chart.
        SPARK_BAR (2):
            The sparkbar will be rendered as a small bar
            chart.
    """

    SPARK_CHART_TYPE_UNSPECIFIED = 0
    SPARK_LINE = 1
    SPARK_BAR = 2


class TimeSeriesQuery(proto.Message):
    r"""TimeSeriesQuery collects the set of supported methods for
    querying time series data from the Stackdriver metrics API.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        time_series_filter (google.cloud.monitoring_dashboard_v1.types.TimeSeriesFilter):
            Filter parameters to fetch time series.

            This field is a member of `oneof`_ ``source``.
        time_series_filter_ratio (google.cloud.monitoring_dashboard_v1.types.TimeSeriesFilterRatio):
            Parameters to fetch a ratio between two time
            series filters.

            This field is a member of `oneof`_ ``source``.
        time_series_query_language (str):
            A query used to fetch time series with MQL.

            This field is a member of `oneof`_ ``source``.
        prometheus_query (str):
            A query used to fetch time series with
            PromQL.

            This field is a member of `oneof`_ ``source``.
        unit_override (str):
            The unit of data contained in fetched time series. If
            non-empty, this unit will override any unit that accompanies
            fetched data. The format is the same as the
            ```unit`` <https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors>`__
            field in ``MetricDescriptor``.
        output_full_duration (bool):
            Optional. If set, Cloud Monitoring will treat the full query
            duration as the alignment period so that there will be only
            1 output value.

            \*Note: This could override the configured alignment period
            except for the cases where a series of data points are
            expected, like

            - XyChart
            - Scorecard's spark chart
    """

    time_series_filter: "TimeSeriesFilter" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="source",
        message="TimeSeriesFilter",
    )
    time_series_filter_ratio: "TimeSeriesFilterRatio" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="source",
        message="TimeSeriesFilterRatio",
    )
    time_series_query_language: str = proto.Field(
        proto.STRING,
        number=3,
        oneof="source",
    )
    prometheus_query: str = proto.Field(
        proto.STRING,
        number=6,
        oneof="source",
    )
    unit_override: str = proto.Field(
        proto.STRING,
        number=5,
    )
    output_full_duration: bool = proto.Field(
        proto.BOOL,
        number=7,
    )


class TimeSeriesFilter(proto.Message):
    r"""A filter that defines a subset of time series data that is displayed
    in a widget. Time series data is fetched using the
    ```ListTimeSeries`` <https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list>`__
    method.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        filter (str):
            Required. The `monitoring
            filter <https://cloud.google.com/monitoring/api/v3/filters>`__
            that identifies the metric types, resources, and projects to
            query.
        aggregation (google.cloud.monitoring_dashboard_v1.types.Aggregation):
            By default, the raw time series data is
            returned. Use this field to combine multiple
            time series for different views of the data.
        secondary_aggregation (google.cloud.monitoring_dashboard_v1.types.Aggregation):
            Apply a second aggregation after ``aggregation`` is applied.
        pick_time_series_filter (google.cloud.monitoring_dashboard_v1.types.PickTimeSeriesFilter):
            Ranking based time series filter.

            This field is a member of `oneof`_ ``output_filter``.
        statistical_time_series_filter (google.cloud.monitoring_dashboard_v1.types.StatisticalTimeSeriesFilter):
            Statistics based time series filter.
            Note: This field is deprecated and completely
            ignored by the API.

            This field is a member of `oneof`_ ``output_filter``.
    """

    filter: str = proto.Field(
        proto.STRING,
        number=1,
    )
    aggregation: common.Aggregation = proto.Field(
        proto.MESSAGE,
        number=2,
        message=common.Aggregation,
    )
    secondary_aggregation: common.Aggregation = proto.Field(
        proto.MESSAGE,
        number=3,
        message=common.Aggregation,
    )
    pick_time_series_filter: common.PickTimeSeriesFilter = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="output_filter",
        message=common.PickTimeSeriesFilter,
    )
    statistical_time_series_filter: common.StatisticalTimeSeriesFilter = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="output_filter",
        message=common.StatisticalTimeSeriesFilter,
    )


class TimeSeriesFilterRatio(proto.Message):
    r"""A pair of time series filters that define a ratio
    computation. The output time series is the pair-wise division of
    each aligned element from the numerator and denominator time
    series.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        numerator (google.cloud.monitoring_dashboard_v1.types.TimeSeriesFilterRatio.RatioPart):
            The numerator of the ratio.
        denominator (google.cloud.monitoring_dashboard_v1.types.TimeSeriesFilterRatio.RatioPart):
            The denominator of the ratio.
        secondary_aggregation (google.cloud.monitoring_dashboard_v1.types.Aggregation):
            Apply a second aggregation after the ratio is
            computed.
        pick_time_series_filter (google.cloud.monitoring_dashboard_v1.types.PickTimeSeriesFilter):
            Ranking based time series filter.

            This field is a member of `oneof`_ ``output_filter``.
        statistical_time_series_filter (google.cloud.monitoring_dashboard_v1.types.StatisticalTimeSeriesFilter):
            Statistics based time series filter.
            Note: This field is deprecated and completely
            ignored by the API.

            This field is a member of `oneof`_ ``output_filter``.
    """

    class RatioPart(proto.Message):
        r"""Describes a query to build the numerator or denominator of a
        TimeSeriesFilterRatio.

        Attributes:
            filter (str):
                Required. The `monitoring
                filter <https://cloud.google.com/monitoring/api/v3/filters>`__
                that identifies the metric types, resources, and projects to
                query.
            aggregation (google.cloud.monitoring_dashboard_v1.types.Aggregation):
                By default, the raw time series data is
                returned. Use this field to combine multiple
                time series for different views of the data.
        """

        filter: str = proto.Field(
            proto.STRING,
            number=1,
        )
        aggregation: common.Aggregation = proto.Field(
            proto.MESSAGE,
            number=2,
            message=common.Aggregation,
        )

    numerator: RatioPart = proto.Field(
        proto.MESSAGE,
        number=1,
        message=RatioPart,
    )
    denominator: RatioPart = proto.Field(
        proto.MESSAGE,
        number=2,
        message=RatioPart,
    )
    secondary_aggregation: common.Aggregation = proto.Field(
        proto.MESSAGE,
        number=3,
        message=common.Aggregation,
    )
    pick_time_series_filter: common.PickTimeSeriesFilter = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="output_filter",
        message=common.PickTimeSeriesFilter,
    )
    statistical_time_series_filter: common.StatisticalTimeSeriesFilter = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="output_filter",
        message=common.StatisticalTimeSeriesFilter,
    )


class Threshold(proto.Message):
    r"""Defines a threshold for categorizing time series values.

    Attributes:
        label (str):
            A label for the threshold.
        value (float):
            The value of the threshold. The value should
            be defined in the native scale of the metric.
        color (google.cloud.monitoring_dashboard_v1.types.Threshold.Color):
            The state color for this threshold. Color is
            not allowed in a XyChart.
        direction (google.cloud.monitoring_dashboard_v1.types.Threshold.Direction):
            The direction for the current threshold.
            Direction is not allowed in a XyChart.
        target_axis (google.cloud.monitoring_dashboard_v1.types.Threshold.TargetAxis):
            The target axis to use for plotting the
            threshold. Target axis is not allowed in a
            Scorecard.
    """

    class Color(proto.Enum):
        r"""The color suggests an interpretation to the viewer when
        actual values cross the threshold. Comments on each color
        provide UX guidance on how users can be expected to interpret a
        given state color.

        Values:
            COLOR_UNSPECIFIED (0):
                Color is unspecified. Not allowed in
                well-formed requests.
            YELLOW (4):
                Crossing the threshold is "concerning"
                behavior.
            RED (6):
                Crossing the threshold is "emergency"
                behavior.
        """

        COLOR_UNSPECIFIED = 0
        YELLOW = 4
        RED = 6

    class Direction(proto.Enum):
        r"""Whether the threshold is considered crossed by an actual
        value above or below its threshold value.

        Values:
            DIRECTION_UNSPECIFIED (0):
                Not allowed in well-formed requests.
            ABOVE (1):
                The threshold will be considered crossed if
                the actual value is above the threshold value.
            BELOW (2):
                The threshold will be considered crossed if
                the actual value is below the threshold value.
        """

        DIRECTION_UNSPECIFIED = 0
        ABOVE = 1
        BELOW = 2

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

    label: str = proto.Field(
        proto.STRING,
        number=1,
    )
    value: float = proto.Field(
        proto.DOUBLE,
        number=2,
    )
    color: Color = proto.Field(
        proto.ENUM,
        number=3,
        enum=Color,
    )
    direction: Direction = proto.Field(
        proto.ENUM,
        number=4,
        enum=Direction,
    )
    target_axis: TargetAxis = proto.Field(
        proto.ENUM,
        number=5,
        enum=TargetAxis,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
