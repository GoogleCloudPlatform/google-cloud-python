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
        "TrafficModel",
    },
)


class TrafficModel(proto.Enum):
    r"""This field specifies one of the following assumptions to use when
    calculating travel time in traffic conditions, shown in the enums
    below. Depending on the enum chosen, the ``duration`` field of the
    TrafficModel response will vary. The value contains the predicted
    time to destination in traffic, based on historical averages.
    ``TrafficModel`` is only available for requests that have set
    [``RoutingPreference``][google.maps.routing.v2.RoutingPreference] to
    ``TRAFFIC_AWARE_OPTIMAL`` and
    [``RouteTravelMode``][google.maps.routing.v2.RouteTravelMode] to
    ``DRIVE``.

    Values:
        TRAFFIC_MODEL_UNSPECIFIED (0):
            Unused. If specified, will default to ``BEST_GUESS``.
        BEST_GUESS (1):
            Indicates that the returned ``duration`` should be the best
            estimate of travel time given what is known about both
            historical traffic conditions and live traffic. Live traffic
            becomes more important the closer the ``departure_time`` is
            to now.
        PESSIMISTIC (2):
            Indicates that the returned duration should
            be longer than the actual travel time on most
            days, though occasional days with particularly
            bad traffic conditions may exceed this value.
        OPTIMISTIC (3):
            Indicates that the returned duration should
            be shorter than the actual travel time on most
            days, though occasional days with particularly
            good traffic conditions may be faster than this
            value.
    """

    TRAFFIC_MODEL_UNSPECIFIED = 0
    BEST_GUESS = 1
    PESSIMISTIC = 2
    OPTIMISTIC = 3


__all__ = tuple(sorted(__protobuf__.manifest))
