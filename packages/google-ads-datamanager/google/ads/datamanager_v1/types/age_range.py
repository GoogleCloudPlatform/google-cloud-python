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
        "AgeRange",
    },
)


class AgeRange(proto.Enum):
    r"""The demographic age ranges

    Values:
        AGE_RANGE_UNSPECIFIED (0):
            Not specified.
        AGE_RANGE_UNKNOWN (1):
            Unknown.
        AGE_RANGE_18_24 (2):
            Between 18 and 24 years old.
        AGE_RANGE_25_34 (3):
            Between 25 and 34 years old.
        AGE_RANGE_35_44 (4):
            Between 35 and 44 years old.
        AGE_RANGE_45_54 (5):
            Between 45 and 54 years old.
        AGE_RANGE_55_64 (6):
            Between 55 and 64 years old.
        AGE_RANGE_65_UP (7):
            65 years old and beyond.
    """

    AGE_RANGE_UNSPECIFIED = 0
    AGE_RANGE_UNKNOWN = 1
    AGE_RANGE_18_24 = 2
    AGE_RANGE_25_34 = 3
    AGE_RANGE_35_44 = 4
    AGE_RANGE_45_54 = 5
    AGE_RANGE_55_64 = 6
    AGE_RANGE_65_UP = 7


__all__ = tuple(sorted(__protobuf__.manifest))
