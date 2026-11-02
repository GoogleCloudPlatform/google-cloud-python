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
    package="google.cloud.cloudcontrolspartner.v1",
    manifest={
        "EkmConnections",
        "GetEkmConnectionsRequest",
        "EkmConnection",
    },
)


class EkmConnections(proto.Message):
    r"""The EKM connections associated with a workload

    Attributes:
        name (str):
            Identifier. Format:
            ``organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}/ekmConnections``
        ekm_connections (MutableSequence[google.cloud.cloudcontrolspartner_v1.types.EkmConnection]):
            The EKM connections associated with the
            workload
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    ekm_connections: MutableSequence["EkmConnection"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="EkmConnection",
    )


class GetEkmConnectionsRequest(proto.Message):
    r"""Request for getting the EKM connections associated with a
    workload

    Attributes:
        name (str):
            Required. Format:
            ``organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}/ekmConnections``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class EkmConnection(proto.Message):
    r"""Details about the EKM connection

    Attributes:
        connection_name (str):
            Resource name of the EKM connection in the format:
            projects/{project}/locations/{location}/ekmConnections/{ekm_connection}
        connection_state (google.cloud.cloudcontrolspartner_v1.types.EkmConnection.ConnectionState):
            Output only. The connection state
        connection_error (google.cloud.cloudcontrolspartner_v1.types.EkmConnection.ConnectionError):
            The connection error that occurred if any
    """

    class ConnectionState(proto.Enum):
        r"""The EKM connection state.

        Values:
            CONNECTION_STATE_UNSPECIFIED (0):
                Unspecified EKM connection state
            AVAILABLE (1):
                Available EKM connection state
            NOT_AVAILABLE (2):
                Not available EKM connection state
            ERROR (3):
                Error EKM connection state
            PERMISSION_DENIED (4):
                Permission denied EKM connection state
        """

        CONNECTION_STATE_UNSPECIFIED = 0
        AVAILABLE = 1
        NOT_AVAILABLE = 2
        ERROR = 3
        PERMISSION_DENIED = 4

    class ConnectionError(proto.Message):
        r"""Information around the error that occurred if the connection
        state is anything other than available or unspecified

        Attributes:
            error_domain (str):
                The error domain for the error
            error_message (str):
                The error message for the error
        """

        error_domain: str = proto.Field(
            proto.STRING,
            number=1,
        )
        error_message: str = proto.Field(
            proto.STRING,
            number=2,
        )

    connection_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    connection_state: ConnectionState = proto.Field(
        proto.ENUM,
        number=2,
        enum=ConnectionState,
    )
    connection_error: ConnectionError = proto.Field(
        proto.MESSAGE,
        number=3,
        message=ConnectionError,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
