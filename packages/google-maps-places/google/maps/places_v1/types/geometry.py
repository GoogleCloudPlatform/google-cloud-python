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

__protobuf__ = proto.module(
    package="google.maps.places.v1",
    manifest={
        "Circle",
    },
)


class Circle(proto.Message):
    r"""Circle with a LatLng as center and radius.

    Attributes:
        center (google.type.latlng_pb2.LatLng):
            Required. Center latitude and longitude.

            The range of latitude must be within [-90.0, 90.0]. The
            range of the longitude must be within [-180.0, 180.0].
        radius (float):
            Required. Radius measured in meters. The radius must be
            within [0.0, 50000.0].
    """

    center: latlng_pb2.LatLng = proto.Field(
        proto.MESSAGE,
        number=1,
        message=latlng_pb2.LatLng,
    )
    radius: float = proto.Field(
        proto.DOUBLE,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
