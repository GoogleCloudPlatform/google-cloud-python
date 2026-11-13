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

import google.protobuf.any_pb2 as any_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.beyondcorp.appconnectors.v1",
    manifest={
        "HealthStatus",
        "ResourceInfo",
        "ContainerHealthDetails",
        "RemoteAgentDetails",
    },
)


class HealthStatus(proto.Enum):
    r"""HealthStatus represents the health status.

    Values:
        HEALTH_STATUS_UNSPECIFIED (0):
            Health status is unknown: not initialized or
            failed to retrieve.
        HEALTHY (1):
            The resource is healthy.
        UNHEALTHY (2):
            The resource is unhealthy.
        UNRESPONSIVE (3):
            The resource is unresponsive.
        DEGRADED (4):
            Some sub-resources are UNHEALTHY.
    """

    HEALTH_STATUS_UNSPECIFIED = 0
    HEALTHY = 1
    UNHEALTHY = 2
    UNRESPONSIVE = 3
    DEGRADED = 4


class ResourceInfo(proto.Message):
    r"""ResourceInfo represents the information or status of an app
    connector resource component that's used to report on various parts
    of the system. For example, ResourceInfo can be used to convey the
    status of a remote_agent, including the status of an appgateway for
    an runtime environment in a container instance.

    Attributes:
        id (str):
            Required. Unique Id for the resource.
        status (google.cloud.beyondcorp_appconnectors_v1.types.HealthStatus):
            Overall health status. Overall status is
            derived based on the status of each sub level
            resources.
        resource (google.protobuf.any_pb2.Any):
            Specific details for the resource. This is
            for internal use only.
        time (google.protobuf.timestamp_pb2.Timestamp):
            The timestamp to collect the info. It is
            suggested to be set by the topmost level
            resource only.
        sub (MutableSequence[google.cloud.beyondcorp_appconnectors_v1.types.ResourceInfo]):
            List of Info for the sub level resources.
    """

    id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    status: "HealthStatus" = proto.Field(
        proto.ENUM,
        number=2,
        enum="HealthStatus",
    )
    resource: any_pb2.Any = proto.Field(
        proto.MESSAGE,
        number=3,
        message=any_pb2.Any,
    )
    time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    sub: MutableSequence["ResourceInfo"] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message="ResourceInfo",
    )


class ContainerHealthDetails(proto.Message):
    r"""ContainerHealthDetails reflects the health details of a
    container.

    Attributes:
        expected_config_version (str):
            The version of the expected config.
        current_config_version (str):
            The version of the current config.
        extended_status (MutableMapping[str, str]):
            The extended status. Such as ExitCode,
            StartedAt, FinishedAt, etc.
        error_msg (str):
            The latest error message.
    """

    expected_config_version: str = proto.Field(
        proto.STRING,
        number=1,
    )
    current_config_version: str = proto.Field(
        proto.STRING,
        number=2,
    )
    extended_status: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=3,
    )
    error_msg: str = proto.Field(
        proto.STRING,
        number=4,
    )


class RemoteAgentDetails(proto.Message):
    r"""RemoteAgentDetails reflects the details of a remote agent."""


__all__ = tuple(sorted(__protobuf__.manifest))
