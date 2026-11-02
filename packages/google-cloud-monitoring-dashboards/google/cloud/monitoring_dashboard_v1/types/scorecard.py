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
import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.monitoring_dashboard_v1.types import metrics

__protobuf__ = proto.module(
    package="google.monitoring.dashboard.v1",
    manifest={
        "Scorecard",
    },
)


class Scorecard(proto.Message):
    r"""A widget showing the latest value of a metric, and how this
    value relates to one or more thresholds.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        time_series_query (google.cloud.monitoring_dashboard_v1.types.TimeSeriesQuery):
            Required. Fields for querying time series
            data from the Stackdriver metrics API.
        gauge_view (google.cloud.monitoring_dashboard_v1.types.Scorecard.GaugeView):
            Will cause the scorecard to show a gauge
            chart.

            This field is a member of `oneof`_ ``data_view``.
        spark_chart_view (google.cloud.monitoring_dashboard_v1.types.Scorecard.SparkChartView):
            Will cause the scorecard to show a spark
            chart.

            This field is a member of `oneof`_ ``data_view``.
        blank_view (google.protobuf.empty_pb2.Empty):
            Will cause the ``Scorecard`` to show only the value, with no
            indicator to its value relative to its thresholds.

            This field is a member of `oneof`_ ``data_view``.
        thresholds (MutableSequence[google.cloud.monitoring_dashboard_v1.types.Threshold]):
            The thresholds used to determine the state of the scorecard
            given the time series' current value. For an actual value x,
            the scorecard is in a danger state if x is less than or
            equal to a danger threshold that triggers below, or greater
            than or equal to a danger threshold that triggers above.
            Similarly, if x is above/below a warning threshold that
            triggers above/below, then the scorecard is in a warning
            state - unless x also puts it in a danger state. (Danger
            trumps warning.)

            As an example, consider a scorecard with the following four
            thresholds:

            ::

               {
                 value: 90,
                 category: 'DANGER',
                 trigger: 'ABOVE',
               },
               {
                 value: 70,
                 category: 'WARNING',
                 trigger: 'ABOVE',
               },
               {
                 value: 10,
                 category: 'DANGER',
                 trigger: 'BELOW',
               },
               {
                 value: 20,
                 category: 'WARNING',
                 trigger: 'BELOW',
               }

            Then: values less than or equal to 10 would put the
            scorecard in a DANGER state, values greater than 10 but less
            than or equal to 20 a WARNING state, values strictly between
            20 and 70 an OK state, values greater than or equal to 70
            but less than 90 a WARNING state, and values greater than or
            equal to 90 a DANGER state.
    """

    class GaugeView(proto.Message):
        r"""A gauge chart shows where the current value sits within a
        pre-defined range. The upper and lower bounds should define the
        possible range of values for the scorecard's query (inclusive).

        Attributes:
            lower_bound (float):
                The lower bound for this gauge chart. The
                value of the chart should always be greater than
                or equal to this.
            upper_bound (float):
                The upper bound for this gauge chart. The
                value of the chart should always be less than or
                equal to this.
        """

        lower_bound: float = proto.Field(
            proto.DOUBLE,
            number=1,
        )
        upper_bound: float = proto.Field(
            proto.DOUBLE,
            number=2,
        )

    class SparkChartView(proto.Message):
        r"""A sparkChart is a small chart suitable for inclusion in a
        table-cell or inline in text. This message contains the
        configuration for a sparkChart to show up on a Scorecard,
        showing recent trends of the scorecard's timeseries.

        Attributes:
            spark_chart_type (google.cloud.monitoring_dashboard_v1.types.SparkChartType):
                Required. The type of sparkchart to show in
                this chartView.
            min_alignment_period (google.protobuf.duration_pb2.Duration):
                The lower bound on data point frequency in
                the chart implemented by specifying the minimum
                alignment period to use in a time series query.
                For example, if the data is published once every
                10 minutes it would not make sense to fetch and
                align data at one minute intervals. This field
                is optional and exists only as a hint.
        """

        spark_chart_type: metrics.SparkChartType = proto.Field(
            proto.ENUM,
            number=1,
            enum=metrics.SparkChartType,
        )
        min_alignment_period: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=2,
            message=duration_pb2.Duration,
        )

    time_series_query: metrics.TimeSeriesQuery = proto.Field(
        proto.MESSAGE,
        number=1,
        message=metrics.TimeSeriesQuery,
    )
    gauge_view: GaugeView = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="data_view",
        message=GaugeView,
    )
    spark_chart_view: SparkChartView = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="data_view",
        message=SparkChartView,
    )
    blank_view: empty_pb2.Empty = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="data_view",
        message=empty_pb2.Empty,
    )
    thresholds: MutableSequence[metrics.Threshold] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message=metrics.Threshold,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
