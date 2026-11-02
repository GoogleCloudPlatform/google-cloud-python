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
import google.type.localized_text_pb2 as localized_text_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.maps.places.v1",
    manifest={
        "TransitStation",
        "TransitAgency",
        "TransitLine",
        "TransitStop",
        "TransitIcon",
    },
)


class TransitStation(proto.Message):
    r"""Represents transit-specific information for a place.

    Attributes:
        display_name (google.type.localized_text_pb2.LocalizedText):
            The name of the station in the local
            language.
        agencies (MutableSequence[google.maps.places_v1.types.TransitAgency]):
            The transit agencies that serve this station.
        stops (MutableSequence[google.maps.places_v1.types.TransitStop]):
            Transit stops at this station.
    """

    display_name: localized_text_pb2.LocalizedText = proto.Field(
        proto.MESSAGE,
        number=1,
        message=localized_text_pb2.LocalizedText,
    )
    agencies: MutableSequence["TransitAgency"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="TransitAgency",
    )
    stops: MutableSequence["TransitStop"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="TransitStop",
    )


class TransitAgency(proto.Message):
    r"""Represents a transit agency.

    Attributes:
        display_name (google.type.localized_text_pb2.LocalizedText):
            Agency name (e.g. "VTA") in the requested
            language.
        url (str):
            The URL of the agency's homepage.
        fare_url (str):
            The URL of the agency's fare details page.
        icon (google.maps.places_v1.types.TransitIcon):
            Icon identifier for localized branded icon of a transit
            system (e.g. London Underground) which should be used
            instead of TransitLine.vehicle_icon in the UI.
        lines (MutableSequence[google.maps.places_v1.types.TransitLine]):
            The transit lines that are served by this
            agency.
    """

    display_name: localized_text_pb2.LocalizedText = proto.Field(
        proto.MESSAGE,
        number=1,
        message=localized_text_pb2.LocalizedText,
    )
    url: str = proto.Field(
        proto.STRING,
        number=2,
    )
    fare_url: str = proto.Field(
        proto.STRING,
        number=3,
    )
    icon: "TransitIcon" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="TransitIcon",
    )
    lines: MutableSequence["TransitLine"] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message="TransitLine",
    )


class TransitLine(proto.Message):
    r"""Represents a single transit line.

    Attributes:
        id (str):
            The id of the transit line that can be used
            to uniquely identify the line among other
            transit lines in the same transit station. This
            identifier is not guaranteed to be stable across
            different responses.
        vehicle_type (google.maps.places_v1.types.TransitLine.VehicleType):
            The type of vehicle using this line.
        display_name (google.type.localized_text_pb2.LocalizedText):
            The long name for this transit line (e.g.
            "Sunnydale local").
        short_display_name (google.type.localized_text_pb2.LocalizedText):
            The short name for this transit line (e.g.
            "S2").
        text_color (str):
            The text color of labels for this transit
            line in #RRGGBB hex format, e.g. #909CE1.
        background_color (str):
            The background color of the labels for this
            transit line in #RRGGBB hex format, e.g.
            #909CE1. This color can also be used for drawing
            shapes for this transit line.
        url (str):
            The URL of a webpage with details about this
            line.
        icon (google.maps.places_v1.types.TransitIcon):
            Icon identifier for this particular line
            (e.g. subway lines in New York).
        vehicle_icon (google.maps.places_v1.types.TransitIcon):
            Icon identifier for this particular vehicle
            type.
    """

    class VehicleType(proto.Enum):
        r"""The type of vehicle for a transit line.

        Values:
            VEHICLE_TYPE_UNSPECIFIED (0):
                Default value when vehicle type is not
                specified.
            RAIL (1):
                Rail.
            METRO_RAIL (2):
                Metro rail.
            SUBWAY (3):
                Subway.
            TRAM (4):
                Tram.
            MONORAIL (5):
                Monorail.
            HEAVY_RAIL (6):
                Heavy rail.
            COMMUTER_TRAIN (7):
                Commuter train.
            HIGH_SPEED_TRAIN (8):
                High speed train.
            LONG_DISTANCE_TRAIN (9):
                Long distance train.
            BUS (10):
                Bus.
            INTERCITY_BUS (11):
                Intercity bus.
            TROLLEYBUS (12):
                Trolleybus.
            SHARE_TAXI (13):
                Share taxi.
            COACH (14):
                Coach.
            FERRY (15):
                Ferry.
            CABLE_CAR (16):
                Cable car.
            GONDOLA_LIFT (17):
                Gondola lift.
            FUNICULAR (18):
                Funicular.
            SPECIAL (19):
                Special.
            HORSE_CARRIAGE (20):
                Horse carriage.
            AIRPLANE (21):
                Airplane.
        """

        VEHICLE_TYPE_UNSPECIFIED = 0
        RAIL = 1
        METRO_RAIL = 2
        SUBWAY = 3
        TRAM = 4
        MONORAIL = 5
        HEAVY_RAIL = 6
        COMMUTER_TRAIN = 7
        HIGH_SPEED_TRAIN = 8
        LONG_DISTANCE_TRAIN = 9
        BUS = 10
        INTERCITY_BUS = 11
        TROLLEYBUS = 12
        SHARE_TAXI = 13
        COACH = 14
        FERRY = 15
        CABLE_CAR = 16
        GONDOLA_LIFT = 17
        FUNICULAR = 18
        SPECIAL = 19
        HORSE_CARRIAGE = 20
        AIRPLANE = 21

    id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    vehicle_type: VehicleType = proto.Field(
        proto.ENUM,
        number=2,
        enum=VehicleType,
    )
    display_name: localized_text_pb2.LocalizedText = proto.Field(
        proto.MESSAGE,
        number=3,
        message=localized_text_pb2.LocalizedText,
    )
    short_display_name: localized_text_pb2.LocalizedText = proto.Field(
        proto.MESSAGE,
        number=4,
        message=localized_text_pb2.LocalizedText,
    )
    text_color: str = proto.Field(
        proto.STRING,
        number=5,
    )
    background_color: str = proto.Field(
        proto.STRING,
        number=6,
    )
    url: str = proto.Field(
        proto.STRING,
        number=7,
    )
    icon: "TransitIcon" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="TransitIcon",
    )
    vehicle_icon: "TransitIcon" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="TransitIcon",
    )


