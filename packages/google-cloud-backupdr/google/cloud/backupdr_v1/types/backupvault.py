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

from google.cloud.backupdr_v1.types import (
    backupvault_alloydb,
    backupvault_ba,
    backupvault_cloudsql,
    backupvault_disk,
    backupvault_gce,
)

__protobuf__ = proto.module(
    package="google.cloud.backupdr.v1",
    manifest={
        "BackupConfigState",
        "BackupView",
        "BackupVaultView",
        "BackupVault",
        "DataSource",
        "BackupConfigInfo",
        "GcpBackupConfig",
        "BackupApplianceBackupConfig",
        "DataSourceGcpResource",
        "DataSourceBackupApplianceApplication",
        "ServiceLockInfo",
        "BackupApplianceLockInfo",
        "BackupLock",
        "Backup",
        "CreateBackupVaultRequest",
        "ListBackupVaultsRequest",
        "ListBackupVaultsResponse",
        "FetchUsableBackupVaultsRequest",
        "FetchUsableBackupVaultsResponse",
        "FetchBackupsForResourceTypeRequest",
        "FetchBackupsForResourceTypeResponse",
        "GetBackupVaultRequest",
        "UpdateBackupVaultRequest",
        "DeleteBackupVaultRequest",
        "ListDataSourcesRequest",
        "ListDataSourcesResponse",
        "GetDataSourceRequest",
        "UpdateDataSourceRequest",
        "ListBackupsRequest",
        "ListBackupsResponse",
        "GetBackupRequest",
        "UpdateBackupRequest",
        "DeleteBackupRequest",
        "RestoreBackupRequest",
        "RestoreBackupResponse",
        "TargetResource",
        "GcpResource",
        "BackupGcpResource",
    },
)


class BackupConfigState(proto.Enum):
    r"""Backup configuration state. Is the resource configured for
    backup?

    Values:
        BACKUP_CONFIG_STATE_UNSPECIFIED (0):
            The possible states of backup configuration.
            Status not set.
        ACTIVE (1):
            The data source is actively protected (i.e.
            there is a BackupPlanAssociation or Appliance
            SLA pointing to it)
        PASSIVE (2):
            The data source is no longer protected (but
            may have backups under it)
    """

    BACKUP_CONFIG_STATE_UNSPECIFIED = 0
    ACTIVE = 1
    PASSIVE = 2


class BackupView(proto.Enum):
    r"""BackupView contains enum options for Partial and Full view.

    Values:
        BACKUP_VIEW_UNSPECIFIED (0):
            If the value is not set, the default 'FULL'
            view is used.
        BACKUP_VIEW_BASIC (1):
            Includes basic data about the Backup, but not
            the full contents.
        BACKUP_VIEW_FULL (2):
            Includes all data about the Backup.
            This is the default value (for both ListBackups
            and GetBackup).
    """

    BACKUP_VIEW_UNSPECIFIED = 0
    BACKUP_VIEW_BASIC = 1
    BACKUP_VIEW_FULL = 2


class BackupVaultView(proto.Enum):
    r"""BackupVaultView contains enum options for Partial and Full
    view.

    Values:
        BACKUP_VAULT_VIEW_UNSPECIFIED (0):
            If the value is not set, the default 'FULL'
            view is used.
        BACKUP_VAULT_VIEW_BASIC (1):
            Includes basic data about the Backup Vault,
            but not the full contents.
        BACKUP_VAULT_VIEW_FULL (2):
            Includes all data about the Backup Vault.
            This is the default value (for both
            ListBackupVaults and GetBackupVault).
    """

    BACKUP_VAULT_VIEW_UNSPECIFIED = 0
    BACKUP_VAULT_VIEW_BASIC = 1
    BACKUP_VAULT_VIEW_FULL = 2


