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
    package="google.cloud.capacityplanner.v1beta",
    manifest={
        "LocationLevel",
        "LocationIdentifier",
    },
)


class LocationLevel(proto.Enum):
    r"""The level of the Google Cloud Platform location.

    Values:
        LOCATION_LEVEL_UNSPECIFIED (0):
            Location level is unspecified.
        REGION (1):
            Cloud region.
        ZONE (2):
            Cloud zone.
        GLOBAL (3):
            Globally.
        METRO (4):
            A metro.
        DUAL_REGION (5):
            Dual region pair.
        MULTI_REGION (6):
            Multiple regions.
    """

    LOCATION_LEVEL_UNSPECIFIED = 0
    REGION = 1
    ZONE = 2
    GLOBAL = 3
    METRO = 4
    DUAL_REGION = 5
    MULTI_REGION = 6


class LocationIdentifier(proto.Message):
    r"""Identifier for a Google Cloud Platform location.

    Attributes:
        location_level (google.cloud.capacityplanner_v1beta.types.LocationLevel):
            The location level such as a region.
        source (str):
            Required. Location where resource is sourced.
            For Cloud Storage, the alphabetically first
            location is the source.
        linked_locations (MutableSequence[google.cloud.capacityplanner_v1beta.types.LocationIdentifier.LinkedLocation]):
            Optional. Other linked locations.
    """

    class LinkedLocation(proto.Message):
        r"""

        Attributes:
            location_level (google.cloud.capacityplanner_v1beta.types.LocationLevel):
                The location level such as a region.
            location (str):
                Required. The linked cloud location.
            label (str):

        """

        location_level: "LocationLevel" = proto.Field(
            proto.ENUM,
            number=1,
            enum="LocationLevel",
        )
        location: str = proto.Field(
            proto.STRING,
            number=2,
        )
        label: str = proto.Field(
            proto.STRING,
            number=3,
        )

    location_level: "LocationLevel" = proto.Field(
        proto.ENUM,
        number=1,
        enum="LocationLevel",
    )
    source: str = proto.Field(
        proto.STRING,
        number=2,
    )
    linked_locations: MutableSequence[LinkedLocation] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=LinkedLocation,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
