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

from google.cloud.oracledatabase_v1.types import (
    autonomous_database as gco_autonomous_database,
)
from google.cloud.oracledatabase_v1.types import (
    autonomous_database_character_set,
    autonomous_db_backup,
    autonomous_db_version,
    db_node,
    db_server,
    db_system_shape,
    entitlement,
    exadata_infra,
    gi_version,
    vm_cluster,
)
from google.cloud.oracledatabase_v1.types import (
    exadb_vm_cluster as gco_exadb_vm_cluster,
)

__protobuf__ = proto.module(
    package="google.cloud.oracledatabase.v1",
    manifest={
        "ListCloudExadataInfrastructuresRequest",
        "ListCloudExadataInfrastructuresResponse",
        "GetCloudExadataInfrastructureRequest",
        "CreateCloudExadataInfrastructureRequest",
        "DeleteCloudExadataInfrastructureRequest",
        "ListCloudVmClustersRequest",
        "ListCloudVmClustersResponse",
        "GetCloudVmClusterRequest",
        "CreateCloudVmClusterRequest",
        "DeleteCloudVmClusterRequest",
        "ListEntitlementsRequest",
        "ListEntitlementsResponse",
        "ListDbServersRequest",
        "ListDbServersResponse",
        "ListDbNodesRequest",
        "ListDbNodesResponse",
        "ListGiVersionsRequest",
        "ListGiVersionsResponse",
        "ListDbSystemShapesRequest",
        "ListDbSystemShapesResponse",
        "OperationMetadata",
        "ListAutonomousDatabasesRequest",
        "ListAutonomousDatabasesResponse",
        "GetAutonomousDatabaseRequest",
        "CreateAutonomousDatabaseRequest",
        "UpdateAutonomousDatabaseRequest",
        "DeleteAutonomousDatabaseRequest",
        "RestoreAutonomousDatabaseRequest",
        "StopAutonomousDatabaseRequest",
        "StartAutonomousDatabaseRequest",
        "RestartAutonomousDatabaseRequest",
        "SwitchoverAutonomousDatabaseRequest",
        "FailoverAutonomousDatabaseRequest",
        "GetAutonomousDatabaseRefreshableClonesRequest",
        "AutonomousDatabaseRefreshableClones",
        "RefreshAutonomousDatabaseRequest",
        "GenerateAutonomousDatabaseWalletRequest",
        "GenerateAutonomousDatabaseWalletResponse",
        "ListAutonomousDbVersionsRequest",
        "ListAutonomousDbVersionsResponse",
        "ListAutonomousDatabaseCharacterSetsRequest",
        "ListAutonomousDatabaseCharacterSetsResponse",
        "ListAutonomousDatabaseBackupsRequest",
        "ListAutonomousDatabaseBackupsResponse",
        "CreateExadbVmClusterRequest",
        "DeleteExadbVmClusterRequest",
        "GetExadbVmClusterRequest",
        "ListExadbVmClustersRequest",
        "ListExadbVmClustersResponse",
        "UpdateExadbVmClusterRequest",
        "RemoveVirtualMachineExadbVmClusterRequest",
    },
)


