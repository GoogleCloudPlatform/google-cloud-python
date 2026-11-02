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
import google.type.date_pb2 as date_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.gke_multicloud_v1.types import common_resources

__protobuf__ = proto.module(
    package="google.cloud.gkemulticloud.v1",
    manifest={
        "AwsCluster",
        "AwsControlPlane",
        "AwsServicesAuthentication",
        "AwsAuthorization",
        "AwsClusterUser",
        "AwsClusterGroup",
        "AwsDatabaseEncryption",
        "AwsVolumeTemplate",
        "AwsClusterNetworking",
        "AwsNodePool",
        "UpdateSettings",
        "SurgeSettings",
        "AwsNodeManagement",
        "AwsNodeConfig",
        "AwsNodePoolAutoscaling",
        "AwsOpenIdConfig",
        "AwsJsonWebKeys",
        "AwsServerConfig",
        "AwsK8sVersionInfo",
        "AwsSshConfig",
        "AwsProxyConfig",
        "AwsConfigEncryption",
        "AwsInstancePlacement",
        "AwsAutoscalingGroupMetricsCollection",
        "SpotConfig",
        "AwsClusterError",
        "AwsNodePoolError",
    },
)


class AwsCluster(proto.Message):
    r"""An Anthos cluster running on AWS.

    Attributes:
        name (str):
            The name of this resource.

            Cluster names are formatted as
            ``projects/<project-number>/locations/<region>/awsClusters/<cluster-id>``.

            See `Resource
            Names <https://cloud.google.com/apis/design/resource_names>`__
            for more details on Google Cloud Platform resource names.
        description (str):
            Optional. A human readable description of
            this cluster. Cannot be longer than 255 UTF-8
            encoded bytes.
        networking (google.cloud.gke_multicloud_v1.types.AwsClusterNetworking):
            Required. Cluster-wide networking
            configuration.
        aws_region (str):
            Required. The AWS region where the cluster runs.

            Each Google Cloud region supports a subset of nearby AWS
            regions. You can call
            [GetAwsServerConfig][google.cloud.gkemulticloud.v1.AwsClusters.GetAwsServerConfig]
            to list all supported AWS regions within a given Google
            Cloud region.
        control_plane (google.cloud.gke_multicloud_v1.types.AwsControlPlane):
            Required. Configuration related to the
            cluster control plane.
        authorization (google.cloud.gke_multicloud_v1.types.AwsAuthorization):
            Required. Configuration related to the
            cluster RBAC settings.
        state (google.cloud.gke_multicloud_v1.types.AwsCluster.State):
            Output only. The current state of the
            cluster.
        endpoint (str):
            Output only. The endpoint of the cluster's
            API server.
        uid (str):
            Output only. A globally unique identifier for
            the cluster.
        reconciling (bool):
            Output only. If set, there are currently
            changes in flight to the cluster.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which this cluster
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which this cluster
            was last updated.
        etag (str):
            Allows clients to perform consistent
            read-modify-writes through optimistic
            concurrency control.

            Can be sent on update and delete requests to
            ensure the client has an up-to-date value before
            proceeding.
        annotations (MutableMapping[str, str]):
            Optional. Annotations on the cluster.

            This field has the same restrictions as Kubernetes
            annotations. The total size of all keys and values combined
            is limited to 256k. Key can have 2 segments: prefix
            (optional) and name (required), separated by a slash (/).
            Prefix must be a DNS subdomain. Name must be 63 characters
            or less, begin and end with alphanumerics, with dashes (-),
            underscores (\_), dots (.), and alphanumerics between.
        workload_identity_config (google.cloud.gke_multicloud_v1.types.WorkloadIdentityConfig):
            Output only. Workload Identity settings.
        cluster_ca_certificate (str):
            Output only. PEM encoded x509 certificate of
            the cluster root of trust.
        fleet (google.cloud.gke_multicloud_v1.types.Fleet):
            Required. Fleet configuration.
        logging_config (google.cloud.gke_multicloud_v1.types.LoggingConfig):
            Optional. Logging configuration for this
            cluster.
        errors (MutableSequence[google.cloud.gke_multicloud_v1.types.AwsClusterError]):
            Output only. A set of errors found in the
            cluster.
        monitoring_config (google.cloud.gke_multicloud_v1.types.MonitoringConfig):
            Optional. Monitoring configuration for this
            cluster.
        binary_authorization (google.cloud.gke_multicloud_v1.types.BinaryAuthorization):
            Optional. Binary Authorization configuration
            for this cluster.
    """

    class State(proto.Enum):
        r"""The lifecycle state of the cluster.

        Values:
            STATE_UNSPECIFIED (0):
                Not set.
            PROVISIONING (1):
                The PROVISIONING state indicates the cluster
                is being created.
            RUNNING (2):
                The RUNNING state indicates the cluster has
                been created and is fully usable.
            RECONCILING (3):
                The RECONCILING state indicates that some
                work is actively being done on the cluster, such
                as upgrading the control plane replicas.
            STOPPING (4):
                The STOPPING state indicates the cluster is
                being deleted.
            ERROR (5):
                The ERROR state indicates the cluster is in a
                broken unrecoverable state.
            DEGRADED (6):
                The DEGRADED state indicates the cluster
                requires user action to restore full
                functionality.
        """

        STATE_UNSPECIFIED = 0
        PROVISIONING = 1
        RUNNING = 2
        RECONCILING = 3
        STOPPING = 4
        ERROR = 5
        DEGRADED = 6

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    networking: "AwsClusterNetworking" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="AwsClusterNetworking",
    )
    aws_region: str = proto.Field(
        proto.STRING,
        number=4,
    )
    control_plane: "AwsControlPlane" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="AwsControlPlane",
    )
    authorization: "AwsAuthorization" = proto.Field(
        proto.MESSAGE,
        number=15,
        message="AwsAuthorization",
    )
    state: State = proto.Field(
        proto.ENUM,
        number=7,
        enum=State,
    )
    endpoint: str = proto.Field(
        proto.STRING,
        number=8,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=9,
    )
    reconciling: bool = proto.Field(
        proto.BOOL,
        number=10,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=11,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=12,
        message=timestamp_pb2.Timestamp,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=13,
    )
    annotations: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=14,
    )
    workload_identity_config: common_resources.WorkloadIdentityConfig = proto.Field(
        proto.MESSAGE,
        number=16,
        message=common_resources.WorkloadIdentityConfig,
    )
    cluster_ca_certificate: str = proto.Field(
        proto.STRING,
        number=17,
    )
    fleet: common_resources.Fleet = proto.Field(
        proto.MESSAGE,
        number=18,
        message=common_resources.Fleet,
    )
    logging_config: common_resources.LoggingConfig = proto.Field(
        proto.MESSAGE,
        number=19,
        message=common_resources.LoggingConfig,
    )
    errors: MutableSequence["AwsClusterError"] = proto.RepeatedField(
        proto.MESSAGE,
        number=20,
        message="AwsClusterError",
    )
    monitoring_config: common_resources.MonitoringConfig = proto.Field(
        proto.MESSAGE,
        number=21,
        message=common_resources.MonitoringConfig,
    )
    binary_authorization: common_resources.BinaryAuthorization = proto.Field(
        proto.MESSAGE,
        number=22,
        message=common_resources.BinaryAuthorization,
    )


