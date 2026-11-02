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

__protobuf__ = proto.module(
    package="google.cloud.workflows.executions.v1",
    manifest={
        "ExecutionView",
        "Execution",
        "ListExecutionsRequest",
        "ListExecutionsResponse",
        "CreateExecutionRequest",
        "GetExecutionRequest",
        "CancelExecutionRequest",
    },
)


class ExecutionView(proto.Enum):
    r"""Defines possible views for execution resource.

    Values:
        EXECUTION_VIEW_UNSPECIFIED (0):
            The default / unset value.
        BASIC (1):
            Includes only basic metadata about the execution. The
            following fields are returned: name, start_time, end_time,
            duration, state, and workflow_revision_id.
        FULL (2):
            Includes all data.
    """

    EXECUTION_VIEW_UNSPECIFIED = 0
    BASIC = 1
    FULL = 2


class Execution(proto.Message):
    r"""A running instance of a
    `Workflow </workflows/docs/reference/rest/v1/projects.locations.workflows>`__.

    Attributes:
        name (str):
            Output only. The resource name of the
            execution. Format:

            projects/{project}/locations/{location}/workflows/{workflow}/executions/{execution}
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Marks the beginning of
            execution.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Marks the end of execution,
            successful or not.
        duration (google.protobuf.duration_pb2.Duration):
            Output only. Measures the duration of the
            execution.
        state (google.cloud.workflows.executions_v1.types.Execution.State):
            Output only. Current state of the execution.
        argument (str):
            Input parameters of the execution represented as a JSON
            string. The size limit is 32KB.

            *Note*: If you are using the REST API directly to run your
            workflow, you must escape any JSON string value of
            ``argument``. Example:
            ``'{"argument":"{\"firstName\":\"FIRST\",\"lastName\":\"LAST\"}"}'``
        result (str):
            Output only. Output of the execution represented as a JSON
            string. The value can only be present if the execution's
            state is ``SUCCEEDED``.
        error (google.cloud.workflows.executions_v1.types.Execution.Error):
            Output only. The error which caused the execution to finish
            prematurely. The value is only present if the execution's
            state is ``FAILED`` or ``CANCELLED``.
        workflow_revision_id (str):
            Output only. Revision of the workflow this
            execution is using.
        call_log_level (google.cloud.workflows.executions_v1.types.Execution.CallLogLevel):
            The call logging level associated to this
            execution.
        status (google.cloud.workflows.executions_v1.types.Execution.Status):
            Output only. Status tracks the current steps
            and progress data of this execution.
        labels (MutableMapping[str, str]):
            Labels associated with this execution.
            Labels can contain at most 64 entries. Keys and
            values can be no longer than 63 characters and
            can only contain lowercase letters, numeric
            characters, underscores, and dashes. Label keys
            must start with a letter. International
            characters are allowed.
            By default, labels are inherited from the
            workflow but are overridden by any labels
            associated with the execution.
        state_error (google.cloud.workflows.executions_v1.types.Execution.StateError):
            Output only. Error regarding the state of the
            Execution resource. For example, this field will
            have error details if the execution data is
            unavailable due to revoked KMS key permissions.
    """

    class State(proto.Enum):
        r"""Describes the current state of the execution. More states
        might be added in the future.

        Values:
            STATE_UNSPECIFIED (0):
                Invalid state.
            ACTIVE (1):
                The execution is in progress.
            SUCCEEDED (2):
                The execution finished successfully.
            FAILED (3):
                The execution failed with an error.
            CANCELLED (4):
                The execution was stopped intentionally.
            UNAVAILABLE (5):
                Execution data is unavailable. See the ``state_error``
                field.
            QUEUED (6):
                Request has been placed in the backlog for
                processing at a later time.
        """

        STATE_UNSPECIFIED = 0
        ACTIVE = 1
        SUCCEEDED = 2
        FAILED = 3
        CANCELLED = 4
        UNAVAILABLE = 5
        QUEUED = 6

    class CallLogLevel(proto.Enum):
        r"""Describes the level of platform logging to apply to calls and
        call responses during workflow executions.

        Values:
            CALL_LOG_LEVEL_UNSPECIFIED (0):
                No call logging level specified.
            LOG_ALL_CALLS (1):
                Log all call steps within workflows, all call
                returns, and all exceptions raised.
            LOG_ERRORS_ONLY (2):
                Log only exceptions that are raised from call
                steps within workflows.
            LOG_NONE (3):
                Explicitly log nothing.
        """

        CALL_LOG_LEVEL_UNSPECIFIED = 0
        LOG_ALL_CALLS = 1
        LOG_ERRORS_ONLY = 2
        LOG_NONE = 3

    class StackTraceElement(proto.Message):
        r"""A single stack element (frame) where an error occurred.

        Attributes:
            step (str):
                The step the error occurred at.
            routine (str):
                The routine where the error occurred.
            position (google.cloud.workflows.executions_v1.types.Execution.StackTraceElement.Position):
                The source position information of the stack
                trace element.
        """

        class Position(proto.Message):
            r"""Position contains source position information about the stack
            trace element such as line number, column number and length of
            the code block in bytes.

            Attributes:
                line (int):
                    The source code line number the current
                    instruction was generated from.
                column (int):
                    The source code column position (of the line)
                    the current instruction was generated from.
                length (int):
                    The number of bytes of source code making up
                    this stack trace element.
            """

            line: int = proto.Field(
                proto.INT64,
                number=1,
            )
            column: int = proto.Field(
                proto.INT64,
                number=2,
            )
            length: int = proto.Field(
                proto.INT64,
                number=3,
            )

        step: str = proto.Field(
            proto.STRING,
            number=1,
        )
        routine: str = proto.Field(
            proto.STRING,
            number=2,
        )
        position: "Execution.StackTraceElement.Position" = proto.Field(
            proto.MESSAGE,
            number=3,
            message="Execution.StackTraceElement.Position",
        )

    class StackTrace(proto.Message):
        r"""A collection of stack elements (frames) where an error
        occurred.

        Attributes:
            elements (MutableSequence[google.cloud.workflows.executions_v1.types.Execution.StackTraceElement]):
                An array of stack elements.
        """

        elements: MutableSequence["Execution.StackTraceElement"] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="Execution.StackTraceElement",
        )

    class Error(proto.Message):
        r"""Error describes why the execution was abnormally terminated.

        Attributes:
            payload (str):
                Error message and data returned represented
                as a JSON string.
            context (str):
                Human-readable stack trace string.
            stack_trace (google.cloud.workflows.executions_v1.types.Execution.StackTrace):
                Stack trace with detailed information of
                where error was generated.
        """

        payload: str = proto.Field(
            proto.STRING,
            number=1,
        )
        context: str = proto.Field(
            proto.STRING,
            number=2,
        )
        stack_trace: "Execution.StackTrace" = proto.Field(
            proto.MESSAGE,
            number=3,
            message="Execution.StackTrace",
        )

    class Status(proto.Message):
        r"""Represents the current status of this execution.

        Attributes:
            current_steps (MutableSequence[google.cloud.workflows.executions_v1.types.Execution.Status.Step]):
                A list of currently executing or last executed step names
                for the workflow execution currently running. If the
                workflow has succeeded or failed, this is the last attempted
                or executed step. Presently, if the current step is inside a
                subworkflow, the list only includes that step. In the
                future, the list will contain items for each step in the
                call stack, starting with the outermost step in the ``main``
                subworkflow, and ending with the most deeply nested step.
        """

        class Step(proto.Message):
            r"""Represents a step of the workflow this execution is running.

            Attributes:
                routine (str):
                    Name of a routine within the workflow.
                step (str):
                    Name of a step within the routine.
            """

            routine: str = proto.Field(
                proto.STRING,
                number=1,
            )
            step: str = proto.Field(
                proto.STRING,
                number=2,
            )

        current_steps: MutableSequence["Execution.Status.Step"] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="Execution.Status.Step",
        )

    class StateError(proto.Message):
        r"""Describes an error related to the current state of the
        Execution resource.

        Attributes:
            details (str):
                Provides specifics about the error.
            type_ (google.cloud.workflows.executions_v1.types.Execution.StateError.Type):
                The type of this state error.
        """

        class Type(proto.Enum):
            r"""Describes the possible types of a state error.

            Values:
                TYPE_UNSPECIFIED (0):
                    No type specified.
                KMS_ERROR (1):
                    Caused by an issue with KMS.
            """

            TYPE_UNSPECIFIED = 0
            KMS_ERROR = 1

        details: str = proto.Field(
            proto.STRING,
            number=1,
        )
        type_: "Execution.StateError.Type" = proto.Field(
            proto.ENUM,
            number=2,
            enum="Execution.StateError.Type",
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=12,
        message=duration_pb2.Duration,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=4,
        enum=State,
    )
    argument: str = proto.Field(
        proto.STRING,
        number=5,
    )
    result: str = proto.Field(
        proto.STRING,
        number=6,
    )
    error: Error = proto.Field(
        proto.MESSAGE,
        number=7,
        message=Error,
    )
    workflow_revision_id: str = proto.Field(
        proto.STRING,
        number=8,
    )
    call_log_level: CallLogLevel = proto.Field(
        proto.ENUM,
        number=9,
        enum=CallLogLevel,
    )
    status: Status = proto.Field(
        proto.MESSAGE,
        number=10,
        message=Status,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=11,
    )
    state_error: StateError = proto.Field(
        proto.MESSAGE,
        number=13,
        message=StateError,
    )


