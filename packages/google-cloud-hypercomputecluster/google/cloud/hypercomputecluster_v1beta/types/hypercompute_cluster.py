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

__protobuf__ = proto.module(
    package="google.cloud.hypercomputecluster.v1beta",
    manifest={
        "Cluster",
        "ListClustersRequest",
        "ListClustersResponse",
        "GetClusterRequest",
        "CreateClusterRequest",
        "UpdateClusterRequest",
        "DeleteClusterRequest",
        "ListNodesRequest",
        "ListNodesResponse",
        "NetworkResource",
        "NetworkReference",
        "NetworkResourceConfig",
        "NewNetworkConfig",
        "ExistingNetworkConfig",
        "StorageResource",
        "FilestoreReference",
        "BucketReference",
        "LustreReference",
        "StorageResourceConfig",
        "NewFilestoreConfig",
        "FileShareConfig",
        "ExistingFilestoreConfig",
        "NewBucketConfig",
        "GcsAutoclassConfig",
        "GcsHierarchicalNamespaceConfig",
        "ExistingBucketConfig",
        "NewLustreConfig",
        "ExistingLustreConfig",
        "ExistingNfsConfig",
        "ComputeResource",
        "ComputeResourceConfig",
        "NewOnDemandInstancesConfig",
        "NewSpotInstancesConfig",
        "NewReservedInstancesConfig",
        "NewFlexStartInstancesConfig",
        "BootDisk",
        "Orchestrator",
        "SlurmOrchestrator",
        "SlurmNodeSet",
        "ComputeInstanceSlurmNodeSet",
        "ResourcePolicyConfig",
        "SlurmPartition",
        "SlurmLoginNodes",
        "ServiceAccount",
        "StorageConfig",
        "ComputeInstance",
        "Node",
        "SlurmNodeDetails",
        "ComputeEngineNodeDetails",
        "ComputeEngineOrchestrator",
        "ManagedInstanceGroup",
        "Disk",
        "ExistingInstances",
    },
)


class Cluster(proto.Message):
    r"""A collection of virtual machines and connected resources
    forming a high-performance computing cluster capable of running
    large-scale, tightly coupled workloads. A cluster combines a set
    a compute resources that perform computations, storage resources
    that contain inputs and store outputs, an orchestrator that is
    responsible for assigning jobs to compute resources, and network
    resources that connect everything together.

    Attributes:
        name (str):
            Identifier. `Relative resource
            name <https://google.aip.dev/122>`__ of the cluster, in the
            format
            ``projects/{project}/locations/{location}/clusters/{cluster}``.
        description (str):
            Optional. A description for your cluster. You
            can use up to 2,048 characters.
        labels (MutableMapping[str, str]):
            Optional.
            `Labels <https://cloud.google.com/compute/docs/labeling-resources>`__
            applied to the cluster. Labels can be used to organize
            clusters and to filter them in queries.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time that the cluster was
            originally created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time that the cluster was most
            recently updated.
        reconciling (bool):
            Output only. Indicates whether changes to the cluster are
            currently in flight. If this is ``true``, then the current
            state might not match the cluster's intended state.
        network_resources (MutableMapping[str, google.cloud.hypercomputecluster_v1beta.types.NetworkResource]):
            Optional. Network resources available to the cluster. Must
            contain exactly one value. Keys specify the ID of the
            network resource by which it can be referenced elsewhere,
            and must conform to
            `RFC-1034 <https://datatracker.ietf.org/doc/html/rfc1034>`__
            (lower-case, alphanumeric, and at most 63 characters).
        storage_resources (MutableMapping[str, google.cloud.hypercomputecluster_v1beta.types.StorageResource]):
            Optional. Storage resources available to the cluster. Keys
            specify the ID of the storage resource by which it can be
            referenced elsewhere, and must conform to
            `RFC-1034 <https://datatracker.ietf.org/doc/html/rfc1034>`__
            (lower-case, alphanumeric, and at most 63 characters).
        compute_resources (MutableMapping[str, google.cloud.hypercomputecluster_v1beta.types.ComputeResource]):
            Optional. Compute resources available to the cluster. Keys
            specify the ID of the compute resource by which it can be
            referenced elsewhere, and must conform to
            `RFC-1034 <https://datatracker.ietf.org/doc/html/rfc1034>`__
            (lower-case, alphanumeric, and at most 63 characters).
        orchestrator (google.cloud.hypercomputecluster_v1beta.types.Orchestrator):
            Optional. Orchestrator that is responsible
            for scheduling and running jobs on the cluster.
        uid (str):
            Output only. The globally unique identifier
            for this Cluster.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=9,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    reconciling: bool = proto.Field(
        proto.BOOL,
        number=10,
    )
    network_resources: MutableMapping[str, "NetworkResource"] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=11,
        message="NetworkResource",
    )
    storage_resources: MutableMapping[str, "StorageResource"] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=12,
        message="StorageResource",
    )
    compute_resources: MutableMapping[str, "ComputeResource"] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=13,
        message="ComputeResource",
    )
    orchestrator: "Orchestrator" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="Orchestrator",
    )
    uid: str = proto.Field(
        proto.STRING,
        number=16,
    )


class ListClustersRequest(proto.Message):
    r"""Request message for
    [ListClusters][google.cloud.hypercomputecluster.v1beta.HypercomputeCluster.ListClusters].

    Attributes:
        parent (str):
            Required. Parent location of the clusters to list, in the
            format ``projects/{project}/locations/{location}``.
        page_size (int):
            Optional. Maximum number of clusters to
            return. The service may return fewer than this
            value.
        page_token (str):
            Optional. A page token received from a previous
            ``ListClusters`` call. Provide this to retrieve the
            subsequent page. When paginating, all other parameters
            provided to ``ListClusters`` must match the call that
            provided the page token.
        filter (str):
            Optional. `Filter <https://google.aip.dev/160>`__ to apply
            to the returned results.
        order_by (str):
            Optional. How to order the resulting clusters. Must be one
            of the following strings:

            - ``name``
            - ``name desc``
            - ``create_time``
            - ``create_time desc``

            If not specified, clusters will be returned in an arbitrary
            order.
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
    r"""Response message for
    [ListClusters][google.cloud.hypercomputecluster.v1beta.HypercomputeCluster.ListClusters].

    Attributes:
        clusters (MutableSequence[google.cloud.hypercomputecluster_v1beta.types.Cluster]):
            Clusters in the specified location.
        next_page_token (str):
            A token that can be sent as ``page_token`` to retrieve the
            next page. If this field is absent, there are no subsequent
            pages.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    clusters: MutableSequence["Cluster"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Cluster",
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
    r"""Request message for
    [GetCluster][google.cloud.hypercomputecluster.v1beta.HypercomputeCluster.GetCluster].

    Attributes:
        name (str):
            Required. Name of the cluster to retrieve, in the format
            ``projects/{project}/locations/{location}/clusters/{cluster}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateClusterRequest(proto.Message):
    r"""Request message for
    [CreateCluster][google.cloud.hypercomputecluster.v1beta.HypercomputeCluster.CreateCluster].

    Attributes:
        parent (str):
            Required. Parent location in which the cluster should be
            created, in the format
            ``projects/{project}/locations/{location}``.
        cluster_id (str):
            Required. The ID of the cluster to create. The cluster ID
            must start with a lowercase letter (``a``-``z``), use only
            lowercase letters or numbers, and contain up to 10
            characters. For example, specify ``cluster001``.
        cluster (google.cloud.hypercomputecluster_v1beta.types.Cluster):
            Required. Cluster to create.
        request_id (str):
            Optional. A unique identifier for this request. A random
            UUID is recommended. This request is idempotent if and only
            if ``request_id`` is provided.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    cluster_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    cluster: "Cluster" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Cluster",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateClusterRequest(proto.Message):
    r"""Request message for
    [UpdateCluster][google.cloud.hypercomputecluster.v1beta.HypercomputeCluster.UpdateCluster].

    Attributes:
        cluster (google.cloud.hypercomputecluster_v1beta.types.Cluster):
            Required. Cluster to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Mask specifying which fields in the
            cluster to update. All paths must be specified
            explicitly - wildcards are not supported. At
            least one path must be provided.
        request_id (str):
            Optional. A unique identifier for this request. A random
            UUID is recommended. This request is idempotent if and only
            if ``request_id`` is provided.
    """

    cluster: "Cluster" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Cluster",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteClusterRequest(proto.Message):
    r"""Request message for
    [DeleteCluster][google.cloud.hypercomputecluster.v1beta.HypercomputeCluster.DeleteCluster].

    Attributes:
        name (str):
            Required. Name of the cluster to delete, in the format
            ``projects/{project}/locations/{location}/clusters/{cluster}``.
        request_id (str):
            Optional. A unique identifier for this request. A random
            UUID is recommended. This request is idempotent if and only
            if ``request_id`` is provided.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListNodesRequest(proto.Message):
    r"""Request message for
    [ListNodes][google.cloud.hypercomputecluster.v1beta.HypercomputeCluster.ListNodes].

    Attributes:
        parent (str):
            Required. Parent cluster of the nodes to list, in the format
            ``projects/{project}/locations/{location}/clusters/{cluster}``.
        page_size (int):
            Optional. Maximum number of nodes to return.
            The service may return fewer than this value.
        page_token (str):
            Optional. A page token received from a previous
            ``ListNodes`` call. Provide this to retrieve the subsequent
            page. When paginating, all other parameters provided to
            ``ListNodes`` must match the call that provided the page
            token.
        filter (str):
            Optional. `Filter <https://google.aip.dev/160>`__ to apply
            to the returned results.
        order_by (str):
            Optional. How to order the resulting nodes. Must be one of
            the following strings:

            - ``name``
            - ``name desc``

            If not specified, nodes will be returned in an arbitrary
            order.
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


class ListNodesResponse(proto.Message):
    r"""Response message for
    [ListNodes][google.cloud.hypercomputecluster.v1beta.HypercomputeCluster.ListNodes].

    Attributes:
        nodes (MutableSequence[google.cloud.hypercomputecluster_v1beta.types.Node]):
            Nodes in the specified cluster.
        next_page_token (str):
            A token that can be sent as ``page_token`` to retrieve the
            next page. If this field is absent, there are no subsequent
            pages.
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


