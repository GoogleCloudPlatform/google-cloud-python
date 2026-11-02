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
    package="google.cloud.run.v2",
    manifest={
        "TrafficTargetAllocationType",
        "TrafficTarget",
        "TrafficTargetStatus",
    },
)


class TrafficTargetAllocationType(proto.Enum):
    r"""The type of instance allocation.

    Values:
        TRAFFIC_TARGET_ALLOCATION_TYPE_UNSPECIFIED (0):
            Unspecified instance allocation type.
        TRAFFIC_TARGET_ALLOCATION_TYPE_LATEST (1):
            Allocates instances to the Service's latest
            ready Revision.
        TRAFFIC_TARGET_ALLOCATION_TYPE_REVISION (2):
            Allocates instances to a Revision by name.
    """

    TRAFFIC_TARGET_ALLOCATION_TYPE_UNSPECIFIED = 0
    TRAFFIC_TARGET_ALLOCATION_TYPE_LATEST = 1
    TRAFFIC_TARGET_ALLOCATION_TYPE_REVISION = 2


class TrafficTarget(proto.Message):
    r"""Holds a single traffic routing entry for the Service.
    Allocations can be done to a specific Revision name, or pointing
    to the latest Ready Revision.

    Attributes:
        type_ (google.cloud.run_v2.types.TrafficTargetAllocationType):
            The allocation type for this traffic target.
        revision (str):
            Revision to which to send this portion of
            traffic, if traffic allocation is by revision.
        percent (int):
            Specifies percent of the traffic to this
            Revision. This defaults to zero if unspecified.
        tag (str):
            Indicates a string to be part of the URI to
            exclusively reference this target.
    """

    type_: "TrafficTargetAllocationType" = proto.Field(
        proto.ENUM,
        number=1,
        enum="TrafficTargetAllocationType",
    )
    revision: str = proto.Field(
        proto.STRING,
        number=2,
    )
    percent: int = proto.Field(
        proto.INT32,
        number=3,
    )
    tag: str = proto.Field(
        proto.STRING,
        number=4,
    )


class TrafficTargetStatus(proto.Message):
    r"""Represents the observed state of a single ``TrafficTarget`` entry.

    Attributes:
        type_ (google.cloud.run_v2.types.TrafficTargetAllocationType):
            The allocation type for this traffic target.
        revision (str):
            Revision to which this traffic is sent.
        percent (int):
            Specifies percent of the traffic to this
            Revision.
        tag (str):
            Indicates the string used in the URI to
            exclusively reference this target.
        uri (str):
            Displays the target URI.
    """

    type_: "TrafficTargetAllocationType" = proto.Field(
        proto.ENUM,
        number=1,
        enum="TrafficTargetAllocationType",
    )
    revision: str = proto.Field(
        proto.STRING,
        number=2,
    )
    percent: int = proto.Field(
        proto.INT32,
        number=3,
    )
    tag: str = proto.Field(
        proto.STRING,
        number=4,
    )
    uri: str = proto.Field(
        proto.STRING,
        number=5,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
