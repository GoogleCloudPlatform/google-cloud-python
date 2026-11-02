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

__protobuf__ = proto.module(
    package="google.cloud.ces.v1",
    manifest={
        "Changelog",
    },
)


class Changelog(proto.Message):
    r"""Changelogs represent a change made to the app or to an
    resource within the app.

    Attributes:
        name (str):
            Identifier. The unique identifier of the changelog. Format:
            ``projects/{project}/locations/{location}/apps/{app}/changelogs/{changelog}``
        author (str):
            Output only. Email address of the change
            author.
        display_name (str):
            Output only. Display name of the change. It
            typically should be the display name of the
            resource that was changed.
        description (str):
            Output only. Description of the change. which
            typically captures the changed fields in the
            resource.
        resource (str):
            Output only. The resource that was changed.
        resource_type (str):
            Output only. The type of the resource that
            was changed.
        action (str):
            Output only. The action that was performed on
            the resource.
        original_resource (google.protobuf.struct_pb2.Struct):
            Output only. The original resource before the
            change.
        new_resource (google.protobuf.struct_pb2.Struct):
            Output only. The new resource after the
            change.
        dependent_resources (MutableSequence[google.protobuf.struct_pb2.Struct]):
            Output only. The dependent resources that
            were changed.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the change was
            made.
        sequence_number (int):
            Output only. The monotonically increasing
            sequence number of the changelog.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    author: str = proto.Field(
        proto.STRING,
        number=2,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    description: str = proto.Field(
        proto.STRING,
        number=11,
    )
    resource: str = proto.Field(
        proto.STRING,
        number=4,
    )
    resource_type: str = proto.Field(
        proto.STRING,
        number=5,
    )
    action: str = proto.Field(
        proto.STRING,
        number=6,
    )
    original_resource: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=7,
        message=struct_pb2.Struct,
    )
    new_resource: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=8,
        message=struct_pb2.Struct,
    )
    dependent_resources: MutableSequence[struct_pb2.Struct] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message=struct_pb2.Struct,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10,
        message=timestamp_pb2.Timestamp,
    )
    sequence_number: int = proto.Field(
        proto.INT64,
        number=12,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
