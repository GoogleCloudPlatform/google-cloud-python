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
        "SizeTypeEnum",
    },
)


class SizeTypeEnum(proto.Message):
    r"""Wrapper message for
    [SizeType][google.ads.admanager.v1.SizeTypeEnum.SizeType].

    """

    class SizeType(proto.Enum):
        r"""The different Size types for an ad.

        Values:
            SIZE_TYPE_UNSPECIFIED (0):
                Default value. This value is unused.
            PIXEL (1):
                Dimension based size, an actual height and
                width in pixels.
            ASPECT_RATIO (2):
                Size is expressed as a ratio. For example,
                4:1 could be met by a 100 x 25 sized image.
            INTERSTITIAL (3):
                Out-of-page (Interstitial) size that is not
                related to the slot it is served. This must be
                used with 1x1 size.
            IGNORED (4):
                Size is ignored. This must be used with 1x1
                size.
            NATIVE (5):
                Native size, which is a function of the how
                the client renders the creative. This must be
                used with 1x1 size.
            FLUID (6):
                Fluid size. Automatically sizes the ad by
                filling the width of the enclosing column and
                adjusting the height as appropriate. This must
                be used with 1x1 size.
            AUDIO (7):
                Audio size. Used with audio ads. This must be
                used with 1x1 size.
        """

        SIZE_TYPE_UNSPECIFIED = 0
        PIXEL = 1
        ASPECT_RATIO = 2
        INTERSTITIAL = 3
        IGNORED = 4
        NATIVE = 5
        FLUID = 6
        AUDIO = 7


__all__ = tuple(sorted(__protobuf__.manifest))
