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
import google.type.interval_pb2 as interval_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.dataproc_v1.types import shared

__protobuf__ = proto.module(
    package="google.cloud.dataproc.v1",
    manifest={
        "Cluster",
        "ClusterConfig",
        "VirtualClusterConfig",
        "AuxiliaryServicesConfig",
        "EndpointConfig",
        "AutoscalingConfig",
        "EncryptionConfig",
        "GceClusterConfig",
        "MultiZoneConfig",
        "NodeGroupAffinity",
        "ShieldedInstanceConfig",
        "ConfidentialInstanceConfig",
        "InstanceGroupConfig",
        "StartupConfig",
        "InstanceReference",
        "ManagedGroupConfig",
        "InstanceFlexibilityPolicy",
        "FlexibleInstanceGroupConfig",
        "AcceleratorConfig",
        "DiskConfig",
        "AttachedDiskConfig",
        "AuxiliaryNodeGroup",
        "NodeGroup",
        "NodeInitializationAction",
        "ClusterStatus",
        "SecurityConfig",
        "KerberosConfig",
        "IdentityConfig",
        "SoftwareConfig",
        "LifecycleConfig",
        "MetastoreConfig",
        "ClusterMetrics",
        "DataprocMetricConfig",
        "CreateClusterRequest",
        "UpdateClusterRequest",
        "StopClusterRequest",
        "StartClusterRequest",
        "DeleteClusterRequest",
        "GetClusterRequest",
        "ListClustersRequest",
        "ListClustersResponse",
        "DiagnoseClusterRequest",
        "DiagnoseClusterResults",
        "ReservationAffinity",
    },
)


class Cluster(proto.Message):
    r"""Describes the identifying information, config, and status of
    a Dataproc cluster

    Attributes:
        project_id (str):
            Required. The Google Cloud Platform project
            ID that the cluster belongs to.
        cluster_name (str):
            Required. The cluster name, which must be
            unique within a project. The name must start
            with a lowercase letter, and can contain up to
            51 lowercase letters, numbers, and hyphens. It
            cannot end with a hyphen. The name of a deleted
            cluster can be reused.
        config (google.cloud.dataproc_v1.types.ClusterConfig):
            Optional. The cluster config for a cluster of
            Compute Engine Instances. Note that Dataproc may
            set default values, and values may change when
            clusters are updated.

            Exactly one of ClusterConfig or
            VirtualClusterConfig must be specified.
        virtual_cluster_config (google.cloud.dataproc_v1.types.VirtualClusterConfig):
            Optional. The virtual cluster config is used when creating a
            Dataproc cluster that does not directly control the
            underlying compute resources, for example, when creating a
            `Dataproc-on-GKE
            cluster <https://cloud.google.com/dataproc/docs/guides/dpgke/dataproc-gke-overview>`__.
            Dataproc may set default values, and values may change when
            clusters are updated. Exactly one of
            [config][google.cloud.dataproc.v1.Cluster.config] or
            [virtual_cluster_config][google.cloud.dataproc.v1.Cluster.virtual_cluster_config]
            must be specified.
        labels (MutableMapping[str, str]):
            Optional. The labels to associate with this cluster. Label
            **keys** must contain 1 to 63 characters, and must conform
            to `RFC 1035 <https://www.ietf.org/rfc/rfc1035.txt>`__.
            Label **values** may be empty, but, if present, must contain
            1 to 63 characters, and must conform to `RFC
            1035 <https://www.ietf.org/rfc/rfc1035.txt>`__. No more than
            32 labels can be associated with a cluster.
        status (google.cloud.dataproc_v1.types.ClusterStatus):
            Output only. Cluster status.
        status_history (MutableSequence[google.cloud.dataproc_v1.types.ClusterStatus]):
            Output only. The previous cluster status.
        cluster_uuid (str):
            Output only. A cluster UUID (Unique Universal
            Identifier). Dataproc generates this value when
            it creates the cluster.
        metrics (google.cloud.dataproc_v1.types.ClusterMetrics):
            Output only. Contains cluster daemon metrics such as HDFS
            and YARN stats.

            **Beta Feature**: This report is available for testing
            purposes only. It may be changed before final release.
    """

    project_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    cluster_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    config: "ClusterConfig" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="ClusterConfig",
    )
    virtual_cluster_config: "VirtualClusterConfig" = proto.Field(
        proto.MESSAGE,
        number=10,
        message="VirtualClusterConfig",
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=8,
    )
    status: "ClusterStatus" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="ClusterStatus",
    )
    status_history: MutableSequence["ClusterStatus"] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message="ClusterStatus",
    )
    cluster_uuid: str = proto.Field(
        proto.STRING,
        number=6,
    )
    metrics: "ClusterMetrics" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="ClusterMetrics",
    )


class ClusterConfig(proto.Message):
    r"""The cluster config.

    Attributes:
        cluster_type (google.cloud.dataproc_v1.types.ClusterConfig.ClusterType):
            Optional. The type of the cluster.
        cluster_tier (google.cloud.dataproc_v1.types.ClusterConfig.ClusterTier):
            Optional. The cluster tier.
        engine (google.cloud.dataproc_v1.types.ClusterConfig.Engine):
            Optional. The cluster engine.
        config_bucket (str):
            Optional. A Cloud Storage bucket used to stage job
            dependencies, config files, and job driver console output.
            If you do not specify a staging bucket, Cloud Dataproc will
            determine a Cloud Storage location (US, ASIA, or EU) for
            your cluster's staging bucket according to the Compute
            Engine zone where your cluster is deployed, and then create
            and manage this project-level, per-location bucket (see
            `Dataproc staging and temp
            buckets <https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/staging-bucket>`__).
            **This field requires a Cloud Storage bucket name, not a
            ``gs://...`` URI to a Cloud Storage bucket.**
        temp_bucket (str):
            Optional. A Cloud Storage bucket used to store ephemeral
            cluster and jobs data, such as Spark and MapReduce history
            files. If you do not specify a temp bucket, Dataproc will
            determine a Cloud Storage location (US, ASIA, or EU) for
            your cluster's temp bucket according to the Compute Engine
            zone where your cluster is deployed, and then create and
            manage this project-level, per-location bucket. The default
            bucket has a TTL of 90 days, but you can use any TTL (or
            none) if you specify a bucket (see `Dataproc staging and
            temp
            buckets <https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/staging-bucket>`__).
            **This field requires a Cloud Storage bucket name, not a
            ``gs://...`` URI to a Cloud Storage bucket.**
        gce_cluster_config (google.cloud.dataproc_v1.types.GceClusterConfig):
            Optional. The shared Compute Engine config
            settings for all instances in a cluster.
        master_config (google.cloud.dataproc_v1.types.InstanceGroupConfig):
            Optional. The Compute Engine config settings
            for the cluster's master instance.
        worker_config (google.cloud.dataproc_v1.types.InstanceGroupConfig):
            Optional. The Compute Engine config settings
            for the cluster's worker instances.
        secondary_worker_config (google.cloud.dataproc_v1.types.InstanceGroupConfig):
            Optional. The Compute Engine config settings
            for a cluster's secondary worker instances
        software_config (google.cloud.dataproc_v1.types.SoftwareConfig):
            Optional. The config settings for cluster
            software.
        initialization_actions (MutableSequence[google.cloud.dataproc_v1.types.NodeInitializationAction]):
            Optional. Commands to execute on each node after config is
            completed. By default, executables are run on master and all
            worker nodes. You can test a node's ``role`` metadata to run
            an executable on a master or worker node, as shown below
            using ``curl`` (you can also use ``wget``):

            ::

                ROLE=$(curl -H Metadata-Flavor:Google
                http://metadata/computeMetadata/v1/instance/attributes/dataproc-role)
                if [[ "${ROLE}" == 'Master' ]]; then
                  ... master specific actions ...
                else
                  ... worker specific actions ...
                fi
        encryption_config (google.cloud.dataproc_v1.types.EncryptionConfig):
            Optional. Encryption settings for the
            cluster.
        autoscaling_config (google.cloud.dataproc_v1.types.AutoscalingConfig):
            Optional. Autoscaling config for the policy
            associated with the cluster. Cluster does not
            autoscale if this field is unset.
        security_config (google.cloud.dataproc_v1.types.SecurityConfig):
            Optional. Security settings for the cluster.
        lifecycle_config (google.cloud.dataproc_v1.types.LifecycleConfig):
            Optional. Lifecycle setting for the cluster.
        endpoint_config (google.cloud.dataproc_v1.types.EndpointConfig):
            Optional. Port/endpoint configuration for
            this cluster
        metastore_config (google.cloud.dataproc_v1.types.MetastoreConfig):
            Optional. Metastore configuration.
        dataproc_metric_config (google.cloud.dataproc_v1.types.DataprocMetricConfig):
            Optional. The config for Dataproc metrics.
        auxiliary_node_groups (MutableSequence[google.cloud.dataproc_v1.types.AuxiliaryNodeGroup]):
            Optional. The node group settings.
        master_flexible_config (google.cloud.dataproc_v1.types.FlexibleInstanceGroupConfig):
            Optional. The High Obtainability (HO) config settings for
            the cluster's master instances.

            In High Obtainability (HO) mode, flexible configs are the
            single source of truth for desired cluster configuration
            across node groups:

            - For single-node clusters: ``master_flexible_config`` must
              be specified, and no worker configs should be set.
            - For multi-node (standard) clusters: both
              ``master_flexible_config`` and
              [worker_flexible_config][google.cloud.dataproc.v1.ClusterConfig.worker_flexible_config]
              must be specified. Mixing standard and flexible configs
              across node groups is not allowed.

            Only one of
            [master_config][google.cloud.dataproc.v1.ClusterConfig.master_config]
            or ``master_flexible_config`` can be set.
        worker_flexible_config (google.cloud.dataproc_v1.types.FlexibleInstanceGroupConfig):
            Optional. The High Obtainability (HO) config settings for
            the cluster's worker instances.

            In High Obtainability (HO) mode, flexible configs are the
            single source of truth for desired cluster configuration.
            ``num_instances`` represents the desired capacity of the
            worker group and is mutable via cluster updates and
            autoscaling.

            Only one of
            [worker_config][google.cloud.dataproc.v1.ClusterConfig.worker_config]
            or ``worker_flexible_config`` can be set.

            In High Obtainability (HO) mode, for multi-node (standard)
            clusters, both
            [master_flexible_config][google.cloud.dataproc.v1.ClusterConfig.master_flexible_config]
            and ``worker_flexible_config`` must be specified. Mixing
            standard and flexible configs across node groups is not
            allowed. Single-node clusters do not specify worker configs.
        secondary_worker_flexible_config (google.cloud.dataproc_v1.types.FlexibleInstanceGroupConfig):
            Optional. The High Obtainability (HO) config settings for a
            cluster's secondary worker instances.

            In High Obtainability (HO) mode, flexible configs are the
            single source of truth for desired cluster configuration.
            ``num_instances`` represents the desired capacity of the
            secondary worker group and is mutable via cluster updates
            and autoscaling.

            Only one of
            [secondary_worker_config][google.cloud.dataproc.v1.ClusterConfig.secondary_worker_config]
            or ``secondary_worker_flexible_config`` can be set.

            In High Obtainability (HO) mode, secondary workers are
            optional. If secondary workers are used in an HO cluster,
            they must be configured using
            ``secondary_worker_flexible_config`` (not
            ``secondary_worker_config``).
    """

    class ClusterType(proto.Enum):
        r"""The type of the cluster.

        Values:
            CLUSTER_TYPE_UNSPECIFIED (0):
                Not set.
            STANDARD (1):
                Standard dataproc cluster with a minimum of
                two primary workers.
            SINGLE_NODE (2):
                https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/single-node-clusters
            ZERO_SCALE (3):
                Clusters that can use only secondary workers
                and be scaled down to zero secondary worker
                nodes.
        """

        CLUSTER_TYPE_UNSPECIFIED = 0
        STANDARD = 1
        SINGLE_NODE = 2
        ZERO_SCALE = 3

    class ClusterTier(proto.Enum):
        r"""The cluster tier.

        Values:
            CLUSTER_TIER_UNSPECIFIED (0):
                Not set. Works the same as CLUSTER_TIER_STANDARD.
            CLUSTER_TIER_STANDARD (1):
                Standard Dataproc cluster.
            CLUSTER_TIER_PREMIUM (2):
                Premium Dataproc cluster.
        """

        CLUSTER_TIER_UNSPECIFIED = 0
        CLUSTER_TIER_STANDARD = 1
        CLUSTER_TIER_PREMIUM = 2

    class Engine(proto.Enum):
        r"""The cluster engine.

        Values:
            ENGINE_UNSPECIFIED (0):
                The engine is not specified. Works the same as
                ENGINE_DEFAULT.
            DEFAULT (1):
                The cluster is a default engine cluster.
            LIGHTNING (2):
                The cluster is a lightning engine cluster.
        """

        ENGINE_UNSPECIFIED = 0
        DEFAULT = 1
        LIGHTNING = 2

    cluster_type: ClusterType = proto.Field(
        proto.ENUM,
        number=27,
        enum=ClusterType,
    )
    cluster_tier: ClusterTier = proto.Field(
        proto.ENUM,
        number=29,
        enum=ClusterTier,
    )
    engine: Engine = proto.Field(
        proto.ENUM,
        number=30,
        enum=Engine,
    )
    config_bucket: str = proto.Field(
        proto.STRING,
        number=1,
    )
    temp_bucket: str = proto.Field(
        proto.STRING,
        number=2,
    )
    gce_cluster_config: "GceClusterConfig" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="GceClusterConfig",
    )
    master_config: "InstanceGroupConfig" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="InstanceGroupConfig",
    )
    worker_config: "InstanceGroupConfig" = proto.Field(
        proto.MESSAGE,
        number=10,
        message="InstanceGroupConfig",
    )
    secondary_worker_config: "InstanceGroupConfig" = proto.Field(
        proto.MESSAGE,
        number=12,
        message="InstanceGroupConfig",
    )
    software_config: "SoftwareConfig" = proto.Field(
        proto.MESSAGE,
        number=13,
        message="SoftwareConfig",
    )
    initialization_actions: MutableSequence["NodeInitializationAction"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=11,
            message="NodeInitializationAction",
        )
    )
    encryption_config: "EncryptionConfig" = proto.Field(
        proto.MESSAGE,
        number=15,
        message="EncryptionConfig",
    )
    autoscaling_config: "AutoscalingConfig" = proto.Field(
        proto.MESSAGE,
        number=18,
        message="AutoscalingConfig",
    )
    security_config: "SecurityConfig" = proto.Field(
        proto.MESSAGE,
        number=16,
        message="SecurityConfig",
    )
    lifecycle_config: "LifecycleConfig" = proto.Field(
        proto.MESSAGE,
        number=17,
        message="LifecycleConfig",
    )
    endpoint_config: "EndpointConfig" = proto.Field(
        proto.MESSAGE,
        number=19,
        message="EndpointConfig",
    )
    metastore_config: "MetastoreConfig" = proto.Field(
        proto.MESSAGE,
        number=20,
        message="MetastoreConfig",
    )
    dataproc_metric_config: "DataprocMetricConfig" = proto.Field(
        proto.MESSAGE,
        number=23,
        message="DataprocMetricConfig",
    )
    auxiliary_node_groups: MutableSequence["AuxiliaryNodeGroup"] = proto.RepeatedField(
        proto.MESSAGE,
        number=25,
        message="AuxiliaryNodeGroup",
    )
    master_flexible_config: "FlexibleInstanceGroupConfig" = proto.Field(
        proto.MESSAGE,
        number=31,
        message="FlexibleInstanceGroupConfig",
    )
    worker_flexible_config: "FlexibleInstanceGroupConfig" = proto.Field(
        proto.MESSAGE,
        number=32,
        message="FlexibleInstanceGroupConfig",
    )
    secondary_worker_flexible_config: "FlexibleInstanceGroupConfig" = proto.Field(
        proto.MESSAGE,
        number=33,
        message="FlexibleInstanceGroupConfig",
    )


