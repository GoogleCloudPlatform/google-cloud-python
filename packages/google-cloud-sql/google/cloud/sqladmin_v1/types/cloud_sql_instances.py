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
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.protobuf.wrappers_pb2 as wrappers_pb2  # type: ignore
import google.rpc.status_pb2 as status_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.sqladmin_v1.types import cloud_sql_resources

__protobuf__ = proto.module(
    package="google.cloud.sql.v1",
    manifest={
        "ExternalSyncParallelLevel",
        "SqlInstanceType",
        "SqlSuspensionReason",
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
        "SqlInstancesPerformDiskShrinkRequest",
        "SqlInstancesUpdateRequest",
        "SqlInstancesRescheduleMaintenanceRequest",
        "SqlInstancesReencryptRequest",
        "InstancesReencryptRequest",
        "BackupReencryptionConfig",
        "ExternalSyncSelectedObject",
        "SqlInstancesGetDiskShrinkConfigRequest",
        "SqlInstancesVerifyExternalSyncSettingsRequest",
        "SqlInstancesStartExternalSyncRequest",
        "SqlInstancesResetReplicaSizeRequest",
        "SqlInstancesCreateEphemeralCertRequest",
        "InstancesCloneRequest",
        "InstancesDemoteMasterRequest",
        "InstancesDemoteRequest",
        "InstancesExportRequest",
        "InstancesFailoverRequest",
        "SslCertsCreateEphemeralRequest",
        "InstancesImportRequest",
        "InstancesPreCheckMajorVersionUpgradeRequest",
        "InstancesListResponse",
        "InstancesListServerCasResponse",
        "InstancesListServerCertificatesResponse",
        "InstancesListEntraIdCertificatesResponse",
        "InstancesRestoreBackupRequest",
        "InstancesRotateServerCaRequest",
        "InstancesRotateServerCertificateRequest",
        "InstancesRotateEntraIdCertificateRequest",
        "InstancesTruncateLogRequest",
        "InstancesAcquireSsrsLeaseRequest",
        "SqlInstancesPreCheckMajorVersionUpgradeRequest",
        "SqlInstancesVerifyExternalSyncSettingsResponse",
        "SqlInstancesGetDiskShrinkConfigResponse",
        "SqlInstancesGetLatestRecoveryTimeRequest",
        "SqlInstancesGetLatestRecoveryTimeResponse",
        "CloneContext",
        "PointInTimeRestoreContext",
        "BinLogCoordinates",
        "DatabaseInstance",
        "BlueGreenDeploymentInfo",
        "GeminiInstanceConfig",
        "ReplicationCluster",
        "AvailableDatabaseVersion",
        "SqlInstancesRescheduleMaintenanceRequestBody",
        "DemoteMasterContext",
        "DemoteContext",
        "FailoverContext",
        "RestoreBackupContext",
        "RotateServerCaContext",
        "RotateServerCertificateContext",
        "RotateEntraIdCertificateContext",
        "TruncateLogContext",
        "SqlExternalSyncSettingError",
        "SelectedObjects",
        "OnPremisesConfiguration",
        "ReplicaConfiguration",
        "SqlInstancesExecuteSqlRequest",
        "ExecuteSqlPayload",
        "SqlInstancesExecuteSqlResponse",
        "QueryResult",
        "Column",
        "Row",
        "Value",
        "Metadata",
        "SqlInstancesAcquireSsrsLeaseRequest",
        "SqlInstancesAcquireSsrsLeaseResponse",
        "SqlInstancesReleaseSsrsLeaseRequest",
        "SqlInstancesReleaseSsrsLeaseResponse",
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


class SqlInstanceType(proto.Enum):
    r"""

    Values:
        SQL_INSTANCE_TYPE_UNSPECIFIED (0):
            This is an unknown Cloud SQL instance type.
        CLOUD_SQL_INSTANCE (1):
            A regular Cloud SQL instance that is not
            replicating from a primary instance.
        ON_PREMISES_INSTANCE (2):
            An instance running on the customer's
            premises that is not managed by Cloud SQL.
        READ_REPLICA_INSTANCE (3):
            A Cloud SQL instance acting as a
            read-replica.
        READ_POOL_INSTANCE (5):
            A Cloud SQL read pool.
        GREEN_INSTANCE (7):
            A Cloud SQL instance acting as a Blue-Green
            deployment target primary. (MySQL only)
    """

    SQL_INSTANCE_TYPE_UNSPECIFIED = 0
    CLOUD_SQL_INSTANCE = 1
    ON_PREMISES_INSTANCE = 2
    READ_REPLICA_INSTANCE = 3
    READ_POOL_INSTANCE = 5
    GREEN_INSTANCE = 7


class SqlSuspensionReason(proto.Enum):
    r"""The suspension reason of the database instance if the state
    is SUSPENDED.

    Values:
        SQL_SUSPENSION_REASON_UNSPECIFIED (0):
            This is an unknown suspension reason.
        BILLING_ISSUE (2):
            The instance is suspended due to billing
            issues (for example:, account issue)
        LEGAL_ISSUE (3):
            The instance is suspended due to illegal
            content (for example:, child pornography,
            copyrighted material, etc.).
        OPERATIONAL_ISSUE (4):
            The instance is causing operational issues
            (for example:, causing the database to crash).
        KMS_KEY_ISSUE (5):
            The KMS key used by the instance is either
            revoked or denied access to
        PROJECT_ABUSE (8):
            The project is suspended due to abuse
            detected by Ares.
    """

    SQL_SUSPENSION_REASON_UNSPECIFIED = 0
    BILLING_ISSUE = 2
    LEGAL_ISSUE = 3
    OPERATIONAL_ISSUE = 4
    KMS_KEY_ISSUE = 5
    PROJECT_ABUSE = 8


class SqlInstancesAddServerCaRequest(proto.Message):
    r"""Instance add server CA request.

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
    r"""Instance add server certificate request.

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


class SqlInstancesAddEntraIdCertificateRequest(proto.Message):
    r"""Instance add Entra ID certificate request.

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
    r"""Instance clone request.

    Attributes:
        instance (str):
            Required. The ID of the Cloud SQL instance to
            be cloned (source). This does not include the
            project ID.
        project (str):
            Required. Project ID of the source Cloud SQL
            instance.
        body (google.cloud.sqladmin_v1.types.InstancesCloneRequest):

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
    body: "InstancesCloneRequest" = proto.Field(
        proto.MESSAGE,
        number=100,
        message="InstancesCloneRequest",
    )
    location: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SqlInstancesDeleteRequest(proto.Message):
    r"""Instance delete request.

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
    r"""Instance demote master request.

    Attributes:
        instance (str):
            Cloud SQL instance name.
        project (str):
            ID of the project that contains the instance.
        body (google.cloud.sqladmin_v1.types.InstancesDemoteMasterRequest):

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
    body: "InstancesDemoteMasterRequest" = proto.Field(
        proto.MESSAGE,
        number=100,
        message="InstancesDemoteMasterRequest",
    )
    location: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SqlInstancesDemoteRequest(proto.Message):
    r"""Instance demote request.

    Attributes:
        instance (str):
            Required. Cloud SQL instance name.
        project (str):
            Required. ID of the project that contains the
            instance.
        body (google.cloud.sqladmin_v1.types.InstancesDemoteRequest):
            Required. The request body.
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
    body: "InstancesDemoteRequest" = proto.Field(
        proto.MESSAGE,
        number=100,
        message="InstancesDemoteRequest",
    )
    location: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SqlInstancesExportRequest(proto.Message):
    r"""Instance export request.

    Attributes:
        instance (str):
            Cloud SQL instance ID. This does not include
            the project ID.
        project (str):
            Project ID of the project that contains the
            instance to be exported.
        body (google.cloud.sqladmin_v1.types.InstancesExportRequest):

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
    body: "InstancesExportRequest" = proto.Field(
        proto.MESSAGE,
        number=100,
        message="InstancesExportRequest",
    )
    location: str = proto.Field(
        proto.STRING,
        number=5,
    )


class SqlInstancesFailoverRequest(proto.Message):
    r"""Instance failover request.

    Attributes:
        instance (str):
            Cloud SQL instance ID. This does not include
            the project ID.
        project (str):
            ID of the project that contains the read
            replica.
        body (google.cloud.sqladmin_v1.types.InstancesFailoverRequest):

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
    body: "InstancesFailoverRequest" = proto.Field(
        proto.MESSAGE,
        number=100,
        message="InstancesFailoverRequest",
    )
    location: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SqlInstancesGetRequest(proto.Message):
    r"""Instance get request.

    Attributes:
        instance (str):
            Required. Database instance ID. This does not
            include the project ID.
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


class SqlInstancesImportRequest(proto.Message):
    r"""Instance import request.

    Attributes:
        instance (str):
            Cloud SQL instance ID. This does not include
            the project ID.
        project (str):
            Project ID of the project that contains the
            instance.
        body (google.cloud.sqladmin_v1.types.InstancesImportRequest):

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
    body: "InstancesImportRequest" = proto.Field(
        proto.MESSAGE,
        number=100,
        message="InstancesImportRequest",
    )
    location: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SqlInstancesInsertRequest(proto.Message):
    r"""Instance insert request.

    Attributes:
        project (str):
            Project ID of the project to which the newly
            created Cloud SQL instances should belong.
        body (google.cloud.sqladmin_v1.types.DatabaseInstance):

        location (str):
            Optional. Region of the Cloud SQL instance.
    """

    project: str = proto.Field(
        proto.STRING,
        number=1,
    )
    body: "DatabaseInstance" = proto.Field(
        proto.MESSAGE,
        number=100,
        message="DatabaseInstance",
    )
    location: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SqlInstancesListRequest(proto.Message):
    r"""Instance list request.

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
    r"""Instance list server CAs request.

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
    r"""Instance list server certificates request.

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
    r"""Instance list Entra ID certificates request.

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
    r"""Instance patch request.

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
        body (google.cloud.sqladmin_v1.types.DatabaseInstance):

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
    body: "DatabaseInstance" = proto.Field(
        proto.MESSAGE,
        number=100,
        message="DatabaseInstance",
    )
    location: str = proto.Field(
        proto.STRING,
        number=6,
    )


class SqlInstancesPromoteReplicaRequest(proto.Message):
    r"""Instance promote replica request.

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
    r"""Instance reset SSL config request.

    Attributes:
        instance (str):
            Cloud SQL instance ID. This does not include
            the project ID.
        project (str):
            Project ID of the project that contains the
            instance.
        mode (google.cloud.sqladmin_v1.types.SqlInstancesResetSslConfigRequest.ResetSslMode):
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
    r"""Instance restart request.

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
    r"""Instance restore backup request.

    Attributes:
        instance (str):
            Cloud SQL instance ID. This does not include
            the project ID.
        project (str):
            Project ID of the project that contains the
            instance.
        body (google.cloud.sqladmin_v1.types.InstancesRestoreBackupRequest):

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
    body: "InstancesRestoreBackupRequest" = proto.Field(
        proto.MESSAGE,
        number=100,
        message="InstancesRestoreBackupRequest",
    )
    location: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SqlInstancesRotateServerCaRequest(proto.Message):
    r"""Instance rotate server CA request.

    Attributes:
        instance (str):
            Cloud SQL instance ID. This does not include
            the project ID.
        project (str):
            Project ID of the project that contains the
            instance.
        body (google.cloud.sqladmin_v1.types.InstancesRotateServerCaRequest):

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
    body: "InstancesRotateServerCaRequest" = proto.Field(
        proto.MESSAGE,
        number=100,
        message="InstancesRotateServerCaRequest",
    )
    location: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SqlInstancesRotateServerCertificateRequest(proto.Message):
    r"""Instance rotate server certificate request.

    Attributes:
        instance (str):
            Required. Cloud SQL instance ID. This does
            not include the project ID.
        project (str):
            Required. Project ID of the project that
            contains the instance.
        body (google.cloud.sqladmin_v1.types.InstancesRotateServerCertificateRequest):
            Optional. Rotate server certificate request
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
    body: "InstancesRotateServerCertificateRequest" = proto.Field(
        proto.MESSAGE,
        number=100,
        message="InstancesRotateServerCertificateRequest",
    )
    location: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SqlInstancesRotateEntraIdCertificateRequest(proto.Message):
    r"""Instance rotate server certificate request.

    Attributes:
        instance (str):
            Required. Cloud SQL instance ID. This does
            not include the project ID.
        project (str):
            Required. Project ID of the project that
            contains the instance.
        body (google.cloud.sqladmin_v1.types.InstancesRotateEntraIdCertificateRequest):
            Optional. Rotate Entra ID certificate request
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
    body: "InstancesRotateEntraIdCertificateRequest" = proto.Field(
        proto.MESSAGE,
        number=100,
        message="InstancesRotateEntraIdCertificateRequest",
    )
    location: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SqlInstancesStartReplicaRequest(proto.Message):
    r"""Instance start replica request.

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
    r"""Instance stop replica request.

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
    r"""Instance truncate log request.

    Attributes:
        instance (str):
            Cloud SQL instance ID. This does not include
            the project ID.
        project (str):
            Project ID of the Cloud SQL project.
        body (google.cloud.sqladmin_v1.types.InstancesTruncateLogRequest):

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
    body: "InstancesTruncateLogRequest" = proto.Field(
        proto.MESSAGE,
        number=100,
        message="InstancesTruncateLogRequest",
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
        body (google.cloud.sqladmin_v1.types.PerformDiskShrinkContext):
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


class SqlInstancesUpdateRequest(proto.Message):
    r"""Instance update request.

    Attributes:
        instance (str):
            Cloud SQL instance ID. This does not include
            the project ID.
        project (str):
            Project ID of the project that contains the
            instance.
        body (google.cloud.sqladmin_v1.types.DatabaseInstance):

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
    body: "DatabaseInstance" = proto.Field(
        proto.MESSAGE,
        number=100,
        message="DatabaseInstance",
    )
    location: str = proto.Field(
        proto.STRING,
        number=4,
    )


class SqlInstancesRescheduleMaintenanceRequest(proto.Message):
    r"""Instance reschedule maintenance request.

    Attributes:
        instance (str):
            Cloud SQL instance ID. This does not include
            the project ID.
        project (str):
            ID of the project that contains the instance.
        body (google.cloud.sqladmin_v1.types.SqlInstancesRescheduleMaintenanceRequestBody):

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
    body: "SqlInstancesRescheduleMaintenanceRequestBody" = proto.Field(
        proto.MESSAGE,
        number=100,
        message="SqlInstancesRescheduleMaintenanceRequestBody",
    )
    location: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SqlInstancesReencryptRequest(proto.Message):
    r"""Instance reencrypt request.

    Attributes:
        instance (str):
            Cloud SQL instance ID. This does not include
            the project ID.
        project (str):
            ID of the project that contains the instance.
        body (google.cloud.sqladmin_v1.types.InstancesReencryptRequest):
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
        backup_reencryption_config (google.cloud.sqladmin_v1.types.BackupReencryptionConfig):
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
        backup_type (google.cloud.sqladmin_v1.types.BackupReencryptionConfig.BackupType):
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


class SqlInstancesVerifyExternalSyncSettingsRequest(proto.Message):
    r"""Instance verify external sync settings request.

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
        sync_mode (google.cloud.sqladmin_v1.types.SqlInstancesVerifyExternalSyncSettingsRequest.ExternalSyncMode):
            External sync mode
        verify_replication_only (bool):
            Optional. Flag to verify settings required by
            replication setup only
        mysql_sync_config (google.cloud.sqladmin_v1.types.MySqlSyncConfig):
            Optional. MySQL-specific settings for start
            external sync.

            This field is a member of `oneof`_ ``sync_config``.
        migration_type (google.cloud.sqladmin_v1.types.SqlInstancesVerifyExternalSyncSettingsRequest.MigrationType):
            Optional. MigrationType configures the migration to use
            physical files or logical dump files. If not set, then the
            logical dump file configuration is used. Valid values are
            ``LOGICAL`` or ``PHYSICAL``. Only applicable to MySQL.
        sync_parallel_level (google.cloud.sqladmin_v1.types.ExternalSyncParallelLevel):
            Optional. Parallel level for initial data
            sync. Only applicable for PostgreSQL.
        selected_objects (MutableSequence[google.cloud.sqladmin_v1.types.ExternalSyncSelectedObject]):
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
    r"""Instance start external sync request.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        instance (str):
            Cloud SQL instance ID. This does not include
            the project ID.
        project (str):
            ID of the project that contains the instance.
        sync_mode (google.cloud.sqladmin_v1.types.SqlInstancesVerifyExternalSyncSettingsRequest.ExternalSyncMode):
            External sync mode.
        skip_verification (bool):
            Whether to skip the verification step (VESS).
        mysql_sync_config (google.cloud.sqladmin_v1.types.MySqlSyncConfig):
            MySQL-specific settings for start external
            sync.

            This field is a member of `oneof`_ ``sync_config``.
        sync_parallel_level (google.cloud.sqladmin_v1.types.ExternalSyncParallelLevel):
            Optional. Parallel level for initial data
            sync. Currently only applicable for MySQL.
        migration_type (google.cloud.sqladmin_v1.types.SqlInstancesVerifyExternalSyncSettingsRequest.MigrationType):
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


class SqlInstancesCreateEphemeralCertRequest(proto.Message):
    r"""Instance create ephemeral certificate request.

    Attributes:
        instance (str):
            Cloud SQL instance ID. This does not include
            the project ID.
        project (str):
            Project ID of the Cloud SQL project.
        body (google.cloud.sqladmin_v1.types.SslCertsCreateEphemeralRequest):

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
    body: "SslCertsCreateEphemeralRequest" = proto.Field(
        proto.MESSAGE,
        number=100,
        message="SslCertsCreateEphemeralRequest",
    )
    location: str = proto.Field(
        proto.STRING,
        number=3,
    )


class InstancesCloneRequest(proto.Message):
    r"""Database instance clone request.

    Attributes:
        clone_context (google.cloud.sqladmin_v1.types.CloneContext):
            Required. Contains details about the clone
            operation.
    """

    clone_context: "CloneContext" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="CloneContext",
    )


class InstancesDemoteMasterRequest(proto.Message):
    r"""Database demote primary instance request.

    Attributes:
        demote_master_context (google.cloud.sqladmin_v1.types.DemoteMasterContext):
            Contains details about the demoteMaster
            operation.
    """

    demote_master_context: "DemoteMasterContext" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="DemoteMasterContext",
    )


class InstancesDemoteRequest(proto.Message):
    r"""This request is used to demote an existing standalone
    instance to be a Cloud SQL read replica for an external database
    server.

    Attributes:
        demote_context (google.cloud.sqladmin_v1.types.DemoteContext):
            Required. Contains details about the demote
            operation.
    """

    demote_context: "DemoteContext" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="DemoteContext",
    )


