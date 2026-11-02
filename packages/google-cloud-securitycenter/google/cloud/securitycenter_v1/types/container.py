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

from google.cloud.securitycenter_v1.types import label

__protobuf__ = proto.module(
    package="google.cloud.securitycenter.v1",
    manifest={
        "Container",
    },
)


class Container(proto.Message):
    r"""Container associated with the finding.

    Attributes:
        name (str):
            Name of the container.
        uri (str):
            Container image URI provided when configuring
            a pod or container. This string can identify a
            container image version using mutable tags.
        image_id (str):
            Optional container image ID, if provided by
            the container runtime. Uniquely identifies the
            container image launched using a container image
            digest.
        labels (MutableSequence[google.cloud.securitycenter_v1.types.Label]):
            Container labels, as provided by the
            container runtime.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            The time that the container was created.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    image_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    labels: MutableSequence[label.Label] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=label.Label,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
