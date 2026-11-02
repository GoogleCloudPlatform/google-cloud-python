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

from google.cloud.support_v2.types import actor

__protobuf__ = proto.module(
    package="google.cloud.support.v2",
    manifest={
        "Comment",
    },
)


class Comment(proto.Message):
    r"""A comment associated with a support case.

    Case comments are the primary way for Google Support to
    communicate with a user who has opened a case. When a user
    responds to Google Support, the user's responses also appear as
    comments.

    Attributes:
        name (str):
            Output only. Identifier. The resource name of
            the comment.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the comment was
            created.
        creator (google.cloud.support_v2.types.Actor):
            Output only. The user or Google Support agent
            who created the comment.
        body (str):
            The full comment body.

            Maximum of 12800 characters.
        plain_text_body (str):
            Output only. DEPRECATED. DO NOT USE.

            A duplicate of the ``body`` field.

            This field is only present for legacy reasons.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    creator: actor.Actor = proto.Field(
        proto.MESSAGE,
        number=3,
        message=actor.Actor,
    )
    body: str = proto.Field(
        proto.STRING,
        number=4,
    )
    plain_text_body: str = proto.Field(
        proto.STRING,
        number=5,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
