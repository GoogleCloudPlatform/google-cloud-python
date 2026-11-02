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
    package="google.cloud.hypercomputecluster.v1",
    manifest={
        "Cluster",
        "ListClustersRequest",
        "ListClustersResponse",
        "GetClusterRequest",
        "CreateClusterRequest",
        "UpdateClusterRequest",
        "DeleteClusterRequest",
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
        "SlurmPartition",
        "SlurmLoginNodes",
        "StorageConfig",
        "ComputeInstance",
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
            Optional. User-provided description of the
            cluster.
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
        network_resources (MutableMapping[str, google.cloud.hypercomputecluster_v1.types.NetworkResource]):
            Optional. Network resources available to the cluster. Must
            contain at most one value. Keys specify the ID of the
            network resource by which it can be referenced elsewhere,
            and must conform to
            `RFC-1034 <https://datatracker.ietf.org/doc/html/rfc1034>`__
            (lower-case, alphanumeric, and at most 63 characters).
        storage_resources (MutableMapping[str, google.cloud.hypercomputecluster_v1.types.StorageResource]):
            Optional. Storage resources available to the cluster. Keys
            specify the ID of the storage resource by which it can be
            referenced elsewhere, and must conform to
            `RFC-1034 <https://datatracker.ietf.org/doc/html/rfc1034>`__
            (lower-case, alphanumeric, and at most 63 characters).
        compute_resources (MutableMapping[str, google.cloud.hypercomputecluster_v1.types.ComputeResource]):
            Optional. Compute resources available to the cluster. Keys
            specify the ID of the compute resource by which it can be
            referenced elsewhere, and must conform to
            `RFC-1034 <https://datatracker.ietf.org/doc/html/rfc1034>`__
            (lower-case, alphanumeric, and at most 63 characters).
        orchestrator (google.cloud.hypercomputecluster_v1.types.Orchestrator):
            Optional. Orchestrator that is responsible
            for scheduling and running jobs on the cluster.
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


class ListClustersRequest(proto.Message):
    r"""Request message for
    [ListClusters][google.cloud.hypercomputecluster.v1.HypercomputeCluster.ListClusters].

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
    [ListClusters][google.cloud.hypercomputecluster.v1.HypercomputeCluster.ListClusters].

    Attributes:
        clusters (MutableSequence[google.cloud.hypercomputecluster_v1.types.Cluster]):
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
    [GetCluster][google.cloud.hypercomputecluster.v1.HypercomputeCluster.GetCluster].

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
    [CreateCluster][google.cloud.hypercomputecluster.v1.HypercomputeCluster.CreateCluster].

    Attributes:
        parent (str):
            Required. Parent location in which the cluster should be
            created, in the format
            ``projects/{project}/locations/{location}``.
        cluster_id (str):
            Required. ID of the cluster to create. Must conform to
            `RFC-1034 <https://datatracker.ietf.org/doc/html/rfc1034>`__
            (lower-case, alphanumeric, and at most 63 characters).
        cluster (google.cloud.hypercomputecluster_v1.types.Cluster):
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
    [UpdateCluster][google.cloud.hypercomputecluster.v1.HypercomputeCluster.UpdateCluster].

    Attributes:
        cluster (google.cloud.hypercomputecluster_v1.types.Cluster):
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
    [DeleteCluster][google.cloud.hypercomputecluster.v1.HypercomputeCluster.DeleteCluster].

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


class NetworkResource(proto.Message):
    r"""A resource representing a network that connects the various
    components of a cluster together.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        network (google.cloud.hypercomputecluster_v1.types.NetworkReference):
            Reference to a network in Google Compute
            Engine.

            This field is a member of `oneof`_ ``reference``.
        config (google.cloud.hypercomputecluster_v1.types.NetworkResourceConfig):
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
        new_network (google.cloud.hypercomputecluster_v1.types.NewNetworkConfig):
            Optional. Immutable. If set, indicates that a
            new network should be created.

            This field is a member of `oneof`_ ``config``.
        existing_network (google.cloud.hypercomputecluster_v1.types.ExistingNetworkConfig):
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
    [NetworkResourceConfig][google.cloud.hypercomputecluster.v1.NetworkResourceConfig],
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
    [NetworkResourceConfig][google.cloud.hypercomputecluster.v1.NetworkResourceConfig],
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
    r"""A resource representing a form of persistent storage that is
    accessible to compute resources in the cluster.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        filestore (google.cloud.hypercomputecluster_v1.types.FilestoreReference):
            Reference to a Filestore instance. Populated
            if and only if the storage resource was
            configured to use Filestore.

            This field is a member of `oneof`_ ``reference``.
        bucket (google.cloud.hypercomputecluster_v1.types.BucketReference):
            Reference to a Google Cloud Storage bucket.
            Populated if and only if the storage resource
            was configured to use Google Cloud Storage.

            This field is a member of `oneof`_ ``reference``.
        lustre (google.cloud.hypercomputecluster_v1.types.LustreReference):
            Reference to a Managed Lustre instance.
            Populated if and only if the storage resource
            was configured to use Managed Lustre.

            This field is a member of `oneof`_ ``reference``.
        config (google.cloud.hypercomputecluster_v1.types.StorageResourceConfig):
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
        new_filestore (google.cloud.hypercomputecluster_v1.types.NewFilestoreConfig):
            Optional. Immutable. If set, indicates that a
            new Filestore instance should be created.

            This field is a member of `oneof`_ ``config``.
        existing_filestore (google.cloud.hypercomputecluster_v1.types.ExistingFilestoreConfig):
            Optional. Immutable. If set, indicates that
            an existing Filestore instance should be
            imported.

            This field is a member of `oneof`_ ``config``.
        new_bucket (google.cloud.hypercomputecluster_v1.types.NewBucketConfig):
            Optional. Immutable. If set, indicates that a
            new Cloud Storage bucket should be created.

            This field is a member of `oneof`_ ``config``.
        existing_bucket (google.cloud.hypercomputecluster_v1.types.ExistingBucketConfig):
            Optional. Immutable. If set, indicates that
            an existing Cloud Storage bucket should be
            imported.

            This field is a member of `oneof`_ ``config``.
        new_lustre (google.cloud.hypercomputecluster_v1.types.NewLustreConfig):
            Optional. Immutable. If set, indicates that a
            new Managed Lustre instance should be created.

            This field is a member of `oneof`_ ``config``.
        existing_lustre (google.cloud.hypercomputecluster_v1.types.ExistingLustreConfig):
            Optional. Immutable. If set, indicates that
            an existing Managed Lustre instance should be
            imported.

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


class NewFilestoreConfig(proto.Message):
    r"""When set in a
    [StorageResourceConfig][google.cloud.hypercomputecluster.v1.StorageResourceConfig],
    indicates that a new
    `Filestore <https://cloud.google.com/filestore>`__ instance should
    be created.

    Attributes:
        filestore (str):
            Required. Immutable. Name of the Filestore instance to
            create, in the format
            ``projects/{project}/locations/{location}/instances/{instance}``
        description (str):
            Optional. Immutable. Description of the
            instance. Maximum of 2048 characters.
        file_shares (MutableSequence[google.cloud.hypercomputecluster_v1.types.FileShareConfig]):
            Required. Immutable. File system shares on
            the instance. Exactly one file share must be
            specified.
        tier (google.cloud.hypercomputecluster_v1.types.NewFilestoreConfig.Tier):
            Required. Immutable. Service tier to use for
            the instance.
        protocol (google.cloud.hypercomputecluster_v1.types.NewFilestoreConfig.Protocol):
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
    [StorageResourceConfig][google.cloud.hypercomputecluster.v1.StorageResourceConfig],
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
    [StorageResourceConfig][google.cloud.hypercomputecluster.v1.StorageResourceConfig],
    indicates that a new `Google Cloud
    Storage <https://cloud.google.com/storage>`__ bucket should be
    created.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        autoclass (google.cloud.hypercomputecluster_v1.types.GcsAutoclassConfig):
            Optional. Immutable. If set, indicates that the bucket
            should use
            `Autoclass <https://cloud.google.com/storage/docs/autoclass>`__.

            This field is a member of `oneof`_ ``option``.
        storage_class (google.cloud.hypercomputecluster_v1.types.NewBucketConfig.StorageClass):
            Optional. Immutable. If set, uses the
            provided storage class as the bucket's default
            storage class.

            This field is a member of `oneof`_ ``option``.
        bucket (str):
            Required. Immutable. Name of the Cloud
            Storage bucket to create.
        hierarchical_namespace (google.cloud.hypercomputecluster_v1.types.GcsHierarchicalNamespaceConfig):
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
        """

        STORAGE_CLASS_UNSPECIFIED = 0
        STANDARD = 1
        NEARLINE = 2
        COLDLINE = 3
        ARCHIVE = 4

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
        terminal_storage_class (google.cloud.hypercomputecluster_v1.types.GcsAutoclassConfig.TerminalStorageClass):
            Optional. Terminal storage class of the
            autoclass bucket
    """

    class TerminalStorageClass(proto.Enum):
        r"""Terminal storage class types of the autoclass bucket

        Values:
            TERMINAL_STORAGE_CLASS_UNSPECIFIED (0):
                Unspecified terminal storage class
        """

        TERMINAL_STORAGE_CLASS_UNSPECIFIED = 0

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
    [StorageResourceConfig][google.cloud.hypercomputecluster.v1.StorageResourceConfig],
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
    [StorageResourceConfig][google.cloud.hypercomputecluster.v1.StorageResourceConfig],
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


class ExistingLustreConfig(proto.Message):
    r"""When set in a
    [StorageResourceConfig][google.cloud.hypercomputecluster.v1.StorageResourceConfig],
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


class ComputeResource(proto.Message):
    r"""A resource defining how virtual machines and accelerators
    should be provisioned for the cluster.

    Attributes:
        config (google.cloud.hypercomputecluster_v1.types.ComputeResourceConfig):
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
        new_on_demand_instances (google.cloud.hypercomputecluster_v1.types.NewOnDemandInstancesConfig):
            Optional. Immutable. If set, indicates that
            this resource should use on-demand VMs.

            This field is a member of `oneof`_ ``config``.
        new_spot_instances (google.cloud.hypercomputecluster_v1.types.NewSpotInstancesConfig):
            Optional. Immutable. If set, indicates that
            this resource should use spot VMs.

            This field is a member of `oneof`_ ``config``.
        new_reserved_instances (google.cloud.hypercomputecluster_v1.types.NewReservedInstancesConfig):
            Optional. Immutable. If set, indicates that
            this resource should use reserved VMs.

            This field is a member of `oneof`_ ``config``.
        new_flex_start_instances (google.cloud.hypercomputecluster_v1.types.NewFlexStartInstancesConfig):
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
    [ComputeResourceConfig][google.cloud.hypercomputecluster.v1.ComputeResourceConfig],
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
    """

    zone: str = proto.Field(
        proto.STRING,
        number=1,
    )
    machine_type: str = proto.Field(
        proto.STRING,
        number=2,
    )


class NewSpotInstancesConfig(proto.Message):
    r"""When set in a
    [ComputeResourceConfig][google.cloud.hypercomputecluster.v1.ComputeResourceConfig],
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
        termination_action (google.cloud.hypercomputecluster_v1.types.NewSpotInstancesConfig.TerminationAction):
            Optional. Termination action for the
            instance. If not specified, Compute Engine sets
            the termination action to DELETE.
    """

    class TerminationAction(proto.Enum):
        r"""Specifies the termination action of the instance

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


class NewReservedInstancesConfig(proto.Message):
    r"""When set in a
    [ComputeResourceConfig][google.cloud.hypercomputecluster.v1.ComputeResourceConfig],
    indicates that VM instances should be created from a
    `reservation <https://cloud.google.com/compute/docs/instances/reservations-overview>`__.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        reservation (str):
            Optional. Immutable. Name of the reservation from which VM
            instances should be created, in the format
            ``projects/{project}/zones/{zone}/reservations/{reservation}``.

            This field is a member of `oneof`_ ``source``.
    """

    reservation: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="source",
    )