class AwsControlPlane(proto.Message):
    r"""ControlPlane defines common parameters between control plane
    nodes.

    Attributes:
        version (str):
            Required. The Kubernetes version to run on control plane
            replicas (e.g. ``1.19.10-gke.1000``).

            You can list all supported versions on a given Google Cloud
            region by calling
            [GetAwsServerConfig][google.cloud.gkemulticloud.v1.AwsClusters.GetAwsServerConfig].
        instance_type (str):
            Optional. The AWS instance type.

            When unspecified, it uses a default based on the
            cluster's version.
        ssh_config (google.cloud.gke_multicloud_v1.types.AwsSshConfig):
            Optional. SSH configuration for how to access
            the underlying control plane machines.
        subnet_ids (MutableSequence[str]):
            Required. The list of subnets where control
            plane replicas will run. A replica will be
            provisioned on each subnet and up to three
            values can be provided.
            Each subnet must be in a different AWS
            Availability Zone (AZ).
        security_group_ids (MutableSequence[str]):
            Optional. The IDs of additional security
            groups to add to control plane replicas. The
            Anthos Multi-Cloud API will automatically create
            and manage security groups with the minimum
            rules needed for a functioning cluster.
        iam_instance_profile (str):
            Required. The name or ARN of the AWS IAM
            instance profile to assign to each control plane
            replica.
        root_volume (google.cloud.gke_multicloud_v1.types.AwsVolumeTemplate):
            Optional. Configuration related to the root
            volume provisioned for each control plane
            replica.

            Volumes will be provisioned in the availability
            zone associated with the corresponding subnet.

            When unspecified, it defaults to 32 GiB with the
            GP2 volume type.
        main_volume (google.cloud.gke_multicloud_v1.types.AwsVolumeTemplate):
            Optional. Configuration related to the main
            volume provisioned for each control plane
            replica. The main volume is in charge of storing
            all of the cluster's etcd state.

            Volumes will be provisioned in the availability
            zone associated with the corresponding subnet.

            When unspecified, it defaults to 8 GiB with the
            GP2 volume type.
        database_encryption (google.cloud.gke_multicloud_v1.types.AwsDatabaseEncryption):
            Required. The ARN of the AWS KMS key used to
            encrypt cluster secrets.
        tags (MutableMapping[str, str]):
            Optional. A set of AWS resource tags to propagate to all
            underlying managed AWS resources.

            Specify at most 50 pairs containing alphanumerics, spaces,
            and symbols (.+-=\_:@/). Keys can be up to 127 Unicode
            characters. Values can be up to 255 Unicode characters.
        aws_services_authentication (google.cloud.gke_multicloud_v1.types.AwsServicesAuthentication):
            Required. Authentication configuration for
            management of AWS resources.
        proxy_config (google.cloud.gke_multicloud_v1.types.AwsProxyConfig):
            Optional. Proxy configuration for outbound
            HTTP(S) traffic.
        config_encryption (google.cloud.gke_multicloud_v1.types.AwsConfigEncryption):
            Required. Config encryption for user data.
        instance_placement (google.cloud.gke_multicloud_v1.types.AwsInstancePlacement):
            Optional. The placement to use on control
            plane instances. When unspecified, the VPC's
            default tenancy will be used.
    """

    version: str = proto.Field(
        proto.STRING,
        number=1,
    )
    instance_type: str = proto.Field(
        proto.STRING,
        number=2,
    )
    ssh_config: "AwsSshConfig" = proto.Field(
        proto.MESSAGE,
        number=14,
        message="AwsSshConfig",
    )
    subnet_ids: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    security_group_ids: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )
    iam_instance_profile: str = proto.Field(
        proto.STRING,
        number=7,
    )
    root_volume: "AwsVolumeTemplate" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="AwsVolumeTemplate",
    )
    main_volume: "AwsVolumeTemplate" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="AwsVolumeTemplate",
    )
    database_encryption: "AwsDatabaseEncryption" = proto.Field(
        proto.MESSAGE,
        number=10,
        message="AwsDatabaseEncryption",
    )
    tags: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=11,
    )
    aws_services_authentication: "AwsServicesAuthentication" = proto.Field(
        proto.MESSAGE,
        number=12,
        message="AwsServicesAuthentication",
    )
    proxy_config: "AwsProxyConfig" = proto.Field(
        proto.MESSAGE,
        number=16,
        message="AwsProxyConfig",
    )
    config_encryption: "AwsConfigEncryption" = proto.Field(
        proto.MESSAGE,
        number=17,
        message="AwsConfigEncryption",
    )
    instance_placement: "AwsInstancePlacement" = proto.Field(
        proto.MESSAGE,
        number=18,
        message="AwsInstancePlacement",
    )