class VirtualClusterConfig(proto.Message):
    r"""The Dataproc cluster config for a cluster that does not directly
    control the underlying compute resources, such as a `Dataproc-on-GKE
    cluster <https://cloud.google.com/dataproc/docs/guides/dpgke/dataproc-gke-overview>`__.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        staging_bucket (str):
            Optional. A Cloud Storage bucket used to stage job
            dependencies, config files, and job driver console output.
            If you do not specify a staging bucket, Cloud Dataproc will
            determine a Cloud Storage location (US, ASIA, or EU) for
            your cluster's staging bucket according to the Compute
            Engine zone where your cluster is deployed, and then create
            and manage this project-level, per-location bucket (see
            `Dataproc staging and temp
            buckets <https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/staging-bucket>`__).
            **This field requires a Cloud Storage bucket name, not a
            ``gs://...`` URI to a Cloud Storage bucket.**
        kubernetes_cluster_config (google.cloud.dataproc_v1.types.KubernetesClusterConfig):
            Required. The configuration for running the
            Dataproc cluster on Kubernetes.

            This field is a member of `oneof`_ ``infrastructure_config``.
        auxiliary_services_config (google.cloud.dataproc_v1.types.AuxiliaryServicesConfig):
            Optional. Configuration of auxiliary services
            used by this cluster.
    """

    staging_bucket: str = proto.Field(
        proto.STRING,
        number=1,
    )
    kubernetes_cluster_config: shared.KubernetesClusterConfig = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="infrastructure_config",
        message=shared.KubernetesClusterConfig,
    )
    auxiliary_services_config: "AuxiliaryServicesConfig" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="AuxiliaryServicesConfig",
    )


class AuxiliaryServicesConfig(proto.Message):
    r"""Auxiliary services configuration for a Cluster.

    Attributes:
        metastore_config (google.cloud.dataproc_v1.types.MetastoreConfig):
            Optional. The Hive Metastore configuration
            for this workload.
        spark_history_server_config (google.cloud.dataproc_v1.types.SparkHistoryServerConfig):
            Optional. The Spark History Server
            configuration for the workload.
    """

    metastore_config: "MetastoreConfig" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="MetastoreConfig",
    )
    spark_history_server_config: shared.SparkHistoryServerConfig = proto.Field(
        proto.MESSAGE,
        number=2,
        message=shared.SparkHistoryServerConfig,
    )


class EndpointConfig(proto.Message):
    r"""Endpoint config for this cluster

    Attributes:
        http_ports (MutableMapping[str, str]):
            Output only. The map of port descriptions to URLs. Will only
            be populated if enable_http_port_access is true.
        enable_http_port_access (bool):
            Optional. If true, enable http access to
            specific ports on the cluster from external
            sources. Defaults to false.
    """

    http_ports: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=1,
    )
    enable_http_port_access: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class AutoscalingConfig(proto.Message):
    r"""Autoscaling Policy config associated with the cluster.

    Attributes:
        policy_uri (str):
            Optional. The autoscaling policy used by the cluster.

            Only resource names including projectid and location
            (region) are valid. Examples:

            - ``https://www.googleapis.com/compute/v1/projects/[project_id]/locations/[dataproc_region]/autoscalingPolicies/[policy_id]``
            - ``projects/[project_id]/locations/[dataproc_region]/autoscalingPolicies/[policy_id]``

            Note that the policy must be in the same project and
            Dataproc region.
    """

    policy_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )


class EncryptionConfig(proto.Message):
    r"""Encryption settings for the cluster.

    Attributes:
        gce_pd_kms_key_name (str):
            Optional. The Cloud KMS key resource name to use for
            persistent disk encryption for all instances in the cluster.
            See [Use CMEK with cluster data]
            (https://cloud.google.com//dataproc/docs/concepts/configuring-clusters/customer-managed-encryption#use_cmek_with_cluster_data)
            for more information.
        kms_key (str):
            Optional. The Cloud KMS key resource name to use for cluster
            persistent disk and job argument encryption. See [Use CMEK
            with cluster data]
            (https://cloud.google.com//dataproc/docs/concepts/configuring-clusters/customer-managed-encryption#use_cmek_with_cluster_data)
            for more information.

            When this key resource name is provided, the following job
            arguments of the following job types submitted to the
            cluster are encrypted using CMEK:

            - `FlinkJob
              args <https://cloud.google.com/dataproc/docs/reference/rest/v1/FlinkJob>`__
            - `HadoopJob
              args <https://cloud.google.com/dataproc/docs/reference/rest/v1/HadoopJob>`__
            - `SparkJob
              args <https://cloud.google.com/dataproc/docs/reference/rest/v1/SparkJob>`__
            - `SparkRJob
              args <https://cloud.google.com/dataproc/docs/reference/rest/v1/SparkRJob>`__
            - `PySparkJob
              args <https://cloud.google.com/dataproc/docs/reference/rest/v1/PySparkJob>`__
            - `SparkSqlJob <https://cloud.google.com/dataproc/docs/reference/rest/v1/SparkSqlJob>`__
              scriptVariables and queryList.queries
            - `HiveJob <https://cloud.google.com/dataproc/docs/reference/rest/v1/HiveJob>`__
              scriptVariables and queryList.queries
            - `PigJob <https://cloud.google.com/dataproc/docs/reference/rest/v1/PigJob>`__
              scriptVariables and queryList.queries
            - `PrestoJob <https://cloud.google.com/dataproc/docs/reference/rest/v1/PrestoJob>`__
              scriptVariables and queryList.queries
    """

    gce_pd_kms_key_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    kms_key: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GceClusterConfig(proto.Message):
    r"""Common config settings for resources of Compute Engine
    cluster instances, applicable to all instances in the cluster.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        zone_uri (str):
            Optional. The Compute Engine zone where the Dataproc cluster
            will be located. If omitted, the service will pick a zone in
            the cluster's Compute Engine region. On a get request, zone
            will always be present.

            A full URL, partial URI, or short name are valid. Examples:

            - ``https://www.googleapis.com/compute/v1/projects/[project_id]/zones/[zone]``
            - ``projects/[project_id]/zones/[zone]``
            - ``[zone]``
        multi_zone_config (google.cloud.dataproc_v1.types.MultiZoneConfig):
            Optional. Controls how instances within this Cluster are
            allowed to exist in multiple Zones within the Region. Only
            one of ``zone_uri`` or ``multi_zone_config`` must be set.
        network_uri (str):
            Optional. The Compute Engine network to be used for machine
            communications. Cannot be specified with subnetwork_uri. If
            neither ``network_uri`` nor ``subnetwork_uri`` is specified,
            the "default" network of the project is used, if it exists.
            Cannot be a "Custom Subnet Network" (see `Using
            Subnetworks <https://cloud.google.com/compute/docs/subnetworks>`__
            for more information).

            A full URL, partial URI, or short name are valid. Examples:

            - ``https://www.googleapis.com/compute/v1/projects/[project_id]/global/networks/default``
            - ``projects/[project_id]/global/networks/default``
            - ``default``
        subnetwork_uri (str):
            Optional. The Compute Engine subnetwork to be used for
            machine communications. Cannot be specified with
            network_uri.

            A full URL, partial URI, or short name are valid. Examples:

            - ``https://www.googleapis.com/compute/v1/projects/[project_id]/regions/[region]/subnetworks/sub0``
            - ``projects/[project_id]/regions/[region]/subnetworks/sub0``
            - ``sub0``
        internal_ip_only (bool):
            Optional. This setting applies to subnetwork-enabled
            networks. It is set to ``true`` by default in clusters
            created with image versions 2.2.x.

            When set to ``true``:

            - All cluster VMs have internal IP addresses.
            - [Google Private Access]
              (https://cloud.google.com/vpc/docs/private-google-access)
              must be enabled to access Dataproc and other Google Cloud
              APIs.
            - Off-cluster dependencies must be configured to be
              accessible without external IP addresses.

            When set to ``false``:

            - Cluster VMs are not restricted to internal IP addresses.
            - Ephemeral external IP addresses are assigned to each
              cluster VM.

            This field is a member of `oneof`_ ``_internal_ip_only``.
        private_ipv6_google_access (google.cloud.dataproc_v1.types.GceClusterConfig.PrivateIpv6GoogleAccess):
            Optional. The type of IPv6 access for a
            cluster.
        service_account (str):
            Optional. The `Dataproc service
            account <https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/service-accounts#service_accounts_in_dataproc>`__
            (also see `VM Data Plane
            identity <https://cloud.google.com/dataproc/docs/concepts/iam/dataproc-principals#vm_service_account_data_plane_identity>`__)
            used by Dataproc cluster VM instances to access Google Cloud
            Platform services.

            If not specified, the `Compute Engine default service
            account <https://cloud.google.com/compute/docs/access/service-accounts#default_service_account>`__
            is used.
        service_account_scopes (MutableSequence[str]):
            Optional. The URIs of service account scopes to be included
            in Compute Engine instances. The following base set of
            scopes is always included:

            - https://www.googleapis.com/auth/cloud.useraccounts.readonly
            - https://www.googleapis.com/auth/devstorage.read_write
            - https://www.googleapis.com/auth/logging.write

            If no scopes are specified, the following defaults are also
            provided:

            - https://www.googleapis.com/auth/bigquery
            - https://www.googleapis.com/auth/bigtable.admin.table
            - https://www.googleapis.com/auth/bigtable.data
            - https://www.googleapis.com/auth/devstorage.full_control
        tags (MutableSequence[str]):
            The Compute Engine network tags to add to all instances (see
            `Tagging
            instances <https://cloud.google.com/vpc/docs/add-remove-network-tags>`__).
        metadata (MutableMapping[str, str]):
            Optional. The Compute Engine metadata entries to add to all
            instances (see `Project and instance
            metadata <https://cloud.google.com/compute/docs/storing-retrieving-metadata#project_and_instance_metadata>`__).
        reservation_affinity (google.cloud.dataproc_v1.types.ReservationAffinity):
            Optional. Reservation Affinity for consuming
            Zonal reservation.
        node_group_affinity (google.cloud.dataproc_v1.types.NodeGroupAffinity):
            Optional. Node Group Affinity for sole-tenant
            clusters.
        shielded_instance_config (google.cloud.dataproc_v1.types.ShieldedInstanceConfig):
            Optional. Shielded Instance Config for clusters using
            `Compute Engine Shielded
            VMs <https://cloud.google.com/security/shielded-cloud/shielded-vm>`__.
        confidential_instance_config (google.cloud.dataproc_v1.types.ConfidentialInstanceConfig):
            Optional. Confidential Instance Config for clusters using
            `Confidential
            VMs <https://cloud.google.com/confidential-computing/confidential-vm/docs>`__.
        resource_manager_tags (MutableMapping[str, str]):
            Optional. [Resource manager tags]
            (https://cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing)
            to add to all instances (see [Use secure tags]
            (https://cloud.google.com/dataproc/docs/guides/use-secure-tags)).
    """

    class PrivateIpv6GoogleAccess(proto.Enum):
        r"""``PrivateIpv6GoogleAccess`` controls whether and how Dataproc
        cluster nodes can communicate with Google Services through gRPC over
        IPv6. These values are directly mapped to corresponding values in
        the `Compute Engine Instance
        fields <https://cloud.google.com/compute/docs/reference/rest/v1/instances>`__.

        Values:
            PRIVATE_IPV6_GOOGLE_ACCESS_UNSPECIFIED (0):
                If unspecified, Compute Engine default behavior will apply,
                which is the same as
                [INHERIT_FROM_SUBNETWORK][google.cloud.dataproc.v1.GceClusterConfig.PrivateIpv6GoogleAccess.INHERIT_FROM_SUBNETWORK].
            INHERIT_FROM_SUBNETWORK (1):
                Private access to and from Google Services
                configuration inherited from the subnetwork
                configuration. This is the default Compute
                Engine behavior.
            OUTBOUND (2):
                Enables outbound private IPv6 access to
                Google Services from the Dataproc cluster.
            BIDIRECTIONAL (3):
                Enables bidirectional private IPv6 access
                between Google Services and the Dataproc
                cluster.
        """

        PRIVATE_IPV6_GOOGLE_ACCESS_UNSPECIFIED = 0
        INHERIT_FROM_SUBNETWORK = 1
        OUTBOUND = 2
        BIDIRECTIONAL = 3

    zone_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    multi_zone_config: "MultiZoneConfig" = proto.Field(
        proto.MESSAGE,
        number=19,
        message="MultiZoneConfig",
    )
    network_uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    subnetwork_uri: str = proto.Field(
        proto.STRING,
        number=6,
    )
    internal_ip_only: bool = proto.Field(
        proto.BOOL,
        number=7,
        optional=True,
    )
    private_ipv6_google_access: PrivateIpv6GoogleAccess = proto.Field(
        proto.ENUM,
        number=12,
        enum=PrivateIpv6GoogleAccess,
    )
    service_account: str = proto.Field(
        proto.STRING,
        number=8,
    )
    service_account_scopes: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    tags: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    metadata: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )
    reservation_affinity: "ReservationAffinity" = proto.Field(
        proto.MESSAGE,
        number=11,
        message="ReservationAffinity",
    )
    node_group_affinity: "NodeGroupAffinity" = proto.Field(
        proto.MESSAGE,
        number=13,
        message="NodeGroupAffinity",
    )
    shielded_instance_config: "ShieldedInstanceConfig" = proto.Field(
        proto.MESSAGE,
        number=14,
        message="ShieldedInstanceConfig",
    )
    confidential_instance_config: "ConfidentialInstanceConfig" = proto.Field(
        proto.MESSAGE,
        number=15,
        message="ConfidentialInstanceConfig",
    )
    resource_manager_tags: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=16,
    )


class MultiZoneConfig(proto.Message):
    r"""Configuration for multi-zonal clusters that can create
    instances across multiple Zones within the Region.

    Attributes:
        target_shape (google.cloud.dataproc_v1.types.MultiZoneConfig.TargetShape):
            Optional. The distribution shape of the nodes
            in the multi-zonal cluster.
    """

    class TargetShape(proto.Enum):
        r"""The distribution shape of the nodes in the multi-zonal
        cluster.

        Values:
            TARGET_SHAPE_UNSPECIFIED (0):
                Target shape is unspecified. Setting this
                will cause error.
            ANY (1):
                Instances may exist in any Zones within the
                Region.
        """

        TARGET_SHAPE_UNSPECIFIED = 0
        ANY = 1

    target_shape: TargetShape = proto.Field(
        proto.ENUM,
        number=1,
        enum=TargetShape,
    )


class NodeGroupAffinity(proto.Message):
    r"""Node Group Affinity for clusters using sole-tenant node groups.
    **The Dataproc ``NodeGroupAffinity`` resource is not related to the
    Dataproc [NodeGroup][google.cloud.dataproc.v1.NodeGroup] resource.**

    Attributes:
        node_group_uri (str):
            Required. The URI of a sole-tenant `node group
            resource <https://cloud.google.com/compute/docs/reference/rest/v1/nodeGroups>`__
            that the cluster will be created on.

            A full URL, partial URI, or node group name are valid.
            Examples:

            - ``https://www.googleapis.com/compute/v1/projects/[project_id]/zones/[zone]/nodeGroups/node-group-1``
            - ``projects/[project_id]/zones/[zone]/nodeGroups/node-group-1``
            - ``node-group-1``
    """

    node_group_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ShieldedInstanceConfig(proto.Message):
    r"""Shielded Instance Config for clusters using `Compute Engine Shielded
    VMs <https://cloud.google.com/security/shielded-cloud/shielded-vm>`__.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        enable_secure_boot (bool):
            Optional. Defines whether instances have
            Secure Boot enabled.

            This field is a member of `oneof`_ ``_enable_secure_boot``.
        enable_vtpm (bool):
            Optional. Defines whether instances have the
            vTPM enabled.

            This field is a member of `oneof`_ ``_enable_vtpm``.
        enable_integrity_monitoring (bool):
            Optional. Defines whether instances have
            integrity monitoring enabled.

            This field is a member of `oneof`_ ``_enable_integrity_monitoring``.
    """

    enable_secure_boot: bool = proto.Field(
        proto.BOOL,
        number=1,
        optional=True,
    )
    enable_vtpm: bool = proto.Field(
        proto.BOOL,
        number=2,
        optional=True,
    )
    enable_integrity_monitoring: bool = proto.Field(
        proto.BOOL,
        number=3,
        optional=True,
    )


class ConfidentialInstanceConfig(proto.Message):
    r"""Confidential Instance Config for clusters using `Confidential
    VMs <https://cloud.google.com/confidential-computing/confidential-vm/docs>`__

    Attributes:
        enable_confidential_compute (bool):
            Optional. Deprecated: Use 'confidential_instance_type'
            instead. Defines whether the instance should have
            confidential compute enabled.
        confidential_instance_type (google.cloud.dataproc_v1.types.ConfidentialInstanceConfig.ConfidentialInstanceType):
            Optional. Defines the type of Confidential
            Compute technology to use.
    """

    class ConfidentialInstanceType(proto.Enum):
        r"""The type of Confidential Compute technology as per `Confidential
        Computing
        types <https://cloud.google.com/confidential-computing/confidential-vm/docs/create-a-confidential-vm-instance#create-instance>`__.
        New values may be added in the future.

        Values:
            CONFIDENTIAL_INSTANCE_TYPE_UNSPECIFIED (0):
                Confidential Instance Type is not specified.
            SEV (1):
                `AMD Secure Encrypted
                Virtualization <https://cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview#amd_sev>`__
            SEV_SNP (2):
                `AMD Secure Encrypted Virtualization-Secure Nested
                Paging <https://cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview#amd_sev-snp>`__
            TDX (3):
                `Intel Trust Domain
                Extensions <https://cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview#intel_tdx>`__
        """

        CONFIDENTIAL_INSTANCE_TYPE_UNSPECIFIED = 0
        SEV = 1
        SEV_SNP = 2
        TDX = 3

    enable_confidential_compute: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    confidential_instance_type: ConfidentialInstanceType = proto.Field(
        proto.ENUM,
        number=2,
        enum=ConfidentialInstanceType,
    )


