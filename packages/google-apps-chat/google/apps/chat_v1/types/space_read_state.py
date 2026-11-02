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

import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.chat.v1",
    manifest={
        "SpaceReadState",
        "GetSpaceReadStateRequest",
        "UpdateSpaceReadStateRequest",
    },
)


class SpaceReadState(proto.Message):
    r"""A user's read state within a space, used to identify read and
    unread messages.

    Attributes:
        name (str):
            Resource name of the space read state.

            Format: ``users/{user}/spaces/{space}/spaceReadState``
        last_read_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. The time when the user's space read
            state was updated. Usually this corresponds with
            either the timestamp of the last read message,
            or a timestamp specified by the user to mark the
            last read position in a space.
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


class GetSpaceReadStateRequest(proto.Message):
    r"""Request message for GetSpaceReadState API.

    Attributes:
        name (str):
            Required. Resource name of the space read state to retrieve.

            Only supports getting read state for the calling user.

            To refer to the calling user, set one of the following:

            - The ``me`` alias. For example,
              ``users/me/spaces/{space}/spaceReadState``.

            - Their Workspace email address. For example,
              ``users/user@example.com/spaces/{space}/spaceReadState``.

            - Their user id. For example,
              ``users/123456789/spaces/{space}/spaceReadState``.

            Format: users/{user}/spaces/{space}/spaceReadState
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateSpaceReadStateRequest(proto.Message):
    r"""Request message for UpdateSpaceReadState API.

    Attributes:
        space_read_state (google.apps.chat_v1.types.SpaceReadState):
            Required. The space read state and fields to update.

            Only supports updating read state for the calling user.

            To refer to the calling user, set one of the following:

            - The ``me`` alias. For example,
              ``users/me/spaces/{space}/spaceReadState``.

            - Their Workspace email address. For example,
              ``users/user@example.com/spaces/{space}/spaceReadState``.

            - Their user id. For example,
              ``users/123456789/spaces/{space}/spaceReadState``.

            Format: users/{user}/spaces/{space}/spaceReadState
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The field paths to update. Currently supported
            field paths:

            - ``last_read_time``

            When the ``last_read_time`` is before the latest message
            create time, the space appears as unread in the UI.

            To mark the space as read, set ``last_read_time`` to any
            value later (larger) than the latest message create time.
            The ``last_read_time`` is coerced to match the latest
            message create time. Note that the space read state only
            affects the read state of messages that are visible in the
            space's top-level conversation. Replies in threads are
            unaffected by this timestamp, and instead rely on the thread
            read state.
    """

    space_read_state: "SpaceReadState" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="SpaceReadState",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
