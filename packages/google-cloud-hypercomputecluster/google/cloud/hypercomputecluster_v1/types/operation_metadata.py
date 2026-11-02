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
    package="google.cloud.hypercomputecluster.v1",
    manifest={
        "OperationMetadata",
        "OperationProgress",
        "OperationStep",
        "CreateNetwork",
        "CreatePrivateServiceAccess",
        "CreateFilestoreInstance",
        "CreateStorageBucket",
        "CreateLustreInstance",
        "CreateOrchestrator",
        "CreateNodeset",
        "CreatePartition",
        "CreateLoginNode",
        "CheckClusterHealth",
        "UpdateOrchestrator",
        "UpdateNodeset",
        "UpdatePartition",
        "UpdateLoginNode",
        "DeleteOrchestrator",
        "DeleteNodeset",
        "DeletePartition",
        "DeleteLoginNode",
        "DeleteFilestoreInstance",
        "DeleteStorageBucket",
        "DeleteLustreInstance",
        "DeletePrivateServiceAccess",
        "DeleteNetwork",
    },
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
        progress (google.cloud.hypercomputecluster_v1.types.OperationProgress):
            Output only. Progress of the operation.
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
    requested_cancellation: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    api_version: str = proto.Field(
        proto.STRING,
        number=6,
    )
    progress: "OperationProgress" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="OperationProgress",
    )


class OperationProgress(proto.Message):
    r"""Message describing the progress of a cluster mutation
    long-running operation.

    Attributes:
        steps (MutableSequence[google.cloud.hypercomputecluster_v1.types.OperationStep]):
            Output only. Steps and status of the
            operation.
    """

    steps: MutableSequence["OperationStep"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="OperationStep",
    )


