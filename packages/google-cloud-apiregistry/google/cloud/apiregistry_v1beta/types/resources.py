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

from google.cloud.apiregistry_v1beta.types import common

__protobuf__ = proto.module(
    package="google.cloud.apiregistry.v1beta",
    manifest={
        "McpServer",
        "McpTool",
    },
)


class McpServer(proto.Message):
    r"""Represents an MCP Server. MCP Servers act as endpoints that
    expose a collection of tools that can be invoked by agents.

    Attributes:
        name (str):
            Identifier. The resource name of the MCP Server. Format:
            ``projects/{project}/locations/{location}/mcpServers/{mcp_server}``.
            Example:
            projects/12345/locations/us-central1/mcpServers/google:bigquery.googleapis.com:mcp
            for 1p
            projects/12345/locations/us-central1/mcpServers/apphub:starbucks
            for 2p
        display_name (str):
            Optional. A human readable name for the MCP
            server.
        description (str):
            Optional. A human-readable description of the
            MCP Server's functionality.
        urls (MutableSequence[str]):
            The base URL of the MCP server. Example:
            [geolocation.googleapis.com/mcp].
        capabilities (google.protobuf.struct_pb2.Struct):
            The capabilities that a server may support.
            Known capabilities defined in
            https://modelcontextprotocol.io/specification/2025-06-18/schema#servercapabilities
            and additional capabilities defined by the
            servers.
        state (google.cloud.apiregistry_v1beta.types.State):
            Output only. The state of the MCP Server.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    urls: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    capabilities: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=6,
        message=struct_pb2.Struct,
    )
    state: common.State = proto.Field(
        proto.ENUM,
        number=7,
        enum=common.State,
    )


class McpTool(proto.Message):
    r"""Message describing McpTool object

    Attributes:
        name (str):
            Identifier. The resource name of the McpTool. Format:
            ``projects/{project}/locations/{location}/mcpServers/{mcp_server}/mcpTools/{mcp_tool}``.
            Example:
            projects/12345/locations/us-central1/mcpServers/google:bigquery.googleapis.com:mcp/mcpTools/insert_job
            for 1p
            projects/12345/locations/us-central1/mcpServers/apphub:starbucks/mcpTools/order_pizza
            for 2p
        display_name (str):
            Optional. A human-readable name for the tool,
            suitable for display.
        description (str):
            A human-readable description of the tool's
            functionality.
        mcp_server_urls (MutableSequence[str]):
            Automatically populated reference to MCP
            Server. Helpful when multiple tools are
            requested across different MCP Servers.
        input_schema (google.protobuf.struct_pb2.Struct):
            A JSON Schema object defining the expected
            parameters for invoking the tool.
        output_schema (google.protobuf.struct_pb2.Struct):
            Optional. A JSON Schema object defining the
            expected structure of the tool's output.
        annotations (google.protobuf.struct_pb2.Struct):
            Optional key-value object that allows
            developers to provide additional information
            regarding tool properties, behavior, and usage
            best practices. Annotations or tags to
            facilitate semantic search across tools
            ("semantic tags") are not in the MVP scope. When
            implemented, the first set of supported
            annotations will likely be the standard,
            predefined annotations from the open-source MCP
            spec. These include:

              - title: A human-readable title for the tool,
              useful for UI display.
              - readOnlyHint: If true, indicates the tool
              does not modify its   environment.
              - destructiveHint: If true, the tool may
              perform destructive updates   (only meaningful
              when readOnlyHint is false).
              - idempotentHint: If true, calling the tool
              repeatedly with the same   arguments has no
              additional effect (only meaningful when
              readOnlyHint is   false).
              - openWorldHint: If true, the tool may
              interact with an "open world" of   external
              entities.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    mcp_server_urls: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    input_schema: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=5,
        message=struct_pb2.Struct,
    )
    output_schema: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=6,
        message=struct_pb2.Struct,
    )
    annotations: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=7,
        message=struct_pb2.Struct,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
