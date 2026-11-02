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
import proto  # type: ignore

from google.cloud.batch_v1alpha.types import task

__protobuf__ = proto.module(
    package="google.cloud.batch.v1alpha",
    manifest={
        "Job",
        "LogsPolicy",
        "JobDependency",
        "JobStatus",
        "ResourceUsage",
        "JobNotification",
        "AllocationPolicy",
        "TaskGroup",
        "ServiceAccount",
    },
)


class Job(proto.Message):
    r"""The Cloud Batch Job description.

    Attributes:
        name (str):
            Output only. Job name.
            For example:
            "projects/123456/locations/us-central1/jobs/job01".
        uid (str):
            Output only. A system generated unique ID for
            the Job.
        priority (int):
            Priority of the Job. The valid value range is [0, 100).
            Default value is 0. Higher value indicates higher priority.
            A job with higher priority value is more likely to run
            earlier if all other requirements are satisfied.
        task_groups (MutableSequence[google.cloud.batch_v1alpha.types.TaskGroup]):
            Required. TaskGroups in the Job. Only one
            TaskGroup is supported now.
        scheduling_policy (google.cloud.batch_v1alpha.types.Job.SchedulingPolicy):
            Scheduling policy for TaskGroups in the job.
        dependencies (MutableSequence[google.cloud.batch_v1alpha.types.JobDependency]):
            At least one of the dependencies must be
            satisfied before the Job is scheduled to run.
            Only one JobDependency is supported now.
            Not yet implemented.
        allocation_policy (google.cloud.batch_v1alpha.types.AllocationPolicy):
            Compute resource allocation for all
            TaskGroups in the Job.
        labels (MutableMapping[str, str]):
            Custom labels to apply to the job and any Cloud Logging
            `LogEntry <https://cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry>`__
            that it generates.

            Use labels to group and describe the resources they are
            applied to. Batch automatically applies predefined labels
            and supports multiple ``labels`` fields for each job, which
            each let you apply custom labels to various resources. Label
            names that start with "goog-" or "google-" are reserved for
            predefined labels. For more information about labels with
            Batch, see `Organize resources using
            labels <https://cloud.google.com/batch/docs/organize-resources-using-labels>`__.
        status (google.cloud.batch_v1alpha.types.JobStatus):
            Output only. Job status. It is read only for
            users.
        notification (google.cloud.batch_v1alpha.types.JobNotification):
            Deprecated: please use notifications instead.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. When the Job was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last time the Job was
            updated.
        logs_policy (google.cloud.batch_v1alpha.types.LogsPolicy):
            Log preservation policy for the Job.
        notifications (MutableSequence[google.cloud.batch_v1alpha.types.JobNotification]):
            Notification configurations.
    """

    class SchedulingPolicy(proto.Enum):
        r"""The order that TaskGroups are scheduled relative to each
        other.
        Not yet implemented.

        Values:
            SCHEDULING_POLICY_UNSPECIFIED (0):
                Unspecified.
            AS_SOON_AS_POSSIBLE (1):
                Run all TaskGroups as soon as possible.
        """

        SCHEDULING_POLICY_UNSPECIFIED = 0
        AS_SOON_AS_POSSIBLE = 1

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=2,
    )
    priority: int = proto.Field(
        proto.INT64,
        number=3,
    )
    task_groups: MutableSequence["TaskGroup"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="TaskGroup",
    )
    scheduling_policy: SchedulingPolicy = proto.Field(
        proto.ENUM,
        number=5,
        enum=SchedulingPolicy,
    )
    dependencies: MutableSequence["JobDependency"] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message="JobDependency",
    )
    allocation_policy: "AllocationPolicy" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="AllocationPolicy",
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=8,
    )
    status: "JobStatus" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="JobStatus",
    )
    notification: "JobNotification" = proto.Field(
        proto.MESSAGE,
        number=10,
        message="JobNotification",
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=11,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=12,
        message=timestamp_pb2.Timestamp,
    )
    logs_policy: "LogsPolicy" = proto.Field(
        proto.MESSAGE,
        number=13,
        message="LogsPolicy",
    )
    notifications: MutableSequence["JobNotification"] = proto.RepeatedField(
        proto.MESSAGE,
        number=14,
        message="JobNotification",
    )


