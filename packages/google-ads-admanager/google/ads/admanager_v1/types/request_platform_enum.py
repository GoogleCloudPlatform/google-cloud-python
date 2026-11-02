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
        "RequestPlatformEnum",
    },
)


class RequestPlatformEnum(proto.Message):
    r"""Wrapper message for
    [RequestPlatform][google.ads.admanager.v1.RequestPlatformEnum.RequestPlatform].

    Describes the platform from which a request is made and on which the
    ad is rendered. In the event of multiple platforms, the platform
    that ultimately renders the ad is the targeted platform. For
    example, a video player on a website would have a request platform
    of ``VIDEO_PLAYER``.

    """

    class RequestPlatform(proto.Enum):
        r"""The different environments in which an ad can be shown.

        Values:
            REQUEST_PLATFORM_UNSPECIFIED (0):
                No value specified
            BROWSER (1):
                Represents a request made from a web browser
                (incl. desktop browsers, mobile browsers,
                webviews, etc.).
            MOBILE_APP (2):
                Represents a request made from a Mobile
                Application.
            VIDEO_PLAYER (3):
                Represents a request made from a video
                player.
        """

        REQUEST_PLATFORM_UNSPECIFIED = 0
        BROWSER = 1
        MOBILE_APP = 2
        VIDEO_PLAYER = 3


__all__ = tuple(sorted(__protobuf__.manifest))
