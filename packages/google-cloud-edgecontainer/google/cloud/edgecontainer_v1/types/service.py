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

import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.edgecontainer_v1.types import resources

__protobuf__ = proto.module(
    package="google.cloud.edgecontainer.v1",
    manifest={
        "OperationMetadata",
        "ListClustersRequest",
        "ListClustersResponse",
        "GetClusterRequest",
        "CreateClusterRequest",
        "UpdateClusterRequest",
        "UpgradeClusterRequest",
        "DeleteClusterRequest",
        "GenerateAccessTokenRequest",
        "GenerateAccessTokenResponse",
        "GenerateOfflineCredentialRequest",
        "GenerateOfflineCredentialResponse",
        "ListNodePoolsRequest",
        "ListNodePoolsResponse",
        "GetNodePoolRequest",
        "CreateNodePoolRequest",
        "UpdateNodePoolRequest",
        "DeleteNodePoolRequest",
        "ListMachinesRequest",
        "ListMachinesResponse",
        "GetMachineRequest",
        "ListVpnConnectionsRequest",
        "ListVpnConnectionsResponse",
        "GetVpnConnectionRequest",
        "CreateVpnConnectionRequest",
        "DeleteVpnConnectionRequest",
        "GetServerConfigRequest",
    },
)


class OperationMetadata(proto.Message):
    r"""Long-running operation metadata for Edge Container API
    methods.

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            The time the operation was created.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            The time the operation finished running.
        target (str):
            Server-defined resource path for the target
            of the operation.
        verb (str):
            The verb executed by the operation.
        status_message (str):
            Human-readable status of the operation, if
            any.
        requested_cancellation (bool):
            Identifies whether the user has requested cancellation of
            the operation. Operations that have successfully been
            cancelled have [Operation.error][] value with a
            [google.rpc.Status.code][google.rpc.Status.code] of 1,
            corresponding to ``Code.CANCELLED``.
        api_version (str):
            API version used to start the operation.
        warnings (MutableSequence[str]):
            Warnings that do not block the operation, but
            still hold relevant information for the end user
            to receive.
        status_reason (google.cloud.edgecontainer_v1.types.OperationMetadata.StatusReason):
            Machine-readable status of the operation, if
            any.
    """

    class StatusReason(proto.Enum):
        r"""Indicates the reason for the status of the operation.

        Values:
            STATUS_REASON_UNSPECIFIED (0):
                Reason unknown.
            UPGRADE_PAUSED (1):
                The cluster upgrade is currently paused.
        """

        STATUS_REASON_UNSPECIFIED = 0
        UPGRADE_PAUSED = 1

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
    warnings: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=8,
    )
    status_reason: StatusReason = proto.Field(
        proto.ENUM,
        number=9,
        enum=StatusReason,
    )


