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
import google.rpc.status_pb2 as status_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.edgecontainer.v1",
    manifest={
        "KmsKeyState",
        "ResourceState",
        "Cluster",
        "ClusterNetworking",
        "Fleet",
        "ClusterUser",
        "Authorization",
        "NodePool",
        "Machine",
        "VpnConnection",
        "LocationMetadata",
        "ZoneMetadata",
        "ConfigData",
        "Quota",
        "MaintenancePolicy",
        "MaintenanceWindow",
        "RecurringTimeWindow",
        "MaintenanceExclusionWindow",
        "TimeWindow",
        "ServerConfig",
        "ChannelConfig",
        "Version",
    },
)


class KmsKeyState(proto.Enum):
    r"""Represents the accessibility state of a customer-managed KMS
    key used for CMEK integration.

    Values:
        KMS_KEY_STATE_UNSPECIFIED (0):
            Unspecified.
        KMS_KEY_STATE_KEY_AVAILABLE (1):
            The key is available for use, and dependent
            resources should be accessible.
        KMS_KEY_STATE_KEY_UNAVAILABLE (2):
            The key is unavailable for an unspecified
            reason. Dependent resources may be inaccessible.
    """

    KMS_KEY_STATE_UNSPECIFIED = 0
    KMS_KEY_STATE_KEY_AVAILABLE = 1
    KMS_KEY_STATE_KEY_UNAVAILABLE = 2


class ResourceState(proto.Enum):
    r"""Represents if the resource is in lock down state or pending.

    Values:
        RESOURCE_STATE_UNSPECIFIED (0):
            Default value.
        RESOURCE_STATE_LOCK_DOWN (1):
            The resource is in LOCK DOWN state.
        RESOURCE_STATE_LOCK_DOWN_PENDING (2):
            The resource is pending lock down.
    """

    RESOURCE_STATE_UNSPECIFIED = 0
    RESOURCE_STATE_LOCK_DOWN = 1
    RESOURCE_STATE_LOCK_DOWN_PENDING = 2


