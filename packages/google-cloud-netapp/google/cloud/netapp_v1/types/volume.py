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
import proto  # type: ignore

from google.cloud.netapp_v1.types import common

__protobuf__ = proto.module(
    package="google.cloud.netapp.v1",
    manifest={
        "Protocols",
        "AccessType",
        "SMBSettings",
        "SplitState",
        "SecurityStyle",
        "RestrictedAction",
        "ListVolumesRequest",
        "ListVolumesResponse",
        "ListBackupConfigsRequest",
        "ListBackupConfigsResponse",
        "VolumeBackupConfig",
        "GetVolumeRequest",
        "CreateVolumeRequest",
        "UpdateVolumeRequest",
        "DeleteVolumeRequest",
        "RevertVolumeRequest",
        "StartSplitRequest",
        "GetSplitStatusRequest",
        "SplitStatus",
        "Volume",
        "LargeCapacityConfig",
        "ExportPolicy",
        "SimpleExportPolicyRule",
        "SnapshotPolicy",
        "HourlySchedule",
        "DailySchedule",
        "WeeklySchedule",
        "MonthlySchedule",
        "MountOption",
        "RestoreParameters",
        "BackupConfig",
        "TieringPolicy",
        "HybridReplicationParameters",
        "CacheParameters",
        "CacheConfig",
        "CachePrePopulate",
        "BlockDevice",
        "RestoreBackupFilesRequest",
        "RestoreBackupFilesResponse",
        "RestoreVolumeRequest",
        "BackupSource",
        "OntapVolumeTarget",
        "RestoreVolumeResponse",
        "EstablishVolumePeeringRequest",
        "UpdateBackupConfigRequest",
        "UpdateBackupConfigResponse",
    },
)


class Protocols(proto.Enum):
    r"""Protocols is an enum of all the supported network protocols
    for a volume.

    Values:
        PROTOCOLS_UNSPECIFIED (0):
            Unspecified protocol
        NFSV3 (1):
            NFS V3 protocol
        NFSV4 (2):
            NFS V4 protocol
        SMB (3):
            SMB protocol
        ISCSI (4):
            ISCSI protocol
        NVME (5):
            NVMe protocol
    """

    PROTOCOLS_UNSPECIFIED = 0
    NFSV3 = 1
    NFSV4 = 2
    SMB = 3
    ISCSI = 4
    NVME = 5


class AccessType(proto.Enum):
    r"""AccessType is an enum of all the supported access types for a
    volume.

    Values:
        ACCESS_TYPE_UNSPECIFIED (0):
            Unspecified Access Type
        READ_ONLY (1):
            Read Only
        READ_WRITE (2):
            Read Write
        READ_NONE (3):
            None
    """

    ACCESS_TYPE_UNSPECIFIED = 0
    READ_ONLY = 1
    READ_WRITE = 2
    READ_NONE = 3


class SMBSettings(proto.Enum):
    r"""SMBSettings
    Modifies the behaviour of a SMB volume.

    Values:
        SMB_SETTINGS_UNSPECIFIED (0):
            Unspecified default option
        ENCRYPT_DATA (1):
            SMB setting encrypt data
        BROWSABLE (2):
            SMB setting browsable
        CHANGE_NOTIFY (3):
            SMB setting notify change
        NON_BROWSABLE (4):
            SMB setting not to notify change
        OPLOCKS (5):
            SMB setting oplocks
        SHOW_SNAPSHOT (6):
            SMB setting to show snapshots
        SHOW_PREVIOUS_VERSIONS (7):
            SMB setting to show previous versions
        ACCESS_BASED_ENUMERATION (8):
            SMB setting to access volume based on
            enumerartion
        CONTINUOUSLY_AVAILABLE (9):
            Continuously available enumeration
    """

    SMB_SETTINGS_UNSPECIFIED = 0
    ENCRYPT_DATA = 1
    BROWSABLE = 2
    CHANGE_NOTIFY = 3
    NON_BROWSABLE = 4
    OPLOCKS = 5
    SHOW_SNAPSHOT = 6
    SHOW_PREVIOUS_VERSIONS = 7
    ACCESS_BASED_ENUMERATION = 8
    CONTINUOUSLY_AVAILABLE = 9


class SplitState(proto.Enum):
    r"""Enum to indicate the state of the clone in relation to the
    split process.

    Values:
        SPLIT_STATE_UNSPECIFIED (0):
            State is not specified.
        SPLIT_STATE_NOT_SPLITTING (1):
            The volume is a thin clone, sharing blocks
            with its source.
        SPLIT_STATE_IN_PROGRESS (2):
            A split operation is currently active and in
            progress.
        SPLIT_STATE_FAILED (3):
            The attempt to split the volume failed.
    """

    SPLIT_STATE_UNSPECIFIED = 0
    SPLIT_STATE_NOT_SPLITTING = 1
    SPLIT_STATE_IN_PROGRESS = 2
    SPLIT_STATE_FAILED = 3


class SecurityStyle(proto.Enum):
    r"""The security style of the volume, can be either UNIX or NTFS.

    Values:
        SECURITY_STYLE_UNSPECIFIED (0):
            SecurityStyle is unspecified
        NTFS (1):
            SecurityStyle uses NTFS
        UNIX (2):
            SecurityStyle uses UNIX
    """

    SECURITY_STYLE_UNSPECIFIED = 0
    NTFS = 1
    UNIX = 2


class RestrictedAction(proto.Enum):
    r"""Actions to be restricted for a volume.

    Values:
        RESTRICTED_ACTION_UNSPECIFIED (0):
            Unspecified restricted action
        DELETE (1):
            Prevent volume from being deleted when
            mounted.
    """

    RESTRICTED_ACTION_UNSPECIFIED = 0
    DELETE = 1


