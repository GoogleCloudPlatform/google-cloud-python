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
        "Runtime",
        "RuntimeAcceleratorConfig",
        "EncryptionConfig",
        "LocalDisk",
        "LocalDiskInitializeParams",
        "RuntimeAccessConfig",
        "RuntimeSoftwareConfig",
        "RuntimeMetrics",
        "RuntimeShieldedInstanceConfig",
        "VirtualMachine",
        "VirtualMachineConfig",
    },
)


class Runtime(proto.Message):
    r"""The definition of a Runtime for a managed notebook instance.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Output only. The resource name of the runtime. Format:
            ``projects/{project}/locations/{location}/runtimes/{runtimeId}``
        virtual_machine (google.cloud.notebooks_v1.types.VirtualMachine):
            Use a Compute Engine VM image to start the
            managed notebook instance.

            This field is a member of `oneof`_ ``runtime_type``.
        state (google.cloud.notebooks_v1.types.Runtime.State):
            Output only. Runtime state.
        health_state (google.cloud.notebooks_v1.types.Runtime.HealthState):
            Output only. Runtime health_state.
        access_config (google.cloud.notebooks_v1.types.RuntimeAccessConfig):
            The config settings for accessing runtime.
        software_config (google.cloud.notebooks_v1.types.RuntimeSoftwareConfig):
            The config settings for software inside the
            runtime.
        metrics (google.cloud.notebooks_v1.types.RuntimeMetrics):
            Output only. Contains Runtime daemon metrics
            such as Service status and JupyterLab stats.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Runtime creation time.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Runtime update time.
    """

    class State(proto.Enum):
        r"""The definition of the states of this runtime.

        Values:
            STATE_UNSPECIFIED (0):
                State is not specified.
            STARTING (1):
                The compute layer is starting the runtime. It
                is not ready for use.
            PROVISIONING (2):
                The compute layer is installing required
                frameworks and registering the runtime with
                notebook proxy. It cannot be used.
            ACTIVE (3):
                The runtime is currently running. It is ready
                for use.
            STOPPING (4):
                The control logic is stopping the runtime. It
                cannot be used.
            STOPPED (5):
                The runtime is stopped. It cannot be used.
            DELETING (6):
                The runtime is being deleted. It cannot be
                used.
            UPGRADING (7):
                The runtime is upgrading. It cannot be used.
            INITIALIZING (8):
                The runtime is being created and set up. It
                is not ready for use.
        """

        STATE_UNSPECIFIED = 0
        STARTING = 1
        PROVISIONING = 2
        ACTIVE = 3
        STOPPING = 4
        STOPPED = 5
        DELETING = 6
        UPGRADING = 7
        INITIALIZING = 8

    class HealthState(proto.Enum):
        r"""The runtime substate.

        Values:
            HEALTH_STATE_UNSPECIFIED (0):
                The runtime substate is unknown.
            HEALTHY (1):
                The runtime is known to be in an healthy
                state (for example, critical daemons are
                running) Applies to ACTIVE state.
            UNHEALTHY (2):
                The runtime is known to be in an unhealthy
                state (for example, critical daemons are not
                running) Applies to ACTIVE state.
            AGENT_NOT_INSTALLED (3):
                The runtime has not installed health
                monitoring agent. Applies to ACTIVE state.
            AGENT_NOT_RUNNING (4):
                The runtime health monitoring agent is not
                running. Applies to ACTIVE state.
        """

        HEALTH_STATE_UNSPECIFIED = 0
        HEALTHY = 1
        UNHEALTHY = 2
        AGENT_NOT_INSTALLED = 3
        AGENT_NOT_RUNNING = 4

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    virtual_machine: "VirtualMachine" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="runtime_type",
        message="VirtualMachine",
    )
    state: State = proto.Field(
        proto.ENUM,
        number=3,
        enum=State,
    )
    health_state: HealthState = proto.Field(
        proto.ENUM,
        number=4,
        enum=HealthState,
    )
    access_config: "RuntimeAccessConfig" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="RuntimeAccessConfig",
    )
    software_config: "RuntimeSoftwareConfig" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="RuntimeSoftwareConfig",
    )
    metrics: "RuntimeMetrics" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="RuntimeMetrics",
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=20,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=21,
        message=timestamp_pb2.Timestamp,
    )


