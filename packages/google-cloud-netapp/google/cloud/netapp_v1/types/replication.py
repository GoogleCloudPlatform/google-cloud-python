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

import google.protobuf.duration_pb2 as duration_pb2  # type: ignore
import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.netapp_v1.types import common, volume

__protobuf__ = proto.module(
    package="google.cloud.netapp.v1",
    manifest={
        "TransferStats",
        "Replication",
        "HybridPeeringDetails",
        "ListReplicationsRequest",
        "ListReplicationsResponse",
        "GetReplicationRequest",
        "DestinationVolumeParameters",
        "CreateReplicationRequest",
        "DeleteReplicationRequest",
        "UpdateReplicationRequest",
        "StopReplicationRequest",
        "ResumeReplicationRequest",
        "ReverseReplicationDirectionRequest",
        "EstablishPeeringRequest",
        "SyncReplicationRequest",
    },
)


class TransferStats(proto.Message):
    r"""TransferStats reports all statistics related to replication
    transfer.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        transfer_bytes (int):
            Cumulative bytes transferred so far for the
            replication relationship.

            This field is a member of `oneof`_ ``_transfer_bytes``.
        total_transfer_duration (google.protobuf.duration_pb2.Duration):
            Cumulative time taken across all transfers
            for the replication relationship.

            This field is a member of `oneof`_ ``_total_transfer_duration``.
        last_transfer_bytes (int):
            Last transfer size in bytes.

            This field is a member of `oneof`_ ``_last_transfer_bytes``.
        last_transfer_duration (google.protobuf.duration_pb2.Duration):
            Time taken during last transfer.

            This field is a member of `oneof`_ ``_last_transfer_duration``.
        lag_duration (google.protobuf.duration_pb2.Duration):
            Lag duration indicates the duration by which
            Destination region volume content lags behind
            the primary region volume content.

            This field is a member of `oneof`_ ``_lag_duration``.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Time when progress was updated last.

            This field is a member of `oneof`_ ``_update_time``.
        last_transfer_end_time (google.protobuf.timestamp_pb2.Timestamp):
            Time when last transfer completed.

            This field is a member of `oneof`_ ``_last_transfer_end_time``.
        last_transfer_error (str):
            A message describing the cause of the last
            transfer failure.

            This field is a member of `oneof`_ ``_last_transfer_error``.
    """

    transfer_bytes: int = proto.Field(
        proto.INT64,
        number=1,
        optional=True,
    )
    total_transfer_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=2,
        optional=True,
        message=duration_pb2.Duration,
    )
    last_transfer_bytes: int = proto.Field(
        proto.INT64,
        number=3,
        optional=True,
    )
    last_transfer_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=4,
        optional=True,
        message=duration_pb2.Duration,
    )
    lag_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=5,
        optional=True,
        message=duration_pb2.Duration,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        optional=True,
        message=timestamp_pb2.Timestamp,
    )
    last_transfer_end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        optional=True,
        message=timestamp_pb2.Timestamp,
    )
    last_transfer_error: str = proto.Field(
        proto.STRING,
        number=8,
        optional=True,
    )