class NetworkResource(proto.Message):
    r"""A resource representing a network that connects the various
    components of a cluster together.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        network (google.cloud.hypercomputecluster_v1beta.types.NetworkReference):
            Output only. A reference to a network in
            Google Compute Engine.

            This field is a member of `oneof`_ ``reference``.
        config (google.cloud.hypercomputecluster_v1beta.types.NetworkResourceConfig):
            Immutable. Configuration for this network
            resource, which describes how it should be
            created or imported. This field only controls
            how the network resource is initially created or
            imported. Subsequent changes to the network
            resource should be made via the resource's API
            and will not be reflected in the configuration.
    """

    network: "NetworkReference" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="reference",
        message="NetworkReference",
    )
    config: "NetworkResourceConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="NetworkResourceConfig",
    )


class NetworkReference(proto.Message):
    r"""A reference to a `VPC
    network <https://cloud.google.com/vpc/docs/vpc>`__ in Google Compute
    Engine.

    Attributes:
        network (str):
            Output only. Name of the network, in the format
            ``projects/{project}/global/networks/{network}``.
        subnetwork (str):
            Output only. Name of the particular subnetwork being used by
            the cluster, in the format
            ``projects/{project}/regions/{region}/subnetworks/{subnetwork}``.
    """

    network: str = proto.Field(
        proto.STRING,
        number=1,
    )
    subnetwork: str = proto.Field(
        proto.STRING,
        number=2,
    )


class NetworkResourceConfig(proto.Message):
    r"""Describes how a network resource should be initialized. Each
    network resource can either be imported from an existing Google
    Cloud resource or initialized when the cluster is created.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        new_network (google.cloud.hypercomputecluster_v1beta.types.NewNetworkConfig):
            Optional. Immutable. If set, indicates that a
            new network should be created.

            This field is a member of `oneof`_ ``config``.
        existing_network (google.cloud.hypercomputecluster_v1beta.types.ExistingNetworkConfig):
            Optional. Immutable. If set, indicates that
            an existing network should be imported.

            This field is a member of `oneof`_ ``config``.
    """

    new_network: "NewNetworkConfig" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="config",
        message="NewNetworkConfig",
    )
    existing_network: "ExistingNetworkConfig" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="config",
        message="ExistingNetworkConfig",
    )


class NewNetworkConfig(proto.Message):
    r"""When set in a
    [NetworkResourceConfig][google.cloud.hypercomputecluster.v1beta.NetworkResourceConfig],
    indicates that a new network should be created.

    Attributes:
        network (str):
            Required. Immutable. Name of the network to create, in the
            format ``projects/{project}/global/networks/{network}``.
        description (str):
            Optional. Immutable. Description of the
            network. Maximum of 2048 characters.
    """

    network: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ExistingNetworkConfig(proto.Message):
    r"""When set in a
    [NetworkResourceConfig][google.cloud.hypercomputecluster.v1beta.NetworkResourceConfig],
    indicates that an existing network should be imported.

    Attributes:
        network (str):
            Required. Immutable. Name of the network to import, in the
            format ``projects/{project}/global/networks/{network}``.
        subnetwork (str):
            Required. Immutable. Particular subnetwork to use, in the
            format
            ``projects/{project}/regions/{region}/subnetworks/{subnetwork}``.
    """

    network: str = proto.Field(
        proto.STRING,
        number=1,
    )
    subnetwork: str = proto.Field(
        proto.STRING,
        number=2,
    )


class StorageResource(proto.Message):
    r"""Represents a form of persistent storage that you can mount
    onto compute resources in the cluster.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        filestore (google.cloud.hypercomputecluster_v1beta.types.FilestoreReference):
            Output only. A reference to a Filestore
            instance. Populated if and only if the storage
            resource was configured to use Filestore.

            This field is a member of `oneof`_ ``reference``.
        bucket (google.cloud.hypercomputecluster_v1beta.types.BucketReference):
            Output only. A reference to a Google Cloud
            Storage bucket. Populated if and only if the
            storage resource was configured to use Google
            Cloud Storage.

            This field is a member of `oneof`_ ``reference``.
        lustre (google.cloud.hypercomputecluster_v1beta.types.LustreReference):
            Output only. A reference to a Managed Lustre
            instance. Populated if and only if the storage
            resource was configured to use Managed Lustre.

            This field is a member of `oneof`_ ``reference``.
        config (google.cloud.hypercomputecluster_v1beta.types.StorageResourceConfig):
            Required. Immutable. Configuration for this
            storage resource, which describes how it should
            be created or imported. This field only controls
            how the storage resource is initially created or
            imported. Subsequent changes to the storage
            resource should be made via the resource's API
            and will not be reflected in the configuration.
    """

    filestore: "FilestoreReference" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="reference",
        message="FilestoreReference",
    )
    bucket: "BucketReference" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="reference",
        message="BucketReference",
    )
    lustre: "LustreReference" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="reference",
        message="LustreReference",
    )
    config: "StorageResourceConfig" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="StorageResourceConfig",
    )


class FilestoreReference(proto.Message):
    r"""A reference to a `Filestore <https://cloud.google.com/filestore>`__
    instance.

    Attributes:
        filestore (str):
            Output only. Name of the Filestore instance, in the format
            ``projects/{project}/locations/{location}/instances/{instance}``
    """

    filestore: str = proto.Field(
        proto.STRING,
        number=1,
    )


class BucketReference(proto.Message):
    r"""A reference to a `Google Cloud
    Storage <https://cloud.google.com/storage>`__ bucket.

    Attributes:
        bucket (str):
            Output only. Name of the bucket.
    """

    bucket: str = proto.Field(
        proto.STRING,
        number=1,
    )


