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
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.dataproc.v1",
    manifest={
        "Component",
        "FailureAction",
        "RuntimeConfig",
        "EnvironmentConfig",
        "ExecutionConfig",
        "SparkHistoryServerConfig",
        "PeripheralsConfig",
        "RuntimeInfo",
        "UsageMetrics",
        "UsageSnapshot",
        "GkeClusterConfig",
        "KubernetesClusterConfig",
        "KubernetesSoftwareConfig",
        "GkeNodePoolTarget",
        "GkeNodePoolConfig",
        "AuthenticationConfig",
        "AutotuningConfig",
        "RepositoryConfig",
        "PyPiRepositoryConfig",
    },
)


class Component(proto.Enum):
    r"""Cluster components that can be activated.

    Values:
        COMPONENT_UNSPECIFIED (0):
            Unspecified component. Specifying this will
            cause Cluster creation to fail.
        ANACONDA (5):
            The Anaconda component is no longer supported or applicable
            to [supported Dataproc on Compute Engine image versions]
            (https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-version-clusters#supported-dataproc-image-versions).
            It cannot be activated on clusters created with supported
            Dataproc on Compute Engine image versions.
        DELTA (20):
            Delta Lake.
        DOCKER (13):
            Docker
        DRUID (9):
            The Druid query engine. (alpha)
        FLINK (14):
            Flink
        HBASE (11):
            HBase. (beta)
        HIVE_WEBHCAT (3):
            The Hive Web HCatalog (the REST service for
            accessing HCatalog).
        HUDI (18):
            Hudi.
        ICEBERG (19):
            Iceberg.
        JUPYTER (1):
            The Jupyter Notebook.
        PIG (21):
            The Pig component.
        PRESTO (6):
            The Presto query engine.
        TRINO (17):
            The Trino query engine.
        RANGER (12):
            The Ranger service.
        SOLR (10):
            The Solr service.
        ZEPPELIN (4):
            The Zeppelin notebook.
        ZOOKEEPER (8):
            The Zookeeper service.
        JUPYTER_KERNEL_GATEWAY (22):
            The Jupyter Kernel Gateway.
    """

    COMPONENT_UNSPECIFIED = 0
    ANACONDA = 5
    DELTA = 20
    DOCKER = 13
    DRUID = 9
    FLINK = 14
    HBASE = 11
    HIVE_WEBHCAT = 3
    HUDI = 18
    ICEBERG = 19
    JUPYTER = 1
    PIG = 21
    PRESTO = 6
    TRINO = 17
    RANGER = 12
    SOLR = 10
    ZEPPELIN = 4
    ZOOKEEPER = 8
    JUPYTER_KERNEL_GATEWAY = 22


class FailureAction(proto.Enum):
    r"""Actions in response to failure of a resource associated with
    a cluster.

    Values:
        FAILURE_ACTION_UNSPECIFIED (0):
            When FailureAction is unspecified, failure action defaults
            to NO_ACTION.
        NO_ACTION (1):
            Take no action on failure to create a cluster resource.
            NO_ACTION is the default.
        DELETE (2):
            Delete the failed cluster resource.
    """

    FAILURE_ACTION_UNSPECIFIED = 0
    NO_ACTION = 1
    DELETE = 2


class RuntimeConfig(proto.Message):
    r"""Runtime configuration for a workload.

    Attributes:
        version (str):
            Optional. Version of the batch runtime.
        container_image (str):
            Optional. Optional custom container image for
            the job runtime environment. If not specified, a
            default container image will be used.
        properties (MutableMapping[str, str]):
            Optional. A mapping of property names to
            values, which are used to configure workload
            execution.
        repository_config (google.cloud.dataproc_v1.types.RepositoryConfig):
            Optional. Dependency repository
            configuration.
        autotuning_config (google.cloud.dataproc_v1.types.AutotuningConfig):
            Optional. Autotuning configuration of the
            workload.
        cohort (str):
            Optional. Cohort identifier. Identifies
            families of the workloads that have the same
            shape, for example, daily ETL jobs.
    """

    version: str = proto.Field(
        proto.STRING,
        number=1,
    )
    container_image: str = proto.Field(
        proto.STRING,
        number=2,
    )
    properties: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=3,
    )
    repository_config: "RepositoryConfig" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="RepositoryConfig",
    )
    autotuning_config: "AutotuningConfig" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="AutotuningConfig",
    )
    cohort: str = proto.Field(
        proto.STRING,
        number=7,
    )


