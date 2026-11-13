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
import proto  # type: ignore

from google.cloud.sqladmin_v1.types import cloud_sql_resources

__protobuf__ = proto.module(
    package="google.cloud.sql.v1",
    manifest={
        "SqlBackupRunStatus",
        "SqlBackupKind",
        "SqlBackupRunType",
        "SqlBackupRunsDeleteRequest",
        "SqlBackupRunsGetRequest",
        "SqlBackupRunsInsertRequest",
        "SqlBackupRunsListRequest",
        "BackupRun",
        "BackupRunsListResponse",
    },
)


class SqlBackupRunStatus(proto.Enum):
    r"""The status of a backup run.

    Values:
        SQL_BACKUP_RUN_STATUS_UNSPECIFIED (0):
            The status of the run is unknown.
        ENQUEUED (1):
            The backup operation was enqueued.
        OVERDUE (2):
            The backup is overdue across a given backup
            window. Indicates a problem. Example:
            Long-running operation in progress during the
            whole window.
        RUNNING (3):
            The backup is in progress.
        FAILED (4):
            The backup failed.
        SUCCESSFUL (5):
            The backup was successful.
        SKIPPED (6):
            The backup was skipped (without problems) for
            a given backup window. Example: Instance was
            idle.
        DELETION_PENDING (7):
            The backup is about to be deleted.
        DELETION_FAILED (8):
            The backup deletion failed.
        DELETED (9):
            The backup has been deleted.
    """

    SQL_BACKUP_RUN_STATUS_UNSPECIFIED = 0
    ENQUEUED = 1
    OVERDUE = 2
    RUNNING = 3
    FAILED = 4
    SUCCESSFUL = 5
    SKIPPED = 6
    DELETION_PENDING = 7
    DELETION_FAILED = 8
    DELETED = 9


class SqlBackupKind(proto.Enum):
    r"""Defines the supported backup kinds.

    Values:
        SQL_BACKUP_KIND_UNSPECIFIED (0):
            This is an unknown BackupKind.
        SNAPSHOT (1):
            Snapshot-based backups.
        PHYSICAL (2):
            Physical backups.
    """

    SQL_BACKUP_KIND_UNSPECIFIED = 0
    SNAPSHOT = 1
    PHYSICAL = 2


class SqlBackupRunType(proto.Enum):
    r"""Type of backup (i.e. automated, on demand, etc).

    Values:
        SQL_BACKUP_RUN_TYPE_UNSPECIFIED (0):
            This is an unknown BackupRun type.
        AUTOMATED (1):
            The backup schedule automatically triggers a
            backup.
        ON_DEMAND (2):
            The user manually triggers a backup.
    """

    SQL_BACKUP_RUN_TYPE_UNSPECIFIED = 0
    AUTOMATED = 1
    ON_DEMAND = 2


class SqlBackupRunsDeleteRequest(proto.Message):
    r"""Backup runs delete request.

    Attributes:
        id (int):
            The ID of the backup run to delete. To find a backup run ID,
            use the
            `list <https://cloud.google.com/sql/docs/mysql/admin-api/rest/v1/backupRuns/list>`__
            method.
        instance (str):
            Cloud SQL instance ID. This does not include
            the project ID.
        project (str):
            Project ID of the project that contains the
            instance.
    """

    id: int = proto.Field(
        proto.INT64,
        number=1,
    )
    instance: str = proto.Field(
        proto.STRING,
        number=2,
    )
    project: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SqlBackupRunsGetRequest(proto.Message):
    r"""Backup runs get request.

    Attributes:
        id (int):
            The ID of this backup run.
        instance (str):
            Cloud SQL instance ID. This does not include
            the project ID.
        project (str):
            Project ID of the project that contains the
            instance.
    """

    id: int = proto.Field(
        proto.INT64,
        number=1,
    )
    instance: str = proto.Field(
        proto.STRING,
        number=2,
    )
    project: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SqlBackupRunsInsertRequest(proto.Message):
    r"""Backup runs insert request.

    Attributes:
        instance (str):
            Cloud SQL instance ID. This does not include
            the project ID.
        project (str):
            Project ID of the project that contains the
            instance.
        body (google.cloud.sqladmin_v1.types.BackupRun):

    """

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    body: "BackupRun" = proto.Field(
        proto.MESSAGE,
        number=100,
        message="BackupRun",
    )


class SqlBackupRunsListRequest(proto.Message):
    r"""Backup runs list request.

    Attributes:
        instance (str):
            Cloud SQL instance ID, or "-" for all
            instances. This does not include the project ID.
        max_results (int):
            Maximum number of backup runs per response.
        page_token (str):
            A previously-returned page token representing
            part of the larger set of results to view.
        project (str):
            Project ID of the project that contains the
            instance.
    """

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    max_results: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    project: str = proto.Field(
        proto.STRING,
        number=4,
    )


