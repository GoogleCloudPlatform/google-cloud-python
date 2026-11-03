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
        "TargetedVideoBumperTypeEnum",
    },
)


class TargetedVideoBumperTypeEnum(proto.Message):
    r"""Wrapper message for
    [TargetedVideoBumperType][google.ads.admanager.v1.TargetedVideoBumperTypeEnum.TargetedVideoBumperType]

    """

    class TargetedVideoBumperType(proto.Enum):
        r"""Represents the options for targetable bumper positions, surrounding
        an ad pod, within a video stream. This includes before and after the
        supported ad pod positions,
        [VideoPositionEnum.VideoPosition.PREROLL][google.ads.admanager.v1.VideoPositionEnum.VideoPosition.PREROLL],
        [VideoPositionEnum.VideoPosition.MIDROLL][google.ads.admanager.v1.VideoPositionEnum.VideoPosition.MIDROLL],
        and
        [VideoPositionEnum.VideoPosition.POSTROLL][google.ads.admanager.v1.VideoPositionEnum.VideoPosition.POSTROLL].

        Values:
            TARGETED_VIDEO_BUMPER_TYPE_UNSPECIFIED (0):
                Default value. This value is unused.
            AFTER (1):
                Represents the bumper position after the ad
                pod.
            BEFORE (2):
                Represents the bumper position before the ad
                pod.
        """

        TARGETED_VIDEO_BUMPER_TYPE_UNSPECIFIED = 0
        AFTER = 1
        BEFORE = 2


__all__ = tuple(sorted(__protobuf__.manifest))
