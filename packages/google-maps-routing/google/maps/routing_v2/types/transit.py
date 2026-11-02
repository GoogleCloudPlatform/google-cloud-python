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

import google.type.localized_text_pb2 as localized_text_pb2  # type: ignore
import proto  # type: ignore

from google.maps.routing_v2.types import location as gmr_location

__protobuf__ = proto.module(
    package="google.maps.routing.v2",
    manifest={
        "TransitAgency",
        "TransitLine",
        "TransitStop",
        "TransitVehicle",
    },
)


class TransitAgency(proto.Message):
    r"""A transit agency that operates a transit line.

    Attributes:
        name (str):
            The name of this transit agency.
        phone_number (str):
            The transit agency's locale-specific
            formatted phone number.
        uri (str):
            The transit agency's URI.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    phone_number: str = proto.Field(
        proto.STRING,
        number=2,
    )
    uri: str = proto.Field(
        proto.STRING,
        number=3,
    )


class TransitLine(proto.Message):
    r"""Contains information about the transit line used in this
    step.

    Attributes:
        agencies (MutableSequence[google.maps.routing_v2.types.TransitAgency]):
            The transit agency (or agencies) that
            operates this transit line.
        name (str):
            The full name of this transit line, For
            example, "8 Avenue Local".
        uri (str):
            the URI for this transit line as provided by
            the transit agency.
        color (str):
            The color commonly used in signage for this
            line. Represented in hexadecimal.
        icon_uri (str):
            The URI for the icon associated with this
            line.
        name_short (str):
            The short name of this transit line. This
            name will normally be a line number, such as
            "M7" or "355".
        text_color (str):
            The color commonly used in text on signage
            for this line. Represented in hexadecimal.
        vehicle (google.maps.routing_v2.types.TransitVehicle):
            The type of vehicle that operates on this
            transit line.
    """

    agencies: MutableSequence["TransitAgency"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="TransitAgency",
    )
    name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    uri: str = proto.Field(
        proto.STRING,
        number=3,
    )
    color: str = proto.Field(
        proto.STRING,
        number=4,
    )
    icon_uri: str = proto.Field(
        proto.STRING,
        number=5,
    )
    name_short: str = proto.Field(
        proto.STRING,
        number=6,
    )
    text_color: str = proto.Field(
        proto.STRING,
        number=7,
    )
    vehicle: "TransitVehicle" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="TransitVehicle",
    )


class TransitStop(proto.Message):
    r"""Information about a transit stop.

    Attributes:
        name (str):
            The name of the transit stop.
        location (google.maps.routing_v2.types.Location):
            The location of the stop expressed in
            latitude/longitude coordinates.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    location: gmr_location.Location = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gmr_location.Location,
    )


class TransitVehicle(proto.Message):
    r"""Information about a vehicle used in transit routes.

    Attributes:
        name (google.type.localized_text_pb2.LocalizedText):
            The name of this vehicle, capitalized.
        type_ (google.maps.routing_v2.types.TransitVehicle.TransitVehicleType):
            The type of vehicle used.
        icon_uri (str):
            The URI for an icon associated with this
            vehicle type.
        local_icon_uri (str):
            The URI for the icon associated with this
            vehicle type, based on the local transport
            signage.
    """

    class TransitVehicleType(proto.Enum):
        r"""The type of vehicles for transit routes.

        Values:
            TRANSIT_VEHICLE_TYPE_UNSPECIFIED (0):
                Unused.
            BUS (1):
                Bus.
            CABLE_CAR (2):
                A vehicle that operates on a cable, usually on the ground.
                Aerial cable cars may be of the type ``GONDOLA_LIFT``.
            COMMUTER_TRAIN (3):
                Commuter rail.
            FERRY (4):
                Ferry.
            FUNICULAR (5):
                A vehicle that is pulled up a steep incline
                by a cable. A Funicular typically consists of
                two cars, with each car acting as a
                counterweight for the other.
            GONDOLA_LIFT (6):
                An aerial cable car.
            HEAVY_RAIL (7):
                Heavy rail.
            HIGH_SPEED_TRAIN (8):
                High speed train.
            INTERCITY_BUS (9):
                Intercity bus.
            LONG_DISTANCE_TRAIN (10):
                Long distance train.
            METRO_RAIL (11):
                Light rail transit.
            MONORAIL (12):
                Monorail.
            OTHER (13):
                All other vehicles.
            RAIL (14):
                Rail.
            SHARE_TAXI (15):
                Share taxi is a kind of bus with the ability
                to drop off and pick up passengers anywhere on
                its route.
            SUBWAY (16):
                Underground light rail.
            TRAM (17):
                Above ground light rail.
            TROLLEYBUS (18):
                Trolleybus.
        """

        TRANSIT_VEHICLE_TYPE_UNSPECIFIED = 0
        BUS = 1
        CABLE_CAR = 2
        COMMUTER_TRAIN = 3
        FERRY = 4
        FUNICULAR = 5
        GONDOLA_LIFT = 6
        HEAVY_RAIL = 7
        HIGH_SPEED_TRAIN = 8
        INTERCITY_BUS = 9
        LONG_DISTANCE_TRAIN = 10
        METRO_RAIL = 11
        MONORAIL = 12
        OTHER = 13
        RAIL = 14
        SHARE_TAXI = 15
        SUBWAY = 16
        TRAM = 17
        TROLLEYBUS = 18

    name: localized_text_pb2.LocalizedText = proto.Field(
        proto.MESSAGE,
        number=1,
        message=localized_text_pb2.LocalizedText,
    )
    type_: TransitVehicleType = proto.Field(
        proto.ENUM,
        number=2,
        enum=TransitVehicleType,
    )
    icon_uri: str = proto.Field(
        proto.STRING,
        number=3,
    )
    local_icon_uri: str = proto.Field(
        proto.STRING,
        number=4,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
