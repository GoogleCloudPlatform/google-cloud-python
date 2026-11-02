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

import google.protobuf.duration_pb2 as duration_pb2  # type: ignore
import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.rpc.status_pb2 as status_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.sqladmin_v1beta4.types import cloud_sql_resources

__protobuf__ = proto.module(
    package="google.cloud.sql.v1beta4",
    manifest={
        "ExternalSyncParallelLevel",
        "CreateBackupRequest",
        "GetBackupRequest",
        "ListBackupsRequest",
        "ListBackupsResponse",
        "UpdateBackupRequest",
        "DeleteBackupRequest",
        "SqlBackupRunsDeleteRequest",
        "SqlBackupRunsGetRequest",
        "SqlBackupRunsInsertRequest",
        "SqlBackupRunsListRequest",
        "SqlDatabasesDeleteRequest",
        "SqlDatabasesGetRequest",
        "SqlDatabasesInsertRequest",
        "SqlDatabasesListRequest",
        "SqlDatabasesUpdateRequest",
        "SqlFlagsListRequest",
        "SqlInstancesAddServerCaRequest",
        "SqlInstancesAddServerCertificateRequest",
        "SqlInstancesAddEntraIdCertificateRequest",
        "SqlInstancesCloneRequest",
        "SqlInstancesDeleteRequest",
        "SqlInstancesDemoteMasterRequest",
        "SqlInstancesDemoteRequest",
        "SqlInstancesExportRequest",
        "SqlInstancesFailoverRequest",
        "SqlInstancesGetRequest",
        "SqlInstancesImportRequest",
        "SqlInstancesInsertRequest",
        "SqlInstancesListRequest",
        "SqlInstancesListServerCasRequest",
        "SqlInstancesListServerCertificatesRequest",
        "SqlInstancesListEntraIdCertificatesRequest",
        "SqlInstancesPatchRequest",
        "SqlInstancesPromoteReplicaRequest",
        "SqlInstancesSwitchoverRequest",
        "SqlInstancesResetSslConfigRequest",
        "SqlInstancesRestartRequest",
        "SqlInstancesRestoreBackupRequest",
        "SqlInstancesRotateServerCaRequest",
        "SqlInstancesRotateServerCertificateRequest",
        "SqlInstancesRotateEntraIdCertificateRequest",
        "SqlInstancesStartReplicaRequest",
        "SqlInstancesStopReplicaRequest",
        "SqlInstancesTruncateLogRequest",
        "SqlInstancesUpdateRequest",
        "SqlInstancesReencryptRequest",
        "InstancesReencryptRequest",
        "BackupReencryptionConfig",
        "SqlInstancesRescheduleMaintenanceRequest",
        "SqlInstancesPerformDiskShrinkRequest",
        "ExternalSyncSelectedObject",
        "SqlInstancesVerifyExternalSyncSettingsRequest",
        "SqlInstancesStartExternalSyncRequest",
        "SqlInstancesResetReplicaSizeRequest",
        "SqlOperationsGetRequest",
        "SqlOperationsListRequest",
        "SqlOperationsCancelRequest",
        "SqlInstancesCreateEphemeralCertRequest",
        "SqlSslCertsDeleteRequest",
        "SqlSslCertsGetRequest",
        "SqlSslCertsInsertRequest",
        "SqlSslCertsListRequest",
        "SqlInstancesGetDiskShrinkConfigRequest",
        "SqlInstancesGetLatestRecoveryTimeRequest",
        "SqlInstancesGetLatestRecoveryTimeResponse",
        "SqlInstancesExecuteSqlRequest",
        "SqlInstancesReleaseSsrsLeaseRequest",
        "SqlInstancesReleaseSsrsLeaseResponse",
        "ExecuteSqlPayload",
        "SqlInstancesExecuteSqlResponse",
        "QueryResult",
        "Column",
        "Row",
        "Value",
        "Metadata",
        "SqlInstancesAcquireSsrsLeaseRequest",
        "SqlInstancesPreCheckMajorVersionUpgradeRequest",
        "SqlInstancesAcquireSsrsLeaseResponse",
        "SqlInstancesPointInTimeRestoreRequest",
    },
)


class ExternalSyncParallelLevel(proto.Enum):
    r"""External Sync parallel level.

    Values:
        EXTERNAL_SYNC_PARALLEL_LEVEL_UNSPECIFIED (0):
            Unknown sync parallel level. Will be
            defaulted to OPTIMAL.
        MIN (1):
            Minimal parallel level.
        OPTIMAL (2):
            Optimal parallel level.
        MAX (3):
            Maximum parallel level.
    """

    EXTERNAL_SYNC_PARALLEL_LEVEL_UNSPECIFIED = 0
    MIN = 1
    OPTIMAL = 2
    MAX = 3


class CreateBackupRequest(proto.Message):
    r"""The request payload to create the backup

    Attributes:
        parent (str):
            Required. The parent resource where this
            backup is created. Format: projects/{project}
        backup (google.cloud.sqladmin_v1beta4.types.Backup):
            Required. The Backup to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    backup: cloud_sql_resources.Backup = proto.Field(
        proto.MESSAGE,
        number=2,
        message=cloud_sql_resources.Backup,
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
        backups (MutableSequence[google.cloud.sqladmin_v1beta4.types.Backup]):
            A list of backups.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, then there aren't
            subsequent pages.
        warnings (MutableSequence[google.cloud.sqladmin_v1beta4.types.ApiWarning]):
            If a region isn't unavailable or if an
            unknown error occurs, then a warning message is
            returned.
    """

    @property
    def raw_page(self):
        return self

    backups: MutableSequence[cloud_sql_resources.Backup] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=cloud_sql_resources.Backup,
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
        backup (google.cloud.sqladmin_v1beta4.types.Backup):
            Required. The backup to update. The backup’s ``name`` field
            is used to identify the backup to update. Format:
            projects/{project}/backups/{backup}
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The list of fields that you can update. You
            can update only the description and retention
            period of the final backup.
    """

    backup: cloud_sql_resources.Backup = proto.Field(
        proto.MESSAGE,
        number=1,
        message=cloud_sql_resources.Backup,
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


class SqlBackupRunsDeleteRequest(proto.Message):
    r"""

    Attributes:
        id (int):
            The ID of the backup run to delete. To find a backup run ID,
            use the
            `list <https://cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/backupRuns/list>`__
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
    r"""

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
    r"""

    Attributes:
        instance (str):
            Cloud SQL instance ID. This does not include
            the project ID.
        project (str):
            Project ID of the project that contains the
            instance.
        body (google.cloud.sqladmin_v1beta4.types.BackupRun):

    """

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    body: cloud_sql_resources.BackupRun = proto.Field(
        proto.MESSAGE,
        number=100,
        message=cloud_sql_resources.BackupRun,
    )


class SqlBackupRunsListRequest(proto.Message):
    r"""

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