class EnvironmentConfig(proto.Message):
    r"""Environment configuration for a workload.

    Attributes:
        execution_config (google.cloud.dataproc_v1.types.ExecutionConfig):
            Optional. Execution configuration for a
            workload.
        peripherals_config (google.cloud.dataproc_v1.types.PeripheralsConfig):
            Optional. Peripherals configuration that
            workload has access to.
    """

    execution_config: "ExecutionConfig" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="ExecutionConfig",
    )
    peripherals_config: "PeripheralsConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="PeripheralsConfig",
    )


class ExecutionConfig(proto.Message):
    r"""Execution configuration for a workload.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        service_account (str):
            Optional. Service account that used to
            execute workload.
        network_uri (str):
            Optional. Network URI to connect workload to.

            This field is a member of `oneof`_ ``network``.
        subnetwork_uri (str):
            Optional. Subnetwork URI to connect workload
            to.

            This field is a member of `oneof`_ ``network``.
        network_tags (MutableSequence[str]):
            Optional. Tags used for network traffic
            control.
        kms_key (str):
            Optional. The Cloud KMS key to use for
            encryption.
        idle_ttl (google.protobuf.duration_pb2.Duration):
            Optional. Applies to sessions only. The duration to keep the
            session alive while it's idling. Exceeding this threshold
            causes the session to terminate. This field cannot be set on
            a batch workload. Minimum value is 10 minutes; maximum value
            is 14 days (see JSON representation of
            `Duration <https://developers.google.com/protocol-buffers/docs/proto3#json>`__).
            Defaults to 1 hour if not set. If both ``ttl`` and
            ``idle_ttl`` are specified for an interactive session, the
            conditions are treated as ``OR`` conditions: the workload
            will be terminated when it has been idle for ``idle_ttl`` or
            when ``ttl`` has been exceeded, whichever occurs first.
        ttl (google.protobuf.duration_pb2.Duration):
            Optional. The duration after which the workload will be
            terminated, specified as the JSON representation for
            `Duration <https://protobuf.dev/programming-guides/proto3/#json>`__.
            When the workload exceeds this duration, it will be
            unconditionally terminated without waiting for ongoing work
            to finish. If ``ttl`` is not specified for a batch workload,
            the workload will be allowed to run until it exits naturally
            (or run forever without exiting). If ``ttl`` is not
            specified for an interactive session, it defaults to 24
            hours. If ``ttl`` is not specified for a batch that uses
            2.1+ runtime version, it defaults to 4 hours. Minimum value
            is 10 minutes; maximum value is 14 days. If both ``ttl`` and
            ``idle_ttl`` are specified (for an interactive session), the
            conditions are treated as ``OR`` conditions: the workload
            will be terminated when it has been idle for ``idle_ttl`` or
            when ``ttl`` has been exceeded, whichever occurs first.
        staging_bucket (str):
            Optional. A Cloud Storage bucket used to stage workload
            dependencies, config files, and store workload output and
            other ephemeral data, such as Spark history files. If you do
            not specify a staging bucket, Cloud Dataproc will determine
            a Cloud Storage location according to the region where your
            workload is running, and then create and manage
            project-level, per-location staging and temporary buckets.
            **This field requires a Cloud Storage bucket name, not a
            ``gs://...`` URI to a Cloud Storage bucket.**
        authentication_config (google.cloud.dataproc_v1.types.AuthenticationConfig):
            Optional. Authentication configuration used
            to set the default identity for the workload
            execution. The config specifies the type of
            identity (service account or user) that will be
            used by workloads to access resources on the
            project(s).
        resource_manager_tags (MutableMapping[str, str]):
            Optional. Associates Resource Manager tags with the workload
            nodes. There is a max limit of 30 tags. Keys and values can
            be either in numeric format, such as
            ``tagKeys/{tag_key_id}`` and ``tagValues/{tag_value_id}``,
            or in namespaced format, such as
            ``{org_id|project_id}/{tag_key_short_name}`` and
            ``{tag_value_short_name}``.
    """

    service_account: str = proto.Field(
        proto.STRING,
        number=2,
    )
    network_uri: str = proto.Field(
        proto.STRING,
        number=4,
        oneof="network",
    )
    subnetwork_uri: str = proto.Field(
        proto.STRING,
        number=5,
        oneof="network",
    )
    network_tags: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )
    kms_key: str = proto.Field(
        proto.STRING,
        number=7,
    )
    idle_ttl: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=8,
        message=duration_pb2.Duration,
    )
    ttl: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=9,
        message=duration_pb2.Duration,
    )
    staging_bucket: str = proto.Field(
        proto.STRING,
        number=10,
    )
    authentication_config: "AuthenticationConfig" = proto.Field(
        proto.MESSAGE,
        number=11,
        message="AuthenticationConfig",
    )
    resource_manager_tags: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=12,
    )