class NewFlexStartInstancesConfig(proto.Message):
    r"""When set in a
    [ComputeResourceConfig][google.cloud.hypercomputecluster.v1.ComputeResourceConfig],
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


class BootDisk(proto.Message):
    r"""A `Persistent disk <https://cloud.google.com/compute/docs/disks>`__
    used as the boot disk for a Compute Engine VM instance.

    Attributes:
        type_ (str):
            Required. Immutable. `Persistent disk
            type <https://cloud.google.com/compute/docs/disks#disk-types>`__,
            in the format
            ``projects/{project}/zones/{zone}/diskTypes/{disk_type}``.
        size_gb (int):
            Required. Immutable. Size of the disk in
            gigabytes. Must be at least 10GB.
    """

    type_: str = proto.Field(
        proto.STRING,
        number=1,
    )
    size_gb: int = proto.Field(
        proto.INT64,
        number=2,
    )


class Orchestrator(proto.Message):
    r"""The component responsible for scheduling and running
    workloads on the cluster as well as providing the user interface
    for interacting with the cluster at runtime.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        slurm (google.cloud.hypercomputecluster_v1.types.SlurmOrchestrator):
            Optional. If set, indicates that the cluster
            should use Slurm as the orchestrator.

            This field is a member of `oneof`_ ``option``.
    """

    slurm: "SlurmOrchestrator" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="option",
        message="SlurmOrchestrator",
    )


class SlurmOrchestrator(proto.Message):
    r"""When set in
    [Orchestrator][google.cloud.hypercomputecluster.v1.Orchestrator],
    indicates that the cluster should use
    `Slurm <https://slurm.schedmd.com/>`__ as the orchestrator.

    Attributes:
        login_nodes (google.cloud.hypercomputecluster_v1.types.SlurmLoginNodes):
            Required. Configuration for login nodes,
            which allow users to access the cluster over
            SSH.
        node_sets (MutableSequence[google.cloud.hypercomputecluster_v1.types.SlurmNodeSet]):
            Optional. Compute resource configuration for
            the Slurm nodesets in your cluster. If not
            specified, the cluster won't create any nodes.
        partitions (MutableSequence[google.cloud.hypercomputecluster_v1.types.SlurmPartition]):
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
        compute_instance (google.cloud.hypercomputecluster_v1.types.ComputeInstanceSlurmNodeSet):
            Optional. If set, indicates that the nodeset
            should be backed by Compute Engine instances.

            This field is a member of `oneof`_ ``type``.
        id (str):
            Required. Identifier for the nodeset, which allows it to be
            referenced by partitions. Must conform to
            `RFC-1034 <https://datatracker.ietf.org/doc/html/rfc1034>`__
            (lower-case, alphanumeric, and at most 63 characters).
        compute_id (str):
            Optional. ID of the compute resource on which this nodeset
            will run. Must match a key in the cluster's
            [compute_resources][google.cloud.hypercomputecluster.v1.Cluster.compute_resources].
        storage_configs (MutableSequence[google.cloud.hypercomputecluster_v1.types.StorageConfig]):
            Optional. How [storage
            resources][google.cloud.hypercomputecluster.v1.StorageResource]
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


