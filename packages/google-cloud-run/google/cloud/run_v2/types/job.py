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

import google.api.launch_stage_pb2 as launch_stage_pb2  # type: ignore
import google.protobuf.duration_pb2 as duration_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.run_v2.types import (
    condition,
    execution_template,
    k8s_min,
    vendor_settings,
)

__protobuf__ = proto.module(
    package="google.cloud.run.v2",
    manifest={
        "CreateJobRequest",
        "GetJobRequest",
        "UpdateJobRequest",
        "ListJobsRequest",
        "ListJobsResponse",
        "DeleteJobRequest",
        "RunJobRequest",
        "Job",
        "ExecutionReference",
    },
)


class CreateJobRequest(proto.Message):
    r"""Request message for creating a Job.

    Attributes:
        parent (str):
            Required. The location and project in which
            this Job should be created. Format:
            projects/{project}/locations/{location}, where
            {project} can be project id or number.
        job (google.cloud.run_v2.types.Job):
            Required. The Job instance to create.
        job_id (str):
            Required. The unique identifier for the Job. The name of the
            job becomes {parent}/jobs/{job_id}.
        validate_only (bool):
            Indicates that the request should be
            validated and default values populated, without
            persisting the request or creating any
            resources.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    job: "Job" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Job",
    )
    job_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class GetJobRequest(proto.Message):
    r"""Request message for obtaining a Job by its full name.

    Attributes:
        name (str):
            Required. The full name of the Job.
            Format:
            projects/{project}/locations/{location}/jobs/{job},
            where {project} can be project id or number.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateJobRequest(proto.Message):
    r"""Request message for updating a Job.

    Attributes:
        job (google.cloud.run_v2.types.Job):
            Required. The Job to be updated.
        validate_only (bool):
            Indicates that the request should be
            validated and default values populated, without
            persisting the request or updating any
            resources.
        allow_missing (bool):
            Optional. If set to true, and if the Job does
            not exist, it will create a new one. Caller must
            have both create and update permissions for this
            call if this is set to true.
    """

    job: "Job" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Job",
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    allow_missing: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class ListJobsRequest(proto.Message):
    r"""Request message for retrieving a list of Jobs.

    Attributes:
        parent (str):
            Required. The location and project to list
            resources on. Format:
            projects/{project}/locations/{location}, where
            {project} can be project id or number.
        page_size (int):
            Maximum number of Jobs to return in this
            call.
        page_token (str):
            A page token received from a previous call to
            ListJobs. All other parameters must match.
        show_deleted (bool):
            If true, returns deleted (but unexpired)
            resources along with active ones.
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
    show_deleted: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class ListJobsResponse(proto.Message):
    r"""Response message containing a list of Jobs.

    Attributes:
        jobs (MutableSequence[google.cloud.run_v2.types.Job]):
            The resulting list of Jobs.
        next_page_token (str):
            A token indicating there are more items than page_size. Use
            it in the next ListJobs request to continue.
    """

    @property
    def raw_page(self):
        return self

    jobs: MutableSequence["Job"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Job",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DeleteJobRequest(proto.Message):
    r"""Request message to delete a Job by its full name.

    Attributes:
        name (str):
            Required. The full name of the Job.
            Format:
            projects/{project}/locations/{location}/jobs/{job},
            where {project} can be project id or number.
        validate_only (bool):
            Indicates that the request should be
            validated without actually deleting any
            resources.
        etag (str):
            A system-generated fingerprint for this
            version of the resource. May be used to detect
            modification conflict during updates.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=4,
    )