class AwsServicesAuthentication(proto.Message):
    r"""Authentication configuration for the management of AWS
    resources.

    Attributes:
        role_arn (str):
            Required. The Amazon Resource Name (ARN) of
            the role that the Anthos Multi-Cloud API will
            assume when managing AWS resources on your
            account.
        role_session_name (str):
            Optional. An identifier for the assumed role session.

            When unspecified, it defaults to
            ``multicloud-service-agent``.
    """

    role_arn: str = proto.Field(
        proto.STRING,
        number=1,
    )
    role_session_name: str = proto.Field(
        proto.STRING,
        number=2,
    )


class AwsAuthorization(proto.Message):
    r"""Configuration related to the cluster RBAC settings.

    Attributes:
        admin_users (MutableSequence[google.cloud.gke_multicloud_v1.types.AwsClusterUser]):
            Optional. Users that can perform operations as a cluster
            admin. A managed ClusterRoleBinding will be created to grant
            the ``cluster-admin`` ClusterRole to the users. Up to ten
            admin users can be provided.

            For more info on RBAC, see
            https://kubernetes.io/docs/reference/access-authn-authz/rbac/#user-facing-roles
        admin_groups (MutableSequence[google.cloud.gke_multicloud_v1.types.AwsClusterGroup]):
            Optional. Groups of users that can perform operations as a
            cluster admin. A managed ClusterRoleBinding will be created
            to grant the ``cluster-admin`` ClusterRole to the groups. Up
            to ten admin groups can be provided.

            For more info on RBAC, see
            https://kubernetes.io/docs/reference/access-authn-authz/rbac/#user-facing-roles
    """

    admin_users: MutableSequence["AwsClusterUser"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="AwsClusterUser",
    )
    admin_groups: MutableSequence["AwsClusterGroup"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="AwsClusterGroup",
    )


class AwsClusterUser(proto.Message):
    r"""Identities of a user-type subject for AWS clusters.

    Attributes:
        username (str):
            Required. The name of the user, e.g.
            ``my-gcp-id@gmail.com``.
    """

    username: str = proto.Field(
        proto.STRING,
        number=1,
    )


