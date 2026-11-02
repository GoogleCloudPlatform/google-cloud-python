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

import proto  # type: ignore

from google.cloud.backupdr_v1.types import backupvault_gce

__protobuf__ = proto.module(
    package="google.cloud.backupdr.v1",
    manifest={
        "DiskTargetEnvironment",
        "RegionDiskTargetEnvironment",
        "DiskRestoreProperties",
        "DiskBackupProperties",
        "DiskDataSourceProperties",
    },
)


class DiskTargetEnvironment(proto.Message):
    r"""DiskTargetEnvironment represents the target environment for
    the disk.

    Attributes:
        project (str):
            Required. Target project for the disk.
        zone (str):
            Required. Target zone for the disk.
    """

    project: str = proto.Field(
        proto.STRING,
        number=1,
    )
    zone: str = proto.Field(
        proto.STRING,
        number=2,
    )


class RegionDiskTargetEnvironment(proto.Message):
    r"""RegionDiskTargetEnvironment represents the target environment
    for the disk.

    Attributes:
        project (str):
            Required. Target project for the disk.
        region (str):
            Required. Target region for the disk.
        replica_zones (MutableSequence[str]):
            Required. Target URLs of the replica zones
            for the disk.
    """

    project: str = proto.Field(
        proto.STRING,
        number=1,
    )
    region: str = proto.Field(
        proto.STRING,
        number=2,
    )
    replica_zones: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class DiskRestoreProperties(proto.Message):
    r"""DiskRestoreProperties represents the properties of a Disk
    restore.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Required. Name of the disk.

            This field is a member of `oneof`_ ``_name``.
        description (str):
            Optional. An optional description of this
            resource. Provide this property when you create
            the resource.

            This field is a member of `oneof`_ ``_description``.
        size_gb (int):
            Required. The size of the disk in GB.

            This field is a member of `oneof`_ ``_size_gb``.
        licenses (MutableSequence[str]):
            Optional. A list of publicly available
            licenses that are applicable to this backup.
            This is applicable if the original image had
            licenses attached, e.g. Windows image
        guest_os_feature (MutableSequence[google.cloud.backupdr_v1.types.GuestOsFeature]):
            Optional. A list of features to enable in the
            guest operating system. This is applicable only
            for bootable images.
        disk_encryption_key (google.cloud.backupdr_v1.types.CustomerEncryptionKey):
            Optional. Encrypts the disk using a
            customer-supplied encryption key or a
            customer-managed encryption key.

            This field is a member of `oneof`_ ``_disk_encryption_key``.
        physical_block_size_bytes (int):
            Optional. Physical block size of the
            persistent disk, in bytes. If not present in a
            request, a default value is used. Currently, the
            supported size is 4096.

            This field is a member of `oneof`_ ``_physical_block_size_bytes``.
        provisioned_iops (int):
            Optional. Indicates how many IOPS to
            provision for the disk. This sets the number of
            I/O operations per second that the disk can
            handle.

            This field is a member of `oneof`_ ``_provisioned_iops``.
        provisioned_throughput (int):
            Optional. Indicates how much throughput to
            provision for the disk. This sets the number of
            throughput MB per second that the disk can
            handle.

            This field is a member of `oneof`_ ``_provisioned_throughput``.
        enable_confidential_compute (bool):
            Optional. Indicates whether this disk is
            using confidential compute mode. Encryption with
            a Cloud KMS key is required to enable this
            option.

            This field is a member of `oneof`_ ``_enable_confidential_compute``.
        storage_pool (str):
            Optional. The storage pool in which the new
            disk is created. You can provide this as a
            partial or full URL to the resource.

            This field is a member of `oneof`_ ``_storage_pool``.
        access_mode (google.cloud.backupdr_v1.types.DiskRestoreProperties.AccessMode):
            Optional. The access mode of the disk.

            This field is a member of `oneof`_ ``_access_mode``.
        architecture (google.cloud.backupdr_v1.types.DiskRestoreProperties.Architecture):
            Optional. The architecture of the source disk. Valid values
            are ARM64 or X86_64.

            This field is a member of `oneof`_ ``_architecture``.
        resource_policy (MutableSequence[str]):
            Optional. Resource policies applied to this
            disk.
        type_ (str):
            Required. URL of the disk type resource
            describing which disk type to use to create the
            disk.

            This field is a member of `oneof`_ ``_type``.
        labels (MutableMapping[str, str]):
            Optional. Labels to apply to this disk. These
            can be modified later using
            <code>setLabels</code> method. Label values can
            be empty.
        resource_manager_tags (MutableMapping[str, str]):
            Optional. Resource manager tags to be bound
            to the disk.
    """

    class AccessMode(proto.Enum):
        r"""The supported access modes of the disk.

        Values:
            READ_WRITE_SINGLE (0):
                The default AccessMode, means the disk can be
                attached to single instance in RW mode.
            READ_WRITE_MANY (1):
                The AccessMode means the disk can be attached
                to multiple instances in RW mode.
            READ_ONLY_MANY (2):
                The AccessMode means the disk can be attached
                to multiple instances in RO mode.
        """

        READ_WRITE_SINGLE = 0
        READ_WRITE_MANY = 1
        READ_ONLY_MANY = 2

    class Architecture(proto.Enum):
        r"""Architecture of the source disk.

        Values:
            ARCHITECTURE_UNSPECIFIED (0):
                Default value. This value is unused.
            X86_64 (1):
                Disks with architecture X86_64
            ARM64 (2):
                Disks with architecture ARM64
        """

        ARCHITECTURE_UNSPECIFIED = 0
        X86_64 = 1
        ARM64 = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    size_gb: int = proto.Field(
        proto.INT64,
        number=3,
        optional=True,
    )
    licenses: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    guest_os_feature: MutableSequence[backupvault_gce.GuestOsFeature] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=5,
            message=backupvault_gce.GuestOsFeature,
        )
    )
    disk_encryption_key: backupvault_gce.CustomerEncryptionKey = proto.Field(
        proto.MESSAGE,
        number=6,
        optional=True,
        message=backupvault_gce.CustomerEncryptionKey,
    )
    physical_block_size_bytes: int = proto.Field(
        proto.INT64,
        number=7,
        optional=True,
    )
    provisioned_iops: int = proto.Field(
        proto.INT64,
        number=8,
        optional=True,
    )
    provisioned_throughput: int = proto.Field(
        proto.INT64,
        number=9,
        optional=True,
    )
    enable_confidential_compute: bool = proto.Field(
        proto.BOOL,
        number=10,
        optional=True,
    )
    storage_pool: str = proto.Field(
        proto.STRING,
        number=11,
        optional=True,
    )
    access_mode: AccessMode = proto.Field(
        proto.ENUM,
        number=12,
        optional=True,
        enum=AccessMode,
    )
    architecture: Architecture = proto.Field(
        proto.ENUM,
        number=14,
        optional=True,
        enum=Architecture,
    )
    resource_policy: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=15,
    )
    type_: str = proto.Field(
        proto.STRING,
        number=16,
        optional=True,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=17,
    )
    resource_manager_tags: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=18,
    )