class SparkHistoryServerConfig(proto.Message):
    r"""Spark History Server configuration for the workload.

    Attributes:
        dataproc_cluster (str):
            Optional. Resource name of an existing Dataproc Cluster to
            act as a Spark History Server for the workload.

            Example:

            - ``projects/[project_id]/regions/[region]/clusters/[cluster_name]``
    """

    dataproc_cluster: str = proto.Field(
        proto.STRING,
        number=1,
    )


class PeripheralsConfig(proto.Message):
    r"""Auxiliary services configuration for a workload.

    Attributes:
        metastore_service (str):
            Optional. Resource name of an existing Dataproc Metastore
            service.

            Example:

            - ``projects/[project_id]/locations/[region]/services/[service_id]``
        spark_history_server_config (google.cloud.dataproc_v1.types.SparkHistoryServerConfig):
            Optional. The Spark History Server
            configuration for the workload.
    """

    metastore_service: str = proto.Field(
        proto.STRING,
        number=1,
    )
    spark_history_server_config: "SparkHistoryServerConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="SparkHistoryServerConfig",
    )


class RuntimeInfo(proto.Message):
    r"""Runtime information about workload execution.

    Attributes:
        endpoints (MutableMapping[str, str]):
            Output only. Map of remote access endpoints
            (such as web interfaces and APIs) to their URIs.
        output_uri (str):
            Output only. A URI pointing to the location
            of the stdout and stderr of the workload.
        diagnostic_output_uri (str):
            Output only. A URI pointing to the location
            of the diagnostics tarball.
        approximate_usage (google.cloud.dataproc_v1.types.UsageMetrics):
            Output only. Approximate workload resource usage, calculated
            when the workload completes (see [Dataproc Serverless
            pricing]
            (https://cloud.google.com/dataproc-serverless/pricing)).

            **Note:** This metric calculation may change in the future,
            for example, to capture cumulative workload resource
            consumption during workload execution (see the [Dataproc
            Serverless release notes]
            (https://cloud.google.com/dataproc-serverless/docs/release-notes)
            for announcements, changes, fixes and other Dataproc
            developments).
        current_usage (google.cloud.dataproc_v1.types.UsageSnapshot):
            Output only. Snapshot of current workload
            resource usage.
    """

    endpoints: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=1,
    )
    output_uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    diagnostic_output_uri: str = proto.Field(
        proto.STRING,
        number=3,
    )
    approximate_usage: "UsageMetrics" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="UsageMetrics",
    )
    current_usage: "UsageSnapshot" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="UsageSnapshot",
    )


class UsageMetrics(proto.Message):
    r"""Usage metrics represent approximate total resources consumed
    by a workload.

    Attributes:
        milli_dcu_seconds (int):
            Optional. DCU (Dataproc Compute Units) usage in
            (``milliDCU`` x ``seconds``) (see [Dataproc Serverless
            pricing]
            (https://cloud.google.com/dataproc-serverless/pricing)).
        shuffle_storage_gb_seconds (int):
            Optional. Shuffle storage usage in (``GB`` x ``seconds``)
            (see [Dataproc Serverless pricing]
            (https://cloud.google.com/dataproc-serverless/pricing)).
        milli_accelerator_seconds (int):
            Optional. [DEPRECATED] Accelerator usage in
            (``milliAccelerator`` x ``seconds``) (see [Dataproc
            Serverless pricing]
            (https://cloud.google.com/dataproc-serverless/pricing)).
        accelerator_type (str):
            Optional. [DEPRECATED] Accelerator type being used, if any
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. The timestamp of the usage metrics.
    """

    milli_dcu_seconds: int = proto.Field(
        proto.INT64,
        number=1,
    )
    shuffle_storage_gb_seconds: int = proto.Field(
        proto.INT64,
        number=2,
    )
    milli_accelerator_seconds: int = proto.Field(
        proto.INT64,
        number=3,
    )
    accelerator_type: str = proto.Field(
        proto.STRING,
        number=4,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )


