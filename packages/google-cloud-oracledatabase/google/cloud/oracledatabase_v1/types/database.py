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
from __future__ import annotations

from typing import MutableMapping, MutableSequence

import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.type.dayofweek_pb2 as dayofweek_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.oracledatabase_v1.types import pluggable_database

__protobuf__ = proto.module(
    package="google.cloud.oracledatabase.v1",
    manifest={
        "Database",
        "DatabaseProperties",
        "DbBackupConfig",
        "GetDatabaseRequest",
        "ListDatabasesRequest",
        "ListDatabasesResponse",
    },
)


class Database(proto.Message):
    r"""Details of the Database resource.
    https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/Database/

    Attributes:
        name (str):
            Identifier. The name of the Database resource
            in the following format:
            projects/{project}/locations/{region}/databases/{database}
        db_name (str):
            Optional. The database name. The name must
            begin with an alphabetic character and can
            contain a maximum of eight alphanumeric
            characters. Special characters are not
            permitted.
        db_unique_name (str):
            Optional. The DB_UNIQUE_NAME of the Oracle Database being
            backed up.
        admin_password (str):
            Optional. The password for the default ADMIN user. Note:
            Only one of ``admin_password_secret_version`` or
            ``admin_password`` can be populated.
        admin_password_secret_version (str):
            Optional. The resource name of a secret version in Secret
            Manager which contains the database admin user's password.
            Format:
            projects/{project}/secrets/{secret}/versions/{version}.
            Note: Only one of ``admin_password_secret_version`` or
            ``admin_password`` can be populated.
        tde_wallet_password (str):
            Optional. The TDE wallet password for the database. Note:
            Only one of ``tde_wallet_password_secret_version`` or
            ``tde_wallet_password`` can be populated.
        tde_wallet_password_secret_version (str):
            Optional. The resource name of a secret version in Secret
            Manager which contains the TDE wallet password for the
            database. Format:
            projects/{project}/secrets/{secret}/versions/{version}.
            Note: Only one of ``tde_wallet_password_secret_version`` or
            ``tde_wallet_password`` can be populated.
        character_set (str):
            Optional. The character set for the database.
            The default is AL32UTF8.
        ncharacter_set (str):
            Optional. The national character set for the
            database. The default is AL16UTF16.
        oci_url (str):
            Output only. HTTPS link to OCI resources
            exposed to Customer via UI Interface.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The date and time that the
            Database was created.
        properties (google.cloud.oracledatabase_v1.types.DatabaseProperties):
            Optional. The properties of the Database.
        database_id (str):
            Optional. The database ID of the Database.
        db_home_name (str):
            Optional. The name of the DbHome resource
            associated with the Database.
        gcp_oracle_zone (str):
            Output only. The GCP Oracle zone where the
            Database is created.
        ops_insights_status (google.cloud.oracledatabase_v1.types.Database.OperationsInsightsStatus):
            Output only. The Status of Operations
            Insights for this Database.
        pluggable_database_id (str):
            Optional. The ID of the pluggable database
            associated with the Database. The ID must be
            unique within the project and location.
        pluggable_database_name (str):
            Optional. The pluggable database associated
            with the Database. The name must begin with an
            alphabetic character and can contain a maximum
            of thirty alphanumeric characters.
    """

    class OperationsInsightsStatus(proto.Enum):
        r"""The Status of Operations Insights for this Database.

        Values:
            OPERATIONS_INSIGHTS_STATUS_UNSPECIFIED (0):
                Default unspecified value.
            ENABLING (1):
                Indicates that the operations insights are
                being enabled.
            ENABLED (2):
                Indicates that the operations insights are
                enabled.
            DISABLING (3):
                Indicates that the operations insights are
                being disabled.
            NOT_ENABLED (4):
                Indicates that the operations insights are
                not enabled.
            FAILED_ENABLING (5):
                Indicates that the operations insights failed
                to enable.
            FAILED_DISABLING (6):
                Indicates that the operations insights failed
                to disable.
        """

        OPERATIONS_INSIGHTS_STATUS_UNSPECIFIED = 0
        ENABLING = 1
        ENABLED = 2
        DISABLING = 3
        NOT_ENABLED = 4
        FAILED_ENABLING = 5
        FAILED_DISABLING = 6

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    db_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    db_unique_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    admin_password: str = proto.Field(
        proto.STRING,
        number=4,
    )
    admin_password_secret_version: str = proto.Field(
        proto.STRING,
        number=17,
    )
    tde_wallet_password: str = proto.Field(
        proto.STRING,
        number=5,
    )
    tde_wallet_password_secret_version: str = proto.Field(
        proto.STRING,
        number=18,
    )
    character_set: str = proto.Field(
        proto.STRING,
        number=6,
    )
    ncharacter_set: str = proto.Field(
        proto.STRING,
        number=7,
    )
    oci_url: str = proto.Field(
        proto.STRING,
        number=8,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    properties: "DatabaseProperties" = proto.Field(
        proto.MESSAGE,
        number=10,
        message="DatabaseProperties",
    )
    database_id: str = proto.Field(
        proto.STRING,
        number=11,
    )
    db_home_name: str = proto.Field(
        proto.STRING,
        number=12,
    )
    gcp_oracle_zone: str = proto.Field(
        proto.STRING,
        number=13,
    )
    ops_insights_status: OperationsInsightsStatus = proto.Field(
        proto.ENUM,
        number=14,
        enum=OperationsInsightsStatus,
    )
    pluggable_database_id: str = proto.Field(
        proto.STRING,
        number=15,
    )
    pluggable_database_name: str = proto.Field(
        proto.STRING,
        number=16,
    )


class DatabaseProperties(proto.Message):
    r"""The properties of a Database.

    Attributes:
        state (google.cloud.oracledatabase_v1.types.DatabaseProperties.DatabaseLifecycleState):
            Output only. State of the Database.
        db_version (str):
            Required. The Oracle Database version.
        db_backup_config (google.cloud.oracledatabase_v1.types.DbBackupConfig):
            Optional. Backup options for the Database.
        database_management_config (google.cloud.oracledatabase_v1.types.DatabaseManagementConfig):
            Output only. The Database Management config.
    """

    class DatabaseLifecycleState(proto.Enum):
        r"""The various lifecycle states of the Database.

        Values:
            DATABASE_LIFECYCLE_STATE_UNSPECIFIED (0):
                Default unspecified value.
            PROVISIONING (1):
                Indicates that the resource is in
                provisioning state.
            AVAILABLE (2):
                Indicates that the resource is in available
                state.
            UPDATING (3):
                Indicates that the resource is in updating
                state.
            BACKUP_IN_PROGRESS (4):
                Indicates that the resource is in backup in
                progress state.
            UPGRADING (5):
                Indicates that the resource is in upgrading
                state.
            CONVERTING (6):
                Indicates that the resource is in converting
                state.
            TERMINATING (7):
                Indicates that the resource is in terminating
                state.
            TERMINATED (8):
                Indicates that the resource is in terminated
                state.
            RESTORE_FAILED (9):
                Indicates that the resource is in restore
                failed state.
            FAILED (10):
                Indicates that the resource is in failed
                state.
        """

        DATABASE_LIFECYCLE_STATE_UNSPECIFIED = 0
        PROVISIONING = 1
        AVAILABLE = 2
        UPDATING = 3
        BACKUP_IN_PROGRESS = 4
        UPGRADING = 5
        CONVERTING = 6
        TERMINATING = 7
        TERMINATED = 8
        RESTORE_FAILED = 9
        FAILED = 10

    state: DatabaseLifecycleState = proto.Field(
        proto.ENUM,
        number=1,
        enum=DatabaseLifecycleState,
    )
    db_version: str = proto.Field(
        proto.STRING,
        number=2,
    )
    db_backup_config: "DbBackupConfig" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="DbBackupConfig",
    )
    database_management_config: pluggable_database.DatabaseManagementConfig = (
        proto.Field(
            proto.MESSAGE,
            number=4,
            message=pluggable_database.DatabaseManagementConfig,
        )
    )