class ListVolumesRequest(proto.Message):
    r"""Message for requesting list of Volumes

    Attributes:
        parent (str):
            Required. Parent value for ListVolumesRequest
        page_size (int):
            Requested page size. Server may return fewer
            items than requested. If unspecified, the server
            will pick an appropriate default.
        page_token (str):
            A token identifying a page of results the
            server should return.
        filter (str):
            Filtering results
        order_by (str):
            Hint for how to order the results
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


class ListVolumesResponse(proto.Message):
    r"""Message for response to listing Volumes

    Attributes:
        volumes (MutableSequence[google.cloud.netapp_v1.types.Volume]):
            The list of Volume
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    volumes: MutableSequence["Volume"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Volume",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class ListBackupConfigsRequest(proto.Message):
    r"""Message for requesting list of BackupConfigs in a
    StoragePool.

    Attributes:
        parent (str):
            Required. The ONTAP StoragePool for which to retrieve backup
            configuration information, in the format
            ``projects/{project}/locations/{location}/storagePools/{storage_pool}``.
        page_size (int):
            Optional. The maximum number of items to
            return. The service may return fewer than this
            value. The maximum value is 1000; values above
            1000 will be coerced to 1000. If unspecified or
            set to 0, a default of 50 will be used.
        page_token (str):
            Optional. The next_page_token value to use if there are
            additional results to retrieve for this list request.
        order_by (str):
            Optional. Sort results. Supported values are "volume_id" or
            "".
        filter (str):
            Optional. The standard list filter.
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
    order_by: str = proto.Field(
        proto.STRING,
        number=4,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListBackupConfigsResponse(proto.Message):
    r"""Message for response to listing BackupConfigs in an ONTAP
    StoragePool.

    Attributes:
        volume_backup_configs (MutableSequence[google.cloud.netapp_v1.types.VolumeBackupConfig]):
            A list of backup configurations for volumes
            in the pool.
        next_page_token (str):
            The token you can use to retrieve the next
            page of results. Not returned if there are no
            more results in the list.
        unreachable (MutableSequence[str]):
            Unordered list. Locations that could not be
            reached.
    """

    @property
    def raw_page(self):
        return self

    volume_backup_configs: MutableSequence["VolumeBackupConfig"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="VolumeBackupConfig",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class VolumeBackupConfig(proto.Message):
    r"""Backup configuration for a volume in a pool.

    Attributes:
        volume_uuid (str):
            Provides the Ontap UUID of the volume within
            the pool.
        backup_config (google.cloud.netapp_v1.types.BackupConfig):
            Backup configuration for the volume.
    """

    volume_uuid: str = proto.Field(
        proto.STRING,
        number=1,
    )
    backup_config: "BackupConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="BackupConfig",
    )


class GetVolumeRequest(proto.Message):
    r"""Message for getting a Volume

    Attributes:
        name (str):
            Required. Name of the volume
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateVolumeRequest(proto.Message):
    r"""Message for creating a Volume

    Attributes:
        parent (str):
            Required. Value for parent.
        volume_id (str):
            Required. Id of the requesting volume. Must
            be unique within the parent resource. Must
            contain only letters, numbers and hyphen, with
            the first character a letter, the last a letter
            or a number, and a 63 character maximum.
        volume (google.cloud.netapp_v1.types.Volume):
            Required. The volume being created.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    volume_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    volume: "Volume" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Volume",
    )


class UpdateVolumeRequest(proto.Message):
    r"""Message for updating a Volume

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask is used to specify the fields to be
            overwritten in the Volume resource by the update. The fields
            specified in the update_mask are relative to the resource,
            not the full request. A field will be overwritten if it is
            in the mask. If the user does not provide a mask then all
            fields will be overwritten.
        volume (google.cloud.netapp_v1.types.Volume):
            Required. The volume being updated
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    volume: "Volume" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Volume",
    )


class DeleteVolumeRequest(proto.Message):
    r"""Message for deleting a Volume

    Attributes:
        name (str):
            Required. Name of the volume
        force (bool):
            If this field is set as true, CCFE will not
            block the volume resource deletion even if it
            has any snapshots resource. (Otherwise, the
            request will only work if the volume has no
            snapshots.)
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class RevertVolumeRequest(proto.Message):
    r"""RevertVolumeRequest reverts the given volume to the specified
    snapshot.

    Attributes:
        name (str):
            Required. The resource name of the volume, in the format of
            projects/{project_id}/locations/{location}/volumes/{volume_id}.
        snapshot_id (str):
            Required. The snapshot resource ID, in the format
            'my-snapshot', where the specified ID is the {snapshot_id}
            of the fully qualified name like
            projects/{project_id}/locations/{location_id}/volumes/{volume_id}/snapshots/{snapshot_id}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    snapshot_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class StartSplitRequest(proto.Message):
    r"""Request message for splitting a volume.

    Attributes:
        name (str):
            Required. The full name of the clone volume to be split from
            its source. Format:
            projects/{project_number}/locations/{location}/volumes/{volume_id}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetSplitStatusRequest(proto.Message):
    r"""Request message for GetSplitStatus.

    Attributes:
        name (str):
            Required. The full name of the volume. Format:
            projects/{project_number}/locations/{location}/volumes/{volume_id}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class SplitStatus(proto.Message):
    r"""Message for SplitStatus.

    Attributes:
        split_state (google.cloud.netapp_v1.types.SplitState):
            Output only. The current state of the clone
            split operation.
        state_details (str):
            Output only. Human-readable details about the
            current state. Mostly used for displaying error
            messages during split failure Examples: "Split
            in progress", "Error: insufficient capacity".
        progress_percent (int):
            Output only. The estimated progress percentage of the split
            operation (0-100). This is meaningful primarily when
            split_state is IN_PROGRESS.
    """

    split_state: "SplitState" = proto.Field(
        proto.ENUM,
        number=1,
        enum="SplitState",
    )
    state_details: str = proto.Field(
        proto.STRING,
        number=2,
    )
    progress_percent: int = proto.Field(
        proto.INT32,
        number=3,
    )