class Cluster(proto.Message):
    r"""A Google Distributed Cloud Edge Kubernetes cluster.

    Attributes:
        name (str):
            Required. The resource name of the cluster.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the cluster was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the cluster was
            last updated.
        labels (MutableMapping[str, str]):
            Labels associated with this resource.
        fleet (google.cloud.edgecontainer_v1.types.Fleet):
            Required. Fleet configuration.
        networking (google.cloud.edgecontainer_v1.types.ClusterNetworking):
            Required. Cluster-wide networking
            configuration.
        authorization (google.cloud.edgecontainer_v1.types.Authorization):
            Required. Immutable. RBAC policy that will be
            applied and managed by GEC.
        default_max_pods_per_node (int):
            Optional. The default maximum number of pods
            per node used if a maximum value is not
            specified explicitly for a node pool in this
            cluster. If unspecified, the Kubernetes default
            value will be used.
        endpoint (str):
            Output only. The IP address of the Kubernetes
            API server.
        port (int):
            Output only. The port number of the
            Kubernetes API server.
        cluster_ca_certificate (str):
            Output only. The PEM-encoded public
            certificate of the cluster's CA.
        maintenance_policy (google.cloud.edgecontainer_v1.types.MaintenancePolicy):
            Optional. Cluster-wide maintenance policy
            configuration.
        control_plane_version (str):
            Output only. The control plane release
            version
        node_version (str):
            Output only. The lowest release version among
            all worker nodes. This field can be empty if the
            cluster does not have any worker nodes.
        control_plane (google.cloud.edgecontainer_v1.types.Cluster.ControlPlane):
            Optional. The configuration of the cluster
            control plane.
        system_addons_config (google.cloud.edgecontainer_v1.types.Cluster.SystemAddonsConfig):
            Optional. The configuration of the system
            add-ons.
        external_load_balancer_ipv4_address_pools (MutableSequence[str]):
            Optional. IPv4 address pools for cluster data
            plane external load balancing.
        control_plane_encryption (google.cloud.edgecontainer_v1.types.Cluster.ControlPlaneEncryption):
            Optional. Remote control plane disk
            encryption options. This field is only used when
            enabling CMEK support.
        status (google.cloud.edgecontainer_v1.types.Cluster.Status):
            Output only. The current status of the
            cluster.
        maintenance_events (MutableSequence[google.cloud.edgecontainer_v1.types.Cluster.MaintenanceEvent]):
            Output only. All the maintenance events
            scheduled for the cluster, including the ones
            ongoing, planned for the future and done in the
            past (up to 90 days).
        target_version (str):
            Optional. The target cluster version. For
            example: "1.5.0".
        release_channel (google.cloud.edgecontainer_v1.types.Cluster.ReleaseChannel):
            Optional. The release channel a cluster is
            subscribed to.
        survivability_config (google.cloud.edgecontainer_v1.types.Cluster.SurvivabilityConfig):
            Optional. Configuration of the cluster
            survivability, e.g., for the case when network
            connectivity is lost. Note: This only applies to
            local control plane clusters.
        external_load_balancer_ipv6_address_pools (MutableSequence[str]):
            Optional. IPv6 address pools for cluster data
            plane external load balancing.
        connection_state (google.cloud.edgecontainer_v1.types.Cluster.ConnectionState):
            Output only. The current connection state of
            the cluster.
    """

    class Status(proto.Enum):
        r"""Indicates the status of the cluster.

        Values:
            STATUS_UNSPECIFIED (0):
                Status unknown.
            PROVISIONING (1):
                The cluster is being created.
            RUNNING (2):
                The cluster is created and fully usable.
            DELETING (3):
                The cluster is being deleted.
            ERROR (4):
                The status indicates that some errors
                occurred while reconciling/deleting the cluster.
            RECONCILING (5):
                The cluster is undergoing some work such as
                version upgrades, etc.
        """

        STATUS_UNSPECIFIED = 0
        PROVISIONING = 1
        RUNNING = 2
        DELETING = 3
        ERROR = 4
        RECONCILING = 5

    class ReleaseChannel(proto.Enum):
        r"""The release channel a cluster is subscribed to.

        Values:
            RELEASE_CHANNEL_UNSPECIFIED (0):
                Unspecified release channel. This will
                default to the REGULAR channel.
            NONE (1):
                No release channel.
            REGULAR (2):
                Regular release channel.
        """

        RELEASE_CHANNEL_UNSPECIFIED = 0
        NONE = 1
        REGULAR = 2

    class ControlPlane(proto.Message):
        r"""Configuration of the cluster control plane.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            remote (google.cloud.edgecontainer_v1.types.Cluster.ControlPlane.Remote):
                Remote control plane configuration.

                This field is a member of `oneof`_ ``config``.
            local (google.cloud.edgecontainer_v1.types.Cluster.ControlPlane.Local):
                Local control plane configuration.

                Warning: Local control plane clusters must be
                created in their own project. Local control
                plane clusters cannot coexist in the same
                project with any other type of clusters,
                including non-GDCE clusters. Mixing local
                control plane GDCE clusters with any other type
                of clusters in the same project can result in
                data loss.

                This field is a member of `oneof`_ ``config``.
        """

        class SharedDeploymentPolicy(proto.Enum):
            r"""Represents the policy configuration about how user
            applications are deployed.

            Values:
                SHARED_DEPLOYMENT_POLICY_UNSPECIFIED (0):
                    Unspecified.
                ALLOWED (1):
                    User applications can be deployed both on
                    control plane and worker nodes.
                DISALLOWED (2):
                    User applications can not be deployed on
                    control plane nodes and can only be deployed on
                    worker nodes.
            """

            SHARED_DEPLOYMENT_POLICY_UNSPECIFIED = 0
            ALLOWED = 1
            DISALLOWED = 2

        class Remote(proto.Message):
            r"""Configuration specific to clusters with a control plane
            hosted remotely.

            """

        class Local(proto.Message):
            r"""Configuration specific to clusters with a control plane
            hosted locally.
            Warning: Local control plane clusters must be created in their
            own project. Local control plane clusters cannot coexist in the
            same project with any other type of clusters, including non-GDCE
            clusters. Mixing local control plane GDCE clusters with any
            other type of clusters in the same project can result in data
            loss.

            Attributes:
                node_location (str):
                    Name of the Google Distributed Cloud Edge zones where this
                    node pool will be created. For example:
                    ``us-central1-edge-customer-a``.
                node_count (int):
                    The number of nodes to serve as replicas of
                    the Control Plane.
                machine_filter (str):
                    Only machines matching this filter will be allowed to host
                    control plane nodes. The filtering language accepts strings
                    like "name=", and is documented here:
                    `AIP-160 <https://google.aip.dev/160>`__.
                shared_deployment_policy (google.cloud.edgecontainer_v1.types.Cluster.ControlPlane.SharedDeploymentPolicy):
                    Policy configuration about how user
                    applications are deployed.
                control_plane_node_storage_schema (str):
                    Optional. Name for the storage schema of
                    control plane nodes.
                    Warning: Configurable node local storage schema
                    feature is an experimental feature, and is not
                    recommended for general use in production
                    clusters/nodepools.
            """

            node_location: str = proto.Field(
                proto.STRING,
                number=1,
            )
            node_count: int = proto.Field(
                proto.INT32,
                number=2,
            )
            machine_filter: str = proto.Field(
                proto.STRING,
                number=3,
            )
            shared_deployment_policy: "Cluster.ControlPlane.SharedDeploymentPolicy" = (
                proto.Field(
                    proto.ENUM,
                    number=4,
                    enum="Cluster.ControlPlane.SharedDeploymentPolicy",
                )
            )
            control_plane_node_storage_schema: str = proto.Field(
                proto.STRING,
                number=5,
            )

        remote: "Cluster.ControlPlane.Remote" = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="config",
            message="Cluster.ControlPlane.Remote",
        )
        local: "Cluster.ControlPlane.Local" = proto.Field(
            proto.MESSAGE,
            number=2,
            oneof="config",
            message="Cluster.ControlPlane.Local",
        )

    class SystemAddonsConfig(proto.Message):
        r"""Config that customers are allowed to define for GDCE system
        add-ons.

        Attributes:
            ingress (google.cloud.edgecontainer_v1.types.Cluster.SystemAddonsConfig.Ingress):
                Optional. Config for Ingress.
            vm_service_config (google.cloud.edgecontainer_v1.types.Cluster.SystemAddonsConfig.VMServiceConfig):
                Optional. Config for VM Service.
        """

        class Ingress(proto.Message):
            r"""Config for the Ingress add-on which allows customers to
            create an Ingress object to manage external access to the
            servers in a cluster. The add-on consists of istiod and
            istio-ingress.

            Attributes:
                disabled (bool):
                    Optional. Whether Ingress is disabled.
                ipv4_vip (str):
                    Optional. Ingress VIP.
            """

            disabled: bool = proto.Field(
                proto.BOOL,
                number=1,
            )
            ipv4_vip: str = proto.Field(
                proto.STRING,
                number=2,
            )

        class VMServiceConfig(proto.Message):
            r"""VMServiceConfig defines the configuration for GDCE VM
            Service.

            Attributes:
                vmm_enabled (bool):
                    Optional. Whether VMM is enabled.
            """

            vmm_enabled: bool = proto.Field(
                proto.BOOL,
                number=1,
            )

        ingress: "Cluster.SystemAddonsConfig.Ingress" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="Cluster.SystemAddonsConfig.Ingress",
        )
        vm_service_config: "Cluster.SystemAddonsConfig.VMServiceConfig" = proto.Field(
            proto.MESSAGE,
            number=4,
            message="Cluster.SystemAddonsConfig.VMServiceConfig",
        )

    class ControlPlaneEncryption(proto.Message):
        r"""Configuration for Customer-managed KMS key support for
        control plane nodes.

        Attributes:
            kms_key (str):
                Optional. The Cloud KMS CryptoKey e.g.
                projects/{project}/locations/{location}/keyRings/{keyRing}/cryptoKeys/{cryptoKey}
                to use for protecting control plane disks. If
                not specified, a Google-managed key will be used
                instead.
            kms_key_active_version (str):
                Output only. The Cloud KMS CryptoKeyVersion currently in use
                for protecting control plane disks. Only applicable if
                kms_key is set.
            kms_key_state (google.cloud.edgecontainer_v1.types.KmsKeyState):
                Output only. Availability of the Cloud KMS CryptoKey. If not
                ``KEY_AVAILABLE``, then nodes may go offline as they cannot
                access their local data. This can be caused by a lack of
                permissions to use the key, or if the key is disabled or
                deleted.
            kms_status (google.rpc.status_pb2.Status):
                Output only. Error status returned by Cloud KMS when using
                this key. This field may be populated only if
                ``kms_key_state`` is not ``KMS_KEY_STATE_KEY_AVAILABLE``. If
                populated, this field contains the error status reported by
                Cloud KMS.
            resource_state (google.cloud.edgecontainer_v1.types.ResourceState):
                Output only. The current resource state
                associated with the cmek.
        """

        kms_key: str = proto.Field(
            proto.STRING,
            number=1,
        )
        kms_key_active_version: str = proto.Field(
            proto.STRING,
            number=2,
        )
        kms_key_state: "KmsKeyState" = proto.Field(
            proto.ENUM,
            number=3,
            enum="KmsKeyState",
        )
        kms_status: status_pb2.Status = proto.Field(
            proto.MESSAGE,
            number=4,
            message=status_pb2.Status,
        )
        resource_state: "ResourceState" = proto.Field(
            proto.ENUM,
            number=5,
            enum="ResourceState",
        )

    class MaintenanceEvent(proto.Message):
        r"""A Maintenance Event is an operation that could cause
        temporary disruptions to the cluster workloads, including
        Google-driven or user-initiated cluster upgrades, user-initiated
        cluster configuration changes that require restarting nodes,
        etc.

        Attributes:
            uuid (str):
                Output only. UUID of the maintenance event.
            target_version (str):
                Output only. The target version of the
                cluster.
            operation (str):
                Output only. The operation for running the maintenance
                event. Specified in the format
                projects/*/locations/*/operations/\*. If the maintenance
                event is split into multiple operations (e.g. due to
                maintenance windows), the latest one is recorded.
            type_ (google.cloud.edgecontainer_v1.types.Cluster.MaintenanceEvent.Type):
                Output only. The type of the maintenance
                event.
            schedule (google.cloud.edgecontainer_v1.types.Cluster.MaintenanceEvent.Schedule):
                Output only. The schedule of the maintenance
                event.
            state (google.cloud.edgecontainer_v1.types.Cluster.MaintenanceEvent.State):
                Output only. The state of the maintenance
                event.
            create_time (google.protobuf.timestamp_pb2.Timestamp):
                Output only. The time when the maintenance
                event request was created.
            start_time (google.protobuf.timestamp_pb2.Timestamp):
                Output only. The time when the maintenance
                event started.
            end_time (google.protobuf.timestamp_pb2.Timestamp):
                Output only. The time when the maintenance event ended,
                either successfully or not. If the maintenance event is
                split into multiple maintenance windows, end_time is only
                updated when the whole flow ends.
            update_time (google.protobuf.timestamp_pb2.Timestamp):
                Output only. The time when the maintenance
                event message was updated.
        """

        class Type(proto.Enum):
            r"""Indicates the maintenance event type.

            Values:
                TYPE_UNSPECIFIED (0):
                    Unspecified.
                USER_INITIATED_UPGRADE (1):
                    Upgrade initiated by users.
                GOOGLE_DRIVEN_UPGRADE (2):
                    Upgrade driven by Google.
            """

            TYPE_UNSPECIFIED = 0
            USER_INITIATED_UPGRADE = 1
            GOOGLE_DRIVEN_UPGRADE = 2

        class Schedule(proto.Enum):
            r"""Indicates when the maintenance event should be performed.

            Values:
                SCHEDULE_UNSPECIFIED (0):
                    Unspecified.
                IMMEDIATELY (1):
                    Immediately after receiving the request.
            """

            SCHEDULE_UNSPECIFIED = 0
            IMMEDIATELY = 1

        class State(proto.Enum):
            r"""Indicates the maintenance event state.

            Values:
                STATE_UNSPECIFIED (0):
                    Unspecified.
                RECONCILING (1):
                    The maintenance event is ongoing. The cluster
                    might be unusable.
                SUCCEEDED (2):
                    The maintenance event succeeded.
                FAILED (3):
                    The maintenance event failed.
            """

            STATE_UNSPECIFIED = 0
            RECONCILING = 1
            SUCCEEDED = 2
            FAILED = 3

        uuid: str = proto.Field(
            proto.STRING,
            number=1,
        )
        target_version: str = proto.Field(
            proto.STRING,
            number=2,
        )
        operation: str = proto.Field(
            proto.STRING,
            number=3,
        )
        type_: "Cluster.MaintenanceEvent.Type" = proto.Field(
            proto.ENUM,
            number=4,
            enum="Cluster.MaintenanceEvent.Type",
        )
        schedule: "Cluster.MaintenanceEvent.Schedule" = proto.Field(
            proto.ENUM,
            number=5,
            enum="Cluster.MaintenanceEvent.Schedule",
        )
        state: "Cluster.MaintenanceEvent.State" = proto.Field(
            proto.ENUM,
            number=6,
            enum="Cluster.MaintenanceEvent.State",
        )
        create_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=7,
            message=timestamp_pb2.Timestamp,
        )
        start_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=8,
            message=timestamp_pb2.Timestamp,
        )
        end_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=9,
            message=timestamp_pb2.Timestamp,
        )
        update_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=10,
            message=timestamp_pb2.Timestamp,
        )

    class SurvivabilityConfig(proto.Message):
        r"""Configuration of the cluster survivability, e.g., for the
        case when network connectivity is lost.

        Attributes:
            offline_reboot_ttl (google.protobuf.duration_pb2.Duration):
                Optional. Time period that allows the cluster
                nodes to be rebooted and become functional
                without network connectivity to Google. The
                default 0 means not allowed. The maximum is 7
                days.
        """

        offline_reboot_ttl: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=1,
            message=duration_pb2.Duration,
        )

    class ConnectionState(proto.Message):
        r"""ConnectionState holds the current connection state from the
        cluster to Google.

        Attributes:
            state (google.cloud.edgecontainer_v1.types.Cluster.ConnectionState.State):
                Output only. The current connection state.
            update_time (google.protobuf.timestamp_pb2.Timestamp):
                Output only. The time when the connection
                state was last changed.
        """

        class State(proto.Enum):
            r"""The connection state.

            Values:
                STATE_UNSPECIFIED (0):
                    Unknown connection state.
                DISCONNECTED (1):
                    This cluster is currently disconnected from
                    Google.
                CONNECTED (2):
                    This cluster is currently connected to
                    Google.
                CONNECTED_AND_SYNCING (3):
                    This cluster is currently connected to
                    Google, but may have recently reconnected after
                    a disconnection. It is still syncing back.
            """

            STATE_UNSPECIFIED = 0
            DISCONNECTED = 1
            CONNECTED = 2
            CONNECTED_AND_SYNCING = 3

        state: "Cluster.ConnectionState.State" = proto.Field(
            proto.ENUM,
            number=1,
            enum="Cluster.ConnectionState.State",
        )
        update_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=2,
            message=timestamp_pb2.Timestamp,
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
    fleet: "Fleet" = proto.Field(
        proto.MESSAGE,
        number=11,
        message="Fleet",
    )
    networking: "ClusterNetworking" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="ClusterNetworking",
    )
    authorization: "Authorization" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="Authorization",
    )
    default_max_pods_per_node: int = proto.Field(
        proto.INT32,
        number=8,
    )
    endpoint: str = proto.Field(
        proto.STRING,
        number=6,
    )
    port: int = proto.Field(
        proto.INT32,
        number=19,
    )
    cluster_ca_certificate: str = proto.Field(
        proto.STRING,
        number=10,
    )
    maintenance_policy: "MaintenancePolicy" = proto.Field(
        proto.MESSAGE,
        number=12,
        message="MaintenancePolicy",
    )
    control_plane_version: str = proto.Field(
        proto.STRING,
        number=13,
    )
    node_version: str = proto.Field(
        proto.STRING,
        number=14,
    )
    control_plane: ControlPlane = proto.Field(
        proto.MESSAGE,
        number=15,
        message=ControlPlane,
    )
    system_addons_config: SystemAddonsConfig = proto.Field(
        proto.MESSAGE,
        number=16,
        message=SystemAddonsConfig,
    )
    external_load_balancer_ipv4_address_pools: MutableSequence[str] = (
        proto.RepeatedField(
            proto.STRING,
            number=17,
        )
    )
    control_plane_encryption: ControlPlaneEncryption = proto.Field(
        proto.MESSAGE,
        number=18,
        message=ControlPlaneEncryption,
    )
    status: Status = proto.Field(
        proto.ENUM,
        number=20,
        enum=Status,
    )
    maintenance_events: MutableSequence[MaintenanceEvent] = proto.RepeatedField(
        proto.MESSAGE,
        number=21,
        message=MaintenanceEvent,
    )
    target_version: str = proto.Field(
        proto.STRING,
        number=22,
    )
    release_channel: ReleaseChannel = proto.Field(
        proto.ENUM,
        number=23,
        enum=ReleaseChannel,
    )
    survivability_config: SurvivabilityConfig = proto.Field(
        proto.MESSAGE,
        number=24,
        message=SurvivabilityConfig,
    )
    external_load_balancer_ipv6_address_pools: MutableSequence[str] = (
        proto.RepeatedField(
            proto.STRING,
            number=25,
        )
    )
    connection_state: ConnectionState = proto.Field(
        proto.MESSAGE,
        number=27,
        message=ConnectionState,
    )