class InstancesExportRequest(proto.Message):
    r"""Database instance export request.

    Attributes:
        export_context (google.cloud.sqladmin_v1.types.ExportContext):
            Contains details about the export operation.
    """

    export_context: cloud_sql_resources.ExportContext = proto.Field(
        proto.MESSAGE,
        number=1,
        message=cloud_sql_resources.ExportContext,
    )


class InstancesFailoverRequest(proto.Message):
    r"""Instance failover request.

    Attributes:
        failover_context (google.cloud.sqladmin_v1.types.FailoverContext):
            Failover Context.
    """

    failover_context: "FailoverContext" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="FailoverContext",
    )


class SslCertsCreateEphemeralRequest(proto.Message):
    r"""SslCerts create ephemeral certificate request.

    Attributes:
        public_key (str):
            PEM encoded public key to include in the
            signed certificate.
        access_token (str):
            Access token to include in the signed
            certificate.
    """

    public_key: str = proto.Field(
        proto.STRING,
        number=1,
    )
    access_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class InstancesImportRequest(proto.Message):
    r"""Database instance import request.

    Attributes:
        import_context (google.cloud.sqladmin_v1.types.ImportContext):
            Contains details about the import operation.
    """

    import_context: cloud_sql_resources.ImportContext = proto.Field(
        proto.MESSAGE,
        number=1,
        message=cloud_sql_resources.ImportContext,
    )


class InstancesPreCheckMajorVersionUpgradeRequest(proto.Message):
    r"""Request for Pre-checks for MVU

    Attributes:
        pre_check_major_version_upgrade_context (google.cloud.sqladmin_v1.types.PreCheckMajorVersionUpgradeContext):
            Required. Contains details about the
            pre-check major version upgrade operation.
    """

    pre_check_major_version_upgrade_context: cloud_sql_resources.PreCheckMajorVersionUpgradeContext = proto.Field(
        proto.MESSAGE,
        number=1,
        message=cloud_sql_resources.PreCheckMajorVersionUpgradeContext,
    )