class ListCloudExadataInfrastructuresRequest(proto.Message):
    r"""The request for ``CloudExadataInfrastructures.List``.

    Attributes:
        parent (str):
            Required. The parent value for
            CloudExadataInfrastructure in the following
            format: projects/{project}/locations/{location}.
        page_size (int):
            Optional. The maximum number of items to
            return. If unspecified, at most 50 Exadata
            infrastructures will be returned. The maximum
            value is 1000; values above 1000 will be coerced
            to 1000.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
        filter (str):
            Optional. An expression for filtering the
            results of the request.
        order_by (str):
            Optional. An expression for ordering the
            results of the request.
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


class ListCloudExadataInfrastructuresResponse(proto.Message):
    r"""The response for ``CloudExadataInfrastructures.list``.

    Attributes:
        cloud_exadata_infrastructures (MutableSequence[google.cloud.oracledatabase_v1.types.CloudExadataInfrastructure]):
            The list of Exadata Infrastructures.
        next_page_token (str):
            A token for fetching next page of response.
        unreachable (MutableSequence[str]):
            Unreachable locations when listing resources
            across all locations using wildcard location
            '-'.
    """

    @property
    def raw_page(self):
        return self

    cloud_exadata_infrastructures: MutableSequence[
        exadata_infra.CloudExadataInfrastructure
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=exadata_infra.CloudExadataInfrastructure,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetCloudExadataInfrastructureRequest(proto.Message):
    r"""The request for ``CloudExadataInfrastructure.Get``.

    Attributes:
        name (str):
            Required. The name of the Cloud Exadata Infrastructure in
            the following format:
            projects/{project}/locations/{location}/cloudExadataInfrastructures/{cloud_exadata_infrastructure}.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateCloudExadataInfrastructureRequest(proto.Message):
    r"""The request for ``CloudExadataInfrastructure.Create``.

    Attributes:
        parent (str):
            Required. The parent value for
            CloudExadataInfrastructure in the following
            format: projects/{project}/locations/{location}.
        cloud_exadata_infrastructure_id (str):
            Required. The ID of the Exadata Infrastructure to create.
            This value is restricted to
            (^\ `a-z <[a-z0-9-]{0,61}[a-z0-9]>`__?$) and must be a
            maximum of 63 characters in length. The value must start
            with a letter and end with a letter or a number.
        cloud_exadata_infrastructure (google.cloud.oracledatabase_v1.types.CloudExadataInfrastructure):
            Required. Details of the Exadata
            Infrastructure instance to create.
        request_id (str):
            Optional. An optional ID to identify the
            request. This value is used to identify
            duplicate requests. If you make a request with
            the same request ID and the original request is
            still in progress or completed, the server
            ignores the second request. This prevents
            clients from accidentally creating duplicate
            commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    cloud_exadata_infrastructure_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    cloud_exadata_infrastructure: exadata_infra.CloudExadataInfrastructure = (
        proto.Field(
            proto.MESSAGE,
            number=3,
            message=exadata_infra.CloudExadataInfrastructure,
        )
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class DeleteCloudExadataInfrastructureRequest(proto.Message):
    r"""The request for ``CloudExadataInfrastructure.Delete``.

    Attributes:
        name (str):
            Required. The name of the Cloud Exadata Infrastructure in
            the following format:
            projects/{project}/locations/{location}/cloudExadataInfrastructures/{cloud_exadata_infrastructure}.
        request_id (str):
            Optional. An optional ID to identify the
            request. This value is used to identify
            duplicate requests. If you make a request with
            the same request ID and the original request is
            still in progress or completed, the server
            ignores the second request. This prevents
            clients from accidentally creating duplicate
            commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        force (bool):
            Optional. If set to true, all VM clusters for
            this Exadata Infrastructure will be deleted. An
            Exadata Infrastructure can only be deleted once
            all its VM clusters have been deleted.
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


