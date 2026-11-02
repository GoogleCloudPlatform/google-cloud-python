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
import google.rpc.status_pb2 as status_pb2  # type: ignore
import google.type.interval_pb2 as interval_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.tpu.v2alpha1",
    manifest={
        "GuestAttributes",
        "GuestAttributesValue",
        "GuestAttributesEntry",
        "AttachedDisk",
        "SchedulingConfig",
        "NetworkEndpoint",
        "AccessConfig",
        "NetworkConfig",
        "ServiceAccount",
        "Node",
        "QueuedResource",
        "QueuedResourceState",
        "ListNodesRequest",
        "ListNodesResponse",
        "GetNodeRequest",
        "CreateNodeRequest",
        "DeleteNodeRequest",
        "StopNodeRequest",
        "StartNodeRequest",
        "UpdateNodeRequest",
        "ListQueuedResourcesRequest",
        "ListQueuedResourcesResponse",
        "GetQueuedResourceRequest",
        "CreateQueuedResourceRequest",
        "DeleteQueuedResourceRequest",
        "ResetQueuedResourceRequest",
        "ServiceIdentity",
        "GenerateServiceIdentityRequest",
        "GenerateServiceIdentityResponse",
        "AcceleratorType",
        "GetAcceleratorTypeRequest",
        "ListAcceleratorTypesRequest",
        "ListAcceleratorTypesResponse",
        "RuntimeVersion",
        "GetRuntimeVersionRequest",
        "ListRuntimeVersionsRequest",
        "ListRuntimeVersionsResponse",
        "OperationMetadata",
        "Symptom",
        "GetGuestAttributesRequest",
        "GetGuestAttributesResponse",
        "SimulateMaintenanceEventRequest",
        "PerformMaintenanceRequest",
        "PerformMaintenanceQueuedResourceRequest",
        "Reservation",
        "ListReservationsRequest",
        "ListReservationsResponse",
        "AcceleratorConfig",
        "ShieldedInstanceConfig",
        "BootDiskConfig",
        "CustomerEncryptionKey",
        "UpcomingMaintenance",
    },
)


class GuestAttributes(proto.Message):
    r"""A guest attributes.

    Attributes:
        query_path (str):
            The path to be queried. This can be the
            default namespace ('/') or a nested namespace
            ('/\<namespace\>/') or a specified key
            ('/\<namespace\>/\<key\>')
        query_value (google.cloud.tpu_v2alpha1.types.GuestAttributesValue):
            The value of the requested queried path.
    """

    query_path: str = proto.Field(
        proto.STRING,
        number=1,
    )
    query_value: "GuestAttributesValue" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="GuestAttributesValue",
    )


class GuestAttributesValue(proto.Message):
    r"""Array of guest attribute namespace/key/value tuples.

    Attributes:
        items (MutableSequence[google.cloud.tpu_v2alpha1.types.GuestAttributesEntry]):
            The list of guest attributes entries.
    """

    items: MutableSequence["GuestAttributesEntry"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="GuestAttributesEntry",
    )


class GuestAttributesEntry(proto.Message):
    r"""A guest attributes namespace/key/value entry.

    Attributes:
        namespace (str):
            Namespace for the guest attribute entry.
        key (str):
            Key for the guest attribute entry.
        value (str):
            Value for the guest attribute entry.
    """

    namespace: str = proto.Field(
        proto.STRING,
        number=1,
    )
    key: str = proto.Field(
        proto.STRING,
        number=2,
    )
    value: str = proto.Field(
        proto.STRING,
        number=3,
    )


class AttachedDisk(proto.Message):
    r"""A node-attached disk resource.
    Next ID: 8;

    Attributes:
        source_disk (str):
            Specifies the full path to an existing disk.
            For example:
            "projects/my-project/zones/us-central1-c/disks/my-disk".
        mode (google.cloud.tpu_v2alpha1.types.AttachedDisk.DiskMode):
            The mode in which to attach this disk. If not specified, the
            default is READ_WRITE mode. Only applicable to data_disks.
    """

    class DiskMode(proto.Enum):
        r"""The different mode of the attached disk.

        Values:
            DISK_MODE_UNSPECIFIED (0):
                The disk mode is not known/set.
            READ_WRITE (1):
                Attaches the disk in read-write mode. Only
                one TPU node can attach a disk in read-write
                mode at a time.
            READ_ONLY (2):
                Attaches the disk in read-only mode. Multiple
                TPU nodes can attach a disk in read-only mode at
                a time.
        """

        DISK_MODE_UNSPECIFIED = 0
        READ_WRITE = 1
        READ_ONLY = 2

    source_disk: str = proto.Field(
        proto.STRING,
        number=3,
    )
    mode: DiskMode = proto.Field(
        proto.ENUM,
        number=4,
        enum=DiskMode,
    )


class SchedulingConfig(proto.Message):
    r"""Sets the scheduling options for this node.

    Attributes:
        preemptible (bool):
            Defines whether the node is preemptible.
        reserved (bool):
            Whether the node is created under a
            reservation.
        spot (bool):
            Optional. Defines whether the node is Spot
            VM.
    """

    preemptible: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    reserved: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    spot: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class NetworkEndpoint(proto.Message):
    r"""A network endpoint over which a TPU worker can be reached.

    Attributes:
        ip_address (str):
            The internal IP address of this network
            endpoint.
        port (int):
            The port of this network endpoint.
        access_config (google.cloud.tpu_v2alpha1.types.AccessConfig):
            The access config for the TPU worker.
    """

    ip_address: str = proto.Field(
        proto.STRING,
        number=1,
    )
    port: int = proto.Field(
        proto.INT32,
        number=2,
    )
    access_config: "AccessConfig" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="AccessConfig",
    )


class AccessConfig(proto.Message):
    r"""An access config attached to the TPU worker.

    Attributes:
        external_ip (str):
            Output only. An external IP address
            associated with the TPU worker.
    """

    external_ip: str = proto.Field(
        proto.STRING,
        number=1,
    )


class NetworkConfig(proto.Message):
    r"""Network related configurations.

    Attributes:
        network (str):
            The name of the network for the TPU node. It
            must be a preexisting Google Compute Engine
            network. If none is provided, "default" will be
            used.
        subnetwork (str):
            The name of the subnetwork for the TPU node.
            It must be a preexisting Google Compute Engine
            subnetwork. If none is provided, "default" will
            be used.
        enable_external_ips (bool):
            Indicates that external IP addresses would be
            associated with the TPU workers. If set to
            false, the specified subnetwork or network
            should have Private Google Access enabled.
        can_ip_forward (bool):
            Allows the TPU node to send and receive
            packets with non-matching destination or source
            IPs. This is required if you plan to use the TPU
            workers to forward routes.
        queue_count (int):
            Optional. Specifies networking queue count
            for TPU VM instance's network interface.
    """

    network: str = proto.Field(
        proto.STRING,
        number=1,
    )
    subnetwork: str = proto.Field(
        proto.STRING,
        number=2,
    )
    enable_external_ips: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    can_ip_forward: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    queue_count: int = proto.Field(
        proto.INT32,
        number=6,
    )