class AwsClusterGroup(proto.Message):
    r"""Identities of a group-type subject for AWS clusters.

    Attributes:
        group (str):
            Required. The name of the group, e.g.
            ``my-group@domain.com``.
    """

    group: str = proto.Field(
        proto.STRING,
        number=1,
    )


class AwsDatabaseEncryption(proto.Message):
    r"""Configuration related to application-layer secrets
    encryption.

    Attributes:
        kms_key_arn (str):
            Required. The ARN of the AWS KMS key used to
            encrypt cluster secrets.
    """

    kms_key_arn: str = proto.Field(
        proto.STRING,
        number=1,
    )


class AwsVolumeTemplate(proto.Message):
    r"""Configuration template for AWS EBS volumes.

    Attributes:
        size_gib (int):
            Optional. The size of the volume, in GiBs.

            When unspecified, a default value is provided.
            See the specific reference in the parent
            resource.
        volume_type (google.cloud.gke_multicloud_v1.types.AwsVolumeTemplate.VolumeType):
            Optional. Type of the EBS volume.

            When unspecified, it defaults to GP2 volume.
        iops (int):
            Optional. The number of I/O operations per
            second (IOPS) to provision for GP3 volume.
        throughput (int):
            Optional. The throughput that the volume supports, in MiB/s.
            Only valid if volume_type is GP3.

            If the volume_type is GP3 and this is not specified, it
            defaults to 125.
        kms_key_arn (str):
            Optional. The Amazon Resource Name (ARN) of
            the Customer Managed Key (CMK) used to encrypt
            AWS EBS volumes.

            If not specified, the default Amazon managed key
            associated to the AWS region where this cluster
            runs will be used.
    """

    class VolumeType(proto.Enum):
        r"""Types of supported EBS volumes. We currently only support GP2
        or GP3 volumes.
        See
        https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html
        for more information.

        Values:
            VOLUME_TYPE_UNSPECIFIED (0):
                Not set.
            GP2 (1):
                GP2 (General Purpose SSD volume type).
            GP3 (2):
                GP3 (General Purpose SSD volume type).
        """

        VOLUME_TYPE_UNSPECIFIED = 0
        GP2 = 1
        GP3 = 2

    size_gib: int = proto.Field(
        proto.INT32,
        number=1,
    )
    volume_type: VolumeType = proto.Field(
        proto.ENUM,
        number=2,
        enum=VolumeType,
    )
    iops: int = proto.Field(
        proto.INT32,
        number=3,
    )
    throughput: int = proto.Field(
        proto.INT32,
        number=5,
    )
    kms_key_arn: str = proto.Field(
        proto.STRING,
        number=4,
    )


