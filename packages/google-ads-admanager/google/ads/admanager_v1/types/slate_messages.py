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

import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

from google.ads.admanager_v1.types import (
    live_stream_event_enums,
    video_transcode_status_enum,
)

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "Slate",
    },
)


class Slate(proto.Message):
    r"""A Slate encapsulates all the information necessary to
    represent a Slate entity, the video creative used by Dynamic Ad
    Insertion to fill vacant ad slots.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the ``Slate``. Format:
            ``networks/{network_code}/slates/{slate_id}``
        display_name (str):
            Required. The display name of the Slate. It
            has a maximum length of 255 characters.

            This field is a member of `oneof`_ ``_display_name``.
        status (google.ads.admanager_v1.types.SlateStatusEnum.SlateStatus):
            Output only. The status of this Slate. Slates are created in
            the
            [SlateStatusEnum.SlateStatus.ACTIVE][google.ads.admanager.v1.SlateStatusEnum.SlateStatus.ACTIVE]
            state.

            This field is a member of `oneof`_ ``_status``.
        transcode_status (google.ads.admanager_v1.types.VideoTranscodeStatusEnum.VideoTranscodeStatus):
            Output only. Server side transcoding status
            of the current slate.

            This field is a member of `oneof`_ ``_transcode_status``.
        video_source_url (str):
            Optional. The location of the original asset
            if publisher provided and slate is externally
            hosted.

            This field is a member of `oneof`_ ``_video_source_url``.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The date and time this slate was
            last modified.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    status: live_stream_event_enums.SlateStatusEnum.SlateStatus = proto.Field(
        proto.ENUM,
        number=3,
        optional=True,
        enum=live_stream_event_enums.SlateStatusEnum.SlateStatus,
    )
    transcode_status: video_transcode_status_enum.VideoTranscodeStatusEnum.VideoTranscodeStatus = proto.Field(
        proto.ENUM,
        number=4,
        optional=True,
        enum=video_transcode_status_enum.VideoTranscodeStatusEnum.VideoTranscodeStatus,
    )
    video_source_url: str = proto.Field(
        proto.STRING,
        number=5,
        optional=True,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