class UsageSnapshot(proto.Message):
    r"""The usage snapshot represents the resources consumed by a
    workload at a specified time.

    Attributes:
        milli_dcu (int):
            Optional. Milli (one-thousandth) Dataproc Compute Units
            (DCUs) (see [Dataproc Serverless pricing]
            (https://cloud.google.com/dataproc-serverless/pricing)).
        shuffle_storage_gb (int):
            Optional. Shuffle Storage in gigabytes (GB). (see [Dataproc
            Serverless pricing]
            (https://cloud.google.com/dataproc-serverless/pricing))
        milli_dcu_premium (int):
            Optional. Milli (one-thousandth) Dataproc Compute Units
            (DCUs) charged at premium tier (see [Dataproc Serverless
            pricing]
            (https://cloud.google.com/dataproc-serverless/pricing)).
        shuffle_storage_gb_premium (int):
            Optional. Shuffle Storage in gigabytes (GB) charged at
            premium tier. (see [Dataproc Serverless pricing]
            (https://cloud.google.com/dataproc-serverless/pricing))
        milli_accelerator (int):
            Optional. Milli (one-thousandth) accelerator. (see [Dataproc
            Serverless pricing]
            (https://cloud.google.com/dataproc-serverless/pricing))
        accelerator_type (str):
            Optional. Accelerator type being used, if any
        snapshot_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. The timestamp of the usage
            snapshot.
    """

    milli_dcu: int = proto.Field(
        proto.INT64,
        number=1,
    )
    shuffle_storage_gb: int = proto.Field(
        proto.INT64,
        number=2,
    )
    milli_dcu_premium: int = proto.Field(
        proto.INT64,
        number=4,
    )
    shuffle_storage_gb_premium: int = proto.Field(
        proto.INT64,
        number=5,
    )
    milli_accelerator: int = proto.Field(
        proto.INT64,
        number=6,
    )
    accelerator_type: str = proto.Field(
        proto.STRING,
        number=7,
    )
    snapshot_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )


class GkeClusterConfig(proto.Message):
    r"""The cluster's GKE config.

    Attributes:
        gke_cluster_target (str):
            Optional. A target GKE cluster to deploy to. It must be in
            the same project and region as the Dataproc cluster (the GKE
            cluster can be zonal or regional). Format:
            'projects/{project}/locations/{location}/clusters/{cluster_id}'
        node_pool_target (MutableSequence[google.cloud.dataproc_v1.types.GkeNodePoolTarget]):
            Optional. GKE node pools where workloads will be scheduled.
            At least one node pool must be assigned the ``DEFAULT``
            [GkeNodePoolTarget.Role][google.cloud.dataproc.v1.GkeNodePoolTarget.Role].
            If a ``GkeNodePoolTarget`` is not specified, Dataproc
            constructs a ``DEFAULT`` ``GkeNodePoolTarget``. Each role
            can be given to only one ``GkeNodePoolTarget``. All node
            pools must have the same location settings.
    """

    gke_cluster_target: str = proto.Field(
        proto.STRING,
        number=2,
    )
    node_pool_target: MutableSequence["GkeNodePoolTarget"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="GkeNodePoolTarget",
    )


class KubernetesClusterConfig(proto.Message):
    r"""The configuration for running the Dataproc cluster on
    Kubernetes.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        kubernetes_namespace (str):
            Optional. A namespace within the Kubernetes
            cluster to deploy into. If this namespace does
            not exist, it is created. If it exists, Dataproc
            verifies that another Dataproc VirtualCluster is
            not installed into it. If not specified, the
            name of the Dataproc Cluster is used.
        gke_cluster_config (google.cloud.dataproc_v1.types.GkeClusterConfig):
            Required. The configuration for running the
            Dataproc cluster on GKE.

            This field is a member of `oneof`_ ``config``.
        kubernetes_software_config (google.cloud.dataproc_v1.types.KubernetesSoftwareConfig):
            Optional. The software configuration for this
            Dataproc cluster running on Kubernetes.
    """

    kubernetes_namespace: str = proto.Field(
        proto.STRING,
        number=1,
    )
    gke_cluster_config: "GkeClusterConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="config",
        message="GkeClusterConfig",
    )
    kubernetes_software_config: "KubernetesSoftwareConfig" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="KubernetesSoftwareConfig",
    )


