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
import proto  # type: ignore

from google.ads.admanager_v1.types import targeting as gaa_targeting

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "TrafficForecastSegment",
    },
)


class TrafficForecastSegment(proto.Message):
    r"""An entity that defines a segment of traffic that will be
    adjusted or explored.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the
            ``TrafficForecastSegment``. Format:
            ``networks/{network_code}/trafficForecastSegments/{trafficForecastSegmentId}``
        display_name (str):
            Required. Name of the TrafficForecastSegment.
            This field must be unique among all segments for
            this network.

            This field is a member of `oneof`_ ``_display_name``.
        targeting (google.ads.admanager_v1.types.Targeting):
            Required. Immutable. The targeting that
            defines a segment of traffic.

            This field is a member of `oneof`_ ``_targeting``.
        forecast_adjustment_count (int):
            Output only. The number of active forecast
            adjustments associated with the
            TrafficForecastSegment.

            This field is a member of `oneof`_ ``_forecast_adjustment_count``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The date and time that the
            TrafficForecastSegment was created.

            This field is a member of `oneof`_ ``_create_time``.
        targeted_ad_units (MutableSequence[str]):
            Optional. The ad units that are targeted by
            the TrafficForecastSegment.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )
    targeting: gaa_targeting.Targeting = proto.Field(
        proto.MESSAGE,
        number=4,
        optional=True,
        message=gaa_targeting.Targeting,
    )
    forecast_adjustment_count: int = proto.Field(
        proto.INT32,
        number=5,
        optional=True,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        optional=True,
        message=timestamp_pb2.Timestamp,
    )
    targeted_ad_units: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=20,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
