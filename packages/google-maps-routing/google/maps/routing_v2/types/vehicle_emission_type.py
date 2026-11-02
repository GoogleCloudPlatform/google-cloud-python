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
        "VehicleEmissionType",
    },
)


class VehicleEmissionType(proto.Enum):
    r"""A set of values describing the vehicle's emission type. Applies only
    to the ``DRIVE``
    [``RouteTravelMode``][google.maps.routing.v2.RouteTravelMode].

    Values:
        VEHICLE_EMISSION_TYPE_UNSPECIFIED (0):
            No emission type specified. Default to ``GASOLINE``.
        GASOLINE (1):
            Gasoline/petrol fueled vehicle.
        ELECTRIC (2):
            Electricity powered vehicle.
        HYBRID (3):
            Hybrid fuel (such as gasoline + electric)
            vehicle.
        DIESEL (4):
            Diesel fueled vehicle.
    """

    VEHICLE_EMISSION_TYPE_UNSPECIFIED = 0
    GASOLINE = 1
    ELECTRIC = 2
    HYBRID = 3
    DIESEL = 4


__all__ = tuple(sorted(__protobuf__.manifest))
