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
        "YieldEnvironmentTypeEnum",
    },
)


class YieldEnvironmentTypeEnum(proto.Message):
    r"""Wrapper message for
    [YieldEnvironmentType][google.ads.admanager.v1.YieldEnvironmentTypeEnum.YieldEnvironmentType]

    """

    class YieldEnvironmentType(proto.Enum):
        r"""Available environment types for mediation. Describes the
        environment/technology rendering the TYM response.

        Values:
            YIELD_ENVIRONMENT_TYPE_UNSPECIFIED (0):
                Default value. This value is unused.
            MOBILE (1):
                Mobile environment type.
            VIDEO_VAST (2):
                Video in-stream environment type.
            WEB (3):
                Web environment type.
        """

        YIELD_ENVIRONMENT_TYPE_UNSPECIFIED = 0
        MOBILE = 1
        VIDEO_VAST = 2
        WEB = 3


__all__ = tuple(sorted(__protobuf__.manifest))
