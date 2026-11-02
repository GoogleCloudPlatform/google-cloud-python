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

import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.chat.v1",
    manifest={
        "ThreadReadState",
        "GetThreadReadStateRequest",
    },
)


class ThreadReadState(proto.Message):
    r"""A user's read state within a thread, used to identify read
    and unread messages.

    Attributes:
        name (str):
            Resource name of the thread read state.

            Format:
            ``users/{user}/spaces/{space}/threads/{thread}/threadReadState``
        last_read_time (google.protobuf.timestamp_pb2.Timestamp):
            The time when the user's thread read state
            was updated. Usually this corresponds with the
            timestamp of the last read message in a thread.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    last_read_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )


class GetThreadReadStateRequest(proto.Message):
    r"""Request message for GetThreadReadStateRequest API.

    Attributes:
        name (str):
            Required. Resource name of the thread read state to
            retrieve.

            Only supports getting read state for the calling user.

            To refer to the calling user, set one of the following:

            - The ``me`` alias. For example,
              ``users/me/spaces/{space}/threads/{thread}/threadReadState``.

            - Their Workspace email address. For example,
              ``users/user@example.com/spaces/{space}/threads/{thread}/threadReadState``.

            - Their user id. For example,
              ``users/123456789/spaces/{space}/threads/{thread}/threadReadState``.

            Format:
            users/{user}/spaces/{space}/threads/{thread}/threadReadState
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