class DbBackupConfig(proto.Message):
    r"""Backup Options for the Database.

    Attributes:
        auto_backup_enabled (bool):
            Optional. If set to true, enables automatic
            backups on the database.
        backup_destination_details (MutableSequence[google.cloud.oracledatabase_v1.types.DbBackupConfig.BackupDestinationDetails]):
            Optional. Details of the database backup
            destinations.
        retention_period_days (int):
            Optional. The number of days an automatic
            backup is retained before being automatically
            deleted. This value determines the earliest
            point in time to which a database can be
            restored. Min: 1, Max: 60.
        backup_deletion_policy (google.cloud.oracledatabase_v1.types.DbBackupConfig.BackupDeletionPolicy):
            Optional. This defines when the backups will
            be deleted after Database termination.
        auto_full_backup_day (google.type.dayofweek_pb2.DayOfWeek):
            Optional. The day of the week on which the
            full backup should be performed on the database.
            If no value is provided, it will default to
            Sunday.
        auto_full_backup_window (google.cloud.oracledatabase_v1.types.DbBackupConfig.BackupWindow):
            Optional. The window in which the full backup
            should be performed on the database. If no value
            is provided, the default is anytime.
        auto_incremental_backup_window (google.cloud.oracledatabase_v1.types.DbBackupConfig.BackupWindow):
            Optional. The window in which the incremental
            backup should be performed on the database. If
            no value is provided, the default is anytime
            except the auto full backup day.
    """

    class BackupDestinationType(proto.Enum):
        r"""The type of the database backup destination.

        Values:
            BACKUP_DESTINATION_TYPE_UNSPECIFIED (0):
                Default unspecified value.
            NFS (1):
                Backup destination type is NFS.
            RECOVERY_APPLIANCE (2):
                Backup destination type is Recovery
                Appliance.
            OBJECT_STORE (3):
                Backup destination type is Object Store.
            LOCAL (4):
                Backup destination type is Local.
            DBRS (5):
                Backup destination type is DBRS.
        """

        BACKUP_DESTINATION_TYPE_UNSPECIFIED = 0
        NFS = 1
        RECOVERY_APPLIANCE = 2
        OBJECT_STORE = 3
        LOCAL = 4
        DBRS = 5

    class BackupWindow(proto.Enum):
        r"""The 2 hour window in which the backup should be performed on
        the database.

        Values:
            BACKUP_WINDOW_UNSPECIFIED (0):
                Default unspecified value.
            SLOT_ONE (1):
                12:00 AM - 2:00 AM
            SLOT_TWO (2):
                2:00 AM - 4:00 AM
            SLOT_THREE (3):
                4:00 AM - 6:00 AM
            SLOT_FOUR (4):
                6:00 AM - 8:00 AM
            SLOT_FIVE (5):
                8:00 AM - 10:00 AM
            SLOT_SIX (6):
                10:00 AM - 12:00 PM
            SLOT_SEVEN (7):
                12:00 PM - 2:00 PM
            SLOT_EIGHT (8):
                2:00 PM - 4:00 PM
            SLOT_NINE (9):
                4:00 PM - 6:00 PM
            SLOT_TEN (10):
                6:00 PM - 8:00 PM
            SLOT_ELEVEN (11):
                8:00 PM - 10:00 PM
            SLOT_TWELVE (12):
                10:00 PM - 12:00 AM
        """

        BACKUP_WINDOW_UNSPECIFIED = 0
        SLOT_ONE = 1
        SLOT_TWO = 2
        SLOT_THREE = 3
        SLOT_FOUR = 4
        SLOT_FIVE = 5
        SLOT_SIX = 6
        SLOT_SEVEN = 7
        SLOT_EIGHT = 8
        SLOT_NINE = 9
        SLOT_TEN = 10
        SLOT_ELEVEN = 11
        SLOT_TWELVE = 12

    class BackupDeletionPolicy(proto.Enum):
        r"""This defines when the backups will be deleted after Database
        termination.

        Values:
            BACKUP_DELETION_POLICY_UNSPECIFIED (0):
                Default unspecified value.
            DELETE_IMMEDIATELY (1):
                Keeps the backup for predefined time
                i.e. 72 hours and then delete permanently.
            DELETE_AFTER_RETENTION_PERIOD (2):
                Keeps the backups as per the policy defined
                for database backups.
        """

        BACKUP_DELETION_POLICY_UNSPECIFIED = 0
        DELETE_IMMEDIATELY = 1
        DELETE_AFTER_RETENTION_PERIOD = 2

    class BackupDestinationDetails(proto.Message):
        r"""The details of the database backup destination.

        Attributes:
            type_ (google.cloud.oracledatabase_v1.types.DbBackupConfig.BackupDestinationType):
                Optional. The type of the database backup
                destination.
        """

        type_: "DbBackupConfig.BackupDestinationType" = proto.Field(
            proto.ENUM,
            number=1,
            enum="DbBackupConfig.BackupDestinationType",
        )

    auto_backup_enabled: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    backup_destination_details: MutableSequence[BackupDestinationDetails] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message=BackupDestinationDetails,
        )
    )
    retention_period_days: int = proto.Field(
        proto.INT32,
        number=3,
    )
    backup_deletion_policy: BackupDeletionPolicy = proto.Field(
        proto.ENUM,
        number=4,
        enum=BackupDeletionPolicy,
    )
    auto_full_backup_day: dayofweek_pb2.DayOfWeek = proto.Field(
        proto.ENUM,
        number=5,
        enum=dayofweek_pb2.DayOfWeek,
    )
    auto_full_backup_window: BackupWindow = proto.Field(
        proto.ENUM,
        number=6,
        enum=BackupWindow,
    )
    auto_incremental_backup_window: BackupWindow = proto.Field(
        proto.ENUM,
        number=7,
        enum=BackupWindow,
    )