class LogsPolicy(proto.Message):
    r"""LogsPolicy describes if and how a job's logs are preserved. Logs
    include information that is automatically written by the Batch
    service agent and any information that you configured the job's
    runnables to write to the ``stdout`` or ``stderr`` streams.

    Attributes:
        destination (google.cloud.batch_v1alpha.types.LogsPolicy.Destination):
            If and where logs should be saved.
        logs_path (str):
            When ``destination`` is set to ``PATH``, you must set this
            field to the path where you want logs to be saved. This path
            can point to a local directory on the VM or (if congifured)
            a directory under the mount path of any Cloud Storage
            bucket, network file system (NFS), or writable persistent
            disk that is mounted to the job. For example, if the job has
            a bucket with ``mountPath`` set to ``/mnt/disks/my-bucket``,
            you can write logs to the root directory of the
            ``remotePath`` of that bucket by setting this field to
            ``/mnt/disks/my-bucket/``.
        cloud_logging_option (google.cloud.batch_v1alpha.types.LogsPolicy.CloudLoggingOption):
            Optional. When ``destination`` is set to ``CLOUD_LOGGING``,
            you can optionally set this field to configure additional
            settings for Cloud Logging.
    """

    class Destination(proto.Enum):
        r"""The destination (if any) for logs.

        Values:
            DESTINATION_UNSPECIFIED (0):
                (Default) Logs are not preserved.
            CLOUD_LOGGING (1):
                Logs are streamed to Cloud Logging. Optionally, you can
                configure additional settings in the ``cloudLoggingOption``
                field.
            PATH (2):
                Logs are saved to the file path specified in the
                ``logsPath`` field.
        """

        DESTINATION_UNSPECIFIED = 0
        CLOUD_LOGGING = 1
        PATH = 2

    class CloudLoggingOption(proto.Message):
        r"""``CloudLoggingOption`` contains additional settings for Cloud
        Logging logs generated by Batch job.

        Attributes:
            use_generic_task_monitored_resource (bool):
                Optional. Set this field to ``true`` to change the
                `monitored resource
                type <https://cloud.google.com/monitoring/api/resources>`__
                for Cloud Logging logs generated by this Batch job from the
                ```batch.googleapis.com/Job`` <https://cloud.google.com/monitoring/api/resources#tag_batch.googleapis.com/Job>`__
                type to the formerly used
                ```generic_task`` <https://cloud.google.com/monitoring/api/resources#tag_generic_task>`__
                type.
        """

        use_generic_task_monitored_resource: bool = proto.Field(
            proto.BOOL,
            number=1,
        )

    destination: Destination = proto.Field(
        proto.ENUM,
        number=1,
        enum=Destination,
    )
    logs_path: str = proto.Field(
        proto.STRING,
        number=2,
    )
    cloud_logging_option: CloudLoggingOption = proto.Field(
        proto.MESSAGE,
        number=3,
        message=CloudLoggingOption,
    )


class JobDependency(proto.Message):
    r"""JobDependency describes the state of other Jobs that the
    start of this Job depends on.
    All dependent Jobs must have been submitted in the same region.

    Attributes:
        items (MutableMapping[str, google.cloud.batch_v1alpha.types.JobDependency.Type]):
            Each item maps a Job name to a Type.
            All items must be satisfied for the
            JobDependency to be satisfied (the AND
            operation).
            Once a condition for one item becomes true, it
            won't go back to false even the dependent Job
            state changes again.
    """

    class Type(proto.Enum):
        r"""Dependency type.

        Values:
            TYPE_UNSPECIFIED (0):
                Unspecified.
            SUCCEEDED (1):
                The dependent Job has succeeded.
            FAILED (2):
                The dependent Job has failed.
            FINISHED (3):
                SUCCEEDED or FAILED.
        """

        TYPE_UNSPECIFIED = 0
        SUCCEEDED = 1
        FAILED = 2
        FINISHED = 3

    items: MutableMapping[str, Type] = proto.MapField(
        proto.STRING,
        proto.ENUM,
        number=1,
        enum=Type,
    )


class JobStatus(proto.Message):
    r"""Job status.

    Attributes:
        state (google.cloud.batch_v1alpha.types.JobStatus.State):
            Job state
        status_events (MutableSequence[google.cloud.batch_v1alpha.types.StatusEvent]):
            Job status events
        task_groups (MutableMapping[str, google.cloud.batch_v1alpha.types.JobStatus.TaskGroupStatus]):
            Aggregated task status for each TaskGroup in
            the Job. The map key is TaskGroup ID.
        run_duration (google.protobuf.duration_pb2.Duration):
            The duration of time that the Job spent in
            status RUNNING.
        resource_usage (google.cloud.batch_v1alpha.types.ResourceUsage):
            The resource usage of the job.
    """

    class State(proto.Enum):
        r"""Valid Job states.

        Values:
            STATE_UNSPECIFIED (0):
                Job state unspecified.
            QUEUED (1):
                Job is admitted (validated and persisted) and
                waiting for resources.
            SCHEDULED (2):
                Job is scheduled to run as soon as resource
                allocation is ready. The resource allocation may
                happen at a later time but with a high chance to
                succeed.
            RUNNING (3):
                Resource allocation has been successful. At
                least one Task in the Job is RUNNING.
            SUCCEEDED (4):
                All Tasks in the Job have finished
                successfully.
            FAILED (5):
                At least one Task in the Job has failed.
            DELETION_IN_PROGRESS (6):
                The Job will be deleted, but has not been
                deleted yet. Typically this is because resources
                used by the Job are still being cleaned up.
            CANCELLATION_IN_PROGRESS (7):
                The Job cancellation is in progress, this is
                because the resources used by the Job are still
                being cleaned up.
            CANCELLED (8):
                The Job has been cancelled, the task
                executions were stopped and the resources were
                cleaned up.
        """

        STATE_UNSPECIFIED = 0
        QUEUED = 1
        SCHEDULED = 2
        RUNNING = 3
        SUCCEEDED = 4
        FAILED = 5
        DELETION_IN_PROGRESS = 6
        CANCELLATION_IN_PROGRESS = 7
        CANCELLED = 8

    class InstanceStatus(proto.Message):
        r"""VM instance status.

        Attributes:
            machine_type (str):
                The Compute Engine machine type.
            provisioning_model (google.cloud.batch_v1alpha.types.AllocationPolicy.ProvisioningModel):
                The VM instance provisioning model.
            task_pack (int):
                The max number of tasks can be assigned to
                this instance type.
            boot_disk (google.cloud.batch_v1alpha.types.AllocationPolicy.Disk):
                The VM boot disk.
        """

        machine_type: str = proto.Field(
            proto.STRING,
            number=1,
        )
        provisioning_model: "AllocationPolicy.ProvisioningModel" = proto.Field(
            proto.ENUM,
            number=2,
            enum="AllocationPolicy.ProvisioningModel",
        )
        task_pack: int = proto.Field(
            proto.INT64,
            number=3,
        )
        boot_disk: "AllocationPolicy.Disk" = proto.Field(
            proto.MESSAGE,
            number=4,
            message="AllocationPolicy.Disk",
        )

    class TaskGroupStatus(proto.Message):
        r"""Aggregated task status for a TaskGroup.

        Attributes:
            counts (MutableMapping[str, int]):
                Count of task in each state in the TaskGroup.
                The map key is task state name.
            instances (MutableSequence[google.cloud.batch_v1alpha.types.JobStatus.InstanceStatus]):
                Status of instances allocated for the
                TaskGroup.
        """

        counts: MutableMapping[str, int] = proto.MapField(
            proto.STRING,
            proto.INT64,
            number=1,
        )
        instances: MutableSequence["JobStatus.InstanceStatus"] = proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="JobStatus.InstanceStatus",
        )

    state: State = proto.Field(
        proto.ENUM,
        number=1,
        enum=State,
    )
    status_events: MutableSequence[task.StatusEvent] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=task.StatusEvent,
    )
    task_groups: MutableMapping[str, TaskGroupStatus] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=4,
        message=TaskGroupStatus,
    )
    run_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=5,
        message=duration_pb2.Duration,
    )
    resource_usage: "ResourceUsage" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="ResourceUsage",
    )


