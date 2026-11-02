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

__protobuf__ = proto.module(
    package="google.cloud.backupdr.v1",
    manifest={
        "KeyRevocationActionType",
        "ComputeInstanceBackupProperties",
        "ComputeInstanceRestoreProperties",
        "ComputeInstanceTargetEnvironment",
        "ComputeInstanceDataSourceProperties",
        "AdvancedMachineFeatures",
        "ConfidentialInstanceConfig",
        "DisplayDevice",
        "AcceleratorConfig",
        "CustomerEncryptionKey",
        "Entry",
        "Metadata",
        "NetworkInterface",
        "NetworkPerformanceConfig",
        "AccessConfig",
        "AliasIpRange",
        "InstanceParams",
        "AllocationAffinity",
        "Scheduling",
        "SchedulingDuration",
        "ServiceAccount",
        "Tags",
        "AttachedDisk",
        "GuestOsFeature",
    },
)


class KeyRevocationActionType(proto.Enum):
    r"""Specifies whether the virtual machine instance will be shut
    down on key revocation. It is currently used in instance,
    instance properties and GMI protos

    Values:
        KEY_REVOCATION_ACTION_TYPE_UNSPECIFIED (0):
            Default value. This value is unused.
        NONE (1):
            Indicates user chose no operation.
        STOP (2):
            Indicates user chose to opt for VM shutdown
            on key revocation.
    """

    KEY_REVOCATION_ACTION_TYPE_UNSPECIFIED = 0
    NONE = 1
    STOP = 2


class ComputeInstanceBackupProperties(proto.Message):
    r"""ComputeInstanceBackupProperties represents Compute Engine
    instance backup properties.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        description (str):
            An optional text description for the
            instances that are created from these
            properties.

            This field is a member of `oneof`_ ``_description``.
        tags (google.cloud.backupdr_v1.types.Tags):
            A list of tags to apply to the instances that
            are created from these properties. The tags
            identify valid sources or targets for network
            firewalls. The setTags method can modify this
            list of tags. Each tag within the list must
            comply with RFC1035
            (https://www.ietf.org/rfc/rfc1035.txt).

            This field is a member of `oneof`_ ``_tags``.
        machine_type (str):
            The machine type to use for instances that
            are created from these properties.

            This field is a member of `oneof`_ ``_machine_type``.
        can_ip_forward (bool):
            Enables instances created based on these properties to send
            packets with source IP addresses other than their own and
            receive packets with destination IP addresses other than
            their own. If these instances will be used as an IP gateway
            or it will be set as the next-hop in a Route resource,
            specify ``true``. If unsure, leave this set to ``false``.
            See the
            https://cloud.google.com/vpc/docs/using-routes#canipforward
            documentation for more information.

            This field is a member of `oneof`_ ``_can_ip_forward``.
        network_interface (MutableSequence[google.cloud.backupdr_v1.types.NetworkInterface]):
            An array of network access configurations for
            this interface.
        disk (MutableSequence[google.cloud.backupdr_v1.types.AttachedDisk]):
            An array of disks that are associated with
            the instances that are created from these
            properties.
        metadata (google.cloud.backupdr_v1.types.Metadata):
            The metadata key/value pairs to assign to
            instances that are created from these
            properties. These pairs can consist of custom
            metadata or predefined keys. See
            https://cloud.google.com/compute/docs/metadata/overview
            for more information.

            This field is a member of `oneof`_ ``_metadata``.
        service_account (MutableSequence[google.cloud.backupdr_v1.types.ServiceAccount]):
            A list of service accounts with specified
            scopes. Access tokens for these service accounts
            are available to the instances that are created
            from these properties. Use metadata queries to
            obtain the access tokens for these instances.
        scheduling (google.cloud.backupdr_v1.types.Scheduling):
            Specifies the scheduling options for the
            instances that are created from these
            properties.

            This field is a member of `oneof`_ ``_scheduling``.
        guest_accelerator (MutableSequence[google.cloud.backupdr_v1.types.AcceleratorConfig]):
            A list of guest accelerator cards' type and
            count to use for instances created from these
            properties.
        min_cpu_platform (str):
            Minimum cpu/platform to be used by instances. The instance
            may be scheduled on the specified or newer cpu/platform.
            Applicable values are the friendly names of CPU platforms,
            such as ``minCpuPlatform: Intel Haswell`` or
            ``minCpuPlatform: Intel Sandy Bridge``. For more
            information, read
            https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform.

            This field is a member of `oneof`_ ``_min_cpu_platform``.
        key_revocation_action_type (google.cloud.backupdr_v1.types.KeyRevocationActionType):
            KeyRevocationActionType of the instance.
            Supported options are "STOP" and "NONE". The
            default value is "NONE" if it is not specified.

            This field is a member of `oneof`_ ``_key_revocation_action_type``.
        source_instance (str):
            The source instance used to create this
            backup. This can be a partial or full URL to the
            resource. For example, the following are valid
            values:

            -https://www.googleapis.com/compute/v1/projects/project/zones/zone/instances/instance
            -projects/project/zones/zone/instances/instance

            This field is a member of `oneof`_ ``_source_instance``.
        labels (MutableMapping[str, str]):
            Labels to apply to instances that are created
            from these properties.
    """

    description: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    tags: "Tags" = proto.Field(
        proto.MESSAGE,
        number=2,
        optional=True,
        message="Tags",
    )
    machine_type: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )
    can_ip_forward: bool = proto.Field(
        proto.BOOL,
        number=4,
        optional=True,
    )
    network_interface: MutableSequence["NetworkInterface"] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message="NetworkInterface",
    )
    disk: MutableSequence["AttachedDisk"] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message="AttachedDisk",
    )
    metadata: "Metadata" = proto.Field(
        proto.MESSAGE,
        number=7,
        optional=True,
        message="Metadata",
    )
    service_account: MutableSequence["ServiceAccount"] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message="ServiceAccount",
    )
    scheduling: "Scheduling" = proto.Field(
        proto.MESSAGE,
        number=9,
        optional=True,
        message="Scheduling",
    )
    guest_accelerator: MutableSequence["AcceleratorConfig"] = proto.RepeatedField(
        proto.MESSAGE,
        number=10,
        message="AcceleratorConfig",
    )
    min_cpu_platform: str = proto.Field(
        proto.STRING,
        number=11,
        optional=True,
    )
    key_revocation_action_type: "KeyRevocationActionType" = proto.Field(
        proto.ENUM,
        number=12,
        optional=True,
        enum="KeyRevocationActionType",
    )
    source_instance: str = proto.Field(
        proto.STRING,
        number=13,
        optional=True,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=14,
    )


