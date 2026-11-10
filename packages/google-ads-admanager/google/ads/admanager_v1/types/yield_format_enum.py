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
        "YieldFormatEnum",
    },
)


class YieldFormatEnum(proto.Message):
    r"""Wrapper message for
    [YieldFormat][google.ads.admanager.v1.YieldFormatEnum.YieldFormat]

    """

    class YieldFormat(proto.Enum):
        r"""Represents possible formats for a yield group.

        Values:
            YIELD_FORMAT_UNSPECIFIED (0):
                Default value. This value is unused.
            APP_OPEN (1):
                App open format when users open their app.
            BANNER (2):
                Banner format, some fixed wxh size.
            INTERSTITIAL (3):
                Interstitial ad format.
            NATIVE (4):
                Native ad format.
            REWARDED (5):
                Rewarded format.
            REWARDED_INTERSTITIAL (6):
                Rewarded interstitial format.
            VIDEO_VAST (7):
                Vast video ad format.
        """

        YIELD_FORMAT_UNSPECIFIED = 0
        APP_OPEN = 1
        BANNER = 2
        INTERSTITIAL = 3
        NATIVE = 4
        REWARDED = 5
        REWARDED_INTERSTITIAL = 6
        VIDEO_VAST = 7


__all__ = tuple(sorted(__protobuf__.manifest))
