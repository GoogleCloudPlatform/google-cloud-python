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
import google.rpc.status_pb2 as status_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.run_v2.types import condition, k8s_min, vendor_settings

__protobuf__ = proto.module(
    package="google.cloud.run.v2",
    manifest={
        "GetTaskRequest",
        "ListTasksRequest",
        "ListTasksResponse",
        "Task",
        "TaskAttemptResult",
    },
)


class GetTaskRequest(proto.Message):
    r"""Request message for obtaining a Task by its full name.

    Attributes:
        name (str):
            Required. The full name of the Task.
            Format:

            projects/{project}/locations/{location}/jobs/{job}/executions/{execution}/tasks/{task}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListTasksRequest(proto.Message):
    r"""Request message for retrieving a list of Tasks.

    Attributes:
        parent (str):
            Required. The Execution from which the Tasks
            should be listed. To list all Tasks across
            Executions of a Job, use "-" instead of
            Execution name. To list all Tasks across Jobs,
            use "-" instead of Job name. Format:

            projects/{project}/locations/{location}/jobs/{job}/executions/{execution}
        page_size (int):
            Maximum number of Tasks to return in this
            call.
        page_token (str):
            A page token received from a previous call to
            ListTasks. All other parameters must match.
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


class ListTasksResponse(proto.Message):
    r"""Response message containing a list of Tasks.

    Attributes:
        tasks (MutableSequence[google.cloud.run_v2.types.Task]):
            The resulting list of Tasks.
        next_page_token (str):
            A token indicating there are more items than page_size. Use
            it in the next ListTasks request to continue.
    """

    @property
    def raw_page(self):
        return self

    tasks: MutableSequence["Task"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Task",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class Task(proto.Message):
    r"""Task represents a single run of a container to completion.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Output only. The unique name of this Task.
        uid (str):
            Output only. Server assigned unique
            identifier for the Task. The value is a UUID4
            string and guaranteed to remain unchanged until
            the resource is deleted.
        generation (int):
            Output only. A number that monotonically
            increases every time the user modifies the
            desired state.
        labels (MutableMapping[str, str]):
            Output only. Unstructured key value map that
            can be used to organize and categorize objects.
            User-provided labels are shared with Google's
            billing system, so they can be used to filter,
            or break down billing charges by team,
            component, environment, state, etc. For more
            information, visit
            https://cloud.google.com/resource-manager/docs/creating-managing-labels
            or
            https://cloud.google.com/run/docs/configuring/labels
        annotations (MutableMapping[str, str]):
            Output only. Unstructured key value map that
            may be set by external tools to store and
            arbitrary metadata. They are not queryable and
            should be preserved when modifying objects.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Represents time when the task
            was created by the system. It is not guaranteed
            to be set in happens-before order across
            separate operations.
        scheduled_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Represents time when the task
            was scheduled to run by the system. It is not
            guaranteed to be set in happens-before order
            across separate operations.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Represents time when the task
            started to run. It is not guaranteed to be set
            in happens-before order across separate
            operations.
        completion_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Represents time when the Task
            was completed. It is not guaranteed to be set in
            happens-before order across separate operations.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last-modified time.
        delete_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. For a deleted resource, the
            deletion time. It is only populated as a
            response to a Delete request.
        expire_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. For a deleted resource, the time
            after which it will be permamently deleted. It
            is only populated as a response to a Delete
            request.
        job (str):
            Output only. The name of the parent Job.
        execution (str):
            Output only. The name of the parent
            Execution.
        containers (MutableSequence[google.cloud.run_v2.types.Container]):
            Holds the single container that defines the
            unit of execution for this task.
        volumes (MutableSequence[google.cloud.run_v2.types.Volume]):
            A list of Volumes to make available to
            containers.
        max_retries (int):
            Number of retries allowed per Task, before
            marking this Task failed.
        timeout (google.protobuf.duration_pb2.Duration):
            Max allowed time duration the Task may be
            active before the system will actively try to
            mark it failed and kill associated containers.
            This applies per attempt of a task, meaning each
            retry can run for the full timeout.
        service_account (str):
            Email address of the IAM service account
            associated with the Task of a Job. The service
            account represents the identity of the running
            task, and determines what permissions the task
            has. If not provided, the task will use the
            project's default service account.
        execution_environment (google.cloud.run_v2.types.ExecutionEnvironment):
            The execution environment being used to host
            this Task.
        reconciling (bool):
            Output only. Indicates whether the resource's reconciliation
            is still in progress. See comments in ``Job.reconciling``
            for additional information on reconciliation process in
            Cloud Run.
        conditions (MutableSequence[google.cloud.run_v2.types.Condition]):
            Output only. The Condition of this Task,
            containing its readiness status, and detailed
            error information in case it did not reach the
            desired state.
        observed_generation (int):
            Output only. The generation of this Task. See comments in
            ``Job.reconciling`` for additional information on
            reconciliation process in Cloud Run.
        index (int):
            Output only. Index of the Task, unique per
            execution, and beginning at 0.
        retried (int):
            Output only. The number of times this Task
            was retried. Tasks are retried when they fail up
            to the maxRetries limit.
        last_attempt_result (google.cloud.run_v2.types.TaskAttemptResult):
            Output only. Result of the last attempt of
            this Task.
        encryption_key (str):
            Output only. A reference to a customer
            managed encryption key (CMEK) to use to encrypt
            this container image. For more information, go
            to
            https://cloud.google.com/run/docs/securing/using-cmek
        vpc_access (google.cloud.run_v2.types.VpcAccess):
            Output only. VPC Access configuration to use
            for this Task. For more information, visit
            https://cloud.google.com/run/docs/configuring/connecting-vpc.
        log_uri (str):
            Output only. URI where logs for this
            execution can be found in Cloud Console.
        satisfies_pzs (bool):
            Output only. Reserved for future use.
        node_selector (google.cloud.run_v2.types.NodeSelector):
            Output only. The node selector for the task.
        gpu_zonal_redundancy_disabled (bool):
            Optional. Output only. True if GPU zonal
            redundancy is disabled on this task.

            This field is a member of `oneof`_ ``_gpu_zonal_redundancy_disabled``.
        etag (str):
            Output only. A system-generated fingerprint
            for this version of the resource. May be used to
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
    scheduled_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=34,
        message=timestamp_pb2.Timestamp,
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=27,
        message=timestamp_pb2.Timestamp,
    )
    completion_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    delete_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    expire_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10,
        message=timestamp_pb2.Timestamp,
    )
    job: str = proto.Field(
        proto.STRING,
        number=12,
    )
    execution: str = proto.Field(
        proto.STRING,
        number=13,
    )
    containers: MutableSequence[k8s_min.Container] = proto.RepeatedField(
        proto.MESSAGE,
        number=14,
        message=k8s_min.Container,
    )
    volumes: MutableSequence[k8s_min.Volume] = proto.RepeatedField(
        proto.MESSAGE,
        number=15,
        message=k8s_min.Volume,
    )
    max_retries: int = proto.Field(
        proto.INT32,
        number=16,
    )
    timeout: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=17,
        message=duration_pb2.Duration,
    )
    service_account: str = proto.Field(
        proto.STRING,
        number=18,
    )
    execution_environment: vendor_settings.ExecutionEnvironment = proto.Field(
        proto.ENUM,
        number=20,
        enum=vendor_settings.ExecutionEnvironment,
    )
    reconciling: bool = proto.Field(
        proto.BOOL,
        number=21,
    )
    conditions: MutableSequence[condition.Condition] = proto.RepeatedField(
        proto.MESSAGE,
        number=22,
        message=condition.Condition,
    )
    observed_generation: int = proto.Field(
        proto.INT64,
        number=23,
    )
    index: int = proto.Field(
        proto.INT32,
        number=24,
    )
    retried: int = proto.Field(
        proto.INT32,
        number=25,
    )
    last_attempt_result: "TaskAttemptResult" = proto.Field(
        proto.MESSAGE,
        number=26,
        message="TaskAttemptResult",
    )
    encryption_key: str = proto.Field(
        proto.STRING,
        number=28,
    )
    vpc_access: vendor_settings.VpcAccess = proto.Field(
        proto.MESSAGE,
        number=29,
        message=vendor_settings.VpcAccess,
    )
    log_uri: str = proto.Field(
        proto.STRING,
        number=32,
    )
    satisfies_pzs: bool = proto.Field(
        proto.BOOL,
        number=33,
    )
    node_selector: vendor_settings.NodeSelector = proto.Field(
        proto.MESSAGE,
        number=36,
        message=vendor_settings.NodeSelector,
    )
    gpu_zonal_redundancy_disabled: bool = proto.Field(
        proto.BOOL,
        number=37,
        optional=True,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=99,
    )


class TaskAttemptResult(proto.Message):
    r"""Result of a task attempt.

    Attributes:
        status (google.rpc.status_pb2.Status):
            Output only. The status of this attempt.
            If the status code is OK, then the attempt
            succeeded.
        exit_code (int):
            Output only. The exit code of this attempt. This may be
            unset if the container was unable to exit cleanly with a
            code due to some other failure. See status field for
            possible failure details.

            At most one of exit_code or term_signal will be set.
        term_signal (int):
            Output only. Termination signal of the container. This is
            set to non-zero if the container is terminated by the
            system.

            At most one of exit_code or term_signal will be set.
    """

    status: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=1,
        message=status_pb2.Status,
    )
    exit_code: int = proto.Field(
        proto.INT32,
        number=2,
    )
    term_signal: int = proto.Field(
        proto.INT32,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
