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
    package="google.cloud.retail.v2beta",
    manifest={
        "HarmCategory",
        "SafetySetting",
    },
)


class HarmCategory(proto.Enum):
    r"""Harm categories that will block the content.

    Values:
        HARM_CATEGORY_UNSPECIFIED (0):
            The harm category is unspecified.
        HARM_CATEGORY_HATE_SPEECH (1):
            The harm category is hate speech.
        HARM_CATEGORY_DANGEROUS_CONTENT (2):
            The harm category is dangerous content.
        HARM_CATEGORY_HARASSMENT (3):
            The harm category is harassment.
        HARM_CATEGORY_SEXUALLY_EXPLICIT (4):
            The harm category is sexually explicit
            content.
        HARM_CATEGORY_CIVIC_INTEGRITY (5):
            The harm category is civic integrity.
    """

    HARM_CATEGORY_UNSPECIFIED = 0
    HARM_CATEGORY_HATE_SPEECH = 1
    HARM_CATEGORY_DANGEROUS_CONTENT = 2
    HARM_CATEGORY_HARASSMENT = 3
    HARM_CATEGORY_SEXUALLY_EXPLICIT = 4
    HARM_CATEGORY_CIVIC_INTEGRITY = 5


class SafetySetting(proto.Message):
    r"""Safety settings.

    Attributes:
        category (google.cloud.retail_v2beta.types.HarmCategory):
            Harm category.
        threshold (google.cloud.retail_v2beta.types.SafetySetting.HarmBlockThreshold):
            The harm block threshold.
        method (google.cloud.retail_v2beta.types.SafetySetting.HarmBlockMethod):
            Optional. Specify if the threshold is used
            for probability or severity score. If not
            specified, the threshold is used for probability
            score.
    """

    class HarmBlockThreshold(proto.Enum):
        r"""Probability based thresholds levels for blocking.

        Values:
            HARM_BLOCK_THRESHOLD_UNSPECIFIED (0):
                Unspecified harm block threshold.
            BLOCK_LOW_AND_ABOVE (1):
                Block low threshold and above (i.e. block
                more).
            BLOCK_MEDIUM_AND_ABOVE (2):
                Block medium threshold and above.
            BLOCK_ONLY_HIGH (3):
                Block only high threshold (i.e. block less).
            BLOCK_NONE (4):
                Block none.
            OFF (5):
                Turn off the safety filter.
        """

        HARM_BLOCK_THRESHOLD_UNSPECIFIED = 0
        BLOCK_LOW_AND_ABOVE = 1
        BLOCK_MEDIUM_AND_ABOVE = 2
        BLOCK_ONLY_HIGH = 3
        BLOCK_NONE = 4
        OFF = 5

    class HarmBlockMethod(proto.Enum):
        r"""Probability vs severity.

        Values:
            HARM_BLOCK_METHOD_UNSPECIFIED (0):
                The harm block method is unspecified.
            SEVERITY (1):
                The harm block method uses both probability
                and severity scores.
            PROBABILITY (2):
                The harm block method uses the probability
                score.
        """

        HARM_BLOCK_METHOD_UNSPECIFIED = 0
        SEVERITY = 1
        PROBABILITY = 2

    category: "HarmCategory" = proto.Field(
        proto.ENUM,
        number=1,
        enum="HarmCategory",
    )
    threshold: HarmBlockThreshold = proto.Field(
        proto.ENUM,
        number=2,
        enum=HarmBlockThreshold,
    )
    method: HarmBlockMethod = proto.Field(
        proto.ENUM,
        number=3,
        enum=HarmBlockMethod,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
