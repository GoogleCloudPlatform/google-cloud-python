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
    package="google.cloud.vectorsearch.v1",
    manifest={
        "DistanceMetric",
    },
)


class DistanceMetric(proto.Enum):
    r"""Distance metric for vector search.

    Values:
        DISTANCE_METRIC_UNSPECIFIED (0):
            Default value, distance metric is not
            specified.
        DOT_PRODUCT (1):
            Dot product distance metric.
        COSINE_DISTANCE (2):
            Cosine distance metric.
    """

    DISTANCE_METRIC_UNSPECIFIED = 0
    DOT_PRODUCT = 1
    COSINE_DISTANCE = 2


__all__ = tuple(sorted(__protobuf__.manifest))
