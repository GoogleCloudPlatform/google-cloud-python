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

from google.cloud.support_v2beta.types import actor

__protobuf__ = proto.module(
    package="google.cloud.support.v2beta",
    manifest={
        "Attachment",
    },
)


class Attachment(proto.Message):
    r"""An Attachment contains metadata about a file that was uploaded to a
    case - it is NOT a file itself. That being said, the name of an
    Attachment object can be used to download its accompanying file
    through the ``media.download`` endpoint.

    While attachments can be uploaded in the console at the same time as
    a comment, they're associated on a "case" level, not a "comment"
    level.

    Attributes:
        name (str):
            Output only. Identifier. The resource name of
            the attachment.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which the attachment
            was created.
        creator (google.cloud.support_v2beta.types.Actor):
            Output only. The user who uploaded the
            attachment. Note, the name and email will be
            obfuscated if the attachment was uploaded by
            Google support.
        filename (str):
            The filename of the attachment (e.g. ``"graph.jpg"``).
        mime_type (str):
            Output only. The MIME type of the attachment
            (e.g. text/plain).
        size_bytes (int):
            Output only. The size of the attachment in
            bytes.
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
    filename: str = proto.Field(
        proto.STRING,
        number=4,
    )
    mime_type: str = proto.Field(
        proto.STRING,
        number=5,
    )
    size_bytes: int = proto.Field(
        proto.INT64,
        number=6,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