class LustreReference(proto.Message):
    r"""A reference to a `Managed
    Lustre <https://cloud.google.com/products/managed-lustre>`__
    instance.

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


class StorageResourceConfig(proto.Message):
    r"""Describes how a storage resource should be initialized. Each
    storage resource can either be imported from an existing Google
    Cloud resource or initialized when the cluster is created.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        new_filestore (google.cloud.hypercomputecluster_v1beta.types.NewFilestoreConfig):
            Optional. Immutable. If set, indicates that a
            new Filestore instance should be created.

            This field is a member of `oneof`_ ``config``.
        existing_filestore (google.cloud.hypercomputecluster_v1beta.types.ExistingFilestoreConfig):
            Optional. Immutable. If set, indicates that
            an existing Filestore instance should be
            imported.

            This field is a member of `oneof`_ ``config``.
        new_bucket (google.cloud.hypercomputecluster_v1beta.types.NewBucketConfig):
            Optional. Immutable. If set, indicates that a
            new Cloud Storage bucket should be created.

            This field is a member of `oneof`_ ``config``.
        existing_bucket (google.cloud.hypercomputecluster_v1beta.types.ExistingBucketConfig):
            Optional. Immutable. If set, indicates that
            an existing Cloud Storage bucket should be
            imported.

            This field is a member of `oneof`_ ``config``.
        new_lustre (google.cloud.hypercomputecluster_v1beta.types.NewLustreConfig):
            Optional. Immutable. If set, indicates that a
            new Managed Lustre instance should be created.

            This field is a member of `oneof`_ ``config``.
        existing_lustre (google.cloud.hypercomputecluster_v1beta.types.ExistingLustreConfig):
            Optional. Immutable. If set, indicates that
            an existing Managed Lustre instance should be
            imported.

            This field is a member of `oneof`_ ``config``.
        existing_nfs (google.cloud.hypercomputecluster_v1beta.types.ExistingNfsConfig):
            Optional. Immutable. If set, indicates that
            an existing NFS share should be imported.

            This field is a member of `oneof`_ ``config``.
    """

    new_filestore: "NewFilestoreConfig" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="config",
        message="NewFilestoreConfig",
    )
    existing_filestore: "ExistingFilestoreConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="config",
        message="ExistingFilestoreConfig",
    )
    new_bucket: "NewBucketConfig" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="config",
        message="NewBucketConfig",
    )
    existing_bucket: "ExistingBucketConfig" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="config",
        message="ExistingBucketConfig",
    )
    new_lustre: "NewLustreConfig" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="config",
        message="NewLustreConfig",
    )
    existing_lustre: "ExistingLustreConfig" = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="config",
        message="ExistingLustreConfig",
    )
    existing_nfs: "ExistingNfsConfig" = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="config",
        message="ExistingNfsConfig",
    )


class NewFilestoreConfig(proto.Message):
    r"""When set in a
    [StorageResourceConfig][google.cloud.hypercomputecluster.v1beta.StorageResourceConfig],
    indicates that a new
    `Filestore <https://cloud.google.com/filestore>`__ instance should
    be created.

    Attributes:
        filestore (str):
            Required. Immutable. Name of the Filestore instance to
            create, in the format
            ``projects/{project}/locations/{location}/instances/{instance}``.
        description (str):
            Optional. Immutable. Description of the
            instance. Maximum of 2048 characters.
        file_shares (MutableSequence[google.cloud.hypercomputecluster_v1beta.types.FileShareConfig]):
            Required. Immutable. File system shares on
            the instance. Exactly one file share must be
            specified.
        tier (google.cloud.hypercomputecluster_v1beta.types.NewFilestoreConfig.Tier):
            Required. Immutable. Service tier to use for
            the instance.
        protocol (google.cloud.hypercomputecluster_v1beta.types.NewFilestoreConfig.Protocol):
            Optional. Immutable. Access protocol to use
            for all file shares in the instance. Defaults to
            NFS V3 if not set.
    """

    class Tier(proto.Enum):
        r"""Available `service
        tiers <https://cloud.google.com/filestore/docs/service-tiers>`__ for
        Filestore instances.

        Values:
            TIER_UNSPECIFIED (0):
                Not set.
            ZONAL (4):
                Offers expanded capacity and performance
                scaling capabilities suitable for
                high-performance computing application
                requirements.
            REGIONAL (6):
                Offers features and availability needed for
                mission-critical, high-performance computing
                workloads.
        """

        TIER_UNSPECIFIED = 0
        ZONAL = 4
        REGIONAL = 6

    class Protocol(proto.Enum):
        r"""File access protocol for Filestore instances.

        Values:
            PROTOCOL_UNSPECIFIED (0):
                Not set.
            NFSV3 (1):
                NFS 3.0.
            NFSV41 (2):
                NFS 4.1.
        """

        PROTOCOL_UNSPECIFIED = 0
        NFSV3 = 1
        NFSV41 = 2

    filestore: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=4,
    )
    file_shares: MutableSequence["FileShareConfig"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="FileShareConfig",
    )
    tier: Tier = proto.Field(
        proto.ENUM,
        number=3,
        enum=Tier,
    )
    protocol: Protocol = proto.Field(
        proto.ENUM,
        number=5,
        enum=Protocol,
    )


class FileShareConfig(proto.Message):
    r"""Message describing filestore configuration

    Attributes:
        capacity_gb (int):
            Required. Size of the filestore in GB. Must
            be between 1024 and 102400, and must meet
            scalability requirements described at
            https://cloud.google.com/filestore/docs/service-tiers.
        file_share (str):
            Required. Filestore share location
    """

    capacity_gb: int = proto.Field(
        proto.INT64,
        number=1,
    )
    file_share: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ExistingFilestoreConfig(proto.Message):
    r"""When set in a
    [StorageResourceConfig][google.cloud.hypercomputecluster.v1beta.StorageResourceConfig],
    indicates that an existing
    `Filestore <https://cloud.google.com/filestore>`__ instance should
    be imported.

    Attributes:
        filestore (str):
            Required. Immutable. Name of the Filestore instance to
            import, in the format
            ``projects/{project}/locations/{location}/instances/{instance}``
    """

    filestore: str = proto.Field(
        proto.STRING,
        number=1,
    )


class NewBucketConfig(proto.Message):
    r"""When set in a
    [StorageResourceConfig][google.cloud.hypercomputecluster.v1beta.StorageResourceConfig],
    indicates that a new `Google Cloud
    Storage <https://cloud.google.com/storage>`__ bucket should be
    created.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        autoclass (google.cloud.hypercomputecluster_v1beta.types.GcsAutoclassConfig):
            Optional. Immutable. If set, indicates that the bucket
            should use
            `Autoclass <https://cloud.google.com/storage/docs/autoclass>`__.

            This field is a member of `oneof`_ ``option``.
        storage_class (google.cloud.hypercomputecluster_v1beta.types.NewBucketConfig.StorageClass):
            Optional. Immutable. If set, uses the
            provided storage class as the bucket's default
            storage class.

            This field is a member of `oneof`_ ``option``.
        bucket (str):
            Required. Immutable. Name of the Cloud
            Storage bucket to create.
        hierarchical_namespace (google.cloud.hypercomputecluster_v1beta.types.GcsHierarchicalNamespaceConfig):
            Optional. Immutable. If set, indicates that the bucket
            should use `hierarchical
            namespaces <https://cloud.google.com/storage/docs/hns-overview>`__.
    """

    class StorageClass(proto.Enum):
        r"""`Storage
        class <https://cloud.google.com/storage/docs/storage-classes>`__ for
        a Cloud Storage bucket.

        Values:
            STORAGE_CLASS_UNSPECIFIED (0):
                Not set.
            STANDARD (1):
                Best for data that is frequently accessed.
            NEARLINE (2):
                Low-cost storage for data that is accessed
                less frequently.
            COLDLINE (3):
                Very low-cost storage for infrequently
                accessed data.
            ARCHIVE (4):
                Lowest-cost storage for data archiving,
                online backup, and disaster recovery.
            RAPID (5):
                Storage class optimized for I/O intensive
                workloads.
        """

        STORAGE_CLASS_UNSPECIFIED = 0
        STANDARD = 1
        NEARLINE = 2
        COLDLINE = 3
        ARCHIVE = 4
        RAPID = 5

    autoclass: "GcsAutoclassConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="option",
        message="GcsAutoclassConfig",
    )
    storage_class: StorageClass = proto.Field(
        proto.ENUM,
        number=3,
        oneof="option",
        enum=StorageClass,
    )
    bucket: str = proto.Field(
        proto.STRING,
        number=1,
    )
    hierarchical_namespace: "GcsHierarchicalNamespaceConfig" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="GcsHierarchicalNamespaceConfig",
    )


class GcsAutoclassConfig(proto.Message):
    r"""Message describing Google Cloud Storage autoclass
    configuration

    Attributes:
        enabled (bool):
            Required. Enables Auto-class feature.
        terminal_storage_class (google.cloud.hypercomputecluster_v1beta.types.GcsAutoclassConfig.TerminalStorageClass):
            Optional. Terminal storage class of the
            autoclass bucket
    """

    class TerminalStorageClass(proto.Enum):
        r"""Terminal storage class types of the autoclass bucket

        Values:
            TERMINAL_STORAGE_CLASS_UNSPECIFIED (0):
                Unspecified terminal storage class
            NEARLINE (1):
                Nearline terminal storage class
            ARCHIVE (2):
                Archive terminal storage class
        """

        TERMINAL_STORAGE_CLASS_UNSPECIFIED = 0
        NEARLINE = 1
        ARCHIVE = 2

    enabled: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    terminal_storage_class: TerminalStorageClass = proto.Field(
        proto.ENUM,
        number=2,
        enum=TerminalStorageClass,
    )


class GcsHierarchicalNamespaceConfig(proto.Message):
    r"""Message describing Google Cloud Storage hierarchical
    namespace configuration

    Attributes:
        enabled (bool):
            Required. Enables hierarchical namespace
            setup for the bucket.
    """

    enabled: bool = proto.Field(
        proto.BOOL,
        number=1,
    )


class ExistingBucketConfig(proto.Message):
    r"""When set in a
    [StorageResourceConfig][google.cloud.hypercomputecluster.v1beta.StorageResourceConfig],
    indicates that an existing `Google Cloud
    Storage <https://cloud.google.com/storage>`__ bucket should be
    imported.

    Attributes:
        bucket (str):
            Required. Immutable. Name of the Cloud
            Storage bucket to import.
    """

    bucket: str = proto.Field(
        proto.STRING,
        number=1,
    )


class NewLustreConfig(proto.Message):
    r"""When set in a
    [StorageResourceConfig][google.cloud.hypercomputecluster.v1beta.StorageResourceConfig],
    indicates that a new `Managed
    Lustre <https://cloud.google.com/products/managed-lustre>`__
    instance should be created.

    Attributes:
        lustre (str):
            Required. Immutable. Name of the Managed Lustre instance to
            create, in the format
            ``projects/{project}/locations/{location}/instances/{instance}``
        description (str):
            Optional. Immutable. Description of the
            Managed Lustre instance. Maximum of 2048
            characters.
        filesystem (str):
            Required. Immutable. Filesystem name for this
            instance. This name is used by client-side
            tools, including when mounting the instance.
            Must be 8 characters or less and can only
            contain letters and numbers.
        capacity_gb (int):
            Required. Immutable. Storage capacity of the
            instance in gibibytes (GiB). Allowed values are
            between 18000 and 7632000.
        per_unit_storage_throughput (int):
            Optional. Immutable. Throughput of the instance in MB/s/TiB.
            Valid values are 125, 250, 500, 1000. See `Performance tiers
            and maximum storage
            capacities <https://cloud.google.com/managed-lustre/docs/create-instance#performance-tiers>`__
            for more information.
    """

    lustre: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    filesystem: str = proto.Field(
        proto.STRING,
        number=3,
    )
    capacity_gb: int = proto.Field(
        proto.INT64,
        number=4,
    )
    per_unit_storage_throughput: int = proto.Field(
        proto.INT64,
        number=5,
    )


class ExistingLustreConfig(proto.Message):
    r"""When set in a
    [StorageResourceConfig][google.cloud.hypercomputecluster.v1beta.StorageResourceConfig],
    indicates that an existing `Managed
    Lustre <https://cloud.google.com/products/managed-lustre>`__
    instance should be imported.

    Attributes:
        lustre (str):
            Required. Immutable. Name of the Managed Lustre instance to
            import, in the format
            ``projects/{project}/locations/{location}/instances/{instance}``
    """

    lustre: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ExistingNfsConfig(proto.Message):
    r"""When set in a
    [StorageResourceConfig][google.cloud.hypercomputecluster.v1beta.StorageResourceConfig],
    indicates that an existing NFS share should be imported.

    Attributes:
        server_ip_address (str):
            Required. Immutable. Server IP address of the
            NFS share.
        remote_mount (str):
            Required. Immutable. Remote mount path of the
            NFS share.
        mount_options (str):
            Optional. Immutable. Options to mount the NFS share, as
            expected by fs_mntops field infstab(5), for example:
            "rw,vers=4.1,nconnect=2,noatime".
    """

    server_ip_address: str = proto.Field(
        proto.STRING,
        number=1,
    )
    remote_mount: str = proto.Field(
        proto.STRING,
        number=2,
    )
    mount_options: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ComputeResource(proto.Message):
    r"""A resource defining how virtual machines and accelerators
    should be provisioned for the cluster.

    Attributes:
        config (google.cloud.hypercomputecluster_v1beta.types.ComputeResourceConfig):
            Required. Immutable. Configuration for this
            compute resource, which describes how it should
            be created at runtime.
    """

    config: "ComputeResourceConfig" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="ComputeResourceConfig",
    )


class ComputeResourceConfig(proto.Message):
    r"""Describes how a compute resource should be created at
    runtime.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        new_on_demand_instances (google.cloud.hypercomputecluster_v1beta.types.NewOnDemandInstancesConfig):
            Optional. Immutable. If set, indicates that
            this resource should use on-demand VMs.

            This field is a member of `oneof`_ ``config``.
        new_spot_instances (google.cloud.hypercomputecluster_v1beta.types.NewSpotInstancesConfig):
            Optional. Immutable. If set, indicates that
            this resource should use spot VMs.

            This field is a member of `oneof`_ ``config``.
        new_reserved_instances (google.cloud.hypercomputecluster_v1beta.types.NewReservedInstancesConfig):
            Optional. Immutable. If set, indicates that
            this resource should use reserved VMs.

            This field is a member of `oneof`_ ``config``.
        new_flex_start_instances (google.cloud.hypercomputecluster_v1beta.types.NewFlexStartInstancesConfig):
            Optional. Immutable. If set, indicates that
            this resource should use flex-start VMs.

            This field is a member of `oneof`_ ``config``.
    """

    new_on_demand_instances: "NewOnDemandInstancesConfig" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="config",
        message="NewOnDemandInstancesConfig",
    )
    new_spot_instances: "NewSpotInstancesConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="config",
        message="NewSpotInstancesConfig",
    )
    new_reserved_instances: "NewReservedInstancesConfig" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="config",
        message="NewReservedInstancesConfig",
    )
    new_flex_start_instances: "NewFlexStartInstancesConfig" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="config",
        message="NewFlexStartInstancesConfig",
    )


class NewOnDemandInstancesConfig(proto.Message):
    r"""When set in a
    [ComputeResourceConfig][google.cloud.hypercomputecluster.v1beta.ComputeResourceConfig],
    indicates that on-demand (i.e., using the standard provisioning
    model) VM instances should be created.

    Attributes:
        zone (str):
            Required. Immutable. Name of the zone in which VM instances
            should run, e.g., ``us-central1-a``. Must be in the same
            region as the cluster, and must match the zone of any other
            resources specified in the cluster.
        machine_type (str):
            Required. Immutable. Name of the Compute Engine `machine
            type <https://cloud.google.com/compute/docs/machine-resource>`__
            to use, e.g. ``n2-standard-2``.
        network_tags (MutableSequence[str]):
            Optional. Immutable. A list of network tags
            to attach to the VM instances. A maximum of 64
            network tags are allowed.
    """

    zone: str = proto.Field(
        proto.STRING,
        number=1,
    )
    machine_type: str = proto.Field(
        proto.STRING,
        number=2,
    )
    network_tags: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )


class NewSpotInstancesConfig(proto.Message):
    r"""When set in a
    [ComputeResourceConfig][google.cloud.hypercomputecluster.v1beta.ComputeResourceConfig],
    indicates that `spot
    VM <https://cloud.google.com/compute/docs/instances/spot>`__
    instances should be created.

    Attributes:
        zone (str):
            Required. Immutable. Name of the zone in which VM instances
            should run, e.g., ``us-central1-a``. Must be in the same
            region as the cluster, and must match the zone of any other
            resources specified in the cluster.
        machine_type (str):
            Required. Immutable. Name of the Compute Engine `machine
            type <https://cloud.google.com/compute/docs/machine-resource>`__
            to use, e.g. ``n2-standard-2``.
        termination_action (google.cloud.hypercomputecluster_v1beta.types.NewSpotInstancesConfig.TerminationAction):
            Optional. Termination action for the
            instance. If not specified, Compute Engine sets
            the termination action to DELETE.
        network_tags (MutableSequence[str]):
            Optional. Immutable. A list of network tags
            to attach to the VM instances. A maximum of 64
            network tags are allowed.
    """

    class TerminationAction(proto.Enum):
        r"""Specifies the termination action of the instance.

        Values:
            TERMINATION_ACTION_UNSPECIFIED (0):
                Not set.
            STOP (1):
                Compute Engine stops the Spot VM on
                preemption.
            DELETE (2):
                Compute Engine deletes the Spot VM on
                preemption.
        """

        TERMINATION_ACTION_UNSPECIFIED = 0
        STOP = 1
        DELETE = 2

    zone: str = proto.Field(
        proto.STRING,
        number=1,
    )
    machine_type: str = proto.Field(
        proto.STRING,
        number=2,
    )
    termination_action: TerminationAction = proto.Field(
        proto.ENUM,
        number=5,
        enum=TerminationAction,
    )
    network_tags: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )


class NewReservedInstancesConfig(proto.Message):
    r"""When set in a
    [ComputeResourceConfig][google.cloud.hypercomputecluster.v1beta.ComputeResourceConfig],
    indicates that VM instances should be created from a
    `reservation <https://cloud.google.com/compute/docs/instances/reservations-overview>`__.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        reservation (str):
            Optional. Immutable. Name of the reservation from which VM
            instances should be created, in the format
            ``projects/{project}/zones/{zone}/reservations/{reservation}``.

            This field is a member of `oneof`_ ``source``.
        reservation_block (str):
            Optional. Immutable. Name of the reservation block from
            which VM instances should be created, in the format
            ``projects/{project}/zones/{zone}/reservations/{reservation}/reservationBlocks/{reservation_block}``.

            This field is a member of `oneof`_ ``source``.
        reservation_sub_block (str):
            Optional. Immutable. Name of the reservation sub block from
            which VM instances should be created, in the format
            ``projects/{project}/zones/{zone}/reservations/{reservation}/reservationBlocks/{reservation_block}/reservationSubBlocks/{reservation_sub_block}``.

            This field is a member of `oneof`_ ``source``.
        network_tags (MutableSequence[str]):
            Optional. Immutable. A list of network tags
            to attach to the VM instances. A maximum of 64
            network tags are allowed.
    """

    reservation: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="source",
    )
    reservation_block: str = proto.Field(
        proto.STRING,
        number=7,
        oneof="source",
    )
    reservation_sub_block: str = proto.Field(
        proto.STRING,
        number=8,
        oneof="source",
    )
    network_tags: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=9,
    )


class NewFlexStartInstancesConfig(proto.Message):
    r"""When set in a
    [ComputeResourceConfig][google.cloud.hypercomputecluster.v1beta.ComputeResourceConfig],
    indicates that VM instances should be created using `Flex
    Start <https://cloud.google.com/compute/docs/instances/provisioning-models>`__.

    Attributes:
        zone (str):
            Required. Immutable. Name of the zone in which VM instances
            should run, e.g., ``us-central1-a``. Must be in the same
            region as the cluster, and must match the zone of any other
            resources specified in the cluster.
        machine_type (str):
            Required. Immutable. Name of the Compute Engine `machine
            type <https://cloud.google.com/compute/docs/machine-resource>`__
            to use, e.g. ``n2-standard-2``.
        max_duration (google.protobuf.duration_pb2.Duration):
            Required. Immutable. Specifies the time limit
            for created instances. Instances will be
            terminated at the end of this duration.
        network_tags (MutableSequence[str]):
            Optional. Immutable. A list of network tags
            to attach to the VM instances. A maximum of 64
            network tags are allowed.
    """

    zone: str = proto.Field(
        proto.STRING,
        number=1,
    )
    machine_type: str = proto.Field(
        proto.STRING,
        number=2,
    )
    max_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=3,
        message=duration_pb2.Duration,
    )
    network_tags: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=7,
    )


class BootDisk(proto.Message):
    r"""A `Persistent disk <https://cloud.google.com/compute/docs/disks>`__
    used as the boot disk for a Compute Engine VM instance.

    Attributes:
        type_ (str):
            Optional. `Persistent disk
            type <https://cloud.google.com/compute/docs/disks#disk-types>`__,
            in the format
            ``projects/{project}/zones/{zone}/diskTypes/{disk_type}``.
        size_gb (int):
            Optional. The size of the disk in gigabytes
            (GB), which must be at least 40 GB.
        storage_pools (MutableSequence[str]):
            Optional. The `storage
            pools <https://docs.cloud.google.com/compute/docs/disks/storage-pools>`__
            used for creating the boot disk, in the format:
            ``projects/{project}/zones/{zone}/storagePools/{storage_pool}``.

            Currently, only one Hyperdisk Balanced storage pool is
            supported. The storage pool must reside in the same zone as
            the compute instance.
    """

    type_: str = proto.Field(
        proto.STRING,
        number=1,
    )
    size_gb: int = proto.Field(
        proto.INT64,
        number=2,
    )
    storage_pools: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )


class Orchestrator(proto.Message):
    r"""The component responsible for scheduling and running
    workloads on the cluster as well as providing the user interface
    for interacting with the cluster at runtime.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        slurm (google.cloud.hypercomputecluster_v1beta.types.SlurmOrchestrator):
            Optional. If set, indicates that the cluster
            should use Slurm as the orchestrator.

            This field is a member of `oneof`_ ``option``.
        compute_engine (google.cloud.hypercomputecluster_v1beta.types.ComputeEngineOrchestrator):
            Optional. If set, indicates that the cluster
            should use Compute Engine as the orchestrator.

            This field is a member of `oneof`_ ``option``.
    """

    slurm: "SlurmOrchestrator" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="option",
        message="SlurmOrchestrator",
    )
    compute_engine: "ComputeEngineOrchestrator" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="option",
        message="ComputeEngineOrchestrator",
    )


class SlurmOrchestrator(proto.Message):
    r"""When set in
    [Orchestrator][google.cloud.hypercomputecluster.v1beta.Orchestrator],
    indicates that the cluster should use
    `Slurm <https://slurm.schedmd.com/>`__ as the orchestrator.

    Attributes:
        login_nodes (google.cloud.hypercomputecluster_v1beta.types.SlurmLoginNodes):
            Required. Configuration for login nodes,
            which allow users to access the cluster over
            SSH.
        node_sets (MutableSequence[google.cloud.hypercomputecluster_v1beta.types.SlurmNodeSet]):
            Optional. Compute resource configuration for
            the Slurm nodesets in your cluster. If not
            specified, the cluster won't create any nodes.
        partitions (MutableSequence[google.cloud.hypercomputecluster_v1beta.types.SlurmPartition]):
            Optional. Configuration for the Slurm
            partitions in your cluster. Each partition can
            contain one or more nodesets, and you can submit
            separate jobs on each partition. If you don't
            specify at least one partition in your cluster,
            you can't submit jobs to the cluster.
        default_partition (str):
            Optional. Default partition to use for
            submitted jobs that do not explicitly specify a
            partition. Required if and only if there is more
            than one partition, in which case it must match
            the id of one of the partitions.
        prolog_bash_scripts (MutableSequence[str]):
            Optional. Slurm `prolog
            scripts <https://slurm.schedmd.com/prolog_epilog.html>`__,
            which will be executed by compute nodes before a node begins
            running a new job. Values must not be empty.
        epilog_bash_scripts (MutableSequence[str]):
            Optional. Slurm `epilog
            scripts <https://slurm.schedmd.com/prolog_epilog.html>`__,
            which will be executed by compute nodes whenever a node
            finishes running a job. Values must not be empty.
    """

    login_nodes: "SlurmLoginNodes" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="SlurmLoginNodes",
    )
    node_sets: MutableSequence["SlurmNodeSet"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="SlurmNodeSet",
    )
    partitions: MutableSequence["SlurmPartition"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="SlurmPartition",
    )
    default_partition: str = proto.Field(
        proto.STRING,
        number=3,
    )
    prolog_bash_scripts: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    epilog_bash_scripts: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )


class SlurmNodeSet(proto.Message):
    r"""Configuration for Slurm nodesets in the cluster. Nodesets are
    groups of compute nodes used by Slurm that are responsible for
    running workloads submitted to the cluster.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        compute_instance (google.cloud.hypercomputecluster_v1beta.types.ComputeInstanceSlurmNodeSet):
            Optional. If set, indicates that the nodeset
            should be backed by Compute Engine instances.

            This field is a member of `oneof`_ ``type``.
        id (str):
            Required. The ID for the nodeset, which allows it to be
            referenced by cluster partitions. The nodeset ID must start
            with a lowercase letter (``a``-``z``), use only lowercase
            letters or numbers, and contain up to 15 characters. For
            example, specify ``nodeset001``.
        compute_id (str):
            Required. The ID of the compute resource on which this
            nodeset runs. Must match a key in the cluster's
            [compute_resources][google.cloud.hypercomputecluster.v1beta.Cluster.compute_resources].
        storage_configs (MutableSequence[google.cloud.hypercomputecluster_v1beta.types.StorageConfig]):
            Optional. How [storage
            resources][google.cloud.hypercomputecluster.v1beta.StorageResource]
            should be mounted on each compute node.
        static_node_count (int):
            Optional. Number of nodes to be statically
            created for this nodeset. The cluster will
            attempt to ensure that at least this many nodes
            exist at all times.
        max_dynamic_node_count (int):
            Optional. Controls how many additional nodes
            a cluster can bring online to handle workloads.
            Set this value to enable dynamic node creation
            and limit the number of additional nodes the
            cluster can bring online. Leave empty if you do
            not want the cluster to create nodes
            dynamically, and instead rely only on static
            nodes.
        resource_policy_config (google.cloud.hypercomputecluster_v1beta.types.ResourcePolicyConfig):
            Optional. Resource policy configuration for
            the nodeset.
    """

    compute_instance: "ComputeInstanceSlurmNodeSet" = proto.Field(
        proto.MESSAGE,
        number=17,
        oneof="type",
        message="ComputeInstanceSlurmNodeSet",
    )
    id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    compute_id: str = proto.Field(
        proto.STRING,
        number=16,
    )
    storage_configs: MutableSequence["StorageConfig"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="StorageConfig",
    )
    static_node_count: int = proto.Field(
        proto.INT64,
        number=4,
    )
    max_dynamic_node_count: int = proto.Field(
        proto.INT64,
        number=5,
    )
    resource_policy_config: "ResourcePolicyConfig" = proto.Field(
        proto.MESSAGE,
        number=19,
        message="ResourcePolicyConfig",
    )


class ComputeInstanceSlurmNodeSet(proto.Message):
    r"""When set in a
    [SlurmNodeSet][google.cloud.hypercomputecluster.v1beta.SlurmNodeSet],
    indicates that the nodeset should be backed by Compute Engine VM
    instances.

    Attributes:
        startup_script (str):
            Optional. `Startup
            script <https://cloud.google.com/compute/docs/instances/startup-scripts/linux>`__
            to be run on each VM instance in the nodeset. Max 256KB.
        labels (MutableMapping[str, str]):
            Optional.
            `Labels <https://cloud.google.com/compute/docs/labeling-resources>`__
            that should be applied to each VM instance in the nodeset.
        boot_disk (google.cloud.hypercomputecluster_v1beta.types.BootDisk):
            Optional. Boot disk for the compute instance
    """

    startup_script: str = proto.Field(
        proto.STRING,
        number=1,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=2,
    )
    boot_disk: "BootDisk" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="BootDisk",
    )


class ResourcePolicyConfig(proto.Message):
    r"""Policy describing how VM instances should be created.

    Attributes:
        accelerator_topology (str):
            Optional. Specifies the topology required to create a
            partition for VMs that have interconnected accelerators, in
            the format ``AxB`` or ``AxBxC``, where ``A``, ``B``, and
            ``C`` are integers.
    """

    accelerator_topology: str = proto.Field(
        proto.STRING,
        number=2,
    )


class SlurmPartition(proto.Message):
    r"""Configuration for Slurm partitions in the cluster. Partitions
    are groups of nodesets, and are how clients specify where their
    workloads should be run.

    Attributes:
        id (str):
            Required. ID of the partition, which is how users will
            identify it. Must conform to
            `RFC-1034 <https://datatracker.ietf.org/doc/html/rfc1034>`__
            (lower-case, alphanumeric, and at most 63 characters).
        node_set_ids (MutableSequence[str]):
            Required. IDs of the nodesets that make up this partition.
            Values must match
            [SlurmNodeSet.id][google.cloud.hypercomputecluster.v1beta.SlurmNodeSet.id].
    """

    id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    node_set_ids: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class SlurmLoginNodes(proto.Message):
    r"""Configuration for Slurm `login
    nodes <https://slurm.schedmd.com/quickstart_admin.html#login>`__ in
    the cluster. Login nodes are Compute Engine VM instances that allow
    users to access the cluster over SSH.

    Attributes:
        count (int):
            Required. Number of login node instances to
            create.
        zone (str):
            Required. Name of the zone in which login nodes should run,
            e.g., ``us-central1-a``. Must be in the same region as the
            cluster, and must match the zone of any other resources
            specified in the cluster.
        machine_type (str):
            Required. Name of the Compute Engine `machine
            type <https://cloud.google.com/compute/docs/machine-resource>`__
            to use for login nodes, e.g. ``n2-standard-2``.
        startup_script (str):
            Optional. `Startup
            script <https://cloud.google.com/compute/docs/instances/startup-scripts/linux>`__
            to be run on each login node instance. Max 256KB. The script
            must complete within the system-defined default timeout of 5
            minutes. For tasks that require more time, consider running
            them in the background using methods such as ``&`` or
            ``nohup``.
        enable_os_login (bool):
            Optional. Whether `OS
            Login <https://cloud.google.com/compute/docs/oslogin>`__
            should be enabled on login node instances.
        enable_public_ips (bool):
            Optional. Whether login node instances should be assigned
            `external IP
            addresses <https://cloud.google.com/compute/docs/ip-addresses#externaladdresses>`__.
        labels (MutableMapping[str, str]):
            Optional.
            `Labels <https://cloud.google.com/compute/docs/labeling-resources>`__
            that should be applied to each login node instance.
        storage_configs (MutableSequence[google.cloud.hypercomputecluster_v1beta.types.StorageConfig]):
            Optional. How [storage
            resources][google.cloud.hypercomputecluster.v1beta.StorageResource]
            should be mounted on each login node.
        instances (MutableSequence[google.cloud.hypercomputecluster_v1beta.types.ComputeInstance]):
            Output only. Information about the login node
            instances that were created in Compute Engine.
        boot_disk (google.cloud.hypercomputecluster_v1beta.types.BootDisk):
            Optional. Boot disk for the login node.
        network_tags (MutableSequence[str]):
            Optional. Network tags to be applied to each
            login node instance. A maximum of 64 network
            tags are allowed.
    """

    count: int = proto.Field(
        proto.INT64,
        number=3,
    )
    zone: str = proto.Field(
        proto.STRING,
        number=2,
    )
    machine_type: str = proto.Field(
        proto.STRING,
        number=1,
    )
    startup_script: str = proto.Field(
        proto.STRING,
        number=5,
    )
    enable_os_login: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    enable_public_ips: bool = proto.Field(
        proto.BOOL,
        number=7,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=8,
    )
    storage_configs: MutableSequence["StorageConfig"] = proto.RepeatedField(
        proto.MESSAGE,
        number=12,
        message="StorageConfig",
    )
    instances: MutableSequence["ComputeInstance"] = proto.RepeatedField(
        proto.MESSAGE,
        number=10,
        message="ComputeInstance",
    )
    boot_disk: "BootDisk" = proto.Field(
        proto.MESSAGE,
        number=13,
        message="BootDisk",
    )
    network_tags: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=14,
    )


class ServiceAccount(proto.Message):
    r"""Service account email and scopes

    Attributes:
        email (str):
            Optional. Service account email
        scopes (MutableSequence[str]):
            Optional. Service account scopes
    """

    email: str = proto.Field(
        proto.STRING,
        number=1,
    )
    scopes: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class StorageConfig(proto.Message):
    r"""Description of how a [storage
    resource][google.cloud.hypercomputecluster.v1beta.StorageResource]
    should be mounted on a VM instance.

    Attributes:
        id (str):
            Required. ID of the storage resource to mount, which must
            match a key in the cluster's
            [storage_resources][google.cloud.hypercomputecluster.v1beta.Cluster.storage_resources].
        local_mount (str):
            Required. A directory inside the VM instance's file system
            where the storage resource should be mounted (e.g.,
            ``/mnt/share``).
    """

    id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    local_mount: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ComputeInstance(proto.Message):
    r"""Details about a Compute Engine
    `instance <https://cloud.google.com/compute/docs/instances>`__.

    Attributes:
        instance (str):
            Output only. Name of the VM instance, in the format
            ``projects/{project}/zones/{zone}/instances/{instance}``.
    """

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )


class Node(proto.Message):
    r"""A resource representing a compute node managed by Cluster
    Director.

    Attributes:
        name (str):
            Identifier. `Relative resource
            name <https://google.aip.dev/122>`__ of the node, in the
            format
            ``projects/{project}/locations/{location}/clusters/{cluster}/nodes/{node}``.
        zone (str):
            Output only. Name of the zone in which the node is running,
            e.g. ``us-central1-a``.
        state (google.cloud.hypercomputecluster_v1beta.types.Node.State):
            Output only. High-level lifecycle state of
            the node.
        state_message (str):
            Output only. Human-readable message providing
            extra information about the current state.
        running_jobs (bool):
            Output only. Indicates whether the node is
            currently executing workloads.
        accepting_jobs (bool):
            Output only. Indicates whether the node is
            available for new job allocations.
        provisioning_model (google.cloud.hypercomputecluster_v1beta.types.Node.ProvisioningModel):
            Output only. Provisioning model of the node.
        slurm_details (google.cloud.hypercomputecluster_v1beta.types.SlurmNodeDetails):
            Output only. Slurm-specific details for the
            node.
        compute_engine_details (google.cloud.hypercomputecluster_v1beta.types.ComputeEngineNodeDetails):
            Output only. Compute Engine-specific details
            for the node.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time that the node was
            originally created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time that the node was most
            recently updated.
    """

    class State(proto.Enum):
        r"""High-level lifecycle state of the node.

        Values:
            STATE_UNSPECIFIED (0):
                Not set.
            CREATING (1):
                The node is being provisioned at the
                infrastructure layer or initialized by the
                orchestrator.
            ACTIVE (2):
                The node is healthy and operational.
            SUSPENDING (3):
                The node is transitioning to a stopped or
                suspended state.
            SUSPENDED (4):
                The node is suspended or stopped and not
                consuming compute resources.
            REPAIRING (5):
                The node is undergoing maintenance or
                automatic recovery.
            FAILED (6):
                The node is in an unhealthy or terminal error
                state.
            DELETING (7):
                The node is being deleted.
            UNPROVISIONED (8):
                The node has no VM assigned to it.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        ACTIVE = 2
        SUSPENDING = 3
        SUSPENDED = 4
        REPAIRING = 5
        FAILED = 6
        DELETING = 7
        UNPROVISIONED = 8

    class ProvisioningModel(proto.Enum):
        r"""Provisioning model of the node.

        Values:
            PROVISIONING_MODEL_UNSPECIFIED (0):
                Not set.
            ON_DEMAND (1):
                The node is provisioned on demand. User
                controlled runtime, no discounts.
            SPOT (2):
                The node is provisioned as a spot VM. Heavily
                discounted, no guaranteed runtime.
            RESERVATION_BOUND (3):
                The node is provisioned as a
                reservation-bound VM. Bound to the lifecycle of
                the reservation in which it is provisioned.
            FLEX_START (4):
                The node is provisioned as a flex-start VM.
                Has a limited runtime.
        """

        PROVISIONING_MODEL_UNSPECIFIED = 0
        ON_DEMAND = 1
        SPOT = 2
        RESERVATION_BOUND = 3
        FLEX_START = 4

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    zone: str = proto.Field(
        proto.STRING,
        number=2,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=3,
        enum=State,
    )
    state_message: str = proto.Field(
        proto.STRING,
        number=4,
    )
    running_jobs: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    accepting_jobs: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    provisioning_model: ProvisioningModel = proto.Field(
        proto.ENUM,
        number=12,
        enum=ProvisioningModel,
    )
    slurm_details: "SlurmNodeDetails" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="SlurmNodeDetails",
    )
    compute_engine_details: "ComputeEngineNodeDetails" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="ComputeEngineNodeDetails",
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=11,
        message=timestamp_pb2.Timestamp,
    )