class InstancesListResponse(proto.Message):
    r"""Database instances list response.

    Attributes:
        kind (str):
            This is always ``sql#instancesList``.
        warnings (MutableSequence[google.cloud.sqladmin_v1.types.ApiWarning]):
            List of warnings that occurred while handling
            the request.
        items (MutableSequence[google.cloud.sqladmin_v1.types.DatabaseInstance]):
            List of database instance resources.
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
    warnings: MutableSequence[cloud_sql_resources.ApiWarning] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=cloud_sql_resources.ApiWarning,
    )
    items: MutableSequence["DatabaseInstance"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="DatabaseInstance",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )


class InstancesListServerCasResponse(proto.Message):
    r"""Instances ListServerCas response.

    Attributes:
        certs (MutableSequence[google.cloud.sqladmin_v1.types.SslCert]):
            List of server CA certificates for the
            instance.
        active_version (str):

        kind (str):
            This is always ``sql#instancesListServerCas``.
    """

    certs: MutableSequence[cloud_sql_resources.SslCert] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=cloud_sql_resources.SslCert,
    )
    active_version: str = proto.Field(
        proto.STRING,
        number=2,
    )
    kind: str = proto.Field(
        proto.STRING,
        number=3,
    )


class InstancesListServerCertificatesResponse(proto.Message):
    r"""Instances ListServerCertificates response.

    Attributes:
        ca_certs (MutableSequence[google.cloud.sqladmin_v1.types.SslCert]):
            List of server CA certificates for the
            instance.
        server_certs (MutableSequence[google.cloud.sqladmin_v1.types.SslCert]):
            List of server certificates for the instance, signed by the
            corresponding CA from the ``ca_certs`` list.
        active_version (str):
            The ``sha1_fingerprint`` of the active certificate from
            ``server_certs``.
        kind (str):
            This is always ``sql#instancesListServerCertificates``.
    """

    ca_certs: MutableSequence[cloud_sql_resources.SslCert] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=cloud_sql_resources.SslCert,
    )
    server_certs: MutableSequence[cloud_sql_resources.SslCert] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=cloud_sql_resources.SslCert,
    )
    active_version: str = proto.Field(
        proto.STRING,
        number=3,
    )
    kind: str = proto.Field(
        proto.STRING,
        number=4,
    )


class InstancesListEntraIdCertificatesResponse(proto.Message):
    r"""Instances ListEntraIdCertificates response.

    Attributes:
        certs (MutableSequence[google.cloud.sqladmin_v1.types.SslCert]):
            List of Entra ID certificates for the
            instance.
        active_version (str):
            The ``sha1_fingerprint`` of the active certificate from
            ``certs``.
        kind (str):
            This is always ``sql#instancesListEntraIdCertificates``.
    """

    certs: MutableSequence[cloud_sql_resources.SslCert] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=cloud_sql_resources.SslCert,
    )
    active_version: str = proto.Field(
        proto.STRING,
        number=2,
    )
    kind: str = proto.Field(
        proto.STRING,
        number=3,
    )


class InstancesRestoreBackupRequest(proto.Message):
    r"""Database instance restore backup request.

    Attributes:
        restore_backup_context (google.cloud.sqladmin_v1.types.RestoreBackupContext):
            Parameters required to perform the restore
            backup operation.
        backup (str):
            The name of the backup that's used to restore a Cloud SQL
            instance: Format:
            projects/{project-id}/backups/{backup-uid}. Only one of
            restore_backup_context, backup, backupdr_backup can be
            passed to the input.
        backupdr_backup (str):
            The name of the backup that's used to restore a Cloud SQL
            instance: Format:
            "projects/{project-id}/locations/{location}/backupVaults/{backupvault}/dataSources/{datasource}/backups/{backup-uid}".
            Only one of restore_backup_context, backup, backupdr_backup
            can be passed to the input.
        restore_instance_settings (google.cloud.sqladmin_v1.types.DatabaseInstance):
            Optional. By using this parameter, Cloud SQL
            overrides any instance settings stored in the
            backup you are restoring from. You can't change
            the instance's major database version and you
            can only increase the disk size. You can use
            this field to restore new instances only. This
            field is not applicable for restore to existing
            instances.
        restore_instance_clear_overrides_field_names (MutableSequence[str]):
            Optional. This field has the same purpose as
            restore_instance_settings, changes any instance settings
            stored in the backup you are restoring from. With the
            difference that these fields are cleared in the settings.
        ignore_maintenance_version (bool):
            Optional. If true, the restore operation
            proceeds even if the target instance's
            maintenance version is older than the source
            instance's maintenance version.
    """

    restore_backup_context: "RestoreBackupContext" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="RestoreBackupContext",
    )
    backup: str = proto.Field(
        proto.STRING,
        number=2,
    )
    backupdr_backup: str = proto.Field(
        proto.STRING,
        number=4,
    )
    restore_instance_settings: "DatabaseInstance" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="DatabaseInstance",
    )
    restore_instance_clear_overrides_field_names: MutableSequence[str] = (
        proto.RepeatedField(
            proto.STRING,
            number=5,
        )
    )
    ignore_maintenance_version: bool = proto.Field(
        proto.BOOL,
        number=6,
    )


class InstancesRotateServerCaRequest(proto.Message):
    r"""Rotate server CA request.

    Attributes:
        rotate_server_ca_context (google.cloud.sqladmin_v1.types.RotateServerCaContext):
            Contains details about the rotate server CA
            operation.
    """

    rotate_server_ca_context: "RotateServerCaContext" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="RotateServerCaContext",
    )


class InstancesRotateServerCertificateRequest(proto.Message):
    r"""Rotate server certificate request.

    Attributes:
        rotate_server_certificate_context (google.cloud.sqladmin_v1.types.RotateServerCertificateContext):
            Optional. Contains details about the rotate
            server certificate operation.
    """

    rotate_server_certificate_context: "RotateServerCertificateContext" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="RotateServerCertificateContext",
    )


class InstancesRotateEntraIdCertificateRequest(proto.Message):
    r"""Rotate Entra ID certificate request.

    Attributes:
        rotate_entra_id_certificate_context (google.cloud.sqladmin_v1.types.RotateEntraIdCertificateContext):
            Optional. Contains details about the rotate
            server certificate operation.
    """

    rotate_entra_id_certificate_context: "RotateEntraIdCertificateContext" = (
        proto.Field(
            proto.MESSAGE,
            number=1,
            message="RotateEntraIdCertificateContext",
        )
    )


class InstancesTruncateLogRequest(proto.Message):
    r"""Instance truncate log request.

    Attributes:
        truncate_log_context (google.cloud.sqladmin_v1.types.TruncateLogContext):
            Contains details about the truncate log
            operation.
    """

    truncate_log_context: "TruncateLogContext" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="TruncateLogContext",
    )


class InstancesAcquireSsrsLeaseRequest(proto.Message):
    r"""Request to acquire a lease for SSRS.

    Attributes:
        acquire_ssrs_lease_context (google.cloud.sqladmin_v1.types.AcquireSsrsLeaseContext):
            Contains details about the acquire SSRS lease
            operation.
    """

    acquire_ssrs_lease_context: cloud_sql_resources.AcquireSsrsLeaseContext = (
        proto.Field(
            proto.MESSAGE,
            number=1,
            message=cloud_sql_resources.AcquireSsrsLeaseContext,
        )
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
        body (google.cloud.sqladmin_v1.types.InstancesPreCheckMajorVersionUpgradeRequest):
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
    body: "InstancesPreCheckMajorVersionUpgradeRequest" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="InstancesPreCheckMajorVersionUpgradeRequest",
    )
    location: str = proto.Field(
        proto.STRING,
        number=4,
    )


class SqlInstancesVerifyExternalSyncSettingsResponse(proto.Message):
    r"""Instance verify external sync settings response.

    Attributes:
        kind (str):
            This is always ``sql#migrationSettingErrorList``.
        errors (MutableSequence[google.cloud.sqladmin_v1.types.SqlExternalSyncSettingError]):
            List of migration violations.
        warnings (MutableSequence[google.cloud.sqladmin_v1.types.SqlExternalSyncSettingError]):
            List of migration warnings.
    """

    kind: str = proto.Field(
        proto.STRING,
        number=1,
    )
    errors: MutableSequence["SqlExternalSyncSettingError"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="SqlExternalSyncSettingError",
    )
    warnings: MutableSequence["SqlExternalSyncSettingError"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="SqlExternalSyncSettingError",
    )


class SqlInstancesGetDiskShrinkConfigResponse(proto.Message):
    r"""Instance get disk shrink config response.

    Attributes:
        kind (str):
            This is always ``sql#getDiskShrinkConfig``.
        minimal_target_size_gb (int):
            The minimum size to which a disk can be
            shrunk in GigaBytes.
        message (str):
            Additional message to customers.
    """

    kind: str = proto.Field(
        proto.STRING,
        number=1,
    )
    minimal_target_size_gb: int = proto.Field(
        proto.INT64,
        number=2,
    )
    message: str = proto.Field(
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


class CloneContext(proto.Message):
    r"""Database instance clone context.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        kind (str):
            This is always ``sql#cloneContext``.
        pitr_timestamp_ms (int):
            Reserved for future use.
        destination_instance_name (str):
            Required. Name of the Cloud SQL instance to
            be created as a clone.
        bin_log_coordinates (google.cloud.sqladmin_v1.types.BinLogCoordinates):
            Binary log coordinates, if specified,
            identify the position up to which the source
            instance is cloned. If not specified, the source
            instance is cloned up to the most recent binary
            log coordinates.
        point_in_time (google.protobuf.timestamp_pb2.Timestamp):
            Timestamp, if specified, identifies the time
            to which the source instance is cloned.
        allocated_ip_range (str):
            The name of the allocated ip range for the private ip Cloud
            SQL instance. For example:
            "google-managed-services-default". If set, the cloned
            instance ip will be created in the allocated range. The
            range name must comply with `RFC
            1035 <https://tools.ietf.org/html/rfc1035>`__. Specifically,
            the name must be 1-63 characters long and match the regular
            expression `a-z <[-a-z0-9]*[a-z0-9]>`__?. Reserved for
            future use.
        database_names (MutableSequence[str]):
            (SQL Server only) Clone only the specified
            databases from the source instance. Clone all
            databases if empty.
        preferred_zone (str):
            Optional. Copy clone and point-in-time
            recovery clone of an instance to the specified
            zone. If no zone is specified, clone to the same
            primary zone as the source instance. This field
            applies to all DB types.

            This field is a member of `oneof`_ ``_preferred_zone``.
        preferred_secondary_zone (str):
            Optional. Copy clone and point-in-time recovery clone of a
            regional instance in the specified zones. If not specified,
            clone to the same secondary zone as the source instance.
            This value cannot be the same as the preferred_zone field.
            This field applies to all DB types.

            This field is a member of `oneof`_ ``_preferred_secondary_zone``.
        source_instance_deletion_time (google.protobuf.timestamp_pb2.Timestamp):
            The timestamp used to identify the time when
            the source instance is deleted. If this instance
            is deleted, then you must set the timestamp.

            This field is a member of `oneof`_ ``_source_instance_deletion_time``.
        destination_project (str):
            Optional. The project ID of the destination
            project where the cloned instance will be
            created. To perform a cross-project clone, this
            field is required. If not specified, the clone
            is created in the same project as the source
            instance.

            This field is a member of `oneof`_ ``_destination_project``.
        destination_network (str):
            Optional. The fully qualified URI of the VPC network to
            which the cloned instance will be connected via private
            services access for private IP. For
            example:``projects/my-network-project/global/networks/my-network``.
            This field is only required for cross-project cloning.

            This field is a member of `oneof`_ ``_destination_network``.
    """

    kind: str = proto.Field(
        proto.STRING,
        number=1,
    )
    pitr_timestamp_ms: int = proto.Field(
        proto.INT64,
        number=2,
    )
    destination_instance_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    bin_log_coordinates: "BinLogCoordinates" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="BinLogCoordinates",
    )
    point_in_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    allocated_ip_range: str = proto.Field(
        proto.STRING,
        number=6,
    )
    database_names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=9,
    )
    preferred_zone: str = proto.Field(
        proto.STRING,
        number=10,
        optional=True,
    )
    preferred_secondary_zone: str = proto.Field(
        proto.STRING,
        number=11,
        optional=True,
    )
    source_instance_deletion_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=12,
        optional=True,
        message=timestamp_pb2.Timestamp,
    )
    destination_project: str = proto.Field(
        proto.STRING,
        number=13,
        optional=True,
    )
    destination_network: str = proto.Field(
        proto.STRING,
        number=14,
        optional=True,
    )


class PointInTimeRestoreContext(proto.Message):
    r"""The context to perform a point-in-time recovery of an
    instance managed by Backup and Disaster Recovery (DR) Service.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        datasource (str):
            The Backup and Disaster Recovery (DR) Service
            Datasource URI. Format:

            projects/{project}/locations/{region}/backupVaults/{backupvault}/dataSources/{datasource}.

            This field is a member of `oneof`_ ``_datasource``.
        point_in_time (google.protobuf.timestamp_pb2.Timestamp):
            Required. The date and time to which you want
            to restore the instance.
        target_instance (str):
            Target instance name.

            This field is a member of `oneof`_ ``_target_instance``.
        private_network (str):
            Optional. The resource link for the VPC network from which
            the Cloud SQL instance is accessible for private IP. For
            example, ``/projects/myProject/global/networks/default``.

            This field is a member of `oneof`_ ``_private_network``.
        allocated_ip_range (str):
            Optional. The name of the allocated IP range for the
            internal IP Cloud SQL instance. For example:
            "google-managed-services-default". If you set this, then
            Cloud SQL creates the IP address for the cloned instance in
            the allocated range. This range must comply with `RFC
            1035 <https://tools.ietf.org/html/rfc1035>`__ standards.
            Specifically, the name must be 1-63 characters long and
            match the regular expression `a-z <[-a-z0-9]*[a-z0-9]>`__?.
            Reserved for future use.

            This field is a member of `oneof`_ ``_allocated_ip_range``.
        preferred_zone (str):
            Optional. Point-in-time recovery of an
            instance to the specified zone. If no zone is
            specified, then clone to the same primary zone
            as the source instance.

            This field is a member of `oneof`_ ``_preferred_zone``.
        preferred_secondary_zone (str):
            Optional. Point-in-time recovery of a regional instance in
            the specified zones. If not specified, clone to the same
            secondary zone as the source instance. This value cannot be
            the same as the preferred_zone field.

            This field is a member of `oneof`_ ``_preferred_secondary_zone``.
        target_instance_settings (google.cloud.sqladmin_v1.types.DatabaseInstance):
            Optional. Specifies the instance settings
            that will be overridden from the source
            instance. This field is only applicable for
            cross project PITRs.
        target_instance_clear_settings_field_names (MutableSequence[str]):
            Optional. Specifies the instance settings
            that will be cleared from the source instance.
            This field is only applicable for cross project
            PITRs.
        region (str):
            Optional. The region of the target instance
            where the datasource will be restored. For
            example: "us-central1".

            This field is a member of `oneof`_ ``_region``.
    """

    datasource: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    point_in_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    target_instance: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )
    private_network: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )
    allocated_ip_range: str = proto.Field(
        proto.STRING,
        number=5,
        optional=True,
    )
    preferred_zone: str = proto.Field(
        proto.STRING,
        number=6,
        optional=True,
    )
    preferred_secondary_zone: str = proto.Field(
        proto.STRING,
        number=9,
        optional=True,
    )
    target_instance_settings: "DatabaseInstance" = proto.Field(
        proto.MESSAGE,
        number=11,
        message="DatabaseInstance",
    )
    target_instance_clear_settings_field_names: MutableSequence[str] = (
        proto.RepeatedField(
            proto.STRING,
            number=12,
        )
    )
    region: str = proto.Field(
        proto.STRING,
        number=13,
        optional=True,
    )


class BinLogCoordinates(proto.Message):
    r"""Binary log coordinates.

    Attributes:
        bin_log_file_name (str):
            Name of the binary log file for a Cloud SQL
            instance.
        bin_log_position (int):
            Position (offset) within the binary log file.
        kind (str):
            This is always ``sql#binLogCoordinates``.
    """

    bin_log_file_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    bin_log_position: int = proto.Field(
        proto.INT64,
        number=2,
    )
    kind: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DatabaseInstance(proto.Message):
    r"""A Cloud SQL instance resource.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        kind (str):
            This is always ``sql#instance``.
        state (google.cloud.sqladmin_v1.types.DatabaseInstance.SqlInstanceState):
            The current serving state of the Cloud SQL
            instance.
        database_version (google.cloud.sqladmin_v1.types.SqlDatabaseVersion):
            The database engine type and version. The
            ``databaseVersion`` field cannot be changed after instance
            creation.
        settings (google.cloud.sqladmin_v1.types.Settings):
            The user settings.
        etag (str):
            This field is deprecated and will be removed from a future
            version of the API. Use the ``settings.settingsVersion``
            field instead.
        failover_replica (google.cloud.sqladmin_v1.types.DatabaseInstance.SqlFailoverReplica):
            The name and status of the failover replica.
        master_instance_name (str):
            The name of the instance which will act as
            primary in the replication setup.
        replica_names (MutableSequence[str]):
            The replicas of the instance.
        max_disk_size (google.protobuf.wrappers_pb2.Int64Value):
            The maximum disk size of the instance in
            bytes.
        current_disk_size (google.protobuf.wrappers_pb2.Int64Value):
            The current disk usage of the instance in bytes. This
            property has been deprecated. Use the
            "cloudsql.googleapis.com/database/disk/bytes_used" metric in
            Cloud Monitoring API instead. Please see `this
            announcement <https://groups.google.com/d/msg/google-cloud-sql-announce/I_7-F9EBhT0/BtvFtdFeAgAJ>`__
            for details.
        ip_addresses (MutableSequence[google.cloud.sqladmin_v1.types.IpMapping]):
            The assigned IP addresses for the instance.
        server_ca_cert (google.cloud.sqladmin_v1.types.SslCert):
            SSL configuration.
        instance_type (google.cloud.sqladmin_v1.types.SqlInstanceType):
            The instance type.
        project (str):
            The project ID of the project containing the
            Cloud SQL instance. The Google apps domain is
            prefixed if applicable.
        ipv6_address (str):
            The IPv6 address assigned to the instance.
            (Deprecated) This property was applicable only
            to First Generation instances.
        service_account_email_address (str):
            The service account email address assigned to
            the instance.\This property is read-only.
        on_premises_configuration (google.cloud.sqladmin_v1.types.OnPremisesConfiguration):
            Configuration specific to on-premises
            instances.
        replica_configuration (google.cloud.sqladmin_v1.types.ReplicaConfiguration):
            Configuration specific to failover replicas
            and read replicas.
        backend_type (google.cloud.sqladmin_v1.types.SqlBackendType):
            The backend type. ``SECOND_GEN``: Cloud SQL database
            instance. ``EXTERNAL``: A database server that is not
            managed by Google.

            This property is read-only; use the ``tier`` property in the
            ``settings`` object to determine the database type.
        self_link (str):
            The URI of this resource.
        suspension_reason (MutableSequence[google.cloud.sqladmin_v1.types.SqlSuspensionReason]):
            If the instance state is SUSPENDED, the
            reason for the suspension.
        connection_name (str):
            Connection name of the Cloud SQL instance
            used in connection strings.
        name (str):
            Name of the Cloud SQL instance. This does not
            include the project ID.
        region (str):
            The geographical region of the Cloud SQL instance.

            It can be one of the
            `regions <https://cloud.google.com/sql/docs/mysql/locations#location-r>`__
            where Cloud SQL operates:

            For example, ``asia-east1``, ``europe-west1``, and
            ``us-central1``. The default value is ``us-central1``.
        gce_zone (str):
            The Compute Engine zone that the instance is
            currently serving from. This value could be
            different from the zone that was specified when
            the instance was created if the instance has
            failed over to its secondary zone. WARNING:

            Changing this might restart the instance.
        secondary_gce_zone (str):
            The Compute Engine zone that the failover
            instance is currently serving from for a
            regional instance. This value could be different
            from the zone that was specified when the
            instance was created if the instance has failed
            over to its secondary/failover zone.
        disk_encryption_configuration (google.cloud.sqladmin_v1.types.DiskEncryptionConfiguration):
            Disk encryption configuration specific to an
            instance.
        disk_encryption_status (google.cloud.sqladmin_v1.types.DiskEncryptionStatus):
            Disk encryption status specific to an
            instance.
        root_password (str):
            Initial root password. Use only on creation.
            You must set root passwords before you can
            connect to PostgreSQL instances.
        scheduled_maintenance (google.cloud.sqladmin_v1.types.DatabaseInstance.SqlScheduledMaintenance):
            The start time of any upcoming scheduled
            maintenance for this instance.
        satisfies_pzs (google.protobuf.wrappers_pb2.BoolValue):
            This status indicates whether the instance
            satisfies PZS.
            The status is reserved for future use.
        database_installed_version (str):
            Output only. Stores the current database version running on
            the instance including minor version such as
            ``MYSQL_8_0_18``.
        out_of_disk_report (google.cloud.sqladmin_v1.types.DatabaseInstance.SqlOutOfDiskReport):
            This field represents the report generated by the proactive
            database wellness job for OutOfDisk issues.

            - Writers:
            - the proactive database wellness job for OOD.
            - Readers:
            - the proactive database wellness job

            This field is a member of `oneof`_ ``_out_of_disk_report``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the instance was created in `RFC
            3339 <https://tools.ietf.org/html/rfc3339>`__ format, for
            example ``2012-11-15T16:19:00.094Z``.
        available_maintenance_versions (MutableSequence[str]):
            Output only. List all maintenance versions
            applicable on the instance
        maintenance_version (str):
            The current software version on the instance.
        upgradable_database_versions (MutableSequence[google.cloud.sqladmin_v1.types.AvailableDatabaseVersion]):
            Output only. All database versions that are
            available for upgrade.
        sql_network_architecture (google.cloud.sqladmin_v1.types.DatabaseInstance.SqlNetworkArchitecture):

            This field is a member of `oneof`_ ``_sql_network_architecture``.
        psc_service_attachment_link (str):
            Output only. The link to service attachment
            of PSC instance.

            This field is a member of `oneof`_ ``_psc_service_attachment_link``.
        dns_name (str):
            Output only. The dns name of the instance.

            This field is a member of `oneof`_ ``_dns_name``.
        primary_dns_name (str):
            Output only. DEPRECATED: please use write_endpoint instead.

            This field is a member of `oneof`_ ``_primary_dns_name``.
        write_endpoint (str):
            Output only. The dns name of the primary
            instance in a replication group.

            This field is a member of `oneof`_ ``_write_endpoint``.
        replication_cluster (google.cloud.sqladmin_v1.types.ReplicationCluster):
            Optional. A primary instance and disaster
            recovery (DR) replica pair. A DR replica is a
            cross-region replica that you designate for
            failover in the event that the primary instance
            experiences regional failure.
            Applicable to MySQL and PostgreSQL.
        gemini_config (google.cloud.sqladmin_v1.types.GeminiInstanceConfig):
            Gemini instance configuration.

            This field is a member of `oneof`_ ``_gemini_config``.
        satisfies_pzi (google.protobuf.wrappers_pb2.BoolValue):
            Output only. This status indicates whether
            the instance satisfies PZI.
            The status is reserved for future use.
        switch_transaction_logs_to_cloud_storage_enabled (google.protobuf.wrappers_pb2.BoolValue):
            Input only. Whether Cloud SQL is enabled to
            switch storing point-in-time recovery log files
            from a data disk to Cloud Storage.

            This field is a member of `oneof`_ ``_switch_transaction_logs_to_cloud_storage_enabled``.
        include_replicas_for_major_version_upgrade (google.protobuf.wrappers_pb2.BoolValue):
            Input only. Determines whether an in-place
            major version upgrade of replicas happens when
            an in-place major version upgrade of a primary
            instance is initiated.

            This field is a member of `oneof`_ ``_include_replicas_for_major_version_upgrade``.
        skip_precheck (google.protobuf.wrappers_pb2.BoolValue):
            Optional. Input only. Determines whether the
            precheck step is skipped during a major version
            upgrade.

            This field is a member of `oneof`_ ``_skip_precheck``.
        tags (MutableMapping[str, str]):
            Optional. Input only. Immutable. Tag keys and tag values
            that are bound to this instance. You must represent each
            item in the map as:
            ``"<tag-key-namespaced-name>" : "<tag-value-short-name>"``.

            For example, a single resource can have the following tags:

            ::

                 "123/environment": "production",
                 "123/costCenter": "marketing",

            For more information on tag creation and management, see
            https://cloud.google.com/resource-manager/docs/tags/tags-overview.
        node_count (int):
            The number of read pool nodes in a read pool.

            This field is a member of `oneof`_ ``_node_count``.
        nodes (MutableSequence[google.cloud.sqladmin_v1.types.DatabaseInstance.PoolNodeConfig]):
            Output only. Entries containing information
            about each read pool node of the read pool.
        dns_names (MutableSequence[google.cloud.sqladmin_v1.types.DnsNameMapping]):
            Output only. The list of DNS names used by
            this instance.
        deployment_info (google.cloud.sqladmin_v1.types.BlueGreenDeploymentInfo):
            Output only. Deployment info for the
            instance. This is set if the instance is
            currently part of any blue-green setup.

            This field is a member of `oneof`_ ``_deployment_info``.
        database_center_integration_enabled (google.protobuf.wrappers_pb2.BoolValue):
            Optional. If true, instance metadata is sent
            to the Database Center. If false, instance
            metadata is not sent to the Database Center.
        database_center_integration (google.cloud.sqladmin_v1.types.DatabaseInstance.DatabaseCenterIntegration):
            Optional. State of the Database Center
            integration for this instance. When unspecified,
            Database Center integration is enabled by
            default.

            This field is a member of `oneof`_ ``_database_center_integration``.
    """

    class SqlInstanceState(proto.Enum):
        r"""The current serving state of the database instance.

        Values:
            SQL_INSTANCE_STATE_UNSPECIFIED (0):
                The state of the instance is unknown.
            RUNNABLE (1):
                The instance is running, or has been stopped
                by owner.
            SUSPENDED (2):
                The instance is not available, for example
                due to problems with billing.
            PENDING_DELETE (3):
                The instance is being deleted.
            PENDING_CREATE (4):
                The instance is being created.
            MAINTENANCE (5):
                The instance is down for maintenance.
            FAILED (6):
                The creation of the instance failed or a
                fatal error occurred during maintenance.
            ONLINE_MAINTENANCE (7):
                Deprecated
            REPAIRING (8):
                (Applicable to read pool nodes only.) The
                read pool node needs to be repaired. The
                database might be unavailable.
        """

        SQL_INSTANCE_STATE_UNSPECIFIED = 0
        RUNNABLE = 1
        SUSPENDED = 2
        PENDING_DELETE = 3
        PENDING_CREATE = 4
        MAINTENANCE = 5
        FAILED = 6
        ONLINE_MAINTENANCE = 7
        REPAIRING = 8

    class SqlNetworkArchitecture(proto.Enum):
        r"""The SQL network architecture for the instance.

        Values:
            SQL_NETWORK_ARCHITECTURE_UNSPECIFIED (0):
                No description available.
            NEW_NETWORK_ARCHITECTURE (1):
                The instance uses the new network
                architecture.
            OLD_NETWORK_ARCHITECTURE (2):
                The instance uses the old network
                architecture.
        """

        SQL_NETWORK_ARCHITECTURE_UNSPECIFIED = 0
        NEW_NETWORK_ARCHITECTURE = 1
        OLD_NETWORK_ARCHITECTURE = 2

    class DatabaseCenterIntegration(proto.Enum):
        r"""State of the integration with Database Center.

        Values:
            DATABASE_CENTER_INTEGRATION_UNSPECIFIED (0):
                Default value. The integration state is
                unspecified. When unspecified, Database Center
                integration is enabled by default.
            ENABLED (1):
                Database Center integration is enabled.
            DISABLED (2):
                Database Center integration is disabled.
        """

        DATABASE_CENTER_INTEGRATION_UNSPECIFIED = 0
        ENABLED = 1
        DISABLED = 2

    class SqlFailoverReplica(proto.Message):
        r"""

        Attributes:
            name (str):
                The name of the failover replica. If
                specified at instance creation, a failover
                replica is created for the instance. The name
                doesn't include the project ID.
            available (google.protobuf.wrappers_pb2.BoolValue):
                The availability status of the failover
                replica. A false status indicates that the
                failover replica is out of sync. The primary
                instance can only failover to the failover
                replica when the status is true.
        """

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        available: wrappers_pb2.BoolValue = proto.Field(
            proto.MESSAGE,
            number=2,
            message=wrappers_pb2.BoolValue,
        )

    class SqlScheduledMaintenance(proto.Message):
        r"""Any scheduled maintenance for this instance.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            start_time (google.protobuf.timestamp_pb2.Timestamp):
                The start time of any upcoming scheduled
                maintenance for this instance.
            can_defer (bool):

            can_reschedule (bool):
                If the scheduled maintenance can be
                rescheduled.
            schedule_deadline_time (google.protobuf.timestamp_pb2.Timestamp):
                Maintenance cannot be rescheduled to start
                beyond this deadline.

                This field is a member of `oneof`_ ``_schedule_deadline_time``.
        """

        start_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=1,
            message=timestamp_pb2.Timestamp,
        )
        can_defer: bool = proto.Field(
            proto.BOOL,
            number=2,
        )
        can_reschedule: bool = proto.Field(
            proto.BOOL,
            number=3,
        )
        schedule_deadline_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=4,
            optional=True,
            message=timestamp_pb2.Timestamp,
        )

    class SqlOutOfDiskReport(proto.Message):
        r"""This message wraps up the information written by out-of-disk
        detection job.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            sql_out_of_disk_state (google.cloud.sqladmin_v1.types.DatabaseInstance.SqlOutOfDiskReport.SqlOutOfDiskState):
                This field represents the state generated by the proactive
                database wellness job for OutOfDisk issues.

                - Writers:
                - the proactive database wellness job for OOD.
                - Readers:
                - the proactive database wellness job

                This field is a member of `oneof`_ ``_sql_out_of_disk_state``.
            sql_min_recommended_increase_size_gb (int):
                The minimum recommended increase size in GigaBytes This
                field is consumed by the frontend

                - Writers:
                - the proactive database wellness job for OOD.
                - Readers:

                This field is a member of `oneof`_ ``_sql_min_recommended_increase_size_gb``.
        """

        class SqlOutOfDiskState(proto.Enum):
            r"""This enum lists all possible states regarding out-of-disk
            issues.

            Values:
                SQL_OUT_OF_DISK_STATE_UNSPECIFIED (0):
                    Unspecified state
                NORMAL (1):
                    The instance has plenty space on data disk
                SOFT_SHUTDOWN (2):
                    Data disk is almost used up. It is shutdown
                    to prevent data corruption.
            """

            SQL_OUT_OF_DISK_STATE_UNSPECIFIED = 0
            NORMAL = 1
            SOFT_SHUTDOWN = 2

        sql_out_of_disk_state: "DatabaseInstance.SqlOutOfDiskReport.SqlOutOfDiskState" = proto.Field(
            proto.ENUM,
            number=1,
            optional=True,
            enum="DatabaseInstance.SqlOutOfDiskReport.SqlOutOfDiskState",
        )
        sql_min_recommended_increase_size_gb: int = proto.Field(
            proto.INT32,
            number=2,
            optional=True,
        )

    class PoolNodeConfig(proto.Message):
        r"""Details of a single read pool node of a read pool.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            name (str):
                Output only. The name of the read pool node,
                to be used for retrieving metrics and logs.

                This field is a member of `oneof`_ ``_name``.
            gce_zone (str):
                Output only. The zone of the read pool node.

                This field is a member of `oneof`_ ``_gce_zone``.
            ip_addresses (MutableSequence[google.cloud.sqladmin_v1.types.IpMapping]):
                Output only. Mappings containing IP addresses
                that can be used to connect to the read pool
                node.
            dns_name (str):
                Output only. The DNS name of the read pool
                node.

                This field is a member of `oneof`_ ``_dns_name``.
            state (google.cloud.sqladmin_v1.types.DatabaseInstance.SqlInstanceState):
                Output only. The current state of the read
                pool node.

                This field is a member of `oneof`_ ``_state``.
            dns_names (MutableSequence[google.cloud.sqladmin_v1.types.DnsNameMapping]):
                Output only. The list of DNS names used by
                this read pool node.
            psc_service_attachment_link (str):
                Output only. The Private Service Connect
                (PSC) service attachment of the read pool node.

                This field is a member of `oneof`_ ``_psc_service_attachment_link``.
            psc_auto_connections (MutableSequence[google.cloud.sqladmin_v1.types.PscAutoConnectionConfig]):
                Output only. The list of settings for
                requested automatically-setup Private Service
                Connect (PSC) consumer endpoints that can be
                used to connect to this read pool node.
        """

        name: str = proto.Field(
            proto.STRING,
            number=1,
            optional=True,
        )
        gce_zone: str = proto.Field(
            proto.STRING,
            number=2,
            optional=True,
        )
        ip_addresses: MutableSequence[cloud_sql_resources.IpMapping] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=3,
                message=cloud_sql_resources.IpMapping,
            )
        )
        dns_name: str = proto.Field(
            proto.STRING,
            number=4,
            optional=True,
        )
        state: "DatabaseInstance.SqlInstanceState" = proto.Field(
            proto.ENUM,
            number=5,
            optional=True,
            enum="DatabaseInstance.SqlInstanceState",
        )
        dns_names: MutableSequence[cloud_sql_resources.DnsNameMapping] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=6,
                message=cloud_sql_resources.DnsNameMapping,
            )
        )
        psc_service_attachment_link: str = proto.Field(
            proto.STRING,
            number=7,
            optional=True,
        )
        psc_auto_connections: MutableSequence[
            cloud_sql_resources.PscAutoConnectionConfig
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=8,
            message=cloud_sql_resources.PscAutoConnectionConfig,
        )

    kind: str = proto.Field(
        proto.STRING,
        number=1,
    )
    state: SqlInstanceState = proto.Field(
        proto.ENUM,
        number=2,
        enum=SqlInstanceState,
    )
    database_version: cloud_sql_resources.SqlDatabaseVersion = proto.Field(
        proto.ENUM,
        number=3,
        enum=cloud_sql_resources.SqlDatabaseVersion,
    )
    settings: cloud_sql_resources.Settings = proto.Field(
        proto.MESSAGE,
        number=4,
        message=cloud_sql_resources.Settings,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=5,
    )
    failover_replica: SqlFailoverReplica = proto.Field(
        proto.MESSAGE,
        number=6,
        message=SqlFailoverReplica,
    )
    master_instance_name: str = proto.Field(
        proto.STRING,
        number=7,
    )
    replica_names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=8,
    )
    max_disk_size: wrappers_pb2.Int64Value = proto.Field(
        proto.MESSAGE,
        number=9,
        message=wrappers_pb2.Int64Value,
    )
    current_disk_size: wrappers_pb2.Int64Value = proto.Field(
        proto.MESSAGE,
        number=10,
        message=wrappers_pb2.Int64Value,
    )
    ip_addresses: MutableSequence[cloud_sql_resources.IpMapping] = proto.RepeatedField(
        proto.MESSAGE,
        number=11,
        message=cloud_sql_resources.IpMapping,
    )
    server_ca_cert: cloud_sql_resources.SslCert = proto.Field(
        proto.MESSAGE,
        number=12,
        message=cloud_sql_resources.SslCert,
    )
    instance_type: "SqlInstanceType" = proto.Field(
        proto.ENUM,
        number=13,
        enum="SqlInstanceType",
    )
    project: str = proto.Field(
        proto.STRING,
        number=14,
    )
    ipv6_address: str = proto.Field(
        proto.STRING,
        number=15,
    )
    service_account_email_address: str = proto.Field(
        proto.STRING,
        number=16,
    )
    on_premises_configuration: "OnPremisesConfiguration" = proto.Field(
        proto.MESSAGE,
        number=17,
        message="OnPremisesConfiguration",
    )
    replica_configuration: "ReplicaConfiguration" = proto.Field(
        proto.MESSAGE,
        number=18,
        message="ReplicaConfiguration",
    )
    backend_type: cloud_sql_resources.SqlBackendType = proto.Field(
        proto.ENUM,
        number=19,
        enum=cloud_sql_resources.SqlBackendType,
    )
    self_link: str = proto.Field(
        proto.STRING,
        number=20,
    )
    suspension_reason: MutableSequence["SqlSuspensionReason"] = proto.RepeatedField(
        proto.ENUM,
        number=21,
        enum="SqlSuspensionReason",
    )
    connection_name: str = proto.Field(
        proto.STRING,
        number=22,
    )
    name: str = proto.Field(
        proto.STRING,
        number=23,
    )
    region: str = proto.Field(
        proto.STRING,
        number=24,
    )
    gce_zone: str = proto.Field(
        proto.STRING,
        number=25,
    )
    secondary_gce_zone: str = proto.Field(
        proto.STRING,
        number=34,
    )
    disk_encryption_configuration: cloud_sql_resources.DiskEncryptionConfiguration = (
        proto.Field(
            proto.MESSAGE,
            number=26,
            message=cloud_sql_resources.DiskEncryptionConfiguration,
        )
    )
    disk_encryption_status: cloud_sql_resources.DiskEncryptionStatus = proto.Field(
        proto.MESSAGE,
        number=27,
        message=cloud_sql_resources.DiskEncryptionStatus,
    )
    root_password: str = proto.Field(
        proto.STRING,
        number=29,
    )
    scheduled_maintenance: SqlScheduledMaintenance = proto.Field(
        proto.MESSAGE,
        number=30,
        message=SqlScheduledMaintenance,
    )
    satisfies_pzs: wrappers_pb2.BoolValue = proto.Field(
        proto.MESSAGE,
        number=35,
        message=wrappers_pb2.BoolValue,
    )
    database_installed_version: str = proto.Field(
        proto.STRING,
        number=40,
    )
    out_of_disk_report: SqlOutOfDiskReport = proto.Field(
        proto.MESSAGE,
        number=38,
        optional=True,
        message=SqlOutOfDiskReport,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=39,
        message=timestamp_pb2.Timestamp,
    )
    available_maintenance_versions: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=41,
    )
    maintenance_version: str = proto.Field(
        proto.STRING,
        number=42,
    )
    upgradable_database_versions: MutableSequence["AvailableDatabaseVersion"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=45,
            message="AvailableDatabaseVersion",
        )
    )
    sql_network_architecture: SqlNetworkArchitecture = proto.Field(
        proto.ENUM,
        number=47,
        optional=True,
        enum=SqlNetworkArchitecture,
    )
    psc_service_attachment_link: str = proto.Field(
        proto.STRING,
        number=48,
        optional=True,
    )
    dns_name: str = proto.Field(
        proto.STRING,
        number=49,
        optional=True,
    )
    primary_dns_name: str = proto.Field(
        proto.STRING,
        number=51,
        optional=True,
    )
    write_endpoint: str = proto.Field(
        proto.STRING,
        number=52,
        optional=True,
    )
    replication_cluster: "ReplicationCluster" = proto.Field(
        proto.MESSAGE,
        number=54,
        message="ReplicationCluster",
    )
    gemini_config: "GeminiInstanceConfig" = proto.Field(
        proto.MESSAGE,
        number=55,
        optional=True,
        message="GeminiInstanceConfig",
    )
    satisfies_pzi: wrappers_pb2.BoolValue = proto.Field(
        proto.MESSAGE,
        number=56,
        message=wrappers_pb2.BoolValue,
    )
    switch_transaction_logs_to_cloud_storage_enabled: wrappers_pb2.BoolValue = (
        proto.Field(
            proto.MESSAGE,
            number=57,
            optional=True,
            message=wrappers_pb2.BoolValue,
        )
    )
    include_replicas_for_major_version_upgrade: wrappers_pb2.BoolValue = proto.Field(
        proto.MESSAGE,
        number=59,
        optional=True,
        message=wrappers_pb2.BoolValue,
    )
    skip_precheck: wrappers_pb2.BoolValue = proto.Field(
        proto.MESSAGE,
        number=77,
        optional=True,
        message=wrappers_pb2.BoolValue,
    )
    tags: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=60,
    )
    node_count: int = proto.Field(
        proto.INT32,
        number=63,
        optional=True,
    )
    nodes: MutableSequence[PoolNodeConfig] = proto.RepeatedField(
        proto.MESSAGE,
        number=64,
        message=PoolNodeConfig,
    )
    dns_names: MutableSequence[cloud_sql_resources.DnsNameMapping] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=67,
            message=cloud_sql_resources.DnsNameMapping,
        )
    )
    deployment_info: "BlueGreenDeploymentInfo" = proto.Field(
        proto.MESSAGE,
        number=73,
        optional=True,
        message="BlueGreenDeploymentInfo",
    )
    database_center_integration_enabled: wrappers_pb2.BoolValue = proto.Field(
        proto.MESSAGE,
        number=72,
        message=wrappers_pb2.BoolValue,
    )
    database_center_integration: DatabaseCenterIntegration = proto.Field(
        proto.ENUM,
        number=76,
        optional=True,
        enum=DatabaseCenterIntegration,
    )


class BlueGreenDeploymentInfo(proto.Message):
    r"""Blue-green deployment metadata for a database instance. In a
    blue-green deployment, we maintain two environments, one of
    which is live. This message contains details about the
    blue-green deployment.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        deployment_id (str):
            Output only. The resource ID of the
            blue-green deployment.

            This field is a member of `oneof`_ ``_deployment_id``.
        source (google.cloud.sqladmin_v1.types.BlueGreenDeploymentInfo.SourceRole):
            Output only. The source instance for the
            Blue-Green deployment.

            This field is a member of `oneof`_ ``role_details``.
        target (google.cloud.sqladmin_v1.types.BlueGreenDeploymentInfo.TargetRole):
            Output only. The target instance for the
            Blue-Green deployment.

            This field is a member of `oneof`_ ``role_details``.
        state (google.cloud.sqladmin_v1.types.BlueGreenDeploymentInfo.State):
            Output only. The current state of
            blue-green-deployment for UI tags

            This field is a member of `oneof`_ ``_state``.
    """

    class State(proto.Enum):
        r"""The state of blue-green-deployment for UI tags

        Values:
            STATE_UNSPECIFIED (0):
                The state of the deployment is unknown.
            PRE_SWITCHOVER (1):
                The deployment is pre-switchover.
            POST_SWITCHOVER (2):
                The deployment is post-switchover.
        """

        STATE_UNSPECIFIED = 0
        PRE_SWITCHOVER = 1
        POST_SWITCHOVER = 2

    class SourceRole(proto.Message):
        r"""The source instance for the Blue-Green deployment.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            target_id (google.cloud.sqladmin_v1.types.InstanceReference):
                Output only. The target instance paired with
                this source instance in a blue-green deployment.

                This field is a member of `oneof`_ ``_target_id``.
        """

        target_id: cloud_sql_resources.InstanceReference = proto.Field(
            proto.MESSAGE,
            number=1,
            optional=True,
            message=cloud_sql_resources.InstanceReference,
        )

    class TargetRole(proto.Message):
        r"""The target instance for the Blue-Green deployment.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            source_id (google.cloud.sqladmin_v1.types.InstanceReference):
                Output only. The source instance paired with
                this target instance in a blue-green deployment.

                This field is a member of `oneof`_ ``_source_id``.
        """

        source_id: cloud_sql_resources.InstanceReference = proto.Field(
            proto.MESSAGE,
            number=1,
            optional=True,
            message=cloud_sql_resources.InstanceReference,
        )

    deployment_id: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    source: SourceRole = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="role_details",
        message=SourceRole,
    )
    target: TargetRole = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="role_details",
        message=TargetRole,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=4,
        optional=True,
        enum=State,
    )


class GeminiInstanceConfig(proto.Message):
    r"""Gemini instance configuration.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        entitled (bool):
            Output only. Whether Gemini is enabled.

            This field is a member of `oneof`_ ``_entitled``.
        google_vacuum_mgmt_enabled (bool):
            Output only. Whether the vacuum management is
            enabled.

            This field is a member of `oneof`_ ``_google_vacuum_mgmt_enabled``.
        oom_session_cancel_enabled (bool):
            Output only. Whether canceling the
            out-of-memory (OOM) session is enabled.

            This field is a member of `oneof`_ ``_oom_session_cancel_enabled``.
        active_query_enabled (bool):
            Output only. Whether the active query is
            enabled.

            This field is a member of `oneof`_ ``_active_query_enabled``.
        index_advisor_enabled (bool):
            Output only. Whether the index advisor is
            enabled.

            This field is a member of `oneof`_ ``_index_advisor_enabled``.
        flag_recommender_enabled (bool):
            Output only. Whether the flag recommender is
            enabled.

            This field is a member of `oneof`_ ``_flag_recommender_enabled``.
    """

    entitled: bool = proto.Field(
        proto.BOOL,
        number=1,
        optional=True,
    )
    google_vacuum_mgmt_enabled: bool = proto.Field(
        proto.BOOL,
        number=2,
        optional=True,
    )
    oom_session_cancel_enabled: bool = proto.Field(
        proto.BOOL,
        number=3,
        optional=True,
    )
    active_query_enabled: bool = proto.Field(
        proto.BOOL,
        number=4,
        optional=True,
    )
    index_advisor_enabled: bool = proto.Field(
        proto.BOOL,
        number=5,
        optional=True,
    )
    flag_recommender_enabled: bool = proto.Field(
        proto.BOOL,
        number=6,
        optional=True,
    )


class ReplicationCluster(proto.Message):
    r"""A primary instance and disaster recovery (DR) replica pair.
    A DR replica is a cross-region replica that you designate for
    failover in the event that the primary instance experiences
    regional failure. Applicable to MySQL and PostgreSQL.

    Attributes:
        psa_write_endpoint (str):
            Output only. If set, this field indicates
            this instance has a private service access (PSA)
            DNS endpoint that is pointing to the primary
            instance of the cluster. If this instance is the
            primary, then the DNS endpoint points to this
            instance. After a switchover or replica failover
            operation, this DNS endpoint points to the
            promoted instance. This is a read-only field,
            returned to the user as information. This field
            can exist even if a standalone instance doesn't
            have a DR replica yet or the DR replica is
            deleted.
        failover_dr_replica_name (str):
            Optional. If the instance is a primary
            instance, then this field identifies the
            disaster recovery (DR) replica. A DR replica is
            an optional configuration for Enterprise Plus
            edition instances. If the instance is a read
            replica, then the field is not set. Set this
            field to a replica name to designate a DR
            replica for a primary instance. Remove the
            replica name to remove the DR replica
            designation.
        dr_replica (bool):
            Output only. Read-only field that indicates
            whether the replica is a DR replica. This field
            is not set if the instance is a primary
            instance.
    """

    psa_write_endpoint: str = proto.Field(
        proto.STRING,
        number=1,
    )
    failover_dr_replica_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    dr_replica: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class AvailableDatabaseVersion(proto.Message):
    r"""An available database version. It can be a major or a minor
    version.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        major_version (str):
            The version's major version name.

            This field is a member of `oneof`_ ``_major_version``.
        name (str):
            The database version name. For MySQL 8.0,
            this string provides the database major and
            minor version.

            This field is a member of `oneof`_ ``_name``.
        display_name (str):
            The database version's display name.

            This field is a member of `oneof`_ ``_display_name``.
    """

    major_version: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )
    name: str = proto.Field(
        proto.STRING,
        number=8,
        optional=True,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=9,
        optional=True,
    )


class SqlInstancesRescheduleMaintenanceRequestBody(proto.Message):
    r"""Reschedule options for maintenance windows.

    Attributes:
        reschedule (google.cloud.sqladmin_v1.types.SqlInstancesRescheduleMaintenanceRequestBody.Reschedule):
            Required. The type of the reschedule the user
            wants.
    """

    class RescheduleType(proto.Enum):
        r"""

        Values:
            RESCHEDULE_TYPE_UNSPECIFIED (0):
                No description available.
            IMMEDIATE (1):
                Reschedules maintenance to happen now (within
                5 minutes).
            NEXT_AVAILABLE_WINDOW (2):
                Reschedules maintenance to occur within one
                week from the originally scheduled day and time.
            SPECIFIC_TIME (3):
                Reschedules maintenance to a specific time
                and day.
        """

        RESCHEDULE_TYPE_UNSPECIFIED = 0
        IMMEDIATE = 1
        NEXT_AVAILABLE_WINDOW = 2
        SPECIFIC_TIME = 3

    class Reschedule(proto.Message):
        r"""

        Attributes:
            reschedule_type (google.cloud.sqladmin_v1.types.SqlInstancesRescheduleMaintenanceRequestBody.RescheduleType):
                Required. The type of the reschedule.
            schedule_time (google.protobuf.timestamp_pb2.Timestamp):
                Optional. Timestamp when the maintenance shall be
                rescheduled to if reschedule_type=SPECIFIC_TIME, in `RFC
                3339 <https://tools.ietf.org/html/rfc3339>`__ format, for
                example ``2012-11-15T16:19:00.094Z``.
        """

        reschedule_type: "SqlInstancesRescheduleMaintenanceRequestBody.RescheduleType" = proto.Field(
            proto.ENUM,
            number=1,
            enum="SqlInstancesRescheduleMaintenanceRequestBody.RescheduleType",
        )
        schedule_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=2,
            message=timestamp_pb2.Timestamp,
        )

    reschedule: Reschedule = proto.Field(
        proto.MESSAGE,
        number=3,
        message=Reschedule,
    )


class DemoteMasterContext(proto.Message):
    r"""Database instance demote primary instance context.

    Attributes:
        kind (str):
            This is always ``sql#demoteMasterContext``.
        verify_gtid_consistency (google.protobuf.wrappers_pb2.BoolValue):
            Verify the GTID consistency for demote operation. Default
            value: ``True``. Setting this flag to ``false`` enables you
            to bypass the GTID consistency check between on-premises
            primary instance and Cloud SQL instance during the demotion
            operation but also exposes you to the risk of future
            replication failures. Change the value only if you know the
            reason for the GTID divergence and are confident that doing
            so will not cause any replication issues.
        master_instance_name (str):
            The name of the instance which will act as
            on-premises primary instance in the replication
            setup.
        replica_configuration (google.cloud.sqladmin_v1.types.DemoteMasterConfiguration):
            Configuration specific to read-replicas
            replicating from the on-premises primary
            instance.
        skip_replication_setup (bool):
            Flag to skip replication setup on the
            instance.
    """

    kind: str = proto.Field(
        proto.STRING,
        number=1,
    )
    verify_gtid_consistency: wrappers_pb2.BoolValue = proto.Field(
        proto.MESSAGE,
        number=2,
        message=wrappers_pb2.BoolValue,
    )
    master_instance_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    replica_configuration: cloud_sql_resources.DemoteMasterConfiguration = proto.Field(
        proto.MESSAGE,
        number=4,
        message=cloud_sql_resources.DemoteMasterConfiguration,
    )
    skip_replication_setup: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class DemoteContext(proto.Message):
    r"""This context is used to demote an existing standalone
    instance to be a Cloud SQL read replica for an external database
    server.

    Attributes:
        kind (str):
            This is always ``sql#demoteContext``.
        source_representative_instance_name (str):
            Required. The name of the instance which acts
            as the on-premises primary instance in the
            replication setup.
    """

    kind: str = proto.Field(
        proto.STRING,
        number=1,
    )
    source_representative_instance_name: str = proto.Field(
        proto.STRING,
        number=2,
    )


class FailoverContext(proto.Message):
    r"""Database instance failover context.

    Attributes:
        settings_version (int):
            The current settings version of this
            instance. Request will be rejected if this
            version doesn't match the current settings
            version.
        kind (str):
            This is always ``sql#failoverContext``.
    """

    settings_version: int = proto.Field(
        proto.INT64,
        number=1,
    )
    kind: str = proto.Field(
        proto.STRING,
        number=2,
    )


class RestoreBackupContext(proto.Message):
    r"""Database instance restore from backup context.
    Backup context contains source instance id and project id.

    Attributes:
        kind (str):
            This is always ``sql#restoreBackupContext``.
        backup_run_id (int):
            The ID of the backup run to restore from.
        instance_id (str):
            The ID of the instance that the backup was
            taken from.
        project (str):
            The full project ID of the source instance.
    """

    kind: str = proto.Field(
        proto.STRING,
        number=1,
    )
    backup_run_id: int = proto.Field(
        proto.INT64,
        number=2,
    )
    instance_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    project: str = proto.Field(
        proto.STRING,
        number=4,
    )


class RotateServerCaContext(proto.Message):
    r"""Instance rotate server CA context.

    Attributes:
        kind (str):
            This is always ``sql#rotateServerCaContext``.
        next_version (str):
            The fingerprint of the next version to be
            rotated to. If left unspecified, will be rotated
            to the most recently added server CA version.
    """

    kind: str = proto.Field(
        proto.STRING,
        number=1,
    )
    next_version: str = proto.Field(
        proto.STRING,
        number=2,
    )


class RotateServerCertificateContext(proto.Message):
    r"""Instance rotate server certificate context.

    Attributes:
        kind (str):
            Optional. This is always
            ``sql#rotateServerCertificateContext``.
        next_version (str):
            The fingerprint of the next version to be
            rotated to. If left unspecified, will be rotated
            to the most recently added server certificate
            version.
    """

    kind: str = proto.Field(
        proto.STRING,
        number=1,
    )
    next_version: str = proto.Field(
        proto.STRING,
        number=2,
    )


class RotateEntraIdCertificateContext(proto.Message):
    r"""Instance rotate Entra ID certificate context.

    Attributes:
        kind (str):
            Optional. This is always
            ``sql#rotateEntraIdCertificateContext``.
        next_version (str):
            Optional. The fingerprint of the next version
            to be rotated to. If left unspecified, will be
            rotated to the most recently added server
            certificate version.
    """

    kind: str = proto.Field(
        proto.STRING,
        number=1,
    )
    next_version: str = proto.Field(
        proto.STRING,
        number=2,
    )


class TruncateLogContext(proto.Message):
    r"""Database Instance truncate log context.

    Attributes:
        kind (str):
            This is always ``sql#truncateLogContext``.
        log_type (str):
            The type of log to truncate. Valid values are
            ``MYSQL_GENERAL_TABLE`` and ``MYSQL_SLOW_TABLE``.
    """

    kind: str = proto.Field(
        proto.STRING,
        number=1,
    )
    log_type: str = proto.Field(
        proto.STRING,
        number=2,
    )


class SqlExternalSyncSettingError(proto.Message):
    r"""External primary instance migration setting error/warning.

    Attributes:
        kind (str):
            Can be ``sql#externalSyncSettingError`` or
            ``sql#externalSyncSettingWarning``.
        type_ (google.cloud.sqladmin_v1.types.SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType):
            Identifies the specific error that occurred.
        detail (str):
            Additional information about the error
            encountered.
    """

    class SqlExternalSyncSettingErrorType(proto.Enum):
        r"""

        Values:
            SQL_EXTERNAL_SYNC_SETTING_ERROR_TYPE_UNSPECIFIED (0):
                No description available.
            CONNECTION_FAILURE (1):
                No description available.
            BINLOG_NOT_ENABLED (2):
                No description available.
            INCOMPATIBLE_DATABASE_VERSION (3):
                No description available.
            REPLICA_ALREADY_SETUP (4):
                No description available.
            INSUFFICIENT_PRIVILEGE (5):
                The replication user is missing privileges
                that are required.
            UNSUPPORTED_MIGRATION_TYPE (6):
                Unsupported migration type.
            NO_PGLOGICAL_INSTALLED (7):
                No pglogical extension installed on
                databases, applicable for postgres.
            PGLOGICAL_NODE_ALREADY_EXISTS (8):
                pglogical node already exists on databases,
                applicable for postgres.
            INVALID_WAL_LEVEL (9):
                The value of parameter wal_level is not set to logical.
            INVALID_SHARED_PRELOAD_LIBRARY (10):
                The value of parameter shared_preload_libraries does not
                include pglogical.
            INSUFFICIENT_MAX_REPLICATION_SLOTS (11):
                The value of parameter max_replication_slots is not
                sufficient.
            INSUFFICIENT_MAX_WAL_SENDERS (12):
                The value of parameter max_wal_senders is not sufficient.
            INSUFFICIENT_MAX_WORKER_PROCESSES (13):
                The value of parameter max_worker_processes is not
                sufficient.
            UNSUPPORTED_EXTENSIONS (14):
                Extensions installed are either not supported
                or having unsupported versions.
            INVALID_RDS_LOGICAL_REPLICATION (15):
                The value of parameter rds.logical_replication is not set to
                1.
            INVALID_LOGGING_SETUP (16):
                The primary instance logging setup doesn't
                allow EM sync.
            INVALID_DB_PARAM (17):
                The primary instance database parameter setup
                doesn't allow EM sync.
            UNSUPPORTED_GTID_MODE (18):
                The gtid_mode is not supported, applicable for MySQL.
            SQLSERVER_AGENT_NOT_RUNNING (19):
                SQL Server Agent is not running.
            UNSUPPORTED_TABLE_DEFINITION (20):
                The table definition is not support due to
                missing primary key or replica identity,
                applicable for postgres. Note that this is a
                warning and won't block the migration.
            UNSUPPORTED_DEFINER (21):
                The customer has a definer that will break EM
                setup.
            SQLSERVER_SERVERNAME_MISMATCH (22):
                SQL Server @@SERVERNAME does not match actual
                host name.
            PRIMARY_ALREADY_SETUP (23):
                The primary instance has been setup and will
                fail the setup.
            UNSUPPORTED_BINLOG_FORMAT (24):
                The primary instance has unsupported binary
                log format.
            BINLOG_RETENTION_SETTING (25):
                The primary instance's binary log retention
                setting.
            UNSUPPORTED_STORAGE_ENGINE (26):
                The primary instance has tables with
                unsupported storage engine.
            LIMITED_SUPPORT_TABLES (27):
                Source has tables with limited support
                eg: PostgreSQL tables without primary keys.
            EXISTING_DATA_IN_REPLICA (28):
                The replica instance contains existing data.
            MISSING_OPTIONAL_PRIVILEGES (29):
                The replication user is missing privileges
                that are optional.
            RISKY_BACKUP_ADMIN_PRIVILEGE (30):
                Additional BACKUP_ADMIN privilege is granted to the
                replication user which may lock source MySQL 8 instance for
                DDLs during initial sync.
            INSUFFICIENT_GCS_PERMISSIONS (31):
                The Cloud Storage bucket is missing necessary
                permissions.
            INVALID_FILE_INFO (32):
                The Cloud Storage bucket has an error in the
                file or contains invalid file information.
            UNSUPPORTED_DATABASE_SETTINGS (33):
                The source instance has unsupported database
                settings for migration.
            MYSQL_PARALLEL_IMPORT_INSUFFICIENT_PRIVILEGE (34):
                The replication user is missing parallel
                import specific privileges. (e.g. LOCK TABLES)
                for MySQL.
            LOCAL_INFILE_OFF (35):
                The global variable local_infile is off on external server
                replica.
            TURN_ON_PITR_AFTER_PROMOTE (36):
                This code instructs customers to turn on
                point-in-time recovery manually for the instance
                after promoting the Cloud SQL for PostgreSQL
                instance.
            INCOMPATIBLE_DATABASE_MINOR_VERSION (37):
                The minor version of replica database is
                incompatible with the source.
            SOURCE_MAX_SUBSCRIPTIONS (38):
                This warning message indicates that Cloud SQL
                uses the maximum number of subscriptions to
                migrate data from the source to the destination.
            UNABLE_TO_VERIFY_DEFINERS (39):
                Unable to verify definers on the source for
                MySQL.
            SUBSCRIPTION_CALCULATION_STATUS (40):
                If a time out occurs while the subscription
                counts are calculated, then this value is set to
                1. Otherwise, this value is set to 2.
            PG_SUBSCRIPTION_COUNT (41):
                Count of subscriptions needed to sync source
                data for PostgreSQL database.
            PG_SYNC_PARALLEL_LEVEL (42):
                Final parallel level that is used to do
                migration.
            INSUFFICIENT_DISK_SIZE (43):
                The disk size of the replica instance is
                smaller than the data size of the source
                instance.
            INSUFFICIENT_MACHINE_TIER (44):
                The data size of the source instance is
                greater than 1 TB, the number of cores of the
                replica instance is less than 8, and the memory
                of the replica is less than 32 GB.
            UNSUPPORTED_EXTENSIONS_NOT_MIGRATED (45):
                The warning message indicates the unsupported
                extensions will not be migrated to the
                destination.
            EXTENSIONS_NOT_MIGRATED (46):
                The warning message indicates the pg_cron extension and
                settings will not be migrated to the destination.
            PG_CRON_FLAG_ENABLED_IN_REPLICA (47):
                The error message indicates that pg_cron flags are enabled
                on the destination which is not supported during the
                migration.
            EXTENSIONS_NOT_ENABLED_IN_REPLICA (48):
                This error message indicates that the
                specified extensions are not enabled on
                destination instance. For example, before you
                can migrate data to the destination instance,
                you must enable the PGAudit extension on the
                instance.
            UNSUPPORTED_COLUMNS (49):
                The source database has generated columns
                that can't be migrated. Please change them to
                regular columns before migration.
            USERS_NOT_CREATED_IN_REPLICA (50):
                The source database has users that aren't created in the
                replica. First, create all users, which are in the
                pg_user_mappings table of the source database, in the
                destination instance. Then, perform the migration.
            UNSUPPORTED_SYSTEM_OBJECTS (51):
                The selected objects include system objects
                that aren't supported for migration.
            UNSUPPORTED_TABLES_WITH_REPLICA_IDENTITY (52):
                The source database has tables with the FULL
                or NOTHING replica identity. Before starting
                your migration, either remove the identity or
                change it to DEFAULT. Note that this is an error
                and will block the migration.
            SELECTED_OBJECTS_NOT_EXIST_ON_SOURCE (53):
                The selected objects don't exist on the
                source instance.
            PSC_ONLY_INSTANCE_WITH_NO_NETWORK_ATTACHMENT_URI (54):
                PSC only destination instance does not have a
                network attachment URI.
            SELECTED_OBJECTS_REFERENCE_UNSELECTED_OBJECTS (55):
                Selected objects reference unselected
                objects. Based on their object type (foreign key
                constraint or view), selected objects will fail
                during migration.
            PROMPT_DELETE_EXISTING (56):
                The migration will delete existing data in the replica; set
                [replica_overwrite_enabled][google.cloud.sql.v1.SqlInstancesStartExternalSyncRequest.replica_overwrite_enabled]
                in the request to acknowledge this. This is an error. MySQL
                only.
            WILL_DELETE_EXISTING (57):
                The migration will delete existing data in the replica;
                [replica_overwrite_enabled][google.cloud.sql.v1.SqlInstancesStartExternalSyncRequest.replica_overwrite_enabled]
                was set in the request acknowledging this. This is a warning
                rather than an error. MySQL only.
            PG_DDL_REPLICATION_INSUFFICIENT_PRIVILEGE (58):
                The replication user is missing specific
                privileges to setup DDL replication. (e.g.
                CREATE EVENT TRIGGER, CREATE SCHEMA) for
                PostgreSQL.
            WRITABLE_DESTINATION_REPLICA_RECREATION_DOWNTIME (59):
                Read replicas of the Writable Destination
                instance will be recreated after external
                synchronization is complete, causing downtime on
                read replicas.
            WRITABLE_DESTINATION_STORAGE_AUTO_INCREASE_DISABLED (60):
                A warning that disk storage auto increase is
                disabled on the destination instance for a
                Writable Destination migration.
        """

        SQL_EXTERNAL_SYNC_SETTING_ERROR_TYPE_UNSPECIFIED = 0
        CONNECTION_FAILURE = 1
        BINLOG_NOT_ENABLED = 2
        INCOMPATIBLE_DATABASE_VERSION = 3
        REPLICA_ALREADY_SETUP = 4
        INSUFFICIENT_PRIVILEGE = 5
        UNSUPPORTED_MIGRATION_TYPE = 6
        NO_PGLOGICAL_INSTALLED = 7
        PGLOGICAL_NODE_ALREADY_EXISTS = 8
        INVALID_WAL_LEVEL = 9
        INVALID_SHARED_PRELOAD_LIBRARY = 10
        INSUFFICIENT_MAX_REPLICATION_SLOTS = 11
        INSUFFICIENT_MAX_WAL_SENDERS = 12
        INSUFFICIENT_MAX_WORKER_PROCESSES = 13
        UNSUPPORTED_EXTENSIONS = 14
        INVALID_RDS_LOGICAL_REPLICATION = 15
        INVALID_LOGGING_SETUP = 16
        INVALID_DB_PARAM = 17
        UNSUPPORTED_GTID_MODE = 18
        SQLSERVER_AGENT_NOT_RUNNING = 19
        UNSUPPORTED_TABLE_DEFINITION = 20
        UNSUPPORTED_DEFINER = 21
        SQLSERVER_SERVERNAME_MISMATCH = 22
        PRIMARY_ALREADY_SETUP = 23
        UNSUPPORTED_BINLOG_FORMAT = 24
        BINLOG_RETENTION_SETTING = 25
        UNSUPPORTED_STORAGE_ENGINE = 26
        LIMITED_SUPPORT_TABLES = 27
        EXISTING_DATA_IN_REPLICA = 28
        MISSING_OPTIONAL_PRIVILEGES = 29
        RISKY_BACKUP_ADMIN_PRIVILEGE = 30
        INSUFFICIENT_GCS_PERMISSIONS = 31
        INVALID_FILE_INFO = 32
        UNSUPPORTED_DATABASE_SETTINGS = 33
        MYSQL_PARALLEL_IMPORT_INSUFFICIENT_PRIVILEGE = 34
        LOCAL_INFILE_OFF = 35
        TURN_ON_PITR_AFTER_PROMOTE = 36
        INCOMPATIBLE_DATABASE_MINOR_VERSION = 37
        SOURCE_MAX_SUBSCRIPTIONS = 38
        UNABLE_TO_VERIFY_DEFINERS = 39
        SUBSCRIPTION_CALCULATION_STATUS = 40
        PG_SUBSCRIPTION_COUNT = 41
        PG_SYNC_PARALLEL_LEVEL = 42
        INSUFFICIENT_DISK_SIZE = 43
        INSUFFICIENT_MACHINE_TIER = 44
        UNSUPPORTED_EXTENSIONS_NOT_MIGRATED = 45
        EXTENSIONS_NOT_MIGRATED = 46
        PG_CRON_FLAG_ENABLED_IN_REPLICA = 47
        EXTENSIONS_NOT_ENABLED_IN_REPLICA = 48
        UNSUPPORTED_COLUMNS = 49
        USERS_NOT_CREATED_IN_REPLICA = 50
        UNSUPPORTED_SYSTEM_OBJECTS = 51
        UNSUPPORTED_TABLES_WITH_REPLICA_IDENTITY = 52
        SELECTED_OBJECTS_NOT_EXIST_ON_SOURCE = 53
        PSC_ONLY_INSTANCE_WITH_NO_NETWORK_ATTACHMENT_URI = 54
        SELECTED_OBJECTS_REFERENCE_UNSELECTED_OBJECTS = 55
        PROMPT_DELETE_EXISTING = 56
        WILL_DELETE_EXISTING = 57
        PG_DDL_REPLICATION_INSUFFICIENT_PRIVILEGE = 58
        WRITABLE_DESTINATION_REPLICA_RECREATION_DOWNTIME = 59
        WRITABLE_DESTINATION_STORAGE_AUTO_INCREASE_DISABLED = 60

    kind: str = proto.Field(
        proto.STRING,
        number=1,
    )
    type_: SqlExternalSyncSettingErrorType = proto.Field(
        proto.ENUM,
        number=2,
        enum=SqlExternalSyncSettingErrorType,
    )
    detail: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SelectedObjects(proto.Message):
    r"""A list of objects that the user selects for replication from
    an external source instance.

    Attributes:
        database (str):
            Required. The name of the database to
            migrate.
    """

    database: str = proto.Field(
        proto.STRING,
        number=1,
    )


class OnPremisesConfiguration(proto.Message):
    r"""On-premises instance configuration.

    Attributes:
        host_port (str):
            The host and port of the on-premises instance
            in host:port format
        kind (str):
            This is always ``sql#onPremisesConfiguration``.
        username (str):
            The username for connecting to on-premises
            instance.
        password (str):
            The password for connecting to on-premises
            instance.
        ca_certificate (str):
            PEM representation of the trusted CA's x509
            certificate.
        client_certificate (str):
            PEM representation of the replica's x509
            certificate.
        client_key (str):
            PEM representation of the replica's private
            key. The corresponding public key is encoded in
            the client's certificate.
        dump_file_path (str):
            The dump file to create the Cloud SQL
            replica.
        source_instance (google.cloud.sqladmin_v1.types.InstanceReference):
            The reference to Cloud SQL instance if the
            source is Cloud SQL.
        selected_objects (MutableSequence[google.cloud.sqladmin_v1.types.SelectedObjects]):
            Optional. A list of objects that the user
            selects for replication from an external source
            instance.
        ssl_option (google.cloud.sqladmin_v1.types.OnPremisesConfiguration.SslOption):
            Optional. SSL option for replica connection
            to the on-premises source.
        dms_managed (bool):
            Output only. Indicates whether the resource
            is managed by Database Migration Service.
    """

    class SslOption(proto.Enum):
        r"""SslOption defines the SSL mode to be used for replica
        connection to the on-premises source.

        Values:
            SSL_OPTION_UNSPECIFIED (0):
                Unknown SSL option i.e. SSL option not
                specified by user.
            DISABLE (1):
                SSL is not used for replica connection to the
                on-premises source.
            REQUIRE (2):
                SSL is required for replica connection to the
                on-premises source.
            VERIFY_CA (3):
                Verify CA is required for replica connection
                to the on-premises source.
        """

        SSL_OPTION_UNSPECIFIED = 0
        DISABLE = 1
        REQUIRE = 2
        VERIFY_CA = 3

    host_port: str = proto.Field(
        proto.STRING,
        number=1,
    )
    kind: str = proto.Field(
        proto.STRING,
        number=2,
    )
    username: str = proto.Field(
        proto.STRING,
        number=3,
    )
    password: str = proto.Field(
        proto.STRING,
        number=4,
    )
    ca_certificate: str = proto.Field(
        proto.STRING,
        number=5,
    )
    client_certificate: str = proto.Field(
        proto.STRING,
        number=6,
    )
    client_key: str = proto.Field(
        proto.STRING,
        number=7,
    )
    dump_file_path: str = proto.Field(
        proto.STRING,
        number=8,
    )
    source_instance: cloud_sql_resources.InstanceReference = proto.Field(
        proto.MESSAGE,
        number=15,
        message=cloud_sql_resources.InstanceReference,
    )
    selected_objects: MutableSequence["SelectedObjects"] = proto.RepeatedField(
        proto.MESSAGE,
        number=16,
        message="SelectedObjects",
    )
    ssl_option: SslOption = proto.Field(
        proto.ENUM,
        number=18,
        enum=SslOption,
    )
    dms_managed: bool = proto.Field(
        proto.BOOL,
        number=20,
    )


class ReplicaConfiguration(proto.Message):
    r"""Read-replica configuration for connecting to the primary
    instance.

    Attributes:
        kind (str):
            This is always ``sql#replicaConfiguration``.
        mysql_replica_configuration (google.cloud.sqladmin_v1.types.MySqlReplicaConfiguration):
            MySQL specific configuration when replicating from a MySQL
            on-premises primary instance. Replication configuration
            information such as the username, password, certificates,
            and keys are not stored in the instance metadata. The
            configuration information is used only to set up the
            replication connection and is stored by MySQL in a file
            named ``master.info`` in the data directory.
        failover_target (google.protobuf.wrappers_pb2.BoolValue):
            Specifies if the replica is the failover target. If the
            field is set to ``true``, the replica will be designated as
            a failover replica. In case the primary instance fails, the
            replica instance will be promoted as the new primary
            instance. Only one replica can be specified as failover
            target, and the replica has to be in different zone with the
            primary instance.
        cascadable_replica (google.protobuf.wrappers_pb2.BoolValue):
            Optional. Specifies if a SQL Server replica
            is a cascadable replica. A cascadable replica is
            a SQL Server cross region replica that supports
            replica(s) under it.
    """

    kind: str = proto.Field(
        proto.STRING,
        number=1,
    )
    mysql_replica_configuration: cloud_sql_resources.MySqlReplicaConfiguration = (
        proto.Field(
            proto.MESSAGE,
            number=2,
            message=cloud_sql_resources.MySqlReplicaConfiguration,
        )
    )
    failover_target: wrappers_pb2.BoolValue = proto.Field(
        proto.MESSAGE,
        number=3,
        message=wrappers_pb2.BoolValue,
    )
    cascadable_replica: wrappers_pb2.BoolValue = proto.Field(
        proto.MESSAGE,
        number=5,
        message=wrappers_pb2.BoolValue,
    )


class SqlInstancesExecuteSqlRequest(proto.Message):
    r"""

    Attributes:
        instance (str):
            Required. Database instance ID. This does not
            include the project ID.
        project (str):
            Required. Project ID of the project that
            contains the instance.
        body (google.cloud.sqladmin_v1.types.ExecuteSqlPayload):
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
            Used together with the ``user`` field. The secret resource
            name will not be stored.

            This field is a member of `oneof`_ ``user_password``.
        auto_iam_authn (bool):
            Optional. When set to ``true``, the API caller identity
            associated with the request is used for database
            authentication. The API caller must be an IAM user in the
            database.

            This field is a member of `oneof`_ ``user_password``.
        row_limit (int):
            Optional. The maximum number of rows returned
            per SQL statement.
        partial_result_mode (google.cloud.sqladmin_v1.types.ExecuteSqlPayload.PartialResultMode):
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
        messages (MutableSequence[google.cloud.sqladmin_v1.types.SqlInstancesExecuteSqlResponse.Message]):
            A list of notices and warnings generated during query
            execution. For PostgreSQL, this includes all notices and
            warnings. For MySQL, this includes warnings generated by the
            last executed statement. To retrieve all warnings for a
            multi-statement query, ``SHOW WARNINGS`` must be executed
            after each statement.
        metadata (google.cloud.sqladmin_v1.types.Metadata):
            The additional metadata information regarding
            the execution of the SQL statements.
        results (MutableSequence[google.cloud.sqladmin_v1.types.QueryResult]):
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
        columns (MutableSequence[google.cloud.sqladmin_v1.types.Column]):
            List of columns included in the result. This
            also includes the data type of the column.
        rows (MutableSequence[google.cloud.sqladmin_v1.types.Row]):
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
        values (MutableSequence[google.cloud.sqladmin_v1.types.Value]):
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
            The cell value in string format.
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
            Required. Project ID of the project that
            contains the instance (Example: project-id).
        body (google.cloud.sqladmin_v1.types.InstancesAcquireSsrsLeaseRequest):
            Required. The request body.
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
    body: "InstancesAcquireSsrsLeaseRequest" = proto.Field(
        proto.MESSAGE,
        number=100,
        message="InstancesAcquireSsrsLeaseRequest",
    )
    location: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SqlInstancesAcquireSsrsLeaseResponse(proto.Message):
    r"""Response for the acquire SSRS lease request.

    Attributes:
        operation_id (str):
            The unique identifier for this operation.
    """

    operation_id: str = proto.Field(
        proto.STRING,
        number=1,
    )


