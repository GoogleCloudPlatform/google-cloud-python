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
import google.rpc.error_details_pb2 as error_details_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.bigquery_migration_v2.types import (
    assessment_task,
    migration_error_details,
    migration_metrics,
    translation_config,
    translation_usability,
)
from google.cloud.bigquery_migration_v2.types import (
    translation_details as gcbm_translation_details,
)

__protobuf__ = proto.module(
    package="google.cloud.bigquery.migration.v2",
    manifest={
        "MigrationWorkflow",
        "MigrationTask",
        "MigrationSubtask",
        "MigrationTaskResult",
        "TranslationTaskResult",
        "TaskOutput",
        "LineageOutput",
    },
)


class MigrationWorkflow(proto.Message):
    r"""A migration workflow which specifies what needs to be done
    for an EDW migration.

    Attributes:
        name (str):
            Output only. Immutable. Identifier. The unique identifier
            for the migration workflow. The ID is server-generated.

            Example: ``projects/123/locations/us/workflows/345``
        display_name (str):
            The display name of the workflow. This can be
            set to give a workflow a descriptive name. There
            is no guarantee or enforcement of uniqueness.
        tasks (MutableMapping[str, google.cloud.bigquery_migration_v2.types.MigrationTask]):
            The tasks in a workflow in a named map. The
            name (i.e. key) has no meaning and is merely a
            convenient way to address a specific task in a
            workflow.
        state (google.cloud.bigquery_migration_v2.types.MigrationWorkflow.State):
            Output only. That status of the workflow.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when the workflow was
            created.
        last_update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when the workflow was last
            updated.
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
        assessment_task_details (google.cloud.bigquery_migration_v2.types.AssessmentTaskDetails):
            Task configuration for Assessment.

            This field is a member of `oneof`_ ``task_details``.
        translation_config_details (google.cloud.bigquery_migration_v2.types.TranslationConfigDetails):
            Task configuration for CW Batch/Offline SQL
            Translation.

            This field is a member of `oneof`_ ``task_details``.
        translation_details (google.cloud.bigquery_migration_v2.types.TranslationDetails):
            Task details for unified SQL Translation.

            This field is a member of `oneof`_ ``task_details``.
        id (str):
            Output only. Immutable. The unique identifier
            for the migration task. The ID is
            server-generated.
        type_ (str):
            The type of the task. This must be one of the supported task
            types.

            Assessment:

            - ``Assessment_Hive`` - Assessment for Hive.
            - ``Assessment_Redshift`` - Assessment for Redshift.
            - ``Assessment_Snowflake`` - Assessment for Snowflake.
            - ``Assessment_Teradata_v2`` - Assessment for Teradata.
            - ``Assessment_Oracle`` - Assessment for Oracle.
            - ``Assessment_Hadoop`` - Assessment for Hadoop.
            - ``Assessment_Informatica`` - Assessment for Informatica.

            Translation: See `Supported Task
            Types <https://docs.cloud.google.com/bigquery/docs/api-sql-translator#supported_task_types>`__
            for a list of supported task types.
        state (google.cloud.bigquery_migration_v2.types.MigrationTask.State):
            Output only. The current state of the task.
        processing_error (google.rpc.error_details_pb2.ErrorInfo):
            Output only. An explanation that may be
            populated when the task is in FAILED state.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when the task was created.
        last_update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when the task was last
            updated.
        resource_error_details (MutableSequence[google.cloud.bigquery_migration_v2.types.ResourceErrorDetail]):
            Output only. Provides details to errors and
            issues encountered while processing the task.
            Presence of error details does not mean that the
            task failed.
        resource_error_count (int):
            Output only. The number or resources with errors. Note: This
            is not the total number of errors as each resource can have
            more than one error. This is used to indicate truncation by
            having a ``resource_error_count`` that is higher than the
            size of ``resource_error_details``.
        metrics (MutableSequence[google.cloud.bigquery_migration_v2.types.TimeSeries]):
            Output only. The metrics for the task.
        task_result (google.cloud.bigquery_migration_v2.types.MigrationTaskResult):
            Output only. The result of the task.
        total_processing_error_count (int):
            Output only. Count of all the processing
            errors in this task and its subtasks.
        total_resource_error_count (int):
            Output only. Count of all the resource errors
            in this task and its subtasks.
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
                The task is paused. Assigned subtasks can
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
    translation_config_details: translation_config.TranslationConfigDetails = (
        proto.Field(
            proto.MESSAGE,
            number=14,
            oneof="task_details",
            message=translation_config.TranslationConfigDetails,
        )
    )
    translation_details: gcbm_translation_details.TranslationDetails = proto.Field(
        proto.MESSAGE,
        number=16,
        oneof="task_details",
        message=gcbm_translation_details.TranslationDetails,
    )
    id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    type_: str = proto.Field(
        proto.STRING,
        number=2,
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
    resource_error_details: MutableSequence[
        migration_error_details.ResourceErrorDetail
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=17,
        message=migration_error_details.ResourceErrorDetail,
    )
    resource_error_count: int = proto.Field(
        proto.INT32,
        number=18,
    )
    metrics: MutableSequence[migration_metrics.TimeSeries] = proto.RepeatedField(
        proto.MESSAGE,
        number=19,
        message=migration_metrics.TimeSeries,
    )
    task_result: "MigrationTaskResult" = proto.Field(
        proto.MESSAGE,
        number=20,
        message="MigrationTaskResult",
    )
    total_processing_error_count: int = proto.Field(
        proto.INT32,
        number=21,
    )
    total_resource_error_count: int = proto.Field(
        proto.INT32,
        number=22,
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
        state (google.cloud.bigquery_migration_v2.types.MigrationSubtask.State):
            Output only. The current state of the
            subtask.
        processing_error (google.rpc.error_details_pb2.ErrorInfo):
            Output only. An explanation that may be
            populated when the task is in FAILED state.
        resource_error_details (MutableSequence[google.cloud.bigquery_migration_v2.types.ResourceErrorDetail]):
            Output only. Provides details to errors and
            issues encountered while processing the subtask.
            Presence of error details does not mean that the
            subtask failed.
        resource_error_count (int):
            Output only. The number or resources with errors. Note: This
            is not the total number of errors as each resource can have
            more than one error. This is used to indicate truncation by
            having a ``resource_error_count`` that is higher than the
            size of ``resource_error_details``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when the subtask was
            created.
        last_update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when the subtask was last
            updated.
        metrics (MutableSequence[google.cloud.bigquery_migration_v2.types.TimeSeries]):
            Output only. The metrics for the subtask.
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
            PENDING_DEPENDENCY (6):
                The subtask is pending a dependency. It will
                be scheduled once its dependencies are done.
        """

        STATE_UNSPECIFIED = 0
        ACTIVE = 1
        RUNNING = 2
        SUCCEEDED = 3
        FAILED = 4
        PAUSED = 5
        PENDING_DEPENDENCY = 6

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


