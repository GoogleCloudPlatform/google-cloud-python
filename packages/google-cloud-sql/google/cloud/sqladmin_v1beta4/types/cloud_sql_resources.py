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
import google.type.interval_pb2 as interval_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.sql.v1beta4",
    manifest={
        "SqlFileType",
        "BakType",
        "AutoDnsStatus",
        "SqlMaintenanceType",
        "SqlBackupRunStatus",
        "SqlBackupRunType",
        "SqlBackupKind",
        "SqlBackendType",
        "SqlIpAddressType",
        "SqlInstanceType",
        "SqlDatabaseVersion",
        "SqlSuspensionReason",
        "SqlPricingPlan",
        "SqlReplicationType",
        "SqlDataDiskType",
        "SqlAvailabilityType",
        "SqlUpdateTrack",
        "SqlFlagType",
        "SqlFlagScope",
        "AclEntry",
        "ApiWarning",
        "BackupRetentionSettings",
        "BackupConfiguration",
        "BackupRun",
        "Backup",
        "BackupRunsListResponse",
        "BinLogCoordinates",
        "BackupContext",
        "CloneContext",
        "Database",
        "SqlServerDatabaseDetails",
        "DatabaseFlags",
        "SyncFlags",
        "InstanceReference",
        "DatabaseInstance",
        "BlueGreenDeploymentInfo",
        "DnsNameMapping",
        "GeminiInstanceConfig",
        "ReplicationCluster",
        "AvailableDatabaseVersion",
        "DatabasesListResponse",
        "DemoteMasterConfiguration",
        "DemoteMasterContext",
        "DemoteMasterMySqlReplicaConfiguration",
        "DemoteContext",
        "ExportContext",
        "FailoverContext",
        "Flag",
        "FlagsListResponse",
        "ImportContext",
        "InstancesCloneRequest",
        "InstancesDemoteMasterRequest",
        "InstancesDemoteRequest",
        "InstancesExportRequest",
        "InstancesFailoverRequest",
        "InstancesImportRequest",
        "InstancesPreCheckMajorVersionUpgradeRequest",
        "MySqlSyncConfig",
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
        "PointInTimeRestoreContext",
        "PerformDiskShrinkContext",
        "PreCheckResponse",
        "PreCheckMajorVersionUpgradeContext",
        "SqlInstancesGetDiskShrinkConfigResponse",
        "SqlInstancesVerifyExternalSyncSettingsResponse",
        "SqlExternalSyncSettingError",
        "IpConfiguration",
        "PscConfig",
        "PscAutoConnectionConfig",
        "IpMapping",
        "LocationPreference",
        "MaintenanceWindow",
        "DenyMaintenancePeriod",
        "InsightsConfig",
        "MySqlReplicaConfiguration",
        "SelectedObjects",
        "OnPremisesConfiguration",
        "DiskEncryptionConfiguration",
        "DiskEncryptionStatus",
        "SqlSubOperationType",
        "Operation",
        "OperationError",
        "OperationErrors",
        "PasswordValidationPolicy",
        "OperationsListResponse",
        "ReplicaConfiguration",
        "RestoreBackupContext",
        "RotateServerCaContext",
        "RotateServerCertificateContext",
        "RotateEntraIdCertificateContext",
        "DataCacheConfig",
        "FinalBackupConfig",
        "Settings",
        "PerformanceCaptureConfig",
        "AdvancedMachineFeatures",
        "SslCert",
        "SslCertDetail",
        "SslCertsCreateEphemeralRequest",
        "SslCertsInsertRequest",
        "SqlInstancesRescheduleMaintenanceRequestBody",
        "SslCertsInsertResponse",
        "SslCertsListResponse",
        "TruncateLogContext",
        "SqlActiveDirectoryConfig",
        "SqlServerAuditConfig",
        "SqlServerEntraIdConfig",
        "ConnectionPoolFlags",
        "ReadPoolAutoScaleConfig",
        "ConnectionPoolConfig",
        "AcquireSsrsLeaseContext",
        "StartWorkloadCaptureContext",
        "StopWorkloadCaptureContext",
        "StartWorkloadReplayContext",
        "StopWorkloadReplayContext",
    },
)


class SqlFileType(proto.Enum):
    r"""

    Values:
        SQL_FILE_TYPE_UNSPECIFIED (0):
            Unknown file type.
        SQL (1):
            File containing SQL statements.
        CSV (2):
            File in CSV format.
        BAK (4):
            No description available.
        TDE (8):
            TDE certificate.
    """

    SQL_FILE_TYPE_UNSPECIFIED = 0
    SQL = 1
    CSV = 2
    BAK = 4
    TDE = 8


class BakType(proto.Enum):
    r"""

    Values:
        BAK_TYPE_UNSPECIFIED (0):
            Default type.
        FULL (1):
            Full backup.
        DIFF (2):
            Differential backup.
        TLOG (3):
            SQL Server Transaction Log
    """

    BAK_TYPE_UNSPECIFIED = 0
    FULL = 1
    DIFF = 2
    TLOG = 3


class AutoDnsStatus(proto.Enum):
    r"""The status of automated DNS provisioning.

    Values:
        AUTO_DNS_STATUS_UNSPECIFIED (0):
            Unspecified status. This means status is
            missing from dependency service.
        AUTO_DNS_OK (1):
            DNS provisioning is OK.
        AUTO_DNS_FAILED (2):
            DNS provisioning failed.
        AUTO_DNS_UNKNOWN (3):
            DNS provisioning status is not recognized by
            Cloud SQL.
    """

    AUTO_DNS_STATUS_UNSPECIFIED = 0
    AUTO_DNS_OK = 1
    AUTO_DNS_FAILED = 2
    AUTO_DNS_UNKNOWN = 3


class SqlMaintenanceType(proto.Enum):
    r"""The type of maintenance to be performed on the instance.

    Values:
        SQL_MAINTENANCE_TYPE_UNSPECIFIED (0):
            Maintenance type is unspecified.
        INSTANCE_MAINTENANCE (1):
            Indicates that a standalone instance is
            undergoing maintenance. The instance can be
            either a primary instance or a replica.
        REPLICA_INCLUDED_MAINTENANCE (2):
            Indicates that the primary instance and all
            of its replicas, including cascading replicas,
            are undergoing maintenance. Maintenance is
            performed on groups of replicas first, followed
            by the primary instance.
        INSTANCE_SELF_SERVICE_MAINTENANCE (3):
            Indicates that the standalone instance is
            undergoing maintenance, initiated by
            self-service. The instance can be either a
            primary instance or a replica.
        REPLICA_INCLUDED_SELF_SERVICE_MAINTENANCE (4):
            Indicates that the primary instance and all
            of its replicas are undergoing maintenance,
            initiated by self-service. Maintenance is
            performed on groups of replicas first, followed
            by the primary instance.
    """

    SQL_MAINTENANCE_TYPE_UNSPECIFIED = 0
    INSTANCE_MAINTENANCE = 1
    REPLICA_INCLUDED_MAINTENANCE = 2
    INSTANCE_SELF_SERVICE_MAINTENANCE = 3
    REPLICA_INCLUDED_SELF_SERVICE_MAINTENANCE = 4


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


class SqlBackupRunType(proto.Enum):
    r"""

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


class SqlBackupKind(proto.Enum):
    r"""Defines the supported backup kinds

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


class SqlBackendType(proto.Enum):
    r"""

    Values:
        SQL_BACKEND_TYPE_UNSPECIFIED (0):
            This is an unknown backend type for instance.
        FIRST_GEN (1):
            V1 speckle instance.
        SECOND_GEN (2):
            V2 speckle instance.
        EXTERNAL (3):
            On premises instance.
    """

    SQL_BACKEND_TYPE_UNSPECIFIED = 0
    FIRST_GEN = 1
    SECOND_GEN = 2
    EXTERNAL = 3


class SqlIpAddressType(proto.Enum):
    r"""

    Values:
        SQL_IP_ADDRESS_TYPE_UNSPECIFIED (0):
            This is an unknown IP address type.
        PRIMARY (1):
            IP address the customer is supposed to
            connect to. Usually this is the load balancer's
            IP address
        OUTGOING (2):
            Source IP address of the connection a read
            replica establishes to its external primary
            instance. This IP address can be allowlisted by
            the customer in case it has a firewall that
            filters incoming connection to its on premises
            primary instance.
        PRIVATE (3):
            Private IP used when using private IPs and
            network peering.
        MIGRATED_1ST_GEN (4):
            V1 IP of a migrated instance. We want the
            user to decommission this IP as soon as the
            migration is complete. Note: V1 instances with
            V1 ip addresses will be counted as PRIMARY.
    """

    SQL_IP_ADDRESS_TYPE_UNSPECIFIED = 0
    PRIMARY = 1
    OUTGOING = 2
    PRIVATE = 3
    MIGRATED_1ST_GEN = 4


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


class SqlDatabaseVersion(proto.Enum):
    r"""The database engine type and version.

    Values:
        SQL_DATABASE_VERSION_UNSPECIFIED (0):
            This is an unknown database version.
        MYSQL_5_1 (2):
            The database version is MySQL 5.1.
        MYSQL_5_5 (3):
            The database version is MySQL 5.5.
        MYSQL_5_6 (5):
            The database version is MySQL 5.6.
        MYSQL_5_7 (6):
            The database version is MySQL 5.7.
        MYSQL_8_0 (20):
            The database version is MySQL 8.
        MYSQL_8_0_18 (41):
            The database major version is MySQL 8.0 and
            the minor version is 18.
        MYSQL_8_0_26 (85):
            The database major version is MySQL 8.0 and
            the minor version is 26.
        MYSQL_8_0_27 (111):
            The database major version is MySQL 8.0 and
            the minor version is 27.
        MYSQL_8_0_28 (132):
            The database major version is MySQL 8.0 and
            the minor version is 28.
        MYSQL_8_0_29 (148):
            The database major version is MySQL 8.0 and
            the minor version is 29.
        MYSQL_8_0_30 (174):
            The database major version is MySQL 8.0 and
            the minor version is 30.
        MYSQL_8_0_31 (197):
            The database major version is MySQL 8.0 and
            the minor version is 31.
        MYSQL_8_0_32 (213):
            The database major version is MySQL 8.0 and
            the minor version is 32.
        MYSQL_8_0_33 (238):
            The database major version is MySQL 8.0 and
            the minor version is 33.
        MYSQL_8_0_34 (239):
            The database major version is MySQL 8.0 and
            the minor version is 34.
        MYSQL_8_0_35 (240):
            The database major version is MySQL 8.0 and
            the minor version is 35.
        MYSQL_8_0_36 (241):
            The database major version is MySQL 8.0 and
            the minor version is 36.
        MYSQL_8_0_37 (355):
            The database major version is MySQL 8.0 and
            the minor version is 37.
        MYSQL_8_0_39 (357):
            The database major version is MySQL 8.0 and
            the minor version is 39.
        MYSQL_8_0_40 (358):
            The database major version is MySQL 8.0 and
            the minor version is 40.
        MYSQL_8_0_41 (488):
            The database major version is MySQL 8.0 and
            the minor version is 41.
        MYSQL_8_0_42 (489):
            The database major version is MySQL 8.0 and
            the minor version is 42.
        MYSQL_8_0_43 (553):
            The database major version is MySQL 8.0 and
            the minor version is 43.
        MYSQL_8_0_44 (554):
            The database major version is MySQL 8.0 and
            the minor version is 44.
        MYSQL_8_0_45 (555):
            The database major version is MySQL 8.0 and
            the minor version is 45.
        MYSQL_8_0_46 (556):
            The database major version is MySQL 8.0 and
            the minor version is 46.
        MYSQL_8_4 (398):
            The database version is MySQL 8.4.
        MYSQL_9_7 (654):
            The database version is MySQL 9.7.
        SQLSERVER_2017_STANDARD (11):
            The database version is SQL Server 2017
            Standard.
        SQLSERVER_2017_ENTERPRISE (14):
            The database version is SQL Server 2017
            Enterprise.
        SQLSERVER_2017_EXPRESS (15):
            The database version is SQL Server 2017
            Express.
        SQLSERVER_2017_WEB (16):
            The database version is SQL Server 2017 Web.
        POSTGRES_9_6 (9):
            The database version is PostgreSQL 9.6.
        POSTGRES_10 (18):
            The database version is PostgreSQL 10.
        POSTGRES_11 (10):
            The database version is PostgreSQL 11.
        POSTGRES_12 (19):
            The database version is PostgreSQL 12.
        POSTGRES_13 (23):
            The database version is PostgreSQL 13.
        POSTGRES_14 (110):
            The database version is PostgreSQL 14.
        POSTGRES_15 (172):
            The database version is PostgreSQL 15.
        POSTGRES_16 (272):
            The database version is PostgreSQL 16.
        POSTGRES_17 (408):
            The database version is PostgreSQL 17.
        POSTGRES_18 (557):
            The database version is PostgreSQL 18.
        POSTGRES_19 (684):
            The database version is PostgreSQL 19.
        POSTGRES_20 (781):
            The database version is PostgreSQL 20.
        SQLSERVER_2019_STANDARD (26):
            The database version is SQL Server 2019
            Standard.
        SQLSERVER_2019_ENTERPRISE (27):
            The database version is SQL Server 2019
            Enterprise.
        SQLSERVER_2019_EXPRESS (28):
            The database version is SQL Server 2019
            Express.
        SQLSERVER_2019_WEB (29):
            The database version is SQL Server 2019 Web.
        SQLSERVER_2022_STANDARD (199):
            The database version is SQL Server 2022
            Standard.
        SQLSERVER_2022_ENTERPRISE (200):
            The database version is SQL Server 2022
            Enterprise.
        SQLSERVER_2022_EXPRESS (201):
            The database version is SQL Server 2022
            Express.
        SQLSERVER_2022_WEB (202):
            The database version is SQL Server 2022 Web.
        SQLSERVER_2025_STANDARD (549):
            The database version is SQL Server 2025
            Standard.
        SQLSERVER_2025_ENTERPRISE (550):
            The database version is SQL Server 2025
            Enterprise.
        SQLSERVER_2025_EXPRESS (551):
            The database version is SQL Server 2025
            Express.
    """

    SQL_DATABASE_VERSION_UNSPECIFIED = 0
    MYSQL_5_1 = 2
    MYSQL_5_5 = 3
    MYSQL_5_6 = 5
    MYSQL_5_7 = 6
    MYSQL_8_0 = 20
    MYSQL_8_0_18 = 41
    MYSQL_8_0_26 = 85
    MYSQL_8_0_27 = 111
    MYSQL_8_0_28 = 132
    MYSQL_8_0_29 = 148
    MYSQL_8_0_30 = 174
    MYSQL_8_0_31 = 197
    MYSQL_8_0_32 = 213
    MYSQL_8_0_33 = 238
    MYSQL_8_0_34 = 239
    MYSQL_8_0_35 = 240
    MYSQL_8_0_36 = 241
    MYSQL_8_0_37 = 355
    MYSQL_8_0_39 = 357
    MYSQL_8_0_40 = 358
    MYSQL_8_0_41 = 488
    MYSQL_8_0_42 = 489
    MYSQL_8_0_43 = 553
    MYSQL_8_0_44 = 554
    MYSQL_8_0_45 = 555
    MYSQL_8_0_46 = 556
    MYSQL_8_4 = 398
    MYSQL_9_7 = 654
    SQLSERVER_2017_STANDARD = 11
    SQLSERVER_2017_ENTERPRISE = 14
    SQLSERVER_2017_EXPRESS = 15
    SQLSERVER_2017_WEB = 16
    POSTGRES_9_6 = 9
    POSTGRES_10 = 18
    POSTGRES_11 = 10
    POSTGRES_12 = 19
    POSTGRES_13 = 23
    POSTGRES_14 = 110
    POSTGRES_15 = 172
    POSTGRES_16 = 272
    POSTGRES_17 = 408
    POSTGRES_18 = 557
    POSTGRES_19 = 684
    POSTGRES_20 = 781
    SQLSERVER_2019_STANDARD = 26
    SQLSERVER_2019_ENTERPRISE = 27
    SQLSERVER_2019_EXPRESS = 28
    SQLSERVER_2019_WEB = 29
    SQLSERVER_2022_STANDARD = 199
    SQLSERVER_2022_ENTERPRISE = 200
    SQLSERVER_2022_EXPRESS = 201
    SQLSERVER_2022_WEB = 202
    SQLSERVER_2025_STANDARD = 549
    SQLSERVER_2025_ENTERPRISE = 550
    SQLSERVER_2025_EXPRESS = 551


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


class SqlPricingPlan(proto.Enum):
    r"""The pricing plan for this instance.

    Values:
        SQL_PRICING_PLAN_UNSPECIFIED (0):
            This is an unknown pricing plan for this
            instance.
        PACKAGE (1):
            The instance is billed at a monthly flat
            rate.
        PER_USE (2):
            The instance is billed per usage.
    """

    SQL_PRICING_PLAN_UNSPECIFIED = 0
    PACKAGE = 1
    PER_USE = 2


class SqlReplicationType(proto.Enum):
    r"""

    Values:
        SQL_REPLICATION_TYPE_UNSPECIFIED (0):
            This is an unknown replication type for a
            Cloud SQL instance.
        SYNCHRONOUS (1):
            The synchronous replication mode for First
            Generation instances. It is the default value.
        ASYNCHRONOUS (2):
            The asynchronous replication mode for First
            Generation instances. It provides a slight
            performance gain, but if an outage occurs while
            this option is set to asynchronous, you can lose
            up to a few seconds of updates to your data.
    """

    SQL_REPLICATION_TYPE_UNSPECIFIED = 0
    SYNCHRONOUS = 1
    ASYNCHRONOUS = 2


class SqlDataDiskType(proto.Enum):
    r"""The type of disk that is used for a v2 instance to use.

    Values:
        SQL_DATA_DISK_TYPE_UNSPECIFIED (0):
            This is an unknown data disk type.
        PD_SSD (1):
            An SSD data disk.
        PD_HDD (2):
            An HDD data disk.
        OBSOLETE_LOCAL_SSD (3):
            This field is deprecated and will be removed
            from a future version of the API.
        HYPERDISK_BALANCED (4):
            A Hyperdisk Balanced data disk.
    """

    SQL_DATA_DISK_TYPE_UNSPECIFIED = 0
    PD_SSD = 1
    PD_HDD = 2
    OBSOLETE_LOCAL_SSD = 3
    HYPERDISK_BALANCED = 4


class SqlAvailabilityType(proto.Enum):
    r"""The availability type of the given Cloud SQL instance.

    Values:
        SQL_AVAILABILITY_TYPE_UNSPECIFIED (0):
            This is an unknown Availability type.
        ZONAL (1):
            Zonal available instance.
        REGIONAL (2):
            Regional available instance.
    """

    SQL_AVAILABILITY_TYPE_UNSPECIFIED = 0
    ZONAL = 1
    REGIONAL = 2


class SqlUpdateTrack(proto.Enum):
    r"""

    Values:
        SQL_UPDATE_TRACK_UNSPECIFIED (0):
            This is an unknown maintenance timing
            preference.
        canary (1):
            For an instance with a scheduled maintenance window, this
            maintenance timing indicates that the maintenance update is
            scheduled 7 to 14 days after the notification is sent out.
            Also referred to as ``Week 1`` (Console) and ``preview``
            (gcloud CLI).
        stable (2):
            For an instance with a scheduled maintenance window, this
            maintenance timing indicates that the maintenance update is
            scheduled 15 to 21 days after the notification is sent out.
            Also referred to as ``Week 2`` (Console) and ``production``
            (gcloud CLI).
        week5 (3):
            For instance with a scheduled maintenance
            window, this maintenance timing indicates that
            the maintenance update is scheduled 35 to 42
            days after the notification is sent out.
    """

    SQL_UPDATE_TRACK_UNSPECIFIED = 0
    canary = 1
    stable = 2
    week5 = 3


class SqlFlagType(proto.Enum):
    r"""

    Values:
        SQL_FLAG_TYPE_UNSPECIFIED (0):
            This is an unknown flag type.
        BOOLEAN (1):
            Boolean type flag.
        STRING (2):
            String type flag.
        INTEGER (3):
            Integer type flag.
        NONE (4):
            Flag type used for a server startup option.
        MYSQL_TIMEZONE_OFFSET (5):
            Type introduced specially for MySQL TimeZone offset. Accept
            a string value with the format [-12:59, 13:00].
        FLOAT (6):
            Float type flag.
        REPEATED_STRING (7):
            Comma-separated list of the strings in a
            SqlFlagType enum.
    """

    SQL_FLAG_TYPE_UNSPECIFIED = 0
    BOOLEAN = 1
    STRING = 2
    INTEGER = 3
    NONE = 4
    MYSQL_TIMEZONE_OFFSET = 5
    FLOAT = 6
    REPEATED_STRING = 7


class SqlFlagScope(proto.Enum):
    r"""Scopes of a flag describe where the flag is used.

    Values:
        SQL_FLAG_SCOPE_UNSPECIFIED (0):
            Assume database flags if unspecified
        SQL_FLAG_SCOPE_DATABASE (1):
            database flags
        SQL_FLAG_SCOPE_CONNECTION_POOL (2):
            connection pool configuration flags
    """

    SQL_FLAG_SCOPE_UNSPECIFIED = 0
    SQL_FLAG_SCOPE_DATABASE = 1
    SQL_FLAG_SCOPE_CONNECTION_POOL = 2


