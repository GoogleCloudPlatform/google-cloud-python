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

import google.protobuf.duration_pb2 as duration_pb2  # type: ignore
import google.protobuf.struct_pb2 as struct_pb2  # type: ignore
import google.type.latlng_pb2 as latlng_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.maps.isochrones.v1",
    manifest={
        "GenerateIsochroneRequest",
        "GenerateIsochroneResponse",
        "Isochrone",
    },
)


class GenerateIsochroneRequest(proto.Message):
    r"""A request to generate a single isochrone.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        location (google.type.latlng_pb2.LatLng):
            The origin as a latitude/longitude
            coordinate.

            This field is a member of `oneof`_ ``origin``.
        place (str):
            The resource name of a place, in the ``places/{place_id}``
            format.

            This field is a member of `oneof`_ ``origin``.
        travel_duration (google.protobuf.duration_pb2.Duration):
            Required. The travel time for the isochrone
            calculation. The value must be positive and is
            capped at 7200 seconds (120 minutes). For DRIVE
            mode, the maximum allowed duration is 3600
            seconds (60 minutes).
        travel_mode (google.maps.isochrones_v1.types.GenerateIsochroneRequest.TravelMode):
            Required. The mode of transportation.
        travel_direction (google.maps.isochrones_v1.types.GenerateIsochroneRequest.TravelDirection):
            Required. The direction of travel.
        routing_preference (google.maps.isochrones_v1.types.GenerateIsochroneRequest.RoutingPreference):
            Optional. Specifies the preference for how to route.
            Defaults to TRAFFIC_UNAWARE.
        enable_smoothing (bool):
            Optional. Specifies whether to smooth the
            edges of the resulting isochrone polygons.
        polygon_fidelity (google.maps.isochrones_v1.types.GenerateIsochroneRequest.PolygonFidelity):
            Optional. Controls the precision of the generated polygon.
            Defaults to POLYGON_FIDELITY_UNSPECIFIED.
    """

    class TravelMode(proto.Enum):
        r"""Defines the mode of transportation for isochrone calculation.

        Values:
            TRAVEL_MODE_UNSPECIFIED (0):
                No travel mode specified.
            DRIVE (1):
                Travel by passenger car.
            BICYCLE (2):
                Travel by bicycle.
            WALK (3):
                Travel by walking.
        """

        TRAVEL_MODE_UNSPECIFIED = 0
        DRIVE = 1
        BICYCLE = 2
        WALK = 3

    class TravelDirection(proto.Enum):
        r"""Specifies the direction of travel for the isochrone
        calculation.

        Values:
            TRAVEL_DIRECTION_UNSPECIFIED (0):
                No travel direction specified.
            FROM (1):
                Calculates the area reachable *from* the origin point.
                Example: "Where can I deliver to from my warehouse in 30
                minutes?".
            TO (2):
                Calculates the area from which you can travel *to* the
                origin point. Example: "Where can my employees commute from
                to reach the office in 30 minutes?".
        """

        TRAVEL_DIRECTION_UNSPECIFIED = 0
        FROM = 1
        TO = 2

    class RoutingPreference(proto.Enum):
        r"""Determines how traffic conditions are incorporated into the
        calculation.

        Values:
            ROUTING_PREFERENCE_UNSPECIFIED (0):
                No routing preference specified. The server will use its
                default, which is TRAFFIC_UNAWARE.
            TRAFFIC_UNAWARE (1):
                The calculation will not take traffic
                conditions into consideration. The isochrone
                will be based on the road network and static
                travel times. This is suitable for planning
                purposes where traffic is not a factor.
            TRAFFIC_AWARE (2):
                The calculation will factor in live traffic
                conditions.
        """

        ROUTING_PREFERENCE_UNSPECIFIED = 0
        TRAFFIC_UNAWARE = 1
        TRAFFIC_AWARE = 2

    class PolygonFidelity(proto.Enum):
        r"""Controls the level of detail in the isochrone polygon.

        Values:
            POLYGON_FIDELITY_UNSPECIFIED (0):
                No polygon fidelity specified. The server
                will use its default, which is based on the
                travel duration.
            LOW (1):
                Low precision. Good for covering large areas
                with fewer vertices.
            MEDIUM (2):
                Medium precision. A balance between detail
                and artifact size.
            HIGH (3):
                High precision. High fidelity edges, but may
                produce holes in the polygon where the road
                network density is low.
        """

        POLYGON_FIDELITY_UNSPECIFIED = 0
        LOW = 1
        MEDIUM = 2
        HIGH = 3

    location: latlng_pb2.LatLng = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="origin",
        message=latlng_pb2.LatLng,
    )
    place: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="origin",
    )
    travel_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=3,
        message=duration_pb2.Duration,
    )
    travel_mode: TravelMode = proto.Field(
        proto.ENUM,
        number=4,
        enum=TravelMode,
    )
    travel_direction: TravelDirection = proto.Field(
        proto.ENUM,
        number=5,
        enum=TravelDirection,
    )
    routing_preference: RoutingPreference = proto.Field(
        proto.ENUM,
        number=6,
        enum=RoutingPreference,
    )
    enable_smoothing: bool = proto.Field(
        proto.BOOL,
        number=7,
    )
    polygon_fidelity: PolygonFidelity = proto.Field(
        proto.ENUM,
        number=8,
        enum=PolygonFidelity,
    )


class GenerateIsochroneResponse(proto.Message):
    r"""A response containing the generated isochrone data.

    Attributes:
        isochrone (google.maps.isochrones_v1.types.Isochrone):
            Output only. The generated isochrone.
    """

    isochrone: "Isochrone" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Isochrone",
    )


class Isochrone(proto.Message):
    r"""The result of an isochrone calculation, representing an area
    of reachability from an origin point within a specified travel
    time.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        geo_json (google.protobuf.struct_pb2.Struct):
            Output only. The isochrone geometry in
            GeoJSON format, using the RFC 7946 format:
            https://datatracker.ietf.org/doc/html/rfc7946#section-3.1.6.

            This field is a member of `oneof`_ ``geometry``.
    """

    geo_json: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="geometry",
        message=struct_pb2.Struct,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