class ClusterNetworking(proto.Message):
    r"""Cluster-wide networking configuration.

    Attributes:
        cluster_ipv4_cidr_blocks (MutableSequence[str]):
            Required. All pods in the cluster are
            assigned an RFC1918 IPv4 address from these
            blocks. Only a single block is supported. This
            field cannot be changed after creation.
        services_ipv4_cidr_blocks (MutableSequence[str]):
            Required. All services in the cluster are
            assigned an RFC1918 IPv4 address from these
            blocks. Only a single block is supported. This
            field cannot be changed after creation.
    """

    cluster_ipv4_cidr_blocks: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    services_ipv4_cidr_blocks: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class Fleet(proto.Message):
    r"""Fleet related configuration.

    Fleets are a Google Cloud concept for logically organizing
    clusters, letting you use and manage multi-cluster capabilities
    and apply consistent policies across your systems.

    Attributes:
        project (str):
            Required. The name of the Fleet host project where this
            cluster will be registered.

            Project names are formatted as
            ``projects/<project-number>``.
        membership (str):
            Output only. The name of the managed Hub Membership resource
            associated to this cluster.

            Membership names are formatted as
            ``projects/<project-number>/locations/global/membership/<cluster-id>``.
    """

    project: str = proto.Field(
        proto.STRING,
        number=1,
    )
    membership: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ClusterUser(proto.Message):
    r"""A user principal for an RBAC policy.

    Attributes:
        username (str):
            Required. An active Google username.
    """

    username: str = proto.Field(
        proto.STRING,
        number=1,
    )


