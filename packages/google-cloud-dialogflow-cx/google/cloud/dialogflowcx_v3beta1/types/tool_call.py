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

__protobuf__ = proto.module(
    package="google.cloud.dialogflow.cx.v3beta1",
    manifest={
        "ToolCall",
        "ToolCallResult",
    },
)


class ToolCall(proto.Message):
    r"""Represents a call of a specific tool's action with the
    specified inputs.

    Attributes:
        tool (str):
            The [tool][Tool] associated with this call. Format:
            ``projects/<Project ID>/locations/<Location ID>/agents/<Agent ID>/tools/<Tool ID>``.
        action (str):
            The name of the tool's action associated with
            this call.
        input_parameters (google.protobuf.struct_pb2.Struct):
            The action's input parameters.
    """

    tool: str = proto.Field(
        proto.STRING,
        number=1,
    )
    action: str = proto.Field(
        proto.STRING,
        number=2,
    )
    input_parameters: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=3,
        message=struct_pb2.Struct,
    )


class ToolCallResult(proto.Message):
    r"""The result of calling a tool's action that has been executed
    by the client.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        tool (str):
            The [tool][Tool] associated with this call. Format:
            ``projects/<Project ID>/locations/<Location ID>/agents/<Agent ID>/tools/<Tool ID>``.
        action (str):
            The name of the tool's action associated with
            this call.
        error (google.cloud.dialogflowcx_v3beta1.types.ToolCallResult.Error):
            The tool call's error.

            This field is a member of `oneof`_ ``result``.
        output_parameters (google.protobuf.struct_pb2.Struct):
            The tool call's output parameters.

            This field is a member of `oneof`_ ``result``.
    """

    class Error(proto.Message):
        r"""An error produced by the tool call.

        Attributes:
            message (str):
                The error message of the function.
        """

        message: str = proto.Field(
            proto.STRING,
            number=1,
        )

    tool: str = proto.Field(
        proto.STRING,
        number=1,
    )
    action: str = proto.Field(
        proto.STRING,
        number=2,
    )
    error: Error = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="result",
        message=Error,
    )
    output_parameters: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="result",
        message=struct_pb2.Struct,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
