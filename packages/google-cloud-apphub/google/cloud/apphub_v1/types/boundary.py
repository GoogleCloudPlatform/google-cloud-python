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
    package="google.cloud.apphub.v1",
    manifest={
        "Boundary",
    },
)


class Boundary(proto.Message):
    r"""Application management boundary.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        crm_node (str):
            Optional. The resource name of the CRM node being attached
            to the boundary. Format: ``projects/{project-number}`` or
            ``projects/{project-id}``

            This field is a member of `oneof`_ ``scope``.
        name (str):
            Identifier. The resource name of the
            boundary. Format:
            "projects/{project}/locations/{location}/boundary".
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Create time.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Update time.
        type_ (google.cloud.apphub_v1.types.Boundary.Type):
            Output only. Boundary type.
    """

    class Type(proto.Enum):
        r"""Boundary management type.

        Values:
            TYPE_UNSPECIFIED (0):
                Unspecified type.
            AUTOMATIC (1):
                The Boundary automatically includes all
                descendants of the CRM node.
            MANUAL (2):
                The list of projects within the Boundary is
                managed by the user.
            MANAGED_AUTOMATIC (3):
                The Boundary automatically includes all
                descendants of the CRM node, which is set via
                App Management folder capability.
        """

        TYPE_UNSPECIFIED = 0
        AUTOMATIC = 1
        MANUAL = 2
        MANAGED_AUTOMATIC = 3

    crm_node: str = proto.Field(
        proto.STRING,
        number=4,
        oneof="scope",
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    type_: Type = proto.Field(
        proto.ENUM,
        number=5,
        enum=Type,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
