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
        "AdRuleSlotBehaviorEnum",
    },
)


class AdRuleSlotBehaviorEnum(proto.Message):
    r"""Wrapper message for
    [AdRuleSlotBehavior][google.ads.admanager.v1.AdRuleSlotBehaviorEnum.AdRuleSlotBehavior]

    """

    class AdRuleSlotBehavior(proto.Enum):
        r"""The types of behaviors for ads within a BaseAdRuleSlot ad
        rule slot.

        Values:
            AD_RULE_SLOT_BEHAVIOR_UNSPECIFIED (0):
                Default value. This value is unused.
            ALWAYS_SHOW (1):
                This ad rule always includes this slot's ads.
            DEFER (2):
                Defer to lower priority rules. This ad rule
                doesn't specify guidelines for this slot's ads.
            NEVER_SHOW (3):
                This ad rule never includes this slot's ads.
        """

        AD_RULE_SLOT_BEHAVIOR_UNSPECIFIED = 0
        ALWAYS_SHOW = 1
        DEFER = 2
        NEVER_SHOW = 3


__all__ = tuple(sorted(__protobuf__.manifest))
