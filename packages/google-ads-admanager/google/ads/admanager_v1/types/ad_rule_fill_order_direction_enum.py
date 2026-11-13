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
        "AdRuleFillOrderDirectionEnum",
    },
)


class AdRuleFillOrderDirectionEnum(proto.Message):
    r"""Wrapper message for
    [AdRuleFillOrderDirection][google.ads.admanager.v1.AdRuleFillOrderDirectionEnum.AdRuleFillOrderDirection]

    """

    class AdRuleFillOrderDirection(proto.Enum):
        r"""Defines the fill order direction of ad breaks with
        [AdBreakOptimizationTypeEnum.AdBreakOptimizationType.POSITION][google.ads.admanager.v1.AdBreakOptimizationTypeEnum.AdBreakOptimizationType.POSITION].

        Values:
            AD_RULE_FILL_ORDER_DIRECTION_UNSPECIFIED (0):
                Default value. This value is unused.
            EDGE_TO_CENTER (1):
                A break template should be filled from edge
                to center.
            LEFT_TO_RIGHT (2):
                A break template should be filled from left
                to right.
            RIGHT_TO_LEFT (3):
                A break template should be filled from right
                to left.
        """

        AD_RULE_FILL_ORDER_DIRECTION_UNSPECIFIED = 0
        EDGE_TO_CENTER = 1
        LEFT_TO_RIGHT = 2
        RIGHT_TO_LEFT = 3


__all__ = tuple(sorted(__protobuf__.manifest))