class SqlDatabasesDeleteRequest(proto.Message):
    r"""

    Attributes:
        database (str):
            Name of the database to be deleted in the
            instance.
        instance (str):
            Database instance ID. This does not include
            the project ID.
        project (str):
            Project ID of the project that contains the
            instance.
        location (str):
            Optional. Region of the Cloud SQL instance.
    """

    database: str = proto.Field(
        proto.STRING,
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
    location: str = proto.Field(
        proto.STRING,
        number=4,
    )


class SqlDatabasesGetRequest(proto.Message):
    r"""

    Attributes:
        database (str):
            Name of the database in the instance.
        instance (str):
            Database instance ID. This does not include
            the project ID.
        project (str):
            Project ID of the project that contains the
            instance.
        location (str):
            Optional. Region of the Cloud SQL instance.
    """

    database: str = proto.Field(
        proto.STRING,
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
    location: str = proto.Field(
        proto.STRING,
        number=4,
    )


class SqlDatabasesInsertRequest(proto.Message):
    r"""

    Attributes:
        instance (str):
            Database instance ID. This does not include
            the project ID.
        project (str):
            Project ID of the project that contains the
            instance.
        body (google.cloud.sqladmin_v1beta4.types.Database):

        location (str):
            Optional. Region of the Cloud SQL instance.
    """

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    body: cloud_sql_resources.Database = proto.Field(
        proto.MESSAGE,
        number=100,
        message=cloud_sql_resources.Database,
    )
    location: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SqlDatabasesListRequest(proto.Message):
    r"""

    Attributes:
        instance (str):
            Cloud SQL instance ID. This does not include
            the project ID.
        project (str):
            Project ID of the project that contains the
            instance.
        location (str):
            Optional. Region of the Cloud SQL instance.
    """

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    location: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SqlDatabasesUpdateRequest(proto.Message):
    r"""

    Attributes:
        database (str):
            Name of the database to be updated in the
            instance.
        instance (str):
            Database instance ID. This does not include
            the project ID.
        project (str):
            Project ID of the project that contains the
            instance.
        body (google.cloud.sqladmin_v1beta4.types.Database):

        location (str):
            Optional. Region of the Cloud SQL instance.
    """

    database: str = proto.Field(
        proto.STRING,
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
    body: cloud_sql_resources.Database = proto.Field(
        proto.MESSAGE,
        number=100,
        message=cloud_sql_resources.Database,
    )
    location: str = proto.Field(
        proto.STRING,
        number=4,
    )


class SqlFlagsListRequest(proto.Message):
    r"""

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        database_version (str):
            Database type and version you want to
            retrieve flags for. By default, this method
            returns flags for all database types and
            versions.
        flag_scope (google.cloud.sqladmin_v1beta4.types.SqlFlagScope):
            Optional. Specify the scope of flags to be
            returned by SqlFlagsListService. Return list of
            database flags if unspecified.

            This field is a member of `oneof`_ ``_flag_scope``.
    """

    database_version: str = proto.Field(
        proto.STRING,
        number=1,
    )
    flag_scope: cloud_sql_resources.SqlFlagScope = proto.Field(
        proto.ENUM,
        number=3,
        optional=True,
        enum=cloud_sql_resources.SqlFlagScope,
    )


class SqlInstancesAddServerCaRequest(proto.Message):
    r"""

    Attributes:
        instance (str):
            Cloud SQL instance ID. This does not include
            the project ID.
        project (str):
            Project ID of the project that contains the
            instance.
        location (str):
            Optional. Region of the Cloud SQL instance.
    """

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    location: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SqlInstancesAddServerCertificateRequest(proto.Message):
    r"""Request for AddServerCertificate RPC.

    Attributes:
        instance (str):
            Required. Cloud SQL instance ID. This does
            not include the project ID.
        project (str):
            Required. Project ID of the project that
            contains the instance.
        location (str):
            Optional. Region of the Cloud SQL instance.
    """

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    location: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SqlInstancesAddEntraIdCertificateRequest(proto.Message):
    r"""Request for AddEntraIdCertificate RPC.

    Attributes:
        instance (str):
            Required. Cloud SQL instance ID. This does
            not include the project ID.
        project (str):
            Required. Project ID of the project that
            contains the instance.
        location (str):
            Optional. Region of the Cloud SQL instance.
    """

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    location: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SqlInstancesCloneRequest(proto.Message):
    r"""

    Attributes:
        instance (str):
            The ID of the Cloud SQL instance to be cloned
            (source). This does not include the project ID.
        project (str):
            Project ID of the source Cloud SQL instance.
        body (google.cloud.sqladmin_v1beta4.types.InstancesCloneRequest):

        location (str):
            Optional. Region of the Cloud SQL instance.
    """

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    body: cloud_sql_resources.InstancesCloneRequest = proto.Field(
        proto.MESSAGE,
        number=100,
        message=cloud_sql_resources.InstancesCloneRequest,
    )
    location: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SqlInstancesDeleteRequest(proto.Message):
    r"""

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        instance (str):
            Cloud SQL instance ID. This does not include
            the project ID.
        project (str):
            Project ID of the project that contains the
            instance to be deleted.
        enable_final_backup (bool):
            Flag to opt-in for final backup. By default,
            it is turned off.

            This field is a member of `oneof`_ ``_enable_final_backup``.
        final_backup_ttl_days (int):
            Optional. Retention period of the final
            backup.

            This field is a member of `oneof`_ ``expiration``.
        final_backup_expiry_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. Final Backup expiration time.
            Timestamp in UTC of when this resource is
            considered expired.

            This field is a member of `oneof`_ ``expiration``.
        final_backup_description (str):
            Optional. The description of the final
            backup.
        location (str):
            Optional. Region of the Cloud SQL instance.
    """

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    enable_final_backup: bool = proto.Field(
        proto.BOOL,
        number=7,
        optional=True,
    )
    final_backup_ttl_days: int = proto.Field(
        proto.INT64,
        number=4,
        oneof="expiration",
    )
    final_backup_expiry_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="expiration",
        message=timestamp_pb2.Timestamp,
    )
    final_backup_description: str = proto.Field(
        proto.STRING,
        number=5,
    )
    location: str = proto.Field(
        proto.STRING,
        number=11,
    )


class SqlInstancesDemoteMasterRequest(proto.Message):
    r"""

    Attributes:
        instance (str):
            Cloud SQL instance name.
        project (str):
            ID of the project that contains the instance.
        body (google.cloud.sqladmin_v1beta4.types.InstancesDemoteMasterRequest):

        location (str):
            Optional. Region of the Cloud SQL instance.
    """

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    body: cloud_sql_resources.InstancesDemoteMasterRequest = proto.Field(
        proto.MESSAGE,
        number=100,
        message=cloud_sql_resources.InstancesDemoteMasterRequest,
    )
    location: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SqlInstancesDemoteRequest(proto.Message):
    r"""Instance demote request.

    Attributes:
        instance (str):
            Required. The name of the Cloud SQL instance.
        project (str):
            Required. The project ID of the project that
            contains the instance.
        body (google.cloud.sqladmin_v1beta4.types.InstancesDemoteRequest):
            The request body.
        location (str):
            Optional. Region of the Cloud SQL instance.
    """

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    body: cloud_sql_resources.InstancesDemoteRequest = proto.Field(
        proto.MESSAGE,
        number=100,
        message=cloud_sql_resources.InstancesDemoteRequest,
    )
    location: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SqlInstancesExportRequest(proto.Message):
    r"""

    Attributes:
        instance (str):
            The Cloud SQL instance ID. This doesn't
            include the project ID.
        project (str):
            Project ID of the project that contains the
            instance to be exported.
        body (google.cloud.sqladmin_v1beta4.types.InstancesExportRequest):

        location (str):
            Optional. Region of the Cloud SQL instance.
    """

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    body: cloud_sql_resources.InstancesExportRequest = proto.Field(
        proto.MESSAGE,
        number=100,
        message=cloud_sql_resources.InstancesExportRequest,
    )
    location: str = proto.Field(
        proto.STRING,
        number=5,
    )


class SqlInstancesFailoverRequest(proto.Message):
    r"""

    Attributes:
        instance (str):
            Cloud SQL instance ID. This does not include
            the project ID.
        project (str):
            ID of the project that contains the read
            replica.
        body (google.cloud.sqladmin_v1beta4.types.InstancesFailoverRequest):

        location (str):
            Optional. Region of the Cloud SQL instance.
    """

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    body: cloud_sql_resources.InstancesFailoverRequest = proto.Field(
        proto.MESSAGE,
        number=100,
        message=cloud_sql_resources.InstancesFailoverRequest,
    )
    location: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SqlInstancesGetRequest(proto.Message):
    r"""

    Attributes:
        instance (str):
            Database instance ID. This does not include
            the project ID.
        project (str):
            Project ID of the project that contains the
            instance.
        location (str):
            Optional. Region of the Cloud SQL instance.
    """

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    location: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SqlInstancesImportRequest(proto.Message):
    r"""

    Attributes:
        instance (str):
            Cloud SQL instance ID. This does not include
            the project ID.
        project (str):
            Project ID of the project that contains the
            instance.
        body (google.cloud.sqladmin_v1beta4.types.InstancesImportRequest):

        location (str):
            Optional. Region of the Cloud SQL instance.
    """

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    body: cloud_sql_resources.InstancesImportRequest = proto.Field(
        proto.MESSAGE,
        number=100,
        message=cloud_sql_resources.InstancesImportRequest,
    )
    location: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SqlInstancesInsertRequest(proto.Message):
    r"""

    Attributes:
        project (str):
            Project ID of the project to which the newly
            created Cloud SQL instances should belong.
        body (google.cloud.sqladmin_v1beta4.types.DatabaseInstance):

        location (str):
            Optional. Region of the Cloud SQL instance.
    """

    project: str = proto.Field(
        proto.STRING,
        number=1,
    )
    body: cloud_sql_resources.DatabaseInstance = proto.Field(
        proto.MESSAGE,
        number=100,
        message=cloud_sql_resources.DatabaseInstance,
    )
    location: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SqlInstancesListRequest(proto.Message):
    r"""

    Attributes:
        filter (str):
            A filter expression that filters resources listed in the
            response. The expression is in the form of field:value. For
            example, 'instanceType:CLOUD_SQL_INSTANCE'. Fields can be
            nested as needed as per their JSON representation, such as
            'settings.userLabels.auto_start:true'.

            Multiple filter queries are space-separated. For example.
            'state:RUNNABLE instanceType:CLOUD_SQL_INSTANCE'. By
            default, each expression is an AND expression. However, you
            can include AND and OR expressions explicitly.
        max_results (int):
            The maximum number of instances to return.
            The service may return fewer than this value. If
            unspecified, at most 500 instances are returned.
            The maximum value is 1000; values above 1000 are
            coerced to 1000.
        page_token (str):
            A previously-returned page token representing
            part of the larger set of results to view.
        project (str):
            Project ID of the project for which to list
            Cloud SQL instances.
        location (str):
            Optional. Region of the Cloud SQL instance.
    """

    filter: str = proto.Field(
        proto.STRING,
        number=1,
    )
    max_results: int = proto.Field(
        proto.UINT32,
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
    location: str = proto.Field(
        proto.STRING,
        number=5,
    )


class SqlInstancesListServerCasRequest(proto.Message):
    r"""

    Attributes:
        instance (str):
            Cloud SQL instance ID. This does not include
            the project ID.
        project (str):
            Project ID of the project that contains the
            instance.
        location (str):
            Optional. Region of the Cloud SQL instance.
    """

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    location: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SqlInstancesListServerCertificatesRequest(proto.Message):
    r"""

    Attributes:
        instance (str):
            Required. Cloud SQL instance ID. This does
            not include the project ID.
        project (str):
            Required. Project ID of the project that
            contains the instance.
        location (str):
            Optional. Region of the Cloud SQL instance.
    """

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    location: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SqlInstancesListEntraIdCertificatesRequest(proto.Message):
    r"""Request message for
    SqlInstancesService.ListEntraIdCertificates.

    Attributes:
        instance (str):
            Required. Cloud SQL instance ID. This does
            not include the project ID.
        project (str):
            Required. Project ID of the project that
            contains the instance.
        location (str):
            Optional. Region of the Cloud SQL instance.
    """

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    location: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SqlInstancesPatchRequest(proto.Message):
    r"""

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        instance (str):
            Cloud SQL instance ID. This does not include
            the project ID.
        project (str):
            Project ID of the project that contains the
            instance.
        reconcile_psc_networking (bool):
            Optional. Set PSC config to the same value as
            the existing config to reconcile the PSC
            networking.

            This field is a member of `oneof`_ ``_reconcile_psc_networking``.
        reconcile_psc_networking_force (bool):
            Optional. Set PSC config to the same value as
            the existing config and force reconcile the PSC
            networking.

            This field is a member of `oneof`_ ``_reconcile_psc_networking_force``.
        body (google.cloud.sqladmin_v1beta4.types.DatabaseInstance):

        location (str):
            Optional. Region of the Cloud SQL instance.
    """

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    reconcile_psc_networking: bool = proto.Field(
        proto.BOOL,
        number=4,
        optional=True,
    )
    reconcile_psc_networking_force: bool = proto.Field(
        proto.BOOL,
        number=5,
        optional=True,
    )
    body: cloud_sql_resources.DatabaseInstance = proto.Field(
        proto.MESSAGE,
        number=100,
        message=cloud_sql_resources.DatabaseInstance,
    )
    location: str = proto.Field(
        proto.STRING,
        number=6,
    )


class SqlInstancesPromoteReplicaRequest(proto.Message):
    r"""

    Attributes:
        instance (str):
            Cloud SQL read replica instance name.
        project (str):
            ID of the project that contains the read
            replica.
        failover (bool):
            Set to true to invoke a replica failover to
            the DR replica. As part of replica failover, the
            promote operation attempts to add the original
            primary instance as a replica of the promoted DR
            replica when the original primary instance comes
            back online. If set to false or not specified,
            then the original primary instance becomes an
            independent Cloud SQL primary instance.
        location (str):
            Optional. Region of the Cloud SQL instance.
    """

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    failover: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    location: str = proto.Field(
        proto.STRING,
        number=4,
    )


class SqlInstancesSwitchoverRequest(proto.Message):
    r"""Instance switchover request.

    Attributes:
        instance (str):
            Cloud SQL read replica instance name.
        project (str):
            ID of the project that contains the replica.
        db_timeout (google.protobuf.duration_pb2.Duration):
            Optional. (MySQL and PostgreSQL only) Cloud
            SQL instance operations timeout, which is a sum
            of all database operations. Default value is 10
            minutes and can be modified to a maximum value
            of 24 hours.
        location (str):
            Optional. Region of the Cloud SQL instance.
    """

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    db_timeout: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=3,
        message=duration_pb2.Duration,
    )
    location: str = proto.Field(
        proto.STRING,
        number=4,
    )


class SqlInstancesResetSslConfigRequest(proto.Message):
    r"""

    Attributes:
        instance (str):
            Cloud SQL instance ID. This does not include
            the project ID.
        project (str):
            Project ID of the project that contains the
            instance.
        mode (google.cloud.sqladmin_v1beta4.types.SqlInstancesResetSslConfigRequest.ResetSslMode):
            Optional. Reset SSL mode to use.
        location (str):
            Optional. Region of the Cloud SQL instance.
    """

    class ResetSslMode(proto.Enum):
        r"""Reset SSL mode to selectively refresh the SSL materials.

        Values:
            RESET_SSL_MODE_UNSPECIFIED (0):
                Reset SSL mode is not specified.
            ALL (1):
                Refresh all TLS configs. This is the default
                behaviour.
            SYNC_FROM_PRIMARY (2):
                Refreshes the replication-related TLS
                configuration settings provided by the primary
                instance. Not applicable to on-premises
                replication instances.
        """

        RESET_SSL_MODE_UNSPECIFIED = 0
        ALL = 1
        SYNC_FROM_PRIMARY = 2

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    mode: ResetSslMode = proto.Field(
        proto.ENUM,
        number=3,
        enum=ResetSslMode,
    )
    location: str = proto.Field(
        proto.STRING,
        number=4,
    )


class SqlInstancesRestartRequest(proto.Message):
    r"""

    Attributes:
        instance (str):
            Cloud SQL instance ID. This does not include
            the project ID.
        project (str):
            Project ID of the project that contains the
            instance to be restarted.
        location (str):
            Optional. Region of the Cloud SQL instance.
    """

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    location: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SqlInstancesRestoreBackupRequest(proto.Message):
    r"""

    Attributes:
        instance (str):
            Cloud SQL instance ID. This does not include
            the project ID.
        project (str):
            Project ID of the project that contains the
            instance.
        body (google.cloud.sqladmin_v1beta4.types.InstancesRestoreBackupRequest):

        location (str):
            Optional. Region of the Cloud SQL instance.
    """

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    body: cloud_sql_resources.InstancesRestoreBackupRequest = proto.Field(
        proto.MESSAGE,
        number=100,
        message=cloud_sql_resources.InstancesRestoreBackupRequest,
    )
    location: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SqlInstancesRotateServerCaRequest(proto.Message):
    r"""

    Attributes:
        instance (str):
            Cloud SQL instance ID. This does not include
            the project ID.
        project (str):
            Project ID of the project that contains the
            instance.
        body (google.cloud.sqladmin_v1beta4.types.InstancesRotateServerCaRequest):

        location (str):
            Optional. Region of the Cloud SQL instance.
    """

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    body: cloud_sql_resources.InstancesRotateServerCaRequest = proto.Field(
        proto.MESSAGE,
        number=100,
        message=cloud_sql_resources.InstancesRotateServerCaRequest,
    )
    location: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SqlInstancesRotateServerCertificateRequest(proto.Message):
    r"""

    Attributes:
        instance (str):
            Required. Cloud SQL instance ID. This does
            not include the project ID.
        project (str):
            Required. Project ID of the project that
            contains the instance.
        body (google.cloud.sqladmin_v1beta4.types.InstancesRotateServerCertificateRequest):
            Required. Rotate server certificate request
            body.
        location (str):
            Optional. Region of the Cloud SQL instance.
    """

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    body: cloud_sql_resources.InstancesRotateServerCertificateRequest = proto.Field(
        proto.MESSAGE,
        number=100,
        message=cloud_sql_resources.InstancesRotateServerCertificateRequest,
    )
    location: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SqlInstancesRotateEntraIdCertificateRequest(proto.Message):
    r"""Request message for
    SqlInstancesService.RotateEntraIdCertificate.

    Attributes:
        instance (str):
            Required. Cloud SQL instance ID. This does
            not include the project ID.
        project (str):
            Required. Project ID of the project that
            contains the instance.
        body (google.cloud.sqladmin_v1beta4.types.InstancesRotateEntraIdCertificateRequest):
            Required. Rotate Entra ID certificate request
            body.
        location (str):
            Optional. Region of the Cloud SQL instance.
    """

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    body: cloud_sql_resources.InstancesRotateEntraIdCertificateRequest = proto.Field(
        proto.MESSAGE,
        number=100,
        message=cloud_sql_resources.InstancesRotateEntraIdCertificateRequest,
    )
    location: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SqlInstancesStartReplicaRequest(proto.Message):
    r"""

    Attributes:
        instance (str):
            Cloud SQL read replica instance name.
        project (str):
            ID of the project that contains the read
            replica.
        location (str):
            Optional. Region of the Cloud SQL instance.
    """

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    location: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SqlInstancesStopReplicaRequest(proto.Message):
    r"""

    Attributes:
        instance (str):
            Cloud SQL read replica instance name.
        project (str):
            ID of the project that contains the read
            replica.
        location (str):
            Optional. Region of the Cloud SQL instance.
    """

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    location: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SqlInstancesTruncateLogRequest(proto.Message):
    r"""

    Attributes:
        instance (str):
            Cloud SQL instance ID. This does not include
            the project ID.
        project (str):
            Project ID of the Cloud SQL project.
        body (google.cloud.sqladmin_v1beta4.types.InstancesTruncateLogRequest):

        location (str):
            Optional. Region of the Cloud SQL instance.
    """

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    body: cloud_sql_resources.InstancesTruncateLogRequest = proto.Field(
        proto.MESSAGE,
        number=100,
        message=cloud_sql_resources.InstancesTruncateLogRequest,
    )
    location: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SqlInstancesUpdateRequest(proto.Message):
    r"""

    Attributes:
        instance (str):
            Cloud SQL instance ID. This does not include
            the project ID.
        project (str):
            Project ID of the project that contains the
            instance.
        body (google.cloud.sqladmin_v1beta4.types.DatabaseInstance):

        location (str):
            Optional. Region of the Cloud SQL instance.
    """

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    body: cloud_sql_resources.DatabaseInstance = proto.Field(
        proto.MESSAGE,
        number=100,
        message=cloud_sql_resources.DatabaseInstance,
    )
    location: str = proto.Field(
        proto.STRING,
        number=4,
    )


class SqlInstancesReencryptRequest(proto.Message):
    r"""Instance reencrypt request.

    Attributes:
        instance (str):
            Cloud SQL instance ID. This does not include
            the project ID.
        project (str):
            ID of the project that contains the instance.
        body (google.cloud.sqladmin_v1beta4.types.InstancesReencryptRequest):
            Reencrypt body that users request
        location (str):
            Optional. Region of the Cloud SQL instance.
    """

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    body: "InstancesReencryptRequest" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="InstancesReencryptRequest",
    )
    location: str = proto.Field(
        proto.STRING,
        number=4,
    )


class InstancesReencryptRequest(proto.Message):
    r"""Database Instance reencrypt request.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        backup_reencryption_config (google.cloud.sqladmin_v1beta4.types.BackupReencryptionConfig):
            Configuration specific to backup
            re-encryption

            This field is a member of `oneof`_ ``_backup_reencryption_config``.
    """

    backup_reencryption_config: "BackupReencryptionConfig" = proto.Field(
        proto.MESSAGE,
        number=1,
        optional=True,
        message="BackupReencryptionConfig",
    )


class BackupReencryptionConfig(proto.Message):
    r"""Backup Reencryption Config

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        backup_limit (int):
            Backup re-encryption limit

            This field is a member of `oneof`_ ``_backup_limit``.
        backup_type (google.cloud.sqladmin_v1beta4.types.BackupReencryptionConfig.BackupType):
            Type of backups users want to re-encrypt.

            This field is a member of `oneof`_ ``_backup_type``.
    """

    class BackupType(proto.Enum):
        r"""Backup type for re-encryption

        Values:
            BACKUP_TYPE_UNSPECIFIED (0):
                Unknown backup type, will be defaulted to
                AUTOMATIC backup type
            AUTOMATED (1):
                Reencrypt automatic backups
            ON_DEMAND (2):
                Reencrypt on-demand backups
        """

        BACKUP_TYPE_UNSPECIFIED = 0
        AUTOMATED = 1
        ON_DEMAND = 2

    backup_limit: int = proto.Field(
        proto.INT32,
        number=1,
        optional=True,
    )
    backup_type: BackupType = proto.Field(
        proto.ENUM,
        number=2,
        optional=True,
        enum=BackupType,
    )


class SqlInstancesRescheduleMaintenanceRequest(proto.Message):
    r"""

    Attributes:
        instance (str):
            Cloud SQL instance ID. This does not include
            the project ID.
        project (str):
            ID of the project that contains the instance.
        body (google.cloud.sqladmin_v1beta4.types.SqlInstancesRescheduleMaintenanceRequestBody):

        location (str):
            Optional. Region of the Cloud SQL instance.
    """

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    body: cloud_sql_resources.SqlInstancesRescheduleMaintenanceRequestBody = (
        proto.Field(
            proto.MESSAGE,
            number=100,
            message=cloud_sql_resources.SqlInstancesRescheduleMaintenanceRequestBody,
        )
    )
    location: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SqlInstancesPerformDiskShrinkRequest(proto.Message):
    r"""Instance perform disk shrink request.

    Attributes:
        instance (str):
            Cloud SQL instance ID. This does not include
            the project ID.
        project (str):
            Project ID of the project that contains the
            instance.
        body (google.cloud.sqladmin_v1beta4.types.PerformDiskShrinkContext):
            Perform disk shrink context.
        location (str):
            Optional. Region of the Cloud SQL instance.
    """

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    body: cloud_sql_resources.PerformDiskShrinkContext = proto.Field(
        proto.MESSAGE,
        number=100,
        message=cloud_sql_resources.PerformDiskShrinkContext,
    )
    location: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ExternalSyncSelectedObject(proto.Message):
    r"""The selected object that Cloud SQL migrates.

    Attributes:
        database (str):
            The name of the database that Cloud SQL
            migrates.
    """

    database: str = proto.Field(
        proto.STRING,
        number=1,
    )


class SqlInstancesVerifyExternalSyncSettingsRequest(proto.Message):
    r"""

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        instance (str):
            Cloud SQL instance ID. This does not include
            the project ID.
        project (str):
            Project ID of the project that contains the
            instance.
        verify_connection_only (bool):
            Flag to enable verifying connection only
        sync_mode (google.cloud.sqladmin_v1beta4.types.SqlInstancesVerifyExternalSyncSettingsRequest.ExternalSyncMode):
            External sync mode
        verify_replication_only (bool):
            Optional. Flag to verify settings required by
            replication setup only
        mysql_sync_config (google.cloud.sqladmin_v1beta4.types.MySqlSyncConfig):
            Optional. MySQL-specific settings for start
            external sync.

            This field is a member of `oneof`_ ``sync_config``.
        migration_type (google.cloud.sqladmin_v1beta4.types.SqlInstancesVerifyExternalSyncSettingsRequest.MigrationType):
            Optional. MigrationType configures the migration to use
            physical files or logical dump files. If not set, then the
            logical dump file configuration is used. Valid values are
            ``LOGICAL`` or ``PHYSICAL``. Only applicable to MySQL.
        sync_parallel_level (google.cloud.sqladmin_v1beta4.types.ExternalSyncParallelLevel):
            Optional. Parallel level for initial data
            sync. Only applicable for PostgreSQL.
        selected_objects (MutableSequence[google.cloud.sqladmin_v1beta4.types.ExternalSyncSelectedObject]):
            Optional. Migrate only the specified objects
            from the source instance. If this field is
            empty, then migrate all objects.
        location (str):
            Optional. Region of the Cloud SQL instance.
    """

    class ExternalSyncMode(proto.Enum):
        r"""

        Values:
            EXTERNAL_SYNC_MODE_UNSPECIFIED (0):
                Unknown external sync mode, will be defaulted
                to ONLINE mode
            ONLINE (1):
                Online external sync will set up replication
                after initial data external sync
            OFFLINE (2):
                Offline external sync only dumps and loads a
                one-time snapshot of the primary instance's data
        """

        EXTERNAL_SYNC_MODE_UNSPECIFIED = 0
        ONLINE = 1
        OFFLINE = 2

    class MigrationType(proto.Enum):
        r"""MigrationType determines whether the migration is a physical
        file-based migration or a logical dump file-based migration.

        Values:
            MIGRATION_TYPE_UNSPECIFIED (0):
                Default value is a logical dump file-based
                migration
            LOGICAL (1):
                Logical dump file-based migration
            PHYSICAL (2):
                Physical file-based migration
        """

        MIGRATION_TYPE_UNSPECIFIED = 0
        LOGICAL = 1
        PHYSICAL = 2

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    verify_connection_only: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    sync_mode: ExternalSyncMode = proto.Field(
        proto.ENUM,
        number=4,
        enum=ExternalSyncMode,
    )
    verify_replication_only: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    mysql_sync_config: cloud_sql_resources.MySqlSyncConfig = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="sync_config",
        message=cloud_sql_resources.MySqlSyncConfig,
    )
    migration_type: MigrationType = proto.Field(
        proto.ENUM,
        number=7,
        enum=MigrationType,
    )
    sync_parallel_level: "ExternalSyncParallelLevel" = proto.Field(
        proto.ENUM,
        number=8,
        enum="ExternalSyncParallelLevel",
    )
    selected_objects: MutableSequence["ExternalSyncSelectedObject"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=9,
            message="ExternalSyncSelectedObject",
        )
    )
    location: str = proto.Field(
        proto.STRING,
        number=10,
    )


