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
        "Service",
    },
)


class Service(proto.Message):
    r"""Represents a user-defined Service.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        agent_spec (google.cloud.agentregistry_v1.types.Service.AgentSpec):
            Optional. The spec of the Agent. When ``agent_spec`` is set,
            the type of the service is Agent.

            This field is a member of `oneof`_ ``spec``.
        mcp_server_spec (google.cloud.agentregistry_v1.types.Service.McpServerSpec):
            Optional. The spec of the MCP Server. When
            ``mcp_server_spec`` is set, the type of the service is MCP
            Server.

            This field is a member of `oneof`_ ``spec``.
        endpoint_spec (google.cloud.agentregistry_v1.types.Service.EndpointSpec):
            Optional. The spec of the Endpoint. When ``endpoint_spec``
            is set, the type of the service is Endpoint.

            This field is a member of `oneof`_ ``spec``.
        name (str):
            Identifier. The resource name of the Service. Format:
            ``projects/{project}/locations/{location}/services/{service}``.
        display_name (str):
            Optional. User-defined display name for the Service. Can
            have a maximum length of ``63`` characters.
        description (str):
            Optional. User-defined description of an Service. Can have a
            maximum length of ``2048`` characters.
        interfaces (MutableSequence[google.cloud.agentregistry_v1.types.Interface]):
            Optional. The connection details for the
            Service.
        registry_resource (str):
            Output only. The resource name of the resulting Agent, MCP
            Server, or Endpoint. Format:

            - ``projects/{project}/locations/{location}/mcpServers/{mcp_server}``
            - ``projects/{project}/locations/{location}/agents/{agent}``
            - ``projects/{project}/locations/{location}/endpoints/{endpoint}``
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Create time.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Update time.
    """

    class AgentSpec(proto.Message):
        r"""The spec of the agent.

        Attributes:
            type_ (google.cloud.agentregistry_v1.types.Service.AgentSpec.Type):
                Required. The type of the agent spec content.
            content (google.protobuf.struct_pb2.Struct):
                Optional. The content of the Agent spec in the JSON format.
                This payload is validated against the schema for the
                specified type. The content size is limited to ``10KB``.
        """

        class Type(proto.Enum):
            r"""The type of the agent spec.

            Values:
                TYPE_UNSPECIFIED (0):
                    Unspecified type.
                NO_SPEC (1):
                    There is no spec for the Agent. The ``content`` field must
                    be empty.
                A2A_AGENT_CARD (2):
                    The content is an A2A Agent Card following the A2A
                    specification. The ``interfaces`` field must be empty.
            """

            TYPE_UNSPECIFIED = 0
            NO_SPEC = 1
            A2A_AGENT_CARD = 2

        type_: "Service.AgentSpec.Type" = proto.Field(
            proto.ENUM,
            number=1,
            enum="Service.AgentSpec.Type",
        )
        content: struct_pb2.Struct = proto.Field(
            proto.MESSAGE,
            number=2,
            message=struct_pb2.Struct,
        )

    class McpServerSpec(proto.Message):
        r"""The spec of the MCP Server.

        Attributes:
            type_ (google.cloud.agentregistry_v1.types.Service.McpServerSpec.Type):
                Required. The type of the MCP Server spec
                content.
            content (google.protobuf.struct_pb2.Struct):
                Optional. The content of the MCP Server spec. This payload
                is validated against the schema for the specified type. The
                content size is limited to ``10KB``.
        """

        class Type(proto.Enum):
            r"""The type of the MCP Server spec.

            Values:
                TYPE_UNSPECIFIED (0):
                    Unspecified type.
                NO_SPEC (1):
                    There is no spec for the MCP Server. The ``content`` field
                    must be empty.
                TOOL_SPEC (2):
                    The content is a MCP Tool Spec following the One MCP
                    specification. The payload is the same as the ``tools/list``
                    response.
            """

            TYPE_UNSPECIFIED = 0
            NO_SPEC = 1
            TOOL_SPEC = 2

        type_: "Service.McpServerSpec.Type" = proto.Field(
            proto.ENUM,
            number=1,
            enum="Service.McpServerSpec.Type",
        )
        content: struct_pb2.Struct = proto.Field(
            proto.MESSAGE,
            number=2,
            message=struct_pb2.Struct,
        )

    class EndpointSpec(proto.Message):
        r"""The spec of the endpoint.

        Attributes:
            type_ (google.cloud.agentregistry_v1.types.Service.EndpointSpec.Type):
                Required. The type of the endpoint spec
                content.
            content (google.protobuf.struct_pb2.Struct):
                Optional. The content of the endpoint spec.
                Reserved for future use.
        """

        class Type(proto.Enum):
            r"""The type of the endpoint spec.

            Values:
                TYPE_UNSPECIFIED (0):
                    Unspecified type.
                NO_SPEC (1):
                    There is no spec for the Endpoint. The ``content`` field
                    must be empty.
            """

            TYPE_UNSPECIFIED = 0
            NO_SPEC = 1

        type_: "Service.EndpointSpec.Type" = proto.Field(
            proto.ENUM,
            number=1,
            enum="Service.EndpointSpec.Type",
        )
        content: struct_pb2.Struct = proto.Field(
            proto.MESSAGE,
            number=2,
            message=struct_pb2.Struct,
        )

    agent_spec: AgentSpec = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="spec",
        message=AgentSpec,
    )
    mcp_server_spec: McpServerSpec = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="spec",
        message=McpServerSpec,
    )
    endpoint_spec: EndpointSpec = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="spec",
        message=EndpointSpec,
    )
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
    interfaces: MutableSequence[properties.Interface] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=properties.Interface,
    )
    registry_resource: str = proto.Field(
        proto.STRING,
        number=10,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