class RunJobRequest(proto.Message):
    r"""Request message to create a new Execution of a Job.

    Attributes:
        name (str):
            Required. The full name of the Job.
            Format:
            projects/{project}/locations/{location}/jobs/{job},
            where {project} can be project id or number.
        validate_only (bool):
            Indicates that the request should be
            validated without actually deleting any
            resources.
        etag (str):
            A system-generated fingerprint for this
            version of the resource. May be used to detect
            modification conflict during updates.
        overrides (google.cloud.run_v2.types.RunJobRequest.Overrides):
            Overrides specification for a given execution
            of a job. If provided, overrides will be applied
            to update the execution or task spec.
    """

    class Overrides(proto.Message):
        r"""RunJob Overrides that contains Execution fields to be
        overridden.

        Attributes:
            container_overrides (MutableSequence[google.cloud.run_v2.types.RunJobRequest.Overrides.ContainerOverride]):
                Per container override specification.
            task_count (int):
                Optional. The desired number of tasks the execution should
                run. Will replace existing task_count value.
            timeout (google.protobuf.duration_pb2.Duration):
                Duration in seconds the task may be active before the system
                will actively try to mark it failed and kill associated
                containers. Will replace existing timeout_seconds value.
        """

        class ContainerOverride(proto.Message):
            r"""Per-container override specification.

            Attributes:
                name (str):
                    The name of the container specified as a DNS_LABEL.
                args (MutableSequence[str]):
                    Optional. Arguments to the entrypoint. Will
                    replace existing args for override.
                env (MutableSequence[google.cloud.run_v2.types.EnvVar]):
                    List of environment variables to set in the
                    container. Will be merged with existing env for
                    override.
                clear_args (bool):
                    Optional. True if the intention is to clear
                    out existing args list.
            """

            name: str = proto.Field(
                proto.STRING,
                number=1,
            )
            args: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=2,
            )
            env: MutableSequence[k8s_min.EnvVar] = proto.RepeatedField(
                proto.MESSAGE,
                number=3,
                message=k8s_min.EnvVar,
            )
            clear_args: bool = proto.Field(
                proto.BOOL,
                number=4,
            )

        container_overrides: MutableSequence[
            "RunJobRequest.Overrides.ContainerOverride"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="RunJobRequest.Overrides.ContainerOverride",
        )
        task_count: int = proto.Field(
            proto.INT32,
            number=2,
        )
        timeout: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=4,
            message=duration_pb2.Duration,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=3,
    )
    overrides: Overrides = proto.Field(
        proto.MESSAGE,
        number=4,
        message=Overrides,
    )


