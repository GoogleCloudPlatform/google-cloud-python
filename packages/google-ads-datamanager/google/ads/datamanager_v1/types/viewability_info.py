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

import google.protobuf.duration_pb2 as duration_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.ads.datamanager.v1",
    manifest={
        "ViewType",
        "MediaQuartile",
        "ViewabilityInfo",
    },
)


class ViewType(proto.Enum):
    r"""The type of the event.

    Values:
        VIEW_TYPE_UNSPECIFIED (0):
            Unspecified view type.
        VIEW_TYPE_MRC_VIEWED (1):
            MRC viewed.
        VIEW_TYPE_MRC_RENDERED (2):
            MRC rendered.
    """

    VIEW_TYPE_UNSPECIFIED = 0
    VIEW_TYPE_MRC_VIEWED = 1
    VIEW_TYPE_MRC_RENDERED = 2


class MediaQuartile(proto.Enum):
    r"""The amount of the media that was played as discrete
    quartiles.

    Values:
        MEDIA_QUARTILE_UNSPECIFIED (0):
            Unspecified media quartile.
        MEDIA_QUARTILE_START (1):
            Start.
        MEDIA_QUARTILE_FIRST_QUARTILE (2):
            First quartile.
        MEDIA_QUARTILE_MIDPOINT (3):
            Midpoint.
        MEDIA_QUARTILE_THIRD_QUARTILE (4):
            Third quartile.
        MEDIA_QUARTILE_COMPLETE (5):
            Complete.
    """

    MEDIA_QUARTILE_UNSPECIFIED = 0
    MEDIA_QUARTILE_START = 1
    MEDIA_QUARTILE_FIRST_QUARTILE = 2
    MEDIA_QUARTILE_MIDPOINT = 3
    MEDIA_QUARTILE_THIRD_QUARTILE = 4
    MEDIA_QUARTILE_COMPLETE = 5


class ViewabilityInfo(proto.Message):
    r"""Details of the viewability of the ad served.

    Attributes:
        view_type (google.ads.datamanager_v1.types.ViewType):
            Required. The type of the event.
        viewable_percent (int):
            Optional. The numerical percent (0-100) of
            the pixels that were viewable.
        viewable_duration (google.protobuf.duration_pb2.Duration):
            Optional. The amount of time the ad was
            viewable for.
        media_skippable (bool):
            Optional. Whether the ad media was skippable
            or not.
        media_quartile (google.ads.datamanager_v1.types.MediaQuartile):
            Optional. The amount of the media that was
            played as discrete quartiles.
        media_duration (google.protobuf.duration_pb2.Duration):
            Optional. The duration of the ad media.
        media_volume_percent (int):
            Optional. The numerical percent (0-100) of
            the volume of the media playback.
        playback_duration (google.protobuf.duration_pb2.Duration):
            Optional. The duration of playback of the ad
            media, regardless of whether it was viewable or
            not.
    """

    view_type: "ViewType" = proto.Field(
        proto.ENUM,
        number=1,
        enum="ViewType",
    )
    viewable_percent: int = proto.Field(
        proto.INT32,
        number=2,
    )
    viewable_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=3,
        message=duration_pb2.Duration,
    )
    media_skippable: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    media_quartile: "MediaQuartile" = proto.Field(
        proto.ENUM,
        number=5,
        enum="MediaQuartile",
    )
    media_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=6,
        message=duration_pb2.Duration,
    )
    media_volume_percent: int = proto.Field(
        proto.INT32,
        number=7,
    )
    playback_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=8,
        message=duration_pb2.Duration,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