class ComputeInstanceRestoreProperties(proto.Message):
    r"""ComputeInstanceRestoreProperties represents Compute Engine
    instance properties to be overridden during restore.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Required. Name of the compute instance.

            This field is a member of `oneof`_ ``_name``.
        advanced_machine_features (google.cloud.backupdr_v1.types.AdvancedMachineFeatures):
            Optional. Controls for advanced
            machine-related behavior features.

            This field is a member of `oneof`_ ``_advanced_machine_features``.
        can_ip_forward (bool):
            Optional. Allows this instance to send and
            receive packets with non-matching destination or
            source IPs.

            This field is a member of `oneof`_ ``_can_ip_forward``.
        confidential_instance_config (google.cloud.backupdr_v1.types.ConfidentialInstanceConfig):
            Optional. Controls Confidential compute
            options on the instance

            This field is a member of `oneof`_ ``_confidential_instance_config``.
        deletion_protection (bool):
            Optional. Whether the resource should be
            protected against deletion.

            This field is a member of `oneof`_ ``_deletion_protection``.
        description (str):
            Optional. An optional description of this
            resource. Provide this property when you create
            the resource.

            This field is a member of `oneof`_ ``_description``.
        disks (MutableSequence[google.cloud.backupdr_v1.types.AttachedDisk]):
            Optional. Array of disks associated with this
            instance. Persistent disks must be created
            before you can assign them. Source regional
            persistent disks will be restored with default
            replica zones if not specified.
        display_device (google.cloud.backupdr_v1.types.DisplayDevice):
            Optional. Enables display device for the
            instance.

            This field is a member of `oneof`_ ``_display_device``.
        guest_accelerators (MutableSequence[google.cloud.backupdr_v1.types.AcceleratorConfig]):
            Optional. A list of the type and count of
            accelerator cards attached to the instance.
        hostname (str):
            Optional. Specifies the hostname of the instance. The
            specified hostname must be RFC1035 compliant. If hostname is
            not specified, the default hostname is
            [INSTANCE_NAME].c.[PROJECT_ID].internal when using the
            global DNS, and
            [INSTANCE_NAME].[ZONE].c.[PROJECT_ID].internal when using
            zonal DNS.

            This field is a member of `oneof`_ ``_hostname``.
        instance_encryption_key (google.cloud.backupdr_v1.types.CustomerEncryptionKey):
            Optional. Encrypts suspended data for an
            instance with a customer-managed encryption key.

            This field is a member of `oneof`_ ``_instance_encryption_key``.
        key_revocation_action_type (google.cloud.backupdr_v1.types.KeyRevocationActionType):
            Optional. KeyRevocationActionType of the
            instance.

            This field is a member of `oneof`_ ``_key_revocation_action_type``.
        labels (MutableMapping[str, str]):
            Optional. Labels to apply to this instance.
        machine_type (str):
            Optional. Full or partial URL of the machine
            type resource to use for this instance.

            This field is a member of `oneof`_ ``_machine_type``.
        metadata (google.cloud.backupdr_v1.types.Metadata):
            Optional. This includes custom metadata and
            predefined keys.

            This field is a member of `oneof`_ ``_metadata``.
        min_cpu_platform (str):
            Optional. Minimum CPU platform to use for
            this instance.

            This field is a member of `oneof`_ ``_min_cpu_platform``.
        network_interfaces (MutableSequence[google.cloud.backupdr_v1.types.NetworkInterface]):
            Optional. An array of network configurations
            for this instance. These specify how interfaces
            are configured to interact with other network
            services, such as connecting to the internet.
            Multiple interfaces are supported per instance.
            Required to restore in different project or
            region.
        network_performance_config (google.cloud.backupdr_v1.types.NetworkPerformanceConfig):
            Optional. Configure network performance such
            as egress bandwidth tier.

            This field is a member of `oneof`_ ``_network_performance_config``.
        params (google.cloud.backupdr_v1.types.InstanceParams):
            Input only. Additional params passed with the
            request, but not persisted as part of resource
            payload.

            This field is a member of `oneof`_ ``_params``.
        private_ipv6_google_access (google.cloud.backupdr_v1.types.ComputeInstanceRestoreProperties.InstancePrivateIpv6GoogleAccess):
            Optional. The private IPv6 google access type for the VM. If
            not specified, use INHERIT_FROM_SUBNETWORK as default.

            This field is a member of `oneof`_ ``_private_ipv6_google_access``.
        allocation_affinity (google.cloud.backupdr_v1.types.AllocationAffinity):
            Optional. Specifies the reservations that
            this instance can consume from.

            This field is a member of `oneof`_ ``_allocation_affinity``.
        resource_policies (MutableSequence[str]):
            Optional. Resource policies applied to this
            instance. By default, no resource policies will
            be applied.
        scheduling (google.cloud.backupdr_v1.types.Scheduling):
            Optional. Sets the scheduling options for
            this instance.

            This field is a member of `oneof`_ ``_scheduling``.
        service_accounts (MutableSequence[google.cloud.backupdr_v1.types.ServiceAccount]):
            Optional. A list of service accounts, with
            their specified scopes, authorized for this
            instance. Only one service account per VM
            instance is supported.
        tags (google.cloud.backupdr_v1.types.Tags):
            Optional. Tags to apply to this instance.
            Tags are used to identify valid sources or
            targets for network firewalls and are specified
            by the client during instance creation.

            This field is a member of `oneof`_ ``_tags``.
    """

    class InstancePrivateIpv6GoogleAccess(proto.Enum):
        r"""The private IPv6 google access type for the VMs.

        Values:
            INSTANCE_PRIVATE_IPV6_GOOGLE_ACCESS_UNSPECIFIED (0):
                Default value. This value is unused.
            INHERIT_FROM_SUBNETWORK (1):
                Each network interface inherits
                PrivateIpv6GoogleAccess from its subnetwork.
            ENABLE_OUTBOUND_VM_ACCESS_TO_GOOGLE (2):
                Outbound private IPv6 access from VMs in this
                subnet to Google services. If specified, the
                subnetwork who is attached to the instance's
                default network interface will be assigned an
                internal IPv6 prefix if it doesn't have before.
            ENABLE_BIDIRECTIONAL_ACCESS_TO_GOOGLE (3):
                Bidirectional private IPv6 access to/from
                Google services. If specified, the subnetwork
                who is attached to the instance's default
                network interface will be assigned an internal
                IPv6 prefix if it doesn't have before.
        """

        INSTANCE_PRIVATE_IPV6_GOOGLE_ACCESS_UNSPECIFIED = 0
        INHERIT_FROM_SUBNETWORK = 1
        ENABLE_OUTBOUND_VM_ACCESS_TO_GOOGLE = 2
        ENABLE_BIDIRECTIONAL_ACCESS_TO_GOOGLE = 3

    name: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    advanced_machine_features: "AdvancedMachineFeatures" = proto.Field(
        proto.MESSAGE,
        number=2,
        optional=True,
        message="AdvancedMachineFeatures",
    )
    can_ip_forward: bool = proto.Field(
        proto.BOOL,
        number=3,
        optional=True,
    )
    confidential_instance_config: "ConfidentialInstanceConfig" = proto.Field(
        proto.MESSAGE,
        number=4,
        optional=True,
        message="ConfidentialInstanceConfig",
    )
    deletion_protection: bool = proto.Field(
        proto.BOOL,
        number=5,
        optional=True,
    )
    description: str = proto.Field(
        proto.STRING,
        number=6,
        optional=True,
    )
    disks: MutableSequence["AttachedDisk"] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message="AttachedDisk",
    )
    display_device: "DisplayDevice" = proto.Field(
        proto.MESSAGE,
        number=8,
        optional=True,
        message="DisplayDevice",
    )
    guest_accelerators: MutableSequence["AcceleratorConfig"] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message="AcceleratorConfig",
    )
    hostname: str = proto.Field(
        proto.STRING,
        number=10,
        optional=True,
    )
    instance_encryption_key: "CustomerEncryptionKey" = proto.Field(
        proto.MESSAGE,
        number=11,
        optional=True,
        message="CustomerEncryptionKey",
    )
    key_revocation_action_type: "KeyRevocationActionType" = proto.Field(
        proto.ENUM,
        number=12,
        optional=True,
        enum="KeyRevocationActionType",
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=13,
    )
    machine_type: str = proto.Field(
        proto.STRING,
        number=14,
        optional=True,
    )
    metadata: "Metadata" = proto.Field(
        proto.MESSAGE,
        number=15,
        optional=True,
        message="Metadata",
    )
    min_cpu_platform: str = proto.Field(
        proto.STRING,
        number=16,
        optional=True,
    )
    network_interfaces: MutableSequence["NetworkInterface"] = proto.RepeatedField(
        proto.MESSAGE,
        number=17,
        message="NetworkInterface",
    )
    network_performance_config: "NetworkPerformanceConfig" = proto.Field(
        proto.MESSAGE,
        number=18,
        optional=True,
        message="NetworkPerformanceConfig",
    )
    params: "InstanceParams" = proto.Field(
        proto.MESSAGE,
        number=19,
        optional=True,
        message="InstanceParams",
    )
    private_ipv6_google_access: InstancePrivateIpv6GoogleAccess = proto.Field(
        proto.ENUM,
        number=20,
        optional=True,
        enum=InstancePrivateIpv6GoogleAccess,
    )
    allocation_affinity: "AllocationAffinity" = proto.Field(
        proto.MESSAGE,
        number=21,
        optional=True,
        message="AllocationAffinity",
    )
    resource_policies: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=22,
    )
    scheduling: "Scheduling" = proto.Field(
        proto.MESSAGE,
        number=23,
        optional=True,
        message="Scheduling",
    )
    service_accounts: MutableSequence["ServiceAccount"] = proto.RepeatedField(
        proto.MESSAGE,
        number=24,
        message="ServiceAccount",
    )
    tags: "Tags" = proto.Field(
        proto.MESSAGE,
        number=26,
        optional=True,
        message="Tags",
    )


