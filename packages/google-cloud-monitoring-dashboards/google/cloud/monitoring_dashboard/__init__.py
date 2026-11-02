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
from google.cloud.monitoring_dashboard import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.monitoring_dashboard_v1.services.dashboards_service.async_client import (
    DashboardsServiceAsyncClient,
)
from google.cloud.monitoring_dashboard_v1.services.dashboards_service.client import (
    DashboardsServiceClient,
)
from google.cloud.monitoring_dashboard_v1.types.alertchart import AlertChart
from google.cloud.monitoring_dashboard_v1.types.collapsible_group import (
    CollapsibleGroup,
)
from google.cloud.monitoring_dashboard_v1.types.common import (
    Aggregation,
    PickTimeSeriesFilter,
    StatisticalTimeSeriesFilter,
)
from google.cloud.monitoring_dashboard_v1.types.dashboard import Dashboard
from google.cloud.monitoring_dashboard_v1.types.dashboard_filter import DashboardFilter
from google.cloud.monitoring_dashboard_v1.types.dashboards_service import (
    CreateDashboardRequest,
    DeleteDashboardRequest,
    GetDashboardRequest,
    ListDashboardsRequest,
    ListDashboardsResponse,
    UpdateDashboardRequest,
)
from google.cloud.monitoring_dashboard_v1.types.error_reporting_panel import (
    ErrorReportingPanel,
)
from google.cloud.monitoring_dashboard_v1.types.incident_list import IncidentList
from google.cloud.monitoring_dashboard_v1.types.layouts import (
    ColumnLayout,
    GridLayout,
    MosaicLayout,
    RowLayout,
)
from google.cloud.monitoring_dashboard_v1.types.logs_panel import LogsPanel
from google.cloud.monitoring_dashboard_v1.types.metrics import (
    SparkChartType,
    Threshold,
    TimeSeriesFilter,
    TimeSeriesFilterRatio,
    TimeSeriesQuery,
)
from google.cloud.monitoring_dashboard_v1.types.piechart import PieChart
from google.cloud.monitoring_dashboard_v1.types.scorecard import Scorecard
from google.cloud.monitoring_dashboard_v1.types.section_header import SectionHeader
from google.cloud.monitoring_dashboard_v1.types.single_view_group import SingleViewGroup
from google.cloud.monitoring_dashboard_v1.types.table import TimeSeriesTable
from google.cloud.monitoring_dashboard_v1.types.table_display_options import (
    TableDisplayOptions,
)
from google.cloud.monitoring_dashboard_v1.types.text import Text
from google.cloud.monitoring_dashboard_v1.types.widget import Widget
from google.cloud.monitoring_dashboard_v1.types.xychart import ChartOptions, XyChart

__all__ = (
    "DashboardsServiceClient",
    "DashboardsServiceAsyncClient",
    "AlertChart",
    "CollapsibleGroup",
    "Aggregation",
    "PickTimeSeriesFilter",
    "StatisticalTimeSeriesFilter",
    "Dashboard",
    "DashboardFilter",
    "CreateDashboardRequest",
    "DeleteDashboardRequest",
    "GetDashboardRequest",
    "ListDashboardsRequest",
    "ListDashboardsResponse",
    "UpdateDashboardRequest",
    "ErrorReportingPanel",
    "IncidentList",
    "ColumnLayout",
    "GridLayout",
    "MosaicLayout",
    "RowLayout",
    "LogsPanel",
    "Threshold",
    "TimeSeriesFilter",
    "TimeSeriesFilterRatio",
    "TimeSeriesQuery",
    "SparkChartType",
    "PieChart",
    "Scorecard",
    "SectionHeader",
    "SingleViewGroup",
    "TimeSeriesTable",
    "TableDisplayOptions",
    "Text",
    "Widget",
    "ChartOptions",
    "XyChart",
)
