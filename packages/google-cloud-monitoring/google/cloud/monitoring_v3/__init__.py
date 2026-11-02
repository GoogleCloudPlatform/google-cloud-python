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

from google.cloud.monitoring_v3 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.monitoring_v3.services.alert_policy_service",
    "google.cloud.monitoring_v3.services.group_service",
    "google.cloud.monitoring_v3.services.metric_service",
    "google.cloud.monitoring_v3.services.notification_channel_service",
    "google.cloud.monitoring_v3.services.query_service",
    "google.cloud.monitoring_v3.services.service_monitoring_service",
    "google.cloud.monitoring_v3.services.snooze_service",
    "google.cloud.monitoring_v3.services.uptime_check_service",
    "google.cloud.monitoring_v3.types.alert",
    "google.cloud.monitoring_v3.types.alert_service",
    "google.cloud.monitoring_v3.types.common",
    "google.cloud.monitoring_v3.types.dropped_labels",
    "google.cloud.monitoring_v3.types.group",
    "google.cloud.monitoring_v3.types.group_service",
    "google.cloud.monitoring_v3.types.metric",
    "google.cloud.monitoring_v3.types.metric_service",
    "google.cloud.monitoring_v3.types.mutation_record",
    "google.cloud.monitoring_v3.types.notification",
    "google.cloud.monitoring_v3.types.notification_service",
    "google.cloud.monitoring_v3.types.query_service",
    "google.cloud.monitoring_v3.types.service",
    "google.cloud.monitoring_v3.types.service_service",
    "google.cloud.monitoring_v3.types.snooze",
    "google.cloud.monitoring_v3.types.snooze_service",
    "google.cloud.monitoring_v3.types.span_context",
    "google.cloud.monitoring_v3.types.uptime",
    "google.cloud.monitoring_v3.types.uptime_service",
}


from .services.alert_policy_service import (
    AlertPolicyServiceAsyncClient,
    AlertPolicyServiceClient,
)
from .services.group_service import GroupServiceAsyncClient, GroupServiceClient
from .services.metric_service import MetricServiceAsyncClient, MetricServiceClient
from .services.notification_channel_service import (
    NotificationChannelServiceAsyncClient,
    NotificationChannelServiceClient,
)
from .services.query_service import QueryServiceAsyncClient, QueryServiceClient
from .services.service_monitoring_service import (
    ServiceMonitoringServiceAsyncClient,
    ServiceMonitoringServiceClient,
)
from .services.snooze_service import SnoozeServiceAsyncClient, SnoozeServiceClient
from .services.uptime_check_service import (
    UptimeCheckServiceAsyncClient,
    UptimeCheckServiceClient,
)
from .types.alert import AlertPolicy
from .types.alert_service import (
    CreateAlertPolicyRequest,
    DeleteAlertPolicyRequest,
    GetAlertPolicyRequest,
    ListAlertPoliciesRequest,
    ListAlertPoliciesResponse,
    UpdateAlertPolicyRequest,
)
from .types.common import (
    Aggregation,
    ComparisonType,
    ServiceTier,
    TimeInterval,
    TypedValue,
)
from .types.dropped_labels import DroppedLabels
from .types.group import Group
from .types.group_service import (
    CreateGroupRequest,
    DeleteGroupRequest,
    GetGroupRequest,
    ListGroupMembersRequest,
    ListGroupMembersResponse,
    ListGroupsRequest,
    ListGroupsResponse,
    UpdateGroupRequest,
)
from .types.metric import (
    LabelValue,
    Point,
    QueryError,
    TextLocator,
    TimeSeries,
    TimeSeriesData,
    TimeSeriesDescriptor,
)
from .types.metric_service import (
    CreateMetricDescriptorRequest,
    CreateTimeSeriesError,
    CreateTimeSeriesRequest,
    CreateTimeSeriesSummary,
    DeleteMetricDescriptorRequest,
    GetMetricDescriptorRequest,
    GetMonitoredResourceDescriptorRequest,
    ListMetricDescriptorsRequest,
    ListMetricDescriptorsResponse,
    ListMonitoredResourceDescriptorsRequest,
    ListMonitoredResourceDescriptorsResponse,
    ListTimeSeriesRequest,
    ListTimeSeriesResponse,
    QueryErrorList,
    QueryTimeSeriesRequest,
    QueryTimeSeriesResponse,
)
from .types.mutation_record import MutationRecord
from .types.notification import NotificationChannel, NotificationChannelDescriptor
from .types.notification_service import (
    CreateNotificationChannelRequest,
    DeleteNotificationChannelRequest,
    GetNotificationChannelDescriptorRequest,
    GetNotificationChannelRequest,
    GetNotificationChannelVerificationCodeRequest,
    GetNotificationChannelVerificationCodeResponse,
    ListNotificationChannelDescriptorsRequest,
    ListNotificationChannelDescriptorsResponse,
    ListNotificationChannelsRequest,
    ListNotificationChannelsResponse,
    SendNotificationChannelVerificationCodeRequest,
    UpdateNotificationChannelRequest,
    VerifyNotificationChannelRequest,
)
from .types.service import (
    BasicSli,
    DistributionCut,
    Range,
    RequestBasedSli,
    Service,
    ServiceLevelIndicator,
    ServiceLevelObjective,
    TimeSeriesRatio,
    WindowsBasedSli,
)
from .types.service_service import (
    CreateServiceLevelObjectiveRequest,
    CreateServiceRequest,
    DeleteServiceLevelObjectiveRequest,
    DeleteServiceRequest,
    GetServiceLevelObjectiveRequest,
    GetServiceRequest,
    ListServiceLevelObjectivesRequest,
    ListServiceLevelObjectivesResponse,
    ListServicesRequest,
    ListServicesResponse,
    UpdateServiceLevelObjectiveRequest,
    UpdateServiceRequest,
)
from .types.snooze import Snooze
from .types.snooze_service import (
    CreateSnoozeRequest,
    GetSnoozeRequest,
    ListSnoozesRequest,
    ListSnoozesResponse,
    UpdateSnoozeRequest,
)
from .types.span_context import SpanContext
from .types.uptime import (
    GroupResourceType,
    InternalChecker,
    SyntheticMonitorTarget,
    UptimeCheckConfig,
    UptimeCheckIp,
    UptimeCheckRegion,
)
from .types.uptime_service import (
    CreateUptimeCheckConfigRequest,
    DeleteUptimeCheckConfigRequest,
    GetUptimeCheckConfigRequest,
    ListUptimeCheckConfigsRequest,
    ListUptimeCheckConfigsResponse,
    ListUptimeCheckIpsRequest,
    ListUptimeCheckIpsResponse,
    UpdateUptimeCheckConfigRequest,
)

