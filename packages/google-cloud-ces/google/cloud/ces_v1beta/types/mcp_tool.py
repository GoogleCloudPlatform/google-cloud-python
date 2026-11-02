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

import proto  # type: ignore

from google.cloud.ces_v1beta.types import auth, common, schema

__protobuf__ = proto.module(
    package="google.cloud.ces.v1beta",
    manifest={
        "McpTool",
    },
)


class McpTool(proto.Message):
    r"""An MCP tool.
    See
    https://modelcontextprotocol.io/specification/2025-06-18/server/tools
    for more details.

    Attributes:
        name (str):
            Required. The name of the MCP tool.
        name_override (str):
            Optional. The name override of the MCP tool.
            This is populated if the name was overridden by
            a Toolset override.
        description (str):
            Optional. The description of the MCP tool.
        input_schema (google.cloud.ces_v1beta.types.Schema):
            Optional. The schema of the input arguments
            of the MCP tool.
        output_schema (google.cloud.ces_v1beta.types.Schema):
            Optional. The schema of the output arguments
            of the MCP tool.
        server_address (str):
            Required. The server address of the MCP server, e.g.,
            "https://example.com/mcp/". If the server is built with the
            MCP SDK, the url should be suffixed with "/mcp/". Only
            Streamable HTTP transport based servers are supported. This
            is the same as the server_address in the McpToolset. See
            https://modelcontextprotocol.io/specification/2025-03-26/basic/transports#streamable-http
            for more details.
        api_authentication (google.cloud.ces_v1beta.types.ApiAuthentication):
            Optional. Authentication information required
            to execute the tool against the MCP server. For
            bearer token authentication, the token applies
            only to tool execution, not to listing tools.
            This requires that tools can be listed without
            authentication.
        tls_config (google.cloud.ces_v1beta.types.TlsConfig):
            Optional. The TLS configuration. Includes the
            custom server certificates that the client
            should trust.
        service_directory_config (google.cloud.ces_v1beta.types.ServiceDirectoryConfig):
            Optional. Service Directory configuration for
            VPC-SC, used to resolve service names within a
            perimeter.
        custom_headers (MutableMapping[str, str]):
            Optional. The custom headers to send in the request to the
            MCP server. The values must be in the format
            ``$context.variables.<name_of_variable>`` and can be set in
            the session variables. See
            https://docs.cloud.google.com/customer-engagement-ai/conversational-agents/ps/tool/open-api#openapi-injection
            for more details.
        state (google.cloud.ces_v1beta.types.McpTool.State):
            Output only. The dynamic availability state
            of the tool on the external server.
    """

    class State(proto.Enum):
        r"""Represents the dynamic availability state of the tool.

        Values:
            STATE_UNSPECIFIED (0):
                Default state.
            ACTIVE (1):
                The tool is available and actively offered by
                the server.
            INACTIVE (2):
                The tool is configured or pinned, but
                currently not offered by the server.
            STALE (3):
                The tool exists on the server, but does not
                match the version on the server.
        """

        STATE_UNSPECIFIED = 0
        ACTIVE = 1
        INACTIVE = 2
        STALE = 3

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    name_override: str = proto.Field(
        proto.STRING,
        number=13,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
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
    server_address: str = proto.Field(
        proto.STRING,
        number=5,
    )
    api_authentication: auth.ApiAuthentication = proto.Field(
        proto.MESSAGE,
        number=6,
        message=auth.ApiAuthentication,
    )
    tls_config: common.TlsConfig = proto.Field(
        proto.MESSAGE,
        number=7,
        message=common.TlsConfig,
    )
    service_directory_config: common.ServiceDirectoryConfig = proto.Field(
        proto.MESSAGE,
        number=8,
        message=common.ServiceDirectoryConfig,
    )
    custom_headers: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=9,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=12,
        enum=State,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
