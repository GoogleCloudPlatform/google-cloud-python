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
    package="google.cloud.notebooks.v2",
    manifest={
        "DiskEncryption",
        "DiskType",
        "NetworkInterface",
        "VmImage",
        "ContainerImage",
        "AcceleratorConfig",
        "ShieldedInstanceConfig",
        "GPUDriverConfig",
        "DataDisk",
        "BootDisk",
        "ServiceAccount",
        "GceSetup",
    },
)


class DiskEncryption(proto.Enum):
    r"""Definition of the disk encryption options.

    Values:
        DISK_ENCRYPTION_UNSPECIFIED (0):
            Disk encryption is not specified.
        GMEK (1):
            Use Google managed encryption keys to encrypt
            the boot disk.
        CMEK (2):
            Use customer managed encryption keys to
            encrypt the boot disk.
    """

    DISK_ENCRYPTION_UNSPECIFIED = 0
    GMEK = 1
    CMEK = 2


class DiskType(proto.Enum):
    r"""Possible disk types.

    Values:
        DISK_TYPE_UNSPECIFIED (0):
            Disk type not set.
        PD_STANDARD (1):
            Standard persistent disk type.
        PD_SSD (2):
            SSD persistent disk type.
        PD_BALANCED (3):
            Balanced persistent disk type.
        PD_EXTREME (4):
            Extreme persistent disk type.
    """

    DISK_TYPE_UNSPECIFIED = 0
    PD_STANDARD = 1
    PD_SSD = 2
    PD_BALANCED = 3
    PD_EXTREME = 4


