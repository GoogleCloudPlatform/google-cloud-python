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
        "GoogleChannelConfig",
    },
)


class GoogleChannelConfig(proto.Message):
    r"""A GoogleChannelConfig is a resource that stores the custom
    settings respected by Eventarc first-party triggers in the
    matching region. Once configured, first-party event data will be
    protected using the specified custom managed encryption key
    instead of Google-managed encryption keys.

    Attributes:
        name (str):
            Required. The resource name of the config. Must be in the
            format of,
            ``projects/{project}/locations/{location}/googleChannelConfig``.
            In API responses, the config name always includes the
            projectID, regardless of whether the projectID or
            projectNumber was provided.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last-modified time.
        crypto_key_name (str):
            Optional. Resource name of a KMS crypto key (managed by the
            user) used to encrypt/decrypt their event data.

            It must match the pattern
            ``projects/*/locations/*/keyRings/*/cryptoKeys/*``.
        labels (MutableMapping[str, str]):
            Optional. Resource labels.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    crypto_key_name: str = proto.Field(
        proto.STRING,
        number=7,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=8,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