class RuntimeAcceleratorConfig(proto.Message):
    r"""Definition of the types of hardware accelerators that can be used.
    Definition of the types of hardware accelerators that can be used.
    See `Compute Engine
    AcceleratorTypes <https://cloud.google.com/compute/docs/reference/beta/acceleratorTypes>`__.
    Examples:

    - ``nvidia-tesla-k80``
    - ``nvidia-tesla-p100``
    - ``nvidia-tesla-v100``
    - ``nvidia-tesla-p4``
    - ``nvidia-tesla-t4``
    - ``nvidia-tesla-a100``

    Attributes:
        type_ (google.cloud.notebooks_v1.types.RuntimeAcceleratorConfig.AcceleratorType):
            Accelerator model.
        core_count (int):
            Count of cores of this accelerator.
    """

    class AcceleratorType(proto.Enum):
        r"""Type of this accelerator.

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
            NVIDIA_TESLA_A100 (6):
                Accelerator type is Nvidia Tesla A100.
            TPU_V2 (7):
                (Coming soon) Accelerator type is TPU V2.
            TPU_V3 (8):
                (Coming soon) Accelerator type is TPU V3.
            NVIDIA_TESLA_T4_VWS (9):
                Accelerator type is NVIDIA Tesla T4 Virtual
                Workstations.
            NVIDIA_TESLA_P100_VWS (10):
                Accelerator type is NVIDIA Tesla P100 Virtual
                Workstations.
            NVIDIA_TESLA_P4_VWS (11):
                Accelerator type is NVIDIA Tesla P4 Virtual
                Workstations.
        """

        ACCELERATOR_TYPE_UNSPECIFIED = 0
        NVIDIA_TESLA_K80 = 1
        NVIDIA_TESLA_P100 = 2
        NVIDIA_TESLA_V100 = 3
        NVIDIA_TESLA_P4 = 4
        NVIDIA_TESLA_T4 = 5
        NVIDIA_TESLA_A100 = 6
        TPU_V2 = 7
        TPU_V3 = 8
        NVIDIA_TESLA_T4_VWS = 9
        NVIDIA_TESLA_P100_VWS = 10
        NVIDIA_TESLA_P4_VWS = 11

    type_: AcceleratorType = proto.Field(
        proto.ENUM,
        number=1,
        enum=AcceleratorType,
    )
    core_count: int = proto.Field(
        proto.INT64,
        number=2,
    )


class EncryptionConfig(proto.Message):
    r"""Represents a custom encryption key configuration that can be
    applied to a resource. This will encrypt all disks in Virtual
    Machine.

    Attributes:
        kms_key (str):
            The Cloud KMS resource identifier of the customer-managed
            encryption key used to protect a resource, such as a disks.
            It has the following format:
            ``projects/{PROJECT_ID}/locations/{REGION}/keyRings/{KEY_RING_NAME}/cryptoKeys/{KEY_NAME}``
    """

    kms_key: str = proto.Field(
        proto.STRING,
        number=1,
    )