class Volume(proto.Message):
    r"""Volume provides a filesystem that you can mount.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. Name of the volume
        state (google.cloud.netapp_v1.types.Volume.State):
            Output only. State of the volume
        state_details (str):
            Output only. State details of the volume
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Create time of the volume
        share_name (str):
            Required. Share name of the volume
        psa_range (str):
            Output only. This field is not implemented.
            The values provided in this field are ignored.
        storage_pool (str):
            Required. StoragePool name of the volume
        network (str):
            Output only. VPC Network name.
            Format:
            projects/{project}/global/networks/{network}
        service_level (google.cloud.netapp_v1.types.ServiceLevel):
            Output only. Service level of the volume
        capacity_gib (int):
            Required. Capacity in GIB of the volume
        export_policy (google.cloud.netapp_v1.types.ExportPolicy):
            Optional. Export policy of the volume
        protocols (MutableSequence[google.cloud.netapp_v1.types.Protocols]):
            Required. Protocols required for the volume
        smb_settings (MutableSequence[google.cloud.netapp_v1.types.SMBSettings]):
            Optional. SMB share settings for the volume.
        mount_options (MutableSequence[google.cloud.netapp_v1.types.MountOption]):
            Output only. Mount options of this volume
        unix_permissions (str):
            Optional. Default unix style permission (e.g.
            777) the mount point will be created with.
            Applicable for NFS protocol types only.
        labels (MutableMapping[str, str]):
            Optional. Labels as key value pairs
        description (str):
            Optional. Description of the volume
        snapshot_policy (google.cloud.netapp_v1.types.SnapshotPolicy):
            Optional. SnapshotPolicy for a volume.
        snap_reserve (float):
            Optional. Snap_reserve specifies percentage of volume
            storage reserved for snapshot storage. Default is 0 percent.
        snapshot_directory (bool):
            Optional. Snapshot_directory if enabled (true) the volume
            will contain a read-only .snapshot directory which provides
            access to each of the volume's snapshots.
        used_gib (int):
            Output only. Used capacity in GIB of the
            volume. This is computed periodically and it
            does not represent the realtime usage.
        security_style (google.cloud.netapp_v1.types.SecurityStyle):
            Optional. Security Style of the Volume
        kerberos_enabled (bool):
            Optional. Flag indicating if the volume is a
            kerberos volume or not, export policy rules
            control kerberos security modes (krb5, krb5i,
            krb5p).
        ldap_enabled (bool):
            Output only. Flag indicating if the volume is
            NFS LDAP enabled or not.
        active_directory (str):
            Output only. Specifies the ActiveDirectory
            name of a SMB volume.
        restore_parameters (google.cloud.netapp_v1.types.RestoreParameters):
            Optional. Specifies the source of the volume
            to be created from.
        kms_config (str):
            Output only. Specifies the KMS config to be
            used for volume encryption.
        encryption_type (google.cloud.netapp_v1.types.EncryptionType):
            Output only. Specified the current volume
            encryption key source.
        has_replication (bool):
            Output only. Indicates whether the volume is
            part of a replication relationship.
        backup_config (google.cloud.netapp_v1.types.BackupConfig):
            BackupConfig of the volume.

            This field is a member of `oneof`_ ``_backup_config``.
        restricted_actions (MutableSequence[google.cloud.netapp_v1.types.RestrictedAction]):
            Optional. List of actions that are restricted
            on this volume.
        large_capacity (bool):
            Optional. Flag indicating if the volume will be a large
            capacity volume or a regular volume. This field is used for
            legacy FILE pools. For Unified pools, use the
            ``large_capacity_config`` field instead. This field and
            ``large_capacity_config`` are mutually exclusive.
        multiple_endpoints (bool):
            Optional. Flag indicating if the volume will have an IP
            address per node for volumes supporting multiple IP
            endpoints. Only the volume with large_capacity will be
            allowed to have multiple endpoints.
        tiering_policy (google.cloud.netapp_v1.types.TieringPolicy):
            Tiering policy for the volume.

            This field is a member of `oneof`_ ``_tiering_policy``.
        replica_zone (str):
            Output only. Specifies the replica zone for
            regional volume.
        zone (str):
            Output only. Specifies the active zone for
            regional volume.
        cold_tier_size_gib (int):
            Output only. Size of the volume cold tier
            data rounded down to the nearest GiB.
        hybrid_replication_parameters (google.cloud.netapp_v1.types.HybridReplicationParameters):
            Optional. The Hybrid Replication parameters
            for the volume.
        throughput_mibps (float):
            Optional. Throughput of the volume (in MiB/s)
        cache_parameters (google.cloud.netapp_v1.types.CacheParameters):
            Optional. Cache parameters for the volume.
        hot_tier_size_used_gib (int):
            Output only. Total hot tier data rounded down
            to the nearest GiB used by the Volume. This
            field is only used for flex Service Level
        block_devices (MutableSequence[google.cloud.netapp_v1.types.BlockDevice]):
            Optional. Block devices for the volume.
            Currently, only one block device is permitted
            per Volume.
        large_capacity_config (google.cloud.netapp_v1.types.LargeCapacityConfig):
            Optional. Large capacity config for the volume. Enables and
            configures large capacity for volumes in Unified pools with
            File protocols. Not applicable for Block protocols in
            Unified pools. This field and the legacy ``large_capacity``
            boolean field are mutually exclusive.
        clone_details (google.cloud.netapp_v1.types.Volume.CloneDetails):
            Output only. If this volume is a clone, this
            field contains details about the clone.
    """

    class State(proto.Enum):
        r"""The volume states

        Values:
            STATE_UNSPECIFIED (0):
                Unspecified Volume State
            READY (1):
                Volume State is Ready
            CREATING (2):
                Volume State is Creating
            DELETING (3):
                Volume State is Deleting
            UPDATING (4):
                Volume State is Updating
            RESTORING (5):
                Volume State is Restoring
            DISABLED (6):
                Volume State is Disabled
            ERROR (7):
                Volume State is Error
            PREPARING (8):
                Volume State is Preparing. Note that this is
                different from CREATING where CREATING means the
                volume is being created, while PREPARING means
                the volume is created and now being prepared for
                the replication.
            READ_ONLY (9):
                Volume State is Read Only
        """

        STATE_UNSPECIFIED = 0
        READY = 1
        CREATING = 2
        DELETING = 3
        UPDATING = 4
        RESTORING = 5
        DISABLED = 6
        ERROR = 7
        PREPARING = 8
        READ_ONLY = 9

    class CloneDetails(proto.Message):
        r"""Details about a clone volume.

        Attributes:
            source_snapshot (str):
                Output only. Specifies the full resource name
                of the source snapshot from which this volume
                was cloned. Format:

                projects/{project}/locations/{location}/volumes/{volume}/snapshots/{snapshot}
            source_volume (str):
                Output only. Full name of the source volume
                resource. Format:

                projects/{project}/locations/{location}/volumes/{volume}
            shared_space_gib (int):
                Output only. Shared space in GiB. Determined
                at volume creation time based on size of source
                snapshot.
            split_state (google.cloud.netapp_v1.types.SplitState):
                Output only. The current state of the clone
                split operation.
        """

        source_snapshot: str = proto.Field(
            proto.STRING,
            number=1,
        )
        source_volume: str = proto.Field(
            proto.STRING,
            number=2,
        )
        shared_space_gib: int = proto.Field(
            proto.INT64,
            number=3,
        )
        split_state: "SplitState" = proto.Field(
            proto.ENUM,
            number=4,
            enum="SplitState",
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=2,
        enum=State,
    )
    state_details: str = proto.Field(
        proto.STRING,
        number=3,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    share_name: str = proto.Field(
        proto.STRING,
        number=5,
    )
    psa_range: str = proto.Field(
        proto.STRING,
        number=6,
    )
    storage_pool: str = proto.Field(
        proto.STRING,
        number=7,
    )
    network: str = proto.Field(
        proto.STRING,
        number=8,
    )
    service_level: common.ServiceLevel = proto.Field(
        proto.ENUM,
        number=9,
        enum=common.ServiceLevel,
    )
    capacity_gib: int = proto.Field(
        proto.INT64,
        number=10,
    )
    export_policy: "ExportPolicy" = proto.Field(
        proto.MESSAGE,
        number=11,
        message="ExportPolicy",
    )
    protocols: MutableSequence["Protocols"] = proto.RepeatedField(
        proto.ENUM,
        number=12,
        enum="Protocols",
    )
    smb_settings: MutableSequence["SMBSettings"] = proto.RepeatedField(
        proto.ENUM,
        number=13,
        enum="SMBSettings",
    )
    mount_options: MutableSequence["MountOption"] = proto.RepeatedField(
        proto.MESSAGE,
        number=14,
        message="MountOption",
    )
    unix_permissions: str = proto.Field(
        proto.STRING,
        number=15,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=16,
    )
    description: str = proto.Field(
        proto.STRING,
        number=17,
    )
    snapshot_policy: "SnapshotPolicy" = proto.Field(
        proto.MESSAGE,
        number=18,
        message="SnapshotPolicy",
    )
    snap_reserve: float = proto.Field(
        proto.DOUBLE,
        number=19,
    )
    snapshot_directory: bool = proto.Field(
        proto.BOOL,
        number=20,
    )
    used_gib: int = proto.Field(
        proto.INT64,
        number=21,
    )
    security_style: "SecurityStyle" = proto.Field(
        proto.ENUM,
        number=22,
        enum="SecurityStyle",
    )
    kerberos_enabled: bool = proto.Field(
        proto.BOOL,
        number=23,
    )
    ldap_enabled: bool = proto.Field(
        proto.BOOL,
        number=24,
    )
    active_directory: str = proto.Field(
        proto.STRING,
        number=25,
    )
    restore_parameters: "RestoreParameters" = proto.Field(
        proto.MESSAGE,
        number=26,
        message="RestoreParameters",
    )
    kms_config: str = proto.Field(
        proto.STRING,
        number=27,
    )
    encryption_type: common.EncryptionType = proto.Field(
        proto.ENUM,
        number=28,
        enum=common.EncryptionType,
    )
    has_replication: bool = proto.Field(
        proto.BOOL,
        number=29,
    )
    backup_config: "BackupConfig" = proto.Field(
        proto.MESSAGE,
        number=30,
        optional=True,
        message="BackupConfig",
    )
    restricted_actions: MutableSequence["RestrictedAction"] = proto.RepeatedField(
        proto.ENUM,
        number=31,
        enum="RestrictedAction",
    )
    large_capacity: bool = proto.Field(
        proto.BOOL,
        number=32,
    )
    multiple_endpoints: bool = proto.Field(
        proto.BOOL,
        number=33,
    )
    tiering_policy: "TieringPolicy" = proto.Field(
        proto.MESSAGE,
        number=34,
        optional=True,
        message="TieringPolicy",
    )
    replica_zone: str = proto.Field(
        proto.STRING,
        number=36,
    )
    zone: str = proto.Field(
        proto.STRING,
        number=37,
    )
    cold_tier_size_gib: int = proto.Field(
        proto.INT64,
        number=39,
    )
    hybrid_replication_parameters: "HybridReplicationParameters" = proto.Field(
        proto.MESSAGE,
        number=40,
        message="HybridReplicationParameters",
    )
    throughput_mibps: float = proto.Field(
        proto.DOUBLE,
        number=41,
    )
    cache_parameters: "CacheParameters" = proto.Field(
        proto.MESSAGE,
        number=42,
        message="CacheParameters",
    )
    hot_tier_size_used_gib: int = proto.Field(
        proto.INT64,
        number=44,
    )
    block_devices: MutableSequence["BlockDevice"] = proto.RepeatedField(
        proto.MESSAGE,
        number=45,
        message="BlockDevice",
    )
    large_capacity_config: "LargeCapacityConfig" = proto.Field(
        proto.MESSAGE,
        number=46,
        message="LargeCapacityConfig",
    )
    clone_details: CloneDetails = proto.Field(
        proto.MESSAGE,
        number=47,
        message=CloneDetails,
    )


class LargeCapacityConfig(proto.Message):
    r"""Configuration for a Large Capacity Volume. A Large Capacity
    Volume supports sizes ranging from 4.8 TiB to 20 PiB; it is
    composed of multiple internal constituents, and must be created
    in a large capacity pool.

    Attributes:
        constituent_count (int):
            Optional. The number of internal constituents
            (e.g., FlexVols) for this large volume. The
            minimum number of constituents is 2.
    """

    constituent_count: int = proto.Field(
        proto.INT32,
        number=1,
    )


class ExportPolicy(proto.Message):
    r"""Defines the export policy for the volume.

    Attributes:
        rules (MutableSequence[google.cloud.netapp_v1.types.SimpleExportPolicyRule]):
            Required. List of export policy rules
    """

    rules: MutableSequence["SimpleExportPolicyRule"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="SimpleExportPolicyRule",
    )


class SimpleExportPolicyRule(proto.Message):
    r"""An export policy rule describing various export options.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        allowed_clients (str):
            Comma separated list of allowed clients IP
            addresses

            This field is a member of `oneof`_ ``_allowed_clients``.
        has_root_access (str):
            Whether Unix root access will be granted.

            This field is a member of `oneof`_ ``_has_root_access``.
        access_type (google.cloud.netapp_v1.types.AccessType):
            Access type (ReadWrite, ReadOnly, None)

            This field is a member of `oneof`_ ``_access_type``.
        nfsv3 (bool):
            NFS V3 protocol.

            This field is a member of `oneof`_ ``_nfsv3``.
        nfsv4 (bool):
            NFS V4 protocol.

            This field is a member of `oneof`_ ``_nfsv4``.
        kerberos_5_read_only (bool):
            If enabled (true) the rule defines a read
            only access for clients matching the
            'allowedClients' specification. It enables nfs
            clients to mount using 'authentication' kerberos
            security mode.

            This field is a member of `oneof`_ ``_kerberos_5_read_only``.
        kerberos_5_read_write (bool):
            If enabled (true) the rule defines read and
            write access for clients matching the
            'allowedClients' specification. It enables nfs
            clients to mount using 'authentication' kerberos
            security mode. The 'kerberos5ReadOnly' value be
            ignored if this is enabled.

            This field is a member of `oneof`_ ``_kerberos_5_read_write``.
        kerberos_5i_read_only (bool):
            If enabled (true) the rule defines a read
            only access for clients matching the
            'allowedClients' specification. It enables nfs
            clients to mount using 'integrity' kerberos
            security mode.

            This field is a member of `oneof`_ ``_kerberos_5i_read_only``.
        kerberos_5i_read_write (bool):
            If enabled (true) the rule defines read and
            write access for clients matching the
            'allowedClients' specification. It enables nfs
            clients to mount using 'integrity' kerberos
            security mode. The 'kerberos5iReadOnly' value be
            ignored if this is enabled.

            This field is a member of `oneof`_ ``_kerberos_5i_read_write``.
        kerberos_5p_read_only (bool):
            If enabled (true) the rule defines a read
            only access for clients matching the
            'allowedClients' specification. It enables nfs
            clients to mount using 'privacy' kerberos
            security mode.

            This field is a member of `oneof`_ ``_kerberos_5p_read_only``.
        kerberos_5p_read_write (bool):
            If enabled (true) the rule defines read and
            write access for clients matching the
            'allowedClients' specification. It enables nfs
            clients to mount using 'privacy' kerberos
            security mode. The 'kerberos5pReadOnly' value be
            ignored if this is enabled.

            This field is a member of `oneof`_ ``_kerberos_5p_read_write``.
        squash_mode (google.cloud.netapp_v1.types.SimpleExportPolicyRule.SquashMode):
            Optional. Defines how user identity squashing is applied for
            this export rule. This field is the preferred way to
            configure squashing behavior and takes precedence over
            ``has_root_access`` if both are provided.

            This field is a member of `oneof`_ ``_squash_mode``.
        anon_uid (int):
            Optional. An integer representing the anonymous user ID.
            Range is 0 to ``4294967295``. Required when ``squash_mode``
            is ``ROOT_SQUASH`` or ``ALL_SQUASH``.

            This field is a member of `oneof`_ ``_anon_uid``.
    """

    class SquashMode(proto.Enum):
        r"""``SquashMode`` defines how remote user privileges are restricted
        when accessing an NFS export. It controls how user identities (like
        root) are mapped to anonymous users to limit access and enforce
        security.

        Values:
            SQUASH_MODE_UNSPECIFIED (0):
                Defaults to ``NO_ROOT_SQUASH``.
            NO_ROOT_SQUASH (1):
                The root user (UID 0) retains full access.
                Other users are unaffected.
            ROOT_SQUASH (2):
                The root user (UID 0) is squashed to
                anonymous user ID. Other users are unaffected.
            ALL_SQUASH (3):
                All users are squashed to anonymous user ID.
        """

        SQUASH_MODE_UNSPECIFIED = 0
        NO_ROOT_SQUASH = 1
        ROOT_SQUASH = 2
        ALL_SQUASH = 3

    allowed_clients: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    has_root_access: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    access_type: "AccessType" = proto.Field(
        proto.ENUM,
        number=3,
        optional=True,
        enum="AccessType",
    )
    nfsv3: bool = proto.Field(
        proto.BOOL,
        number=4,
        optional=True,
    )
    nfsv4: bool = proto.Field(
        proto.BOOL,
        number=5,
        optional=True,
    )
    kerberos_5_read_only: bool = proto.Field(
        proto.BOOL,
        number=6,
        optional=True,
    )
    kerberos_5_read_write: bool = proto.Field(
        proto.BOOL,
        number=7,
        optional=True,
    )
    kerberos_5i_read_only: bool = proto.Field(
        proto.BOOL,
        number=8,
        optional=True,
    )
    kerberos_5i_read_write: bool = proto.Field(
        proto.BOOL,
        number=9,
        optional=True,
    )
    kerberos_5p_read_only: bool = proto.Field(
        proto.BOOL,
        number=10,
        optional=True,
    )
    kerberos_5p_read_write: bool = proto.Field(
        proto.BOOL,
        number=11,
        optional=True,
    )
    squash_mode: SquashMode = proto.Field(
        proto.ENUM,
        number=12,
        optional=True,
        enum=SquashMode,
    )
    anon_uid: int = proto.Field(
        proto.INT64,
        number=13,
        optional=True,
    )


class SnapshotPolicy(proto.Message):
    r"""Snapshot Policy for a volume.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        enabled (bool):
            If enabled, make snapshots automatically
            according to the schedules. Default is false.

            This field is a member of `oneof`_ ``_enabled``.
        hourly_schedule (google.cloud.netapp_v1.types.HourlySchedule):
            Hourly schedule policy.

            This field is a member of `oneof`_ ``_hourly_schedule``.
        daily_schedule (google.cloud.netapp_v1.types.DailySchedule):
            Daily schedule policy.

            This field is a member of `oneof`_ ``_daily_schedule``.
        weekly_schedule (google.cloud.netapp_v1.types.WeeklySchedule):
            Weekly schedule policy.

            This field is a member of `oneof`_ ``_weekly_schedule``.
        monthly_schedule (google.cloud.netapp_v1.types.MonthlySchedule):
            Monthly schedule policy.

            This field is a member of `oneof`_ ``_monthly_schedule``.
    """

    enabled: bool = proto.Field(
        proto.BOOL,
        number=1,
        optional=True,
    )
    hourly_schedule: "HourlySchedule" = proto.Field(
        proto.MESSAGE,
        number=2,
        optional=True,
        message="HourlySchedule",
    )
    daily_schedule: "DailySchedule" = proto.Field(
        proto.MESSAGE,
        number=3,
        optional=True,
        message="DailySchedule",
    )
    weekly_schedule: "WeeklySchedule" = proto.Field(
        proto.MESSAGE,
        number=4,
        optional=True,
        message="WeeklySchedule",
    )
    monthly_schedule: "MonthlySchedule" = proto.Field(
        proto.MESSAGE,
        number=5,
        optional=True,
        message="MonthlySchedule",
    )


class HourlySchedule(proto.Message):
    r"""Make a snapshot every hour e.g. at 04:00, 05:00, 06:00.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        snapshots_to_keep (float):
            The maximum number of Snapshots to keep for
            the hourly schedule

            This field is a member of `oneof`_ ``_snapshots_to_keep``.
        minute (float):
            Set the minute of the hour to start the
            snapshot (0-59), defaults to the top of the hour
            (0).

            This field is a member of `oneof`_ ``_minute``.
    """

    snapshots_to_keep: float = proto.Field(
        proto.DOUBLE,
        number=1,
        optional=True,
    )
    minute: float = proto.Field(
        proto.DOUBLE,
        number=2,
        optional=True,
    )


class DailySchedule(proto.Message):
    r"""Make a snapshot every day e.g. at 04:00, 05:20, 23:50

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        snapshots_to_keep (float):
            The maximum number of Snapshots to keep for
            the hourly schedule

            This field is a member of `oneof`_ ``_snapshots_to_keep``.
        minute (float):
            Set the minute of the hour to start the
            snapshot (0-59), defaults to the top of the hour
            (0).

            This field is a member of `oneof`_ ``_minute``.
        hour (float):
            Set the hour to start the snapshot (0-23),
            defaults to midnight (0).

            This field is a member of `oneof`_ ``_hour``.
    """

    snapshots_to_keep: float = proto.Field(
        proto.DOUBLE,
        number=1,
        optional=True,
    )
    minute: float = proto.Field(
        proto.DOUBLE,
        number=2,
        optional=True,
    )
    hour: float = proto.Field(
        proto.DOUBLE,
        number=3,
        optional=True,
    )


class WeeklySchedule(proto.Message):
    r"""Make a snapshot every week e.g. at Monday 04:00, Wednesday
    05:20, Sunday 23:50


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        snapshots_to_keep (float):
            The maximum number of Snapshots to keep for
            the hourly schedule

            This field is a member of `oneof`_ ``_snapshots_to_keep``.
        minute (float):
            Set the minute of the hour to start the
            snapshot (0-59), defaults to the top of the hour
            (0).

            This field is a member of `oneof`_ ``_minute``.
        hour (float):
            Set the hour to start the snapshot (0-23),
            defaults to midnight (0).

            This field is a member of `oneof`_ ``_hour``.
        day (str):
            Set the day or days of the week to make a
            snapshot. Accepts a comma separated days of the
            week. Defaults to 'Sunday'.

            This field is a member of `oneof`_ ``_day``.
    """

    snapshots_to_keep: float = proto.Field(
        proto.DOUBLE,
        number=1,
        optional=True,
    )
    minute: float = proto.Field(
        proto.DOUBLE,
        number=2,
        optional=True,
    )
    hour: float = proto.Field(
        proto.DOUBLE,
        number=3,
        optional=True,
    )
    day: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )


