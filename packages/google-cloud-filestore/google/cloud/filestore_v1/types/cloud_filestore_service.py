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
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.filestore.v1",
    manifest={
        "NetworkConfig",
        "FileShareConfig",
        "NfsExportOptions",
        "ReplicaConfig",
        "Replication",
        "Instance",
        "CreateInstanceRequest",
        "GetInstanceRequest",
        "UpdateInstanceRequest",
        "RestoreInstanceRequest",
        "RevertInstanceRequest",
        "DeleteInstanceRequest",
        "ListInstancesRequest",
        "ListInstancesResponse",
        "Snapshot",
        "CreateSnapshotRequest",
        "GetSnapshotRequest",
        "DeleteSnapshotRequest",
        "UpdateSnapshotRequest",
        "ListSnapshotsRequest",
        "ListSnapshotsResponse",
        "Backup",
        "CreateBackupRequest",
        "DeleteBackupRequest",
        "UpdateBackupRequest",
        "PromoteReplicaRequest",
        "GetBackupRequest",
        "ListBackupsRequest",
        "ListBackupsResponse",
    },
)


class NetworkConfig(proto.Message):
    r"""Network configuration for the instance.

    Attributes:
        network (str):
            The name of the Google Compute Engine `VPC
            network <https://cloud.google.com/vpc/docs/vpc>`__ to which
            the instance is connected.
        modes (MutableSequence[google.cloud.filestore_v1.types.NetworkConfig.AddressMode]):
            Internet protocol versions for which the instance has IP
            addresses assigned. For this version, only MODE_IPV4 is
            supported.
        reserved_ip_range (str):
            Optional, reserved_ip_range can have one of the following
            two types of values.

            - CIDR range value when using DIRECT_PEERING connect mode.
            - `Allocated IP address
              range <https://cloud.google.com/compute/docs/ip-addresses/reserve-static-internal-ip-address>`__
              when using PRIVATE_SERVICE_ACCESS connect mode.

            When the name of an allocated IP address range is specified,
            it must be one of the ranges associated with the private
            service access connection. When specified as a direct CIDR
            value, it must be a /29 CIDR block for Basic tier, a /24
            CIDR block for High Scale tier, or a /26 CIDR block for
            Enterprise tier in one of the `internal IP address
            ranges <https://www.arin.net/reference/research/statistics/address_filters/>`__
            that identifies the range of IP addresses reserved for this
            instance. For example, 10.0.0.0/29, 192.168.0.0/24 or
            192.168.0.0/26, respectively. The range you specify can't
            overlap with either existing subnets or assigned IP address
            ranges for other Filestore instances in the selected VPC
            network.
        ip_addresses (MutableSequence[str]):
            Output only. IPv4 addresses in the format
            ``{octet1}.{octet2}.{octet3}.{octet4}`` or IPv6 addresses in
            the format
            ``{block1}:{block2}:{block3}:{block4}:{block5}:{block6}:{block7}:{block8}``.
        connect_mode (google.cloud.filestore_v1.types.NetworkConfig.ConnectMode):
            The network connect mode of the Filestore instance. If not
            provided, the connect mode defaults to DIRECT_PEERING.
    """

    class AddressMode(proto.Enum):
        r"""Internet protocol versions supported by Filestore.

        Values:
            ADDRESS_MODE_UNSPECIFIED (0):
                Internet protocol not set.
            MODE_IPV4 (1):
                Use the IPv4 internet protocol.
        """

        ADDRESS_MODE_UNSPECIFIED = 0
        MODE_IPV4 = 1

    class ConnectMode(proto.Enum):
        r"""Available connection modes.

        Values:
            CONNECT_MODE_UNSPECIFIED (0):
                Not set.
            DIRECT_PEERING (1):
                Connect via direct peering to the Filestore
                service.
            PRIVATE_SERVICE_ACCESS (2):
                Connect to your Filestore instance using
                Private Service Access. Private services access
                provides an IP address range for multiple Google
                Cloud services, including Filestore.
        """

        CONNECT_MODE_UNSPECIFIED = 0
        DIRECT_PEERING = 1
        PRIVATE_SERVICE_ACCESS = 2

    network: str = proto.Field(
        proto.STRING,
        number=1,
    )
    modes: MutableSequence[AddressMode] = proto.RepeatedField(
        proto.ENUM,
        number=3,
        enum=AddressMode,
    )
    reserved_ip_range: str = proto.Field(
        proto.STRING,
        number=4,
    )
    ip_addresses: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )
    connect_mode: ConnectMode = proto.Field(
        proto.ENUM,
        number=6,
        enum=ConnectMode,
    )