class SqlInstancesStartExternalSyncRequest(proto.Message):
    r"""

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        instance (str):
            Cloud SQL instance ID. This does not include
            the project ID.
        project (str):
            ID of the project that contains the instance.
        sync_mode (google.cloud.sqladmin_v1beta4.types.SqlInstancesVerifyExternalSyncSettingsRequest.ExternalSyncMode):
            External sync mode.
        skip_verification (bool):
            Whether to skip the verification step (VESS).
        mysql_sync_config (google.cloud.sqladmin_v1beta4.types.MySqlSyncConfig):
            MySQL-specific settings for start external
            sync.

            This field is a member of `oneof`_ ``sync_config``.
        sync_parallel_level (google.cloud.sqladmin_v1beta4.types.ExternalSyncParallelLevel):
            Optional. Parallel level for initial data
            sync. Currently only applicable for MySQL.
        migration_type (google.cloud.sqladmin_v1beta4.types.SqlInstancesVerifyExternalSyncSettingsRequest.MigrationType):
            Optional. MigrationType configures the migration to use
            physical files or logical dump files. If not set, then the
            logical dump file configuration is used. Valid values are
            ``LOGICAL`` or ``PHYSICAL``. Only applicable to MySQL.
        replica_overwrite_enabled (bool):
            Optional. MySQL only. True if end-user has confirmed that
            this SES call will wipe replica databases overlapping with
            the proposed selected_objects. If this field is not set and
            there are both overlapping and additional databases
            proposed, an error will be returned.
        location (str):
            Optional. Region of the Cloud SQL instance.
    """

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    sync_mode: "SqlInstancesVerifyExternalSyncSettingsRequest.ExternalSyncMode" = (
        proto.Field(
            proto.ENUM,
            number=3,
            enum="SqlInstancesVerifyExternalSyncSettingsRequest.ExternalSyncMode",
        )
    )
    skip_verification: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    mysql_sync_config: cloud_sql_resources.MySqlSyncConfig = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="sync_config",
        message=cloud_sql_resources.MySqlSyncConfig,
    )
    sync_parallel_level: "ExternalSyncParallelLevel" = proto.Field(
        proto.ENUM,
        number=7,
        enum="ExternalSyncParallelLevel",
    )
    migration_type: "SqlInstancesVerifyExternalSyncSettingsRequest.MigrationType" = (
        proto.Field(
            proto.ENUM,
            number=8,
            enum="SqlInstancesVerifyExternalSyncSettingsRequest.MigrationType",
        )
    )
    replica_overwrite_enabled: bool = proto.Field(
        proto.BOOL,
        number=9,
    )
    location: str = proto.Field(
        proto.STRING,
        number=10,
    )