class ListClustersRequest(proto.Message):
    r"""Lists clusters in a location.

    Attributes:
        parent (str):
            Required. The parent location, which owns
            this collection of clusters.
        page_size (int):
            The maximum number of resources to list.
        page_token (str):
            A page token received from previous list
            request. A page token received from previous
            list request.
        filter (str):
            Only resources matching this filter will be
            listed.
        order_by (str):
            Specifies the order in which resources will
            be listed.
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
        number=4,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListClustersResponse(proto.Message):
    r"""List of clusters in a location.

    Attributes:
        clusters (MutableSequence[google.cloud.edgecontainer_v1.types.Cluster]):
            Clusters in the location.
        next_page_token (str):
            A token to retrieve next page of results.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    clusters: MutableSequence[resources.Cluster] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.Cluster,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetClusterRequest(proto.Message):
    r"""Gets a cluster.

    Attributes:
        name (str):
            Required. The resource name of the cluster.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateClusterRequest(proto.Message):
    r"""Creates a cluster.

    Attributes:
        parent (str):
            Required. The parent location where this
            cluster will be created.
        cluster_id (str):
            Required. A client-specified unique
            identifier for the cluster.
        cluster (google.cloud.edgecontainer_v1.types.Cluster):
            Required. The cluster to create.
        request_id (str):
            A unique identifier for this request. Restricted to 36 ASCII
            characters. A random UUID is recommended. This request is
            only idempotent if ``request_id`` is provided.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    cluster_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    cluster: resources.Cluster = proto.Field(
        proto.MESSAGE,
        number=3,
        message=resources.Cluster,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateClusterRequest(proto.Message):
    r"""Updates a cluster.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Field mask is used to specify the fields to be overwritten
            in the Cluster resource by the update. The fields specified
            in the update_mask are relative to the resource, not the
            full request. A field will be overwritten if it is in the
            mask. If the user does not provide a mask then all fields
            will be overwritten.
        cluster (google.cloud.edgecontainer_v1.types.Cluster):
            The updated cluster.
        request_id (str):
            A unique identifier for this request. Restricted to 36 ASCII
            characters. A random UUID is recommended. This request is
            only idempotent if ``request_id`` is provided.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    cluster: resources.Cluster = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.Cluster,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class UpgradeClusterRequest(proto.Message):
    r"""Upgrades a cluster.

    Attributes:
        name (str):
            Required. The resource name of the cluster.
        target_version (str):
            Required. The version the cluster is going to
            be upgraded to.
        schedule (google.cloud.edgecontainer_v1.types.UpgradeClusterRequest.Schedule):
            The schedule for the upgrade.
        request_id (str):
            A unique identifier for this request. Restricted to 36 ASCII
            characters. A random UUID is recommended. This request is
            only idempotent if ``request_id`` is provided.
    """

    class Schedule(proto.Enum):
        r"""Represents the schedule about when the cluster is going to be
        upgraded.

        Values:
            SCHEDULE_UNSPECIFIED (0):
                Unspecified. The default is to upgrade the
                cluster immediately which is the only option
                today.
            IMMEDIATELY (1):
                The cluster is going to be upgraded
                immediately after receiving the request.
        """

        SCHEDULE_UNSPECIFIED = 0
        IMMEDIATELY = 1

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    target_version: str = proto.Field(
        proto.STRING,
        number=2,
    )
    schedule: Schedule = proto.Field(
        proto.ENUM,
        number=3,
        enum=Schedule,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class DeleteClusterRequest(proto.Message):
    r"""Deletes a cluster.

    Attributes:
        name (str):
            Required. The resource name of the cluster.
        request_id (str):
            A unique identifier for this request. Restricted to 36 ASCII
            characters. A random UUID is recommended. This request is
            only idempotent if ``request_id`` is provided.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GenerateAccessTokenRequest(proto.Message):
    r"""Generates an access token for a cluster.

    Attributes:
        cluster (str):
            Required. The resource name of the cluster.
    """

    cluster: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GenerateAccessTokenResponse(proto.Message):
    r"""An access token for a cluster.

    Attributes:
        access_token (str):
            Output only. Access token to authenticate to
            k8s api-server.
        expire_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp at which the token
            will expire.
    """

    access_token: str = proto.Field(
        proto.STRING,
        number=1,
    )
    expire_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )


class GenerateOfflineCredentialRequest(proto.Message):
    r"""Generates an offline credential(offline) for a cluster.

    Attributes:
        cluster (str):
            Required. The resource name of the cluster.
    """

    cluster: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GenerateOfflineCredentialResponse(proto.Message):
    r"""An offline credential for a cluster.

    Attributes:
        client_certificate (str):
            Output only. Client certificate to
            authenticate to k8s api-server.
        client_key (str):
            Output only. Client private key to
            authenticate to k8s api-server.
        user_id (str):
            Output only. Client's identity.
        expire_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp at which this
            credential will expire.
    """

    client_certificate: str = proto.Field(
        proto.STRING,
        number=1,
    )
    client_key: str = proto.Field(
        proto.STRING,
        number=2,
    )
    user_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    expire_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )


class ListNodePoolsRequest(proto.Message):
    r"""Lists node pools in a cluster.

    Attributes:
        parent (str):
            Required. The parent cluster, which owns this
            collection of node pools.
        page_size (int):
            The maximum number of resources to list.
        page_token (str):
            A page token received from previous list
            request.
        filter (str):
            Only resources matching this filter will be
            listed.
        order_by (str):
            Specifies the order in which resources will
            be listed.
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
        number=4,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListNodePoolsResponse(proto.Message):
    r"""List of node pools in a cluster.

    Attributes:
        node_pools (MutableSequence[google.cloud.edgecontainer_v1.types.NodePool]):
            Node pools in the cluster.
        next_page_token (str):
            A token to retrieve next page of results.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    node_pools: MutableSequence[resources.NodePool] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.NodePool,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetNodePoolRequest(proto.Message):
    r"""Gets a node pool.

    Attributes:
        name (str):
            Required. The resource name of the node pool.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateNodePoolRequest(proto.Message):
    r"""Creates a node pool.

    Attributes:
        parent (str):
            Required. The parent cluster where this node
            pool will be created.
        node_pool_id (str):
            Required. A client-specified unique
            identifier for the node pool.
        node_pool (google.cloud.edgecontainer_v1.types.NodePool):
            Required. The node pool to create.
        request_id (str):
            A unique identifier for this request. Restricted to 36 ASCII
            characters. A random UUID is recommended. This request is
            only idempotent if ``request_id`` is provided.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    node_pool_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    node_pool: resources.NodePool = proto.Field(
        proto.MESSAGE,
        number=3,
        message=resources.NodePool,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateNodePoolRequest(proto.Message):
    r"""Updates a node pool.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Field mask is used to specify the fields to be overwritten
            in the NodePool resource by the update. The fields specified
            in the update_mask are relative to the resource, not the
            full request. A field will be overwritten if it is in the
            mask. If the user does not provide a mask then all fields
            will be overwritten.
        node_pool (google.cloud.edgecontainer_v1.types.NodePool):
            The updated node pool.
        request_id (str):
            A unique identifier for this request. Restricted to 36 ASCII
            characters. A random UUID is recommended. This request is
            only idempotent if ``request_id`` is provided.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    node_pool: resources.NodePool = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.NodePool,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteNodePoolRequest(proto.Message):
    r"""Deletes a node pool.

    Attributes:
        name (str):
            Required. The resource name of the node pool.
        request_id (str):
            A unique identifier for this request. Restricted to 36 ASCII
            characters. A random UUID is recommended. This request is
            only idempotent if ``request_id`` is provided.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListMachinesRequest(proto.Message):
    r"""Lists machines in a site.

    Attributes:
        parent (str):
            Required. The parent site, which owns this
            collection of machines.
        page_size (int):
            The maximum number of resources to list.
        page_token (str):
            A page token received from previous list
            request.
        filter (str):
            Only resources matching this filter will be
            listed.
        order_by (str):
            Specifies the order in which resources will
            be listed.
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
        number=4,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListMachinesResponse(proto.Message):
    r"""List of machines in a site.

    Attributes:
        machines (MutableSequence[google.cloud.edgecontainer_v1.types.Machine]):
            Machines in the site.
        next_page_token (str):
            A token to retrieve next page of results.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    machines: MutableSequence[resources.Machine] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.Machine,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetMachineRequest(proto.Message):
    r"""Gets a machine.

    Attributes:
        name (str):
            Required. The resource name of the machine.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListVpnConnectionsRequest(proto.Message):
    r"""Lists VPN connections.

    Attributes:
        parent (str):
            Required. The parent location, which owns
            this collection of VPN connections.
        page_size (int):
            The maximum number of resources to list.
        page_token (str):
            A page token received from previous list
            request.
        filter (str):
            Only resources matching this filter will be
            listed.
        order_by (str):
            Specifies the order in which resources will
            be listed.
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
        number=4,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListVpnConnectionsResponse(proto.Message):
    r"""List of VPN connections in a location.

    Attributes:
        vpn_connections (MutableSequence[google.cloud.edgecontainer_v1.types.VpnConnection]):
            VpnConnections in the location.
        next_page_token (str):
            A token to retrieve next page of results.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    vpn_connections: MutableSequence[resources.VpnConnection] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.VpnConnection,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetVpnConnectionRequest(proto.Message):
    r"""Gets a VPN connection.

    Attributes:
        name (str):
            Required. The resource name of the vpn
            connection.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateVpnConnectionRequest(proto.Message):
    r"""Creates a VPN connection.

    Attributes:
        parent (str):
            Required. The parent location where this vpn
            connection will be created.
        vpn_connection_id (str):
            Required. The VPN connection identifier.
        vpn_connection (google.cloud.edgecontainer_v1.types.VpnConnection):
            Required. The VPN connection to create.
        request_id (str):
            A unique identifier for this request. Restricted to 36 ASCII
            characters. A random UUID is recommended. This request is
            only idempotent if ``request_id`` is provided.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    vpn_connection_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    vpn_connection: resources.VpnConnection = proto.Field(
        proto.MESSAGE,
        number=3,
        message=resources.VpnConnection,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class DeleteVpnConnectionRequest(proto.Message):
    r"""Deletes a vpn connection.

    Attributes:
        name (str):
            Required. The resource name of the vpn
            connection.
        request_id (str):
            A unique identifier for this request. Restricted to 36 ASCII
            characters. A random UUID is recommended. This request is
            only idempotent if ``request_id`` is provided.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetServerConfigRequest(proto.Message):
    r"""Gets the server config.

    Attributes:
        name (str):
            Required. The name (project and location) of the server
            config to get, specified in the format
            ``projects/*/locations/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
