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
from google.cloud.errorreporting import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.errorreporting_v1beta1.services.error_group_service.async_client import (
    ErrorGroupServiceAsyncClient,
)
from google.cloud.errorreporting_v1beta1.services.error_group_service.client import (
    ErrorGroupServiceClient,
)
from google.cloud.errorreporting_v1beta1.services.error_stats_service.async_client import (
    ErrorStatsServiceAsyncClient,
)
from google.cloud.errorreporting_v1beta1.services.error_stats_service.client import (
    ErrorStatsServiceClient,
)
from google.cloud.errorreporting_v1beta1.services.report_errors_service.async_client import (
    ReportErrorsServiceAsyncClient,
)
from google.cloud.errorreporting_v1beta1.services.report_errors_service.client import (
    ReportErrorsServiceClient,
)
from google.cloud.errorreporting_v1beta1.types.common import (
    ErrorContext,
    ErrorEvent,
    ErrorGroup,
    HttpRequestContext,
    ResolutionStatus,
    ServiceContext,
    SourceLocation,
    TrackingIssue,
)
from google.cloud.errorreporting_v1beta1.types.error_group_service import (
    GetGroupRequest,
    UpdateGroupRequest,
)
from google.cloud.errorreporting_v1beta1.types.error_stats_service import (
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
from google.cloud.errorreporting_v1beta1.types.report_errors_service import (
    ReportedErrorEvent,
    ReportErrorEventRequest,
    ReportErrorEventResponse,
)

__all__ = (
    "ErrorGroupServiceClient",
    "ErrorGroupServiceAsyncClient",
    "ErrorStatsServiceClient",
    "ErrorStatsServiceAsyncClient",
    "ReportErrorsServiceClient",
    "ReportErrorsServiceAsyncClient",
    "ErrorContext",
    "ErrorEvent",
    "ErrorGroup",
    "HttpRequestContext",
    "ServiceContext",
    "SourceLocation",
    "TrackingIssue",
    "ResolutionStatus",
    "GetGroupRequest",
    "UpdateGroupRequest",
    "DeleteEventsRequest",
    "DeleteEventsResponse",
    "ErrorGroupStats",
    "ListEventsRequest",
    "ListEventsResponse",
    "ListGroupStatsRequest",
    "ListGroupStatsResponse",
    "QueryTimeRange",
    "ServiceContextFilter",
    "TimedCount",
    "ErrorGroupOrder",
    "TimedCountAlignment",
    "ReportedErrorEvent",
    "ReportErrorEventRequest",
    "ReportErrorEventResponse",
)
