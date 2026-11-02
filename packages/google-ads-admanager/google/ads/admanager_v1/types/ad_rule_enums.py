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
        "AdRuleStatusEnum",
        "AdRuleFrequencyCapBehaviorEnum",
    },
)


class AdRuleStatusEnum(proto.Message):
    r""" """

    class AdRuleStatus(proto.Enum):
        r"""Represents the status of ad rules and ad rule slots.

        Values:
            AD_RULE_STATUS_UNSPECIFIED (0):
                Default value. This value is unused.
            ACTIVE (1):
                Created and ready to be served. Is
                user-visible.
            DELETED (2):
                Marked as deleted, not user-visible.
            INACTIVE (5):
                Inactive, not user-visible.
        """

        AD_RULE_STATUS_UNSPECIFIED = 0
        ACTIVE = 1
        DELETED = 2
        INACTIVE = 5


class AdRuleFrequencyCapBehaviorEnum(proto.Message):
    r"""Wrapper message for
    [AdRuleFrequencyCapBehavior][google.ads.admanager.v1.AdRuleFrequencyCapBehaviorEnum.AdRuleFrequencyCapBehavior]

    """

    class AdRuleFrequencyCapBehavior(proto.Enum):
        r"""Types of behavior for frequency caps within ad rules.

        Values:
            AD_RULE_FREQUENCY_CAP_BEHAVIOR_UNSPECIFIED (0):
                Default value. This value is unused.
            DEFER (1):
                Defer frequency cap decisions to the next ad
                rule in priority order.
            TURN_OFF (2):
                Turn off all frequency caps.
            TURN_ON (3):
                Turn on at least one of the frequency caps.
        """

        AD_RULE_FREQUENCY_CAP_BEHAVIOR_UNSPECIFIED = 0
        DEFER = 1
        TURN_OFF = 2
        TURN_ON = 3


__all__ = tuple(sorted(__protobuf__.manifest))
