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

from google.cloud.databasecenter_v1beta import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.databasecenter_v1beta.services.database_center",
    "google.cloud.databasecenter_v1beta.types.affiliation",
    "google.cloud.databasecenter_v1beta.types.machine_config",
    "google.cloud.databasecenter_v1beta.types.maintenance",
    "google.cloud.databasecenter_v1beta.types.metric_data",
    "google.cloud.databasecenter_v1beta.types.operation_error_type",
    "google.cloud.databasecenter_v1beta.types.product",
    "google.cloud.databasecenter_v1beta.types.service",
    "google.cloud.databasecenter_v1beta.types.signals",
    "google.cloud.databasecenter_v1beta.types.suspension_reason",
}


from .services.database_center import DatabaseCenterAsyncClient, DatabaseCenterClient
from .types.affiliation import Affiliation
from .types.machine_config import MachineConfig
from .types.maintenance import (
    MaintenanceInfo,
    MaintenanceState,
    Phase,
    PossibleFailureReason,
    ResourceMaintenanceDenySchedule,
    ResourceMaintenanceSchedule,
    UpcomingMaintenance,
)
from .types.metric_data import MetricData, Metrics, TypedValue
from .types.operation_error_type import OperationErrorType
from .types.product import Engine, Product, ProductType
from .types.service import (
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
from .types.signals import (
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
from .types.suspension_reason import SuspensionReason

__all__ = (
    "DatabaseCenterAsyncClient",
    "AdditionalDetail",
    "Affiliation",
    "AggregateFleetRequest",
    "AggregateFleetResponse",
    "AggregateFleetRow",
    "AggregateIssueStatsRequest",
    "AggregateIssueStatsResponse",
    "AggregateQueryStatsRequest",
    "AggregateQueryStatsResponse",
    "AutomatedBackupPolicyInfo",
    "BackupDRConfig",
    "BackupRunInfo",
    "DatabaseCenterClient",
    "DatabaseResource",
    "DatabaseResourceGroup",
    "DatabaseResourceIssue",
    "DeletionProtectionInfo",
    "DeltaDetails",
    "Dimension",
    "Edition",
    "Engine",
    "InefficientQueryInfo",
    "IssueCount",
    "IssueGroupStats",
    "IssueSeverity",
    "IssueStats",
    "Label",
    "MachineConfig",
    "MaintenanceInfo",
    "MaintenanceRecommendationInfo",
    "MaintenanceState",
    "ManagementType",
    "MetricData",
    "Metrics",
    "OperationErrorType",
    "OutdatedMinorVersionInfo",
    "Phase",
    "PossibleFailureReason",
    "Product",
    "ProductType",
    "QueryDatabaseResourceGroupsRequest",
    "QueryDatabaseResourceGroupsResponse",
    "QueryIssuesRequest",
    "QueryIssuesResponse",
    "QueryMetrics",
    "QueryProductsRequest",
    "QueryProductsResponse",
    "QueryStats",
    "QueryStatsInfo",
    "RecommendationInfo",
    "RegulatoryStandard",
    "ResourceCategory",
    "ResourceDetails",
    "ResourceId",
    "ResourceMaintenanceDenySchedule",
    "ResourceMaintenanceSchedule",
    "ResourceSuspensionInfo",
    "RetentionSettingsInfo",
    "SCCInfo",
    "Signal",
    "SignalFilter",
    "SignalGroup",
    "SignalProductsFilters",
    "SignalSource",
    "SignalStatus",
    "SignalType",
    "SignalTypeGroup",
    "SubResource",
    "SubResourceType",
    "SuspensionReason",
    "Tag",
    "TypedValue",
    "UpcomingMaintenance",
)

api_core.check_python_version("google.cloud.databasecenter_v1beta")
api_core.check_dependency_versions("google.cloud.databasecenter_v1beta")
