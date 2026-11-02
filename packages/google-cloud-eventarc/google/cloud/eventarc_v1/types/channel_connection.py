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

__protobuf__ = proto.module(
    package="google.cloud.eventarc.v1",
    manifest={
        "ChannelConnection",
    },
)


class ChannelConnection(proto.Message):
    r"""A representation of the ChannelConnection resource.
    A ChannelConnection is a resource which event providers create
    during the activation process to establish a connection between
    the provider and the subscriber channel.

    Attributes:
        name (str):
            Required. The name of the connection.
        uid (str):
            Output only. Server assigned ID of the
            resource. The server guarantees uniqueness and
            immutability until deleted.
        channel (str):
            Required. The name of the connected subscriber Channel. This
            is a weak reference to avoid cross project and cross
            accounts references. This must be in
            ``projects/{project}/location/{location}/channels/{channel_id}``
            format.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The creation time.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last-modified time.
        activation_token (str):
            Input only. Activation token for the channel.
            The token will be used during the creation of
            ChannelConnection to bind the channel with the
            provider project. This field will not be stored
            in the provider resource.
        labels (MutableMapping[str, str]):
            Optional. Resource labels.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=2,
    )
    channel: str = proto.Field(
        proto.STRING,
        number=5,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    activation_token: str = proto.Field(
        proto.STRING,
        number=8,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=9,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
