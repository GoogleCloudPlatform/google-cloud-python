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

import google.rpc.status_pb2 as status_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.maps.routing.v2",
    manifest={
        "GeocodingResults",
        "GeocodedWaypoint",
    },
)


class GeocodingResults(proto.Message):
    r"""Contains
    [``GeocodedWaypoints``][google.maps.routing.v2.GeocodedWaypoint] for
    origin, destination and intermediate waypoints. Only populated for
    address waypoints.

    Attributes:
        origin (google.maps.routing_v2.types.GeocodedWaypoint):
            Origin geocoded waypoint.
        destination (google.maps.routing_v2.types.GeocodedWaypoint):
            Destination geocoded waypoint.
        intermediates (MutableSequence[google.maps.routing_v2.types.GeocodedWaypoint]):
            A list of intermediate geocoded waypoints
            each containing an index field that corresponds
            to the zero-based position of the waypoint in
            the order they were specified in the request.
    """

    origin: "GeocodedWaypoint" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="GeocodedWaypoint",
    )
    destination: "GeocodedWaypoint" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="GeocodedWaypoint",
    )
    intermediates: MutableSequence["GeocodedWaypoint"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="GeocodedWaypoint",
    )


class GeocodedWaypoint(proto.Message):
    r"""Details about the locations used as waypoints. Only populated
    for address waypoints. Includes details about the geocoding
    results for the purposes of determining what the address was
    geocoded to.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        geocoder_status (google.rpc.status_pb2.Status):
            Indicates the status code resulting from the
            geocoding operation.
        intermediate_waypoint_request_index (int):
            The index of the corresponding intermediate
            waypoint in the request. Only populated if the
            corresponding waypoint is an intermediate
            waypoint.

            This field is a member of `oneof`_ ``_intermediate_waypoint_request_index``.
        type_ (MutableSequence[str]):
            The type(s) of the result, in the form of zero or more type
            tags. Supported types: `Address types and address component
            types <https://developers.google.com/maps/documentation/geocoding/requests-geocoding#Types>`__.
        partial_match (bool):
            Indicates that the geocoder did not return an
            exact match for the original request, though it
            was able to match part of the requested address.
            You may wish to examine the original request for
            misspellings and/or an incomplete address.
        place_id (str):
            The place ID for this result.
    """

    geocoder_status: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=1,
        message=status_pb2.Status,
    )
    intermediate_waypoint_request_index: int = proto.Field(
        proto.INT32,
        number=2,
        optional=True,
    )
    type_: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    partial_match: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    place_id: str = proto.Field(
        proto.STRING,
        number=5,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
