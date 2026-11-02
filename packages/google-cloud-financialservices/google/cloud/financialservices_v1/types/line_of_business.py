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
    package="google.cloud.financialservices.v1",
    manifest={
        "LineOfBusiness",
    },
)


class LineOfBusiness(proto.Enum):
    r"""Indicate which LineOfBusiness a party belongs to.

    Values:
        LINE_OF_BUSINESS_UNSPECIFIED (0):
            An unspecified LineOfBusiness. Do not use.
        COMMERCIAL (1):
            Commercial LineOfBusiness.
        RETAIL (2):
            Retail LineOfBusiness.
    """

    LINE_OF_BUSINESS_UNSPECIFIED = 0
    COMMERCIAL = 1
    RETAIL = 2


__all__ = tuple(sorted(__protobuf__.manifest))
