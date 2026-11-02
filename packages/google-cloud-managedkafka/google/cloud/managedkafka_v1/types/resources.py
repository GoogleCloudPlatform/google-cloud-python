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
    package="google.cloud.managedkafka.v1",
    manifest={
        "Cluster",
        "CapacityConfig",
        "RebalanceConfig",
        "NetworkConfig",
        "AccessConfig",
        "GcpConfig",
        "TlsConfig",
        "TrustConfig",
        "Topic",
        "ConsumerTopicMetadata",
        "ConsumerPartitionMetadata",
        "ConsumerGroup",
        "OperationMetadata",
        "ConnectCluster",
        "ConnectNetworkConfig",
        "ConnectAccessConfig",
        "ConnectGcpConfig",
        "Connector",
        "TaskRetryPolicy",
        "Acl",
        "AclEntry",
    },
)


class Cluster(proto.Message):
    r"""An Apache Kafka cluster deployed in a location.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        gcp_config (google.cloud.managedkafka_v1.types.GcpConfig):
            Required. Configuration properties for a
            Kafka cluster deployed to Google Cloud Platform.

            This field is a member of `oneof`_ ``platform_config``.
        name (str):
            Identifier. The name of the cluster. Structured like:
            projects/{project_number}/locations/{location}/clusters/{cluster_id}
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the cluster was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the cluster was
            last updated.
        labels (MutableMapping[str, str]):
            Optional. Labels as key value pairs.
        capacity_config (google.cloud.managedkafka_v1.types.CapacityConfig):
            Required. Capacity configuration for the
            Kafka cluster.
        rebalance_config (google.cloud.managedkafka_v1.types.RebalanceConfig):
            Optional. Rebalance configuration for the
            Kafka cluster.
        state (google.cloud.managedkafka_v1.types.Cluster.State):
            Output only. The current state of the
            cluster.
        satisfies_pzi (bool):
            Output only. Reserved for future use.

            This field is a member of `oneof`_ ``_satisfies_pzi``.
        satisfies_pzs (bool):
            Output only. Reserved for future use.

            This field is a member of `oneof`_ ``_satisfies_pzs``.
        tls_config (google.cloud.managedkafka_v1.types.TlsConfig):
            Optional. TLS configuration for the Kafka
            cluster.
    """

    class State(proto.Enum):
        r"""The state of the cluster.

        Values:
            STATE_UNSPECIFIED (0):
                A state was not specified.
            CREATING (1):
                The cluster is being created.
            ACTIVE (2):
                The cluster is active.
            DELETING (3):
                The cluster is being deleted.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        ACTIVE = 2
        DELETING = 3

    gcp_config: "GcpConfig" = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="platform_config",
        message="GcpConfig",
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
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
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    capacity_config: "CapacityConfig" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="CapacityConfig",
    )
    rebalance_config: "RebalanceConfig" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="RebalanceConfig",
    )
    state: State = proto.Field(
        proto.ENUM,
        number=10,
        enum=State,
    )
    satisfies_pzi: bool = proto.Field(
        proto.BOOL,
        number=11,
        optional=True,
    )
    satisfies_pzs: bool = proto.Field(
        proto.BOOL,
        number=12,
        optional=True,
    )
    tls_config: "TlsConfig" = proto.Field(
        proto.MESSAGE,
        number=13,
        message="TlsConfig",
    )


class CapacityConfig(proto.Message):
    r"""A capacity configuration of a Kafka cluster.

    Attributes:
        vcpu_count (int):
            Required. The number of vCPUs to provision
            for the cluster. Minimum: 3.
        memory_bytes (int):
            Required. The memory to provision for the
            cluster in bytes. The CPU:memory ratio
            (vCPU:GiB) must be between 1:1 and 1:8. Minimum:
            3221225472 (3 GiB).
    """

    vcpu_count: int = proto.Field(
        proto.INT64,
        number=1,
    )
    memory_bytes: int = proto.Field(
        proto.INT64,
        number=2,
    )


class RebalanceConfig(proto.Message):
    r"""Defines rebalancing behavior of a Kafka cluster.

    Attributes:
        mode (google.cloud.managedkafka_v1.types.RebalanceConfig.Mode):
            Optional. The rebalance behavior for the cluster. When not
            specified, defaults to ``NO_REBALANCE``.
    """

    class Mode(proto.Enum):
        r"""The partition rebalance mode for the cluster.

        Values:
            MODE_UNSPECIFIED (0):
                A mode was not specified. Do not use.
            NO_REBALANCE (1):
                Do not rebalance automatically.
            AUTO_REBALANCE_ON_SCALE_UP (2):
                Automatically rebalance topic partitions
                among brokers when the cluster is scaled up.
        """

        MODE_UNSPECIFIED = 0
        NO_REBALANCE = 1
        AUTO_REBALANCE_ON_SCALE_UP = 2

    mode: Mode = proto.Field(
        proto.ENUM,
        number=1,
        enum=Mode,
    )


class NetworkConfig(proto.Message):
    r"""The configuration of a Virtual Private Cloud (VPC) network
    that can access the Kafka cluster.

    Attributes:
        subnet (str):
            Required. Name of the VPC subnet in which to create Private
            Service Connect (PSC) endpoints for the Kafka brokers and
            bootstrap address. Structured like:
            projects/{project}/regions/{region}/subnetworks/{subnet_id}

            The subnet must be located in the same region as the Kafka
            cluster. The project may differ. Multiple subnets from the
            same parent network must not be specified.
    """

    subnet: str = proto.Field(
        proto.STRING,
        number=2,
    )


class AccessConfig(proto.Message):
    r"""The configuration of access to the Kafka cluster.

    Attributes:
        network_configs (MutableSequence[google.cloud.managedkafka_v1.types.NetworkConfig]):
            Required. Virtual Private Cloud (VPC)
            networks that must be granted direct access to
            the Kafka cluster. Minimum of 1 network is
            required. Maximum 10 networks can be specified.
    """

    network_configs: MutableSequence["NetworkConfig"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="NetworkConfig",
    )


class GcpConfig(proto.Message):
    r"""Configuration properties for a Kafka cluster deployed to
    Google Cloud Platform.

    Attributes:
        access_config (google.cloud.managedkafka_v1.types.AccessConfig):
            Required. Access configuration for the Kafka
            cluster.
        kms_key (str):
            Optional. Immutable. The Cloud KMS Key name to use for
            encryption. The key must be located in the same region as
            the cluster and cannot be changed. Structured like:
            projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}.
    """

    access_config: "AccessConfig" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="AccessConfig",
    )
    kms_key: str = proto.Field(
        proto.STRING,
        number=2,
    )


class TlsConfig(proto.Message):
    r"""The TLS configuration for the Kafka cluster.

    Attributes:
        trust_config (google.cloud.managedkafka_v1.types.TrustConfig):
            Optional. The configuration of the broker
            truststore. If specified, clients can use mTLS
            for authentication.
        ssl_principal_mapping_rules (str):
            Optional. A list of rules for mapping from SSL principal
            names to short names. These are applied in order by Kafka.
            Refer to the Apache Kafka documentation for
            ``ssl.principal.mapping.rules`` for the precise formatting
            details and syntax. Example:
            "RULE:^CN=(.\ *?),OU=ServiceUsers.*\ $/$1@example.com/,DEFAULT"

            This is a static Kafka broker configuration. Setting or
            modifying this field will trigger a rolling restart of the
            Kafka brokers to apply the change. An empty string means no
            rules are applied (Kafka default).
    """

    trust_config: "TrustConfig" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="TrustConfig",
    )
    ssl_principal_mapping_rules: str = proto.Field(
        proto.STRING,
        number=2,
    )


class TrustConfig(proto.Message):
    r"""Sources of CA certificates to install in the broker's
    truststore.

    Attributes:
        cas_configs (MutableSequence[google.cloud.managedkafka_v1.types.TrustConfig.CertificateAuthorityServiceConfig]):
            Optional. Configuration for the Google
            Certificate Authority Service. Maximum 10.
    """

    class CertificateAuthorityServiceConfig(proto.Message):
        r"""A configuration for the Google Certificate Authority Service.

        Attributes:
            ca_pool (str):
                Required. The name of the CA pool to pull CA certificates
                from. Structured like:
                projects/{project}/locations/{location}/caPools/{ca_pool}.
                The CA pool does not need to be in the same project or
                location as the Kafka cluster.
        """

        ca_pool: str = proto.Field(
            proto.STRING,
            number=1,
        )

    cas_configs: MutableSequence[CertificateAuthorityServiceConfig] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=CertificateAuthorityServiceConfig,
        )
    )


class Topic(proto.Message):
    r"""A Kafka topic in a given cluster.

    Attributes:
        name (str):
            Identifier. The name of the topic. The ``topic`` segment is
            used when connecting directly to the cluster. Structured
            like:
            projects/{project}/locations/{location}/clusters/{cluster}/topics/{topic}
        partition_count (int):
            Required. The number of partitions this topic
            has. The partition count can only be increased,
            not decreased. Please note that if partitions
            are increased for a topic that has a key, the
            partitioning logic or the ordering of the
            messages will be affected.
        replication_factor (int):
            Required. Immutable. The number of replicas
            of each partition. A replication factor of 3 is
            recommended for high availability.
        configs (MutableMapping[str, str]):
            Optional. Configurations for the topic that are overridden
            from the cluster defaults. The key of the map is a Kafka
            topic property name, for example: ``cleanup.policy``,
            ``compression.type``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    partition_count: int = proto.Field(
        proto.INT32,
        number=2,
    )
    replication_factor: int = proto.Field(
        proto.INT32,
        number=3,
    )
    configs: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )


class ConsumerTopicMetadata(proto.Message):
    r"""Metadata for a consumer group corresponding to a specific
    topic.

    Attributes:
        partitions (MutableMapping[int, google.cloud.managedkafka_v1.types.ConsumerPartitionMetadata]):
            Optional. Metadata for this consumer group
            and topic for all partition indexes it has
            metadata for.
    """

    partitions: MutableMapping[int, "ConsumerPartitionMetadata"] = proto.MapField(
        proto.INT32,
        proto.MESSAGE,
        number=1,
        message="ConsumerPartitionMetadata",
    )


class ConsumerPartitionMetadata(proto.Message):
    r"""Metadata for a consumer group corresponding to a specific
    partition.

    Attributes:
        offset (int):
            Required. The current offset for this
            partition, or 0 if no offset has been committed.
        metadata (str):
            Optional. The associated metadata for this
            partition, or empty if it does not exist.
    """

    offset: int = proto.Field(
        proto.INT64,
        number=1,
    )
    metadata: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ConsumerGroup(proto.Message):
    r"""A Kafka consumer group in a given cluster.

    Attributes:
        name (str):
            Identifier. The name of the consumer group. The
            ``consumer_group`` segment is used when connecting directly
            to the cluster. Structured like:
            projects/{project}/locations/{location}/clusters/{cluster}/consumerGroups/{consumer_group}
        topics (MutableMapping[str, google.cloud.managedkafka_v1.types.ConsumerTopicMetadata]):
            Optional. Metadata for this consumer group
            for all topics it has metadata for. The key of
            the map is a topic name, structured like:

            projects/{project}/locations/{location}/clusters/{cluster}/topics/{topic}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    topics: MutableMapping[str, "ConsumerTopicMetadata"] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=2,
        message="ConsumerTopicMetadata",
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
            Output only. Human-readable status of the
            operation, if any.
        requested_cancellation (bool):
            Output only. Identifies whether the user has requested
            cancellation of the operation. Operations that have been
            cancelled successfully have [Operation.error][] value with a
            [google.rpc.Status.code][google.rpc.Status.code] of 1,
            corresponding to ``Code.CANCELLED``.
        api_version (str):
            Output only. API version used to start the
            operation.
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


class ConnectCluster(proto.Message):
    r"""An Apache Kafka Connect cluster deployed in a location.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        gcp_config (google.cloud.managedkafka_v1.types.ConnectGcpConfig):
            Required. Configuration properties for a
            Kafka Connect cluster deployed to Google Cloud
            Platform.

            This field is a member of `oneof`_ ``platform_config``.
        name (str):
            Identifier. The name of the Kafka Connect cluster.
            Structured like:
            projects/{project_number}/locations/{location}/connectClusters/{connect_cluster_id}
        kafka_cluster (str):
            Required. Immutable. The name of the Kafka
            cluster this Kafka Connect cluster is attached
            to. Structured like:

            projects/{project}/locations/{location}/clusters/{cluster}
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the cluster was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the cluster was
            last updated.
        labels (MutableMapping[str, str]):
            Optional. Labels as key value pairs.
        capacity_config (google.cloud.managedkafka_v1.types.CapacityConfig):
            Required. Capacity configuration for the
            Kafka Connect cluster.
        state (google.cloud.managedkafka_v1.types.ConnectCluster.State):
            Output only. The current state of the
            cluster.
        config (MutableMapping[str, str]):
            Optional. Configurations for the worker that are overridden
            from the defaults. The key of the map is a Kafka Connect
            worker property name, for example:
            ``exactly.once.source.support``.
    """

    class State(proto.Enum):
        r"""The state of the cluster.

        Values:
            STATE_UNSPECIFIED (0):
                A state was not specified.
            CREATING (1):
                The cluster is being created.
            ACTIVE (2):
                The cluster is active.
            DELETING (3):
                The cluster is being deleted.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        ACTIVE = 2
        DELETING = 3

    gcp_config: "ConnectGcpConfig" = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="platform_config",
        message="ConnectGcpConfig",
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    kafka_cluster: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )
    capacity_config: "CapacityConfig" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="CapacityConfig",
    )
    state: State = proto.Field(
        proto.ENUM,
        number=8,
        enum=State,
    )
    config: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=9,
    )