class KubernetesSoftwareConfig(proto.Message):
    r"""The software configuration for this Dataproc cluster running
    on Kubernetes.

    Attributes:
        component_version (MutableMapping[str, str]):
            The components that should be installed in
            this Dataproc cluster. The key must be a string
            from the KubernetesComponent enumeration. The
            value is the version of the software to be
            installed.
            At least one entry must be specified.
        properties (MutableMapping[str, str]):
            The properties to set on daemon config files.

            Property keys are specified in ``prefix:property`` format,
            for example ``spark:spark.kubernetes.container.image``. The
            following are supported prefixes and their mappings:

            - spark: ``spark-defaults.conf``

            For more information, see `Cluster
            properties <https://cloud.google.com/dataproc/docs/concepts/cluster-properties>`__.
    """

    component_version: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=1,
    )
    properties: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=2,
    )


class GkeNodePoolTarget(proto.Message):
    r"""GKE node pools that Dataproc workloads run on.

    Attributes:
        node_pool (str):
            Required. The target GKE node pool. Format:
            'projects/{project}/locations/{location}/clusters/{cluster}/nodePools/{node_pool}'
        roles (MutableSequence[google.cloud.dataproc_v1.types.GkeNodePoolTarget.Role]):
            Required. The roles associated with the GKE
            node pool.
        node_pool_config (google.cloud.dataproc_v1.types.GkeNodePoolConfig):
            Input only. The configuration for the GKE
            node pool.
            If specified, Dataproc attempts to create a node
            pool with the specified shape. If one with the
            same name already exists, it is verified against
            all specified fields. If a field differs, the
            virtual cluster creation will fail.

            If omitted, any node pool with the specified
            name is used. If a node pool with the specified
            name does not exist, Dataproc create a node pool
            with default values.

            This is an input only field. It will not be
            returned by the API.
    """

    class Role(proto.Enum):
        r"""``Role`` specifies the tasks that will run on the node pool. Roles
        can be specific to workloads. Exactly one
        [GkeNodePoolTarget][google.cloud.dataproc.v1.GkeNodePoolTarget]
        within the virtual cluster must have the ``DEFAULT`` role, which is
        used to run all workloads that are not associated with a node pool.

        Values:
            ROLE_UNSPECIFIED (0):
                Role is unspecified.
            DEFAULT (1):
                At least one node pool must have the ``DEFAULT`` role. Work
                assigned to a role that is not associated with a node pool
                is assigned to the node pool with the ``DEFAULT`` role. For
                example, work assigned to the ``CONTROLLER`` role will be
                assigned to the node pool with the ``DEFAULT`` role if no
                node pool has the ``CONTROLLER`` role.
            CONTROLLER (2):
                Run work associated with the Dataproc control
                plane (for example, controllers and webhooks).
                Very low resource requirements.
            SPARK_DRIVER (3):
                Run work associated with a Spark driver of a
                job.
            SPARK_EXECUTOR (4):
                Run work associated with a Spark executor of
                a job.
        """

        ROLE_UNSPECIFIED = 0
        DEFAULT = 1
        CONTROLLER = 2
        SPARK_DRIVER = 3
        SPARK_EXECUTOR = 4

    node_pool: str = proto.Field(
        proto.STRING,
        number=1,
    )
    roles: MutableSequence[Role] = proto.RepeatedField(
        proto.ENUM,
        number=2,
        enum=Role,
    )
    node_pool_config: "GkeNodePoolConfig" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="GkeNodePoolConfig",
    )


