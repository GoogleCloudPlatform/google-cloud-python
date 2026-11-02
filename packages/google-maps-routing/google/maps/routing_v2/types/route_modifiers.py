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

from google.maps.routing_v2.types import toll_passes as gmr_toll_passes
from google.maps.routing_v2.types import vehicle_info as gmr_vehicle_info

__protobuf__ = proto.module(
    package="google.maps.routing.v2",
    manifest={
        "RouteModifiers",
    },
)


class RouteModifiers(proto.Message):
    r"""Encapsulates a set of optional conditions to satisfy when
    calculating the routes.

    Attributes:
        avoid_tolls (bool):
            When set to true, avoids toll roads where reasonable, giving
            preference to routes not containing toll roads. Applies only
            to the ``DRIVE`` and ``TWO_WHEELER``
            [``RouteTravelMode``][google.maps.routing.v2.RouteTravelMode].
        avoid_highways (bool):
            When set to true, avoids highways where reasonable, giving
            preference to routes not containing highways. Applies only
            to the ``DRIVE`` and ``TWO_WHEELER``
            [``RouteTravelMode``][google.maps.routing.v2.RouteTravelMode].
        avoid_ferries (bool):
            When set to true, avoids ferries where reasonable, giving
            preference to routes not containing ferries. Applies only to
            the ``DRIVE`` and\ ``TWO_WHEELER``
            [``RouteTravelMode``][google.maps.routing.v2.RouteTravelMode].
        avoid_indoor (bool):
            When set to true, avoids navigating indoors where
            reasonable, giving preference to routes not containing
            indoor navigation. Applies only to the ``WALK``
            [``RouteTravelMode``][google.maps.routing.v2.RouteTravelMode].
        vehicle_info (google.maps.routing_v2.types.VehicleInfo):
            Specifies the vehicle information.
        toll_passes (MutableSequence[google.maps.routing_v2.types.TollPass]):
            Encapsulates information about toll passes. If toll passes
            are provided, the API tries to return the pass price. If
            toll passes are not provided, the API treats the toll pass
            as unknown and tries to return the cash price. Applies only
            to the ``DRIVE`` and ``TWO_WHEELER``
            [``RouteTravelMode``][google.maps.routing.v2.RouteTravelMode].
        avoid_tunnels (bool):
            Optional. When set to true, avoids tunnels where reasonable,
            giving preference to routes not containing tunnels. Applies
            only to the ``DRIVE`` and ``TWO_WHEELER``
            [``RouteTravelMode``][google.maps.routing.v2.RouteTravelMode].
            [``RoutingPreference``][google.maps.routing.v2.RoutingPreference]
            must be set to ``TRAFFIC_AWARE_OPTIMAL``. This field is not
            supported in ComputeRouteMatrix.
    """

    avoid_tolls: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    avoid_highways: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    avoid_ferries: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    avoid_indoor: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    vehicle_info: gmr_vehicle_info.VehicleInfo = proto.Field(
        proto.MESSAGE,
        number=5,
        message=gmr_vehicle_info.VehicleInfo,
    )
    toll_passes: MutableSequence[gmr_toll_passes.TollPass] = proto.RepeatedField(
        proto.ENUM,
        number=6,
        enum=gmr_toll_passes.TollPass,
    )
    avoid_tunnels: bool = proto.Field(
        proto.BOOL,
        number=7,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