class SqlInstancesResetReplicaSizeRequest(proto.Message):
    r"""Instance reset replica size request.

    Attributes:
        instance (str):
            Cloud SQL read replica instance name.
        project (str):
            ID of the project that contains the read
            replica.
        location (str):
            Optional. Region of the Cloud SQL instance.
    """

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    location: str = proto.Field(
        proto.STRING,
        number=4,
    )


class SqlOperationsGetRequest(proto.Message):
    r"""

    Attributes:
        operation (str):
            Instance operation ID.
        project (str):
            Project ID of the project that contains the
            instance.
        location (str):
            Optional. Region of the Cloud SQL instance.
    """

    operation: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    location: str = proto.Field(
        proto.STRING,
        number=4,
    )


class SqlOperationsListRequest(proto.Message):
    r"""

    Attributes:
        instance (str):
            Cloud SQL instance ID. This does not include
            the project ID.
        max_results (int):
            Maximum number of operations per response.
        page_token (str):
            A previously-returned page token representing
            part of the larger set of results to view.
        project (str):
            Project ID of the project that contains the
            instance.
        location (str):
            Optional. Region of the Cloud SQL instance.
    """

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    max_results: int = proto.Field(
        proto.UINT32,
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
    location: str = proto.Field(
        proto.STRING,
        number=6,
    )


class SqlOperationsCancelRequest(proto.Message):
    r"""The request payload to cancel an operation.

    Attributes:
        operation (str):
            Instance operation ID.
        project (str):
            Project ID of the project that contains the
            instance.
        location (str):
            Optional. Region of the Cloud SQL instance.
    """

    operation: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    location: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SqlInstancesCreateEphemeralCertRequest(proto.Message):
    r"""

    Attributes:
        instance (str):
            Cloud SQL instance ID. This does not include
            the project ID.
        project (str):
            Project ID of the Cloud SQL project.
        body (google.cloud.sqladmin_v1beta4.types.SslCertsCreateEphemeralRequest):

        location (str):
            Optional. Region of the Cloud SQL instance.
    """

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    body: cloud_sql_resources.SslCertsCreateEphemeralRequest = proto.Field(
        proto.MESSAGE,
        number=100,
        message=cloud_sql_resources.SslCertsCreateEphemeralRequest,
    )
    location: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SqlSslCertsDeleteRequest(proto.Message):
    r"""

    Attributes:
        instance (str):
            Cloud SQL instance ID. This does not include
            the project ID.
        project (str):
            Project ID of the project that contains the
            instance.
        sha1_fingerprint (str):
            Sha1 FingerPrint.
    """

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    sha1_fingerprint: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SqlSslCertsGetRequest(proto.Message):
    r"""

    Attributes:
        instance (str):
            Cloud SQL instance ID. This does not include
            the project ID.
        project (str):
            Project ID of the project that contains the
            instance.
        sha1_fingerprint (str):
            Sha1 FingerPrint.
    """

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    sha1_fingerprint: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SqlSslCertsInsertRequest(proto.Message):
    r"""

    Attributes:
        instance (str):
            Cloud SQL instance ID. This does not include
            the project ID.
        project (str):
            Project ID of the project that contains the
            instance.
        body (google.cloud.sqladmin_v1beta4.types.SslCertsInsertRequest):

    """

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    body: cloud_sql_resources.SslCertsInsertRequest = proto.Field(
        proto.MESSAGE,
        number=100,
        message=cloud_sql_resources.SslCertsInsertRequest,
    )


class SqlSslCertsListRequest(proto.Message):
    r"""

    Attributes:
        instance (str):
            Cloud SQL instance ID. This does not include
            the project ID.
        project (str):
            Project ID of the project that contains the
            instance.
    """

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project: str = proto.Field(
        proto.STRING,
        number=2,
    )


class SqlInstancesGetDiskShrinkConfigRequest(proto.Message):
    r"""Instance get disk shrink config request.

    Attributes:
        instance (str):
            Cloud SQL instance ID. This does not include
            the project ID.
        project (str):
            Project ID of the project that contains the
            instance.
        location (str):
            Optional. Region of the Cloud SQL instance.
    """

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    location: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SqlInstancesGetLatestRecoveryTimeRequest(proto.Message):
    r"""Instance get latest recovery time request.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        instance (str):
            Cloud SQL instance ID. This does not include
            the project ID.
        project (str):
            Project ID of the project that contains the
            instance.
        source_instance_deletion_time (google.protobuf.timestamp_pb2.Timestamp):
            The timestamp used to identify the time when
            the source instance is deleted. If this instance
            is deleted, then you must set the timestamp.

            This field is a member of `oneof`_ ``_source_instance_deletion_time``.
        location (str):
            Optional. Region of the Cloud SQL instance.
    """

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    source_instance_deletion_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        optional=True,
        message=timestamp_pb2.Timestamp,
    )
    location: str = proto.Field(
        proto.STRING,
        number=5,
    )


