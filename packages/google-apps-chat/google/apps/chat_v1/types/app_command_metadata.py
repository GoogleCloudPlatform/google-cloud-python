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
    package="google.chat.v1",
    manifest={
        "AppCommandMetadata",
    },
)


class AppCommandMetadata(proto.Message):
    r"""Metadata about a `Chat app
    command <https://developers.google.com/workspace/chat/commands>`__.

    Attributes:
        app_command_id (int):
            The ID for the command specified in the Chat
            API configuration.
        app_command_type (google.apps.chat_v1.types.AppCommandMetadata.AppCommandType):
            The type of Chat app command.
    """

    class AppCommandType(proto.Enum):
        r"""The type of Chat app command. For details, see `Types of Chat app
        commands <https://developers.google.com/workspace/chat/commands#types>`__.

        Values:
            APP_COMMAND_TYPE_UNSPECIFIED (0):
                Default value. Unspecified.
            SLASH_COMMAND (1):
                A slash command. The user sends the command
                in a Chat message.
            QUICK_COMMAND (3):
                A quick command. The user selects the command
                from the Chat menu in the message reply area.
            MESSAGE_ACTION (4):
                A message action. The user selects the
                command from the message context menu in Chat.
        """

        APP_COMMAND_TYPE_UNSPECIFIED = 0
        SLASH_COMMAND = 1
        QUICK_COMMAND = 3
        MESSAGE_ACTION = 4

    app_command_id: int = proto.Field(
        proto.INT32,
        number=1,
    )
    app_command_type: AppCommandType = proto.Field(
        proto.ENUM,
        number=2,
        enum=AppCommandType,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