class Authorization(proto.Message):
    r"""RBAC policy that will be applied and managed by GEC.

    Attributes:
        admin_users (google.cloud.edgecontainer_v1.types.ClusterUser):
            Required. User that will be granted the
            cluster-admin role on the cluster, providing
            full access to the cluster. Currently, this is a
            singular field, but will be expanded to allow
            multiple admins in the future.
    """

    admin_users: "ClusterUser" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="ClusterUser",
    )


class NodePool(proto.Message):
    r"""A set of Kubernetes nodes in a cluster with common
    configuration and specification.

    Attributes:
        name (str):
            Required. The resource name of the node pool.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the node pool was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the node pool was
            last updated.
        labels (MutableMapping[str, str]):
            Labels associated with this resource.
        node_location (str):
            Name of the Google Distributed Cloud Edge zone where this
            node pool will be created. For example:
            ``us-central1-edge-customer-a``.
        node_count (int):
            Required. The number of nodes in the pool.
        machine_filter (str):
            Only machines matching this filter will be allowed to join
            the node pool. The filtering language accepts strings like
            "name=", and is documented in more detail in
            `AIP-160 <https://google.aip.dev/160>`__.
        local_disk_encryption (google.cloud.edgecontainer_v1.types.NodePool.LocalDiskEncryption):
            Optional. Local disk encryption options. This
            field is only used when enabling CMEK support.
        node_version (str):
            Output only. The lowest release version among
            all worker nodes.
        node_config (google.cloud.edgecontainer_v1.types.NodePool.NodeConfig):
            Optional. Configuration for each node in the
            NodePool
    """

    class LocalDiskEncryption(proto.Message):
        r"""Configuration for CMEK support for edge machine local disk
        encryption.

        Attributes:
            kms_key (str):
                Optional. The Cloud KMS CryptoKey e.g.
                projects/{project}/locations/{location}/keyRings/{keyRing}/cryptoKeys/{cryptoKey}
                to use for protecting node local disks. If not
                specified, a Google-managed key will be used
                instead.
            kms_key_active_version (str):
                Output only. The Cloud KMS CryptoKeyVersion currently in use
                for protecting node local disks. Only applicable if kms_key
                is set.
            kms_key_state (google.cloud.edgecontainer_v1.types.KmsKeyState):
                Output only. Availability of the Cloud KMS CryptoKey. If not
                ``KEY_AVAILABLE``, then nodes may go offline as they cannot
                access their local data. This can be caused by a lack of
                permissions to use the key, or if the key is disabled or
                deleted.
            kms_status (google.rpc.status_pb2.Status):
                Output only. Error status returned by Cloud KMS when using
                this key. This field may be populated only if
                ``kms_key_state`` is not ``KMS_KEY_STATE_KEY_AVAILABLE``. If
                populated, this field contains the error status reported by
                Cloud KMS.
            resource_state (google.cloud.edgecontainer_v1.types.ResourceState):
                Output only. The current resource state
                associated with the cmek.
        """

        kms_key: str = proto.Field(
            proto.STRING,
            number=1,
        )
        kms_key_active_version: str = proto.Field(
            proto.STRING,
            number=2,
        )
        kms_key_state: "KmsKeyState" = proto.Field(
            proto.ENUM,
            number=3,
            enum="KmsKeyState",
        )
        kms_status: status_pb2.Status = proto.Field(
            proto.MESSAGE,
            number=4,
            message=status_pb2.Status,
        )
        resource_state: "ResourceState" = proto.Field(
            proto.ENUM,
            number=5,
            enum="ResourceState",
        )

    class NodeConfig(proto.Message):
        r"""Configuration for each node in the NodePool

        Attributes:
            labels (MutableMapping[str, str]):
                Optional. The Kubernetes node labels
            node_storage_schema (str):
                Optional. Name for the storage schema of
                worker nodes.
                Warning: Configurable node local storage schema
                feature is an experimental feature, and is not
                recommended for general use in production
                clusters/nodepools.
        """

        labels: MutableMapping[str, str] = proto.MapField(
            proto.STRING,
            proto.STRING,
            number=1,
        )
        node_storage_schema: str = proto.Field(
            proto.STRING,
            number=2,
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
    node_location: str = proto.Field(
        proto.STRING,
        number=8,
    )
    node_count: int = proto.Field(
        proto.INT32,
        number=6,
    )
    machine_filter: str = proto.Field(
        proto.STRING,
        number=7,
    )
    local_disk_encryption: LocalDiskEncryption = proto.Field(
        proto.MESSAGE,
        number=9,
        message=LocalDiskEncryption,
    )
    node_version: str = proto.Field(
        proto.STRING,
        number=10,
    )
    node_config: NodeConfig = proto.Field(
        proto.MESSAGE,
        number=11,
        message=NodeConfig,
    )


class Machine(proto.Message):
    r"""A Google Distributed Cloud Edge machine capable of acting as
    a Kubernetes node.

    Attributes:
        name (str):
            Required. The resource name of the machine.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the node pool was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the node pool was
            last updated.
        labels (MutableMapping[str, str]):
            Labels associated with this resource.
        hosted_node (str):
            Canonical resource name of the node that this machine is
            responsible for hosting e.g.
            projects/{project}/locations/{location}/clusters/{cluster_id}/nodePools/{pool_id}/{node},
            Or empty if the machine is not assigned to assume the role
            of a node.

            For control plane nodes hosted on edge machines, this will
            return the following format:
            "projects/{project}/locations/{location}/clusters/{cluster_id}/controlPlaneNodes/{node}".
        zone (str):
            The Google Distributed Cloud Edge zone of
            this machine.
        version (str):
            Output only. The software version of the
            machine.
        disabled (bool):
            Output only. Whether the machine is disabled.
            If disabled, the machine is unable to enter
            service.
    """

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
    hosted_node: str = proto.Field(
        proto.STRING,
        number=5,
    )
    zone: str = proto.Field(
        proto.STRING,
        number=6,
    )
    version: str = proto.Field(
        proto.STRING,
        number=7,
    )
    disabled: bool = proto.Field(
        proto.BOOL,
        number=8,
    )


class VpnConnection(proto.Message):
    r"""A VPN connection .

    Attributes:
        name (str):
            Required. The resource name of VPN connection
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the VPN connection
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the VPN connection
            was last updated.
        labels (MutableMapping[str, str]):
            Labels associated with this resource.
        nat_gateway_ip (str):
            NAT gateway IP, or WAN IP address. If a
            customer has multiple NAT IPs, the customer
            needs to configure NAT such that only one
            external IP maps to the GMEC Anthos cluster.
            This is empty if NAT is not used.
        bgp_routing_mode (google.cloud.edgecontainer_v1.types.VpnConnection.BgpRoutingMode):
            Dynamic routing mode of the VPC network, ``regional`` or
            ``global``.
        cluster (str):
            The canonical Cluster name to connect to. It
            is in the form of
            projects/{project}/locations/{location}/clusters/{cluster}.
        vpc (str):
            The network ID of VPC to connect to.
        vpc_project (google.cloud.edgecontainer_v1.types.VpnConnection.VpcProject):
            Optional. Project detail of the VPC network.
            Required if VPC is in a different project than
            the cluster project.
        enable_high_availability (bool):
            Whether this VPN connection has HA enabled on
            cluster side. If enabled, when creating VPN
            connection we will attempt to use 2 ANG floating
            IPs.
        router (str):
            Optional. The VPN connection Cloud Router
            name.
        details (google.cloud.edgecontainer_v1.types.VpnConnection.Details):
            Output only. The created connection details.
    """

    class BgpRoutingMode(proto.Enum):
        r"""Routing mode.

        Values:
            BGP_ROUTING_MODE_UNSPECIFIED (0):
                Unknown.
            REGIONAL (1):
                Regional mode.
            GLOBAL (2):
                Global mode.
        """

        BGP_ROUTING_MODE_UNSPECIFIED = 0
        REGIONAL = 1
        GLOBAL = 2

    class VpcProject(proto.Message):
        r"""Project detail of the VPC network.

        Attributes:
            project_id (str):
                The project of the VPC to connect to. If not
                specified, it is the same as the cluster
                project.
            service_account (str):
                Optional. Deprecated: do not use.
        """

        project_id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        service_account: str = proto.Field(
            proto.STRING,
            number=2,
        )

    class Details(proto.Message):
        r"""The created connection details.

        Attributes:
            state (google.cloud.edgecontainer_v1.types.VpnConnection.Details.State):
                The state of this connection.
            error (str):
                The error message. This is only populated
                when state=ERROR.
            cloud_router (google.cloud.edgecontainer_v1.types.VpnConnection.Details.CloudRouter):
                The Cloud Router info.
            cloud_vpns (MutableSequence[google.cloud.edgecontainer_v1.types.VpnConnection.Details.CloudVpn]):
                Each connection has multiple Cloud VPN
                gateways.
        """

        class State(proto.Enum):
            r"""The current connection state.

            Values:
                STATE_UNSPECIFIED (0):
                    Unknown.
                STATE_CONNECTED (1):
                    Connected.
                STATE_CONNECTING (2):
                    Still connecting.
                STATE_ERROR (3):
                    Error occurred.
            """

            STATE_UNSPECIFIED = 0
            STATE_CONNECTED = 1
            STATE_CONNECTING = 2
            STATE_ERROR = 3

        class CloudRouter(proto.Message):
            r"""The Cloud Router info.

            Attributes:
                name (str):
                    The associated Cloud Router name.
            """

            name: str = proto.Field(
                proto.STRING,
                number=1,
            )

        class CloudVpn(proto.Message):
            r"""The Cloud VPN info.

            Attributes:
                gateway (str):
                    The created Cloud VPN gateway name.
            """

            gateway: str = proto.Field(
                proto.STRING,
                number=1,
            )

        state: "VpnConnection.Details.State" = proto.Field(
            proto.ENUM,
            number=1,
            enum="VpnConnection.Details.State",
        )
        error: str = proto.Field(
            proto.STRING,
            number=2,
        )
        cloud_router: "VpnConnection.Details.CloudRouter" = proto.Field(
            proto.MESSAGE,
            number=3,
            message="VpnConnection.Details.CloudRouter",
        )
        cloud_vpns: MutableSequence["VpnConnection.Details.CloudVpn"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=4,
                message="VpnConnection.Details.CloudVpn",
            )
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
    nat_gateway_ip: str = proto.Field(
        proto.STRING,
        number=5,
    )
    bgp_routing_mode: BgpRoutingMode = proto.Field(
        proto.ENUM,
        number=6,
        enum=BgpRoutingMode,
    )
    cluster: str = proto.Field(
        proto.STRING,
        number=7,
    )
    vpc: str = proto.Field(
        proto.STRING,
        number=8,
    )
    vpc_project: VpcProject = proto.Field(
        proto.MESSAGE,
        number=11,
        message=VpcProject,
    )
    enable_high_availability: bool = proto.Field(
        proto.BOOL,
        number=9,
    )
    router: str = proto.Field(
        proto.STRING,
        number=12,
    )
    details: Details = proto.Field(
        proto.MESSAGE,
        number=10,
        message=Details,
    )


class LocationMetadata(proto.Message):
    r"""Metadata for a given
    [google.cloud.location.Location][google.cloud.location.Location].

    Attributes:
        available_zones (MutableMapping[str, google.cloud.edgecontainer_v1.types.ZoneMetadata]):
            The set of available Google Distributed Cloud
            Edge zones in the location. The map is keyed by
            the lowercase ID of each zone.
    """

    available_zones: MutableMapping[str, "ZoneMetadata"] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=1,
        message="ZoneMetadata",
    )