class DiskBackupProperties(proto.Message):
    r"""DiskBackupProperties represents the properties of a Disk
    backup.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        description (str):
            A description of the source disk.

            This field is a member of `oneof`_ ``_description``.
        licenses (MutableSequence[str]):
            A list of publicly available licenses that
            are applicable to this backup. This is
            applicable if the original image had licenses
            attached, e.g. Windows image.
        guest_os_feature (MutableSequence[google.cloud.backupdr_v1.types.GuestOsFeature]):
            A list of guest OS features that are
            applicable to this backup.
        architecture (google.cloud.backupdr_v1.types.DiskBackupProperties.Architecture):
            The architecture of the source disk. Valid values are ARM64
            or X86_64.

            This field is a member of `oneof`_ ``_architecture``.
        type_ (str):
            The URL of the type of the disk.

            This field is a member of `oneof`_ ``_type``.
        size_gb (int):
            Size(in GB) of the source disk.

            This field is a member of `oneof`_ ``_size_gb``.
        region (str):
            Region and zone are mutually exclusive
            fields. The URL of the region of the source
            disk.

            This field is a member of `oneof`_ ``_region``.
        zone (str):
            The URL of the Zone where the source disk.

            This field is a member of `oneof`_ ``_zone``.
        replica_zones (MutableSequence[str]):
            The URL of the Zones where the source disk
            should be replicated.
        source_disk (str):
            The source disk used to create this backup.

            This field is a member of `oneof`_ ``_source_disk``.
    """

    class Architecture(proto.Enum):
        r"""Architecture of the source disk.

        Values:
            ARCHITECTURE_UNSPECIFIED (0):
                Default value. This value is unused.
            X86_64 (1):
                Disks with architecture X86_64
            ARM64 (2):
                Disks with architecture ARM64
        """

        ARCHITECTURE_UNSPECIFIED = 0
        X86_64 = 1
        ARM64 = 2

    description: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    licenses: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    guest_os_feature: MutableSequence[backupvault_gce.GuestOsFeature] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=3,
            message=backupvault_gce.GuestOsFeature,
        )
    )
    architecture: Architecture = proto.Field(
        proto.ENUM,
        number=4,
        optional=True,
        enum=Architecture,
    )
    type_: str = proto.Field(
        proto.STRING,
        number=5,
        optional=True,
    )
    size_gb: int = proto.Field(
        proto.INT64,
        number=6,
        optional=True,
    )
    region: str = proto.Field(
        proto.STRING,
        number=7,
        optional=True,
    )
    zone: str = proto.Field(
        proto.STRING,
        number=8,
        optional=True,
    )
    replica_zones: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=9,
    )
    source_disk: str = proto.Field(
        proto.STRING,
        number=10,
        optional=True,
    )


class DiskDataSourceProperties(proto.Message):
    r"""DiskDataSourceProperties represents the properties of a
    Disk resource that are stored in the DataSource.
    .

    Attributes:
        name (str):
            Name of the disk backed up by the datasource.
        description (str):
            The description of the disk.
        type_ (str):
            The type of the disk.
        size_gb (int):
            The size of the disk in GB.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    type_: str = proto.Field(
        proto.STRING,
        number=3,
    )
    size_gb: int = proto.Field(
        proto.INT64,
        number=4,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
