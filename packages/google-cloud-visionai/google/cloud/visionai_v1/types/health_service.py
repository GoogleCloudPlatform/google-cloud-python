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

__protobuf__ = proto.module(
    package="google.cloud.visionai.v1",
    manifest={
        "HealthCheckRequest",
        "HealthCheckResponse",
        "ClusterInfo",
    },
)


class HealthCheckRequest(proto.Message):
    r"""HealthCheckRequest is the request message for Check.

    Attributes:
        cluster (str):
            The parent of the resource.
    """

    cluster: str = proto.Field(
        proto.STRING,
        number=1,
    )


class HealthCheckResponse(proto.Message):
    r"""HealthCheckResponse is the response message for Check.

    Attributes:
        healthy (bool):
            Indicates whether the cluster is in healthy
            state or not.
        reason (str):
            Reason of why the cluster is in unhealthy
            state.
        cluster_info (google.cloud.visionai_v1.types.ClusterInfo):
            Other information of the cluster client may
            be interested.
    """

    healthy: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    reason: str = proto.Field(
        proto.STRING,
        number=2,
    )
    cluster_info: "ClusterInfo" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="ClusterInfo",
    )


class ClusterInfo(proto.Message):
    r"""

    Attributes:
        streams_count (int):
            The number of active streams in the cluster.
        processes_count (int):
            The number of active processes in the
            cluster.
    """

    streams_count: int = proto.Field(
        proto.INT32,
        number=1,
    )
    processes_count: int = proto.Field(
        proto.INT32,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