class ZoneMetadata(proto.Message):
    r"""A Google Distributed Cloud Edge zone where edge machines are
    located.

    Attributes:
        quota (MutableSequence[google.cloud.edgecontainer_v1.types.Quota]):
            Quota for resources in this zone.
        rack_types (MutableMapping[str, google.cloud.edgecontainer_v1.types.ZoneMetadata.RackType]):
            The map keyed by rack name and has value of
            RackType.
        config_data (google.cloud.edgecontainer_v1.types.ConfigData):
            Config data for the zone.
    """

    class RackType(proto.Enum):
        r"""Type of the rack.

        Values:
            RACK_TYPE_UNSPECIFIED (0):
                Unspecified rack type, single rack also
                belongs to this type.
            BASE (1):
                Base rack type, a pair of two modified
                Config-1 racks containing Aggregation switches.
            EXPANSION (2):
                Expansion rack type, also known as standalone
                racks, added by customers on demand.
        """

        RACK_TYPE_UNSPECIFIED = 0
        BASE = 1
        EXPANSION = 2

    quota: MutableSequence["Quota"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Quota",
    )
    rack_types: MutableMapping[str, RackType] = proto.MapField(
        proto.STRING,
        proto.ENUM,
        number=2,
        enum=RackType,
    )
    config_data: "ConfigData" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="ConfigData",
    )