class AwsClusterNetworking(proto.Message):
    r"""ClusterNetworking defines cluster-wide networking
    configuration.
    Anthos clusters on AWS run on a single VPC. This includes
    control plane replicas and node pool nodes.

    Attributes:
        vpc_id (str):
            Required. The VPC associated with the
            cluster. All component clusters (i.e. control
            plane and node pools) run on a single VPC.

            This field cannot be changed after creation.
        pod_address_cidr_blocks (MutableSequence[str]):
            Required. All pods in the cluster are
            assigned an IPv4 address from these ranges. Only
            a single range is supported. This field cannot
            be changed after creation.
        service_address_cidr_blocks (MutableSequence[str]):
            Required. All services in the cluster are
            assigned an IPv4 address from these ranges. Only
            a single range is supported. This field cannot
            be changed after creation.
        per_node_pool_sg_rules_disabled (bool):
            Optional. Disable the per node pool subnet
            security group rules on the control plane
            security group. When set to true, you must also
            provide one or more security groups that ensure
            node pools are able to send requests to the
            control plane on TCP/443 and TCP/8132. Failure
            to do so may result in unavailable node pools.
    """

    vpc_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    pod_address_cidr_blocks: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    service_address_cidr_blocks: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    per_node_pool_sg_rules_disabled: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class AwsNodePool(proto.Message):
    r"""An Anthos node pool running on AWS.

    Attributes:
        name (str):
            The name of this resource.

            Node pool names are formatted as
            ``projects/<project-number>/locations/<region>/awsClusters/<cluster-id>/awsNodePools/<node-pool-id>``.

            For more details on Google Cloud resource names, see
            `Resource
            Names <https://cloud.google.com/apis/design/resource_names>`__
        version (str):
            Required. The Kubernetes version to run on this node pool
            (e.g. ``1.19.10-gke.1000``).

            You can list all supported versions on a given Google Cloud
            region by calling
            [GetAwsServerConfig][google.cloud.gkemulticloud.v1.AwsClusters.GetAwsServerConfig].
        config (google.cloud.gke_multicloud_v1.types.AwsNodeConfig):
            Required. The configuration of the node pool.
        autoscaling (google.cloud.gke_multicloud_v1.types.AwsNodePoolAutoscaling):
            Required. Autoscaler configuration for this
            node pool.
        subnet_id (str):
            Required. The subnet where the node pool node
            run.
        state (google.cloud.gke_multicloud_v1.types.AwsNodePool.State):
            Output only. The lifecycle state of the node
            pool.
        uid (str):
            Output only. A globally unique identifier for
            the node pool.
        reconciling (bool):
            Output only. If set, there are currently
            changes in flight to the node pool.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which this node pool
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which this node pool
            was last updated.
        etag (str):
            Allows clients to perform consistent
            read-modify-writes through optimistic
            concurrency control.

            Can be sent on update and delete requests to
            ensure the client has an up-to-date value before
            proceeding.
        annotations (MutableMapping[str, str]):
            Optional. Annotations on the node pool.

            This field has the same restrictions as Kubernetes
            annotations. The total size of all keys and values combined
            is limited to 256k. Key can have 2 segments: prefix
            (optional) and name (required), separated by a slash (/).
            Prefix must be a DNS subdomain. Name must be 63 characters
            or less, begin and end with alphanumerics, with dashes (-),
            underscores (\_), dots (.), and alphanumerics between.
        max_pods_constraint (google.cloud.gke_multicloud_v1.types.MaxPodsConstraint):
            Required. The constraint on the maximum
            number of pods that can be run simultaneously on
            a node in the node pool.
        errors (MutableSequence[google.cloud.gke_multicloud_v1.types.AwsNodePoolError]):
            Output only. A set of errors found in the
            node pool.
        management (google.cloud.gke_multicloud_v1.types.AwsNodeManagement):
            Optional. The Management configuration for
            this node pool.
        kubelet_config (google.cloud.gke_multicloud_v1.types.NodeKubeletConfig):
            Optional. Node kubelet configs.
        update_settings (google.cloud.gke_multicloud_v1.types.UpdateSettings):
            Optional. Update settings control the speed
            and disruption of the update.
    """

    class State(proto.Enum):
        r"""The lifecycle state of the node pool.

        Values:
            STATE_UNSPECIFIED (0):
                Not set.
            PROVISIONING (1):
                The PROVISIONING state indicates the node
                pool is being created.
            RUNNING (2):
                The RUNNING state indicates the node pool has
                been created and is fully usable.
            RECONCILING (3):
                The RECONCILING state indicates that the node
                pool is being reconciled.
            STOPPING (4):
                The STOPPING state indicates the node pool is
                being deleted.
            ERROR (5):
                The ERROR state indicates the node pool is in
                a broken unrecoverable state.
            DEGRADED (6):
                The DEGRADED state indicates the node pool
                requires user action to restore full
                functionality.
        """

        STATE_UNSPECIFIED = 0
        PROVISIONING = 1
        RUNNING = 2
        RECONCILING = 3
        STOPPING = 4
        ERROR = 5
        DEGRADED = 6

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    version: str = proto.Field(
        proto.STRING,
        number=3,
    )
    config: "AwsNodeConfig" = proto.Field(
        proto.MESSAGE,
        number=28,
        message="AwsNodeConfig",
    )
    autoscaling: "AwsNodePoolAutoscaling" = proto.Field(
        proto.MESSAGE,
        number=25,
        message="AwsNodePoolAutoscaling",
    )
    subnet_id: str = proto.Field(
        proto.STRING,
        number=6,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=16,
        enum=State,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=17,
    )
    reconciling: bool = proto.Field(
        proto.BOOL,
        number=18,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=19,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=20,
        message=timestamp_pb2.Timestamp,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=21,
    )
    annotations: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=22,
    )
    max_pods_constraint: common_resources.MaxPodsConstraint = proto.Field(
        proto.MESSAGE,
        number=27,
        message=common_resources.MaxPodsConstraint,
    )
    errors: MutableSequence["AwsNodePoolError"] = proto.RepeatedField(
        proto.MESSAGE,
        number=29,
        message="AwsNodePoolError",
    )
    management: "AwsNodeManagement" = proto.Field(
        proto.MESSAGE,
        number=30,
        message="AwsNodeManagement",
    )
    kubelet_config: common_resources.NodeKubeletConfig = proto.Field(
        proto.MESSAGE,
        number=31,
        message=common_resources.NodeKubeletConfig,
    )
    update_settings: "UpdateSettings" = proto.Field(
        proto.MESSAGE,
        number=32,
        message="UpdateSettings",
    )


