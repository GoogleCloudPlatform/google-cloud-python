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

import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.type.money_pb2 as money_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.maps.places.v1",
    manifest={
        "FuelOptions",
    },
)


class FuelOptions(proto.Message):
    r"""The most recent information about fuel options in a gas
    station. This information is updated regularly.

    Attributes:
        fuel_prices (MutableSequence[google.maps.places_v1.types.FuelOptions.FuelPrice]):
            The last known fuel price for each type of
            fuel this station has. There is one entry per
            fuel type this station has. Order is not
            important.
    """

    class FuelPrice(proto.Message):
        r"""Fuel price information for a given type.

        Attributes:
            type_ (google.maps.places_v1.types.FuelOptions.FuelPrice.FuelType):
                The type of fuel.
            price (google.type.money_pb2.Money):
                The price of the fuel.
            update_time (google.protobuf.timestamp_pb2.Timestamp):
                The time the fuel price was last updated.
        """

        class FuelType(proto.Enum):
            r"""Types of fuel.

            Values:
                FUEL_TYPE_UNSPECIFIED (0):
                    Unspecified fuel type.
                DIESEL (1):
                    Diesel fuel.
                DIESEL_PLUS (19):
                    Diesel plus fuel.
                REGULAR_UNLEADED (2):
                    Regular unleaded.
                MIDGRADE (3):
                    Midgrade.
                PREMIUM (4):
                    Premium.
                SP91 (5):
                    SP 91.
                SP91_E10 (6):
                    SP 91 E10.
                SP92 (7):
                    SP 92.
                SP95 (8):
                    SP 95.
                SP95_E10 (9):
                    SP95 E10.
                SP98 (10):
                    SP 98.
                SP99 (11):
                    SP 99.
                SP100 (12):
                    SP 100.
                LPG (13):
                    Liquefied Petroleum Gas.
                E80 (14):
                    E 80.
                E85 (15):
                    E 85.
                E100 (20):
                    E 100.
                METHANE (16):
                    Methane.
                BIO_DIESEL (17):
                    Bio-diesel.
                TRUCK_DIESEL (18):
                    Truck diesel.
            """

            FUEL_TYPE_UNSPECIFIED = 0
            DIESEL = 1
            DIESEL_PLUS = 19
            REGULAR_UNLEADED = 2
            MIDGRADE = 3
            PREMIUM = 4
            SP91 = 5
            SP91_E10 = 6
            SP92 = 7
            SP95 = 8
            SP95_E10 = 9
            SP98 = 10
            SP99 = 11
            SP100 = 12
            LPG = 13
            E80 = 14
            E85 = 15
            E100 = 20
            METHANE = 16
            BIO_DIESEL = 17
            TRUCK_DIESEL = 18

        type_: "FuelOptions.FuelPrice.FuelType" = proto.Field(
            proto.ENUM,
            number=1,
            enum="FuelOptions.FuelPrice.FuelType",
        )
        price: money_pb2.Money = proto.Field(
            proto.MESSAGE,
            number=2,
            message=money_pb2.Money,
        )
        update_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=3,
            message=timestamp_pb2.Timestamp,
        )

    fuel_prices: MutableSequence[FuelPrice] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=FuelPrice,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