class MonthlySchedule(proto.Message):
    r"""Make a snapshot once a month e.g. at 2nd 04:00, 7th 05:20,
    24th 23:50


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        snapshots_to_keep (float):
            The maximum number of Snapshots to keep for
            the hourly schedule

            This field is a member of `oneof`_ ``_snapshots_to_keep``.
        minute (float):
            Set the minute of the hour to start the
            snapshot (0-59), defaults to the top of the hour
            (0).

            This field is a member of `oneof`_ ``_minute``.
        hour (float):
            Set the hour to start the snapshot (0-23),
            defaults to midnight (0).

            This field is a member of `oneof`_ ``_hour``.
        days_of_month (str):
            Set the day or days of the month to make a
            snapshot (1-31). Accepts a comma separated
            number of days. Defaults to '1'.

            This field is a member of `oneof`_ ``_days_of_month``.
    """

    snapshots_to_keep: float = proto.Field(
        proto.DOUBLE,
        number=1,
        optional=True,
    )
    minute: float = proto.Field(
        proto.DOUBLE,
        number=2,
        optional=True,
    )
    hour: float = proto.Field(
        proto.DOUBLE,
        number=3,
        optional=True,
    )
    days_of_month: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )


class MountOption(proto.Message):
    r"""View only mount options for a volume.

    Attributes:
        export (str):
            Export string
        export_full (str):
            Full export string
        protocol (google.cloud.netapp_v1.types.Protocols):
            Protocol to mount with.
        instructions (str):
            Instructions for mounting
        ip_address (str):
            Output only. IP Address.
    """

    export: str = proto.Field(
        proto.STRING,
        number=1,
    )
    export_full: str = proto.Field(
        proto.STRING,
        number=2,
    )
    protocol: "Protocols" = proto.Field(
        proto.ENUM,
        number=3,
        enum="Protocols",
    )
    instructions: str = proto.Field(
        proto.STRING,
        number=4,
    )
    ip_address: str = proto.Field(
        proto.STRING,
        number=5,
    )