class ServiceAccount(proto.Message):
    r"""A service account.

    Attributes:
        email (str):
            Email address of the service account. If
            empty, default Compute service account will be
            used.
        scope (MutableSequence[str]):
            The list of scopes to be made available for
            this service account. If empty, access to all
            Cloud APIs will be allowed.
    """

    email: str = proto.Field(
        proto.STRING,
        number=1,
    )
    scope: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class Node(proto.Message):
    r"""A TPU instance.

    Attributes:
        name (str):
            Output only. Immutable. The name of the TPU.
        description (str):
            The user-supplied description of the TPU.
            Maximum of 512 characters.
        accelerator_type (str):
            The type of hardware accelerators associated
            with this node.
        state (google.cloud.tpu_v2alpha1.types.Node.State):
            Output only. The current state for the TPU
            Node.
        health_description (str):
            Output only. If this field is populated, it
            contains a description of why the TPU Node is
            unhealthy.
        runtime_version (str):
            Required. The runtime version running in the
            Node.
        network_config (google.cloud.tpu_v2alpha1.types.NetworkConfig):
            Network configurations for the TPU node. network_config and
            network_configs are mutually exclusive, you can only specify
            one of them. If both are specified, an error will be
            returned.
        network_configs (MutableSequence[google.cloud.tpu_v2alpha1.types.NetworkConfig]):
            Optional. Repeated network configurations for the TPU node.
            This field is used to specify multiple networks configs for
            the TPU node. network_config and network_configs are
            mutually exclusive, you can only specify one of them. If
            both are specified, an error will be returned.
        cidr_block (str):
            The CIDR block that the TPU node will use
            when selecting an IP address. This CIDR block
            must be a /29 block; the Compute Engine networks
            API forbids a smaller block, and using a larger
            block would be wasteful (a node can only consume
            one IP address). Errors will occur if the CIDR
            block has already been used for a currently
            existing TPU node, the CIDR block conflicts with
            any subnetworks in the user's provided network,
            or the provided network is peered with another
            network that is using that CIDR block.
        service_account (google.cloud.tpu_v2alpha1.types.ServiceAccount):
            The Google Cloud Platform Service Account to
            be used by the TPU node VMs. If None is
            specified, the default compute service account
            will be used.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the node was
            created.
        scheduling_config (google.cloud.tpu_v2alpha1.types.SchedulingConfig):
            The scheduling options for this node.
        network_endpoints (MutableSequence[google.cloud.tpu_v2alpha1.types.NetworkEndpoint]):
            Output only. The network endpoints where TPU
            workers can be accessed and sent work. It is
            recommended that runtime clients of the node
            reach out to the 0th entry in this map first.
        health (google.cloud.tpu_v2alpha1.types.Node.Health):
            The health status of the TPU node.
        labels (MutableMapping[str, str]):
            Resource labels to represent user-provided
            metadata.
        metadata (MutableMapping[str, str]):
            Custom metadata to apply to the TPU Node.
            Can set startup-script and shutdown-script
        tags (MutableSequence[str]):
            Tags to apply to the TPU Node. Tags are used
            to identify valid sources or targets for network
            firewalls.
        id (int):
            Output only. The unique identifier for the
            TPU Node.
        data_disks (MutableSequence[google.cloud.tpu_v2alpha1.types.AttachedDisk]):
            The additional data disks for the Node.
        api_version (google.cloud.tpu_v2alpha1.types.Node.ApiVersion):
            Output only. The API version that created
            this Node.
        symptoms (MutableSequence[google.cloud.tpu_v2alpha1.types.Symptom]):
            Output only. The Symptoms that have occurred
            to the TPU Node.
        queued_resource (str):
            Output only. The qualified name of the
            QueuedResource that requested this Node.
        accelerator_config (google.cloud.tpu_v2alpha1.types.AcceleratorConfig):
            The AccleratorConfig for the TPU Node.
        shielded_instance_config (google.cloud.tpu_v2alpha1.types.ShieldedInstanceConfig):
            Shielded Instance options.
        multislice_node (bool):
            Output only. Whether the Node belongs to a
            Multislice group.
        autocheckpoint_enabled (bool):
            Optional. Whether Autocheckpoint is enabled.
        boot_disk_config (google.cloud.tpu_v2alpha1.types.BootDiskConfig):
            Optional. Boot disk configuration.
        upcoming_maintenance (google.cloud.tpu_v2alpha1.types.UpcomingMaintenance):
            Output only. Upcoming maintenance on this TPU
            node.
    """

    class State(proto.Enum):
        r"""Represents the different states of a TPU node during its
        lifecycle.

        Values:
            STATE_UNSPECIFIED (0):
                TPU node state is not known/set.
            CREATING (1):
                TPU node is being created.
            READY (2):
                TPU node has been created.
            RESTARTING (3):
                TPU node is restarting.
            REIMAGING (4):
                TPU node is undergoing reimaging.
            DELETING (5):
                TPU node is being deleted.
            REPAIRING (6):
                TPU node is being repaired and may be unusable. Details can
                be found in the 'help_description' field.
            STOPPED (8):
                TPU node is stopped.
            STOPPING (9):
                TPU node is currently stopping.
            STARTING (10):
                TPU node is currently starting.
            PREEMPTED (11):
                TPU node has been preempted. Only applies to
                Preemptible TPU Nodes.
            TERMINATED (12):
                TPU node has been terminated due to
                maintenance or has reached the end of its life
                cycle (for preemptible nodes).
            HIDING (13):
                TPU node is currently hiding.
            HIDDEN (14):
                TPU node has been hidden.
            UNHIDING (15):
                TPU node is currently unhiding.
            UNKNOWN (16):
                TPU node has unknown state after a failed
                repair.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        READY = 2
        RESTARTING = 3
        REIMAGING = 4
        DELETING = 5
        REPAIRING = 6
        STOPPED = 8
        STOPPING = 9
        STARTING = 10
        PREEMPTED = 11
        TERMINATED = 12
        HIDING = 13
        HIDDEN = 14
        UNHIDING = 15
        UNKNOWN = 16

    class Health(proto.Enum):
        r"""Health defines the status of a TPU node as reported by
        Health Monitor.

        Values:
            HEALTH_UNSPECIFIED (0):
                Health status is unknown: not initialized or
                failed to retrieve.
            HEALTHY (1):
                The resource is healthy.
            TIMEOUT (3):
                The resource is unresponsive.
            UNHEALTHY_TENSORFLOW (4):
                The in-guest ML stack is unhealthy.
            UNHEALTHY_MAINTENANCE (5):
                The node is under maintenance/priority boost
                caused rescheduling and will resume running once
                rescheduled.
        """

        HEALTH_UNSPECIFIED = 0
        HEALTHY = 1
        TIMEOUT = 3
        UNHEALTHY_TENSORFLOW = 4
        UNHEALTHY_MAINTENANCE = 5

    class ApiVersion(proto.Enum):
        r"""TPU API Version.

        Values:
            API_VERSION_UNSPECIFIED (0):
                API version is unknown.
            V1_ALPHA1 (1):
                TPU API V1Alpha1 version.
            V1 (2):
                TPU API V1 version.
            V2_ALPHA1 (3):
                TPU API V2Alpha1 version.
        """

        API_VERSION_UNSPECIFIED = 0
        V1_ALPHA1 = 1
        V1 = 2
        V2_ALPHA1 = 3

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    accelerator_type: str = proto.Field(
        proto.STRING,
        number=5,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=9,
        enum=State,
    )
    health_description: str = proto.Field(
        proto.STRING,
        number=10,
    )
    runtime_version: str = proto.Field(
        proto.STRING,
        number=11,
    )
    network_config: "NetworkConfig" = proto.Field(
        proto.MESSAGE,
        number=36,
        message="NetworkConfig",
    )
    network_configs: MutableSequence["NetworkConfig"] = proto.RepeatedField(
        proto.MESSAGE,
        number=50,
        message="NetworkConfig",
    )
    cidr_block: str = proto.Field(
        proto.STRING,
        number=13,
    )
    service_account: "ServiceAccount" = proto.Field(
        proto.MESSAGE,
        number=37,
        message="ServiceAccount",
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=16,
        message=timestamp_pb2.Timestamp,
    )
    scheduling_config: "SchedulingConfig" = proto.Field(
        proto.MESSAGE,
        number=17,
        message="SchedulingConfig",
    )
    network_endpoints: MutableSequence["NetworkEndpoint"] = proto.RepeatedField(
        proto.MESSAGE,
        number=21,
        message="NetworkEndpoint",
    )
    health: Health = proto.Field(
        proto.ENUM,
        number=22,
        enum=Health,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=24,
    )
    metadata: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=34,
    )
    tags: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=40,
    )
    id: int = proto.Field(
        proto.INT64,
        number=33,
    )
    data_disks: MutableSequence["AttachedDisk"] = proto.RepeatedField(
        proto.MESSAGE,
        number=41,
        message="AttachedDisk",
    )
    api_version: ApiVersion = proto.Field(
        proto.ENUM,
        number=38,
        enum=ApiVersion,
    )
    symptoms: MutableSequence["Symptom"] = proto.RepeatedField(
        proto.MESSAGE,
        number=39,
        message="Symptom",
    )
    queued_resource: str = proto.Field(
        proto.STRING,
        number=43,
    )
    accelerator_config: "AcceleratorConfig" = proto.Field(
        proto.MESSAGE,
        number=44,
        message="AcceleratorConfig",
    )
    shielded_instance_config: "ShieldedInstanceConfig" = proto.Field(
        proto.MESSAGE,
        number=45,
        message="ShieldedInstanceConfig",
    )
    multislice_node: bool = proto.Field(
        proto.BOOL,
        number=47,
    )
    autocheckpoint_enabled: bool = proto.Field(
        proto.BOOL,
        number=48,
    )
    boot_disk_config: "BootDiskConfig" = proto.Field(
        proto.MESSAGE,
        number=49,
        message="BootDiskConfig",
    )
    upcoming_maintenance: "UpcomingMaintenance" = proto.Field(
        proto.MESSAGE,
        number=51,
        message="UpcomingMaintenance",
    )


class QueuedResource(proto.Message):
    r"""A QueuedResource represents a request for resources that will
    be placed in a queue and fulfilled when the necessary resources
    are available.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Output only. Immutable. The name of the
            QueuedResource.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the QueuedResource
            was created.
        tpu (google.cloud.tpu_v2alpha1.types.QueuedResource.Tpu):
            Defines a TPU resource.

            This field is a member of `oneof`_ ``resource``.
        best_effort (google.cloud.tpu_v2alpha1.types.QueuedResource.BestEffort):
            The BestEffort tier.

            This field is a member of `oneof`_ ``tier``.
        guaranteed (google.cloud.tpu_v2alpha1.types.QueuedResource.Guaranteed):
            The Guaranteed tier.

            This field is a member of `oneof`_ ``tier``.
        spot (google.cloud.tpu_v2alpha1.types.QueuedResource.Spot):
            Optional. The Spot tier.

            This field is a member of `oneof`_ ``tier``.
        queueing_policy (google.cloud.tpu_v2alpha1.types.QueuedResource.QueueingPolicy):
            The queueing policy of the QueuedRequest.
        state (google.cloud.tpu_v2alpha1.types.QueuedResourceState):
            Output only. State of the QueuedResource
            request.
        reservation_name (str):
            Name of the reservation in which the resource
            should be provisioned. Format:
            projects/{project}/locations/{zone}/reservations/{reservation}
    """

    class Tpu(proto.Message):
        r"""Details of the TPU resource(s) being requested.

        Attributes:
            node_spec (MutableSequence[google.cloud.tpu_v2alpha1.types.QueuedResource.Tpu.NodeSpec]):
                The TPU node(s) being requested.
        """

        class NodeSpec(proto.Message):
            r"""Details of the TPU node(s) being requested. Users can request
            either a single node or multiple nodes.
            NodeSpec provides the specification for node(s) to be created.

            Attributes:
                parent (str):
                    Required. The parent resource name.
                node_id (str):
                    The unqualified resource name. Should follow the
                    ``^[A-Za-z0-9_.~+%-]+$`` regex format. This is only
                    specified when requesting a single node. In case of
                    multi-node requests, multi_node_params must be populated
                    instead. It's an error to specify both node_id and
                    multi_node_params.
                multi_node_params (google.cloud.tpu_v2alpha1.types.QueuedResource.Tpu.NodeSpec.MultiNodeParams):
                    Optional. Fields to specify in case of
                    multi-node request.
                node (google.cloud.tpu_v2alpha1.types.Node):
                    Required. The node.
            """

            class MultiNodeParams(proto.Message):
                r"""Parameters to specify for multi-node QueuedResource requests. This
                field must be populated in case of multi-node requests instead of
                node_id. It's an error to specify both node_id and
                multi_node_params.

                Attributes:
                    node_count (int):
                        Required. Number of nodes with this spec. The system will
                        attempt to provison "node_count" nodes as part of the
                        request. This needs to be > 1.
                    node_id_prefix (str):
                        Prefix of node_ids in case of multi-node request Should
                        follow the ``^[A-Za-z0-9_.~+%-]+$`` regex format. If
                        node_count = 3 and node_id_prefix = "np", node ids of nodes
                        created will be "np-0", "np-1", "np-2". If this field is not
                        provided we use queued_resource_id as the node_id_prefix.
                    workload_type (google.cloud.tpu_v2alpha1.types.QueuedResource.Tpu.NodeSpec.MultiNodeParams.WorkloadType):
                        Optional. The workload type for the
                        multi-node request.
                """

                class WorkloadType(proto.Enum):
                    r"""The workload type for the multi-node request.

                    Values:
                        WORKLOAD_TYPE_UNSPECIFIED (0):
                            Not specified.
                        THROUGHPUT_OPTIMIZED (1):
                            All of the nodes are available most of the
                            time. Recommended for training workloads.
                        AVAILABILITY_OPTIMIZED (2):
                            Most of the nodes are available all of the
                            time. Recommended for serving workloads.
                    """

                    WORKLOAD_TYPE_UNSPECIFIED = 0
                    THROUGHPUT_OPTIMIZED = 1
                    AVAILABILITY_OPTIMIZED = 2

                node_count: int = proto.Field(
                    proto.INT32,
                    number=1,
                )
                node_id_prefix: str = proto.Field(
                    proto.STRING,
                    number=2,
                )
                workload_type: "QueuedResource.Tpu.NodeSpec.MultiNodeParams.WorkloadType" = proto.Field(
                    proto.ENUM,
                    number=4,
                    enum="QueuedResource.Tpu.NodeSpec.MultiNodeParams.WorkloadType",
                )

            parent: str = proto.Field(
                proto.STRING,
                number=1,
            )
            node_id: str = proto.Field(
                proto.STRING,
                number=2,
            )
            multi_node_params: "QueuedResource.Tpu.NodeSpec.MultiNodeParams" = (
                proto.Field(
                    proto.MESSAGE,
                    number=6,
                    message="QueuedResource.Tpu.NodeSpec.MultiNodeParams",
                )
            )
            node: "Node" = proto.Field(
                proto.MESSAGE,
                number=3,
                message="Node",
            )

        node_spec: MutableSequence["QueuedResource.Tpu.NodeSpec"] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="QueuedResource.Tpu.NodeSpec",
        )

    class BestEffort(proto.Message):
        r"""BestEffort tier definition."""

    class Spot(proto.Message):
        r"""Spot tier definition."""

    class Guaranteed(proto.Message):
        r"""Guaranteed tier definition.

        Attributes:
            min_duration (google.protobuf.duration_pb2.Duration):
                Optional. Defines the minimum duration of the
                guarantee. If specified, the requested resources
                will only be provisioned if they can be
                allocated for at least the given duration.
            reserved (bool):
                Optional. Specifies the request should be
                scheduled on reserved capacity.
        """

        min_duration: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=1,
            message=duration_pb2.Duration,
        )
        reserved: bool = proto.Field(
            proto.BOOL,
            number=2,
        )

    class QueueingPolicy(proto.Message):
        r"""Defines the policy of the QueuedRequest.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            valid_until_duration (google.protobuf.duration_pb2.Duration):
                A relative time after which resources should
                not be created. If the request cannot be
                fulfilled by this time the request will be
                failed.

                This field is a member of `oneof`_ ``start_timing_constraints``.
            valid_until_time (google.protobuf.timestamp_pb2.Timestamp):
                An absolute time after which resources should
                not be created. If the request cannot be
                fulfilled by this time the request will be
                failed.

                This field is a member of `oneof`_ ``start_timing_constraints``.
            valid_after_duration (google.protobuf.duration_pb2.Duration):
                A relative time after which resources may be
                created.

                This field is a member of `oneof`_ ``start_timing_constraints``.
            valid_after_time (google.protobuf.timestamp_pb2.Timestamp):
                An absolute time at which resources may be
                created.

                This field is a member of `oneof`_ ``start_timing_constraints``.
            valid_interval (google.type.interval_pb2.Interval):
                An absolute time interval within which
                resources may be created.

                This field is a member of `oneof`_ ``start_timing_constraints``.
        """

        valid_until_duration: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="start_timing_constraints",
            message=duration_pb2.Duration,
        )
        valid_until_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=2,
            oneof="start_timing_constraints",
            message=timestamp_pb2.Timestamp,
        )
        valid_after_duration: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=3,
            oneof="start_timing_constraints",
            message=duration_pb2.Duration,
        )
        valid_after_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=4,
            oneof="start_timing_constraints",
            message=timestamp_pb2.Timestamp,
        )
        valid_interval: interval_pb2.Interval = proto.Field(
            proto.MESSAGE,
            number=5,
            oneof="start_timing_constraints",
            message=interval_pb2.Interval,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=11,
        message=timestamp_pb2.Timestamp,
    )
    tpu: Tpu = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="resource",
        message=Tpu,
    )
    best_effort: BestEffort = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="tier",
        message=BestEffort,
    )
    guaranteed: Guaranteed = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="tier",
        message=Guaranteed,
    )
    spot: Spot = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="tier",
        message=Spot,
    )
    queueing_policy: QueueingPolicy = proto.Field(
        proto.MESSAGE,
        number=5,
        message=QueueingPolicy,
    )
    state: "QueuedResourceState" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="QueuedResourceState",
    )
    reservation_name: str = proto.Field(
        proto.STRING,
        number=8,
    )


class QueuedResourceState(proto.Message):
    r"""QueuedResourceState defines the details of the QueuedResource
    request.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        state (google.cloud.tpu_v2alpha1.types.QueuedResourceState.State):
            State of the QueuedResource request.
        creating_data (google.cloud.tpu_v2alpha1.types.QueuedResourceState.CreatingData):
            Further data for the creating state.

            This field is a member of `oneof`_ ``state_data``.
        accepted_data (google.cloud.tpu_v2alpha1.types.QueuedResourceState.AcceptedData):
            Further data for the accepted state.

            This field is a member of `oneof`_ ``state_data``.
        provisioning_data (google.cloud.tpu_v2alpha1.types.QueuedResourceState.ProvisioningData):
            Further data for the provisioning state.

            This field is a member of `oneof`_ ``state_data``.
        failed_data (google.cloud.tpu_v2alpha1.types.QueuedResourceState.FailedData):
            Further data for the failed state.

            This field is a member of `oneof`_ ``state_data``.
        deleting_data (google.cloud.tpu_v2alpha1.types.QueuedResourceState.DeletingData):
            Further data for the deleting state.

            This field is a member of `oneof`_ ``state_data``.
        active_data (google.cloud.tpu_v2alpha1.types.QueuedResourceState.ActiveData):
            Further data for the active state.

            This field is a member of `oneof`_ ``state_data``.
        suspending_data (google.cloud.tpu_v2alpha1.types.QueuedResourceState.SuspendingData):
            Further data for the suspending state.

            This field is a member of `oneof`_ ``state_data``.
        suspended_data (google.cloud.tpu_v2alpha1.types.QueuedResourceState.SuspendedData):
            Further data for the suspended state.

            This field is a member of `oneof`_ ``state_data``.
        state_initiator (google.cloud.tpu_v2alpha1.types.QueuedResourceState.StateInitiator):
            Output only. The initiator of the
            QueuedResources's current state. Used to
            indicate whether the SUSPENDING/SUSPENDED state
            was initiated by the user or the service.
    """

    class State(proto.Enum):
        r"""Output only state of the request

        Values:
            STATE_UNSPECIFIED (0):
                State of the QueuedResource request is not
                known/set.
            CREATING (1):
                The QueuedResource request has been received.
                We're still working on determining if we will be
                able to honor this request.
            ACCEPTED (2):
                The QueuedResource request has passed initial
                validation/admission control and has been
                persisted in the queue.
            PROVISIONING (3):
                The QueuedResource request has been selected.
                The associated resources are currently being
                provisioned (or very soon will begin
                provisioning).
            FAILED (4):
                The request could not be completed. This may
                be due to some late-discovered problem with the
                request itself, or due to unavailability of
                resources within the constraints of the request
                (e.g., the 'valid until' start timing constraint
                expired).
            DELETING (5):
                The QueuedResource is being deleted.
            ACTIVE (6):
                The resources specified in the QueuedResource
                request have been provisioned and are ready for
                use by the end-user/consumer.
            SUSPENDING (7):
                The resources specified in the QueuedResource
                request are being deleted. This may have been
                initiated by the user, or the Cloud TPU service.
                Inspect the state data for more details.
            SUSPENDED (8):
                The resources specified in the QueuedResource
                request have been deleted.
            WAITING_FOR_RESOURCES (9):
                The QueuedResource request has passed initial validation and
                has been persisted in the queue. It will remain in this
                state until there are sufficient free resources to begin
                provisioning your request. Wait times will vary
                significantly depending on demand levels. When demand is
                high, not all requests can be immediately provisioned. If
                you need more reliable obtainability of TPUs consider
                purchasing a reservation. To put a limit on how long you are
                willing to wait, use `timing
                constraints <https://cloud.google.com/tpu/docs/queued-resources#request_a_queued_resource_before_a_specified_time>`__.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        ACCEPTED = 2
        PROVISIONING = 3
        FAILED = 4
        DELETING = 5
        ACTIVE = 6
        SUSPENDING = 7
        SUSPENDED = 8
        WAITING_FOR_RESOURCES = 9

    class StateInitiator(proto.Enum):
        r"""The initiator of the QueuedResource's SUSPENDING/SUSPENDED
        state.

        Values:
            STATE_INITIATOR_UNSPECIFIED (0):
                The state initiator is unspecified.
            USER (1):
                The current QueuedResource state was
                initiated by the user.
            SERVICE (2):
                The current QueuedResource state was
                initiated by the service.
        """

        STATE_INITIATOR_UNSPECIFIED = 0
        USER = 1
        SERVICE = 2

    class CreatingData(proto.Message):
        r"""Further data for the creating state."""

    class AcceptedData(proto.Message):
        r"""Further data for the accepted state."""

    class ProvisioningData(proto.Message):
        r"""Further data for the provisioning state."""

    class FailedData(proto.Message):
        r"""Further data for the failed state.

        Attributes:
            error (google.rpc.status_pb2.Status):
                The error that caused the queued resource to
                enter the FAILED state.
        """

        error: status_pb2.Status = proto.Field(
            proto.MESSAGE,
            number=1,
            message=status_pb2.Status,
        )

    class DeletingData(proto.Message):
        r"""Further data for the deleting state."""

    class ActiveData(proto.Message):
        r"""Further data for the active state."""

    class SuspendingData(proto.Message):
        r"""Further data for the suspending state."""

    class SuspendedData(proto.Message):
        r"""Further data for the suspended state."""

    state: State = proto.Field(
        proto.ENUM,
        number=1,
        enum=State,
    )
    creating_data: CreatingData = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="state_data",
        message=CreatingData,
    )
    accepted_data: AcceptedData = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="state_data",
        message=AcceptedData,
    )
    provisioning_data: ProvisioningData = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="state_data",
        message=ProvisioningData,
    )
    failed_data: FailedData = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="state_data",
        message=FailedData,
    )
    deleting_data: DeletingData = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="state_data",
        message=DeletingData,
    )
    active_data: ActiveData = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="state_data",
        message=ActiveData,
    )
    suspending_data: SuspendingData = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="state_data",
        message=SuspendingData,
    )
    suspended_data: SuspendedData = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="state_data",
        message=SuspendedData,
    )
    state_initiator: StateInitiator = proto.Field(
        proto.ENUM,
        number=10,
        enum=StateInitiator,
    )


