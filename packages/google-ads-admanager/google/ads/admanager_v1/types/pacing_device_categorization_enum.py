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
        "PacingDeviceCategorizationEnum",
    },
)


class PacingDeviceCategorizationEnum(proto.Message):
    r"""Wrapper message for
    [PacingDeviceCategorization][google.ads.admanager.v1.PacingDeviceCategorizationEnum.PacingDeviceCategorization]

    """

    class PacingDeviceCategorization(proto.Enum):
        r"""Represents whose device categorization to use on Nielsen
        measured line item with auto-pacing enabled.

        Values:
            PACING_DEVICE_CATEGORIZATION_UNSPECIFIED (0):
                Default value. This value is unused.
            GOOGLE (1):
                Use Google's device categorization in
                auto-pacing.
            NIELSEN (2):
                Use Nielsen device categorization in
                auto-pacing
        """

        PACING_DEVICE_CATEGORIZATION_UNSPECIFIED = 0
        GOOGLE = 1
        NIELSEN = 2


__all__ = tuple(sorted(__protobuf__.manifest))