class SqlInstancesGetLatestRecoveryTimeResponse(proto.Message):
    r"""Instance get latest recovery time response.

    Attributes:
        kind (str):
            This is always ``sql#getLatestRecoveryTime``.
        latest_recovery_time (google.protobuf.timestamp_pb2.Timestamp):
            Timestamp, identifies the latest recovery
            time of the source instance.
        earliest_recovery_time (google.protobuf.timestamp_pb2.Timestamp):
            Timestamp, identifies the earliest recovery
            time of the source instance.
    """

    kind: str = proto.Field(
        proto.STRING,
        number=1,
    )
    latest_recovery_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    earliest_recovery_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )


class SqlInstancesExecuteSqlRequest(proto.Message):
    r"""Execute SQL statements request.

    Attributes:
        instance (str):
            Required. Database instance ID. This does not
            include the project ID.
        project (str):
            Required. Project ID of the project that
            contains the instance.
        body (google.cloud.sqladmin_v1beta4.types.ExecuteSqlPayload):
            The request body.
        location (str):
            Optional. Region of the Cloud SQL instance.
    """

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    body: "ExecuteSqlPayload" = proto.Field(
        proto.MESSAGE,
        number=100,
        message="ExecuteSqlPayload",
    )
    location: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SqlInstancesReleaseSsrsLeaseRequest(proto.Message):
    r"""Request to release a lease for SSRS.

    Attributes:
        instance (str):
            Required. The Cloud SQL instance ID. This
            doesn't include the project ID. It's composed of
            lowercase letters, numbers, and hyphens, and it
            must start with a letter. The total length must
            be 98 characters or less (Example:

            instance-id).
        project (str):
            Required. The ID of the project that contains
            the instance (Example: project-id).
        location (str):
            Optional. Region of the Cloud SQL instance.
    """

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    location: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SqlInstancesReleaseSsrsLeaseResponse(proto.Message):
    r"""The response for the release of the SSRS lease.

    Attributes:
        operation_id (str):
            The operation ID.
    """

    operation_id: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ExecuteSqlPayload(proto.Message):
    r"""The request payload used to execute SQL statements.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        user (str):
            Optional. The name of an existing database user to connect
            to the database. When ``auto_iam_authn`` is set to true,
            this field is ignored and the API caller's IAM user is used.
        sql_statement (str):
            Required. SQL statements to run on the
            database. It can be a single statement or a
            sequence of statements separated by semicolons.
        database (str):
            Optional. Name of the database on which the
            statement will be executed. For Postgres and SQL
            Server it's required, for MySQL it's optional.
        password_secret_version (str):
            Optional. The resource name of the Secret Manager secret
            holding the password for the user to log into the database.
            The secret should be created using the regional endpoint
            (for API) or from the Regional Secrets page (for UI), and
            stored in the same region as the Cloud SQL instance. The
            expected resource name format is
            ``projects/{project}/locations/{location}/secrets/{secret}/versions/{secret_version}``.
            This field is used together with the ``user`` field. The
            secret resource name will not be stored.

            This field is a member of `oneof`_ ``user_password``.
        auto_iam_authn (bool):
            Optional. When set to true, the API caller
            identity associated with the request is used for
            database authentication. The API caller must be
            an IAM user in the database.

            This field is a member of `oneof`_ ``user_password``.
        row_limit (int):
            Optional. The maximum number of rows returned
            per SQL statement.
        partial_result_mode (google.cloud.sqladmin_v1beta4.types.ExecuteSqlPayload.PartialResultMode):
            Optional. Controls how the API should respond
            when the SQL execution result is incomplete due
            to the size limit or another error. The default
            mode is to throw an error.
        application (str):
            Optional. Specifies the name of the
            application that is making the request. This
            field is used for telemetry. Only alphanumeric
            characters, dashes, and underscores are allowed.
            The maximum length is 32 characters.
    """

    class PartialResultMode(proto.Enum):
        r"""Controls how the API should respond when the SQL execution
        result exceeds 10 MB.

        Values:
            PARTIAL_RESULT_MODE_UNSPECIFIED (0):
                Unspecified mode, effectively the same as
                ``FAIL_PARTIAL_RESULT``.
            FAIL_PARTIAL_RESULT (1):
                Throw an error if the result exceeds 10 MB or
                if only a partial result can be retrieved. Don't
                return the result.
            ALLOW_PARTIAL_RESULT (2):
                Return a truncated result and set ``partial_result`` to true
                if the result exceeds 10 MB or if only a partial result can
                be retrieved due to error. Don't throw an error.
        """

        PARTIAL_RESULT_MODE_UNSPECIFIED = 0
        FAIL_PARTIAL_RESULT = 1
        ALLOW_PARTIAL_RESULT = 2

    user: str = proto.Field(
        proto.STRING,
        number=1,
    )
    sql_statement: str = proto.Field(
        proto.STRING,
        number=2,
    )
    database: str = proto.Field(
        proto.STRING,
        number=3,
    )
    password_secret_version: str = proto.Field(
        proto.STRING,
        number=5,
        oneof="user_password",
    )
    auto_iam_authn: bool = proto.Field(
        proto.BOOL,
        number=11,
        oneof="user_password",
    )
    row_limit: int = proto.Field(
        proto.INT64,
        number=10,
    )
    partial_result_mode: PartialResultMode = proto.Field(
        proto.ENUM,
        number=13,
        enum=PartialResultMode,
    )
    application: str = proto.Field(
        proto.STRING,
        number=16,
    )


