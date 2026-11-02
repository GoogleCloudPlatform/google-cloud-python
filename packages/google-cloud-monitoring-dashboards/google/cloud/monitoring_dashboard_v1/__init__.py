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
import google.api_core as api_core

from google.cloud.monitoring_dashboard_v1 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.monitoring_dashboard_v1.services.dashboards_service",
    "google.cloud.monitoring_dashboard_v1.types.alertchart",
    "google.cloud.monitoring_dashboard_v1.types.collapsible_group",
    "google.cloud.monitoring_dashboard_v1.types.common",
    "google.cloud.monitoring_dashboard_v1.types.dashboard",
    "google.cloud.monitoring_dashboard_v1.types.dashboard_filter",
    "google.cloud.monitoring_dashboard_v1.types.dashboards_service",
    "google.cloud.monitoring_dashboard_v1.types.drilldowns",
    "google.cloud.monitoring_dashboard_v1.types.error_reporting_panel",
    "google.cloud.monitoring_dashboard_v1.types.incident_list",
    "google.cloud.monitoring_dashboard_v1.types.layouts",
    "google.cloud.monitoring_dashboard_v1.types.logs_panel",
    "google.cloud.monitoring_dashboard_v1.types.metrics",
    "google.cloud.monitoring_dashboard_v1.types.piechart",
    "google.cloud.monitoring_dashboard_v1.types.scorecard",
    "google.cloud.monitoring_dashboard_v1.types.section_header",
    "google.cloud.monitoring_dashboard_v1.types.service",
    "google.cloud.monitoring_dashboard_v1.types.single_view_group",
    "google.cloud.monitoring_dashboard_v1.types.table",
    "google.cloud.monitoring_dashboard_v1.types.table_display_options",
    "google.cloud.monitoring_dashboard_v1.types.text",
    "google.cloud.monitoring_dashboard_v1.types.widget",
    "google.cloud.monitoring_dashboard_v1.types.xychart",
}


from .services.dashboards_service import (
    DashboardsServiceAsyncClient,
    DashboardsServiceClient,
)
from .types.alertchart import AlertChart
from .types.collapsible_group import CollapsibleGroup
from .types.common import Aggregation, PickTimeSeriesFilter, StatisticalTimeSeriesFilter
from .types.dashboard import Dashboard
from .types.dashboard_filter import DashboardFilter
from .types.dashboards_service import (
    CreateDashboardRequest,
    DeleteDashboardRequest,
    GetDashboardRequest,
    ListDashboardsRequest,
    ListDashboardsResponse,
    UpdateDashboardRequest,
)
from .types.error_reporting_panel import ErrorReportingPanel
from .types.incident_list import IncidentList
from .types.layouts import ColumnLayout, GridLayout, MosaicLayout, RowLayout
from .types.logs_panel import LogsPanel
from .types.metrics import (
    SparkChartType,
    Threshold,
    TimeSeriesFilter,
    TimeSeriesFilterRatio,
    TimeSeriesQuery,
)
from .types.piechart import PieChart
from .types.scorecard import Scorecard
from .types.section_header import SectionHeader
from .types.single_view_group import SingleViewGroup
from .types.table import TimeSeriesTable
from .types.table_display_options import TableDisplayOptions
from .types.text import Text
from .types.widget import Widget
from .types.xychart import ChartOptions, XyChart

__all__ = (
    "DashboardsServiceAsyncClient",
    "Aggregation",
    "AlertChart",
    "ChartOptions",
    "CollapsibleGroup",
    "ColumnLayout",
    "CreateDashboardRequest",
    "Dashboard",
    "DashboardFilter",
    "DashboardsServiceClient",
    "DeleteDashboardRequest",
    "ErrorReportingPanel",
    "GetDashboardRequest",
    "GridLayout",
    "IncidentList",
    "ListDashboardsRequest",
    "ListDashboardsResponse",
    "LogsPanel",
    "MosaicLayout",
    "PickTimeSeriesFilter",
    "PieChart",
    "RowLayout",
    "Scorecard",
    "SectionHeader",
    "SingleViewGroup",
    "SparkChartType",
    "StatisticalTimeSeriesFilter",
    "TableDisplayOptions",
    "Text",
    "Threshold",
    "TimeSeriesFilter",
    "TimeSeriesFilterRatio",
    "TimeSeriesQuery",
    "TimeSeriesTable",
    "UpdateDashboardRequest",
    "Widget",
    "XyChart",
)

api_core.check_python_version("google.cloud.monitoring_dashboard_v1")
api_core.check_dependency_versions("google.cloud.monitoring_dashboard_v1")
