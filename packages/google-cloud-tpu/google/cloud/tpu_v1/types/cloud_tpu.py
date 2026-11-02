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
    package="google.cloud.tpu.v1",
    manifest={
        "SchedulingConfig",
        "NetworkEndpoint",
        "Node",
        "ListNodesRequest",
        "ListNodesResponse",
        "GetNodeRequest",
        "CreateNodeRequest",
        "DeleteNodeRequest",
        "ReimageNodeRequest",
        "StopNodeRequest",
        "StartNodeRequest",
        "TensorFlowVersion",
        "GetTensorFlowVersionRequest",
        "ListTensorFlowVersionsRequest",
        "ListTensorFlowVersionsResponse",
        "AcceleratorType",
        "GetAcceleratorTypeRequest",
        "ListAcceleratorTypesRequest",
        "ListAcceleratorTypesResponse",
        "OperationMetadata",
        "Symptom",
    },
)


class SchedulingConfig(proto.Message):
    r"""Sets the scheduling options for this node.

    Attributes:
        preemptible (bool):
            Defines whether the node is preemptible.
        reserved (bool):
            Whether the node is created under a
            reservation.
    """

    preemptible: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    reserved: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class NetworkEndpoint(proto.Message):
    r"""A network endpoint over which a TPU worker can be reached.

    Attributes:
        ip_address (str):
            The IP address of this network endpoint.
        port (int):
            The port of this network endpoint.
    """

    ip_address: str = proto.Field(
        proto.STRING,
        number=1,
    )
    port: int = proto.Field(
        proto.INT32,
        number=2,
    )