class BackupVault(proto.Message):
    r"""Message describing a BackupVault object.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Output only. Identifier. Name of the backup vault to create.
            It must have the
            format\ ``"projects/{project}/locations/{location}/backupVaults/{backupvault}"``.
            ``{backupvault}`` cannot be changed after creation. It must
            be between 3-63 characters long and must be unique within
            the project and location.
        description (str):
            Optional. The description of the BackupVault
            instance (2048 characters or less).

            This field is a member of `oneof`_ ``_description``.
        labels (MutableMapping[str, str]):
            Optional. Resource labels to represent user
            provided metadata. No labels currently defined:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the instance was
            created.

            This field is a member of `oneof`_ ``_create_time``.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the instance was
            updated.

            This field is a member of `oneof`_ ``_update_time``.
        backup_minimum_enforced_retention_duration (google.protobuf.duration_pb2.Duration):
            Required. The default and minimum enforced
            retention for each backup within the backup
            vault.  The enforced retention for each backup
            can be extended.

            This field is a member of `oneof`_ ``_backup_minimum_enforced_retention_duration``.
        backup_retention_inheritance (google.cloud.backupdr_v1.types.BackupVault.BackupRetentionInheritance):
            Optional. Setting for how a backup's enforced
            retention end time is inherited.

            This field is a member of `oneof`_ ``_backup_retention_inheritance``.
        deletable (bool):
            Output only. Set to true when there are no
            backups nested under this resource.

            This field is a member of `oneof`_ ``_deletable``.
        etag (str):
            Optional. Server specified ETag for the
            backup vault resource to prevent simultaneous
            updates from overwiting each other.

            This field is a member of `oneof`_ ``_etag``.
        state (google.cloud.backupdr_v1.types.BackupVault.State):
            Output only. The BackupVault resource
            instance state.
        effective_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. Time after which the BackupVault
            resource is locked.

            This field is a member of `oneof`_ ``_effective_time``.
        backup_count (int):
            Output only. The number of backups in this
            backup vault.
        service_account (str):
            Output only. Service account used by the
            BackupVault Service for this BackupVault.  The
            user should grant this account permissions in
            their workload project to enable the service to
            run backups and restores there.
        total_stored_bytes (int):
            Output only. Total size of the storage used
            by all backup resources.
        uid (str):
            Output only. Immutable after resource
            creation until resource deletion.
        annotations (MutableMapping[str, str]):
            Optional. User annotations. See
            https://google.aip.dev/128#annotations Stores
            small amounts of arbitrary data.
        access_restriction (google.cloud.backupdr_v1.types.BackupVault.AccessRestriction):
            Optional. Restricts access to certain sources and
            destinations for data being sent into, or restored from, the
            backup vault. Defaults to WITHIN_ORGANIZATION if not
            provided during creation.
        encryption_config (google.cloud.backupdr_v1.types.BackupVault.EncryptionConfig):
            Optional. The encryption config of the backup
            vault.

            This field is a member of `oneof`_ ``_encryption_config``.
    """

    class BackupRetentionInheritance(proto.Enum):
        r"""How a backup's enforced retention end time is inherited.

        Values:
            BACKUP_RETENTION_INHERITANCE_UNSPECIFIED (0):
                Inheritance behavior not set. This will default to
                ``INHERIT_VAULT_RETENTION``.
            INHERIT_VAULT_RETENTION (1):
                The enforced retention end time of a backup will be
                inherited from the backup vault's
                ``backup_minimum_enforced_retention_duration`` field.

                This is the default behavior.
            MATCH_BACKUP_EXPIRE_TIME (2):
                The enforced retention end time of a backup
                will always match the expire time of the backup.

                If this is set, the backup's enforced retention
                end time will be set to match the expire time
                during creation of the backup. When updating,
                the ERET and expire time must be updated
                together and have the same value. Invalid update
                requests will be rejected by the server.
        """

        BACKUP_RETENTION_INHERITANCE_UNSPECIFIED = 0
        INHERIT_VAULT_RETENTION = 1
        MATCH_BACKUP_EXPIRE_TIME = 2

    class State(proto.Enum):
        r"""Holds the state of the backup vault resource.

        Values:
            STATE_UNSPECIFIED (0):
                State not set.
            CREATING (1):
                The backup vault is being created.
            ACTIVE (2):
                The backup vault has been created and is
                fully usable.
            DELETING (3):
                The backup vault is being deleted.
            ERROR (4):
                The backup vault is experiencing an issue and
                might be unusable.
            UPDATING (5):
                The backup vault is being updated.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        ACTIVE = 2
        DELETING = 3
        ERROR = 4
        UPDATING = 5

    class AccessRestriction(proto.Enum):
        r"""Holds the access restriction for the backup vault.

        Values:
            ACCESS_RESTRICTION_UNSPECIFIED (0):
                Access restriction not set. If user does not provide any
                value or pass this value, it will be changed to
                WITHIN_ORGANIZATION.
            WITHIN_PROJECT (1):
                Access to or from resources outside your
                current project will be denied.
            WITHIN_ORGANIZATION (2):
                Access to or from resources outside your
                current organization will be denied.
            UNRESTRICTED (3):
                No access restriction.
            WITHIN_ORG_BUT_UNRESTRICTED_FOR_BA (4):
                Access to or from resources outside your
                current organization will be denied except for
                backup appliance.
        """

        ACCESS_RESTRICTION_UNSPECIFIED = 0
        WITHIN_PROJECT = 1
        WITHIN_ORGANIZATION = 2
        UNRESTRICTED = 3
        WITHIN_ORG_BUT_UNRESTRICTED_FOR_BA = 4

    class EncryptionConfig(proto.Message):
        r"""Message describing the EncryptionConfig of backup vault.
        This determines how data within the vault is encrypted at rest.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            kms_key_name (str):
                Optional. The Cloud KMS key name to encrypt
                backups in this backup vault. Must be in the
                same region as the vault. Some workload backups
                like compute disk backups may use their
                inherited source key instead. Format:

                projects/{project}/locations/{location}/keyRings/{ring}/cryptoKeys/{key}

                This field is a member of `oneof`_ ``_kms_key_name``.
        """

        kms_key_name: str = proto.Field(
            proto.STRING,
            number=1,
            optional=True,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=3,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        optional=True,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        optional=True,
        message=timestamp_pb2.Timestamp,
    )
    backup_minimum_enforced_retention_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=20,
        optional=True,
        message=duration_pb2.Duration,
    )
    backup_retention_inheritance: BackupRetentionInheritance = proto.Field(
        proto.ENUM,
        number=27,
        optional=True,
        enum=BackupRetentionInheritance,
    )
    deletable: bool = proto.Field(
        proto.BOOL,
        number=8,
        optional=True,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=9,
        optional=True,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=10,
        enum=State,
    )
    effective_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=12,
        optional=True,
        message=timestamp_pb2.Timestamp,
    )
    backup_count: int = proto.Field(
        proto.INT64,
        number=17,
    )
    service_account: str = proto.Field(
        proto.STRING,
        number=18,
    )
    total_stored_bytes: int = proto.Field(
        proto.INT64,
        number=19,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=21,
    )
    annotations: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=22,
    )
    access_restriction: AccessRestriction = proto.Field(
        proto.ENUM,
        number=24,
        enum=AccessRestriction,
    )
    encryption_config: EncryptionConfig = proto.Field(
        proto.MESSAGE,
        number=29,
        optional=True,
        message=EncryptionConfig,
    )


class DataSource(proto.Message):
    r"""Message describing a DataSource object.
    Datasource object used to represent Datasource details for both
    admin and basic view.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Output only. Identifier. Name of the datasource to create.
            It must have the
            format\ ``"projects/{project}/locations/{location}/backupVaults/{backupvault}/dataSources/{datasource}"``.
            ``{datasource}`` cannot be changed after creation. It must
            be between 3-63 characters long and must be unique within
            the backup vault.
        state (google.cloud.backupdr_v1.types.DataSource.State):
            Output only. The DataSource resource instance
            state.
        labels (MutableMapping[str, str]):
            Optional. Resource labels to represent user
            provided metadata. No labels currently defined:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the instance was
            created.

            This field is a member of `oneof`_ ``_create_time``.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the instance was
            updated.

            This field is a member of `oneof`_ ``_update_time``.
        backup_count (int):
            Number of backups in the data source.

            This field is a member of `oneof`_ ``_backup_count``.
        etag (str):
            Server specified ETag for the
            ManagementServer resource to prevent
            simultaneous updates from overwiting each other.

            This field is a member of `oneof`_ ``_etag``.
        total_stored_bytes (int):
            The number of bytes (metadata and data)
            stored in this datasource.

            This field is a member of `oneof`_ ``_total_stored_bytes``.
        config_state (google.cloud.backupdr_v1.types.BackupConfigState):
            Output only. The backup configuration state.
        backup_config_info (google.cloud.backupdr_v1.types.BackupConfigInfo):
            Output only. Details of how the resource is
            configured for backup.
        data_source_gcp_resource (google.cloud.backupdr_v1.types.DataSourceGcpResource):
            The backed up resource is a Google Cloud
            resource. The word 'DataSource' was included in
            the names to indicate that this is the
            representation of the Google Cloud resource used
            within the DataSource object.

            This field is a member of `oneof`_ ``source_resource``.
        data_source_backup_appliance_application (google.cloud.backupdr_v1.types.DataSourceBackupApplianceApplication):
            The backed up resource is a backup appliance
            application.

            This field is a member of `oneof`_ ``source_resource``.
        backup_blocked_by_vault_access_restriction (bool):
            Output only. This field is set to true if the
            backup is blocked by vault access restriction.
    """

    class State(proto.Enum):
        r"""Holds the state of the data source resource.

        Values:
            STATE_UNSPECIFIED (0):
                State not set.
            CREATING (1):
                The data source is being created.
            ACTIVE (2):
                The data source has been created and is fully
                usable.
            DELETING (3):
                The data source is being deleted.
            ERROR (4):
                The data source is experiencing an issue and
                might be unusable.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        ACTIVE = 2
        DELETING = 3
        ERROR = 4

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=21,
        enum=State,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        optional=True,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        optional=True,
        message=timestamp_pb2.Timestamp,
    )
    backup_count: int = proto.Field(
        proto.INT64,
        number=7,
        optional=True,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=14,
        optional=True,
    )
    total_stored_bytes: int = proto.Field(
        proto.INT64,
        number=23,
        optional=True,
    )
    config_state: "BackupConfigState" = proto.Field(
        proto.ENUM,
        number=24,
        enum="BackupConfigState",
    )
    backup_config_info: "BackupConfigInfo" = proto.Field(
        proto.MESSAGE,
        number=25,
        message="BackupConfigInfo",
    )
    data_source_gcp_resource: "DataSourceGcpResource" = proto.Field(
        proto.MESSAGE,
        number=26,
        oneof="source_resource",
        message="DataSourceGcpResource",
    )
    data_source_backup_appliance_application: "DataSourceBackupApplianceApplication" = (
        proto.Field(
            proto.MESSAGE,
            number=27,
            oneof="source_resource",
            message="DataSourceBackupApplianceApplication",
        )
    )
    backup_blocked_by_vault_access_restriction: bool = proto.Field(
        proto.BOOL,
        number=28,
    )


