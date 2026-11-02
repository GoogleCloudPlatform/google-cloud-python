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
    package="google.ads.datamanager.v1",
    manifest={
        "MatchRateRange",
    },
)


class MatchRateRange(proto.Enum):
    r"""The match rate range of the upload or userlist.

    Values:
        MATCH_RATE_RANGE_UNKNOWN (0):
            The match rate range is unknown.
        MATCH_RATE_RANGE_NOT_ELIGIBLE (1):
            The match rate range is not eligible.
        MATCH_RATE_RANGE_LESS_THAN_20 (2):
            The match rate range is less than 20% (in the interval
            ``[0, 20)``).
        MATCH_RATE_RANGE_20_TO_30 (3):
            The match rate range is between 20% and 30% (in the interval
            ``[20, 31)``).
        MATCH_RATE_RANGE_31_TO_40 (4):
            The match rate range is between 31% and 40% (in the interval
            ``[31, 41)``).
        MATCH_RATE_RANGE_41_TO_50 (5):
            The match rate range is between 41% and 50% (in the interval
            ``[41, 51)``).
        MATCH_RATE_RANGE_51_TO_60 (6):
            The match rate range is between 51% and 60% (in the interval
            ``[51, 61)``.
        MATCH_RATE_RANGE_61_TO_70 (7):
            The match rate range is between 61% and 70% (in the interval
            ``[61, 71)``).
        MATCH_RATE_RANGE_71_TO_80 (8):
            The match rate range is between 71% and 80% (in the interval
            ``[71, 81)``).
        MATCH_RATE_RANGE_81_TO_90 (9):
            The match rate range is between 81% and 90% (in the interval
            ``[81, 91)``).
        MATCH_RATE_RANGE_91_TO_100 (10):
            The match rate range is between 91% and 100% (in the
            interval ``[91, 100]``).
    """

    MATCH_RATE_RANGE_UNKNOWN = 0
    MATCH_RATE_RANGE_NOT_ELIGIBLE = 1
    MATCH_RATE_RANGE_LESS_THAN_20 = 2
    MATCH_RATE_RANGE_20_TO_30 = 3
    MATCH_RATE_RANGE_31_TO_40 = 4
    MATCH_RATE_RANGE_41_TO_50 = 5
    MATCH_RATE_RANGE_51_TO_60 = 6
    MATCH_RATE_RANGE_61_TO_70 = 7
    MATCH_RATE_RANGE_71_TO_80 = 8
    MATCH_RATE_RANGE_81_TO_90 = 9
    MATCH_RATE_RANGE_91_TO_100 = 10


__all__ = tuple(sorted(__protobuf__.manifest))
