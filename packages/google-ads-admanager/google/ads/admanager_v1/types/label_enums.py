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
        "LabelTypeEnum",
    },
)


class LabelTypeEnum(proto.Message):
    r"""Wrapper message for
    [LabelType][google.ads.admanager.v1.LabelTypeEnum.LabelType]

    """

    class LabelType(proto.Enum):
        r"""Represents the types of labels supported.

        Values:
            LABEL_TYPE_UNSPECIFIED (0):
                Default value. This value is unused.
            AD_EXCLUSION (1):
                Allows for the creation of labels to exclude
                ads from showing against a tag that specifies
                the label as an exclusion.
            AD_UNIT_FREQUENCY_CAP (2):
                Allows for the creation of limits on the
                frequency that a user sees a particular type of
                creative over a portion of the inventory.
            CANONICAL_CATEGORY (3):
                Allows for the creation of labels mapped to a
                Google canonical ad category, which can be used
                for competitive exclusions and blocking across
                Google systems.
            COMPETITIVE_EXCLUSION (4):
                Allows for the creation of labels to exclude
                competing ads from showing on the same page.
            CREATIVE_WRAPPER (5):
                Allows for the creation of labels that can be
                used to force the wrapping of a delivering
                creative with header/footer creatives.
        """

        LABEL_TYPE_UNSPECIFIED = 0
        AD_EXCLUSION = 1
        AD_UNIT_FREQUENCY_CAP = 2
        CANONICAL_CATEGORY = 3
        COMPETITIVE_EXCLUSION = 4
        CREATIVE_WRAPPER = 5


__all__ = tuple(sorted(__protobuf__.manifest))
