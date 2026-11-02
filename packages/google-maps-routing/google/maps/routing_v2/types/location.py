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

import google.protobuf.wrappers_pb2 as wrappers_pb2  # type: ignore
import google.type.latlng_pb2 as latlng_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.maps.routing.v2",
    manifest={
        "Location",
    },
)


class Location(proto.Message):
    r"""Encapsulates a location (a geographic point, and an optional
    heading).

    Attributes:
        lat_lng (google.type.latlng_pb2.LatLng):
            The waypoint's geographic coordinates.
        heading (google.protobuf.wrappers_pb2.Int32Value):
            The compass heading associated with the direction of the
            flow of traffic. This value specifies the side of the road
            for pickup and drop-off. Heading values can be from 0 to
            360, where 0 specifies a heading of due North, 90 specifies
            a heading of due East, and so on. You can use this field
            only for ``DRIVE`` and ``TWO_WHEELER``
            [``RouteTravelMode``][google.maps.routing.v2.RouteTravelMode].
    """

    lat_lng: latlng_pb2.LatLng = proto.Field(
        proto.MESSAGE,
        number=1,
        message=latlng_pb2.LatLng,
    )
    heading: wrappers_pb2.Int32Value = proto.Field(
        proto.MESSAGE,
        number=2,
        message=wrappers_pb2.Int32Value,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
