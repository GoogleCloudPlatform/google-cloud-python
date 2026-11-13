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

import google.protobuf.struct_pb2 as struct_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.dialogflow.v2",
    manifest={
        "ToolCall",
        "ToolCallResult",
    },
)


class ToolCall(proto.Message):
    r"""Represents a call of a specific tool's action with the
    specified inputs.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        tool (str):
            Optional. The [tool][google.cloud.dialogflow.v2.Tool]
            associated with this call. Format:
            ``projects/<ProjectID>/locations/<LocationID>/tools/<ToolID>``.

            This field is a member of `oneof`_ ``source``.
        ces_tool (str):
            Optional. CES tool name for this call. Format:
            ``projects/<ProjectID>/locations/<LocationID>/apps/<AppID>/tools/<ToolID>``.

            This field is a member of `oneof`_ ``source``.
        ces_toolset (str):
            Optional. CES toolset name for this call. Format:
            ``projects/<ProjectID>/locations/<LocationID>/apps/<AppID>/toolsets/ToolsetID>``.

            This field is a member of `oneof`_ ``source``.
        ces_app (str):
            Optional. CES app name for this call. Format:
            ``projects/<ProjectID>/locations/<LocationID>/apps/<AppID>``.

            This field is a member of `oneof`_ ``source``.
        tool_display_name (str):
            Optional. A human readable short name of the
            tool, to be shown on the UI.
        tool_display_details (str):
            Optional. A human readable description of the
            tool.
        action (str):
            Optional. The name of the tool's action
            associated with this call.
        input_parameters (google.protobuf.struct_pb2.Struct):
            Optional. The action's input parameters.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Create time of the tool call.
        answer_record (str):
            Optional. The answer record associated with
            this tool call.
        state (google.cloud.dialogflow_v2.types.ToolCall.State):
            Output only. State of the tool call.
    """

    class State(proto.Enum):
        r"""Tool call states.

        Values:
            STATE_UNSPECIFIED (0):
                Default value.
            TRIGGERED (1):
                The tool call has been triggered.
            NEEDS_CONFIRMATION (2):
                The tool call requires confirmation from a
                human.
        """

        STATE_UNSPECIFIED = 0
        TRIGGERED = 1
        NEEDS_CONFIRMATION = 2

    tool: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="source",
    )
    ces_tool: str = proto.Field(
        proto.STRING,
        number=11,
        oneof="source",
    )
    ces_toolset: str = proto.Field(
        proto.STRING,
        number=12,
        oneof="source",
    )
    ces_app: str = proto.Field(
        proto.STRING,
        number=8,
        oneof="source",
    )
    tool_display_name: str = proto.Field(
        proto.STRING,
        number=9,
    )
    tool_display_details: str = proto.Field(
        proto.STRING,
        number=10,
    )
    action: str = proto.Field(
        proto.STRING,
        number=2,
    )
    input_parameters: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=3,
        message=struct_pb2.Struct,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    answer_record: str = proto.Field(
        proto.STRING,
        number=6,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=7,
        enum=State,
    )


class ToolCallResult(proto.Message):
    r"""The result of calling a tool's action.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        tool (str):
            Optional. The [tool][google.cloud.dialogflow.v2.Tool]
            associated with this call. Format:
            ``projects/<ProjectID>/locations/<LocationID>/tools/<ToolID>``.

            This field is a member of `oneof`_ ``source``.
        ces_toolset (str):
            Optional. CES toolset name for this call. Format:
            ``projects/<ProjectID>/locations/<LocationID>/apps/<AppID>/toolsets/ToolsetID>``.

            This field is a member of `oneof`_ ``source``.
        ces_tool (str):
            Optional. CES tool name for this call. Format:
            ``projects/<ProjectID>/locations/<LocationID>/apps/<AppID>/tools/<ToolID>``.

            This field is a member of `oneof`_ ``source``.
        ces_app (str):
            Optional. CES app name for this call. Format:
            ``projects/<ProjectID>/locations/<LocationID>/apps/<AppID>``.

            This field is a member of `oneof`_ ``source``.
        action (str):
            Optional. The name of the tool's action
            associated with this call.
        error (google.cloud.dialogflow_v2.types.ToolCallResult.Error):
            Optional. The tool call's error.

            This field is a member of `oneof`_ ``result``.
        raw_content (bytes):
            Optional. Only populated if the response
            content is not utf-8 encoded. (by definition
            byte fields are base64 encoded).

            This field is a member of `oneof`_ ``result``.
        content (str):
            Optional. Only populated if the response
            content is utf-8 encoded.

            This field is a member of `oneof`_ ``result``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Create time of the tool call
            result.
        answer_record (str):
            Optional. The answer record associated with
            this tool call result.
    """

    class Error(proto.Message):
        r"""An error produced by the tool call.

        Attributes:
            message (str):
                Optional. The error message of the function.
            retryable (bool):
                Optional. Specifies whether the tool call is
                retryable.
        """

        message: str = proto.Field(
            proto.STRING,
            number=1,
        )
        retryable: bool = proto.Field(
            proto.BOOL,
            number=2,
        )

    tool: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="source",
    )
    ces_toolset: str = proto.Field(
        proto.STRING,
        number=13,
        oneof="source",
    )
    ces_tool: str = proto.Field(
        proto.STRING,
        number=12,
        oneof="source",
    )
    ces_app: str = proto.Field(
        proto.STRING,
        number=11,
        oneof="source",
    )
    action: str = proto.Field(
        proto.STRING,
        number=2,
    )
    error: Error = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="result",
        message=Error,
    )
    raw_content: bytes = proto.Field(
        proto.BYTES,
        number=5,
        oneof="result",
    )
    content: str = proto.Field(
        proto.STRING,
        number=6,
        oneof="result",
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    answer_record: str = proto.Field(
        proto.STRING,
        number=9,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
