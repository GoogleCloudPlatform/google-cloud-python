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
        "VideoPositionEnum",
    },
)


class VideoPositionEnum(proto.Message):
    r"""Wrapper message for
    [VideoPosition][google.ads.admanager.v1.VideoPositionEnum.VideoPosition]

    """

    class VideoPosition(proto.Enum):
        r"""Represents a targetable position within a video.

        Values:
            VIDEO_POSITION_UNSPECIFIED (0):
                Default value. This value is unused.
            ALL (1):
                Allow ad placement at any position within the
                video.
            MIDROLL (2):
                Target ad placement during the video.
            POSTROLL (3):
                Target ad placement after the video ends.
            PREROLL (4):
                Target ad placement before the video starts.
        """

        VIDEO_POSITION_UNSPECIFIED = 0
        ALL = 1
        MIDROLL = 2
        POSTROLL = 3
        PREROLL = 4


__all__ = tuple(sorted(__protobuf__.manifest))