class NetworkInterface(proto.Message):
    r"""The definition of a network interface resource attached to a
    VM.

    Attributes:
        network (str):
            Optional. The name of the VPC that this VM instance is in.
            Format:
            ``projects/{project_id}/global/networks/{network_id}``
        subnet (str):
            Optional. The name of the subnet that this VM instance is
            in. Format:
            ``projects/{project_id}/regions/{region}/subnetworks/{subnetwork_id}``
        nic_type (google.cloud.notebooks_v2.types.NetworkInterface.NicType):
            Optional. The type of vNIC to be used on this
            interface. This may be gVNIC or VirtioNet.
    """

    class NicType(proto.Enum):
        r"""The type of vNIC driver. Default should be NIC_TYPE_UNSPECIFIED.

        Values:
            NIC_TYPE_UNSPECIFIED (0):
                No type specified.
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
    )
    subnet: str = proto.Field(
        proto.STRING,
        number=2,
    )
    nic_type: NicType = proto.Field(
        proto.ENUM,
        number=3,
        enum=NicType,
    )


class VmImage(proto.Message):
    r"""Definition of a custom Compute Engine virtual machine image
    for starting a notebook instance with the environment installed
    directly on the VM.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        project (str):
            Required. The name of the Google Cloud project that this VM
            image belongs to. Format: ``{project_id}``
        name (str):
            Optional. Use VM image name to find the
            image.

            This field is a member of `oneof`_ ``image``.
        family (str):
            Optional. Use this VM image family to find
            the image; the newest image in this family will
            be used.

            This field is a member of `oneof`_ ``image``.
    """

    project: str = proto.Field(
        proto.STRING,
        number=1,
    )
    name: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="image",
    )
    family: str = proto.Field(
        proto.STRING,
        number=3,
        oneof="image",
    )


class ContainerImage(proto.Message):
    r"""Definition of a container image for starting a notebook
    instance with the environment installed in a container.

    Attributes:
        repository (str):
            Required. The path to the container image repository. For
            example: ``gcr.io/{project_id}/{image_name}``
        tag (str):
            Optional. The tag of the container image. If
            not specified, this defaults to the latest tag.
    """

    repository: str = proto.Field(
        proto.STRING,
        number=1,
    )
    tag: str = proto.Field(
        proto.STRING,
        number=2,
    )


class AcceleratorConfig(proto.Message):
    r"""An accelerator configuration for a VM instance Definition of a
    hardware accelerator. Note that there is no check on ``type`` and
    ``core_count`` combinations. TPUs are not supported. See `GPUs on
    Compute
    Engine <https://cloud.google.com/compute/docs/gpus/#gpus-list>`__ to
    find a valid combination.

    Attributes:
        type_ (google.cloud.notebooks_v2.types.AcceleratorConfig.AcceleratorType):
            Optional. Type of this accelerator.
        core_count (int):
            Optional. Count of cores of this accelerator.
    """

    class AcceleratorType(proto.Enum):
        r"""Definition of the types of hardware accelerators that can be
        used on this instance.

        Values:
            ACCELERATOR_TYPE_UNSPECIFIED (0):
                Accelerator type is not specified.
            NVIDIA_TESLA_P100 (2):
                Accelerator type is Nvidia Tesla P100.
            NVIDIA_TESLA_V100 (3):
                Accelerator type is Nvidia Tesla V100.
            NVIDIA_TESLA_P4 (4):
                Accelerator type is Nvidia Tesla P4.
            NVIDIA_TESLA_T4 (5):
                Accelerator type is Nvidia Tesla T4.
            NVIDIA_TESLA_A100 (11):
                Accelerator type is Nvidia Tesla A100 - 40GB.
            NVIDIA_A100_80GB (12):
                Accelerator type is Nvidia Tesla A100 - 80GB.
            NVIDIA_L4 (13):
                Accelerator type is Nvidia Tesla L4.
            NVIDIA_TESLA_T4_VWS (8):
                Accelerator type is NVIDIA Tesla T4 Virtual
                Workstations.
            NVIDIA_TESLA_P100_VWS (9):
                Accelerator type is NVIDIA Tesla P100 Virtual
                Workstations.
            NVIDIA_TESLA_P4_VWS (10):
                Accelerator type is NVIDIA Tesla P4 Virtual
                Workstations.
        """

        ACCELERATOR_TYPE_UNSPECIFIED = 0
        NVIDIA_TESLA_P100 = 2
        NVIDIA_TESLA_V100 = 3
        NVIDIA_TESLA_P4 = 4
        NVIDIA_TESLA_T4 = 5
        NVIDIA_TESLA_A100 = 11
        NVIDIA_A100_80GB = 12
        NVIDIA_L4 = 13
        NVIDIA_TESLA_T4_VWS = 8
        NVIDIA_TESLA_P100_VWS = 9
        NVIDIA_TESLA_P4_VWS = 10

    type_: AcceleratorType = proto.Field(
        proto.ENUM,
        number=1,
        enum=AcceleratorType,
    )
    core_count: int = proto.Field(
        proto.INT64,
        number=2,
    )


class ShieldedInstanceConfig(proto.Message):
    r"""A set of Shielded Instance options. See `Images using supported
    Shielded VM
    features <https://cloud.google.com/compute/docs/instances/modifying-shielded-vm>`__.
    Not all combinations are valid.

    Attributes:
        enable_secure_boot (bool):
            Optional. Defines whether the VM instance has
            Secure Boot enabled.
            Secure Boot helps ensure that the system only
            runs authentic software by verifying the digital
            signature of all boot components, and halting
            the boot process if signature verification
            fails. Disabled by default.
        enable_vtpm (bool):
            Optional. Defines whether the VM instance has
            the vTPM enabled. Enabled by default.
        enable_integrity_monitoring (bool):
            Optional. Defines whether the VM instance has
            integrity monitoring enabled.
            Enables monitoring and attestation of the boot
            integrity of the VM instance. The attestation is
            performed against the integrity policy baseline.
            This baseline is initially derived from the
            implicitly trusted boot image when the VM
            instance is created. Enabled by default.
    """

    enable_secure_boot: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    enable_vtpm: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    enable_integrity_monitoring: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class GPUDriverConfig(proto.Message):
    r"""A GPU driver configuration

    Attributes:
        enable_gpu_driver (bool):
            Optional. Whether the end user authorizes
            Google Cloud to install GPU driver on this VM
            instance. If this field is empty or set to
            false, the GPU driver won't be installed. Only
            applicable to instances with GPUs.
        custom_gpu_driver_path (str):
            Optional. Specify a custom Cloud Storage path
            where the GPU driver is stored. If not
            specified, we'll automatically choose from
            official GPU drivers.
    """

    enable_gpu_driver: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    custom_gpu_driver_path: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DataDisk(proto.Message):
    r"""An instance-attached disk resource.

    Attributes:
        disk_size_gb (int):
            Optional. The size of the disk in GB attached
            to this VM instance, up to a maximum of 64000 GB
            (64 TB). If not specified, this defaults to 100.
        disk_type (google.cloud.notebooks_v2.types.DiskType):
            Optional. Input only. Indicates the type of
            the disk.
        disk_encryption (google.cloud.notebooks_v2.types.DiskEncryption):
            Optional. Input only. Disk encryption method
            used on the boot and data disks, defaults to
            GMEK.
        kms_key (str):
            Optional. Input only. The KMS key used to encrypt the disks,
            only applicable if disk_encryption is CMEK. Format:
            ``projects/{project_id}/locations/{location}/keyRings/{key_ring_id}/cryptoKeys/{key_id}``

            Learn more about using your own encryption keys.
    """

    disk_size_gb: int = proto.Field(
        proto.INT64,
        number=1,
    )
    disk_type: "DiskType" = proto.Field(
        proto.ENUM,
        number=2,
        enum="DiskType",
    )
    disk_encryption: "DiskEncryption" = proto.Field(
        proto.ENUM,
        number=5,
        enum="DiskEncryption",
    )
    kms_key: str = proto.Field(
        proto.STRING,
        number=6,
    )


class BootDisk(proto.Message):
    r"""The definition of a boot disk.

    Attributes:
        disk_size_gb (int):
            Optional. The size of the boot disk in GB
            attached to this instance, up to a maximum of
            64000 GB (64 TB). If not specified, this
            defaults to the recommended value of 150GB.
        disk_type (google.cloud.notebooks_v2.types.DiskType):
            Optional. Indicates the type of the disk.
        disk_encryption (google.cloud.notebooks_v2.types.DiskEncryption):
            Optional. Input only. Disk encryption method
            used on the boot and data disks, defaults to
            GMEK.
        kms_key (str):
            Optional. Input only. The KMS key used to encrypt the disks,
            only applicable if disk_encryption is CMEK. Format:
            ``projects/{project_id}/locations/{location}/keyRings/{key_ring_id}/cryptoKeys/{key_id}``

            Learn more about using your own encryption keys.
    """

    disk_size_gb: int = proto.Field(
        proto.INT64,
        number=1,
    )
    disk_type: "DiskType" = proto.Field(
        proto.ENUM,
        number=2,
        enum="DiskType",
    )
    disk_encryption: "DiskEncryption" = proto.Field(
        proto.ENUM,
        number=3,
        enum="DiskEncryption",
    )
    kms_key: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ServiceAccount(proto.Message):
    r"""A service account that acts as an identity.

    Attributes:
        email (str):
            Optional. Email address of the service
            account.
        scopes (MutableSequence[str]):
            Output only. The list of scopes to be made
            available for this service account. Set by the
            CLH to
            https://www.googleapis.com/auth/cloud-platform
    """

    email: str = proto.Field(
        proto.STRING,
        number=1,
    )
    scopes: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class GceSetup(proto.Message):
    r"""The definition of how to configure a VM instance outside of
    Resources and Identity.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        machine_type (str):
            Optional. The machine type of the VM
            instance.
            https://cloud.google.com/compute/docs/machine-resource
        accelerator_configs (MutableSequence[google.cloud.notebooks_v2.types.AcceleratorConfig]):
            Optional. The hardware accelerators used on this instance.
            If you use accelerators, make sure that your configuration
            has `enough vCPUs and memory to support the ``machine_type``
            you have
            selected <https://cloud.google.com/compute/docs/gpus/#gpus-list>`__.
            Currently supports only one accelerator configuration.
        service_accounts (MutableSequence[google.cloud.notebooks_v2.types.ServiceAccount]):
            Optional. The service account that serves as
            an identity for the VM instance. Currently
            supports only one service account.
        vm_image (google.cloud.notebooks_v2.types.VmImage):
            Optional. Use a Compute Engine VM image to
            start the notebook instance.

            This field is a member of `oneof`_ ``image``.
        container_image (google.cloud.notebooks_v2.types.ContainerImage):
            Optional. Use a container image to start the
            notebook instance.

            This field is a member of `oneof`_ ``image``.
        boot_disk (google.cloud.notebooks_v2.types.BootDisk):
            Optional. The boot disk for the VM.
        data_disks (MutableSequence[google.cloud.notebooks_v2.types.DataDisk]):
            Optional. Data disks attached to the VM
            instance. Currently supports only one data disk.
        shielded_instance_config (google.cloud.notebooks_v2.types.ShieldedInstanceConfig):
            Optional. Shielded VM configuration. `Images using supported
            Shielded VM
            features <https://cloud.google.com/compute/docs/instances/modifying-shielded-vm>`__.
        network_interfaces (MutableSequence[google.cloud.notebooks_v2.types.NetworkInterface]):
            Optional. The network interfaces for the VM.
            Supports only one interface.
        disable_public_ip (bool):
            Optional. If true, no external IP will be
            assigned to this VM instance.
        tags (MutableSequence[str]):
            Optional. The Compute Engine tags to add to runtime (see
            `Tagging
            instances <https://cloud.google.com/compute/docs/label-or-tag-resources#tags>`__).
        metadata (MutableMapping[str, str]):
            Optional. Custom metadata to apply to this
            instance.
        enable_ip_forwarding (bool):
            Optional. Flag to enable ip forwarding or
            not, default false/off.
            https://cloud.google.com/vpc/docs/using-routes#canipforward
        gpu_driver_config (google.cloud.notebooks_v2.types.GPUDriverConfig):
            Optional. Configuration for GPU drivers.
    """

    machine_type: str = proto.Field(
        proto.STRING,
        number=1,
    )
    accelerator_configs: MutableSequence["AcceleratorConfig"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="AcceleratorConfig",
    )
    service_accounts: MutableSequence["ServiceAccount"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="ServiceAccount",
    )
    vm_image: "VmImage" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="image",
        message="VmImage",
    )
    container_image: "ContainerImage" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="image",
        message="ContainerImage",
    )
    boot_disk: "BootDisk" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="BootDisk",
    )
    data_disks: MutableSequence["DataDisk"] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message="DataDisk",
    )
    shielded_instance_config: "ShieldedInstanceConfig" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="ShieldedInstanceConfig",
    )
    network_interfaces: MutableSequence["NetworkInterface"] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message="NetworkInterface",
    )
    disable_public_ip: bool = proto.Field(
        proto.BOOL,
        number=10,
    )
    tags: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=11,
    )
    metadata: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=12,
    )
    enable_ip_forwarding: bool = proto.Field(
        proto.BOOL,
        number=13,
    )
    gpu_driver_config: "GPUDriverConfig" = proto.Field(
        proto.MESSAGE,
        number=14,
        message="GPUDriverConfig",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
