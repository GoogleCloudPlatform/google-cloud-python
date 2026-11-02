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
    package="google.cloud.datalabeling.v1beta1",
    manifest={
        "ImagePayload",
        "TextPayload",
        "VideoThumbnail",
        "VideoPayload",
    },
)


class ImagePayload(proto.Message):
    r"""Container of information about an image.

    Attributes:
        mime_type (str):
            Image format.
        image_thumbnail (bytes):
            A byte string of a thumbnail image.
        image_uri (str):
            Image uri from the user bucket.
        signed_uri (str):
            Signed uri of the image file in the service
            bucket.
    """

    mime_type: str = proto.Field(
        proto.STRING,
        number=1,
    )
    image_thumbnail: bytes = proto.Field(
        proto.BYTES,
        number=2,
    )
    image_uri: str = proto.Field(
        proto.STRING,
        number=3,
    )
    signed_uri: str = proto.Field(
        proto.STRING,
        number=4,
    )


class TextPayload(proto.Message):
    r"""Container of information about a piece of text.

    Attributes:
        text_content (str):
            Text content.
    """

    text_content: str = proto.Field(
        proto.STRING,
        number=1,
    )


class VideoThumbnail(proto.Message):
    r"""Container of information of a video thumbnail.

    Attributes:
        thumbnail (bytes):
            A byte string of the video frame.
        time_offset (google.protobuf.duration_pb2.Duration):
            Time offset relative to the beginning of the
            video, corresponding to the video frame where
            the thumbnail has been extracted from.
    """

    thumbnail: bytes = proto.Field(
        proto.BYTES,
        number=1,
    )
    time_offset: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=2,
        message=duration_pb2.Duration,
    )


class VideoPayload(proto.Message):
    r"""Container of information of a video.

    Attributes:
        mime_type (str):
            Video format.
        video_uri (str):
            Video uri from the user bucket.
        video_thumbnails (MutableSequence[google.cloud.datalabeling_v1beta1.types.VideoThumbnail]):
            The list of video thumbnails.
        frame_rate (float):
            FPS of the video.
        signed_uri (str):
            Signed uri of the video file in the service
            bucket.
    """

    mime_type: str = proto.Field(
        proto.STRING,
        number=1,
    )
    video_uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    video_thumbnails: MutableSequence["VideoThumbnail"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="VideoThumbnail",
    )
    frame_rate: float = proto.Field(
        proto.FLOAT,
        number=4,
    )
    signed_uri: str = proto.Field(
        proto.STRING,
        number=5,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
