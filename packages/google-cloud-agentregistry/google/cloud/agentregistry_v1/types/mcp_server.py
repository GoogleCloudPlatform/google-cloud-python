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

from google.cloud.agentregistry_v1.types import properties

__protobuf__ = proto.module(
    package="google.cloud.agentregistry.v1",
    manifest={
        "McpServer",
    },
)


class McpServer(proto.Message):
    r"""Represents an MCP (Model Context Protocol) Server.

    Attributes:
        name (str):
            Identifier. The resource name of the MCP Server. Format:
            ``projects/{project}/locations/{location}/mcpServers/{mcp_server}``.
        mcp_server_id (str):
            Output only. A stable, globally unique
            identifier for MCP Servers.
        display_name (str):
            Output only. The display name of the MCP
            Server.
        description (str):
            Output only. The description of the MCP
            Server.
        interfaces (MutableSequence[google.cloud.agentregistry_v1.types.Interface]):
            Output only. The connection details for the
            MCP Server.
        tools (MutableSequence[google.cloud.agentregistry_v1.types.McpServer.Tool]):
            Output only. Tools provided by the MCP
            Server.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Create time.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Update time.
        attributes (MutableMapping[str, google.protobuf.struct_pb2.Struct]):
            Output only. Attributes of the MCP Server. Valid values:

            - ``agentregistry.googleapis.com/system/RuntimeIdentity``:
              {"principal": "principal://..."} - the runtime identity
              associated with the MCP Server.
            - ``agentregistry.googleapis.com/system/RuntimeReference``:
              {"uri": "//..."}

            - the URI of the underlying resource hosting the MCP Server,
              for example, the GKE Deployment.
    """

    class Tool(proto.Message):
        r"""Represents a single tool provided by an MCP Server.

        Attributes:
            name (str):
                Output only. Human-readable name of the tool.
            description (str):
                Output only. Description of what the tool
                does.
            annotations (google.cloud.agentregistry_v1.types.McpServer.Tool.Annotations):
                Output only. Annotations associated with the
                tool.
        """

        class Annotations(proto.Message):
            r"""Annotations describing the characteristics and behavior of a
            tool or operation.

            Attributes:
                title (str):
                    Output only. A human-readable title for the
                    tool.
                destructive_hint (bool):
                    Output only. If true, the tool may perform destructive
                    updates to its environment. If false, the tool performs only
                    additive updates. NOTE: This property is meaningful only
                    when ``read_only_hint == false`` Default: true
                idempotent_hint (bool):
                    Output only. If true, calling the tool repeatedly with the
                    same arguments will have no additional effect on its
                    environment. NOTE: This property is meaningful only when
                    ``read_only_hint == false`` Default: false
                open_world_hint (bool):
                    Output only. If true, this tool may interact
                    with an "open world" of external entities. If
                    false, the tool's domain of interaction is
                    closed. For example, the world of a web search
                    tool is open, whereas that of a memory tool is
                    not. Default: true
                read_only_hint (bool):
                    Output only. If true, the tool does not
                    modify its environment. Default: false
            """

            title: str = proto.Field(
                proto.STRING,
                number=1,
            )
            destructive_hint: bool = proto.Field(
                proto.BOOL,
                number=2,
            )
            idempotent_hint: bool = proto.Field(
                proto.BOOL,
                number=3,
            )
            open_world_hint: bool = proto.Field(
                proto.BOOL,
                number=4,
            )
            read_only_hint: bool = proto.Field(
                proto.BOOL,
                number=5,
            )

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        description: str = proto.Field(
            proto.STRING,
            number=2,
        )
        annotations: "McpServer.Tool.Annotations" = proto.Field(
            proto.MESSAGE,
            number=3,
            message="McpServer.Tool.Annotations",
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    mcp_server_id: str = proto.Field(
        proto.STRING,
        number=9,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    interfaces: MutableSequence[properties.Interface] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=properties.Interface,
    )
    tools: MutableSequence[Tool] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message=Tool,
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
    attributes: MutableMapping[str, struct_pb2.Struct] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=8,
        message=struct_pb2.Struct,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
