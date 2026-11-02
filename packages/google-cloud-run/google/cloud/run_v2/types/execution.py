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
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.run_v2.types import condition, task_template

__protobuf__ = proto.module(
    package="google.cloud.run.v2",
    manifest={
        "GetExecutionRequest",
        "ListExecutionsRequest",
        "ListExecutionsResponse",
        "DeleteExecutionRequest",
        "CancelExecutionRequest",
        "Execution",
    },
)


class GetExecutionRequest(proto.Message):
    r"""Request message for obtaining a Execution by its full name.

    Attributes:
        name (str):
            Required. The full name of the Execution. Format:
            ``projects/{project}/locations/{location}/jobs/{job}/executions/{execution}``,
            where ``{project}`` can be project id or number.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListExecutionsRequest(proto.Message):
    r"""Request message for retrieving a list of Executions.

    Attributes:
        parent (str):
            Required. The Execution from which the Executions should be
            listed. To list all Executions across Jobs, use "-" instead
            of Job name. Format:
            ``projects/{project}/locations/{location}/jobs/{job}``,
            where ``{project}`` can be project id or number.
        page_size (int):
            Maximum number of Executions to return in
            this call.
        page_token (str):
            A page token received from a previous call to
            ListExecutions. All other parameters must match.
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


class ListExecutionsResponse(proto.Message):
    r"""Response message containing a list of Executions.

    Attributes:
        executions (MutableSequence[google.cloud.run_v2.types.Execution]):
            The resulting list of Executions.
        next_page_token (str):
            A token indicating there are more items than page_size. Use
            it in the next ListExecutions request to continue.
    """

    @property
    def raw_page(self):
        return self

    executions: MutableSequence["Execution"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Execution",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DeleteExecutionRequest(proto.Message):
    r"""Request message for deleting an Execution.

    Attributes:
        name (str):
            Required. The name of the Execution to delete. Format:
            ``projects/{project}/locations/{location}/jobs/{job}/executions/{execution}``,
            where ``{project}`` can be project id or number.
        validate_only (bool):
            Indicates that the request should be
            validated without actually deleting any
            resources.
        etag (str):
            A system-generated fingerprint for this
            version of the resource. This may be used to
            detect modification conflict during updates.
    """

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


class CancelExecutionRequest(proto.Message):
    r"""Request message for deleting an Execution.

    Attributes:
        name (str):
            Required. The name of the Execution to cancel. Format:
            ``projects/{project}/locations/{location}/jobs/{job}/executions/{execution}``,
            where ``{project}`` can be project id or number.
        validate_only (bool):
            Indicates that the request should be
            validated without actually cancelling any
            resources.
        etag (str):
            A system-generated fingerprint for this
            version of the resource. This may be used to
            detect modification conflict during updates.
    """

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


class Execution(proto.Message):
    r"""Execution represents the configuration of a single execution.
    A execution an immutable resource that references a container
    image which is run to completion.

    Attributes:
        name (str):
            Output only. The unique name of this
            Execution.
        uid (str):
            Output only. Server assigned unique
            identifier for the Execution. The value is a
            UUID4 string and guaranteed to remain unchanged
            until the resource is deleted.
        creator (str):
            Output only. Email address of the
            authenticated creator.
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
            Output only. Represents time when the
            execution was acknowledged by the execution
            controller. It is not guaranteed to be set in
            happens-before order across separate operations.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Represents time when the
            execution started to run. It is not guaranteed
            to be set in happens-before order across
            separate operations.
        completion_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Represents time when the
            execution was completed. It is not guaranteed to
            be set in happens-before order across separate
            operations.
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
        launch_stage (google.api.launch_stage_pb2.LaunchStage):
            The least stable launch stage needed to create this
            resource, as defined by `Google Cloud Platform Launch
            Stages <https://cloud.google.com/terms/launch-stages>`__.
            Cloud Run supports ``ALPHA``, ``BETA``, and ``GA``.

            Note that this value might not be what was used as input.
            For example, if ALPHA was provided as input in the parent
            resource, but only BETA and GA-level features are were, this
            field will be BETA.
        job (str):
            Output only. The name of the parent Job.
        parallelism (int):
            Output only. Specifies the maximum desired number of tasks
            the execution should run at any given time. Must be <=
            task_count. The actual number of tasks running in steady
            state will be less than this number when ((.spec.task_count
            - .status.successful) < .spec.parallelism), i.e. when the
            work left to do is less than max parallelism.
        task_count (int):
            Output only. Specifies the desired number of
            tasks the execution should run. Setting to 1
            means that parallelism is limited to 1 and the
            success of that task signals the success of the
            execution.
        template (google.cloud.run_v2.types.TaskTemplate):
            Output only. The template used to create
            tasks for this execution.
        reconciling (bool):
            Output only. Indicates whether the resource's reconciliation
            is still in progress. See comments in ``Job.reconciling``
            for additional information on reconciliation process in
            Cloud Run.
        conditions (MutableSequence[google.cloud.run_v2.types.Condition]):
            Output only. The Condition of this Execution,
            containing its readiness status, and detailed
            error information in case it did not reach the
            desired state.
        observed_generation (int):
            Output only. The generation of this Execution. See comments
            in ``reconciling`` for additional information on
            reconciliation process in Cloud Run.
        running_count (int):
            Output only. The number of actively running
            tasks.
        succeeded_count (int):
            Output only. The number of tasks which
            reached phase Succeeded.
        failed_count (int):
            Output only. The number of tasks which
            reached phase Failed.
        cancelled_count (int):
            Output only. The number of tasks which
            reached phase Cancelled.
        retried_count (int):
            Output only. The number of tasks which have
            retried at least once.
        log_uri (str):
            Output only. URI where logs for this
            execution can be found in Cloud Console.
        satisfies_pzs (bool):
            Output only. Reserved for future use.
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
    creator: str = proto.Field(
        proto.STRING,
        number=32,
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
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=22,
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
    launch_stage: launch_stage_pb2.LaunchStage = proto.Field(
        proto.ENUM,
        number=11,
        enum=launch_stage_pb2.LaunchStage,
    )
    job: str = proto.Field(
        proto.STRING,
        number=12,
    )
    parallelism: int = proto.Field(
        proto.INT32,
        number=13,
    )
    task_count: int = proto.Field(
        proto.INT32,
        number=14,
    )
    template: task_template.TaskTemplate = proto.Field(
        proto.MESSAGE,
        number=15,
        message=task_template.TaskTemplate,
    )
    reconciling: bool = proto.Field(
        proto.BOOL,
        number=16,
    )
    conditions: MutableSequence[condition.Condition] = proto.RepeatedField(
        proto.MESSAGE,
        number=17,
        message=condition.Condition,
    )
    observed_generation: int = proto.Field(
        proto.INT64,
        number=18,
    )
    running_count: int = proto.Field(
        proto.INT32,
        number=19,
    )
    succeeded_count: int = proto.Field(
        proto.INT32,
        number=20,
    )
    failed_count: int = proto.Field(
        proto.INT32,
        number=21,
    )
    cancelled_count: int = proto.Field(
        proto.INT32,
        number=24,
    )
    retried_count: int = proto.Field(
        proto.INT32,
        number=25,
    )
    log_uri: str = proto.Field(
        proto.STRING,
        number=26,
    )
    satisfies_pzs: bool = proto.Field(
        proto.BOOL,
        number=27,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=99,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