class BackupConfigInfo(proto.Message):
    r"""BackupConfigInfo has information about how the resource is
    configured for Backup and about the most recent backup to this
    vault.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        last_backup_state (google.cloud.backupdr_v1.types.BackupConfigInfo.LastBackupState):
            Output only. The status of the last backup to
            this BackupVault
        last_successful_backup_consistency_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. If the last backup were
            successful, this field has the consistency date.
        last_backup_error (google.rpc.status_pb2.Status):
            Output only. If the last backup failed, this
            field has the error message.
        gcp_backup_config (google.cloud.backupdr_v1.types.GcpBackupConfig):
            Configuration for a Google Cloud resource.

            This field is a member of `oneof`_ ``backup_config``.
        backup_appliance_backup_config (google.cloud.backupdr_v1.types.BackupApplianceBackupConfig):
            Configuration for an application backed up by
            a Backup Appliance.

            This field is a member of `oneof`_ ``backup_config``.
    """

    class LastBackupState(proto.Enum):
        r"""LastBackupstate tracks whether the last backup was not yet
        started, successful, failed, or could not be run because of the
        lack of permissions.

        Values:
            LAST_BACKUP_STATE_UNSPECIFIED (0):
                Status not set.
            FIRST_BACKUP_PENDING (1):
                The first backup has not yet completed
            SUCCEEDED (2):
                The most recent backup was successful
            FAILED (3):
                The most recent backup failed
            PERMISSION_DENIED (4):
                The most recent backup could not be
                run/failed because of the lack of permissions
        """

        LAST_BACKUP_STATE_UNSPECIFIED = 0
        FIRST_BACKUP_PENDING = 1
        SUCCEEDED = 2
        FAILED = 3
        PERMISSION_DENIED = 4

    last_backup_state: LastBackupState = proto.Field(
        proto.ENUM,
        number=1,
        enum=LastBackupState,
    )
    last_successful_backup_consistency_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    last_backup_error: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=3,
        message=status_pb2.Status,
    )
    gcp_backup_config: "GcpBackupConfig" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="backup_config",
        message="GcpBackupConfig",
    )
    backup_appliance_backup_config: "BackupApplianceBackupConfig" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="backup_config",
        message="BackupApplianceBackupConfig",
    )


class GcpBackupConfig(proto.Message):
    r"""GcpBackupConfig captures the Backup configuration details for
    Google Cloud resources. All Google Cloud resources regardless of
    type are protected with backup plan associations.

    Attributes:
        backup_plan (str):
            The name of the backup plan.
        backup_plan_description (str):
            The description of the backup plan.
        backup_plan_association (str):
            The name of the backup plan association.
        backup_plan_rules (MutableSequence[str]):
            The names of the backup plan rules which
            point to this backupvault
        backup_plan_revision_name (str):
            The name of the backup plan revision.
        backup_plan_revision_id (str):
            The user friendly id of the backup plan
            revision. E.g. v0, v1 etc.
    """

    backup_plan: str = proto.Field(
        proto.STRING,
        number=1,
    )
    backup_plan_description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    backup_plan_association: str = proto.Field(
        proto.STRING,
        number=3,
    )
    backup_plan_rules: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    backup_plan_revision_name: str = proto.Field(
        proto.STRING,
        number=5,
    )
    backup_plan_revision_id: str = proto.Field(
        proto.STRING,
        number=6,
    )


class BackupApplianceBackupConfig(proto.Message):
    r"""BackupApplianceBackupConfig captures the backup configuration
    for applications that are protected by Backup Appliances.

    Attributes:
        backup_appliance_name (str):
            The name of the backup appliance.
        backup_appliance_id (int):
            The ID of the backup appliance.
        sla_id (int):
            The ID of the SLA of this application.
        application_name (str):
            The name of the application.
        host_name (str):
            The name of the host where the application is
            running.
        slt_name (str):
            The name of the SLT associated with the
            application.
        slp_name (str):
            The name of the SLP associated with the
            application.
    """

    backup_appliance_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    backup_appliance_id: int = proto.Field(
        proto.INT64,
        number=2,
    )
    sla_id: int = proto.Field(
        proto.INT64,
        number=3,
    )
    application_name: str = proto.Field(
        proto.STRING,
        number=4,
    )
    host_name: str = proto.Field(
        proto.STRING,
        number=5,
    )
    slt_name: str = proto.Field(
        proto.STRING,
        number=6,
    )
    slp_name: str = proto.Field(
        proto.STRING,
        number=7,
    )