class FileShareConfig(proto.Message):
    r"""File share configuration for the instance.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Required. The name of the file share. Must use 1-16
            characters for the basic service tier and 1-63 characters
            for all other service tiers. Must use lowercase letters,
            numbers, or underscores ``[a-z0-9_]``. Must start with a
            letter. Immutable.
        capacity_gb (int):
            File share capacity in gigabytes (GB).
            Filestore defines 1 GB as 1024^3 bytes.
        source_backup (str):
            The resource name of the backup, in the format
            ``projects/{project_number}/locations/{location_id}/backups/{backup_id}``,
            that this file share has been restored from.

            This field is a member of `oneof`_ ``source``.
        nfs_export_options (MutableSequence[google.cloud.filestore_v1.types.NfsExportOptions]):
            Nfs Export Options.
            There is a limit of 10 export options per file
            share.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    capacity_gb: int = proto.Field(
        proto.INT64,
        number=2,
    )
    source_backup: str = proto.Field(
        proto.STRING,
        number=8,
        oneof="source",
    )
    nfs_export_options: MutableSequence["NfsExportOptions"] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message="NfsExportOptions",
    )


class NfsExportOptions(proto.Message):
    r"""NFS export options specifications.

    Attributes:
        ip_ranges (MutableSequence[str]):
            List of either an IPv4 addresses in the format
            ``{octet1}.{octet2}.{octet3}.{octet4}`` or CIDR ranges in
            the format
            ``{octet1}.{octet2}.{octet3}.{octet4}/{mask size}`` which
            may mount the file share. Overlapping IP ranges are not
            allowed, both within and across NfsExportOptions. An error
            will be returned. The limit is 64 IP ranges/addresses for
            each FileShareConfig among all NfsExportOptions.
        access_mode (google.cloud.filestore_v1.types.NfsExportOptions.AccessMode):
            Either READ_ONLY, for allowing only read requests on the
            exported directory, or READ_WRITE, for allowing both read
            and write requests. The default is READ_WRITE.
        squash_mode (google.cloud.filestore_v1.types.NfsExportOptions.SquashMode):
            Either NO_ROOT_SQUASH, for allowing root access on the
            exported directory, or ROOT_SQUASH, for not allowing root
            access. The default is NO_ROOT_SQUASH.
        anon_uid (int):
            An integer representing the anonymous user id with a default
            value of 65534. Anon_uid may only be set with squash_mode of
            ROOT_SQUASH. An error will be returned if this field is
            specified for other squash_mode settings.
        anon_gid (int):
            An integer representing the anonymous group id with a
            default value of 65534. Anon_gid may only be set with
            squash_mode of ROOT_SQUASH. An error will be returned if
            this field is specified for other squash_mode settings.
    """

    class AccessMode(proto.Enum):
        r"""The access mode.

        Values:
            ACCESS_MODE_UNSPECIFIED (0):
                AccessMode not set.
            READ_ONLY (1):
                The client can only read the file share.
            READ_WRITE (2):
                The client can read and write the file share
                (default).
        """

        ACCESS_MODE_UNSPECIFIED = 0
        READ_ONLY = 1
        READ_WRITE = 2

    class SquashMode(proto.Enum):
        r"""The squash mode.

        Values:
            SQUASH_MODE_UNSPECIFIED (0):
                SquashMode not set.
            NO_ROOT_SQUASH (1):
                The Root user has root access to the file
                share (default).
            ROOT_SQUASH (2):
                The Root user has squashed access to the
                anonymous uid/gid.
        """

        SQUASH_MODE_UNSPECIFIED = 0
        NO_ROOT_SQUASH = 1
        ROOT_SQUASH = 2

    ip_ranges: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    access_mode: AccessMode = proto.Field(
        proto.ENUM,
        number=2,
        enum=AccessMode,
    )
    squash_mode: SquashMode = proto.Field(
        proto.ENUM,
        number=3,
        enum=SquashMode,
    )
    anon_uid: int = proto.Field(
        proto.INT64,
        number=4,
    )
    anon_gid: int = proto.Field(
        proto.INT64,
        number=5,
    )


class ReplicaConfig(proto.Message):
    r"""Replica configuration for the instance.

    Attributes:
        state (google.cloud.filestore_v1.types.ReplicaConfig.State):
            Output only. The replica state.
        state_reasons (MutableSequence[google.cloud.filestore_v1.types.ReplicaConfig.StateReason]):
            Output only. Additional information about the
            replication state, if available.
        peer_instance (str):
            Optional. The peer instance.
        last_active_sync_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp of the latest
            replication snapshot taken on the active
            instance and is already replicated safely.
    """

    class State(proto.Enum):
        r"""The replica state.

        Values:
            STATE_UNSPECIFIED (0):
                State not set.
            CREATING (1):
                The replica is being created.
            READY (3):
                The replica is ready.
            REMOVING (4):
                The replica is being removed.
            FAILED (5):
                The replica is experiencing an issue and might be unusable.
                You can get further details from the ``stateReasons`` field
                of the ``ReplicaConfig`` object.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        READY = 3
        REMOVING = 4
        FAILED = 5

    class StateReason(proto.Enum):
        r"""Additional information about the replication state, if
        available.

        Values:
            STATE_REASON_UNSPECIFIED (0):
                Reason not specified.
            PEER_INSTANCE_UNREACHABLE (1):
                The peer instance is unreachable.
            REMOVE_FAILED (2):
                The remove replica peer instance operation
                failed.
        """

        STATE_REASON_UNSPECIFIED = 0
        PEER_INSTANCE_UNREACHABLE = 1
        REMOVE_FAILED = 2

    state: State = proto.Field(
        proto.ENUM,
        number=1,
        enum=State,
    )
    state_reasons: MutableSequence[StateReason] = proto.RepeatedField(
        proto.ENUM,
        number=2,
        enum=StateReason,
    )
    peer_instance: str = proto.Field(
        proto.STRING,
        number=3,
    )
    last_active_sync_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10,
        message=timestamp_pb2.Timestamp,
    )