class RestoreParameters(proto.Message):
    r"""The RestoreParameters if volume is created from a snapshot or
    backup.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        source_snapshot (str):
            Full name of the snapshot resource.
            Format:

            projects/{project}/locations/{location}/volumes/{volume}/snapshots/{snapshot}

            This field is a member of `oneof`_ ``source``.
        source_backup (str):
            Full name of the backup resource. Format for standard
            backup:
            projects/{project}/locations/{location}/backupVaults/{backup_vault_id}/backups/{backup_id}.
            Format for BackupDR backup:
            projects/{project}/locations/{location}/backupVaults/{backup_vault}/dataSources/{data_source}/backups/{backup}

            This field is a member of `oneof`_ ``source``.
    """

    source_snapshot: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="source",
    )
    source_backup: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="source",
    )


class BackupConfig(proto.Message):
    r"""BackupConfig contains backup related config on a volume.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        backup_policies (MutableSequence[str]):
            Optional. When specified, schedule backups
            will be created based on the policy
            configuration.
        backup_vault (str):
            Optional. Name of backup vault. Format:
            projects/{project_id}/locations/{location}/backupVaults/{backup_vault_id}
        scheduled_backup_enabled (bool):
            Optional. When set to true, scheduled backup
            is enabled on the volume. This field should be
            nil when there's no backup policy attached.

            This field is a member of `oneof`_ ``_scheduled_backup_enabled``.
        backup_chain_bytes (int):
            Output only. Total size of all backups in a
            chain in bytes = baseline backup size +
            sum(incremental backup size).

            This field is a member of `oneof`_ ``_backup_chain_bytes``.
    """

    backup_policies: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    backup_vault: str = proto.Field(
        proto.STRING,
        number=2,
    )
    scheduled_backup_enabled: bool = proto.Field(
        proto.BOOL,
        number=3,
        optional=True,
    )
    backup_chain_bytes: int = proto.Field(
        proto.INT64,
        number=4,
        optional=True,
    )


