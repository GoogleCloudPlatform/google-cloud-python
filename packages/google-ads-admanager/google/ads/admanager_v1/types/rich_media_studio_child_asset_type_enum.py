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
        "RichMediaStudioChildAssetTypeEnum",
    },
)


class RichMediaStudioChildAssetTypeEnum(proto.Message):
    r"""Wrapper message for
    [RichMediaStudioChildAssetType][google.ads.admanager.v1.RichMediaStudioChildAssetTypeEnum.RichMediaStudioChildAssetType]

    """

    class RichMediaStudioChildAssetType(proto.Enum):
        r"""Type of RichMediaStudioChildAssetProperty

        Values:
            RICH_MEDIA_STUDIO_CHILD_ASSET_TYPE_UNSPECIFIED (0):
                Default value. This value is unused.
            DATA (1):
                The rest of the supported file types .txt,
                .xml, etc.
            FLASH (2):
                SWF files
            IMAGE (3):
                Image files
            VIDEO (4):
                FLVS and any other video file types
        """

        RICH_MEDIA_STUDIO_CHILD_ASSET_TYPE_UNSPECIFIED = 0
        DATA = 1
        FLASH = 2
        IMAGE = 3
        VIDEO = 4


__all__ = tuple(sorted(__protobuf__.manifest))