class Replication(proto.Message):
    r"""Replication specifications.

    Attributes:
        role (google.cloud.filestore_v1.types.Replication.Role):
            Optional. The replication role.
        replicas (MutableSequence[google.cloud.filestore_v1.types.ReplicaConfig]):
            Optional. Replication configuration for the
            replica instance associated with this instance.
            Only a single replica is supported.
    """

    class Role(proto.Enum):
        r"""Replication role.

        Values:
            ROLE_UNSPECIFIED (0):
                Role not set.
            ACTIVE (1):
                The instance is the ``ACTIVE`` replication member, functions
                as the replication source instance.
            STANDBY (2):
                The instance is the ``STANDBY`` replication member,
                functions as the replication destination instance.
        """

        ROLE_UNSPECIFIED = 0
        ACTIVE = 1
        STANDBY = 2

    role: Role = proto.Field(
        proto.ENUM,
        number=1,
        enum=Role,
    )
    replicas: MutableSequence["ReplicaConfig"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="ReplicaConfig",
    )


class Instance(proto.Message):
    r"""A Filestore instance.

    Attributes:
        name (str):
            Output only. The resource name of the instance, in the
            format
            ``projects/{project}/locations/{location}/instances/{instance}``.
        description (str):
            The description of the instance (2048
            characters or less).
        state (google.cloud.filestore_v1.types.Instance.State):
            Output only. The instance state.
        status_message (str):
            Output only. Additional information about the
            instance state, if available.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the instance was
            created.
        tier (google.cloud.filestore_v1.types.Instance.Tier):
            The service tier of the instance.
        labels (MutableMapping[str, str]):
            Resource labels to represent user provided
            metadata.
        file_shares (MutableSequence[google.cloud.filestore_v1.types.FileShareConfig]):
            File system shares on the instance.
            For this version, only a single file share is
            supported.
        networks (MutableSequence[google.cloud.filestore_v1.types.NetworkConfig]):
            VPC networks to which the instance is
            connected. For this version, only a single
            network is supported.
        etag (str):
            Server-specified ETag for the instance
            resource to prevent simultaneous updates from
            overwriting each other.
        satisfies_pzs (google.protobuf.wrappers_pb2.BoolValue):
            Output only. Reserved for future use.
        satisfies_pzi (bool):
            Output only. Reserved for future use.
        kms_key_name (str):
            KMS key name used for data encryption.
        suspension_reasons (MutableSequence[google.cloud.filestore_v1.types.Instance.SuspensionReason]):
            Output only. Field indicates all the reasons
            the instance is in "SUSPENDED" state.
        replication (google.cloud.filestore_v1.types.Replication):
            Optional. Replication configuration.
        tags (MutableMapping[str, str]):
            Optional. Input only. Immutable. Tag key-value pairs bound
            to this resource. Each key must be a namespaced name and
            each value a short name. Example: "123456789012/environment"
            : "production", "123456789013/costCenter" : "marketing" See
            the documentation for more information:

            - Namespaced name:
              https://cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#retrieving_tag_key
            - Short name:
              https://cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#retrieving_tag_value
        protocol (google.cloud.filestore_v1.types.Instance.FileProtocol):
            Immutable. The protocol indicates the access protocol for
            all shares in the instance. This field is immutable and it
            cannot be changed after the instance has been created.
            Default value: ``NFS_V3``.
        custom_performance_supported (bool):
            Output only. Indicates whether this instance supports
            configuring its performance. If true, the user can configure
            the instance's performance by using the 'performance_config'
            field.
        performance_config (google.cloud.filestore_v1.types.Instance.PerformanceConfig):
            Optional. Used to configure performance.
        performance_limits (google.cloud.filestore_v1.types.Instance.PerformanceLimits):
            Output only. Used for getting performance
            limits.
        deletion_protection_enabled (bool):
            Optional. Indicates whether the instance is
            protected against deletion.
        deletion_protection_reason (str):
            Optional. The reason for enabling deletion
            protection.
    """

    class State(proto.Enum):
        r"""The instance state.

        Values:
            STATE_UNSPECIFIED (0):
                State not set.
            CREATING (1):
                The instance is being created.
            READY (2):
                The instance is available for use.
            REPAIRING (3):
                Work is being done on the instance. You can get further
                details from the ``statusMessage`` field of the ``Instance``
                resource.
            DELETING (4):
                The instance is shutting down.
            ERROR (6):
                The instance is experiencing an issue and might be unusable.
                You can get further details from the ``statusMessage`` field
                of the ``Instance`` resource.
            RESTORING (7):
                The instance is restoring a backup to an
                existing file share and may be unusable during
                this time.
            SUSPENDED (8):
                The instance is suspended. You can get further details from
                the ``suspension_reasons`` field of the ``Instance``
                resource.
            SUSPENDING (9):
                The instance is in the process of becoming
                suspended.
            RESUMING (10):
                The instance is in the process of becoming
                active.
            REVERTING (12):
                The instance is reverting to a snapshot.
            PROMOTING (13):
                The replica instance is being promoted.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        READY = 2
        REPAIRING = 3
        DELETING = 4
        ERROR = 6
        RESTORING = 7
        SUSPENDED = 8
        SUSPENDING = 9
        RESUMING = 10
        REVERTING = 12
        PROMOTING = 13

    class Tier(proto.Enum):
        r"""Available service tiers.

        Values:
            TIER_UNSPECIFIED (0):
                Not set.
            STANDARD (1):
                STANDARD tier. BASIC_HDD is the preferred term for this
                tier.
            PREMIUM (2):
                PREMIUM tier. BASIC_SSD is the preferred term for this tier.
            BASIC_HDD (3):
                BASIC instances offer a maximum capacity of 63.9 TB.
                BASIC_HDD is an alias for STANDARD Tier, offering economical
                performance backed by HDD.
            BASIC_SSD (4):
                BASIC instances offer a maximum capacity of 63.9 TB.
                BASIC_SSD is an alias for PREMIUM Tier, and offers improved
                performance backed by SSD.
            HIGH_SCALE_SSD (5):
                HIGH_SCALE instances offer expanded capacity and performance
                scaling capabilities.
            ENTERPRISE (6):
                ENTERPRISE instances offer the features and
                availability needed for mission-critical
                workloads.
            ZONAL (7):
                ZONAL instances offer expanded capacity and
                performance scaling capabilities.
            REGIONAL (8):
                REGIONAL instances offer the features and
                availability needed for mission-critical
                workloads.
        """

        TIER_UNSPECIFIED = 0
        STANDARD = 1
        PREMIUM = 2
        BASIC_HDD = 3
        BASIC_SSD = 4
        HIGH_SCALE_SSD = 5
        ENTERPRISE = 6
        ZONAL = 7
        REGIONAL = 8

    class SuspensionReason(proto.Enum):
        r"""SuspensionReason contains the possible reasons for a
        suspension.

        Values:
            SUSPENSION_REASON_UNSPECIFIED (0):
                Not set.
            KMS_KEY_ISSUE (1):
                The KMS key used by the instance is either
                revoked or denied access to.
        """

        SUSPENSION_REASON_UNSPECIFIED = 0
        KMS_KEY_ISSUE = 1

    class FileProtocol(proto.Enum):
        r"""File access protocol.

        Values:
            FILE_PROTOCOL_UNSPECIFIED (0):
                FILE_PROTOCOL_UNSPECIFIED serves a "not set" default value
                when a FileProtocol is a separate field in a message.
            NFS_V3 (1):
                NFS 3.0.
            NFS_V4_1 (2):
                NFS 4.1.
        """

        FILE_PROTOCOL_UNSPECIFIED = 0
        NFS_V3 = 1
        NFS_V4_1 = 2

    class IOPSPerTB(proto.Message):
        r"""IOPS per TB.
        Filestore defines TB as 1024^4 bytes (TiB).

        Attributes:
            max_iops_per_tb (int):
                Required. Maximum IOPS per TiB.
        """

        max_iops_per_tb: int = proto.Field(
            proto.INT64,
            number=2,
        )

    class FixedIOPS(proto.Message):
        r"""Fixed IOPS (input/output operations per second) parameters.

        Attributes:
            max_iops (int):
                Required. Maximum IOPS.
        """

        max_iops: int = proto.Field(
            proto.INT64,
            number=2,
        )

    class PerformanceConfig(proto.Message):
        r"""Used for setting the performance configuration.
        If the user doesn't specify PerformanceConfig, automatically
        provision the default performance settings as described in
        https://cloud.google.com/filestore/docs/performance. Larger
        instances will be linearly set to more IOPS. If the instance's
        capacity is increased or decreased, its performance will be
        automatically adjusted upwards or downwards accordingly
        (respectively).

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            iops_per_tb (google.cloud.filestore_v1.types.Instance.IOPSPerTB):
                Provision IOPS dynamically based on the capacity of the
                instance. Provisioned IOPS will be calculated by multiplying
                the capacity of the instance in TiB by the ``iops_per_tb``
                value. For example, for a 2 TiB instance with an
                ``iops_per_tb`` value of 17000 the provisioned IOPS will be
                34000.

                If the calculated value is outside the supported range for
                the instance's capacity during instance creation, instance
                creation will fail with an ``InvalidArgument`` error.
                Similarly, if an instance capacity update would result in a
                value outside the supported range, the update will fail with
                an ``InvalidArgument`` error.

                This field is a member of `oneof`_ ``mode``.
            fixed_iops (google.cloud.filestore_v1.types.Instance.FixedIOPS):
                Choose a fixed provisioned IOPS value for the instance,
                which will remain constant regardless of instance capacity.
                Value must be a multiple of 1000.

                If the chosen value is outside the supported range for the
                instance's capacity during instance creation, instance
                creation will fail with an ``InvalidArgument`` error.
                Similarly, if an instance capacity update would result in a
                value outside the supported range, the update will fail with
                an ``InvalidArgument`` error.

                This field is a member of `oneof`_ ``mode``.
        """

        iops_per_tb: "Instance.IOPSPerTB" = proto.Field(
            proto.MESSAGE,
            number=4,
            oneof="mode",
            message="Instance.IOPSPerTB",
        )
        fixed_iops: "Instance.FixedIOPS" = proto.Field(
            proto.MESSAGE,
            number=2,
            oneof="mode",
            message="Instance.FixedIOPS",
        )

    class PerformanceLimits(proto.Message):
        r"""The enforced performance limits, calculated from the
        instance's performance configuration.

        Attributes:
            max_iops (int):
                Output only. The max IOPS.
            max_read_iops (int):
                Output only. The max read IOPS.
            max_write_iops (int):
                Output only. The max write IOPS.
            max_read_throughput_bps (int):
                Output only. The max read throughput in bytes
                per second.
            max_write_throughput_bps (int):
                Output only. The max write throughput in
                bytes per second.
        """

        max_iops: int = proto.Field(
            proto.INT64,
            number=7,
        )
        max_read_iops: int = proto.Field(
            proto.INT64,
            number=1,
        )
        max_write_iops: int = proto.Field(
            proto.INT64,
            number=2,
        )
        max_read_throughput_bps: int = proto.Field(
            proto.INT64,
            number=5,
        )
        max_write_throughput_bps: int = proto.Field(
            proto.INT64,
            number=6,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=5,
        enum=State,
    )
    status_message: str = proto.Field(
        proto.STRING,
        number=6,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    tier: Tier = proto.Field(
        proto.ENUM,
        number=8,
        enum=Tier,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=9,
    )
    file_shares: MutableSequence["FileShareConfig"] = proto.RepeatedField(
        proto.MESSAGE,
        number=10,
        message="FileShareConfig",
    )
    networks: MutableSequence["NetworkConfig"] = proto.RepeatedField(
        proto.MESSAGE,
        number=11,
        message="NetworkConfig",
    )
    etag: str = proto.Field(
        proto.STRING,
        number=12,
    )
    satisfies_pzs: wrappers_pb2.BoolValue = proto.Field(
        proto.MESSAGE,
        number=13,
        message=wrappers_pb2.BoolValue,
    )
    satisfies_pzi: bool = proto.Field(
        proto.BOOL,
        number=18,
    )
    kms_key_name: str = proto.Field(
        proto.STRING,
        number=14,
    )
    suspension_reasons: MutableSequence[SuspensionReason] = proto.RepeatedField(
        proto.ENUM,
        number=15,
        enum=SuspensionReason,
    )
    replication: "Replication" = proto.Field(
        proto.MESSAGE,
        number=19,
        message="Replication",
    )
    tags: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=20,
    )
    protocol: FileProtocol = proto.Field(
        proto.ENUM,
        number=21,
        enum=FileProtocol,
    )
    custom_performance_supported: bool = proto.Field(
        proto.BOOL,
        number=23,
    )
    performance_config: PerformanceConfig = proto.Field(
        proto.MESSAGE,
        number=24,
        message=PerformanceConfig,
    )
    performance_limits: PerformanceLimits = proto.Field(
        proto.MESSAGE,
        number=25,
        message=PerformanceLimits,
    )
    deletion_protection_enabled: bool = proto.Field(
        proto.BOOL,
        number=26,
    )
    deletion_protection_reason: str = proto.Field(
        proto.STRING,
        number=27,
    )


class CreateInstanceRequest(proto.Message):
    r"""CreateInstanceRequest creates an instance.

    Attributes:
        parent (str):
            Required. The instance's project and location, in the format
            ``projects/{project_id}/locations/{location}``. In
            Filestore, locations map to Google Cloud zones, for example
            **us-west1-b**.
        instance_id (str):
            Required. The name of the instance to create.
            The name must be unique for the specified
            project and location.
        instance (google.cloud.filestore_v1.types.Instance):
            Required. An [instance
            resource][google.cloud.filestore.v1.Instance]
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    instance_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    instance: "Instance" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Instance",
    )