class AclEntry(proto.Message):
    r"""An entry for an Access Control list.

    Attributes:
        value (str):
            The allowlisted value for the access control
            list.
        expiration_time (google.protobuf.timestamp_pb2.Timestamp):
            The time when this access control entry expires in `RFC
            3339 <https://tools.ietf.org/html/rfc3339>`__ format, for
            example ``2012-11-15T16:19:00.094Z``.
        name (str):
            Optional. A label to identify this entry.
        kind (str):
            This is always ``sql#aclEntry``.
    """

    value: str = proto.Field(
        proto.STRING,
        number=1,
    )
    expiration_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    kind: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ApiWarning(proto.Message):
    r"""An Admin API warning message.

    Attributes:
        code (google.cloud.sqladmin_v1beta4.types.ApiWarning.SqlApiWarningCode):
            Code to uniquely identify the warning type.
        message (str):
            The warning message.
        region (str):
            The region name for REGION_UNREACHABLE warning.
    """

    class SqlApiWarningCode(proto.Enum):
        r"""

        Values:
            SQL_API_WARNING_CODE_UNSPECIFIED (0):
                An unknown or unset warning type from Cloud
                SQL API.
            REGION_UNREACHABLE (1):
                Warning when one or more regions are not
                reachable.  The returned result set may be
                incomplete.
            MAX_RESULTS_EXCEEDS_LIMIT (2):
                Warning when user provided maxResults
                parameter exceeds the limit.  The returned
                result set may be incomplete.
            COMPROMISED_CREDENTIALS (3):
                Warning when user tries to create/update a
                user with credentials that have previously been
                compromised by a public data breach.
            INTERNAL_STATE_FAILURE (4):
                Warning when the operation succeeds but some
                non-critical workflow state failed.
        """

        SQL_API_WARNING_CODE_UNSPECIFIED = 0
        REGION_UNREACHABLE = 1
        MAX_RESULTS_EXCEEDS_LIMIT = 2
        COMPROMISED_CREDENTIALS = 3
        INTERNAL_STATE_FAILURE = 4

    code: SqlApiWarningCode = proto.Field(
        proto.ENUM,
        number=1,
        enum=SqlApiWarningCode,
    )
    message: str = proto.Field(
        proto.STRING,
        number=2,
    )
    region: str = proto.Field(
        proto.STRING,
        number=3,
    )


class BackupRetentionSettings(proto.Message):
    r"""We currently only support backup retention by specifying the
    number of backups we will retain.

    Attributes:
        retention_unit (google.cloud.sqladmin_v1beta4.types.BackupRetentionSettings.RetentionUnit):
            The unit that 'retained_backups' represents.
        retained_backups (google.protobuf.wrappers_pb2.Int32Value):
            Depending on the value of retention_unit, this is used to
            determine if a backup needs to be deleted. If retention_unit
            is 'COUNT', we will retain this many backups.
    """

    class RetentionUnit(proto.Enum):
        r"""The units that retained_backups specifies, we only support COUNT.

        Values:
            RETENTION_UNIT_UNSPECIFIED (0):
                Backup retention unit is unspecified, will be
                treated as COUNT.
            COUNT (1):
                Retention will be by count, eg. "retain the
                most recent 7 backups".
        """

        RETENTION_UNIT_UNSPECIFIED = 0
        COUNT = 1

    retention_unit: RetentionUnit = proto.Field(
        proto.ENUM,
        number=1,
        enum=RetentionUnit,
    )
    retained_backups: wrappers_pb2.Int32Value = proto.Field(
        proto.MESSAGE,
        number=2,
        message=wrappers_pb2.Int32Value,
    )


class BackupConfiguration(proto.Message):
    r"""Database instance backup configuration.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        start_time (str):
            Start time for the daily backup configuration in UTC
            timezone in the 24 hour format - ``HH:MM``.
        enabled (google.protobuf.wrappers_pb2.BoolValue):
            Whether this configuration is enabled.
        kind (str):
            This is always ``sql#backupConfiguration``.
        binary_log_enabled (google.protobuf.wrappers_pb2.BoolValue):
            (MySQL only) Whether binary log is enabled.
            If backup configuration is disabled, binarylog
            must be disabled as well.
        replication_log_archiving_enabled (google.protobuf.wrappers_pb2.BoolValue):
            Optional. Deprecated: replication_log_archiving_enabled is
            deprecated and will be removed from a future version of the
            API. Use
            [point_in_time_recovery_enabled][google.cloud.sql.v1beta4.BackupConfiguration.point_in_time_recovery_enabled]
            instead.
        location (str):
            Location of the backup
        point_in_time_recovery_enabled (google.protobuf.wrappers_pb2.BoolValue):
            Whether point in time recovery is enabled.
        transaction_log_retention_days (google.protobuf.wrappers_pb2.Int32Value):
            The number of days of transaction logs we
            retain for point in time restore, from 1-7.
        backup_retention_settings (google.cloud.sqladmin_v1beta4.types.BackupRetentionSettings):
            Backup retention settings.
        transactional_log_storage_state (google.cloud.sqladmin_v1beta4.types.BackupConfiguration.TransactionalLogStorageState):
            Output only. This value contains the storage
            location of transactional logs for the database
            for point-in-time recovery.

            This field is a member of `oneof`_ ``_transactional_log_storage_state``.
        backup_tier (google.cloud.sqladmin_v1beta4.types.BackupConfiguration.BackupTier):
            Output only. Backup tier that manages the
            backups for the instance.

            This field is a member of `oneof`_ ``_backup_tier``.
    """

    class TransactionalLogStorageState(proto.Enum):
        r"""This value contains the storage location of the transactional
        logs used to perform point-in-time recovery (PITR) for the
        database.

        Values:
            TRANSACTIONAL_LOG_STORAGE_STATE_UNSPECIFIED (0):
                Unspecified.
            DISK (1):
                The transaction logs used for PITR for the
                instance are stored on a data disk.
            SWITCHING_TO_CLOUD_STORAGE (2):
                The transaction logs used for PITR for the
                instance are switching from being stored on a
                data disk to being stored in Cloud Storage. Only
                applicable to MySQL.
            SWITCHED_TO_CLOUD_STORAGE (3):
                The transaction logs used for PITR for the
                instance are now stored in Cloud Storage.
                Previously, they were stored on a data disk.
                Only applicable to MySQL.
            CLOUD_STORAGE (4):
                The transaction logs used for PITR for the
                instance are stored in Cloud Storage. Only
                applicable to MySQL and PostgreSQL.
        """

        TRANSACTIONAL_LOG_STORAGE_STATE_UNSPECIFIED = 0
        DISK = 1
        SWITCHING_TO_CLOUD_STORAGE = 2
        SWITCHED_TO_CLOUD_STORAGE = 3
        CLOUD_STORAGE = 4

    class BackupTier(proto.Enum):
        r"""Backup tier that manages the backups for the instance.

        Values:
            BACKUP_TIER_UNSPECIFIED (0):
                Unspecified.
            STANDARD (1):
                Instance is managed by Cloud SQL.
            ADVANCED (2):
                Deprecated: ADVANCED is deprecated. Please
                use ENHANCED instead.
            ENHANCED (3):
                Instance is managed by Google Cloud Backup
                and DR Service.
        """

        BACKUP_TIER_UNSPECIFIED = 0
        STANDARD = 1
        ADVANCED = 2
        ENHANCED = 3

    start_time: str = proto.Field(
        proto.STRING,
        number=1,
    )
    enabled: wrappers_pb2.BoolValue = proto.Field(
        proto.MESSAGE,
        number=2,
        message=wrappers_pb2.BoolValue,
    )
    kind: str = proto.Field(
        proto.STRING,
        number=3,
    )
    binary_log_enabled: wrappers_pb2.BoolValue = proto.Field(
        proto.MESSAGE,
        number=4,
        message=wrappers_pb2.BoolValue,
    )
    replication_log_archiving_enabled: wrappers_pb2.BoolValue = proto.Field(
        proto.MESSAGE,
        number=5,
        message=wrappers_pb2.BoolValue,
    )
    location: str = proto.Field(
        proto.STRING,
        number=6,
    )
    point_in_time_recovery_enabled: wrappers_pb2.BoolValue = proto.Field(
        proto.MESSAGE,
        number=7,
        message=wrappers_pb2.BoolValue,
    )
    transaction_log_retention_days: wrappers_pb2.Int32Value = proto.Field(
        proto.MESSAGE,
        number=9,
        message=wrappers_pb2.Int32Value,
    )
    backup_retention_settings: "BackupRetentionSettings" = proto.Field(
        proto.MESSAGE,
        number=10,
        message="BackupRetentionSettings",
    )
    transactional_log_storage_state: TransactionalLogStorageState = proto.Field(
        proto.ENUM,
        number=11,
        optional=True,
        enum=TransactionalLogStorageState,
    )
    backup_tier: BackupTier = proto.Field(
        proto.ENUM,
        number=12,
        optional=True,
        enum=BackupTier,
    )


class BackupRun(proto.Message):
    r"""A BackupRun resource.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        kind (str):
            This is always ``sql#backupRun``.
        status (google.cloud.sqladmin_v1beta4.types.SqlBackupRunStatus):
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
        error (google.cloud.sqladmin_v1beta4.types.OperationError):
            Information about why the backup operation
            failed. This is only present if the run has the
            FAILED status.
        type_ (google.cloud.sqladmin_v1beta4.types.SqlBackupRunType):
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
        database_version (google.cloud.sqladmin_v1beta4.types.SqlDatabaseVersion):
            Output only. The instance database version at
            the time this backup was made.
        disk_encryption_configuration (google.cloud.sqladmin_v1beta4.types.DiskEncryptionConfiguration):
            Encryption configuration specific to a
            backup.
        disk_encryption_status (google.cloud.sqladmin_v1beta4.types.DiskEncryptionStatus):
            Encryption status specific to a backup.
        backup_kind (google.cloud.sqladmin_v1beta4.types.SqlBackupKind):
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
    error: "OperationError" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="OperationError",
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
    database_version: "SqlDatabaseVersion" = proto.Field(
        proto.ENUM,
        number=15,
        enum="SqlDatabaseVersion",
    )
    disk_encryption_configuration: "DiskEncryptionConfiguration" = proto.Field(
        proto.MESSAGE,
        number=16,
        message="DiskEncryptionConfiguration",
    )
    disk_encryption_status: "DiskEncryptionStatus" = proto.Field(
        proto.MESSAGE,
        number=17,
        message="DiskEncryptionStatus",
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
        type_ (google.cloud.sqladmin_v1beta4.types.Backup.SqlBackupType):
            Output only. The type of this backup. The type can be
            "AUTOMATED", "ON_DEMAND", or “FINAL”.
        description (str):
            The description of this backup.
        instance (str):
            The name of the database instance.
        location (str):
            The storage location of the backups. The
            location can be multi-regional.
        backup_interval (google.type.interval_pb2.Interval):
            Output only. This output contains the following values:
            start_time: All database writes up to this time are
            available. end_time: Any database writes after this time
            aren't available.
        state (google.cloud.sqladmin_v1beta4.types.Backup.SqlBackupState):
            Output only. The state of this backup.
        error (google.cloud.sqladmin_v1beta4.types.OperationError):
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
        backup_kind (google.cloud.sqladmin_v1beta4.types.SqlBackupKind):
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
            A UTC timestamp of when this resource expired.

            This field is a member of `oneof`_ ``expiration``.
        database_version (google.cloud.sqladmin_v1beta4.types.SqlDatabaseVersion):
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
        instance_settings (google.cloud.sqladmin_v1beta4.types.DatabaseInstance):
            Optional. Output only. Instance setting of
            the source instance that's associated with this
            backup.
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
                The backup that's created when the instance
                is deleted.
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
    error: "OperationError" = proto.Field(
        proto.MESSAGE,
        number=10,
        message="OperationError",
    )
    kms_key: str = proto.Field(
        proto.STRING,
        number=11,
    )
    kms_key_version: str = proto.Field(
        proto.STRING,
        number=12,
    )
    backup_kind: "SqlBackupKind" = proto.Field(
        proto.ENUM,
        number=13,
        enum="SqlBackupKind",
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
    database_version: "SqlDatabaseVersion" = proto.Field(
        proto.ENUM,
        number=20,
        enum="SqlDatabaseVersion",
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
    instance_settings: "DatabaseInstance" = proto.Field(
        proto.MESSAGE,
        number=25,
        message="DatabaseInstance",
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


class BackupRunsListResponse(proto.Message):
    r"""Backup run list results.

    Attributes:
        kind (str):
            This is always ``sql#backupRunsList``.
        items (MutableSequence[google.cloud.sqladmin_v1beta4.types.BackupRun]):
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


class BackupContext(proto.Message):
    r"""Backup context.

    Attributes:
        backup_id (int):
            The identifier of the backup.
        kind (str):
            This is always ``sql#backupContext``.
        name (str):
            The name of the backup.
            Format: projects/{project}/backups/{backup}
    """

    backup_id: int = proto.Field(
        proto.INT64,
        number=1,
    )
    kind: str = proto.Field(
        proto.STRING,
        number=2,
    )
    name: str = proto.Field(
        proto.STRING,
        number=3,
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
            Name of the Cloud SQL instance to be created
            as a clone.
        bin_log_coordinates (google.cloud.sqladmin_v1beta4.types.BinLogCoordinates):
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
            primary zone as the source instance.

            This field is a member of `oneof`_ ``_preferred_zone``.
        preferred_secondary_zone (str):
            Optional. Copy clone and point-in-time recovery clone of a
            regional instance in the specified zones. If not specified,
            clone to the same secondary zone as the source instance.
            This value cannot be the same as the preferred_zone field.

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


class Database(proto.Message):
    r"""Represents a SQL database on the Cloud SQL instance.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        kind (str):
            This is always ``sql#database``.
        charset (str):
            The Cloud SQL charset value.
        collation (str):
            The Cloud SQL collation value.
        etag (str):
            This field is deprecated and will be removed
            from a future version of the API.
        name (str):
            The name of the database in the Cloud SQL
            instance. This does not include the project ID
            or instance name.
        instance (str):
            The name of the Cloud SQL instance. This does
            not include the project ID.
        self_link (str):
            The URI of this resource.
        project (str):
            The project ID of the project containing the
            Cloud SQL database. The Google apps domain is
            prefixed if applicable.
        sqlserver_database_details (google.cloud.sqladmin_v1beta4.types.SqlServerDatabaseDetails):

            This field is a member of `oneof`_ ``database_details``.
    """

    kind: str = proto.Field(
        proto.STRING,
        number=1,
    )
    charset: str = proto.Field(
        proto.STRING,
        number=2,
    )
    collation: str = proto.Field(
        proto.STRING,
        number=3,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=4,
    )
    name: str = proto.Field(
        proto.STRING,
        number=5,
    )
    instance: str = proto.Field(
        proto.STRING,
        number=6,
    )
    self_link: str = proto.Field(
        proto.STRING,
        number=7,
    )
    project: str = proto.Field(
        proto.STRING,
        number=8,
    )
    sqlserver_database_details: "SqlServerDatabaseDetails" = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="database_details",
        message="SqlServerDatabaseDetails",
    )


class SqlServerDatabaseDetails(proto.Message):
    r"""Represents a Sql Server database on the Cloud SQL instance.

    Attributes:
        compatibility_level (int):
            The version of SQL Server with which the
            database is to be made compatible
        recovery_model (str):
            The recovery model of a SQL Server database
    """

    compatibility_level: int = proto.Field(
        proto.INT32,
        number=1,
    )
    recovery_model: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DatabaseFlags(proto.Message):
    r"""Database flags for Cloud SQL instances.

    Attributes:
        name (str):
            The name of the flag. These flags are passed at instance
            startup, so include both server options and system
            variables. Flags are specified with underscores, not
            hyphens. For more information, see `Configuring Database
            Flags <https://cloud.google.com/sql/docs/mysql/flags>`__ in
            the Cloud SQL documentation.
        value (str):
            The value of the flag. Boolean flags are set to ``on`` for
            true and ``off`` for false. This field must be omitted if
            the flag doesn't take a value.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    value: str = proto.Field(
        proto.STRING,
        number=2,
    )


class SyncFlags(proto.Message):
    r"""Initial sync flags for certain Cloud SQL APIs.
    Currently used for the MySQL external server initial dump.

    Attributes:
        name (str):
            The name of the flag.
        value (str):
            The value of the flag. This field must be
            omitted if the flag doesn't take a value.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    value: str = proto.Field(
        proto.STRING,
        number=2,
    )