class InstanceGroupConfig(proto.Message):
    r"""The config settings for Compute Engine resources in
    an instance group, such as a master or worker group.

    Attributes:
        num_instances (int):
            Optional. The number of VM instances in the instance group.
            For `HA
            cluster </dataproc/docs/concepts/configuring-clusters/high-availability>`__
            `master_config <#FIELDS.master_config>`__ groups, **must be
            set to 3**. For standard cluster
            `master_config <#FIELDS.master_config>`__ groups, **must be
            set to 1**.
        instance_names (MutableSequence[str]):
            Output only. The list of instance names. Dataproc derives
            the names from ``cluster_name``, ``num_instances``, and the
            instance group.
        instance_references (MutableSequence[google.cloud.dataproc_v1.types.InstanceReference]):
            Output only. List of references to Compute
            Engine instances.
        image_uri (str):
            Optional. The Compute Engine image resource used for cluster
            instances.

            The URI can represent an image or image family.

            Image examples:

            - ``https://www.googleapis.com/compute/v1/projects/[project_id]/global/images/[image-id]``
            - ``projects/[project_id]/global/images/[image-id]``
            - ``image-id``

            Image family examples. Dataproc will use the most recent
            image from the family:

            - ``https://www.googleapis.com/compute/v1/projects/[project_id]/global/images/family/[custom-image-family-name]``
            - ``projects/[project_id]/global/images/family/[custom-image-family-name]``

            If the URI is unspecified, it will be inferred from
            ``SoftwareConfig.image_version`` or the system default.
        machine_type_uri (str):
            Optional. The Compute Engine machine type used for cluster
            instances.

            A full URL, partial URI, or short name are valid. Examples:

            - ``https://www.googleapis.com/compute/v1/projects/[project_id]/zones/[zone]/machineTypes/n1-standard-2``
            - ``projects/[project_id]/zones/[zone]/machineTypes/n1-standard-2``
            - ``n1-standard-2``

            **Auto Zone Exception**: If you are using the Dataproc `Auto
            Zone
            Placement <https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/auto-zone#using_auto_zone_placement>`__
            feature, you must use the short name of the machine type
            resource, for example, ``n1-standard-2``.
        disk_config (google.cloud.dataproc_v1.types.DiskConfig):
            Optional. Disk option config settings.
        is_preemptible (bool):
            Output only. Specifies that this instance
            group contains preemptible instances.
        preemptibility (google.cloud.dataproc_v1.types.InstanceGroupConfig.Preemptibility):
            Optional. Specifies the preemptibility of the instance
            group.

            The default value for master and worker groups is
            ``NON_PREEMPTIBLE``. This default cannot be changed.

            The default value for secondary instances is
            ``PREEMPTIBLE``.
        managed_group_config (google.cloud.dataproc_v1.types.ManagedGroupConfig):
            Output only. The config for Compute Engine
            Instance Group Manager that manages this group.
            This is only used for preemptible instance
            groups.
        accelerators (MutableSequence[google.cloud.dataproc_v1.types.AcceleratorConfig]):
            Optional. The Compute Engine accelerator
            configuration for these instances.
        min_cpu_platform (str):
            Optional. Specifies the minimum cpu platform for the
            Instance Group. See `Dataproc -> Minimum CPU
            Platform <https://cloud.google.com/dataproc/docs/concepts/compute/dataproc-min-cpu>`__.
        min_num_instances (int):
            Optional. The minimum number of primary worker instances to
            create. If ``min_num_instances`` is set, cluster creation
            will succeed if the number of primary workers created is at
            least equal to the ``min_num_instances`` number.

            Example: Cluster creation request with ``num_instances`` =
            ``5`` and ``min_num_instances`` = ``3``:

            - If 4 VMs are created and 1 instance fails, the failed VM
              is deleted. The cluster is resized to 4 instances and
              placed in a ``RUNNING`` state.
            - If 2 instances are created and 3 instances fail, the
              cluster in placed in an ``ERROR`` state. The failed VMs
              are not deleted.
        instance_flexibility_policy (google.cloud.dataproc_v1.types.InstanceFlexibilityPolicy):
            Optional. Instance flexibility Policy
            allowing a mixture of VM shapes and provisioning
            models.
        startup_config (google.cloud.dataproc_v1.types.StartupConfig):
            Optional. Configuration to handle the startup
            of instances during cluster create and update
            process.
    """

    class Preemptibility(proto.Enum):
        r"""Controls the use of preemptible instances within the group.

        Values:
            PREEMPTIBILITY_UNSPECIFIED (0):
                Preemptibility is unspecified, the system
                will choose the appropriate setting for each
                instance group.
            NON_PREEMPTIBLE (1):
                Instances are non-preemptible.

                This option is allowed for all instance groups
                and is the only valid value for Master and
                Worker instance groups.
            PREEMPTIBLE (2):
                Instances are [preemptible]
                (https://cloud.google.com/compute/docs/instances/preemptible).

                This option is allowed only for [secondary worker]
                (https://cloud.google.com/dataproc/docs/concepts/compute/secondary-vms)
                groups.
            SPOT (3):
                Instances are [Spot VMs]
                (https://cloud.google.com/compute/docs/instances/spot).

                This option is allowed only for [secondary worker]
                (https://cloud.google.com/dataproc/docs/concepts/compute/secondary-vms)
                groups. Spot VMs are the latest version of [preemptible VMs]
                (https://cloud.google.com/compute/docs/instances/preemptible),
                and provide additional features.
        """

        PREEMPTIBILITY_UNSPECIFIED = 0
        NON_PREEMPTIBLE = 1
        PREEMPTIBLE = 2
        SPOT = 3

    num_instances: int = proto.Field(
        proto.INT32,
        number=1,
    )
    instance_names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    instance_references: MutableSequence["InstanceReference"] = proto.RepeatedField(
        proto.MESSAGE,
        number=11,
        message="InstanceReference",
    )
    image_uri: str = proto.Field(
        proto.STRING,
        number=3,
    )
    machine_type_uri: str = proto.Field(
        proto.STRING,
        number=4,
    )
    disk_config: "DiskConfig" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="DiskConfig",
    )
    is_preemptible: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    preemptibility: Preemptibility = proto.Field(
        proto.ENUM,
        number=10,
        enum=Preemptibility,
    )
    managed_group_config: "ManagedGroupConfig" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="ManagedGroupConfig",
    )
    accelerators: MutableSequence["AcceleratorConfig"] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message="AcceleratorConfig",
    )
    min_cpu_platform: str = proto.Field(
        proto.STRING,
        number=9,
    )
    min_num_instances: int = proto.Field(
        proto.INT32,
        number=12,
    )
    instance_flexibility_policy: "InstanceFlexibilityPolicy" = proto.Field(
        proto.MESSAGE,
        number=13,
        message="InstanceFlexibilityPolicy",
    )
    startup_config: "StartupConfig" = proto.Field(
        proto.MESSAGE,
        number=14,
        message="StartupConfig",
    )


class StartupConfig(proto.Message):
    r"""Configuration to handle the startup of instances during
    cluster create and update process.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        required_registration_fraction (float):
            Optional. The config setting to enable cluster creation/
            updation to be successful only after
            required_registration_fraction of instances are up and
            running. This configuration is applicable to only secondary
            workers for now. The cluster will fail if
            required_registration_fraction of instances are not
            available. This will include instance creation, agent
            registration, and service registration (if enabled).

            This field is a member of `oneof`_ ``_required_registration_fraction``.
    """

    required_registration_fraction: float = proto.Field(
        proto.DOUBLE,
        number=1,
        optional=True,
    )


class InstanceReference(proto.Message):
    r"""A reference to a Compute Engine instance.

    Attributes:
        instance_name (str):
            The user-friendly name of the Compute Engine
            instance.
        instance_id (str):
            The unique identifier of the Compute Engine
            instance.
        public_key (str):
            The public RSA key used for sharing data with
            this instance.
        public_ecies_key (str):
            The public ECIES key used for sharing data
            with this instance.
    """

    instance_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    instance_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    public_key: str = proto.Field(
        proto.STRING,
        number=3,
    )
    public_ecies_key: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ManagedGroupConfig(proto.Message):
    r"""Specifies the resources used to actively manage an instance
    group.

    Attributes:
        instance_template_name (str):
            Output only. The name of the Instance
            Template used for the Managed Instance Group.
        instance_group_manager_name (str):
            Output only. The name of the Instance Group
            Manager for this group.
        instance_group_manager_uri (str):
            Output only. The partial URI to the instance
            group manager for this group. E.g.
            projects/my-project/regions/us-central1/instanceGroupManagers/my-igm.
    """

    instance_template_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    instance_group_manager_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    instance_group_manager_uri: str = proto.Field(
        proto.STRING,
        number=3,
    )


class InstanceFlexibilityPolicy(proto.Message):
    r"""Instance flexibility Policy allowing a mixture of VM shapes
    and provisioning models.

    Attributes:
        provisioning_model_mix (google.cloud.dataproc_v1.types.InstanceFlexibilityPolicy.ProvisioningModelMix):
            Optional. Defines how the Group selects the
            provisioning model to ensure required
            reliability.
        instance_selection_list (MutableSequence[google.cloud.dataproc_v1.types.InstanceFlexibilityPolicy.InstanceSelection]):
            Optional. List of instance selection options
            that the group will use when creating new VMs.
        instance_selection_results (MutableSequence[google.cloud.dataproc_v1.types.InstanceFlexibilityPolicy.InstanceSelectionResult]):
            Output only. A list of instance selection
            results in the group.
    """

    class ProvisioningModelMix(proto.Message):
        r"""Defines how Dataproc should create VMs with a mixture of
        provisioning models.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            standard_capacity_base (int):
                Optional. The base capacity that will always use Standard
                VMs to avoid risk of more preemption than the minimum
                capacity you need. Dataproc will create only standard VMs
                until it reaches standard_capacity_base, then it will start
                using standard_capacity_percent_above_base to mix Spot with
                Standard VMs. eg. If 15 instances are requested and
                standard_capacity_base is 5, Dataproc will create 5 standard
                VMs and then start mixing spot and standard VMs for
                remaining 10 instances.

                This field is a member of `oneof`_ ``_standard_capacity_base``.
            standard_capacity_percent_above_base (int):
                Optional. The percentage of target capacity that should use
                Standard VM. The remaining percentage will use Spot VMs. The
                percentage applies only to the capacity above
                standard_capacity_base. eg. If 15 instances are requested
                and standard_capacity_base is 5 and
                standard_capacity_percent_above_base is 30, Dataproc will
                create 5 standard VMs and then start mixing spot and
                standard VMs for remaining 10 instances. The mix will be 30%
                standard and 70% spot.

                This field is a member of `oneof`_ ``_standard_capacity_percent_above_base``.
        """

        standard_capacity_base: int = proto.Field(
            proto.INT32,
            number=1,
            optional=True,
        )
        standard_capacity_percent_above_base: int = proto.Field(
            proto.INT32,
            number=2,
            optional=True,
        )

    class InstanceSelection(proto.Message):
        r"""Defines machines types and a rank to which the machines types
        belong.

        Attributes:
            machine_types (MutableSequence[str]):
                Optional. Full machine-type names, e.g.
                "n1-standard-16".
            rank (int):
                Optional. Preference of this instance
                selection. Lower number means higher preference.
                Dataproc will first try to create a VM based on
                the machine-type with priority rank and fallback
                to next rank based on availability. Machine
                types and instance selections with the same
                priority have the same preference.
            disk_config (google.cloud.dataproc_v1.types.DiskConfig):
                Optional. Disk configuration to apply to the
                instances in this instance selection. If
                specified on any entry in instanceSelectionList,
                then it must be specified on every entry in
                instanceSelectionList and the
                instanceGroupConfig must not specify any
                diskConfig.
        """

        machine_types: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )
        rank: int = proto.Field(
            proto.INT32,
            number=2,
        )
        disk_config: "DiskConfig" = proto.Field(
            proto.MESSAGE,
            number=3,
            message="DiskConfig",
        )

    class InstanceSelectionResult(proto.Message):
        r"""Defines a mapping from machine types to the number of VMs
        that are created with each machine type.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            machine_type (str):
                Output only. Full machine-type names, e.g.
                "n1-standard-16".

                This field is a member of `oneof`_ ``_machine_type``.
            vm_count (int):
                Output only. Number of VM provisioned with the machine_type.

                This field is a member of `oneof`_ ``_vm_count``.
        """

        machine_type: str = proto.Field(
            proto.STRING,
            number=1,
            optional=True,
        )
        vm_count: int = proto.Field(
            proto.INT32,
            number=2,
            optional=True,
        )

    provisioning_model_mix: ProvisioningModelMix = proto.Field(
        proto.MESSAGE,
        number=1,
        message=ProvisioningModelMix,
    )
    instance_selection_list: MutableSequence[InstanceSelection] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=InstanceSelection,
    )
    instance_selection_results: MutableSequence[InstanceSelectionResult] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=3,
            message=InstanceSelectionResult,
        )
    )


