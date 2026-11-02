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
    package="google.cloud.securitycenter.v2",
    manifest={
        "GroupMembership",
    },
)


class GroupMembership(proto.Message):
    r"""Contains details about groups of which this finding is a
    member. A group is a collection of findings that are related in
    some way.

    Attributes:
        group_type (google.cloud.securitycenter_v2.types.GroupMembership.GroupType):
            Type of group.
        group_id (str):
            ID of the group.
    """

    class GroupType(proto.Enum):
        r"""Possible types of groups.

        Values:
            GROUP_TYPE_UNSPECIFIED (0):
                Default value.
            GROUP_TYPE_TOXIC_COMBINATION (1):
                Group represents a toxic combination.
            GROUP_TYPE_CHOKEPOINT (3):
                Group represents a chokepoint.
        """

        GROUP_TYPE_UNSPECIFIED = 0
        GROUP_TYPE_TOXIC_COMBINATION = 1
        GROUP_TYPE_CHOKEPOINT = 3

    group_type: GroupType = proto.Field(
        proto.ENUM,
        number=1,
        enum=GroupType,
    )
    group_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