class GetInstanceRequest(proto.Message):
    r"""GetInstanceRequest gets the state of an instance.

    Attributes:
        name (str):
            Required. The instance resource name, in the format
            ``projects/{project_id}/locations/{location}/instances/{instance_id}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateInstanceRequest(proto.Message):
    r"""UpdateInstanceRequest updates the settings of an instance.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Mask of fields to update. At least one path must be supplied
            in this field. The elements of the repeated paths field may
            only include these fields:

            - "description"
            - "file_shares"
            - "labels"
            - "performance_config"
            - "deletion_protection_enabled"
            - "deletion_protection_reason".
        instance (google.cloud.filestore_v1.types.Instance):
            Only fields specified in update_mask are updated.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    instance: "Instance" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Instance",
    )


class RestoreInstanceRequest(proto.Message):
    r"""RestoreInstanceRequest restores an existing instance's file
    share from a backup.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Required. The resource name of the instance, in the format
            ``projects/{project_number}/locations/{location_id}/instances/{instance_id}``.
        file_share (str):
            Required. Name of the file share in the
            Filestore instance that the backup is being
            restored to.
        source_backup (str):
            The resource name of the backup, in the format
            ``projects/{project_number}/locations/{location_id}/backups/{backup_id}``.

            This field is a member of `oneof`_ ``source``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    file_share: str = proto.Field(
        proto.STRING,
        number=2,
    )
    source_backup: str = proto.Field(
        proto.STRING,
        number=3,
        oneof="source",
    )


class RevertInstanceRequest(proto.Message):
    r"""RevertInstanceRequest reverts the given instance's file share
    to the specified snapshot.

    Attributes:
        name (str):
            Required. The resource name of the instance, in the format
            ``projects/{project_id}/locations/{location_id}/instances/{instance_id}``.
        target_snapshot_id (str):
            Required. The snapshot resource ID, in the format
            'my-snapshot', where the specified ID is the {snapshot_id}
            of the fully qualified name like
            ``projects/{project_id}/locations/{location_id}/instances/{instance_id}/snapshots/{snapshot_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    target_snapshot_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DeleteInstanceRequest(proto.Message):
    r"""DeleteInstanceRequest deletes an instance.

    Attributes:
        name (str):
            Required. The instance resource name, in the format
            ``projects/{project_id}/locations/{location}/instances/{instance_id}``
        force (bool):
            If set to true, all snapshots of the instance
            will also be deleted. (Otherwise, the request
            will only work if the instance has no
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


class ListInstancesRequest(proto.Message):
    r"""ListInstancesRequest lists instances.

    Attributes:
        parent (str):
            Required. The project and location for which to retrieve
            instance information, in the format
            ``projects/{project_id}/locations/{location}``. In Cloud
            Filestore, locations map to Google Cloud zones, for example
            **us-west1-b**. To retrieve instance information for all
            locations, use "-" for the ``{location}`` value.
        page_size (int):
            The maximum number of items to return.
        page_token (str):
            The next_page_token value to use if there are additional
            results to retrieve for this list request.
        order_by (str):
            Sort results. Supported values are "name",
            "name desc" or "" (unsorted).
        filter (str):
            List filter.
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


class ListInstancesResponse(proto.Message):
    r"""ListInstancesResponse is the result of ListInstancesRequest.

    Attributes:
        instances (MutableSequence[google.cloud.filestore_v1.types.Instance]):
            A list of instances in the project for the specified
            location.

            If the ``{location}`` value in the request is "-", the
            response contains a list of instances from all locations. If
            any location is unreachable, the response will only return
            instances in reachable locations and the "unreachable" field
            will be populated with a list of unreachable locations.
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

    instances: MutableSequence["Instance"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Instance",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class Snapshot(proto.Message):
    r"""A Filestore snapshot.

    Attributes:
        name (str):
            Output only. The resource name of the snapshot, in the
            format
            ``projects/{project_id}/locations/{location_id}/instances/{instance_id}/snapshots/{snapshot_id}``.
        description (str):
            A description of the snapshot with 2048
            characters or less. Requests with longer
            descriptions will be rejected.
        state (google.cloud.filestore_v1.types.Snapshot.State):
            Output only. The snapshot state.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the snapshot was
            created.
        labels (MutableMapping[str, str]):
            Resource labels to represent user provided
            metadata.
        filesystem_used_bytes (int):
            Output only. The amount of bytes needed to
            allocate a full copy of the snapshot content
        tags (MutableMapping[str, str]):
            Optional. Input only. Immutable. Tag key-value pairs bound
            to this resource. Each key must be a namespaced name and
            each value a short name. Example: "123456789012/environment"
            : "production", "123456789013/costCenter" : "marketing" See
            the documentation for more information:

            - Namespaced name:
              https://cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#retrieving_tag_key
            - Short name:
              https://cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#retrieving_tag_value
    """

    class State(proto.Enum):
        r"""The snapshot state.

        Values:
            STATE_UNSPECIFIED (0):
                State not set.
            CREATING (1):
                Snapshot is being created.
            READY (2):
                Snapshot is available for use.
            DELETING (3):
                Snapshot is being deleted.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        READY = 2
        DELETING = 3

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=3,
        enum=State,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )
    filesystem_used_bytes: int = proto.Field(
        proto.INT64,
        number=6,
    )
    tags: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=7,
    )


