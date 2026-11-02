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
    package="google.cloud.orchestration.airflow.service.v1",
    manifest={
        "OperationMetadata",
    },
)


class OperationMetadata(proto.Message):
    r"""Metadata describing an operation.

    Attributes:
        state (google.cloud.orchestration.airflow.service_v1.types.OperationMetadata.State):
            Output only. The current operation state.
        operation_type (google.cloud.orchestration.airflow.service_v1.types.OperationMetadata.Type):
            Output only. The type of operation being
            performed.
        resource (str):
            Output only. The resource being operated on, as a `relative
            resource
            name </apis/design/resource_names#relative_resource_name>`__.
        resource_uuid (str):
            Output only. The UUID of the resource being
            operated on.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation was
            submitted to the server.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the operation
            terminated, regardless of its success. This
            field is unset if the operation is still
            ongoing.
    """

    class State(proto.Enum):
        r"""An enum describing the overall state of an operation.

        Values:
            STATE_UNSPECIFIED (0):
                Unused.
            PENDING (1):
                The operation has been created but is not yet
                started.
            RUNNING (2):
                The operation is underway.
            SUCCEEDED (3):
                The operation completed successfully.
            SUCCESSFUL (3):
                No description available.
            FAILED (4):
                The operation is no longer running but did
                not succeed.
        """

        _pb_options = {"allow_alias": True}
        STATE_UNSPECIFIED = 0
        PENDING = 1
        RUNNING = 2
        SUCCEEDED = 3
        SUCCESSFUL = 3
        FAILED = 4

    class Type(proto.Enum):
        r"""Type of longrunning operation.

        Values:
            TYPE_UNSPECIFIED (0):
                Unused.
            CREATE (1):
                A resource creation operation.
            DELETE (2):
                A resource deletion operation.
            UPDATE (3):
                A resource update operation.
            CHECK (4):
                A resource check operation.
            SAVE_SNAPSHOT (5):
                Saves snapshot of the resource operation.
            LOAD_SNAPSHOT (6):
                Loads snapshot of the resource operation.
            DATABASE_FAILOVER (7):
                Triggers failover of environment's Cloud SQL
                instance (only for highly resilient
                environments).
        """

        TYPE_UNSPECIFIED = 0
        CREATE = 1
        DELETE = 2
        UPDATE = 3
        CHECK = 4
        SAVE_SNAPSHOT = 5
        LOAD_SNAPSHOT = 6
        DATABASE_FAILOVER = 7

    state: State = proto.Field(
        proto.ENUM,
        number=1,
        enum=State,
    )
    operation_type: Type = proto.Field(
        proto.ENUM,
        number=2,
        enum=Type,
    )
    resource: str = proto.Field(
        proto.STRING,
        number=3,
    )
    resource_uuid: str = proto.Field(
        proto.STRING,
        number=4,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