class MigrationTaskResult(proto.Message):
    r"""The migration task result.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        translation_task_result (google.cloud.bigquery_migration_v2.types.TranslationTaskResult):
            Details specific to translation task types.

            This field is a member of `oneof`_ ``details``.
        task_outputs (MutableMapping[str, google.cloud.bigquery_migration_v2.types.TaskOutput]):
            The map of task output types to the task
            outputs, e.g. "LINEAGE".
    """

    translation_task_result: "TranslationTaskResult" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="details",
        message="TranslationTaskResult",
    )
    task_outputs: MutableMapping[str, "TaskOutput"] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=3,
        message="TaskOutput",
    )


class TranslationTaskResult(proto.Message):
    r"""Translation specific result details from the migration task.

    Attributes:
        translated_literals (MutableSequence[google.cloud.bigquery_migration_v2.types.Literal]):
            The list of the translated literals.
        report_log_messages (MutableSequence[google.cloud.bigquery_migration_v2.types.GcsReportLogMessage]):
            The records from the aggregate CSV report for
            a migration workflow.
        console_uri (str):
            The Cloud Console URI for the migration
            workflow.
    """

    translated_literals: MutableSequence[gcbm_translation_details.Literal] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=gcbm_translation_details.Literal,
        )
    )
    report_log_messages: MutableSequence[translation_usability.GcsReportLogMessage] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message=translation_usability.GcsReportLogMessage,
        )
    )
    console_uri: str = proto.Field(
        proto.STRING,
        number=3,
    )