class GetDatabaseRequest(proto.Message):
    r"""The request for ``Database.Get``.

    Attributes:
        name (str):
            Required. The name of the Database resource
            in the following format:
            projects/{project}/locations/{region}/databases/{database}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListDatabasesRequest(proto.Message):
    r"""The request for ``Database.List``.

    Attributes:
        parent (str):
            Required. The parent resource name in the
            following format:
            projects/{project}/locations/{region}
        page_size (int):
            Optional. The maximum number of items to
            return. If unspecified, a maximum of 50
            Databases will be returned. The maximum value is
            1000; values above 1000 will be reset to 1000.
        page_token (str):
            Optional. A token identifying the requested
            page of results to return. All fields except the
            filter should remain the same as in the request
            that provided this page token.
        filter (str):
            Optional. An expression for filtering the results of the
            request. list for container databases is supported only with
            a valid dbSystem (full resource name) filter in this format:
            ``dbSystem="projects/{project}/locations/{location}/dbSystems/{dbSystemId}"``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListDatabasesResponse(proto.Message):
    r"""The response for ``Database.List``.

    Attributes:
        databases (MutableSequence[google.cloud.oracledatabase_v1.types.Database]):
            The list of Databases.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
    """

    @property
    def raw_page(self):
        return self

    databases: MutableSequence["Database"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Database",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