class FlexibleInstanceGroupConfig(proto.Message):
    r"""The configuration for High Obtainability (HO) flexible
    instance groups. Flexible instance group configs serve as the
    single source of truth for desired state.

    Attributes:
        num_instances (int):
            Optional. The number of VM instances
            requested.
            For master instances, this must be 1. For worker
            and secondary worker instances, this represents
            the desired capacity of the group and is mutable
            via cluster update operations and autoscaling.
        core_count (int):
            Optional. The number of vCPUs per instance.
            Must be a power of 2 (2, 4, 8, 16, 32). This is
            a create-time specification and is not currently
            mutable via update masks.
        boot_disk_size_gb (int):
            Optional. The boot disk size in GB. This is a
            create-time specification and is not currently
            mutable via update masks.
        hardware_class (google.cloud.dataproc_v1.types.FlexibleInstanceGroupConfig.HardwareClass):
            Optional. The hardware class of the
            instances. This is a create-time specification
            and is not currently mutable via update masks.
    """

    class HardwareClass(proto.Enum):
        r"""Controls the hardware class for the flexible instance group.

        Values:
            HARDWARE_CLASS_UNSPECIFIED (0):
                Unspecified hardware class.
            STANDARD (1):
                Standard hardware class. Provides a balanced compute
                configuration with approximately 4GB of memory per vCPU and
                standard disk storage tiers.

                Candidate machine types include ``n4-standard``,
                ``n4d-standard``, ``n2-standard``, and ``n2d-standard``
                (Rank 0), and ``c4-standard`` and ``c4d-standard`` (Rank 1)
                (for requested core counts 2, 4, 8, 16, 32).

                Warning: The specific machine families and types selected
                for this hardware class are subject to change. Users should
                not take a dependency on the underlying machine type
                selection.
            PERFORMANCE (2):
                Performance hardware class. Provides a high-performance
                configuration with approximately 8GB of memory per vCPU
                (e.g. high-memory machine types) and higher-tier disk
                configurations (e.g. higher IOPS and throughput).

                Candidate machine types include ``n4-highmem``,
                ``n4d-highmem``, ``n2-highmem``, and ``n2d-highmem`` (Rank
                0), and ``c4-highmem`` and ``c4d-highmem`` (Rank 1) (for
                requested core counts 2, 4, 8, 16, 32). ``n4``, ``n4d``,
                ``c4``, and ``c4d`` use Hyperdisk Balanced with provisioned
                storage, whereas ``n2`` and ``n2d`` use SSD persistent
                disks.

                Warning: The specific machine families and types selected
                for this hardware class are subject to change. Users should
                not take a dependency on the underlying machine type
                selection.
        """

        HARDWARE_CLASS_UNSPECIFIED = 0
        STANDARD = 1
        PERFORMANCE = 2

    num_instances: int = proto.Field(
        proto.INT32,
        number=1,
    )
    core_count: int = proto.Field(
        proto.INT32,
        number=2,
    )
    boot_disk_size_gb: int = proto.Field(
        proto.INT32,
        number=3,
    )
    hardware_class: HardwareClass = proto.Field(
        proto.ENUM,
        number=4,
        enum=HardwareClass,
    )


class AcceleratorConfig(proto.Message):
    r"""Specifies the type and number of accelerator cards attached to the
    instances of an instance. See `GPUs on Compute
    Engine <https://cloud.google.com/compute/docs/gpus/>`__.

    Attributes:
        accelerator_type_uri (str):
            Full URL, partial URI, or short name of the accelerator type
            resource to expose to this instance. See `Compute Engine
            AcceleratorTypes <https://cloud.google.com/compute/docs/reference/v1/acceleratorTypes>`__.

            Examples:

            - ``https://www.googleapis.com/compute/v1/projects/[project_id]/zones/[zone]/acceleratorTypes/nvidia-tesla-t4``
            - ``projects/[project_id]/zones/[zone]/acceleratorTypes/nvidia-tesla-t4``
            - ``nvidia-tesla-t4``

            **Auto Zone Exception**: If you are using the Dataproc `Auto
            Zone
            Placement <https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/auto-zone#using_auto_zone_placement>`__
            feature, you must use the short name of the accelerator type
            resource, for example, ``nvidia-tesla-t4``.
        accelerator_count (int):
            The number of the accelerator cards of this
            type exposed to this instance.
    """

    accelerator_type_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    accelerator_count: int = proto.Field(
        proto.INT32,
        number=2,
    )


class DiskConfig(proto.Message):
    r"""Specifies the config of boot disk and attached disk options
    for a group of VM instances.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        boot_disk_type (str):
            Optional. Type of the boot disk (default is
            ``pd-standard``). Valid values: ``pd-balanced`` (Persistent
            Disk Balanced Solid State Drive), ``pd-ssd`` (Persistent
            Disk Solid State Drive), or ``pd-standard`` (Persistent Disk
            Hard Disk Drive). See `Disk
            types <https://cloud.google.com/compute/docs/disks#disk-types>`__.
        boot_disk_size_gb (int):
            Optional. Size in GB of the boot disk
            (default is 500GB).
        num_local_ssds (int):
            Optional. Number of attached SSDs, from 0 to 8 (default is
            0). If SSDs are not attached, the boot disk is used to store
            runtime logs and
            `HDFS <https://hadoop.apache.org/docs/r1.2.1/hdfs_user_guide.html>`__
            data. If one or more SSDs are attached, this runtime bulk
            data is spread across them, and the boot disk contains only
            basic config and installed binaries.

            Note: Local SSD options may vary by machine type and number
            of vCPUs selected.
        local_ssd_interface (str):
            Optional. Interface type of local SSDs (default is
            ``scsi``). Valid values: ``scsi`` (Small Computer System
            Interface), ``nvme`` (Non-Volatile Memory Express). See
            `local SSD
            performance <https://cloud.google.com/compute/docs/disks/local-ssd#performance>`__.
        boot_disk_provisioned_iops (int):
            Optional. Indicates how many IOPS to provision for the disk.
            This sets the number of I/O operations per second that the
            disk can handle. **This field is supported only if
            [boot_disk_type][google.cloud.dataproc.v1.DiskConfig.boot_disk_type]
            is ``hyperdisk-balanced``.**

            This field is a member of `oneof`_ ``_boot_disk_provisioned_iops``.
        boot_disk_provisioned_throughput (int):
            Optional. Indicates how much throughput to provision for the
            disk. This sets the number of throughput mb per second that
            the disk can handle. Values must be greater than or equal to
            1. **This field is supported only if
            [boot_disk_type][google.cloud.dataproc.v1.DiskConfig.boot_disk_type]
            is ``hyperdisk-balanced``.**

            This field is a member of `oneof`_ ``_boot_disk_provisioned_throughput``.
        attached_disk_configs (MutableSequence[google.cloud.dataproc_v1.types.AttachedDiskConfig]):
            Optional. A list of attached disk configs for
            a group of VM instances.
    """

    boot_disk_type: str = proto.Field(
        proto.STRING,
        number=3,
    )
    boot_disk_size_gb: int = proto.Field(
        proto.INT32,
        number=1,
    )
    num_local_ssds: int = proto.Field(
        proto.INT32,
        number=2,
    )
    local_ssd_interface: str = proto.Field(
        proto.STRING,
        number=4,
    )
    boot_disk_provisioned_iops: int = proto.Field(
        proto.INT64,
        number=5,
        optional=True,
    )
    boot_disk_provisioned_throughput: int = proto.Field(
        proto.INT64,
        number=6,
        optional=True,
    )
    attached_disk_configs: MutableSequence["AttachedDiskConfig"] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message="AttachedDiskConfig",
    )


class AttachedDiskConfig(proto.Message):
    r"""Specifies the config of attached disk options for single VM
    instance.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        disk_type (google.cloud.dataproc_v1.types.AttachedDiskConfig.DiskType):
            Optional. Disk type.
        disk_size_gb (int):
            Optional. Disk size in GB.
        provisioned_iops (int):
            Optional. Indicates how many IOPS to
            provision for the attached disk. This sets the
            number of I/O operations per second that the
            disk can handle. See
            https://cloud.google.com/compute/docs/disks/hyperdisks#hyperdisk-features

            This field is a member of `oneof`_ ``_provisioned_iops``.
        provisioned_throughput (int):
            Optional. Indicates how much throughput to
            provision for the attached disk. This sets the
            number of throughput mb per second that the disk
            can handle. See
            https://cloud.google.com/compute/docs/disks/hyperdisks#hyperdisk-features

            This field is a member of `oneof`_ ``_provisioned_throughput``.
    """

    class DiskType(proto.Enum):
        r"""

        Values:
            DISK_TYPE_UNSPECIFIED (0):
                Required unspecified disk type.
            HYPERDISK_BALANCED (1):
                Hyperdisk Balanced disk type.
            HYPERDISK_EXTREME (2):
                Hyperdisk Extreme disk type.
            HYPERDISK_ML (3):
                Hyperdisk ML disk type.
            HYPERDISK_THROUGHPUT (4):
                Hyperdisk Throughput disk type.
        """

        DISK_TYPE_UNSPECIFIED = 0
        HYPERDISK_BALANCED = 1
        HYPERDISK_EXTREME = 2
        HYPERDISK_ML = 3
        HYPERDISK_THROUGHPUT = 4

    disk_type: DiskType = proto.Field(
        proto.ENUM,
        number=1,
        enum=DiskType,
    )
    disk_size_gb: int = proto.Field(
        proto.INT32,
        number=2,
    )
    provisioned_iops: int = proto.Field(
        proto.INT64,
        number=3,
        optional=True,
    )
    provisioned_throughput: int = proto.Field(
        proto.INT64,
        number=4,
        optional=True,
    )


