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
        "CustomTargetingValueStatusEnum",
        "CustomTargetingValueMatchTypeEnum",
    },
)


class CustomTargetingValueStatusEnum(proto.Message):
    r"""Wrapper message for
    [CustomTargetingValueStatus][google.ads.admanager.v1.CustomTargetingValueStatusEnum.CustomTargetingValueStatus]

    """

    class CustomTargetingValueStatus(proto.Enum):
        r"""Status of the custom targeting value.

        Values:
            CUSTOM_TARGETING_VALUE_STATUS_UNSPECIFIED (0):
                Not specified value.
            ACTIVE (1):
                Custom targeting value is active.
            INACTIVE (2):
                Custom targeting value is inactive.
        """

        CUSTOM_TARGETING_VALUE_STATUS_UNSPECIFIED = 0
        ACTIVE = 1
        INACTIVE = 2


class CustomTargetingValueMatchTypeEnum(proto.Message):
    r"""Wrapper message for
    [CustomTargetingValueMatchType][google.ads.admanager.v1.CustomTargetingValueMatchTypeEnum.CustomTargetingValueMatchType]

    """

    class CustomTargetingValueMatchType(proto.Enum):
        r"""Match type of the custom targeting value.

        Values:
            CUSTOM_TARGETING_VALUE_MATCH_TYPE_UNSPECIFIED (0):
                Not specified value.
            EXACT (1):
                Used for exact matching. For example, the
                targeting value car=honda will only match to the
                ad request car=honda.
            BROAD (2):
                Used for lenient matching when at least one
                of the words in the ad request matches the
                targeted value. The targeting value car=honda
                will match to ad requests containing the word
                honda. So ad requests car=honda or car=honda
                civic or car=buy honda or car=how much does a
                honda cost will all have the line item
                delivered.
                This match type can not be used within an
                audience segment rule.
            PREFIX (3):
                Used for 'starts with' matching when the
                first few characters in the ad request match all
                of the characters in the targeted value. The
                targeting value car=honda will match to ad
                requests car=honda or car=hondas for sale but
                not to car=I want a honda.
            BROAD_PREFIX (4):
                This is a combination of MatchType#BROAD and
                MatchType#PREFIX matching. The targeting value
                car=honda will match to ad requests that contain
                words that start with the characters in the
                targeted value, for example with car=civic
                hondas.
                This match type can not be used within an
                audience segment rule.
            SUFFIX (5):
                Used for 'ends with' matching when the last
                characters in the ad request match all of the
                characters in the targeted value. The targeting
                value car=honda will match with ad requests
                car=honda or car=I want a honda but not to
                car=hondas for sale.
                This match type can not be used within line item
                targeting.
            CONTAINS (6):
                Used for 'within' matching when the string in
                the ad request contains the string in the
                targeted value. The targeting value car=honda
                will match with ad requests car=honda, car=I
                want a honda, and also with car=hondas for sale,
                but not with car=misspelled hond a. This match
                type can not be used within line item targeting.
        """

        CUSTOM_TARGETING_VALUE_MATCH_TYPE_UNSPECIFIED = 0
        EXACT = 1
        BROAD = 2
        PREFIX = 3
        BROAD_PREFIX = 4
        SUFFIX = 5
        CONTAINS = 6


__all__ = tuple(sorted(__protobuf__.manifest))