class DataSourceGcpResource(proto.Message):
    r"""DataSourceGcpResource is used for protected resources that
    are Google Cloud Resources. This name is easeier to understand
    than GcpResourceDataSource or GcpDataSourceResource

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        gcp_resourcename (str):
            Output only. Full resource pathname URL of
            the source Google Cloud resource.
        location (str):
            Location of the resource:
            <region>/<zone>/"global"/"unspecified".
        type_ (str):
            The type of the Google Cloud resource. Use
            the Unified Resource Type, eg.
            compute.googleapis.com/Instance.
        compute_instance_datasource_properties (google.cloud.backupdr_v1.types.ComputeInstanceDataSourceProperties):
            ComputeInstanceDataSourceProperties has a
            subset of Compute Instance properties that are
            useful at the Datasource level.

            This field is a member of `oneof`_ ``gcp_resource_properties``.
        cloud_sql_instance_datasource_properties (google.cloud.backupdr_v1.types.CloudSqlInstanceDataSourceProperties):
            Output only.
            CloudSqlInstanceDataSourceProperties has a
            subset of Cloud SQL Instance properties that are
            useful at the Datasource level.

            This field is a member of `oneof`_ ``gcp_resource_properties``.
        alloy_db_cluster_datasource_properties (google.cloud.backupdr_v1.types.AlloyDBClusterDataSourceProperties):
            Output only.
            AlloyDBClusterDataSourceProperties has a subset
            of AlloyDB cluster properties that are useful at
            the Datasource level.

            This field is a member of `oneof`_ ``gcp_resource_properties``.
        disk_datasource_properties (google.cloud.backupdr_v1.types.DiskDataSourceProperties):
            DiskDataSourceProperties has a subset of Disk
            properties that are useful at the Datasource
            level.

            This field is a member of `oneof`_ ``gcp_resource_properties``.
    """

    gcp_resourcename: str = proto.Field(
        proto.STRING,
        number=1,
    )
    location: str = proto.Field(
        proto.STRING,
        number=2,
    )
    type_: str = proto.Field(
        proto.STRING,
        number=3,
    )
    compute_instance_datasource_properties: backupvault_gce.ComputeInstanceDataSourceProperties = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="gcp_resource_properties",
        message=backupvault_gce.ComputeInstanceDataSourceProperties,
    )
    cloud_sql_instance_datasource_properties: backupvault_cloudsql.CloudSqlInstanceDataSourceProperties = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="gcp_resource_properties",
        message=backupvault_cloudsql.CloudSqlInstanceDataSourceProperties,
    )
    alloy_db_cluster_datasource_properties: backupvault_alloydb.AlloyDBClusterDataSourceProperties = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="gcp_resource_properties",
        message=backupvault_alloydb.AlloyDBClusterDataSourceProperties,
    )
    disk_datasource_properties: backupvault_disk.DiskDataSourceProperties = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="gcp_resource_properties",
        message=backupvault_disk.DiskDataSourceProperties,
    )


class DataSourceBackupApplianceApplication(proto.Message):
    r"""BackupApplianceApplication describes a Source Resource when
    it is an application backed up by a BackupAppliance.

    Attributes:
        application_name (str):
            The name of the Application as known to the
            Backup Appliance.
        backup_appliance (str):
            Appliance name.
        appliance_id (int):
            Appliance Id of the Backup Appliance.
        type_ (str):
            The type of the application. e.g. VMBackup
        application_id (int):
            The appid field of the application within the
            Backup Appliance.
        hostname (str):
            Hostname of the host where the application is
            running.
        host_id (int):
            Hostid of the application host.
    """

    application_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    backup_appliance: str = proto.Field(
        proto.STRING,
        number=2,
    )
    appliance_id: int = proto.Field(
        proto.INT64,
        number=3,
    )
    type_: str = proto.Field(
        proto.STRING,
        number=4,
    )
    application_id: int = proto.Field(
        proto.INT64,
        number=8,
    )
    hostname: str = proto.Field(
        proto.STRING,
        number=6,
    )
    host_id: int = proto.Field(
        proto.INT64,
        number=7,
    )


class ServiceLockInfo(proto.Message):
    r"""ServiceLockInfo represents the details of a lock taken by the
    service on a Backup resource.

    Attributes:
        operation (str):
            Output only. The name of the operation that
            created this lock. The lock will automatically
            be released when the operation completes.
    """

    operation: str = proto.Field(
        proto.STRING,
        number=1,
    )


class BackupApplianceLockInfo(proto.Message):
    r"""BackupApplianceLockInfo contains metadata about the
    backupappliance that created the lock.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        backup_appliance_id (int):
            Required. The ID of the backup/recovery
            appliance that created this lock.
        backup_appliance_name (str):
            Required. The name of the backup/recovery
            appliance that created this lock.
        lock_reason (str):
            Required. The reason for the lock: e.g.
            MOUNT/RESTORE/BACKUP/etc.  The value of this
            string is only meaningful to the client and it
            is not interpreted by the BackupVault service.
        job_name (str):
            The job name on the backup/recovery appliance
            that created this lock.

            This field is a member of `oneof`_ ``lock_source``.
        backup_image (str):
            The image name that depends on this Backup.

            This field is a member of `oneof`_ ``lock_source``.
        sla_id (int):
            The SLA on the backup/recovery appliance that
            owns the lock.

            This field is a member of `oneof`_ ``lock_source``.
    """

    backup_appliance_id: int = proto.Field(
        proto.INT64,
        number=1,
    )
    backup_appliance_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    lock_reason: str = proto.Field(
        proto.STRING,
        number=5,
    )
    job_name: str = proto.Field(
        proto.STRING,
        number=6,
        oneof="lock_source",
    )
    backup_image: str = proto.Field(
        proto.STRING,
        number=7,
        oneof="lock_source",
    )
    sla_id: int = proto.Field(
        proto.INT64,
        number=8,
        oneof="lock_source",
    )


class BackupLock(proto.Message):
    r"""BackupLock represents a single lock on a Backup resource.  An
    unexpired lock on a Backup prevents the Backup from being
    deleted.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        lock_until_time (google.protobuf.timestamp_pb2.Timestamp):
            Required. The time after which this lock is
            not considered valid and will no longer protect
            the Backup from deletion.
        backup_appliance_lock_info (google.cloud.backupdr_v1.types.BackupApplianceLockInfo):
            If the client is a backup and recovery
            appliance, this contains metadata about why the
            lock exists.

            This field is a member of `oneof`_ ``ClientLockInfo``.
        service_lock_info (google.cloud.backupdr_v1.types.ServiceLockInfo):
            Output only. Contains metadata about the lock
            exist for Google Cloud native backups.

            This field is a member of `oneof`_ ``ClientLockInfo``.
    """

    lock_until_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    backup_appliance_lock_info: "BackupApplianceLockInfo" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="ClientLockInfo",
        message="BackupApplianceLockInfo",
    )
    service_lock_info: "ServiceLockInfo" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="ClientLockInfo",
        message="ServiceLockInfo",
    )


