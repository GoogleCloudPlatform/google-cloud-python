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

from google.cloud.ces_v1.types import toolset_tool as gcc_toolset_tool

__protobuf__ = proto.module(
    package="google.cloud.ces.v1",
    manifest={
        "Example",
        "Message",
        "Chunk",
        "Blob",
        "Image",
        "ToolCall",
        "ToolResponse",
        "AgentTransfer",
    },
)


class Example(proto.Message):
    r"""An example represents a sample conversation between the user
    and the agent(s).

    Attributes:
        name (str):
            Identifier. The unique identifier of the example. Format:
            ``projects/{project}/locations/{location}/apps/{app}/examples/{example}``
        display_name (str):
            Required. Display name of the example.
        description (str):
            Optional. Human-readable description of the
            example.
        entry_agent (str):
            Optional. The agent that initially handles the conversation.
            If not specified, the example represents a conversation that
            is handled by the root agent. Format:
            ``projects/{project}/locations/{location}/apps/{app}/agents/{agent}``
        messages (MutableSequence[google.cloud.ces_v1.types.Message]):
            Optional. The collection of messages that
            make up the conversation.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when the example was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when the example was
            last updated.
        invalid (bool):
            Output only. The example may become invalid
            if referencing resources are deleted. Invalid
            examples will not be used as few-shot examples.
        etag (str):
            Etag used to ensure the object hasn't changed
            during a read-modify-write operation. If the
            etag is empty, the update will overwrite any
            concurrent changes.
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
    entry_agent: str = proto.Field(
        proto.STRING,
        number=4,
    )
    messages: MutableSequence["Message"] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message="Message",
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
    invalid: bool = proto.Field(
        proto.BOOL,
        number=8,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=9,
    )


class Message(proto.Message):
    r"""A message within a conversation.

    Attributes:
        role (str):
            Optional. The role within the conversation,
            e.g., user, agent.
        chunks (MutableSequence[google.cloud.ces_v1.types.Chunk]):
            Optional. Content of the message as a series
            of chunks.
        event_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. Timestamp when the message was sent or received.
            Should not be used if the message is part of an
            [example][google.cloud.ces.v1.Example].
    """

    role: str = proto.Field(
        proto.STRING,
        number=1,
    )
    chunks: MutableSequence["Chunk"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="Chunk",
    )
    event_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )


class Chunk(proto.Message):
    r"""A chunk of content within a message.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        text (str):
            Optional. Text data.

            This field is a member of `oneof`_ ``data``.
        transcript (str):
            Optional. Transcript associated with the
            audio.

            This field is a member of `oneof`_ ``data``.
        blob (google.cloud.ces_v1.types.Blob):
            Optional. Blob data.

            This field is a member of `oneof`_ ``data``.
        payload (google.protobuf.struct_pb2.Struct):
            Optional. Custom payload data.

            This field is a member of `oneof`_ ``data``.
        image (google.cloud.ces_v1.types.Image):
            Optional. Image data.

            This field is a member of `oneof`_ ``data``.
        tool_call (google.cloud.ces_v1.types.ToolCall):
            Optional. Tool execution request.

            This field is a member of `oneof`_ ``data``.
        tool_response (google.cloud.ces_v1.types.ToolResponse):
            Optional. Tool execution response.

            This field is a member of `oneof`_ ``data``.
        agent_transfer (google.cloud.ces_v1.types.AgentTransfer):
            Optional. Agent transfer event.

            This field is a member of `oneof`_ ``data``.
        updated_variables (google.protobuf.struct_pb2.Struct):
            A struct represents variables that were
            updated in the conversation, keyed by variable
            names.

            This field is a member of `oneof`_ ``data``.
        default_variables (google.protobuf.struct_pb2.Struct):
            A struct represents default variables at the
            start of the conversation, keyed by variable
            names.

            This field is a member of `oneof`_ ``data``.
    """

    text: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="data",
    )
    transcript: str = proto.Field(
        proto.STRING,
        number=9,
        oneof="data",
    )
    blob: "Blob" = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="data",
        message="Blob",
    )
    payload: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=11,
        oneof="data",
        message=struct_pb2.Struct,
    )
    image: "Image" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="data",
        message="Image",
    )
    tool_call: "ToolCall" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="data",
        message="ToolCall",
    )
    tool_response: "ToolResponse" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="data",
        message="ToolResponse",
    )
    agent_transfer: "AgentTransfer" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="data",
        message="AgentTransfer",
    )
    updated_variables: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="data",
        message=struct_pb2.Struct,
    )
    default_variables: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=10,
        oneof="data",
        message=struct_pb2.Struct,
    )


class Blob(proto.Message):
    r"""Represents a blob input or output in the conversation.

    Attributes:
        mime_type (str):
            Required. The IANA standard MIME type of the
            source data.
        data (bytes):
            Required. Raw bytes of the blob.
    """

    mime_type: str = proto.Field(
        proto.STRING,
        number=1,
    )
    data: bytes = proto.Field(
        proto.BYTES,
        number=2,
    )


class Image(proto.Message):
    r"""Represents an image input or output in the conversation.

    Attributes:
        mime_type (str):
            Required. The IANA standard MIME type of the source data.
            Supported image types includes:

            - image/png
            - image/jpeg
            - image/webp
        data (bytes):
            Required. Raw bytes of the image.
    """

    mime_type: str = proto.Field(
        proto.STRING,
        number=1,
    )
    data: bytes = proto.Field(
        proto.BYTES,
        number=2,
    )


class ToolCall(proto.Message):
    r"""Request for the client or the agent to execute the specified
    tool.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        tool (str):
            Optional. The name of the tool to execute. Format:
            ``projects/{project}/locations/{location}/apps/{app}/tools/{tool}``

            This field is a member of `oneof`_ ``tool_identifier``.
        toolset_tool (google.cloud.ces_v1.types.ToolsetTool):
            Optional. The toolset tool to execute.

            This field is a member of `oneof`_ ``tool_identifier``.
        id (str):
            Optional. The unique identifier of the tool call. If
            populated, the client should return the execution result
            with the matching ID in
            [ToolResponse][google.cloud.ces.v1.ToolResponse.id].
        display_name (str):
            Output only. Display name of the tool.
        args (google.protobuf.struct_pb2.Struct):
            Optional. The input parameters and values for
            the tool in JSON object format.
    """

    tool: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="tool_identifier",
    )
    toolset_tool: gcc_toolset_tool.ToolsetTool = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="tool_identifier",
        message=gcc_toolset_tool.ToolsetTool,
    )
    id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=4,
    )
    args: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=3,
        message=struct_pb2.Struct,
    )


class ToolResponse(proto.Message):
    r"""The execution result of a specific tool from the client or
    the agent.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        tool (str):
            Optional. The name of the tool to execute. Format:
            ``projects/{project}/locations/{location}/apps/{app}/tools/{tool}``

            This field is a member of `oneof`_ ``tool_identifier``.
        toolset_tool (google.cloud.ces_v1.types.ToolsetTool):
            Optional. The toolset tool that got executed.

            This field is a member of `oneof`_ ``tool_identifier``.
        id (str):
            Optional. The matching ID of the [tool
            call][google.cloud.ces.v1.ToolCall] the response is for.
        display_name (str):
            Output only. Display name of the tool.
        response (google.protobuf.struct_pb2.Struct):
            Required. The tool execution result in JSON
            object format. Use "output" key to specify tool
            response and "error" key to specify error
            details (if any). If "output" and "error" keys
            are not specified, then whole "response" is
            treated as tool execution result.
    """

    tool: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="tool_identifier",
    )
    toolset_tool: gcc_toolset_tool.ToolsetTool = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="tool_identifier",
        message=gcc_toolset_tool.ToolsetTool,
    )
    id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=4,
    )
    response: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=3,
        message=struct_pb2.Struct,
    )


class AgentTransfer(proto.Message):
    r"""Represents an event indicating the transfer of a conversation
    to a different agent.

    Attributes:
        target_agent (str):
            Required. The agent to which the conversation is being
            transferred. The agent will handle the conversation from
            this point forward. Format:
            ``projects/{project}/locations/{location}/apps/{app}/agents/{agent}``
        display_name (str):
            Output only. Display name of the agent.
    """

    target_agent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