class ConnectNetworkConfig(proto.Message):
    r"""The configuration of a Virtual Private Cloud (VPC) network
    that can access the Kafka Connect cluster.

    Attributes:
        primary_subnet (str):
            Required. VPC subnet to make available to the Kafka Connect
            cluster. Structured like:
            projects/{project}/regions/{region}/subnetworks/{subnet_id}

            It is used to create a Private Service Connect (PSC)
            interface for the Kafka Connect workers. It must be located
            in the same region as the Kafka Connect cluster.

            The CIDR range of the subnet must be within the IPv4 address
            ranges for private networks, as specified in RFC 1918. The
            primary subnet CIDR range must have a minimum size of /22
            (1024 addresses).
        additional_subnets (MutableSequence[str]):
            Optional. Additional subnets may be
            specified. They may be in another region, but
            must be in the same VPC network. The Connect
            workers can communicate with network endpoints
            in either the primary or additional subnets.
        dns_domain_names (MutableSequence[str]):
            Optional. Additional DNS domain names from
            the subnet's network to be made visible to the
            Connect Cluster. When using MirrorMaker2, it's
            necessary to add the bootstrap address's dns
            domain name of the target cluster to make it
            visible to the connector. For example:

            my-kafka-cluster.us-central1.managedkafka.my-project.cloud.goog
    """

    primary_subnet: str = proto.Field(
        proto.STRING,
        number=3,
    )
    additional_subnets: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    dns_domain_names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class ConnectAccessConfig(proto.Message):
    r"""The configuration of access to the Kafka Connect cluster.

    Attributes:
        network_configs (MutableSequence[google.cloud.managedkafka_v1.types.ConnectNetworkConfig]):
            Required.
            Virtual Private Cloud (VPC) networks that must
            be granted direct access to the Kafka Connect
            cluster. Minimum of 1 network is required.
            Maximum 10 networks can be specified.
    """

    network_configs: MutableSequence["ConnectNetworkConfig"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ConnectNetworkConfig",
    )