class InstanceReference(proto.Message):
    r"""Reference to another Cloud SQL instance.

    Attributes:
        name (str):
            The name of the Cloud SQL instance being
            referenced. This does not include the project
            ID.
        region (str):
            The region of the Cloud SQL instance being
            referenced.
        project (str):
            The project ID of the Cloud SQL instance
            being referenced. The default is the same
            project ID as the instance references it.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    region: str = proto.Field(
        proto.STRING,
        number=2,
    )
    project: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DatabaseInstance(proto.Message):
    r"""A Cloud SQL instance resource.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        kind (str):
            This is always ``sql#instance``.
        state (google.cloud.sqladmin_v1beta4.types.DatabaseInstance.SqlInstanceState):
            The current serving state of the Cloud SQL
            instance.
        database_version (google.cloud.sqladmin_v1beta4.types.SqlDatabaseVersion):
            The database engine type and version. The
            ``databaseVersion`` field cannot be changed after instance
            creation.
        settings (google.cloud.sqladmin_v1beta4.types.Settings):
            The user settings.
        etag (str):
            This field is deprecated and will be removed from a future
            version of the API. Use the ``settings.settingsVersion``
            field instead.
        failover_replica (google.cloud.sqladmin_v1beta4.types.DatabaseInstance.SqlFailoverReplica):
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
        ip_addresses (MutableSequence[google.cloud.sqladmin_v1beta4.types.IpMapping]):
            The assigned IP addresses for the instance.
        server_ca_cert (google.cloud.sqladmin_v1beta4.types.SslCert):
            SSL configuration.
        instance_type (google.cloud.sqladmin_v1beta4.types.SqlInstanceType):
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
            the instance. \This property is read-only.
        on_premises_configuration (google.cloud.sqladmin_v1beta4.types.OnPremisesConfiguration):
            Configuration specific to on-premises
            instances.
        replica_configuration (google.cloud.sqladmin_v1beta4.types.ReplicaConfiguration):
            Configuration specific to failover replicas
            and read replicas.
        backend_type (google.cloud.sqladmin_v1beta4.types.SqlBackendType):
            The backend type. ``SECOND_GEN``: Cloud SQL database
            instance. ``EXTERNAL``: A database server that is not
            managed by Google.

            This property is read-only; use the ``tier`` property in the
            ``settings`` object to determine the database type.
        self_link (str):
            The URI of this resource.
        suspension_reason (MutableSequence[google.cloud.sqladmin_v1beta4.types.SqlSuspensionReason]):
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
        disk_encryption_configuration (google.cloud.sqladmin_v1beta4.types.DiskEncryptionConfiguration):
            Disk encryption configuration specific to an
            instance.
        disk_encryption_status (google.cloud.sqladmin_v1beta4.types.DiskEncryptionStatus):
            Disk encryption status specific to an
            instance.
        root_password (str):
            Initial root password. Use only on creation.
            You must set root passwords before you can
            connect to PostgreSQL instances.
        scheduled_maintenance (google.cloud.sqladmin_v1beta4.types.DatabaseInstance.SqlScheduledMaintenance):
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
        out_of_disk_report (google.cloud.sqladmin_v1beta4.types.DatabaseInstance.SqlOutOfDiskReport):
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
        upgradable_database_versions (MutableSequence[google.cloud.sqladmin_v1beta4.types.AvailableDatabaseVersion]):
            Output only. All database versions that are
            available for upgrade.
        sql_network_architecture (google.cloud.sqladmin_v1beta4.types.DatabaseInstance.SqlNetworkArchitecture):
            The SQL network architecture for the
            instance.

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
        replication_cluster (google.cloud.sqladmin_v1beta4.types.ReplicationCluster):
            A primary instance and disaster recovery (DR)
            replica pair. A DR replica is a cross-region
            replica that you designate for failover in the
            event that the primary instance experiences
            regional failure.
            Applicable to MySQL and PostgreSQL.

            This field is a member of `oneof`_ ``_replication_cluster``.
        gemini_config (google.cloud.sqladmin_v1beta4.types.GeminiInstanceConfig):
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
        nodes (MutableSequence[google.cloud.sqladmin_v1beta4.types.DatabaseInstance.PoolNodeConfig]):
            Output only. Entries containing information
            about each read pool node of the read pool.
        dns_names (MutableSequence[google.cloud.sqladmin_v1beta4.types.DnsNameMapping]):
            Output only. The list of DNS names used by
            this instance.
        deployment_info (google.cloud.sqladmin_v1beta4.types.BlueGreenDeploymentInfo):
            Output only. Deployment info for the
            instance. This is set if the instance is
            currently part of any blue-green setup.

            This field is a member of `oneof`_ ``_deployment_info``.
        database_center_integration_enabled (google.protobuf.wrappers_pb2.BoolValue):
            Optional. If true, instance metadata is sent
            to the Database Center. If false, instance
            metadata is not sent to the Database Center.
        database_center_integration (google.cloud.sqladmin_v1beta4.types.DatabaseInstance.DatabaseCenterIntegration):
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
            sql_out_of_disk_state (google.cloud.sqladmin_v1beta4.types.DatabaseInstance.SqlOutOfDiskReport.SqlOutOfDiskState):
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
            ip_addresses (MutableSequence[google.cloud.sqladmin_v1beta4.types.IpMapping]):
                Output only. Mappings containing IP addresses
                that can be used to connect to the read pool
                node.
            dns_name (str):
                Output only. The DNS name of the read pool
                node.

                This field is a member of `oneof`_ ``_dns_name``.
            state (google.cloud.sqladmin_v1beta4.types.DatabaseInstance.SqlInstanceState):
                Output only. The current state of the read
                pool node.

                This field is a member of `oneof`_ ``_state``.
            dns_names (MutableSequence[google.cloud.sqladmin_v1beta4.types.DnsNameMapping]):
                Output only. The list of DNS names used by
                this read pool node.
            psc_service_attachment_link (str):
                Output only. The Private Service Connect
                (PSC) service attachment of the read pool node.

                This field is a member of `oneof`_ ``_psc_service_attachment_link``.
            psc_auto_connections (MutableSequence[google.cloud.sqladmin_v1beta4.types.PscAutoConnectionConfig]):
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
        ip_addresses: MutableSequence["IpMapping"] = proto.RepeatedField(
            proto.MESSAGE,
            number=3,
            message="IpMapping",
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
        dns_names: MutableSequence["DnsNameMapping"] = proto.RepeatedField(
            proto.MESSAGE,
            number=6,
            message="DnsNameMapping",
        )
        psc_service_attachment_link: str = proto.Field(
            proto.STRING,
            number=7,
            optional=True,
        )
        psc_auto_connections: MutableSequence["PscAutoConnectionConfig"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=8,
                message="PscAutoConnectionConfig",
            )
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
    database_version: "SqlDatabaseVersion" = proto.Field(
        proto.ENUM,
        number=3,
        enum="SqlDatabaseVersion",
    )
    settings: "Settings" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="Settings",
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
    ip_addresses: MutableSequence["IpMapping"] = proto.RepeatedField(
        proto.MESSAGE,
        number=11,
        message="IpMapping",
    )
    server_ca_cert: "SslCert" = proto.Field(
        proto.MESSAGE,
        number=12,
        message="SslCert",
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
    backend_type: "SqlBackendType" = proto.Field(
        proto.ENUM,
        number=19,
        enum="SqlBackendType",
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
    disk_encryption_configuration: "DiskEncryptionConfiguration" = proto.Field(
        proto.MESSAGE,
        number=26,
        message="DiskEncryptionConfiguration",
    )
    disk_encryption_status: "DiskEncryptionStatus" = proto.Field(
        proto.MESSAGE,
        number=27,
        message="DiskEncryptionStatus",
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
        optional=True,
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
    dns_names: MutableSequence["DnsNameMapping"] = proto.RepeatedField(
        proto.MESSAGE,
        number=67,
        message="DnsNameMapping",
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
        source (google.cloud.sqladmin_v1beta4.types.BlueGreenDeploymentInfo.SourceRole):
            Output only. The source instance for the
            Blue-Green deployment.

            This field is a member of `oneof`_ ``role_details``.
        target (google.cloud.sqladmin_v1beta4.types.BlueGreenDeploymentInfo.TargetRole):
            Output only. The target instance for the
            Blue-Green deployment.

            This field is a member of `oneof`_ ``role_details``.
        state (google.cloud.sqladmin_v1beta4.types.BlueGreenDeploymentInfo.State):
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
            target_id (google.cloud.sqladmin_v1beta4.types.InstanceReference):
                Output only. The target instance paired with
                this source instance in a blue-green deployment.

                This field is a member of `oneof`_ ``_target_id``.
        """

        target_id: "InstanceReference" = proto.Field(
            proto.MESSAGE,
            number=1,
            optional=True,
            message="InstanceReference",
        )

    class TargetRole(proto.Message):
        r"""The target instance for the Blue-Green deployment.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            source_id (google.cloud.sqladmin_v1beta4.types.InstanceReference):
                Output only. The source instance paired with
                this target instance in a blue-green deployment.

                This field is a member of `oneof`_ ``_source_id``.
        """

        source_id: "InstanceReference" = proto.Field(
            proto.MESSAGE,
            number=1,
            optional=True,
            message="InstanceReference",
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


class DnsNameMapping(proto.Message):
    r"""DNS metadata.

    Attributes:
        name (str):
            Output only. The DNS name.
        connection_type (google.cloud.sqladmin_v1beta4.types.DnsNameMapping.ConnectionType):
            Output only. The connection type of the DNS
            name.
        dns_scope (google.cloud.sqladmin_v1beta4.types.DnsNameMapping.DnsScope):
            Output only. The scope that the DNS name
            applies to.
        record_manager (google.cloud.sqladmin_v1beta4.types.DnsNameMapping.RecordManager):
            Output only. The manager for this DNS record.
    """

    class ConnectionType(proto.Enum):
        r"""The connection type of the DNS name.

        Values:
            CONNECTION_TYPE_UNSPECIFIED (0):
                Unknown connection type.
            PUBLIC (1):
                Public IP.
            PRIVATE_SERVICES_ACCESS (2):
                Private services access (private IP).
            PRIVATE_SERVICE_CONNECT (3):
                Private Service Connect.
        """

        CONNECTION_TYPE_UNSPECIFIED = 0
        PUBLIC = 1
        PRIVATE_SERVICES_ACCESS = 2
        PRIVATE_SERVICE_CONNECT = 3

    class DnsScope(proto.Enum):
        r"""The scope that the DNS name applies to.

        Values:
            DNS_SCOPE_UNSPECIFIED (0):
                DNS scope not set. This value should not be
                used.
            INSTANCE (1):
                Indicates an instance-level DNS name.
            CLUSTER (2):
                Indicates a cluster-level DNS name.
        """

        DNS_SCOPE_UNSPECIFIED = 0
        INSTANCE = 1
        CLUSTER = 2

    class RecordManager(proto.Enum):
        r"""The system responsible for managing the DNS record.

        Values:
            RECORD_MANAGER_UNSPECIFIED (0):
                Record manager not set. This value should not
                be used.
            CUSTOMER (1):
                The record may be managed by the customer. It
                is not automatically managed by Cloud SQL
                automation.
            CLOUD_SQL_AUTOMATION (2):
                The record is managed by Cloud SQL, which
                will create, update, and delete the DNS records
                for the zone automatically when the Cloud SQL
                database instance is created or updated.
        """

        RECORD_MANAGER_UNSPECIFIED = 0
        CUSTOMER = 1
        CLOUD_SQL_AUTOMATION = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    connection_type: ConnectionType = proto.Field(
        proto.ENUM,
        number=2,
        enum=ConnectionType,
    )
    dns_scope: DnsScope = proto.Field(
        proto.ENUM,
        number=3,
        enum=DnsScope,
    )
    record_manager: RecordManager = proto.Field(
        proto.ENUM,
        number=4,
        enum=RecordManager,
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
    failover in the event that the primary instance has regional
    failure. Applicable to MySQL and PostgreSQL.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

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

            This field is a member of `oneof`_ ``_psa_write_endpoint``.
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

            This field is a member of `oneof`_ ``_failover_dr_replica_name``.
        dr_replica (bool):
            Output only. Read-only field that indicates
            whether the replica is a DR replica. This field
            is not set if the instance is a primary
            instance.

            This field is a member of `oneof`_ ``_dr_replica``.
    """

    psa_write_endpoint: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    failover_dr_replica_name: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    dr_replica: bool = proto.Field(
        proto.BOOL,
        number=4,
        optional=True,
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


class DatabasesListResponse(proto.Message):
    r"""Database list response.

    Attributes:
        kind (str):
            This is always ``sql#databasesList``.
        items (MutableSequence[google.cloud.sqladmin_v1beta4.types.Database]):
            List of database resources in the instance.
    """

    kind: str = proto.Field(
        proto.STRING,
        number=1,
    )
    items: MutableSequence["Database"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="Database",
    )


class DemoteMasterConfiguration(proto.Message):
    r"""Read-replica configuration for connecting to the on-premises
    primary instance.

    Attributes:
        kind (str):
            This is always ``sql#demoteMasterConfiguration``.
        mysql_replica_configuration (google.cloud.sqladmin_v1beta4.types.DemoteMasterMySqlReplicaConfiguration):
            MySQL specific configuration when replicating from a MySQL
            on-premises primary instance. Replication configuration
            information such as the username, password, certificates,
            and keys are not stored in the instance metadata. The
            configuration information is used only to set up the
            replication connection and is stored by MySQL in a file
            named ``master.info`` in the data directory.
    """

    kind: str = proto.Field(
        proto.STRING,
        number=1,
    )
    mysql_replica_configuration: "DemoteMasterMySqlReplicaConfiguration" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="DemoteMasterMySqlReplicaConfiguration",
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
        replica_configuration (google.cloud.sqladmin_v1beta4.types.DemoteMasterConfiguration):
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
    replica_configuration: "DemoteMasterConfiguration" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="DemoteMasterConfiguration",
    )
    skip_replication_setup: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class DemoteMasterMySqlReplicaConfiguration(proto.Message):
    r"""Read-replica configuration specific to MySQL databases.

    Attributes:
        kind (str):
            This is always
            ``sql#demoteMasterMysqlReplicaConfiguration``.
        username (str):
            The username for the replication connection.
        password (str):
            The password for the replication connection.
        client_key (str):
            PEM representation of the replica's private
            key. The corresponding public key is encoded in
            the client's certificate. The format of the
            replica's private key can be either PKCS #1 or
            PKCS #8.
        client_certificate (str):
            PEM representation of the replica's x509
            certificate.
        ca_certificate (str):
            PEM representation of the trusted CA's x509
            certificate.
    """

    kind: str = proto.Field(
        proto.STRING,
        number=1,
    )
    username: str = proto.Field(
        proto.STRING,
        number=2,
    )
    password: str = proto.Field(
        proto.STRING,
        number=3,
    )
    client_key: str = proto.Field(
        proto.STRING,
        number=4,
    )
    client_certificate: str = proto.Field(
        proto.STRING,
        number=5,
    )
    ca_certificate: str = proto.Field(
        proto.STRING,
        number=6,
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
            as an on-premises primary instance in the
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


class ExportContext(proto.Message):
    r"""Database instance export context.

    Attributes:
        uri (str):
            The path to the file in Google Cloud Storage where the
            export will be stored. The URI is in the form
            ``gs://bucketName/fileName``. If the file already exists,
            the request succeeds, but the operation fails. If
            ``fileType`` is ``SQL`` and the filename ends with .gz, the
            contents are compressed.
        databases (MutableSequence[str]):
            Databases to be exported. ``MySQL instances:`` If
            ``fileType`` is ``SQL`` and no database is specified, all
            databases are exported, except for the ``mysql`` system
            database. If ``fileType`` is ``CSV``, you can specify one
            database, either by using this property or by using the
            ``csvExportOptions.selectQuery`` property, which takes
            precedence over this property. ``PostgreSQL instances:`` If
            you don't specify a database by name, all user databases in
            the instance are exported. This excludes system databases
            and Cloud SQL databases used to manage internal operations.
            Exporting all user databases is only available for
            directory-formatted parallel export. If ``fileType`` is
            ``CSV``, this database must match the one specified in the
            ``csvExportOptions.selectQuery`` property.
            ``SQL Server instances:`` You must specify one database to
            be exported, and the ``fileType`` must be ``BAK``.
        kind (str):
            This is always ``sql#exportContext``.
        sql_export_options (google.cloud.sqladmin_v1beta4.types.ExportContext.SqlExportOptions):
            Options for exporting data as SQL statements.
        csv_export_options (google.cloud.sqladmin_v1beta4.types.ExportContext.SqlCsvExportOptions):
            Options for exporting data as CSV. ``MySQL`` and
            ``PostgreSQL`` instances only.
        file_type (google.cloud.sqladmin_v1beta4.types.SqlFileType):
            The file type for the specified uri.
        offload (google.protobuf.wrappers_pb2.BoolValue):
            Whether to perform a serverless export.
        bak_export_options (google.cloud.sqladmin_v1beta4.types.ExportContext.SqlBakExportOptions):
            Options for exporting data as BAK files.
        tde_export_options (google.cloud.sqladmin_v1beta4.types.ExportContext.SqlTdeExportOptions):
            Optional. Export parameters specific to SQL
            Server TDE certificates
    """

    class SqlCsvExportOptions(proto.Message):
        r"""

        Attributes:
            select_query (str):
                The select query used to extract the data.
            escape_character (str):
                Specifies the character that should appear
                before a data character that needs to be
                escaped.
            quote_character (str):
                Specifies the quoting character to be used
                when a data value is quoted.
            fields_terminated_by (str):
                Specifies the character that separates
                columns within each row (line) of the file.
            lines_terminated_by (str):
                This is used to separate lines. If a line
                does not contain all fields, the rest of the
                columns are set to their default values.
        """

        select_query: str = proto.Field(
            proto.STRING,
            number=1,
        )
        escape_character: str = proto.Field(
            proto.STRING,
            number=2,
        )
        quote_character: str = proto.Field(
            proto.STRING,
            number=3,
        )
        fields_terminated_by: str = proto.Field(
            proto.STRING,
            number=4,
        )
        lines_terminated_by: str = proto.Field(
            proto.STRING,
            number=6,
        )

    class SqlExportOptions(proto.Message):
        r"""

        Attributes:
            tables (MutableSequence[str]):
                Tables to export, or that were exported, from
                the specified database. If you specify tables,
                specify one and only one database. For
                PostgreSQL instances, you can specify only one
                table.
            schema_only (google.protobuf.wrappers_pb2.BoolValue):
                Export only schemas.
            mysql_export_options (google.cloud.sqladmin_v1beta4.types.ExportContext.SqlExportOptions.MysqlExportOptions):

            threads (google.protobuf.wrappers_pb2.Int32Value):
                Optional. The number of threads to use for
                parallel export.
            parallel (google.protobuf.wrappers_pb2.BoolValue):
                Optional. Whether or not the export should be
                parallel.
            postgres_export_options (google.cloud.sqladmin_v1beta4.types.ExportContext.SqlExportOptions.PostgresExportOptions):
                Optional. Options for exporting from a Cloud
                SQL for PostgreSQL instance.
        """

        class MysqlExportOptions(proto.Message):
            r"""Options for exporting from MySQL.

            Attributes:
                master_data (google.protobuf.wrappers_pb2.Int32Value):
                    Option to include SQL statement required to set up
                    replication. If set to ``1``, the dump file includes a
                    CHANGE MASTER TO statement with the binary log coordinates,
                    and --set-gtid-purged is set to ON. If set to ``2``, the
                    CHANGE MASTER TO statement is written as a SQL comment and
                    has no effect. If set to any value other than ``1``,
                    --set-gtid-purged is set to OFF.
            """

            master_data: wrappers_pb2.Int32Value = proto.Field(
                proto.MESSAGE,
                number=1,
                message=wrappers_pb2.Int32Value,
            )

        class PostgresExportOptions(proto.Message):
            r"""Options for exporting from a Cloud SQL for PostgreSQL
            instance.

            Attributes:
                clean (google.protobuf.wrappers_pb2.BoolValue):
                    Optional. Use this option to include DROP
                    <code>&lt;object&gt;</code> SQL statements. Use
                    these statements to delete database objects
                    before running the import operation.
                if_exists (google.protobuf.wrappers_pb2.BoolValue):
                    Optional. Option to include an IF EXISTS SQL
                    statement with each DROP statement produced by
                    clean.
            """

            clean: wrappers_pb2.BoolValue = proto.Field(
                proto.MESSAGE,
                number=1,
                message=wrappers_pb2.BoolValue,
            )
            if_exists: wrappers_pb2.BoolValue = proto.Field(
                proto.MESSAGE,
                number=2,
                message=wrappers_pb2.BoolValue,
            )

        tables: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )
        schema_only: wrappers_pb2.BoolValue = proto.Field(
            proto.MESSAGE,
            number=2,
            message=wrappers_pb2.BoolValue,
        )
        mysql_export_options: "ExportContext.SqlExportOptions.MysqlExportOptions" = (
            proto.Field(
                proto.MESSAGE,
                number=3,
                message="ExportContext.SqlExportOptions.MysqlExportOptions",
            )
        )
        threads: wrappers_pb2.Int32Value = proto.Field(
            proto.MESSAGE,
            number=4,
            message=wrappers_pb2.Int32Value,
        )
        parallel: wrappers_pb2.BoolValue = proto.Field(
            proto.MESSAGE,
            number=5,
            message=wrappers_pb2.BoolValue,
        )
        postgres_export_options: "ExportContext.SqlExportOptions.PostgresExportOptions" = proto.Field(
            proto.MESSAGE,
            number=6,
            message="ExportContext.SqlExportOptions.PostgresExportOptions",
        )

    class SqlBakExportOptions(proto.Message):
        r"""Options for exporting BAK files (SQL Server-only)

        Attributes:
            striped (google.protobuf.wrappers_pb2.BoolValue):
                Whether or not the export should be striped.
            stripe_count (google.protobuf.wrappers_pb2.Int32Value):
                Option for specifying how many stripes to use
                for the export. If blank, and the value of the
                striped field is true, the number of stripes is
                automatically chosen.
            bak_type (google.cloud.sqladmin_v1beta4.types.BakType):
                Type of this bak file will be export, FULL or
                DIFF, SQL Server only
            copy_only (google.protobuf.wrappers_pb2.BoolValue):
                Deprecated: copy_only is deprecated. Use differential_base
                instead
            differential_base (google.protobuf.wrappers_pb2.BoolValue):
                Whether or not the backup can be used as a differential base
                copy_only backup can not be served as differential base
            export_log_start_time (google.protobuf.timestamp_pb2.Timestamp):
                Optional. The begin timestamp when transaction log will be
                included in the export operation. `RFC
                3339 <https://tools.ietf.org/html/rfc3339>`__ format (for
                example, ``2023-10-01T16:19:00.094``) in UTC. When omitted,
                all available logs from the beginning of retention period
                will be included. Only applied to Cloud SQL for SQL Server.
            export_log_end_time (google.protobuf.timestamp_pb2.Timestamp):
                Optional. The end timestamp when transaction log will be
                included in the export operation. `RFC
                3339 <https://tools.ietf.org/html/rfc3339>`__ format (for
                example, ``2023-10-01T16:19:00.094``) in UTC. When omitted,
                all available logs until current time will be included. Only
                applied to Cloud SQL for SQL Server.
        """

        striped: wrappers_pb2.BoolValue = proto.Field(
            proto.MESSAGE,
            number=1,
            message=wrappers_pb2.BoolValue,
        )
        stripe_count: wrappers_pb2.Int32Value = proto.Field(
            proto.MESSAGE,
            number=2,
            message=wrappers_pb2.Int32Value,
        )
        bak_type: "BakType" = proto.Field(
            proto.ENUM,
            number=4,
            enum="BakType",
        )
        copy_only: wrappers_pb2.BoolValue = proto.Field(
            proto.MESSAGE,
            number=5,
            message=wrappers_pb2.BoolValue,
        )
        differential_base: wrappers_pb2.BoolValue = proto.Field(
            proto.MESSAGE,
            number=6,
            message=wrappers_pb2.BoolValue,
        )
        export_log_start_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=7,
            message=timestamp_pb2.Timestamp,
        )
        export_log_end_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=8,
            message=timestamp_pb2.Timestamp,
        )

    class SqlTdeExportOptions(proto.Message):
        r"""

        Attributes:
            certificate_path (str):
                Required. Path to the TDE certificate public
                key in the form gs://bucketName/fileName.
                The instance must have write access to the
                location. Applicable only for SQL Server
                instances.
            private_key_path (str):
                Required. Path to the TDE certificate private
                key in the form gs://bucketName/fileName.
                The instance must have write access to the
                location. Applicable only for SQL Server
                instances.
            private_key_password (str):
                Required. Password that encrypts the private
                key.
            name (str):
                Required. Certificate name.
                Applicable only for SQL Server instances.
        """

        certificate_path: str = proto.Field(
            proto.STRING,
            number=1,
        )
        private_key_path: str = proto.Field(
            proto.STRING,
            number=2,
        )
        private_key_password: str = proto.Field(
            proto.STRING,
            number=3,
        )
        name: str = proto.Field(
            proto.STRING,
            number=5,
        )

    uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    databases: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    kind: str = proto.Field(
        proto.STRING,
        number=3,
    )
    sql_export_options: SqlExportOptions = proto.Field(
        proto.MESSAGE,
        number=4,
        message=SqlExportOptions,
    )
    csv_export_options: SqlCsvExportOptions = proto.Field(
        proto.MESSAGE,
        number=5,
        message=SqlCsvExportOptions,
    )
    file_type: "SqlFileType" = proto.Field(
        proto.ENUM,
        number=6,
        enum="SqlFileType",
    )
    offload: wrappers_pb2.BoolValue = proto.Field(
        proto.MESSAGE,
        number=8,
        message=wrappers_pb2.BoolValue,
    )
    bak_export_options: SqlBakExportOptions = proto.Field(
        proto.MESSAGE,
        number=9,
        message=SqlBakExportOptions,
    )
    tde_export_options: SqlTdeExportOptions = proto.Field(
        proto.MESSAGE,
        number=10,
        message=SqlTdeExportOptions,
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


class Flag(proto.Message):
    r"""A flag resource.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            This is the name of the flag. Flag names always use
            underscores, not hyphens, for example:
            ``max_allowed_packet``
        type_ (google.cloud.sqladmin_v1beta4.types.SqlFlagType):
            The type of the flag. Flags are typed to being ``BOOLEAN``,
            ``STRING``, ``INTEGER`` or ``NONE``. ``NONE`` is used for
            flags which do not take a value, such as
            ``skip_grant_tables``.
        applies_to (MutableSequence[google.cloud.sqladmin_v1beta4.types.SqlDatabaseVersion]):
            The database version this flag applies to. Can be MySQL
            instances: ``MYSQL_8_0``, ``MYSQL_8_0_18``,
            ``MYSQL_8_0_26``, ``MYSQL_5_7``, or ``MYSQL_5_6``.
            PostgreSQL instances: ``POSTGRES_9_6``, ``POSTGRES_10``,
            ``POSTGRES_11`` or ``POSTGRES_12``. SQL Server instances:
            ``SQLSERVER_2017_STANDARD``, ``SQLSERVER_2017_ENTERPRISE``,
            ``SQLSERVER_2017_EXPRESS``, ``SQLSERVER_2017_WEB``,
            ``SQLSERVER_2019_STANDARD``, ``SQLSERVER_2019_ENTERPRISE``,
            ``SQLSERVER_2019_EXPRESS``, or ``SQLSERVER_2019_WEB``. See
            `the complete
            list </sql/docs/mysql/admin-api/rest/v1/SqlDatabaseVersion>`__.
        allowed_string_values (MutableSequence[str]):
            For ``STRING`` flags, a list of strings that the value can
            be set to.
        min_value (google.protobuf.wrappers_pb2.Int64Value):
            For ``INTEGER`` flags, the minimum allowed value.
        max_value (google.protobuf.wrappers_pb2.Int64Value):
            For ``INTEGER`` flags, the maximum allowed value.
        requires_restart (google.protobuf.wrappers_pb2.BoolValue):
            Indicates whether changing this flag will
            trigger a database restart. Only applicable to
            Second Generation instances.
        kind (str):
            This is always ``sql#flag``.
        in_beta (google.protobuf.wrappers_pb2.BoolValue):
            Whether or not the flag is considered in
            beta.
        allowed_int_values (MutableSequence[int]):
            Use this field if only certain integers are accepted. Can be
            combined with min_value and max_value to add additional
            values.
        flag_scope (google.cloud.sqladmin_v1beta4.types.SqlFlagScope):
            Scope of flag.
        recommended_string_value (str):
            Recommended flag value in string format for
            UI display.

            This field is a member of `oneof`_ ``recommended_value``.
        recommended_int_value (google.protobuf.wrappers_pb2.Int64Value):
            Recommended flag value in integer format for
            UI display.

            This field is a member of `oneof`_ ``recommended_value``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    type_: "SqlFlagType" = proto.Field(
        proto.ENUM,
        number=2,
        enum="SqlFlagType",
    )
    applies_to: MutableSequence["SqlDatabaseVersion"] = proto.RepeatedField(
        proto.ENUM,
        number=3,
        enum="SqlDatabaseVersion",
    )
    allowed_string_values: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    min_value: wrappers_pb2.Int64Value = proto.Field(
        proto.MESSAGE,
        number=5,
        message=wrappers_pb2.Int64Value,
    )
    max_value: wrappers_pb2.Int64Value = proto.Field(
        proto.MESSAGE,
        number=6,
        message=wrappers_pb2.Int64Value,
    )
    requires_restart: wrappers_pb2.BoolValue = proto.Field(
        proto.MESSAGE,
        number=7,
        message=wrappers_pb2.BoolValue,
    )
    kind: str = proto.Field(
        proto.STRING,
        number=8,
    )
    in_beta: wrappers_pb2.BoolValue = proto.Field(
        proto.MESSAGE,
        number=9,
        message=wrappers_pb2.BoolValue,
    )
    allowed_int_values: MutableSequence[int] = proto.RepeatedField(
        proto.INT64,
        number=10,
    )
    flag_scope: "SqlFlagScope" = proto.Field(
        proto.ENUM,
        number=15,
        enum="SqlFlagScope",
    )
    recommended_string_value: str = proto.Field(
        proto.STRING,
        number=16,
        oneof="recommended_value",
    )
    recommended_int_value: wrappers_pb2.Int64Value = proto.Field(
        proto.MESSAGE,
        number=17,
        oneof="recommended_value",
        message=wrappers_pb2.Int64Value,
    )


class FlagsListResponse(proto.Message):
    r"""Flags list response.

    Attributes:
        kind (str):
            This is always ``sql#flagsList``.
        items (MutableSequence[google.cloud.sqladmin_v1beta4.types.Flag]):
            List of flags.
    """

    kind: str = proto.Field(
        proto.STRING,
        number=1,
    )
    items: MutableSequence["Flag"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="Flag",
    )


class ImportContext(proto.Message):
    r"""Database instance import context.

    Attributes:
        uri (str):
            Path to the import file in Cloud Storage, in the form
            ``gs://bucketName/fileName``. Compressed gzip files (.gz)
            are supported when ``fileType`` is ``SQL``. The instance
            must have write permissions to the bucket and read access to
            the file.
        database (str):
            The target database for the import. If ``fileType`` is
            ``SQL``, this field is required only if the import file does
            not specify a database, and is overridden by any database
            specification in the import file. For entire instance
            parallel import operations, the database is overridden by
            the database name stored in subdirectory name. If
            ``fileType`` is ``CSV``, one database must be specified.
        kind (str):
            This is always ``sql#importContext``.
        file_type (google.cloud.sqladmin_v1beta4.types.SqlFileType):
            The file type for the specified uri.

            - ``SQL``: The file contains SQL statements.
            - ``CSV``: The file contains CSV data.
            - ``BAK``: The file contains backup data for a SQL Server
              instance.
        csv_import_options (google.cloud.sqladmin_v1beta4.types.ImportContext.SqlCsvImportOptions):
            Options for importing data as CSV.
        import_user (str):
            The PostgreSQL user for this import
            operation. PostgreSQL instances only.
        bak_import_options (google.cloud.sqladmin_v1beta4.types.ImportContext.SqlBakImportOptions):
            Import parameters specific to SQL Server .BAK
            files
        sql_import_options (google.cloud.sqladmin_v1beta4.types.ImportContext.SqlImportOptions):
            Optional. Options for importing data from SQL
            statements.
        tde_import_options (google.cloud.sqladmin_v1beta4.types.ImportContext.SqlTdeImportOptions):
            Optional. Import parameters specific to SQL
            Server .TDE files Import parameters specific to
            SQL Server TDE certificates
    """

    class SqlImportOptions(proto.Message):
        r"""

        Attributes:
            threads (google.protobuf.wrappers_pb2.Int32Value):
                Optional. The number of threads to use for
                parallel import.
            parallel (google.protobuf.wrappers_pb2.BoolValue):
                Optional. Whether or not the import should be
                parallel.
            postgres_import_options (google.cloud.sqladmin_v1beta4.types.ImportContext.SqlImportOptions.PostgresImportOptions):
                Optional. Options for importing from a Cloud
                SQL for PostgreSQL instance.
        """

        class PostgresImportOptions(proto.Message):
            r"""

            Attributes:
                clean (google.protobuf.wrappers_pb2.BoolValue):
                    Optional. The --clean flag for the pg_restore utility. This
                    flag applies only if you enabled Cloud SQL to import files
                    in parallel.
                if_exists (google.protobuf.wrappers_pb2.BoolValue):
                    Optional. The --if-exists flag for the pg_restore utility.
                    This flag applies only if you enabled Cloud SQL to import
                    files in parallel.
            """

            clean: wrappers_pb2.BoolValue = proto.Field(
                proto.MESSAGE,
                number=1,
                message=wrappers_pb2.BoolValue,
            )
            if_exists: wrappers_pb2.BoolValue = proto.Field(
                proto.MESSAGE,
                number=2,
                message=wrappers_pb2.BoolValue,
            )

        threads: wrappers_pb2.Int32Value = proto.Field(
            proto.MESSAGE,
            number=1,
            message=wrappers_pb2.Int32Value,
        )
        parallel: wrappers_pb2.BoolValue = proto.Field(
            proto.MESSAGE,
            number=2,
            message=wrappers_pb2.BoolValue,
        )
        postgres_import_options: "ImportContext.SqlImportOptions.PostgresImportOptions" = proto.Field(
            proto.MESSAGE,
            number=3,
            message="ImportContext.SqlImportOptions.PostgresImportOptions",
        )

    class SqlCsvImportOptions(proto.Message):
        r"""

        Attributes:
            table (str):
                The table to which CSV data is imported.
            columns (MutableSequence[str]):
                The columns to which CSV data is imported. If
                not specified, all columns of the database table
                are loaded with CSV data.
            escape_character (str):
                Specifies the character that should appear
                before a data character that needs to be
                escaped.
            quote_character (str):
                Specifies the quoting character to be used
                when a data value is quoted.
            fields_terminated_by (str):
                Specifies the character that separates
                columns within each row (line) of the file.
            lines_terminated_by (str):
                This is used to separate lines. If a line
                does not contain all fields, the rest of the
                columns are set to their default values.
        """

        table: str = proto.Field(
            proto.STRING,
            number=1,
        )
        columns: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=2,
        )
        escape_character: str = proto.Field(
            proto.STRING,
            number=4,
        )
        quote_character: str = proto.Field(
            proto.STRING,
            number=5,
        )
        fields_terminated_by: str = proto.Field(
            proto.STRING,
            number=6,
        )
        lines_terminated_by: str = proto.Field(
            proto.STRING,
            number=8,
        )

    class SqlBakImportOptions(proto.Message):
        r"""

        Attributes:
            encryption_options (google.cloud.sqladmin_v1beta4.types.ImportContext.SqlBakImportOptions.EncryptionOptions):

            striped (google.protobuf.wrappers_pb2.BoolValue):
                Whether or not the backup set being restored
                is striped. Applies only to Cloud SQL for SQL
                Server.
            no_recovery (google.protobuf.wrappers_pb2.BoolValue):
                Whether or not the backup importing will
                restore database with NORECOVERY option.
                Applies only to Cloud SQL for SQL Server.
            recovery_only (google.protobuf.wrappers_pb2.BoolValue):
                Whether or not the backup importing request will just bring
                database online without downloading Bak content only one of
                "no_recovery" and "recovery_only" can be true otherwise
                error will return. Applies only to Cloud SQL for SQL Server.
            bak_type (google.cloud.sqladmin_v1beta4.types.BakType):
                Type of the bak content, FULL or DIFF.
            stop_at (google.protobuf.timestamp_pb2.Timestamp):
                Optional. The timestamp when the import should stop. This
                timestamp is in the `RFC
                3339 <https://tools.ietf.org/html/rfc3339>`__ format (for
                example, ``2023-10-01T16:19:00.094``). This field is
                equivalent to the STOPAT keyword and applies to Cloud SQL
                for SQL Server only.
            stop_at_mark (str):
                Optional. The marked transaction where the
                import should stop. This field is equivalent to
                the STOPATMARK keyword and applies to Cloud SQL
                for SQL Server only.
        """

        class EncryptionOptions(proto.Message):
            r"""

            Attributes:
                cert_path (str):
                    Path to the Certificate (.cer) in Cloud Storage, in the form
                    ``gs://bucketName/fileName``. The instance must have write
                    permissions to the bucket and read access to the file.
                pvk_path (str):
                    Path to the Certificate Private Key (.pvk) in Cloud Storage,
                    in the form ``gs://bucketName/fileName``. The instance must
                    have write permissions to the bucket and read access to the
                    file.
                pvk_password (str):
                    Password that encrypts the private key
                keep_encrypted (google.protobuf.wrappers_pb2.BoolValue):
                    Optional. Whether the imported file remains
                    encrypted.
            """

            cert_path: str = proto.Field(
                proto.STRING,
                number=1,
            )
            pvk_path: str = proto.Field(
                proto.STRING,
                number=2,
            )
            pvk_password: str = proto.Field(
                proto.STRING,
                number=3,
            )
            keep_encrypted: wrappers_pb2.BoolValue = proto.Field(
                proto.MESSAGE,
                number=5,
                message=wrappers_pb2.BoolValue,
            )

        encryption_options: "ImportContext.SqlBakImportOptions.EncryptionOptions" = (
            proto.Field(
                proto.MESSAGE,
                number=1,
                message="ImportContext.SqlBakImportOptions.EncryptionOptions",
            )
        )
        striped: wrappers_pb2.BoolValue = proto.Field(
            proto.MESSAGE,
            number=2,
            message=wrappers_pb2.BoolValue,
        )
        no_recovery: wrappers_pb2.BoolValue = proto.Field(
            proto.MESSAGE,
            number=4,
            message=wrappers_pb2.BoolValue,
        )
        recovery_only: wrappers_pb2.BoolValue = proto.Field(
            proto.MESSAGE,
            number=5,
            message=wrappers_pb2.BoolValue,
        )
        bak_type: "BakType" = proto.Field(
            proto.ENUM,
            number=6,
            enum="BakType",
        )
        stop_at: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=7,
            message=timestamp_pb2.Timestamp,
        )
        stop_at_mark: str = proto.Field(
            proto.STRING,
            number=8,
        )

    class SqlTdeImportOptions(proto.Message):
        r"""

        Attributes:
            certificate_path (str):
                Required. Path to the TDE certificate public
                key in the form gs://bucketName/fileName.
                The instance must have read access to the file.
                Applicable only for SQL Server instances.
            private_key_path (str):
                Required. Path to the TDE certificate private
                key in the form gs://bucketName/fileName.
                The instance must have read access to the file.
                Applicable only for SQL Server instances.
            private_key_password (str):
                Required. Password that encrypts the private
                key.
            name (str):
                Required. Certificate name.
                Applicable only for SQL Server instances.
        """

        certificate_path: str = proto.Field(
            proto.STRING,
            number=1,
        )
        private_key_path: str = proto.Field(
            proto.STRING,
            number=2,
        )
        private_key_password: str = proto.Field(
            proto.STRING,
            number=3,
        )
        name: str = proto.Field(
            proto.STRING,
            number=5,
        )

    uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    database: str = proto.Field(
        proto.STRING,
        number=2,
    )
    kind: str = proto.Field(
        proto.STRING,
        number=3,
    )
    file_type: "SqlFileType" = proto.Field(
        proto.ENUM,
        number=4,
        enum="SqlFileType",
    )
    csv_import_options: SqlCsvImportOptions = proto.Field(
        proto.MESSAGE,
        number=5,
        message=SqlCsvImportOptions,
    )
    import_user: str = proto.Field(
        proto.STRING,
        number=6,
    )
    bak_import_options: SqlBakImportOptions = proto.Field(
        proto.MESSAGE,
        number=7,
        message=SqlBakImportOptions,
    )
    sql_import_options: SqlImportOptions = proto.Field(
        proto.MESSAGE,
        number=8,
        message=SqlImportOptions,
    )
    tde_import_options: SqlTdeImportOptions = proto.Field(
        proto.MESSAGE,
        number=9,
        message=SqlTdeImportOptions,
    )


class InstancesCloneRequest(proto.Message):
    r"""Database instance clone request.

    Attributes:
        clone_context (google.cloud.sqladmin_v1beta4.types.CloneContext):
            Contains details about the clone operation.
    """

    clone_context: "CloneContext" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="CloneContext",
    )


class InstancesDemoteMasterRequest(proto.Message):
    r"""Database demote primary instance request.

    Attributes:
        demote_master_context (google.cloud.sqladmin_v1beta4.types.DemoteMasterContext):
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
        demote_context (google.cloud.sqladmin_v1beta4.types.DemoteContext):
            Required. This context is used to demote an
            existing standalone instance to be a Cloud SQL
            read replica for an external database server.
    """

    demote_context: "DemoteContext" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="DemoteContext",
    )


class InstancesExportRequest(proto.Message):
    r"""Database instance export request.

    Attributes:
        export_context (google.cloud.sqladmin_v1beta4.types.ExportContext):
            Contains details about the export operation.
    """

    export_context: "ExportContext" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="ExportContext",
    )


class InstancesFailoverRequest(proto.Message):
    r"""Instance failover request.

    Attributes:
        failover_context (google.cloud.sqladmin_v1beta4.types.FailoverContext):
            Failover Context.
    """

    failover_context: "FailoverContext" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="FailoverContext",
    )


class InstancesImportRequest(proto.Message):
    r"""Database instance import request.

    Attributes:
        import_context (google.cloud.sqladmin_v1beta4.types.ImportContext):
            Contains details about the import operation.
    """

    import_context: "ImportContext" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="ImportContext",
    )


class InstancesPreCheckMajorVersionUpgradeRequest(proto.Message):
    r"""Request for Pre-checks for MVU

    Attributes:
        pre_check_major_version_upgrade_context (google.cloud.sqladmin_v1beta4.types.PreCheckMajorVersionUpgradeContext):
            Required. Contains details about the
            pre-check major version upgrade operation.
    """

    pre_check_major_version_upgrade_context: "PreCheckMajorVersionUpgradeContext" = (
        proto.Field(
            proto.MESSAGE,
            number=1,
            message="PreCheckMajorVersionUpgradeContext",
        )
    )


class MySqlSyncConfig(proto.Message):
    r"""MySQL-specific external server sync settings.

    Attributes:
        initial_sync_flags (MutableSequence[google.cloud.sqladmin_v1beta4.types.SyncFlags]):
            Flags to use for the initial dump.
    """

    initial_sync_flags: MutableSequence["SyncFlags"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="SyncFlags",
    )


class InstancesListResponse(proto.Message):
    r"""Database instances list response.

    Attributes:
        kind (str):
            This is always ``sql#instancesList``.
        warnings (MutableSequence[google.cloud.sqladmin_v1beta4.types.ApiWarning]):
            List of warnings that occurred while handling
            the request.
        items (MutableSequence[google.cloud.sqladmin_v1beta4.types.DatabaseInstance]):
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
    warnings: MutableSequence["ApiWarning"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="ApiWarning",
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
        certs (MutableSequence[google.cloud.sqladmin_v1beta4.types.SslCert]):
            List of server CA certificates for the
            instance.
        active_version (str):

        kind (str):
            This is always ``sql#instancesListServerCas``.
    """

    certs: MutableSequence["SslCert"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="SslCert",
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
    r"""Instances ListServerCertificatess response.

    Attributes:
        ca_certs (MutableSequence[google.cloud.sqladmin_v1beta4.types.SslCert]):
            List of server CA certificates for the
            instance.
        server_certs (MutableSequence[google.cloud.sqladmin_v1beta4.types.SslCert]):
            List of server certificates for the instance, signed by the
            corresponding CA from the ``ca_certs`` list.
        active_version (str):
            The ``sha1_fingerprint`` of the active certificate from
            ``server_certs``.
        kind (str):
            This is always ``sql#instancesListServerCertificates``.
    """

    ca_certs: MutableSequence["SslCert"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="SslCert",
    )
    server_certs: MutableSequence["SslCert"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="SslCert",
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
        certs (MutableSequence[google.cloud.sqladmin_v1beta4.types.SslCert]):
            List of Entra ID certificates for the
            instance.
        active_version (str):
            The ``sha1_fingerprint`` of the active certificate from
            ``certs``.
        kind (str):
            This is always ``sql#instancesListEntraIdCertificates``.
    """

    certs: MutableSequence["SslCert"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="SslCert",
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
        restore_backup_context (google.cloud.sqladmin_v1beta4.types.RestoreBackupContext):
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
        restore_instance_settings (google.cloud.sqladmin_v1beta4.types.DatabaseInstance):
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
    r"""Rotate Server CA request.

    Attributes:
        rotate_server_ca_context (google.cloud.sqladmin_v1beta4.types.RotateServerCaContext):
            Contains details about the rotate server CA
            operation.
    """

    rotate_server_ca_context: "RotateServerCaContext" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="RotateServerCaContext",
    )


class InstancesRotateServerCertificateRequest(proto.Message):
    r"""Rotate Server Certificate request.

    Attributes:
        rotate_server_certificate_context (google.cloud.sqladmin_v1beta4.types.RotateServerCertificateContext):
            Optional. Contains details about the rotate
            server CA operation.
    """

    rotate_server_certificate_context: "RotateServerCertificateContext" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="RotateServerCertificateContext",
    )


class InstancesRotateEntraIdCertificateRequest(proto.Message):
    r"""Rotate Entra ID Certificate request.

    Attributes:
        rotate_entra_id_certificate_context (google.cloud.sqladmin_v1beta4.types.RotateEntraIdCertificateContext):
            Optional. Contains details about the rotate
            Entra ID certificate operation.
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
        truncate_log_context (google.cloud.sqladmin_v1beta4.types.TruncateLogContext):
            Contains details about the truncate log
            operation.
    """

    truncate_log_context: "TruncateLogContext" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="TruncateLogContext",
    )


class InstancesAcquireSsrsLeaseRequest(proto.Message):
    r"""Request to acquire an SSRS lease for an instance.

    Attributes:
        acquire_ssrs_lease_context (google.cloud.sqladmin_v1beta4.types.AcquireSsrsLeaseContext):
            Contains details about the acquire SSRS lease
            operation.
    """

    acquire_ssrs_lease_context: "AcquireSsrsLeaseContext" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="AcquireSsrsLeaseContext",
    )


class PointInTimeRestoreContext(proto.Message):
    r"""Context to perform a point-in-time restore of an instance
    managed by Backup and Disaster Recovery (DR) Service.


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
        target_instance_settings (google.cloud.sqladmin_v1beta4.types.DatabaseInstance):
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


class PerformDiskShrinkContext(proto.Message):
    r"""Perform disk shrink context.

    Attributes:
        target_size_gb (int):
            The target disk shrink size in GigaBytes.
    """

    target_size_gb: int = proto.Field(
        proto.INT64,
        number=1,
    )


class PreCheckResponse(proto.Message):
    r"""Structured PreCheckResponse containing message, type, and
    required actions.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        message (str):
            The message to be displayed to the user.

            This field is a member of `oneof`_ ``_message``.
        message_type (google.cloud.sqladmin_v1beta4.types.PreCheckResponse.MessageType):
            The type of message whether it is an info,
            warning, or error.

            This field is a member of `oneof`_ ``_message_type``.
        actions_required (MutableSequence[str]):
            The actions that the user needs to take. Use
            repeated for multiple actions.
    """

    class MessageType(proto.Enum):
        r"""The type of message which can be an info, a warning, or an
        error that requires user intervention.

        Values:
            MESSAGE_TYPE_UNSPECIFIED (0):
                Default unspecified value to prevent
                unintended behavior changes.
            INFO (1):
                General informational messages that don't
                require action.
            WARNING (2):
                Warnings that might impact the upgrade but
                don't block it.
            ERROR (3):
                Errors that a user must resolve before
                proceeding with the upgrade.
        """

        MESSAGE_TYPE_UNSPECIFIED = 0
        INFO = 1
        WARNING = 2
        ERROR = 3

    message: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    message_type: MessageType = proto.Field(
        proto.ENUM,
        number=3,
        optional=True,
        enum=MessageType,
    )
    actions_required: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )


class PreCheckMajorVersionUpgradeContext(proto.Message):
    r"""Pre-check major version upgrade context.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        target_database_version (google.cloud.sqladmin_v1beta4.types.SqlDatabaseVersion):
            Required. The target database version to
            upgrade to.
        pre_check_response (MutableSequence[google.cloud.sqladmin_v1beta4.types.PreCheckResponse]):
            Output only. The responses from the precheck
            operation.
        kind (str):
            Optional. This is always
            ``sql#preCheckMajorVersionUpgradeContext``.
        max_runtime (google.protobuf.duration_pb2.Duration):
            Optional. The maximum allowed runtime for the
            precheck operation.

            This field is a member of `oneof`_ ``_max_runtime``.
    """

    target_database_version: "SqlDatabaseVersion" = proto.Field(
        proto.ENUM,
        number=1,
        enum="SqlDatabaseVersion",
    )
    pre_check_response: MutableSequence["PreCheckResponse"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="PreCheckResponse",
    )
    kind: str = proto.Field(
        proto.STRING,
        number=3,
    )
    max_runtime: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=4,
        optional=True,
        message=duration_pb2.Duration,
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


class SqlInstancesVerifyExternalSyncSettingsResponse(proto.Message):
    r"""Instance verify external sync settings response.

    Attributes:
        kind (str):
            This is always ``sql#migrationSettingErrorList``.
        errors (MutableSequence[google.cloud.sqladmin_v1beta4.types.SqlExternalSyncSettingError]):
            List of migration violations.
        warnings (MutableSequence[google.cloud.sqladmin_v1beta4.types.SqlExternalSyncSettingError]):
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


class SqlExternalSyncSettingError(proto.Message):
    r"""External primary instance migration setting error/warning.

    Attributes:
        kind (str):
            Can be ``sql#externalSyncSettingError`` or
            ``sql#externalSyncSettingWarning``.
        type_ (google.cloud.sqladmin_v1beta4.types.SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType):
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
                or having unsupported versions
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
                [replica_overwrite_enabled][google.cloud.sql.v1beta4.SqlInstancesStartExternalSyncRequest.replica_overwrite_enabled]
                in the request to acknowledge this. This is an error. MySQL
                only.
            WILL_DELETE_EXISTING (57):
                The migration will delete existing data in the replica;
                [replica_overwrite_enabled][google.cloud.sql.v1beta4.SqlInstancesStartExternalSyncRequest.replica_overwrite_enabled]
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


class IpConfiguration(proto.Message):
    r"""IP Management configuration.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        ipv4_enabled (google.protobuf.wrappers_pb2.BoolValue):
            Whether the instance is assigned a public IP
            address or not.
        private_network (str):
            The resource link for the VPC network from which the Cloud
            SQL instance is accessible for private IP. For example,
            ``/projects/myProject/global/networks/default``. This
            setting can be updated, but it cannot be removed after it is
            set.
        require_ssl (google.protobuf.wrappers_pb2.BoolValue):
            Use ``ssl_mode`` instead.

            Whether SSL/TLS connections over IP are enforced. If set to
            false, then allow both non-SSL/non-TLS and SSL/TLS
            connections. For SSL/TLS connections, the client certificate
            won't be verified. If set to true, then only allow
            connections encrypted with SSL/TLS and with valid client
            certificates. If you want to enforce SSL/TLS without
            enforcing the requirement for valid client certificates,
            then use the ``ssl_mode`` flag instead of the legacy
            ``require_ssl`` flag.
        authorized_networks (MutableSequence[google.cloud.sqladmin_v1beta4.types.AclEntry]):
            The list of external networks that are allowed to connect to
            the instance using the IP. In 'CIDR' notation, also known as
            'slash' notation (for example: ``157.197.200.0/24``).
        allocated_ip_range (str):
            The name of the allocated ip range for the private ip Cloud
            SQL instance. For example:
            "google-managed-services-default". If set, the instance ip
            will be created in the allocated range. The range name must
            comply with `RFC
            1035 <https://tools.ietf.org/html/rfc1035>`__. Specifically,
            the name must be 1-63 characters long and match the regular
            expression ``[a-z]([-a-z0-9]*[a-z0-9])?.``
        enable_private_path_for_google_cloud_services (google.protobuf.wrappers_pb2.BoolValue):
            Controls connectivity to private IP instances
            from Google services, such as BigQuery.
        ssl_mode (google.cloud.sqladmin_v1beta4.types.IpConfiguration.SslMode):
            Specify how SSL/TLS is enforced in database connections. If
            you must use the ``require_ssl`` flag for backward
            compatibility, then only the following value pairs are
            valid:

            For PostgreSQL and MySQL:

            - ``ssl_mode=ALLOW_UNENCRYPTED_AND_ENCRYPTED`` and
              ``require_ssl=false``
            - ``ssl_mode=ENCRYPTED_ONLY`` and ``require_ssl=false``
            - ``ssl_mode=TRUSTED_CLIENT_CERTIFICATE_REQUIRED`` and
              ``require_ssl=true``

            For SQL Server:

            - ``ssl_mode=ALLOW_UNENCRYPTED_AND_ENCRYPTED`` and
              ``require_ssl=false``
            - ``ssl_mode=ENCRYPTED_ONLY`` and ``require_ssl=true``

            The value of ``ssl_mode`` has priority over the value of
            ``require_ssl``.

            For example, for the pair ``ssl_mode=ENCRYPTED_ONLY`` and
            ``require_ssl=false``, ``ssl_mode=ENCRYPTED_ONLY`` means
            accept only SSL connections, while ``require_ssl=false``
            means accept both non-SSL and SSL connections. In this case,
            MySQL and PostgreSQL databases respect ``ssl_mode`` and
            accepts only SSL connections.
        psc_config (google.cloud.sqladmin_v1beta4.types.PscConfig):
            PSC settings for this instance.

            This field is a member of `oneof`_ ``_psc_config``.
        server_ca_mode (google.cloud.sqladmin_v1beta4.types.IpConfiguration.CaMode):
            Specify what type of CA is used for the
            server certificate.

            This field is a member of `oneof`_ ``_server_ca_mode``.
        custom_subject_alternative_names (MutableSequence[str]):
            Optional. Custom Subject Alternative
            Name(SAN)s for a Cloud SQL instance.
        server_ca_pool (str):
            Optional. The resource name of the server CA pool for an
            instance with ``CUSTOMER_MANAGED_CAS_CA`` as the
            ``server_ca_mode``. Format:
            projects/{PROJECT}/locations/{REGION}/caPools/{CA_POOL_ID}

            This field is a member of `oneof`_ ``_server_ca_pool``.
        server_certificate_rotation_mode (google.cloud.sqladmin_v1beta4.types.IpConfiguration.ServerCertificateRotationMode):
            Optional. Controls the automatic server certificate rotation
            feature. This feature is disabled by default. When enabled,
            the server certificate will be automatically rotated during
            Cloud SQL scheduled maintenance or self-service maintenance
            updates up to six months before it expires. This setting can
            only be set if server_ca_mode is either
            GOOGLE_MANAGED_CAS_CA or CUSTOMER_MANAGED_CAS_CA.

            This field is a member of `oneof`_ ``_server_certificate_rotation_mode``.
    """

    class SslMode(proto.Enum):
        r"""The SSL options for database connections.

        Values:
            SSL_MODE_UNSPECIFIED (0):
                The SSL mode is unknown.
            ALLOW_UNENCRYPTED_AND_ENCRYPTED (1):
                Allow non-SSL/non-TLS and SSL/TLS connections. For SSL
                connections to MySQL and PostgreSQL, the client certificate
                isn't verified.

                When this value is used, the legacy ``require_ssl`` flag
                must be false or cleared to avoid a conflict between the
                values of the two flags.
            ENCRYPTED_ONLY (2):
                Only allow connections encrypted with SSL/TLS. For SSL
                connections to MySQL and PostgreSQL, the client certificate
                isn't verified.

                When this value is used, the legacy ``require_ssl`` flag
                must be false or cleared to avoid a conflict between the
                values of the two flags.
            TRUSTED_CLIENT_CERTIFICATE_REQUIRED (3):
                Only allow connections encrypted with SSL/TLS and with valid
                client certificates.

                When this value is used, the legacy ``require_ssl`` flag
                must be true or cleared to avoid the conflict between values
                of two flags. PostgreSQL clients or users that connect using
                IAM database authentication must use either the `Cloud SQL
                Auth
                Proxy <https://cloud.google.com/sql/docs/postgres/connect-auth-proxy>`__
                or `Cloud SQL
                Connectors <https://cloud.google.com/sql/docs/postgres/connect-connectors>`__
                to enforce client identity verification.

                Only applicable to MySQL and PostgreSQL. Not applicable to
                SQL Server.
        """

        SSL_MODE_UNSPECIFIED = 0
        ALLOW_UNENCRYPTED_AND_ENCRYPTED = 1
        ENCRYPTED_ONLY = 2
        TRUSTED_CLIENT_CERTIFICATE_REQUIRED = 3

    class CaMode(proto.Enum):
        r"""Various Certificate Authority (CA) modes for certificate
        signing.

        Values:
            CA_MODE_UNSPECIFIED (0):
                CA mode is unspecified. It is effectively the same as
                ``GOOGLE_MANAGED_INTERNAL_CA``.
            GOOGLE_MANAGED_INTERNAL_CA (1):
                Google-managed self-signed internal CA.
            GOOGLE_MANAGED_CAS_CA (2):
                Google-managed regional CA part of root CA
                hierarchy hosted on Google Cloud's Certificate
                Authority Service (CAS).
            CUSTOMER_MANAGED_CAS_CA (3):
                Customer-managed CA hosted on Google Cloud's
                Certificate Authority Service (CAS).
        """

        CA_MODE_UNSPECIFIED = 0
        GOOGLE_MANAGED_INTERNAL_CA = 1
        GOOGLE_MANAGED_CAS_CA = 2
        CUSTOMER_MANAGED_CAS_CA = 3

    class ServerCertificateRotationMode(proto.Enum):
        r"""Settings for automatic server certificate rotation.

        Values:
            SERVER_CERTIFICATE_ROTATION_MODE_UNSPECIFIED (0):
                Unspecified: no automatic server certificate
                rotation.
            NO_AUTOMATIC_ROTATION (1):
                No automatic server certificate rotation. The user must
                `manage server certificate
                rotation </sql/docs/mysql/manage-ssl-instance#rotate-server-certificate-cas>`__
                on their side.
            AUTOMATIC_ROTATION_DURING_MAINTENANCE (2):
                Automatic server certificate rotation during Cloud SQL
                scheduled maintenance or self-service maintenance updates.
                Requires ``server_ca_mode`` to be ``GOOGLE_MANAGED_CAS_CA``
                or ``CUSTOMER_MANAGED_CAS_CA``.
        """

        SERVER_CERTIFICATE_ROTATION_MODE_UNSPECIFIED = 0
        NO_AUTOMATIC_ROTATION = 1
        AUTOMATIC_ROTATION_DURING_MAINTENANCE = 2

    ipv4_enabled: wrappers_pb2.BoolValue = proto.Field(
        proto.MESSAGE,
        number=1,
        message=wrappers_pb2.BoolValue,
    )
    private_network: str = proto.Field(
        proto.STRING,
        number=2,
    )
    require_ssl: wrappers_pb2.BoolValue = proto.Field(
        proto.MESSAGE,
        number=3,
        message=wrappers_pb2.BoolValue,
    )
    authorized_networks: MutableSequence["AclEntry"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="AclEntry",
    )
    allocated_ip_range: str = proto.Field(
        proto.STRING,
        number=6,
    )
    enable_private_path_for_google_cloud_services: wrappers_pb2.BoolValue = proto.Field(
        proto.MESSAGE,
        number=7,
        message=wrappers_pb2.BoolValue,
    )
    ssl_mode: SslMode = proto.Field(
        proto.ENUM,
        number=8,
        enum=SslMode,
    )
    psc_config: "PscConfig" = proto.Field(
        proto.MESSAGE,
        number=9,
        optional=True,
        message="PscConfig",
    )
    server_ca_mode: CaMode = proto.Field(
        proto.ENUM,
        number=10,
        optional=True,
        enum=CaMode,
    )
    custom_subject_alternative_names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=11,
    )
    server_ca_pool: str = proto.Field(
        proto.STRING,
        number=12,
        optional=True,
    )
    server_certificate_rotation_mode: ServerCertificateRotationMode = proto.Field(
        proto.ENUM,
        number=16,
        optional=True,
        enum=ServerCertificateRotationMode,
    )


class PscConfig(proto.Message):
    r"""PSC settings for a Cloud SQL instance.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        psc_enabled (bool):
            Whether PSC connectivity is enabled for this
            instance.

            This field is a member of `oneof`_ ``_psc_enabled``.
        allowed_consumer_projects (MutableSequence[str]):
            Optional. The list of consumer projects that
            are allow-listed for PSC connections to this
            instance. This instance can be connected to with
            PSC from any network in these projects.

            Each consumer project in this list may be
            represented by a project number (numeric) or by
            a project id (alphanumeric).
        psc_auto_connections (MutableSequence[google.cloud.sqladmin_v1beta4.types.PscAutoConnectionConfig]):
            Optional. The list of settings for requested
            Private Service Connect consumer endpoints that
            can be used to connect to this Cloud SQL
            instance.
        network_attachment_uri (str):
            Optional. The network attachment of the
            consumer network that the Private Service
            Connect enabled Cloud SQL instance is authorized
            to connect using the PSC interface. format:
            projects/PROJECT/regions/REGION/networkAttachments/ID
        psc_auto_dns_enabled (bool):
            Optional. Indicates whether Private Service
            Connect DNS automation is enabled for this
            instance. When enabled, Cloud SQL provisions a
            universal DNS record across all networks
            configured with Private Service Connect
            auto-connections. This will default to true for
            new instances when Private Service Connect is
            enabled.

            This field is a member of `oneof`_ ``_psc_auto_dns_enabled``.
        psc_write_endpoint_dns_enabled (bool):
            Optional. Indicates whether Private Service Connect write
            endpoint DNS automation is enabled for this instance. When
            enabled, Cloud SQL provisions a universal global DNS record
            across all networks configured with Private Service Connect
            auto-connections that points to the cluster primary
            instance. This feature is only supported for Enterprise Plus
            edition. This will default to true for new enterprise plus
            instances when ``psc_auto_dns_enabled`` is enabled.

            This field is a member of `oneof`_ ``_psc_write_endpoint_dns_enabled``.
        psc_auto_connection_policy_enabled (bool):
            Optional. Whether to set up the PSC service
            connection policy automatically.

            This field is a member of `oneof`_ ``_psc_auto_connection_policy_enabled``.
    """

    psc_enabled: bool = proto.Field(
        proto.BOOL,
        number=1,
        optional=True,
    )
    allowed_consumer_projects: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    psc_auto_connections: MutableSequence["PscAutoConnectionConfig"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=3,
            message="PscAutoConnectionConfig",
        )
    )
    network_attachment_uri: str = proto.Field(
        proto.STRING,
        number=4,
    )
    psc_auto_dns_enabled: bool = proto.Field(
        proto.BOOL,
        number=5,
        optional=True,
    )
    psc_write_endpoint_dns_enabled: bool = proto.Field(
        proto.BOOL,
        number=6,
        optional=True,
    )
    psc_auto_connection_policy_enabled: bool = proto.Field(
        proto.BOOL,
        number=7,
        optional=True,
    )


class PscAutoConnectionConfig(proto.Message):
    r"""Settings for an automatically-setup Private Service Connect
    consumer endpoint that is used to connect to a Cloud SQL
    instance.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        consumer_project (str):
            Optional. This is the project ID of consumer service project
            of this consumer endpoint.

            Optional. This is only applicable if consumer_network is a
            shared vpc network.
        consumer_network (str):
            Optional. The consumer network of this consumer endpoint.
            This must be a resource path that includes both the host
            project and the network name.

            For example, ``projects/project1/global/networks/network1``.

            The consumer host project of this network might be different
            from the consumer service project.
        ip_address (str):
            The IP address of the consumer endpoint.

            This field is a member of `oneof`_ ``_ip_address``.
        status (str):
            The connection status of the consumer
            endpoint.

            This field is a member of `oneof`_ ``_status``.
        consumer_network_status (str):
            The connection policy status of the consumer
            network.

            This field is a member of `oneof`_ ``_consumer_network_status``.
        service_connection_policy (str):
            Output only. The service connection policy created
            automatically for the consumer network when
            ``psc_auto_connection_policy_enabled`` is true. It is in the
            format of:
            ``projects/{project}/regions/{region}/serviceConnectionPolicies/{policy_id}``
            The ``policy_id`` is in format of ``$NETWORK-$RANDOM``.

            This field is a member of `oneof`_ ``_service_connection_policy``.
        service_connection_policy_creation_result (str):
            Output only. The status of service connection
            policy creation.

            This field is a member of `oneof`_ ``_service_connection_policy_creation_result``.
        instance_auto_dns_status (google.cloud.sqladmin_v1beta4.types.AutoDnsStatus):
            Output only. The status of automated DNS
            provisioning.

            This field is a member of `oneof`_ ``_instance_auto_dns_status``.
        write_endpoint_auto_dns_status (google.cloud.sqladmin_v1beta4.types.AutoDnsStatus):
            Output only. The status of automated DNS
            provisioning for the write endpoint.

            This field is a member of `oneof`_ ``_write_endpoint_auto_dns_status``.
    """

    consumer_project: str = proto.Field(
        proto.STRING,
        number=1,
    )
    consumer_network: str = proto.Field(
        proto.STRING,
        number=2,
    )
    ip_address: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )
    status: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )
    consumer_network_status: str = proto.Field(
        proto.STRING,
        number=5,
        optional=True,
    )
    service_connection_policy: str = proto.Field(
        proto.STRING,
        number=6,
        optional=True,
    )
    service_connection_policy_creation_result: str = proto.Field(
        proto.STRING,
        number=7,
        optional=True,
    )
    instance_auto_dns_status: "AutoDnsStatus" = proto.Field(
        proto.ENUM,
        number=8,
        optional=True,
        enum="AutoDnsStatus",
    )
    write_endpoint_auto_dns_status: "AutoDnsStatus" = proto.Field(
        proto.ENUM,
        number=9,
        optional=True,
        enum="AutoDnsStatus",
    )


class IpMapping(proto.Message):
    r"""Database instance IP mapping

    Attributes:
        type_ (google.cloud.sqladmin_v1beta4.types.SqlIpAddressType):
            The type of this IP address. A ``PRIMARY`` address is a
            public address that can accept incoming connections. A
            ``PRIVATE`` address is a private address that can accept
            incoming connections. An ``OUTGOING`` address is the source
            address of connections originating from the instance, if
            supported.
        ip_address (str):
            The IP address assigned.
        time_to_retire (google.protobuf.timestamp_pb2.Timestamp):
            The due time for this IP to be retired in `RFC
            3339 <https://tools.ietf.org/html/rfc3339>`__ format, for
            example ``2012-11-15T16:19:00.094Z``. This field is only
            available when the IP is scheduled to be retired.
    """

    type_: "SqlIpAddressType" = proto.Field(
        proto.ENUM,
        number=1,
        enum="SqlIpAddressType",
    )
    ip_address: str = proto.Field(
        proto.STRING,
        number=2,
    )
    time_to_retire: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )


class LocationPreference(proto.Message):
    r"""Preferred location. This specifies where a Cloud SQL instance
    is located. Note that if the preferred location is not
    available, the instance will be located as close as possible
    within the region. Only one location may be specified.

    Attributes:
        follow_gae_application (str):
            The App Engine application to follow, it must
            be in the same region as the Cloud SQL instance.
            WARNING: Changing this might restart the
            instance.
        zone (str):
            The preferred Compute Engine zone (for
            example: us-central1-a, us-central1-b, etc.).
            WARNING: Changing this might restart the
            instance.
        secondary_zone (str):
            The preferred Compute Engine zone for the secondary/failover
            (for example: us-central1-a, us-central1-b, etc.). To
            disable this field, set it to 'no_secondary_zone'.
        kind (str):
            This is always ``sql#locationPreference``.
    """

    follow_gae_application: str = proto.Field(
        proto.STRING,
        number=1,
    )
    zone: str = proto.Field(
        proto.STRING,
        number=2,
    )
    secondary_zone: str = proto.Field(
        proto.STRING,
        number=4,
    )
    kind: str = proto.Field(
        proto.STRING,
        number=3,
    )


class MaintenanceWindow(proto.Message):
    r"""Maintenance window. This specifies when a Cloud SQL instance
    is restarted for system maintenance purposes.

    Attributes:
        hour (google.protobuf.wrappers_pb2.Int32Value):
            Hour of day - 0 to 23. Specify in the UTC
            time zone.
        day (google.protobuf.wrappers_pb2.Int32Value):
            Day of week - ``MONDAY``, ``TUESDAY``, ``WEDNESDAY``,
            ``THURSDAY``, ``FRIDAY``, ``SATURDAY``, or ``SUNDAY``.
            Specify in the UTC time zone. Returned in output as an
            integer, 1 to 7, where ``1`` equals Monday.
        update_track (google.cloud.sqladmin_v1beta4.types.SqlUpdateTrack):
            Maintenance timing settings: ``canary``, ``stable``, or
            ``week5``. For more information, see `About maintenance on
            Cloud SQL
            instances <https://cloud.google.com/sql/docs/mysql/maintenance>`__.
        kind (str):
            This is always ``sql#maintenanceWindow``.
    """

    hour: wrappers_pb2.Int32Value = proto.Field(
        proto.MESSAGE,
        number=1,
        message=wrappers_pb2.Int32Value,
    )
    day: wrappers_pb2.Int32Value = proto.Field(
        proto.MESSAGE,
        number=2,
        message=wrappers_pb2.Int32Value,
    )
    update_track: "SqlUpdateTrack" = proto.Field(
        proto.ENUM,
        number=3,
        enum="SqlUpdateTrack",
    )
    kind: str = proto.Field(
        proto.STRING,
        number=4,
    )


class DenyMaintenancePeriod(proto.Message):
    r"""Deny Maintenance Periods. This specifies a date range during
    when all CSA rollout will be denied.

    Attributes:
        start_date (str):
            "deny maintenance period" start date. If the
            year of the start date is empty, the year of the
            end date also must be empty. In this case, it
            means the deny maintenance period recurs every
            year. The date is in format yyyy-mm-dd i.e.,
            2020-11-01, or mm-dd, i.e., 11-01
        end_date (str):
            "deny maintenance period" end date. If the
            year of the end date is empty, the year of the
            start date also must be empty. In this case, it
            means the deny maintenance period recurs every
            year. The date is in format yyyy-mm-dd i.e.,
            2020-11-01, or mm-dd, i.e., 11-01
        time (str):
            Time in UTC when the "deny maintenance period" starts on
            start_date and ends on end_date. The time is in format:
            HH:mm:SS, i.e., 00:00:00
    """

    start_date: str = proto.Field(
        proto.STRING,
        number=1,
    )
    end_date: str = proto.Field(
        proto.STRING,
        number=2,
    )
    time: str = proto.Field(
        proto.STRING,
        number=3,
    )


class InsightsConfig(proto.Message):
    r"""Insights configuration. This specifies when Cloud SQL
    Insights feature is enabled and optional configuration.

    Attributes:
        query_insights_enabled (bool):
            Whether Query Insights feature is enabled.
        record_client_address (bool):
            Whether Query Insights will record client
            address when enabled.
        record_application_tags (bool):
            Whether Query Insights will record
            application tags from query when enabled.
        query_string_length (google.protobuf.wrappers_pb2.Int32Value):
            Maximum query length stored in bytes. Default
            value: 1024 bytes. Range: 256-4500 bytes. Query
            lengths greater than this field value will be
            truncated to this value. When unset, query
            length will be the default value. Changing query
            length will restart the database.
        query_plans_per_minute (google.protobuf.wrappers_pb2.Int32Value):
            Number of query execution plans captured by
            Insights per minute for all queries combined.
            Default is 5.
        enhanced_query_insights_enabled (google.protobuf.wrappers_pb2.BoolValue):
            Optional. Whether enhanced query insights
            feature is enabled.
    """

    query_insights_enabled: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    record_client_address: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    record_application_tags: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    query_string_length: wrappers_pb2.Int32Value = proto.Field(
        proto.MESSAGE,
        number=4,
        message=wrappers_pb2.Int32Value,
    )
    query_plans_per_minute: wrappers_pb2.Int32Value = proto.Field(
        proto.MESSAGE,
        number=5,
        message=wrappers_pb2.Int32Value,
    )
    enhanced_query_insights_enabled: wrappers_pb2.BoolValue = proto.Field(
        proto.MESSAGE,
        number=8,
        message=wrappers_pb2.BoolValue,
    )


class MySqlReplicaConfiguration(proto.Message):
    r"""Read-replica configuration specific to MySQL databases.

    Attributes:
        dump_file_path (str):
            Path to a SQL dump file in Google Cloud
            Storage from which the replica instance is to be
            created. The URI is in the form
            gs://bucketName/fileName. Compressed gzip files
            (.gz) are also supported. Dumps have the binlog
            co-ordinates from which replication begins. This
            can be accomplished by setting --master-data to
            1 when using mysqldump.
        username (str):
            The username for the replication connection.
        password (str):
            The password for the replication connection.
        connect_retry_interval (google.protobuf.wrappers_pb2.Int32Value):
            Seconds to wait between connect retries.
            MySQL's default is 60 seconds.
        master_heartbeat_period (google.protobuf.wrappers_pb2.Int64Value):
            Interval in milliseconds between replication
            heartbeats.
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
        ssl_cipher (str):
            A list of permissible ciphers to use for SSL
            encryption.
        verify_server_certificate (google.protobuf.wrappers_pb2.BoolValue):
            Whether or not to check the primary
            instance's Common Name value in the certificate
            that it sends during the SSL handshake.
        kind (str):
            This is always ``sql#mysqlReplicaConfiguration``.
    """

    dump_file_path: str = proto.Field(
        proto.STRING,
        number=1,
    )
    username: str = proto.Field(
        proto.STRING,
        number=2,
    )
    password: str = proto.Field(
        proto.STRING,
        number=3,
    )
    connect_retry_interval: wrappers_pb2.Int32Value = proto.Field(
        proto.MESSAGE,
        number=4,
        message=wrappers_pb2.Int32Value,
    )
    master_heartbeat_period: wrappers_pb2.Int64Value = proto.Field(
        proto.MESSAGE,
        number=5,
        message=wrappers_pb2.Int64Value,
    )
    ca_certificate: str = proto.Field(
        proto.STRING,
        number=6,
    )
    client_certificate: str = proto.Field(
        proto.STRING,
        number=7,
    )
    client_key: str = proto.Field(
        proto.STRING,
        number=8,
    )
    ssl_cipher: str = proto.Field(
        proto.STRING,
        number=9,
    )
    verify_server_certificate: wrappers_pb2.BoolValue = proto.Field(
        proto.MESSAGE,
        number=10,
        message=wrappers_pb2.BoolValue,
    )
    kind: str = proto.Field(
        proto.STRING,
        number=11,
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
        source_instance (google.cloud.sqladmin_v1beta4.types.InstanceReference):
            The reference to Cloud SQL instance if the
            source is Cloud SQL.
        selected_objects (MutableSequence[google.cloud.sqladmin_v1beta4.types.SelectedObjects]):
            Optional. A list of objects that the user
            selects for replication from an external source
            instance.
        ssl_option (google.cloud.sqladmin_v1beta4.types.OnPremisesConfiguration.SslOption):
            Optional. SslOption for replica connection to
            the on-premises source.
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
                SSL is disabled for replica connection to the
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
    source_instance: "InstanceReference" = proto.Field(
        proto.MESSAGE,
        number=15,
        message="InstanceReference",
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


class DiskEncryptionConfiguration(proto.Message):
    r"""Disk encryption configuration for an instance.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        kms_key_name (str):
            Resource name of KMS key for disk encryption
        kind (str):
            This is always ``sql#diskEncryptionConfiguration``.
        confidential_mode (bool):
            Optional. If true, enables Confidential Mode
            for the instance's Hyperdisk Balanced volumes.
            Only supported for zonal C4A instances
            currently.

            This field is a member of `oneof`_ ``_confidential_mode``.
        cmek_source_log_encryption_enforced (bool):
            Optional. Whether to enforce CMEK log
            encryption at source. When enforced, transaction
            logs are encrypted prior to being uploaded to
            Cloud Storage. If not enforced, then CMEK logs
            are encrypted by the Cloud Storage service.

            This field is a member of `oneof`_ ``_cmek_source_log_encryption_enforced``.
    """

    kms_key_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    kind: str = proto.Field(
        proto.STRING,
        number=2,
    )
    confidential_mode: bool = proto.Field(
        proto.BOOL,
        number=3,
        optional=True,
    )
    cmek_source_log_encryption_enforced: bool = proto.Field(
        proto.BOOL,
        number=4,
        optional=True,
    )


class DiskEncryptionStatus(proto.Message):
    r"""Disk encryption status for an instance.

    Attributes:
        kms_key_version_name (str):
            KMS key version used to encrypt the Cloud SQL
            instance resource
        kind (str):
            This is always ``sql#diskEncryptionStatus``.
    """

    kms_key_version_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    kind: str = proto.Field(
        proto.STRING,
        number=2,
    )


class SqlSubOperationType(proto.Message):
    r"""The sub operation type based on the operation type.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        maintenance_type (google.cloud.sqladmin_v1beta4.types.SqlMaintenanceType):
            The type of maintenance to be performed on
            the instance.

            This field is a member of `oneof`_ ``sub_operation_details``.
    """

    maintenance_type: "SqlMaintenanceType" = proto.Field(
        proto.ENUM,
        number=1,
        oneof="sub_operation_details",
        enum="SqlMaintenanceType",
    )


class Operation(proto.Message):
    r"""An Operation resource.&nbsp;For successful operations that
    return an Operation resource, only the fields relevant to the
    operation are populated in the resource.

    Attributes:
        kind (str):
            This is always ``sql#operation``.
        target_link (str):

        status (google.cloud.sqladmin_v1beta4.types.Operation.SqlOperationStatus):
            The status of an operation.
        user (str):
            The email address of the user who initiated
            this operation.
        insert_time (google.protobuf.timestamp_pb2.Timestamp):
            The time this operation was enqueued in UTC timezone in `RFC
            3339 <https://tools.ietf.org/html/rfc3339>`__ format, for
            example ``2012-11-15T16:19:00.094Z``.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            The time this operation actually started in UTC timezone in
            `RFC 3339 <https://tools.ietf.org/html/rfc3339>`__ format,
            for example ``2012-11-15T16:19:00.094Z``.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            The time this operation finished in UTC timezone in `RFC
            3339 <https://tools.ietf.org/html/rfc3339>`__ format, for
            example ``2012-11-15T16:19:00.094Z``.
        error (google.cloud.sqladmin_v1beta4.types.OperationErrors):
            If errors occurred during processing of this
            operation, this field will be populated.
        api_warning (google.cloud.sqladmin_v1beta4.types.ApiWarning):
            An Admin API warning message.
        operation_type (google.cloud.sqladmin_v1beta4.types.Operation.SqlOperationType):
            The type of the operation. Valid values are:

            - ``CREATE``
            - ``DELETE``
            - ``UPDATE``
            - ``RESTART``
            - ``IMPORT``
            - ``EXPORT``
            - ``BACKUP_VOLUME``
            - ``RESTORE_VOLUME``
            - ``CREATE_USER``
            - ``DELETE_USER``
            - ``CREATE_DATABASE``
            - ``DELETE_DATABASE``
        import_context (google.cloud.sqladmin_v1beta4.types.ImportContext):
            The context for import operation, if
            applicable.
        export_context (google.cloud.sqladmin_v1beta4.types.ExportContext):
            The context for export operation, if
            applicable.
        backup_context (google.cloud.sqladmin_v1beta4.types.BackupContext):
            The context for backup operation, if
            applicable.
        pre_check_major_version_upgrade_context (google.cloud.sqladmin_v1beta4.types.PreCheckMajorVersionUpgradeContext):
            The context for pre-check major version upgrade operation,
            if applicable. This field is only populated when the
            operation_type is PRE_CHECK_MAJOR_VERSION_UPGRADE. The
            PreCheckMajorVersionUpgradeContext message itself contains
            the details for that pre-check, such as the target database
            version for the upgrade and the results of the check
            (including any warnings or errors found).
        start_workload_capture_context (google.cloud.sqladmin_v1beta4.types.StartWorkloadCaptureContext):
            The context for the ``StartWorkloadCapture`` operation,
            which contains details to start recording the workload (SQL
            queries) on a Cloud SQL instance.
        stop_workload_capture_context (google.cloud.sqladmin_v1beta4.types.StopWorkloadCaptureContext):
            The context for the ``StopWorkloadCapture`` operation, which
            contains details to stop recording the workload (SQL
            queries) on a Cloud SQL instance.
        start_workload_replay_context (google.cloud.sqladmin_v1beta4.types.StartWorkloadReplayContext):
            The context for the ``StartWorkloadReplay`` operation, which
            contains details about starting the execution of a captured
            workload (recorded read and write SQL queries) on a replay
            instance (the Cloud SQL instance where the recorded SQL
            queries are executed).
        stop_workload_replay_context (google.cloud.sqladmin_v1beta4.types.StopWorkloadReplayContext):
            The context for the ``StopWorkloadReplay`` operation, which
            contains details about stopping the execution of a captured
            workload (recorded read and write SQL queries) on a replay
            instance.
        name (str):
            An identifier that uniquely identifies the
            operation. You can use this identifier to
            retrieve the Operations resource that has
            information about the operation.
        target_id (str):
            Name of the resource on which this operation
            runs.
        self_link (str):
            The URI of this resource.
        target_project (str):
            The project ID of the target instance related
            to this operation.
        acquire_ssrs_lease_context (google.cloud.sqladmin_v1beta4.types.AcquireSsrsLeaseContext):
            The context for acquire SSRS lease operation,
            if applicable.
        sub_operation_type (google.cloud.sqladmin_v1beta4.types.SqlSubOperationType):
            Optional. The sub operation based on the
            operation type.
    """

    class SqlOperationType(proto.Enum):
        r"""The type of Cloud SQL operation.

        Values:
            SQL_OPERATION_TYPE_UNSPECIFIED (0):
                Unknown operation type.
            IMPORT (1):
                Imports data into a Cloud SQL instance.
            EXPORT (2):
                Exports data from a Cloud SQL instance to a
                Cloud Storage bucket.
            CREATE (3):
                Creates a new Cloud SQL instance.
            UPDATE (4):
                Updates the settings of a Cloud SQL instance.
            DELETE (5):
                Deletes a Cloud SQL instance.
            RESTART (6):
                Restarts the Cloud SQL instance.
            BACKUP (7):
                No description available.
            SNAPSHOT (8):
                No description available.
            BACKUP_VOLUME (9):
                Performs instance backup.
            DELETE_VOLUME (10):
                Deletes an instance backup.
            RESTORE_VOLUME (11):
                Restores an instance backup.
            INJECT_USER (12):
                Injects a privileged user in mysql for MOB
                instances.
            CLONE (14):
                Clones a Cloud SQL instance.
            STOP_REPLICA (15):
                Stops replication on a Cloud SQL read replica
                instance.
            START_REPLICA (16):
                Starts replication on a Cloud SQL read
                replica instance.
            PROMOTE_REPLICA (17):
                Promotes a Cloud SQL replica instance.
            CREATE_REPLICA (18):
                Creates a Cloud SQL replica instance.
            CREATE_USER (19):
                Creates a new user in a Cloud SQL instance.
            DELETE_USER (20):
                Deletes a user from a Cloud SQL instance.
            UPDATE_USER (21):
                Updates an existing user in a Cloud SQL
                instance. If a user with the specified username
                doesn't exist, a new user is created.
            CREATE_DATABASE (22):
                Creates a database in the Cloud SQL instance.
            DELETE_DATABASE (23):
                Deletes a database in the Cloud SQL instance.
            UPDATE_DATABASE (24):
                Updates a database in the Cloud SQL instance.
            FAILOVER (25):
                Performs failover of an HA-enabled Cloud SQL
                failover replica.
            DELETE_BACKUP (26):
                Deletes the backup taken by a backup run.
            RECREATE_REPLICA (27):
                No description available.
            TRUNCATE_LOG (28):
                Truncates a general or slow log table in
                MySQL.
            DEMOTE_MASTER (29):
                Demotes the stand-alone instance to be a
                Cloud SQL read replica for an external database
                server.
            MAINTENANCE (30):
                Indicates that the instance is currently in
                maintenance. Maintenance typically causes the
                instance to be unavailable for 1-3 minutes.
            ENABLE_PRIVATE_IP (31):
                This field is deprecated, and will be removed
                in future version of API.
            DEFER_MAINTENANCE (32):
                No description available.
            CREATE_CLONE (33):
                Creates clone instance.
            RESCHEDULE_MAINTENANCE (34):
                Reschedule maintenance to another time.
            START_EXTERNAL_SYNC (35):
                Starts external sync of a Cloud SQL EM
                replica to an external primary instance.
            LOG_CLEANUP (36):
                Recovers logs from an instance's old data
                disk.
            AUTO_RESTART (37):
                Performs auto-restart of an HA-enabled Cloud
                SQL database for auto recovery.
            REENCRYPT (38):
                Re-encrypts CMEK instances with latest key
                version.
            SWITCHOVER (39):
                Switches the roles of the primary and replica
                pair. The target instance should be the replica.
            UPDATE_BACKUP (40):
                Update a backup.
            ACQUIRE_SSRS_LEASE (42):
                Acquire a lease for the setup of SQL Server
                Reporting Services (SSRS).
            RELEASE_SSRS_LEASE (43):
                Release a lease for the setup of SQL Server
                Reporting Services (SSRS).
            RECONFIGURE_OLD_PRIMARY (44):
                Reconfigures old primary after a promote
                replica operation. Effect of a promote operation
                to the old primary is executed in this
                operation, asynchronously from the promote
                replica operation executed to the replica.
            CLUSTER_MAINTENANCE (45):
                Indicates that the instance, its read
                replicas, and its cascading replicas are in
                maintenance. Maintenance typically gets
                initiated on groups of replicas first, followed
                by the primary instance. For each instance,
                maintenance typically causes the instance to be
                unavailable for 1-3 minutes.
            SELF_SERVICE_MAINTENANCE (46):
                Indicates that the instance (and any of its
                replicas) are currently in maintenance. This is
                initiated as a self-service request by using
                SSM. Maintenance typically causes the instance
                to be unavailable for 1-3 minutes.
            SWITCHOVER_TO_REPLICA (47):
                Switches a primary instance to a replica.
                This operation runs as part of a switchover
                operation to the original primary instance.
            MAJOR_VERSION_UPGRADE (48):
                Updates the major version of a Cloud SQL
                instance.
            ADVANCED_BACKUP (49):
                Deprecated: ADVANCED_BACKUP is deprecated. Use
                ENHANCED_BACKUP instead.
            MANAGE_BACKUP (50):
                Changes the BackupTier of a Cloud SQL
                instance.
            ENHANCED_BACKUP (51):
                Creates a backup for an Enhanced BackupTier
                Cloud SQL instance.
            REPAIR_READ_POOL (52):
                Repairs entire read pool or specified read
                pool nodes in the read pool.
            CREATE_READ_POOL (53):
                Creates a Cloud SQL read pool instance.
            PRE_CHECK_MAJOR_VERSION_UPGRADE (54):
                Pre-checks for major version upgrade.
            CREATE_BLUE_GREEN_DEPLOYMENT (55):
                Creates a new Blue-Green deployment.
            SWITCHOVER_BLUE_GREEN_DEPLOYMENT (56):
                Switches over a Blue-Green deployment.
            DELETE_BLUE_GREEN_DEPLOYMENT (57):
                Deletes a Blue-Green deployment.
            SETUP_MIGRATION (58):
                This operation type represents individual
                steps in a multi-step setup migration workflow:
                including configuration, replication,
                switchover/back, and data reseeding, as defined
                by operation's intent.
            AGENT_SEND_MESSAGE (59):
                Sends a message to a Cloud SQL agent.
        """

        SQL_OPERATION_TYPE_UNSPECIFIED = 0
        IMPORT = 1
        EXPORT = 2
        CREATE = 3
        UPDATE = 4
        DELETE = 5
        RESTART = 6
        BACKUP = 7
        SNAPSHOT = 8
        BACKUP_VOLUME = 9
        DELETE_VOLUME = 10
        RESTORE_VOLUME = 11
        INJECT_USER = 12
        CLONE = 14
        STOP_REPLICA = 15
        START_REPLICA = 16
        PROMOTE_REPLICA = 17
        CREATE_REPLICA = 18
        CREATE_USER = 19
        DELETE_USER = 20
        UPDATE_USER = 21
        CREATE_DATABASE = 22
        DELETE_DATABASE = 23
        UPDATE_DATABASE = 24
        FAILOVER = 25
        DELETE_BACKUP = 26
        RECREATE_REPLICA = 27
        TRUNCATE_LOG = 28
        DEMOTE_MASTER = 29
        MAINTENANCE = 30
        ENABLE_PRIVATE_IP = 31
        DEFER_MAINTENANCE = 32
        CREATE_CLONE = 33
        RESCHEDULE_MAINTENANCE = 34
        START_EXTERNAL_SYNC = 35
        LOG_CLEANUP = 36
        AUTO_RESTART = 37
        REENCRYPT = 38
        SWITCHOVER = 39
        UPDATE_BACKUP = 40
        ACQUIRE_SSRS_LEASE = 42
        RELEASE_SSRS_LEASE = 43
        RECONFIGURE_OLD_PRIMARY = 44
        CLUSTER_MAINTENANCE = 45
        SELF_SERVICE_MAINTENANCE = 46
        SWITCHOVER_TO_REPLICA = 47
        MAJOR_VERSION_UPGRADE = 48
        ADVANCED_BACKUP = 49
        MANAGE_BACKUP = 50
        ENHANCED_BACKUP = 51
        REPAIR_READ_POOL = 52
        CREATE_READ_POOL = 53
        PRE_CHECK_MAJOR_VERSION_UPGRADE = 54
        CREATE_BLUE_GREEN_DEPLOYMENT = 55
        SWITCHOVER_BLUE_GREEN_DEPLOYMENT = 56
        DELETE_BLUE_GREEN_DEPLOYMENT = 57
        SETUP_MIGRATION = 58
        AGENT_SEND_MESSAGE = 59

    class SqlOperationStatus(proto.Enum):
        r"""The status of an operation.

        Values:
            SQL_OPERATION_STATUS_UNSPECIFIED (0):
                The state of the operation is unknown.
            PENDING (1):
                The operation has been queued, but has not
                started yet.
            RUNNING (2):
                The operation is running.
            DONE (3):
                The operation completed.
        """

        SQL_OPERATION_STATUS_UNSPECIFIED = 0
        PENDING = 1
        RUNNING = 2
        DONE = 3

    kind: str = proto.Field(
        proto.STRING,
        number=1,
    )
    target_link: str = proto.Field(
        proto.STRING,
        number=2,
    )
    status: SqlOperationStatus = proto.Field(
        proto.ENUM,
        number=3,
        enum=SqlOperationStatus,
    )
    user: str = proto.Field(
        proto.STRING,
        number=4,
    )
    insert_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    error: "OperationErrors" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="OperationErrors",
    )
    api_warning: "ApiWarning" = proto.Field(
        proto.MESSAGE,
        number=19,
        message="ApiWarning",
    )
    operation_type: SqlOperationType = proto.Field(
        proto.ENUM,
        number=9,
        enum=SqlOperationType,
    )
    import_context: "ImportContext" = proto.Field(
        proto.MESSAGE,
        number=10,
        message="ImportContext",
    )
    export_context: "ExportContext" = proto.Field(
        proto.MESSAGE,
        number=11,
        message="ExportContext",
    )
    backup_context: "BackupContext" = proto.Field(
        proto.MESSAGE,
        number=17,
        message="BackupContext",
    )
    pre_check_major_version_upgrade_context: "PreCheckMajorVersionUpgradeContext" = (
        proto.Field(
            proto.MESSAGE,
            number=50,
            message="PreCheckMajorVersionUpgradeContext",
        )
    )
    start_workload_capture_context: "StartWorkloadCaptureContext" = proto.Field(
        proto.MESSAGE,
        number=56,
        message="StartWorkloadCaptureContext",
    )
    stop_workload_capture_context: "StopWorkloadCaptureContext" = proto.Field(
        proto.MESSAGE,
        number=57,
        message="StopWorkloadCaptureContext",
    )
    start_workload_replay_context: "StartWorkloadReplayContext" = proto.Field(
        proto.MESSAGE,
        number=58,
        message="StartWorkloadReplayContext",
    )
    stop_workload_replay_context: "StopWorkloadReplayContext" = proto.Field(
        proto.MESSAGE,
        number=59,
        message="StopWorkloadReplayContext",
    )
    name: str = proto.Field(
        proto.STRING,
        number=12,
    )
    target_id: str = proto.Field(
        proto.STRING,
        number=13,
    )
    self_link: str = proto.Field(
        proto.STRING,
        number=14,
    )
    target_project: str = proto.Field(
        proto.STRING,
        number=15,
    )
    acquire_ssrs_lease_context: "AcquireSsrsLeaseContext" = proto.Field(
        proto.MESSAGE,
        number=20,
        message="AcquireSsrsLeaseContext",
    )
    sub_operation_type: "SqlSubOperationType" = proto.Field(
        proto.MESSAGE,
        number=48,
        message="SqlSubOperationType",
    )


class OperationError(proto.Message):
    r"""Database instance operation error.

    Attributes:
        kind (str):
            This is always ``sql#operationError``.
        code (str):
            Identifies the specific error that occurred.
        message (str):
            Additional information about the error
            encountered.
    """

    kind: str = proto.Field(
        proto.STRING,
        number=1,
    )
    code: str = proto.Field(
        proto.STRING,
        number=2,
    )
    message: str = proto.Field(
        proto.STRING,
        number=3,
    )


class OperationErrors(proto.Message):
    r"""Database instance operation errors list wrapper.

    Attributes:
        kind (str):
            This is always ``sql#operationErrors``.
        errors (MutableSequence[google.cloud.sqladmin_v1beta4.types.OperationError]):
            The list of errors encountered while
            processing this operation.
    """

    kind: str = proto.Field(
        proto.STRING,
        number=1,
    )
    errors: MutableSequence["OperationError"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="OperationError",
    )


class PasswordValidationPolicy(proto.Message):
    r"""Database instance local user password validation policy.
    This message defines the password policy for local database
    users. When enabled, it enforces constraints on password
    complexity, length, and reuse. Keep this policy enabled to help
    prevent unauthorized access.

    Attributes:
        min_length (google.protobuf.wrappers_pb2.Int32Value):
            Minimum number of characters allowed.
        complexity (google.cloud.sqladmin_v1beta4.types.PasswordValidationPolicy.Complexity):
            The complexity of the password.
        reuse_interval (google.protobuf.wrappers_pb2.Int32Value):
            Number of previous passwords that cannot be
            reused.
        disallow_username_substring (google.protobuf.wrappers_pb2.BoolValue):
            Disallow username as a part of the password.
        password_change_interval (google.protobuf.duration_pb2.Duration):
            Minimum interval after which the password can
            be changed. This flag is only supported for
            PostgreSQL.
        enable_password_policy (google.protobuf.wrappers_pb2.BoolValue):
            Whether to enable the password policy or not.
            When enabled, passwords must meet complexity
            requirements. Keep this policy enabled to help
            prevent unauthorized access. Disabling this
            policy allows weak passwords.
        disallow_compromised_credentials (google.protobuf.wrappers_pb2.BoolValue):
            This field is deprecated and will be removed
            in a future version of the API.
    """

    class Complexity(proto.Enum):
        r"""The complexity choices of the password.

        Values:
            COMPLEXITY_UNSPECIFIED (0):
                Complexity check is not specified.
            COMPLEXITY_DEFAULT (1):
                A combination of lowercase, uppercase,
                numeric, and non-alphanumeric characters.
        """

        COMPLEXITY_UNSPECIFIED = 0
        COMPLEXITY_DEFAULT = 1

    min_length: wrappers_pb2.Int32Value = proto.Field(
        proto.MESSAGE,
        number=1,
        message=wrappers_pb2.Int32Value,
    )
    complexity: Complexity = proto.Field(
        proto.ENUM,
        number=2,
        enum=Complexity,
    )
    reuse_interval: wrappers_pb2.Int32Value = proto.Field(
        proto.MESSAGE,
        number=3,
        message=wrappers_pb2.Int32Value,
    )
    disallow_username_substring: wrappers_pb2.BoolValue = proto.Field(
        proto.MESSAGE,
        number=4,
        message=wrappers_pb2.BoolValue,
    )
    password_change_interval: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=5,
        message=duration_pb2.Duration,
    )
    enable_password_policy: wrappers_pb2.BoolValue = proto.Field(
        proto.MESSAGE,
        number=6,
        message=wrappers_pb2.BoolValue,
    )
    disallow_compromised_credentials: wrappers_pb2.BoolValue = proto.Field(
        proto.MESSAGE,
        number=7,
        message=wrappers_pb2.BoolValue,
    )


class OperationsListResponse(proto.Message):
    r"""Operations list response.

    Attributes:
        kind (str):
            This is always ``sql#operationsList``.
        items (MutableSequence[google.cloud.sqladmin_v1beta4.types.Operation]):
            List of operation resources.
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
    items: MutableSequence["Operation"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="Operation",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ReplicaConfiguration(proto.Message):
    r"""Read-replica configuration for connecting to the primary
    instance.

    Attributes:
        kind (str):
            This is always ``sql#replicaConfiguration``.
        mysql_replica_configuration (google.cloud.sqladmin_v1beta4.types.MySqlReplicaConfiguration):
            MySQL specific configuration when replicating from a MySQL
            on-premises primary instance. Replication configuration
            information such as the username, password, certificates,
            and keys are not stored in the instance metadata. The
            configuration information is used only to set up the
            replication connection and is stored by MySQL in a file
            named ``master.info`` in the data directory.
        failover_target (google.protobuf.wrappers_pb2.BoolValue):
            Specifies if the replica is the failover target. If the
            field is set to ``true`` the replica will be designated as a
            failover replica. In case the primary instance fails, the
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
    mysql_replica_configuration: "MySqlReplicaConfiguration" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="MySqlReplicaConfiguration",
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


class RotateEntraIdCertificateContext(proto.Message):
    r"""Instance rotate Entra ID certificate context.

    Attributes:
        kind (str):
            Optional. This is always
            ``sql#rotateEntraIdCertificateContext``.
        next_version (str):
            Optional. The fingerprint of the next version
            to be rotated to. If left unspecified, will be
            rotated to the most recently added Entra ID
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


class DataCacheConfig(proto.Message):
    r"""Data cache configurations.

    Attributes:
        data_cache_enabled (bool):
            Whether data cache is enabled for the
            instance.
    """

    data_cache_enabled: bool = proto.Field(
        proto.BOOL,
        number=1,
    )


class FinalBackupConfig(proto.Message):
    r"""Config used to determine the final backup settings for the
    instance.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        enabled (bool):
            Whether the final backup is enabled for the
            instance.

            This field is a member of `oneof`_ ``_enabled``.
        retention_days (int):
            The number of days to retain the final backup after the
            instance deletion. The final backup will be purged at
            (time_of_instance_deletion + retention_days).

            This field is a member of `oneof`_ ``_retention_days``.
    """

    enabled: bool = proto.Field(
        proto.BOOL,
        number=1,
        optional=True,
    )
    retention_days: int = proto.Field(
        proto.INT32,
        number=3,
        optional=True,
    )


class Settings(proto.Message):
    r"""Database instance settings.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        settings_version (google.protobuf.wrappers_pb2.Int64Value):
            The version of instance settings. This is a
            required field for update method to make sure
            concurrent updates are handled properly. During
            update, use the most recent settingsVersion
            value for this instance and do not try to update
            this value.
        authorized_gae_applications (MutableSequence[str]):
            The App Engine app IDs that can access this
            instance. (Deprecated) Applied to First
            Generation instances only.
        tier (str):
            The tier (or machine type) for this instance, for example
            ``db-custom-1-3840``. WARNING: Changing this restarts the
            instance.
        kind (str):
            This is always ``sql#settings``.
        user_labels (MutableMapping[str, str]):
            User-provided labels, represented as a
            dictionary where each label is a single key
            value pair.
        availability_type (google.cloud.sqladmin_v1beta4.types.SqlAvailabilityType):
            Availability type. Potential values:

            - ``ZONAL``: The instance serves data from only one zone.
              Outages in that zone affect data accessibility.
            - ``REGIONAL``: The instance can serve data from more than
              one zone in a region (it is highly available)./

            For more information, see `Overview of the High Availability
            Configuration <https://cloud.google.com/sql/docs/mysql/high-availability>`__.
        pricing_plan (google.cloud.sqladmin_v1beta4.types.SqlPricingPlan):
            The pricing plan for this instance. This can be either
            ``PER_USE`` or ``PACKAGE``. Only ``PER_USE`` is supported
            for Second Generation instances.
        replication_type (google.cloud.sqladmin_v1beta4.types.SqlReplicationType):
            The type of replication this instance uses. This can be
            either ``ASYNCHRONOUS`` or ``SYNCHRONOUS``. (Deprecated)
            This property was only applicable to First Generation
            instances.
        storage_auto_resize_limit (google.protobuf.wrappers_pb2.Int64Value):
            The maximum size to which storage capacity
            can be automatically increased. The default
            value is 0, which specifies that there is no
            limit.
        activation_policy (google.cloud.sqladmin_v1beta4.types.Settings.SqlActivationPolicy):
            The activation policy specifies when the instance is
            activated; it is applicable only when the instance state is
            RUNNABLE. Valid values:

            - ``ALWAYS``: The instance is on, and remains so even in the
              absence of connection requests.
            - ``NEVER``: The instance is off; it is not activated, even
              if a connection request arrives.
        ip_configuration (google.cloud.sqladmin_v1beta4.types.IpConfiguration):
            The settings for IP Management. This allows
            to enable or disable the instance IP and manage
            which external networks can connect to the
            instance. The IPv4 address cannot be disabled
            for Second Generation instances.
        storage_auto_resize (google.protobuf.wrappers_pb2.BoolValue):
            Configuration to increase storage size
            automatically. The default value is true.
        location_preference (google.cloud.sqladmin_v1beta4.types.LocationPreference):
            The location preference settings. This allows
            the instance to be located as near as possible
            to either an App Engine app or Compute Engine
            zone for better performance. App Engine
            co-location was only applicable to First
            Generation instances.
        database_flags (MutableSequence[google.cloud.sqladmin_v1beta4.types.DatabaseFlags]):
            The database flags passed to the instance at
            startup.
        data_disk_type (google.cloud.sqladmin_v1beta4.types.SqlDataDiskType):
            The type of data disk: ``PD_SSD`` (default) or ``PD_HDD``.
            Not used for First Generation instances.
        maintenance_window (google.cloud.sqladmin_v1beta4.types.MaintenanceWindow):
            The maintenance window for this instance.
            This specifies when the instance can be
            restarted for maintenance purposes.
        backup_configuration (google.cloud.sqladmin_v1beta4.types.BackupConfiguration):
            The daily backup configuration for the
            instance.
        database_replication_enabled (google.protobuf.wrappers_pb2.BoolValue):
            Configuration specific to read replica
            instances. Indicates whether replication is
            enabled or not. WARNING: Changing this restarts
            the instance.
        crash_safe_replication_enabled (google.protobuf.wrappers_pb2.BoolValue):
            Configuration specific to read replica
            instances. Indicates whether database flags for
            crash-safe replication are enabled. This
            property was only applicable to First Generation
            instances.
        data_disk_size_gb (google.protobuf.wrappers_pb2.Int64Value):
            The size of data disk, in GB. The data disk
            size minimum is 10GB.
        active_directory_config (google.cloud.sqladmin_v1beta4.types.SqlActiveDirectoryConfig):
            Active Directory configuration, relevant only
            for Cloud SQL for SQL Server.
        collation (str):
            The name of server Instance collation.
        deny_maintenance_periods (MutableSequence[google.cloud.sqladmin_v1beta4.types.DenyMaintenancePeriod]):
            Deny maintenance periods
        insights_config (google.cloud.sqladmin_v1beta4.types.InsightsConfig):
            Insights configuration, for now relevant only
            for Postgres.
        password_validation_policy (google.cloud.sqladmin_v1beta4.types.PasswordValidationPolicy):
            The local user password validation policy of
            the instance for PostgreSQL and MySQL.
        sql_server_audit_config (google.cloud.sqladmin_v1beta4.types.SqlServerAuditConfig):
            SQL Server specific audit configuration.
        edition (google.cloud.sqladmin_v1beta4.types.Settings.Edition):
            Optional. The edition type of the Cloud SQL
            instance.
        connector_enforcement (google.cloud.sqladmin_v1beta4.types.Settings.ConnectorEnforcement):
            Specifies if connections must use Cloud SQL connectors.
            Option values include the following: ``NOT_REQUIRED`` (Cloud
            SQL instances can be connected without Cloud SQL Connectors)
            and ``REQUIRED`` (Only allow connections that use Cloud SQL
            Connectors)

            Note that using REQUIRED disables all existing authorized
            networks. If this field is not specified when creating a new
            instance, NOT_REQUIRED is used. If this field is not
            specified when patching or updating an existing instance, it
            is left unchanged in the instance.
        deletion_protection_enabled (google.protobuf.wrappers_pb2.BoolValue):
            Configuration to protect against accidental
            instance deletion.
        time_zone (str):
            Server timezone, relevant only for Cloud SQL
            for SQL Server.
        advanced_machine_features (google.cloud.sqladmin_v1beta4.types.AdvancedMachineFeatures):
            Specifies advanced machine configuration for
            the instances relevant only for SQL Server.
        data_cache_config (google.cloud.sqladmin_v1beta4.types.DataCacheConfig):
            Configuration for data cache.
        replication_lag_max_seconds (google.protobuf.wrappers_pb2.Int32Value):
            Optional. Configuration value for recreation
            of replica after certain replication lag.
        enable_google_ml_integration (google.protobuf.wrappers_pb2.BoolValue):
            Optional. When this parameter is set to true,
            Cloud SQL instances can connect to Vertex AI to
            pass requests for real-time predictions and
            insights to the AI. The default value is false.
            This applies only to Cloud SQL for MySQL and
            Cloud SQL for PostgreSQL instances.
        enable_dataplex_integration (google.protobuf.wrappers_pb2.BoolValue):
            Optional. By default, Cloud SQL instances
            have schema extraction disabled for Dataplex.
            When this parameter is set to true, schema
            extraction for Dataplex on Cloud SQL instances
            is activated.
        retain_backups_on_delete (google.protobuf.wrappers_pb2.BoolValue):
            Optional. When this parameter is set to true, Cloud SQL
            retains backups of the instance even after the instance is
            deleted. The ON_DEMAND backup will be retained until
            customer deletes the backup or the project. The AUTOMATED
            backup will be retained based on the backups retention
            setting.
        data_disk_provisioned_iops (int):
            Optional. Provisioned number of I/O
            operations per second for the data disk. This
            field is only used for hyperdisk-balanced disk
            types.

            This field is a member of `oneof`_ ``_data_disk_provisioned_iops``.
        data_disk_provisioned_throughput (int):
            Optional. Provisioned throughput measured in
            MiB per second for the data disk. This field is
            only used for hyperdisk-balanced disk types.

            This field is a member of `oneof`_ ``_data_disk_provisioned_throughput``.
        connection_pool_config (google.cloud.sqladmin_v1beta4.types.ConnectionPoolConfig):
            Optional. The managed connection pooling
            configuration for the instance.

            This field is a member of `oneof`_ ``_connection_pool_config``.
        final_backup_config (google.cloud.sqladmin_v1beta4.types.FinalBackupConfig):
            Optional. The final backup configuration for
            the instance.

            This field is a member of `oneof`_ ``_final_backup_config``.
        read_pool_auto_scale_config (google.cloud.sqladmin_v1beta4.types.ReadPoolAutoScaleConfig):
            Optional. The read pool auto-scale
            configuration for the instance.

            This field is a member of `oneof`_ ``_read_pool_auto_scale_config``.
        accelerated_replica_mode (google.protobuf.wrappers_pb2.BoolValue):
            Optional. Configures whether the replica is
            in accelerated mode. This feature is in private
            preview and requires allowlisting to take
            effect.
        auto_upgrade_enabled (bool):
            Optional. Cloud SQL for MySQL auto-upgrade
            configuration. When this parameter is set to
            true, auto-upgrade is enabled for MySQL 8.0
            minor versions. The MySQL version must be 8.0.35
            or higher.

            This field is a member of `oneof`_ ``_auto_upgrade_enabled``.
        entraid_config (google.cloud.sqladmin_v1beta4.types.SqlServerEntraIdConfig):
            Optional. The Microsoft Entra ID
            configuration for the SQL Server instance.
        data_api_access (google.cloud.sqladmin_v1beta4.types.Settings.DataApiAccess):
            This parameter controls whether to allow
            using ExecuteSql API to connect to the instance.
            Not allowed by default.

            This field is a member of `oneof`_ ``_data_api_access``.
        performance_capture_config (google.cloud.sqladmin_v1beta4.types.PerformanceCaptureConfig):
            Optional. Configuration for Performance
            Capture, provides diagnostic metrics during high
            load situations.
    """

    class SqlActivationPolicy(proto.Enum):
        r"""Specifies when the instance is activated.

        Values:
            SQL_ACTIVATION_POLICY_UNSPECIFIED (0):
                Unknown activation plan.
            ALWAYS (1):
                The instance is always up and running.
            NEVER (2):
                The instance never starts.
            ON_DEMAND (3):
                The instance starts upon receiving requests.
        """

        SQL_ACTIVATION_POLICY_UNSPECIFIED = 0
        ALWAYS = 1
        NEVER = 2
        ON_DEMAND = 3

    class Edition(proto.Enum):
        r"""The list of Cloud SQL editions available to users.

        Values:
            EDITION_UNSPECIFIED (0):
                The instance did not specify the edition.
            ENTERPRISE (2):
                The instance is an enterprise edition.
            ENTERPRISE_PLUS (3):
                The instance is an Enterprise Plus edition.
            DEVELOPER (5):
                This instance is a Cloud SQL developer
                edition instance.
        """

        EDITION_UNSPECIFIED = 0
        ENTERPRISE = 2
        ENTERPRISE_PLUS = 3
        DEVELOPER = 5

    class ConnectorEnforcement(proto.Enum):
        r"""The options for enforcing Cloud SQL connectors in the
        instance.

        Values:
            CONNECTOR_ENFORCEMENT_UNSPECIFIED (0):
                The requirement for Cloud SQL connectors is
                unknown.
            NOT_REQUIRED (1):
                Do not require Cloud SQL connectors.
            REQUIRED (2):
                Require all connections to use Cloud SQL
                connectors, including the Cloud SQL Auth Proxy
                and Cloud SQL Java, Python, and Go connectors.
                Note: This disables all existing authorized
                networks.
        """

        CONNECTOR_ENFORCEMENT_UNSPECIFIED = 0
        NOT_REQUIRED = 1
        REQUIRED = 2

    class DataApiAccess(proto.Enum):
        r"""ExecuteSql API's access to the instance.

        Values:
            DATA_API_ACCESS_UNSPECIFIED (0):
                Unspecified, effectively the same as ``DISALLOW_DATA_API``.
            DISALLOW_DATA_API (1):
                Disallow using ExecuteSql API to connect to
                the instance.
            ALLOW_DATA_API (2):
                Allow using ExecuteSql API to connect to the
                instance. For private IP instances, this allows
                authorized users to access the instance from the
                public internet using ExecuteSql API.
        """

        DATA_API_ACCESS_UNSPECIFIED = 0
        DISALLOW_DATA_API = 1
        ALLOW_DATA_API = 2

    settings_version: wrappers_pb2.Int64Value = proto.Field(
        proto.MESSAGE,
        number=1,
        message=wrappers_pb2.Int64Value,
    )
    authorized_gae_applications: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    tier: str = proto.Field(
        proto.STRING,
        number=3,
    )
    kind: str = proto.Field(
        proto.STRING,
        number=4,
    )
    user_labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )
    availability_type: "SqlAvailabilityType" = proto.Field(
        proto.ENUM,
        number=6,
        enum="SqlAvailabilityType",
    )
    pricing_plan: "SqlPricingPlan" = proto.Field(
        proto.ENUM,
        number=7,
        enum="SqlPricingPlan",
    )
    replication_type: "SqlReplicationType" = proto.Field(
        proto.ENUM,
        number=8,
        enum="SqlReplicationType",
    )
    storage_auto_resize_limit: wrappers_pb2.Int64Value = proto.Field(
        proto.MESSAGE,
        number=9,
        message=wrappers_pb2.Int64Value,
    )
    activation_policy: SqlActivationPolicy = proto.Field(
        proto.ENUM,
        number=10,
        enum=SqlActivationPolicy,
    )
    ip_configuration: "IpConfiguration" = proto.Field(
        proto.MESSAGE,
        number=11,
        message="IpConfiguration",
    )
    storage_auto_resize: wrappers_pb2.BoolValue = proto.Field(
        proto.MESSAGE,
        number=12,
        message=wrappers_pb2.BoolValue,
    )
    location_preference: "LocationPreference" = proto.Field(
        proto.MESSAGE,
        number=13,
        message="LocationPreference",
    )
    database_flags: MutableSequence["DatabaseFlags"] = proto.RepeatedField(
        proto.MESSAGE,
        number=14,
        message="DatabaseFlags",
    )
    data_disk_type: "SqlDataDiskType" = proto.Field(
        proto.ENUM,
        number=15,
        enum="SqlDataDiskType",
    )
    maintenance_window: "MaintenanceWindow" = proto.Field(
        proto.MESSAGE,
        number=16,
        message="MaintenanceWindow",
    )
    backup_configuration: "BackupConfiguration" = proto.Field(
        proto.MESSAGE,
        number=17,
        message="BackupConfiguration",
    )
    database_replication_enabled: wrappers_pb2.BoolValue = proto.Field(
        proto.MESSAGE,
        number=18,
        message=wrappers_pb2.BoolValue,
    )
    crash_safe_replication_enabled: wrappers_pb2.BoolValue = proto.Field(
        proto.MESSAGE,
        number=19,
        message=wrappers_pb2.BoolValue,
    )
    data_disk_size_gb: wrappers_pb2.Int64Value = proto.Field(
        proto.MESSAGE,
        number=20,
        message=wrappers_pb2.Int64Value,
    )
    active_directory_config: "SqlActiveDirectoryConfig" = proto.Field(
        proto.MESSAGE,
        number=22,
        message="SqlActiveDirectoryConfig",
    )
    collation: str = proto.Field(
        proto.STRING,
        number=23,
    )
    deny_maintenance_periods: MutableSequence["DenyMaintenancePeriod"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=24,
            message="DenyMaintenancePeriod",
        )
    )
    insights_config: "InsightsConfig" = proto.Field(
        proto.MESSAGE,
        number=25,
        message="InsightsConfig",
    )
    password_validation_policy: "PasswordValidationPolicy" = proto.Field(
        proto.MESSAGE,
        number=27,
        message="PasswordValidationPolicy",
    )
    sql_server_audit_config: "SqlServerAuditConfig" = proto.Field(
        proto.MESSAGE,
        number=29,
        message="SqlServerAuditConfig",
    )
    edition: Edition = proto.Field(
        proto.ENUM,
        number=38,
        enum=Edition,
    )
    connector_enforcement: ConnectorEnforcement = proto.Field(
        proto.ENUM,
        number=32,
        enum=ConnectorEnforcement,
    )
    deletion_protection_enabled: wrappers_pb2.BoolValue = proto.Field(
        proto.MESSAGE,
        number=33,
        message=wrappers_pb2.BoolValue,
    )
    time_zone: str = proto.Field(
        proto.STRING,
        number=34,
    )
    advanced_machine_features: "AdvancedMachineFeatures" = proto.Field(
        proto.MESSAGE,
        number=35,
        message="AdvancedMachineFeatures",
    )
    data_cache_config: "DataCacheConfig" = proto.Field(
        proto.MESSAGE,
        number=37,
        message="DataCacheConfig",
    )
    replication_lag_max_seconds: wrappers_pb2.Int32Value = proto.Field(
        proto.MESSAGE,
        number=39,
        message=wrappers_pb2.Int32Value,
    )
    enable_google_ml_integration: wrappers_pb2.BoolValue = proto.Field(
        proto.MESSAGE,
        number=40,
        message=wrappers_pb2.BoolValue,
    )
    enable_dataplex_integration: wrappers_pb2.BoolValue = proto.Field(
        proto.MESSAGE,
        number=41,
        message=wrappers_pb2.BoolValue,
    )
    retain_backups_on_delete: wrappers_pb2.BoolValue = proto.Field(
        proto.MESSAGE,
        number=42,
        message=wrappers_pb2.BoolValue,
    )
    data_disk_provisioned_iops: int = proto.Field(
        proto.INT64,
        number=43,
        optional=True,
    )
    data_disk_provisioned_throughput: int = proto.Field(
        proto.INT64,
        number=44,
        optional=True,
    )
    connection_pool_config: "ConnectionPoolConfig" = proto.Field(
        proto.MESSAGE,
        number=45,
        optional=True,
        message="ConnectionPoolConfig",
    )
    final_backup_config: "FinalBackupConfig" = proto.Field(
        proto.MESSAGE,
        number=47,
        optional=True,
        message="FinalBackupConfig",
    )
    read_pool_auto_scale_config: "ReadPoolAutoScaleConfig" = proto.Field(
        proto.MESSAGE,
        number=48,
        optional=True,
        message="ReadPoolAutoScaleConfig",
    )
    accelerated_replica_mode: wrappers_pb2.BoolValue = proto.Field(
        proto.MESSAGE,
        number=49,
        message=wrappers_pb2.BoolValue,
    )
    auto_upgrade_enabled: bool = proto.Field(
        proto.BOOL,
        number=50,
        optional=True,
    )
    entraid_config: "SqlServerEntraIdConfig" = proto.Field(
        proto.MESSAGE,
        number=52,
        message="SqlServerEntraIdConfig",
    )
    data_api_access: DataApiAccess = proto.Field(
        proto.ENUM,
        number=53,
        optional=True,
        enum=DataApiAccess,
    )
    performance_capture_config: "PerformanceCaptureConfig" = proto.Field(
        proto.MESSAGE,
        number=54,
        message="PerformanceCaptureConfig",
    )


class PerformanceCaptureConfig(proto.Message):
    r"""Performance capture configuration.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        enabled (bool):
            Optional. Enables or disables the performance
            capture feature.

            This field is a member of `oneof`_ ``_enabled``.
        probing_interval_seconds (int):
            Optional. Specifies the interval in seconds
            between consecutive probes that check if any
            trigger condition thresholds have been reached.

            This field is a member of `oneof`_ ``_probing_interval_seconds``.
        probe_threshold (int):
            Optional. Specifies the minimum number of
            consecutive probe threshold that triggers
            performance capture.

            This field is a member of `oneof`_ ``_probe_threshold``.
        running_threads_threshold (int):
            Optional. Specifies the minimum number of MySQL
            ``Threads_running`` to trigger the performance capture on
            the primary instance.

            This field is a member of `oneof`_ ``_running_threads_threshold``.
        seconds_behind_source_threshold (int):
            Optional. Specifies the minimum number of
            seconds replica must be lagging behind primary
            instance to trigger the performance capture on
            replica.

            This field is a member of `oneof`_ ``_seconds_behind_source_threshold``.
        transaction_duration_threshold (int):
            Optional. Specifies the amount of time in
            seconds that a transaction needs to have been
            open before the watcher starts recording it.

            This field is a member of `oneof`_ ``_transaction_duration_threshold``.
        cpu_utilization_threshold_percent (int):
            Optional. Specifies the minimum percentage of CPU
            utilization to trigger the performance capture. Valid
            integers range from ``10`` to ``99``. Enter ``0`` to disable
            the check.

            This field is a member of `oneof`_ ``_cpu_utilization_threshold_percent``.
        memory_usage_threshold_percent (int):
            Optional. Specifies the minimum percentage of memory usage
            to trigger the performance capture. Valid integers range
            from ``10`` to ``99``. Enter ``0`` to disable the check.

            This field is a member of `oneof`_ ``_memory_usage_threshold_percent``.
        transaction_lock_wait_threshold_count (int):
            Optional. Specifies the minimum allowed number of
            transactions in lock wait state to trigger the performance
            capture. Valid integers range from ``10`` to ``10000``.
            Enter ``0`` to disable the check.

            This field is a member of `oneof`_ ``_transaction_lock_wait_threshold_count``.
        semaphore_wait_threshold_count (int):
            Optional. Specifies the minimum allowed number of semaphore
            waits to trigger the performance capture. Valid integers
            range from ``10`` to ``10000``. Enter ``0`` to disable the
            check.

            This field is a member of `oneof`_ ``_semaphore_wait_threshold_count``.
        history_list_length_threshold_count (int):
            Optional. Specifies the minimum number of undo log entries
            in the history list length to trigger the performance
            capture. Valid integers range from ``10000`` to
            ``10000000``. Enter ``0`` to disable the check.

            This field is a member of `oneof`_ ``_history_list_length_threshold_count``.
        transaction_kill_threshold_seconds (int):
            Optional. Specifies the amount of time in seconds that a
            transaction needs to have been open before the watcher
            starts terminating it. Valid integers range from ``60`` to
            ``604800`` (7 days). Enter ``0`` to disable. If enabled
            (i.e., > 0), this value must be greater than or equal to
            ``transaction_duration_threshold``. Configurations where
            ``0 < transaction_kill_threshold_seconds < transaction_duration_threshold``
            will be rejected.

            This field is a member of `oneof`_ ``_transaction_kill_threshold_seconds``.
        transaction_kill_excluded_user_hosts (MutableSequence[str]):
            Optional. Specifies a customer-defined list of users to
            exclude from transaction termination. Entries can be in the
            format 'user@host' or just 'user'. A standalone 'user'
            implies 'user@%', excluding the user from any host. Wildcard
            '%' is allowed in the host part of the 'user@host' format.
            Example:
            ``["app_user", "db_admin@10.1.2.3", "report_user@%"]``
        transaction_kill_type (google.cloud.sqladmin_v1beta4.types.PerformanceCaptureConfig.TransactionKillType):
            Optional. Determines which transactions are allowed to be
            terminated when they exceed
            ``transaction_kill_threshold_seconds``. This allows
            protecting write-heavy transactions from auto-termination if
            desired. Defaults to ``READ_ONLY_TRANSACTIONS`` if
            unspecified.

            This field is a member of `oneof`_ ``_transaction_kill_type``.
    """

    class TransactionKillType(proto.Enum):
        r"""Defines the categories of long-running transactions eligible
        for automatic termination by the Performance Capture.

        Values:
            TRANSACTION_KILL_TYPE_UNSPECIFIED (0):
                Unspecified.
            READ_ONLY_TRANSACTIONS (1):
                Only read-only transactions are eligible for
                termination.
            ALL_TRANSACTIONS (2):
                All transactions are eligible for
                termination, including those with write
                operations (such as INSERT, UPDATE, DELETE, or
                DDL).
        """

        TRANSACTION_KILL_TYPE_UNSPECIFIED = 0
        READ_ONLY_TRANSACTIONS = 1
        ALL_TRANSACTIONS = 2

    enabled: bool = proto.Field(
        proto.BOOL,
        number=1,
        optional=True,
    )
    probing_interval_seconds: int = proto.Field(
        proto.INT32,
        number=2,
        optional=True,
    )
    probe_threshold: int = proto.Field(
        proto.INT32,
        number=3,
        optional=True,
    )
    running_threads_threshold: int = proto.Field(
        proto.INT32,
        number=4,
        optional=True,
    )
    seconds_behind_source_threshold: int = proto.Field(
        proto.INT32,
        number=5,
        optional=True,
    )
    transaction_duration_threshold: int = proto.Field(
        proto.INT32,
        number=8,
        optional=True,
    )
    cpu_utilization_threshold_percent: int = proto.Field(
        proto.INT32,
        number=9,
        optional=True,
    )
    memory_usage_threshold_percent: int = proto.Field(
        proto.INT32,
        number=10,
        optional=True,
    )
    transaction_lock_wait_threshold_count: int = proto.Field(
        proto.INT32,
        number=11,
        optional=True,
    )
    semaphore_wait_threshold_count: int = proto.Field(
        proto.INT32,
        number=12,
        optional=True,
    )
    history_list_length_threshold_count: int = proto.Field(
        proto.INT32,
        number=13,
        optional=True,
    )
    transaction_kill_threshold_seconds: int = proto.Field(
        proto.INT32,
        number=14,
        optional=True,
    )
    transaction_kill_excluded_user_hosts: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=16,
    )
    transaction_kill_type: TransactionKillType = proto.Field(
        proto.ENUM,
        number=17,
        optional=True,
        enum=TransactionKillType,
    )


