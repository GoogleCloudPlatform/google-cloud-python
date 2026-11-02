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
        "ContainerTypeEnum",
        "DaiEncodingProfileStatusEnum",
        "DaiEncodingProfileVariantTypeEnum",
    },
)


class ContainerTypeEnum(proto.Message):
    r"""Wrapper message for
    [ContainerType][google.ads.admanager.v1.ContainerTypeEnum.ContainerType]

    """

    class ContainerType(proto.Enum):
        r"""The container type of the DaiEncodingProfile.

        Values:
            CONTAINER_TYPE_UNSPECIFIED (0):
                Not specified value.
            TS (1):
                Transport stream (TS) container.
            FMP4 (2):
                Fragmented MPEG-4 (fMP4) output container.
            HLS_AUDIO (3):
                HTTP live streaming (HLS) packed audio
                container.
        """

        CONTAINER_TYPE_UNSPECIFIED = 0
        TS = 1
        FMP4 = 2
        HLS_AUDIO = 3


class DaiEncodingProfileStatusEnum(proto.Message):
    r"""Wrapper message for
    [DaiEncodingProfileStatus][google.ads.admanager.v1.DaiEncodingProfileStatusEnum.DaiEncodingProfileStatus]

    """

    class DaiEncodingProfileStatus(proto.Enum):
        r"""The status of the DaiEncodingProfile.

        Values:
            DAI_ENCODING_PROFILE_STATUS_UNSPECIFIED (0):
                Not specified value.
            ACTIVE (1):
                Indicates the DaiEncodingProfile has been
                created and is eligible for streaming.
            ARCHIVED (2):
                Indicates the DaiEncodingProfile has been
                archived.
        """

        DAI_ENCODING_PROFILE_STATUS_UNSPECIFIED = 0
        ACTIVE = 1
        ARCHIVED = 2


class DaiEncodingProfileVariantTypeEnum(proto.Message):
    r"""Wrapper message for
    [DaiEncodingProfileVariantType][google.ads.admanager.v1.DaiEncodingProfileVariantTypeEnum.DaiEncodingProfileVariantType]

    """

    class DaiEncodingProfileVariantType(proto.Enum):
        r"""The variant type of the DaiEncodingProfile.

        Values:
            DAI_ENCODING_PROFILE_VARIANT_TYPE_UNSPECIFIED (0):
                Not specified value.
            MEDIA (1):
                Media variant playlist type. Media playlists
                may: contain audio only video only, or audio and
                video.
            IFRAME (2):
                iFrame variant playlist type. iFrame
                playlists may: contain video or contain audio
                and video (i.e. video must be present).
            SUBTITLES (3):
                Subtitles variant playlist type.
        """

        DAI_ENCODING_PROFILE_VARIANT_TYPE_UNSPECIFIED = 0
        MEDIA = 1
        IFRAME = 2
        SUBTITLES = 3


__all__ = tuple(sorted(__protobuf__.manifest))