class ListNodesRequest(proto.Message):
    r"""Request for [ListNodes][google.cloud.tpu.v2alpha1.Tpu.ListNodes].

    Attributes:
        parent (str):
            Required. The parent resource name.
        page_size (int):
            The maximum number of items to return.
        page_token (str):
            The next_page_token value returned from a previous List
            request, if any.
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


class ListNodesResponse(proto.Message):
    r"""Response for [ListNodes][google.cloud.tpu.v2alpha1.Tpu.ListNodes].

    Attributes:
        nodes (MutableSequence[google.cloud.tpu_v2alpha1.types.Node]):
            The listed nodes.
        next_page_token (str):
            The next page token or empty if none.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    nodes: MutableSequence["Node"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Node",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetNodeRequest(proto.Message):
    r"""Request for [GetNode][google.cloud.tpu.v2alpha1.Tpu.GetNode].

    Attributes:
        name (str):
            Required. The resource name.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateNodeRequest(proto.Message):
    r"""Request for [CreateNode][google.cloud.tpu.v2alpha1.Tpu.CreateNode].

    Attributes:
        parent (str):
            Required. The parent resource name.
        node_id (str):
            The unqualified resource name.
        node (google.cloud.tpu_v2alpha1.types.Node):
            Required. The node.
        request_id (str):
            Idempotent request UUID.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    node_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    node: "Node" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Node",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=6,
    )


