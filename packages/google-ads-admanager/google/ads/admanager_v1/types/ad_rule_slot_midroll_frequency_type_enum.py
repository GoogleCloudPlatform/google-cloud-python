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
        "AdRuleSlotMidrollFrequencyTypeEnum",
    },
)


class AdRuleSlotMidrollFrequencyTypeEnum(proto.Message):
    r"""Wrapper message for
    [AdRuleSlotMidrollFrequencyType][google.ads.admanager.v1.AdRuleSlotMidrollFrequencyTypeEnum.AdRuleSlotMidrollFrequencyType]

    """

    class AdRuleSlotMidrollFrequencyType(proto.Enum):
        r"""Frequency types for mid-roll BaseAdRuleSlot ad rule slots.

        Values:
            AD_RULE_SLOT_MIDROLL_FREQUENCY_TYPE_UNSPECIFIED (0):
                Default value. This value is unused.
            EVERY_N_CUEPOINTS (1):
                MidrollFrequency is a cue point interval and
                is a single integer value, such as "5", which
                means "play a mid-roll every 5th cue point".
            EVERY_N_SECONDS (2):
                MidrollFrequency is a time interval and
                mentioned as a single numeric value in seconds.
                For example, "100" would mean "play a mid-roll
                every 100 seconds".
            FIXED_CUE_POINTS (3):
                Same as
                [AdRuleSlotMidrollFrequencyTypeEnum.AdRuleSlotMidrollFrequencyType.FIXED_TIME][google.ads.admanager.v1.AdRuleSlotMidrollFrequencyTypeEnum.AdRuleSlotMidrollFrequencyType.FIXED_TIME],
                except the values represent the ordinal cue points ("1,3,5",
                for example).
            FIXED_TIME (4):
                MidrollFrequency is a comma-delimited list of
                points in time (in seconds) when an ad should
                play. For example, "100,300" would mean "play an
                ad at 100 seconds and 300 seconds".
            NONE (5):
                The ad rule slot is not a mid-roll and
                MidrollFrequency should be ignored.
            REVERSE_MIDROLL_INDEX (6):
                After all other frequency type is applied and
                the number of midrolls are settled, this slot
                setting will override the mid-roll defined by
                ReverseMidrollIndex.
        """

        AD_RULE_SLOT_MIDROLL_FREQUENCY_TYPE_UNSPECIFIED = 0
        EVERY_N_CUEPOINTS = 1
        EVERY_N_SECONDS = 2
        FIXED_CUE_POINTS = 3
        FIXED_TIME = 4
        NONE = 5
        REVERSE_MIDROLL_INDEX = 6


__all__ = tuple(sorted(__protobuf__.manifest))