class ListCloudVmClustersRequest(proto.Message):
    r"""The request for ``CloudVmCluster.List``.

    Attributes:
        parent (str):
            Required. The name of the parent in the
            following format:
            projects/{project}/locations/{location}.
        page_size (int):
            Optional. The number of VM clusters to
            return. If unspecified, at most 50 VM clusters
            will be returned. The maximum value is 1,000.
        page_token (str):
            Optional. A token identifying the page of
            results the server returns.
        filter (str):
            Optional. An expression for filtering the
            results of the request.
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


class ListCloudVmClustersResponse(proto.Message):
    r"""The response for ``CloudVmCluster.List``.

    Attributes:
        cloud_vm_clusters (MutableSequence[google.cloud.oracledatabase_v1.types.CloudVmCluster]):
            The list of VM Clusters.
        next_page_token (str):
            A token to fetch the next page of results.
        unreachable (MutableSequence[str]):
            Unreachable locations when listing resources
            across all locations using wildcard location
            '-'.
    """

    @property
    def raw_page(self):
        return self

    cloud_vm_clusters: MutableSequence[vm_cluster.CloudVmCluster] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=vm_cluster.CloudVmCluster,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetCloudVmClusterRequest(proto.Message):
    r"""The request for ``CloudVmCluster.Get``.

    Attributes:
        name (str):
            Required. The name of the Cloud VM Cluster in the following
            format:
            projects/{project}/locations/{location}/cloudVmClusters/{cloud_vm_cluster}.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateCloudVmClusterRequest(proto.Message):
    r"""The request for ``CloudVmCluster.Create``.

    Attributes:
        parent (str):
            Required. The name of the parent in the
            following format:
            projects/{project}/locations/{location}.
        cloud_vm_cluster_id (str):
            Required. The ID of the VM Cluster to create. This value is
            restricted to (^\ `a-z <[a-z0-9-]{0,61}[a-z0-9]>`__?$) and
            must be a maximum of 63 characters in length. The value must
            start with a letter and end with a letter or a number.
        cloud_vm_cluster (google.cloud.oracledatabase_v1.types.CloudVmCluster):
            Required. The resource being created
        request_id (str):
            Optional. An optional ID to identify the
            request. This value is used to identify
            duplicate requests. If you make a request with
            the same request ID and the original request is
            still in progress or completed, the server
            ignores the second request. This prevents
            clients from accidentally creating duplicate
            commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    cloud_vm_cluster_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    cloud_vm_cluster: vm_cluster.CloudVmCluster = proto.Field(
        proto.MESSAGE,
        number=3,
        message=vm_cluster.CloudVmCluster,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class DeleteCloudVmClusterRequest(proto.Message):
    r"""The request for ``CloudVmCluster.Delete``.

    Attributes:
        name (str):
            Required. The name of the Cloud VM Cluster in the following
            format:
            projects/{project}/locations/{location}/cloudVmClusters/{cloud_vm_cluster}.
        request_id (str):
            Optional. An optional ID to identify the
            request. This value is used to identify
            duplicate requests. If you make a request with
            the same request ID and the original request is
            still in progress or completed, the server
            ignores the second request. This prevents
            clients from accidentally creating duplicate
            commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        force (bool):
            Optional. If set to true, all child resources
            for the VM Cluster will be deleted. A VM Cluster
            can only be deleted once all its child resources
            have been deleted.
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


class ListEntitlementsRequest(proto.Message):
    r"""The request for ``Entitlement.List``.

    Attributes:
        parent (str):
            Required. The parent value for the
            entitlement in the following format:
            projects/{project}/locations/{location}.
        page_size (int):
            Optional. The maximum number of items to
            return. If unspecified, a maximum of 50
            entitlements will be returned. The maximum value
            is 1000.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
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


class ListEntitlementsResponse(proto.Message):
    r"""The response for ``Entitlement.List``.

    Attributes:
        entitlements (MutableSequence[google.cloud.oracledatabase_v1.types.Entitlement]):
            The list of Entitlements
        next_page_token (str):
            A token identifying a page of results the
            server should return.
    """

    @property
    def raw_page(self):
        return self

    entitlements: MutableSequence[entitlement.Entitlement] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=entitlement.Entitlement,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListDbServersRequest(proto.Message):
    r"""The request for ``DbServer.List``.

    Attributes:
        parent (str):
            Required. The parent value for database
            server in the following format:
            projects/{project}/locations/{location}/cloudExadataInfrastructures/{cloudExadataInfrastructure}.
        page_size (int):
            Optional. The maximum number of items to
            return. If unspecified, a maximum of 50 db
            servers will be returned. The maximum value is
            1000; values above 1000 will be reset to 1000.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
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


class ListDbServersResponse(proto.Message):
    r"""The response for ``DbServer.List``.

    Attributes:
        db_servers (MutableSequence[google.cloud.oracledatabase_v1.types.DbServer]):
            The list of database servers.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
    """

    @property
    def raw_page(self):
        return self

    db_servers: MutableSequence[db_server.DbServer] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=db_server.DbServer,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListDbNodesRequest(proto.Message):
    r"""The request for ``DbNode.List``.

    Attributes:
        parent (str):
            Required. The parent value for database node
            in the following format:
            projects/{project}/locations/{location}/cloudVmClusters/{cloudVmCluster}.
            .
        page_size (int):
            Optional. The maximum number of items to
            return. If unspecified, at most 50 db nodes will
            be returned. The maximum value is 1000; values
            above 1000 will be coerced to 1000.
        page_token (str):
            Optional. A token identifying a page of
            results the node should return.
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


class ListDbNodesResponse(proto.Message):
    r"""The response for ``DbNode.List``.

    Attributes:
        db_nodes (MutableSequence[google.cloud.oracledatabase_v1.types.DbNode]):
            The list of DB Nodes
        next_page_token (str):
            A token identifying a page of results the
            node should return.
    """

    @property
    def raw_page(self):
        return self

    db_nodes: MutableSequence[db_node.DbNode] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=db_node.DbNode,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListGiVersionsRequest(proto.Message):
    r"""The request for ``GiVersion.List``.

    Attributes:
        parent (str):
            Required. The parent value for Grid
            Infrastructure Version in the following format:
            Format: projects/{project}/locations/{location}.
        page_size (int):
            Optional. The maximum number of items to
            return. If unspecified, a maximum of 50 Oracle
            Grid Infrastructure (GI) versions will be
            returned. The maximum value is 1000; values
            above 1000 will be reset to 1000.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
        filter (str):
            Optional. An expression for filtering the results of the
            request. Only the ``shape`` and ``gcp_oracle_zone_id``
            fields are supported in the following format:
            ``shape="{shape}" AND gcp_oracle_zone_id="{gcp_oracle_zone_id}"``.
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