class SlurmNodeDetails(proto.Message):
    r"""Slurm-specific details for a Node.

    Attributes:
        states (MutableSequence[str]):
            Output only. Raw state flags directly from
            Slurm.
        reason (str):
            Output only. User-readable reason for the
            current state.
        partitions (MutableSequence[str]):
            Output only. Slurm partitions this node
            belongs to.
        nodeset (str):
            Output only. The ID of the nodeset this node
            belongs to.
        comment (str):
            Output only. System comments from Slurm.
    """

    states: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    reason: str = proto.Field(
        proto.STRING,
        number=2,
    )
    partitions: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    nodeset: str = proto.Field(
        proto.STRING,
        number=4,
    )
    comment: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ComputeEngineNodeDetails(proto.Message):
    r"""Compute Engine-specific details for a Node.

    Attributes:
        instance (str):
            Output only. `Relative resource
            name <https://google.aip.dev/122>`__ of the VM instance, in
            the format
            ``projects/{project}/zones/{zone}/instances/{instance}``.
        machine_type (str):
            Output only. Name of the Compute Engine `machine
            type <https://cloud.google.com/compute/docs/machine-resource>`__
            to use, e.g. ``n2-standard-2``.
        state (str):
            Output only. The Compute Engine VM `instance lifecycle
            state <https://cloud.google.com/compute/docs/instances/instance-lifecycle>`__.
        instance_group_manager (str):
            Output only. `Relative resource
            name <https://google.aip.dev/122>`__ of the managed instance
            group, in the format
            ``projects/{project}/zones/{zone}/instanceGroupManagers/{instance_group_manager}``.
            or
            ``projects/{project}/regions/{region}/instanceGroupManagers/{instance_group_manager}``
    """

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    machine_type: str = proto.Field(
        proto.STRING,
        number=2,
    )
    state: str = proto.Field(
        proto.STRING,
        number=3,
    )
    instance_group_manager: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ComputeEngineOrchestrator(proto.Message):
    r"""When set in
    [Orchestrator][google.cloud.hypercomputecluster.v1beta.Orchestrator],
    indicates that the cluster should create nodes using Compute Engine.

    Attributes:
        managed_instance_groups (MutableMapping[str, google.cloud.hypercomputecluster_v1beta.types.ManagedInstanceGroup]):
            Optional. Managed instance groups that should be created by
            the orchestrator. Keys must conform to
            `RFC-1034 <https://datatracker.ietf.org/doc/html/rfc1034>`__
            (lower-case, alphanumeric, and at most 63 characters).
        existing_instances (MutableMapping[str, google.cloud.hypercomputecluster_v1beta.types.ExistingInstances]):
            Optional. Existing instances that will be governed by the
            orchestrator. Keys must conform to
            `RFC-1034 <https://datatracker.ietf.org/doc/html/rfc1034>`__
            (lower-case, alphanumeric, and at most 63 characters).
    """

    managed_instance_groups: MutableMapping[str, "ManagedInstanceGroup"] = (
        proto.MapField(
            proto.STRING,
            proto.MESSAGE,
            number=1,
            message="ManagedInstanceGroup",
        )
    )
    existing_instances: MutableMapping[str, "ExistingInstances"] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=2,
        message="ExistingInstances",
    )


