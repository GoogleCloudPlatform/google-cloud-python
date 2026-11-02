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
from google.cloud.monitoring_dashboard_v1.types import (
    table_display_options as gmd_table_display_options,
)

__protobuf__ = proto.module(
    package="google.monitoring.dashboard.v1",
    manifest={
        "TimeSeriesTable",
    },
)


class TimeSeriesTable(proto.Message):
    r"""A table that displays time series data.

    Attributes:
        data_sets (MutableSequence[google.cloud.monitoring_dashboard_v1.types.TimeSeriesTable.TableDataSet]):
            Required. The data displayed in this table.
        metric_visualization (google.cloud.monitoring_dashboard_v1.types.TimeSeriesTable.MetricVisualization):
            Optional. Store rendering strategy
        column_settings (MutableSequence[google.cloud.monitoring_dashboard_v1.types.TimeSeriesTable.ColumnSettings]):
            Optional. The list of the persistent column
            settings for the table.
    """

    class MetricVisualization(proto.Enum):
        r"""Enum for metric metric_visualization

        Values:
            METRIC_VISUALIZATION_UNSPECIFIED (0):
                Unspecified state
            NUMBER (1):
                Default text rendering
            BAR (2):
                Horizontal bar rendering
        """

        METRIC_VISUALIZATION_UNSPECIFIED = 0
        NUMBER = 1
        BAR = 2

    class TableDataSet(proto.Message):
        r"""Groups a time series query definition with table options.

        Attributes:
            time_series_query (google.cloud.monitoring_dashboard_v1.types.TimeSeriesQuery):
                Required. Fields for querying time series
                data from the Stackdriver metrics API.
            table_template (str):
                Optional. A template string for naming ``TimeSeries`` in the
                resulting data set. This should be a string with
                interpolations of the form ``${label_name}``, which will
                resolve to the label's value i.e.
                "${resource.labels.project_id}.".
            min_alignment_period (google.protobuf.duration_pb2.Duration):
                Optional. The lower bound on data point frequency for this
                data set, implemented by specifying the minimum alignment
                period to use in a time series query For example, if the
                data is published once every 10 minutes, the
                ``min_alignment_period`` should be at least 10 minutes. It
                would not make sense to fetch and align data at one minute
                intervals.
            table_display_options (google.cloud.monitoring_dashboard_v1.types.TableDisplayOptions):
                Optional. Table display options for
                configuring how the table is rendered.
        """

        time_series_query: metrics.TimeSeriesQuery = proto.Field(
            proto.MESSAGE,
            number=1,
            message=metrics.TimeSeriesQuery,
        )
        table_template: str = proto.Field(
            proto.STRING,
            number=2,
        )
        min_alignment_period: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=3,
            message=duration_pb2.Duration,
        )
        table_display_options: gmd_table_display_options.TableDisplayOptions = (
            proto.Field(
                proto.MESSAGE,
                number=4,
                message=gmd_table_display_options.TableDisplayOptions,
            )
        )

    class ColumnSettings(proto.Message):
        r"""The persistent settings for a table's columns.

        Attributes:
            column (str):
                Required. The id of the column.
            visible (bool):
                Required. Whether the column should be
                visible on page load.
        """

        column: str = proto.Field(
            proto.STRING,
            number=1,
        )
        visible: bool = proto.Field(
            proto.BOOL,
            number=2,
        )

    data_sets: MutableSequence[TableDataSet] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=TableDataSet,
    )
    metric_visualization: MetricVisualization = proto.Field(
        proto.ENUM,
        number=2,
        enum=MetricVisualization,
    )
    column_settings: MutableSequence[ColumnSettings] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=ColumnSettings,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
