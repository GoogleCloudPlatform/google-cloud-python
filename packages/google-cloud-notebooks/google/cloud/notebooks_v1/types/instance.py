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

import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.notebooks_v1.types import environment

__protobuf__ = proto.module(
    package="google.cloud.notebooks.v1",
    manifest={
        "ReservationAffinity",
        "Instance",
    },
)


class ReservationAffinity(proto.Message):
    r"""Reservation Affinity for consuming Zonal reservation.

    Attributes:
        consume_reservation_type (google.cloud.notebooks_v1.types.ReservationAffinity.Type):
            Optional. Type of reservation to consume
        key (str):
            Optional. Corresponds to the label key of
            reservation resource.
        values (MutableSequence[str]):
            Optional. Corresponds to the label values of
            reservation resource.
    """

    class Type(proto.Enum):
        r"""Indicates whether to consume capacity from an reservation or
        not.

        Values:
            TYPE_UNSPECIFIED (0):
                Default type.
            NO_RESERVATION (1):
                Do not consume from any allocated capacity.
            ANY_RESERVATION (2):
                Consume any reservation available.
            SPECIFIC_RESERVATION (3):
                Must consume from a specific reservation.
                Must specify key value fields for specifying the
                reservations.
        """

        TYPE_UNSPECIFIED = 0
        NO_RESERVATION = 1
        ANY_RESERVATION = 2
        SPECIFIC_RESERVATION = 3

    consume_reservation_type: Type = proto.Field(
        proto.ENUM,
        number=1,
        enum=Type,
    )
    key: str = proto.Field(
        proto.STRING,
        number=2,
    )
    values: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class Instance(proto.Message):
    r"""The definition of a notebook instance.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Output only. The name of this notebook instance. Format:
            ``projects/{project_id}/locations/{location}/instances/{instance_id}``
        vm_image (google.cloud.notebooks_v1.types.VmImage):
            Use a Compute Engine VM image to start the
            notebook instance.

            This field is a member of `oneof`_ ``environment``.
        container_image (google.cloud.notebooks_v1.types.ContainerImage):
            Use a container image to start the notebook
            instance.

            This field is a member of `oneof`_ ``environment``.
        post_startup_script (str):
            Path to a Bash script that automatically runs after a
            notebook instance fully boots up. The path must be a URL or
            Cloud Storage path (``gs://path-to-file/file-name``).
        proxy_uri (str):
            Output only. The proxy endpoint that is used
            to access the Jupyter notebook.
        instance_owners (MutableSequence[str]):
            Input only. The owner of this instance after creation.
            Format: ``alias@example.com``

            Currently supports one owner only. If not specified, all of
            the service account users of your VM instance's service
            account can use the instance.
        service_account (str):
            The service account on this instance, giving access to other
            Google Cloud services. You can use any service account
            within the same project, but you must have the service
            account user permission to use the instance.

            If not specified, the `Compute Engine default service
            account <https://cloud.google.com/compute/docs/access/service-accounts#default_service_account>`__
            is used.
        service_account_scopes (MutableSequence[str]):
            Optional. The URIs of service account scopes to be included
            in Compute Engine instances.

            If not specified, the following
            `scopes <https://cloud.google.com/compute/docs/access/service-accounts#accesscopesiam>`__
            are defined:

            - https://www.googleapis.com/auth/cloud-platform
            - https://www.googleapis.com/auth/userinfo.email If not
              using default scopes, you need at least:
              https://www.googleapis.com/auth/compute
        machine_type (str):
            Required. The `Compute Engine machine
            type <https://cloud.google.com/compute/docs/machine-types>`__
            of this instance.
        accelerator_config (google.cloud.notebooks_v1.types.Instance.AcceleratorConfig):
            The hardware accelerator used on this instance. If you use
            accelerators, make sure that your configuration has `enough
            vCPUs and memory to support the ``machine_type`` you have
            selected <https://cloud.google.com/compute/docs/gpus/#gpus-list>`__.
        state (google.cloud.notebooks_v1.types.Instance.State):
            Output only. The state of this instance.
        install_gpu_driver (bool):
            Whether the end user authorizes Google Cloud
            to install GPU driver on this instance.
            If this field is empty or set to false, the GPU
            driver won't be installed. Only applicable to
            instances with GPUs.
        custom_gpu_driver_path (str):
            Specify a custom Cloud Storage path where the
            GPU driver is stored. If not specified, we'll
            automatically choose from official GPU drivers.
        boot_disk_type (google.cloud.notebooks_v1.types.Instance.DiskType):
            Input only. The type of the boot disk attached to this
            instance, defaults to standard persistent disk
            (``PD_STANDARD``).
        boot_disk_size_gb (int):
            Input only. The size of the boot disk in GB
            attached to this instance, up to a maximum of
            64000 GB (64 TB). The minimum recommended value
            is 100 GB. If not specified, this defaults to
            100.
        data_disk_type (google.cloud.notebooks_v1.types.Instance.DiskType):
            Input only. The type of the data disk attached to this
            instance, defaults to standard persistent disk
            (``PD_STANDARD``).
        data_disk_size_gb (int):
            Input only. The size of the data disk in GB
            attached to this instance, up to a maximum of
            64000 GB (64 TB). You can choose the size of the
            data disk based on how big your notebooks and
            data are. If not specified, this defaults to
            100.
        no_remove_data_disk (bool):
            Input only. If true, the data disk will not
            be auto deleted when deleting the instance.
        disk_encryption (google.cloud.notebooks_v1.types.Instance.DiskEncryption):
            Input only. Disk encryption method used on
            the boot and data disks, defaults to GMEK.
        kms_key (str):
            Input only. The KMS key used to encrypt the disks, only
            applicable if disk_encryption is CMEK. Format:
            ``projects/{project_id}/locations/{location}/keyRings/{key_ring_id}/cryptoKeys/{key_id}``

            Learn more about `using your own encryption
            keys </kms/docs/quickstart>`__.
        disks (MutableSequence[google.cloud.notebooks_v1.types.Instance.Disk]):
            Output only. Attached disks to notebook
            instance.
        shielded_instance_config (google.cloud.notebooks_v1.types.Instance.ShieldedInstanceConfig):
            Optional. Shielded VM configuration. `Images using supported
            Shielded VM
            features <https://cloud.google.com/compute/docs/instances/modifying-shielded-vm>`__.
        no_public_ip (bool):
            If true, no public IP will be assigned to
            this instance.
        no_proxy_access (bool):
            If true, the notebook instance will not
            register with the proxy.
        network (str):
            The name of the VPC that this instance is in. Format:
            ``projects/{project_id}/global/networks/{network_id}``
        subnet (str):
            The name of the subnet that this instance is in. Format:
            ``projects/{project_id}/regions/{region}/subnetworks/{subnetwork_id}``
        labels (MutableMapping[str, str]):
            Labels to apply to this instance.
            These can be later modified by the setLabels
            method.
        metadata (MutableMapping[str, str]):
            Custom metadata to apply to this instance.
        tags (MutableSequence[str]):
            Optional. The Compute Engine tags to add to runtime (see
            `Tagging
            instances <https://cloud.google.com/compute/docs/label-or-tag-resources#tags>`__).
        upgrade_history (MutableSequence[google.cloud.notebooks_v1.types.Instance.UpgradeHistoryEntry]):
            The upgrade history of this instance.
        nic_type (google.cloud.notebooks_v1.types.Instance.NicType):
            Optional. The type of vNIC to be used on this
            interface. This may be gVNIC or VirtioNet.
        reservation_affinity (google.cloud.notebooks_v1.types.ReservationAffinity):
            Optional. The optional reservation affinity. Setting this
            field will apply the specified `Zonal Compute
            Reservation <https://cloud.google.com/compute/docs/instances/reserving-zonal-resources>`__
            to this notebook instance.
        creator (str):
            Output only. Email address of entity that
            sent original CreateInstance request.
        can_ip_forward (bool):
            Optional. Flag to enable ip forwarding or
            not, default false/off.
            https://cloud.google.com/vpc/docs/using-routes#canipforward
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Instance creation time.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Instance update time.
    """

    class AcceleratorType(proto.Enum):
        r"""Definition of the types of hardware accelerators that can be
        used on this instance.

        Values:
            ACCELERATOR_TYPE_UNSPECIFIED (0):
                Accelerator type is not specified.
            NVIDIA_TESLA_K80 (1):
                Accelerator type is Nvidia Tesla K80.
            NVIDIA_TESLA_P100 (2):
                Accelerator type is Nvidia Tesla P100.
            NVIDIA_TESLA_V100 (3):
                Accelerator type is Nvidia Tesla V100.
            NVIDIA_TESLA_P4 (4):
                Accelerator type is Nvidia Tesla P4.
            NVIDIA_TESLA_T4 (5):
                Accelerator type is Nvidia Tesla T4.
            NVIDIA_TESLA_A100 (11):
                Accelerator type is Nvidia Tesla A100.
            NVIDIA_TESLA_T4_VWS (8):
                Accelerator type is NVIDIA Tesla T4 Virtual
                Workstations.
            NVIDIA_TESLA_P100_VWS (9):
                Accelerator type is NVIDIA Tesla P100 Virtual
                Workstations.
            NVIDIA_TESLA_P4_VWS (10):
                Accelerator type is NVIDIA Tesla P4 Virtual
                Workstations.
            TPU_V2 (6):
                (Coming soon) Accelerator type is TPU V2.
            TPU_V3 (7):
                (Coming soon) Accelerator type is TPU V3.
        """

        ACCELERATOR_TYPE_UNSPECIFIED = 0
        NVIDIA_TESLA_K80 = 1
        NVIDIA_TESLA_P100 = 2
        NVIDIA_TESLA_V100 = 3
        NVIDIA_TESLA_P4 = 4
        NVIDIA_TESLA_T4 = 5
        NVIDIA_TESLA_A100 = 11
        NVIDIA_TESLA_T4_VWS = 8
        NVIDIA_TESLA_P100_VWS = 9
        NVIDIA_TESLA_P4_VWS = 10
        TPU_V2 = 6
        TPU_V3 = 7

    class State(proto.Enum):
        r"""The definition of the states of this instance.

        Values:
            STATE_UNSPECIFIED (0):
                State is not specified.
            STARTING (1):
                The control logic is starting the instance.
            PROVISIONING (2):
                The control logic is installing required
                frameworks and registering the instance with
                notebook proxy
            ACTIVE (3):
                The instance is running.
            STOPPING (4):
                The control logic is stopping the instance.
            STOPPED (5):
                The instance is stopped.
            DELETED (6):
                The instance is deleted.
            UPGRADING (7):
                The instance is upgrading.
            INITIALIZING (8):
                The instance is being created.
            REGISTERING (9):
                The instance is getting registered.
            SUSPENDING (10):
                The instance is suspending.
            SUSPENDED (11):
                The instance is suspended.
        """

        STATE_UNSPECIFIED = 0
        STARTING = 1
        PROVISIONING = 2
        ACTIVE = 3
        STOPPING = 4
        STOPPED = 5
        DELETED = 6
        UPGRADING = 7
        INITIALIZING = 8
        REGISTERING = 9
        SUSPENDING = 10
        SUSPENDED = 11

    class DiskType(proto.Enum):
        r"""Possible disk types for notebook instances.

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

    class NicType(proto.Enum):
        r"""The type of vNIC driver. Default should be UNSPECIFIED_NIC_TYPE.

        Values:
            UNSPECIFIED_NIC_TYPE (0):
                No type specified.
            VIRTIO_NET (1):
                VIRTIO
            GVNIC (2):
                GVNIC
        """

        UNSPECIFIED_NIC_TYPE = 0
        VIRTIO_NET = 1
        GVNIC = 2

    class AcceleratorConfig(proto.Message):
        r"""Definition of a hardware accelerator. Note that not all combinations
        of ``type`` and ``core_count`` are valid. Check `GPUs on Compute
        Engine <https://cloud.google.com/compute/docs/gpus/#gpus-list>`__ to
        find a valid combination. TPUs are not supported.

        Attributes:
            type_ (google.cloud.notebooks_v1.types.Instance.AcceleratorType):
                Type of this accelerator.
            core_count (int):
                Count of cores of this accelerator.
        """

        type_: "Instance.AcceleratorType" = proto.Field(
            proto.ENUM,
            number=1,
            enum="Instance.AcceleratorType",
        )
        core_count: int = proto.Field(
            proto.INT64,
            number=2,
        )

    class Disk(proto.Message):
        r"""An instance-attached disk resource.

        Attributes:
            auto_delete (bool):
                Indicates whether the disk will be
                auto-deleted when the instance is deleted (but
                not when the disk is detached from the
                instance).
            boot (bool):
                Indicates that this is a boot disk. The
                virtual machine will use the first partition of
                the disk for its root filesystem.
            device_name (str):
                Indicates a unique device name of your choice that is
                reflected into the ``/dev/disk/by-id/google-*`` tree of a
                Linux operating system running within the instance. This
                name can be used to reference the device for mounting,
                resizing, and so on, from within the instance.

                If not specified, the server chooses a default device name
                to apply to this disk, in the form persistent-disk-x, where
                x is a number assigned by Google Compute Engine.This field
                is only applicable for persistent disks.
            disk_size_gb (int):
                Indicates the size of the disk in base-2 GB.
            guest_os_features (MutableSequence[google.cloud.notebooks_v1.types.Instance.Disk.GuestOsFeature]):
                Indicates a list of features to enable on the
                guest operating system. Applicable only for
                bootable images. Read  Enabling guest operating
                system features to see a list of available
                options.
            index (int):
                A zero-based index to this disk, where 0 is
                reserved for the boot disk. If you have many
                disks attached to an instance, each disk would
                have a unique index number.
            interface (str):
                Indicates the disk interface to use for attaching this disk,
                which is either SCSI or NVME. The default is SCSI.
                Persistent disks must always use SCSI and the request will
                fail if you attempt to attach a persistent disk in any other
                format than SCSI. Local SSDs can use either NVME or SCSI.
                For performance characteristics of SCSI over NVMe, see Local
                SSD performance. Valid values:

                - ``NVME``
                - ``SCSI``
            kind (str):
                Type of the resource. Always
                compute#attachedDisk for attached disks.
            licenses (MutableSequence[str]):
                A list of publicly visible licenses. Reserved
                for Google's use. A License represents billing
                and aggregate usage data for public and
                marketplace images.
            mode (str):
                The mode in which to attach this disk, either ``READ_WRITE``
                or ``READ_ONLY``. If not specified, the default is to attach
                the disk in ``READ_WRITE`` mode. Valid values:

                - ``READ_ONLY``
                - ``READ_WRITE``
            source (str):
                Indicates a valid partial or full URL to an
                existing Persistent Disk resource.
            type_ (str):
                Indicates the type of the disk, either ``SCRATCH`` or
                ``PERSISTENT``. Valid values:

                - ``PERSISTENT``
                - ``SCRATCH``
        """

        class GuestOsFeature(proto.Message):
            r"""Guest OS features for boot disk.

            Attributes:
                type_ (str):
                    The ID of a supported feature. Read Enabling guest operating
                    system features to see a list of available options. Valid
                    values:

                    - ``FEATURE_TYPE_UNSPECIFIED``
                    - ``MULTI_IP_SUBNET``
                    - ``SECURE_BOOT``
                    - ``UEFI_COMPATIBLE``
                    - ``VIRTIO_SCSI_MULTIQUEUE``
                    - ``WINDOWS``
            """

            type_: str = proto.Field(
                proto.STRING,
                number=1,
            )

        auto_delete: bool = proto.Field(
            proto.BOOL,
            number=1,
        )
        boot: bool = proto.Field(
            proto.BOOL,
            number=2,
        )
        device_name: str = proto.Field(
            proto.STRING,
            number=3,
        )
        disk_size_gb: int = proto.Field(
            proto.INT64,
            number=4,
        )
        guest_os_features: MutableSequence["Instance.Disk.GuestOsFeature"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=5,
                message="Instance.Disk.GuestOsFeature",
            )
        )
        index: int = proto.Field(
            proto.INT64,
            number=6,
        )
        interface: str = proto.Field(
            proto.STRING,
            number=7,
        )
        kind: str = proto.Field(
            proto.STRING,
            number=8,
        )
        licenses: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=9,
        )
        mode: str = proto.Field(
            proto.STRING,
            number=10,
        )
        source: str = proto.Field(
            proto.STRING,
            number=11,
        )
        type_: str = proto.Field(
            proto.STRING,
            number=12,
        )

    class ShieldedInstanceConfig(proto.Message):
        r"""A set of Shielded Instance options. Check `Images using supported
        Shielded VM
        features <https://cloud.google.com/compute/docs/instances/modifying-shielded-vm>`__.
        Not all combinations are valid.

        Attributes:
            enable_secure_boot (bool):
                Defines whether the instance has Secure Boot
                enabled.
                Secure Boot helps ensure that the system only
                runs authentic software by verifying the digital
                signature of all boot components, and halting
                the boot process if signature verification
                fails. Disabled by default.
            enable_vtpm (bool):
                Defines whether the instance has the vTPM
                enabled. Enabled by default.
            enable_integrity_monitoring (bool):
                Defines whether the instance has integrity
                monitoring enabled.
                Enables monitoring and attestation of the boot
                integrity of the instance. The attestation is
                performed against the integrity policy baseline.
                This baseline is initially derived from the
                implicitly trusted boot image when the instance
                is created. Enabled by default.
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

    class UpgradeHistoryEntry(proto.Message):
        r"""The entry of VM image upgrade history.

        Attributes:
            snapshot (str):
                The snapshot of the boot disk of this
                notebook instance before upgrade.
            vm_image (str):
                The VM image before this instance upgrade.
            container_image (str):
                The container image before this instance
                upgrade.
            framework (str):
                The framework of this notebook instance.
            version (str):
                The version of the notebook instance before
                this upgrade.
            state (google.cloud.notebooks_v1.types.Instance.UpgradeHistoryEntry.State):
                The state of this instance upgrade history
                entry.
            create_time (google.protobuf.timestamp_pb2.Timestamp):
                The time that this instance upgrade history
                entry is created.
            target_image (str):
                Target VM Image. Format:
                ``ainotebooks-vm/project/image-name/name``.
            action (google.cloud.notebooks_v1.types.Instance.UpgradeHistoryEntry.Action):
                Action. Rolloback or Upgrade.
            target_version (str):
                Target VM Version, like m63.
        """

        class State(proto.Enum):
            r"""The definition of the states of this upgrade history entry.

            Values:
                STATE_UNSPECIFIED (0):
                    State is not specified.
                STARTED (1):
                    The instance upgrade is started.
                SUCCEEDED (2):
                    The instance upgrade is succeeded.
                FAILED (3):
                    The instance upgrade is failed.
            """

            STATE_UNSPECIFIED = 0
            STARTED = 1
            SUCCEEDED = 2
            FAILED = 3

        class Action(proto.Enum):
            r"""The definition of operations of this upgrade history entry.

            Values:
                ACTION_UNSPECIFIED (0):
                    Operation is not specified.
                UPGRADE (1):
                    Upgrade.
                ROLLBACK (2):
                    Rollback.
            """

            ACTION_UNSPECIFIED = 0
            UPGRADE = 1
            ROLLBACK = 2

        snapshot: str = proto.Field(
            proto.STRING,
            number=1,
        )
        vm_image: str = proto.Field(
            proto.STRING,
            number=2,
        )
        container_image: str = proto.Field(
            proto.STRING,
            number=3,
        )
        framework: str = proto.Field(
            proto.STRING,
            number=4,
        )
        version: str = proto.Field(
            proto.STRING,
            number=5,
        )
        state: "Instance.UpgradeHistoryEntry.State" = proto.Field(
            proto.ENUM,
            number=6,
            enum="Instance.UpgradeHistoryEntry.State",
        )
        create_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=7,
            message=timestamp_pb2.Timestamp,
        )
        target_image: str = proto.Field(
            proto.STRING,
            number=8,
        )
        action: "Instance.UpgradeHistoryEntry.Action" = proto.Field(
            proto.ENUM,
            number=9,
            enum="Instance.UpgradeHistoryEntry.Action",
        )
        target_version: str = proto.Field(
            proto.STRING,
            number=10,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    vm_image: environment.VmImage = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="environment",
        message=environment.VmImage,
    )
    container_image: environment.ContainerImage = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="environment",
        message=environment.ContainerImage,
    )
    post_startup_script: str = proto.Field(
        proto.STRING,
        number=4,
    )
    proxy_uri: str = proto.Field(
        proto.STRING,
        number=5,
    )
    instance_owners: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )
    service_account: str = proto.Field(
        proto.STRING,
        number=7,
    )
    service_account_scopes: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=31,
    )
    machine_type: str = proto.Field(
        proto.STRING,
        number=8,
    )
    accelerator_config: AcceleratorConfig = proto.Field(
        proto.MESSAGE,
        number=9,
        message=AcceleratorConfig,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=10,
        enum=State,
    )
    install_gpu_driver: bool = proto.Field(
        proto.BOOL,
        number=11,
    )
    custom_gpu_driver_path: str = proto.Field(
        proto.STRING,
        number=12,
    )
    boot_disk_type: DiskType = proto.Field(
        proto.ENUM,
        number=13,
        enum=DiskType,
    )
    boot_disk_size_gb: int = proto.Field(
        proto.INT64,
        number=14,
    )
    data_disk_type: DiskType = proto.Field(
        proto.ENUM,
        number=25,
        enum=DiskType,
    )
    data_disk_size_gb: int = proto.Field(
        proto.INT64,
        number=26,
    )
    no_remove_data_disk: bool = proto.Field(
        proto.BOOL,
        number=27,
    )
    disk_encryption: DiskEncryption = proto.Field(
        proto.ENUM,
        number=15,
        enum=DiskEncryption,
    )
    kms_key: str = proto.Field(
        proto.STRING,
        number=16,
    )
    disks: MutableSequence[Disk] = proto.RepeatedField(
        proto.MESSAGE,
        number=28,
        message=Disk,
    )
    shielded_instance_config: ShieldedInstanceConfig = proto.Field(
        proto.MESSAGE,
        number=30,
        message=ShieldedInstanceConfig,
    )
    no_public_ip: bool = proto.Field(
        proto.BOOL,
        number=17,
    )
    no_proxy_access: bool = proto.Field(
        proto.BOOL,
        number=18,
    )
    network: str = proto.Field(
        proto.STRING,
        number=19,
    )
    subnet: str = proto.Field(
        proto.STRING,
        number=20,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=21,
    )
    metadata: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=22,
    )
    tags: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=32,
    )
    upgrade_history: MutableSequence[UpgradeHistoryEntry] = proto.RepeatedField(
        proto.MESSAGE,
        number=29,
        message=UpgradeHistoryEntry,
    )
    nic_type: NicType = proto.Field(
        proto.ENUM,
        number=33,
        enum=NicType,
    )
    reservation_affinity: "ReservationAffinity" = proto.Field(
        proto.MESSAGE,
        number=34,
        message="ReservationAffinity",
    )
    creator: str = proto.Field(
        proto.STRING,
        number=36,
    )
    can_ip_forward: bool = proto.Field(
        proto.BOOL,
        number=39,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=23,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=24,
        message=timestamp_pb2.Timestamp,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
