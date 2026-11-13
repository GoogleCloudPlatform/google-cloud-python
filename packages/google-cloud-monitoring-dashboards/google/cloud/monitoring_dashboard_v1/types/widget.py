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

import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.monitoring_dashboard_v1.types import (
    alertchart,
    piechart,
    table,
    xychart,
)
from google.cloud.monitoring_dashboard_v1.types import (
    collapsible_group as gmd_collapsible_group,
)
from google.cloud.monitoring_dashboard_v1.types import (
    error_reporting_panel as gmd_error_reporting_panel,
)
from google.cloud.monitoring_dashboard_v1.types import (
    incident_list as gmd_incident_list,
)
from google.cloud.monitoring_dashboard_v1.types import logs_panel as gmd_logs_panel
from google.cloud.monitoring_dashboard_v1.types import scorecard as gmd_scorecard
from google.cloud.monitoring_dashboard_v1.types import (
    section_header as gmd_section_header,
)
from google.cloud.monitoring_dashboard_v1.types import (
    single_view_group as gmd_single_view_group,
)
from google.cloud.monitoring_dashboard_v1.types import text as gmd_text

__protobuf__ = proto.module(
    package="google.monitoring.dashboard.v1",
    manifest={
        "Widget",
    },
)


class Widget(proto.Message):
    r"""Widget contains a single dashboard component and
    configuration of how to present the component in the dashboard.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        title (str):
            Optional. The title of the widget.
        xy_chart (google.cloud.monitoring_dashboard_v1.types.XyChart):
            A chart of time series data.

            This field is a member of `oneof`_ ``content``.
        scorecard (google.cloud.monitoring_dashboard_v1.types.Scorecard):
            A scorecard summarizing time series data.

            This field is a member of `oneof`_ ``content``.
        text (google.cloud.monitoring_dashboard_v1.types.Text):
            A raw string or markdown displaying textual
            content.

            This field is a member of `oneof`_ ``content``.
        blank (google.protobuf.empty_pb2.Empty):
            A blank space.

            This field is a member of `oneof`_ ``content``.
        alert_chart (google.cloud.monitoring_dashboard_v1.types.AlertChart):
            A chart of alert policy data.

            This field is a member of `oneof`_ ``content``.
        time_series_table (google.cloud.monitoring_dashboard_v1.types.TimeSeriesTable):
            A widget that displays time series data in a
            tabular format.

            This field is a member of `oneof`_ ``content``.
        collapsible_group (google.cloud.monitoring_dashboard_v1.types.CollapsibleGroup):
            A widget that groups the other widgets. All
            widgets that are within the area spanned by the
            grouping widget are considered member widgets.

            This field is a member of `oneof`_ ``content``.
        logs_panel (google.cloud.monitoring_dashboard_v1.types.LogsPanel):
            A widget that shows a stream of logs.

            This field is a member of `oneof`_ ``content``.
        incident_list (google.cloud.monitoring_dashboard_v1.types.IncidentList):
            A widget that shows list of alerts.

            This field is a member of `oneof`_ ``content``.
        pie_chart (google.cloud.monitoring_dashboard_v1.types.PieChart):
            A widget that displays timeseries data as a
            pie chart.

            This field is a member of `oneof`_ ``content``.
        error_reporting_panel (google.cloud.monitoring_dashboard_v1.types.ErrorReportingPanel):
            A widget that displays a list of error
            groups.

            This field is a member of `oneof`_ ``content``.
        section_header (google.cloud.monitoring_dashboard_v1.types.SectionHeader):
            A widget that defines a section header for
            easier navigation of the dashboard.

            This field is a member of `oneof`_ ``content``.
        single_view_group (google.cloud.monitoring_dashboard_v1.types.SingleViewGroup):
            A widget that groups the other widgets by
            using a dropdown menu.

            This field is a member of `oneof`_ ``content``.
        id (str):
            Optional. The widget id. Ids may be made up
            of alphanumerics, dashes and underscores. Widget
            ids are optional.
    """

    title: str = proto.Field(
        proto.STRING,
        number=1,
    )
    xy_chart: xychart.XyChart = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="content",
        message=xychart.XyChart,
    )
    scorecard: gmd_scorecard.Scorecard = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="content",
        message=gmd_scorecard.Scorecard,
    )
    text: gmd_text.Text = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="content",
        message=gmd_text.Text,
    )
    blank: empty_pb2.Empty = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="content",
        message=empty_pb2.Empty,
    )
    alert_chart: alertchart.AlertChart = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="content",
        message=alertchart.AlertChart,
    )
    time_series_table: table.TimeSeriesTable = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="content",
        message=table.TimeSeriesTable,
    )
    collapsible_group: gmd_collapsible_group.CollapsibleGroup = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="content",
        message=gmd_collapsible_group.CollapsibleGroup,
    )
    logs_panel: gmd_logs_panel.LogsPanel = proto.Field(
        proto.MESSAGE,
        number=10,
        oneof="content",
        message=gmd_logs_panel.LogsPanel,
    )
    incident_list: gmd_incident_list.IncidentList = proto.Field(
        proto.MESSAGE,
        number=12,
        oneof="content",
        message=gmd_incident_list.IncidentList,
    )
    pie_chart: piechart.PieChart = proto.Field(
        proto.MESSAGE,
        number=14,
        oneof="content",
        message=piechart.PieChart,
    )
    error_reporting_panel: gmd_error_reporting_panel.ErrorReportingPanel = proto.Field(
        proto.MESSAGE,
        number=19,
        oneof="content",
        message=gmd_error_reporting_panel.ErrorReportingPanel,
    )
    section_header: gmd_section_header.SectionHeader = proto.Field(
        proto.MESSAGE,
        number=21,
        oneof="content",
        message=gmd_section_header.SectionHeader,
    )
    single_view_group: gmd_single_view_group.SingleViewGroup = proto.Field(
        proto.MESSAGE,
        number=22,
        oneof="content",
        message=gmd_single_view_group.SingleViewGroup,
    )
    id: str = proto.Field(
        proto.STRING,
        number=17,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