class BackupRun(proto.Message):
    r"""A BackupRun resource.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        kind (str):
            This is always ``sql#backupRun``.
        status (google.cloud.sqladmin_v1.types.SqlBackupRunStatus):
            The status of this run.
        enqueued_time (google.protobuf.timestamp_pb2.Timestamp):
            The time the run was enqueued in UTC timezone in `RFC
            3339 <https://tools.ietf.org/html/rfc3339>`__ format, for
            example ``2012-11-15T16:19:00.094Z``.
        id (int):
            The identifier for this backup run. Unique
            only for a specific Cloud SQL instance.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            The time the backup operation actually started in UTC
            timezone in `RFC
            3339 <https://tools.ietf.org/html/rfc3339>`__ format, for
            example ``2012-11-15T16:19:00.094Z``.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            The time the backup operation completed in UTC timezone in
            `RFC 3339 <https://tools.ietf.org/html/rfc3339>`__ format,
            for example ``2012-11-15T16:19:00.094Z``.
        error (google.cloud.sqladmin_v1.types.OperationError):
            Information about why the backup operation
            failed. This is only present if the run has the
            FAILED status.
        type_ (google.cloud.sqladmin_v1.types.SqlBackupRunType):
            The type of this run; can be either "AUTOMATED" or
            "ON_DEMAND" or "FINAL". This field defaults to "ON_DEMAND"
            and is ignored, when specified for insert requests.
        description (str):
            The description of this run, only applicable
            to on-demand backups.
        window_start_time (google.protobuf.timestamp_pb2.Timestamp):
            The start time of the backup window during which this the
            backup was attempted in `RFC
            3339 <https://tools.ietf.org/html/rfc3339>`__ format, for
            example ``2012-11-15T16:19:00.094Z``.
        instance (str):
            Name of the database instance.
        self_link (str):
            The URI of this resource.
        location (str):
            Location of the backups.
        database_version (google.cloud.sqladmin_v1.types.SqlDatabaseVersion):
            Output only. The instance database version at
            the time this backup was made.
        disk_encryption_configuration (google.cloud.sqladmin_v1.types.DiskEncryptionConfiguration):
            Encryption configuration specific to a
            backup.
        disk_encryption_status (google.cloud.sqladmin_v1.types.DiskEncryptionStatus):
            Encryption status specific to a backup.
        backup_kind (google.cloud.sqladmin_v1.types.SqlBackupKind):
            Specifies the kind of backup, PHYSICAL or DEFAULT_SNAPSHOT.
        time_zone (str):
            Backup time zone to prevent restores to an
            instance with a different time zone. Now
            relevant only for SQL Server.
        max_chargeable_bytes (int):
            Output only. The maximum chargeable bytes for
            the backup.

            This field is a member of `oneof`_ ``_max_chargeable_bytes``.
    """

    kind: str = proto.Field(
        proto.STRING,
        number=1,
    )
    status: "SqlBackupRunStatus" = proto.Field(
        proto.ENUM,
        number=2,
        enum="SqlBackupRunStatus",
    )
    enqueued_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    id: int = proto.Field(
        proto.INT64,
        number=4,
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    error: cloud_sql_resources.OperationError = proto.Field(
        proto.MESSAGE,
        number=7,
        message=cloud_sql_resources.OperationError,
    )
    type_: "SqlBackupRunType" = proto.Field(
        proto.ENUM,
        number=8,
        enum="SqlBackupRunType",
    )
    description: str = proto.Field(
        proto.STRING,
        number=9,
    )
    window_start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10,
        message=timestamp_pb2.Timestamp,
    )
    instance: str = proto.Field(
        proto.STRING,
        number=11,
    )
    self_link: str = proto.Field(
        proto.STRING,
        number=12,
    )
    location: str = proto.Field(
        proto.STRING,
        number=13,
    )
    database_version: cloud_sql_resources.SqlDatabaseVersion = proto.Field(
        proto.ENUM,
        number=15,
        enum=cloud_sql_resources.SqlDatabaseVersion,
    )
    disk_encryption_configuration: cloud_sql_resources.DiskEncryptionConfiguration = (
        proto.Field(
            proto.MESSAGE,
            number=16,
            message=cloud_sql_resources.DiskEncryptionConfiguration,
        )
    )
    disk_encryption_status: cloud_sql_resources.DiskEncryptionStatus = proto.Field(
        proto.MESSAGE,
        number=17,
        message=cloud_sql_resources.DiskEncryptionStatus,
    )
    backup_kind: "SqlBackupKind" = proto.Field(
        proto.ENUM,
        number=19,
        enum="SqlBackupKind",
    )
    time_zone: str = proto.Field(
        proto.STRING,
        number=23,
    )
    max_chargeable_bytes: int = proto.Field(
        proto.INT64,
        number=24,
        optional=True,
    )


class BackupRunsListResponse(proto.Message):
    r"""Backup run list results.

    Attributes:
        kind (str):
            This is always ``sql#backupRunsList``.
        items (MutableSequence[google.cloud.sqladmin_v1.types.BackupRun]):
            A list of backup runs in reverse
            chronological order of the enqueued time.
        next_page_token (str):
            The continuation token, used to page through
            large result sets. Provide this value in a
            subsequent request to return the next page of
            results.
    """

    @property
    def raw_page(self):
        return self

    kind: str = proto.Field(
        proto.STRING,
        number=1,
    )
    items: MutableSequence["BackupRun"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="BackupRun",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