class Backup(proto.Message):
    r"""Message describing a Backup object.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Output only. Identifier. Name of the backup to create. It
            must have the
            format\ ``"projects/<project>/locations/<location>/backupVaults/<backupvault>/dataSources/{datasource}/backups/{backup}"``.
            ``{backup}`` cannot be changed after creation. It must be
            between 3-63 characters long and must be unique within the
            datasource.
        description (str):
            Output only. The description of the Backup
            instance (2048 characters or less).

            This field is a member of `oneof`_ ``_description``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the instance was
            created.

            This field is a member of `oneof`_ ``_create_time``.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the instance was
            updated.

            This field is a member of `oneof`_ ``_update_time``.
        labels (MutableMapping[str, str]):
            Optional. Resource labels to represent user
            provided metadata. No labels currently defined.
        enforced_retention_end_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. The backup can not be deleted
            before this time.

            This field is a member of `oneof`_ ``_enforced_retention_end_time``.
        backup_retention_inheritance (google.cloud.backupdr_v1.types.BackupVault.BackupRetentionInheritance):
            Output only. Setting for how the enforced
            retention end time is inherited. This value is
            copied from this backup's BackupVault.

            This field is a member of `oneof`_ ``_backup_retention_inheritance``.
        expire_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. When this backup is automatically
            expired.

            This field is a member of `oneof`_ ``_expire_time``.
        consistency_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The point in time when this
            backup was captured from the source.

            This field is a member of `oneof`_ ``_consistency_time``.
        etag (str):
            Optional. Server specified ETag to prevent
            updates from overwriting each other.

            This field is a member of `oneof`_ ``_etag``.
        state (google.cloud.backupdr_v1.types.Backup.State):
            Output only. The Backup resource instance
            state.
        service_locks (MutableSequence[google.cloud.backupdr_v1.types.BackupLock]):
            Output only. The list of BackupLocks taken by
            the service to prevent the deletion of the
            backup.
        backup_appliance_locks (MutableSequence[google.cloud.backupdr_v1.types.BackupLock]):
            Optional. The list of BackupLocks taken by
            the accessor Backup Appliance.
        compute_instance_backup_properties (google.cloud.backupdr_v1.types.ComputeInstanceBackupProperties):
            Output only. Compute Engine specific backup
            properties.

            This field is a member of `oneof`_ ``backup_properties``.
        cloud_sql_instance_backup_properties (google.cloud.backupdr_v1.types.CloudSqlInstanceBackupProperties):
            Output only. Cloud SQL specific backup
            properties.

            This field is a member of `oneof`_ ``backup_properties``.
        backup_appliance_backup_properties (google.cloud.backupdr_v1.types.BackupApplianceBackupProperties):
            Output only. Backup Appliance specific backup
            properties.

            This field is a member of `oneof`_ ``backup_properties``.
        alloy_db_backup_properties (google.cloud.backupdr_v1.types.AlloyDbClusterBackupProperties):
            Output only. AlloyDB specific backup
            properties.

            This field is a member of `oneof`_ ``backup_properties``.
        disk_backup_properties (google.cloud.backupdr_v1.types.DiskBackupProperties):
            Output only. Disk specific backup properties.

            This field is a member of `oneof`_ ``backup_properties``.
        backup_type (google.cloud.backupdr_v1.types.Backup.BackupType):
            Output only. Type of the backup, unspecified,
            scheduled or ondemand.
        gcp_backup_plan_info (google.cloud.backupdr_v1.types.Backup.GCPBackupPlanInfo):
            Output only. Configuration for a Google Cloud
            resource.

            This field is a member of `oneof`_ ``plan_info``.
        resource_size_bytes (int):
            Output only. source resource size in bytes at
            the time of the backup.
        satisfies_pzs (bool):
            Optional. Output only. Reserved for future
            use.

            This field is a member of `oneof`_ ``_satisfies_pzs``.
        satisfies_pzi (bool):
            Optional. Output only. Reserved for future
            use.

            This field is a member of `oneof`_ ``_satisfies_pzi``.
        gcp_resource (google.cloud.backupdr_v1.types.BackupGcpResource):
            Output only. Unique identifier of the GCP
            resource that is being backed up.

            This field is a member of `oneof`_ ``source_resource``.
        kms_key_versions (MutableSequence[str]):
            Optional. Output only. The list of KMS key
            versions used to encrypt the backup.
    """

    class State(proto.Enum):
        r"""Holds the state of the backup resource.

        Values:
            STATE_UNSPECIFIED (0):
                State not set.
            CREATING (1):
                The backup is being created.
            ACTIVE (2):
                The backup has been created and is fully
                usable.
            DELETING (3):
                The backup is being deleted.
            ERROR (4):
                The backup is experiencing an issue and might
                be unusable.
            UPLOADING (5):
                The backup is being uploaded.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        ACTIVE = 2
        DELETING = 3
        ERROR = 4
        UPLOADING = 5

    class BackupType(proto.Enum):
        r"""Type of the backup, scheduled or ondemand.

        Values:
            BACKUP_TYPE_UNSPECIFIED (0):
                Backup type is unspecified.
            SCHEDULED (1):
                Scheduled backup.
            ON_DEMAND (2):
                On demand backup.
            ON_DEMAND_OPERATIONAL (3):
                Operational backup.
        """

        BACKUP_TYPE_UNSPECIFIED = 0
        SCHEDULED = 1
        ON_DEMAND = 2
        ON_DEMAND_OPERATIONAL = 3

    class GCPBackupPlanInfo(proto.Message):
        r"""GCPBackupPlanInfo captures the plan configuration details of
        Google Cloud resources at the time of backup.

        Attributes:
            backup_plan (str):
                Resource name of backup plan by which
                workload is protected at the time of the backup.
                Format:

                projects/{project}/locations/{location}/backupPlans/{backupPlanId}
            backup_plan_rule_id (str):
                The rule id of the backup plan which
                triggered this backup in case of scheduled
                backup or used for
            backup_plan_revision_name (str):
                Resource name of the backup plan revision
                which triggered this backup in case of scheduled
                backup or used for on demand backup. Format:

                projects/{project}/locations/{location}/backupPlans/{backupPlanId}/revisions/{revisionId}
            backup_plan_revision_id (str):
                The user friendly id of the backup plan
                revision which triggered this backup in case of
                scheduled backup or used for on demand backup.
        """

        backup_plan: str = proto.Field(
            proto.STRING,
            number=1,
        )
        backup_plan_rule_id: str = proto.Field(
            proto.STRING,
            number=2,
        )
        backup_plan_revision_name: str = proto.Field(
            proto.STRING,
            number=3,
        )
        backup_plan_revision_id: str = proto.Field(
            proto.STRING,
            number=4,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        optional=True,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        optional=True,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )
    enforced_retention_end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        optional=True,
        message=timestamp_pb2.Timestamp,
    )
    backup_retention_inheritance: "BackupVault.BackupRetentionInheritance" = (
        proto.Field(
            proto.ENUM,
            number=30,
            optional=True,
            enum="BackupVault.BackupRetentionInheritance",
        )
    )
    expire_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        optional=True,
        message=timestamp_pb2.Timestamp,
    )
    consistency_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        optional=True,
        message=timestamp_pb2.Timestamp,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=11,
        optional=True,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=15,
        enum=State,
    )
    service_locks: MutableSequence["BackupLock"] = proto.RepeatedField(
        proto.MESSAGE,
        number=17,
        message="BackupLock",
    )
    backup_appliance_locks: MutableSequence["BackupLock"] = proto.RepeatedField(
        proto.MESSAGE,
        number=18,
        message="BackupLock",
    )
    compute_instance_backup_properties: backupvault_gce.ComputeInstanceBackupProperties = proto.Field(
        proto.MESSAGE,
        number=19,
        oneof="backup_properties",
        message=backupvault_gce.ComputeInstanceBackupProperties,
    )
    cloud_sql_instance_backup_properties: backupvault_cloudsql.CloudSqlInstanceBackupProperties = proto.Field(
        proto.MESSAGE,
        number=26,
        oneof="backup_properties",
        message=backupvault_cloudsql.CloudSqlInstanceBackupProperties,
    )
    backup_appliance_backup_properties: backupvault_ba.BackupApplianceBackupProperties = proto.Field(
        proto.MESSAGE,
        number=21,
        oneof="backup_properties",
        message=backupvault_ba.BackupApplianceBackupProperties,
    )
    alloy_db_backup_properties: backupvault_alloydb.AlloyDbClusterBackupProperties = (
        proto.Field(
            proto.MESSAGE,
            number=27,
            oneof="backup_properties",
            message=backupvault_alloydb.AlloyDbClusterBackupProperties,
        )
    )
    disk_backup_properties: backupvault_disk.DiskBackupProperties = proto.Field(
        proto.MESSAGE,
        number=28,
        oneof="backup_properties",
        message=backupvault_disk.DiskBackupProperties,
    )
    backup_type: BackupType = proto.Field(
        proto.ENUM,
        number=20,
        enum=BackupType,
    )
    gcp_backup_plan_info: GCPBackupPlanInfo = proto.Field(
        proto.MESSAGE,
        number=22,
        oneof="plan_info",
        message=GCPBackupPlanInfo,
    )
    resource_size_bytes: int = proto.Field(
        proto.INT64,
        number=23,
    )
    satisfies_pzs: bool = proto.Field(
        proto.BOOL,
        number=24,
        optional=True,
    )
    satisfies_pzi: bool = proto.Field(
        proto.BOOL,
        number=25,
        optional=True,
    )
    gcp_resource: "BackupGcpResource" = proto.Field(
        proto.MESSAGE,
        number=31,
        oneof="source_resource",
        message="BackupGcpResource",
    )
    kms_key_versions: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=33,
    )


class CreateBackupVaultRequest(proto.Message):
    r"""Message for creating a BackupVault.

    Attributes:
        parent (str):
            Required. Value for parent.
        backup_vault_id (str):
            Required. ID of the requesting object If auto-generating ID
            server-side, remove this field and backup_vault_id from the
            method_signature of Create RPC
        backup_vault (google.cloud.backupdr_v1.types.BackupVault):
            Required. The resource being created
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        validate_only (bool):
            Optional. Only validate the request, but do
            not perform mutations. The default is 'false'.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    backup_vault_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    backup_vault: "BackupVault" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="BackupVault",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class ListBackupVaultsRequest(proto.Message):
    r"""Request message for listing backupvault stores.

    Attributes:
        parent (str):
            Required. The project and location for which to retrieve
            backupvault stores information, in the format
            'projects/{project_id}/locations/{location}'. In Cloud
            Backup and DR, locations map to Google Cloud regions, for
            example **us-central1**. To retrieve backupvault stores for
            all locations, use "-" for the '{location}' value.
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
        filter (str):
            Optional. Filtering results.
        order_by (str):
            Optional. Hint for how to order the results.
        view (google.cloud.backupdr_v1.types.BackupVaultView):
            Optional. Reserved for future use to provide
            a BASIC & FULL view of Backup Vault.
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
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )
    view: "BackupVaultView" = proto.Field(
        proto.ENUM,
        number=6,
        enum="BackupVaultView",
    )


class ListBackupVaultsResponse(proto.Message):
    r"""Response message for listing BackupVaults.

    Attributes:
        backup_vaults (MutableSequence[google.cloud.backupdr_v1.types.BackupVault]):
            The list of BackupVault instances in the
            project for the specified location.

            If the '{location}' value in the request is "-",
            the response contains a list of instances from
            all locations. In case any location is
            unreachable, the response will only return
            backup vaults in reachable locations and the
            'unreachable' field will be populated with a
            list of unreachable locations.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    backup_vaults: MutableSequence["BackupVault"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="BackupVault",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class FetchUsableBackupVaultsRequest(proto.Message):
    r"""Request message for fetching usable BackupVaults.

    Attributes:
        parent (str):
            Required. The project and location for which to retrieve
            backupvault stores information, in the format
            'projects/{project_id}/locations/{location}'. In Cloud
            Backup and DR, locations map to Google Cloud regions, for
            example **us-central1**. To retrieve backupvault stores for
            all locations, use "-" for the '{location}' value.
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
        filter (str):
            Optional. Filtering results.
        order_by (str):
            Optional. Hint for how to order the results.
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
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )


class FetchUsableBackupVaultsResponse(proto.Message):
    r"""Response message for fetching usable BackupVaults.

    Attributes:
        backup_vaults (MutableSequence[google.cloud.backupdr_v1.types.BackupVault]):
            The list of BackupVault instances in the
            project for the specified location.

            If the '{location}' value in the request is "-",
            the response contains a list of instances from
            all locations. In case any location is
            unreachable, the response will only return
            backup vaults in reachable locations and the
            'unreachable' field will be populated with a
            list of unreachable locations.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    backup_vaults: MutableSequence["BackupVault"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="BackupVault",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class FetchBackupsForResourceTypeRequest(proto.Message):
    r"""Request for the FetchBackupsForResourceType method.

    Attributes:
        parent (str):
            Required. Datasources are the parent resource
            for the backups. Format:

            projects/{project}/locations/{location}/backupVaults/{backupVaultId}/dataSources/{datasourceId}
        resource_type (str):
            Required. The type of the GCP resource.
            Ex: sqladmin.googleapis.com/Instance
        page_size (int):
            Optional. The maximum number of Backups to
            return. The service may return fewer than this
            value. If unspecified, at most 50 Backups will
            be returned. The maximum value is 100; values
            above 100 will be coerced to 100.
        page_token (str):
            Optional. A page token, received from a previous call of
            ``FetchBackupsForResourceType``. Provide this to retrieve
            the subsequent page.

            When paginating, all other parameters provided to
            ``FetchBackupsForResourceType`` must match the call that
            provided the page token.
        filter (str):
            Optional. A filter expression that filters
            the results fetched in the response. The
            expression must specify the field name, a
            comparison operator, and the value that you want
            to use for filtering. Supported fields:
        order_by (str):
            Optional. A comma-separated list of fields to
            order by, sorted in ascending order. Use "desc"
            after a field name for descending.
        view (google.cloud.backupdr_v1.types.BackupView):
            Optional. This parameter is used to specify
            the view of the backup. If not specified, the
            default view is BASIC.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    resource_type: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=5,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=6,
    )
    view: "BackupView" = proto.Field(
        proto.ENUM,
        number=7,
        enum="BackupView",
    )


class FetchBackupsForResourceTypeResponse(proto.Message):
    r"""Response for the FetchBackupsForResourceType method.

    Attributes:
        backups (MutableSequence[google.cloud.backupdr_v1.types.Backup]):
            The Backups from the specified parent.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
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


class GetBackupVaultRequest(proto.Message):
    r"""Request message for getting a BackupVault.

    Attributes:
        name (str):
            Required. Name of the backupvault store resource name, in
            the format
            'projects/{project_id}/locations/{location}/backupVaults/{resource_name}'
        view (google.cloud.backupdr_v1.types.BackupVaultView):
            Optional. Reserved for future use to provide
            a BASIC & FULL view of Backup Vault
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    view: "BackupVaultView" = proto.Field(
        proto.ENUM,
        number=2,
        enum="BackupVaultView",
    )


class UpdateBackupVaultRequest(proto.Message):
    r"""Request message for updating a BackupVault.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask is used to specify the fields to be
            overwritten in the BackupVault resource by the update. The
            fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask. If the user does not provide a mask
            then the request will fail.
        backup_vault (google.cloud.backupdr_v1.types.BackupVault):
            Required. The resource being updated
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        validate_only (bool):
            Optional. Only validate the request, but do
            not perform mutations. The default is 'false'.
        force (bool):
            Optional. If set to true, will not check plan
            duration against backup vault enforcement
            duration.
        force_update_access_restriction (bool):
            Optional. If set to true, we will force
            update access restriction even if some non
            compliant data sources are present. The default
            is 'false'.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    backup_vault: "BackupVault" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="BackupVault",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    force_update_access_restriction: bool = proto.Field(
        proto.BOOL,
        number=6,
    )


class DeleteBackupVaultRequest(proto.Message):
    r"""Message for deleting a BackupVault.

    Attributes:
        name (str):
            Required. Name of the resource.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes after the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        force (bool):
            Optional. If set to true, any data source
            from this backup vault will also be deleted.
        etag (str):
            The current etag of the backup vault.
            If an etag is provided and does not match the
            current etag of the connection, deletion will be
            blocked.
        validate_only (bool):
            Optional. Only validate the request, but do
            not perform mutations. The default is 'false'.
        allow_missing (bool):
            Optional. If true and the BackupVault is not
            found, the request will succeed but no action
            will be taken.
        ignore_backup_plan_references (bool):
            Optional. If set to true, backupvault
            deletion will proceed even if there are backup
            plans referencing the backupvault. The default
            is 'false'.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=4,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    allow_missing: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    ignore_backup_plan_references: bool = proto.Field(
        proto.BOOL,
        number=7,
    )


class ListDataSourcesRequest(proto.Message):
    r"""Request message for listing DataSources.

    Attributes:
        parent (str):
            Required. The project and location for which to retrieve
            data sources information, in the format
            'projects/{project_id}/locations/{location}'. In Cloud
            Backup and DR, locations map to Google Cloud regions, for
            example **us-central1**. To retrieve data sources for all
            locations, use "-" for the '{location}' value.
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
        filter (str):
            Optional. Filtering results.
        order_by (str):
            Optional. Hint for how to order the results.
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
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListDataSourcesResponse(proto.Message):
    r"""Response message for listing DataSources.

    Attributes:
        data_sources (MutableSequence[google.cloud.backupdr_v1.types.DataSource]):
            The list of DataSource instances in the
            project for the specified location.

            If the '{location}' value in the request is "-",
            the response contains a list of instances from
            all locations. In case any location is
            unreachable, the response will only return data
            sources in reachable locations and the
            'unreachable' field will be populated with a
            list of unreachable locations.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    data_sources: MutableSequence["DataSource"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="DataSource",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetDataSourceRequest(proto.Message):
    r"""Request message for getting a DataSource instance.

    Attributes:
        name (str):
            Required. Name of the data source resource name, in the
            format
            'projects/{project_id}/locations/{location}/backupVaults/{resource_name}/dataSource/{resource_name}'
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateDataSourceRequest(proto.Message):
    r"""Request message for updating a data source instance.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask is used to specify the fields to be
            overwritten in the DataSource resource by the update. The
            fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask. If the user does not provide a mask
            then the request will fail.
        data_source (google.cloud.backupdr_v1.types.DataSource):
            Required. The resource being updated
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        allow_missing (bool):
            Optional. Enable upsert.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    data_source: "DataSource" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="DataSource",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    allow_missing: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class ListBackupsRequest(proto.Message):
    r"""Request message for listing Backups.

    Attributes:
        parent (str):
            Required. The project and location for which to retrieve
            backup information, in the format
            'projects/{project_id}/locations/{location}'. In Cloud
            Backup and DR, locations map to Google Cloud regions, for
            example **us-central1**. To retrieve data sources for all
            locations, use "-" for the '{location}' value.
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
        filter (str):
            Optional. Filtering results.
        order_by (str):
            Optional. Hint for how to order the results.
        view (google.cloud.backupdr_v1.types.BackupView):
            Optional. Reserved for future use to provide
            a BASIC & FULL view of Backup resource.
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
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )
    view: "BackupView" = proto.Field(
        proto.ENUM,
        number=6,
        enum="BackupView",
    )


class ListBackupsResponse(proto.Message):
    r"""Response message for listing Backups.

    Attributes:
        backups (MutableSequence[google.cloud.backupdr_v1.types.Backup]):
            The list of Backup instances in the project
            for the specified location.

            If the '{location}' value in the request is "-",
            the response contains a list of instances from
            all locations. In case any location is
            unreachable, the response will only return data
            sources in reachable locations and the
            'unreachable' field will be populated with a
            list of unreachable locations.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
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
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetBackupRequest(proto.Message):
    r"""Request message for getting a Backup.

    Attributes:
        name (str):
            Required. Name of the data source resource name, in the
            format
            'projects/{project_id}/locations/{location}/backupVaults/{backupVault}/dataSources/{datasource}/backups/{backup}'
        view (google.cloud.backupdr_v1.types.BackupView):
            Optional. Reserved for future use to provide
            a BASIC & FULL view of Backup resource.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    view: "BackupView" = proto.Field(
        proto.ENUM,
        number=2,
        enum="BackupView",
    )


class UpdateBackupRequest(proto.Message):
    r"""Request message for updating a Backup.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask is used to specify the fields to be
            overwritten in the Backup resource by the update. The fields
            specified in the update_mask are relative to the resource,
            not the full request. A field will be overwritten if it is
            in the mask. If the user does not provide a mask then the
            request will fail.
        backup (google.cloud.backupdr_v1.types.Backup):
            Required. The resource being updated
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    backup: "Backup" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Backup",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteBackupRequest(proto.Message):
    r"""Message for deleting a Backup.

    Attributes:
        name (str):
            Required. Name of the resource.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes after the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class RestoreBackupRequest(proto.Message):
    r"""Request message for restoring from a Backup.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Required. The resource name of the Backup instance, in the
            format
            'projects/*/locations/*/backupVaults/*/dataSources/*/backups/'.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes after the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        compute_instance_target_environment (google.cloud.backupdr_v1.types.ComputeInstanceTargetEnvironment):
            Compute Engine target environment to be used
            during restore.

            This field is a member of `oneof`_ ``target_environment``.
        disk_target_environment (google.cloud.backupdr_v1.types.DiskTargetEnvironment):
            Disk target environment to be used during
            restore.

            This field is a member of `oneof`_ ``target_environment``.
        region_disk_target_environment (google.cloud.backupdr_v1.types.RegionDiskTargetEnvironment):
            Region disk target environment to be used
            during restore.

            This field is a member of `oneof`_ ``target_environment``.
        compute_instance_restore_properties (google.cloud.backupdr_v1.types.ComputeInstanceRestoreProperties):
            Compute Engine instance properties to be
            overridden during restore.

            This field is a member of `oneof`_ ``instance_properties``.
        disk_restore_properties (google.cloud.backupdr_v1.types.DiskRestoreProperties):
            Disk properties to be overridden during
            restore.

            This field is a member of `oneof`_ ``instance_properties``.
        clear_overrides_field_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. A field mask used to clear server-side default
            values for fields within the ``instance_properties`` oneof.

            When a field in this mask is cleared, the server will not
            apply its default logic (like inheriting a value from the
            source) for that field.

            The most common current use case is clearing default
            encryption keys.

            Examples of field mask paths:

            - Compute Instance Disks:
              ``compute_instance_restore_properties.disks.*.disk_encryption_key``
            - Single Disk:
              ``disk_restore_properties.disk_encryption_key``

            This field is a member of `oneof`_ ``_clear_overrides_field_mask``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    compute_instance_target_environment: backupvault_gce.ComputeInstanceTargetEnvironment = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="target_environment",
        message=backupvault_gce.ComputeInstanceTargetEnvironment,
    )
    disk_target_environment: backupvault_disk.DiskTargetEnvironment = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="target_environment",
        message=backupvault_disk.DiskTargetEnvironment,
    )
    region_disk_target_environment: backupvault_disk.RegionDiskTargetEnvironment = (
        proto.Field(
            proto.MESSAGE,
            number=6,
            oneof="target_environment",
            message=backupvault_disk.RegionDiskTargetEnvironment,
        )
    )
    compute_instance_restore_properties: backupvault_gce.ComputeInstanceRestoreProperties = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="instance_properties",
        message=backupvault_gce.ComputeInstanceRestoreProperties,
    )
    disk_restore_properties: backupvault_disk.DiskRestoreProperties = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="instance_properties",
        message=backupvault_disk.DiskRestoreProperties,
    )
    clear_overrides_field_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=8,
        optional=True,
        message=field_mask_pb2.FieldMask,
    )


class RestoreBackupResponse(proto.Message):
    r"""Response message for restoring from a Backup.

    Attributes:
        target_resource (google.cloud.backupdr_v1.types.TargetResource):
            Details of the target resource
            created/modified as part of restore.
    """

    target_resource: "TargetResource" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="TargetResource",
    )


class TargetResource(proto.Message):
    r"""Details of the target resource created/modified as part of
    restore.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        gcp_resource (google.cloud.backupdr_v1.types.GcpResource):
            Details of the native Google Cloud resource
            created as part of restore.

            This field is a member of `oneof`_ ``target_resource_info``.
    """

    gcp_resource: "GcpResource" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="target_resource_info",
        message="GcpResource",
    )


class GcpResource(proto.Message):
    r"""Minimum details to identify a Google Cloud resource

    Attributes:
        gcp_resourcename (str):
            Name of the Google Cloud resource.
        location (str):
            Location of the resource:
            <region>/<zone>/"global"/"unspecified".
        type_ (str):
            Type of the resource. Use the Unified
            Resource Type, eg.
            compute.googleapis.com/Instance.
    """

    gcp_resourcename: str = proto.Field(
        proto.STRING,
        number=1,
    )
    location: str = proto.Field(
        proto.STRING,
        number=2,
    )
    type_: str = proto.Field(
        proto.STRING,
        number=3,
    )


class BackupGcpResource(proto.Message):
    r"""Minimum details to identify a Google Cloud resource for a
    backup.

    Attributes:
        gcp_resourcename (str):
            Name of the Google Cloud resource.
        location (str):
            Location of the resource:
            <region>/<zone>/"global"/"unspecified".
        type_ (str):
            Type of the resource. Use the Unified
            Resource Type, eg.
            compute.googleapis.com/Instance.
    """

    gcp_resourcename: str = proto.Field(
        proto.STRING,
        number=1,
    )
    location: str = proto.Field(
        proto.STRING,
        number=2,
    )
    type_: str = proto.Field(
        proto.STRING,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