class AuxiliaryNodeGroup(proto.Message):
    r"""Node group identification and configuration information.

    Attributes:
        node_group (google.cloud.dataproc_v1.types.NodeGroup):
            Required. Node group configuration.
        node_group_id (str):
            Optional. A node group ID. Generated if not specified.

            The ID must contain only letters (a-z, A-Z), numbers (0-9),
            underscores (\_), and hyphens (-). Cannot begin or end with
            underscore or hyphen. Must consist of from 3 to 33
            characters.
    """

    node_group: "NodeGroup" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="NodeGroup",
    )
    node_group_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class NodeGroup(proto.Message):
    r"""Dataproc Node Group. **The Dataproc ``NodeGroup`` resource is not
    related to the Dataproc
    [NodeGroupAffinity][google.cloud.dataproc.v1.NodeGroupAffinity]
    resource.**

    Attributes:
        name (str):
            The Node group `resource name <https://aip.dev/122>`__.
        roles (MutableSequence[google.cloud.dataproc_v1.types.NodeGroup.Role]):
            Required. Node group roles.
        node_group_config (google.cloud.dataproc_v1.types.InstanceGroupConfig):
            Optional. The node group instance group
            configuration.
        labels (MutableMapping[str, str]):
            Optional. Node group labels.

            - Label **keys** must consist of from 1 to 63 characters and
              conform to `RFC
              1035 <https://www.ietf.org/rfc/rfc1035.txt>`__.
            - Label **values** can be empty. If specified, they must
              consist of from 1 to 63 characters and conform to [RFC
              1035] (https://www.ietf.org/rfc/rfc1035.txt).
            - The node group must have no more than 32 labels.
    """

    class Role(proto.Enum):
        r"""Node pool roles.

        Values:
            ROLE_UNSPECIFIED (0):
                Required unspecified role.
            DRIVER (1):
                Job drivers run on the node pool.
        """

        ROLE_UNSPECIFIED = 0
        DRIVER = 1

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    roles: MutableSequence[Role] = proto.RepeatedField(
        proto.ENUM,
        number=2,
        enum=Role,
    )
    node_group_config: "InstanceGroupConfig" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="InstanceGroupConfig",
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )


class NodeInitializationAction(proto.Message):
    r"""Specifies an executable to run on a fully configured node and
    a timeout period for executable completion.

    Attributes:
        executable_file (str):
            Required. Cloud Storage URI of executable
            file.
        execution_timeout (google.protobuf.duration_pb2.Duration):
            Optional. Amount of time executable has to complete. Default
            is 10 minutes (see JSON representation of
            `Duration <https://developers.google.com/protocol-buffers/docs/proto3#json>`__).

            Cluster creation fails with an explanatory error message
            (the name of the executable that caused the error and the
            exceeded timeout period) if the executable is not completed
            at end of the timeout period.
    """

    executable_file: str = proto.Field(
        proto.STRING,
        number=1,
    )
    execution_timeout: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=2,
        message=duration_pb2.Duration,
    )


class ClusterStatus(proto.Message):
    r"""The status of a cluster and its instances.

    Attributes:
        state (google.cloud.dataproc_v1.types.ClusterStatus.State):
            Output only. The cluster's state.
        detail (str):
            Optional. Output only. Details of cluster's
            state.
        state_start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when this state was entered (see JSON
            representation of
            `Timestamp <https://developers.google.com/protocol-buffers/docs/proto3#json>`__).
        substate (google.cloud.dataproc_v1.types.ClusterStatus.Substate):
            Output only. Additional state information
            that includes status reported by the agent.
    """

    class State(proto.Enum):
        r"""The cluster state.

        Values:
            UNKNOWN (0):
                The cluster state is unknown.
            CREATING (1):
                The cluster is being created and set up. It
                is not ready for use.
            RUNNING (2):
                The cluster is currently running and healthy. It is ready
                for use.

                **Note:** The cluster state changes from "creating" to
                "running" status after the master node(s), first two primary
                worker nodes (and the last primary worker node if primary
                workers > 2) are running.
            ERROR (3):
                The cluster encountered an error. It is not
                ready for use.
            ERROR_DUE_TO_UPDATE (9):
                The cluster has encountered an error while
                being updated. Jobs can be submitted to the
                cluster, but the cluster cannot be updated.
            DELETING (4):
                The cluster is being deleted. It cannot be
                used.
            UPDATING (5):
                The cluster is being updated. It continues to
                accept and process jobs.
            STOPPING (6):
                The cluster is being stopped. It cannot be
                used.
            STOPPED (7):
                The cluster is currently stopped. It is not
                ready for use.
            STARTING (8):
                The cluster is being started. It is not ready
                for use.
            REPAIRING (10):
                The cluster is being repaired. It is not
                ready for use.
        """

        UNKNOWN = 0
        CREATING = 1
        RUNNING = 2
        ERROR = 3
        ERROR_DUE_TO_UPDATE = 9
        DELETING = 4
        UPDATING = 5
        STOPPING = 6
        STOPPED = 7
        STARTING = 8
        REPAIRING = 10

    class Substate(proto.Enum):
        r"""The cluster substate.

        Values:
            UNSPECIFIED (0):
                The cluster substate is unknown.
            UNHEALTHY (1):
                The cluster is known to be in an unhealthy
                state (for example, critical daemons are not
                running or HDFS capacity is exhausted).

                Applies to RUNNING state.
            STALE_STATUS (2):
                The agent-reported status is out of date (may
                occur if Dataproc loses communication with
                Agent).

                Applies to RUNNING state.
        """

        UNSPECIFIED = 0
        UNHEALTHY = 1
        STALE_STATUS = 2

    state: State = proto.Field(
        proto.ENUM,
        number=1,
        enum=State,
    )
    detail: str = proto.Field(
        proto.STRING,
        number=2,
    )
    state_start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    substate: Substate = proto.Field(
        proto.ENUM,
        number=4,
        enum=Substate,
    )


class SecurityConfig(proto.Message):
    r"""Security related configuration, including encryption,
    Kerberos, etc.

    Attributes:
        kerberos_config (google.cloud.dataproc_v1.types.KerberosConfig):
            Optional. Kerberos related configuration.
        identity_config (google.cloud.dataproc_v1.types.IdentityConfig):
            Optional. Identity related configuration,
            including service account based secure
            multi-tenancy user mappings.
    """

    kerberos_config: "KerberosConfig" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="KerberosConfig",
    )
    identity_config: "IdentityConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="IdentityConfig",
    )


class KerberosConfig(proto.Message):
    r"""Specifies Kerberos related configuration.

    Attributes:
        enable_kerberos (bool):
            Optional. Flag to indicate whether to
            Kerberize the cluster (default: false). Set this
            field to true to enable Kerberos on a cluster.
        root_principal_password_uri (str):
            Optional. The Cloud Storage URI of a KMS
            encrypted file containing the root principal
            password.
        kms_key_uri (str):
            Optional. The URI of the KMS key used to
            encrypt sensitive files.
        keystore_uri (str):
            Optional. The Cloud Storage URI of the
            keystore file used for SSL encryption. If not
            provided, Dataproc will provide a self-signed
            certificate.
        truststore_uri (str):
            Optional. The Cloud Storage URI of the
            truststore file used for SSL encryption. If not
            provided, Dataproc will provide a self-signed
            certificate.
        keystore_password_uri (str):
            Optional. The Cloud Storage URI of a KMS
            encrypted file containing the password to the
            user provided keystore. For the self-signed
            certificate, this password is generated by
            Dataproc.
        key_password_uri (str):
            Optional. The Cloud Storage URI of a KMS
            encrypted file containing the password to the
            user provided key. For the self-signed
            certificate, this password is generated by
            Dataproc.
        truststore_password_uri (str):
            Optional. The Cloud Storage URI of a KMS
            encrypted file containing the password to the
            user provided truststore. For the self-signed
            certificate, this password is generated by
            Dataproc.
        cross_realm_trust_realm (str):
            Optional. The remote realm the Dataproc
            on-cluster KDC will trust, should the user
            enable cross realm trust.
        cross_realm_trust_kdc (str):
            Optional. The KDC (IP or hostname) for the
            remote trusted realm in a cross realm trust
            relationship.
        cross_realm_trust_admin_server (str):
            Optional. The admin server (IP or hostname)
            for the remote trusted realm in a cross realm
            trust relationship.
        cross_realm_trust_shared_password_uri (str):
            Optional. The Cloud Storage URI of a KMS
            encrypted file containing the shared password
            between the on-cluster Kerberos realm and the
            remote trusted realm, in a cross realm trust
            relationship.
        kdc_db_key_uri (str):
            Optional. The Cloud Storage URI of a KMS
            encrypted file containing the master key of the
            KDC database.
        tgt_lifetime_hours (int):
            Optional. The lifetime of the ticket granting
            ticket, in hours. If not specified, or user
            specifies 0, then default value 10 will be used.
        realm (str):
            Optional. The name of the on-cluster Kerberos
            realm. If not specified, the uppercased domain
            of hostnames will be the realm.
    """

    enable_kerberos: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    root_principal_password_uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    kms_key_uri: str = proto.Field(
        proto.STRING,
        number=3,
    )
    keystore_uri: str = proto.Field(
        proto.STRING,
        number=4,
    )
    truststore_uri: str = proto.Field(
        proto.STRING,
        number=5,
    )
    keystore_password_uri: str = proto.Field(
        proto.STRING,
        number=6,
    )
    key_password_uri: str = proto.Field(
        proto.STRING,
        number=7,
    )
    truststore_password_uri: str = proto.Field(
        proto.STRING,
        number=8,
    )
    cross_realm_trust_realm: str = proto.Field(
        proto.STRING,
        number=9,
    )
    cross_realm_trust_kdc: str = proto.Field(
        proto.STRING,
        number=10,
    )
    cross_realm_trust_admin_server: str = proto.Field(
        proto.STRING,
        number=11,
    )
    cross_realm_trust_shared_password_uri: str = proto.Field(
        proto.STRING,
        number=12,
    )
    kdc_db_key_uri: str = proto.Field(
        proto.STRING,
        number=13,
    )
    tgt_lifetime_hours: int = proto.Field(
        proto.INT32,
        number=14,
    )
    realm: str = proto.Field(
        proto.STRING,
        number=15,
    )


class IdentityConfig(proto.Message):
    r"""Identity related configuration, including service account
    based secure multi-tenancy user mappings.

    Attributes:
        user_service_account_mapping (MutableMapping[str, str]):
            Required. Map of user to service account.
    """

    user_service_account_mapping: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=1,
    )


class SoftwareConfig(proto.Message):
    r"""Specifies the selection and config of software inside the
    cluster.

    Attributes:
        image_version (str):
            Optional. The version of software inside the cluster. It
            must be one of the supported `Dataproc
            Versions <https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions#supported-dataproc-image-versions>`__,
            such as "1.2" (including a subminor version, such as
            "1.2.29"), or the `"preview"
            version <https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions#other_versions>`__.
            If unspecified, it defaults to the latest Debian version.
        properties (MutableMapping[str, str]):
            Optional. The properties to set on daemon config files.

            Property keys are specified in ``prefix:property`` format,
            for example ``core:hadoop.tmp.dir``. The following are
            supported prefixes and their mappings:

            - capacity-scheduler: ``capacity-scheduler.xml``
            - core: ``core-site.xml``
            - distcp: ``distcp-default.xml``
            - hdfs: ``hdfs-site.xml``
            - hive: ``hive-site.xml``
            - mapred: ``mapred-site.xml``
            - pig: ``pig.properties``
            - spark: ``spark-defaults.conf``
            - yarn: ``yarn-site.xml``

            For more information, see `Cluster
            properties <https://cloud.google.com/dataproc/docs/concepts/cluster-properties>`__.
        optional_components (MutableSequence[google.cloud.dataproc_v1.types.Component]):
            Optional. The set of components to activate
            on the cluster.
    """

    image_version: str = proto.Field(
        proto.STRING,
        number=1,
    )
    properties: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=2,
    )
    optional_components: MutableSequence[shared.Component] = proto.RepeatedField(
        proto.ENUM,
        number=3,
        enum=shared.Component,
    )


