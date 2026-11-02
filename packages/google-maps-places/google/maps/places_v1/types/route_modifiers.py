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
        "RouteModifiers",
    },
)


class RouteModifiers(proto.Message):
    r"""Encapsulates a set of optional conditions to satisfy when
    calculating the routes.

    Attributes:
        avoid_tolls (bool):
            Optional. When set to true, avoids toll roads where
            reasonable, giving preference to routes not containing toll
            roads. Applies only to the ``DRIVE`` and ``TWO_WHEELER``
            [``TravelMode``][google.maps.places.v1.TravelMode].
        avoid_highways (bool):
            Optional. When set to true, avoids highways where
            reasonable, giving preference to routes not containing
            highways. Applies only to the ``DRIVE`` and ``TWO_WHEELER``
            [``TravelMode``][google.maps.places.v1.TravelMode].
        avoid_ferries (bool):
            Optional. When set to true, avoids ferries where reasonable,
            giving preference to routes not containing ferries. Applies
            only to the ``DRIVE`` and ``TWO_WHEELER``
            [``TravelMode``][google.maps.places.v1.TravelMode].
        avoid_indoor (bool):
            Optional. When set to true, avoids navigating indoors where
            reasonable, giving preference to routes not containing
            indoor navigation. Applies only to the ``WALK``
            [``TravelMode``][google.maps.places.v1.TravelMode].
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


__all__ = tuple(sorted(__protobuf__.manifest))