class ComputeInstanceTargetEnvironment(proto.Message):
    r"""ComputeInstanceTargetEnvironment represents Compute Engine
    target environment to be used during restore.

    Attributes:
        project (str):
            Required. Target project for the Compute
            Engine instance.
        zone (str):
            Required. The zone of the Compute Engine
            instance.
    """

    project: str = proto.Field(
        proto.STRING,
        number=1,
    )
    zone: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ComputeInstanceDataSourceProperties(proto.Message):
    r"""ComputeInstanceDataSourceProperties represents the properties
    of a ComputeEngine resource that are stored in the DataSource.

    Attributes:
        name (str):
            Name of the compute instance backed up by the
            datasource.
        description (str):
            The description of the Compute Engine
            instance.
        machine_type (str):
            The machine type of the instance.
        total_disk_count (int):
            The total number of disks attached to the
            Instance.
        total_disk_size_gb (int):
            The sum of all the disk sizes.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    machine_type: str = proto.Field(
        proto.STRING,
        number=3,
    )
    total_disk_count: int = proto.Field(
        proto.INT64,
        number=4,
    )
    total_disk_size_gb: int = proto.Field(
        proto.INT64,
        number=5,
    )


class AdvancedMachineFeatures(proto.Message):
    r"""Specifies options for controlling advanced machine features.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        enable_nested_virtualization (bool):
            Optional. Whether to enable nested
            virtualization or not (default is false).

            This field is a member of `oneof`_ ``_enable_nested_virtualization``.
        threads_per_core (int):
            Optional. The number of threads per physical
            core. To disable simultaneous multithreading
            (SMT) set this to 1. If unset, the maximum
            number of threads supported per core by the
            underlying processor is assumed.

            This field is a member of `oneof`_ ``_threads_per_core``.
        visible_core_count (int):
            Optional. The number of physical cores to
            expose to an instance. Multiply by the number of
            threads per core to compute the total number of
            virtual CPUs to expose to the instance. If
            unset, the number of cores is inferred from the
            instance's nominal CPU count and the underlying
            platform's SMT width.

            This field is a member of `oneof`_ ``_visible_core_count``.
        enable_uefi_networking (bool):
            Optional. Whether to enable UEFI networking
            for instance creation.

            This field is a member of `oneof`_ ``_enable_uefi_networking``.
    """

    enable_nested_virtualization: bool = proto.Field(
        proto.BOOL,
        number=1,
        optional=True,
    )
    threads_per_core: int = proto.Field(
        proto.INT32,
        number=2,
        optional=True,
    )
    visible_core_count: int = proto.Field(
        proto.INT32,
        number=3,
        optional=True,
    )
    enable_uefi_networking: bool = proto.Field(
        proto.BOOL,
        number=4,
        optional=True,
    )


class ConfidentialInstanceConfig(proto.Message):
    r"""A set of Confidential Instance options.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        enable_confidential_compute (bool):
            Optional. Defines whether the instance should
            have confidential compute enabled.

            This field is a member of `oneof`_ ``_enable_confidential_compute``.
    """

    enable_confidential_compute: bool = proto.Field(
        proto.BOOL,
        number=1,
        optional=True,
    )


class DisplayDevice(proto.Message):
    r"""A set of Display Device options

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        enable_display (bool):
            Optional. Enables display for the Compute
            Engine VM

            This field is a member of `oneof`_ ``_enable_display``.
    """

    enable_display: bool = proto.Field(
        proto.BOOL,
        number=1,
        optional=True,
    )


class AcceleratorConfig(proto.Message):
    r"""A specification of the type and number of accelerator cards
    attached to the instance.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        accelerator_type (str):
            Optional. Full or partial URL of the
            accelerator type resource to attach to this
            instance.

            This field is a member of `oneof`_ ``_accelerator_type``.
        accelerator_count (int):
            Optional. The number of the guest accelerator
            cards exposed to this instance.

            This field is a member of `oneof`_ ``_accelerator_count``.
    """

    accelerator_type: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    accelerator_count: int = proto.Field(
        proto.INT32,
        number=2,
        optional=True,
    )


class CustomerEncryptionKey(proto.Message):
    r"""A customer-supplied encryption key.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        raw_key (str):
            Optional. Specifies a 256-bit
            customer-supplied encryption key.

            This field is a member of `oneof`_ ``key``.
        rsa_encrypted_key (str):
            Optional. RSA-wrapped 2048-bit
            customer-supplied encryption key to either
            encrypt or decrypt this resource.

            This field is a member of `oneof`_ ``key``.
        kms_key_name (str):
            Optional. The name of the encryption key that
            is stored in Google Cloud KMS.

            This field is a member of `oneof`_ ``key``.
        kms_key_service_account (str):
            Optional. The service account being used for
            the encryption request for the given KMS key. If
            absent, the Compute Engine default service
            account is used.

            This field is a member of `oneof`_ ``_kms_key_service_account``.
    """

    raw_key: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="key",
    )
    rsa_encrypted_key: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="key",
    )
    kms_key_name: str = proto.Field(
        proto.STRING,
        number=3,
        oneof="key",
    )
    kms_key_service_account: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )


class Entry(proto.Message):
    r"""A key/value pair to be used for storing metadata.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        key (str):
            Optional. Key for the metadata entry.

            This field is a member of `oneof`_ ``_key``.
        value (str):
            Optional. Value for the metadata entry. These
            are free-form strings, and only have meaning as
            interpreted by the image running in the
            instance. The only restriction placed on values
            is that their size must be less than or equal to
            262144 bytes (256 KiB).

            This field is a member of `oneof`_ ``_value``.
    """

    key: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    value: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )


class Metadata(proto.Message):
    r"""A metadata key/value entry.

    Attributes:
        items (MutableSequence[google.cloud.backupdr_v1.types.Entry]):
            Optional. Array of key/value pairs. The total
            size of all keys and values must be less than
            512 KB.
    """

    items: MutableSequence["Entry"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Entry",
    )


class NetworkInterface(proto.Message):
    r"""A network interface resource attached to an instance.
    s


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        network (str):
            Optional. URL of the VPC network resource for
            this instance.

            This field is a member of `oneof`_ ``_network``.
        subnetwork (str):
            Optional. The URL of the Subnetwork resource
            for this instance.

            This field is a member of `oneof`_ ``_subnetwork``.
        ip_address (str):
            Optional. An IPv4 internal IP address to
            assign to the instance for this network
            interface. If not specified by the user, an
            unused internal IP is assigned by the system.

            This field is a member of `oneof`_ ``_ip_address``.
        ipv6_address (str):
            Optional. An IPv6 internal network address
            for this network interface. To use a static
            internal IP address, it must be unused and in
            the same region as the instance's zone. If not
            specified, Google Cloud will automatically
            assign an internal IPv6 address from the
            instance's subnetwork.

            This field is a member of `oneof`_ ``_ipv6_address``.
        internal_ipv6_prefix_length (int):
            Optional. The prefix length of the primary
            internal IPv6 range.

            This field is a member of `oneof`_ ``_internal_ipv6_prefix_length``.
        name (str):
            Output only. [Output Only] The name of the network
            interface, which is generated by the server.

            This field is a member of `oneof`_ ``_name``.
        access_configs (MutableSequence[google.cloud.backupdr_v1.types.AccessConfig]):
            Optional. An array of configurations for this interface.
            Currently, only one access config,ONE_TO_ONE_NAT is
            supported. If there are no accessConfigs specified, then
            this instance will have no external internet access.
        ipv6_access_configs (MutableSequence[google.cloud.backupdr_v1.types.AccessConfig]):
            Optional. An array of IPv6 access configurations for this
            interface. Currently, only one IPv6 access config,
            DIRECT_IPV6, is supported. If there is no ipv6AccessConfig
            specified, then this instance will have no external IPv6
            Internet access.
        alias_ip_ranges (MutableSequence[google.cloud.backupdr_v1.types.AliasIpRange]):
            Optional. An array of alias IP ranges for
            this network interface. You can only specify
            this field for network interfaces in VPC
            networks.
        stack_type (google.cloud.backupdr_v1.types.NetworkInterface.StackType):
            The stack type for this network interface.

            This field is a member of `oneof`_ ``_stack_type``.
        ipv6_access_type (google.cloud.backupdr_v1.types.NetworkInterface.Ipv6AccessType):
            Optional. [Output Only] One of EXTERNAL, INTERNAL to
            indicate whether the IP can be accessed from the Internet.
            This field is always inherited from its subnetwork.

            This field is a member of `oneof`_ ``_ipv6_access_type``.
        queue_count (int):
            Optional. The networking queue count that's
            specified by users for the network interface.
            Both Rx and Tx queues will be set to this
            number. It'll be empty if not specified by the
            users.

            This field is a member of `oneof`_ ``_queue_count``.
        nic_type (google.cloud.backupdr_v1.types.NetworkInterface.NicType):
            Optional. The type of vNIC to be used on this
            interface. This may be gVNIC or VirtioNet.

            This field is a member of `oneof`_ ``_nic_type``.
        network_attachment (str):
            Optional. The URL of the network attachment that this
            interface should connect to in the following format:
            projects/{project_number}/regions/{region_name}/networkAttachments/{network_attachment_name}.

            This field is a member of `oneof`_ ``_network_attachment``.
    """

    class StackType(proto.Enum):
        r"""Stack type for this network interface.

        Values:
            STACK_TYPE_UNSPECIFIED (0):
                Default should be STACK_TYPE_UNSPECIFIED.
            IPV4_ONLY (1):
                The network interface will be assigned IPv4
                address.
            IPV4_IPV6 (2):
                The network interface can have both IPv4 and
                IPv6 addresses.
        """

        STACK_TYPE_UNSPECIFIED = 0
        IPV4_ONLY = 1
        IPV4_IPV6 = 2

    class Ipv6AccessType(proto.Enum):
        r"""IPv6 access type for this network interface.

        Values:
            UNSPECIFIED_IPV6_ACCESS_TYPE (0):
                IPv6 access type not set. Means this network
                interface hasn't been turned on IPv6 yet.
            INTERNAL (1):
                This network interface can have internal
                IPv6.
            EXTERNAL (2):
                This network interface can have external
                IPv6.
        """

        UNSPECIFIED_IPV6_ACCESS_TYPE = 0
        INTERNAL = 1
        EXTERNAL = 2

    class NicType(proto.Enum):
        r"""Nic type for this network interface.

        Values:
            NIC_TYPE_UNSPECIFIED (0):
                Default should be NIC_TYPE_UNSPECIFIED.
            VIRTIO_NET (1):
                VIRTIO
            GVNIC (2):
                GVNIC
        """

        NIC_TYPE_UNSPECIFIED = 0
        VIRTIO_NET = 1
        GVNIC = 2

    network: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    subnetwork: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    ip_address: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )
    ipv6_address: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )
    internal_ipv6_prefix_length: int = proto.Field(
        proto.INT32,
        number=5,
        optional=True,
    )
    name: str = proto.Field(
        proto.STRING,
        number=6,
        optional=True,
    )
    access_configs: MutableSequence["AccessConfig"] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message="AccessConfig",
    )
    ipv6_access_configs: MutableSequence["AccessConfig"] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message="AccessConfig",
    )
    alias_ip_ranges: MutableSequence["AliasIpRange"] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message="AliasIpRange",
    )
    stack_type: StackType = proto.Field(
        proto.ENUM,
        number=10,
        optional=True,
        enum=StackType,
    )
    ipv6_access_type: Ipv6AccessType = proto.Field(
        proto.ENUM,
        number=11,
        optional=True,
        enum=Ipv6AccessType,
    )
    queue_count: int = proto.Field(
        proto.INT32,
        number=12,
        optional=True,
    )
    nic_type: NicType = proto.Field(
        proto.ENUM,
        number=13,
        optional=True,
        enum=NicType,
    )
    network_attachment: str = proto.Field(
        proto.STRING,
        number=14,
        optional=True,
    )


class NetworkPerformanceConfig(proto.Message):
    r"""Network performance configuration.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        total_egress_bandwidth_tier (google.cloud.backupdr_v1.types.NetworkPerformanceConfig.Tier):
            Optional. The tier of the total egress
            bandwidth.

            This field is a member of `oneof`_ ``_total_egress_bandwidth_tier``.
    """

    class Tier(proto.Enum):
        r"""Network performance tier.

        Values:
            TIER_UNSPECIFIED (0):
                This value is unused.
            DEFAULT (1):
                Default network performance config.
            TIER_1 (2):
                Tier 1 network performance config.
        """

        TIER_UNSPECIFIED = 0
        DEFAULT = 1
        TIER_1 = 2

    total_egress_bandwidth_tier: Tier = proto.Field(
        proto.ENUM,
        number=1,
        optional=True,
        enum=Tier,
    )


class AccessConfig(proto.Message):
    r"""An access configuration attached to an instance's network
    interface. Only one access config per instance is supported.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        type_ (google.cloud.backupdr_v1.types.AccessConfig.AccessType):
            Optional. In accessConfigs (IPv4), the default and only
            option is ONE_TO_ONE_NAT. In ipv6AccessConfigs, the default
            and only option is DIRECT_IPV6.

            This field is a member of `oneof`_ ``_type``.
        name (str):
            Optional. The name of this access
            configuration.

            This field is a member of `oneof`_ ``_name``.
        external_ip (str):
            Optional. The external IP address of this
            access configuration.

            This field is a member of `oneof`_ ``_external_ip``.
        external_ipv6 (str):
            Optional. The external IPv6 address of this
            access configuration.

            This field is a member of `oneof`_ ``_external_ipv6``.
        external_ipv6_prefix_length (int):
            Optional. The prefix length of the external
            IPv6 range.

            This field is a member of `oneof`_ ``_external_ipv6_prefix_length``.
        set_public_ptr (bool):
            Optional. Specifies whether a public DNS
            'PTR' record should be created to map the
            external IP address of the instance to a DNS
            domain name.

            This field is a member of `oneof`_ ``_set_public_ptr``.
        public_ptr_domain_name (str):
            Optional. The DNS domain name for the public
            PTR record.

            This field is a member of `oneof`_ ``_public_ptr_domain_name``.
        network_tier (google.cloud.backupdr_v1.types.AccessConfig.NetworkTier):
            Optional. This signifies the networking tier
            used for configuring this access

            This field is a member of `oneof`_ ``_network_tier``.
    """

    class AccessType(proto.Enum):
        r"""The type of configuration.

        Values:
            ACCESS_TYPE_UNSPECIFIED (0):
                Default value. This value is unused.
            ONE_TO_ONE_NAT (1):
                ONE_TO_ONE_NAT
            DIRECT_IPV6 (2):
                Direct IPv6 access.
        """

        ACCESS_TYPE_UNSPECIFIED = 0
        ONE_TO_ONE_NAT = 1
        DIRECT_IPV6 = 2

    class NetworkTier(proto.Enum):
        r"""Network tier property used by addresses, instances and
        forwarding rules.

        Values:
            NETWORK_TIER_UNSPECIFIED (0):
                Default value. This value is unused.
            PREMIUM (1):
                High quality, Google-grade network tier,
                support for all networking products.
            STANDARD (2):
                Public internet quality, only limited support
                for other networking products.
        """

        NETWORK_TIER_UNSPECIFIED = 0
        PREMIUM = 1
        STANDARD = 2

    type_: AccessType = proto.Field(
        proto.ENUM,
        number=1,
        optional=True,
        enum=AccessType,
    )
    name: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    external_ip: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )
    external_ipv6: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )
    external_ipv6_prefix_length: int = proto.Field(
        proto.INT32,
        number=5,
        optional=True,
    )
    set_public_ptr: bool = proto.Field(
        proto.BOOL,
        number=6,
        optional=True,
    )
    public_ptr_domain_name: str = proto.Field(
        proto.STRING,
        number=7,
        optional=True,
    )
    network_tier: NetworkTier = proto.Field(
        proto.ENUM,
        number=8,
        optional=True,
        enum=NetworkTier,
    )


class AliasIpRange(proto.Message):
    r"""An alias IP range attached to an instance's network
    interface.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        ip_cidr_range (str):
            Optional. The IP alias ranges to allocate for
            this interface.

            This field is a member of `oneof`_ ``_ip_cidr_range``.
        subnetwork_range_name (str):
            Optional. The name of a subnetwork secondary
            IP range from which to allocate an IP alias
            range. If not specified, the primary range of
            the subnetwork is used.

            This field is a member of `oneof`_ ``_subnetwork_range_name``.
    """

    ip_cidr_range: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    subnetwork_range_name: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )


class InstanceParams(proto.Message):
    r"""Additional instance params.

    Attributes:
        resource_manager_tags (MutableMapping[str, str]):
            Optional. Resource manager tags to be bound
            to the instance.
    """

    resource_manager_tags: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=1,
    )


class AllocationAffinity(proto.Message):
    r"""Specifies the reservations that this instance can consume
    from.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        consume_allocation_type (google.cloud.backupdr_v1.types.AllocationAffinity.Type):
            Optional. Specifies the type of reservation
            from which this instance can consume

            This field is a member of `oneof`_ ``_consume_allocation_type``.
        key (str):
            Optional. Corresponds to the label key of a
            reservation resource.

            This field is a member of `oneof`_ ``_key``.
        values (MutableSequence[str]):
            Optional. Corresponds to the label values of
            a reservation resource.
    """

    class Type(proto.Enum):
        r"""Indicates whether to consume from a reservation or not.

        Values:
            TYPE_UNSPECIFIED (0):
                Default value. This value is unused.
            NO_RESERVATION (1):
                Do not consume from any allocated capacity.
            ANY_RESERVATION (2):
                Consume any allocation available.
            SPECIFIC_RESERVATION (3):
                Must consume from a specific reservation.
                Must specify key value fields for specifying the
                reservations.
        """

        TYPE_UNSPECIFIED = 0
        NO_RESERVATION = 1
        ANY_RESERVATION = 2
        SPECIFIC_RESERVATION = 3

    consume_allocation_type: Type = proto.Field(
        proto.ENUM,
        number=1,
        optional=True,
        enum=Type,
    )
    key: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    values: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class Scheduling(proto.Message):
    r"""Sets the scheduling options for an Instance.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        on_host_maintenance (google.cloud.backupdr_v1.types.Scheduling.OnHostMaintenance):
            Optional. Defines the maintenance behavior
            for this instance.

            This field is a member of `oneof`_ ``_on_host_maintenance``.
        automatic_restart (bool):
            Optional. Specifies whether the instance
            should be automatically restarted if it is
            terminated by Compute Engine (not terminated by
            a user).

            This field is a member of `oneof`_ ``_automatic_restart``.
        preemptible (bool):
            Optional. Defines whether the instance is
            preemptible.

            This field is a member of `oneof`_ ``_preemptible``.
        node_affinities (MutableSequence[google.cloud.backupdr_v1.types.Scheduling.NodeAffinity]):
            Optional. A set of node affinity and
            anti-affinity configurations. Overrides
            reservationAffinity.
        min_node_cpus (int):
            Optional. The minimum number of virtual CPUs
            this instance will consume when running on a
            sole-tenant node.

            This field is a member of `oneof`_ ``_min_node_cpus``.
        provisioning_model (google.cloud.backupdr_v1.types.Scheduling.ProvisioningModel):
            Optional. Specifies the provisioning model of
            the instance.

            This field is a member of `oneof`_ ``_provisioning_model``.
        instance_termination_action (google.cloud.backupdr_v1.types.Scheduling.InstanceTerminationAction):
            Optional. Specifies the termination action
            for the instance.

            This field is a member of `oneof`_ ``_instance_termination_action``.
        local_ssd_recovery_timeout (google.cloud.backupdr_v1.types.SchedulingDuration):
            Optional. Specifies the maximum amount of
            time a Local Ssd Vm should wait while recovery
            of the Local Ssd state is attempted. Its value
            should be in between 0 and 168 hours with hour
            granularity and the default value being 1 hour.

            This field is a member of `oneof`_ ``_local_ssd_recovery_timeout``.
    """

    class OnHostMaintenance(proto.Enum):
        r"""Defines the maintenance behavior for this instance=

        Values:
            ON_HOST_MAINTENANCE_UNSPECIFIED (0):
                Default value. This value is unused.
            TERMINATE (1):
                Tells Compute Engine to terminate and
                (optionally) restart the instance away from the
                maintenance activity.
            MIGRATE (1000):
                Default, Allows Compute Engine to
                automatically migrate instances out of the way
                of maintenance events.
        """

        ON_HOST_MAINTENANCE_UNSPECIFIED = 0
        TERMINATE = 1
        MIGRATE = 1000

    class ProvisioningModel(proto.Enum):
        r"""Defines the provisioning model for an instance.

        Values:
            PROVISIONING_MODEL_UNSPECIFIED (0):
                Default value. This value is not used.
            STANDARD (1):
                Standard provisioning with user controlled
                runtime, no discounts.
            SPOT (2):
                Heavily discounted, no guaranteed runtime.
        """

        PROVISIONING_MODEL_UNSPECIFIED = 0
        STANDARD = 1
        SPOT = 2

    class InstanceTerminationAction(proto.Enum):
        r"""Defines the supported termination actions for an instance.

        Values:
            INSTANCE_TERMINATION_ACTION_UNSPECIFIED (0):
                Default value. This value is unused.
            DELETE (1):
                Delete the VM.
            STOP (2):
                Stop the VM without storing in-memory
                content. default action.
        """

        INSTANCE_TERMINATION_ACTION_UNSPECIFIED = 0
        DELETE = 1
        STOP = 2

    class NodeAffinity(proto.Message):
        r"""Node Affinity: the configuration of desired nodes onto which
        this Instance could be scheduled.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            key (str):
                Optional. Corresponds to the label key of
                Node resource.

                This field is a member of `oneof`_ ``_key``.
            operator (google.cloud.backupdr_v1.types.Scheduling.NodeAffinity.Operator):
                Optional. Defines the operation of node
                selection.

                This field is a member of `oneof`_ ``_operator``.
            values (MutableSequence[str]):
                Optional. Corresponds to the label values of
                Node resource.
        """

        class Operator(proto.Enum):
            r"""Defines the type of node selections.

            Values:
                OPERATOR_UNSPECIFIED (0):
                    Default value. This value is unused.
                IN (1):
                    Requires Compute Engine to seek for matched
                    nodes.
                NOT_IN (2):
                    Requires Compute Engine to avoid certain
                    nodes.
            """

            OPERATOR_UNSPECIFIED = 0
            IN = 1
            NOT_IN = 2

        key: str = proto.Field(
            proto.STRING,
            number=1,
            optional=True,
        )
        operator: "Scheduling.NodeAffinity.Operator" = proto.Field(
            proto.ENUM,
            number=2,
            optional=True,
            enum="Scheduling.NodeAffinity.Operator",
        )
        values: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=3,
        )

    on_host_maintenance: OnHostMaintenance = proto.Field(
        proto.ENUM,
        number=1,
        optional=True,
        enum=OnHostMaintenance,
    )
    automatic_restart: bool = proto.Field(
        proto.BOOL,
        number=2,
        optional=True,
    )
    preemptible: bool = proto.Field(
        proto.BOOL,
        number=3,
        optional=True,
    )
    node_affinities: MutableSequence[NodeAffinity] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=NodeAffinity,
    )
    min_node_cpus: int = proto.Field(
        proto.INT32,
        number=5,
        optional=True,
    )
    provisioning_model: ProvisioningModel = proto.Field(
        proto.ENUM,
        number=6,
        optional=True,
        enum=ProvisioningModel,
    )
    instance_termination_action: InstanceTerminationAction = proto.Field(
        proto.ENUM,
        number=7,
        optional=True,
        enum=InstanceTerminationAction,
    )
    local_ssd_recovery_timeout: "SchedulingDuration" = proto.Field(
        proto.MESSAGE,
        number=10,
        optional=True,
        message="SchedulingDuration",
    )


class SchedulingDuration(proto.Message):
    r"""A SchedulingDuration represents a fixed-length span of time
    represented as a count of seconds and fractions of seconds at
    nanosecond resolution. It is independent of any calendar and
    concepts like "day" or "month". Range is approximately 10,000
    years.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        seconds (int):
            Optional. Span of time at a resolution of a
            second.

            This field is a member of `oneof`_ ``_seconds``.
        nanos (int):
            Optional. Span of time that's a fraction of a
            second at nanosecond resolution.

            This field is a member of `oneof`_ ``_nanos``.
    """

    seconds: int = proto.Field(
        proto.INT64,
        number=1,
        optional=True,
    )
    nanos: int = proto.Field(
        proto.INT32,
        number=2,
        optional=True,
    )


class ServiceAccount(proto.Message):
    r"""A service account.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        email (str):
            Optional. Email address of the service
            account.

            This field is a member of `oneof`_ ``_email``.
        scopes (MutableSequence[str]):
            Optional. The list of scopes to be made
            available for this service account.
    """

    email: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    scopes: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class Tags(proto.Message):
    r"""A set of instance tags.

    Attributes:
        items (MutableSequence[str]):
            Optional. An array of tags. Each tag must be
            1-63 characters long, and comply with RFC1035.
    """

    items: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class AttachedDisk(proto.Message):
    r"""An instance-attached disk resource.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        initialize_params (google.cloud.backupdr_v1.types.AttachedDisk.InitializeParams):
            Optional. Specifies the parameters to
            initialize this disk.

            This field is a member of `oneof`_ ``_initialize_params``.
        device_name (str):
            Optional. This is used as an identifier for the disks. This
            is the unique name has to provided to modify disk parameters
            like disk_name and replica_zones (in case of RePDs)

            This field is a member of `oneof`_ ``_device_name``.
        kind (str):
            Optional. Type of the resource.

            This field is a member of `oneof`_ ``_kind``.
        disk_type_deprecated (google.cloud.backupdr_v1.types.AttachedDisk.DiskType):
            Specifies the type of the disk.

            This field is a member of `oneof`_ ``_disk_type_deprecated``.
        mode (google.cloud.backupdr_v1.types.AttachedDisk.DiskMode):
            Optional. The mode in which to attach this
            disk.

            This field is a member of `oneof`_ ``_mode``.
        source (str):
            Optional. Specifies a valid partial or full
            URL to an existing Persistent Disk resource.

            This field is a member of `oneof`_ ``_source``.
        index (int):
            Optional. A zero-based index to this disk,
            where 0 is reserved for the boot disk.

            This field is a member of `oneof`_ ``_index``.
        boot (bool):
            Optional. Indicates that this is a boot disk.
            The virtual machine will use the first partition
            of the disk for its root filesystem.

            This field is a member of `oneof`_ ``_boot``.
        auto_delete (bool):
            Optional. Specifies whether the disk will be
            auto-deleted when the instance is deleted (but
            not when the disk is detached from the
            instance).

            This field is a member of `oneof`_ ``_auto_delete``.
        license_ (MutableSequence[str]):
            Optional. Any valid publicly visible
            licenses.
        disk_interface (google.cloud.backupdr_v1.types.AttachedDisk.DiskInterface):
            Optional. Specifies the disk interface to use
            for attaching this disk.

            This field is a member of `oneof`_ ``_disk_interface``.
        guest_os_feature (MutableSequence[google.cloud.backupdr_v1.types.GuestOsFeature]):
            Optional. A list of features to enable on the
            guest operating system. Applicable only for
            bootable images.
        disk_encryption_key (google.cloud.backupdr_v1.types.CustomerEncryptionKey):
            Optional. Encrypts or decrypts a disk using a
            customer-supplied encryption key.

            This field is a member of `oneof`_ ``_disk_encryption_key``.
        disk_size_gb (int):
            Optional. The size of the disk in GB.

            This field is a member of `oneof`_ ``_disk_size_gb``.
        saved_state (google.cloud.backupdr_v1.types.AttachedDisk.DiskSavedState):
            Optional. Output only. The state of the disk.

            This field is a member of `oneof`_ ``_saved_state``.
        disk_type (str):
            Optional. Output only. The URI of the disk
            type resource. For example:
            projects/project/zones/zone/diskTypes/pd-standard
            or pd-ssd

            This field is a member of `oneof`_ ``_disk_type``.
        type_ (google.cloud.backupdr_v1.types.AttachedDisk.DiskType):
            Optional. Specifies the type of the disk.

            This field is a member of `oneof`_ ``_type``.
    """

    class DiskType(proto.Enum):
        r"""List of the Disk Types.

        Values:
            DISK_TYPE_UNSPECIFIED (0):
                Default value, which is unused.
            SCRATCH (1):
                A scratch disk type.
            PERSISTENT (2):
                A persistent disk type.
        """

        DISK_TYPE_UNSPECIFIED = 0
        SCRATCH = 1
        PERSISTENT = 2

    class DiskMode(proto.Enum):
        r"""List of the Disk Modes.

        Values:
            DISK_MODE_UNSPECIFIED (0):
                Default value, which is unused.
            READ_WRITE (1):
                Attaches this disk in read-write mode. Only
                one virtual machine at a time can be attached to
                a disk in read-write mode.
            READ_ONLY (2):
                Attaches this disk in read-only mode.
                Multiple virtual machines can use a disk in
                read-only mode at a time.
            LOCKED (3):
                The disk is locked for administrative
                reasons. Nobody else can use the disk. This mode
                is used (for example) when taking a snapshot of
                a disk to prevent mounting the disk while it is
                being snapshotted.
        """

        DISK_MODE_UNSPECIFIED = 0
        READ_WRITE = 1
        READ_ONLY = 2
        LOCKED = 3

    class DiskInterface(proto.Enum):
        r"""List of the Disk Interfaces.

        Values:
            DISK_INTERFACE_UNSPECIFIED (0):
                Default value, which is unused.
            SCSI (1):
                SCSI Disk Interface.
            NVME (2):
                NVME Disk Interface.
            NVDIMM (3):
                NVDIMM Disk Interface.
            ISCSI (4):
                ISCSI Disk Interface.
        """

        DISK_INTERFACE_UNSPECIFIED = 0
        SCSI = 1
        NVME = 2
        NVDIMM = 3
        ISCSI = 4

    class DiskSavedState(proto.Enum):
        r"""List of the states of the Disk.

        Values:
            DISK_SAVED_STATE_UNSPECIFIED (0):
                Default Disk state has not been preserved.
            PRESERVED (1):
                Disk state has been preserved.
        """

        DISK_SAVED_STATE_UNSPECIFIED = 0
        PRESERVED = 1

    class InitializeParams(proto.Message):
        r"""Specifies the parameters to initialize this disk.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            disk_name (str):
                Optional. Specifies the disk name. If not
                specified, the default is to use the name of the
                instance.

                This field is a member of `oneof`_ ``_disk_name``.
            replica_zones (MutableSequence[str]):
                Optional. URL of the zone where the disk
                should be created. Required for each regional
                disk associated with the instance.
        """

        disk_name: str = proto.Field(
            proto.STRING,
            number=1,
            optional=True,
        )
        replica_zones: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=2,
        )

    initialize_params: InitializeParams = proto.Field(
        proto.MESSAGE,
        number=1,
        optional=True,
        message=InitializeParams,
    )
    device_name: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )
    kind: str = proto.Field(
        proto.STRING,
        number=5,
        optional=True,
    )
    disk_type_deprecated: DiskType = proto.Field(
        proto.ENUM,
        number=6,
        optional=True,
        enum=DiskType,
    )
    mode: DiskMode = proto.Field(
        proto.ENUM,
        number=7,
        optional=True,
        enum=DiskMode,
    )
    source: str = proto.Field(
        proto.STRING,
        number=8,
        optional=True,
    )
    index: int = proto.Field(
        proto.INT64,
        number=9,
        optional=True,
    )
    boot: bool = proto.Field(
        proto.BOOL,
        number=10,
        optional=True,
    )
    auto_delete: bool = proto.Field(
        proto.BOOL,
        number=11,
        optional=True,
    )
    license_: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=12,
    )
    disk_interface: DiskInterface = proto.Field(
        proto.ENUM,
        number=13,
        optional=True,
        enum=DiskInterface,
    )
    guest_os_feature: MutableSequence["GuestOsFeature"] = proto.RepeatedField(
        proto.MESSAGE,
        number=14,
        message="GuestOsFeature",
    )
    disk_encryption_key: "CustomerEncryptionKey" = proto.Field(
        proto.MESSAGE,
        number=15,
        optional=True,
        message="CustomerEncryptionKey",
    )
    disk_size_gb: int = proto.Field(
        proto.INT64,
        number=16,
        optional=True,
    )
    saved_state: DiskSavedState = proto.Field(
        proto.ENUM,
        number=17,
        optional=True,
        enum=DiskSavedState,
    )
    disk_type: str = proto.Field(
        proto.STRING,
        number=18,
        optional=True,
    )
    type_: DiskType = proto.Field(
        proto.ENUM,
        number=19,
        optional=True,
        enum=DiskType,
    )


class GuestOsFeature(proto.Message):
    r"""Feature type of the Guest OS.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        type_ (google.cloud.backupdr_v1.types.GuestOsFeature.FeatureType):
            The ID of a supported feature.

            This field is a member of `oneof`_ ``_type``.
    """

    class FeatureType(proto.Enum):
        r"""List of the Feature Types.

        Values:
            FEATURE_TYPE_UNSPECIFIED (0):
                Default value, which is unused.
            VIRTIO_SCSI_MULTIQUEUE (1):
                VIRTIO_SCSI_MULTIQUEUE feature type.
            WINDOWS (2):
                WINDOWS feature type.
            MULTI_IP_SUBNET (3):
                MULTI_IP_SUBNET feature type.
            UEFI_COMPATIBLE (4):
                UEFI_COMPATIBLE feature type.
            SECURE_BOOT (5):
                SECURE_BOOT feature type.
            GVNIC (6):
                GVNIC feature type.
            SEV_CAPABLE (7):
                SEV_CAPABLE feature type.
            BARE_METAL_LINUX_COMPATIBLE (8):
                BARE_METAL_LINUX_COMPATIBLE feature type.
            SUSPEND_RESUME_COMPATIBLE (9):
                SUSPEND_RESUME_COMPATIBLE feature type.
            SEV_LIVE_MIGRATABLE (10):
                SEV_LIVE_MIGRATABLE feature type.
            SEV_SNP_CAPABLE (11):
                SEV_SNP_CAPABLE feature type.
            TDX_CAPABLE (12):
                TDX_CAPABLE feature type.
            IDPF (13):
                IDPF feature type.
            SEV_LIVE_MIGRATABLE_V2 (14):
                SEV_LIVE_MIGRATABLE_V2 feature type.
        """

        FEATURE_TYPE_UNSPECIFIED = 0
        VIRTIO_SCSI_MULTIQUEUE = 1
        WINDOWS = 2
        MULTI_IP_SUBNET = 3
        UEFI_COMPATIBLE = 4
        SECURE_BOOT = 5
        GVNIC = 6
        SEV_CAPABLE = 7
        BARE_METAL_LINUX_COMPATIBLE = 8
        SUSPEND_RESUME_COMPATIBLE = 9
        SEV_LIVE_MIGRATABLE = 10
        SEV_SNP_CAPABLE = 11
        TDX_CAPABLE = 12
        IDPF = 13
        SEV_LIVE_MIGRATABLE_V2 = 14

    type_: FeatureType = proto.Field(
        proto.ENUM,
        number=1,
        optional=True,
        enum=FeatureType,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
