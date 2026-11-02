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

from google.maps.routing_v2.types import vehicle_emission_type

__protobuf__ = proto.module(
    package="google.maps.routing.v2",
    manifest={
        "VehicleInfo",
    },
)


class VehicleInfo(proto.Message):
    r"""Contains the vehicle information, such as the vehicle
    emission type.

    Attributes:
        emission_type (google.maps.routing_v2.types.VehicleEmissionType):
            Describes the vehicle's emission type. Applies only to the
            ``DRIVE``
            [``RouteTravelMode``][google.maps.routing.v2.RouteTravelMode].
    """

    emission_type: vehicle_emission_type.VehicleEmissionType = proto.Field(
        proto.ENUM,
        number=2,
        enum=vehicle_emission_type.VehicleEmissionType,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
