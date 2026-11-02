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
        "AdSpotTargetingTypeEnum",
    },
)


class AdSpotTargetingTypeEnum(proto.Message):
    r"""Wrapper message for
    [AdSpotTargetingType][google.ads.admanager.v1.AdSpotTargetingTypeEnum.AdSpotTargetingType]

    """

    class AdSpotTargetingType(proto.Enum):
        r"""Defines the targeting behavior of an ad spot.

        Values:
            AD_SPOT_TARGETING_TYPE_UNSPECIFIED (0):
                Default value. This value is unused.
            EXPLICITLY_TARGETED (1):
                Only line items targeting this ad spots
                explicitly may serve in it
            EXPLICITLY_TARGETED_EXCEPT_HOUSE (2):
                If house ads are an allowed reservation type,
                they may serve in the ad spot regardless of
                whether they explicitly target it. Ads of other
                reservation types (whose type is allowed in the
                ad spot), may serve in the ad spot only if
                explicitly targeted.
            NOT_REQUIRED (3):
                Line items not targeting this ad spot
                explicitly may serve in it.
        """

        AD_SPOT_TARGETING_TYPE_UNSPECIFIED = 0
        EXPLICITLY_TARGETED = 1
        EXPLICITLY_TARGETED_EXCEPT_HOUSE = 2
        NOT_REQUIRED = 3


__all__ = tuple(sorted(__protobuf__.manifest))
