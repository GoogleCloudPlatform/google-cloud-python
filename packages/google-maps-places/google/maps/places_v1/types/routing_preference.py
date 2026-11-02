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
    package="google.maps.places.v1",
    manifest={
        "RoutingPreference",
    },
)


class RoutingPreference(proto.Enum):
    r"""A set of values that specify factors to take into
    consideration when calculating the route.

    Values:
        ROUTING_PREFERENCE_UNSPECIFIED (0):
            No routing preference specified. Default to
            ``TRAFFIC_UNAWARE``.
        TRAFFIC_UNAWARE (1):
            Computes routes without taking live traffic conditions into
            consideration. Suitable when traffic conditions don't matter
            or are not applicable. Using this value produces the lowest
            latency. Note: For
            [``TravelMode``][google.maps.places.v1.TravelMode] ``DRIVE``
            and ``TWO_WHEELER``, the route and duration chosen are based
            on road network and average time-independent traffic
            conditions, not current road conditions. Consequently,
            routes may include roads that are temporarily closed.
            Results for a given request may vary over time due to
            changes in the road network, updated average traffic
            conditions, and the distributed nature of the service.
            Results may also vary between nearly-equivalent routes at
            any time or frequency.
        TRAFFIC_AWARE (2):
            Calculates routes taking live traffic conditions into
            consideration. In contrast to ``TRAFFIC_AWARE_OPTIMAL``,
            some optimizations are applied to significantly reduce
            latency.
        TRAFFIC_AWARE_OPTIMAL (3):
            Calculates the routes taking live traffic
            conditions into consideration, without applying
            most performance optimizations. Using this value
            produces the highest latency.
    """

    ROUTING_PREFERENCE_UNSPECIFIED = 0
    TRAFFIC_UNAWARE = 1
    TRAFFIC_AWARE = 2
    TRAFFIC_AWARE_OPTIMAL = 3


__all__ = tuple(sorted(__protobuf__.manifest))