class ListExecutionsRequest(proto.Message):
    r"""Request for the [ListExecutions][] method.

    Attributes:
        parent (str):
            Required. Name of the workflow for which the
            executions should be listed. Format:
            projects/{project}/locations/{location}/workflows/{workflow}
        page_size (int):
            Maximum number of executions to return per
            call. Max supported value depends on the
            selected Execution view: it's 1000 for BASIC and
            100 for FULL. The default value used if the
            field is not specified is 100, regardless of the
            selected view. Values greater than the max value
            will be coerced down to it.
        page_token (str):
            A page token, received from a previous ``ListExecutions``
            call. Provide this to retrieve the subsequent page.

            When paginating, all other parameters provided to
            ``ListExecutions`` must match the call that provided the
            page token.

            Note that pagination is applied to dynamic data. The list of
            executions returned can change between page requests.
        view (google.cloud.workflows.executions_v1.types.ExecutionView):
            Optional. A view defining which fields should
            be filled in the returned executions. The API
            will default to the BASIC view.
        filter (str):
            Optional. Filters applied to the [Executions.ListExecutions]
            results. The following fields are supported for filtering:
            executionID, state, startTime, endTime, duration,
            workflowRevisionID, stepName, and label.
        order_by (str):
            Optional. The ordering applied to the
            [Executions.ListExecutions] results. By default the ordering
            is based on descending start time. The following fields are
            supported for order by: executionID, startTime, endTime,
            duration, state, and workflowRevisionID.
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
    view: "ExecutionView" = proto.Field(
        proto.ENUM,
        number=4,
        enum="ExecutionView",
    )
    filter: str = proto.Field(
        proto.STRING,
        number=5,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=6,
    )


class ListExecutionsResponse(proto.Message):
    r"""Response for the
    [ListExecutions][google.cloud.workflows.executions.v1.Executions.ListExecutions]
    method.

    Attributes:
        executions (MutableSequence[google.cloud.workflows.executions_v1.types.Execution]):
            The executions which match the request.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
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


