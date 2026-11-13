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
        "AdBreakOptimizationTypeEnum",
    },
)


class AdBreakOptimizationTypeEnum(proto.Message):
    r"""Wrapper message for
    [AdBreakOptimizationType][google.ads.admanager.v1.AdBreakOptimizationTypeEnum.AdBreakOptimizationType]

    """

    class AdBreakOptimizationType(proto.Enum):
        r"""Defines how non-required ad spots within in an ad break are
        filled.

        Values:
            AD_BREAK_OPTIMIZATION_TYPE_UNSPECIFIED (0):
                Default value. This value is unused.
            POSITION (1):
                Non-required ad spots within the ad break
                will be filled according to the fill order
                direction, potentially reducing revenue for the
                break.
            REVENUE (2):
                Non-required ad spots within the ad break
                will be filled using a revenue optimizing
                algorithm.
        """

        AD_BREAK_OPTIMIZATION_TYPE_UNSPECIFIED = 0
        POSITION = 1
        REVENUE = 2


__all__ = tuple(sorted(__protobuf__.manifest))
