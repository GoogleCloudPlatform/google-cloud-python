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
        "VideoTranscodeStatusEnum",
    },
)


class VideoTranscodeStatusEnum(proto.Message):
    r"""Wrapper message for
    [VideoTranscodeStatus][google.ads.admanager.v1.VideoTranscodeStatusEnum.VideoTranscodeStatus]

    """

    class VideoTranscodeStatus(proto.Enum):
        r"""Possible server side transcoding states.

        Values:
            VIDEO_TRANSCODE_STATUS_UNSPECIFIED (0):
                Default value. This value is unused.
            COMPLETED (1):
                The video transcoding is complete.
            FAILED (2):
                The video transcoding failed.
            IN_PROGRESS (3):
                The video transcode is in progress.
            NEEDS_TRANSCODE (4):
                The video needs to be transcoded.
            NOT_READY (5):
                The video is not ready.
        """

        VIDEO_TRANSCODE_STATUS_UNSPECIFIED = 0
        COMPLETED = 1
        FAILED = 2
        IN_PROGRESS = 3
        NEEDS_TRANSCODE = 4
        NOT_READY = 5


__all__ = tuple(sorted(__protobuf__.manifest))
