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
        "CustomPacingGoalUnitEnum",
    },
)


class CustomPacingGoalUnitEnum(proto.Message):
    r"""Wrapper message for
    [CustomPacingGoalUnit][google.ads.admanager.v1.CustomPacingGoalUnitEnum.CustomPacingGoalUnit]

    """

    class CustomPacingGoalUnit(proto.Enum):
        r"""Options for the unit of the custom pacing goal amounts.

        Values:
            CUSTOM_PACING_GOAL_UNIT_UNSPECIFIED (0):
                Default value. This value is unused.
            ABSOLUTE (1):
                The custom pacing goal amounts represent absolute numbers
                corresponding to the line item's
                [Goal.unitType][google.ads.admanager.v1.Goal.unit_type].
            MILLI_PERCENT (2):
                The custom pacing goal amounts represent a
                millipercent. For example, 15000 millipercent
                equals 15%.
        """

        CUSTOM_PACING_GOAL_UNIT_UNSPECIFIED = 0
        ABSOLUTE = 1
        MILLI_PERCENT = 2


__all__ = tuple(sorted(__protobuf__.manifest))
