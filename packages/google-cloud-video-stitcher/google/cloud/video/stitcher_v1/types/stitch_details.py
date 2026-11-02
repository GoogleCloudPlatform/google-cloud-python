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
import google.protobuf.struct_pb2 as struct_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.video.stitcher.v1",
    manifest={
        "VodStitchDetail",
        "AdStitchDetail",
    },
)


class VodStitchDetail(proto.Message):
    r"""Information related to the interstitial of a VOD session.
    This resource is only available for VOD sessions that do not
    implement Google Ad Manager ad insertion.

    Attributes:
        name (str):
            The name of the stitch detail in the specified VOD session,
            in the form of
            ``projects/{project}/locations/{location}/vodSessions/{vod_session_id}/vodStitchDetails/{id}``.
        ad_stitch_details (MutableSequence[google.cloud.video.stitcher_v1.types.AdStitchDetail]):
            A list of ad processing details for the
            fetched ad playlist.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    ad_stitch_details: MutableSequence["AdStitchDetail"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="AdStitchDetail",
    )


class AdStitchDetail(proto.Message):
    r"""Metadata for a stitched ad.

    Attributes:
        ad_break_id (str):
            Required. The ad break ID of the processed
            ad.
        ad_id (str):
            Required. The ad ID of the processed ad.
        ad_time_offset (google.protobuf.duration_pb2.Duration):
            Required. The time offset of the processed
            ad.
        skip_reason (str):
            Optional. Indicates the reason why the ad has
            been skipped.
        media (MutableMapping[str, google.protobuf.struct_pb2.Value]):
            Optional. The metadata of the chosen media
            file for the ad.
    """

    ad_break_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    ad_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    ad_time_offset: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=3,
        message=duration_pb2.Duration,
    )
    skip_reason: str = proto.Field(
        proto.STRING,
        number=4,
    )
    media: MutableMapping[str, struct_pb2.Value] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=5,
        message=struct_pb2.Value,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