class ResourceUsage(proto.Message):
    r"""ResourceUsage describes the resource usage of the job.

    Attributes:
        core_hours (float):
            The CPU core hours that the job consumes.
    """

    core_hours: float = proto.Field(
        proto.DOUBLE,
        number=1,
    )


class JobNotification(proto.Message):
    r"""Notification configurations.

    Attributes:
        pubsub_topic (str):
            The Pub/Sub topic where notifications for the job, like
            state changes, will be published. If undefined, no Pub/Sub
            notifications are sent for this job.

            Specify the topic using the following format:
            ``projects/{project}/topics/{topic}``. Notably, if you want
            to specify a Pub/Sub topic that is in a different project
            than the job, your administrator must grant your project's
            Batch service agent permission to publish to that topic.

            For more information about configuring Pub/Sub notifications
            for a job, see
            https://cloud.google.com/batch/docs/enable-notifications.
        message (google.cloud.batch_v1alpha.types.JobNotification.Message):
            The attribute requirements of messages to be
            sent to this Pub/Sub topic. Without this field,
            no message will be sent.
    """

    class Type(proto.Enum):
        r"""The message type.

        Values:
            TYPE_UNSPECIFIED (0):
                Unspecified.
            JOB_STATE_CHANGED (1):
                Notify users that the job state has changed.
            TASK_STATE_CHANGED (2):
                Notify users that the task state has changed.
        """

        TYPE_UNSPECIFIED = 0
        JOB_STATE_CHANGED = 1
        TASK_STATE_CHANGED = 2

    class Message(proto.Message):
        r"""Message details. Describe the conditions under which messages will
        be sent. If no attribute is defined, no message will be sent by
        default. One message should specify either the job or the task level
        attributes, but not both. For example, job level: JOB_STATE_CHANGED
        and/or a specified new_job_state; task level: TASK_STATE_CHANGED
        and/or a specified new_task_state.

        Attributes:
            type_ (google.cloud.batch_v1alpha.types.JobNotification.Type):
                The message type.
            new_job_state (google.cloud.batch_v1alpha.types.JobStatus.State):
                The new job state.
            new_task_state (google.cloud.batch_v1alpha.types.TaskStatus.State):
                The new task state.
        """

        type_: "JobNotification.Type" = proto.Field(
            proto.ENUM,
            number=1,
            enum="JobNotification.Type",
        )
        new_job_state: "JobStatus.State" = proto.Field(
            proto.ENUM,
            number=2,
            enum="JobStatus.State",
        )
        new_task_state: task.TaskStatus.State = proto.Field(
            proto.ENUM,
            number=3,
            enum=task.TaskStatus.State,
        )

    pubsub_topic: str = proto.Field(
        proto.STRING,
        number=1,
    )
    message: Message = proto.Field(
        proto.MESSAGE,
        number=2,
        message=Message,
    )


