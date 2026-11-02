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
import google.type.dayofweek_pb2 as dayofweek_pb2  # type: ignore
import google.type.timeofday_pb2 as timeofday_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.oracledatabase_v1.types import common

__protobuf__ = proto.module(
    package="google.cloud.oracledatabase.v1",
    manifest={
        "GenerateType",
        "State",
        "OperationsInsightsState",
        "DBWorkload",
        "AutonomousDatabase",
        "SourceConfig",
        "AutonomousDatabaseProperties",
        "EncryptionKeyHistoryEntry",
        "EncryptionKey",
        "AutonomousDatabaseApex",
        "AutonomousDatabaseConnectionStrings",
        "DatabaseConnectionStringProfile",
        "AllConnectionStrings",
        "AutonomousDatabaseConnectionUrls",
        "AutonomousDatabaseStandbySummary",
        "ScheduledOperationDetails",
        "AutonomousDatabaseRefreshableClone",
    },
)


class GenerateType(proto.Enum):
    r"""The type of wallet generation.

    Values:
        GENERATE_TYPE_UNSPECIFIED (0):
            Default unspecified value.
        ALL (1):
            Used to generate wallet for all databases in
            the region.
        SINGLE (2):
            Used to generate wallet for a single
            database.
    """

    GENERATE_TYPE_UNSPECIFIED = 0
    ALL = 1
    SINGLE = 2


class State(proto.Enum):
    r"""The various lifecycle states of the Autonomous Database.

    Values:
        STATE_UNSPECIFIED (0):
            Default unspecified value.
        PROVISIONING (1):
            Indicates that the Autonomous Database is in
            provisioning state.
        AVAILABLE (2):
            Indicates that the Autonomous Database is in
            available state.
        STOPPING (3):
            Indicates that the Autonomous Database is in
            stopping state.
        STOPPED (4):
            Indicates that the Autonomous Database is in
            stopped state.
        STARTING (5):
            Indicates that the Autonomous Database is in
            starting state.
        TERMINATING (6):
            Indicates that the Autonomous Database is in
            terminating state.
        TERMINATED (7):
            Indicates that the Autonomous Database is in
            terminated state.
        UNAVAILABLE (8):
            Indicates that the Autonomous Database is in
            unavailable state.
        RESTORE_IN_PROGRESS (9):
            Indicates that the Autonomous Database
            restore is in progress.
        RESTORE_FAILED (10):
            Indicates that the Autonomous Database failed
            to restore.
        BACKUP_IN_PROGRESS (11):
            Indicates that the Autonomous Database backup
            is in progress.
        SCALE_IN_PROGRESS (12):
            Indicates that the Autonomous Database scale
            is in progress.
        AVAILABLE_NEEDS_ATTENTION (13):
            Indicates that the Autonomous Database is
            available but needs attention state.
        UPDATING (14):
            Indicates that the Autonomous Database is in
            updating state.
        MAINTENANCE_IN_PROGRESS (15):
            Indicates that the Autonomous Database's
            maintenance is in progress state.
        RESTARTING (16):
            Indicates that the Autonomous Database is in
            restarting state.
        RECREATING (17):
            Indicates that the Autonomous Database is in
            recreating state.
        ROLE_CHANGE_IN_PROGRESS (18):
            Indicates that the Autonomous Database's role
            change is in progress state.
        UPGRADING (19):
            Indicates that the Autonomous Database is in
            upgrading state.
        INACCESSIBLE (20):
            Indicates that the Autonomous Database is in
            inaccessible state.
        STANDBY (21):
            Indicates that the Autonomous Database is in
            standby state.
    """

    STATE_UNSPECIFIED = 0
    PROVISIONING = 1
    AVAILABLE = 2
    STOPPING = 3
    STOPPED = 4
    STARTING = 5
    TERMINATING = 6
    TERMINATED = 7
    UNAVAILABLE = 8
    RESTORE_IN_PROGRESS = 9
    RESTORE_FAILED = 10
    BACKUP_IN_PROGRESS = 11
    SCALE_IN_PROGRESS = 12
    AVAILABLE_NEEDS_ATTENTION = 13
    UPDATING = 14
    MAINTENANCE_IN_PROGRESS = 15
    RESTARTING = 16
    RECREATING = 17
    ROLE_CHANGE_IN_PROGRESS = 18
    UPGRADING = 19
    INACCESSIBLE = 20
    STANDBY = 21


class OperationsInsightsState(proto.Enum):
    r"""The state of the Operations Insights for this Autonomous
    Database.

    Values:
        OPERATIONS_INSIGHTS_STATE_UNSPECIFIED (0):
            Default unspecified value.
        ENABLING (1):
            Enabling status for operation insights.
        ENABLED (2):
            Enabled status for operation insights.
        DISABLING (3):
            Disabling status for operation insights.
        NOT_ENABLED (4):
            Not Enabled status for operation insights.
        FAILED_ENABLING (5):
            Failed enabling status for operation
            insights.
        FAILED_DISABLING (6):
            Failed disabling status for operation
            insights.
    """

    OPERATIONS_INSIGHTS_STATE_UNSPECIFIED = 0
    ENABLING = 1
    ENABLED = 2
    DISABLING = 3
    NOT_ENABLED = 4
    FAILED_ENABLING = 5
    FAILED_DISABLING = 6


class DBWorkload(proto.Enum):
    r"""The various states available for the Autonomous Database
    workload type.

    Values:
        DB_WORKLOAD_UNSPECIFIED (0):
            Default unspecified value.
        OLTP (1):
            Autonomous Transaction Processing database.
        DW (2):
            Autonomous Data Warehouse database.
        AJD (3):
            Autonomous JSON Database.
        APEX (4):
            Autonomous Database with the Oracle APEX
            Application Development workload type.
    """

    DB_WORKLOAD_UNSPECIFIED = 0
    OLTP = 1
    DW = 2
    AJD = 3
    APEX = 4