class ListGiVersionsResponse(proto.Message):
    r"""The response for ``GiVersion.List``.

    Attributes:
        gi_versions (MutableSequence[google.cloud.oracledatabase_v1.types.GiVersion]):
            The list of Oracle Grid Infrastructure (GI)
            versions.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
    """

    @property
    def raw_page(self):
        return self

    gi_versions: MutableSequence[gi_version.GiVersion] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gi_version.GiVersion,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListDbSystemShapesRequest(proto.Message):
    r"""The request for ``DbSystemShape.List``.

    Attributes:
        parent (str):
            Required. The parent value for Database
            System Shapes in the following format:
            projects/{project}/locations/{location}.
        page_size (int):
            Optional. The maximum number of items to
            return. If unspecified, at most 50 database
            system shapes will be returned. The maximum
            value is 1000; values above 1000 will be coerced
            to 1000.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
        filter (str):
            Optional. An expression for filtering the results of the
            request. The ``gcp_oracle_zone_id``, ``shape_family``, and
            ``database_edition`` fields are supported in the following
            format:
            ``gcp_oracle_zone_id="{gcp_oracle_zone_id}" AND shape_family="{shape_family}" AND database_edition="{database_edition}"``.
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


class ListDbSystemShapesResponse(proto.Message):
    r"""The response for ``DbSystemShape.List``.

    Attributes:
        db_system_shapes (MutableSequence[google.cloud.oracledatabase_v1.types.DbSystemShape]):
            The list of Database System shapes.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
    """

    @property
    def raw_page(self):
        return self

    db_system_shapes: MutableSequence[db_system_shape.DbSystemShape] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=db_system_shape.DbSystemShape,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
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
            Output only. The status of the operation.
        requested_cancellation (bool):
            Output only. Identifies whether the user has requested
            cancellation of the operation. Operations that have been
            cancelled successfully have [Operation.error][] value with a
            [google.rpc.Status.code][google.rpc.Status.code] of 1,
            corresponding to ``Code.CANCELLED``.
        api_version (str):
            Output only. API version used to start the
            operation.
        percent_complete (float):
            Output only. An estimated percentage of the
            operation that has been completed at a given
            moment of time, between 0 and 100.
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
    percent_complete: float = proto.Field(
        proto.DOUBLE,
        number=8,
    )


class ListAutonomousDatabasesRequest(proto.Message):
    r"""The request for ``AutonomousDatabase.List``.

    Attributes:
        parent (str):
            Required. The parent value for the Autonomous
            Database in the following format:
            projects/{project}/locations/{location}.
        page_size (int):
            Optional. The maximum number of items to
            return. If unspecified, at most 50 Autonomous
            Database will be returned. The maximum value is
            1000; values above 1000 will be coerced to 1000.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
        filter (str):
            Optional. An expression for filtering the
            results of the request.
        order_by (str):
            Optional. An expression for ordering the
            results of the request.
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


