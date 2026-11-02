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
        "TransitPreferences",
    },
)


class TransitPreferences(proto.Message):
    r"""Preferences for ``TRANSIT`` based routes that influence the route
    that is returned.

    Attributes:
        allowed_travel_modes (MutableSequence[google.maps.routing_v2.types.TransitPreferences.TransitTravelMode]):
            A set of travel modes to use when getting a ``TRANSIT``
            route. Defaults to all supported modes of travel.
        routing_preference (google.maps.routing_v2.types.TransitPreferences.TransitRoutingPreference):
            A routing preference that, when specified, influences the
            ``TRANSIT`` route returned.
    """

    class TransitTravelMode(proto.Enum):
        r"""A set of values used to specify the mode of transit.

        Values:
            TRANSIT_TRAVEL_MODE_UNSPECIFIED (0):
                No transit travel mode specified.
            BUS (1):
                Travel by bus.
            SUBWAY (2):
                Travel by subway.
            TRAIN (3):
                Travel by train.
            LIGHT_RAIL (4):
                Travel by light rail or tram.
            RAIL (5):
                Travel by rail. This is equivalent to a combination of
                ``SUBWAY``, ``TRAIN``, and ``LIGHT_RAIL``.
        """

        TRANSIT_TRAVEL_MODE_UNSPECIFIED = 0
        BUS = 1
        SUBWAY = 2
        TRAIN = 3
        LIGHT_RAIL = 4
        RAIL = 5

    class TransitRoutingPreference(proto.Enum):
        r"""Specifies routing preferences for transit routes.

        Values:
            TRANSIT_ROUTING_PREFERENCE_UNSPECIFIED (0):
                No preference specified.
            LESS_WALKING (1):
                Indicates that the calculated route should
                prefer limited amounts of walking.
            FEWER_TRANSFERS (2):
                Indicates that the calculated route should
                prefer a limited number of transfers.
        """

        TRANSIT_ROUTING_PREFERENCE_UNSPECIFIED = 0
        LESS_WALKING = 1
        FEWER_TRANSFERS = 2

    allowed_travel_modes: MutableSequence[TransitTravelMode] = proto.RepeatedField(
        proto.ENUM,
        number=1,
        enum=TransitTravelMode,
    )
    routing_preference: TransitRoutingPreference = proto.Field(
        proto.ENUM,
        number=2,
        enum=TransitRoutingPreference,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