class GkeNodePoolConfig(proto.Message):
    r"""The configuration of a GKE node pool used by a `Dataproc-on-GKE
    cluster <https://cloud.google.com/dataproc/docs/concepts/jobs/dataproc-gke#create-a-dataproc-on-gke-cluster>`__.

    Attributes:
        config (google.cloud.dataproc_v1.types.GkeNodePoolConfig.GkeNodeConfig):
            Optional. The node pool configuration.
        locations (MutableSequence[str]):
            Optional. The list of Compute Engine
            `zones <https://cloud.google.com/compute/docs/zones#available>`__
            where node pool nodes associated with a Dataproc on GKE
            virtual cluster will be located.

            **Note:** All node pools associated with a virtual cluster
            must be located in the same region as the virtual cluster,
            and they must be located in the same zone within that
            region.

            If a location is not specified during node pool creation,
            Dataproc on GKE will choose the zone.
        autoscaling (google.cloud.dataproc_v1.types.GkeNodePoolConfig.GkeNodePoolAutoscalingConfig):
            Optional. The autoscaler configuration for
            this node pool. The autoscaler is enabled only
            when a valid configuration is present.
    """

    class GkeNodeConfig(proto.Message):
        r"""Parameters that describe cluster nodes.

        Attributes:
            machine_type (str):
                Optional. The name of a Compute Engine `machine
                type <https://cloud.google.com/compute/docs/machine-types>`__.
            local_ssd_count (int):
                Optional. The number of local SSD disks to attach to the
                node, which is limited by the maximum number of disks
                allowable per zone (see `Adding Local
                SSDs <https://cloud.google.com/compute/docs/disks/local-ssd>`__).
            preemptible (bool):
                Optional. Whether the nodes are created as legacy
                [preemptible VM instances]
                (https://cloud.google.com/compute/docs/instances/preemptible).
                Also see
                [Spot][google.cloud.dataproc.v1.GkeNodePoolConfig.GkeNodeConfig.spot]
                VMs, preemptible VM instances without a maximum lifetime.
                Legacy and Spot preemptible nodes cannot be used in a node
                pool with the ``CONTROLLER`` [role]
                (/dataproc/docs/reference/rest/v1/projects.regions.clusters#role)
                or in the DEFAULT node pool if the CONTROLLER role is not
                assigned (the DEFAULT node pool will assume the CONTROLLER
                role).
            accelerators (MutableSequence[google.cloud.dataproc_v1.types.GkeNodePoolConfig.GkeNodePoolAcceleratorConfig]):
                Optional. A list of `hardware
                accelerators <https://cloud.google.com/compute/docs/gpus>`__
                to attach to each node.
            min_cpu_platform (str):
                Optional. `Minimum CPU
                platform <https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform>`__
                to be used by this instance. The instance may be scheduled
                on the specified or a newer CPU platform. Specify the
                friendly names of CPU platforms, such as "Intel Haswell"\`
                or Intel Sandy Bridge".
            boot_disk_kms_key (str):
                Optional. The [Customer Managed Encryption Key (CMEK)]
                (https://cloud.google.com/kubernetes-engine/docs/how-to/using-cmek)
                used to encrypt the boot disk attached to each node in the
                node pool. Specify the key using the following format:
                ``projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}``
            spot (bool):
                Optional. Whether the nodes are created as [Spot VM
                instances]
                (https://cloud.google.com/compute/docs/instances/spot). Spot
                VMs are the latest update to legacy [preemptible
                VMs][google.cloud.dataproc.v1.GkeNodePoolConfig.GkeNodeConfig.preemptible].
                Spot VMs do not have a maximum lifetime. Legacy and Spot
                preemptible nodes cannot be used in a node pool with the
                ``CONTROLLER``
                `role </dataproc/docs/reference/rest/v1/projects.regions.clusters#role>`__
                or in the DEFAULT node pool if the CONTROLLER role is not
                assigned (the DEFAULT node pool will assume the CONTROLLER
                role).
        """

        machine_type: str = proto.Field(
            proto.STRING,
            number=1,
        )
        local_ssd_count: int = proto.Field(
            proto.INT32,
            number=7,
        )
        preemptible: bool = proto.Field(
            proto.BOOL,
            number=10,
        )
        accelerators: MutableSequence[
            "GkeNodePoolConfig.GkeNodePoolAcceleratorConfig"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=11,
            message="GkeNodePoolConfig.GkeNodePoolAcceleratorConfig",
        )
        min_cpu_platform: str = proto.Field(
            proto.STRING,
            number=13,
        )
        boot_disk_kms_key: str = proto.Field(
            proto.STRING,
            number=23,
        )
        spot: bool = proto.Field(
            proto.BOOL,
            number=32,
        )

    class GkeNodePoolAcceleratorConfig(proto.Message):
        r"""A GkeNodeConfigAcceleratorConfig represents a Hardware
        Accelerator request for a node pool.

        Attributes:
            accelerator_count (int):
                The number of accelerator cards exposed to an
                instance.
            accelerator_type (str):
                The accelerator type resource namename (see
                GPUs on Compute Engine).
            gpu_partition_size (str):
                Size of partitions to create on the GPU. Valid values are
                described in the NVIDIA `mig user
                guide <https://docs.nvidia.com/datacenter/tesla/mig-user-guide/#partitioning>`__.
        """

        accelerator_count: int = proto.Field(
            proto.INT64,
            number=1,
        )
        accelerator_type: str = proto.Field(
            proto.STRING,
            number=2,
        )
        gpu_partition_size: str = proto.Field(
            proto.STRING,
            number=3,
        )

    class GkeNodePoolAutoscalingConfig(proto.Message):
        r"""GkeNodePoolAutoscaling contains information the cluster
        autoscaler needs to adjust the size of the node pool to the
        current cluster usage.

        Attributes:
            min_node_count (int):
                The minimum number of nodes in the node pool. Must be >= 0
                and <= max_node_count.
            max_node_count (int):
                The maximum number of nodes in the node pool. Must be >=
                min_node_count, and must be > 0. **Note:** Quota must be
                sufficient to scale up the cluster.
        """

        min_node_count: int = proto.Field(
            proto.INT32,
            number=2,
        )
        max_node_count: int = proto.Field(
            proto.INT32,
            number=3,
        )

    config: GkeNodeConfig = proto.Field(
        proto.MESSAGE,
        number=2,
        message=GkeNodeConfig,
    )
    locations: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=13,
    )
    autoscaling: GkeNodePoolAutoscalingConfig = proto.Field(
        proto.MESSAGE,
        number=4,
        message=GkeNodePoolAutoscalingConfig,
    )


