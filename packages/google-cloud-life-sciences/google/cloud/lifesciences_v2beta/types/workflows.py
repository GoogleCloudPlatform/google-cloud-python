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
import google.rpc.code_pb2 as code_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.lifesciences.v2beta",
    manifest={
        "RunPipelineRequest",
        "RunPipelineResponse",
        "Pipeline",
        "Action",
        "Secret",
        "Mount",
        "Resources",
        "VirtualMachine",
        "ServiceAccount",
        "Accelerator",
        "Network",
        "Disk",
        "Volume",
        "PersistentDisk",
        "ExistingDisk",
        "NFSMount",
        "Metadata",
        "Event",
        "DelayedEvent",
        "WorkerAssignedEvent",
        "WorkerReleasedEvent",
        "PullStartedEvent",
        "PullStoppedEvent",
        "ContainerStartedEvent",
        "ContainerStoppedEvent",
        "UnexpectedExitStatusEvent",
        "ContainerKilledEvent",
        "FailedEvent",
    },
)


class RunPipelineRequest(proto.Message):
    r"""The arguments to the ``RunPipeline`` method. The requesting user
    must have the ``iam.serviceAccounts.actAs`` permission for the Cloud
    Life Sciences service account or the request will fail.

    Attributes:
        parent (str):
            The project and location that this request
            should be executed against.
        pipeline (google.cloud.lifesciences_v2beta.types.Pipeline):
            Required. The description of the pipeline to
            run.
        labels (MutableMapping[str, str]):
            User-defined labels to associate with the returned
            operation. These labels are not propagated to any Google
            Cloud Platform resources used by the operation, and can be
            modified at any time.

            To associate labels with resources created while executing
            the operation, see the appropriate resource message (for
            example, ``VirtualMachine``).
        pub_sub_topic (str):
            The name of an existing Pub/Sub topic.  The
            server will publish messages to this topic
            whenever the status of the operation changes.
            The Life Sciences Service Agent account must
            have publisher permissions to the specified
            topic or notifications will not be sent.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=4,
    )
    pipeline: "Pipeline" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Pipeline",
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=2,
    )
    pub_sub_topic: str = proto.Field(
        proto.STRING,
        number=3,
    )


class RunPipelineResponse(proto.Message):
    r"""The response to the RunPipeline method, returned in the
    operation's result field on success.

    """


class Pipeline(proto.Message):
    r"""Specifies a series of actions to execute, expressed as Docker
    containers.

    Attributes:
        actions (MutableSequence[google.cloud.lifesciences_v2beta.types.Action]):
            The list of actions to execute, in the order
            they are specified.
        resources (google.cloud.lifesciences_v2beta.types.Resources):
            The resources required for execution.
        environment (MutableMapping[str, str]):
            The environment to pass into every action.
            Each action can also specify additional
            environment variables but cannot delete an entry
            from this map (though they can overwrite it with
            a different value).
        encrypted_environment (google.cloud.lifesciences_v2beta.types.Secret):
            The encrypted environment to pass into every action. Each
            action can also specify its own encrypted environment.

            The secret must decrypt to a JSON-encoded dictionary where
            key-value pairs serve as environment variable names and
            their values. The decoded environment variables can
            overwrite the values specified by the ``environment`` field.
        timeout (google.protobuf.duration_pb2.Duration):
            The maximum amount of time to give the pipeline to complete.
            This includes the time spent waiting for a worker to be
            allocated. If the pipeline fails to complete before the
            timeout, it will be cancelled and the error code will be set
            to DEADLINE_EXCEEDED.

            If unspecified, it will default to 7 days.
    """

    actions: MutableSequence["Action"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Action",
    )
    resources: "Resources" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Resources",
    )
    environment: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=3,
    )
    encrypted_environment: "Secret" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="Secret",
    )
    timeout: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=4,
        message=duration_pb2.Duration,
    )


class Action(proto.Message):
    r"""Specifies a single action that runs a Docker container.

    Attributes:
        container_name (str):
            An optional name for the container. The
            container hostname will be set to this name,
            making it useful for inter-container
            communication. The name must contain only upper
            and lowercase alphanumeric characters and
            hyphens and cannot start with a hyphen.
        image_uri (str):
            Required. The URI to pull the container image from. Note
            that all images referenced by actions in the pipeline are
            pulled before the first action runs. If multiple actions
            reference the same image, it is only pulled once, ensuring
            that the same image is used for all actions in a single
            pipeline.

            The image URI can be either a complete host and image
            specification (e.g., quay.io/biocontainers/samtools), a
            library and image name (e.g., google/cloud-sdk) or a bare
            image name ('bash') to pull from the default library. No
            schema is required in any of these cases.

            If the specified image is not public, the service account
            specified for the Virtual Machine must have access to pull
            the images from GCR, or appropriate credentials must be
            specified in the
            [google.cloud.lifesciences.v2beta.Action.credentials][google.cloud.lifesciences.v2beta.Action.credentials]
            field.
        commands (MutableSequence[str]):
            If specified, overrides the ``CMD`` specified in the
            container. If the container also has an ``ENTRYPOINT`` the
            values are used as entrypoint arguments. Otherwise, they are
            used as a command and arguments to run inside the container.
        entrypoint (str):
            If specified, overrides the ``ENTRYPOINT`` specified in the
            container.
        environment (MutableMapping[str, str]):
            The environment to pass into the container. This environment
            is merged with values specified in the
            [google.cloud.lifesciences.v2beta.Pipeline][google.cloud.lifesciences.v2beta.Pipeline]
            message, overwriting any duplicate values.

            In addition to the values passed here, a few other values
            are automatically injected into the environment. These
            cannot be hidden or overwritten.

            ``GOOGLE_PIPELINE_FAILED`` will be set to "1" if the
            pipeline failed because an action has exited with a non-zero
            status (and did not have the ``IGNORE_EXIT_STATUS`` flag
            set). This can be used to determine if additional debug or
            logging actions should execute.

            ``GOOGLE_LAST_EXIT_STATUS`` will be set to the exit status
            of the last non-background action that executed. This can be
            used by workflow engine authors to determine whether an
            individual action has succeeded or failed.
        encrypted_environment (google.cloud.lifesciences_v2beta.types.Secret):
            The encrypted environment to pass into the container. This
            environment is merged with values specified in the
            [google.cloud.lifesciences.v2beta.Pipeline][google.cloud.lifesciences.v2beta.Pipeline]
            message, overwriting any duplicate values.

            The secret must decrypt to a JSON-encoded dictionary where
            key-value pairs serve as environment variable names and
            their values. The decoded environment variables can
            overwrite the values specified by the ``environment`` field.
        pid_namespace (str):
            An optional identifier for a PID namespace to
            run the action inside. Multiple actions should
            use the same string to share a namespace.  If
            unspecified, a separate isolated namespace is
            used.
        port_mappings (MutableMapping[int, int]):
            A map of containers to host port mappings for this
            container. If the container already specifies exposed ports,
            use the ``PUBLISH_EXPOSED_PORTS`` flag instead.

            The host port number must be less than 65536. If it is zero,
            an unused random port is assigned. To determine the
            resulting port number, consult the ``ContainerStartedEvent``
            in the operation metadata.
        mounts (MutableSequence[google.cloud.lifesciences_v2beta.types.Mount]):
            A list of mounts to make available to the action.

            In addition to the values specified here, every action has a
            special virtual disk mounted under ``/google`` that contains
            log files and other operational components.

            .. raw:: html

                <ul>
                  <li><code>/google/logs</code> All logs written during the pipeline
                  execution.</li>
                  <li><code>/google/logs/output</code> The combined standard output and
                  standard error of all actions run as part of the pipeline
                  execution.</li>
                  <li><code>/google/logs/action/*/stdout</code> The complete contents of
                  each individual action's standard output.</li>
                  <li><code>/google/logs/action/*/stderr</code> The complete contents of
                  each individual action's standard error output.</li>
                </ul>
        labels (MutableMapping[str, str]):
            Labels to associate with the action. This
            field is provided to assist workflow engine
            authors in identifying actions (for example, to
            indicate what sort of action they perform, such
            as localization or debugging). They are returned
            in the operation metadata, but are otherwise
            ignored.
        credentials (google.cloud.lifesciences_v2beta.types.Secret):
            If the specified image is hosted on a private registry other
            than Google Container Registry, the credentials required to
            pull the image must be specified here as an encrypted
            secret.

            The secret must decrypt to a JSON-encoded dictionary
            containing both ``username`` and ``password`` keys.
        timeout (google.protobuf.duration_pb2.Duration):
            The maximum amount of time to give the action to complete.
            If the action fails to complete before the timeout, it will
            be terminated and the exit status will be non-zero. The
            pipeline will continue or terminate based on the rules
            defined by the ``ALWAYS_RUN`` and ``IGNORE_EXIT_STATUS``
            flags.
        ignore_exit_status (bool):
            Normally, a non-zero exit status causes the
            pipeline to fail. This flag allows execution of
            other actions to continue instead.
        run_in_background (bool):
            This flag allows an action to continue
            running in the background while executing
            subsequent actions. This is useful to provide
            services to other actions (or to provide
            debugging support tools like SSH servers).
        always_run (bool):
            By default, after an action fails, no further
            actions are run. This flag indicates that this
            action must be run even if the pipeline has
            already failed. This is useful for actions that
            copy output files off of the VM or for
            debugging. Note that no actions will be run if
            image prefetching fails.
        enable_fuse (bool):
            Enable access to the FUSE device for this action.
            Filesystems can then be mounted into disks shared with other
            actions. The other actions do not need the ``enable_fuse``
            flag to access the mounted filesystem.

            This has the effect of causing the container to be executed
            with ``CAP_SYS_ADMIN`` and exposes ``/dev/fuse`` to the
            container, so use it only for containers you trust.
        publish_exposed_ports (bool):
            Exposes all ports specified by ``EXPOSE`` statements in the
            container. To discover the host side port numbers, consult
            the ``ACTION_STARTED`` event in the operation metadata.
        disable_image_prefetch (bool):
            All container images are typically downloaded
            before any actions are executed. This helps
            prevent typos in URIs or issues like lack of
            disk space from wasting large amounts of compute
            resources.

            If set, this flag prevents the worker from
            downloading the image until just before the
            action is executed.
        disable_standard_error_capture (bool):
            A small portion of the container's standard error stream is
            typically captured and returned inside the
            ``ContainerStoppedEvent``. Setting this flag disables this
            functionality.
        block_external_network (bool):
            Prevents the container from accessing the
            external network.
    """

    container_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    image_uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    commands: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    entrypoint: str = proto.Field(
        proto.STRING,
        number=4,
    )
    environment: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )
    encrypted_environment: "Secret" = proto.Field(
        proto.MESSAGE,
        number=21,
        message="Secret",
    )
    pid_namespace: str = proto.Field(
        proto.STRING,
        number=6,
    )
    port_mappings: MutableMapping[int, int] = proto.MapField(
        proto.INT32,
        proto.INT32,
        number=8,
    )
    mounts: MutableSequence["Mount"] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message="Mount",
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=10,
    )
    credentials: "Secret" = proto.Field(
        proto.MESSAGE,
        number=11,
        message="Secret",
    )
    timeout: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=12,
        message=duration_pb2.Duration,
    )
    ignore_exit_status: bool = proto.Field(
        proto.BOOL,
        number=13,
    )
    run_in_background: bool = proto.Field(
        proto.BOOL,
        number=14,
    )
    always_run: bool = proto.Field(
        proto.BOOL,
        number=15,
    )
    enable_fuse: bool = proto.Field(
        proto.BOOL,
        number=16,
    )
    publish_exposed_ports: bool = proto.Field(
        proto.BOOL,
        number=17,
    )
    disable_image_prefetch: bool = proto.Field(
        proto.BOOL,
        number=18,
    )
    disable_standard_error_capture: bool = proto.Field(
        proto.BOOL,
        number=19,
    )
    block_external_network: bool = proto.Field(
        proto.BOOL,
        number=20,
    )


class Secret(proto.Message):
    r"""Holds encrypted information that is only decrypted and stored
    in RAM by the worker VM when running the pipeline.

    Attributes:
        key_name (str):
            The name of the Cloud KMS key that will be used to decrypt
            the secret value. The VM service account must have the
            required permissions and authentication scopes to invoke the
            ``decrypt`` method on the specified key.
        cipher_text (str):
            The value of the cipherText response from the ``encrypt``
            method. This field is intentionally unaudited.
    """

    key_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    cipher_text: str = proto.Field(
        proto.STRING,
        number=2,
    )


class Mount(proto.Message):
    r"""Carries information about a particular disk mount inside a
    container.

    Attributes:
        disk (str):
            The name of the disk to mount, as specified
            in the resources section.
        path (str):
            The path to mount the disk inside the
            container.
        read_only (bool):
            If true, the disk is mounted read-only inside
            the container.
    """

    disk: str = proto.Field(
        proto.STRING,
        number=1,
    )
    path: str = proto.Field(
        proto.STRING,
        number=2,
    )
    read_only: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class Resources(proto.Message):
    r"""The system resources for the pipeline run.

    At least one zone or region must be specified or the pipeline
    run will fail.

    Attributes:
        regions (MutableSequence[str]):
            The list of regions allowed for VM allocation. If set, the
            ``zones`` field must not be set.
        zones (MutableSequence[str]):
            The list of zones allowed for VM allocation. If set, the
            ``regions`` field must not be set.
        virtual_machine (google.cloud.lifesciences_v2beta.types.VirtualMachine):
            The virtual machine specification.
    """

    regions: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    zones: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    virtual_machine: "VirtualMachine" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="VirtualMachine",
    )


class VirtualMachine(proto.Message):
    r"""Carries information about a Compute Engine VM resource.

    Attributes:
        machine_type (str):
            Required. The machine type of the virtual machine to create.
            Must be the short name of a standard machine type (such as
            "n1-standard-1") or a custom machine type (such as
            "custom-1-4096", where "1" indicates the number of vCPUs and
            "4096" indicates the memory in MB). See `Creating an
            instance with a custom machine
            type <https://cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type#create>`__
            for more specifications on creating a custom machine type.
        preemptible (bool):
            If true, allocate a preemptible VM.
        labels (MutableMapping[str, str]):
            Optional set of labels to apply to the VM and any attached
            disk resources. These labels must adhere to the `name and
            value
            restrictions <https://cloud.google.com/compute/docs/labeling-resources>`__
            on VM labels imposed by Compute Engine.

            Labels keys with the prefix 'google-' are reserved for use
            by Google.

            Labels applied at creation time to the VM. Applied on a
            best-effort basis to attached disk resources shortly after
            VM creation.
        disks (MutableSequence[google.cloud.lifesciences_v2beta.types.Disk]):
            The list of disks to create and attach to the VM.

            Specify either the ``volumes[]`` field or the ``disks[]``
            field, but not both.
        network (google.cloud.lifesciences_v2beta.types.Network):
            The VM network configuration.
        accelerators (MutableSequence[google.cloud.lifesciences_v2beta.types.Accelerator]):
            The list of accelerators to attach to the VM.
        service_account (google.cloud.lifesciences_v2beta.types.ServiceAccount):
            The service account to install on the VM.
            This account does not need any permissions other
            than those required by the pipeline.
        boot_disk_size_gb (int):
            The size of the boot disk, in GB. The boot
            disk must be large enough to accommodate all of
            the Docker images from each action in the
            pipeline at the same time. If not specified, a
            small but reasonable default value is used.
        cpu_platform (str):
            The CPU platform to request. An instance
            based on a newer platform can be allocated, but
            never one with fewer capabilities. The value of
            this parameter must be a valid Compute Engine
            CPU platform name (such as "Intel Skylake").
            This parameter is only useful for carefully
            optimized work loads where the CPU platform has
            a significant impact.

            For more information about the effect of this
            parameter, see
            https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform.
        boot_image (str):
            The host operating system image to use.

            Currently, only Container-Optimized OS images can be used.

            The default value is
            ``projects/cos-cloud/global/images/family/cos-stable``,
            which selects the latest stable release of
            Container-Optimized OS.

            This option is provided to allow testing against the beta
            release of the operating system to ensure that the new
            version does not interact negatively with production
            pipelines.

            To test a pipeline against the beta release of
            Container-Optimized OS, use the value
            ``projects/cos-cloud/global/images/family/cos-beta``.
        nvidia_driver_version (str):
            The NVIDIA driver version to use when attaching an NVIDIA
            GPU accelerator. The version specified here must be
            compatible with the GPU libraries contained in the container
            being executed, and must be one of the drivers hosted in the
            ``nvidia-drivers-us-public`` bucket on Google Cloud Storage.
        enable_stackdriver_monitoring (bool):
            Whether Stackdriver monitoring should be
            enabled on the VM.
        docker_cache_images (MutableSequence[str]):
            The Compute Engine Disk Images to use as a Docker cache. The
            disks will be mounted into the Docker folder in a way that
            the images present in the cache will not need to be pulled.
            The digests of the cached images must match those of the
            tags used or the latest version will still be pulled. The
            root directory of the ext4 image must contain ``image`` and
            ``overlay2`` directories copied from the Docker directory of
            a VM where the desired Docker images have already been
            pulled. Any images pulled that are not cached will be stored
            on the first cache disk instead of the boot disk. Only a
            single image is supported.
        volumes (MutableSequence[google.cloud.lifesciences_v2beta.types.Volume]):
            The list of disks and other storage to create or attach to
            the VM.

            Specify either the ``volumes[]`` field or the ``disks[]``
            field, but not both.
        reservation (str):
            If specified, the VM will only be allocated
            inside the matching reservation. It will fail if
            the VM parameters don't match the reservation.
    """

    machine_type: str = proto.Field(
        proto.STRING,
        number=1,
    )
    preemptible: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=3,
    )
    disks: MutableSequence["Disk"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="Disk",
    )
    network: "Network" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="Network",
    )
    accelerators: MutableSequence["Accelerator"] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message="Accelerator",
    )
    service_account: "ServiceAccount" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="ServiceAccount",
    )
    boot_disk_size_gb: int = proto.Field(
        proto.INT32,
        number=8,
    )
    cpu_platform: str = proto.Field(
        proto.STRING,
        number=9,
    )
    boot_image: str = proto.Field(
        proto.STRING,
        number=10,
    )
    nvidia_driver_version: str = proto.Field(
        proto.STRING,
        number=11,
    )
    enable_stackdriver_monitoring: bool = proto.Field(
        proto.BOOL,
        number=12,
    )
    docker_cache_images: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=13,
    )
    volumes: MutableSequence["Volume"] = proto.RepeatedField(
        proto.MESSAGE,
        number=14,
        message="Volume",
    )
    reservation: str = proto.Field(
        proto.STRING,
        number=15,
    )


class ServiceAccount(proto.Message):
    r"""Carries information about a Google Cloud service account.

    Attributes:
        email (str):
            Email address of the service account. If not
            specified, the default Compute Engine service
            account for the project will be used.
        scopes (MutableSequence[str]):
            List of scopes to be enabled for this service
            account on the VM, in addition to the
            cloud-platform API scope that will be added by
            default.
    """

    email: str = proto.Field(
        proto.STRING,
        number=1,
    )
    scopes: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class Accelerator(proto.Message):
    r"""Carries information about an accelerator that can be attached
    to a VM.

    Attributes:
        type_ (str):
            The accelerator type string (for example,
            "nvidia-tesla-t4").

            Only NVIDIA GPU accelerators are currently supported. If an
            NVIDIA GPU is attached, the required runtime libraries will
            be made available to all containers under
            ``/usr/local/nvidia``. The driver version to install must be
            specified using the NVIDIA driver version parameter on the
            virtual machine specification. Note that attaching a GPU
            increases the worker VM startup time by a few minutes.
        count (int):
            How many accelerators of this type to attach.
    """

    type_: str = proto.Field(
        proto.STRING,
        number=1,
    )
    count: int = proto.Field(
        proto.INT64,
        number=2,
    )


class Network(proto.Message):
    r"""VM networking options.

    Attributes:
        network (str):
            The network name to attach the VM's network interface to.
            The value will be prefixed with ``global/networks/`` unless
            it contains a ``/``, in which case it is assumed to be a
            fully specified network resource URL.

            If unspecified, the global default network is used.
        use_private_address (bool):
            If set to true, do not attach a public IP
            address to the VM. Note that without a public IP
            address, additional configuration is required to
            allow the VM to access Google services.

            See
            https://cloud.google.com/vpc/docs/configure-private-google-access
            for more information.
        subnetwork (str):
            If the specified network is configured for custom subnet
            creation, the name of the subnetwork to attach the instance
            to must be specified here.

            The value is prefixed with ``regions/*/subnetworks/`` unless
            it contains a ``/``, in which case it is assumed to be a
            fully specified subnetwork resource URL.

            If the ``*`` character appears in the value, it is replaced
            with the region that the virtual machine has been allocated
            in.
    """

    network: str = proto.Field(
        proto.STRING,
        number=1,
    )
    use_private_address: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    subnetwork: str = proto.Field(
        proto.STRING,
        number=3,
    )


class Disk(proto.Message):
    r"""Carries information about a disk that can be attached to a VM.

    See https://cloud.google.com/compute/docs/disks/performance for more
    information about disk type, size, and performance considerations.

    Specify either [``Volume``][google.cloud.lifesciences.v2beta.Volume]
    or [``Disk``][google.cloud.lifesciences.v2beta.Disk], but not both.

    Attributes:
        name (str):
            A user-supplied name for the disk. Used when
            mounting the disk into actions. The name must
            contain only upper and lowercase alphanumeric
            characters and hyphens and cannot start with a
            hyphen.
        size_gb (int):
            The size, in GB, of the disk to attach. If the size is not
            specified, a default is chosen to ensure reasonable I/O
            performance.

            If the disk type is specified as ``local-ssd``, multiple
            local drives are automatically combined to provide the
            requested size. Note, however, that each physical SSD is
            375GB in size, and no more than 8 drives can be attached to
            a single instance.
        type_ (str):
            The Compute Engine disk type. If unspecified,
            ``pd-standard`` is used.
        source_image (str):
            An optional image to put on the disk before
            attaching it to the VM.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    size_gb: int = proto.Field(
        proto.INT32,
        number=2,
    )
    type_: str = proto.Field(
        proto.STRING,
        number=3,
    )
    source_image: str = proto.Field(
        proto.STRING,
        number=4,
    )


class Volume(proto.Message):
    r"""Carries information about storage that can be attached to a VM.

    Specify either [``Volume``][google.cloud.lifesciences.v2beta.Volume]
    or [``Disk``][google.cloud.lifesciences.v2beta.Disk], but not both.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        volume (str):
            A user-supplied name for the volume. Used when mounting the
            volume into
            [``Actions``][google.cloud.lifesciences.v2beta.Action]. The
            name must contain only upper and lowercase alphanumeric
            characters and hyphens and cannot start with a hyphen.
        persistent_disk (google.cloud.lifesciences_v2beta.types.PersistentDisk):
            Configuration for a persistent disk.

            This field is a member of `oneof`_ ``storage``.
        existing_disk (google.cloud.lifesciences_v2beta.types.ExistingDisk):
            Configuration for a existing disk.

            This field is a member of `oneof`_ ``storage``.
        nfs_mount (google.cloud.lifesciences_v2beta.types.NFSMount):
            Configuration for an NFS mount.

            This field is a member of `oneof`_ ``storage``.
    """

    volume: str = proto.Field(
        proto.STRING,
        number=1,
    )
    persistent_disk: "PersistentDisk" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="storage",
        message="PersistentDisk",
    )
    existing_disk: "ExistingDisk" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="storage",
        message="ExistingDisk",
    )
    nfs_mount: "NFSMount" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="storage",
        message="NFSMount",
    )


class PersistentDisk(proto.Message):
    r"""Configuration for a persistent disk to be attached to the VM.

    See https://cloud.google.com/compute/docs/disks/performance for
    more information about disk type, size, and performance
    considerations.

    Attributes:
        size_gb (int):
            The size, in GB, of the disk to attach. If the size is not
            specified, a default is chosen to ensure reasonable I/O
            performance.

            If the disk type is specified as ``local-ssd``, multiple
            local drives are automatically combined to provide the
            requested size. Note, however, that each physical SSD is
            375GB in size, and no more than 8 drives can be attached to
            a single instance.
        type_ (str):
            The Compute Engine disk type. If unspecified,
            ``pd-standard`` is used.
        source_image (str):
            An image to put on the disk before attaching
            it to the VM.
    """

    size_gb: int = proto.Field(
        proto.INT32,
        number=1,
    )
    type_: str = proto.Field(
        proto.STRING,
        number=2,
    )
    source_image: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ExistingDisk(proto.Message):
    r"""Configuration for an existing disk to be attached to the VM.

    Attributes:
        disk (str):
            If ``disk`` contains slashes, the Cloud Life Sciences API
            assumes that it is a complete URL for the disk. If ``disk``
            does not contain slashes, the Cloud Life Sciences API
            assumes that the disk is a zonal disk and a URL will be
            generated of the form ``zones/<zone>/disks/<disk>``, where
            ``<zone>`` is the zone in which the instance is allocated.
            The disk must be ext4 formatted.

            If all ``Mount`` references to this disk have the
            ``read_only`` flag set to true, the disk will be attached in
            ``read-only`` mode and can be shared with other instances.
            Otherwise, the disk will be available for writing but cannot
            be shared.
    """

    disk: str = proto.Field(
        proto.STRING,
        number=1,
    )


class NFSMount(proto.Message):
    r"""Configuration for an ``NFSMount`` to be attached to the VM.

    Attributes:
        target (str):
            A target NFS mount. The target must be specified as
            \`address:/mount".
    """

    target: str = proto.Field(
        proto.STRING,
        number=1,
    )


class Metadata(proto.Message):
    r"""Carries information about the pipeline execution that is
    returned in the long running operation's metadata field.

    Attributes:
        pipeline (google.cloud.lifesciences_v2beta.types.Pipeline):
            The pipeline this operation represents.
        labels (MutableMapping[str, str]):
            The user-defined labels associated with this
            operation.
        events (MutableSequence[google.cloud.lifesciences_v2beta.types.Event]):
            The list of events that have happened so far
            during the execution of this operation.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            The time at which the operation was created
            by the API.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            The first time at which resources were
            allocated to execute the pipeline.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            The time at which execution was completed and
            resources were cleaned up.
        pub_sub_topic (str):
            The name of the Cloud Pub/Sub topic where
            notifications of operation status changes are
            sent.
    """

    pipeline: "Pipeline" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Pipeline",
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=2,
    )
    events: MutableSequence["Event"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="Event",
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    pub_sub_topic: str = proto.Field(
        proto.STRING,
        number=7,
    )


class Event(proto.Message):
    r"""Carries information about events that occur during pipeline
    execution.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        timestamp (google.protobuf.timestamp_pb2.Timestamp):
            The time at which the event occurred.
        description (str):
            A human-readable description of the event. Note that these
            strings can change at any time without notice. Any
            application logic must use the information in the
            ``details`` field.
        delayed (google.cloud.lifesciences_v2beta.types.DelayedEvent):
            See
            [google.cloud.lifesciences.v2beta.DelayedEvent][google.cloud.lifesciences.v2beta.DelayedEvent].

            This field is a member of `oneof`_ ``details``.
        worker_assigned (google.cloud.lifesciences_v2beta.types.WorkerAssignedEvent):
            See
            [google.cloud.lifesciences.v2beta.WorkerAssignedEvent][google.cloud.lifesciences.v2beta.WorkerAssignedEvent].

            This field is a member of `oneof`_ ``details``.
        worker_released (google.cloud.lifesciences_v2beta.types.WorkerReleasedEvent):
            See
            [google.cloud.lifesciences.v2beta.WorkerReleasedEvent][google.cloud.lifesciences.v2beta.WorkerReleasedEvent].

            This field is a member of `oneof`_ ``details``.
        pull_started (google.cloud.lifesciences_v2beta.types.PullStartedEvent):
            See
            [google.cloud.lifesciences.v2beta.PullStartedEvent][google.cloud.lifesciences.v2beta.PullStartedEvent].

            This field is a member of `oneof`_ ``details``.
        pull_stopped (google.cloud.lifesciences_v2beta.types.PullStoppedEvent):
            See
            [google.cloud.lifesciences.v2beta.PullStoppedEvent][google.cloud.lifesciences.v2beta.PullStoppedEvent].

            This field is a member of `oneof`_ ``details``.
        container_started (google.cloud.lifesciences_v2beta.types.ContainerStartedEvent):
            See
            [google.cloud.lifesciences.v2beta.ContainerStartedEvent][google.cloud.lifesciences.v2beta.ContainerStartedEvent].

            This field is a member of `oneof`_ ``details``.
        container_stopped (google.cloud.lifesciences_v2beta.types.ContainerStoppedEvent):
            See
            [google.cloud.lifesciences.v2beta.ContainerStoppedEvent][google.cloud.lifesciences.v2beta.ContainerStoppedEvent].

            This field is a member of `oneof`_ ``details``.
        container_killed (google.cloud.lifesciences_v2beta.types.ContainerKilledEvent):
            See
            [google.cloud.lifesciences.v2beta.ContainerKilledEvent][google.cloud.lifesciences.v2beta.ContainerKilledEvent].

            This field is a member of `oneof`_ ``details``.
        unexpected_exit_status (google.cloud.lifesciences_v2beta.types.UnexpectedExitStatusEvent):
            See
            [google.cloud.lifesciences.v2beta.UnexpectedExitStatusEvent][google.cloud.lifesciences.v2beta.UnexpectedExitStatusEvent].

            This field is a member of `oneof`_ ``details``.
        failed (google.cloud.lifesciences_v2beta.types.FailedEvent):
            See
            [google.cloud.lifesciences.v2beta.FailedEvent][google.cloud.lifesciences.v2beta.FailedEvent].

            This field is a member of `oneof`_ ``details``.
    """

    timestamp: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    delayed: "DelayedEvent" = proto.Field(
        proto.MESSAGE,
        number=17,
        oneof="details",
        message="DelayedEvent",
    )
    worker_assigned: "WorkerAssignedEvent" = proto.Field(
        proto.MESSAGE,
        number=18,
        oneof="details",
        message="WorkerAssignedEvent",
    )
    worker_released: "WorkerReleasedEvent" = proto.Field(
        proto.MESSAGE,
        number=19,
        oneof="details",
        message="WorkerReleasedEvent",
    )
    pull_started: "PullStartedEvent" = proto.Field(
        proto.MESSAGE,
        number=20,
        oneof="details",
        message="PullStartedEvent",
    )
    pull_stopped: "PullStoppedEvent" = proto.Field(
        proto.MESSAGE,
        number=21,
        oneof="details",
        message="PullStoppedEvent",
    )
    container_started: "ContainerStartedEvent" = proto.Field(
        proto.MESSAGE,
        number=22,
        oneof="details",
        message="ContainerStartedEvent",
    )
    container_stopped: "ContainerStoppedEvent" = proto.Field(
        proto.MESSAGE,
        number=23,
        oneof="details",
        message="ContainerStoppedEvent",
    )
    container_killed: "ContainerKilledEvent" = proto.Field(
        proto.MESSAGE,
        number=24,
        oneof="details",
        message="ContainerKilledEvent",
    )
    unexpected_exit_status: "UnexpectedExitStatusEvent" = proto.Field(
        proto.MESSAGE,
        number=25,
        oneof="details",
        message="UnexpectedExitStatusEvent",
    )
    failed: "FailedEvent" = proto.Field(
        proto.MESSAGE,
        number=26,
        oneof="details",
        message="FailedEvent",
    )


class DelayedEvent(proto.Message):
    r"""An event generated whenever a resource limitation or
    transient error delays execution of a pipeline that was
    otherwise ready to run.

    Attributes:
        cause (str):
            A textual description of the cause of the
            delay. The string can change without notice
            because it is often generated by another service
            (such as Compute Engine).
        metrics (MutableSequence[str]):
            If the delay was caused by a resource shortage, this field
            lists the Compute Engine metrics that are preventing this
            operation from running (for example, ``CPUS`` or
            ``INSTANCES``). If the particular metric is not known, a
            single ``UNKNOWN`` metric will be present.
    """

    cause: str = proto.Field(
        proto.STRING,
        number=1,
    )
    metrics: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class WorkerAssignedEvent(proto.Message):
    r"""An event generated after a worker VM has been assigned to run
    the pipeline.

    Attributes:
        zone (str):
            The zone the worker is running in.
        instance (str):
            The worker's instance name.
        machine_type (str):
            The machine type that was assigned for the
            worker.
    """

    zone: str = proto.Field(
        proto.STRING,
        number=1,
    )
    instance: str = proto.Field(
        proto.STRING,
        number=2,
    )
    machine_type: str = proto.Field(
        proto.STRING,
        number=3,
    )


class WorkerReleasedEvent(proto.Message):
    r"""An event generated when the worker VM that was assigned to
    the pipeline has been released (deleted).

    Attributes:
        zone (str):
            The zone the worker was running in.
        instance (str):
            The worker's instance name.
    """

    zone: str = proto.Field(
        proto.STRING,
        number=1,
    )
    instance: str = proto.Field(
        proto.STRING,
        number=2,
    )


class PullStartedEvent(proto.Message):
    r"""An event generated when the worker starts pulling an image.

    Attributes:
        image_uri (str):
            The URI of the image that was pulled.
    """

    image_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )


class PullStoppedEvent(proto.Message):
    r"""An event generated when the worker stops pulling an image.

    Attributes:
        image_uri (str):
            The URI of the image that was pulled.
    """

    image_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ContainerStartedEvent(proto.Message):
    r"""An event generated when a container starts.

    Attributes:
        action_id (int):
            The numeric ID of the action that started
            this container.
        port_mappings (MutableMapping[int, int]):
            The container-to-host port mappings installed for this
            container. This set will contain any ports exposed using the
            ``PUBLISH_EXPOSED_PORTS`` flag as well as any specified in
            the ``Action`` definition.
        ip_address (str):
            The public IP address that can be used to
            connect to the container. This field is only
            populated when at least one port mapping is
            present. If the instance was created with a
            private address, this field will be empty even
            if port mappings exist.
    """

    action_id: int = proto.Field(
        proto.INT32,
        number=1,
    )
    port_mappings: MutableMapping[int, int] = proto.MapField(
        proto.INT32,
        proto.INT32,
        number=2,
    )
    ip_address: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ContainerStoppedEvent(proto.Message):
    r"""An event generated when a container exits.

    Attributes:
        action_id (int):
            The numeric ID of the action that started
            this container.
        exit_status (int):
            The exit status of the container.
        stderr (str):
            The tail end of any content written to standard error by the
            container. If the content emits large amounts of debugging
            noise or contains sensitive information, you can prevent the
            content from being printed by setting the
            ``DISABLE_STANDARD_ERROR_CAPTURE`` flag.

            Note that only a small amount of the end of the stream is
            captured here. The entire stream is stored in the
            ``/google/logs`` directory mounted into each action, and can
            be copied off the machine as described elsewhere.
    """

    action_id: int = proto.Field(
        proto.INT32,
        number=1,
    )
    exit_status: int = proto.Field(
        proto.INT32,
        number=2,
    )
    stderr: str = proto.Field(
        proto.STRING,
        number=3,
    )


class UnexpectedExitStatusEvent(proto.Message):
    r"""An event generated when the execution of a container results in a
    non-zero exit status that was not otherwise ignored. Execution will
    continue, but only actions that are flagged as ``ALWAYS_RUN`` will
    be executed. Other actions will be skipped.

    Attributes:
        action_id (int):
            The numeric ID of the action that started the
            container.
        exit_status (int):
            The exit status of the container.
    """

    action_id: int = proto.Field(
        proto.INT32,
        number=1,
    )
    exit_status: int = proto.Field(
        proto.INT32,
        number=2,
    )


class ContainerKilledEvent(proto.Message):
    r"""An event generated when a container is forcibly terminated by
    the worker. Currently, this only occurs when the container
    outlives the timeout specified by the user.

    Attributes:
        action_id (int):
            The numeric ID of the action that started the
            container.
    """

    action_id: int = proto.Field(
        proto.INT32,
        number=1,
    )


class FailedEvent(proto.Message):
    r"""An event generated when the execution of a pipeline has
    failed. Note that other events can continue to occur after this
    event.

    Attributes:
        code (google.rpc.code_pb2.Code):
            The Google standard error code that best
            describes this failure.
        cause (str):
            The human-readable description of the cause
            of the failure.
    """

    code: code_pb2.Code = proto.Field(
        proto.ENUM,
        number=1,
        enum=code_pb2.Code,
    )
    cause: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
