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
        "NielsenCtvPacingEnum",
    },
)


class NielsenCtvPacingEnum(proto.Message):
    r"""Wrapper message for
    [NielsenCtvPacing][google.ads.admanager.v1.NielsenCtvPacingEnum.NielsenCtvPacing]

    """

    class NielsenCtvPacing(proto.Enum):
        r"""Represents the pacing computation method for impressions on
        connected devices for a Nielsen measured line item. This only
        applies when Nielsen measurement is enabled for connected
        devices.

        Values:
            NIELSEN_CTV_PACING_UNSPECIFIED (0):
                Default value. This value is unused.
            COVIEW (1):
                Indicates that Nielsen impressions on
                connected devices are included, and we apply
                coviewing in pacing.
            NONE (2):
                The value returned if Nielsen measurement is
                disabled for connected devices.
            STRICT_COVIEW (3):
                Indicates that Nielsen impressions on
                connected devices are included, and we apply
                strict coviewing in pacing.
        """

        NIELSEN_CTV_PACING_UNSPECIFIED = 0
        COVIEW = 1
        NONE = 2
        STRICT_COVIEW = 3


__all__ = tuple(sorted(__protobuf__.manifest))