class CreateSnapshotRequest(proto.Message):
    r"""CreateSnapshotRequest creates a snapshot.

    Attributes:
        parent (str):
            Required. The Filestore Instance to create the snapshots of,
            in the format
            ``projects/{project_id}/locations/{location}/instances/{instance_id}``
        snapshot_id (str):
            Required. The ID to use for the snapshot.
            The ID must be unique within the specified
            instance.

            This value must start with a lowercase letter
            followed by up to 62 lowercase letters, numbers,
            or hyphens, and cannot end with a hyphen.
        snapshot (google.cloud.filestore_v1.types.Snapshot):
            Required. A snapshot resource.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    snapshot_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    snapshot: "Snapshot" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Snapshot",
    )


class GetSnapshotRequest(proto.Message):
    r"""GetSnapshotRequest gets the state of a snapshot.

    Attributes:
        name (str):
            Required. The snapshot resource name, in the format
            ``projects/{project_id}/locations/{location}/instances/{instance_id}/snapshots/{snapshot_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteSnapshotRequest(proto.Message):
    r"""DeleteSnapshotRequest deletes a snapshot.

    Attributes:
        name (str):
            Required. The snapshot resource name, in the format
            ``projects/{project_id}/locations/{location}/instances/{instance_id}/snapshots/{snapshot_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateSnapshotRequest(proto.Message):
    r"""UpdateSnapshotRequest updates description and/or labels for a
    snapshot.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Mask of fields to update. At least
            one path must be supplied in this field.
        snapshot (google.cloud.filestore_v1.types.Snapshot):
            Required. A snapshot resource.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    snapshot: "Snapshot" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Snapshot",
    )