class LifecycleConfig(proto.Message):
    r"""Specifies the cluster auto-delete schedule configuration.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        idle_delete_ttl (google.protobuf.duration_pb2.Duration):
            Optional. The duration to keep the cluster alive while
            idling (when no jobs are running). Passing this threshold
            will cause the cluster to be deleted. Minimum value is 5
            minutes; maximum value is 14 days (see JSON representation
            of
            `Duration <https://developers.google.com/protocol-buffers/docs/proto3#json>`__).
        auto_delete_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. The time when cluster will be auto-deleted (see
            JSON representation of
            `Timestamp <https://developers.google.com/protocol-buffers/docs/proto3#json>`__).

            This field is a member of `oneof`_ ``ttl``.
        auto_delete_ttl (google.protobuf.duration_pb2.Duration):
            Optional. The lifetime duration of cluster. The cluster will
            be auto-deleted at the end of this period. Minimum value is
            10 minutes; maximum value is 14 days (see JSON
            representation of
            `Duration <https://developers.google.com/protocol-buffers/docs/proto3#json>`__).

            This field is a member of `oneof`_ ``ttl``.
        idle_stop_ttl (google.protobuf.duration_pb2.Duration):
            Optional. The duration to keep the cluster started while
            idling (when no jobs are running). Passing this threshold
            will cause the cluster to be stopped. Minimum value is 5
            minutes; maximum value is 14 days (see JSON representation
            of
            `Duration <https://developers.google.com/protocol-buffers/docs/proto3#json>`__).
        auto_stop_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. The time when cluster will be auto-stopped (see
            JSON representation of
            `Timestamp <https://developers.google.com/protocol-buffers/docs/proto3#json>`__).

            This field is a member of `oneof`_ ``stop_ttl``.
        auto_stop_ttl (google.protobuf.duration_pb2.Duration):
            Optional. The lifetime duration of the cluster. The cluster
            will be auto-stopped at the end of this period, calculated
            from the time of submission of the create or update cluster
            request. Minimum value is 10 minutes; maximum value is 14
            days (see JSON representation of
            `Duration <https://developers.google.com/protocol-buffers/docs/proto3#json>`__).

            This field is a member of `oneof`_ ``stop_ttl``.
        idle_start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when cluster became idle (most recent
            job finished) and became eligible for deletion due to
            idleness (see JSON representation of
            `Timestamp <https://developers.google.com/protocol-buffers/docs/proto3#json>`__).
    """

    idle_delete_ttl: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=1,
        message=duration_pb2.Duration,
    )
    auto_delete_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="ttl",
        message=timestamp_pb2.Timestamp,
    )
    auto_delete_ttl: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="ttl",
        message=duration_pb2.Duration,
    )
    idle_stop_ttl: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=5,
        message=duration_pb2.Duration,
    )
    auto_stop_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="stop_ttl",
        message=timestamp_pb2.Timestamp,
    )
    auto_stop_ttl: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="stop_ttl",
        message=duration_pb2.Duration,
    )
    idle_start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )


class MetastoreConfig(proto.Message):
    r"""Specifies a Metastore configuration.

    Attributes:
        dataproc_metastore_service (str):
            Required. Resource name of an existing Dataproc Metastore
            service.

            Example:

            - ``projects/[project_id]/locations/[dataproc_region]/services/[service-name]``
    """

    dataproc_metastore_service: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ClusterMetrics(proto.Message):
    r"""Contains cluster daemon metrics, such as HDFS and YARN stats.

    **Beta Feature**: This report is available for testing purposes
    only. It may be changed before final release.

    Attributes:
        hdfs_metrics (MutableMapping[str, int]):
            The HDFS metrics.
        yarn_metrics (MutableMapping[str, int]):
            YARN metrics.
    """

    hdfs_metrics: MutableMapping[str, int] = proto.MapField(
        proto.STRING,
        proto.INT64,
        number=1,
    )
    yarn_metrics: MutableMapping[str, int] = proto.MapField(
        proto.STRING,
        proto.INT64,
        number=2,
    )


class DataprocMetricConfig(proto.Message):
    r"""Dataproc metric config.

    Attributes:
        metrics (MutableSequence[google.cloud.dataproc_v1.types.DataprocMetricConfig.Metric]):
            Required. Metrics sources to enable.
    """

    class MetricSource(proto.Enum):
        r"""A source for the collection of Dataproc custom metrics (see [Custom
        metrics]
        (https://cloud.google.com//dataproc/docs/guides/dataproc-metrics#custom_metrics)).

        Values:
            METRIC_SOURCE_UNSPECIFIED (0):
                Required unspecified metric source.
            MONITORING_AGENT_DEFAULTS (1):
                Monitoring agent metrics. If this source is enabled,
                Dataproc enables the monitoring agent in Compute Engine, and
                collects monitoring agent metrics, which are published with
                an ``agent.googleapis.com`` prefix.
            HDFS (2):
                HDFS metric source.
            SPARK (3):
                Spark metric source.
            YARN (4):
                YARN metric source.
            SPARK_HISTORY_SERVER (5):
                Spark History Server metric source.
            HIVESERVER2 (6):
                Hiveserver2 metric source.
            HIVEMETASTORE (7):
                hivemetastore metric source
            FLINK (8):
                flink metric source
        """

        METRIC_SOURCE_UNSPECIFIED = 0
        MONITORING_AGENT_DEFAULTS = 1
        HDFS = 2
        SPARK = 3
        YARN = 4
        SPARK_HISTORY_SERVER = 5
        HIVESERVER2 = 6
        HIVEMETASTORE = 7
        FLINK = 8

    class Metric(proto.Message):
        r"""A Dataproc custom metric.

        Attributes:
            metric_source (google.cloud.dataproc_v1.types.DataprocMetricConfig.MetricSource):
                Required. A standard set of metrics is collected unless
                ``metricOverrides`` are specified for the metric source (see
                [Custom metrics]
                (https://cloud.google.com/dataproc/docs/guides/dataproc-metrics#custom_metrics)
                for more information).
            metric_overrides (MutableSequence[str]):
                Optional. Specify one or more [Custom metrics]
                (https://cloud.google.com/dataproc/docs/guides/dataproc-metrics#custom_metrics)
                to collect for the metric course (for the ``SPARK`` metric
                source (any [Spark metric]
                (https://spark.apache.org/docs/latest/monitoring.html#metrics)
                can be specified).

                Provide metrics in the following format:
                METRIC_SOURCE:INSTANCE:GROUP:METRIC Use camelcase as
                appropriate.

                Examples:

                ::

                   yarn:ResourceManager:QueueMetrics:AppsCompleted
                   spark:driver:DAGScheduler:job.allJobs
                   sparkHistoryServer:JVM:Memory:NonHeapMemoryUsage.committed
                   hiveserver2:JVM:Memory:NonHeapMemoryUsage.used

                Notes:

                - Only the specified overridden metrics are collected for
                  the metric source. For example, if one or more
                  ``spark:executive`` metrics are listed as metric
                  overrides, other ``SPARK`` metrics are not collected. The
                  collection of the metrics for other enabled custom metric
                  sources is unaffected. For example, if both ``SPARK`` andd
                  ``YARN`` metric sources are enabled, and overrides are
                  provided for Spark metrics only, all YARN metrics are
                  collected.
        """

        metric_source: "DataprocMetricConfig.MetricSource" = proto.Field(
            proto.ENUM,
            number=1,
            enum="DataprocMetricConfig.MetricSource",
        )
        metric_overrides: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=2,
        )

    metrics: MutableSequence[Metric] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=Metric,
    )


class CreateClusterRequest(proto.Message):
    r"""A request to create a cluster.

    Attributes:
        project_id (str):
            Required. The ID of the Google Cloud Platform
            project that the cluster belongs to.
        region (str):
            Required. The Dataproc region in which to
            handle the request.
        cluster (google.cloud.dataproc_v1.types.Cluster):
            Required. The cluster to create.
        request_id (str):
            Optional. A unique ID used to identify the request. If the
            server receives two
            `CreateClusterRequest <https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#google.cloud.dataproc.v1.CreateClusterRequest>`__\ s
            with the same id, then the second request will be ignored
            and the first
            [google.longrunning.Operation][google.longrunning.Operation]
            created and stored in the backend is returned.

            It is recommended to always set this value to a
            `UUID <https://en.wikipedia.org/wiki/Universally_unique_identifier>`__.

            The ID must contain only letters (a-z, A-Z), numbers (0-9),
            underscores (\_), and hyphens (-). The maximum length is 40
            characters.
        action_on_failed_primary_workers (google.cloud.dataproc_v1.types.FailureAction):
            Optional. Failure action when primary worker
            creation fails.
    """

    project_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    region: str = proto.Field(
        proto.STRING,
        number=3,
    )
    cluster: "Cluster" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Cluster",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    action_on_failed_primary_workers: shared.FailureAction = proto.Field(
        proto.ENUM,
        number=5,
        enum=shared.FailureAction,
    )


class UpdateClusterRequest(proto.Message):
    r"""A request to update a cluster.

    Attributes:
        project_id (str):
            Required. The ID of the Google Cloud Platform
            project the cluster belongs to.
        region (str):
            Required. The Dataproc region in which to
            handle the request.
        cluster_name (str):
            Required. The cluster name.
        cluster (google.cloud.dataproc_v1.types.Cluster):
            Required. The changes to the cluster.
        graceful_decommission_timeout (google.protobuf.duration_pb2.Duration):
            Optional. Timeout for graceful YARN decommissioning.
            Graceful decommissioning allows removing nodes from the
            cluster without interrupting jobs in progress. Timeout
            specifies how long to wait for jobs in progress to finish
            before forcefully removing nodes (and potentially
            interrupting jobs). Default timeout is 0 (for forceful
            decommission), and the maximum allowed timeout is 1 day.
            (see JSON representation of
            `Duration <https://developers.google.com/protocol-buffers/docs/proto3#json>`__).

            Only supported on Dataproc image versions 1.2 and higher.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Specifies the path, relative to ``Cluster``, of
            the field to update. For example, to change the number of
            workers in a cluster to 5, the ``update_mask`` parameter
            would be specified as
            ``config.worker_config.num_instances``, and the ``PATCH``
            request body would specify the new value, as follows:

            ::

                {
                  "config":{
                    "workerConfig":{
                      "numInstances":"5"
                    }
                  }
                }

            Similarly, to change the number of preemptible workers in a
            cluster to 5, the ``update_mask`` parameter would be
            ``config.secondary_worker_config.num_instances``, and the
            ``PATCH`` request body would be set as follows:

            ::

                {
                  "config":{
                    "secondaryWorkerConfig":{
                      "numInstances":"5"
                    }
                  }
                }

            Note: Currently, only the following fields can be updated:

            .. raw:: html

                 <table>
                 <tbody>
                 <tr>
                 <td><strong>Mask</strong></td>
                 <td><strong>Purpose</strong></td>
                 </tr>
                 <tr>
                 <td><strong><em>labels</em></strong></td>
                 <td>Update labels</td>
                 </tr>
                 <tr>
                 <td><strong><em>config.worker_config.num_instances</em></strong></td>
                 <td>Resize primary worker group</td>
                 </tr>
                 <tr>
                 <td><strong><em>config.secondary_worker_config.num_instances</em></strong></td>
                 <td>Resize secondary worker group</td>
                 </tr>
                 <tr>
                 <td>config.autoscaling_config.policy_uri</td><td>Use, stop using, or
                 change autoscaling policies</td>
                 </tr>
                 </tbody>
                 </table>
        request_id (str):
            Optional. A unique ID used to identify the request. If the
            server receives two
            `UpdateClusterRequest <https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#google.cloud.dataproc.v1.UpdateClusterRequest>`__\ s
            with the same id, then the second request will be ignored
            and the first
            [google.longrunning.Operation][google.longrunning.Operation]
            created and stored in the backend is returned.

            It is recommended to always set this value to a
            `UUID <https://en.wikipedia.org/wiki/Universally_unique_identifier>`__.

            The ID must contain only letters (a-z, A-Z), numbers (0-9),
            underscores (\_), and hyphens (-). The maximum length is 40
            characters.
    """

    project_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    region: str = proto.Field(
        proto.STRING,
        number=5,
    )
    cluster_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    cluster: "Cluster" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Cluster",
    )
    graceful_decommission_timeout: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=6,
        message=duration_pb2.Duration,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=4,
        message=field_mask_pb2.FieldMask,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=7,
    )