class SqlInstancesExecuteSqlResponse(proto.Message):
    r"""

    Attributes:
        messages (MutableSequence[google.cloud.sqladmin_v1beta4.types.SqlInstancesExecuteSqlResponse.Message]):
            A list of notices and warnings generated during query
            execution. For PostgreSQL, this includes all notices and
            warnings. For MySQL, this includes warnings generated by the
            last executed statement. To retrieve all warnings for a
            multi-statement query, ``SHOW WARNINGS`` must be executed
            after each statement.
        metadata (google.cloud.sqladmin_v1beta4.types.Metadata):
            The additional metadata information regarding
            the execution of the SQL statements.
        results (MutableSequence[google.cloud.sqladmin_v1beta4.types.QueryResult]):
            The list of results after executing all the
            SQL statements.
        status (google.rpc.status_pb2.Status):
            Contains the error from the database if the
            SQL execution failed.
    """

    class Message(proto.Message):
        r"""Represents a notice or warning message from the database.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            message (str):
                The full message string.
                For PostgreSQL, this is a formatted string that
                may include severity, code, and the
                notice/warning message.
                For MySQL, this contains the warning message.

                This field is a member of `oneof`_ ``_message``.
            severity (str):
                The severity of the message (e.g., "NOTICE"
                for PostgreSQL, "WARNING" for MySQL).

                This field is a member of `oneof`_ ``_severity``.
        """

        message: str = proto.Field(
            proto.STRING,
            number=1,
            optional=True,
        )
        severity: str = proto.Field(
            proto.STRING,
            number=2,
            optional=True,
        )

    messages: MutableSequence[Message] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message=Message,
    )
    metadata: "Metadata" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="Metadata",
    )
    results: MutableSequence["QueryResult"] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message="QueryResult",
    )
    status: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=8,
        message=status_pb2.Status,
    )


