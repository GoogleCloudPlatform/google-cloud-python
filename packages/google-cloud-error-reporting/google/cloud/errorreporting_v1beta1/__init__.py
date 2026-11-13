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

from google.cloud.errorreporting_v1beta1 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.errorreporting_v1beta1.services.error_group_service",
    "google.cloud.errorreporting_v1beta1.services.error_stats_service",
    "google.cloud.errorreporting_v1beta1.services.report_errors_service",
    "google.cloud.errorreporting_v1beta1.types.common",
    "google.cloud.errorreporting_v1beta1.types.error_group_service",
    "google.cloud.errorreporting_v1beta1.types.error_stats_service",
    "google.cloud.errorreporting_v1beta1.types.report_errors_service",
}


from .services.error_group_service import (
    ErrorGroupServiceAsyncClient,
    ErrorGroupServiceClient,
)
from .services.error_stats_service import (
    ErrorStatsServiceAsyncClient,
    ErrorStatsServiceClient,
)
from .services.report_errors_service import (
    ReportErrorsServiceAsyncClient,
    ReportErrorsServiceClient,
)
from .types.common import (
    ErrorContext,
    ErrorEvent,
    ErrorGroup,
    HttpRequestContext,
    ResolutionStatus,
    ServiceContext,
    SourceLocation,
    TrackingIssue,
)
from .types.error_group_service import GetGroupRequest, UpdateGroupRequest
from .types.error_stats_service import (
    DeleteEventsRequest,
    DeleteEventsResponse,
    ErrorGroupOrder,
    ErrorGroupStats,
    ListEventsRequest,
    ListEventsResponse,
    ListGroupStatsRequest,
    ListGroupStatsResponse,
    QueryTimeRange,
    ServiceContextFilter,
    TimedCount,
    TimedCountAlignment,
)
from .types.report_errors_service import (
    ReportedErrorEvent,
    ReportErrorEventRequest,
    ReportErrorEventResponse,
)

__all__ = (
    "ErrorGroupServiceAsyncClient",
    "ErrorStatsServiceAsyncClient",
    "ReportErrorsServiceAsyncClient",
    "DeleteEventsRequest",
    "DeleteEventsResponse",
    "ErrorContext",
    "ErrorEvent",
    "ErrorGroup",
    "ErrorGroupOrder",
    "ErrorGroupServiceClient",
    "ErrorGroupStats",
    "ErrorStatsServiceClient",
    "GetGroupRequest",
    "HttpRequestContext",
    "ListEventsRequest",
    "ListEventsResponse",
    "ListGroupStatsRequest",
    "ListGroupStatsResponse",
    "QueryTimeRange",
    "ReportErrorEventRequest",
    "ReportErrorEventResponse",
    "ReportErrorsServiceClient",
    "ReportedErrorEvent",
    "ResolutionStatus",
    "ServiceContext",
    "ServiceContextFilter",
    "SourceLocation",
    "TimedCount",
    "TimedCountAlignment",
    "TrackingIssue",
    "UpdateGroupRequest",
)

api_core.check_python_version("google.cloud.errorreporting_v1beta1")
api_core.check_dependency_versions("google.cloud.errorreporting_v1beta1")
