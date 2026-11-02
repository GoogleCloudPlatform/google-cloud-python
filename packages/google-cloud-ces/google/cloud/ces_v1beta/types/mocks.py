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
import proto  # type: ignore

from google.cloud.ces_v1beta.types import toolset_tool

__protobuf__ = proto.module(
    package="google.cloud.ces.v1beta",
    manifest={
        "MockedToolCall",
    },
)


class MockedToolCall(proto.Message):
    r"""A mocked tool call.

    Expresses the target tool + a pattern to match against that
    tool's args / inputs. If the pattern matches, then the mock
    response will be returned.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        tool_id (str):
            Optional. The name of the tool to mock. Format:
            ``projects/{project}/locations/{location}/apps/{app}/tools/{tool}``

            This field is a member of `oneof`_ ``tool_identifier``.
        toolset (google.cloud.ces_v1beta.types.ToolsetTool):
            Optional. The toolset to mock.

            This field is a member of `oneof`_ ``tool_identifier``.
        tool (str):
            Optional. Deprecated. Use tool_identifier instead.
        expected_args_pattern (google.protobuf.struct_pb2.Struct):
            Required. A pattern to match against the args
            / inputs of all dispatched tool calls. If the
            tool call inputs match this pattern, then mock
            output will be returned.
        mock_response (google.protobuf.struct_pb2.Struct):
            Optional. The mock response / output to
            return if the tool call args / inputs match the
            pattern.
    """

    tool_id: str = proto.Field(
        proto.STRING,
        number=4,
        oneof="tool_identifier",
    )
    toolset: toolset_tool.ToolsetTool = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="tool_identifier",
        message=toolset_tool.ToolsetTool,
    )
    tool: str = proto.Field(
        proto.STRING,
        number=1,
    )
    expected_args_pattern: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=2,
        message=struct_pb2.Struct,
    )
    mock_response: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=3,
        message=struct_pb2.Struct,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