class Replication(proto.Message):
    r"""Replication is a nested resource under Volume, that describes
    a cross-region replication relationship between 2 volumes in
    different regions.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the Replication. Format:
            ``projects/{project_id}/locations/{location}/volumes/{volume_id}/replications/{replication_id}``.
        state (google.cloud.netapp_v1.types.Replication.State):
            Output only. State of the replication.
        state_details (str):
            Output only. State details of the
            replication.
        role (google.cloud.netapp_v1.types.Replication.ReplicationRole):
            Output only. Indicates whether this points to
            source or destination.
        replication_schedule (google.cloud.netapp_v1.types.Replication.ReplicationSchedule):
            Required. Indicates the schedule for
            replication.
        mirror_state (google.cloud.netapp_v1.types.Replication.MirrorState):
            Output only. Indicates the state of
            mirroring.
        healthy (bool):
            Output only. Condition of the relationship.
            Can be one of the following:

            - true: The replication relationship is healthy.
              It has not missed the most recent scheduled
              transfer.
            - false: The replication relationship is not
              healthy. It has missed the most recent
              scheduled transfer.

            This field is a member of `oneof`_ ``_healthy``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Replication create time.
        destination_volume (str):
            Output only. Full name of destination volume resource.
            Example :
            "projects/{project}/locations/{location}/volumes/{volume_id}".
        transfer_stats (google.cloud.netapp_v1.types.TransferStats):
            Output only. Replication transfer statistics.
        labels (MutableMapping[str, str]):
            Resource labels to represent user provided
            metadata.
        description (str):
            A description about this replication
            relationship.

            This field is a member of `oneof`_ ``_description``.
        destination_volume_parameters (google.cloud.netapp_v1.types.DestinationVolumeParameters):
            Required. Input only. Destination volume
            parameters
        source_volume (str):
            Output only. Full name of source volume resource. Example :
            "projects/{project}/locations/{location}/volumes/{volume_id}".
        hybrid_peering_details (google.cloud.netapp_v1.types.HybridPeeringDetails):
            Output only. Hybrid peering details.
        cluster_location (str):
            Optional. Location of the user cluster.
        hybrid_replication_type (google.cloud.netapp_v1.types.Replication.HybridReplicationType):
            Output only. Type of the hybrid replication.
        hybrid_replication_user_commands (google.cloud.netapp_v1.types.UserCommands):
            Output only. Copy pastable snapmirror
            commands to be executed on onprem cluster by the
            customer.
    """

    class State(proto.Enum):
        r"""The replication states
        New enum values may be added in future to indicate possible new
        states.

        Values:
            STATE_UNSPECIFIED (0):
                Unspecified replication State
            CREATING (1):
                Replication is creating.
            READY (2):
                Replication is ready.
            UPDATING (3):
                Replication is updating.
            DELETING (5):
                Replication is deleting.
            ERROR (6):
                Replication is in error state.
            PENDING_CLUSTER_PEERING (8):
                Replication is waiting for cluster peering to
                be established.
            PENDING_SVM_PEERING (9):
                Replication is waiting for SVM peering to be
                established.
            PENDING_REMOTE_RESYNC (10):
                Replication is waiting for Commands to be
                executed on Onprem ONTAP.
            EXTERNALLY_MANAGED_REPLICATION (11):
                Onprem ONTAP is destination and Replication
                can only be managed from Onprem.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        READY = 2
        UPDATING = 3
        DELETING = 5
        ERROR = 6
        PENDING_CLUSTER_PEERING = 8
        PENDING_SVM_PEERING = 9
        PENDING_REMOTE_RESYNC = 10
        EXTERNALLY_MANAGED_REPLICATION = 11

    class ReplicationRole(proto.Enum):
        r"""New enum values may be added in future to support different
        replication topology.

        Values:
            REPLICATION_ROLE_UNSPECIFIED (0):
                Unspecified replication role
            SOURCE (1):
                Indicates Source volume.
            DESTINATION (2):
                Indicates Destination volume.
        """

        REPLICATION_ROLE_UNSPECIFIED = 0
        SOURCE = 1
        DESTINATION = 2

    class ReplicationSchedule(proto.Enum):
        r"""Schedule for Replication.
        New enum values may be added in future to support different
        frequency of replication.

        Values:
            REPLICATION_SCHEDULE_UNSPECIFIED (0):
                Unspecified ReplicationSchedule
            EVERY_10_MINUTES (1):
                Replication happens once every 10 minutes.
            HOURLY (2):
                Replication happens once every hour.
            DAILY (3):
                Replication happens once every day.
        """

        REPLICATION_SCHEDULE_UNSPECIFIED = 0
        EVERY_10_MINUTES = 1
        HOURLY = 2
        DAILY = 3

    class MirrorState(proto.Enum):
        r"""Mirroring states.
        No new value is expected to be added in future.

        Values:
            MIRROR_STATE_UNSPECIFIED (0):
                Unspecified MirrorState
            PREPARING (1):
                Destination volume is being prepared.
            MIRRORED (2):
                Destination volume has been initialized and
                is ready to receive replication transfers.
            STOPPED (3):
                Destination volume is not receiving
                replication transfers.
            TRANSFERRING (4):
                Incremental replication is in progress.
            BASELINE_TRANSFERRING (5):
                Baseline replication is in progress.
            ABORTED (6):
                Replication is aborted.
            EXTERNALLY_MANAGED (7):
                Replication is being managed from Onprem
                ONTAP.
            PENDING_PEERING (8):
                Peering is yet to be established.
        """

        MIRROR_STATE_UNSPECIFIED = 0
        PREPARING = 1
        MIRRORED = 2
        STOPPED = 3
        TRANSFERRING = 4
        BASELINE_TRANSFERRING = 5
        ABORTED = 6
        EXTERNALLY_MANAGED = 7
        PENDING_PEERING = 8

    class HybridReplicationType(proto.Enum):
        r"""Hybrid replication type.

        Values:
            HYBRID_REPLICATION_TYPE_UNSPECIFIED (0):
                Unspecified hybrid replication type.
            MIGRATION (1):
                Hybrid replication type for migration.
            CONTINUOUS_REPLICATION (2):
                Hybrid replication type for continuous
                replication.
            ONPREM_REPLICATION (3):
                New field for reversible OnPrem replication,
                to be used for data protection.
            REVERSE_ONPREM_REPLICATION (4):
                Hybrid replication type for incremental
                Transfer in the reverse direction (GCNV is
                source and Onprem is destination)
        """

        HYBRID_REPLICATION_TYPE_UNSPECIFIED = 0
        MIGRATION = 1
        CONTINUOUS_REPLICATION = 2
        ONPREM_REPLICATION = 3
        REVERSE_ONPREM_REPLICATION = 4

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=2,
        enum=State,
    )
    state_details: str = proto.Field(
        proto.STRING,
        number=3,
    )
    role: ReplicationRole = proto.Field(
        proto.ENUM,
        number=4,
        enum=ReplicationRole,
    )
    replication_schedule: ReplicationSchedule = proto.Field(
        proto.ENUM,
        number=5,
        enum=ReplicationSchedule,
    )
    mirror_state: MirrorState = proto.Field(
        proto.ENUM,
        number=6,
        enum=MirrorState,
    )
    healthy: bool = proto.Field(
        proto.BOOL,
        number=8,
        optional=True,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    destination_volume: str = proto.Field(
        proto.STRING,
        number=10,
    )
    transfer_stats: "TransferStats" = proto.Field(
        proto.MESSAGE,
        number=11,
        message="TransferStats",
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=12,
    )
    description: str = proto.Field(
        proto.STRING,
        number=13,
        optional=True,
    )
    destination_volume_parameters: "DestinationVolumeParameters" = proto.Field(
        proto.MESSAGE,
        number=14,
        message="DestinationVolumeParameters",
    )
    source_volume: str = proto.Field(
        proto.STRING,
        number=15,
    )
    hybrid_peering_details: "HybridPeeringDetails" = proto.Field(
        proto.MESSAGE,
        number=16,
        message="HybridPeeringDetails",
    )
    cluster_location: str = proto.Field(
        proto.STRING,
        number=18,
    )
    hybrid_replication_type: HybridReplicationType = proto.Field(
        proto.ENUM,
        number=19,
        enum=HybridReplicationType,
    )
    hybrid_replication_user_commands: common.UserCommands = proto.Field(
        proto.MESSAGE,
        number=20,
        message=common.UserCommands,
    )


class HybridPeeringDetails(proto.Message):
    r"""HybridPeeringDetails contains details about the hybrid
    peering.

    Attributes:
        subnet_ip (str):
            Output only. IP address of the subnet.
        command (str):
            Output only. Copy-paste-able commands to be
            used on user's ONTAP to accept peering requests.
        command_expiry_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Expiration time for the peering
            command to be executed on user's ONTAP.
        passphrase (str):
            Output only. Temporary passphrase generated
            to accept cluster peering command.
        peer_volume_name (str):
            Output only. Name of the user's local source
            volume to be peered with the destination volume.
        peer_cluster_name (str):
            Output only. Name of the user's local source
            cluster to be peered with the destination
            cluster.
        peer_svm_name (str):
            Output only. Name of the user's local source
            vserver svm to be peered with the destination
            vserver svm.
    """

    subnet_ip: str = proto.Field(
        proto.STRING,
        number=1,
    )
    command: str = proto.Field(
        proto.STRING,
        number=2,
    )
    command_expiry_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    passphrase: str = proto.Field(
        proto.STRING,
        number=4,
    )
    peer_volume_name: str = proto.Field(
        proto.STRING,
        number=5,
    )
    peer_cluster_name: str = proto.Field(
        proto.STRING,
        number=6,
    )
    peer_svm_name: str = proto.Field(
        proto.STRING,
        number=7,
    )


class ListReplicationsRequest(proto.Message):
    r"""ListReplications lists replications.

    Attributes:
        parent (str):
            Required. The volume for which to retrieve replication
            information, in the format
            ``projects/{project_id}/locations/{location}/volumes/{volume_id}``.
        page_size (int):
            The maximum number of items to return.
        page_token (str):
            The next_page_token value to use if there are additional
            results to retrieve for this list request.
        order_by (str):
            Sort results. Supported values are "name",
            "name desc" or "" (unsorted).
        filter (str):
            List filter.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=4,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListReplicationsResponse(proto.Message):
    r"""ListReplicationsResponse is the result of
    ListReplicationsRequest.

    Attributes:
        replications (MutableSequence[google.cloud.netapp_v1.types.Replication]):
            A list of replications in the project for the
            specified volume.
        next_page_token (str):
            The token you can use to retrieve the next
            page of results. Not returned if there are no
            more results in the list.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    replications: MutableSequence["Replication"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Replication",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetReplicationRequest(proto.Message):
    r"""GetReplicationRequest gets the state of a replication.

    Attributes:
        name (str):
            Required. The replication resource name, in the format
            ``projects/{project_id}/locations/{location}/volumes/{volume_id}/replications/{replication_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DestinationVolumeParameters(proto.Message):
    r"""DestinationVolumeParameters specify input parameters used for
    creating destination volume.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        storage_pool (str):
            Required. Existing destination StoragePool
            name.
        volume_id (str):
            Desired destination volume resource id. If
            not specified, source volume's resource id will
            be used. This value must start with a lowercase
            letter followed by up to 62 lowercase letters,
            numbers, or hyphens, and cannot end with a
            hyphen.
        share_name (str):
            Destination volume's share name. If not
            specified, source volume's share name will be
            used.
        description (str):
            Description for the destination volume.

            This field is a member of `oneof`_ ``_description``.
        tiering_policy (google.cloud.netapp_v1.types.TieringPolicy):
            Optional. Tiering policy for the volume.

            This field is a member of `oneof`_ ``_tiering_policy``.
    """

    storage_pool: str = proto.Field(
        proto.STRING,
        number=1,
    )
    volume_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    share_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    description: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )
    tiering_policy: volume.TieringPolicy = proto.Field(
        proto.MESSAGE,
        number=5,
        optional=True,
        message=volume.TieringPolicy,
    )


