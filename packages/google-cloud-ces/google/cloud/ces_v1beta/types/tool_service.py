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

from google.cloud.ces_v1beta.types import schema, search_suggestions, session_service
from google.cloud.ces_v1beta.types import tool as gcc_tool
from google.cloud.ces_v1beta.types import toolset_tool as gcc_toolset_tool

__protobuf__ = proto.module(
    package="google.cloud.ces.v1beta",
    manifest={
        "ExecuteToolRequest",
        "ExecuteToolResponse",
        "RetrieveToolSchemaRequest",
        "RetrieveToolSchemaResponse",
        "RetrieveToolsRequest",
        "RetrieveToolsResponse",
    },
)


class ExecuteToolRequest(proto.Message):
    r"""Request message for
    [ToolService.ExecuteTool][google.cloud.ces.v1beta.ToolService.ExecuteTool].

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        tool (str):
            Optional. The name of the tool to execute.
            Format:

            projects/{project}/locations/{location}/apps/{app}/tools/{tool}

            This field is a member of `oneof`_ ``tool_identifier``.
        toolset_tool (google.cloud.ces_v1beta.types.ToolsetTool):
            Optional. The toolset tool to execute. Only
            one tool should match the predicate from the
            toolset. Otherwise, an error will be returned.

            This field is a member of `oneof`_ ``tool_identifier``.
        variables (google.protobuf.struct_pb2.Struct):
            Optional. The variables that are available
            for the tool execution.

            This field is a member of `oneof`_ ``tool_execution_context``.
        context (google.protobuf.struct_pb2.Struct):
            Optional. The
            [ToolCallContext](https://docs.cloud.google.com/customer-engagement-ai/conversational-agents/ps/tool/python#environment
            for details) to be passed to the Python tool.

            This field is a member of `oneof`_ ``tool_execution_context``.
        parent (str):
            Required. The resource name of the app which the
            tool/toolset belongs to. Format:
            ``projects/{project}/locations/{location}/apps/{app}``
        args (google.protobuf.struct_pb2.Struct):
            Optional. The input parameters and values for
            the tool in JSON object format.
        mock_config (google.cloud.ces_v1beta.types.MockConfig):
            Optional. Mock configuration for the tool
            execution. If this field is set, tools that call
            other tools will be mocked based on the provided
            patterns and responses.
    """

    tool: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="tool_identifier",
    )
    toolset_tool: gcc_toolset_tool.ToolsetTool = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="tool_identifier",
        message=gcc_toolset_tool.ToolsetTool,
    )
    variables: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="tool_execution_context",
        message=struct_pb2.Struct,
    )
    context: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="tool_execution_context",
        message=struct_pb2.Struct,
    )
    parent: str = proto.Field(
        proto.STRING,
        number=4,
    )
    args: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=2,
        message=struct_pb2.Struct,
    )
    mock_config: session_service.MockConfig = proto.Field(
        proto.MESSAGE,
        number=7,
        message=session_service.MockConfig,
    )


class ExecuteToolResponse(proto.Message):
    r"""Response message for
    [ToolService.ExecuteTool][google.cloud.ces.v1beta.ToolService.ExecuteTool].

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        tool (str):
            The name of the tool that got executed. Format:
            ``projects/{project}/locations/{location}/apps/{app}/tools/{tool}``

            This field is a member of `oneof`_ ``tool_identifier``.
        toolset_tool (google.cloud.ces_v1beta.types.ToolsetTool):
            The toolset tool that got executed.

            This field is a member of `oneof`_ ``tool_identifier``.
        response (google.protobuf.struct_pb2.Struct):
            The tool execution result in JSON object
            format. Use "output" key to specify tool
            response and "error" key to specify error
            details (if any). If "output" and "error" keys
            are not specified, then whole "response" is
            treated as tool execution result.
        variables (google.protobuf.struct_pb2.Struct):
            The variable values at the end of the tool
            execution.
        citations (google.cloud.ces_v1beta.types.Citations):
            Citations that provide the source information
            for the tool's execution.
        google_search_suggestions (google.cloud.ces_v1beta.types.GoogleSearchSuggestions):
            The suggestions returned from Google Search
            as a result of invoking the Google Search Tool
            during the tool execution.
    """

    tool: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="tool_identifier",
    )
    toolset_tool: gcc_toolset_tool.ToolsetTool = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="tool_identifier",
        message=gcc_toolset_tool.ToolsetTool,
    )
    response: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=2,
        message=struct_pb2.Struct,
    )
    variables: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=4,
        message=struct_pb2.Struct,
    )
    citations: session_service.Citations = proto.Field(
        proto.MESSAGE,
        number=5,
        message=session_service.Citations,
    )
    google_search_suggestions: search_suggestions.GoogleSearchSuggestions = proto.Field(
        proto.MESSAGE,
        number=6,
        message=search_suggestions.GoogleSearchSuggestions,
    )


