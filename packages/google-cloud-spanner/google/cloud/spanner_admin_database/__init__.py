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
from google.cloud.spanner_admin_database import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.spanner_admin_database_v1.services.database_admin.async_client import (
    DatabaseAdminAsyncClient,
)
from google.cloud.spanner_admin_database_v1.services.database_admin.client import (
    DatabaseAdminClient,
)
from google.cloud.spanner_admin_database_v1.types.backup import (
    Backup,
    BackupInfo,
    BackupInstancePartition,
    CopyBackupEncryptionConfig,
    CopyBackupMetadata,
    CopyBackupRequest,
    CreateBackupEncryptionConfig,
    CreateBackupMetadata,
    CreateBackupRequest,
    DeleteBackupRequest,
    FullBackupSpec,
    GetBackupRequest,
    IncrementalBackupSpec,
    ListBackupOperationsRequest,
    ListBackupOperationsResponse,
    ListBackupsRequest,
    ListBackupsResponse,
    UpdateBackupRequest,
)
from google.cloud.spanner_admin_database_v1.types.backup_schedule import (
    BackupSchedule,
    BackupScheduleSpec,
    CreateBackupScheduleRequest,
    CrontabSpec,
    DeleteBackupScheduleRequest,
    GetBackupScheduleRequest,
    ListBackupSchedulesRequest,
    ListBackupSchedulesResponse,
    UpdateBackupScheduleRequest,
)
from google.cloud.spanner_admin_database_v1.types.common import (
    DatabaseDialect,
    EncryptionConfig,
    EncryptionInfo,
    OperationProgress,
)
from google.cloud.spanner_admin_database_v1.types.spanner_database_admin import (
    AddSplitPointsRequest,
    AddSplitPointsResponse,
    CreateDatabaseMetadata,
    CreateDatabaseRequest,
    Database,
    DatabaseRole,
    DdlStatementActionInfo,
    DropDatabaseRequest,
    GetDatabaseDdlRequest,
    GetDatabaseDdlResponse,
    GetDatabaseRequest,
    InternalUpdateGraphOperationRequest,
    InternalUpdateGraphOperationResponse,
    ListDatabaseOperationsRequest,
    ListDatabaseOperationsResponse,
    ListDatabaseRolesRequest,
    ListDatabaseRolesResponse,
    ListDatabasesRequest,
    ListDatabasesResponse,
    OptimizeRestoredDatabaseMetadata,
    RestoreDatabaseEncryptionConfig,
    RestoreDatabaseMetadata,
    RestoreDatabaseRequest,
    RestoreInfo,
    RestoreSourceType,
    SplitPoints,
    UpdateDatabaseDdlMetadata,
    UpdateDatabaseDdlRequest,
    UpdateDatabaseMetadata,
    UpdateDatabaseRequest,
)

__all__ = (
    "DatabaseAdminClient",
    "DatabaseAdminAsyncClient",
    "Backup",
    "BackupInfo",
    "BackupInstancePartition",
    "CopyBackupEncryptionConfig",
    "CopyBackupMetadata",
    "CopyBackupRequest",
    "CreateBackupEncryptionConfig",
    "CreateBackupMetadata",
    "CreateBackupRequest",
    "DeleteBackupRequest",
    "FullBackupSpec",
    "GetBackupRequest",
    "IncrementalBackupSpec",
    "ListBackupOperationsRequest",
    "ListBackupOperationsResponse",
    "ListBackupsRequest",
    "ListBackupsResponse",
    "UpdateBackupRequest",
    "BackupSchedule",
    "BackupScheduleSpec",
    "CreateBackupScheduleRequest",
    "CrontabSpec",
    "DeleteBackupScheduleRequest",
    "GetBackupScheduleRequest",
    "ListBackupSchedulesRequest",
    "ListBackupSchedulesResponse",
    "UpdateBackupScheduleRequest",
    "EncryptionConfig",
    "EncryptionInfo",
    "OperationProgress",
    "DatabaseDialect",
    "AddSplitPointsRequest",
    "AddSplitPointsResponse",
    "CreateDatabaseMetadata",
    "CreateDatabaseRequest",
    "Database",
    "DatabaseRole",
    "DdlStatementActionInfo",
    "DropDatabaseRequest",
    "GetDatabaseDdlRequest",
    "GetDatabaseDdlResponse",
    "GetDatabaseRequest",
    "InternalUpdateGraphOperationRequest",
    "InternalUpdateGraphOperationResponse",
    "ListDatabaseOperationsRequest",
    "ListDatabaseOperationsResponse",
    "ListDatabaseRolesRequest",
    "ListDatabaseRolesResponse",
    "ListDatabasesRequest",
    "ListDatabasesResponse",
    "OptimizeRestoredDatabaseMetadata",
    "RestoreDatabaseEncryptionConfig",
    "RestoreDatabaseMetadata",
    "RestoreDatabaseRequest",
    "RestoreInfo",
    "SplitPoints",
    "UpdateDatabaseDdlMetadata",
    "UpdateDatabaseDdlRequest",
    "UpdateDatabaseMetadata",
    "UpdateDatabaseRequest",
    "RestoreSourceType",
)
