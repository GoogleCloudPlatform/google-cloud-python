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
    package="google.cloud.dataproc.v1",
    manifest={
        "BatchOperationMetadata",
        "SessionOperationMetadata",
        "ClusterOperationStatus",
        "ClusterOperationMetadata",
        "NodeGroupOperationMetadata",
    },
)


class BatchOperationMetadata(proto.Message):
    r"""Metadata describing the Batch operation.

    Attributes:
        batch (str):
            Name of the batch for the operation.
        batch_uuid (str):
            Batch UUID for the operation.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            The time when the operation was created.
        done_time (google.protobuf.timestamp_pb2.Timestamp):
            The time when the operation finished.
        operation_type (google.cloud.dataproc_v1.types.BatchOperationMetadata.BatchOperationType):
            The operation type.
        description (str):
            Short description of the operation.
        labels (MutableMapping[str, str]):
            Labels associated with the operation.
        warnings (MutableSequence[str]):
            Warnings encountered during operation
            execution.
    """

    class BatchOperationType(proto.Enum):
        r"""Operation type for Batch resources

        Values:
            BATCH_OPERATION_TYPE_UNSPECIFIED (0):
                Batch operation type is unknown.
            BATCH (1):
                Batch operation type.
        """

        BATCH_OPERATION_TYPE_UNSPECIFIED = 0
        BATCH = 1

    batch: str = proto.Field(
        proto.STRING,
        number=1,
    )
    batch_uuid: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    done_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    operation_type: BatchOperationType = proto.Field(
        proto.ENUM,
        number=6,
        enum=BatchOperationType,
    )
    description: str = proto.Field(
        proto.STRING,
        number=7,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=8,
    )
    warnings: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=9,
    )


class SessionOperationMetadata(proto.Message):
    r"""Metadata describing the Session operation.

    Attributes:
        session (str):
            Name of the session for the operation.
        session_uuid (str):
            Session UUID for the operation.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            The time when the operation was created.
        done_time (google.protobuf.timestamp_pb2.Timestamp):
            The time when the operation was finished.
        operation_type (google.cloud.dataproc_v1.types.SessionOperationMetadata.SessionOperationType):
            The operation type.
        description (str):
            Short description of the operation.
        labels (MutableMapping[str, str]):
            Labels associated with the operation.
        warnings (MutableSequence[str]):
            Warnings encountered during operation
            execution.
    """

    class SessionOperationType(proto.Enum):
        r"""Operation type for Session resources

        Values:
            SESSION_OPERATION_TYPE_UNSPECIFIED (0):
                Session operation type is unknown.
            CREATE (1):
                Create Session operation type.
            TERMINATE (2):
                Terminate Session operation type.
            DELETE (3):
                Delete Session operation type.
        """

        SESSION_OPERATION_TYPE_UNSPECIFIED = 0
        CREATE = 1
        TERMINATE = 2
        DELETE = 3

    session: str = proto.Field(
        proto.STRING,
        number=1,
    )
    session_uuid: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    done_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    operation_type: SessionOperationType = proto.Field(
        proto.ENUM,
        number=6,
        enum=SessionOperationType,
    )
    description: str = proto.Field(
        proto.STRING,
        number=7,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=8,
    )
    warnings: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=9,
    )


class ClusterOperationStatus(proto.Message):
    r"""The status of the operation.

    Attributes:
        state (google.cloud.dataproc_v1.types.ClusterOperationStatus.State):
            Output only. A message containing the
            operation state.
        inner_state (str):
            Output only. A message containing the
            detailed operation state.
        details (str):
            Output only. A message containing any
            operation metadata details.
        state_start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time this state was entered.
    """

    class State(proto.Enum):
        r"""The operation state.

        Values:
            UNKNOWN (0):
                Unused.
            PENDING (1):
                The operation has been created.
            RUNNING (2):
                The operation is running.
            DONE (3):
                The operation is done; either cancelled or
                completed.
        """

        UNKNOWN = 0
        PENDING = 1
        RUNNING = 2
        DONE = 3

    state: State = proto.Field(
        proto.ENUM,
        number=1,
        enum=State,
    )
    inner_state: str = proto.Field(
        proto.STRING,
        number=2,
    )
    details: str = proto.Field(
        proto.STRING,
        number=3,
    )
    state_start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )


class ClusterOperationMetadata(proto.Message):
    r"""Metadata describing the operation.

    Attributes:
        cluster_name (str):
            Output only. Name of the cluster for the
            operation.
        cluster_uuid (str):
            Output only. Cluster UUID for the operation.
        status (google.cloud.dataproc_v1.types.ClusterOperationStatus):
            Output only. Current operation status.
        status_history (MutableSequence[google.cloud.dataproc_v1.types.ClusterOperationStatus]):
            Output only. The previous operation status.
        operation_type (str):
            Output only. The operation type.
        description (str):
            Output only. Short description of operation.
        labels (MutableMapping[str, str]):
            Output only. Labels associated with the
            operation
        warnings (MutableSequence[str]):
            Output only. Errors encountered during
            operation execution.
        child_operation_ids (MutableSequence[str]):
            Output only. Child operation ids
    """

    cluster_name: str = proto.Field(
        proto.STRING,
        number=7,
    )
    cluster_uuid: str = proto.Field(
        proto.STRING,
        number=8,
    )
    status: "ClusterOperationStatus" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="ClusterOperationStatus",
    )
    status_history: MutableSequence["ClusterOperationStatus"] = proto.RepeatedField(
        proto.MESSAGE,
        number=10,
        message="ClusterOperationStatus",
    )
    operation_type: str = proto.Field(
        proto.STRING,
        number=11,
    )
    description: str = proto.Field(
        proto.STRING,
        number=12,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=13,
    )
    warnings: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=14,
    )
    child_operation_ids: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=15,
    )


class NodeGroupOperationMetadata(proto.Message):
    r"""Metadata describing the node group operation.

    Attributes:
        node_group_id (str):
            Output only. Node group ID for the operation.
        cluster_uuid (str):
            Output only. Cluster UUID associated with the
            node group operation.
        status (google.cloud.dataproc_v1.types.ClusterOperationStatus):
            Output only. Current operation status.
        status_history (MutableSequence[google.cloud.dataproc_v1.types.ClusterOperationStatus]):
            Output only. The previous operation status.
        operation_type (google.cloud.dataproc_v1.types.NodeGroupOperationMetadata.NodeGroupOperationType):
            The operation type.
        description (str):
            Output only. Short description of operation.
        labels (MutableMapping[str, str]):
            Output only. Labels associated with the
            operation.
        warnings (MutableSequence[str]):
            Output only. Errors encountered during
            operation execution.
    """

    class NodeGroupOperationType(proto.Enum):
        r"""Operation type for node group resources.

        Values:
            NODE_GROUP_OPERATION_TYPE_UNSPECIFIED (0):
                Node group operation type is unknown.
            CREATE (1):
                Create node group operation type.
            UPDATE (2):
                Update node group operation type.
            DELETE (3):
                Delete node group operation type.
            RESIZE (4):
                Resize node group operation type.
        """

        NODE_GROUP_OPERATION_TYPE_UNSPECIFIED = 0
        CREATE = 1
        UPDATE = 2
        DELETE = 3
        RESIZE = 4

    node_group_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    cluster_uuid: str = proto.Field(
        proto.STRING,
        number=2,
    )
    status: "ClusterOperationStatus" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="ClusterOperationStatus",
    )
    status_history: MutableSequence["ClusterOperationStatus"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="ClusterOperationStatus",
    )
    operation_type: NodeGroupOperationType = proto.Field(
        proto.ENUM,
        number=5,
        enum=NodeGroupOperationType,
    )
    description: str = proto.Field(
        proto.STRING,
        number=6,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=7,
    )
    warnings: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=8,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