class CreateExecutionRequest(proto.Message):
    r"""Request for the
    [CreateExecution][google.cloud.workflows.executions.v1.Executions.CreateExecution]
    method.

    Attributes:
        parent (str):
            Required. Name of the workflow for which an
            execution should be created. Format:
            projects/{project}/locations/{location}/workflows/{workflow}
            The latest revision of the workflow will be
            used.
        execution (google.cloud.workflows.executions_v1.types.Execution):
            Required. Execution to be created.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    execution: "Execution" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Execution",
    )


class GetExecutionRequest(proto.Message):
    r"""Request for the
    [GetExecution][google.cloud.workflows.executions.v1.Executions.GetExecution]
    method.

    Attributes:
        name (str):
            Required. Name of the execution to be
            retrieved. Format:

            projects/{project}/locations/{location}/workflows/{workflow}/executions/{execution}
        view (google.cloud.workflows.executions_v1.types.ExecutionView):
            Optional. A view defining which fields should
            be filled in the returned execution. The API
            will default to the FULL view.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    view: "ExecutionView" = proto.Field(
        proto.ENUM,
        number=2,
        enum="ExecutionView",
    )


class CancelExecutionRequest(proto.Message):
    r"""Request for the
    [CancelExecution][google.cloud.workflows.executions.v1.Executions.CancelExecution]
    method.

    Attributes:
        name (str):
            Required. Name of the execution to be
            cancelled. Format:

            projects/{project}/locations/{location}/workflows/{workflow}/executions/{execution}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
