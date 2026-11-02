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
        "InstanceSplitAllocationType",
        "InstanceSplit",
        "InstanceSplitStatus",
    },
)


class InstanceSplitAllocationType(proto.Enum):
    r"""The type of instance split allocation.

    Values:
        INSTANCE_SPLIT_ALLOCATION_TYPE_UNSPECIFIED (0):
            Unspecified instance allocation type.
        INSTANCE_SPLIT_ALLOCATION_TYPE_LATEST (1):
            Allocates instances to the Service's latest
            ready Revision.
        INSTANCE_SPLIT_ALLOCATION_TYPE_REVISION (2):
            Allocates instances to a Revision by name.
    """

    INSTANCE_SPLIT_ALLOCATION_TYPE_UNSPECIFIED = 0
    INSTANCE_SPLIT_ALLOCATION_TYPE_LATEST = 1
    INSTANCE_SPLIT_ALLOCATION_TYPE_REVISION = 2


class InstanceSplit(proto.Message):
    r"""Holds a single instance split entry for the Worker.
    Allocations can be done to a specific Revision name, or pointing
    to the latest Ready Revision.

    Attributes:
        type_ (google.cloud.run_v2.types.InstanceSplitAllocationType):
            The allocation type for this instance split.
        revision (str):
            Revision to which to assign this portion of
            instances, if split allocation is by revision.
        percent (int):
            Specifies percent of the instance split to
            this Revision. This defaults to zero if
            unspecified.
    """

    type_: "InstanceSplitAllocationType" = proto.Field(
        proto.ENUM,
        number=1,
        enum="InstanceSplitAllocationType",
    )
    revision: str = proto.Field(
        proto.STRING,
        number=2,
    )
    percent: int = proto.Field(
        proto.INT32,
        number=3,
    )


class InstanceSplitStatus(proto.Message):
    r"""Represents the observed state of a single ``InstanceSplit`` entry.

    Attributes:
        type_ (google.cloud.run_v2.types.InstanceSplitAllocationType):
            The allocation type for this instance split.
        revision (str):
            Revision to which this instance split is
            assigned.
        percent (int):
            Specifies percent of the instance split to
            this Revision.
    """

    type_: "InstanceSplitAllocationType" = proto.Field(
        proto.ENUM,
        number=1,
        enum="InstanceSplitAllocationType",
    )
    revision: str = proto.Field(
        proto.STRING,
        number=2,
    )
    percent: int = proto.Field(
        proto.INT32,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