class ManagedInstanceGroup(proto.Message):
    r"""A managed instance group based on a compute resource.

    Attributes:
        instance_group_manager (str):
            Output only. Name of the managed instance group, in the
            format
            ``projects/{project}/zones/{zone}/instanceGroupManagers/{instance_group_manager}``.
            or
            ``projects/{project}/regions/{region}/instanceGroupManagers/{instance_group_manager}``
        compute_id (str):
            Required. ID of the compute resource used to
            create this managed instance group.
        target_size (int):
            Optional. Target number of running instances
            for this managed instance group.
        storage_configs (MutableSequence[google.cloud.hypercomputecluster_v1beta.types.StorageConfig]):
            Optional. How [storage
            resources][google.cloud.hypercomputecluster.v1beta.StorageResource]
            should be mounted on each instance in this managed instance
            group.
        instance_template (str):
            Output only. Instance template used to create
            instances in this group.
        resource_policy_config (google.cloud.hypercomputecluster_v1beta.types.ResourcePolicyConfig):
            Optional. Resource policy configuration for
            this managed instance group.
        boot_disk (google.cloud.hypercomputecluster_v1beta.types.BootDisk):
            Optional. Boot disk for the managed instance
            group.
        additional_disks (MutableMapping[str, google.cloud.hypercomputecluster_v1beta.types.Disk]):
            Optional. Additional disks for the managed instance group.
            Each VM of the MIG will have its own clone of each disk
            described in the additional_disks map. The disks themselves
            live as long as the MIG and if a VM is replaced by a new VM
            of the same name then the replacement VM attaches to the
            same disks as the VM it replaced. Each disk has a custom
            device name matching the key in the map.
        startup_script (str):
            Optional. Startup script to be run on each VM
            instance in the nodeset.
        enable_public_ips (bool):
            Optional. Whether to enable public IPs for
            the instances in the managed instance group.
        enable_os_login (bool):
            Optional. Whether `OS
            Login <https://cloud.google.com/compute/docs/oslogin>`__
            should be enabled on instances in this managed instance
            group.
        startup_script_timeout (google.protobuf.duration_pb2.Duration):
            Optional. The maximum time to wait for the
            startup script to complete. If the script
            exceeds this duration, the instance setup will
            be considered failed. This value must be
            positive. If this value is unset, a default
            timeout of 5 minutes (300 seconds) will be used
            by the system.
        metadata (MutableMapping[str, str]):
            Optional. Custom
            `metadata <https://cloud.google.com/compute/docs/metadata/overview>`__
            key-value pairs to be applied to each VM instance in the
            managed instance group.
        service_account (google.cloud.hypercomputecluster_v1beta.types.ServiceAccount):
            Required. Immutable. Service account to be
            used by the instances in the managed instance
            group.
        labels (MutableMapping[str, str]):
            Optional.
            `Labels <https://cloud.google.com/compute/docs/labeling-resources>`__
            that should be applied to each VM instance in the managed
            instance group.
    """

    instance_group_manager: str = proto.Field(
        proto.STRING,
        number=7,
    )
    compute_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    target_size: int = proto.Field(
        proto.INT64,
        number=2,
    )
    storage_configs: MutableSequence["StorageConfig"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="StorageConfig",
    )
    instance_template: str = proto.Field(
        proto.STRING,
        number=4,
    )
    resource_policy_config: "ResourcePolicyConfig" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="ResourcePolicyConfig",
    )
    boot_disk: "BootDisk" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="BootDisk",
    )
    additional_disks: MutableMapping[str, "Disk"] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=15,
        message="Disk",
    )
    startup_script: str = proto.Field(
        proto.STRING,
        number=8,
    )
    enable_public_ips: bool = proto.Field(
        proto.BOOL,
        number=9,
    )
    enable_os_login: bool = proto.Field(
        proto.BOOL,
        number=10,
    )
    startup_script_timeout: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=11,
        message=duration_pb2.Duration,
    )
    metadata: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=12,
    )
    service_account: "ServiceAccount" = proto.Field(
        proto.MESSAGE,
        number=13,
        message="ServiceAccount",
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=14,
    )