class Job(proto.Message):
    r"""Job represents the configuration of a single job, which
    references a container image that is run to completion.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            The fully qualified name of this Job.

            Format:

            projects/{project}/locations/{location}/jobs/{job}
        uid (str):
            Output only. Server assigned unique
            identifier for the Execution. The value is a
            UUID4 string and guaranteed to remain unchanged
            until the resource is deleted.
        generation (int):
            Output only. A number that monotonically
            increases every time the user modifies the
            desired state.
        labels (MutableMapping[str, str]):
            Unstructured key value map that can be used to organize and
            categorize objects. User-provided labels are shared with
            Google's billing system, so they can be used to filter, or
            break down billing charges by team, component, environment,
            state, etc. For more information, visit
            https://cloud.google.com/resource-manager/docs/creating-managing-labels
            or https://cloud.google.com/run/docs/configuring/labels.

            .. raw:: html

                <p>Cloud Run API v2 does not support labels with `run.googleapis.com`,
                `cloud.googleapis.com`, `serving.knative.dev`, or `autoscaling.knative.dev`
                namespaces, and they will be rejected. All system labels in v1 now have a
                corresponding field in v2 Job.
        annotations (MutableMapping[str, str]):
            Unstructured key value map that may be set by external tools
            to store and arbitrary metadata. They are not queryable and
            should be preserved when modifying objects.

            .. raw:: html

                <p>Cloud Run API v2 does not support annotations with `run.googleapis.com`,
                `cloud.googleapis.com`, `serving.knative.dev`, or `autoscaling.knative.dev`
                namespaces, and they will be rejected on new resources. All system
                annotations in v1 now have a corresponding field in v2 Job.

            .. raw:: html

                <p>This field follows Kubernetes annotations' namespacing, limits, and
                rules.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The creation time.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last-modified time.
        delete_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The deletion time. It is only
            populated as a response to a Delete request.
        expire_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. For a deleted resource, the time
            after which it will be permamently deleted.
        creator (str):
            Output only. Email address of the
            authenticated creator.
        last_modifier (str):
            Output only. Email address of the last
            authenticated modifier.
        client (str):
            Arbitrary identifier for the API client.
        client_version (str):
            Arbitrary version identifier for the API
            client.
        launch_stage (google.api.launch_stage_pb2.LaunchStage):
            The launch stage as defined by `Google Cloud Platform Launch
            Stages <https://cloud.google.com/terms/launch-stages>`__.
            Cloud Run supports ``ALPHA``, ``BETA``, and ``GA``. If no
            value is specified, GA is assumed. Set the launch stage to a
            preview stage on input to allow use of preview features in
            that stage. On read (or output), describes whether the
            resource uses preview features.

            For example, if ALPHA is provided as input, but only BETA
            and GA-level features are used, this field will be BETA on
            output.
        binary_authorization (google.cloud.run_v2.types.BinaryAuthorization):
            Settings for the Binary Authorization
            feature.
        template (google.cloud.run_v2.types.ExecutionTemplate):
            Required. The template used to create
            executions for this Job.
        observed_generation (int):
            Output only. The generation of this Job. See comments in
            ``reconciling`` for additional information on reconciliation
            process in Cloud Run.
        terminal_condition (google.cloud.run_v2.types.Condition):
            Output only. The Condition of this Job,
            containing its readiness status, and detailed
            error information in case it did not reach the
            desired state.
        conditions (MutableSequence[google.cloud.run_v2.types.Condition]):
            Output only. The Conditions of all other associated
            sub-resources. They contain additional diagnostics
            information in case the Job does not reach its desired
            state. See comments in ``reconciling`` for additional
            information on reconciliation process in Cloud Run.
        execution_count (int):
            Output only. Number of executions created for
            this job.
        latest_created_execution (google.cloud.run_v2.types.ExecutionReference):
            Output only. Name of the last created
            execution.
        reconciling (bool):
            Output only. Returns true if the Job is currently being
            acted upon by the system to bring it into the desired state.

            When a new Job is created, or an existing one is updated,
            Cloud Run will asynchronously perform all necessary steps to
            bring the Job to the desired state. This process is called
            reconciliation. While reconciliation is in process,
            ``observed_generation`` and ``latest_succeeded_execution``,
            will have transient values that might mismatch the intended
            state: Once reconciliation is over (and this field is
            false), there are two possible outcomes: reconciliation
            succeeded and the state matches the Job, or there was an
            error, and reconciliation failed. This state can be found in
            ``terminal_condition.state``.

            If reconciliation succeeded, the following fields will
            match: ``observed_generation`` and ``generation``,
            ``latest_succeeded_execution`` and
            ``latest_created_execution``.

            If reconciliation failed, ``observed_generation`` and
            ``latest_succeeded_execution`` will have the state of the
            last succeeded execution or empty for newly created Job.
            Additional information on the failure can be found in
            ``terminal_condition`` and ``conditions``.
        satisfies_pzs (bool):
            Output only. Reserved for future use.
        start_execution_token (str):
            A unique string used as a suffix creating a
            new execution. The Job will become ready when
            the execution is successfully started. The sum
            of job name and token length must be fewer than
            63 characters.

            This field is a member of `oneof`_ ``create_execution``.
        run_execution_token (str):
            A unique string used as a suffix for creating
            a new execution. The Job will become ready when
            the execution is successfully completed. The sum
            of job name and token length must be fewer than
            63 characters.

            This field is a member of `oneof`_ ``create_execution``.
        etag (str):
            Optional. A system-generated fingerprint for
            this version of the resource. May be used to
            detect modification conflict during updates.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=2,
    )
    generation: int = proto.Field(
        proto.INT64,
        number=3,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    annotations: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    delete_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    expire_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    creator: str = proto.Field(
        proto.STRING,
        number=10,
    )
    last_modifier: str = proto.Field(
        proto.STRING,
        number=11,
    )
    client: str = proto.Field(
        proto.STRING,
        number=12,
    )
    client_version: str = proto.Field(
        proto.STRING,
        number=13,
    )
    launch_stage: launch_stage_pb2.LaunchStage = proto.Field(
        proto.ENUM,
        number=14,
        enum=launch_stage_pb2.LaunchStage,
    )
    binary_authorization: vendor_settings.BinaryAuthorization = proto.Field(
        proto.MESSAGE,
        number=15,
        message=vendor_settings.BinaryAuthorization,
    )
    template: execution_template.ExecutionTemplate = proto.Field(
        proto.MESSAGE,
        number=16,
        message=execution_template.ExecutionTemplate,
    )
    observed_generation: int = proto.Field(
        proto.INT64,
        number=17,
    )
    terminal_condition: condition.Condition = proto.Field(
        proto.MESSAGE,
        number=18,
        message=condition.Condition,
    )
    conditions: MutableSequence[condition.Condition] = proto.RepeatedField(
        proto.MESSAGE,
        number=19,
        message=condition.Condition,
    )
    execution_count: int = proto.Field(
        proto.INT32,
        number=20,
    )
    latest_created_execution: "ExecutionReference" = proto.Field(
        proto.MESSAGE,
        number=22,
        message="ExecutionReference",
    )
    reconciling: bool = proto.Field(
        proto.BOOL,
        number=23,
    )
    satisfies_pzs: bool = proto.Field(
        proto.BOOL,
        number=25,
    )
    start_execution_token: str = proto.Field(
        proto.STRING,
        number=26,
        oneof="create_execution",
    )
    run_execution_token: str = proto.Field(
        proto.STRING,
        number=27,
        oneof="create_execution",
    )
    etag: str = proto.Field(
        proto.STRING,
        number=99,
    )


class ExecutionReference(proto.Message):
    r"""Reference to an Execution. Use /Executions.GetExecution with
    the given name to get full execution including the latest
    status.

    Attributes:
        name (str):
            Name of the execution.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Creation timestamp of the execution.
        completion_time (google.protobuf.timestamp_pb2.Timestamp):
            Creation timestamp of the execution.
        delete_time (google.protobuf.timestamp_pb2.Timestamp):
            The deletion time of the execution. It is
            only populated as a response to a Delete
            request.
        completion_status (google.cloud.run_v2.types.ExecutionReference.CompletionStatus):
            Status for the execution completion.
    """

    class CompletionStatus(proto.Enum):
        r"""Possible execution completion status.

        Values:
            COMPLETION_STATUS_UNSPECIFIED (0):
                The default value. This value is used if the
                state is omitted.
            EXECUTION_SUCCEEDED (1):
                Job execution has succeeded.
            EXECUTION_FAILED (2):
                Job execution has failed.
            EXECUTION_RUNNING (3):
                Job execution is running normally.
            EXECUTION_PENDING (4):
                Waiting for backing resources to be
                provisioned.
            EXECUTION_CANCELLED (5):
                Job execution has been cancelled by the user.
        """

        COMPLETION_STATUS_UNSPECIFIED = 0
        EXECUTION_SUCCEEDED = 1
        EXECUTION_FAILED = 2
        EXECUTION_RUNNING = 3
        EXECUTION_PENDING = 4
        EXECUTION_CANCELLED = 5

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    completion_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    delete_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    completion_status: CompletionStatus = proto.Field(
        proto.ENUM,
        number=4,
        enum=CompletionStatus,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