class LocalDisk(proto.Message):
    r"""A Local attached disk resource.

    Attributes:
        auto_delete (bool):
            Optional. Output only. Specifies whether the
            disk will be auto-deleted when the instance is
            deleted (but not when the disk is detached from
            the instance).
        boot (bool):
            Optional. Output only. Indicates that this is
            a boot disk. The virtual machine will use the
            first partition of the disk for its root
            filesystem.
        device_name (str):
            Optional. Output only. Specifies a unique device name of
            your choice that is reflected into the
            ``/dev/disk/by-id/google-*`` tree of a Linux operating
            system running within the instance. This name can be used to
            reference the device for mounting, resizing, and so on, from
            within the instance.

            If not specified, the server chooses a default device name
            to apply to this disk, in the form persistent-disk-x, where
            x is a number assigned by Google Compute Engine. This field
            is only applicable for persistent disks.
        guest_os_features (MutableSequence[google.cloud.notebooks_v1.types.LocalDisk.RuntimeGuestOsFeature]):
            Output only. Indicates a list of features to
            enable on the guest operating system. Applicable
            only for bootable images. Read  Enabling guest
            operating system features to see a list of
            available options.
        index (int):
            Output only. A zero-based index to this disk,
            where 0 is reserved for the boot disk. If you
            have many disks attached to an instance, each
            disk would have a unique index number.
        initialize_params (google.cloud.notebooks_v1.types.LocalDiskInitializeParams):
            Input only. Specifies the parameters for a
            new disk that will be created alongside the new
            instance. Use initialization parameters to
            create boot disks or local SSDs attached to the
            new instance.

            This property is mutually exclusive with the
            source property; you can only define one or the
            other, but not both.
        interface (str):
            Specifies the disk interface to use for attaching this disk,
            which is either SCSI or NVME. The default is SCSI.
            Persistent disks must always use SCSI and the request will
            fail if you attempt to attach a persistent disk in any other
            format than SCSI. Local SSDs can use either NVME or SCSI.
            For performance characteristics of SCSI over NVMe, see Local
            SSD performance. Valid values:

            - ``NVME``
            - ``SCSI``
        kind (str):
            Output only. Type of the resource. Always
            compute#attachedDisk for attached disks.
        licenses (MutableSequence[str]):
            Output only. Any valid publicly visible
            licenses.
        mode (str):
            The mode in which to attach this disk, either ``READ_WRITE``
            or ``READ_ONLY``. If not specified, the default is to attach
            the disk in ``READ_WRITE`` mode. Valid values:

            - ``READ_ONLY``
            - ``READ_WRITE``
        source (str):
            Specifies a valid partial or full URL to an
            existing Persistent Disk resource.
        type_ (str):
            Specifies the type of the disk, either ``SCRATCH`` or
            ``PERSISTENT``. If not specified, the default is
            ``PERSISTENT``. Valid values:

            - ``PERSISTENT``
            - ``SCRATCH``
    """

    class RuntimeGuestOsFeature(proto.Message):
        r"""Optional. A list of features to enable on the guest operating
        system. Applicable only for bootable images. Read `Enabling guest
        operating system
        features <https://cloud.google.com/compute/docs/images/create-delete-deprecate-private-images#guest-os-features>`__
        to see a list of available options. Guest OS features for boot disk.

        Attributes:
            type_ (str):
                The ID of a supported feature. Read `Enabling guest
                operating system
                features <https://cloud.google.com/compute/docs/images/create-delete-deprecate-private-images#guest-os-features>`__
                to see a list of available options.

                Valid values:

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
    guest_os_features: MutableSequence[RuntimeGuestOsFeature] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=RuntimeGuestOsFeature,
    )
    index: int = proto.Field(
        proto.INT32,
        number=5,
    )
    initialize_params: "LocalDiskInitializeParams" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="LocalDiskInitializeParams",
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


class LocalDiskInitializeParams(proto.Message):
    r"""Input only. Specifies the parameters for a new disk that will
    be created alongside the new instance. Use initialization
    parameters to create boot disks or local SSDs attached to the
    new runtime.
    This property is mutually exclusive with the source property;
    you can only define one or the other, but not both.

    Attributes:
        description (str):
            Optional. Provide this property when creating
            the disk.
        disk_name (str):
            Optional. Specifies the disk name. If not
            specified, the default is to use the name of the
            instance. If the disk with the instance name
            exists already in the given zone/region, a new
            name will be automatically generated.
        disk_size_gb (int):
            Optional. Specifies the size of the disk in
            base-2 GB. If not specified, the disk will be
            the same size as the image (usually 10GB). If
            specified, the size must be equal to or larger
            than 10GB. Default 100 GB.
        disk_type (google.cloud.notebooks_v1.types.LocalDiskInitializeParams.DiskType):
            Input only. The type of the boot disk attached to this
            instance, defaults to standard persistent disk
            (``PD_STANDARD``).
        labels (MutableMapping[str, str]):
            Optional. Labels to apply to this disk. These
            can be later modified by the disks.setLabels
            method. This field is only applicable for
            persistent disks.
    """

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

    description: str = proto.Field(
        proto.STRING,
        number=1,
    )
    disk_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    disk_size_gb: int = proto.Field(
        proto.INT64,
        number=3,
    )
    disk_type: DiskType = proto.Field(
        proto.ENUM,
        number=4,
        enum=DiskType,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )


class RuntimeAccessConfig(proto.Message):
    r"""Specifies the login configuration for Runtime

    Attributes:
        access_type (google.cloud.notebooks_v1.types.RuntimeAccessConfig.RuntimeAccessType):
            The type of access mode this instance.
        runtime_owner (str):
            The owner of this runtime after creation. Format:
            ``alias@example.com`` Currently supports one owner only.
        proxy_uri (str):
            Output only. The proxy endpoint that is used
            to access the runtime.
    """

    class RuntimeAccessType(proto.Enum):
        r"""Possible ways to access runtime. Authentication mode.
        Currently supports: Single User only.

        Values:
            RUNTIME_ACCESS_TYPE_UNSPECIFIED (0):
                Unspecified access.
            SINGLE_USER (1):
                Single user login.
            SERVICE_ACCOUNT (2):
                Service Account mode.
                In Service Account mode, Runtime creator will
                specify a SA that exists in the consumer
                project. Using Runtime Service Account field.
                Users accessing the Runtime need ActAs (Service
                Account User) permission.
        """

        RUNTIME_ACCESS_TYPE_UNSPECIFIED = 0
        SINGLE_USER = 1
        SERVICE_ACCOUNT = 2

    access_type: RuntimeAccessType = proto.Field(
        proto.ENUM,
        number=1,
        enum=RuntimeAccessType,
    )
    runtime_owner: str = proto.Field(
        proto.STRING,
        number=2,
    )
    proxy_uri: str = proto.Field(
        proto.STRING,
        number=3,
    )


class RuntimeSoftwareConfig(proto.Message):
    r"""Specifies the selection and configuration of software inside the
    runtime. The properties to set on runtime. Properties keys are
    specified in ``key:value`` format, for example:

    - ``idle_shutdown: true``
    - ``idle_shutdown_timeout: 180``
    - ``enable_health_monitoring: true``


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        notebook_upgrade_schedule (str):
            Cron expression in UTC timezone, used to schedule instance
            auto upgrade. Please follow the `cron
            format <https://en.wikipedia.org/wiki/Cron>`__.
        enable_health_monitoring (bool):
            Verifies core internal services are running.
            Default: True

            This field is a member of `oneof`_ ``_enable_health_monitoring``.
        idle_shutdown (bool):
            Runtime will automatically shutdown after
            idle_shutdown_time. Default: True

            This field is a member of `oneof`_ ``_idle_shutdown``.
        idle_shutdown_timeout (int):
            Time in minutes to wait before shutting down
            runtime. Default: 180 minutes
        install_gpu_driver (bool):
            Install Nvidia Driver automatically.
            Default: True
        custom_gpu_driver_path (str):
            Specify a custom Cloud Storage path where the
            GPU driver is stored. If not specified, we'll
            automatically choose from official GPU drivers.
        post_startup_script (str):
            Path to a Bash script that automatically runs after a
            notebook instance fully boots up. The path must be a URL or
            Cloud Storage path (``gs://path-to-file/file-name``).
        kernels (MutableSequence[google.cloud.notebooks_v1.types.ContainerImage]):
            Optional. Use a list of container images to
            use as Kernels in the notebook instance.
        upgradeable (bool):
            Output only. Bool indicating whether an newer
            image is available in an image family.

            This field is a member of `oneof`_ ``_upgradeable``.
        post_startup_script_behavior (google.cloud.notebooks_v1.types.RuntimeSoftwareConfig.PostStartupScriptBehavior):
            Behavior for the post startup script.
        disable_terminal (bool):
            Bool indicating whether JupyterLab terminal
            will be available or not. Default: False

            This field is a member of `oneof`_ ``_disable_terminal``.
        version (str):
            Output only. version of boot image such as
            M100, from release label of the image.

            This field is a member of `oneof`_ ``_version``.
    """

    class PostStartupScriptBehavior(proto.Enum):
        r"""Behavior for the post startup script.

        Values:
            POST_STARTUP_SCRIPT_BEHAVIOR_UNSPECIFIED (0):
                Unspecified post startup script behavior.
                Will run only once at creation.
            RUN_EVERY_START (1):
                Runs the post startup script provided during
                creation at every start.
            DOWNLOAD_AND_RUN_EVERY_START (2):
                Downloads and runs the provided post startup
                script at every start.
        """

        POST_STARTUP_SCRIPT_BEHAVIOR_UNSPECIFIED = 0
        RUN_EVERY_START = 1
        DOWNLOAD_AND_RUN_EVERY_START = 2

    notebook_upgrade_schedule: str = proto.Field(
        proto.STRING,
        number=1,
    )
    enable_health_monitoring: bool = proto.Field(
        proto.BOOL,
        number=2,
        optional=True,
    )
    idle_shutdown: bool = proto.Field(
        proto.BOOL,
        number=3,
        optional=True,
    )
    idle_shutdown_timeout: int = proto.Field(
        proto.INT32,
        number=4,
    )
    install_gpu_driver: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    custom_gpu_driver_path: str = proto.Field(
        proto.STRING,
        number=6,
    )
    post_startup_script: str = proto.Field(
        proto.STRING,
        number=7,
    )
    kernels: MutableSequence[environment.ContainerImage] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message=environment.ContainerImage,
    )
    upgradeable: bool = proto.Field(
        proto.BOOL,
        number=9,
        optional=True,
    )
    post_startup_script_behavior: PostStartupScriptBehavior = proto.Field(
        proto.ENUM,
        number=10,
        enum=PostStartupScriptBehavior,
    )
    disable_terminal: bool = proto.Field(
        proto.BOOL,
        number=11,
        optional=True,
    )
    version: str = proto.Field(
        proto.STRING,
        number=12,
        optional=True,
    )


class RuntimeMetrics(proto.Message):
    r"""Contains runtime daemon metrics, such as OS and kernels and
    sessions stats.

    Attributes:
        system_metrics (MutableMapping[str, str]):
            Output only. The system metrics.
    """

    system_metrics: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=1,
    )


class RuntimeShieldedInstanceConfig(proto.Message):
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


class VirtualMachine(proto.Message):
    r"""Runtime using Virtual Machine for computing.

    Attributes:
        instance_name (str):
            Output only. The user-friendly name of the
            Managed Compute Engine instance.
        instance_id (str):
            Output only. The unique identifier of the
            Managed Compute Engine instance.
        virtual_machine_config (google.cloud.notebooks_v1.types.VirtualMachineConfig):
            Virtual Machine configuration settings.
    """

    instance_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    instance_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    virtual_machine_config: "VirtualMachineConfig" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="VirtualMachineConfig",
    )


class VirtualMachineConfig(proto.Message):
    r"""The config settings for virtual machine.

    Attributes:
        zone (str):
            Output only. The zone where the virtual machine is located.
            If using regional request, the notebooks service will pick a
            location in the corresponding runtime region. On a get
            request, zone will always be present. Example:

            - ``us-central1-b``
        machine_type (str):
            Required. The Compute Engine machine type used for runtimes.
            Short name is valid. Examples:

            - ``n1-standard-2``
            - ``e2-standard-8``
        container_images (MutableSequence[google.cloud.notebooks_v1.types.ContainerImage]):
            Optional. Use a list of container images to
            use as Kernels in the notebook instance.
        data_disk (google.cloud.notebooks_v1.types.LocalDisk):
            Required. Data disk option configuration
            settings.
        encryption_config (google.cloud.notebooks_v1.types.EncryptionConfig):
            Optional. Encryption settings for virtual
            machine data disk.
        shielded_instance_config (google.cloud.notebooks_v1.types.RuntimeShieldedInstanceConfig):
            Optional. Shielded VM Instance configuration
            settings.
        accelerator_config (google.cloud.notebooks_v1.types.RuntimeAcceleratorConfig):
            Optional. The Compute Engine accelerator
            configuration for this runtime.
        network (str):
            Optional. The Compute Engine network to be used for machine
            communications. Cannot be specified with subnetwork. If
            neither ``network`` nor ``subnet`` is specified, the
            "default" network of the project is used, if it exists.

            A full URL or partial URI. Examples:

            - ``https://www.googleapis.com/compute/v1/projects/[project_id]/global/networks/default``
            - ``projects/[project_id]/global/networks/default``

            Runtimes are managed resources inside Google Infrastructure.
            Runtimes support the following network configurations:

            - Google Managed Network (Network & subnet are empty)
            - Consumer Project VPC (network & subnet are required).
              Requires configuring Private Service Access.
            - Shared VPC (network & subnet are required). Requires
              configuring Private Service Access.
        subnet (str):
            Optional. The Compute Engine subnetwork to be used for
            machine communications. Cannot be specified with network.

            A full URL or partial URI are valid. Examples:

            - ``https://www.googleapis.com/compute/v1/projects/[project_id]/regions/us-east1/subnetworks/sub0``
            - ``projects/[project_id]/regions/us-east1/subnetworks/sub0``
        internal_ip_only (bool):
            Optional. If true, runtime will only have internal IP
            addresses. By default, runtimes are not restricted to
            internal IP addresses, and will have ephemeral external IP
            addresses assigned to each vm. This ``internal_ip_only``
            restriction can only be enabled for subnetwork enabled
            networks, and all dependencies must be configured to be
            accessible without external IP addresses.
        tags (MutableSequence[str]):
            Optional. The Compute Engine tags to add to runtime (see
            `Tagging
            instances <https://cloud.google.com/compute/docs/label-or-tag-resources#tags>`__).
        guest_attributes (MutableMapping[str, str]):
            Output only. The Compute Engine guest attributes. (see
            `Project and instance guest
            attributes <https://cloud.google.com/compute/docs/storing-retrieving-metadata#guest_attributes>`__).
        metadata (MutableMapping[str, str]):
            Optional. The Compute Engine metadata entries to add to
            virtual machine. (see `Project and instance
            metadata <https://cloud.google.com/compute/docs/storing-retrieving-metadata#project_and_instance_metadata>`__).
        labels (MutableMapping[str, str]):
            Optional. The labels to associate with this runtime. Label
            **keys** must contain 1 to 63 characters, and must conform
            to `RFC 1035 <https://www.ietf.org/rfc/rfc1035.txt>`__.
            Label **values** may be empty, but, if present, must contain
            1 to 63 characters, and must conform to `RFC
            1035 <https://www.ietf.org/rfc/rfc1035.txt>`__. No more than
            32 labels can be associated with a cluster.
        nic_type (google.cloud.notebooks_v1.types.VirtualMachineConfig.NicType):
            Optional. The type of vNIC to be used on this
            interface. This may be gVNIC or VirtioNet.
        reserved_ip_range (str):
            Optional. Reserved IP Range name is used for VPC Peering.
            The subnetwork allocation will use the range *name* if it's
            assigned.

            Example: managed-notebooks-range-c

            ::

                PEERING_RANGE_NAME_3=managed-notebooks-range-c
                gcloud compute addresses create $PEERING_RANGE_NAME_3 \
                  --global \
                  --prefix-length=24 \
                  --description="Google Cloud Managed Notebooks Range 24 c" \
                  --network=$NETWORK \
                  --addresses=192.168.0.0 \
                  --purpose=VPC_PEERING

            Field value will be: ``managed-notebooks-range-c``
        boot_image (google.cloud.notebooks_v1.types.VirtualMachineConfig.BootImage):
            Optional. Boot image metadata used for
            runtime upgradeability.
    """

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

    class BootImage(proto.Message):
        r"""Definition of the boot image used by the Runtime.
        Used to facilitate runtime upgradeability.

        """

    zone: str = proto.Field(
        proto.STRING,
        number=1,
    )
    machine_type: str = proto.Field(
        proto.STRING,
        number=2,
    )
    container_images: MutableSequence[environment.ContainerImage] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=environment.ContainerImage,
    )
    data_disk: "LocalDisk" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="LocalDisk",
    )
    encryption_config: "EncryptionConfig" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="EncryptionConfig",
    )
    shielded_instance_config: "RuntimeShieldedInstanceConfig" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="RuntimeShieldedInstanceConfig",
    )
    accelerator_config: "RuntimeAcceleratorConfig" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="RuntimeAcceleratorConfig",
    )
    network: str = proto.Field(
        proto.STRING,
        number=8,
    )
    subnet: str = proto.Field(
        proto.STRING,
        number=9,
    )
    internal_ip_only: bool = proto.Field(
        proto.BOOL,
        number=10,
    )
    tags: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=13,
    )
    guest_attributes: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=14,
    )
    metadata: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=15,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=16,
    )
    nic_type: NicType = proto.Field(
        proto.ENUM,
        number=17,
        enum=NicType,
    )
    reserved_ip_range: str = proto.Field(
        proto.STRING,
        number=18,
    )
    boot_image: BootImage = proto.Field(
        proto.MESSAGE,
        number=19,
        message=BootImage,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