class AdvancedMachineFeatures(proto.Message):
    r"""Specifies options for controlling advanced machine features.

    Attributes:
        threads_per_core (int):
            The number of threads per physical core.
    """

    threads_per_core: int = proto.Field(
        proto.INT32,
        number=1,
    )


class SslCert(proto.Message):
    r"""SslCerts Resource

    Attributes:
        kind (str):
            This is always ``sql#sslCert``.
        cert_serial_number (str):
            Serial number, as extracted from the
            certificate.
        cert (str):
            PEM representation.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            The time when the certificate was created in `RFC
            3339 <https://tools.ietf.org/html/rfc3339>`__ format, for
            example ``2012-11-15T16:19:00.094Z``.
        common_name (str):
            User supplied name. Constrained to [a-zA-Z.-\_ ]+.
        expiration_time (google.protobuf.timestamp_pb2.Timestamp):
            The time when the certificate expires in `RFC
            3339 <https://tools.ietf.org/html/rfc3339>`__ format, for
            example ``2012-11-15T16:19:00.094Z``.
        sha1_fingerprint (str):
            Sha1 Fingerprint.
        instance (str):
            Name of the database instance.
        self_link (str):
            The URI of this resource.
    """

    kind: str = proto.Field(
        proto.STRING,
        number=1,
    )
    cert_serial_number: str = proto.Field(
        proto.STRING,
        number=2,
    )
    cert: str = proto.Field(
        proto.STRING,
        number=3,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    common_name: str = proto.Field(
        proto.STRING,
        number=5,
    )
    expiration_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    sha1_fingerprint: str = proto.Field(
        proto.STRING,
        number=7,
    )
    instance: str = proto.Field(
        proto.STRING,
        number=8,
    )
    self_link: str = proto.Field(
        proto.STRING,
        number=9,
    )


class SslCertDetail(proto.Message):
    r"""SslCertDetail.

    Attributes:
        cert_info (google.cloud.sqladmin_v1beta4.types.SslCert):
            The public information about the cert.
        cert_private_key (str):
            The private key for the client cert, in pem
            format.  Keep private in order to protect your
            security.
    """

    cert_info: "SslCert" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="SslCert",
    )
    cert_private_key: str = proto.Field(
        proto.STRING,
        number=2,
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


class SslCertsInsertRequest(proto.Message):
    r"""SslCerts insert request.

    Attributes:
        common_name (str):
            User supplied name.  Must be a distinct name
            from the other certificates for this instance.
    """

    common_name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class SqlInstancesRescheduleMaintenanceRequestBody(proto.Message):
    r"""Reschedule options for maintenance windows.

    Attributes:
        reschedule (google.cloud.sqladmin_v1beta4.types.SqlInstancesRescheduleMaintenanceRequestBody.Reschedule):
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
            reschedule_type (google.cloud.sqladmin_v1beta4.types.SqlInstancesRescheduleMaintenanceRequestBody.RescheduleType):
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


class SslCertsInsertResponse(proto.Message):
    r"""SslCert insert response.

    Attributes:
        kind (str):
            This is always ``sql#sslCertsInsert``.
        operation (google.cloud.sqladmin_v1beta4.types.Operation):
            The operation to track the ssl certs insert
            request.
        server_ca_cert (google.cloud.sqladmin_v1beta4.types.SslCert):
            The server Certificate Authority's
            certificate.  If this is missing you can force a
            new one to be generated by calling
            resetSslConfig method on instances resource.
        client_cert (google.cloud.sqladmin_v1beta4.types.SslCertDetail):
            The new client certificate and private key.
    """

    kind: str = proto.Field(
        proto.STRING,
        number=1,
    )
    operation: "Operation" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Operation",
    )
    server_ca_cert: "SslCert" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="SslCert",
    )
    client_cert: "SslCertDetail" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="SslCertDetail",
    )


class SslCertsListResponse(proto.Message):
    r"""SslCerts list response.

    Attributes:
        kind (str):
            This is always ``sql#sslCertsList``.
        items (MutableSequence[google.cloud.sqladmin_v1beta4.types.SslCert]):
            List of client certificates for the instance.
    """

    kind: str = proto.Field(
        proto.STRING,
        number=1,
    )
    items: MutableSequence["SslCert"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="SslCert",
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


class SqlActiveDirectoryConfig(proto.Message):
    r"""Active Directory configuration, relevant only for Cloud SQL
    for SQL Server.

    Attributes:
        kind (str):
            This is always sql#activeDirectoryConfig.
        domain (str):
            The name of the domain (e.g., mydomain.com).
        mode (google.cloud.sqladmin_v1beta4.types.SqlActiveDirectoryConfig.ActiveDirectoryMode):
            Optional. The mode of the Active Directory
            configuration.
        dns_servers (MutableSequence[str]):
            Optional. Domain controller IPv4 addresses
            used to bootstrap Active Directory.
        admin_credential_secret_name (str):
            Optional. The secret manager key storing the
            administrator credential. (e.g.,
            projects/{project}/secrets/{secret}).
        organizational_unit (str):
            Optional. The organizational unit
            distinguished name. This is the full
            hierarchical path to the organizational unit.
    """

    class ActiveDirectoryMode(proto.Enum):
        r"""The modes of Active Directory configuration.

        Values:
            ACTIVE_DIRECTORY_MODE_UNSPECIFIED (0):
                Unspecified mode.
            MANAGED_ACTIVE_DIRECTORY (1):
                Managed Active Directory mode. This is the
                fallback option to maintain backward
                compatibility.
            SELF_MANAGED_ACTIVE_DIRECTORY (2):
                Deprecated: Use CUSTOMER_MANAGED_ACTIVE_DIRECTORY instead.
            CUSTOMER_MANAGED_ACTIVE_DIRECTORY (3):
                Customer-managed Active Directory mode.
        """

        ACTIVE_DIRECTORY_MODE_UNSPECIFIED = 0
        MANAGED_ACTIVE_DIRECTORY = 1
        SELF_MANAGED_ACTIVE_DIRECTORY = 2
        CUSTOMER_MANAGED_ACTIVE_DIRECTORY = 3

    kind: str = proto.Field(
        proto.STRING,
        number=1,
    )
    domain: str = proto.Field(
        proto.STRING,
        number=2,
    )
    mode: ActiveDirectoryMode = proto.Field(
        proto.ENUM,
        number=3,
        enum=ActiveDirectoryMode,
    )
    dns_servers: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    admin_credential_secret_name: str = proto.Field(
        proto.STRING,
        number=5,
    )
    organizational_unit: str = proto.Field(
        proto.STRING,
        number=6,
    )


class SqlServerAuditConfig(proto.Message):
    r"""SQL Server specific audit configuration.

    Attributes:
        kind (str):
            This is always sql#sqlServerAuditConfig
        bucket (str):
            The name of the destination bucket (e.g.,
            gs://mybucket).
        retention_interval (google.protobuf.duration_pb2.Duration):
            How long to keep generated audit files.
        upload_interval (google.protobuf.duration_pb2.Duration):
            How often to upload generated audit files.
    """

    kind: str = proto.Field(
        proto.STRING,
        number=1,
    )
    bucket: str = proto.Field(
        proto.STRING,
        number=2,
    )
    retention_interval: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=3,
        message=duration_pb2.Duration,
    )
    upload_interval: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=4,
        message=duration_pb2.Duration,
    )


class SqlServerEntraIdConfig(proto.Message):
    r"""SQL Server Entra ID configuration.

    Attributes:
        kind (str):
            Output only. This is always
            sql#sqlServerEntraIdConfig
        tenant_id (str):
            Optional. The tenant ID for the Entra ID
            configuration.
        application_id (str):
            Optional. The application ID for the Entra ID
            configuration.
    """

    kind: str = proto.Field(
        proto.STRING,
        number=1,
    )
    tenant_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    application_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ConnectionPoolFlags(proto.Message):
    r"""Connection pool flags for Cloud SQL instances managed
    connection pool configuration.

    Attributes:
        name (str):
            Required. The name of the flag.
        value (str):
            Required. The value of the flag. Boolean flags are set to
            ``on`` for true and ``off`` for false. This field must be
            omitted if the flag doesn't take a value.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    value: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ReadPoolAutoScaleConfig(proto.Message):
    r"""The read pool auto-scale configuration.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        enabled (bool):
            Indicates whether read pool auto scaling is
            enabled.

            This field is a member of `oneof`_ ``_enabled``.
        min_node_count (int):
            Minimum number of read pool nodes to be
            maintained.

            This field is a member of `oneof`_ ``_min_node_count``.
        max_node_count (int):
            Maximum number of read pool nodes to be
            maintained.

            This field is a member of `oneof`_ ``_max_node_count``.
        target_metrics (MutableSequence[google.cloud.sqladmin_v1beta4.types.ReadPoolAutoScaleConfig.TargetMetric]):
            Optional. Target metrics for read pool auto
            scaling.
        disable_scale_in (bool):
            Indicates whether read pool auto scaling
            supports scale in operations (removing nodes).

            This field is a member of `oneof`_ ``_disable_scale_in``.
        scale_in_cooldown_seconds (int):
            The cooldown period for scale in operations.

            This field is a member of `oneof`_ ``_scale_in_cooldown_seconds``.
        scale_out_cooldown_seconds (int):
            The cooldown period for scale out operations.

            This field is a member of `oneof`_ ``_scale_out_cooldown_seconds``.
    """

    class TargetMetric(proto.Message):
        r"""Target metric for read pool auto scaling.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            metric (str):
                The metric name to be used for auto scaling.

                This field is a member of `oneof`_ ``_metric``.
            target_value (float):
                The target value for the metric.

                This field is a member of `oneof`_ ``_target_value``.
        """

        metric: str = proto.Field(
            proto.STRING,
            number=1,
            optional=True,
        )
        target_value: float = proto.Field(
            proto.FLOAT,
            number=2,
            optional=True,
        )

    enabled: bool = proto.Field(
        proto.BOOL,
        number=1,
        optional=True,
    )
    min_node_count: int = proto.Field(
        proto.INT32,
        number=2,
        optional=True,
    )
    max_node_count: int = proto.Field(
        proto.INT32,
        number=3,
        optional=True,
    )
    target_metrics: MutableSequence[TargetMetric] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=TargetMetric,
    )
    disable_scale_in: bool = proto.Field(
        proto.BOOL,
        number=5,
        optional=True,
    )
    scale_in_cooldown_seconds: int = proto.Field(
        proto.INT32,
        number=6,
        optional=True,
    )
    scale_out_cooldown_seconds: int = proto.Field(
        proto.INT32,
        number=7,
        optional=True,
    )


class ConnectionPoolConfig(proto.Message):
    r"""The managed connection pooling configuration.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        connection_pooling_enabled (bool):
            Whether managed connection pooling is
            enabled.

            This field is a member of `oneof`_ ``_connection_pooling_enabled``.
        flags (MutableSequence[google.cloud.sqladmin_v1beta4.types.ConnectionPoolFlags]):
            Optional. List of connection pool
            configuration flags.
        pooler_count (int):
            Output only. Number of connection poolers.

            This field is a member of `oneof`_ ``_pooler_count``.
    """

    connection_pooling_enabled: bool = proto.Field(
        proto.BOOL,
        number=1,
        optional=True,
    )
    flags: MutableSequence["ConnectionPoolFlags"] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message="ConnectionPoolFlags",
    )
    pooler_count: int = proto.Field(
        proto.INT32,
        number=9,
        optional=True,
    )


