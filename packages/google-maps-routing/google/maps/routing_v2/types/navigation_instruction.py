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

from google.maps.routing_v2.types import maneuver as gmr_maneuver

__protobuf__ = proto.module(
    package="google.maps.routing.v2",
    manifest={
        "NavigationInstruction",
    },
)


class NavigationInstruction(proto.Message):
    r"""Encapsulates navigation instructions for a
    [``RouteLegStep``][google.maps.routing.v2.RouteLegStep].

    Attributes:
        maneuver (google.maps.routing_v2.types.Maneuver):
            Encapsulates the navigation instructions for
            the current step (for example, turn left, merge,
            or straight). This field determines which icon
            to display.
        instructions (str):
            Instructions for navigating this step.
    """

    maneuver: gmr_maneuver.Maneuver = proto.Field(
        proto.ENUM,
        number=1,
        enum=gmr_maneuver.Maneuver,
    )
    instructions: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