class AllocationPolicy(proto.Message):
    r"""A Job's resource allocation policy describes when, where, and
    how compute resources should be allocated for the Job.

    Attributes:
        location (google.cloud.batch_v1alpha.types.AllocationPolicy.LocationPolicy):
            Location where compute resources should be
            allocated for the Job.
        instance (google.cloud.batch_v1alpha.types.AllocationPolicy.InstancePolicy):
            Deprecated: please use instances[0].policy instead.
        instances (MutableSequence[google.cloud.batch_v1alpha.types.AllocationPolicy.InstancePolicyOrTemplate]):
            Describe instances that can be created by this
            AllocationPolicy. Only instances[0] is supported now.
        instance_templates (MutableSequence[str]):
            Deprecated: please use instances[0].template instead.
        provisioning_models (MutableSequence[google.cloud.batch_v1alpha.types.AllocationPolicy.ProvisioningModel]):
            Deprecated: please use
            instances[0].policy.provisioning_model instead.
        service_account_email (str):
            Deprecated: please use service_account instead.
        service_account (google.cloud.batch_v1alpha.types.ServiceAccount):
            Defines the service account for Batch-created VMs. If
            omitted, the `default Compute Engine service
            account <https://cloud.google.com/compute/docs/access/service-accounts#default_service_account>`__
            is used. Must match the service account specified in any
            used instance template configured in the Batch job.

            Includes the following fields:

            - email: The service account's email address. If not set,
              the default Compute Engine service account is used.
            - scopes: Additional OAuth scopes to grant the service
              account, beyond the default cloud-platform scope. (list of
              strings)
        labels (MutableMapping[str, str]):
            Custom labels to apply to the job and all the Compute Engine
            resources that both are created by this allocation policy
            and support labels.

            Use labels to group and describe the resources they are
            applied to. Batch automatically applies predefined labels
            and supports multiple ``labels`` fields for each job, which
            each let you apply custom labels to various resources. Label
            names that start with "goog-" or "google-" are reserved for
            predefined labels. For more information about labels with
            Batch, see `Organize resources using
            labels <https://cloud.google.com/batch/docs/organize-resources-using-labels>`__.
        network (google.cloud.batch_v1alpha.types.AllocationPolicy.NetworkPolicy):
            The network policy.

            If you define an instance template in the
            ``InstancePolicyOrTemplate`` field, Batch will use the
            network settings in the instance template instead of this
            field.
        placement (google.cloud.batch_v1alpha.types.AllocationPolicy.PlacementPolicy):
            The placement policy.
        tags (MutableSequence[str]):
            Optional. Tags applied to the VM instances.

            The tags identify valid sources or targets for network
            firewalls. Each tag must be 1-63 characters long, and comply
            with `RFC1035 <https://www.ietf.org/rfc/rfc1035.txt>`__.
        instance_flexibility_policy (google.cloud.batch_v1alpha.types.AllocationPolicy.InstanceFlexibilityPolicy):
            Optional. The instance flexibility policy for the job. This
            configuration overrides the ``instances`` configuration.
            Only allowed in job level. Not allowed in task group level.
    """

    class ProvisioningModel(proto.Enum):
        r"""Compute Engine VM instance provisioning model.

        Values:
            PROVISIONING_MODEL_UNSPECIFIED (0):
                Unspecified.
            STANDARD (1):
                Standard VM.
            SPOT (2):
                SPOT VM.
            PREEMPTIBLE (3):
                Preemptible VM (PVM).

                Above SPOT VM is the preferable model for
                preemptible VM instances: the old preemptible VM
                model (indicated by this field) is the older
                model, and has been migrated to use the SPOT
                model as the underlying technology. This old
                model will still be supported.
            RESERVATION_BOUND (4):
                Bound to the lifecycle of the reservation in
                which it is provisioned.
            FLEX_START (5):
                Instance is provisioned with DWS Flex Start
                and has limited max run duration.
        """

        PROVISIONING_MODEL_UNSPECIFIED = 0
        STANDARD = 1
        SPOT = 2
        PREEMPTIBLE = 3
        RESERVATION_BOUND = 4
        FLEX_START = 5

    class LocationPolicy(proto.Message):
        r"""

        Attributes:
            allowed_locations (MutableSequence[str]):
                A list of location names that are allowed for the job's VMs
                formatted as URLs. Each location can be a region or a zone,
                but you can only specify one region or multiple zones in one
                region per job. For example, ``["regions/us-central1"]``
                allow VMs in any zones in region ``us-central1``, and
                ``["zones/us-central1-a", "zones/us-central1-c"]`` only
                allow VMs in zones ``us-central1-a`` and ``us-central1-c``.
                However,
                ``["regions/us-central1", "zones/us-central1-a", "zones/us-central1-b", "zones/us-west1-a"]``
                causes an error because it contains multiple regions
                (``us-central1`` and ``us-west1``).

                The specified region or zones must be in the same region in
                which the job is created starting on the following dates:

                - For projects that have successfully submitted before July
                  31, 2026 at least one job that uses the
                  ``allowedLocations[]`` field with any region or zones
                  outside of the job's location, the changes are starting on
                  *June 30, 2027*.

                - For all other projects, the changes are starting on *July
                  31, 2026*.

                For example, for job
                ``projects/123/locations/us-central1/jobs/jobid``, the
                specified region or zones must be in ``us-central1``. Using
                a different region (e.g. ``regions/us-west1``) or a zone not
                in ``us-central1`` (e.g. ``zones/us-west1-a``) causes an
                error.
            denied_locations (MutableSequence[str]):
                A list of denied location names.

                Not yet implemented.
        """

        allowed_locations: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )
        denied_locations: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=2,
        )

    class Disk(proto.Message):
        r"""A new persistent disk or a local ssd.
        A VM can only have one local SSD setting but multiple local SSD
        partitions. See
        https://cloud.google.com/compute/docs/disks#pdspecs and
        https://cloud.google.com/compute/docs/disks#localssds.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            image (str):
                URL for a VM image to use as the data source for this disk.
                For example, the following are all valid URLs:

                - Specify the image by its family name:
                  projects/{project}/global/images/family/{image_family}
                - Specify the image version:
                  projects/{project}/global/images/{image_version}

                You can also use Batch customized image in short names. The
                following image values are supported for a boot disk:

                - ``batch-debian``: use Batch Debian images.
                - ``batch-cos``: use Batch Container-Optimized images.
                - ``batch-hpc-rocky``: use Batch HPC Rocky Linux images.

                This field is a member of `oneof`_ ``data_source``.
            snapshot (str):
                Name of a snapshot used as the data source.
                Snapshot is not supported as boot disk now.

                This field is a member of `oneof`_ ``data_source``.
            type_ (str):
                Disk type as shown in ``gcloud compute disk-types list``.
                For example, local SSD uses type "local-ssd". Persistent
                disks and boot disks use "pd-balanced", "pd-extreme",
                "pd-ssd" or "pd-standard". If not specified, "pd-standard"
                will be used as the default type for non-boot disks,
                "pd-balanced" will be used as the default type for boot
                disks.
            size_gb (int):
                Disk size in GB.

                **Non-Boot Disk**: If the ``type`` specifies a persistent
                disk, this field is ignored if ``data_source`` is set as
                ``image`` or ``snapshot``. If the ``type`` specifies a local
                SSD, this field should be a multiple of 375 GB, otherwise,
                the final size will be the next greater multiple of 375 GB.

                **Boot Disk**: Batch will calculate the boot disk size based
                on source image and task requirements if you do not speicify
                the size. If both this field and the ``boot_disk_mib`` field
                in task spec's ``compute_resource`` are defined, Batch will
                only honor this field. Also, this field should be no smaller
                than the source disk's size when the ``data_source`` is set
                as ``snapshot`` or ``image``. For example, if you set an
                image as the ``data_source`` field and the image's default
                disk size 30 GB, you can only use this field to make the
                disk larger or equal to 30 GB.
            disk_interface (str):
                Local SSDs are available through both "SCSI" and "NVMe"
                interfaces. If not indicated, "NVMe" will be the default one
                for local ssds. This field is ignored for persistent disks
                as the interface is chosen automatically. See
                https://cloud.google.com/compute/docs/disks/persistent-disks#choose_an_interface.
        """

        image: str = proto.Field(
            proto.STRING,
            number=4,
            oneof="data_source",
        )
        snapshot: str = proto.Field(
            proto.STRING,
            number=5,
            oneof="data_source",
        )
        type_: str = proto.Field(
            proto.STRING,
            number=1,
        )
        size_gb: int = proto.Field(
            proto.INT64,
            number=2,
        )
        disk_interface: str = proto.Field(
            proto.STRING,
            number=6,
        )

    class AttachedDisk(proto.Message):
        r"""A new or an existing persistent disk (PD) or a local ssd
        attached to a VM instance.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            new_disk (google.cloud.batch_v1alpha.types.AllocationPolicy.Disk):

                This field is a member of `oneof`_ ``attached``.
            existing_disk (str):
                Name of an existing PD.

                This field is a member of `oneof`_ ``attached``.
            device_name (str):
                Device name that the guest operating system will see. It is
                used by Runnable.volumes field to mount disks. So please
                specify the device_name if you want Batch to help mount the
                disk, and it should match the device_name field in volumes.
        """

        new_disk: "AllocationPolicy.Disk" = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="attached",
            message="AllocationPolicy.Disk",
        )
        existing_disk: str = proto.Field(
            proto.STRING,
            number=2,
            oneof="attached",
        )
        device_name: str = proto.Field(
            proto.STRING,
            number=3,
        )

    class Accelerator(proto.Message):
        r"""Accelerator describes Compute Engine accelerators to be
        attached to the VM.

        Attributes:
            type_ (str):
                The accelerator type. For example, "nvidia-tesla-t4". See
                ``gcloud compute accelerator-types list``.
            count (int):
                The number of accelerators of this type.
            install_gpu_drivers (bool):
                Deprecated: please use instances[0].install_gpu_drivers
                instead.
            driver_version (str):
                Optional. The NVIDIA GPU driver version that
                should be installed for this type.

                You can define the specific driver version such
                as "470.103.01", following the driver version
                requirements in
                https://cloud.google.com/compute/docs/gpus/install-drivers-gpu#minimum-driver.
                Batch will install the specific accelerator
                driver if qualified.
        """

        type_: str = proto.Field(
            proto.STRING,
            number=1,
        )
        count: int = proto.Field(
            proto.INT64,
            number=2,
        )
        install_gpu_drivers: bool = proto.Field(
            proto.BOOL,
            number=3,
        )
        driver_version: str = proto.Field(
            proto.STRING,
            number=4,
        )

    class InstancePolicy(proto.Message):
        r"""InstancePolicy describes an instance type and resources
        attached to each VM created by this InstancePolicy.

        Attributes:
            allowed_machine_types (MutableSequence[str]):
                Deprecated: please use machine_type instead.
            machine_type (str):
                The Compute Engine machine type.
            min_cpu_platform (str):
                The minimum CPU platform.
                See
                https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform.
            provisioning_model (google.cloud.batch_v1alpha.types.AllocationPolicy.ProvisioningModel):
                The provisioning model.
            accelerators (MutableSequence[google.cloud.batch_v1alpha.types.AllocationPolicy.Accelerator]):
                The accelerators attached to each VM
                instance.
            boot_disk (google.cloud.batch_v1alpha.types.AllocationPolicy.Disk):
                Boot disk to be created and attached to each
                VM by this InstancePolicy. Boot disk will be
                deleted when the VM is deleted. Batch API now
                only supports booting from image.
            disks (MutableSequence[google.cloud.batch_v1alpha.types.AllocationPolicy.AttachedDisk]):
                Non-boot disks to be attached for each VM
                created by this InstancePolicy. New disks will
                be deleted when the VM is deleted. A non-boot
                disk is a disk that can be of a device with a
                file system or a raw storage drive that is not
                ready for data storage and accessing.
            reservation (str):
                Optional. If not specified (default), VMs will consume any
                applicable reservation. If "NO_RESERVATION" is specified,
                VMs will not consume any reservation. Otherwise, if
                specified, VMs will consume only the specified reservation.
        """

        allowed_machine_types: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )
        machine_type: str = proto.Field(
            proto.STRING,
            number=2,
        )
        min_cpu_platform: str = proto.Field(
            proto.STRING,
            number=3,
        )
        provisioning_model: "AllocationPolicy.ProvisioningModel" = proto.Field(
            proto.ENUM,
            number=4,
            enum="AllocationPolicy.ProvisioningModel",
        )
        accelerators: MutableSequence["AllocationPolicy.Accelerator"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=5,
                message="AllocationPolicy.Accelerator",
            )
        )
        boot_disk: "AllocationPolicy.Disk" = proto.Field(
            proto.MESSAGE,
            number=8,
            message="AllocationPolicy.Disk",
        )
        disks: MutableSequence["AllocationPolicy.AttachedDisk"] = proto.RepeatedField(
            proto.MESSAGE,
            number=6,
            message="AllocationPolicy.AttachedDisk",
        )
        reservation: str = proto.Field(
            proto.STRING,
            number=7,
        )

    class InstancePolicyOrTemplate(proto.Message):
        r"""InstancePolicyOrTemplate lets you define the type of
        resources to use for this job either with an InstancePolicy or
        an instance template. If undefined, Batch picks the type of VM
        to use and doesn't include optional VM resources such as GPUs
        and extra disks.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            policy (google.cloud.batch_v1alpha.types.AllocationPolicy.InstancePolicy):
                InstancePolicy.

                This field is a member of `oneof`_ ``policy_template``.
            instance_template (str):
                Name of an instance template used to create VMs. Named the
                field as 'instance_template' instead of 'template' to avoid
                C++ keyword conflict.

                Batch only supports global instance templates from the same
                project as the job. You can specify the global instance
                template as a full or partial URL.

                This field is a member of `oneof`_ ``policy_template``.
            install_gpu_drivers (bool):
                Set this field true if you want Batch to help fetch drivers
                from a third party location and install them for GPUs
                specified in ``policy.accelerators`` or
                ``instance_template`` on your behalf. Default is false.

                For Container-Optimized Image cases, Batch will install the
                accelerator driver following milestones of
                https://cloud.google.com/container-optimized-os/docs/release-notes.
                For non Container-Optimized Image cases, following
                https://github.com/GoogleCloudPlatform/compute-gpu-installation/blob/main/linux/install_gpu_driver.py.
            install_ops_agent (bool):
                Optional. Set this field true if you want
                Batch to install Ops Agent on your behalf.
                Default is false.
            block_project_ssh_keys (bool):
                Optional. Set this field to ``true`` if you want Batch to
                block project-level SSH keys from accessing this job's VMs.
                Alternatively, you can configure the job to specify a VM
                instance template that blocks project-level SSH keys. In
                either case, Batch blocks project-level SSH keys while
                creating the VMs for this job.

                Batch allows project-level SSH keys for a job's VMs only if
                all the following are true:

                - This field is undefined or set to ``false``.
                - The job's VM instance template (if any) doesn't block
                  project-level SSH keys.

                Notably, you can override this behavior by manually updating
                a VM to block or allow project-level SSH keys. For more
                information about blocking project-level SSH keys, see the
                Compute Engine documentation:
                https://cloud.google.com/compute/docs/connect/restrict-ssh-keys#block-keys
        """

        policy: "AllocationPolicy.InstancePolicy" = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="policy_template",
            message="AllocationPolicy.InstancePolicy",
        )
        instance_template: str = proto.Field(
            proto.STRING,
            number=2,
            oneof="policy_template",
        )
        install_gpu_drivers: bool = proto.Field(
            proto.BOOL,
            number=3,
        )
        install_ops_agent: bool = proto.Field(
            proto.BOOL,
            number=4,
        )
        block_project_ssh_keys: bool = proto.Field(
            proto.BOOL,
            number=5,
        )

    class NetworkInterface(proto.Message):
        r"""A network interface.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            network (str):
                The URL of an existing network resource. You can specify the
                network as a full or partial URL.

                For example, the following are all valid URLs:

                - https://www.googleapis.com/compute/v1/projects/{project}/global/networks/{network}
                - projects/{project}/global/networks/{network}
                - global/networks/{network}
            subnetwork (str):
                The URL of an existing subnetwork resource in the network.
                You can specify the subnetwork as a full or partial URL.

                For example, the following are all valid URLs:

                - https://www.googleapis.com/compute/v1/projects/{project}/regions/{region}/subnetworks/{subnetwork}
                - projects/{project}/regions/{region}/subnetworks/{subnetwork}
                - regions/{region}/subnetworks/{subnetwork}
            no_external_ip_address (bool):
                Default is false (with an external IP
                address). Required if no external public IP
                address is attached to the VM. If no external
                public IP address, additional configuration is
                required to allow the VM to access Google
                Services. See
                https://cloud.google.com/vpc/docs/configure-private-google-access
                and
                https://cloud.google.com/nat/docs/gce-example#create-nat
                for more information.
            nic_type (google.cloud.batch_v1alpha.types.AllocationPolicy.NetworkInterface.NicType):
                Optional. The NIC type of the network
                interface.

                This field is a member of `oneof`_ ``_nic_type``.
        """

        class NicType(proto.Enum):
            r"""Compute Engine VM instance NIC type.

            Values:
                NIC_TYPE_UNSPECIFIED (0):
                    No type specified.
                GVNIC (1):
                    GVNIC
                IRDMA (2):
                    IRDMA
                MRDMA (3):
                    MRDMA
            """

            NIC_TYPE_UNSPECIFIED = 0
            GVNIC = 1
            IRDMA = 2
            MRDMA = 3

        network: str = proto.Field(
            proto.STRING,
            number=1,
        )
        subnetwork: str = proto.Field(
            proto.STRING,
            number=2,
        )
        no_external_ip_address: bool = proto.Field(
            proto.BOOL,
            number=3,
        )
        nic_type: "AllocationPolicy.NetworkInterface.NicType" = proto.Field(
            proto.ENUM,
            number=7,
            optional=True,
            enum="AllocationPolicy.NetworkInterface.NicType",
        )

    class NetworkPolicy(proto.Message):
        r"""NetworkPolicy describes VM instance network configurations.

        Attributes:
            network_interfaces (MutableSequence[google.cloud.batch_v1alpha.types.AllocationPolicy.NetworkInterface]):
                Network configurations.
        """

        network_interfaces: MutableSequence["AllocationPolicy.NetworkInterface"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=1,
                message="AllocationPolicy.NetworkInterface",
            )
        )

    class PlacementPolicy(proto.Message):
        r"""PlacementPolicy describes a group placement policy for the
        VMs controlled by this AllocationPolicy.

        Attributes:
            collocation (str):
                UNSPECIFIED vs. COLLOCATED (default
                UNSPECIFIED). Use COLLOCATED when you want VMs
                to be located close to each other for low
                network latency between the VMs. No placement
                policy will be generated when collocation is
                UNSPECIFIED.
            max_distance (int):
                When specified, causes the job to fail if more than
                max_distance logical switches are required between VMs.
                Batch uses the most compact possible placement of VMs even
                when max_distance is not specified. An explicit max_distance
                makes that level of compactness a strict requirement. Not
                yet implemented
        """

        collocation: str = proto.Field(
            proto.STRING,
            number=1,
        )
        max_distance: int = proto.Field(
            proto.INT64,
            number=2,
        )

    class InstanceFlexibilityPolicy(proto.Message):
        r"""Allows creating VMs from multiple types of machines. Instance
        flexibility configuration overrides instances configuration.

        Attributes:
            instance_selections (MutableMapping[str, google.cloud.batch_v1alpha.types.AllocationPolicy.InstanceSelection]):
                Required. Named instance selections configuring properties
                that the group will use when creating new VMs. The map key
                is a user-specified name for the instance selection. The key
                must be 1-63 characters long, and comply with
                `RFC1035 <https://www.ietf.org/rfc/rfc1035.txt>`__.
                Specifically, the key must consist of lowercase letters,
                numbers, and hyphens. The first character must be a
                lowercase letter, and the last character must be a lowercase
                letter or number. The maximum number of instance selections
                is 50. Exceeding this limit results in a validation error
                with code ``INVALID_ARGUMENT``.
        """

        instance_selections: MutableMapping[
            str, "AllocationPolicy.InstanceSelection"
        ] = proto.MapField(
            proto.STRING,
            proto.MESSAGE,
            number=1,
            message="AllocationPolicy.InstanceSelection",
        )

    class InstanceSelection(proto.Message):
        r"""Defines an instance selection for a given instance
        flexibility policy.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            machine_types (MutableSequence[str]):
                Required. The Compute Engine machine type IDs. Only the
                machine type ID is supported, such as ``n1-standard-16``.
                Full or partial URLs are not accepted. The total maximum
                number of machine types across all instance selections is
                200. Exceeding this limit results in a validation error with
                code ``INVALID_ARGUMENT``.
            rank (int):
                Optional. Indicates the preference of this
                instance selection. Lower number means higher
                preference. First try is to create a VM based on
                the machine-type with lowest rank and fallback
                to next rank based on availability. Machine
                types and instance selections with the same rank
                have the same preference.

                This field is a member of `oneof`_ ``_rank``.
        """

        machine_types: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )
        rank: int = proto.Field(
            proto.INT32,
            number=2,
            optional=True,
        )

    location: LocationPolicy = proto.Field(
        proto.MESSAGE,
        number=1,
        message=LocationPolicy,
    )
    instance: InstancePolicy = proto.Field(
        proto.MESSAGE,
        number=2,
        message=InstancePolicy,
    )
    instances: MutableSequence[InstancePolicyOrTemplate] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message=InstancePolicyOrTemplate,
    )
    instance_templates: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    provisioning_models: MutableSequence[ProvisioningModel] = proto.RepeatedField(
        proto.ENUM,
        number=4,
        enum=ProvisioningModel,
    )
    service_account_email: str = proto.Field(
        proto.STRING,
        number=5,
    )
    service_account: "ServiceAccount" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="ServiceAccount",
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=6,
    )
    network: NetworkPolicy = proto.Field(
        proto.MESSAGE,
        number=7,
        message=NetworkPolicy,
    )
    placement: PlacementPolicy = proto.Field(
        proto.MESSAGE,
        number=10,
        message=PlacementPolicy,
    )
    tags: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=11,
    )
    instance_flexibility_policy: InstanceFlexibilityPolicy = proto.Field(
        proto.MESSAGE,
        number=12,
        message=InstanceFlexibilityPolicy,
    )


