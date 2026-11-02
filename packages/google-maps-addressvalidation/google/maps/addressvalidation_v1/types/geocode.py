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

import google.type.latlng_pb2 as latlng_pb2  # type: ignore
import proto  # type: ignore
from google.geo.type.types import viewport

__protobuf__ = proto.module(
    package="google.maps.addressvalidation.v1",
    manifest={
        "Geocode",
        "PlusCode",
    },
)


class Geocode(proto.Message):
    r"""Contains information about the place the input was geocoded
    to.

    Attributes:
        location (google.type.latlng_pb2.LatLng):
            The geocoded location of the input.

            Using place IDs is preferred over using
            addresses, latitude/longitude coordinates, or
            plus codes. Using coordinates when routing or
            calculating driving directions will always
            result in the point being snapped to the road
            nearest to those coordinates. This may not be a
            road that will quickly or safely lead to the
            destination and may not be near an access point
            to the property. Additionally, when a location
            is reverse geocoded, there is no guarantee that
            the returned address will match the original.
        plus_code (google.maps.addressvalidation_v1.types.PlusCode):
            The plus code corresponding to the ``location``.
        bounds (google.geo.type.types.Viewport):
            The bounds of the geocoded place.
        feature_size_meters (float):
            The size of the geocoded place, in meters.
            This is another measure of the coarseness of the
            geocoded location, but in physical size rather
            than in semantic meaning.
        place_id (str):
            The PlaceID of the place this input geocodes to.

            For more information about Place IDs see
            `here <https://developers.google.com/maps/documentation/places/web-service/place-id>`__.
        place_types (MutableSequence[str]):
            The type(s) of place that the input geocoded to. For
            example, ``['locality', 'political']``. The full list of
            types can be found
            `here <https://developers.google.com/maps/documentation/geocoding/requests-geocoding#Types>`__.
    """

    location: latlng_pb2.LatLng = proto.Field(
        proto.MESSAGE,
        number=1,
        message=latlng_pb2.LatLng,
    )
    plus_code: "PlusCode" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="PlusCode",
    )
    bounds: viewport.Viewport = proto.Field(
        proto.MESSAGE,
        number=4,
        message=viewport.Viewport,
    )
    feature_size_meters: float = proto.Field(
        proto.FLOAT,
        number=5,
    )
    place_id: str = proto.Field(
        proto.STRING,
        number=6,
    )
    place_types: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=7,
    )


class PlusCode(proto.Message):
    r"""Plus code (http://plus.codes) is a location reference with
    two formats: global code defining a 14mx14m (1/8000th of a
    degree) or smaller rectangle, and compound code, replacing the
    prefix with a reference location.

    Attributes:
        global_code (str):
            Place's global (full) code, such as
            "9FWM33GV+HQ", representing an 1/8000 by 1/8000
            degree area (~14 by 14 meters).
        compound_code (str):
            Place's compound code, such as "33GV+HQ,
            Ramberg, Norway", containing the suffix of the
            global code and replacing the prefix with a
            formatted name of a reference entity.
    """

    global_code: str = proto.Field(
        proto.STRING,
        number=1,
    )
    compound_code: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
