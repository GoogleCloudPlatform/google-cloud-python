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

from google.cloud.alloydb_v1 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.alloydb_v1.services.alloy_db_admin",
    "google.cloud.alloydb_v1.services.alloy_dbcsql_admin",
    "google.cloud.alloydb_v1.types.csql_resources",
    "google.cloud.alloydb_v1.types.csql_service",
    "google.cloud.alloydb_v1.types.data_model",
    "google.cloud.alloydb_v1.types.resources",
    "google.cloud.alloydb_v1.types.service",
}


from .services.alloy_db_admin import AlloyDBAdminAsyncClient, AlloyDBAdminClient
from .services.alloy_dbcsql_admin import (
    AlloyDBCSQLAdminAsyncClient,
    AlloyDBCSQLAdminClient,
)
from .types.csql_resources import CloudSQLBackupRunSource
from .types.csql_service import RestoreFromCloudSQLRequest
from .types.data_model import SqlResult, SqlResultColumn, SqlResultRow, SqlResultValue
from .types.resources import (
    AutomatedBackupPolicy,
    Backup,
    BackupSource,
    Cluster,
    ClusterView,
    ConnectionInfo,
    ContinuousBackupConfig,
    ContinuousBackupInfo,
    ContinuousBackupSource,
    Database,
    DatabaseVersion,
    EncryptionConfig,
    EncryptionInfo,
    Instance,
    InstanceView,
    MaintenanceSchedule,
    MaintenanceUpdatePolicy,
    MigrationSource,
    SslConfig,
    SubscriptionType,
    SupportedDatabaseFlag,
    User,
    UserPassword,
)
from .types.service import (
    BatchCreateInstancesMetadata,
    BatchCreateInstancesRequest,
    BatchCreateInstancesResponse,
    BatchCreateInstanceStatus,
    CreateBackupRequest,
    CreateClusterRequest,
    CreateInstanceRequest,
    CreateInstanceRequests,
    CreateSecondaryClusterRequest,
    CreateSecondaryInstanceRequest,
    CreateUserRequest,
    DeleteBackupRequest,
    DeleteClusterRequest,
    DeleteInstanceRequest,
    DeleteUserRequest,
    ExecuteSqlMetadata,
    ExecuteSqlRequest,
    ExecuteSqlResponse,
    ExportClusterRequest,
    ExportClusterResponse,
    FailoverInstanceRequest,
    GcsDestination,
    GenerateClientCertificateRequest,
    GenerateClientCertificateResponse,
    GetBackupRequest,
    GetClusterRequest,
    GetConnectionInfoRequest,
    GetInstanceRequest,
    GetUserRequest,
    ImportClusterRequest,
    ImportClusterResponse,
    InjectFaultRequest,
    ListBackupsRequest,
    ListBackupsResponse,
    ListClustersRequest,
    ListClustersResponse,
    ListDatabasesRequest,
    ListDatabasesResponse,
    ListInstancesRequest,
    ListInstancesResponse,
    ListSupportedDatabaseFlagsRequest,
    ListSupportedDatabaseFlagsResponse,
    ListUsersRequest,
    ListUsersResponse,
    OperationMetadata,
    PromoteClusterRequest,
    RestartInstanceRequest,
    RestoreClusterRequest,
    SwitchoverClusterRequest,
    UpdateBackupRequest,
    UpdateClusterRequest,
    UpdateInstanceRequest,
    UpdateUserRequest,
    UpgradeClusterRequest,
    UpgradeClusterResponse,
    UpgradeClusterStatus,
)

__all__ = (
    "AlloyDBAdminAsyncClient",
    "AlloyDBCSQLAdminAsyncClient",
    "AlloyDBAdminClient",
    "AlloyDBCSQLAdminClient",
    "AutomatedBackupPolicy",
    "Backup",
    "BackupSource",
    "BatchCreateInstanceStatus",
    "BatchCreateInstancesMetadata",
    "BatchCreateInstancesRequest",
    "BatchCreateInstancesResponse",
    "CloudSQLBackupRunSource",
    "Cluster",
    "ClusterView",
    "ConnectionInfo",
    "ContinuousBackupConfig",
    "ContinuousBackupInfo",
    "ContinuousBackupSource",
    "CreateBackupRequest",
    "CreateClusterRequest",
    "CreateInstanceRequest",
    "CreateInstanceRequests",
    "CreateSecondaryClusterRequest",
    "CreateSecondaryInstanceRequest",
    "CreateUserRequest",
    "Database",
    "DatabaseVersion",
    "DeleteBackupRequest",
    "DeleteClusterRequest",
    "DeleteInstanceRequest",
    "DeleteUserRequest",
    "EncryptionConfig",
    "EncryptionInfo",
    "ExecuteSqlMetadata",
    "ExecuteSqlRequest",
    "ExecuteSqlResponse",
    "ExportClusterRequest",
    "ExportClusterResponse",
    "FailoverInstanceRequest",
    "GcsDestination",
    "GenerateClientCertificateRequest",
    "GenerateClientCertificateResponse",
    "GetBackupRequest",
    "GetClusterRequest",
    "GetConnectionInfoRequest",
    "GetInstanceRequest",
    "GetUserRequest",
    "ImportClusterRequest",
    "ImportClusterResponse",
    "InjectFaultRequest",
    "Instance",
    "InstanceView",
    "ListBackupsRequest",
    "ListBackupsResponse",
    "ListClustersRequest",
    "ListClustersResponse",
    "ListDatabasesRequest",
    "ListDatabasesResponse",
    "ListInstancesRequest",
    "ListInstancesResponse",
    "ListSupportedDatabaseFlagsRequest",
    "ListSupportedDatabaseFlagsResponse",
    "ListUsersRequest",
    "ListUsersResponse",
    "MaintenanceSchedule",
    "MaintenanceUpdatePolicy",
    "MigrationSource",
    "OperationMetadata",
    "PromoteClusterRequest",
    "RestartInstanceRequest",
    "RestoreClusterRequest",
    "RestoreFromCloudSQLRequest",
    "SqlResult",
    "SqlResultColumn",
    "SqlResultRow",
    "SqlResultValue",
    "SslConfig",
    "SubscriptionType",
    "SupportedDatabaseFlag",
    "SwitchoverClusterRequest",
    "UpdateBackupRequest",
    "UpdateClusterRequest",
    "UpdateInstanceRequest",
    "UpdateUserRequest",
    "UpgradeClusterRequest",
    "UpgradeClusterResponse",
    "UpgradeClusterStatus",
    "User",
    "UserPassword",
)

api_core.check_python_version("google.cloud.alloydb_v1")
api_core.check_dependency_versions("google.cloud.alloydb_v1")
