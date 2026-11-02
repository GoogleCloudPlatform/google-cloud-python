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

from google.cloud.spanner_admin_database_v1 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.spanner_admin_database_v1.services.database_admin",
    "google.cloud.spanner_admin_database_v1.types.backup",
    "google.cloud.spanner_admin_database_v1.types.backup_schedule",
    "google.cloud.spanner_admin_database_v1.types.common",
    "google.cloud.spanner_admin_database_v1.types.spanner_database_admin",
}


from .services.database_admin import DatabaseAdminAsyncClient, DatabaseAdminClient
from .types.backup import (
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
from .types.backup_schedule import (
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
from .types.common import (
    DatabaseDialect,
    EncryptionConfig,
    EncryptionInfo,
    OperationProgress,
)
from .types.spanner_database_admin import (
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
    "DatabaseAdminAsyncClient",
    "AddSplitPointsRequest",
    "AddSplitPointsResponse",
    "Backup",
    "BackupInfo",
    "BackupInstancePartition",
    "BackupSchedule",
    "BackupScheduleSpec",
    "CopyBackupEncryptionConfig",
    "CopyBackupMetadata",
    "CopyBackupRequest",
    "CreateBackupEncryptionConfig",
    "CreateBackupMetadata",
    "CreateBackupRequest",
    "CreateBackupScheduleRequest",
    "CreateDatabaseMetadata",
    "CreateDatabaseRequest",
    "CrontabSpec",
    "Database",
    "DatabaseAdminClient",
    "DatabaseDialect",
    "DatabaseRole",
    "DdlStatementActionInfo",
    "DeleteBackupRequest",
    "DeleteBackupScheduleRequest",
    "DropDatabaseRequest",
    "EncryptionConfig",
    "EncryptionInfo",
    "FullBackupSpec",
    "GetBackupRequest",
    "GetBackupScheduleRequest",
    "GetDatabaseDdlRequest",
    "GetDatabaseDdlResponse",
    "GetDatabaseRequest",
    "IncrementalBackupSpec",
    "InternalUpdateGraphOperationRequest",
    "InternalUpdateGraphOperationResponse",
    "ListBackupOperationsRequest",
    "ListBackupOperationsResponse",
    "ListBackupSchedulesRequest",
    "ListBackupSchedulesResponse",
    "ListBackupsRequest",
    "ListBackupsResponse",
    "ListDatabaseOperationsRequest",
    "ListDatabaseOperationsResponse",
    "ListDatabaseRolesRequest",
    "ListDatabaseRolesResponse",
    "ListDatabasesRequest",
    "ListDatabasesResponse",
    "OperationProgress",
    "OptimizeRestoredDatabaseMetadata",
    "RestoreDatabaseEncryptionConfig",
    "RestoreDatabaseMetadata",
    "RestoreDatabaseRequest",
    "RestoreInfo",
    "RestoreSourceType",
    "SplitPoints",
    "UpdateBackupRequest",
    "UpdateBackupScheduleRequest",
    "UpdateDatabaseDdlMetadata",
    "UpdateDatabaseDdlRequest",
    "UpdateDatabaseMetadata",
    "UpdateDatabaseRequest",
)

api_core.check_python_version("google.cloud.spanner_admin_database_v1")
api_core.check_dependency_versions("google.cloud.spanner_admin_database_v1")