class Disk(proto.Message):
    r"""Additional disk for managed instance groups.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        image (str):
            Optional. Source image for the disk.

            This field is a member of `oneof`_ ``source``.
        snapshot (str):
            Optional. Source snapshot for the disk.

            This field is a member of `oneof`_ ``source``.
        existing_disk (str):
            Optional. An existing persistent disk to attach read-only to
            all VMs in the managed instance group, in the format
            ``projects/{project}/zones/{zone}/disks/{disk}``.

            This field is a member of `oneof`_ ``source``.
        type_ (str):
            Optional. `Persistent disk
            type <https://cloud.google.com/compute/docs/disks#disk-types>`__,
            in the format
            ``projects/{project}/zones/{zone}/diskTypes/{disk_type}``.
            This field is required when creating a new disk.
        size_gb (int):
            Optional. Size of the disk in GB.
            This field is required when creating a new disk.
    """

    image: str = proto.Field(
        proto.STRING,
        number=3,
        oneof="source",
    )
    snapshot: str = proto.Field(
        proto.STRING,
        number=4,
        oneof="source",
    )
    existing_disk: str = proto.Field(
        proto.STRING,
        number=5,
        oneof="source",
    )
    type_: str = proto.Field(
        proto.STRING,
        number=1,
    )
    size_gb: int = proto.Field(
        proto.INT64,
        number=2,
    )


