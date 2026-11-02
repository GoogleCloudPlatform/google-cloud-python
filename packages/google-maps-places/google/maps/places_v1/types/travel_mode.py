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
        "TravelMode",
    },
)


class TravelMode(proto.Enum):
    r"""Travel mode options. These options map to what `Routes API
    offers <https://developers.google.com/maps/documentation/routes/reference/rest/v2/RouteTravelMode>`__.

    Values:
        TRAVEL_MODE_UNSPECIFIED (0):
            No travel mode specified. Defaults to ``DRIVE``.
        DRIVE (1):
            Travel by passenger car.
        BICYCLE (2):
            Travel by bicycle. Not supported with
            ``search_along_route_parameters``.
        WALK (3):
            Travel by walking. Not supported with
            ``search_along_route_parameters``.
        TWO_WHEELER (4):
            Motorized two wheeled vehicles of all kinds such as scooters
            and motorcycles. Note that this is distinct from the
            ``BICYCLE`` travel mode which covers human-powered
            transport. Not supported with
            ``search_along_route_parameters``. Only supported in those
            countries listed at `Countries and regions supported for
            two-wheeled
            vehicles <https://developers.google.com/maps/documentation/routes/coverage-two-wheeled>`__.
    """

    TRAVEL_MODE_UNSPECIFIED = 0
    DRIVE = 1
    BICYCLE = 2
    WALK = 3
    TWO_WHEELER = 4


__all__ = tuple(sorted(__protobuf__.manifest))
