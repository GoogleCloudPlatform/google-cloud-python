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
        "DaypartingTimeZoneEnum",
    },
)


class DaypartingTimeZoneEnum(proto.Message):
    r"""Wrapper message for
    [DaypartingTimeZone][google.ads.admanager.v1.DaypartingTimeZoneEnum.DaypartingTimeZone]

    """

    class DaypartingTimeZone(proto.Enum):
        r"""Represents the time zone to be used for daypart targeting.

        Values:
            DAYPARTING_TIME_ZONE_UNSPECIFIED (0):
                Default value. This value is unused.
            PUBLISHER (1):
                Use the time zone of the publisher for
                daypart targeting.
            USER (2):
                Use the time zone of the browser for daypart
                targeting.
        """

        DAYPARTING_TIME_ZONE_UNSPECIFIED = 0
        PUBLISHER = 1
        USER = 2


__all__ = tuple(sorted(__protobuf__.manifest))
