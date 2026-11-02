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
    package="google.cloud.baremetalsolution.v2",
    manifest={
        "VolumePerformanceTier",
        "WorkloadProfile",
    },
)


class VolumePerformanceTier(proto.Enum):
    r"""Performance tier of the Volume.

    Values:
        VOLUME_PERFORMANCE_TIER_UNSPECIFIED (0):
            Value is not specified.
        VOLUME_PERFORMANCE_TIER_SHARED (1):
            Regular volumes, shared aggregates.
        VOLUME_PERFORMANCE_TIER_ASSIGNED (2):
            Assigned aggregates.
        VOLUME_PERFORMANCE_TIER_HT (3):
            High throughput aggregates.
    """

    VOLUME_PERFORMANCE_TIER_UNSPECIFIED = 0
    VOLUME_PERFORMANCE_TIER_SHARED = 1
    VOLUME_PERFORMANCE_TIER_ASSIGNED = 2
    VOLUME_PERFORMANCE_TIER_HT = 3


class WorkloadProfile(proto.Enum):
    r"""The possible values for a workload profile.

    Values:
        WORKLOAD_PROFILE_UNSPECIFIED (0):
            The workload profile is in an unknown state.
        WORKLOAD_PROFILE_GENERIC (1):
            The workload profile is generic.
        WORKLOAD_PROFILE_HANA (2):
            The workload profile is hana.
    """

    WORKLOAD_PROFILE_UNSPECIFIED = 0
    WORKLOAD_PROFILE_GENERIC = 1
    WORKLOAD_PROFILE_HANA = 2


__all__ = tuple(sorted(__protobuf__.manifest))