class AcquireSsrsLeaseContext(proto.Message):
    r"""Acquire SSRS lease context.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        setup_login (str):
            The username to be used as the setup login to
            connect to the database server for SSRS setup.

            This field is a member of `oneof`_ ``_setup_login``.
        service_login (str):
            The username to be used as the service login
            to connect to the report database for SSRS
            setup.

            This field is a member of `oneof`_ ``_service_login``.
        report_database (str):
            The report database to be used for the SSRS
            setup.

            This field is a member of `oneof`_ ``_report_database``.
        duration (google.protobuf.duration_pb2.Duration):
            Lease duration needed for the SSRS setup.

            This field is a member of `oneof`_ ``_duration``.
    """

    setup_login: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    service_login: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    report_database: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )
    duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=4,
        optional=True,
        message=duration_pb2.Duration,
    )


class StartWorkloadCaptureContext(proto.Message):
    r"""The context for the ``StartWorkloadCapture`` operation, which
    contains details to start recording the workload (SQL queries) on a
    Cloud SQL instance.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        enable_live_replay (bool):
            Optional. If true, the captured workload is simultaneously
            executed on a separate, ephemeral Cloud SQL instance. This
            "live replay" instance is automatically provisioned and is
            cloned from the source instance. If false (the default), the
            workload is only stored and no live replay occurs. It can be
            replayed later using a separate
            ``StartWorkloadReplayRequest``. Note: The workload capture
            runs continuously until an explicit
            ``StopWorkloadCaptureRequest`` is issued.
        replay_instance (str):
            Optional. Required if ``enable_live_replay`` is true. The
            name of the Cloud SQL instance where the captured workload
            (SQL queries) is being executed, excluding the project ID
            (for example, ``my-replay-instance``). The instance name
            must start with a lowercase letter and contain only
            lowercase letters, numbers, and hyphens. The combined length
            of ``project-ID:instance-name`` must be 98 characters or
            less.

            This field is a member of `oneof`_ ``_replay_instance``.
    """

    enable_live_replay: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    replay_instance: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )


