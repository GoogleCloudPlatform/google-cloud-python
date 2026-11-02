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
        "PieChart",
    },
)


class PieChart(proto.Message):
    r"""A widget that displays timeseries data as a pie or a donut.

    Attributes:
        data_sets (MutableSequence[google.cloud.monitoring_dashboard_v1.types.PieChart.PieChartDataSet]):
            Required. The queries for the chart's data.
        chart_type (google.cloud.monitoring_dashboard_v1.types.PieChart.PieChartType):
            Required. Indicates the visualization type
            for the PieChart.
        show_labels (bool):
            Optional. Indicates whether or not the pie
            chart should show slices' labels
    """

    class PieChartType(proto.Enum):
        r"""Types for the pie chart.

        Values:
            PIE_CHART_TYPE_UNSPECIFIED (0):
                The zero value. No type specified. Do not
                use.
            PIE (1):
                A Pie type PieChart.
            DONUT (2):
                Similar to PIE, but the DONUT type PieChart
                has a hole in the middle.
        """

        PIE_CHART_TYPE_UNSPECIFIED = 0
        PIE = 1
        DONUT = 2

    class PieChartDataSet(proto.Message):
        r"""Groups a time series query definition.

        Attributes:
            time_series_query (google.cloud.monitoring_dashboard_v1.types.TimeSeriesQuery):
                Required. The query for the PieChart. See,
                ``google.monitoring.dashboard.v1.TimeSeriesQuery``.
            slice_name_template (str):
                Optional. A template for the name of the slice. This name
                will be displayed in the legend and the tooltip of the pie
                chart. It replaces the auto-generated names for the slices.
                For example, if the template is set to
                ``${resource.labels.zone}``, the zone's value will be used
                for the name instead of the default name.
            min_alignment_period (google.protobuf.duration_pb2.Duration):
                Optional. The lower bound on data point frequency for this
                data set, implemented by specifying the minimum alignment
                period to use in a time series query. For example, if the
                data is published once every 10 minutes, the
                ``min_alignment_period`` should be at least 10 minutes. It
                would not make sense to fetch and align data at one minute
                intervals.
        """

        time_series_query: metrics.TimeSeriesQuery = proto.Field(
            proto.MESSAGE,
            number=1,
            message=metrics.TimeSeriesQuery,
        )
        slice_name_template: str = proto.Field(
            proto.STRING,
            number=2,
        )
        min_alignment_period: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=3,
            message=duration_pb2.Duration,
        )

    data_sets: MutableSequence[PieChartDataSet] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=PieChartDataSet,
    )
    chart_type: PieChartType = proto.Field(
        proto.ENUM,
        number=2,
        enum=PieChartType,
    )
    show_labels: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