class UpdateSettings(proto.Message):
    r"""UpdateSettings control the level of parallelism and the level of
    disruption caused during the update of a node pool.

    These settings are applicable when the node pool update requires
    replacing the existing node pool nodes with the updated ones.

    UpdateSettings are optional. When UpdateSettings are not specified
    during the node pool creation, a default is chosen based on the
    parent cluster's version. For clusters with minor version 1.27 and
    later, a default surge_settings configuration with max_surge = 1 and
    max_unavailable = 0 is used. For clusters with older versions, node
    pool updates use the traditional rolling update mechanism of
    updating one node at a time in a "terminate before create" fashion
    and update_settings is not applicable.

    Set the surge_settings parameter to use the Surge Update mechanism
    for the rolling update of node pool nodes.

    1. max_surge controls the number of additional nodes that can be
       created beyond the current size of the node pool temporarily for
       the time of the update to increase the number of available nodes.
    2. max_unavailable controls the number of nodes that can be
       simultaneously unavailable during the update.
    3. (max_surge + max_unavailable) determines the level of parallelism
       (i.e., the number of nodes being updated at the same time).

    Attributes:
        surge_settings (google.cloud.gke_multicloud_v1.types.SurgeSettings):
            Optional. Settings for surge update.
    """

    surge_settings: "SurgeSettings" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="SurgeSettings",
    )


class SurgeSettings(proto.Message):
    r"""SurgeSettings contains the parameters for Surge update.

    Attributes:
        max_surge (int):
            Optional. The maximum number of nodes that
            can be created beyond the current size of the
            node pool during the update process.
        max_unavailable (int):
            Optional. The maximum number of nodes that
            can be simultaneously unavailable during the
            update process. A node is considered unavailable
            if its status is not Ready.
    """

    max_surge: int = proto.Field(
        proto.INT32,
        number=1,
    )
    max_unavailable: int = proto.Field(
        proto.INT32,
        number=2,
    )


class AwsNodeManagement(proto.Message):
    r"""AwsNodeManagement defines the set of node management features
    turned on for an AWS node pool.

    Attributes:
        auto_repair (bool):
            Optional. Whether or not the nodes will be
            automatically repaired. When set to true, the
            nodes in this node pool will be monitored and if
            they fail health checks consistently over a
            period of time, an automatic repair action will
            be triggered to replace them with new nodes.
    """

    auto_repair: bool = proto.Field(
        proto.BOOL,
        number=1,
    )


class AwsNodeConfig(proto.Message):
    r"""Parameters that describe the nodes in a cluster.

    Attributes:
        instance_type (str):
            Optional. The EC2 instance type when creating
            on-Demand instances.
            If unspecified during node pool creation, a
            default will be chosen based on the node pool
            version, and assigned to this field.
        root_volume (google.cloud.gke_multicloud_v1.types.AwsVolumeTemplate):
            Optional. Template for the root volume
            provisioned for node pool nodes. Volumes will be
            provisioned in the availability zone assigned to
            the node pool subnet.

            When unspecified, it defaults to 32 GiB with the
            GP2 volume type.
        taints (MutableSequence[google.cloud.gke_multicloud_v1.types.NodeTaint]):
            Optional. The initial taints assigned to
            nodes of this node pool.
        labels (MutableMapping[str, str]):
            Optional. The initial labels assigned to
            nodes of this node pool. An object containing a
            list of "key": value pairs. Example: { "name":
            "wrench", "mass": "1.3kg", "count": "3" }.
        tags (MutableMapping[str, str]):
            Optional. Key/value metadata to assign to each underlying
            AWS resource. Specify at most 50 pairs containing
            alphanumerics, spaces, and symbols (.+-=\_:@/). Keys can be
            up to 127 Unicode characters. Values can be up to 255
            Unicode characters.
        iam_instance_profile (str):
            Required. The name or ARN of the AWS IAM
            instance profile to assign to nodes in the pool.
        image_type (str):
            Optional. The OS image type to use on node pool instances.
            Can be unspecified, or have a value of ``ubuntu``.

            When unspecified, it defaults to ``ubuntu``.
        ssh_config (google.cloud.gke_multicloud_v1.types.AwsSshConfig):
            Optional. The SSH configuration.
        security_group_ids (MutableSequence[str]):
            Optional. The IDs of additional security
            groups to add to nodes in this pool. The manager
            will automatically create security groups with
            minimum rules needed for a functioning cluster.
        proxy_config (google.cloud.gke_multicloud_v1.types.AwsProxyConfig):
            Optional. Proxy configuration for outbound
            HTTP(S) traffic.
        config_encryption (google.cloud.gke_multicloud_v1.types.AwsConfigEncryption):
            Required. Config encryption for user data.
        instance_placement (google.cloud.gke_multicloud_v1.types.AwsInstancePlacement):
            Optional. Placement related info for this
            node. When unspecified, the VPC's default
            tenancy will be used.
        autoscaling_metrics_collection (google.cloud.gke_multicloud_v1.types.AwsAutoscalingGroupMetricsCollection):
            Optional. Configuration related to CloudWatch
            metrics collection on the Auto Scaling group of
            the node pool.

            When unspecified, metrics collection is
            disabled.
        spot_config (google.cloud.gke_multicloud_v1.types.SpotConfig):
            Optional. Configuration for provisioning EC2 Spot instances

            When specified, the node pool will provision Spot instances
            from the set of spot_config.instance_types. This field is
            mutually exclusive with ``instance_type``.
    """

    instance_type: str = proto.Field(
        proto.STRING,
        number=1,
    )
    root_volume: "AwsVolumeTemplate" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="AwsVolumeTemplate",
    )
    taints: MutableSequence[common_resources.NodeTaint] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=common_resources.NodeTaint,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    tags: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )
    iam_instance_profile: str = proto.Field(
        proto.STRING,
        number=6,
    )
    image_type: str = proto.Field(
        proto.STRING,
        number=11,
    )
    ssh_config: "AwsSshConfig" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="AwsSshConfig",
    )
    security_group_ids: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=10,
    )
    proxy_config: "AwsProxyConfig" = proto.Field(
        proto.MESSAGE,
        number=12,
        message="AwsProxyConfig",
    )
    config_encryption: "AwsConfigEncryption" = proto.Field(
        proto.MESSAGE,
        number=13,
        message="AwsConfigEncryption",
    )
    instance_placement: "AwsInstancePlacement" = proto.Field(
        proto.MESSAGE,
        number=14,
        message="AwsInstancePlacement",
    )
    autoscaling_metrics_collection: "AwsAutoscalingGroupMetricsCollection" = (
        proto.Field(
            proto.MESSAGE,
            number=15,
            message="AwsAutoscalingGroupMetricsCollection",
        )
    )
    spot_config: "SpotConfig" = proto.Field(
        proto.MESSAGE,
        number=16,
        message="SpotConfig",
    )