class CreateReplicationRequest(proto.Message):
    r"""CreateReplicationRequest creates a replication.

    Attributes:
        parent (str):
            Required. The NetApp volume to create the replications of,
            in the format
            ``projects/{project_id}/locations/{location}/volumes/{volume_id}``
        replication (google.cloud.netapp_v1.types.Replication):
            Required. A replication resource
        replication_id (str):
            Required. ID of the replication to create.
            Must be unique within the parent resource. Must
            contain only letters, numbers and hyphen, with
            the first character a letter, the last a letter
            or a
            number, and a 63 character maximum.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    replication: "Replication" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Replication",
    )
    replication_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteReplicationRequest(proto.Message):
    r"""DeleteReplicationRequest deletes a replication.

    Attributes:
        name (str):
            Required. The replication resource name, in the format
            ``projects/*/locations/*/volumes/*/replications/{replication_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateReplicationRequest(proto.Message):
    r"""UpdateReplicationRequest updates description and/or labels
    for a replication.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Mask of fields to update.  At least
            one path must be supplied in this field.
        replication (google.cloud.netapp_v1.types.Replication):
            Required. A replication resource
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    replication: "Replication" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Replication",
    )


class StopReplicationRequest(proto.Message):
    r"""StopReplicationRequest stops a replication until resumed.

    Attributes:
        name (str):
            Required. The resource name of the replication, in the
            format of
            projects/{project_id}/locations/{location}/volumes/{volume_id}/replications/{replication_id}.
        force (bool):
            Indicates whether to stop replication
            forcefully while data transfer is in progress.
            Warning! if force is true, this will abort any
            current transfers and can lead to data loss due
            to partial transfer. If force is false, stop
            replication will fail while data transfer is in
            progress and you will need to retry later.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class ResumeReplicationRequest(proto.Message):
    r"""ResumeReplicationRequest resumes a stopped replication.

    Attributes:
        name (str):
            Required. The resource name of the replication, in the
            format of
            projects/{project_id}/locations/{location}/volumes/{volume_id}/replications/{replication_id}.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ReverseReplicationDirectionRequest(proto.Message):
    r"""ReverseReplicationDirectionRequest reverses direction of
    replication. Source becomes destination and destination becomes
    source.

    Attributes:
        name (str):
            Required. The resource name of the replication, in the
            format of
            projects/{project_id}/locations/{location}/volumes/{volume_id}/replications/{replication_id}.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class EstablishPeeringRequest(proto.Message):
    r"""EstablishPeeringRequest establishes cluster and svm peerings
    between the source and the destination replications.

    Attributes:
        name (str):
            Required. The resource name of the replication, in the
            format of
            projects/{project_id}/locations/{location}/volumes/{volume_id}/replications/{replication_id}.
        peer_cluster_name (str):
            Required. Name of the user's local source
            cluster to be peered with the destination
            cluster.
        peer_svm_name (str):
            Required. Name of the user's local source
            vserver svm to be peered with the destination
            vserver svm.
        peer_ip_addresses (MutableSequence[str]):
            Optional. List of IPv4 ip addresses to be
            used for peering.
        peer_volume_name (str):
            Required. Name of the user's local source
            volume to be peered with the destination volume.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    peer_cluster_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    peer_svm_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    peer_ip_addresses: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    peer_volume_name: str = proto.Field(
        proto.STRING,
        number=5,
    )


class SyncReplicationRequest(proto.Message):
    r"""SyncReplicationRequest syncs the replication from source to
    destination.

    Attributes:
        name (str):
            Required. The resource name of the replication, in the
            format of
            projects/{project_id}/locations/{location}/volumes/{volume_id}/replications/{replication_id}.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