class TaskOutput(proto.Message):
    r"""The task output for a task type including the status and any
    errors.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        lineage_output (google.cloud.bigquery_migration_v2.types.LineageOutput):
            The output of the task with output type
            "LINEAGE".

            This field is a member of `oneof`_ ``output``.
        state (google.cloud.bigquery_migration_v2.types.TaskOutput.State):
            Output only. The current state of the task
            output.
        processing_error (google.rpc.error_details_pb2.ErrorInfo):
            An explanation that may be populated when the
            task output is in FAILED state.
    """

    class State(proto.Enum):
        r"""Possible task output states.

        Values:
            STATE_UNSPECIFIED (0):
                Task output state is unspecified.
            PENDING (1):
                Task output is pending.
            SUCCEEDED (2):
                Task output is succeeded.
            FAILED (3):
                Task output is failed. This does not mean
                that there is no useful information in the
                output; partial outputs or failure details may
                be available.
        """

        STATE_UNSPECIFIED = 0
        PENDING = 1
        SUCCEEDED = 2
        FAILED = 3

    lineage_output: "LineageOutput" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="output",
        message="LineageOutput",
    )
    state: State = proto.Field(
        proto.ENUM,
        number=1,
        enum=State,
    )
    processing_error: error_details_pb2.ErrorInfo = proto.Field(
        proto.MESSAGE,
        number=2,
        message=error_details_pb2.ErrorInfo,
    )


