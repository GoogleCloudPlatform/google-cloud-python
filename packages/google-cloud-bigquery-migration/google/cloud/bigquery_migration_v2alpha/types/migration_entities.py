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

import google.protobuf.any_pb2 as any_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.rpc.error_details_pb2 as error_details_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.bigquery_migration_v2alpha.types import (
    assessment_task,
    migration_error_details,
    migration_metrics,
    translation_task,
)

__protobuf__ = proto.module(
    package="google.cloud.bigquery.migration.v2alpha",
    manifest={
        "MigrationWorkflow",
        "MigrationTask",
        "MigrationSubtask",
        "MigrationTaskOrchestrationResult",
    },
)


class MigrationWorkflow(proto.Message):
    r"""A migration workflow which specifies what needs to be done
    for an EDW migration.

    Attributes:
        name (str):
            Output only. Immutable. The unique identifier for the
            migration workflow. The ID is server-generated.

            Example: ``projects/123/locations/us/workflows/345``
        display_name (str):
            The display name of the workflow. This can be
            set to give a workflow a descriptive name. There
            is no guarantee or enforcement of uniqueness.
        tasks (MutableMapping[str, google.cloud.bigquery_migration_v2alpha.types.MigrationTask]):
            The tasks in a workflow in a named map. The
            name (i.e. key) has no meaning and is merely a
            convenient way to address a specific task in a
            workflow.
        state (google.cloud.bigquery_migration_v2alpha.types.MigrationWorkflow.State):
            Output only. That status of the workflow.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Time when the workflow was created.
        last_update_time (google.protobuf.timestamp_pb2.Timestamp):
            Time when the workflow was last updated.
    """

    class State(proto.Enum):
        r"""Possible migration workflow states.

        Values:
            STATE_UNSPECIFIED (0):
                Workflow state is unspecified.
            DRAFT (1):
                Workflow is in draft status, i.e. tasks are
                not yet eligible for execution.
            RUNNING (2):
                Workflow is running (i.e. tasks are eligible
                for execution).
            PAUSED (3):
                Workflow is paused. Tasks currently in
                progress may continue, but no further tasks will
                be scheduled.
            COMPLETED (4):
                Workflow is complete. There should not be any
                task in a non-terminal state, but if they are
                (e.g. forced termination), they will not be
                scheduled.
        """

        STATE_UNSPECIFIED = 0
        DRAFT = 1
        RUNNING = 2
        PAUSED = 3
        COMPLETED = 4

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=6,
    )
    tasks: MutableMapping[str, "MigrationTask"] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=2,
        message="MigrationTask",
    )
    state: State = proto.Field(
        proto.ENUM,
        number=3,
        enum=State,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    last_update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )


