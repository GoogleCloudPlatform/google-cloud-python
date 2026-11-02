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

import google.protobuf.struct_pb2 as struct_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.agentregistry_v1.types import properties

__protobuf__ = proto.module(
    package="google.cloud.agentregistry.v1",
    manifest={
        "Endpoint",
    },
)


class Endpoint(proto.Message):
    r"""Represents an Endpoint.

    Attributes:
        name (str):
            Identifier. The resource name of the Endpoint. Format:
            ``projects/{project}/locations/{location}/endpoints/{endpoint}``.
        endpoint_id (str):
            Output only. A stable, globally unique
            identifier for Endpoint.
        display_name (str):
            Output only. Display name for the Endpoint.
        description (str):
            Output only. Description of an Endpoint.
        interfaces (MutableSequence[google.cloud.agentregistry_v1.types.Interface]):
            Required. The connection details for the
            Endpoint.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Create time.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Update time.
        attributes (MutableMapping[str, google.protobuf.struct_pb2.Struct]):
            Output only. Attributes of the Endpoint.

            Valid values:

            - ``agentregistry.googleapis.com/system/RuntimeReference``:
              {"uri": "//..."} - the URI of the underlying resource
              hosting the Endpoint, for example, the GKE Deployment.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    endpoint_id: str = proto.Field(
        proto.STRING,
        number=8,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    interfaces: MutableSequence[properties.Interface] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=properties.Interface,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    attributes: MutableMapping[str, struct_pb2.Struct] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=7,
        message=struct_pb2.Struct,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