class Node(proto.Message):
    r"""A TPU instance.

    Attributes:
        name (str):
            Output only. Immutable. The name of the TPU
        description (str):
            The user-supplied description of the TPU.
            Maximum of 512 characters.
        accelerator_type (str):
            Required. The type of hardware accelerators
            associated with this node.
        ip_address (str):
            Output only. DEPRECATED! Use network_endpoints instead. The
            network address for the TPU Node as visible to Compute
            Engine instances.
        port (str):
            Output only. DEPRECATED! Use network_endpoints instead. The
            network port for the TPU Node as visible to Compute Engine
            instances.
        state (google.cloud.tpu_v1.types.Node.State):
            Output only. The current state for the TPU
            Node.
        health_description (str):
            Output only. If this field is populated, it
            contains a description of why the TPU Node is
            unhealthy.
        tensorflow_version (str):
            Required. The version of Tensorflow running
            in the Node.
        network (str):
            The name of a network they wish to peer the
            TPU node to. It must be a preexisting Compute
            Engine network inside of the project on which
            this API has been activated. If none is
            provided, "default" will be used.
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
        service_account (str):
            Output only. The service account used to run
            the tensor flow services within the node. To
            share resources, including Google Cloud Storage
            data, with the Tensorflow job running in the
            Node, this account must have permissions to that
            data.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the node was
            created.
        scheduling_config (google.cloud.tpu_v1.types.SchedulingConfig):
            The scheduling options for this node.
        network_endpoints (MutableSequence[google.cloud.tpu_v1.types.NetworkEndpoint]):
            Output only. The network endpoints where TPU
            workers can be accessed and sent work. It is
            recommended that Tensorflow clients of the node
            reach out to the 0th entry in this map first.
        health (google.cloud.tpu_v1.types.Node.Health):
            The health status of the TPU node.
        labels (MutableMapping[str, str]):
            Resource labels to represent user-provided
            metadata.
        use_service_networking (bool):
            Whether the VPC peering for the node is set up through
            Service Networking API. The VPC Peering should be set up
            before provisioning the node. If this field is set,
            cidr_block field should not be specified. If the network,
            that you want to peer the TPU Node to, is Shared VPC
            networks, the node must be created with this this field
            enabled.
        api_version (google.cloud.tpu_v1.types.Node.ApiVersion):
            Output only. The API version that created
            this Node.
        symptoms (MutableSequence[google.cloud.tpu_v1.types.Symptom]):
            Output only. The Symptoms that have occurred
            to the TPU Node.
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
                be found in the ``help_description`` field.
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
            DEPRECATED_UNHEALTHY (2):
                The resource is unhealthy.
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
        DEPRECATED_UNHEALTHY = 2
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
    ip_address: str = proto.Field(
        proto.STRING,
        number=8,
    )
    port: str = proto.Field(
        proto.STRING,
        number=14,
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
    tensorflow_version: str = proto.Field(
        proto.STRING,
        number=11,
    )
    network: str = proto.Field(
        proto.STRING,
        number=12,
    )
    cidr_block: str = proto.Field(
        proto.STRING,
        number=13,
    )
    service_account: str = proto.Field(
        proto.STRING,
        number=15,
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
    use_service_networking: bool = proto.Field(
        proto.BOOL,
        number=27,
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


class ListNodesRequest(proto.Message):
    r"""Request for [ListNodes][google.cloud.tpu.v1.Tpu.ListNodes].

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
    r"""Response for [ListNodes][google.cloud.tpu.v1.Tpu.ListNodes].

    Attributes:
        nodes (MutableSequence[google.cloud.tpu_v1.types.Node]):
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
    r"""Request for [GetNode][google.cloud.tpu.v1.Tpu.GetNode].

    Attributes:
        name (str):
            Required. The resource name.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateNodeRequest(proto.Message):
    r"""Request for [CreateNode][google.cloud.tpu.v1.Tpu.CreateNode].

    Attributes:
        parent (str):
            Required. The parent resource name.
        node_id (str):
            The unqualified resource name.
        node (google.cloud.tpu_v1.types.Node):
            Required. The node.
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


class DeleteNodeRequest(proto.Message):
    r"""Request for [DeleteNode][google.cloud.tpu.v1.Tpu.DeleteNode].

    Attributes:
        name (str):
            Required. The resource name.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ReimageNodeRequest(proto.Message):
    r"""Request for [ReimageNode][google.cloud.tpu.v1.Tpu.ReimageNode].

    Attributes:
        name (str):
            The resource name.
        tensorflow_version (str):
            The version for reimage to create.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    tensorflow_version: str = proto.Field(
        proto.STRING,
        number=2,
    )


class StopNodeRequest(proto.Message):
    r"""Request for [StopNode][google.cloud.tpu.v1.Tpu.StopNode].

    Attributes:
        name (str):
            The resource name.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class StartNodeRequest(proto.Message):
    r"""Request for [StartNode][google.cloud.tpu.v1.Tpu.StartNode].

    Attributes:
        name (str):
            The resource name.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class TensorFlowVersion(proto.Message):
    r"""A tensorflow version that a Node can be configured with.

    Attributes:
        name (str):
            The resource name.
        version (str):
            the tensorflow version.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    version: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetTensorFlowVersionRequest(proto.Message):
    r"""Request for
    [GetTensorFlowVersion][google.cloud.tpu.v1.Tpu.GetTensorFlowVersion].

    Attributes:
        name (str):
            Required. The resource name.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListTensorFlowVersionsRequest(proto.Message):
    r"""Request for
    [ListTensorFlowVersions][google.cloud.tpu.v1.Tpu.ListTensorFlowVersions].

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


class ListTensorFlowVersionsResponse(proto.Message):
    r"""Response for
    [ListTensorFlowVersions][google.cloud.tpu.v1.Tpu.ListTensorFlowVersions].

    Attributes:
        tensorflow_versions (MutableSequence[google.cloud.tpu_v1.types.TensorFlowVersion]):
            The listed nodes.
        next_page_token (str):
            The next page token or empty if none.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    tensorflow_versions: MutableSequence["TensorFlowVersion"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="TensorFlowVersion",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class AcceleratorType(proto.Message):
    r"""A accelerator type that a Node can be configured with.

    Attributes:
        name (str):
            The resource name.
        type_ (str):
            the accelerator type.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    type_: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetAcceleratorTypeRequest(proto.Message):
    r"""Request for
    [GetAcceleratorType][google.cloud.tpu.v1.Tpu.GetAcceleratorType].

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
    [ListAcceleratorTypes][google.cloud.tpu.v1.Tpu.ListAcceleratorTypes].

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
    [ListAcceleratorTypes][google.cloud.tpu.v1.Tpu.ListAcceleratorTypes].

    Attributes:
        accelerator_types (MutableSequence[google.cloud.tpu_v1.types.AcceleratorType]):
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
        symptom_type (google.cloud.tpu_v1.types.Symptom.SymptomType):
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


__all__ = tuple(sorted(__protobuf__.manifest))