class ConfigData(proto.Message):
    r"""Config data holds all the config related data for the zone.

    Attributes:
        available_external_lb_pools_ipv4 (MutableSequence[str]):
            list of available v4 ip pools for external
            loadbalancer
        available_external_lb_pools_ipv6 (MutableSequence[str]):
            list of available v6 ip pools for external
            loadbalancer
    """

    available_external_lb_pools_ipv4: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    available_external_lb_pools_ipv6: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class Quota(proto.Message):
    r"""Represents quota for Edge Container resources.

    Attributes:
        metric (str):
            Name of the quota metric.
        limit (float):
            Quota limit for this metric.
        usage (float):
            Current usage of this metric.
    """

    metric: str = proto.Field(
        proto.STRING,
        number=1,
    )
    limit: float = proto.Field(
        proto.DOUBLE,
        number=2,
    )
    usage: float = proto.Field(
        proto.DOUBLE,
        number=3,
    )


class MaintenancePolicy(proto.Message):
    r"""Maintenance policy configuration.

    Attributes:
        window (google.cloud.edgecontainer_v1.types.MaintenanceWindow):
            Specifies the maintenance window in which
            maintenance may be performed.
        maintenance_exclusions (MutableSequence[google.cloud.edgecontainer_v1.types.MaintenanceExclusionWindow]):
            Optional. Exclusions to automatic
            maintenance. Non-emergency maintenance should
            not occur in these windows. Each exclusion has a
            unique name and may be active or expired. The
            max number of maintenance exclusions allowed at
            a given time is 3.
    """

    window: "MaintenanceWindow" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="MaintenanceWindow",
    )
    maintenance_exclusions: MutableSequence["MaintenanceExclusionWindow"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="MaintenanceExclusionWindow",
        )
    )


