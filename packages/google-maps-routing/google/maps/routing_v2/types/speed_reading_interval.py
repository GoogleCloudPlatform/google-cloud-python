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
    package="google.maps.routing.v2",
    manifest={
        "SpeedReadingInterval",
    },
)


class SpeedReadingInterval(proto.Message):
    r"""Traffic density indicator on a contiguous segment of a polyline or
    path. Given a path with points P_0, P_1, ... , P_N (zero-based
    index), the ``SpeedReadingInterval`` defines an interval and
    describes its traffic using the following categories.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        start_polyline_point_index (int):
            The starting index of this interval in the
            polyline.

            This field is a member of `oneof`_ ``_start_polyline_point_index``.
        end_polyline_point_index (int):
            The ending index of this interval in the
            polyline.

            This field is a member of `oneof`_ ``_end_polyline_point_index``.
        speed (google.maps.routing_v2.types.SpeedReadingInterval.Speed):
            Traffic speed in this interval.

            This field is a member of `oneof`_ ``speed_type``.
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
        optional=True,
    )
    end_polyline_point_index: int = proto.Field(
        proto.INT32,
        number=2,
        optional=True,
    )
    speed: Speed = proto.Field(
        proto.ENUM,
        number=3,
        oneof="speed_type",
        enum=Speed,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