class ListSnapshotsRequest(proto.Message):
    r"""ListSnapshotsRequest lists snapshots.

    Attributes:
        parent (str):
            Required. The instance for which to retrieve snapshot
            information, in the format
            ``projects/{project_id}/locations/{location}/instances/{instance_id}``.
        page_size (int):
            The maximum number of items to return.
        page_token (str):
            The next_page_token value to use if there are additional
            results to retrieve for this list request.
        order_by (str):
            Sort results. Supported values are "name",
            "name desc" or "" (unsorted).
        filter (str):
            List filter.
        return_partial_success (bool):
            Optional. If true, allow partial responses
            for multi-regional Aggregated List requests.
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
    return_partial_success: bool = proto.Field(
        proto.BOOL,
        number=6,
    )


class ListSnapshotsResponse(proto.Message):
    r"""ListSnapshotsResponse is the result of ListSnapshotsRequest.

    Attributes:
        snapshots (MutableSequence[google.cloud.filestore_v1.types.Snapshot]):
            A list of snapshots in the project for the
            specified instance.
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

    snapshots: MutableSequence["Snapshot"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Snapshot",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class Backup(proto.Message):
    r"""A Filestore backup.

    Attributes:
        name (str):
            Output only. The resource name of the backup, in the format
            ``projects/{project_number}/locations/{location_id}/backups/{backup_id}``.
        description (str):
            A description of the backup with 2048
            characters or less. Requests with longer
            descriptions will be rejected.
        state (google.cloud.filestore_v1.types.Backup.State):
            Output only. The backup state.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the backup was
            created.
        labels (MutableMapping[str, str]):
            Resource labels to represent user provided
            metadata.
        capacity_gb (int):
            Output only. Capacity of the source file
            share when the backup was created.
        storage_bytes (int):
            Output only. The size of the storage used by
            the backup. As backups share storage, this
            number is expected to change with backup
            creation/deletion.
        source_instance (str):
            The resource name of the source Filestore instance, in the
            format
            ``projects/{project_number}/locations/{location_id}/instances/{instance_id}``,
            used to create this backup.
        source_file_share (str):
            Name of the file share in the source
            Filestore instance that the backup is created
            from.
        source_instance_tier (google.cloud.filestore_v1.types.Instance.Tier):
            Output only. The service tier of the source
            Filestore instance that this backup is created
            from.
        download_bytes (int):
            Output only. Amount of bytes that will be
            downloaded if the backup is restored. This may
            be different than storage bytes, since
            sequential backups of the same disk will share
            storage.
        satisfies_pzs (google.protobuf.wrappers_pb2.BoolValue):
            Output only. Reserved for future use.
        satisfies_pzi (bool):
            Output only. Reserved for future use.
        kms_key (str):
            Immutable. KMS key name used for data
            encryption.
        tags (MutableMapping[str, str]):
            Optional. Input only. Immutable. Tag key-value pairs bound
            to this resource. Each key must be a namespaced name and
            each value a short name. Example: "123456789012/environment"
            : "production", "123456789013/costCenter" : "marketing" See
            the documentation for more information:

            - Namespaced name:
              https://cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#retrieving_tag_key
            - Short name:
              https://cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#retrieving_tag_value
        file_system_protocol (google.cloud.filestore_v1.types.Instance.FileProtocol):
            Output only. The file system protocol of the
            source Filestore instance that this backup is
            created from.
    """

    class State(proto.Enum):
        r"""The backup state.

        Values:
            STATE_UNSPECIFIED (0):
                State not set.
            CREATING (1):
                Backup is being created.
            FINALIZING (2):
                Backup has been taken and the operation is
                being finalized. At this point, changes to the
                file share will not be reflected in the backup.
            READY (3):
                Backup is available for use.
            DELETING (4):
                Backup is being deleted.
            INVALID (5):
                Backup is not valid and cannot be used for
                creating new instances or restoring existing
                instances.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        FINALIZING = 2
        READY = 3
        DELETING = 4
        INVALID = 5

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=3,
        enum=State,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )
    capacity_gb: int = proto.Field(
        proto.INT64,
        number=6,
    )
    storage_bytes: int = proto.Field(
        proto.INT64,
        number=7,
    )
    source_instance: str = proto.Field(
        proto.STRING,
        number=8,
    )
    source_file_share: str = proto.Field(
        proto.STRING,
        number=9,
    )
    source_instance_tier: "Instance.Tier" = proto.Field(
        proto.ENUM,
        number=10,
        enum="Instance.Tier",
    )
    download_bytes: int = proto.Field(
        proto.INT64,
        number=11,
    )
    satisfies_pzs: wrappers_pb2.BoolValue = proto.Field(
        proto.MESSAGE,
        number=12,
        message=wrappers_pb2.BoolValue,
    )
    satisfies_pzi: bool = proto.Field(
        proto.BOOL,
        number=14,
    )
    kms_key: str = proto.Field(
        proto.STRING,
        number=13,
    )
    tags: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=15,
    )
    file_system_protocol: "Instance.FileProtocol" = proto.Field(
        proto.ENUM,
        number=16,
        enum="Instance.FileProtocol",
    )


class CreateBackupRequest(proto.Message):
    r"""CreateBackupRequest creates a backup.

    Attributes:
        parent (str):
            Required. The backup's project and location, in the format
            ``projects/{project_number}/locations/{location}``. In
            Filestore, backup locations map to Google Cloud regions, for
            example **us-west1**.
        backup (google.cloud.filestore_v1.types.Backup):
            Required. A [backup
            resource][google.cloud.filestore.v1.Backup]
        backup_id (str):
            Required. The ID to use for the backup. The ID must be
            unique within the specified project and location.

            This value must start with a lowercase letter followed by up
            to 62 lowercase letters, numbers, or hyphens, and cannot end
            with a hyphen. Values that do not match this pattern will
            trigger an INVALID_ARGUMENT error.
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
    backup_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteBackupRequest(proto.Message):
    r"""DeleteBackupRequest deletes a backup.

    Attributes:
        name (str):
            Required. The backup resource name, in the format
            ``projects/{project_number}/locations/{location}/backups/{backup_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateBackupRequest(proto.Message):
    r"""UpdateBackupRequest updates description and/or labels for a
    backup.

    Attributes:
        backup (google.cloud.filestore_v1.types.Backup):
            Required. A [backup
            resource][google.cloud.filestore.v1.Backup]
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Mask of fields to update.  At least
            one path must be supplied in this field.
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


class PromoteReplicaRequest(proto.Message):
    r"""PromoteReplicaRequest promotes a Filestore standby instance
    (replica).

    Attributes:
        name (str):
            Required. The resource name of the instance, in the format
            ``projects/{project_id}/locations/{location_id}/instances/{instance_id}``.
        peer_instance (str):
            Optional. The resource name of the peer instance to promote,
            in the format
            ``projects/{project_id}/locations/{location_id}/instances/{instance_id}``.
            The peer instance is required if the operation is called on
            an active instance.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    peer_instance: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetBackupRequest(proto.Message):
    r"""GetBackupRequest gets the state of a backup.

    Attributes:
        name (str):
            Required. The backup resource name, in the format
            ``projects/{project_number}/locations/{location}/backups/{backup_id}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListBackupsRequest(proto.Message):
    r"""ListBackupsRequest lists backups.

    Attributes:
        parent (str):
            Required. The project and location for which to retrieve
            backup information, in the format
            ``projects/{project_number}/locations/{location}``. In
            Filestore, backup locations map to Google Cloud regions, for
            example **us-west1**. To retrieve backup information for all
            locations, use "-" for the ``{location}`` value.
        page_size (int):
            The maximum number of items to return.
        page_token (str):
            The next_page_token value to use if there are additional
            results to retrieve for this list request.
        order_by (str):
            Sort results. Supported values are "name",
            "name desc" or "" (unsorted).
        filter (str):
            List filter.
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


class ListBackupsResponse(proto.Message):
    r"""ListBackupsResponse is the result of ListBackupsRequest.

    Attributes:
        backups (MutableSequence[google.cloud.filestore_v1.types.Backup]):
            A list of backups in the project for the specified location.

            If the ``{location}`` value in the request is "-", the
            response contains a list of backups from all locations. If
            any location is unreachable, the response will only return
            backups in reachable locations and the "unreachable" field
            will be populated with a list of unreachable locations.
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


__all__ = tuple(sorted(__protobuf__.manifest))
