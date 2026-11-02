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

from google.cloud.securitycenter_v1.types import resource, valued_resource

__protobuf__ = proto.module(
    package="google.cloud.securitycenter.v1",
    manifest={
        "Simulation",
    },
)


class Simulation(proto.Message):
    r"""Attack path simulation

    Attributes:
        name (str):
            Full resource name of the Simulation:
            ``organizations/123/simulations/456``
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time simulation was created
        resource_value_configs_metadata (MutableSequence[google.cloud.securitycenter_v1.types.ResourceValueConfigMetadata]):
            Resource value configurations' metadata used
            in this simulation. Maximum of 100.
        cloud_provider (google.cloud.securitycenter_v1.types.CloudProvider):
            Indicates which cloud provider was used in
            this simulation.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    resource_value_configs_metadata: MutableSequence[
        valued_resource.ResourceValueConfigMetadata
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=valued_resource.ResourceValueConfigMetadata,
    )
    cloud_provider: resource.CloudProvider = proto.Field(
        proto.ENUM,
        number=4,
        enum=resource.CloudProvider,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
