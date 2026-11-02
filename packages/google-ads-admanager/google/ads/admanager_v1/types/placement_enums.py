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
    package="google.ads.admanager.v1",
    manifest={
        "PlacementStatusEnum",
    },
)


class PlacementStatusEnum(proto.Message):
    r"""Wrapper message for
    [PlacementStatus][google.ads.admanager.v1.PlacementStatusEnum.PlacementStatus]

    """

    class PlacementStatus(proto.Enum):
        r"""Status of the placement.

        Values:
            PLACEMENT_STATUS_UNSPECIFIED (0):
                Not specified value.
            ACTIVE (1):
                Stats are collected, user-visible.
            INACTIVE (2):
                No stats collected, not user-visible.
            ARCHIVED (3):
                No stats collected, user-visible.
        """

        PLACEMENT_STATUS_UNSPECIFIED = 0
        ACTIVE = 1
        INACTIVE = 2
        ARCHIVED = 3


__all__ = tuple(sorted(__protobuf__.manifest))
