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
    package="google.cloud.automl.v1",
    manifest={
        "NormalizedVertex",
        "BoundingPoly",
    },
)


class NormalizedVertex(proto.Message):
    r"""A vertex represents a 2D point in the image.
    The normalized vertex coordinates are between 0 to 1 fractions
    relative to the original plane (image, video). E.g. if the plane
    (e.g. whole image) would have size 10 x 20 then a point with
    normalized coordinates (0.1, 0.3) would be at the position (1,
    6) on that plane.

    Attributes:
        x (float):
            Required. Horizontal coordinate.
        y (float):
            Required. Vertical coordinate.
    """

    x: float = proto.Field(
        proto.FLOAT,
        number=1,
    )
    y: float = proto.Field(
        proto.FLOAT,
        number=2,
    )


class BoundingPoly(proto.Message):
    r"""A bounding polygon of a detected object on a plane. On output both
    vertices and normalized_vertices are provided. The polygon is formed
    by connecting vertices in the order they are listed.

    Attributes:
        normalized_vertices (MutableSequence[google.cloud.automl_v1.types.NormalizedVertex]):
            Output only . The bounding polygon normalized
            vertices.
    """

    normalized_vertices: MutableSequence["NormalizedVertex"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="NormalizedVertex",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
