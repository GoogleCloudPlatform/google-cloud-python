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
        "AdRuleSlotBumperEnum",
    },
)


class AdRuleSlotBumperEnum(proto.Message):
    r"""Wrapper message for
    [AdRuleSlotBumper][google.ads.admanager.v1.AdRuleSlotBumperEnum.AdRuleSlotBumper]

    """

    class AdRuleSlotBumper(proto.Enum):
        r"""Types of bumper ads on an ad rule slot.

        Values:
            AD_RULE_SLOT_BUMPER_UNSPECIFIED (0):
                Default value. This value is unused.
            AFTER (1):
                Show a bumper ad after the slot's other ads.
            BEFORE (2):
                Show a bumper ad before the slot's other ads.
            BEFORE_AND_AFTER (3):
                Show a bumper before and after the slot's
                other ads.
            NONE (4):
                Do not show a bumper ad.
        """

        AD_RULE_SLOT_BUMPER_UNSPECIFIED = 0
        AFTER = 1
        BEFORE = 2
        BEFORE_AND_AFTER = 3
        NONE = 4


__all__ = tuple(sorted(__protobuf__.manifest))
