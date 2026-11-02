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

from google.cloud.apiregistry_v1beta.types import resources

__protobuf__ = proto.module(
    package="google.cloud.apiregistry.v1beta",
    manifest={
        "GetMcpServerRequest",
        "ListMcpServersRequest",
        "ListMcpServersResponse",
        "GetMcpToolRequest",
        "ListMcpToolsRequest",
        "ListMcpToolsResponse",
    },
)


class GetMcpServerRequest(proto.Message):
    r"""Message for getting a McpServer

    Attributes:
        name (str):
            Required. Name of the resource
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListMcpServersRequest(proto.Message):
    r"""Message for requesting list of McpServers

    Attributes:
        parent (str):
            Required. Parent value for
            ListMcpServersRequest
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
        filter (str):
            Optional. Filtering results
        order_by (str):
            Optional. Hint for how to order the results
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
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListMcpServersResponse(proto.Message):
    r"""Message for response to listing McpServers

    Attributes:
        mcp_servers (MutableSequence[google.cloud.apiregistry_v1beta.types.McpServer]):
            The list of McpServer
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    mcp_servers: MutableSequence[resources.McpServer] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.McpServer,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetMcpToolRequest(proto.Message):
    r"""Message for getting a McpTool

    Attributes:
        name (str):
            Required. Name of the resource
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListMcpToolsRequest(proto.Message):
    r"""Message for requesting list of McpTools

    Attributes:
        parent (str):
            Required. Parent value for
            ListMcpToolsRequest
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
        filter (str):
            Optional. Filtering results
        order_by (str):
            Optional. Hint for how to order the results
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
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListMcpToolsResponse(proto.Message):
    r"""Message for response to listing McpTools

    Attributes:
        mcp_tools (MutableSequence[google.cloud.apiregistry_v1beta.types.McpTool]):
            The list of McpTool
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    mcp_tools: MutableSequence[resources.McpTool] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.McpTool,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