class DeleteNodeRequest(proto.Message):
    r"""Request for [DeleteNode][google.cloud.tpu.v2alpha1.Tpu.DeleteNode].

    Attributes:
        name (str):
            Required. The resource name.
        request_id (str):
            Idempotent request UUID.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class StopNodeRequest(proto.Message):
    r"""Request for [StopNode][google.cloud.tpu.v2alpha1.Tpu.StopNode].

    Attributes:
        name (str):
            Required. The resource name.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class StartNodeRequest(proto.Message):
    r"""Request for [StartNode][google.cloud.tpu.v2alpha1.Tpu.StartNode].

    Attributes:
        name (str):
            Required. The resource name.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateNodeRequest(proto.Message):
    r"""Request for [UpdateNode][google.cloud.tpu.v2alpha1.Tpu.UpdateNode].

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Mask of fields from [Node][Tpu.Node] to update.
            Supported fields: [description, tags, labels, metadata,
            network_config.enable_external_ips].
        node (google.cloud.tpu_v2alpha1.types.Node):
            Required. The node. Only fields specified in update_mask are
            updated.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    node: "Node" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Node",
    )


class ListQueuedResourcesRequest(proto.Message):
    r"""Request for
    [ListQueuedResources][google.cloud.tpu.v2alpha1.Tpu.ListQueuedResources].

    Attributes:
        parent (str):
            Required. The parent resource name.
        page_size (int):
            The maximum number of items to return.
        page_token (str):
            The next_page_token value returned from a previous List
            request, if any.
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


class ListQueuedResourcesResponse(proto.Message):
    r"""Response for
    [ListQueuedResources][google.cloud.tpu.v2alpha1.Tpu.ListQueuedResources].

    Attributes:
        queued_resources (MutableSequence[google.cloud.tpu_v2alpha1.types.QueuedResource]):
            The listed queued resources.
        next_page_token (str):
            The next page token or empty if none.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    queued_resources: MutableSequence["QueuedResource"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="QueuedResource",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetQueuedResourceRequest(proto.Message):
    r"""Request for
    [GetQueuedResource][google.cloud.tpu.v2alpha1.Tpu.GetQueuedResource]

    Attributes:
        name (str):
            Required. The resource name.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateQueuedResourceRequest(proto.Message):
    r"""Request for
    [CreateQueuedResource][google.cloud.tpu.v2alpha1.Tpu.CreateQueuedResource].

    Attributes:
        parent (str):
            Required. The parent resource name.
        queued_resource_id (str):
            The unqualified resource name. Should follow the
            ``^[A-Za-z0-9_.~+%-]+$`` regex format.
        queued_resource (google.cloud.tpu_v2alpha1.types.QueuedResource):
            Required. The queued resource.
        request_id (str):
            Idempotent request UUID.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    queued_resource_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    queued_resource: "QueuedResource" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="QueuedResource",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class DeleteQueuedResourceRequest(proto.Message):
    r"""Request for
    [DeleteQueuedResource][google.cloud.tpu.v2alpha1.Tpu.DeleteQueuedResource].

    Attributes:
        name (str):
            Required. The resource name.
        request_id (str):
            Idempotent request UUID.
        force (bool):
            If set to true, all running nodes belonging
            to this queued resource will be deleted first
            and then the queued resource will be deleted.
            Otherwise (i.e. force=false), the queued
            resource will only be deleted if its nodes have
            already been deleted or the queued resource is
            in the ACCEPTED, FAILED, or SUSPENDED state.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class ResetQueuedResourceRequest(proto.Message):
    r"""Request for
    [ResetQueuedResource][google.cloud.tpu.v2alpha1.Tpu.ResetQueuedResource].

    Attributes:
        name (str):
            Required. The name of the queued resource.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ServiceIdentity(proto.Message):
    r"""The per-product per-project service identity for Cloud TPU
    service.

    Attributes:
        email (str):
            The email address of the service identity.
    """

    email: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GenerateServiceIdentityRequest(proto.Message):
    r"""Request for
    [GenerateServiceIdentity][google.cloud.tpu.v2alpha1.Tpu.GenerateServiceIdentity].

    Attributes:
        parent (str):
            Required. The parent resource name.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GenerateServiceIdentityResponse(proto.Message):
    r"""Response for
    [GenerateServiceIdentity][google.cloud.tpu.v2alpha1.Tpu.GenerateServiceIdentity].

    Attributes:
        identity (google.cloud.tpu_v2alpha1.types.ServiceIdentity):
            ServiceIdentity that was created or
            retrieved.
    """

    identity: "ServiceIdentity" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="ServiceIdentity",
    )


class AcceleratorType(proto.Message):
    r"""A accelerator type that a Node can be configured with.

    Attributes:
        name (str):
            The resource name.
        type_ (str):
            The accelerator type.
        accelerator_configs (MutableSequence[google.cloud.tpu_v2alpha1.types.AcceleratorConfig]):
            The accelerator config.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    type_: str = proto.Field(
        proto.STRING,
        number=2,
    )
    accelerator_configs: MutableSequence["AcceleratorConfig"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="AcceleratorConfig",
    )


class GetAcceleratorTypeRequest(proto.Message):
    r"""Request for
    [GetAcceleratorType][google.cloud.tpu.v2alpha1.Tpu.GetAcceleratorType].

    Attributes:
        name (str):
            Required. The resource name.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListAcceleratorTypesRequest(proto.Message):
    r"""Request for
    [ListAcceleratorTypes][google.cloud.tpu.v2alpha1.Tpu.ListAcceleratorTypes].

    Attributes:
        parent (str):
            Required. The parent resource name.
        page_size (int):
            The maximum number of items to return.
        page_token (str):
            The next_page_token value returned from a previous List
            request, if any.
        filter (str):
            List filter.
        order_by (str):
            Sort results.
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
    filter: str = proto.Field(
        proto.STRING,
        number=5,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=6,
    )


class ListAcceleratorTypesResponse(proto.Message):
    r"""Response for
    [ListAcceleratorTypes][google.cloud.tpu.v2alpha1.Tpu.ListAcceleratorTypes].

    Attributes:
        accelerator_types (MutableSequence[google.cloud.tpu_v2alpha1.types.AcceleratorType]):
            The listed nodes.
        next_page_token (str):
            The next page token or empty if none.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    accelerator_types: MutableSequence["AcceleratorType"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="AcceleratorType",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class RuntimeVersion(proto.Message):
    r"""A runtime version that a Node can be configured with.

    Attributes:
        name (str):
            The resource name.
        version (str):
            The runtime version.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    version: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetRuntimeVersionRequest(proto.Message):
    r"""Request for
    [GetRuntimeVersion][google.cloud.tpu.v2alpha1.Tpu.GetRuntimeVersion].

    Attributes:
        name (str):
            Required. The resource name.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListRuntimeVersionsRequest(proto.Message):
    r"""Request for
    [ListRuntimeVersions][google.cloud.tpu.v2alpha1.Tpu.ListRuntimeVersions].

    Attributes:
        parent (str):
            Required. The parent resource name.
        page_size (int):
            The maximum number of items to return.
        page_token (str):
            The next_page_token value returned from a previous List
            request, if any.
        filter (str):
            List filter.
        order_by (str):
            Sort results.
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
    filter: str = proto.Field(
        proto.STRING,
        number=5,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=6,
    )


class ListRuntimeVersionsResponse(proto.Message):
    r"""Response for
    [ListRuntimeVersions][google.cloud.tpu.v2alpha1.Tpu.ListRuntimeVersions].

    Attributes:
        runtime_versions (MutableSequence[google.cloud.tpu_v2alpha1.types.RuntimeVersion]):
            The listed nodes.
        next_page_token (str):
            The next page token or empty if none.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    runtime_versions: MutableSequence["RuntimeVersion"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="RuntimeVersion",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class OperationMetadata(proto.Message):
    r"""Metadata describing an [Operation][google.longrunning.Operation]

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            The time the operation was created.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            The time the operation finished running.
        target (str):
            Target of the operation - for example
            projects/project-1/connectivityTests/test-1
        verb (str):
            Name of the verb executed by the operation.
        status_detail (str):
            Human-readable status of the operation, if
            any.
        cancel_requested (bool):
            Specifies if cancellation was requested for
            the operation.
        api_version (str):
            API version.
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
    status_detail: str = proto.Field(
        proto.STRING,
        number=5,
    )
    cancel_requested: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    api_version: str = proto.Field(
        proto.STRING,
        number=7,
    )


class Symptom(proto.Message):
    r"""A Symptom instance.

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Timestamp when the Symptom is created.
        symptom_type (google.cloud.tpu_v2alpha1.types.Symptom.SymptomType):
            Type of the Symptom.
        details (str):
            Detailed information of the current Symptom.
        worker_id (str):
            A string used to uniquely distinguish a
            worker within a TPU node.
    """

    class SymptomType(proto.Enum):
        r"""SymptomType represents the different types of Symptoms that a
        TPU can be at.

        Values:
            SYMPTOM_TYPE_UNSPECIFIED (0):
                Unspecified symptom.
            LOW_MEMORY (1):
                TPU VM memory is low.
            OUT_OF_MEMORY (2):
                TPU runtime is out of memory.
            EXECUTE_TIMED_OUT (3):
                TPU runtime execution has timed out.
            MESH_BUILD_FAIL (4):
                TPU runtime fails to construct a mesh that
                recognizes each TPU device's neighbors.
            HBM_OUT_OF_MEMORY (5):
                TPU HBM is out of memory.
            PROJECT_ABUSE (6):
                Abusive behaviors have been identified on the
                current project.
        """

        SYMPTOM_TYPE_UNSPECIFIED = 0
        LOW_MEMORY = 1
        OUT_OF_MEMORY = 2
        EXECUTE_TIMED_OUT = 3
        MESH_BUILD_FAIL = 4
        HBM_OUT_OF_MEMORY = 5
        PROJECT_ABUSE = 6

    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    symptom_type: SymptomType = proto.Field(
        proto.ENUM,
        number=2,
        enum=SymptomType,
    )
    details: str = proto.Field(
        proto.STRING,
        number=3,
    )
    worker_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class GetGuestAttributesRequest(proto.Message):
    r"""Request for
    [GetGuestAttributes][google.cloud.tpu.v2alpha1.Tpu.GetGuestAttributes].

    Attributes:
        name (str):
            Required. The resource name.
        query_path (str):
            The guest attributes path to be queried.
        worker_ids (MutableSequence[str]):
            The 0-based worker ID. If it is empty, all
            workers' GuestAttributes will be returned.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    query_path: str = proto.Field(
        proto.STRING,
        number=2,
    )
    worker_ids: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetGuestAttributesResponse(proto.Message):
    r"""Response for
    [GetGuestAttributes][google.cloud.tpu.v2alpha1.Tpu.GetGuestAttributes].

    Attributes:
        guest_attributes (MutableSequence[google.cloud.tpu_v2alpha1.types.GuestAttributes]):
            The guest attributes for the TPU workers.
    """

    guest_attributes: MutableSequence["GuestAttributes"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="GuestAttributes",
    )


class SimulateMaintenanceEventRequest(proto.Message):
    r"""Request for
    [SimulateMaintenanceEvent][google.cloud.tpu.v2alpha1.Tpu.SimulateMaintenanceEvent].

    Attributes:
        name (str):
            Required. The resource name.
        worker_ids (MutableSequence[str]):
            The 0-based worker ID. If it is empty, worker
            ID 0 will be selected for maintenance event
            simulation. A maintenance event will only be
            fired on the first specified worker ID. Future
            implementations may support firing on multiple
            workers.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    worker_ids: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class PerformMaintenanceRequest(proto.Message):
    r"""Request for
    [PerformMaintenance][google.cloud.tpu.v2alpha1.Tpu.PerformMaintenance].

    Attributes:
        name (str):
            Required. The resource name.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class PerformMaintenanceQueuedResourceRequest(proto.Message):
    r"""Request for
    [PerformMaintenanceQueuedResource][google.cloud.tpu.v2alpha1.Tpu.PerformMaintenanceQueuedResource].

    Attributes:
        name (str):
            Required. The name of the QueuedResource
            which holds the nodes to perform maintenance on.
        node_names (MutableSequence[str]):
            The names of the nodes to perform maintenance
            on.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    node_names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class Reservation(proto.Message):
    r"""A reservation describes the amount of a resource 'allotted'
    for a defined period of time.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            The reservation name with the format:

            projects/{projectID}/locations/{location}/reservations/{reservationID}
        standard (google.cloud.tpu_v2alpha1.types.Reservation.Standard):
            A standard reservation.

            This field is a member of `oneof`_ ``kind``.
        state (google.cloud.tpu_v2alpha1.types.Reservation.State):
            Output only. The state of the Reservation.
    """

    class State(proto.Enum):
        r"""State of the Reservation.

        Values:
            STATE_UNSPECIFIED (0):
                The Reservation state is unspecified.
            APPROVED (3):
                The Reservation has been approved.
            PROVISIONING (4):
                The Reservation is being provisioned.
            ACTIVE (5):
                The Reservation is active.
            DEPROVISIONING (6):
                The Reservation is being deprovisioned.
            EXPIRED (7):
                The Reservation is past its end date.
            FAILED (8):
                The Reservation encountered a failure during
                mutation.
        """

        STATE_UNSPECIFIED = 0
        APPROVED = 3
        PROVISIONING = 4
        ACTIVE = 5
        DEPROVISIONING = 6
        EXPIRED = 7
        FAILED = 8

    class Standard(proto.Message):
        r"""Details of a standard reservation.

        Attributes:
            size (int):
                The size of the reservation, in the units specified in the
                'capacity_units' field.
            capacity_units (google.cloud.tpu_v2alpha1.types.Reservation.Standard.CapacityUnits):
                Capacity units this reservation is measured
                in.
            resource_type (str):
                The resource type of the reservation.
            interval (google.type.interval_pb2.Interval):
                The start and end time of the reservation.
            usage (google.cloud.tpu_v2alpha1.types.Reservation.Standard.Usage):
                The current usage of the reservation.
        """

        class CapacityUnits(proto.Enum):
            r"""Units in which capacity for a reservation is measured.

            Values:
                CAPACITY_UNITS_UNSPECIFIED (0):
                    The capacity units is not known/set.
                CORES (1):
                    The capacity unit is set to CORES.
                CHIPS (2):
                    The capacity unit is set to CHIPS.
            """

            CAPACITY_UNITS_UNSPECIFIED = 0
            CORES = 1
            CHIPS = 2

        class Usage(proto.Message):
            r"""Usage details of a reservation.

            Attributes:
                total (int):
                    The real-time value of usage within the reservation, with
                    the unit specified in field capacity_units.
            """

            total: int = proto.Field(
                proto.INT64,
                number=1,
            )

        size: int = proto.Field(
            proto.INT32,
            number=1,
        )
        capacity_units: "Reservation.Standard.CapacityUnits" = proto.Field(
            proto.ENUM,
            number=2,
            enum="Reservation.Standard.CapacityUnits",
        )
        resource_type: str = proto.Field(
            proto.STRING,
            number=3,
        )
        interval: interval_pb2.Interval = proto.Field(
            proto.MESSAGE,
            number=4,
            message=interval_pb2.Interval,
        )
        usage: "Reservation.Standard.Usage" = proto.Field(
            proto.MESSAGE,
            number=5,
            message="Reservation.Standard.Usage",
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    standard: Standard = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="kind",
        message=Standard,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=3,
        enum=State,
    )


class ListReservationsRequest(proto.Message):
    r"""Request for
    [ListReservations][google.cloud.tpu.v2alpha1.Tpu.ListReservations].

    Attributes:
        parent (str):
            Required. The parent for reservations.
        page_size (int):
            The maximum number of items to return.
            Defaults to 0 if not specified, which means no
            limit.
        page_token (str):
            The next_page_token value returned from a previous List
            request, if any.
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


class ListReservationsResponse(proto.Message):
    r"""Response for
    [ListReservations][google.cloud.tpu.v2alpha1.Tpu.ListReservations].

    Attributes:
        reservations (MutableSequence[google.cloud.tpu_v2alpha1.types.Reservation]):
            The listed reservations.
        next_page_token (str):
            The next page token or empty if none.
    """

    @property
    def raw_page(self):
        return self

    reservations: MutableSequence["Reservation"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Reservation",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class AcceleratorConfig(proto.Message):
    r"""A TPU accelerator configuration.

    Attributes:
        type_ (google.cloud.tpu_v2alpha1.types.AcceleratorConfig.Type):
            Required. Type of TPU.
        topology (str):
            Required. Topology of TPU in chips.
    """

    class Type(proto.Enum):
        r"""TPU type.

        Values:
            TYPE_UNSPECIFIED (0):
                Unspecified version.
            V2 (2):
                TPU v2.
            V3 (4):
                TPU v3.
            V4 (7):
                TPU v4.
            V5LITE_POD (9):
                TPU v5lite pod.
            V5P (10):
                TPU v5.
            V6E (11):
                TPU v6e.
        """

        TYPE_UNSPECIFIED = 0
        V2 = 2
        V3 = 4
        V4 = 7
        V5LITE_POD = 9
        V5P = 10
        V6E = 11

    type_: Type = proto.Field(
        proto.ENUM,
        number=1,
        enum=Type,
    )
    topology: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ShieldedInstanceConfig(proto.Message):
    r"""A set of Shielded Instance options.

    Attributes:
        enable_secure_boot (bool):
            Defines whether the instance has Secure Boot
            enabled.
    """

    enable_secure_boot: bool = proto.Field(
        proto.BOOL,
        number=1,
    )


class BootDiskConfig(proto.Message):
    r"""Boot disk configurations.

    Attributes:
        customer_encryption_key (google.cloud.tpu_v2alpha1.types.CustomerEncryptionKey):
            Optional. Customer encryption key for boot
            disk.
        enable_confidential_compute (bool):
            Optional. Whether the boot disk will be
            created with confidential compute mode.
    """

    customer_encryption_key: "CustomerEncryptionKey" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="CustomerEncryptionKey",
    )
    enable_confidential_compute: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class CustomerEncryptionKey(proto.Message):
    r"""Customer's encryption key.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        kms_key_name (str):
            The name of the encryption key that is stored in Google
            Cloud KMS. For example:

            .. raw:: html

                <pre class="lang-html">"kmsKeyName": "projects/
                <var class="apiparam">kms_project_id</var>/locations/
                <var class="apiparam">region</var>/keyRings/<var class="apiparam">
                key_region</var>/cryptoKeys/<var class="apiparam">key</var>
                </pre>

            The fully-qualifed key name may be returned for resource GET
            requests. For example:

            .. raw:: html

                <pre class="lang-html">"kmsKeyName": "projects/
                <var class="apiparam">kms_project_id</var>/locations/
                <var class="apiparam">region</var>/keyRings/<var class="apiparam">
                key_region</var>/cryptoKeys/<var class="apiparam">key</var>
                /cryptoKeyVersions/1</pre>

            This field is a member of `oneof`_ ``key``.
    """

    kms_key_name: str = proto.Field(
        proto.STRING,
        number=7,
        oneof="key",
    )


class UpcomingMaintenance(proto.Message):
    r"""Upcoming Maintenance notification information.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        type_ (google.cloud.tpu_v2alpha1.types.UpcomingMaintenance.MaintenanceType):
            Defines the type of maintenance.

            This field is a member of `oneof`_ ``_type``.
        can_reschedule (bool):
            Indicates if the maintenance can be customer
            triggered.

            This field is a member of `oneof`_ ``_can_reschedule``.
        window_start_time (str):
            The current start time of the maintenance
            window. This timestamp value is in RFC3339 text
            format.

            This field is a member of `oneof`_ ``_window_start_time``.
        window_end_time (str):
            The time by which the maintenance disruption
            will be completed. This timestamp value is in
            RFC3339 text format.

            This field is a member of `oneof`_ ``_window_end_time``.
        latest_window_start_time (str):
            The latest time for the planned maintenance
            window to start. This timestamp value is in
            RFC3339 text format.

            This field is a member of `oneof`_ ``_latest_window_start_time``.
        maintenance_status (google.cloud.tpu_v2alpha1.types.UpcomingMaintenance.MaintenanceStatus):
            The status of the maintenance.

            This field is a member of `oneof`_ ``_maintenance_status``.
    """

    class MaintenanceType(proto.Enum):
        r"""The type of maintenance for this notification.

        Values:
            UNKNOWN_TYPE (0):
                No type specified. Do not use this value.
            SCHEDULED (1):
                Scheduled maintenance (e.g. maintenance after
                uptime guarantee is complete).
            UNSCHEDULED (2):
                Unscheduled maintenance (e.g. emergency
                maintenance during uptime guarantee).
        """

        UNKNOWN_TYPE = 0
        SCHEDULED = 1
        UNSCHEDULED = 2

    class MaintenanceStatus(proto.Enum):
        r"""The status of the maintenance for this notification.

        Values:
            UNKNOWN (0):
                Unknown maintenance status. Do not use this
                value.
            PENDING (1):
                There is pending maintenance.
            ONGOING (2):
                There is ongoing maintenance on this VM.
        """

        UNKNOWN = 0
        PENDING = 1
        ONGOING = 2

    type_: MaintenanceType = proto.Field(
        proto.ENUM,
        number=1,
        optional=True,
        enum=MaintenanceType,
    )
    can_reschedule: bool = proto.Field(
        proto.BOOL,
        number=5,
        optional=True,
    )
    window_start_time: str = proto.Field(
        proto.STRING,
        number=6,
        optional=True,
    )
    window_end_time: str = proto.Field(
        proto.STRING,
        number=7,
        optional=True,
    )
    latest_window_start_time: str = proto.Field(
        proto.STRING,
        number=8,
        optional=True,
    )
    maintenance_status: MaintenanceStatus = proto.Field(
        proto.ENUM,
        number=9,
        optional=True,
        enum=MaintenanceStatus,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