class TieringPolicy(proto.Message):
    r"""Defines tiering policy for the volume.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        tier_action (google.cloud.netapp_v1.types.TieringPolicy.TierAction):
            Optional. Flag indicating if the volume has
            tiering policy enable/pause. Default is PAUSED.

            This field is a member of `oneof`_ ``_tier_action``.
        cooling_threshold_days (int):
            Optional. Time in days to mark the volume's
            data block as cold and make it eligible for
            tiering, can be range from 2-183. Default is 31.

            This field is a member of `oneof`_ ``_cooling_threshold_days``.
        hot_tier_bypass_mode_enabled (bool):
            Optional. Flag indicating that the hot tier
            bypass mode is enabled. Default is false. This
            is only applicable to Flex service level.

            This field is a member of `oneof`_ ``_hot_tier_bypass_mode_enabled``.
    """

    class TierAction(proto.Enum):
        r"""Tier action for the volume.

        Values:
            TIER_ACTION_UNSPECIFIED (0):
                Unspecified.
            ENABLED (1):
                When tiering is enabled, new cold data will
                be tiered.
            PAUSED (2):
                When paused, tiering won't be performed on
                new data. Existing data stays tiered until
                accessed.
        """

        TIER_ACTION_UNSPECIFIED = 0
        ENABLED = 1
        PAUSED = 2

    tier_action: TierAction = proto.Field(
        proto.ENUM,
        number=1,
        optional=True,
        enum=TierAction,
    )
    cooling_threshold_days: int = proto.Field(
        proto.INT32,
        number=2,
        optional=True,
    )
    hot_tier_bypass_mode_enabled: bool = proto.Field(
        proto.BOOL,
        number=3,
        optional=True,
    )


