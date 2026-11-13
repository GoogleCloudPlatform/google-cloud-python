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
        "AdSpotFillTypeEnum",
    },
)


class AdSpotFillTypeEnum(proto.Message):
    r"""Wrapper message for
    [AdSpotFillType][google.ads.admanager.v1.AdSpotFillTypeEnum.AdSpotFillType]

    """

    class AdSpotFillType(proto.Enum):
        r"""The different options for how ad spots are filled. Only some
        allocations of ads to subpods produce a valid final pod.

        Values:
            AD_SPOT_FILL_TYPE_UNSPECIFIED (0):
                Default value. This value is unused.
            CONDITIONAL (1):
                The ad spot may only contain an ad when all
                ad spots with higher fill priority are
                "satisfied".
            OPTIONAL (2):
                The ad spot is always "satisfied", whether
                empty or nonempty.
            REQUIRED (3):
                If this ad spot is empty, the overall pod is
                invalid.
        """

        AD_SPOT_FILL_TYPE_UNSPECIFIED = 0
        CONDITIONAL = 1
        OPTIONAL = 2
        REQUIRED = 3


__all__ = tuple(sorted(__protobuf__.manifest))