class OperationStep(proto.Message):
    r"""Message describing the status of a single step in a cluster
    mutation long-running operation.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        create_network (google.cloud.hypercomputecluster_v1.types.CreateNetwork):
            Output only. If set, indicates that new
            network creation is part of the operation.

            This field is a member of `oneof`_ ``type``.
        create_private_service_access (google.cloud.hypercomputecluster_v1.types.CreatePrivateServiceAccess):
            Output only. If set, indicates that new
            private service access creation is part of the
            operation.

            This field is a member of `oneof`_ ``type``.
        create_filestore_instance (google.cloud.hypercomputecluster_v1.types.CreateFilestoreInstance):
            Output only. If set, indicates that new
            Filestore instance creation is part of the
            operation.

            This field is a member of `oneof`_ ``type``.
        create_storage_bucket (google.cloud.hypercomputecluster_v1.types.CreateStorageBucket):
            Output only. If set, indicates that new Cloud
            Storage bucket creation is part of the
            operation.

            This field is a member of `oneof`_ ``type``.
        create_lustre_instance (google.cloud.hypercomputecluster_v1.types.CreateLustreInstance):
            Output only. If set, indicates that new
            Lustre instance creation is part of the
            operation.

            This field is a member of `oneof`_ ``type``.
        create_orchestrator (google.cloud.hypercomputecluster_v1.types.CreateOrchestrator):
            Output only. If set, indicates that
            orchestrator creation is part of the operation.

            This field is a member of `oneof`_ ``type``.
        create_nodeset (google.cloud.hypercomputecluster_v1.types.CreateNodeset):
            Output only. If set, indicates that new
            nodeset creation is part of the operation.

            This field is a member of `oneof`_ ``type``.
        create_partition (google.cloud.hypercomputecluster_v1.types.CreatePartition):
            Output only. If set, indicates that new
            partition creation is part of the operation.

            This field is a member of `oneof`_ ``type``.
        create_login_node (google.cloud.hypercomputecluster_v1.types.CreateLoginNode):
            Output only. If set, indicates that new login
            node creation is part of the operation.

            This field is a member of `oneof`_ ``type``.
        check_cluster_health (google.cloud.hypercomputecluster_v1.types.CheckClusterHealth):
            Output only. If set, indicates that cluster
            health check is part of the operation.

            This field is a member of `oneof`_ ``type``.
        update_orchestrator (google.cloud.hypercomputecluster_v1.types.UpdateOrchestrator):
            Output only. If set, indicates that an
            orchestrator update is part of the operation.

            This field is a member of `oneof`_ ``type``.
        update_nodeset (google.cloud.hypercomputecluster_v1.types.UpdateNodeset):
            Output only. If set, indicates that nodeset
            update is part of the operation.

            This field is a member of `oneof`_ ``type``.
        update_partition (google.cloud.hypercomputecluster_v1.types.UpdatePartition):
            Output only. If set, indicates that partition
            update is part of the operation.

            This field is a member of `oneof`_ ``type``.
        update_login_node (google.cloud.hypercomputecluster_v1.types.UpdateLoginNode):
            Output only. If set, indicates that login
            node update is part of the operation.

            This field is a member of `oneof`_ ``type``.
        delete_orchestrator (google.cloud.hypercomputecluster_v1.types.DeleteOrchestrator):
            Output only. If set, indicates that
            orchestrator deletion is part of the operation.

            This field is a member of `oneof`_ ``type``.
        delete_nodeset (google.cloud.hypercomputecluster_v1.types.DeleteNodeset):
            Output only. If set, indicates that nodeset
            deletion is part of the operation.

            This field is a member of `oneof`_ ``type``.
        delete_partition (google.cloud.hypercomputecluster_v1.types.DeletePartition):
            Output only. If set, indicates that partition
            deletion is part of the operation.

            This field is a member of `oneof`_ ``type``.
        delete_login_node (google.cloud.hypercomputecluster_v1.types.DeleteLoginNode):
            Output only. If set, indicates that login
            node deletion is part of the operation.

            This field is a member of `oneof`_ ``type``.
        delete_filestore_instance (google.cloud.hypercomputecluster_v1.types.DeleteFilestoreInstance):
            Output only. If set, indicates that Filestore
            instance deletion is part of the operation.

            This field is a member of `oneof`_ ``type``.
        delete_storage_bucket (google.cloud.hypercomputecluster_v1.types.DeleteStorageBucket):
            Output only. If set, indicates that Cloud
            Storage bucket deletion is part of the
            operation.

            This field is a member of `oneof`_ ``type``.
        delete_lustre_instance (google.cloud.hypercomputecluster_v1.types.DeleteLustreInstance):
            Output only. If set, indicates that Lustre
            instance deletion is part of the operation.

            This field is a member of `oneof`_ ``type``.
        delete_private_service_access (google.cloud.hypercomputecluster_v1.types.DeletePrivateServiceAccess):
            Output only. If set, indicates that private
            service access deletion is part of the
            operation.

            This field is a member of `oneof`_ ``type``.
        delete_network (google.cloud.hypercomputecluster_v1.types.DeleteNetwork):
            Output only. If set, indicates that network
            deletion is part of the operation.

            This field is a member of `oneof`_ ``type``.
        state (google.cloud.hypercomputecluster_v1.types.OperationStep.State):
            Output only. State of the operation step.
    """

    class State(proto.Enum):
        r"""State of the operation step.

        Values:
            STATE_UNSPECIFIED (0):
                Unspecified state.
            WAITING (1):
                Initial state before step execution starts.
            IN_PROGRESS (2):
                Step execution is running in progress.
            DONE (3):
                Step execution is completed.
        """

        STATE_UNSPECIFIED = 0
        WAITING = 1
        IN_PROGRESS = 2
        DONE = 3

    create_network: "CreateNetwork" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="type",
        message="CreateNetwork",
    )
    create_private_service_access: "CreatePrivateServiceAccess" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="type",
        message="CreatePrivateServiceAccess",
    )
    create_filestore_instance: "CreateFilestoreInstance" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="type",
        message="CreateFilestoreInstance",
    )
    create_storage_bucket: "CreateStorageBucket" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="type",
        message="CreateStorageBucket",
    )
    create_lustre_instance: "CreateLustreInstance" = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="type",
        message="CreateLustreInstance",
    )
    create_orchestrator: "CreateOrchestrator" = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="type",
        message="CreateOrchestrator",
    )
    create_nodeset: "CreateNodeset" = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="type",
        message="CreateNodeset",
    )
    create_partition: "CreatePartition" = proto.Field(
        proto.MESSAGE,
        number=10,
        oneof="type",
        message="CreatePartition",
    )
    create_login_node: "CreateLoginNode" = proto.Field(
        proto.MESSAGE,
        number=11,
        oneof="type",
        message="CreateLoginNode",
    )
    check_cluster_health: "CheckClusterHealth" = proto.Field(
        proto.MESSAGE,
        number=12,
        oneof="type",
        message="CheckClusterHealth",
    )
    update_orchestrator: "UpdateOrchestrator" = proto.Field(
        proto.MESSAGE,
        number=13,
        oneof="type",
        message="UpdateOrchestrator",
    )
    update_nodeset: "UpdateNodeset" = proto.Field(
        proto.MESSAGE,
        number=14,
        oneof="type",
        message="UpdateNodeset",
    )
    update_partition: "UpdatePartition" = proto.Field(
        proto.MESSAGE,
        number=15,
        oneof="type",
        message="UpdatePartition",
    )
    update_login_node: "UpdateLoginNode" = proto.Field(
        proto.MESSAGE,
        number=16,
        oneof="type",
        message="UpdateLoginNode",
    )
    delete_orchestrator: "DeleteOrchestrator" = proto.Field(
        proto.MESSAGE,
        number=18,
        oneof="type",
        message="DeleteOrchestrator",
    )
    delete_nodeset: "DeleteNodeset" = proto.Field(
        proto.MESSAGE,
        number=19,
        oneof="type",
        message="DeleteNodeset",
    )
    delete_partition: "DeletePartition" = proto.Field(
        proto.MESSAGE,
        number=20,
        oneof="type",
        message="DeletePartition",
    )
    delete_login_node: "DeleteLoginNode" = proto.Field(
        proto.MESSAGE,
        number=21,
        oneof="type",
        message="DeleteLoginNode",
    )
    delete_filestore_instance: "DeleteFilestoreInstance" = proto.Field(
        proto.MESSAGE,
        number=22,
        oneof="type",
        message="DeleteFilestoreInstance",
    )
    delete_storage_bucket: "DeleteStorageBucket" = proto.Field(
        proto.MESSAGE,
        number=23,
        oneof="type",
        message="DeleteStorageBucket",
    )
    delete_lustre_instance: "DeleteLustreInstance" = proto.Field(
        proto.MESSAGE,
        number=24,
        oneof="type",
        message="DeleteLustreInstance",
    )
    delete_private_service_access: "DeletePrivateServiceAccess" = proto.Field(
        proto.MESSAGE,
        number=25,
        oneof="type",
        message="DeletePrivateServiceAccess",
    )
    delete_network: "DeleteNetwork" = proto.Field(
        proto.MESSAGE,
        number=26,
        oneof="type",
        message="DeleteNetwork",
    )
    state: State = proto.Field(
        proto.ENUM,
        number=1,
        enum=State,
    )