class SqlInstancesReleaseSsrsLeaseRequest(proto.Message):
    r"""Request to release a lease for SSRS.

    Attributes:
        instance (str):
            Required. The Cloud SQL instance ID. This
            doesn't include the project ID. The instance ID
            contains lowercase letters, numbers, and
            hyphens, and it must start with a letter. This
            ID can have a maximum length of 98 characters.
        project (str):
            Required. The project ID that contains the
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


class SqlInstancesReleaseSsrsLeaseResponse(proto.Message):
    r"""Response for the release SSRS lease request.

    Attributes:
        operation_id (str):
            The unique identifier for this operation.
    """

    operation_id: str = proto.Field(
        proto.STRING,
        number=1,
    )


class SqlInstancesPointInTimeRestoreRequest(proto.Message):
    r"""Request to perform a point in time restore on a Google Cloud
    Backup and Disaster Recovery managed instance.

    Attributes:
        parent (str):
            Required. The parent resource where you
            created this instance. Format:
            projects/{project}
        context (google.cloud.sqladmin_v1.types.PointInTimeRestoreContext):
            Required. The context for request to perform
            a PITR on a Google Cloud Backup and Disaster
            Recovery managed instance.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    context: "PointInTimeRestoreContext" = proto.Field(
        proto.MESSAGE,
        number=100,
        message="PointInTimeRestoreContext",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