class ConnectGcpConfig(proto.Message):
    r"""Configuration properties for a Kafka Connect cluster deployed
    to Google Cloud Platform.

    Attributes:
        access_config (google.cloud.managedkafka_v1.types.ConnectAccessConfig):
            Required. Access configuration for the Kafka
            Connect cluster.
        secret_paths (MutableSequence[str]):
            Optional. Secrets to load into workers. Exact
            SecretVersions from Secret Manager must be
            provided -- aliases are not supported. Up to 32
            secrets may be loaded into one cluster. Format:

            projects/<project-id>/secrets/<secret-name>/versions/<version-id>
    """

    access_config: "ConnectAccessConfig" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="ConnectAccessConfig",
    )
    secret_paths: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class Connector(proto.Message):
    r"""A Kafka Connect connector in a given ConnectCluster.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        task_restart_policy (google.cloud.managedkafka_v1.types.TaskRetryPolicy):
            Optional. Restarts the individual tasks of a
            Connector.

            This field is a member of `oneof`_ ``restart_policy``.
        name (str):
            Identifier. The name of the connector. Structured like:
            projects/{project}/locations/{location}/connectClusters/{connect_cluster}/connectors/{connector}
        configs (MutableMapping[str, str]):
            Optional. Connector config as keys/values. The keys of the
            map are connector property names, for example:
            ``connector.class``, ``tasks.max``, ``key.converter``.
        state (google.cloud.managedkafka_v1.types.Connector.State):
            Output only. The current state of the
            connector.
    """

    class State(proto.Enum):
        r"""The state of the connector.

        Values:
            STATE_UNSPECIFIED (0):
                A state was not specified.
            UNASSIGNED (1):
                The connector is not assigned to any tasks,
                usually transient.
            RUNNING (2):
                The connector is running.
            PAUSED (3):
                The connector has been paused.
            FAILED (4):
                The connector has failed. See logs for why.
            RESTARTING (5):
                The connector is restarting.
            STOPPED (6):
                The connector has been stopped.
        """

        STATE_UNSPECIFIED = 0
        UNASSIGNED = 1
        RUNNING = 2
        PAUSED = 3
        FAILED = 4
        RESTARTING = 5
        STOPPED = 6

    task_restart_policy: "TaskRetryPolicy" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="restart_policy",
        message="TaskRetryPolicy",
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    configs: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=2,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=3,
        enum=State,
    )


