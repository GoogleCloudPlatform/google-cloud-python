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
    package="google.ads.admanager.v1",
    manifest={
        "TeamStatusEnum",
        "TeamAccessTypeEnum",
    },
)


class TeamStatusEnum(proto.Message):
    r"""Wrapper message for
    [TeamStatus][google.ads.admanager.v1.TeamStatusEnum.TeamStatus]

    """

    class TeamStatus(proto.Enum):
        r"""Represents the status of a team, whether it is active or
        inactive.

        Values:
            TEAM_STATUS_UNSPECIFIED (0):
                Default value. This value is unused.
            ACTIVE (1):
                The status of an active team.
            INACTIVE (2):
                The status of an inactive team.
        """

        TEAM_STATUS_UNSPECIFIED = 0
        ACTIVE = 1
        INACTIVE = 2


class TeamAccessTypeEnum(proto.Message):
    r"""Wrapper message for
    [TeamAccessType][google.ads.admanager.v1.TeamAccessTypeEnum.TeamAccessType]

    """

    class TeamAccessType(proto.Enum):
        r"""Represents the types of team access supported for orders.

        Values:
            TEAM_ACCESS_TYPE_UNSPECIFIED (0):
                Default value. This value is unused.
            NONE (1):
                The level of access in which team members
                can't view or edit a team's orders.
            READ_ONLY (2):
                The level of access in which team members can
                only view a team's orders.
            READ_WRITE (3):
                The level of access in which team members can
                view and edit a team's orders.
        """

        TEAM_ACCESS_TYPE_UNSPECIFIED = 0
        NONE = 1
        READ_ONLY = 2
        READ_WRITE = 3


__all__ = tuple(sorted(__protobuf__.manifest))
