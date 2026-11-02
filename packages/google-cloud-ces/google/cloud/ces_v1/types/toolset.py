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

from google.cloud.ces_v1.types import common, fakes
from google.cloud.ces_v1.types import connector_toolset as gcc_connector_toolset
from google.cloud.ces_v1.types import mcp_toolset as gcc_mcp_toolset
from google.cloud.ces_v1.types import open_api_toolset as gcc_open_api_toolset

__protobuf__ = proto.module(
    package="google.cloud.ces.v1",
    manifest={
        "Toolset",
    },
)


class Toolset(proto.Message):
    r"""A toolset represents a group of dynamically managed tools
    that can be used by the agent.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        mcp_toolset (google.cloud.ces_v1.types.McpToolset):
            Optional. A toolset that contains a list of
            tools that are offered by the MCP server.

            This field is a member of `oneof`_ ``toolset_type``.
        open_api_toolset (google.cloud.ces_v1.types.OpenApiToolset):
            Optional. A toolset that contains a list of
            tools that are defined by an OpenAPI schema.

            This field is a member of `oneof`_ ``toolset_type``.
        connector_toolset (google.cloud.ces_v1.types.ConnectorToolset):
            Optional. A toolset that generates tools from
            an Integration Connectors Connection.

            This field is a member of `oneof`_ ``toolset_type``.
        name (str):
            Identifier. The unique identifier of the toolset. Format:
            ``projects/{project}/locations/{location}/apps/{app}/toolsets/{toolset}``
        display_name (str):
            Optional. The display name of the toolset.
            Must be unique within the same app.
        description (str):
            Optional. The description of the toolset.
        timeout (google.protobuf.duration_pb2.Duration):
            Optional. The timeout for the toolset execution. If not set,
            the default timeout is 30 seconds for ``SYNCHRONOUS``
            toolsets and 60 seconds for ``ASYNCHRONOUS`` toolsets.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when the toolset was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when the toolset was
            last updated.
        etag (str):
            ETag used to ensure the object hasn't changed
            during a read-modify-write operation. If the
            etag is empty, the update will overwrite any
            concurrent changes.
        execution_type (google.cloud.ces_v1.types.ExecutionType):
            Optional. The execution type of the tools in
            the toolset.
        tool_fake_config (google.cloud.ces_v1.types.ToolFakeConfig):
            Optional. Configuration for tools behavior in
            fake mode.
    """

    mcp_toolset: gcc_mcp_toolset.McpToolset = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="toolset_type",
        message=gcc_mcp_toolset.McpToolset,
    )
    open_api_toolset: gcc_open_api_toolset.OpenApiToolset = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="toolset_type",
        message=gcc_open_api_toolset.OpenApiToolset,
    )
    connector_toolset: gcc_connector_toolset.ConnectorToolset = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="toolset_type",
        message=gcc_connector_toolset.ConnectorToolset,
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
        number=10,
    )
    timeout: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=12,
        message=duration_pb2.Duration,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=5,
    )
    execution_type: common.ExecutionType = proto.Field(
        proto.ENUM,
        number=9,
        enum=common.ExecutionType,
    )
    tool_fake_config: fakes.ToolFakeConfig = proto.Field(
        proto.MESSAGE,
        number=11,
        message=fakes.ToolFakeConfig,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