class TransitStop(proto.Message):
    r"""Represents a transit stop within a station. This is a specific
    location where passengers board and alight transit vehicles, such as
    a platform or bus bay. This is distinct from a ``Departure``, which
    is an event of a vehicle leaving a stop at a specific time.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        id (str):
            The id of the transit stop that can be used
            to uniquely identify the stop among other
            transit stops in the same transit station. This
            identifier is not guaranteed to be stable across
            different responses.
        display_name (google.type.localized_text_pb2.LocalizedText):
            The name of the stop.
        platform_code (google.type.localized_text_pb2.LocalizedText):
            The platform code represented by this stop.
            It can be formatted in any way. (eg: "2",
            "Platform 2", "2-4", or "1x").
        signage_text (google.type.localized_text_pb2.LocalizedText):
            The verbatim text written on the signboard for this
            platform, e.g. "Towards Central" or "East side & Brooklyn".
            When ``platform_code`` is absent, this field is potentially
            the only identifier for the platform; however, both
            ``platform_code`` and ``signage_text`` may be set
            simultaneously.
        stop_code (google.type.localized_text_pb2.LocalizedText):
            Human readable identifier of the stop, used
            by transit agencies to distinguish stops with
            the same name.
        location (google.type.latlng_pb2.LatLng):
            The stop's location.
        wheelchair_accessible_entrance (bool):
            Wheelchair accessibility of this stop. This
            field indicates whether there is an accessible
            path from outside the station to the stop. It
            does not indicate whether it is possible to
            board a vehicle from the stop.

            This field is a member of `oneof`_ ``_wheelchair_accessible_entrance``.
    """

    id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: localized_text_pb2.LocalizedText = proto.Field(
        proto.MESSAGE,
        number=2,
        message=localized_text_pb2.LocalizedText,
    )
    platform_code: localized_text_pb2.LocalizedText = proto.Field(
        proto.MESSAGE,
        number=3,
        message=localized_text_pb2.LocalizedText,
    )
    signage_text: localized_text_pb2.LocalizedText = proto.Field(
        proto.MESSAGE,
        number=4,
        message=localized_text_pb2.LocalizedText,
    )
    stop_code: localized_text_pb2.LocalizedText = proto.Field(
        proto.MESSAGE,
        number=5,
        message=localized_text_pb2.LocalizedText,
    )
    location: latlng_pb2.LatLng = proto.Field(
        proto.MESSAGE,
        number=6,
        message=latlng_pb2.LatLng,
    )
    wheelchair_accessible_entrance: bool = proto.Field(
        proto.BOOL,
        number=7,
        optional=True,
    )


class TransitIcon(proto.Message):
    r"""Icon for a transit line, vehicle, or agency.

    Attributes:
        url (str):
            The URL of the icon.
        name_included (bool):
            Whether the name is contained in the icon and
            there is no need to display it next to the icon.
    """

    url: str = proto.Field(
        proto.STRING,
        number=1,
    )
    name_included: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
