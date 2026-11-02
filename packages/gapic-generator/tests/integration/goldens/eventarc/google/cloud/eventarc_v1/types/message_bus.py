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

from google.cloud.eventarc_v1.types import logging_config as gce_logging_config
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore


__protobuf__ = proto.module(
    package='google.cloud.eventarc.v1',
    manifest={
        'MessageBus',
    },
)


class MessageBus(proto.Message):
    r"""MessageBus for the messages flowing through the system. The
    admin has visibility and control over the messages being
    published and consumed and can restrict publishers and
    subscribers to only a subset of data available in the system by
    defining authorization policies.

    Attributes:
        name (str):
            Identifier. Resource name of the form
            projects/{project}/locations/{location}/messageBuses/{message_bus}
        uid (str):
            Output only. Server assigned unique
            identifier for the channel. The value is a UUID4
            string and guaranteed to remain unchanged until
            the resource is deleted.
        etag (str):
            Output only. This checksum is computed by the
            server based on the value of other fields, and
            might be sent only on update and delete requests
            to ensure that the client has an up-to-date
            value before proceeding.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The creation time.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last-modified time.
        labels (MutableMapping[str, str]):
            Optional. Resource labels.
        annotations (MutableMapping[str, str]):
            Optional. Resource annotations.
        display_name (str):
            Optional. Resource display name.
        crypto_key_name (str):
            Optional. Resource name of a KMS crypto key (managed by the
            user) used to encrypt/decrypt their event data.

            It must match the pattern
            ``projects/*/locations/*/keyRings/*/cryptoKeys/*``.
        logging_config (google.cloud.eventarc_v1.types.LoggingConfig):
            Optional. Config to control Platform logging
            for the Message Bus. This log configuration is
            applied to the Message Bus itself, and all the
            Enrollments attached to it.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=2,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=3,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=6,
    )
    annotations: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=7,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=8,
    )
    crypto_key_name: str = proto.Field(
        proto.STRING,
        number=10,
    )
    logging_config: gce_logging_config.LoggingConfig = proto.Field(
        proto.MESSAGE,
        number=11,
        message=gce_logging_config.LoggingConfig,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
