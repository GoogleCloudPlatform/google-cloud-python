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
    package="google.cloud.workloadidentity.v1",
    manifest={
        "ServiceAgent",
        "GenerateServiceAgentsRequest",
        "GenerateServiceAgentsResponse",
        "OperationMetadata",
    },
)


class ServiceAgent(proto.Message):
    r"""Message describing ServiceAgent object

    Attributes:
        name (str):
            Identifier. The name of the service agent
            resource
        container (str):
            Optional. Name of the container that the service agent is
            associated with. For example:

            - projects/1234
            - folders/1234
            - organizations/2344
        service_producer (str):
            Optional. The service the agent belongs to.
            For example, bigquery.googleapis.com
        principal (str):
            Optional. The principal identifier for the
            service agent. This identifier is used in allow
            policies to grant access to the service agent.
        role (str):
            Optional. The role that should be granted to
            service agent on consumer project, if any. For
            example, "roles/aiplatform.serviceAgent".
        state (google.cloud.workloadidentity_v1.types.ServiceAgent.State):
            Output only. Service agent state.
    """

    class State(proto.Enum):
        r"""Enum for service agent ``state``.

        Values:
            STATE_UNSPECIFIED (0):
                Default service agent ``state``. This value is used if the
                state is omitted.
            ACTIVE (1):
                Indicates that the service agent has been
                created and can be used.
            FAILED (2):
                Indicates that the service agent was not
                created.
        """

        STATE_UNSPECIFIED = 0
        ACTIVE = 1
        FAILED = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    container: str = proto.Field(
        proto.STRING,
        number=5,
    )
    service_producer: str = proto.Field(
        proto.STRING,
        number=6,
    )
    principal: str = proto.Field(
        proto.STRING,
        number=7,
    )
    role: str = proto.Field(
        proto.STRING,
        number=9,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=10,
        enum=State,
    )


class GenerateServiceAgentsRequest(proto.Message):
    r"""Message for creating all ServiceAgents for a ServiceProducer
    in a project and location.

    Attributes:
        parent (str):
            Required. The parent resource. The ``location`` for the
            parent resource must be ``global``.

            Examples:

            - projects/1234/locations/global/serviceProducers/bigquery.googleapis.com
            - folders/2344/locations/global/serviceProducers/vertexai.googleapis.com
            - organizations/3344/locations/global/serviceProducers/iam.googleapis.com
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GenerateServiceAgentsResponse(proto.Message):
    r"""Message for creating all ServiceAgents for a ServiceProducer
    in a project and location.

    Attributes:
        service_agents (MutableSequence[google.cloud.workloadidentity_v1.types.ServiceAgent]):
            The list of service agents
    """

    service_agents: MutableSequence["ServiceAgent"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ServiceAgent",
    )


class OperationMetadata(proto.Message):
    r"""Represents the metadata of the long-running operation.

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation was
            created.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation finished
            running.
        target (str):
            Output only. Server-defined resource path for
            the target of the operation.
        verb (str):
            Output only. Name of the verb executed by the
            operation.
        status_message (str):
            Output only. Human-readable status of the
            operation, if any.
        requested_cancellation (bool):
            Output only. Identifies whether the user has requested
            cancellation of the operation. Operations that have been
            cancelled successfully have
            [google.longrunning.Operation.error][google.longrunning.Operation.error]
            value with a
            [google.rpc.Status.code][google.rpc.Status.code] of ``1``,
            corresponding to ``Code.CANCELLED``.
        api_version (str):
            Output only. API version used to start the
            operation.
    """

    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    target: str = proto.Field(
        proto.STRING,
        number=3,
    )
    verb: str = proto.Field(
        proto.STRING,
        number=4,
    )
    status_message: str = proto.Field(
        proto.STRING,
        number=5,
    )
    requested_cancellation: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    api_version: str = proto.Field(
        proto.STRING,
        number=7,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