class QueryResult(proto.Message):
    r"""QueryResult contains the result of executing a single SQL
    statement.

    Attributes:
        columns (MutableSequence[google.cloud.sqladmin_v1beta4.types.Column]):
            List of columns included in the result. This
            also includes the data type of the column.
        rows (MutableSequence[google.cloud.sqladmin_v1beta4.types.Row]):
            Rows returned by the SQL statement.
        message (str):
            Message related to the SQL execution result.
        partial_result (bool):
            Set to true if the SQL execution's result is
            truncated due to size limits or an error
            retrieving results.
        status (google.rpc.status_pb2.Status):
            If results were truncated due to an error,
            details of that error.
    """

    columns: MutableSequence["Column"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Column",
    )
    rows: MutableSequence["Row"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="Row",
    )
    message: str = proto.Field(
        proto.STRING,
        number=3,
    )
    partial_result: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    status: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=8,
        message=status_pb2.Status,
    )


class Column(proto.Message):
    r"""Contains the name and datatype of a column.

    Attributes:
        name (str):
            Name of the column.
        type_ (str):
            Datatype of the column.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    type_: str = proto.Field(
        proto.STRING,
        number=2,
    )


class Row(proto.Message):
    r"""Contains the values for a row.

    Attributes:
        values (MutableSequence[google.cloud.sqladmin_v1beta4.types.Value]):
            The values for the row.
    """

    values: MutableSequence["Value"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Value",
    )


class Value(proto.Message):
    r"""The cell value of the table.

    Attributes:
        value (str):
            The cell value represented in string format.
        null_value (bool):
            If cell value is null, then this flag will be
            set to true.
    """

    value: str = proto.Field(
        proto.STRING,
        number=1,
    )
    null_value: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class Metadata(proto.Message):
    r"""The additional metadata information regarding the execution
    of the SQL statements.

    Attributes:
        sql_statement_execution_time (google.protobuf.duration_pb2.Duration):
            The time taken to execute the SQL statements.
    """

    sql_statement_execution_time: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=1,
        message=duration_pb2.Duration,
    )


class SqlInstancesAcquireSsrsLeaseRequest(proto.Message):
    r"""Request to acquire a lease for SSRS.

    Attributes:
        instance (str):
            Required. Cloud SQL instance ID. This doesn't
            include the project ID. It's composed of
            lowercase letters, numbers, and hyphens, and it
            must start with a letter. The total length must
            be 98 characters or less (Example:

            instance-id).
        project (str):
            Required. ID of the project that contains the
            instance (Example: project-id).
        body (google.cloud.sqladmin_v1beta4.types.InstancesAcquireSsrsLeaseRequest):
            The body for request to acquire an SSRS
            lease.
        location (str):
            Optional. Region of the Cloud SQL instance.
    """

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    body: cloud_sql_resources.InstancesAcquireSsrsLeaseRequest = proto.Field(
        proto.MESSAGE,
        number=100,
        message=cloud_sql_resources.InstancesAcquireSsrsLeaseRequest,
    )
    location: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SqlInstancesPreCheckMajorVersionUpgradeRequest(proto.Message):
    r"""Request for Pre-checks for MVU

    Attributes:
        instance (str):
            Required. Cloud SQL instance ID. This does
            not include the project ID.
        project (str):
            Required. Project ID of the project that
            contains the instance.
        body (google.cloud.sqladmin_v1beta4.types.InstancesPreCheckMajorVersionUpgradeRequest):
            Required. The context for request to perform
            the pre-check major version upgrade operation.
        location (str):
            Optional. Region of the Cloud SQL instance.
    """

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    body: cloud_sql_resources.InstancesPreCheckMajorVersionUpgradeRequest = proto.Field(
        proto.MESSAGE,
        number=3,
        message=cloud_sql_resources.InstancesPreCheckMajorVersionUpgradeRequest,
    )
    location: str = proto.Field(
        proto.STRING,
        number=4,
    )


class SqlInstancesAcquireSsrsLeaseResponse(proto.Message):
    r"""Acquire SSRS lease response.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        operation_id (str):
            The unique identifier for this operation.

            This field is a member of `oneof`_ ``_operation_id``.
    """

    operation_id: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )


class SqlInstancesPointInTimeRestoreRequest(proto.Message):
    r"""Request to perform a point in time restore on a Google Cloud
    Backup and Disaster Recovery managed instance.

    Attributes:
        parent (str):
            Required. The parent resource where you
            created this instance. Format:
            projects/{project}
        context (google.cloud.sqladmin_v1beta4.types.PointInTimeRestoreContext):
            Required. The context for request to perform
            a PITR on a Google Cloud Backup and Disaster
            Recovery managed instance.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    context: cloud_sql_resources.PointInTimeRestoreContext = proto.Field(
        proto.MESSAGE,
        number=100,
        message=cloud_sql_resources.PointInTimeRestoreContext,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