class TaskRetryPolicy(proto.Message):
    r"""Task Retry Policy is implemented on a best-effort basis. Retry delay
    will be exponential based on provided minimum and maximum backoffs.
    https://en.wikipedia.org/wiki/Exponential_backoff. Note that the
    delay between consecutive task restarts may not always precisely
    match the configured settings. This can happen when the
    ConnectCluster is in rebalancing state or if the ConnectCluster is
    unresponsive etc. The default values for minimum and maximum
    backoffs are 60 seconds and 30 minutes respectively.

    Attributes:
        minimum_backoff (google.protobuf.duration_pb2.Duration):
            Optional. The minimum amount of time to wait
            before retrying a failed task. This sets a lower
            bound for the backoff delay.
        maximum_backoff (google.protobuf.duration_pb2.Duration):
            Optional. The maximum amount of time to wait
            before retrying a failed task. This sets an
            upper bound for the backoff delay.
    """

    minimum_backoff: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=1,
        message=duration_pb2.Duration,
    )
    maximum_backoff: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=2,
        message=duration_pb2.Duration,
    )


class Acl(proto.Message):
    r"""Represents the set of ACLs for a given Kafka Resource Pattern, which
    consists of resource_type, resource_name and pattern_type.

    Attributes:
        name (str):
            Identifier. The name for the acl. Represents a single
            Resource Pattern. Structured like:
            projects/{project}/locations/{location}/clusters/{cluster}/acls/{acl_id}

            The structure of ``acl_id`` defines the Resource Pattern
            (resource_type, resource_name, pattern_type) of the acl.
            ``acl_id`` is structured like one of the following:

            For acls on the cluster: ``cluster``

            For acls on a single resource within the cluster:
            ``topic/{resource_name}`` ``consumerGroup/{resource_name}``
            ``transactionalId/{resource_name}``

            For acls on all resources that match a prefix:
            ``topicPrefixed/{resource_name}``
            ``consumerGroupPrefixed/{resource_name}``
            ``transactionalIdPrefixed/{resource_name}``

            For acls on all resources of a given type (i.e. the wildcard
            literal "\*"): ``allTopics`` (represents ``topic/*``)
            ``allConsumerGroups`` (represents ``consumerGroup/*``)
            ``allTransactionalIds`` (represents ``transactionalId/*``)
        acl_entries (MutableSequence[google.cloud.managedkafka_v1.types.AclEntry]):
            Required. The ACL entries that apply to the
            resource pattern. The maximum number of allowed
            entries 100.
        etag (str):
            Optional. ``etag`` is used for concurrency control. An
            ``etag`` is returned in the response to ``GetAcl`` and
            ``CreateAcl``. Callers are required to put that etag in the
            request to ``UpdateAcl`` to ensure that their change will be
            applied to the same version of the acl that exists in the
            Kafka Cluster.

            A terminal 'T' character in the etag indicates that the
            AclEntries were truncated; more entries for the Acl exist on
            the Kafka Cluster, but can't be returned in the Acl due to
            repeated field limits.
        resource_type (str):
            Output only. The ACL resource type derived from the name.
            One of: CLUSTER, TOPIC, GROUP, TRANSACTIONAL_ID.
        resource_name (str):
            Output only. The ACL resource name derived from the name.
            For cluster resource_type, this is always "kafka-cluster".
            Can be the wildcard literal "\*".
        pattern_type (str):
            Output only. The ACL pattern type derived
            from the name. One of: LITERAL, PREFIXED.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    acl_entries: MutableSequence["AclEntry"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="AclEntry",
    )
    etag: str = proto.Field(
        proto.STRING,
        number=3,
    )
    resource_type: str = proto.Field(
        proto.STRING,
        number=4,
    )
    resource_name: str = proto.Field(
        proto.STRING,
        number=5,
    )
    pattern_type: str = proto.Field(
        proto.STRING,
        number=6,
    )


class AclEntry(proto.Message):
    r"""Represents the access granted for a given Resource Pattern in
    an ACL.

    Attributes:
        principal (str):
            Required. The principal. Specified as Google Cloud account,
            with the Kafka StandardAuthorizer prefix "User:". For
            example:
            "User:test-kafka-client@test-project.iam.gserviceaccount.com".
            Can be the wildcard "User:\*" to refer to all users.
        permission_type (str):
            Required. The permission type. Accepted
            values are (case insensitive): ALLOW, DENY.
        operation (str):
            Required. The operation type. Allowed values are (case
            insensitive): ALL, READ, WRITE, CREATE, DELETE, ALTER,
            DESCRIBE, CLUSTER_ACTION, DESCRIBE_CONFIGS, ALTER_CONFIGS,
            and IDEMPOTENT_WRITE. See
            https://kafka.apache.org/documentation/#operations_resources_and_protocols
            for valid combinations of resource_type and operation for
            different Kafka API requests.
        host (str):
            Required. The host. Must be set to "\*" for Managed Service
            for Apache Kafka.
    """

    principal: str = proto.Field(
        proto.STRING,
        number=4,
    )
    permission_type: str = proto.Field(
        proto.STRING,
        number=5,
    )
    operation: str = proto.Field(
        proto.STRING,
        number=6,
    )
    host: str = proto.Field(
        proto.STRING,
        number=7,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