class AuthenticationConfig(proto.Message):
    r"""Authentication configuration for a workload is used to set
    the default identity for the workload execution.
    The config specifies the type of identity (service account or
    user) that will be used by workloads to access resources on the
    project(s).

    Attributes:
        user_workload_authentication_type (google.cloud.dataproc_v1.types.AuthenticationConfig.AuthenticationType):
            Optional. Authentication type for the user
            workload running in containers.
    """

    class AuthenticationType(proto.Enum):
        r"""Authentication types for workload execution.

        Values:
            AUTHENTICATION_TYPE_UNSPECIFIED (0):
                If AuthenticationType is unspecified then
                END_USER_CREDENTIALS is used for 3.0 and newer runtimes, and
                SERVICE_ACCOUNT is used for older runtimes.
            SERVICE_ACCOUNT (1):
                Use service account credentials for
                authenticating to other services.
            END_USER_CREDENTIALS (2):
                Use OAuth credentials associated with the
                workload creator/user for authenticating to
                other services.
        """

        AUTHENTICATION_TYPE_UNSPECIFIED = 0
        SERVICE_ACCOUNT = 1
        END_USER_CREDENTIALS = 2

    user_workload_authentication_type: AuthenticationType = proto.Field(
        proto.ENUM,
        number=1,
        enum=AuthenticationType,
    )


class AutotuningConfig(proto.Message):
    r"""Autotuning configuration of the workload.

    Attributes:
        scenarios (MutableSequence[google.cloud.dataproc_v1.types.AutotuningConfig.Scenario]):
            Optional. Scenarios for which tunings are
            applied.
    """

    class Scenario(proto.Enum):
        r"""Scenario represents a specific goal that autotuning will
        attempt to achieve by modifying workloads.

        Values:
            SCENARIO_UNSPECIFIED (0):
                Default value.
            SCALING (2):
                Scaling recommendations such as
                initialExecutors.
            BROADCAST_HASH_JOIN (3):
                Adding hints for potential relation
                broadcasts.
            MEMORY (4):
                Memory management for workloads.
            NONE (5):
                No autotuning.
            AUTO (6):
                Automatic selection of scenarios.
        """

        SCENARIO_UNSPECIFIED = 0
        SCALING = 2
        BROADCAST_HASH_JOIN = 3
        MEMORY = 4
        NONE = 5
        AUTO = 6

    scenarios: MutableSequence[Scenario] = proto.RepeatedField(
        proto.ENUM,
        number=2,
        enum=Scenario,
    )


class RepositoryConfig(proto.Message):
    r"""Configuration for dependency repositories

    Attributes:
        pypi_repository_config (google.cloud.dataproc_v1.types.PyPiRepositoryConfig):
            Optional. Configuration for PyPi repository.
    """

    pypi_repository_config: "PyPiRepositoryConfig" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="PyPiRepositoryConfig",
    )


class PyPiRepositoryConfig(proto.Message):
    r"""Configuration for PyPi repository

    Attributes:
        pypi_repository (str):
            Optional. The PyPi repository address. **Note: This field is
            not available for batch workloads.**
    """

    pypi_repository: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
