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
from google.cloud.databasecenter import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.databasecenter_v1beta.services.database_center.async_client import (
    DatabaseCenterAsyncClient,
)
from google.cloud.databasecenter_v1beta.services.database_center.client import (
    DatabaseCenterClient,
)
from google.cloud.databasecenter_v1beta.types.affiliation import Affiliation
from google.cloud.databasecenter_v1beta.types.machine_config import MachineConfig
from google.cloud.databasecenter_v1beta.types.maintenance import (
    MaintenanceInfo,
    MaintenanceState,
    Phase,
    PossibleFailureReason,
    ResourceMaintenanceDenySchedule,
    ResourceMaintenanceSchedule,
    UpcomingMaintenance,
)
from google.cloud.databasecenter_v1beta.types.metric_data import (
    MetricData,
    Metrics,
    TypedValue,
)
from google.cloud.databasecenter_v1beta.types.operation_error_type import (
    OperationErrorType,
)
from google.cloud.databasecenter_v1beta.types.product import (
    Engine,
    Product,
    ProductType,
)
from google.cloud.databasecenter_v1beta.types.service import (
    AggregateFleetRequest,
    AggregateFleetResponse,
    AggregateFleetRow,
    AggregateIssueStatsRequest,
    AggregateIssueStatsResponse,
    AggregateQueryStatsRequest,
    AggregateQueryStatsResponse,
    BackupDRConfig,
    DatabaseResource,
    DatabaseResourceGroup,
    DatabaseResourceIssue,
    DeltaDetails,
    Dimension,
    Edition,
    IssueGroupStats,
    IssueStats,
    Label,
    ManagementType,
    QueryDatabaseResourceGroupsRequest,
    QueryDatabaseResourceGroupsResponse,
    QueryIssuesRequest,
    QueryIssuesResponse,
    QueryMetrics,
    QueryProductsRequest,
    QueryProductsResponse,
    QueryStats,
    QueryStatsInfo,
    ResourceCategory,
    ResourceDetails,
    ResourceId,
    SignalProductsFilters,
    SubResourceType,
    Tag,
)
from google.cloud.databasecenter_v1beta.types.signals import (
    AdditionalDetail,
    AutomatedBackupPolicyInfo,
    BackupRunInfo,
    DeletionProtectionInfo,
    InefficientQueryInfo,
    IssueCount,
    IssueSeverity,
    MaintenanceRecommendationInfo,
    OutdatedMinorVersionInfo,
    RecommendationInfo,
    RegulatoryStandard,
    ResourceSuspensionInfo,
    RetentionSettingsInfo,
    SCCInfo,
    Signal,
    SignalFilter,
    SignalGroup,
    SignalSource,
    SignalStatus,
    SignalType,
    SignalTypeGroup,
    SubResource,
)
from google.cloud.databasecenter_v1beta.types.suspension_reason import SuspensionReason

__all__ = (
    "DatabaseCenterClient",
    "DatabaseCenterAsyncClient",
    "Affiliation",
    "MachineConfig",
    "MaintenanceInfo",
    "ResourceMaintenanceDenySchedule",
    "ResourceMaintenanceSchedule",
    "UpcomingMaintenance",
    "MaintenanceState",
    "Phase",
    "PossibleFailureReason",
    "MetricData",
    "Metrics",
    "TypedValue",
    "OperationErrorType",
    "Product",
    "Engine",
    "ProductType",
    "AggregateFleetRequest",
    "AggregateFleetResponse",
    "AggregateFleetRow",
    "AggregateIssueStatsRequest",
    "AggregateIssueStatsResponse",
    "AggregateQueryStatsRequest",
    "AggregateQueryStatsResponse",
    "BackupDRConfig",
    "DatabaseResource",
    "DatabaseResourceGroup",
    "DatabaseResourceIssue",
    "DeltaDetails",
    "Dimension",
    "IssueGroupStats",
    "IssueStats",
    "Label",
    "QueryDatabaseResourceGroupsRequest",
    "QueryDatabaseResourceGroupsResponse",
    "QueryIssuesRequest",
    "QueryIssuesResponse",
    "QueryMetrics",
    "QueryProductsRequest",
    "QueryProductsResponse",
    "QueryStats",
    "QueryStatsInfo",
    "ResourceDetails",
    "ResourceId",
    "SignalProductsFilters",
    "Tag",
    "Edition",
    "ManagementType",
    "ResourceCategory",
    "SubResourceType",
    "AdditionalDetail",
    "AutomatedBackupPolicyInfo",
    "BackupRunInfo",
    "DeletionProtectionInfo",
    "InefficientQueryInfo",
    "IssueCount",
    "MaintenanceRecommendationInfo",
    "OutdatedMinorVersionInfo",
    "RecommendationInfo",
    "RegulatoryStandard",
    "ResourceSuspensionInfo",
    "RetentionSettingsInfo",
    "SCCInfo",
    "Signal",
    "SignalFilter",
    "SignalGroup",
    "SignalTypeGroup",
    "SubResource",
    "IssueSeverity",
    "SignalSource",
    "SignalStatus",
    "SignalType",
    "SuspensionReason",
)
