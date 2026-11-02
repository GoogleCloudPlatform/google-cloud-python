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
    package="maps.fleetengine.v1",
    manifest={
        "SpeedReadingInterval",
        "ConsumableTrafficPolyline",
    },
)


class SpeedReadingInterval(proto.Message):
    r"""Traffic density indicator on a contiguous segment of a path. Given a
    path with points P_0, P_1, ... , P_N (zero-based index), the
    SpeedReadingInterval defines an interval and describes its traffic
    using the following categories.

    Attributes:
        start_polyline_point_index (int):
            The starting index of this interval in the
            path. In JSON, when the index is 0, the field
            will appear to be unpopulated.
        end_polyline_point_index (int):
            The ending index of this interval in the
            path. In JSON, when the index is 0, the field
            will appear to be unpopulated.
        speed (google.maps.fleetengine_v1.types.SpeedReadingInterval.Speed):
            Traffic speed in this interval.
    """

    class Speed(proto.Enum):
        r"""The classification of polyline speed based on traffic data.

        Values:
            SPEED_UNSPECIFIED (0):
                Default value. This value is unused.
            NORMAL (1):
                Normal speed, no traffic delays.
            SLOW (2):
                Slowdown detected, medium amount of traffic.
            TRAFFIC_JAM (3):
                Traffic delays.
        """

        SPEED_UNSPECIFIED = 0
        NORMAL = 1
        SLOW = 2
        TRAFFIC_JAM = 3

    start_polyline_point_index: int = proto.Field(
        proto.INT32,
        number=1,
    )
    end_polyline_point_index: int = proto.Field(
        proto.INT32,
        number=2,
    )
    speed: Speed = proto.Field(
        proto.ENUM,
        number=3,
        enum=Speed,
    )


class ConsumableTrafficPolyline(proto.Message):
    r"""Traffic density along a Vehicle's path.

    Attributes:
        speed_reading_interval (MutableSequence[google.maps.fleetengine_v1.types.SpeedReadingInterval]):
            Traffic speed along the path from the
            previous waypoint to the current waypoint.
        encoded_path_to_waypoint (str):
            The path the driver is taking from the previous waypoint to
            the current waypoint. This path has landmarks in it so
            clients can show traffic markers along the path (see
            ``speed_reading_interval``). Decoding is not yet supported.
    """

    speed_reading_interval: MutableSequence["SpeedReadingInterval"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="SpeedReadingInterval",
        )
    )
    encoded_path_to_waypoint: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