class CreateNetwork(proto.Message):
    r"""When set in OperationStep, indicates that a new network
    should be created.

    Attributes:
        network (str):
            Output only. Name of the network to create, in the format
            ``projects/{project}/global/networks/{network}``.
    """

    network: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreatePrivateServiceAccess(proto.Message):
    r"""When set in OperationStep, indicates that a new private
    service access should be created.

    """


class CreateFilestoreInstance(proto.Message):
    r"""When set in OperationStep, indicates that a new filestore
    instance should be created.

    Attributes:
        filestore (str):
            Output only. Name of the Filestore instance, in the format
            ``projects/{project}/locations/{location}/instances/{instance}``
    """

    filestore: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateStorageBucket(proto.Message):
    r"""When set in OperationStep, indicates that a new storage
    bucket should be created.

    Attributes:
        bucket (str):
            Output only. Name of the bucket.
    """

    bucket: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateLustreInstance(proto.Message):
    r"""When set in OperationStep, indicates that a new lustre
    instance should be created.

    Attributes:
        lustre (str):
            Output only. Name of the Managed Lustre instance, in the
            format
            ``projects/{project}/locations/{location}/instances/{instance}``
    """

    lustre: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateOrchestrator(proto.Message):
    r"""When set in OperationStep, indicates that an orchestrator
    should be created.

    """