class StopWorkloadCaptureContext(proto.Message):
    r"""The context for the ``StopWorkloadCapture`` operation, which
    contains details to stop recording the workload (SQL queries) on a
    Cloud SQL instance.

    Attributes:
        abort_live_replay (bool):
            Optional. If true, immediately aborts the
            concurrent live replay and discards any
            un-replayed traffic alongside stopping the
            capture. If false (the default), the capture
            stops recording new traffic, but the live replay
            will continue executing until the entire backlog
            of captured traffic has been replayed.
    """

    abort_live_replay: bool = proto.Field(
        proto.BOOL,
        number=1,
    )


class StartWorkloadReplayContext(proto.Message):
    r"""The context for the ``StartWorkloadReplay`` operation, which
    contains details about starting the execution of a captured workload
    (recorded read and write SQL queries) on a replay instance (the
    Cloud SQL instance where the recorded SQL queries are executed).

    Attributes:
        replay_instance (str):
            Required. The name of the Cloud SQL instance where the
            captured workload (SQL queries) is being executed, excluding
            the project ID (for example, ``my-replay-instance``). The
            instance name must start with a lowercase letter and contain
            only lowercase letters, numbers, and hyphens. The combined
            length of ``project-ID:instance-name`` must be 98 characters
            or less.
        workload_id (str):
            Output only. The ID of the workload to start executing on
            the replay instance. Each workload capture generates a
            unique ID in the format ``workload-<epoch_timestamp>`` (for
            example, ``workload-1786046400``). Use this ID to start
            executing the recorded SQL queries.
    """

    replay_instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    workload_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class StopWorkloadReplayContext(proto.Message):
    r"""The context for the ``StopWorkloadReplay`` operation, which
    represents an operation that stops an active workload replay on a
    target Cloud SQL replay instance.

    """


__all__ = tuple(sorted(__protobuf__.manifest))