class ExistingInstances(proto.Message):
    r"""ExistingInstances defines a list of existing VM instances to
    include in the cluster.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        project (str):
            Optional. Immutable. Project containing the instances, in
            the format ``projects/{project}``.

            This field is a member of `oneof`_ ``source``.
        instance_group_manager (str):
            Optional. Immutable. Managed instance group containing the
            instances, in the format
            ``projects/{project}/zones/{zone}/instanceGroupManagers/{instanceGroupManager}``.

            This field is a member of `oneof`_ ``source``.
        region_instance_group_manager (str):
            Optional. Immutable. Regional managed instance group
            containing the instances, in the format
            ``projects/{project}/regions/{region}/instanceGroupManagers/{instanceGroupManager}``.

            This field is a member of `oneof`_ ``source``.
        reservation (str):
            Optional. Immutable. Reservation containing the instances,
            in the format
            ``projects/{project}/zones/{zone}/reservations/{reservation}``.

            This field is a member of `oneof`_ ``source``.
        reservation_block (str):
            Optional. Immutable. Reservation block containing the
            instances, in the format
            ``projects/{project}/zones/{zone}/reservations/{reservation}/reservationBlocks/{reservationBlock}``.

            This field is a member of `oneof`_ ``source``.
        reservation_sub_block (str):
            Optional. Immutable. Reservation sub block containing the
            instances, in the format
            ``projects/{project}/zones/{zone}/reservations/{reservation}/reservationBlocks/{reservationBlock}/reservationSubBlocks/{reservationSubBlock}``.

            This field is a member of `oneof`_ ``source``.
        labels (MutableMapping[str, str]):
            Optional. Immutable. Labels specifying the
            instances to include. Instances from the source
            will be included only if they contain each of
            these labels. If no labels are specified, all
            instances from the source will be included.
            Example: {"env": "prod", "app": "worker"}
        networks (MutableSequence[google.cloud.hypercomputecluster_v1beta.types.NetworkReference]):
            Output only. Networks stores the list of `VPC
            networks <https://cloud.google.com/vpc/docs/vpc>`__ attached
            to these existing instances, discovered during the cluster
            creation and update.
    """

    project: str = proto.Field(
        proto.STRING,
        number=7,
        oneof="source",
    )
    instance_group_manager: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="source",
    )
    region_instance_group_manager: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="source",
    )
    reservation: str = proto.Field(
        proto.STRING,
        number=3,
        oneof="source",
    )
    reservation_block: str = proto.Field(
        proto.STRING,
        number=4,
        oneof="source",
    )
    reservation_sub_block: str = proto.Field(
        proto.STRING,
        number=5,
        oneof="source",
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=6,
    )
    networks: MutableSequence["NetworkReference"] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message="NetworkReference",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
