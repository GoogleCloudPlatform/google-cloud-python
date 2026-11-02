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
    package="google.cloud.securitycenter.v2",
    manifest={
        "DataFlowEvent",
    },
)


class DataFlowEvent(proto.Message):
    r"""Details about a data flow event, in which either the data is
    moved to or is accessed from a non-compliant geo-location, as
    defined in the applicable data security policy.

    Attributes:
        event_id (str):
            Unique identifier for data flow event.
        principal_email (str):
            The email address of the principal that
            initiated the data flow event. The principal
            could be a user account, service account, Google
            group, or other.
        operation (google.cloud.securitycenter_v2.types.DataFlowEvent.Operation):
            The operation performed by the principal for
            the data flow event.
        violated_location (str):
            Non-compliant location of the principal or
            the data destination.
        event_time (google.protobuf.timestamp_pb2.Timestamp):
            Timestamp of data flow event.
    """

    class Operation(proto.Enum):
        r"""The operation of a data flow event.

        Values:
            OPERATION_UNSPECIFIED (0):
                The operation is unspecified.
            READ (1):
                Represents a read operation.
            MOVE (2):
                Represents a move operation.
            COPY (3):
                Represents a copy operation.
        """

        OPERATION_UNSPECIFIED = 0
        READ = 1
        MOVE = 2
        COPY = 3

    event_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    principal_email: str = proto.Field(
        proto.STRING,
        number=2,
    )
    operation: Operation = proto.Field(
        proto.ENUM,
        number=3,
        enum=Operation,
    )
    violated_location: str = proto.Field(
        proto.STRING,
        number=4,
    )
    event_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
