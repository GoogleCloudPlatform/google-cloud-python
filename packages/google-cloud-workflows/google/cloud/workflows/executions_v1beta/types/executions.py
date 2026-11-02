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

__protobuf__ = proto.module(
    package="google.cloud.workflows.executions.v1beta",
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
            Includes only basic metadata about the execution. Following
            fields are returned: name, start_time, end_time, state and
            workflow_revision_id.
        FULL (2):
            Includes all data.
    """

    EXECUTION_VIEW_UNSPECIFIED = 0
    BASIC = 1
    FULL = 2


class Execution(proto.Message):
    r"""A running instance of a
    [Workflow][google.cloud.workflows.v1beta.Workflow].

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
        state (google.cloud.workflows.executions_v1beta.types.Execution.State):
            Output only. Current state of the execution.
        argument (str):
            Input parameters of the execution represented
            as a JSON string. The size limit is 32KB.
        result (str):
            Output only. Output of the execution represented as a JSON
            string. The value can only be present if the execution's
            state is ``SUCCEEDED``.
        error (google.cloud.workflows.executions_v1beta.types.Execution.Error):
            Output only. The error which caused the execution to finish
            prematurely. The value is only present if the execution's
            state is ``FAILED`` or ``CANCELLED``.
        workflow_revision_id (str):
            Output only. Revision of the workflow this
            execution is using.
    """

    class State(proto.Enum):
        r"""Describes the current state of the execution. More states may
        be added in the future.

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
        """

        STATE_UNSPECIFIED = 0
        ACTIVE = 1
        SUCCEEDED = 2
        FAILED = 3
        CANCELLED = 4

    class Error(proto.Message):
        r"""Error describes why the execution was abnormally terminated.

        Attributes:
            payload (str):
                Error payload returned by the execution,
                represented as a JSON string.
            context (str):
                Human readable error context, helpful for
                debugging purposes.
        """

        payload: str = proto.Field(
            proto.STRING,
            number=1,
        )
        context: str = proto.Field(
            proto.STRING,
            number=2,
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


class ListExecutionsRequest(proto.Message):
    r"""Request for the
    [ListExecutions][google.cloud.workflows.executions.v1beta.Executions.ListExecutions]
    method.

    Attributes:
        parent (str):
            Required. Name of the workflow for which the
            executions should be listed. Format:
            projects/{project}/locations/{location}/workflows/{workflow}
        page_size (int):
            Maximum number of executions to return per
            call. Max supported value depends on the
            selected Execution view: it's 10000 for BASIC
            and 100 for FULL. The default value used if the
            field is not specified is 100, regardless of the
            selected view. Values greater than the max value
            will be coerced down to it.
        page_token (str):
            A page token, received from a previous ``ListExecutions``
            call. Provide this to retrieve the subsequent page.

            When paginating, all other parameters provided to
            ``ListExecutions`` must match the call that provided the
            page token.
        view (google.cloud.workflows.executions_v1beta.types.ExecutionView):
            Optional. A view defining which fields should
            be filled in the returned executions. The API
            will default to the BASIC view.
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


class ListExecutionsResponse(proto.Message):
    r"""Response for the
    [ListExecutions][google.cloud.workflows.executions.v1beta.Executions.ListExecutions]
    method.

    Attributes:
        executions (MutableSequence[google.cloud.workflows.executions_v1beta.types.Execution]):
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
    [CreateExecution][google.cloud.workflows.executions.v1beta.Executions.CreateExecution]
    method.

    Attributes:
        parent (str):
            Required. Name of the workflow for which an
            execution should be created. Format:
            projects/{project}/locations/{location}/workflows/{workflow}
            The latest revision of the workflow will be
            used.
        execution (google.cloud.workflows.executions_v1beta.types.Execution):
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
    [GetExecution][google.cloud.workflows.executions.v1beta.Executions.GetExecution]
    method.

    Attributes:
        name (str):
            Required. Name of the execution to be
            retrieved. Format:

            projects/{project}/locations/{location}/workflows/{workflow}/executions/{execution}
        view (google.cloud.workflows.executions_v1beta.types.ExecutionView):
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
    [CancelExecution][google.cloud.workflows.executions.v1beta.Executions.CancelExecution]
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
