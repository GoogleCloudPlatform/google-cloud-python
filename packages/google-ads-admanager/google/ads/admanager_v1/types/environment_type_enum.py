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
        "EnvironmentTypeEnum",
    },
)


class EnvironmentTypeEnum(proto.Message):
    r"""Wrapper message for
    [EnvironmentType][google.ads.admanager.v1.EnvironmentTypeEnum.EnvironmentType].

    """

    class EnvironmentType(proto.Enum):
        r"""The different environments in which an ad can be shown.

        Values:
            ENVIRONMENT_TYPE_UNSPECIFIED (0):
                No value specified
            BROWSER (1):
                A regular web browser.
            VIDEO_PLAYER (2):
                Video players.
        """

        ENVIRONMENT_TYPE_UNSPECIFIED = 0
        BROWSER = 1
        VIDEO_PLAYER = 2


__all__ = tuple(sorted(__protobuf__.manifest))