class TaskGroup(proto.Message):
    r"""A TaskGroup defines one or more Tasks that all share the same
    TaskSpec.

    Attributes:
        name (str):
            Output only. TaskGroup name.
            The system generates this field based on parent
            Job name. For example:

            "projects/123456/locations/us-west1/jobs/job01/taskGroups/group01".
        task_spec (google.cloud.batch_v1alpha.types.TaskSpec):
            Required. Tasks in the group share the same
            task spec.
        task_count (int):
            Number of Tasks in the TaskGroup.
            Default is 1.
        parallelism (int):
            Max number of tasks that can run in parallel. Default to
            min(task_count, parallel tasks per job limit). See: `Job
            Limits <https://cloud.google.com/batch/quotas#job_limits>`__.
            Field parallelism must be 1 if the scheduling_policy is
            IN_ORDER.
        scheduling_policy (google.cloud.batch_v1alpha.types.TaskGroup.SchedulingPolicy):
            Scheduling policy for Tasks in the TaskGroup. The default
            value is AS_SOON_AS_POSSIBLE.
        allocation_policy (google.cloud.batch_v1alpha.types.AllocationPolicy):
            Compute resource allocation for the
            TaskGroup. If specified, it overrides resources
            in Job.
        labels (MutableMapping[str, str]):
            Labels for the TaskGroup. Labels could be user provided or
            system generated. You can assign up to 64 labels. `Google
            Compute Engine label
            restrictions <https://cloud.google.com/compute/docs/labeling-resources#restrictions>`__
            apply. Label names that start with "goog-" or "google-" are
            reserved.
        task_environments (MutableSequence[google.cloud.batch_v1alpha.types.Environment]):
            An array of environment variable mappings, which are passed
            to Tasks with matching indices. If task_environments is used
            then task_count should not be specified in the request (and
            will be ignored). Task count will be the length of
            task_environments.

            Tasks get a BATCH_TASK_INDEX and BATCH_TASK_COUNT
            environment variable, in addition to any environment
            variables set in task_environments, specifying the number of
            Tasks in the Task's parent TaskGroup, and the specific
            Task's index in the TaskGroup (0 through BATCH_TASK_COUNT -
            1).
        task_count_per_node (int):
            Max number of tasks that can be run on a VM
            at the same time. If not specified, the system
            will decide a value based on available compute
            resources on a VM and task requirements.
        require_hosts_file (bool):
            When true, Batch will populate a file with a list of all VMs
            assigned to the TaskGroup and set the BATCH_HOSTS_FILE
            environment variable to the path of that file. Defaults to
            false. The host file supports up to 1000 VMs.
        permissive_ssh (bool):
            When true, Batch will configure SSH to allow
            passwordless login between VMs running the Batch
            tasks in the same TaskGroup.
        run_as_non_root (bool):
            Optional. If not set or set to false, Batch uses the root
            user to execute runnables. If set to true, Batch runs the
            runnables using a non-root user. Currently, the non-root
            user Batch used is generated by OS Login. For more
            information, see `About OS
            Login <https://cloud.google.com/compute/docs/oslogin>`__.
        service_account (google.cloud.batch_v1alpha.types.ServiceAccount):
            Optional. ServiceAccount used by tasks within the task group
            for the access to other Cloud resources. This allows tasks
            to operate with permissions distinct from the service
            account for the VM set at ``AllocationPolicy``. Use this
            field when tasks require different access rights than those
            of the VM.

            Specify the service account's ``email`` field. Ensure
            ``scopes`` include any necessary permissions for tasks, in
            addition to the default 'cloud-platform' scope.
    """

    class SchedulingPolicy(proto.Enum):
        r"""How Tasks in the TaskGroup should be scheduled relative to
        each other.

        Values:
            SCHEDULING_POLICY_UNSPECIFIED (0):
                Unspecified.
            AS_SOON_AS_POSSIBLE (1):
                Run Tasks as soon as resources are available.

                Tasks might be executed in parallel depending on parallelism
                and task_count values.
            IN_ORDER (2):
                Run Tasks sequentially with increased task
                index.
        """

        SCHEDULING_POLICY_UNSPECIFIED = 0
        AS_SOON_AS_POSSIBLE = 1
        IN_ORDER = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    task_spec: task.TaskSpec = proto.Field(
        proto.MESSAGE,
        number=3,
        message=task.TaskSpec,
    )
    task_count: int = proto.Field(
        proto.INT64,
        number=4,
    )
    parallelism: int = proto.Field(
        proto.INT64,
        number=5,
    )
    scheduling_policy: SchedulingPolicy = proto.Field(
        proto.ENUM,
        number=6,
        enum=SchedulingPolicy,
    )
    allocation_policy: "AllocationPolicy" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="AllocationPolicy",
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=8,
    )
    task_environments: MutableSequence[task.Environment] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message=task.Environment,
    )
    task_count_per_node: int = proto.Field(
        proto.INT64,
        number=10,
    )
    require_hosts_file: bool = proto.Field(
        proto.BOOL,
        number=11,
    )
    permissive_ssh: bool = proto.Field(
        proto.BOOL,
        number=12,
    )
    run_as_non_root: bool = proto.Field(
        proto.BOOL,
        number=14,
    )
    service_account: "ServiceAccount" = proto.Field(
        proto.MESSAGE,
        number=15,
        message="ServiceAccount",
    )


class ServiceAccount(proto.Message):
    r"""Carries information about a Google Cloud service account.

    Attributes:
        email (str):
            Email address of the service account.
        scopes (MutableSequence[str]):
            List of scopes to be enabled for this service
            account.
    """

    email: str = proto.Field(
        proto.STRING,
        number=1,
    )
    scopes: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