class AwsNodePoolAutoscaling(proto.Message):
    r"""AwsNodePoolAutoscaling contains information required by
    cluster autoscaler to adjust the size of the node pool to the
    current cluster usage.

    Attributes:
        min_node_count (int):
            Required. Minimum number of nodes in the node pool. Must be
            greater than or equal to 1 and less than or equal to
            max_node_count.
        max_node_count (int):
            Required. Maximum number of nodes in the node pool. Must be
            greater than or equal to min_node_count and less than or
            equal to 50.
    """

    min_node_count: int = proto.Field(
        proto.INT32,
        number=1,
    )
    max_node_count: int = proto.Field(
        proto.INT32,
        number=2,
    )


class AwsOpenIdConfig(proto.Message):
    r"""AwsOpenIdConfig is an OIDC discovery document for the
    cluster. See the OpenID Connect Discovery 1.0 specification for
    details.

    Attributes:
        issuer (str):
            OIDC Issuer.
        jwks_uri (str):
            JSON Web Key uri.
        response_types_supported (MutableSequence[str]):
            Supported response types.
        subject_types_supported (MutableSequence[str]):
            Supported subject types.
        id_token_signing_alg_values_supported (MutableSequence[str]):
            supported ID Token signing Algorithms.
        claims_supported (MutableSequence[str]):
            Supported claims.
        grant_types (MutableSequence[str]):
            Supported grant types.
    """

    issuer: str = proto.Field(
        proto.STRING,
        number=1,
    )
    jwks_uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    response_types_supported: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    subject_types_supported: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    id_token_signing_alg_values_supported: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )
    claims_supported: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )
    grant_types: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=7,
    )


class AwsJsonWebKeys(proto.Message):
    r"""AwsJsonWebKeys is a valid JSON Web Key Set as specififed in
    RFC 7517.

    Attributes:
        keys (MutableSequence[google.cloud.gke_multicloud_v1.types.Jwk]):
            The public component of the keys used by the
            cluster to sign token requests.
    """

    keys: MutableSequence[common_resources.Jwk] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=common_resources.Jwk,
    )