class MaintenanceWindow(proto.Message):
    r"""Maintenance window configuration

    Attributes:
        recurring_window (google.cloud.edgecontainer_v1.types.RecurringTimeWindow):
            Configuration of a recurring maintenance
            window.
    """

    recurring_window: "RecurringTimeWindow" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="RecurringTimeWindow",
    )


class RecurringTimeWindow(proto.Message):
    r"""Represents an arbitrary window of time that recurs.

    Attributes:
        window (google.cloud.edgecontainer_v1.types.TimeWindow):
            The window of the first recurrence.
        recurrence (str):
            An RRULE
            (https://tools.ietf.org/html/rfc5545#section-3.8.5.3)
            for how this window recurs. They go on for the
            span of time between the start and end time.
    """

    window: "TimeWindow" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="TimeWindow",
    )
    recurrence: str = proto.Field(
        proto.STRING,
        number=2,
    )


class MaintenanceExclusionWindow(proto.Message):
    r"""Represents a maintenance exclusion window.

    Attributes:
        window (google.cloud.edgecontainer_v1.types.TimeWindow):
            Optional. The time window.
        id (str):
            Optional. A unique (per cluster) id for the
            window.
    """

    window: "TimeWindow" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="TimeWindow",
    )
    id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class TimeWindow(proto.Message):
    r"""Represents an arbitrary window of time.

    Attributes:
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            The time that the window first starts.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            The time that the window ends. The end time
            must take place after the start time.
    """

    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )


class ServerConfig(proto.Message):
    r"""Server configuration for supported versions and release
    channels.

    Attributes:
        channels (MutableMapping[str, google.cloud.edgecontainer_v1.types.ChannelConfig]):
            Output only. Mapping from release channel to
            channel config.
        versions (MutableSequence[google.cloud.edgecontainer_v1.types.Version]):
            Output only. Supported versions, e.g.: ["1.4.0", "1.5.0"].
        default_version (str):
            Output only. Default version, e.g.: "1.4.0".
    """

    channels: MutableMapping[str, "ChannelConfig"] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=1,
        message="ChannelConfig",
    )
    versions: MutableSequence["Version"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="Version",
    )
    default_version: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ChannelConfig(proto.Message):
    r"""Configuration for a release channel.

    Attributes:
        default_version (str):
            Output only. Default version for this release
            channel, e.g.: "1.4.0".
    """

    default_version: str = proto.Field(
        proto.STRING,
        number=1,
    )


class Version(proto.Message):
    r"""Version of a cluster.

    Attributes:
        name (str):
            Output only. Name of the version, e.g.:
            "1.4.0".
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
