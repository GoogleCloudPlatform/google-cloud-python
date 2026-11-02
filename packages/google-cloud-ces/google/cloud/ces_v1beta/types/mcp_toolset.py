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
        "McpToolset",
        "McpToolOverride",
        "McpToolDefinition",
    },
)


class McpToolset(proto.Message):
    r"""A toolset that contains a list of tools that are offered by
    the MCP server.

    Attributes:
        server_address (str):
            Required. The address of the MCP server, for
            example, "https://example.com/mcp/". If the
            server is built with the MCP SDK, the url should
            be suffixed with
            "/mcp/". Only Streamable HTTP transport based
            servers are supported. See
            https://modelcontextprotocol.io/specification/2025-03-26/basic/transports#streamable-http
            for more details.
        api_authentication (google.cloud.ces_v1beta.types.ApiAuthentication):
            Optional. Authentication information required
            to access tools and execute a tool against the
            MCP server. For bearer token authentication, the
            token applies only to tool execution, not to
            listing tools. This requires that tools can be
            listed without authentication.
        service_directory_config (google.cloud.ces_v1beta.types.ServiceDirectoryConfig):
            Optional. Service Directory configuration for
            VPC-SC, used to resolve service names within a
            perimeter.
        tls_config (google.cloud.ces_v1beta.types.TlsConfig):
            Optional. The TLS configuration. Includes the
            custom server certificates that the client
            should trust.
        custom_headers (MutableMapping[str, str]):
            Optional. The custom headers to send in the request to the
            MCP server. The values must be in the format
            ``$context.variables.<name_of_variable>`` and can be set in
            the session variables. See
            https://docs.cloud.google.com/customer-engagement-ai/conversational-agents/ps/tool/open-api#openapi-injection
            for more details.
        tool_overrides (MutableSequence[google.cloud.ces_v1beta.types.McpToolOverride]):
            Optional. Overrides for individual tools
            within this toolset. This allows overriding
            specific details like descriptions, names, or
            pinning the tools' states so they aren't fully
            dynamic.
    """

    server_address: str = proto.Field(
        proto.STRING,
        number=1,
    )
    api_authentication: auth.ApiAuthentication = proto.Field(
        proto.MESSAGE,
        number=2,
        message=auth.ApiAuthentication,
    )
    service_directory_config: common.ServiceDirectoryConfig = proto.Field(
        proto.MESSAGE,
        number=3,
        message=common.ServiceDirectoryConfig,
    )
    tls_config: common.TlsConfig = proto.Field(
        proto.MESSAGE,
        number=4,
        message=common.TlsConfig,
    )
    custom_headers: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )
    tool_overrides: MutableSequence["McpToolOverride"] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message="McpToolOverride",
    )


class McpToolOverride(proto.Message):
    r"""Overrides associated with a given tool in a Toolset.
    This enables "pinning" or "overriding" of tool definitions from
    the external dynamic server.

    Attributes:
        tool (str):
            Required. The original name of the tool as it
            is emitted by the MCP server.
        name_override (str):
            Optional. If present, this tool uses this
            name in the Agent instead of the original name.
            This is primarily used as an alias if the MCP
            server offers poorly named tools.
        description_override (str):
            Optional. If present, this tool uses this
            description instead of the original description
            from the server.
        snapshot (google.cloud.ces_v1beta.types.McpToolDefinition):
            Output only. If present, this tool is
            "Pinned" and uses the snapshot values as
            fallbacks if the server becomes temporarily
            unavailable or if no Override is present.
    """

    tool: str = proto.Field(
        proto.STRING,
        number=1,
    )
    name_override: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description_override: str = proto.Field(
        proto.STRING,
        number=3,
    )
    snapshot: "McpToolDefinition" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="McpToolDefinition",
    )


class McpToolDefinition(proto.Message):
    r"""Container for a tool's core definition elements that are
    snapshot. Schemas in the snapshot are used as-is and cannot be
    overridden.

    Attributes:
        description (str):
            Output only. The description of the MCP tool. This can be
            overridden by ``description_override`` in
            ``McpToolOverride``.
        input_schema (google.cloud.ces_v1beta.types.Schema):
            Output only. The schema of the input
            arguments of the MCP tool.
        output_schema (google.cloud.ces_v1beta.types.Schema):
            Output only. The schema of the output
            arguments of the MCP tool.
    """

    description: str = proto.Field(
        proto.STRING,
        number=1,
    )
    input_schema: schema.Schema = proto.Field(
        proto.MESSAGE,
        number=2,
        message=schema.Schema,
    )
    output_schema: schema.Schema = proto.Field(
        proto.MESSAGE,
        number=3,
        message=schema.Schema,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