class ComputeInstanceSlurmNodeSet(proto.Message):
    r"""When set in a
    [SlurmNodeSet][google.cloud.hypercomputecluster.v1.SlurmNodeSet],
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
        boot_disk (google.cloud.hypercomputecluster_v1.types.BootDisk):
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
            [SlurmNodeSet.id][google.cloud.hypercomputecluster.v1.SlurmNodeSet.id].
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
        storage_configs (MutableSequence[google.cloud.hypercomputecluster_v1.types.StorageConfig]):
            Optional. How [storage
            resources][google.cloud.hypercomputecluster.v1.StorageResource]
            should be mounted on each login node.
        instances (MutableSequence[google.cloud.hypercomputecluster_v1.types.ComputeInstance]):
            Output only. Information about the login node
            instances that were created in Compute Engine.
        boot_disk (google.cloud.hypercomputecluster_v1.types.BootDisk):
            Optional. Boot disk for the login node.
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


class StorageConfig(proto.Message):
    r"""Description of how a [storage
    resource][google.cloud.hypercomputecluster.v1.StorageResource]
    should be mounted on a VM instance.

    Attributes:
        id (str):
            Required. ID of the storage resource to mount, which must
            match a key in the cluster's
            [storage_resources][google.cloud.hypercomputecluster.v1.Cluster.storage_resources].
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


__all__ = tuple(sorted(__protobuf__.manifest))
