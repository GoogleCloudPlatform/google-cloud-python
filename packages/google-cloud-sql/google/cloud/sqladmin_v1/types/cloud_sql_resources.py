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
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.sql.v1",
    manifest={
        "SqlFileType",
        "BakType",
        "SqlMaintenanceType",
        "SqlBackendType",
        "SqlIpAddressType",
        "SqlDatabaseVersion",
        "SqlPricingPlan",
        "SqlReplicationType",
        "SqlDataDiskType",
        "SqlAvailabilityType",
        "SqlUpdateTrack",
        "AutoDnsStatus",
        "AclEntry",
        "ApiWarning",
        "BackupRetentionSettings",
        "BackupConfiguration",
        "PerformDiskShrinkContext",
        "PreCheckResponse",
        "PreCheckMajorVersionUpgradeContext",
        "BackupContext",
        "Database",
        "SqlServerDatabaseDetails",
        "DatabaseFlags",
        "MySqlSyncConfig",
        "SyncFlags",
        "InstanceReference",
        "DemoteMasterConfiguration",
        "DemoteMasterMySqlReplicaConfiguration",
        "ExportContext",
        "ImportContext",
        "IpConfiguration",
        "PscConfig",
        "PscAutoConnectionConfig",
        "LocationPreference",
        "MaintenanceWindow",
        "DenyMaintenancePeriod",
        "InsightsConfig",
        "MySqlReplicaConfiguration",
        "DiskEncryptionConfiguration",
        "DiskEncryptionStatus",
        "IpMapping",
        "SqlSubOperationType",
        "Operation",
        "OperationError",
        "OperationErrors",
        "PasswordValidationPolicy",
        "DataCacheConfig",
        "FinalBackupConfig",
        "Settings",
        "PerformanceCaptureConfig",
        "ConnectionPoolFlags",
        "ConnectionPoolConfig",
        "ReadPoolAutoScaleConfig",
        "AdvancedMachineFeatures",
        "SslCert",
        "SslCertDetail",
        "SqlActiveDirectoryConfig",
        "SqlServerAuditConfig",
        "SqlServerEntraIdConfig",
        "AcquireSsrsLeaseContext",
        "DnsNameMapping",
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
            Transaction Log backup
    """

    BAK_TYPE_UNSPECIFIED = 0
    FULL = 1
    DIFF = 2
    TLOG = 3


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
        code (google.cloud.sqladmin_v1.types.ApiWarning.SqlApiWarningCode):
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
        retention_unit (google.cloud.sqladmin_v1.types.BackupRetentionSettings.RetentionUnit):
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
            [point_in_time_recovery_enabled][google.cloud.sql.v1.BackupConfiguration.point_in_time_recovery_enabled]
            instead.
        location (str):
            Location of the backup
        point_in_time_recovery_enabled (google.protobuf.wrappers_pb2.BoolValue):
            Whether point in time recovery is enabled.
        backup_retention_settings (google.cloud.sqladmin_v1.types.BackupRetentionSettings):
            Backup retention settings.
        transaction_log_retention_days (google.protobuf.wrappers_pb2.Int32Value):
            The number of days of transaction logs we
            retain for point in time restore, from 1-7.
        transactional_log_storage_state (google.cloud.sqladmin_v1.types.BackupConfiguration.TransactionalLogStorageState):
            Output only. This value contains the storage
            location of transactional logs used to perform
            point-in-time recovery (PITR) for the database.

            This field is a member of `oneof`_ ``_transactional_log_storage_state``.
        backup_tier (google.cloud.sqladmin_v1.types.BackupConfiguration.BackupTier):
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
    backup_retention_settings: "BackupRetentionSettings" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="BackupRetentionSettings",
    )
    transaction_log_retention_days: wrappers_pb2.Int32Value = proto.Field(
        proto.MESSAGE,
        number=9,
        message=wrappers_pb2.Int32Value,
    )
    transactional_log_storage_state: TransactionalLogStorageState = proto.Field(
        proto.ENUM,
        number=10,
        optional=True,
        enum=TransactionalLogStorageState,
    )
    backup_tier: BackupTier = proto.Field(
        proto.ENUM,
        number=11,
        optional=True,
        enum=BackupTier,
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
        message_type (google.cloud.sqladmin_v1.types.PreCheckResponse.MessageType):
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
        target_database_version (google.cloud.sqladmin_v1.types.SqlDatabaseVersion):
            Required. The target database version to
            upgrade to.
        pre_check_response (MutableSequence[google.cloud.sqladmin_v1.types.PreCheckResponse]):
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
        sqlserver_database_details (google.cloud.sqladmin_v1.types.SqlServerDatabaseDetails):

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


class MySqlSyncConfig(proto.Message):
    r"""MySQL-specific external server sync settings.

    Attributes:
        initial_sync_flags (MutableSequence[google.cloud.sqladmin_v1.types.SyncFlags]):
            Flags to use for the initial dump.
    """

    initial_sync_flags: MutableSequence["SyncFlags"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="SyncFlags",
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


class DemoteMasterConfiguration(proto.Message):
    r"""Read-replica configuration for connecting to the on-premises
    primary instance.

    Attributes:
        kind (str):
            This is always ``sql#demoteMasterConfiguration``.
        mysql_replica_configuration (google.cloud.sqladmin_v1.types.DemoteMasterMySqlReplicaConfiguration):
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
        sql_export_options (google.cloud.sqladmin_v1.types.ExportContext.SqlExportOptions):
            Options for exporting data as SQL statements.
        csv_export_options (google.cloud.sqladmin_v1.types.ExportContext.SqlCsvExportOptions):
            Options for exporting data as CSV. ``MySQL`` and
            ``PostgreSQL`` instances only.
        file_type (google.cloud.sqladmin_v1.types.SqlFileType):
            The file type for the specified uri.
        offload (google.protobuf.wrappers_pb2.BoolValue):
            Whether to perform a serverless export.
        bak_export_options (google.cloud.sqladmin_v1.types.ExportContext.SqlBakExportOptions):
            Options for exporting data as BAK files.
        tde_export_options (google.cloud.sqladmin_v1.types.ExportContext.SqlTdeExportOptions):
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
            mysql_export_options (google.cloud.sqladmin_v1.types.ExportContext.SqlExportOptions.MysqlExportOptions):

            threads (google.protobuf.wrappers_pb2.Int32Value):
                Optional. The number of threads to use for
                parallel export.
            parallel (google.protobuf.wrappers_pb2.BoolValue):
                Optional. Whether or not the export should be
                parallel.
            postgres_export_options (google.cloud.sqladmin_v1.types.ExportContext.SqlExportOptions.PostgresExportOptions):
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
            bak_type (google.cloud.sqladmin_v1.types.BakType):
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
                bucket. Applicable only for SQL Server
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
        file_type (google.cloud.sqladmin_v1.types.SqlFileType):
            The file type for the specified
            uri.`SQL\ ``: The file contains SQL statements. \``\ CSV\`:
            The file contains CSV data.
        csv_import_options (google.cloud.sqladmin_v1.types.ImportContext.SqlCsvImportOptions):
            Options for importing data as CSV.
        import_user (str):
            The PostgreSQL user for this import
            operation. PostgreSQL instances only.
        bak_import_options (google.cloud.sqladmin_v1.types.ImportContext.SqlBakImportOptions):
            Import parameters specific to SQL Server .BAK
            files
        sql_import_options (google.cloud.sqladmin_v1.types.ImportContext.SqlImportOptions):
            Optional. Options for importing data from SQL
            statements.
        tde_import_options (google.cloud.sqladmin_v1.types.ImportContext.SqlTdeImportOptions):
            Optional. Import parameters specific to SQL
            Server TDE certificates
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
            postgres_import_options (google.cloud.sqladmin_v1.types.ImportContext.SqlImportOptions.PostgresImportOptions):
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
            encryption_options (google.cloud.sqladmin_v1.types.ImportContext.SqlBakImportOptions.EncryptionOptions):

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
            bak_type (google.cloud.sqladmin_v1.types.BakType):
                Type of the bak content, FULL or DIFF
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
            then use the ``ssl_mode`` flag instead of the
            ``require_ssl`` flag.
        authorized_networks (MutableSequence[google.cloud.sqladmin_v1.types.AclEntry]):
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
        ssl_mode (google.cloud.sqladmin_v1.types.IpConfiguration.SslMode):
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
        psc_config (google.cloud.sqladmin_v1.types.PscConfig):
            PSC settings for this instance.

            This field is a member of `oneof`_ ``_psc_config``.
        server_ca_mode (google.cloud.sqladmin_v1.types.IpConfiguration.CaMode):
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
        server_certificate_rotation_mode (google.cloud.sqladmin_v1.types.IpConfiguration.ServerCertificateRotationMode):
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
        psc_auto_connections (MutableSequence[google.cloud.sqladmin_v1.types.PscAutoConnectionConfig]):
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
            edition. This will default to true for new Enterprise Plus
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

            This is only applicable if ``consumer_network`` is a shared
            VPC network.
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
        instance_auto_dns_status (google.cloud.sqladmin_v1.types.AutoDnsStatus):
            Output only. The status of automated DNS
            provisioning.

            This field is a member of `oneof`_ ``_instance_auto_dns_status``.
        write_endpoint_auto_dns_status (google.cloud.sqladmin_v1.types.AutoDnsStatus):
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
        update_track (google.cloud.sqladmin_v1.types.SqlUpdateTrack):
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
    r"""Deny maintenance Periods. This specifies a date range during
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
            means the no maintenance interval recurs every
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


class DiskEncryptionConfiguration(proto.Message):
    r"""Disk encryption configuration for an instance.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        kms_key_name (str):
            Resource name of KMS key for disk encryption.
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


class IpMapping(proto.Message):
    r"""Database instance IP mapping

    Attributes:
        type_ (google.cloud.sqladmin_v1.types.SqlIpAddressType):
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


class SqlSubOperationType(proto.Message):
    r"""The sub operation type based on the operation type.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        maintenance_type (google.cloud.sqladmin_v1.types.SqlMaintenanceType):
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

        status (google.cloud.sqladmin_v1.types.Operation.SqlOperationStatus):
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
        error (google.cloud.sqladmin_v1.types.OperationErrors):
            If errors occurred during processing of this
            operation, this field will be populated.
        api_warning (google.cloud.sqladmin_v1.types.ApiWarning):
            An Admin API warning message.
        operation_type (google.cloud.sqladmin_v1.types.Operation.SqlOperationType):
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
        import_context (google.cloud.sqladmin_v1.types.ImportContext):
            The context for import operation, if
            applicable.
        export_context (google.cloud.sqladmin_v1.types.ExportContext):
            The context for export operation, if
            applicable.
        backup_context (google.cloud.sqladmin_v1.types.BackupContext):
            The context for backup operation, if
            applicable.
        pre_check_major_version_upgrade_context (google.cloud.sqladmin_v1.types.PreCheckMajorVersionUpgradeContext):
            This field is only populated when the operation_type is
            PRE_CHECK_MAJOR_VERSION_UPGRADE. The
            PreCheckMajorVersionUpgradeContext message itself contains
            the details for that pre-check, such as the target database
            version for the upgrade and the results of the check
            (including any warnings or errors found).
        start_workload_capture_context (google.cloud.sqladmin_v1.types.StartWorkloadCaptureContext):
            The context for the ``StartWorkloadCapture`` operation,
            which contains details to start recording the workload (SQL
            queries) on a Cloud SQL instance.
        stop_workload_capture_context (google.cloud.sqladmin_v1.types.StopWorkloadCaptureContext):
            The context for the ``StopWorkloadCapture`` operation, which
            contains details to stop recording the workload (SQL
            queries) on a Cloud SQL instance.
        start_workload_replay_context (google.cloud.sqladmin_v1.types.StartWorkloadReplayContext):
            The context for the ``StartWorkloadReplay`` operation, which
            contains details about starting the execution of a captured
            workload (recorded read and write SQL queries) on a replay
            instance (the Cloud SQL instance where the recorded SQL
            queries are executed).
        stop_workload_replay_context (google.cloud.sqladmin_v1.types.StopWorkloadReplayContext):
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
        acquire_ssrs_lease_context (google.cloud.sqladmin_v1.types.AcquireSsrsLeaseContext):
            The context for acquire SSRS lease operation,
            if applicable.
        sub_operation_type (google.cloud.sqladmin_v1.types.SqlSubOperationType):
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
                Pre-checks the major version upgrade
                operation.
            SETUP_MIGRATION (55):
                This operation type represents individual
                steps in a multi-step setup migration workflow:
                including configuration, replication,
                switchover/back, and data reseeding, as defined
                by operation's intent.
            CREATE_BLUE_GREEN_DEPLOYMENT (56):
                Creates a new Blue-Green deployment.
            SWITCHOVER_BLUE_GREEN_DEPLOYMENT (57):
                Switches over a Blue-Green deployment.
            DELETE_BLUE_GREEN_DEPLOYMENT (58):
                Deletes a Blue-Green deployment.
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
        SETUP_MIGRATION = 55
        CREATE_BLUE_GREEN_DEPLOYMENT = 56
        SWITCHOVER_BLUE_GREEN_DEPLOYMENT = 57
        DELETE_BLUE_GREEN_DEPLOYMENT = 58

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
        number=59,
        message="StartWorkloadCaptureContext",
    )
    stop_workload_capture_context: "StopWorkloadCaptureContext" = proto.Field(
        proto.MESSAGE,
        number=60,
        message="StopWorkloadCaptureContext",
    )
    start_workload_replay_context: "StartWorkloadReplayContext" = proto.Field(
        proto.MESSAGE,
        number=61,
        message="StartWorkloadReplayContext",
    )
    stop_workload_replay_context: "StopWorkloadReplayContext" = proto.Field(
        proto.MESSAGE,
        number=62,
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
        errors (MutableSequence[google.cloud.sqladmin_v1.types.OperationError]):
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
        complexity (google.cloud.sqladmin_v1.types.PasswordValidationPolicy.Complexity):
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
        availability_type (google.cloud.sqladmin_v1.types.SqlAvailabilityType):
            Availability type. Potential values:

            - ``ZONAL``: The instance serves data from only one zone.
              Outages in that zone affect data accessibility.
            - ``REGIONAL``: The instance can serve data from more than
              one zone in a region (it is highly available)./

            For more information, see `Overview of the High Availability
            Configuration <https://cloud.google.com/sql/docs/mysql/high-availability>`__.
        pricing_plan (google.cloud.sqladmin_v1.types.SqlPricingPlan):
            The pricing plan for this instance. This can be either
            ``PER_USE`` or ``PACKAGE``. Only ``PER_USE`` is supported
            for Second Generation instances.
        replication_type (google.cloud.sqladmin_v1.types.SqlReplicationType):
            The type of replication this instance uses. This can be
            either ``ASYNCHRONOUS`` or ``SYNCHRONOUS``. (Deprecated)
            This property was only applicable to First Generation
            instances.
        storage_auto_resize_limit (google.protobuf.wrappers_pb2.Int64Value):
            The maximum size to which storage capacity
            can be automatically increased. The default
            value is 0, which specifies that there is no
            limit.
        activation_policy (google.cloud.sqladmin_v1.types.Settings.SqlActivationPolicy):
            The activation policy specifies when the instance is
            activated; it is applicable only when the instance state is
            RUNNABLE. Valid values:

            - ``ALWAYS``: The instance is on, and remains so even in the
              absence of connection requests.
            - ``NEVER``: The instance is off; it is not activated, even
              if a connection request arrives.
        ip_configuration (google.cloud.sqladmin_v1.types.IpConfiguration):
            The settings for IP Management. This allows
            to enable or disable the instance IP and manage
            which external networks can connect to the
            instance. The IPv4 address cannot be disabled
            for Second Generation instances.
        storage_auto_resize (google.protobuf.wrappers_pb2.BoolValue):
            Configuration to increase storage size
            automatically. The default value is true.
        location_preference (google.cloud.sqladmin_v1.types.LocationPreference):
            The location preference settings. This allows
            the instance to be located as near as possible
            to either an App Engine app or Compute Engine
            zone for better performance. App Engine
            co-location was only applicable to First
            Generation instances.
        database_flags (MutableSequence[google.cloud.sqladmin_v1.types.DatabaseFlags]):
            The database flags passed to the instance at
            startup.
        data_disk_type (google.cloud.sqladmin_v1.types.SqlDataDiskType):
            The type of data disk: ``PD_SSD`` (default) or ``PD_HDD``.
            Not used for First Generation instances.
        maintenance_window (google.cloud.sqladmin_v1.types.MaintenanceWindow):
            The maintenance window for this instance.
            This specifies when the instance can be
            restarted for maintenance purposes.
        backup_configuration (google.cloud.sqladmin_v1.types.BackupConfiguration):
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
        active_directory_config (google.cloud.sqladmin_v1.types.SqlActiveDirectoryConfig):
            Active Directory configuration, relevant only
            for Cloud SQL for SQL Server.
        collation (str):
            The name of server Instance collation.
        deny_maintenance_periods (MutableSequence[google.cloud.sqladmin_v1.types.DenyMaintenancePeriod]):
            Deny maintenance periods
        insights_config (google.cloud.sqladmin_v1.types.InsightsConfig):
            Insights configuration, for now relevant only
            for Postgres.
        password_validation_policy (google.cloud.sqladmin_v1.types.PasswordValidationPolicy):
            The local user password validation policy of
            the instance for PostgreSQL and MySQL.
        sql_server_audit_config (google.cloud.sqladmin_v1.types.SqlServerAuditConfig):
            SQL Server specific audit configuration.
        edition (google.cloud.sqladmin_v1.types.Settings.Edition):
            Optional. The edition type of the Cloud SQL
            instance.
        connector_enforcement (google.cloud.sqladmin_v1.types.Settings.ConnectorEnforcement):
            Specifies if connections must use Cloud SQL connectors.
            Option values include the following: ``NOT_REQUIRED`` (Cloud
            SQL instances can be connected without Cloud SQL Connectors)
            and ``REQUIRED`` (Only allow connections that use Cloud SQL
            Connectors).

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
        advanced_machine_features (google.cloud.sqladmin_v1.types.AdvancedMachineFeatures):
            Specifies advanced machine configuration for
            the instances relevant only for SQL Server.
        data_cache_config (google.cloud.sqladmin_v1.types.DataCacheConfig):
            Configuration for data cache.
        replication_lag_max_seconds (google.protobuf.wrappers_pb2.Int32Value):
            Optional. Configuration value for recreation
            of replica after certain replication lag
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
        connection_pool_config (google.cloud.sqladmin_v1.types.ConnectionPoolConfig):
            Optional. The managed connection pooling
            configuration for the instance.

            This field is a member of `oneof`_ ``_connection_pool_config``.
        final_backup_config (google.cloud.sqladmin_v1.types.FinalBackupConfig):
            Optional. The final backup configuration for
            the instance.

            This field is a member of `oneof`_ ``_final_backup_config``.
        read_pool_auto_scale_config (google.cloud.sqladmin_v1.types.ReadPoolAutoScaleConfig):
            Optional. The read pool auto-scale
            configuration for the instance.

            This field is a member of `oneof`_ ``_read_pool_auto_scale_config``.
        accelerated_replica_mode (google.protobuf.wrappers_pb2.BoolValue):
            Optional. Whether the replica is in
            accelerated mode. This feature is in private
            preview and requires allowlisting to take
            effect.
        auto_upgrade_enabled (bool):
            Optional. Cloud SQL for MySQL auto-upgrade
            configuration. When this parameter is set to
            true, auto-upgrade is enabled for MySQL 8.0
            minor versions. The MySQL version must be 8.0.35
            or higher.

            This field is a member of `oneof`_ ``_auto_upgrade_enabled``.
        entraid_config (google.cloud.sqladmin_v1.types.SqlServerEntraIdConfig):
            Optional. The Microsoft Entra ID
            configuration for the SQL Server instance.
        data_api_access (google.cloud.sqladmin_v1.types.Settings.DataApiAccess):
            This parameter controls whether to allow
            using ExecuteSql API to connect to the instance.
            Not allowed by default.

            This field is a member of `oneof`_ ``_data_api_access``.
        performance_capture_config (google.cloud.sqladmin_v1.types.PerformanceCaptureConfig):
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
        transaction_kill_type (google.cloud.sqladmin_v1.types.PerformanceCaptureConfig.TransactionKillType):
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


class ConnectionPoolConfig(proto.Message):
    r"""The managed connection pooling configuration.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        connection_pooling_enabled (bool):
            Whether managed connection pooling is
            enabled.

            This field is a member of `oneof`_ ``_connection_pooling_enabled``.
        flags (MutableSequence[google.cloud.sqladmin_v1.types.ConnectionPoolFlags]):
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
        target_metrics (MutableSequence[google.cloud.sqladmin_v1.types.ReadPoolAutoScaleConfig.TargetMetric]):
            Optional. Target metrics for read pool auto
            scaling.
        disable_scale_in (bool):
            Indicates whether read pool auto scaling
            supports scale in operations (removing nodes).

            This field is a member of `oneof`_ ``_disable_scale_in``.
        scale_in_cooldown_seconds (int):
            The cooldown period for scale-in operations.

            This field is a member of `oneof`_ ``_scale_in_cooldown_seconds``.
        scale_out_cooldown_seconds (int):
            The cooldown period for scale-out operations.

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
            example ``2012-11-15T16:19:00.094Z``
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
        cert_info (google.cloud.sqladmin_v1.types.SslCert):
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


class SqlActiveDirectoryConfig(proto.Message):
    r"""Active Directory configuration, relevant only for Cloud SQL
    for SQL Server.

    Attributes:
        kind (str):
            This is always sql#activeDirectoryConfig.
        domain (str):
            The name of the domain (e.g., mydomain.com).
        mode (google.cloud.sqladmin_v1.types.SqlActiveDirectoryConfig.ActiveDirectoryMode):
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
                Unspecified mode. Will default to MANAGED_ACTIVE_DIRECTORY
                if the mode is not specified to maintain backward
                compatibility.
            MANAGED_ACTIVE_DIRECTORY (1):
                Managed Active Directory mode.
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
            The report database to be used for SSRS
            setup.

            This field is a member of `oneof`_ ``_report_database``.
        duration (google.protobuf.duration_pb2.Duration):
            Lease duration needed for SSRS setup.

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


class DnsNameMapping(proto.Message):
    r"""DNS metadata.

    Attributes:
        name (str):
            Output only. The DNS name.
        connection_type (google.cloud.sqladmin_v1.types.DnsNameMapping.ConnectionType):
            Output only. The connection type of the DNS
            name.
        dns_scope (google.cloud.sqladmin_v1.types.DnsNameMapping.DnsScope):
            Output only. The scope that the DNS name
            applies to.
        record_manager (google.cloud.sqladmin_v1.types.DnsNameMapping.RecordManager):
            Output only. The manager for this DNS record.
    """

    class ConnectionType(proto.Enum):
        r"""The connection type of the DNS name.
        This enum is not frozen, and new values may be added in the
        future.

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
