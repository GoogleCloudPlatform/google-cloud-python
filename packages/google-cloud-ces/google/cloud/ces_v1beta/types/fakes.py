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

__protobuf__ = proto.module(
    package="google.cloud.ces.v1beta",
    manifest={
        "EvaluationToolCallBehaviour",
        "CodeBlock",
        "ToolFakeConfig",
    },
)


class EvaluationToolCallBehaviour(proto.Enum):
    r"""Configures the tool call behaviour for evaluation runs.

    Values:
        EVALUATION_TOOL_CALL_BEHAVIOUR_UNSPECIFIED (0):
            Unspecified tool call behavior. Will default
            to real tool calls.
        REAL (1):
            Use real tool calls.
        FAKE (2):
            Use fake tool calls.
    """

    EVALUATION_TOOL_CALL_BEHAVIOUR_UNSPECIFIED = 0
    REAL = 1
    FAKE = 2


class CodeBlock(proto.Message):
    r"""A code block to be executed instead of a real tool call.

    Attributes:
        python_code (str):
            Required. Python code which will be invoked in tool fake
            mode. Expected Python function signature - To catch all tool
            calls: def fake_tool_call(tool: Tool, input: dict[str, Any],
            callback_context: CallbackContext) -> Optional[dict[str,
            Any]]: To catch a specific tool call: def
            fake\_{tool_id}(tool: Tool, input: dict[str, Any],
            callback_context: CallbackContext) -> Optional[dict[str,
            Any]]: If the function returns None, the real tool will be
            invoked instead.
    """

    python_code: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ToolFakeConfig(proto.Message):
    r"""Configuration for tool behavior in fake mode.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        code_block (google.cloud.ces_v1beta.types.CodeBlock):
            Optional. Code block which will be executed
            instead of a real tool call.

            This field is a member of `oneof`_ ``tool_response``.
        enable_fake_mode (bool):
            Optional. Whether the tool is using fake
            mode.
    """

    code_block: "CodeBlock" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="tool_response",
        message="CodeBlock",
    )
    enable_fake_mode: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
