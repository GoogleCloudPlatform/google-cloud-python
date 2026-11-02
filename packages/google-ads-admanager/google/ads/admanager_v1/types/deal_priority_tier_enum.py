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
        "DealPriorityTierEnum",
    },
)


class DealPriorityTierEnum(proto.Message):
    r"""Wrapper message for
    [DealPriorityTier][google.ads.admanager.v1.DealPriorityTierEnum.DealPriorityTier].

    """

    class DealPriorityTier(proto.Enum):
        r"""Priority tier of non guaranteed deal products.

        Values:
            DEAL_PRIORITY_TIER_UNSPECIFIED (0):
                No value specified.
            TIER1 (1):
                Tier 1
            TIER2 (2):
                Tier 2
            TIER3 (3):
                Tier 3
            TIER4 (4):
                Tier 4
            TIER5 (5):
                Tier 5
            TIER6 (6):
                Tier 6
            TIER7 (7):
                Tier 7
            TIER8 (8):
                Tier 8
            TIER9 (9):
                Tier 9
            OPTIMIZED (1000):
                Open Auction optimized tier
        """

        DEAL_PRIORITY_TIER_UNSPECIFIED = 0
        TIER1 = 1
        TIER2 = 2
        TIER3 = 3
        TIER4 = 4
        TIER5 = 5
        TIER6 = 6
        TIER7 = 7
        TIER8 = 8
        TIER9 = 9
        OPTIMIZED = 1000


__all__ = tuple(sorted(__protobuf__.manifest))