class CreateNodeset(proto.Message):
    r"""When set in OperationStep, indicates that a nodeset should be
    created.

    Attributes:
        nodesets (MutableSequence[str]):
            Output only. Name of the nodeset to create
    """

    nodesets: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class CreatePartition(proto.Message):
    r"""When set in OperationStep, indicates that a partition should
    be created.

    Attributes:
        partitions (MutableSequence[str]):
            Output only. Name of the partition to create
    """

    partitions: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class CreateLoginNode(proto.Message):
    r"""When set in OperationStep, indicates that a login node should
    be created.

    """


class CheckClusterHealth(proto.Message):
    r"""When set in OperationStep, indicates that cluster health
    check should be performed.

    """


class UpdateOrchestrator(proto.Message):
    r"""When set in OperationStep, indicates that an orchestrator
    should be updated.

    """


class UpdateNodeset(proto.Message):
    r"""When set in OperationStep, indicates that a nodeset should be
    updated.

    Attributes:
        nodesets (MutableSequence[str]):
            Output only. Name of the nodeset to update
    """

    nodesets: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class UpdatePartition(proto.Message):
    r"""When set in OperationStep, indicates that a partition should
    be updated.

    Attributes:
        partitions (MutableSequence[str]):
            Output only. Name of the partition to update
    """

    partitions: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class UpdateLoginNode(proto.Message):
    r"""When set in OperationStep, indicates that a login node should
    be updated.

    """


class DeleteOrchestrator(proto.Message):
    r"""When set in OperationStep, indicates that an orchestrator
    should be deleted.

    """


class DeleteNodeset(proto.Message):
    r"""When set in OperationStep, indicates that a nodeset should be
    deleted.

    Attributes:
        nodesets (MutableSequence[str]):
            Output only. Name of the nodeset to delete
    """

    nodesets: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class DeletePartition(proto.Message):
    r"""When set in OperationStep, indicates that a partition should
    be deleted.

    Attributes:
        partitions (MutableSequence[str]):
            Output only. Name of the partition to delete
    """

    partitions: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class DeleteLoginNode(proto.Message):
    r"""When set in OperationStep, indicates that a login node should
    be deleted.

    """


class DeleteFilestoreInstance(proto.Message):
    r"""When set in OperationStep, indicates that a Filestore
    instance should be deleted.

    Attributes:
        filestore (str):
            Output only. Name of the Filestore instance, in the format
            ``projects/{project}/locations/{location}/instances/{instance}``
    """

    filestore: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteStorageBucket(proto.Message):
    r"""When set in OperationStep, indicates that Cloud Storage
    bucket should be deleted.

    Attributes:
        bucket (str):
            Output only. Name of the bucket.
    """

    bucket: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteLustreInstance(proto.Message):
    r"""When set in OperationStep, indicates that a Lustre instance
    should be deleted.

    Attributes:
        lustre (str):
            Output only. Name of the Managed Lustre instance, in the
            format
            ``projects/{project}/locations/{location}/instances/{instance}``
    """

    lustre: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeletePrivateServiceAccess(proto.Message):
    r"""When set in OperationStep, indicates private service access
    deletion step.

    """


class DeleteNetwork(proto.Message):
    r"""When set in OperationStep, indicates network deletion step
    with the resource name.

    Attributes:
        network (str):
            Output only. Name of the network to delete, in the format
            ``projects/{project}/global/networks/{network}``.
    """

    network: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
