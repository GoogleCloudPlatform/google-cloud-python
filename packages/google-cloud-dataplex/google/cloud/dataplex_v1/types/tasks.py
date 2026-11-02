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

from google.cloud.dataplex_v1.types import resources

__protobuf__ = proto.module(
    package="google.cloud.dataplex.v1",
    manifest={
        "Task",
        "Job",
    },
)


class Task(proto.Message):
    r"""A task represents a user-visible job.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Output only. The relative resource name of the task, of the
            form:
            projects/{project_number}/locations/{location_id}/lakes/{lake_id}/
            tasks/{task_id}.
        uid (str):
            Output only. System generated globally unique
            ID for the task. This ID will be different if
            the task is deleted and re-created with the same
            name.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the task was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the task was last
            updated.
        description (str):
            Optional. Description of the task.
        display_name (str):
            Optional. User friendly display name.
        state (google.cloud.dataplex_v1.types.State):
            Output only. Current state of the task.
        labels (MutableMapping[str, str]):
            Optional. User-defined labels for the task.
        trigger_spec (google.cloud.dataplex_v1.types.Task.TriggerSpec):
            Required. Spec related to how often and when
            a task should be triggered.
        execution_spec (google.cloud.dataplex_v1.types.Task.ExecutionSpec):
            Required. Spec related to how a task is
            executed.
        execution_status (google.cloud.dataplex_v1.types.Task.ExecutionStatus):
            Output only. Status of the latest task
            executions.
        spark (google.cloud.dataplex_v1.types.Task.SparkTaskConfig):
            Config related to running custom Spark tasks.

            This field is a member of `oneof`_ ``config``.
        notebook (google.cloud.dataplex_v1.types.Task.NotebookTaskConfig):
            Config related to running scheduled
            Notebooks.

            This field is a member of `oneof`_ ``config``.
    """

    class InfrastructureSpec(proto.Message):
        r"""Configuration for the underlying infrastructure used to run
        workloads.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            batch (google.cloud.dataplex_v1.types.Task.InfrastructureSpec.BatchComputeResources):
                Compute resources needed for a Task when
                using Dataproc Serverless.

                This field is a member of `oneof`_ ``resources``.
            container_image (google.cloud.dataplex_v1.types.Task.InfrastructureSpec.ContainerImageRuntime):
                Container Image Runtime Configuration.

                This field is a member of `oneof`_ ``runtime``.
            vpc_network (google.cloud.dataplex_v1.types.Task.InfrastructureSpec.VpcNetwork):
                Vpc network.

                This field is a member of `oneof`_ ``network``.
        """

        class BatchComputeResources(proto.Message):
            r"""Batch compute resources associated with the task.

            Attributes:
                executors_count (int):
                    Optional. Total number of job executors. Executor Count
                    should be between 2 and 100. [Default=2]
                max_executors_count (int):
                    Optional. Max configurable executors. If max_executors_count
                    > executors_count, then auto-scaling is enabled. Max
                    Executor Count should be between 2 and 1000. [Default=1000]
            """

            executors_count: int = proto.Field(
                proto.INT32,
                number=1,
            )
            max_executors_count: int = proto.Field(
                proto.INT32,
                number=2,
            )

        class ContainerImageRuntime(proto.Message):
            r"""Container Image Runtime Configuration used with Batch
            execution.

            Attributes:
                image (str):
                    Optional. Container image to use.
                java_jars (MutableSequence[str]):
                    Optional. A list of Java JARS to add to the
                    classpath. Valid input includes Cloud Storage
                    URIs to Jar binaries. For example,
                    gs://bucket-name/my/path/to/file.jar
                python_packages (MutableSequence[str]):
                    Optional. A list of python packages to be
                    installed. Valid formats include Cloud Storage
                    URI to a PIP installable library. For example,
                    gs://bucket-name/my/path/to/lib.tar.gz
                properties (MutableMapping[str, str]):
                    Optional. Override to common configuration of open source
                    components installed on the Dataproc cluster. The properties
                    to set on daemon config files. Property keys are specified
                    in ``prefix:property`` format, for example
                    ``core:hadoop.tmp.dir``. For more information, see `Cluster
                    properties <https://cloud.google.com/dataproc/docs/concepts/cluster-properties>`__.
            """

            image: str = proto.Field(
                proto.STRING,
                number=1,
            )
            java_jars: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=2,
            )
            python_packages: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=3,
            )
            properties: MutableMapping[str, str] = proto.MapField(
                proto.STRING,
                proto.STRING,
                number=4,
            )

        class VpcNetwork(proto.Message):
            r"""Cloud VPC Network used to run the infrastructure.

            This message has `oneof`_ fields (mutually exclusive fields).
            For each oneof, at most one member field can be set at the same time.
            Setting any member of the oneof automatically clears all other
            members.

            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                network (str):
                    Optional. The Cloud VPC network in which the
                    job is run. By default, the Cloud VPC network
                    named Default within the project is used.

                    This field is a member of `oneof`_ ``network_name``.
                sub_network (str):
                    Optional. The Cloud VPC sub-network in which
                    the job is run.

                    This field is a member of `oneof`_ ``network_name``.
                network_tags (MutableSequence[str]):
                    Optional. List of network tags to apply to
                    the job.
            """

            network: str = proto.Field(
                proto.STRING,
                number=1,
                oneof="network_name",
            )
            sub_network: str = proto.Field(
                proto.STRING,
                number=2,
                oneof="network_name",
            )
            network_tags: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=3,
            )

        batch: "Task.InfrastructureSpec.BatchComputeResources" = proto.Field(
            proto.MESSAGE,
            number=52,
            oneof="resources",
            message="Task.InfrastructureSpec.BatchComputeResources",
        )
        container_image: "Task.InfrastructureSpec.ContainerImageRuntime" = proto.Field(
            proto.MESSAGE,
            number=101,
            oneof="runtime",
            message="Task.InfrastructureSpec.ContainerImageRuntime",
        )
        vpc_network: "Task.InfrastructureSpec.VpcNetwork" = proto.Field(
            proto.MESSAGE,
            number=150,
            oneof="network",
            message="Task.InfrastructureSpec.VpcNetwork",
        )

    class TriggerSpec(proto.Message):
        r"""Task scheduling and trigger settings.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            type_ (google.cloud.dataplex_v1.types.Task.TriggerSpec.Type):
                Required. Immutable. Trigger type of the
                user-specified Task.
            start_time (google.protobuf.timestamp_pb2.Timestamp):
                Optional. The first run of the task will be after this time.
                If not specified, the task will run shortly after being
                submitted if ON_DEMAND and based on the schedule if
                RECURRING.
            disabled (bool):
                Optional. Prevent the task from executing.
                This does not cancel already running tasks. It
                is intended to temporarily disable RECURRING
                tasks.
            max_retries (int):
                Optional. Number of retry attempts before
                aborting. Set to zero to never attempt to retry
                a failed task.
            schedule (str):
                Optional. Cron schedule (https://en.wikipedia.org/wiki/Cron)
                for running tasks periodically. To explicitly set a timezone
                to the cron tab, apply a prefix in the cron tab:
                "CRON_TZ=${IANA_TIME_ZONE}" or "TZ=${IANA_TIME_ZONE}". The
                ${IANA_TIME_ZONE} may only be a valid string from IANA time
                zone database. For example,
                ``CRON_TZ=America/New_York 1 * * * *``, or
                ``TZ=America/New_York 1 * * * *``. This field is required
                for RECURRING tasks.

                This field is a member of `oneof`_ ``trigger``.
        """

        class Type(proto.Enum):
            r"""Determines how often and when the job will run.

            Values:
                TYPE_UNSPECIFIED (0):
                    Unspecified trigger type.
                ON_DEMAND (1):
                    The task runs one-time shortly after Task
                    Creation.
                RECURRING (2):
                    The task is scheduled to run periodically.
            """

            TYPE_UNSPECIFIED = 0
            ON_DEMAND = 1
            RECURRING = 2

        type_: "Task.TriggerSpec.Type" = proto.Field(
            proto.ENUM,
            number=5,
            enum="Task.TriggerSpec.Type",
        )
        start_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=6,
            message=timestamp_pb2.Timestamp,
        )
        disabled: bool = proto.Field(
            proto.BOOL,
            number=4,
        )
        max_retries: int = proto.Field(
            proto.INT32,
            number=7,
        )
        schedule: str = proto.Field(
            proto.STRING,
            number=100,
            oneof="trigger",
        )

    class ExecutionSpec(proto.Message):
        r"""Execution related settings, like retry and service_account.

        Attributes:
            args (MutableMapping[str, str]):
                Optional. The arguments to pass to the task. The args can
                use placeholders of the format ${placeholder} as part of
                key/value string. These will be interpolated before passing
                the args to the driver. Currently supported placeholders:

                - ${task_id}
                - ${job_time} To pass positional args, set the key as
                  TASK_ARGS. The value should be a comma-separated string of
                  all the positional arguments. To use a delimiter other
                  than comma, refer to
                  https://cloud.google.com/sdk/gcloud/reference/topic/escaping.
                  In case of other keys being present in the args, then
                  TASK_ARGS will be passed as the last argument.
            service_account (str):
                Required. Service account to use to execute a
                task. If not provided, the default Compute
                service account for the project is used.
            project (str):
                Optional. The project in which jobs are run. By default, the
                project containing the Lake is used. If a project is
                provided, the
                [ExecutionSpec.service_account][google.cloud.dataplex.v1.Task.ExecutionSpec.service_account]
                must belong to this project.
            max_job_execution_lifetime (google.protobuf.duration_pb2.Duration):
                Optional. The maximum duration after which
                the job execution is expired.
            kms_key (str):
                Optional. The Cloud KMS key to use for encryption, of the
                form:
                ``projects/{project_number}/locations/{location_id}/keyRings/{key-ring-name}/cryptoKeys/{key-name}``.
        """

        args: MutableMapping[str, str] = proto.MapField(
            proto.STRING,
            proto.STRING,
            number=4,
        )
        service_account: str = proto.Field(
            proto.STRING,
            number=5,
        )
        project: str = proto.Field(
            proto.STRING,
            number=7,
        )
        max_job_execution_lifetime: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=8,
            message=duration_pb2.Duration,
        )
        kms_key: str = proto.Field(
            proto.STRING,
            number=9,
        )

    class SparkTaskConfig(proto.Message):
        r"""User-specified config for running a Spark task.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            main_jar_file_uri (str):
                The Cloud Storage URI of the jar file that contains the main
                class. The execution args are passed in as a sequence of
                named process arguments (``--key=value``).

                This field is a member of `oneof`_ ``driver``.
            main_class (str):
                The name of the driver's main class. The jar file that
                contains the class must be in the default CLASSPATH or
                specified in ``jar_file_uris``. The execution args are
                passed in as a sequence of named process arguments
                (``--key=value``).

                This field is a member of `oneof`_ ``driver``.
            python_script_file (str):
                The Gcloud Storage URI of the main Python file to use as the
                driver. Must be a .py file. The execution args are passed in
                as a sequence of named process arguments (``--key=value``).

                This field is a member of `oneof`_ ``driver``.
            sql_script_file (str):
                A reference to a query file. This should be the Cloud
                Storage URI of the query file. The execution args are used
                to declare a set of script variables (``set key="value";``).

                This field is a member of `oneof`_ ``driver``.
            sql_script (str):
                The query text. The execution args are used to declare a set
                of script variables (``set key="value";``).

                This field is a member of `oneof`_ ``driver``.
            file_uris (MutableSequence[str]):
                Optional. Cloud Storage URIs of files to be
                placed in the working directory of each
                executor.
            archive_uris (MutableSequence[str]):
                Optional. Cloud Storage URIs of archives to
                be extracted into the working directory of each
                executor. Supported file types: .jar, .tar,
                .tar.gz, .tgz, and .zip.
            infrastructure_spec (google.cloud.dataplex_v1.types.Task.InfrastructureSpec):
                Optional. Infrastructure specification for
                the execution.
        """

        main_jar_file_uri: str = proto.Field(
            proto.STRING,
            number=100,
            oneof="driver",
        )
        main_class: str = proto.Field(
            proto.STRING,
            number=101,
            oneof="driver",
        )
        python_script_file: str = proto.Field(
            proto.STRING,
            number=102,
            oneof="driver",
        )
        sql_script_file: str = proto.Field(
            proto.STRING,
            number=104,
            oneof="driver",
        )
        sql_script: str = proto.Field(
            proto.STRING,
            number=105,
            oneof="driver",
        )
        file_uris: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=3,
        )
        archive_uris: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=4,
        )
        infrastructure_spec: "Task.InfrastructureSpec" = proto.Field(
            proto.MESSAGE,
            number=6,
            message="Task.InfrastructureSpec",
        )

    class NotebookTaskConfig(proto.Message):
        r"""Config for running scheduled notebooks.

        Attributes:
            notebook (str):
                Required. Path to input notebook. This can be the Cloud
                Storage URI of the notebook file or the path to a Notebook
                Content. The execution args are accessible as environment
                variables (``TASK_key=value``).
            infrastructure_spec (google.cloud.dataplex_v1.types.Task.InfrastructureSpec):
                Optional. Infrastructure specification for
                the execution.
            file_uris (MutableSequence[str]):
                Optional. Cloud Storage URIs of files to be
                placed in the working directory of each
                executor.
            archive_uris (MutableSequence[str]):
                Optional. Cloud Storage URIs of archives to
                be extracted into the working directory of each
                executor. Supported file types: .jar, .tar,
                .tar.gz, .tgz, and .zip.
        """

        notebook: str = proto.Field(
            proto.STRING,
            number=4,
        )
        infrastructure_spec: "Task.InfrastructureSpec" = proto.Field(
            proto.MESSAGE,
            number=3,
            message="Task.InfrastructureSpec",
        )
        file_uris: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=5,
        )
        archive_uris: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=6,
        )

    class ExecutionStatus(proto.Message):
        r"""Status of the task execution (e.g. Jobs).

        Attributes:
            update_time (google.protobuf.timestamp_pb2.Timestamp):
                Output only. Last update time of the status.
            latest_job (google.cloud.dataplex_v1.types.Job):
                Output only. latest job execution
        """

        update_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=3,
            message=timestamp_pb2.Timestamp,
        )
        latest_job: "Job" = proto.Field(
            proto.MESSAGE,
            number=9,
            message="Job",
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    description: str = proto.Field(
        proto.STRING,
        number=5,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=6,
    )
    state: resources.State = proto.Field(
        proto.ENUM,
        number=7,
        enum=resources.State,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=8,
    )
    trigger_spec: TriggerSpec = proto.Field(
        proto.MESSAGE,
        number=100,
        message=TriggerSpec,
    )
    execution_spec: ExecutionSpec = proto.Field(
        proto.MESSAGE,
        number=101,
        message=ExecutionSpec,
    )
    execution_status: ExecutionStatus = proto.Field(
        proto.MESSAGE,
        number=201,
        message=ExecutionStatus,
    )
    spark: SparkTaskConfig = proto.Field(
        proto.MESSAGE,
        number=300,
        oneof="config",
        message=SparkTaskConfig,
    )
    notebook: NotebookTaskConfig = proto.Field(
        proto.MESSAGE,
        number=302,
        oneof="config",
        message=NotebookTaskConfig,
    )


class Job(proto.Message):
    r"""A job represents an instance of a task.

    Attributes:
        name (str):
            Output only. The relative resource name of the job, of the
            form:
            ``projects/{project_number}/locations/{location_id}/lakes/{lake_id}/tasks/{task_id}/jobs/{job_id}``.
        uid (str):
            Output only. System generated globally unique
            ID for the job.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the job was
            started.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the job ended.
        state (google.cloud.dataplex_v1.types.Job.State):
            Output only. Execution state for the job.
        retry_count (int):
            Output only. The number of times the job has
            been retried (excluding the initial attempt).
        service (google.cloud.dataplex_v1.types.Job.Service):
            Output only. The underlying service running a
            job.
        service_job (str):
            Output only. The full resource name for the
            job run under a particular service.
        message (str):
            Output only. Additional information about the
            current state.
        labels (MutableMapping[str, str]):
            Output only. User-defined labels for the
            task.
        trigger (google.cloud.dataplex_v1.types.Job.Trigger):
            Output only. Job execution trigger.
        execution_spec (google.cloud.dataplex_v1.types.Task.ExecutionSpec):
            Output only. Spec related to how a task is
            executed.
    """

    class Service(proto.Enum):
        r"""

        Values:
            SERVICE_UNSPECIFIED (0):
                Service used to run the job is unspecified.
            DATAPROC (1):
                Dataproc service is used to run this job.
        """

        SERVICE_UNSPECIFIED = 0
        DATAPROC = 1

    class State(proto.Enum):
        r"""

        Values:
            STATE_UNSPECIFIED (0):
                The job state is unknown.
            RUNNING (1):
                The job is running.
            CANCELLING (2):
                The job is cancelling.
            CANCELLED (3):
                The job cancellation was successful.
            SUCCEEDED (4):
                The job completed successfully.
            FAILED (5):
                The job is no longer running due to an error.
            ABORTED (6):
                The job was cancelled outside of Dataplex
                Universal Catalog.
        """

        STATE_UNSPECIFIED = 0
        RUNNING = 1
        CANCELLING = 2
        CANCELLED = 3
        SUCCEEDED = 4
        FAILED = 5
        ABORTED = 6

    class Trigger(proto.Enum):
        r"""Job execution trigger.

        Values:
            TRIGGER_UNSPECIFIED (0):
                The trigger is unspecified.
            TASK_CONFIG (1):
                The job was triggered by Dataplex Universal
                Catalog based on trigger spec from task
                definition.
            RUN_REQUEST (2):
                The job was triggered by the explicit call of
                Task API.
        """

        TRIGGER_UNSPECIFIED = 0
        TASK_CONFIG = 1
        RUN_REQUEST = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=2,
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=5,
        enum=State,
    )
    retry_count: int = proto.Field(
        proto.UINT32,
        number=6,
    )
    service: Service = proto.Field(
        proto.ENUM,
        number=7,
        enum=Service,
    )
    service_job: str = proto.Field(
        proto.STRING,
        number=8,
    )
    message: str = proto.Field(
        proto.STRING,
        number=9,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=10,
    )
    trigger: Trigger = proto.Field(
        proto.ENUM,
        number=11,
        enum=Trigger,
    )
    execution_spec: "Task.ExecutionSpec" = proto.Field(
        proto.MESSAGE,
        number=100,
        message="Task.ExecutionSpec",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