class MigrationTask(proto.Message):
    r"""A single task for a migration which has details about the
    configuration of the task.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        assessment_task_details (google.cloud.bigquery_migration_v2alpha.types.AssessmentTaskDetails):
            Task configuration for Assessment.

            This field is a member of `oneof`_ ``task_details``.
        translation_task_details (google.cloud.bigquery_migration_v2alpha.types.TranslationTaskDetails):
            Task configuration for Batch/Offline SQL
            Translation.

            This field is a member of `oneof`_ ``task_details``.
        id (str):
            Output only. Immutable. The unique identifier
            for the migration task. The ID is
            server-generated.
        type_ (str):
            The type of the task. This must be a
            supported task type.
        details (google.protobuf.any_pb2.Any):
            DEPRECATED! Use one of the task_details below. The details
            of the task. The type URL must be one of the supported task
            details messages and correspond to the Task's type.
        state (google.cloud.bigquery_migration_v2alpha.types.MigrationTask.State):
            Output only. The current state of the task.
        processing_error (google.rpc.error_details_pb2.ErrorInfo):
            Output only. An explanation that may be
            populated when the task is in FAILED state.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Time when the task was created.
        last_update_time (google.protobuf.timestamp_pb2.Timestamp):
            Time when the task was last updated.
        orchestration_result (google.cloud.bigquery_migration_v2alpha.types.MigrationTaskOrchestrationResult):
            Output only. Additional information about the
            orchestration.
    """

    class State(proto.Enum):
        r"""Possible states of a migration task.

        Values:
            STATE_UNSPECIFIED (0):
                The state is unspecified.
            PENDING (1):
                The task is waiting for orchestration.
            ORCHESTRATING (2):
                The task is assigned to an orchestrator.
            RUNNING (3):
                The task is running, i.e. its subtasks are
                ready for execution.
            PAUSED (4):
                Tha task is paused. Assigned subtasks can
                continue, but no new subtasks will be scheduled.
            SUCCEEDED (5):
                The task finished successfully.
            FAILED (6):
                The task finished unsuccessfully.
        """

        STATE_UNSPECIFIED = 0
        PENDING = 1
        ORCHESTRATING = 2
        RUNNING = 3
        PAUSED = 4
        SUCCEEDED = 5
        FAILED = 6

    assessment_task_details: assessment_task.AssessmentTaskDetails = proto.Field(
        proto.MESSAGE,
        number=12,
        oneof="task_details",
        message=assessment_task.AssessmentTaskDetails,
    )
    translation_task_details: translation_task.TranslationTaskDetails = proto.Field(
        proto.MESSAGE,
        number=13,
        oneof="task_details",
        message=translation_task.TranslationTaskDetails,
    )
    id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    type_: str = proto.Field(
        proto.STRING,
        number=2,
    )
    details: any_pb2.Any = proto.Field(
        proto.MESSAGE,
        number=3,
        message=any_pb2.Any,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=4,
        enum=State,
    )
    processing_error: error_details_pb2.ErrorInfo = proto.Field(
        proto.MESSAGE,
        number=5,
        message=error_details_pb2.ErrorInfo,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    last_update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    orchestration_result: "MigrationTaskOrchestrationResult" = proto.Field(
        proto.MESSAGE,
        number=10,
        message="MigrationTaskOrchestrationResult",
    )


class MigrationSubtask(proto.Message):
    r"""A subtask for a migration which carries details about the
    configuration of the subtask. The content of the details should
    not matter to the end user, but is a contract between the
    subtask creator and subtask worker.

    Attributes:
        name (str):
            Output only. Immutable. The resource name for the migration
            subtask. The ID is server-generated.

            Example:
            ``projects/123/locations/us/workflows/345/subtasks/678``
        task_id (str):
            The unique ID of the task to which this
            subtask belongs.
        type_ (str):
            The type of the Subtask. The migration
            service does not check whether this is a known
            type. It is up to the task creator (i.e.
            orchestrator or worker) to ensure it only
            creates subtasks for which there are compatible
            workers polling for Subtasks.
        state (google.cloud.bigquery_migration_v2alpha.types.MigrationSubtask.State):
            Output only. The current state of the
            subtask.
        processing_error (google.rpc.error_details_pb2.ErrorInfo):
            Output only. An explanation that may be
            populated when the task is in FAILED state.
        resource_error_details (MutableSequence[google.cloud.bigquery_migration_v2alpha.types.ResourceErrorDetail]):
            Output only. Provides details to errors and
            issues encountered while processing the subtask.
            Presence of error details does not mean that the
            subtask failed.
        resource_error_count (int):
            The number or resources with errors. Note: This is not the
            total number of errors as each resource can have more than
            one error. This is used to indicate truncation by having a
            ``resource_error_count`` that is higher than the size of
            ``resource_error_details``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Time when the subtask was created.
        last_update_time (google.protobuf.timestamp_pb2.Timestamp):
            Time when the subtask was last updated.
        metrics (MutableSequence[google.cloud.bigquery_migration_v2alpha.types.TimeSeries]):
            The metrics for the subtask.
    """

    class State(proto.Enum):
        r"""Possible states of a migration subtask.

        Values:
            STATE_UNSPECIFIED (0):
                The state is unspecified.
            ACTIVE (1):
                The subtask is ready, i.e. it is ready for
                execution.
            RUNNING (2):
                The subtask is running, i.e. it is assigned
                to a worker for execution.
            SUCCEEDED (3):
                The subtask finished successfully.
            FAILED (4):
                The subtask finished unsuccessfully.
            PAUSED (5):
                The subtask is paused, i.e., it will not be
                scheduled. If it was already assigned,it might
                still finish but no new lease renewals will be
                granted.
        """

        STATE_UNSPECIFIED = 0
        ACTIVE = 1
        RUNNING = 2
        SUCCEEDED = 3
        FAILED = 4
        PAUSED = 5

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    task_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    type_: str = proto.Field(
        proto.STRING,
        number=3,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=5,
        enum=State,
    )
    processing_error: error_details_pb2.ErrorInfo = proto.Field(
        proto.MESSAGE,
        number=6,
        message=error_details_pb2.ErrorInfo,
    )
    resource_error_details: MutableSequence[
        migration_error_details.ResourceErrorDetail
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=12,
        message=migration_error_details.ResourceErrorDetail,
    )
    resource_error_count: int = proto.Field(
        proto.INT32,
        number=13,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    last_update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    metrics: MutableSequence[migration_metrics.TimeSeries] = proto.RepeatedField(
        proto.MESSAGE,
        number=11,
        message=migration_metrics.TimeSeries,
    )


class MigrationTaskOrchestrationResult(proto.Message):
    r"""Additional information from the orchestrator when it is done
    with the task orchestration.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        assessment_details (google.cloud.bigquery_migration_v2alpha.types.AssessmentOrchestrationResultDetails):
            Details specific to assessment task types.

            This field is a member of `oneof`_ ``details``.
    """

    assessment_details: assessment_task.AssessmentOrchestrationResultDetails = (
        proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="details",
            message=assessment_task.AssessmentOrchestrationResultDetails,
        )
    )


__all__ = tuple(sorted(__protobuf__.manifest))