class AutonomousDatabase(proto.Message):
    r"""Details of the Autonomous Database resource.
    https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/AutonomousDatabase/

    Attributes:
        name (str):
            Identifier. The name of the Autonomous Database resource in
            the following format:
            projects/{project}/locations/{region}/autonomousDatabases/{autonomous_database}
        database (str):
            Optional. Immutable. The name of the
            Autonomous Database. The database name must be
            unique in the project. The name must begin with
            a letter and can contain a maximum of 30
            alphanumeric characters.
        display_name (str):
            Optional. Immutable. The display name for the
            Autonomous Database. The name does not have to
            be unique within your project.
        entitlement_id (str):
            Output only. The ID of the subscription
            entitlement associated with the Autonomous
            Database.
        admin_password (str):
            Optional. Immutable. The password for the default ADMIN
            user. Note: Only one of ``admin_password_secret_version`` or
            ``admin_password`` can be populated.
        admin_password_secret_version (str):
            Optional. Immutable. The resource name of a secret version
            in Secret Manager which contains the database admin user's
            password. Format:
            projects/{project}/secrets/{secret}/versions/{version}.
            Note: Only one of ``admin_password_secret_version`` or
            ``admin_password`` can be populated.
        properties (google.cloud.oracledatabase_v1.types.AutonomousDatabaseProperties):
            Optional. The properties of the Autonomous
            Database.
        labels (MutableMapping[str, str]):
            Optional. The labels or tags associated with
            the Autonomous Database.
        network (str):
            Optional. Immutable. The name of the VPC
            network used by the Autonomous Database in the
            following format:

            projects/{project}/global/networks/{network}
        cidr (str):
            Optional. Immutable. The subnet CIDR range
            for the Autonomous Database.
        odb_network (str):
            Optional. Immutable. The name of the OdbNetwork associated
            with the Autonomous Database. Format:
            projects/{project}/locations/{location}/odbNetworks/{odb_network}
            It is optional but if specified, this should match the
            parent ODBNetwork of the OdbSubnet.
        odb_subnet (str):
            Optional. Immutable. The name of the OdbSubnet associated
            with the Autonomous Database. Format:
            projects/{project}/locations/{location}/odbNetworks/{odb_network}/odbSubnets/{odb_subnet}
        source_config (google.cloud.oracledatabase_v1.types.SourceConfig):
            Optional. Immutable. The source Autonomous
            Database configuration for the standby
            Autonomous Database. The source Autonomous
            Database is configured while creating the Peer
            Autonomous Database and can't be updated after
            creation.
        peer_autonomous_databases (MutableSequence[str]):
            Output only. The peer Autonomous Database
            names of the given Autonomous Database.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The date and time that the
            Autonomous Database was created.
        disaster_recovery_supported_locations (MutableSequence[str]):
            Output only. List of supported GCP region to clone the
            Autonomous Database for disaster recovery. Format:
            ``project/{project}/locations/{location}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    database: str = proto.Field(
        proto.STRING,
        number=2,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    entitlement_id: str = proto.Field(
        proto.STRING,
        number=5,
    )
    admin_password: str = proto.Field(
        proto.STRING,
        number=6,
    )
    admin_password_secret_version: str = proto.Field(
        proto.STRING,
        number=18,
    )
    properties: "AutonomousDatabaseProperties" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="AutonomousDatabaseProperties",
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=8,
    )
    network: str = proto.Field(
        proto.STRING,
        number=9,
    )
    cidr: str = proto.Field(
        proto.STRING,
        number=10,
    )
    odb_network: str = proto.Field(
        proto.STRING,
        number=16,
    )
    odb_subnet: str = proto.Field(
        proto.STRING,
        number=17,
    )
    source_config: "SourceConfig" = proto.Field(
        proto.MESSAGE,
        number=11,
        message="SourceConfig",
    )
    peer_autonomous_databases: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=12,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=13,
        message=timestamp_pb2.Timestamp,
    )
    disaster_recovery_supported_locations: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=15,
    )


class SourceConfig(proto.Message):
    r"""The source configuration for the standby Autonomous Database.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        autonomous_database (str):
            Optional. The name of the primary Autonomous
            Database that is used to create a Peer
            Autonomous Database from a source.
        automatic_backups_replication_enabled (bool):
            Optional. This field specifies if the
            replication of automatic backups is enabled when
            creating a Data Guard.
        source_type (google.cloud.oracledatabase_v1.types.SourceConfig.SourceType):
            Optional. The source type of the Autonomous
            Database.
        clone_type (google.cloud.oracledatabase_v1.types.SourceConfig.CloneType):
            Optional. The clone type of the Autonomous
            Database. This field is only applicable in case
            of cloning
        refreshable_mode (google.cloud.oracledatabase_v1.types.SourceConfig.RefreshableMode):
            Optional. The refresh mode of the clone.
        auto_refresh_frequency_seconds (int):
            Optional. The frequency in seconds a
            refreshable clone is refreshed after
            auto-refresh is enabled.
        auto_refresh_point_lag_seconds (int):
            Optional. The time, in seconds, the data of
            the automatic refreshable clone lags the primary
            database at the point of refresh.

            This field is a member of `oneof`_ ``_auto_refresh_point_lag_seconds``.
        auto_refresh_start_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. The date and time that
            auto-refreshing will begin for an Autonomous
            Database refreshable clone. This value controls
            only the start time for the first refresh
            operation.
        autonomous_database_backup (str):
            Optional. The name of the Autonomous Database Backup
            resource with the format:
            projects/{project}/locations/{region}/autonomousDatabaseBackups/{autonomous_database_backup}
            Required when source_type is BACKUP_FROM_ID.
        backup_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. The timestamp specified for the point-in-time
            clone of the source Autonomous Database. This field is only
            applicable in case of BACKUP_FROM_TIMESTAMP source type and
            when use_latest_available_backup is false.
        use_latest_available_backup (bool):
            Optional. Clone from latest available backup timestamp. This
            field is only applicable in case of BACKUP_FROM_TIMESTAMP
            source type.
    """

    class RefreshableMode(proto.Enum):
        r"""The refresh mode of a refreshable clone.

        Values:
            REFRESHABLE_MODE_UNSPECIFIED (0):
                Default unspecified value.
            AUTOMATIC (1):
                Automatic refresh.
            MANUAL (2):
                Manual refresh.
        """

        REFRESHABLE_MODE_UNSPECIFIED = 0
        AUTOMATIC = 1
        MANUAL = 2

    class SourceType(proto.Enum):
        r"""Specifies the source of the database. For example, a clone or
        peer from an existing database.
        This enum may be expanded to include other source types in the
        future.

        Values:
            SOURCE_TYPE_UNSPECIFIED (0):
                Default unspecified value.
            CLONE_DATABASE (1):
                Clone database from an existing database specified in
                autonomous_database field.
            CROSS_REGION_DISASTER_RECOVERY (2):
                Create a cross-region disaster recovery peer
                adb from an existing adb.
            CLONE_TO_REFRESHABLE (3):
                Create a refreshable clone from an existing database
                specified in autonomous_database field.
            BACKUP_FROM_ID (4):
                Create clone from the backup resource.
            BACKUP_FROM_TIMESTAMP (5):
                Create clone from backup specified by backup_time field, or
                use latest available backup if use_latest_available_backup
                is true. The autonomous_database field must specify the
                source database to clone from.
        """

        SOURCE_TYPE_UNSPECIFIED = 0
        CLONE_DATABASE = 1
        CROSS_REGION_DISASTER_RECOVERY = 2
        CLONE_TO_REFRESHABLE = 3
        BACKUP_FROM_ID = 4
        BACKUP_FROM_TIMESTAMP = 5

    class CloneType(proto.Enum):
        r"""The clone type of the Autonomous Database.

        Values:
            CLONE_TYPE_UNSPECIFIED (0):
                Default unspecified value.
            FULL (1):
                Creates a new database with the source
                database's data and metadata.
            METADATA (2):
                Creates a new database that includes all the
                source database schema metadata, but none of the
                source database data.
        """

        CLONE_TYPE_UNSPECIFIED = 0
        FULL = 1
        METADATA = 2

    autonomous_database: str = proto.Field(
        proto.STRING,
        number=1,
    )
    automatic_backups_replication_enabled: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    source_type: SourceType = proto.Field(
        proto.ENUM,
        number=3,
        enum=SourceType,
    )
    clone_type: CloneType = proto.Field(
        proto.ENUM,
        number=4,
        enum=CloneType,
    )
    refreshable_mode: RefreshableMode = proto.Field(
        proto.ENUM,
        number=5,
        enum=RefreshableMode,
    )
    auto_refresh_frequency_seconds: int = proto.Field(
        proto.INT32,
        number=6,
    )
    auto_refresh_point_lag_seconds: int = proto.Field(
        proto.INT32,
        number=7,
        optional=True,
    )
    auto_refresh_start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    autonomous_database_backup: str = proto.Field(
        proto.STRING,
        number=9,
    )
    backup_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10,
        message=timestamp_pb2.Timestamp,
    )
    use_latest_available_backup: bool = proto.Field(
        proto.BOOL,
        number=11,
    )


class AutonomousDatabaseProperties(proto.Message):
    r"""The properties of an Autonomous Database.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        ocid (str):
            Output only. OCID of the Autonomous Database.
            https://docs.oracle.com/en-us/iaas/Content/General/Concepts/identifiers.htm#Oracle
        compute_count (float):
            Optional. Immutable. The number of compute
            servers for the Autonomous Database.
        cpu_core_count (int):
            Optional. Immutable. The number of CPU cores
            to be made available to the database.
        data_storage_size_tb (int):
            Optional. Immutable. The size of the data
            stored in the database, in terabytes.
        data_storage_size_gb (int):
            Optional. Immutable. The size of the data
            stored in the database, in gigabytes.
        db_workload (google.cloud.oracledatabase_v1.types.DBWorkload):
            Required. Immutable. The workload type of the
            Autonomous Database.
        db_edition (google.cloud.oracledatabase_v1.types.AutonomousDatabaseProperties.DatabaseEdition):
            Optional. Immutable. The edition of the
            Autonomous Databases.
        character_set (str):
            Optional. Immutable. The character set for
            the Autonomous Database. The default is
            AL32UTF8.
        n_character_set (str):
            Optional. Immutable. The national character
            set for the Autonomous Database. The default is
            AL16UTF16.
        private_endpoint_ip (str):
            Optional. Immutable. The private endpoint IP
            address for the Autonomous Database.
        private_endpoint_label (str):
            Optional. Immutable. The private endpoint
            label for the Autonomous Database.
        db_version (str):
            Optional. Immutable. The Oracle Database
            version for the Autonomous Database.
        is_auto_scaling_enabled (bool):
            Optional. Immutable. This field indicates if
            auto scaling is enabled for the Autonomous
            Database CPU core count.
        is_storage_auto_scaling_enabled (bool):
            Optional. Immutable. This field indicates if
            auto scaling is enabled for the Autonomous
            Database storage.
        license_type (google.cloud.oracledatabase_v1.types.AutonomousDatabaseProperties.LicenseType):
            Required. Immutable. The license type used
            for the Autonomous Database.
        customer_contacts (MutableSequence[google.cloud.oracledatabase_v1.types.CustomerContact]):
            Optional. Immutable. The list of customer
            contacts.
        secret_id (str):
            Optional. Immutable. The ID of the Oracle
            Cloud Infrastructure vault secret.
        vault_id (str):
            Optional. Immutable. The ID of the Oracle
            Cloud Infrastructure vault.
        maintenance_schedule_type (google.cloud.oracledatabase_v1.types.AutonomousDatabaseProperties.MaintenanceScheduleType):
            Optional. Immutable. The maintenance schedule
            of the Autonomous Database.
        mtls_connection_required (bool):
            Optional. Immutable. This field specifies if
            the Autonomous Database requires mTLS
            connections.
        backup_retention_period_days (int):
            Optional. Immutable. The retention period for
            the Autonomous Database. This field is specified
            in days, can range from 1 day to 60 days, and
            has a default value of 60 days.
        actual_used_data_storage_size_tb (float):
            Output only. The amount of storage currently
            being used for user and system data, in
            terabytes.
        allocated_storage_size_tb (float):
            Output only. The amount of storage currently
            allocated for the database tables and billed
            for, rounded up in terabytes.
        apex_details (google.cloud.oracledatabase_v1.types.AutonomousDatabaseApex):
            Output only. The details for the Oracle APEX
            Application Development.
        are_primary_allowlisted_ips_used (bool):
            Output only. This field indicates the status
            of Data Guard and Access control for the
            Autonomous Database. The field's value is null
            if Data Guard is disabled or Access Control is
            disabled. The field's value is TRUE if both Data
            Guard and Access Control are enabled, and the
            Autonomous Database is using primary IP access
            control list (ACL) for standby. The field's
            value is FALSE if both Data Guard and Access
            Control are enabled, and the Autonomous Database
            is using a different IP access control list
            (ACL) for standby compared to primary.

            This field is a member of `oneof`_ ``_are_primary_allowlisted_ips_used``.
        lifecycle_details (str):
            Output only. The details of the current
            lifestyle state of the Autonomous Database.
        state (google.cloud.oracledatabase_v1.types.State):
            Output only. The current lifecycle state of
            the Autonomous Database.
        autonomous_container_database_id (str):
            Output only. The Autonomous Container
            Database OCID.
        available_upgrade_versions (MutableSequence[str]):
            Output only. The list of available Oracle
            Database upgrade versions for an Autonomous
            Database.
        connection_strings (google.cloud.oracledatabase_v1.types.AutonomousDatabaseConnectionStrings):
            Output only. The connection strings used to
            connect to an Autonomous Database.
        connection_urls (google.cloud.oracledatabase_v1.types.AutonomousDatabaseConnectionUrls):
            Output only. The Oracle Connection URLs for
            an Autonomous Database.
        failed_data_recovery_duration (google.protobuf.duration_pb2.Duration):
            Output only. This field indicates the number
            of seconds of data loss during a Data Guard
            failover.
        memory_table_gbs (int):
            Output only. The memory assigned to in-memory
            tables in an Autonomous Database.
        is_local_data_guard_enabled (bool):
            Output only. Deprecated: Please use
            ``local_data_guard_enabled`` instead. This field indicates
            whether the Autonomous Database has local (in-region) Data
            Guard enabled.
        local_adg_auto_failover_max_data_loss_limit (int):
            Output only. Deprecated: Please use
            ``local_adg_auto_failover_max_data_loss_limit_duration``
            instead. This field indicates the maximum data loss limit
            for an Autonomous Database, in seconds.
        local_standby_db (google.cloud.oracledatabase_v1.types.AutonomousDatabaseStandbySummary):
            Output only. The details of the Autonomous
            Data Guard standby database.
        memory_per_oracle_compute_unit_gbs (int):
            Output only. The amount of memory enabled per
            ECPU, in gigabytes.
        local_disaster_recovery_type (google.cloud.oracledatabase_v1.types.AutonomousDatabaseProperties.LocalDisasterRecoveryType):
            Output only. This field indicates the local
            disaster recovery (DR) type of an Autonomous
            Database.
        data_safe_state (google.cloud.oracledatabase_v1.types.AutonomousDatabaseProperties.DataSafeState):
            Output only. The current state of the Data
            Safe registration for the Autonomous Database.
        database_management_state (google.cloud.oracledatabase_v1.types.AutonomousDatabaseProperties.DatabaseManagementState):
            Output only. The current state of database
            management for the Autonomous Database.
        open_mode (google.cloud.oracledatabase_v1.types.AutonomousDatabaseProperties.OpenMode):
            Output only. This field indicates the current
            mode of the Autonomous Database.
        operations_insights_state (google.cloud.oracledatabase_v1.types.OperationsInsightsState):
            Output only. This field indicates the state
            of Operations Insights for the Autonomous
            Database.
        peer_db_ids (MutableSequence[str]):
            Output only. The list of OCIDs of standby
            databases located in Autonomous Data Guard
            remote regions that are associated with the
            source database.
        permission_level (google.cloud.oracledatabase_v1.types.AutonomousDatabaseProperties.PermissionLevel):
            Output only. The permission level of the
            Autonomous Database.
        private_endpoint (str):
            Output only. The private endpoint for the
            Autonomous Database.
        refreshable_mode (google.cloud.oracledatabase_v1.types.AutonomousDatabaseProperties.RefreshableMode):
            Output only. The refresh mode of the cloned
            Autonomous Database.
        refreshable_state (google.cloud.oracledatabase_v1.types.AutonomousDatabaseProperties.RefreshableState):
            Output only. The refresh State of the clone.
        role (google.cloud.oracledatabase_v1.types.AutonomousDatabaseProperties.Role):
            Output only. The Data Guard role of the
            Autonomous Database.
        scheduled_operation_details (MutableSequence[google.cloud.oracledatabase_v1.types.ScheduledOperationDetails]):
            Output only. The list and details of the
            scheduled operations of the Autonomous Database.
        sql_web_developer_url (str):
            Output only. The SQL Web Developer URL for
            the Autonomous Database.
        supported_clone_regions (MutableSequence[str]):
            Output only. The list of available regions
            that can be used to create a clone for the
            Autonomous Database.
        used_data_storage_size_tbs (int):
            Output only. The storage space used by
            Autonomous Database, in gigabytes.
        oci_url (str):
            Output only. The Oracle Cloud Infrastructure
            link for the Autonomous Database.
        total_auto_backup_storage_size_gbs (float):
            Output only. The storage space used by
            automatic backups of Autonomous Database, in
            gigabytes.
        next_long_term_backup_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The long term backup schedule of
            the Autonomous Database.
        data_guard_role_changed_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The date and time the Autonomous
            Data Guard role was changed for the standby
            Autonomous Database.
        disaster_recovery_role_changed_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The date and time the Disaster
            Recovery role was changed for the standby
            Autonomous Database.
        maintenance_begin_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The date and time when
            maintenance will begin.
        maintenance_end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The date and time when
            maintenance will end.
        allowlisted_ips (MutableSequence[str]):
            Optional. Immutable. The list of allowlisted
            IP addresses for the Autonomous Database.
        encryption_key (google.cloud.oracledatabase_v1.types.EncryptionKey):
            Optional. The encryption key used to encrypt the Autonomous
            Database. Updating this field will add a new entry in the
            ``encryption_key_history_entries`` field with the former
            version.
        encryption_key_history_entries (MutableSequence[google.cloud.oracledatabase_v1.types.EncryptionKeyHistoryEntry]):
            Output only. The history of the encryption
            keys used to encrypt the Autonomous Database.
        service_agent_email (str):
            Output only. An Oracle-managed Google Cloud
            service account on which customers can grant
            roles to access resources in the customer
            project.
        local_data_guard_enabled (bool):
            Optional. Indicates whether the Autonomous
            Database has a local (in-region) standby
            database. Not applicable to cross-region Data
            Guard or dedicated Exadata infrastructure.

            This field is a member of `oneof`_ ``_local_data_guard_enabled``.
        local_adg_auto_failover_max_data_loss_limit_duration (int):
            Optional. This field indicates the maximum
            data loss limit for an Autonomous Database, in
            seconds.

            This field is a member of `oneof`_ ``_local_adg_auto_failover_max_data_loss_limit_duration``.
        refreshable_clone (bool):
            Optional. Indicates if the Autonomous
            Database is a refreshable clone. This field is
            used in update flow to connect / disconnect a
            refreshable clone from its source database.

            This field is a member of `oneof`_ ``_refreshable_clone``.
    """

    class DatabaseEdition(proto.Enum):
        r"""The editions available for the Autonomous Database.

        Values:
            DATABASE_EDITION_UNSPECIFIED (0):
                Default unspecified value.
            STANDARD_EDITION (1):
                Standard Database Edition
            ENTERPRISE_EDITION (2):
                Enterprise Database Edition
        """

        DATABASE_EDITION_UNSPECIFIED = 0
        STANDARD_EDITION = 1
        ENTERPRISE_EDITION = 2

    class LicenseType(proto.Enum):
        r"""The license types available for the Autonomous Database.

        Values:
            LICENSE_TYPE_UNSPECIFIED (0):
                Unspecified
            LICENSE_INCLUDED (1):
                License included part of offer
            BRING_YOUR_OWN_LICENSE (2):
                Bring your own license
        """

        LICENSE_TYPE_UNSPECIFIED = 0
        LICENSE_INCLUDED = 1
        BRING_YOUR_OWN_LICENSE = 2

    class MaintenanceScheduleType(proto.Enum):
        r"""The available maintenance schedules for the Autonomous
        Database.

        Values:
            MAINTENANCE_SCHEDULE_TYPE_UNSPECIFIED (0):
                Default unspecified value.
            EARLY (1):
                An EARLY maintenance schedule patches the
                database before the regular scheduled
                maintenance.
            REGULAR (2):
                A REGULAR maintenance schedule follows the
                normal maintenance cycle.
        """

        MAINTENANCE_SCHEDULE_TYPE_UNSPECIFIED = 0
        EARLY = 1
        REGULAR = 2

    class LocalDisasterRecoveryType(proto.Enum):
        r"""The types of local disaster recovery available for an
        Autonomous Database.

        Values:
            LOCAL_DISASTER_RECOVERY_TYPE_UNSPECIFIED (0):
                Default unspecified value.
            ADG (1):
                Autonomous Data Guard recovery.
            BACKUP_BASED (2):
                Backup based recovery.
            NOT_AVAILABLE (3):
                Local disaster recovery is not available.
        """

        LOCAL_DISASTER_RECOVERY_TYPE_UNSPECIFIED = 0
        ADG = 1
        BACKUP_BASED = 2
        NOT_AVAILABLE = 3

    class DataSafeState(proto.Enum):
        r"""Varies states of the Data Safe registration for the
        Autonomous Database.

        Values:
            DATA_SAFE_STATE_UNSPECIFIED (0):
                Default unspecified value.
            REGISTERING (1):
                Registering data safe state.
            REGISTERED (2):
                Registered data safe state.
            DEREGISTERING (3):
                Deregistering data safe state.
            NOT_REGISTERED (4):
                Not registered data safe state.
            FAILED (5):
                Failed data safe state.
        """

        DATA_SAFE_STATE_UNSPECIFIED = 0
        REGISTERING = 1
        REGISTERED = 2
        DEREGISTERING = 3
        NOT_REGISTERED = 4
        FAILED = 5

    class DatabaseManagementState(proto.Enum):
        r"""The different states of database management for an Autonomous
        Database.

        Values:
            DATABASE_MANAGEMENT_STATE_UNSPECIFIED (0):
                Default unspecified value.
            ENABLING (1):
                Enabling Database Management state
            ENABLED (2):
                Enabled Database Management state
            DISABLING (3):
                Disabling Database Management state
            NOT_ENABLED (4):
                Not Enabled Database Management state
            FAILED_ENABLING (5):
                Failed enabling Database Management state
            FAILED_DISABLING (6):
                Failed disabling Database Management state
        """

        DATABASE_MANAGEMENT_STATE_UNSPECIFIED = 0
        ENABLING = 1
        ENABLED = 2
        DISABLING = 3
        NOT_ENABLED = 4
        FAILED_ENABLING = 5
        FAILED_DISABLING = 6

    class OpenMode(proto.Enum):
        r"""This field indicates the modes of an Autonomous Database.

        Values:
            OPEN_MODE_UNSPECIFIED (0):
                Default unspecified value.
            READ_ONLY (1):
                Read Only Mode
            READ_WRITE (2):
                Read Write Mode
        """

        OPEN_MODE_UNSPECIFIED = 0
        READ_ONLY = 1
        READ_WRITE = 2

    class PermissionLevel(proto.Enum):
        r"""The types of permission levels for an Autonomous Database.

        Values:
            PERMISSION_LEVEL_UNSPECIFIED (0):
                Default unspecified value.
            RESTRICTED (1):
                Restricted mode allows access only by admin
                users.
            UNRESTRICTED (2):
                Normal access.
        """

        PERMISSION_LEVEL_UNSPECIFIED = 0
        RESTRICTED = 1
        UNRESTRICTED = 2

    class RefreshableMode(proto.Enum):
        r"""The refresh mode of the cloned Autonomous Database.

        Values:
            REFRESHABLE_MODE_UNSPECIFIED (0):
                The default unspecified value.
            AUTOMATIC (1):
                AUTOMATIC indicates that the cloned database
                is automatically refreshed with data from the
                source Autonomous Database.
            MANUAL (2):
                MANUAL indicates that the cloned database is
                manually refreshed with data from the source
                Autonomous Database.
        """

        REFRESHABLE_MODE_UNSPECIFIED = 0
        AUTOMATIC = 1
        MANUAL = 2

    class RefreshableState(proto.Enum):
        r"""The refresh state of the cloned Autonomous Database.

        Values:
            REFRESHABLE_STATE_UNSPECIFIED (0):
                Default unspecified value.
            REFRESHING (1):
                Refreshing
            NOT_REFRESHING (2):
                Not refreshed
        """

        REFRESHABLE_STATE_UNSPECIFIED = 0
        REFRESHING = 1
        NOT_REFRESHING = 2

    class Role(proto.Enum):
        r"""The Data Guard role of the Autonomous Database.

        Values:
            ROLE_UNSPECIFIED (0):
                Default unspecified value.
            PRIMARY (1):
                Primary role
            STANDBY (2):
                Standby role
            DISABLED_STANDBY (3):
                Disabled standby role
            BACKUP_COPY (4):
                Backup copy role
            SNAPSHOT_STANDBY (5):
                Snapshot standby role
        """

        ROLE_UNSPECIFIED = 0
        PRIMARY = 1
        STANDBY = 2
        DISABLED_STANDBY = 3
        BACKUP_COPY = 4
        SNAPSHOT_STANDBY = 5

    ocid: str = proto.Field(
        proto.STRING,
        number=1,
    )
    compute_count: float = proto.Field(
        proto.FLOAT,
        number=2,
    )
    cpu_core_count: int = proto.Field(
        proto.INT32,
        number=3,
    )
    data_storage_size_tb: int = proto.Field(
        proto.INT32,
        number=4,
    )
    data_storage_size_gb: int = proto.Field(
        proto.INT32,
        number=63,
    )
    db_workload: "DBWorkload" = proto.Field(
        proto.ENUM,
        number=5,
        enum="DBWorkload",
    )
    db_edition: DatabaseEdition = proto.Field(
        proto.ENUM,
        number=6,
        enum=DatabaseEdition,
    )
    character_set: str = proto.Field(
        proto.STRING,
        number=8,
    )
    n_character_set: str = proto.Field(
        proto.STRING,
        number=9,
    )
    private_endpoint_ip: str = proto.Field(
        proto.STRING,
        number=10,
    )
    private_endpoint_label: str = proto.Field(
        proto.STRING,
        number=11,
    )
    db_version: str = proto.Field(
        proto.STRING,
        number=12,
    )
    is_auto_scaling_enabled: bool = proto.Field(
        proto.BOOL,
        number=14,
    )
    is_storage_auto_scaling_enabled: bool = proto.Field(
        proto.BOOL,
        number=15,
    )
    license_type: LicenseType = proto.Field(
        proto.ENUM,
        number=16,
        enum=LicenseType,
    )
    customer_contacts: MutableSequence[common.CustomerContact] = proto.RepeatedField(
        proto.MESSAGE,
        number=17,
        message=common.CustomerContact,
    )
    secret_id: str = proto.Field(
        proto.STRING,
        number=18,
    )
    vault_id: str = proto.Field(
        proto.STRING,
        number=19,
    )
    maintenance_schedule_type: MaintenanceScheduleType = proto.Field(
        proto.ENUM,
        number=20,
        enum=MaintenanceScheduleType,
    )
    mtls_connection_required: bool = proto.Field(
        proto.BOOL,
        number=34,
    )
    backup_retention_period_days: int = proto.Field(
        proto.INT32,
        number=57,
    )
    actual_used_data_storage_size_tb: float = proto.Field(
        proto.DOUBLE,
        number=21,
    )
    allocated_storage_size_tb: float = proto.Field(
        proto.DOUBLE,
        number=22,
    )
    apex_details: "AutonomousDatabaseApex" = proto.Field(
        proto.MESSAGE,
        number=23,
        message="AutonomousDatabaseApex",
    )
    are_primary_allowlisted_ips_used: bool = proto.Field(
        proto.BOOL,
        number=24,
        optional=True,
    )
    lifecycle_details: str = proto.Field(
        proto.STRING,
        number=25,
    )
    state: "State" = proto.Field(
        proto.ENUM,
        number=26,
        enum="State",
    )
    autonomous_container_database_id: str = proto.Field(
        proto.STRING,
        number=27,
    )
    available_upgrade_versions: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=28,
    )
    connection_strings: "AutonomousDatabaseConnectionStrings" = proto.Field(
        proto.MESSAGE,
        number=29,
        message="AutonomousDatabaseConnectionStrings",
    )
    connection_urls: "AutonomousDatabaseConnectionUrls" = proto.Field(
        proto.MESSAGE,
        number=30,
        message="AutonomousDatabaseConnectionUrls",
    )
    failed_data_recovery_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=31,
        message=duration_pb2.Duration,
    )
    memory_table_gbs: int = proto.Field(
        proto.INT32,
        number=32,
    )
    is_local_data_guard_enabled: bool = proto.Field(
        proto.BOOL,
        number=33,
    )
    local_adg_auto_failover_max_data_loss_limit: int = proto.Field(
        proto.INT32,
        number=35,
    )
    local_standby_db: "AutonomousDatabaseStandbySummary" = proto.Field(
        proto.MESSAGE,
        number=36,
        message="AutonomousDatabaseStandbySummary",
    )
    memory_per_oracle_compute_unit_gbs: int = proto.Field(
        proto.INT32,
        number=37,
    )
    local_disaster_recovery_type: LocalDisasterRecoveryType = proto.Field(
        proto.ENUM,
        number=38,
        enum=LocalDisasterRecoveryType,
    )
    data_safe_state: DataSafeState = proto.Field(
        proto.ENUM,
        number=39,
        enum=DataSafeState,
    )
    database_management_state: DatabaseManagementState = proto.Field(
        proto.ENUM,
        number=40,
        enum=DatabaseManagementState,
    )
    open_mode: OpenMode = proto.Field(
        proto.ENUM,
        number=41,
        enum=OpenMode,
    )
    operations_insights_state: "OperationsInsightsState" = proto.Field(
        proto.ENUM,
        number=42,
        enum="OperationsInsightsState",
    )
    peer_db_ids: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=43,
    )
    permission_level: PermissionLevel = proto.Field(
        proto.ENUM,
        number=44,
        enum=PermissionLevel,
    )
    private_endpoint: str = proto.Field(
        proto.STRING,
        number=45,
    )
    refreshable_mode: RefreshableMode = proto.Field(
        proto.ENUM,
        number=46,
        enum=RefreshableMode,
    )
    refreshable_state: RefreshableState = proto.Field(
        proto.ENUM,
        number=47,
        enum=RefreshableState,
    )
    role: Role = proto.Field(
        proto.ENUM,
        number=48,
        enum=Role,
    )
    scheduled_operation_details: MutableSequence["ScheduledOperationDetails"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=64,
            message="ScheduledOperationDetails",
        )
    )
    sql_web_developer_url: str = proto.Field(
        proto.STRING,
        number=50,
    )
    supported_clone_regions: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=51,
    )
    used_data_storage_size_tbs: int = proto.Field(
        proto.INT32,
        number=53,
    )
    oci_url: str = proto.Field(
        proto.STRING,
        number=54,
    )
    total_auto_backup_storage_size_gbs: float = proto.Field(
        proto.FLOAT,
        number=59,
    )
    next_long_term_backup_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=60,
        message=timestamp_pb2.Timestamp,
    )
    data_guard_role_changed_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=61,
        message=timestamp_pb2.Timestamp,
    )
    disaster_recovery_role_changed_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=62,
        message=timestamp_pb2.Timestamp,
    )
    maintenance_begin_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=65,
        message=timestamp_pb2.Timestamp,
    )
    maintenance_end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=66,
        message=timestamp_pb2.Timestamp,
    )
    allowlisted_ips: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=67,
    )
    encryption_key: "EncryptionKey" = proto.Field(
        proto.MESSAGE,
        number=68,
        message="EncryptionKey",
    )
    encryption_key_history_entries: MutableSequence["EncryptionKeyHistoryEntry"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=69,
            message="EncryptionKeyHistoryEntry",
        )
    )
    service_agent_email: str = proto.Field(
        proto.STRING,
        number=70,
    )
    local_data_guard_enabled: bool = proto.Field(
        proto.BOOL,
        number=71,
        optional=True,
    )
    local_adg_auto_failover_max_data_loss_limit_duration: int = proto.Field(
        proto.INT32,
        number=72,
        optional=True,
    )
    refreshable_clone: bool = proto.Field(
        proto.BOOL,
        number=73,
        optional=True,
    )


class EncryptionKeyHistoryEntry(proto.Message):
    r"""The history of the encryption keys used to encrypt the
    Autonomous Database.

    Attributes:
        encryption_key (google.cloud.oracledatabase_v1.types.EncryptionKey):
            Output only. The encryption key used to
            encrypt the Autonomous Database.
        activation_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The date and time when the
            encryption key was activated on the Autonomous
            Database..
    """

    encryption_key: "EncryptionKey" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="EncryptionKey",
    )
    activation_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )


class EncryptionKey(proto.Message):
    r"""The encryption key used to encrypt the Autonomous Database.

    Attributes:
        provider (google.cloud.oracledatabase_v1.types.EncryptionKey.Provider):
            Optional. The provider of the encryption key.
        kms_key (str):
            Optional. The KMS key used to encrypt the Autonomous
            Database. This field is required if the provider is
            GOOGLE_MANAGED. The name of the KMS key resource in the
            following format:
            ``projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}``.
    """

    class Provider(proto.Enum):
        r"""The provider of the encryption key.

        Values:
            PROVIDER_UNSPECIFIED (0):
                Default unspecified value.
            GOOGLE_MANAGED (1):
                Google Managed KMS key, if selected, please
                provide the KMS key name.
            ORACLE_MANAGED (2):
                Oracle Managed.
        """

        PROVIDER_UNSPECIFIED = 0
        GOOGLE_MANAGED = 1
        ORACLE_MANAGED = 2

    provider: Provider = proto.Field(
        proto.ENUM,
        number=1,
        enum=Provider,
    )
    kms_key: str = proto.Field(
        proto.STRING,
        number=2,
    )


class AutonomousDatabaseApex(proto.Message):
    r"""Oracle APEX Application Development.
    https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/datatypes/AutonomousDatabaseApex

    Attributes:
        apex_version (str):
            Output only. The Oracle APEX Application
            Development version.
        ords_version (str):
            Output only. The Oracle REST Data Services
            (ORDS) version.
    """

    apex_version: str = proto.Field(
        proto.STRING,
        number=1,
    )
    ords_version: str = proto.Field(
        proto.STRING,
        number=2,
    )


class AutonomousDatabaseConnectionStrings(proto.Message):
    r"""The connection string used to connect to the Autonomous
    Database.
    https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/datatypes/AutonomousDatabaseConnectionStrings

    Attributes:
        all_connection_strings (google.cloud.oracledatabase_v1.types.AllConnectionStrings):
            Output only. Returns all connection strings
            that can be used to connect to the Autonomous
            Database.
        dedicated (str):
            Output only. The database service provides
            the least level of resources to each SQL
            statement, but supports the most number of
            concurrent SQL statements.
        high (str):
            Output only. The database service provides
            the highest level of resources to each SQL
            statement.
        low (str):
            Output only. The database service provides
            the least level of resources to each SQL
            statement.
        medium (str):
            Output only. The database service provides a
            lower level of resources to each SQL statement.
        profiles (MutableSequence[google.cloud.oracledatabase_v1.types.DatabaseConnectionStringProfile]):
            Output only. A list of connection string
            profiles to allow clients to group, filter, and
            select values based on the structured metadata.
    """

    all_connection_strings: "AllConnectionStrings" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="AllConnectionStrings",
    )
    dedicated: str = proto.Field(
        proto.STRING,
        number=2,
    )
    high: str = proto.Field(
        proto.STRING,
        number=3,
    )
    low: str = proto.Field(
        proto.STRING,
        number=4,
    )
    medium: str = proto.Field(
        proto.STRING,
        number=5,
    )
    profiles: MutableSequence["DatabaseConnectionStringProfile"] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message="DatabaseConnectionStringProfile",
    )


class DatabaseConnectionStringProfile(proto.Message):
    r"""The connection string profile to allow clients to group.
    https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/datatypes/DatabaseConnectionStringProfile

    Attributes:
        consumer_group (google.cloud.oracledatabase_v1.types.DatabaseConnectionStringProfile.ConsumerGroup):
            Output only. The current consumer group being
            used by the connection.
        display_name (str):
            Output only. The display name for the
            database connection.
        host_format (google.cloud.oracledatabase_v1.types.DatabaseConnectionStringProfile.HostFormat):
            Output only. The host name format being
            currently used in connection string.
        is_regional (bool):
            Output only. This field indicates if the
            connection string is regional and is only
            applicable for cross-region Data Guard.
        protocol (google.cloud.oracledatabase_v1.types.DatabaseConnectionStringProfile.Protocol):
            Output only. The protocol being used by the
            connection.
        session_mode (google.cloud.oracledatabase_v1.types.DatabaseConnectionStringProfile.SessionMode):
            Output only. The current session mode of the
            connection.
        syntax_format (google.cloud.oracledatabase_v1.types.DatabaseConnectionStringProfile.SyntaxFormat):
            Output only. The syntax of the connection
            string.
        tls_authentication (google.cloud.oracledatabase_v1.types.DatabaseConnectionStringProfile.TLSAuthentication):
            Output only. This field indicates the TLS
            authentication type of the connection.
        value (str):
            Output only. The value of the connection
            string.
    """

    class ConsumerGroup(proto.Enum):
        r"""The various consumer groups available in the connection
        string profile.

        Values:
            CONSUMER_GROUP_UNSPECIFIED (0):
                Default unspecified value.
            HIGH (1):
                High consumer group.
            MEDIUM (2):
                Medium consumer group.
            LOW (3):
                Low consumer group.
            TP (4):
                TP consumer group.
            TPURGENT (5):
                TPURGENT consumer group.
        """

        CONSUMER_GROUP_UNSPECIFIED = 0
        HIGH = 1
        MEDIUM = 2
        LOW = 3
        TP = 4
        TPURGENT = 5

    class HostFormat(proto.Enum):
        r"""The host name format being used in the connection string.

        Values:
            HOST_FORMAT_UNSPECIFIED (0):
                Default unspecified value.
            FQDN (1):
                FQDN
            IP (2):
                IP
        """

        HOST_FORMAT_UNSPECIFIED = 0
        FQDN = 1
        IP = 2

    class Protocol(proto.Enum):
        r"""The protocol being used by the connection.

        Values:
            PROTOCOL_UNSPECIFIED (0):
                Default unspecified value.
            TCP (1):
                Tcp
            TCPS (2):
                Tcps
        """

        PROTOCOL_UNSPECIFIED = 0
        TCP = 1
        TCPS = 2

    class SessionMode(proto.Enum):
        r"""The session mode of the connection.

        Values:
            SESSION_MODE_UNSPECIFIED (0):
                Default unspecified value.
            DIRECT (1):
                Direct
            INDIRECT (2):
                Indirect
        """

        SESSION_MODE_UNSPECIFIED = 0
        DIRECT = 1
        INDIRECT = 2

    class SyntaxFormat(proto.Enum):
        r"""Specifies syntax of the connection string.

        Values:
            SYNTAX_FORMAT_UNSPECIFIED (0):
                Default unspecified value.
            LONG (1):
                Long
            EZCONNECT (2):
                Ezconnect
            EZCONNECTPLUS (3):
                Ezconnectplus
        """

        SYNTAX_FORMAT_UNSPECIFIED = 0
        LONG = 1
        EZCONNECT = 2
        EZCONNECTPLUS = 3

    class TLSAuthentication(proto.Enum):
        r"""This field indicates the TLS authentication type of the
        connection.

        Values:
            TLS_AUTHENTICATION_UNSPECIFIED (0):
                Default unspecified value.
            SERVER (1):
                Server
            MUTUAL (2):
                Mutual
        """

        TLS_AUTHENTICATION_UNSPECIFIED = 0
        SERVER = 1
        MUTUAL = 2

    consumer_group: ConsumerGroup = proto.Field(
        proto.ENUM,
        number=1,
        enum=ConsumerGroup,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    host_format: HostFormat = proto.Field(
        proto.ENUM,
        number=3,
        enum=HostFormat,
    )
    is_regional: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    protocol: Protocol = proto.Field(
        proto.ENUM,
        number=5,
        enum=Protocol,
    )
    session_mode: SessionMode = proto.Field(
        proto.ENUM,
        number=6,
        enum=SessionMode,
    )
    syntax_format: SyntaxFormat = proto.Field(
        proto.ENUM,
        number=7,
        enum=SyntaxFormat,
    )
    tls_authentication: TLSAuthentication = proto.Field(
        proto.ENUM,
        number=8,
        enum=TLSAuthentication,
    )
    value: str = proto.Field(
        proto.STRING,
        number=9,
    )


class AllConnectionStrings(proto.Message):
    r"""A list of all connection strings that can be used to connect
    to the Autonomous Database.

    Attributes:
        high (str):
            Output only. The database service provides
            the highest level of resources to each SQL
            statement.
        low (str):
            Output only. The database service provides
            the least level of resources to each SQL
            statement.
        medium (str):
            Output only. The database service provides a
            lower level of resources to each SQL statement.
    """

    high: str = proto.Field(
        proto.STRING,
        number=1,
    )
    low: str = proto.Field(
        proto.STRING,
        number=2,
    )
    medium: str = proto.Field(
        proto.STRING,
        number=3,
    )


class AutonomousDatabaseConnectionUrls(proto.Message):
    r"""The URLs for accessing Oracle Application Express (APEX) and
    SQL Developer Web with a browser from a Compute instance.
    https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/datatypes/AutonomousDatabaseConnectionUrls

    Attributes:
        apex_uri (str):
            Output only. Oracle Application Express
            (APEX) URL.
        database_transforms_uri (str):
            Output only. The URL of the Database
            Transforms for the Autonomous Database.
        graph_studio_uri (str):
            Output only. The URL of the Graph Studio for
            the Autonomous Database.
        machine_learning_notebook_uri (str):
            Output only. The URL of the Oracle Machine
            Learning (OML) Notebook for the Autonomous
            Database.
        machine_learning_user_management_uri (str):
            Output only. The URL of Machine Learning user
            management the Autonomous Database.
        mongo_db_uri (str):
            Output only. The URL of the MongoDB API for
            the Autonomous Database.
        ords_uri (str):
            Output only. The Oracle REST Data Services
            (ORDS) URL of the Web Access for the Autonomous
            Database.
        sql_dev_web_uri (str):
            Output only. The URL of the Oracle SQL
            Developer Web for the Autonomous Database.
    """

    apex_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    database_transforms_uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    graph_studio_uri: str = proto.Field(
        proto.STRING,
        number=3,
    )
    machine_learning_notebook_uri: str = proto.Field(
        proto.STRING,
        number=4,
    )
    machine_learning_user_management_uri: str = proto.Field(
        proto.STRING,
        number=5,
    )
    mongo_db_uri: str = proto.Field(
        proto.STRING,
        number=6,
    )
    ords_uri: str = proto.Field(
        proto.STRING,
        number=7,
    )
    sql_dev_web_uri: str = proto.Field(
        proto.STRING,
        number=8,
    )


class AutonomousDatabaseStandbySummary(proto.Message):
    r"""Autonomous Data Guard standby database details.
    https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/datatypes/AutonomousDatabaseStandbySummary

    Attributes:
        lag_time_duration (google.protobuf.duration_pb2.Duration):
            Output only. The amount of time, in seconds,
            that the data of the standby database lags in
            comparison to the data of the primary database.
        lifecycle_details (str):
            Output only. The additional details about the
            current lifecycle state of the Autonomous
            Database.
        state (google.cloud.oracledatabase_v1.types.State):
            Output only. The current lifecycle state of
            the Autonomous Database.
        data_guard_role_changed_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The date and time the Autonomous
            Data Guard role was switched for the standby
            Autonomous Database.
        disaster_recovery_role_changed_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The date and time the Disaster
            Recovery role was switched for the standby
            Autonomous Database.
    """

    lag_time_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=1,
        message=duration_pb2.Duration,
    )
    lifecycle_details: str = proto.Field(
        proto.STRING,
        number=2,
    )
    state: "State" = proto.Field(
        proto.ENUM,
        number=3,
        enum="State",
    )
    data_guard_role_changed_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    disaster_recovery_role_changed_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )


class ScheduledOperationDetails(proto.Message):
    r"""Details of scheduled operation.
    https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/datatypes/ScheduledOperationDetails

    Attributes:
        day_of_week (google.type.dayofweek_pb2.DayOfWeek):
            Output only. Day of week.
        start_time (google.type.timeofday_pb2.TimeOfDay):
            Output only. Auto start time.
        stop_time (google.type.timeofday_pb2.TimeOfDay):
            Output only. Auto stop time.
    """

    day_of_week: dayofweek_pb2.DayOfWeek = proto.Field(
        proto.ENUM,
        number=1,
        enum=dayofweek_pb2.DayOfWeek,
    )
    start_time: timeofday_pb2.TimeOfDay = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timeofday_pb2.TimeOfDay,
    )
    stop_time: timeofday_pb2.TimeOfDay = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timeofday_pb2.TimeOfDay,
    )


class AutonomousDatabaseRefreshableClone(proto.Message):
    r"""An Autonomous Database refreshable clone

    Attributes:
        name (str):
            Output only. The GCP resource name of the
            Autonomous Database.
        region (str):
            Output only. The Google Cloud region where
            the refreshable clone exists.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    region: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
