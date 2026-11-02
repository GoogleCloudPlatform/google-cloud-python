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

import google.rpc.code_pb2 as code_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.chat.v1",
    manifest={
        "ActionStatus",
    },
)


class ActionStatus(proto.Message):
    r"""Represents the status for a request to either invoke or submit a
    `dialog <https://developers.google.com/workspace/chat/dialogs>`__.

    Attributes:
        status_code (google.rpc.code_pb2.Code):
            The status code.
        user_facing_message (str):
            The message to send users about the status of their request.
            If unset, a generic message based on the ``status_code`` is
            sent.
    """

    status_code: code_pb2.Code = proto.Field(
        proto.ENUM,
        number=1,
        enum=code_pb2.Code,
    )
    user_facing_message: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
