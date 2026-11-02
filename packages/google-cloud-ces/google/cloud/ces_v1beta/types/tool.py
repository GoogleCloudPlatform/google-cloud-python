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

from google.cloud.ces_v1beta.types import agent_card, common, fakes
from google.cloud.ces_v1beta.types import agent_tool as gcc_agent_tool
from google.cloud.ces_v1beta.types import client_function as gcc_client_function
from google.cloud.ces_v1beta.types import connector_tool as gcc_connector_tool
from google.cloud.ces_v1beta.types import data_store_tool as gcc_data_store_tool
from google.cloud.ces_v1beta.types import file_search_tool as gcc_file_search_tool
from google.cloud.ces_v1beta.types import google_search_tool as gcc_google_search_tool
from google.cloud.ces_v1beta.types import mcp_tool as gcc_mcp_tool
from google.cloud.ces_v1beta.types import open_api_tool as gcc_open_api_tool
from google.cloud.ces_v1beta.types import python_function as gcc_python_function
from google.cloud.ces_v1beta.types import system_tool as gcc_system_tool
from google.cloud.ces_v1beta.types import widget_tool as gcc_widget_tool

__protobuf__ = proto.module(
    package="google.cloud.ces.v1beta",
    manifest={
        "Tool",
    },
)


class Tool(proto.Message):
    r"""A tool represents an action that the CES agent can take to
    achieve certain goals.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        client_function (google.cloud.ces_v1beta.types.ClientFunction):
            Optional. The client function.

            This field is a member of `oneof`_ ``tool_type``.
        open_api_tool (google.cloud.ces_v1beta.types.OpenApiTool):
            Optional. The open API tool.

            This field is a member of `oneof`_ ``tool_type``.
        google_search_tool (google.cloud.ces_v1beta.types.GoogleSearchTool):
            Optional. The google search tool.

            This field is a member of `oneof`_ ``tool_type``.
        connector_tool (google.cloud.ces_v1beta.types.ConnectorTool):
            Optional. The Integration Connector tool.

            This field is a member of `oneof`_ ``tool_type``.
        data_store_tool (google.cloud.ces_v1beta.types.DataStoreTool):
            Optional. The data store tool.

            This field is a member of `oneof`_ ``tool_type``.
        python_function (google.cloud.ces_v1beta.types.PythonFunction):
            Optional. The python function tool.

            This field is a member of `oneof`_ ``tool_type``.
        mcp_tool (google.cloud.ces_v1beta.types.McpTool):
            Optional. The MCP tool. An MCP tool cannot be
            created or updated directly and is managed by
            the MCP toolset.

            This field is a member of `oneof`_ ``tool_type``.
        file_search_tool (google.cloud.ces_v1beta.types.FileSearchTool):
            Optional. The file search tool.

            This field is a member of `oneof`_ ``tool_type``.
        system_tool (google.cloud.ces_v1beta.types.SystemTool):
            Optional. The system tool.

            This field is a member of `oneof`_ ``tool_type``.
        agent_tool (google.cloud.ces_v1beta.types.AgentTool):
            Optional. The agent tool.

            This field is a member of `oneof`_ ``tool_type``.
        widget_tool (google.cloud.ces_v1beta.types.WidgetTool):
            Optional. The widget tool.

            This field is a member of `oneof`_ ``tool_type``.
        remote_agent_tool (google.cloud.ces_v1beta.types.RemoteAgentTool):
            Optional. The remote agent tool.

            This field is a member of `oneof`_ ``tool_type``.
        name (str):
            Identifier. The resource name of the tool. Format:

            - ``projects/{project}/locations/{location}/apps/{app}/tools/{tool}``
              for standalone tools.
            - ``projects/{project}/locations/{location}/apps/{app}/toolsets/{toolset}/tools/{tool}``
              for tools retrieved from a toolset.

            These tools are dynamic and output-only; they cannot be
            referenced directly where a tool is expected.
        display_name (str):
            Output only. The display name of the tool, derived based on
            the tool's type. For example, display name of a
            [ClientFunction][Tool.ClientFunction] is derived from its
            ``name`` property.
        execution_type (google.cloud.ces_v1beta.types.ExecutionType):
            Optional. The execution type of the tool.
        timeout (google.protobuf.duration_pb2.Duration):
            Optional. The timeout for the tool execution. If not set,
            the default timeout is 30 seconds for ``SYNCHRONOUS`` tools
            and 60 seconds for ``ASYNCHRONOUS`` tools.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when the tool was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when the tool was last
            updated.
        etag (str):
            Etag used to ensure the object hasn't changed
            during a read-modify-write operation. If the
            etag is empty, the update will overwrite any
            concurrent changes.
        generated_summary (str):
            Output only. If the tool is generated by the
            LLM assistant, this field contains a descriptive
            summary of the generation.
        tool_fake_config (google.cloud.ces_v1beta.types.ToolFakeConfig):
            Optional. Configuration for tool behavior in
            fake mode.
    """

    client_function: gcc_client_function.ClientFunction = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="tool_type",
        message=gcc_client_function.ClientFunction,
    )
    open_api_tool: gcc_open_api_tool.OpenApiTool = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="tool_type",
        message=gcc_open_api_tool.OpenApiTool,
    )
    google_search_tool: gcc_google_search_tool.GoogleSearchTool = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="tool_type",
        message=gcc_google_search_tool.GoogleSearchTool,
    )
    connector_tool: gcc_connector_tool.ConnectorTool = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="tool_type",
        message=gcc_connector_tool.ConnectorTool,
    )
    data_store_tool: gcc_data_store_tool.DataStoreTool = proto.Field(
        proto.MESSAGE,
        number=10,
        oneof="tool_type",
        message=gcc_data_store_tool.DataStoreTool,
    )
    python_function: gcc_python_function.PythonFunction = proto.Field(
        proto.MESSAGE,
        number=11,
        oneof="tool_type",
        message=gcc_python_function.PythonFunction,
    )
    mcp_tool: gcc_mcp_tool.McpTool = proto.Field(
        proto.MESSAGE,
        number=16,
        oneof="tool_type",
        message=gcc_mcp_tool.McpTool,
    )
    file_search_tool: gcc_file_search_tool.FileSearchTool = proto.Field(
        proto.MESSAGE,
        number=17,
        oneof="tool_type",
        message=gcc_file_search_tool.FileSearchTool,
    )
    system_tool: gcc_system_tool.SystemTool = proto.Field(
        proto.MESSAGE,
        number=18,
        oneof="tool_type",
        message=gcc_system_tool.SystemTool,
    )
    agent_tool: gcc_agent_tool.AgentTool = proto.Field(
        proto.MESSAGE,
        number=23,
        oneof="tool_type",
        message=gcc_agent_tool.AgentTool,
    )
    widget_tool: gcc_widget_tool.WidgetTool = proto.Field(
        proto.MESSAGE,
        number=24,
        oneof="tool_type",
        message=gcc_widget_tool.WidgetTool,
    )
    remote_agent_tool: agent_card.RemoteAgentTool = proto.Field(
        proto.MESSAGE,
        number=25,
        oneof="tool_type",
        message=agent_card.RemoteAgentTool,
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=13,
    )
    execution_type: common.ExecutionType = proto.Field(
        proto.ENUM,
        number=12,
        enum=common.ExecutionType,
    )
    timeout: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=22,
        message=duration_pb2.Duration,
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
    etag: str = proto.Field(
        proto.STRING,
        number=14,
    )
    generated_summary: str = proto.Field(
        proto.STRING,
        number=15,
    )
    tool_fake_config: fakes.ToolFakeConfig = proto.Field(
        proto.MESSAGE,
        number=20,
        message=fakes.ToolFakeConfig,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