class HybridReplicationParameters(proto.Message):
    r"""The Hybrid Replication parameters for the volume.

    Attributes:
        replication (str):
            Required. Desired name for the replication of
            this volume.
        peer_volume_name (str):
            Required. Name of the user's local source
            volume to be peered with the destination volume.
        peer_cluster_name (str):
            Required. Name of the user's local source
            cluster to be peered with the destination
            cluster.
        peer_svm_name (str):
            Required. Name of the user's local source
            vserver svm to be peered with the destination
            vserver svm.
        peer_ip_addresses (MutableSequence[str]):
            Required. List of node ip addresses to be
            peered with.
        cluster_location (str):
            Optional. Name of source cluster location
            associated with the Hybrid replication. This is
            a free-form field for the display purpose only.
        description (str):
            Optional. Description of the replication.
        labels (MutableMapping[str, str]):
            Optional. Labels to be added to the
            replication as the key value pairs.
        replication_schedule (google.cloud.netapp_v1.types.HybridReplicationSchedule):
            Optional. Replication Schedule for the
            replication created.
        hybrid_replication_type (google.cloud.netapp_v1.types.HybridReplicationParameters.VolumeHybridReplicationType):
            Optional. Type of the hybrid replication.
        large_volume_constituent_count (int):
            Optional. Constituent volume count for large
            volume.
    """

    class VolumeHybridReplicationType(proto.Enum):
        r"""Type of the volume's hybrid replication.

        Values:
            VOLUME_HYBRID_REPLICATION_TYPE_UNSPECIFIED (0):
                Unspecified hybrid replication type.
            MIGRATION (1):
                Hybrid replication type for migration.
            CONTINUOUS_REPLICATION (2):
                Hybrid replication type for continuous
                replication.
            ONPREM_REPLICATION (3):
                New field for reversible OnPrem replication,
                to be used for data protection.
            REVERSE_ONPREM_REPLICATION (4):
                New field for reversible OnPrem replication,
                to be used for data protection.
        """

        VOLUME_HYBRID_REPLICATION_TYPE_UNSPECIFIED = 0
        MIGRATION = 1
        CONTINUOUS_REPLICATION = 2
        ONPREM_REPLICATION = 3
        REVERSE_ONPREM_REPLICATION = 4

    replication: str = proto.Field(
        proto.STRING,
        number=1,
    )
    peer_volume_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    peer_cluster_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    peer_svm_name: str = proto.Field(
        proto.STRING,
        number=4,
    )
    peer_ip_addresses: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )
    cluster_location: str = proto.Field(
        proto.STRING,
        number=6,
    )
    description: str = proto.Field(
        proto.STRING,
        number=7,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=8,
    )
    replication_schedule: common.HybridReplicationSchedule = proto.Field(
        proto.ENUM,
        number=9,
        enum=common.HybridReplicationSchedule,
    )
    hybrid_replication_type: VolumeHybridReplicationType = proto.Field(
        proto.ENUM,
        number=10,
        enum=VolumeHybridReplicationType,
    )
    large_volume_constituent_count: int = proto.Field(
        proto.INT32,
        number=11,
    )


class CacheParameters(proto.Message):
    r"""Cache Parameters for the volume.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        peer_volume_name (str):
            Required. Name of the origin volume for the
            cache volume.
        peer_cluster_name (str):
            Required. Name of the origin volume's ONTAP
            cluster.
        peer_svm_name (str):
            Required. Name of the origin volume's SVM.
        peer_ip_addresses (MutableSequence[str]):
            Required. List of IC LIF addresses of the
            origin volume's ONTAP cluster.
        enable_global_file_lock (bool):
            Optional. Indicates whether the cache volume
            has global file lock enabled.

            This field is a member of `oneof`_ ``_enable_global_file_lock``.
        cache_config (google.cloud.netapp_v1.types.CacheConfig):
            Optional. Configuration of the cache volume.
        cache_state (google.cloud.netapp_v1.types.CacheParameters.CacheState):
            Output only. State of the cache volume
            indicating the peering status.
        command (str):
            Output only. Copy-paste-able commands to be
            used on user's ONTAP to accept peering requests.
        peering_command_expiry_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. Expiration time for the peering
            command to be executed on user's ONTAP.
        passphrase (str):
            Output only. Temporary passphrase generated
            to accept cluster peering command.
        state_details (str):
            Output only. Detailed description of the
            current cache state.
    """

    class CacheState(proto.Enum):
        r"""State of the cache volume indicating the peering status.

        Values:
            CACHE_STATE_UNSPECIFIED (0):
                Default unspecified state.
            PENDING_CLUSTER_PEERING (1):
                State indicating waiting for cluster peering
                to be established.
            PENDING_SVM_PEERING (2):
                State indicating waiting for SVM peering to
                be established.
            PEERED (3):
                State indicating successful establishment of
                peering with origin volumes's ONTAP cluster.
            ERROR (4):
                Terminal state wherein peering with origin
                volume's ONTAP cluster has failed.
        """

        CACHE_STATE_UNSPECIFIED = 0
        PENDING_CLUSTER_PEERING = 1
        PENDING_SVM_PEERING = 2
        PEERED = 3
        ERROR = 4

    peer_volume_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    peer_cluster_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    peer_svm_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    peer_ip_addresses: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    enable_global_file_lock: bool = proto.Field(
        proto.BOOL,
        number=5,
        optional=True,
    )
    cache_config: "CacheConfig" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="CacheConfig",
    )
    cache_state: CacheState = proto.Field(
        proto.ENUM,
        number=7,
        enum=CacheState,
    )
    command: str = proto.Field(
        proto.STRING,
        number=8,
    )
    peering_command_expiry_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    passphrase: str = proto.Field(
        proto.STRING,
        number=10,
    )
    state_details: str = proto.Field(
        proto.STRING,
        number=12,
    )


class CacheConfig(proto.Message):
    r"""Configuration of the cache volume.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        cache_pre_populate (google.cloud.netapp_v1.types.CachePrePopulate):
            Optional. Pre-populate cache volume with data
            from the origin volume.
        writeback_enabled (bool):
            Optional. Flag indicating whether writeback
            is enabled for the FlexCache volume.

            This field is a member of `oneof`_ ``_writeback_enabled``.
        cifs_change_notify_enabled (bool):
            Optional. Flag indicating whether a CIFS
            change notification is enabled for the FlexCache
            volume.

            This field is a member of `oneof`_ ``_cifs_change_notify_enabled``.
        cache_pre_populate_state (google.cloud.netapp_v1.types.CacheConfig.CachePrePopulateState):
            Output only. State of the prepopulation job
            indicating how the prepopulation is progressing.
    """

    class CachePrePopulateState(proto.Enum):
        r"""State of the prepopulation job indicating how the
        prepopulation is progressing.

        Values:
            CACHE_PRE_POPULATE_STATE_UNSPECIFIED (0):
                Default unspecified state.
            NOT_NEEDED (1):
                State representing when the most recent
                create or update request did not require a
                prepopulation job.
            IN_PROGRESS (2):
                State representing when the most recent
                update request requested a prepopulation job but
                it has not yet completed.
            COMPLETE (3):
                State representing when the most recent
                update request requested a prepopulation job and
                it has completed successfully.
            ERROR (4):
                State representing when the most recent
                update request requested a prepopulation job but
                the prepopulate job failed.
        """

        CACHE_PRE_POPULATE_STATE_UNSPECIFIED = 0
        NOT_NEEDED = 1
        IN_PROGRESS = 2
        COMPLETE = 3
        ERROR = 4

    cache_pre_populate: "CachePrePopulate" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="CachePrePopulate",
    )
    writeback_enabled: bool = proto.Field(
        proto.BOOL,
        number=2,
        optional=True,
    )
    cifs_change_notify_enabled: bool = proto.Field(
        proto.BOOL,
        number=5,
        optional=True,
    )
    cache_pre_populate_state: CachePrePopulateState = proto.Field(
        proto.ENUM,
        number=6,
        enum=CachePrePopulateState,
    )


class CachePrePopulate(proto.Message):
    r"""Pre-populate cache volume with data from the origin volume.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        path_list (MutableSequence[str]):
            Optional. List of directory-paths to be
            pre-populated for the FlexCache volume.
        exclude_path_list (MutableSequence[str]):
            Optional. List of directory-paths to be
            excluded for pre-population for the FlexCache
            volume.
        recursion (bool):
            Optional. Flag indicating whether the directories listed
            with the ``path_list`` need to be recursively pre-populated.

            This field is a member of `oneof`_ ``_recursion``.
    """

    path_list: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    exclude_path_list: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    recursion: bool = proto.Field(
        proto.BOOL,
        number=3,
        optional=True,
    )