class RetrieveToolSchemaRequest(proto.Message):
    r"""Request message for
    [ToolService.RetrieveToolSchema][google.cloud.ces.v1beta.ToolService.RetrieveToolSchema].

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        tool (str):
            Optional. The name of the tool to retrieve
            the schema for. Format:

            projects/{project}/locations/{location}/apps/{app}/tools/{tool}

            This field is a member of `oneof`_ ``tool_identifier``.
        toolset_tool (google.cloud.ces_v1beta.types.ToolsetTool):
            Optional. The toolset tool to retrieve the
            schema for. Only one tool should match the
            predicate from the toolset. Otherwise, an error
            will be returned.

            This field is a member of `oneof`_ ``tool_identifier``.
        parent (str):
            Required. The resource name of the app which the
            tool/toolset belongs to. Format:
            ``projects/{project}/locations/{location}/apps/{app}``
    """

    tool: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="tool_identifier",
    )
    toolset_tool: gcc_toolset_tool.ToolsetTool = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="tool_identifier",
        message=gcc_toolset_tool.ToolsetTool,
    )
    parent: str = proto.Field(
        proto.STRING,
        number=3,
    )


class RetrieveToolSchemaResponse(proto.Message):
    r"""Response message for
    [ToolService.RetrieveToolSchema][google.cloud.ces.v1beta.ToolService.RetrieveToolSchema].

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        tool (str):
            The name of the tool that the schema is for. Format:
            ``projects/{project}/locations/{location}/apps/{app}/tools/{tool}``

            This field is a member of `oneof`_ ``tool_identifier``.
        toolset_tool (google.cloud.ces_v1beta.types.ToolsetTool):
            The toolset tool that the schema is for.

            This field is a member of `oneof`_ ``tool_identifier``.
        input_schema (google.cloud.ces_v1beta.types.Schema):
            The schema of the tool input parameters.
        output_schema (google.cloud.ces_v1beta.types.Schema):
            The schema of the tool output parameters.
    """

    tool: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="tool_identifier",
    )
    toolset_tool: gcc_toolset_tool.ToolsetTool = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="tool_identifier",
        message=gcc_toolset_tool.ToolsetTool,
    )
    input_schema: schema.Schema = proto.Field(
        proto.MESSAGE,
        number=3,
        message=schema.Schema,
    )
    output_schema: schema.Schema = proto.Field(
        proto.MESSAGE,
        number=4,
        message=schema.Schema,
    )


class RetrieveToolsRequest(proto.Message):
    r"""Request message for
    [ToolService.RetrieveTools][google.cloud.ces.v1beta.ToolService.RetrieveTools].

    Attributes:
        toolset (str):
            Required. The name of the toolset to retrieve the tools for.
            Format:
            ``projects/{project}/locations/{location}/apps/{app}/toolsets/{toolset}``
        tool_ids (MutableSequence[str]):
            Optional. The identifiers of the tools to
            retrieve from the toolset. If empty, all tools
            in the toolset will be returned.
        bypass_persistence_config (bool):
            Optional. If true, the returned tools will
            contain raw descriptions and schemas directly
            from the server, bypassing any stored
            persistence configurations
            (overrides/snapshots).
    """

    toolset: str = proto.Field(
        proto.STRING,
        number=1,
    )
    tool_ids: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    bypass_persistence_config: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class RetrieveToolsResponse(proto.Message):
    r"""Response message for
    [ToolService.RetrieveTools][google.cloud.ces.v1beta.ToolService.RetrieveTools].

    Attributes:
        tools (MutableSequence[google.cloud.ces_v1beta.types.Tool]):
            The list of tools that are included in the
            specified toolset.
    """

    tools: MutableSequence[gcc_tool.Tool] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcc_tool.Tool,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