class ListAutonomousDatabasesResponse(proto.Message):
    r"""The response for ``AutonomousDatabase.List``.

    Attributes:
        autonomous_databases (MutableSequence[google.cloud.oracledatabase_v1.types.AutonomousDatabase]):
            The list of Autonomous Databases.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Unreachable locations when listing resources
            across all locations using wildcard location
            '-'.
    """

    @property
    def raw_page(self):
        return self

    autonomous_databases: MutableSequence[
        gco_autonomous_database.AutonomousDatabase
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gco_autonomous_database.AutonomousDatabase,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetAutonomousDatabaseRequest(proto.Message):
    r"""The request for ``AutonomousDatabase.Get``.

    Attributes:
        name (str):
            Required. The name of the Autonomous Database in the
            following format:
            projects/{project}/locations/{location}/autonomousDatabases/{autonomous_database}.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateAutonomousDatabaseRequest(proto.Message):
    r"""The request for ``AutonomousDatabase.Create``.

    Attributes:
        parent (str):
            Required. The name of the parent in the
            following format:
            projects/{project}/locations/{location}.
        autonomous_database_id (str):
            Required. The ID of the Autonomous Database to create. This
            value is restricted to
            (^\ `a-z <[a-z0-9-]{0,61}[a-z0-9]>`__?$) and must be a
            maximum of 63 characters in length. The value must start
            with a letter and end with a letter or a number.
        autonomous_database (google.cloud.oracledatabase_v1.types.AutonomousDatabase):
            Required. The Autonomous Database being
            created.
        request_id (str):
            Optional. An optional ID to identify the
            request. This value is used to identify
            duplicate requests. If you make a request with
            the same request ID and the original request is
            still in progress or completed, the server
            ignores the second request. This prevents
            clients from accidentally creating duplicate
            commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    autonomous_database_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    autonomous_database: gco_autonomous_database.AutonomousDatabase = proto.Field(
        proto.MESSAGE,
        number=3,
        message=gco_autonomous_database.AutonomousDatabase,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateAutonomousDatabaseRequest(proto.Message):
    r"""The request for ``AutonomousDatabase.Update``.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the fields to be
            overwritten in the Exadata resource by the update. The
            fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask. If the user does not provide a mask
            then all fields will be overwritten.
        autonomous_database (google.cloud.oracledatabase_v1.types.AutonomousDatabase):
            Required. The resource being updated
        request_id (str):
            Optional. An optional ID to identify the
            request. This value is used to identify
            duplicate requests. If you make a request with
            the same request ID and the original request is
            still in progress or completed, the server
            ignores the second request. This prevents
            clients from accidentally creating duplicate
            commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    autonomous_database: gco_autonomous_database.AutonomousDatabase = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gco_autonomous_database.AutonomousDatabase,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteAutonomousDatabaseRequest(proto.Message):
    r"""The request for ``AutonomousDatabase.Delete``.

    Attributes:
        name (str):
            Required. The name of the resource in the following format:
            projects/{project}/locations/{location}/autonomousDatabases/{autonomous_database}.
        request_id (str):
            Optional. An optional ID to identify the
            request. This value is used to identify
            duplicate requests. If you make a request with
            the same request ID and the original request is
            still in progress or completed, the server
            ignores the second request. This prevents
            clients from accidentally creating duplicate
            commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class RestoreAutonomousDatabaseRequest(proto.Message):
    r"""The request for ``AutonomousDatabase.Restore``.

    Attributes:
        name (str):
            Required. The name of the Autonomous Database in the
            following format:
            projects/{project}/locations/{location}/autonomousDatabases/{autonomous_database}.
        restore_time (google.protobuf.timestamp_pb2.Timestamp):
            Required. The time and date to restore the
            database to.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    restore_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )


class StopAutonomousDatabaseRequest(proto.Message):
    r"""The request for ``AutonomousDatabase.Stop``.

    Attributes:
        name (str):
            Required. The name of the Autonomous Database in the
            following format:
            projects/{project}/locations/{location}/autonomousDatabases/{autonomous_database}.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class StartAutonomousDatabaseRequest(proto.Message):
    r"""The request for ``AutonomousDatabase.Start``.

    Attributes:
        name (str):
            Required. The name of the Autonomous Database in the
            following format:
            projects/{project}/locations/{location}/autonomousDatabases/{autonomous_database}.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class RestartAutonomousDatabaseRequest(proto.Message):
    r"""The request for ``AutonomousDatabase.Restart``.

    Attributes:
        name (str):
            Required. The name of the Autonomous Database in the
            following format:
            projects/{project}/locations/{location}/autonomousDatabases/{autonomous_database}.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class SwitchoverAutonomousDatabaseRequest(proto.Message):
    r"""The request for ``OracleDatabase.SwitchoverAutonomousDatabase``.

    Attributes:
        name (str):
            Required. The name of the Autonomous Database in the
            following format:
            projects/{project}/locations/{location}/autonomousDatabases/{autonomous_database}.
        peer_autonomous_database (str):
            Optional. The peer database name to switch
            over to. Required for cross-region standby, and
            must be omitted for in-region Data Guard.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    peer_autonomous_database: str = proto.Field(
        proto.STRING,
        number=2,
    )


class FailoverAutonomousDatabaseRequest(proto.Message):
    r"""The request for ``OracleDatabase.FailoverAutonomousDatabase``.

    Attributes:
        name (str):
            Required. The name of the Autonomous Database in the
            following format:
            projects/{project}/locations/{location}/autonomousDatabases/{autonomous_database}.
        peer_autonomous_database (str):
            Optional. The peer database name to fail over
            to. Required for cross-region standby, and must
            be omitted for in-region Data Guard.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    peer_autonomous_database: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetAutonomousDatabaseRefreshableClonesRequest(proto.Message):
    r"""Request message for getting refreshable clones for an
    Autonomous Database.

    Attributes:
        name (str):
            Required. The Autonomous Database resource whose refreshable
            clones are to be listed. Format:
            projects/{project}/locations/{location}/autonomousDatabases/{autonomous_database}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class AutonomousDatabaseRefreshableClones(proto.Message):
    r"""Response message for getting the Autonomous Database
    refreshable clones.

    Attributes:
        autonomous_database_refreshable_clones (MutableSequence[google.cloud.oracledatabase_v1.types.AutonomousDatabaseRefreshableClone]):
            The list of Autonomous Database refreshable
            clones.
    """

    autonomous_database_refreshable_clones: MutableSequence[
        gco_autonomous_database.AutonomousDatabaseRefreshableClone
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gco_autonomous_database.AutonomousDatabaseRefreshableClone,
    )


class RefreshAutonomousDatabaseRequest(proto.Message):
    r"""Request message for RefreshAutonomousDatabase method.

    Attributes:
        name (str):
            Required. The name of the AutonomousDatabase resource.
            Format:
            projects/{project}/location/{location}/autonomousDatabases/{autonomous_database}
        refresh_cutoff_time (google.protobuf.timestamp_pb2.Timestamp):
            Required. The timestamp to which the
            Autonomous Database refreshable clone will be
            refreshed. Changes made in the primary database
            after this timestamp are not part of the data
            refresh.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    refresh_cutoff_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )


class GenerateAutonomousDatabaseWalletRequest(proto.Message):
    r"""The request for ``AutonomousDatabase.GenerateWallet``.

    Attributes:
        name (str):
            Required. The name of the Autonomous Database in the
            following format:
            projects/{project}/locations/{location}/autonomousDatabases/{autonomous_database}.
        type_ (google.cloud.oracledatabase_v1.types.GenerateType):
            Optional. The type of wallet generation for
            the Autonomous Database. The default value is
            SINGLE.
        is_regional (bool):
            Optional. True when requesting regional
            connection strings in PDB connect info,
            applicable to cross-region Data Guard only.
        password (str):
            Required. The password used to encrypt the
            keys inside the wallet. The password must be a
            minimum of 8 characters.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    type_: gco_autonomous_database.GenerateType = proto.Field(
        proto.ENUM,
        number=2,
        enum=gco_autonomous_database.GenerateType,
    )
    is_regional: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    password: str = proto.Field(
        proto.STRING,
        number=4,
    )


class GenerateAutonomousDatabaseWalletResponse(proto.Message):
    r"""The response for ``AutonomousDatabase.GenerateWallet``.

    Attributes:
        archive_content (bytes):
            Output only. The base64 encoded wallet files.
    """

    archive_content: bytes = proto.Field(
        proto.BYTES,
        number=1,
    )


class ListAutonomousDbVersionsRequest(proto.Message):
    r"""The request for ``AutonomousDbVersion.List``.

    Attributes:
        parent (str):
            Required. The parent value for the Autonomous
            Database in the following format:
            projects/{project}/locations/{location}.
        page_size (int):
            Optional. The maximum number of items to
            return. If unspecified, at most 50 Autonomous DB
            Versions will be returned. The maximum value is
            1000; values above 1000 will be coerced to 1000.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
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


class ListAutonomousDbVersionsResponse(proto.Message):
    r"""The response for ``AutonomousDbVersion.List``.

    Attributes:
        autonomous_db_versions (MutableSequence[google.cloud.oracledatabase_v1.types.AutonomousDbVersion]):
            The list of Autonomous Database versions.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
    """

    @property
    def raw_page(self):
        return self

    autonomous_db_versions: MutableSequence[
        autonomous_db_version.AutonomousDbVersion
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=autonomous_db_version.AutonomousDbVersion,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListAutonomousDatabaseCharacterSetsRequest(proto.Message):
    r"""The request for ``AutonomousDatabaseCharacterSet.List``.

    Attributes:
        parent (str):
            Required. The parent value for the Autonomous
            Database in the following format:
            projects/{project}/locations/{location}.
        page_size (int):
            Optional. The maximum number of items to
            return. If unspecified, at most 50 Autonomous DB
            Character Sets will be returned. The maximum
            value is 1000; values above 1000 will be coerced
            to 1000.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
        filter (str):
            Optional. An expression for filtering the results of the
            request. Only the **character_set_type** field is supported
            in the following format:
            ``character_set_type="{characterSetType}"``. Accepted values
            include ``DATABASE`` and ``NATIONAL``.
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


class ListAutonomousDatabaseCharacterSetsResponse(proto.Message):
    r"""The response for ``AutonomousDatabaseCharacterSet.List``.

    Attributes:
        autonomous_database_character_sets (MutableSequence[google.cloud.oracledatabase_v1.types.AutonomousDatabaseCharacterSet]):
            The list of Autonomous Database Character
            Sets.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
    """

    @property
    def raw_page(self):
        return self

    autonomous_database_character_sets: MutableSequence[
        autonomous_database_character_set.AutonomousDatabaseCharacterSet
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=autonomous_database_character_set.AutonomousDatabaseCharacterSet,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListAutonomousDatabaseBackupsRequest(proto.Message):
    r"""The request for ``AutonomousDatabaseBackup.List``.

    Attributes:
        parent (str):
            Required. The parent value for
            ListAutonomousDatabaseBackups in the following
            format: projects/{project}/locations/{location}.
        filter (str):
            Optional. An expression for filtering the results of the
            request. Only the **autonomous_database_id** field is
            supported in the following format:
            ``autonomous_database_id="{autonomous_database_id}"``. The
            accepted values must be a valid Autonomous Database ID,
            limited to the naming restrictions of the ID:
            ^\ `a-z <[a-z0-9-]{0,61}[a-z0-9]>`__?$). The ID must start
            with a letter, end with a letter or a number, and be a
            maximum of 63 characters.
        page_size (int):
            Optional. The maximum number of items to
            return. If unspecified, at most 50 Autonomous DB
            Backups will be returned. The maximum value is
            1000; values above 1000 will be coerced to 1000.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=5,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListAutonomousDatabaseBackupsResponse(proto.Message):
    r"""The response for ``AutonomousDatabaseBackup.List``.

    Attributes:
        autonomous_database_backups (MutableSequence[google.cloud.oracledatabase_v1.types.AutonomousDatabaseBackup]):
            The list of Autonomous Database Backups.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
    """

    @property
    def raw_page(self):
        return self

    autonomous_database_backups: MutableSequence[
        autonomous_db_backup.AutonomousDatabaseBackup
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=autonomous_db_backup.AutonomousDatabaseBackup,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreateExadbVmClusterRequest(proto.Message):
    r"""The request for ``ExadbVmCluster.Create``.

    Attributes:
        parent (str):
            Required. The value for parent of the
            ExadbVmCluster in the following format:
            projects/{project}/locations/{location}.
        exadb_vm_cluster_id (str):
            Required. The ID of the ExadbVmCluster to create. This value
            is restricted to (^\ `a-z <[a-z0-9-]{0,61}[a-z0-9]>`__?$)
            and must be a maximum of 63 characters in length. The value
            must start with a letter and end with a letter or a number.
        exadb_vm_cluster (google.cloud.oracledatabase_v1.types.ExadbVmCluster):
            Required. The resource being created.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    exadb_vm_cluster_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    exadb_vm_cluster: gco_exadb_vm_cluster.ExadbVmCluster = proto.Field(
        proto.MESSAGE,
        number=3,
        message=gco_exadb_vm_cluster.ExadbVmCluster,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class DeleteExadbVmClusterRequest(proto.Message):
    r"""The request for ``ExadbVmCluster.Delete``.

    Attributes:
        name (str):
            Required. The name of the ExadbVmCluster in the following
            format:
            projects/{project}/locations/{location}/exadbVmClusters/{exadb_vm_cluster}.
        request_id (str):
            Optional. An optional ID to identify the
            request. This value is used to identify
            duplicate requests. If you make a request with
            the same request ID and the original request is
            still in progress or completed, the server
            ignores the second request. This prevents
            clients from accidentally creating duplicate
            commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetExadbVmClusterRequest(proto.Message):
    r"""The request for ``ExadbVmCluster.Get``.

    Attributes:
        name (str):
            Required. The name of the ExadbVmCluster in the following
            format:
            projects/{project}/locations/{location}/exadbVmClusters/{exadb_vm_cluster}.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListExadbVmClustersRequest(proto.Message):
    r"""The request for ``ExadbVmCluster.List``.

    Attributes:
        parent (str):
            Required. The parent value for
            ExadbVmClusters in the following format:
            projects/{project}/locations/{location}.
        page_size (int):
            Optional. The maximum number of items to
            return. If unspecified, at most 50
            ExadbVmClusters will be returned. The maximum
            value is 1000; values above 1000 will be coerced
            to 1000.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
        filter (str):
            Optional. An expression for filtering the
            results of the request.
        order_by (str):
            Optional. An expression for ordering the
            results of the request.
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


class ListExadbVmClustersResponse(proto.Message):
    r"""The response for ``ExadbVmCluster.List``.

    Attributes:
        exadb_vm_clusters (MutableSequence[google.cloud.oracledatabase_v1.types.ExadbVmCluster]):
            The list of ExadbVmClusters.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Unreachable locations when listing resources
            across all locations using wildcard location
            '-'.
    """

    @property
    def raw_page(self):
        return self

    exadb_vm_clusters: MutableSequence[gco_exadb_vm_cluster.ExadbVmCluster] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=gco_exadb_vm_cluster.ExadbVmCluster,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class UpdateExadbVmClusterRequest(proto.Message):
    r"""The request for ``ExadbVmCluster.Update``. We only support adding
    the Virtual Machine to the ExadbVmCluster. Rest of the fields in
    ExadbVmCluster are immutable.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. A mask specifying which fields in
            th VM Cluster should be updated. A field
            specified in the mask is overwritten. If a mask
            isn't provided then all the fields in the VM
            Cluster are overwritten.
        exadb_vm_cluster (google.cloud.oracledatabase_v1.types.ExadbVmCluster):
            Required. The resource being updated.
        request_id (str):
            Optional. An optional ID to identify the
            request. This value is used to identify
            duplicate requests. If you make a request with
            the same request ID and the original request is
            still in progress or completed, the server
            ignores the second request. This prevents
            clients from accidentally creating duplicate
            commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    exadb_vm_cluster: gco_exadb_vm_cluster.ExadbVmCluster = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gco_exadb_vm_cluster.ExadbVmCluster,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class RemoveVirtualMachineExadbVmClusterRequest(proto.Message):
    r"""The request for ``ExadbVmCluster.RemoveVirtualMachine``.

    Attributes:
        name (str):
            Required. The name of the ExadbVmCluster in the following
            format:
            projects/{project}/locations/{location}/exadbVmClusters/{exadb_vm_cluster}.
        request_id (str):
            Optional. An optional ID to identify the
            request. This value is used to identify
            duplicate requests. If you make a request with
            the same request ID and the original request is
            still in progress or completed, the server
            ignores the second request. This prevents
            clients from accidentally creating duplicate
            commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        hostnames (MutableSequence[str]):
            Required. The list of host names of db nodes
            to be removed from the ExadbVmCluster.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    hostnames: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
