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
    package="google.maps.routing.v2",
    manifest={
        "Maneuver",
    },
)


class Maneuver(proto.Enum):
    r"""A set of values that specify the navigation action to take
    for the current step (for example, turn left, merge, or
    straight).

    Values:
        MANEUVER_UNSPECIFIED (0):
            Not used.
        TURN_SLIGHT_LEFT (1):
            Turn slightly to the left.
        TURN_SHARP_LEFT (2):
            Turn sharply to the left.
        UTURN_LEFT (3):
            Make a left u-turn.
        TURN_LEFT (4):
            Turn left.
        TURN_SLIGHT_RIGHT (5):
            Turn slightly to the right.
        TURN_SHARP_RIGHT (6):
            Turn sharply to the right.
        UTURN_RIGHT (7):
            Make a right u-turn.
        TURN_RIGHT (8):
            Turn right.
        STRAIGHT (9):
            Go straight.
        RAMP_LEFT (10):
            Take the left ramp.
        RAMP_RIGHT (11):
            Take the right ramp.
        MERGE (12):
            Merge into traffic.
        FORK_LEFT (13):
            Take the left fork.
        FORK_RIGHT (14):
            Take the right fork.
        FERRY (15):
            Take the ferry.
        FERRY_TRAIN (16):
            Take the train leading onto the ferry.
        ROUNDABOUT_LEFT (17):
            Turn left at the roundabout.
        ROUNDABOUT_RIGHT (18):
            Turn right at the roundabout.
        DEPART (19):
            Initial maneuver.
        NAME_CHANGE (20):
            Used to indicate a street name change.
    """

    MANEUVER_UNSPECIFIED = 0
    TURN_SLIGHT_LEFT = 1
    TURN_SHARP_LEFT = 2
    UTURN_LEFT = 3
    TURN_LEFT = 4
    TURN_SLIGHT_RIGHT = 5
    TURN_SHARP_RIGHT = 6
    UTURN_RIGHT = 7
    TURN_RIGHT = 8
    STRAIGHT = 9
    RAMP_LEFT = 10
    RAMP_RIGHT = 11
    MERGE = 12
    FORK_LEFT = 13
    FORK_RIGHT = 14
    FERRY = 15
    FERRY_TRAIN = 16
    ROUNDABOUT_LEFT = 17
    ROUNDABOUT_RIGHT = 18
    DEPART = 19
    NAME_CHANGE = 20


__all__ = tuple(sorted(__protobuf__.manifest))