class AwsServerConfig(proto.Message):
    r"""AwsServerConfig is the configuration of GKE cluster on AWS.

    Attributes:
        name (str):
            The resource name of the config.
        valid_versions (MutableSequence[google.cloud.gke_multicloud_v1.types.AwsK8sVersionInfo]):
            List of all released Kubernetes versions, including ones
            which are end of life and can no longer be used. Filter by
            the ``enabled`` property to limit to currently available
            versions. Valid versions supported for both create and
            update operations
        supported_aws_regions (MutableSequence[str]):
            The list of supported AWS regions.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    valid_versions: MutableSequence["AwsK8sVersionInfo"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="AwsK8sVersionInfo",
    )
    supported_aws_regions: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class AwsK8sVersionInfo(proto.Message):
    r"""Kubernetes version information of GKE cluster on AWS.

    Attributes:
        version (str):
            Kubernetes version name.
        enabled (bool):
            Optional. True if the version is available
            for cluster creation. If a version is enabled
            for creation, it can be used to create new
            clusters. Otherwise, cluster creation will fail.
            However, cluster upgrade operations may succeed,
            even if the version is not enabled.
        end_of_life (bool):
            Optional. True if this cluster version
            belongs to a minor version that has reached its
            end of life and is no longer in scope to receive
            security and bug fixes.
        end_of_life_date (google.type.date_pb2.Date):
            Optional. The estimated date (in Pacific Time) when this
            cluster version will reach its end of life. Or if this
            version is no longer supported (the ``end_of_life`` field is
            true), this is the actual date (in Pacific time) when the
            version reached its end of life.
        release_date (google.type.date_pb2.Date):
            Optional. The date (in Pacific Time) when the
            cluster version was released.
    """

    version: str = proto.Field(
        proto.STRING,
        number=1,
    )
    enabled: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    end_of_life: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    end_of_life_date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=5,
        message=date_pb2.Date,
    )
    release_date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=6,
        message=date_pb2.Date,
    )


class AwsSshConfig(proto.Message):
    r"""SSH configuration for AWS resources.

    Attributes:
        ec2_key_pair (str):
            Required. The name of the EC2 key pair used
            to login into cluster machines.
    """

    ec2_key_pair: str = proto.Field(
        proto.STRING,
        number=1,
    )


class AwsProxyConfig(proto.Message):
    r"""Details of a proxy config stored in AWS Secret Manager.

    Attributes:
        secret_arn (str):
            The ARN of the AWS Secret Manager secret that contains the
            HTTP(S) proxy configuration.

            The secret must be a JSON encoded proxy configuration as
            described in
            https://cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/use-a-proxy#create_a_proxy_configuration_file
        secret_version (str):
            The version string of the AWS Secret Manager
            secret that contains the HTTP(S) proxy
            configuration.
    """

    secret_arn: str = proto.Field(
        proto.STRING,
        number=1,
    )
    secret_version: str = proto.Field(
        proto.STRING,
        number=2,
    )


class AwsConfigEncryption(proto.Message):
    r"""Config encryption for user data.

    Attributes:
        kms_key_arn (str):
            Required. The ARN of the AWS KMS key used to
            encrypt user data.
    """

    kms_key_arn: str = proto.Field(
        proto.STRING,
        number=1,
    )


class AwsInstancePlacement(proto.Message):
    r"""Details of placement information for an instance. Limitations for
    using the ``host`` tenancy:

    - T3 instances that use the unlimited CPU credit option don't
      support host tenancy.

    Attributes:
        tenancy (google.cloud.gke_multicloud_v1.types.AwsInstancePlacement.Tenancy):
            Required. The tenancy for instance.
    """

    class Tenancy(proto.Enum):
        r"""Tenancy defines how EC2 instances are distributed across
        physical hardware.

        Values:
            TENANCY_UNSPECIFIED (0):
                Not set.
            DEFAULT (1):
                Use default VPC tenancy.
            DEDICATED (2):
                Run a dedicated instance.
            HOST (3):
                Launch this instance to a dedicated host.
        """

        TENANCY_UNSPECIFIED = 0
        DEFAULT = 1
        DEDICATED = 2
        HOST = 3

    tenancy: Tenancy = proto.Field(
        proto.ENUM,
        number=1,
        enum=Tenancy,
    )


class AwsAutoscalingGroupMetricsCollection(proto.Message):
    r"""Configuration related to CloudWatch metrics collection in an
    AWS Auto Scaling group.

    Attributes:
        granularity (str):
            Required. The frequency at which EC2 Auto
            Scaling sends aggregated data to AWS CloudWatch.
            The only valid value is "1Minute".
        metrics (MutableSequence[str]):
            Optional. The metrics to enable. For a list of valid
            metrics, see
            https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_EnableMetricsCollection.html.
            If you specify Granularity and don't specify any metrics,
            all metrics are enabled.
    """

    granularity: str = proto.Field(
        proto.STRING,
        number=1,
    )
    metrics: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class SpotConfig(proto.Message):
    r"""SpotConfig has configuration info for Spot node.

    Attributes:
        instance_types (MutableSequence[str]):
            Required. A list of instance types for
            creating spot node pool.
    """

    instance_types: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class AwsClusterError(proto.Message):
    r"""AwsClusterError describes errors found on AWS clusters.

    Attributes:
        message (str):
            Human-friendly description of the error.
    """

    message: str = proto.Field(
        proto.STRING,
        number=1,
    )


class AwsNodePoolError(proto.Message):
    r"""AwsNodePoolError describes errors found on AWS node pools.

    Attributes:
        message (str):
            Human-friendly description of the error.
    """

    message: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
