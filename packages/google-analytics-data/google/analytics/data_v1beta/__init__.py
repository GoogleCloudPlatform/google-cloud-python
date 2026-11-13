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

from google.analytics.data_v1beta import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.analytics.data_v1beta.services.beta_analytics_data",
    "google.analytics.data_v1beta.types.analytics_data_api",
    "google.analytics.data_v1beta.types.data",
}


from .services.beta_analytics_data import (
    BetaAnalyticsDataAsyncClient,
    BetaAnalyticsDataClient,
)
from .types.analytics_data_api import (
    AudienceDimension,
    AudienceDimensionValue,
    AudienceExport,
    AudienceExportMetadata,
    AudienceRow,
    BatchRunPivotReportsRequest,
    BatchRunPivotReportsResponse,
    BatchRunReportsRequest,
    BatchRunReportsResponse,
    CheckCompatibilityRequest,
    CheckCompatibilityResponse,
    CreateAudienceExportRequest,
    GetAudienceExportRequest,
    GetMetadataRequest,
    ListAudienceExportsRequest,
    ListAudienceExportsResponse,
    Metadata,
    QueryAudienceExportRequest,
    QueryAudienceExportResponse,
    RunPivotReportRequest,
    RunPivotReportResponse,
    RunRealtimeReportRequest,
    RunRealtimeReportResponse,
    RunReportRequest,
    RunReportResponse,
)
from .types.data import (
    Cohort,
    CohortReportSettings,
    CohortSpec,
    CohortsRange,
    Comparison,
    ComparisonMetadata,
    Compatibility,
    DateRange,
    Dimension,
    DimensionCompatibility,
    DimensionExpression,
    DimensionHeader,
    DimensionMetadata,
    DimensionValue,
    Filter,
    FilterExpression,
    FilterExpressionList,
    Metric,
    MetricAggregation,
    MetricCompatibility,
    MetricHeader,
    MetricMetadata,
    MetricType,
    MetricValue,
    MinuteRange,
    NumericValue,
    OrderBy,
    Pivot,
    PivotDimensionHeader,
    PivotHeader,
    PropertyQuota,
    QuotaStatus,
    ResponseMetaData,
    RestrictedMetricType,
    Row,
    SamplingMetadata,
)

__all__ = (
    "BetaAnalyticsDataAsyncClient",
    "AudienceDimension",
    "AudienceDimensionValue",
    "AudienceExport",
    "AudienceExportMetadata",
    "AudienceRow",
    "BatchRunPivotReportsRequest",
    "BatchRunPivotReportsResponse",
    "BatchRunReportsRequest",
    "BatchRunReportsResponse",
    "BetaAnalyticsDataClient",
    "CheckCompatibilityRequest",
    "CheckCompatibilityResponse",
    "Cohort",
    "CohortReportSettings",
    "CohortSpec",
    "CohortsRange",
    "Comparison",
    "ComparisonMetadata",
    "Compatibility",
    "CreateAudienceExportRequest",
    "DateRange",
    "Dimension",
    "DimensionCompatibility",
    "DimensionExpression",
    "DimensionHeader",
    "DimensionMetadata",
    "DimensionValue",
    "Filter",
    "FilterExpression",
    "FilterExpressionList",
    "GetAudienceExportRequest",
    "GetMetadataRequest",
    "ListAudienceExportsRequest",
    "ListAudienceExportsResponse",
    "Metadata",
    "Metric",
    "MetricAggregation",
    "MetricCompatibility",
    "MetricHeader",
    "MetricMetadata",
    "MetricType",
    "MetricValue",
    "MinuteRange",
    "NumericValue",
    "OrderBy",
    "Pivot",
    "PivotDimensionHeader",
    "PivotHeader",
    "PropertyQuota",
    "QueryAudienceExportRequest",
    "QueryAudienceExportResponse",
    "QuotaStatus",
    "ResponseMetaData",
    "RestrictedMetricType",
    "Row",
    "RunPivotReportRequest",
    "RunPivotReportResponse",
    "RunRealtimeReportRequest",
    "RunRealtimeReportResponse",
    "RunReportRequest",
    "RunReportResponse",
    "SamplingMetadata",
)

api_core.check_python_version("google.analytics.data_v1beta")
api_core.check_dependency_versions("google.analytics.data_v1beta")