__all__ = (
    "AlertPolicyServiceAsyncClient",
    "GroupServiceAsyncClient",
    "MetricServiceAsyncClient",
    "NotificationChannelServiceAsyncClient",
    "QueryServiceAsyncClient",
    "ServiceMonitoringServiceAsyncClient",
    "SnoozeServiceAsyncClient",
    "UptimeCheckServiceAsyncClient",
    "Aggregation",
    "AlertPolicy",
    "AlertPolicyServiceClient",
    "BasicSli",
    "ComparisonType",
    "CreateAlertPolicyRequest",
    "CreateGroupRequest",
    "CreateMetricDescriptorRequest",
    "CreateNotificationChannelRequest",
    "CreateServiceLevelObjectiveRequest",
    "CreateServiceRequest",
    "CreateSnoozeRequest",
    "CreateTimeSeriesError",
    "CreateTimeSeriesRequest",
    "CreateTimeSeriesSummary",
    "CreateUptimeCheckConfigRequest",
    "DeleteAlertPolicyRequest",
    "DeleteGroupRequest",
    "DeleteMetricDescriptorRequest",
    "DeleteNotificationChannelRequest",
    "DeleteServiceLevelObjectiveRequest",
    "DeleteServiceRequest",
    "DeleteUptimeCheckConfigRequest",
    "DistributionCut",
    "DroppedLabels",
    "GetAlertPolicyRequest",
    "GetGroupRequest",
    "GetMetricDescriptorRequest",
    "GetMonitoredResourceDescriptorRequest",
    "GetNotificationChannelDescriptorRequest",
    "GetNotificationChannelRequest",
    "GetNotificationChannelVerificationCodeRequest",
    "GetNotificationChannelVerificationCodeResponse",
    "GetServiceLevelObjectiveRequest",
    "GetServiceRequest",
    "GetSnoozeRequest",
    "GetUptimeCheckConfigRequest",
    "Group",
    "GroupResourceType",
    "GroupServiceClient",
    "InternalChecker",
    "LabelValue",
    "ListAlertPoliciesRequest",
    "ListAlertPoliciesResponse",
    "ListGroupMembersRequest",
    "ListGroupMembersResponse",
    "ListGroupsRequest",
    "ListGroupsResponse",
    "ListMetricDescriptorsRequest",
    "ListMetricDescriptorsResponse",
    "ListMonitoredResourceDescriptorsRequest",
    "ListMonitoredResourceDescriptorsResponse",
    "ListNotificationChannelDescriptorsRequest",
    "ListNotificationChannelDescriptorsResponse",
    "ListNotificationChannelsRequest",
    "ListNotificationChannelsResponse",
    "ListServiceLevelObjectivesRequest",
    "ListServiceLevelObjectivesResponse",
    "ListServicesRequest",
    "ListServicesResponse",
    "ListSnoozesRequest",
    "ListSnoozesResponse",
    "ListTimeSeriesRequest",
    "ListTimeSeriesResponse",
    "ListUptimeCheckConfigsRequest",
    "ListUptimeCheckConfigsResponse",
    "ListUptimeCheckIpsRequest",
    "ListUptimeCheckIpsResponse",
    "MetricServiceClient",
    "MutationRecord",
    "NotificationChannel",
    "NotificationChannelDescriptor",
    "NotificationChannelServiceClient",
    "Point",
    "QueryError",
    "QueryErrorList",
    "QueryServiceClient",
    "QueryTimeSeriesRequest",
    "QueryTimeSeriesResponse",
    "Range",
    "RequestBasedSli",
    "SendNotificationChannelVerificationCodeRequest",
    "Service",
    "ServiceLevelIndicator",
    "ServiceLevelObjective",
    "ServiceMonitoringServiceClient",
    "ServiceTier",
    "Snooze",
    "SnoozeServiceClient",
    "SpanContext",
    "SyntheticMonitorTarget",
    "TextLocator",
    "TimeInterval",
    "TimeSeries",
    "TimeSeriesData",
    "TimeSeriesDescriptor",
    "TimeSeriesRatio",
    "TypedValue",
    "UpdateAlertPolicyRequest",
    "UpdateGroupRequest",
    "UpdateNotificationChannelRequest",
    "UpdateServiceLevelObjectiveRequest",
    "UpdateServiceRequest",
    "UpdateSnoozeRequest",
    "UpdateUptimeCheckConfigRequest",
    "UptimeCheckConfig",
    "UptimeCheckIp",
    "UptimeCheckRegion",
    "UptimeCheckServiceClient",
    "VerifyNotificationChannelRequest",
    "WindowsBasedSli",
)

api_core.check_python_version("google.cloud.monitoring_v3")
api_core.check_dependency_versions("google.cloud.monitoring_v3")