class LineageOutput(proto.Message):
    r"""The output of a task with output type "LINEAGE".

    Actual generated lineage can be queried separately (see
    [webapp_uri][google.cloud.bigquery.migration.v2.LineageOutput.webapp_uri]),
    this message contains only metadata: processing status, errors, etc.

    Attributes:
        webapp_uri (str):
            The URI of the webapp that visualizes the lineage. The user
            needs the
            ``bigquerymigration.googleapis.com/lineageDbs.query`` IAM
            permission to use the webapp.
        recognized_inputs (MutableSequence[google.cloud.bigquery_migration_v2.types.LineageOutput.RecognizedInput]):
            Output only. Recognized lineage inputs.

            All inputs are processed only if the task succeeds and all
            work is in state
            `SUCCEEDED <ProgressReport.WorkSummary.State.SUCCEEDED>`__
            (in particular, nothing is
            `SKIPPED <ProgressReport.WorkSummary.State.SKIPPED>`__).

            Even with all inputs processed successfully, there may be
            transpiler errors present leading to inaccurate lineage.
        processing_progress_reports (MutableSequence[google.cloud.bigquery_migration_v2.types.LineageOutput.ProgressReport]):
            Output only. Work processing progress reports
            broken up by processing stage.
    """

    class RecognizedInput(proto.Message):
        r"""Information about lineage input of the given type that
        lineage generation recognized.

        If you expected to process more of the given input, verify your
        input was uploaded and is in the correct format and the request
        to generate lineage correctly specified the input location.

        Attributes:
            type_ (google.cloud.bigquery_migration_v2.types.LineageOutput.RecognizedInput.Type):
                Output only. The type of the input.
            uncompressed_size_bytes (int):
                Output only. The uncompressed size of the
                recognized input of the given type.
        """

        class Type(proto.Enum):
            r"""Input type recognized by the lineage processing.

            Values:
                TYPE_UNSPECIFIED (0):
                    The type is not specified.
                METADATA (1):
                    The input is metadata.
                QUERY_LOG (2):
                    The input is a query log.
                SCRIPT (3):
                    The input is a SQL script.
            """

            TYPE_UNSPECIFIED = 0
            METADATA = 1
            QUERY_LOG = 2
            SCRIPT = 3

        type_: "LineageOutput.RecognizedInput.Type" = proto.Field(
            proto.ENUM,
            number=1,
            enum="LineageOutput.RecognizedInput.Type",
        )
        uncompressed_size_bytes: int = proto.Field(
            proto.INT64,
            number=2,
        )

    class ProgressReport(proto.Message):
        r"""Breaks down processing progress of work.

        Attributes:
            processing_stage (google.cloud.bigquery_migration_v2.types.LineageOutput.ProgressReport.ProcessingStage):
                Output only. The processing stage this
                progress report describes.
            work_summaries (MutableSequence[google.cloud.bigquery_migration_v2.types.LineageOutput.ProgressReport.WorkSummary]):
                Output only. Summaries of work broken up by
                the state of the work. Each work summary
                describes how much work is in the given state.

                To get numbers for the total work covered,
                aggregate the numbers from all summaries.
        """

        class ProcessingStage(proto.Enum):
            r"""The processing stage the progress report describes.

            Values:
                PROCESSING_STAGE_UNSPECIFIED (0):
                    The stage is not specified.
                INPUT_INGESTION (1000):
                    The input ingestion stage.
                POSTPROCESSING (2000):
                    The lineage DB postprocessing stage.
            """

            PROCESSING_STAGE_UNSPECIFIED = 0
            INPUT_INGESTION = 1000
            POSTPROCESSING = 2000

        class WorkSummary(proto.Message):
            r"""Summary of work in the given state.

            Attributes:
                state (google.cloud.bigquery_migration_v2.types.LineageOutput.ProgressReport.WorkSummary.State):
                    Output only. The state of the work this
                    summary describes.
                size (int):
                    Output only. Size of the work in the given
                    State.
                    Size counts "units of work". Units represent
                    arbitrary division of work; there's no
                    expectation each unit takes similar time to
                    process.
                comment (str):
                    Output only. Human-readable comment.
            """

            class State(proto.Enum):
                r"""States of work. Each piece of work is in exactly one state.
                [SUCCEEDED], [FAILED] and [SKIPPED] are terminal states; work in the
                [IN_PROGRESS] will eventually transition to one of the terminal
                states.

                Values:
                    STATE_UNSPECIFIED (0):
                        The state is not specified.
                    SUCCEEDED (1):
                        Work that was processed successfully.
                    FAILED (2):
                        Work that failed processing.
                    IN_PROGRESS (3):
                        Work that is currently being processed or
                        queued for processing.
                    SKIPPED (4):
                        Work that was recognised as necessary to
                        fully process inputs but was skipped due to
                        system limitations.
                """

                STATE_UNSPECIFIED = 0
                SUCCEEDED = 1
                FAILED = 2
                IN_PROGRESS = 3
                SKIPPED = 4

            state: "LineageOutput.ProgressReport.WorkSummary.State" = proto.Field(
                proto.ENUM,
                number=1,
                enum="LineageOutput.ProgressReport.WorkSummary.State",
            )
            size: int = proto.Field(
                proto.INT64,
                number=2,
            )
            comment: str = proto.Field(
                proto.STRING,
                number=3,
            )

        processing_stage: "LineageOutput.ProgressReport.ProcessingStage" = proto.Field(
            proto.ENUM,
            number=1,
            enum="LineageOutput.ProgressReport.ProcessingStage",
        )
        work_summaries: MutableSequence["LineageOutput.ProgressReport.WorkSummary"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=2,
                message="LineageOutput.ProgressReport.WorkSummary",
            )
        )

    webapp_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    recognized_inputs: MutableSequence[RecognizedInput] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=RecognizedInput,
    )
    processing_progress_reports: MutableSequence[ProgressReport] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=ProgressReport,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
