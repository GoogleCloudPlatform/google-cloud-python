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

import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.protobuf.wrappers_pb2 as wrappers_pb2  # type: ignore
import google.type.interval_pb2 as interval_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.sqladmin_v1.types import (
    cloud_sql_backup_runs,
    cloud_sql_instances,
    cloud_sql_resources,
)

__protobuf__ = proto.module(
    package="google.cloud.sql.v1",
    manifest={
        "CreateBackupRequest",
        "GetBackupRequest",
        "ListBackupsRequest",
        "ListBackupsResponse",
        "UpdateBackupRequest",
        "DeleteBackupRequest",
        "Backup",
    },
)


class CreateBackupRequest(proto.Message):
    r"""The request payload to create the backup

    Attributes:
        parent (str):
            Required. The parent resource where this
            backup is created. Format: projects/{project}
        backup (google.cloud.sqladmin_v1.types.Backup):
            Required. The Backup to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    backup: "Backup" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Backup",
    )


class GetBackupRequest(proto.Message):
    r"""The request payload to get the backup.

    Attributes:
        name (str):
            Required. The name of the backup to retrieve.
            Format: projects/{project}/backups/{backup}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListBackupsRequest(proto.Message):
    r"""The request payload to list the backups.

    Attributes:
        parent (str):
            Required. The parent that owns this
            collection of backups. Format:
            projects/{project}
        page_size (int):
            The maximum number of backups to return per
            response. The service might return fewer backups
            than this value. If a value for this parameter
            isn't specified, then, at most, 500 backups are
            returned. The maximum value is 2,000. Any values
            that you set, which are greater than 2,000, are
            changed to 2,000.
        page_token (str):
            A page token, received from a previous ``ListBackups`` call.
            Provide this to retrieve the subsequent page.

            When paginating, all other parameters provided to
            ``ListBackups`` must match the call that provided the page
            token.
        filter (str):
            Multiple filter queries are separated by
            spaces. For example, 'instance:abc AND
            type:FINAL, 'location:us',
            'backupInterval.startTime>=1950-01-01T01:01:25.771Z'.
            You can filter by type, instance,
            backupInterval.startTime (creation time), or
            location.
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


class ListBackupsResponse(proto.Message):
    r"""The response payload containing a list of the backups.

    Attributes:
        backups (MutableSequence[google.cloud.sqladmin_v1.types.Backup]):
            A list of backups.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, then there aren't
            subsequent pages.
        warnings (MutableSequence[google.cloud.sqladmin_v1.types.ApiWarning]):
            If a region isn't unavailable or if an
            unknown error occurs, then a warning message is
            returned.
    """

    @property
    def raw_page(self):
        return self

    backups: MutableSequence["Backup"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Backup",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    warnings: MutableSequence[cloud_sql_resources.ApiWarning] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=cloud_sql_resources.ApiWarning,
    )


class UpdateBackupRequest(proto.Message):
    r"""The request payload to update the backup.

    Attributes:
        backup (google.cloud.sqladmin_v1.types.Backup):
            Required. The backup to update. The backup’s ``name`` field
            is used to identify the backup to update. Format:
            projects/{project}/backups/{backup}
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The list of fields that you can update. You
            can update only the description and retention
            period of the final backup.
    """

    backup: "Backup" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Backup",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteBackupRequest(proto.Message):
    r"""The request payload to delete the backup.

    Attributes:
        name (str):
            Required. The name of the backup to delete.
            Format: projects/{project}/backups/{backup}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class Backup(proto.Message):
    r"""A backup resource.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Output only. The resource name of the backup.
            Format: projects/{project}/backups/{backup}.
        kind (str):
            Output only. This is always ``sql#backup``.
        self_link (str):
            Output only. The URI of this resource.
        type_ (google.cloud.sqladmin_v1.types.Backup.SqlBackupType):
            Output only. The type of this backup. The type can be
            "AUTOMATED", "ON_DEMAND" or “FINAL”.
        description (str):
            The description of this backup.
        instance (str):
            The name of the source database instance.
        location (str):
            The storage location of the backups. The
            location can be multi-regional.
        backup_interval (google.type.interval_pb2.Interval):
            Output only. This output contains the following values:
            start_time: All database writes up to this time are
            available. end_time: Any database writes after this time
            aren't available.
        state (google.cloud.sqladmin_v1.types.Backup.SqlBackupState):
            Output only. The status of this backup.
        error (google.cloud.sqladmin_v1.types.OperationError):
            Output only. Information about why the backup
            operation fails (for example, when the backup
            state fails).
        kms_key (str):
            Output only. This output contains the
            encryption configuration for a backup and the
            resource name of the KMS key for disk
            encryption.
        kms_key_version (str):
            Output only. This output contains the
            encryption status for a backup and the version
            of the KMS key that's used to encrypt the Cloud
            SQL instance.
        backup_kind (google.cloud.sqladmin_v1.types.SqlBackupKind):
            Output only. Specifies the kind of backup, PHYSICAL or
            DEFAULT_SNAPSHOT.
        time_zone (str):
            Output only. This output contains a backup
            time zone. If a Cloud SQL for SQL Server
            instance has a different time zone from the
            backup's time zone, then the restore to the
            instance doesn't happen.
        ttl_days (int):
            Input only. The time-to-live (TTL) interval
            for this resource (in days). For example:
            ttlDays:7, means 7 days from the current time.
            The expiration time can't exceed 365 days from
            the time that the backup is created.

            This field is a member of `oneof`_ ``expiration``.
        expiry_time (google.protobuf.timestamp_pb2.Timestamp):
            Backup expiration time.
            A UTC timestamp of when this backup expired.

            This field is a member of `oneof`_ ``expiration``.
        database_version (google.cloud.sqladmin_v1.types.SqlDatabaseVersion):
            Output only. The database version of the
            instance of at the time this backup was made.
        max_chargeable_bytes (int):
            Output only. The maximum chargeable bytes for
            the backup.

            This field is a member of `oneof`_ ``_max_chargeable_bytes``.
        instance_deletion_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. Output only. Timestamp in UTC of
            when the instance associated with this backup is
            deleted.
        instance_settings (google.cloud.sqladmin_v1.types.DatabaseInstance):
            Optional. Output only. The instance setting
            of the source instance that's associated with
            this backup.
        backup_run (str):
            Output only. The mapping to backup run
            resource used for IAM validations.
        satisfies_pzs (google.protobuf.wrappers_pb2.BoolValue):
            Output only. This status indicates whether
            the backup satisfies PZS.
            The status is reserved for future use.
        satisfies_pzi (google.protobuf.wrappers_pb2.BoolValue):
            Output only. This status indicates whether
            the backup satisfies PZI.
            The status is reserved for future use.
    """

    class SqlBackupType(proto.Enum):
        r"""The backup type.

        Values:
            SQL_BACKUP_TYPE_UNSPECIFIED (0):
                This is an unknown backup type.
            AUTOMATED (1):
                The backup schedule triggers a backup
                automatically.
            ON_DEMAND (2):
                The user triggers a backup manually.
            FINAL (3):
                The backup created when instance is deleted.
        """

        SQL_BACKUP_TYPE_UNSPECIFIED = 0
        AUTOMATED = 1
        ON_DEMAND = 2
        FINAL = 3

    class SqlBackupState(proto.Enum):
        r"""The backup's state

        Values:
            SQL_BACKUP_STATE_UNSPECIFIED (0):
                The state of the backup is unknown.
            ENQUEUED (1):
                The backup that's added to a queue.
            RUNNING (2):
                The backup is in progress.
            FAILED (3):
                The backup failed.
            SUCCESSFUL (4):
                The backup is successful.
            DELETING (5):
                The backup is being deleted.
            DELETION_FAILED (6):
                Deletion of the backup failed.
        """

        SQL_BACKUP_STATE_UNSPECIFIED = 0
        ENQUEUED = 1
        RUNNING = 2
        FAILED = 3
        SUCCESSFUL = 4
        DELETING = 5
        DELETION_FAILED = 6

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    kind: str = proto.Field(
        proto.STRING,
        number=2,
    )
    self_link: str = proto.Field(
        proto.STRING,
        number=3,
    )
    type_: SqlBackupType = proto.Field(
        proto.ENUM,
        number=4,
        enum=SqlBackupType,
    )
    description: str = proto.Field(
        proto.STRING,
        number=5,
    )
    instance: str = proto.Field(
        proto.STRING,
        number=6,
    )
    location: str = proto.Field(
        proto.STRING,
        number=7,
    )
    backup_interval: interval_pb2.Interval = proto.Field(
        proto.MESSAGE,
        number=8,
        message=interval_pb2.Interval,
    )
    state: SqlBackupState = proto.Field(
        proto.ENUM,
        number=9,
        enum=SqlBackupState,
    )
    error: cloud_sql_resources.OperationError = proto.Field(
        proto.MESSAGE,
        number=10,
        message=cloud_sql_resources.OperationError,
    )
    kms_key: str = proto.Field(
        proto.STRING,
        number=11,
    )
    kms_key_version: str = proto.Field(
        proto.STRING,
        number=12,
    )
    backup_kind: cloud_sql_backup_runs.SqlBackupKind = proto.Field(
        proto.ENUM,
        number=13,
        enum=cloud_sql_backup_runs.SqlBackupKind,
    )
    time_zone: str = proto.Field(
        proto.STRING,
        number=15,
    )
    ttl_days: int = proto.Field(
        proto.INT64,
        number=16,
        oneof="expiration",
    )
    expiry_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=17,
        oneof="expiration",
        message=timestamp_pb2.Timestamp,
    )
    database_version: cloud_sql_resources.SqlDatabaseVersion = proto.Field(
        proto.ENUM,
        number=20,
        enum=cloud_sql_resources.SqlDatabaseVersion,
    )
    max_chargeable_bytes: int = proto.Field(
        proto.INT64,
        number=23,
        optional=True,
    )
    instance_deletion_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=24,
        message=timestamp_pb2.Timestamp,
    )
    instance_settings: cloud_sql_instances.DatabaseInstance = proto.Field(
        proto.MESSAGE,
        number=25,
        message=cloud_sql_instances.DatabaseInstance,
    )
    backup_run: str = proto.Field(
        proto.STRING,
        number=26,
    )
    satisfies_pzs: wrappers_pb2.BoolValue = proto.Field(
        proto.MESSAGE,
        number=27,
        message=wrappers_pb2.BoolValue,
    )
    satisfies_pzi: wrappers_pb2.BoolValue = proto.Field(
        proto.MESSAGE,
        number=28,
        message=wrappers_pb2.BoolValue,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
