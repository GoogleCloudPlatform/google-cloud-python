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
        "SupplyPathTypeEnum",
    },
)


class SupplyPathTypeEnum(proto.Message):
    r"""Wrapper message for
    [SupplyPathType][google.ads.admanager.v1.SupplyPathTypeEnum.SupplyPathType].

    """

    class SupplyPathType(proto.Enum):
        r"""Describes how the demand will be supplied

        Values:
            SUPPLY_PATH_TYPE_UNSPECIFIED (0):
                Not specified value.
            DIRECT (1):
                The demand will be supplied by the ad server
                directly.
            DEMAND_SIDE_PLATFORM (2):
                The demand will be supplied by a demand side
                platform (DSP).
        """

        SUPPLY_PATH_TYPE_UNSPECIFIED = 0
        DIRECT = 1
        DEMAND_SIDE_PLATFORM = 2


__all__ = tuple(sorted(__protobuf__.manifest))
