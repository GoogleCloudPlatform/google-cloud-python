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
        "LiveAdTagDetail",
        "VodAdTagDetail",
        "AdRequest",
        "RequestMetadata",
        "ResponseMetadata",
    },
)


class LiveAdTagDetail(proto.Message):
    r"""Information related to the details for one ad tag. This
    resource is only available for live sessions that do not
    implement Google Ad Manager ad insertion.

    Attributes:
        name (str):
            The resource name in the form of
            ``projects/{project}/locations/{location}/liveSessions/{live_session}/liveAdTagDetails/{id}``.
        ad_requests (MutableSequence[google.cloud.video.stitcher_v1.types.AdRequest]):
            A list of ad requests.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    ad_requests: MutableSequence["AdRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="AdRequest",
    )


class VodAdTagDetail(proto.Message):
    r"""Information related to the details for one ad tag. This
    resource is only available for VOD sessions that do not
    implement Google Ad Manager ad insertion.

    Attributes:
        name (str):
            The name of the ad tag detail for the specified VOD session,
            in the form of
            ``projects/{project}/locations/{location}/vodSessions/{vod_session_id}/vodAdTagDetails/{id}``.
        ad_requests (MutableSequence[google.cloud.video.stitcher_v1.types.AdRequest]):
            A list of ad requests for one ad tag.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    ad_requests: MutableSequence["AdRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="AdRequest",
    )


class AdRequest(proto.Message):
    r"""Details of an ad request to an ad server.

    Attributes:
        uri (str):
            The ad tag URI processed with integrated
            macros.
        request_metadata (google.cloud.video.stitcher_v1.types.RequestMetadata):
            The request metadata used to make the ad
            request.
        response_metadata (google.cloud.video.stitcher_v1.types.ResponseMetadata):
            The response metadata received from the ad
            request.
    """

    uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_metadata: "RequestMetadata" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="RequestMetadata",
    )
    response_metadata: "ResponseMetadata" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="ResponseMetadata",
    )


class RequestMetadata(proto.Message):
    r"""Metadata for an ad request.

    Attributes:
        headers (google.protobuf.struct_pb2.Struct):
            The HTTP headers of the ad request.
    """

    headers: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=1,
        message=struct_pb2.Struct,
    )


class ResponseMetadata(proto.Message):
    r"""Metadata for the response of an ad request.

    Attributes:
        error (str):
            Error message received when making the ad
            request.
        headers (google.protobuf.struct_pb2.Struct):
            Headers from the response.
        status_code (str):
            Status code for the response.
        size_bytes (int):
            Size in bytes of the response.
        duration (google.protobuf.duration_pb2.Duration):
            Total time elapsed for the response.
        body (str):
            The body of the response.
    """

    error: str = proto.Field(
        proto.STRING,
        number=1,
    )
    headers: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=2,
        message=struct_pb2.Struct,
    )
    status_code: str = proto.Field(
        proto.STRING,
        number=3,
    )
    size_bytes: int = proto.Field(
        proto.INT32,
        number=4,
    )
    duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=5,
        message=duration_pb2.Duration,
    )
    body: str = proto.Field(
        proto.STRING,
        number=6,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