class BlockDevice(proto.Message):
    r"""Block device represents the device(s) which are stored in the
    block volume.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Optional. User-defined name for the block device, unique
            within the volume. In case no user input is provided, name
            will be auto-generated in the backend. The name must meet
            the following requirements:

            - Be between 1 and 255 characters long.
            - Contain only uppercase or lowercase letters (A-Z, a-z),
              numbers (0-9), and the following special characters: "-",
              "\_", "}", "{", ".".
            - Spaces are not allowed.

            This field is a member of `oneof`_ ``_name``.
        host_groups (MutableSequence[str]):
            Optional. A list of host groups that identify hosts that can
            mount the block volume. Format:
            ``projects/{project_id}/locations/{location}/hostGroups/{host_group_id}``
            This field can be updated after the block device is created.
        identifier (str):
            Output only. Device identifier of the block volume. This
            represents ``lun_serial_number`` for iSCSI volumes.
        size_gib (int):
            Optional. The size of the block device in GiB. Any value
            provided for the ``size_gib`` field during volume creation
            is ignored. The block device's size is system-managed and
            will be set to match the parent Volume's ``capacity_gib``.

            This field is a member of `oneof`_ ``_size_gib``.
        os_type (google.cloud.netapp_v1.types.OsType):
            Required. Immutable. The OS type of the
            volume. This field can't be changed after the
            block device is created.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    host_groups: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    identifier: str = proto.Field(
        proto.STRING,
        number=3,
    )
    size_gib: int = proto.Field(
        proto.INT64,
        number=4,
        optional=True,
    )
    os_type: common.OsType = proto.Field(
        proto.ENUM,
        number=5,
        enum=common.OsType,
    )


class RestoreBackupFilesRequest(proto.Message):
    r"""RestoreBackupFilesRequest restores files from a backup to a
    volume.

    Attributes:
        name (str):
            Required. The volume resource name, in the format
            ``projects/{project_id}/locations/{location}/volumes/{volume_id}``
        backup (str):
            Required. The backup resource name, in the format
            ``projects/{project_id}/locations/{location}/backupVaults/{backup_vault_id}/backups/{backup_id}``
        file_list (MutableSequence[str]):
            Required. List of files to be restored,
            specified by their absolute path in the source
            volume.
        restore_destination_path (str):
            Optional. Absolute directory path in the destination volume.
            This is required if the ``file_list`` is provided.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    backup: str = proto.Field(
        proto.STRING,
        number=2,
    )
    file_list: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    restore_destination_path: str = proto.Field(
        proto.STRING,
        number=4,
    )


class RestoreBackupFilesResponse(proto.Message):
    r"""RestoreBackupFilesResponse is the result of
    RestoreBackupFilesRequest.

    """


class RestoreVolumeRequest(proto.Message):
    r"""Request message for ``RestoreVolume`` API.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        backup_source (google.cloud.netapp_v1.types.BackupSource):
            The backup source of the restore operation.

            This field is a member of `oneof`_ ``source``.
        ontap_volume_target (google.cloud.netapp_v1.types.OntapVolumeTarget):
            The ONTAP volume target of the restore
            operation.

            This field is a member of `oneof`_ ``target``.
        name (str):
            Required. The resource name of the ONTAP mode storage pool,
            in the format of
            ``projects/{project}/locations/{location}/storagePools/{storage_pool}``
    """

    backup_source: "BackupSource" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="source",
        message="BackupSource",
    )
    ontap_volume_target: "OntapVolumeTarget" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="target",
        message="OntapVolumeTarget",
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class BackupSource(proto.Message):
    r"""Represents the backup source of the restore operation.

    Attributes:
        backup (str):
            Required. The backup resource name.
        file_list (MutableSequence[str]):
            Optional. List of files to be restored in the
            form of their absolute path as in source volume.
            If provided, only these files will be restored.
            If not provided, the entire backup will be
            restored (Full Backup Restore)
    """

    backup: str = proto.Field(
        proto.STRING,
        number=1,
    )
    file_list: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class OntapVolumeTarget(proto.Message):
    r"""Represents the ONTAP volume target of the restore operation.

    Attributes:
        volume_uuid (str):
            Required. The UUID of the ONTAP volume to
            restore to.
        restore_destination_path (str):
            Optional. Absolute directory path in the
            destination volume.
    """

    volume_uuid: str = proto.Field(
        proto.STRING,
        number=1,
    )
    restore_destination_path: str = proto.Field(
        proto.STRING,
        number=2,
    )


class RestoreVolumeResponse(proto.Message):
    r"""Response message for ``RestoreVolume`` API."""


class EstablishVolumePeeringRequest(proto.Message):
    r"""EstablishVolumePeeringRequest establishes cluster and svm
    peerings between the source and destination clusters.

    Attributes:
        name (str):
            Required. The volume resource name, in the format
            ``projects/{project_id}/locations/{location}/volumes/{volume_id}``
        peer_cluster_name (str):
            Required. Name of the user's local source
            cluster to be peered with the destination
            cluster.
        peer_svm_name (str):
            Required. Name of the user's local source
            vserver svm to be peered with the destination
            vserver svm.
        peer_ip_addresses (MutableSequence[str]):
            Optional. List of IPv4 IP addresses to be
            used for peering.
        peer_volume_name (str):
            Required. Name of the user's local source
            volume to be peered with the destination volume.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    peer_cluster_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    peer_svm_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    peer_ip_addresses: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    peer_volume_name: str = proto.Field(
        proto.STRING,
        number=5,
    )


class UpdateBackupConfigRequest(proto.Message):
    r"""Request message for UpdateBackupConfig

    Attributes:
        name (str):
            Required. The resource name of the
            StoragePool, in the format:
            projects/{projectNumber}/locations/{locationId}/storagePools/{poolId}
        volume_uuid (str):
            Required. The UUID of the ONTAP-mode volume.
        backup_config (google.cloud.netapp_v1.types.BackupConfig):
            Required. Backup configuration to apply.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask is used to specify the fields to be
            overwritten in the BackupConfig for the Volume. The fields
            specified in the update_mask are relative to the resource,
            not the full request. A field will be overwritten if it is
            in the mask.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    volume_uuid: str = proto.Field(
        proto.STRING,
        number=2,
    )
    backup_config: "BackupConfig" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="BackupConfig",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=4,
        message=field_mask_pb2.FieldMask,
    )


class UpdateBackupConfigResponse(proto.Message):
    r"""Response message for UpdateBackupConfig

    Attributes:
        volume_uuid (str):
            The UUID of the ONTAP-mode volume.
        backup_config (google.cloud.netapp_v1.types.BackupConfig):
            The updated Backup configuration for the
            volume.
    """

    volume_uuid: str = proto.Field(
        proto.STRING,
        number=1,
    )
    backup_config: "BackupConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="BackupConfig",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