class StopClusterRequest(proto.Message):
    r"""A request to stop a cluster.

    Attributes:
        project_id (str):
            Required. The ID of the Google Cloud Platform
            project the cluster belongs to.
        region (str):
            Required. The Dataproc region in which to
            handle the request.
        cluster_name (str):
            Required. The cluster name.
        cluster_uuid (str):
            Optional. Specifying the ``cluster_uuid`` means the RPC will
            fail (with error NOT_FOUND) if a cluster with the specified
            UUID does not exist.
        request_id (str):
            Optional. A unique ID used to identify the request. If the
            server receives two
            `StopClusterRequest <https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#google.cloud.dataproc.v1.StopClusterRequest>`__\ s
            with the same id, then the second request will be ignored
            and the first
            [google.longrunning.Operation][google.longrunning.Operation]
            created and stored in the backend is returned.

            Recommendation: Set this value to a
            `UUID <https://en.wikipedia.org/wiki/Universally_unique_identifier>`__.

            The ID must contain only letters (a-z, A-Z), numbers (0-9),
            underscores (\_), and hyphens (-). The maximum length is 40
            characters.
    """

    project_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    region: str = proto.Field(
        proto.STRING,
        number=2,
    )
    cluster_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    cluster_uuid: str = proto.Field(
        proto.STRING,
        number=4,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=5,
    )


class StartClusterRequest(proto.Message):
    r"""A request to start a cluster.

    Attributes:
        project_id (str):
            Required. The ID of the Google Cloud Platform
            project the cluster belongs to.
        region (str):
            Required. The Dataproc region in which to
            handle the request.
        cluster_name (str):
            Required. The cluster name.
        cluster_uuid (str):
            Optional. Specifying the ``cluster_uuid`` means the RPC will
            fail (with error NOT_FOUND) if a cluster with the specified
            UUID does not exist.
        request_id (str):
            Optional. A unique ID used to identify the request. If the
            server receives two
            `StartClusterRequest <https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#google.cloud.dataproc.v1.StartClusterRequest>`__\ s
            with the same id, then the second request will be ignored
            and the first
            [google.longrunning.Operation][google.longrunning.Operation]
            created and stored in the backend is returned.

            Recommendation: Set this value to a
            `UUID <https://en.wikipedia.org/wiki/Universally_unique_identifier>`__.

            The ID must contain only letters (a-z, A-Z), numbers (0-9),
            underscores (\_), and hyphens (-). The maximum length is 40
            characters.
    """

    project_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    region: str = proto.Field(
        proto.STRING,
        number=2,
    )
    cluster_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    cluster_uuid: str = proto.Field(
        proto.STRING,
        number=4,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=5,
    )


class DeleteClusterRequest(proto.Message):
    r"""A request to delete a cluster.

    Attributes:
        project_id (str):
            Required. The ID of the Google Cloud Platform
            project that the cluster belongs to.
        region (str):
            Required. The Dataproc region in which to
            handle the request.
        cluster_name (str):
            Required. The cluster name.
        cluster_uuid (str):
            Optional. Specifying the ``cluster_uuid`` means the RPC
            should fail (with error NOT_FOUND) if cluster with specified
            UUID does not exist.
        request_id (str):
            Optional. A unique ID used to identify the request. If the
            server receives two
            `DeleteClusterRequest <https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#google.cloud.dataproc.v1.DeleteClusterRequest>`__\ s
            with the same id, then the second request will be ignored
            and the first
            [google.longrunning.Operation][google.longrunning.Operation]
            created and stored in the backend is returned.

            It is recommended to always set this value to a
            `UUID <https://en.wikipedia.org/wiki/Universally_unique_identifier>`__.

            The ID must contain only letters (a-z, A-Z), numbers (0-9),
            underscores (\_), and hyphens (-). The maximum length is 40
            characters.
    """

    project_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    region: str = proto.Field(
        proto.STRING,
        number=3,
    )
    cluster_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    cluster_uuid: str = proto.Field(
        proto.STRING,
        number=4,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=5,
    )


class GetClusterRequest(proto.Message):
    r"""Request to get the resource representation for a cluster in a
    project.

    Attributes:
        project_id (str):
            Required. The ID of the Google Cloud Platform
            project that the cluster belongs to.
        region (str):
            Required. The Dataproc region in which to
            handle the request.
        cluster_name (str):
            Required. The cluster name.
    """

    project_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    region: str = proto.Field(
        proto.STRING,
        number=3,
    )
    cluster_name: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListClustersRequest(proto.Message):
    r"""A request to list the clusters in a project.

    Attributes:
        project_id (str):
            Required. The ID of the Google Cloud Platform
            project that the cluster belongs to.
        region (str):
            Required. The Dataproc region in which to
            handle the request.
        filter (str):
            Optional. A filter constraining the clusters to list.
            Filters are case-sensitive and have the following syntax:

            field = value [AND [field = value]] ...

            where **field** is one of ``status.state``, ``clusterName``,
            or ``labels.[KEY]``, and ``[KEY]`` is a label key. **value**
            can be ``*`` to match all values. ``status.state`` can be
            one of the following: ``ACTIVE``, ``INACTIVE``,
            ``CREATING``, ``RUNNING``, ``ERROR``, ``DELETING``,
            ``UPDATING``, ``STOPPING``, or ``STOPPED``. ``ACTIVE``
            contains the ``CREATING``, ``UPDATING``, and ``RUNNING``
            states. ``INACTIVE`` contains the ``DELETING``, ``ERROR``,
            ``STOPPING``, and ``STOPPED`` states. ``clusterName`` is the
            name of the cluster provided at creation time. Only the
            logical ``AND`` operator is supported; space-separated items
            are treated as having an implicit ``AND`` operator.

            Example filter:

            status.state = ACTIVE AND clusterName = mycluster AND
            labels.env = staging AND labels.starred = \*
        page_size (int):
            Optional. The standard List page size.
        page_token (str):
            Optional. The standard List page token.
    """

    project_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    region: str = proto.Field(
        proto.STRING,
        number=4,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=5,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListClustersResponse(proto.Message):
    r"""The list of all clusters in a project.

    Attributes:
        clusters (MutableSequence[google.cloud.dataproc_v1.types.Cluster]):
            Output only. The clusters in the project.
        next_page_token (str):
            Output only. This token is included in the response if there
            are more results to fetch. To fetch additional results,
            provide this value as the ``page_token`` in a subsequent
            ``ListClustersRequest``.
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


class DiagnoseClusterRequest(proto.Message):
    r"""A request to collect cluster diagnostic information.

    Attributes:
        project_id (str):
            Required. The ID of the Google Cloud Platform
            project that the cluster belongs to.
        region (str):
            Required. The Dataproc region in which to
            handle the request.
        cluster_name (str):
            Required. The cluster name.
        tarball_gcs_dir (str):
            Optional. (Optional) The output Cloud Storage
            directory for the diagnostic tarball. If not
            specified, a task-specific directory in the
            cluster's staging bucket will be used.
        tarball_access (google.cloud.dataproc_v1.types.DiagnoseClusterRequest.TarballAccess):
            Optional. (Optional) The access type to the
            diagnostic tarball. If not specified, falls back
            to default access of the bucket
        diagnosis_interval (google.type.interval_pb2.Interval):
            Optional. Time interval in which diagnosis
            should be carried out on the cluster.
        jobs (MutableSequence[str]):
            Optional. Specifies a list of jobs on which
            diagnosis is to be performed. Format:
            projects/{project}/regions/{region}/jobs/{job}
        yarn_application_ids (MutableSequence[str]):
            Optional. Specifies a list of yarn
            applications on which diagnosis is to be
            performed.
    """

    class TarballAccess(proto.Enum):
        r"""Defines who has access to the diagnostic tarball

        Values:
            TARBALL_ACCESS_UNSPECIFIED (0):
                Tarball Access unspecified. Falls back to
                default access of the bucket
            GOOGLE_CLOUD_SUPPORT (1):
                Google Cloud Support group has read access to
                the diagnostic tarball
            GOOGLE_DATAPROC_DIAGNOSE (2):
                Google Cloud Dataproc Diagnose service
                account has read access to the diagnostic
                tarball
        """

        TARBALL_ACCESS_UNSPECIFIED = 0
        GOOGLE_CLOUD_SUPPORT = 1
        GOOGLE_DATAPROC_DIAGNOSE = 2

    project_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    region: str = proto.Field(
        proto.STRING,
        number=3,
    )
    cluster_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    tarball_gcs_dir: str = proto.Field(
        proto.STRING,
        number=4,
    )
    tarball_access: TarballAccess = proto.Field(
        proto.ENUM,
        number=5,
        enum=TarballAccess,
    )
    diagnosis_interval: interval_pb2.Interval = proto.Field(
        proto.MESSAGE,
        number=6,
        message=interval_pb2.Interval,
    )
    jobs: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=10,
    )
    yarn_application_ids: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=11,
    )


class DiagnoseClusterResults(proto.Message):
    r"""The location of diagnostic output.

    Attributes:
        output_uri (str):
            Output only. The Cloud Storage URI of the
            diagnostic output. The output report is a plain
            text file with a summary of collected
            diagnostics.
    """

    output_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ReservationAffinity(proto.Message):
    r"""Reservation Affinity for consuming Zonal reservation.

    Attributes:
        consume_reservation_type (google.cloud.dataproc_v1.types.ReservationAffinity.Type):
            Optional. Type of reservation to consume
        key (str):
            Optional. Corresponds to the label key of
            reservation resource.
        values (MutableSequence[str]):
            Optional. Corresponds to the label values of
            reservation resource.
    """

    class Type(proto.Enum):
        r"""Indicates whether to consume capacity from an reservation or
        not.

        Values:
            TYPE_UNSPECIFIED (0):
                No description available.
            NO_RESERVATION (1):
                Do not consume from any allocated capacity.
            ANY_RESERVATION (2):
                Consume any reservation available.
            SPECIFIC_RESERVATION (3):
                Must consume from a specific reservation.
                Must specify key value fields for specifying the
                reservations.
        """

        TYPE_UNSPECIFIED = 0
        NO_RESERVATION = 1
        ANY_RESERVATION = 2
        SPECIFIC_RESERVATION = 3

    consume_reservation_type: Type = proto.Field(
        proto.ENUM,
        number=1,
        enum=Type,
    )
    key: str = proto.Field(
        proto.STRING,
        number=2,
    )
    values: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
