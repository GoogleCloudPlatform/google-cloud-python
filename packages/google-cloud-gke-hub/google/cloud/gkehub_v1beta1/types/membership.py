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
import google.rpc.status_pb2 as status_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.gkehub.v1beta1",
    manifest={
        "Membership",
        "MembershipEndpoint",
        "KubernetesResource",
        "ResourceOptions",
        "ResourceManifest",
        "GkeCluster",
        "OnPremCluster",
        "MultiCloudCluster",
        "EdgeCluster",
        "ApplianceCluster",
        "KubernetesMetadata",
        "Authority",
        "MonitoringConfig",
        "MembershipState",
        "ListMembershipsRequest",
        "ListMembershipsResponse",
        "GetMembershipRequest",
        "CreateMembershipRequest",
        "DeleteMembershipRequest",
        "UpdateMembershipRequest",
        "GenerateConnectManifestRequest",
        "GenerateConnectManifestResponse",
        "ConnectAgentResource",
        "TypeMeta",
        "ConnectAgent",
        "ValidateExclusivityRequest",
        "ValidateExclusivityResponse",
        "GenerateExclusivityManifestRequest",
        "GenerateExclusivityManifestResponse",
        "OperationMetadata",
    },
)


class Membership(proto.Message):
    r"""Membership contains information about a member cluster.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Output only. The full, unique name of this Membership
            resource in the format
            ``projects/*/locations/*/memberships/{membership_id}``, set
            during creation.

            ``membership_id`` must be a valid RFC 1123 compliant DNS
            label:

            1. At most 63 characters in length
            2. It must consist of lower case alphanumeric characters or
               ``-``
            3. It must start and end with an alphanumeric character

            Which can be expressed as the regex:
            ``[a-z0-9]([-a-z0-9]*[a-z0-9])?``, with a maximum length of
            63 characters.
        labels (MutableMapping[str, str]):
            Optional. GCP labels for this membership.
        description (str):
            Optional. Description of this membership, limited to 63
            characters. Must match the regex:
            ``[a-zA-Z0-9][a-zA-Z0-9_\-\.\ ]*``
        endpoint (google.cloud.gkehub_v1beta1.types.MembershipEndpoint):
            Optional. Endpoint information to reach this
            member.

            This field is a member of `oneof`_ ``type``.
        state (google.cloud.gkehub_v1beta1.types.MembershipState):
            Output only. State of the Membership
            resource.
        authority (google.cloud.gkehub_v1beta1.types.Authority):
            Optional. How to identify workloads from this
            Membership. See the documentation on Workload
            Identity for more details:

            https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. When the Membership was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. When the Membership was last
            updated.
        delete_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. When the Membership was deleted.
        external_id (str):
            Optional. An externally-generated and managed ID for this
            Membership. This ID may be modified after creation, but this
            is not recommended. For GKE clusters, external_id is managed
            by the Hub API and updates will be ignored.

            The ID must match the regex:
            ``[a-zA-Z0-9][a-zA-Z0-9_\-\.]*``

            If this Membership represents a Kubernetes cluster, this
            value should be set to the UID of the ``kube-system``
            namespace object.
        last_connection_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. For clusters using Connect, the
            timestamp of the most recent connection
            established with Google Cloud. This time is
            updated every several minutes, not continuously.
            For clusters that do not use GKE Connect, or
            that have never connected successfully, this
            field will be unset.
        unique_id (str):
            Output only. Google-generated UUID for this resource. This
            is unique across all Membership resources. If a Membership
            resource is deleted and another resource with the same name
            is created, it gets a different unique_id.
        infrastructure_type (google.cloud.gkehub_v1beta1.types.Membership.InfrastructureType):
            Optional. The infrastructure type this
            Membership is running on.
        monitoring_config (google.cloud.gkehub_v1beta1.types.MonitoringConfig):
            Optional. The monitoring config information
            for this membership.
    """

    class InfrastructureType(proto.Enum):
        r"""Specifies the infrastructure type of a Membership.
        Infrastructure type is used by Hub to control
        infrastructure-specific behavior, including pricing.

        Each GKE distribution (on-GCP, on-Prem, on-X,...) will set this
        field automatically, but Attached Clusters customers should
        specify a type during registration.

        Values:
            INFRASTRUCTURE_TYPE_UNSPECIFIED (0):
                No type was specified. Some Hub functionality
                may require a type be specified, and will not
                support Memberships with this value.
            ON_PREM (1):
                Private infrastructure that is owned or
                operated by customer. This includes GKE
                distributions such as GKE-OnPrem and
                GKE-OnBareMetal.
            MULTI_CLOUD (2):
                Public cloud infrastructure.
        """

        INFRASTRUCTURE_TYPE_UNSPECIFIED = 0
        ON_PREM = 1
        MULTI_CLOUD = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    endpoint: "MembershipEndpoint" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="type",
        message="MembershipEndpoint",
    )
    state: "MembershipState" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="MembershipState",
    )
    authority: "Authority" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="Authority",
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    delete_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    external_id: str = proto.Field(
        proto.STRING,
        number=10,
    )
    last_connection_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=11,
        message=timestamp_pb2.Timestamp,
    )
    unique_id: str = proto.Field(
        proto.STRING,
        number=12,
    )
    infrastructure_type: InfrastructureType = proto.Field(
        proto.ENUM,
        number=13,
        enum=InfrastructureType,
    )
    monitoring_config: "MonitoringConfig" = proto.Field(
        proto.MESSAGE,
        number=14,
        message="MonitoringConfig",
    )


class MembershipEndpoint(proto.Message):
    r"""MembershipEndpoint contains information needed to contact a
    Kubernetes API, endpoint and any additional Kubernetes metadata.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        gke_cluster (google.cloud.gkehub_v1beta1.types.GkeCluster):
            Optional. Specific information for a
            GKE-on-GCP cluster.

            This field is a member of `oneof`_ ``type``.
        on_prem_cluster (google.cloud.gkehub_v1beta1.types.OnPremCluster):
            Optional. Specific information for a GKE
            On-Prem cluster. An onprem user-cluster who has
            no resourceLink is not allowed to use this
            field, it should have a nil "type" instead.

            This field is a member of `oneof`_ ``type``.
        multi_cloud_cluster (google.cloud.gkehub_v1beta1.types.MultiCloudCluster):
            Optional. Specific information for a GKE
            Multi-Cloud cluster.

            This field is a member of `oneof`_ ``type``.
        edge_cluster (google.cloud.gkehub_v1beta1.types.EdgeCluster):
            Optional. Specific information for a Google
            Edge cluster.

            This field is a member of `oneof`_ ``type``.
        appliance_cluster (google.cloud.gkehub_v1beta1.types.ApplianceCluster):
            Optional. Specific information for a GDC Edge
            Appliance cluster.

            This field is a member of `oneof`_ ``type``.
        kubernetes_metadata (google.cloud.gkehub_v1beta1.types.KubernetesMetadata):
            Output only. Useful Kubernetes-specific
            metadata.
        kubernetes_resource (google.cloud.gkehub_v1beta1.types.KubernetesResource):
            Optional. The in-cluster Kubernetes Resources that should be
            applied for a correctly registered cluster, in the steady
            state. These resources:

            - Ensure that the cluster is exclusively registered to one
              and only one Hub Membership.
            - Propagate Workload Pool Information available in the
              Membership Authority field.
            - Ensure proper initial configuration of default Hub
              Features.
    """

    gke_cluster: "GkeCluster" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="type",
        message="GkeCluster",
    )
    on_prem_cluster: "OnPremCluster" = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="type",
        message="OnPremCluster",
    )
    multi_cloud_cluster: "MultiCloudCluster" = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="type",
        message="MultiCloudCluster",
    )
    edge_cluster: "EdgeCluster" = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="type",
        message="EdgeCluster",
    )
    appliance_cluster: "ApplianceCluster" = proto.Field(
        proto.MESSAGE,
        number=10,
        oneof="type",
        message="ApplianceCluster",
    )
    kubernetes_metadata: "KubernetesMetadata" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="KubernetesMetadata",
    )
    kubernetes_resource: "KubernetesResource" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="KubernetesResource",
    )


class KubernetesResource(proto.Message):
    r"""KubernetesResource contains the YAML manifests and
    configuration for Membership Kubernetes resources in the
    cluster. After CreateMembership or UpdateMembership, these
    resources should be re-applied in the cluster.

    Attributes:
        membership_cr_manifest (str):
            Input only. The YAML representation of the
            Membership CR. This field is ignored for GKE
            clusters where Hub can read the CR directly.

            Callers should provide the CR that is currently
            present in the cluster during CreateMembership
            or UpdateMembership, or leave this field empty
            if none exists. The CR manifest is used to
            validate the cluster has not been registered
            with another Membership.
        membership_resources (MutableSequence[google.cloud.gkehub_v1beta1.types.ResourceManifest]):
            Output only. Additional Kubernetes resources
            that need to be applied to the cluster after
            Membership creation, and after every update.

            This field is only populated in the Membership
            returned from a successful long-running
            operation from CreateMembership or
            UpdateMembership. It is not populated during
            normal GetMembership or ListMemberships
            requests. To get the resource manifest after the
            initial registration, the caller should make a
            UpdateMembership call with an empty field mask.
        connect_resources (MutableSequence[google.cloud.gkehub_v1beta1.types.ResourceManifest]):
            Output only. The Kubernetes resources for
            installing the GKE Connect agent
            This field is only populated in the Membership
            returned from a successful long-running
            operation from CreateMembership or
            UpdateMembership. It is not populated during
            normal GetMembership or ListMemberships
            requests. To get the resource manifest after the
            initial registration, the caller should make a
            UpdateMembership call with an empty field mask.
        resource_options (google.cloud.gkehub_v1beta1.types.ResourceOptions):
            Optional. Options for Kubernetes resource
            generation.
    """

    membership_cr_manifest: str = proto.Field(
        proto.STRING,
        number=1,
    )
    membership_resources: MutableSequence["ResourceManifest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="ResourceManifest",
    )
    connect_resources: MutableSequence["ResourceManifest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="ResourceManifest",
    )
    resource_options: "ResourceOptions" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="ResourceOptions",
    )


class ResourceOptions(proto.Message):
    r"""ResourceOptions represent options for Kubernetes resource
    generation.

    Attributes:
        connect_version (str):
            Optional. The Connect agent version to use for
            connect_resources. Defaults to the latest GKE Connect
            version. The version must be a currently supported version,
            obsolete versions will be rejected.
        v1beta1_crd (bool):
            Optional. Use ``apiextensions/v1beta1`` instead of
            ``apiextensions/v1`` for CustomResourceDefinition resources.
            This option should be set for clusters with Kubernetes
            apiserver versions <1.16.
        k8s_version (str):
            Optional. Major and minor version of the Kubernetes cluster.
            This is only used to determine which version to use for the
            CustomResourceDefinition resources,
            ``apiextensions/v1beta1`` or\ ``apiextensions/v1``.
        k8s_git_version (str):
            Optional. Git version of the Kubernetes
            cluster. This is only used to gate the Connect
            Agent migration to svc.id.goog on GDC-SO
            1.33.100 patch and above.
    """

    connect_version: str = proto.Field(
        proto.STRING,
        number=1,
    )
    v1beta1_crd: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    k8s_version: str = proto.Field(
        proto.STRING,
        number=3,
    )
    k8s_git_version: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ResourceManifest(proto.Message):
    r"""ResourceManifest represents a single Kubernetes resource to
    be applied to the cluster.

    Attributes:
        manifest (str):
            YAML manifest of the resource.
        cluster_scoped (bool):
            Whether the resource provided in the manifest is
            ``cluster_scoped``. If unset, the manifest is assumed to be
            namespace scoped.

            This field is used for REST mapping when applying the
            resource in a cluster.
    """

    manifest: str = proto.Field(
        proto.STRING,
        number=1,
    )
    cluster_scoped: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class GkeCluster(proto.Message):
    r"""GkeCluster contains information specific to GKE clusters.

    Attributes:
        resource_link (str):
            Immutable. Self-link of the GCP resource for
            the GKE cluster. For example:
            //container.googleapis.com/projects/my-project/locations/us-west1-a/clusters/my-cluster

            Zonal clusters are also supported.
        cluster_missing (bool):
            Output only. If cluster_missing is set then it denotes that
            the GKE cluster no longer exists in the GKE Control Plane.
    """

    resource_link: str = proto.Field(
        proto.STRING,
        number=1,
    )
    cluster_missing: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class OnPremCluster(proto.Message):
    r"""OnPremCluster contains information specific to GKE On-Prem
    clusters.

    Attributes:
        resource_link (str):
            Immutable. Self-link of the GCP resource for
            the GKE On-Prem cluster. For example:

            //gkeonprem.googleapis.com/projects/my-project/locations/us-west1-a/vmwareClusters/my-cluster
            //gkeonprem.googleapis.com/projects/my-project/locations/us-west1-a/bareMetalClusters/my-cluster
        cluster_missing (bool):
            Output only. If cluster_missing is set then it denotes that
            API(gkeonprem.googleapis.com) resource for this GKE On-Prem
            cluster no longer exists.
        admin_cluster (bool):
            Immutable. Whether the cluster is an admin
            cluster.
        cluster_type (google.cloud.gkehub_v1beta1.types.OnPremCluster.ClusterType):
            Immutable. The on prem cluster's type.
    """

    class ClusterType(proto.Enum):
        r"""ClusterType describes on prem cluster's type.

        Values:
            CLUSTERTYPE_UNSPECIFIED (0):
                The ClusterType is not set.
            BOOTSTRAP (1):
                The ClusterType is bootstrap cluster.
            HYBRID (2):
                The ClusterType is baremetal hybrid cluster.
            STANDALONE (3):
                The ClusterType is baremetal standalone
                cluster.
            USER (4):
                The ClusterType is user cluster.
        """

        CLUSTERTYPE_UNSPECIFIED = 0
        BOOTSTRAP = 1
        HYBRID = 2
        STANDALONE = 3
        USER = 4

    resource_link: str = proto.Field(
        proto.STRING,
        number=1,
    )
    cluster_missing: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    admin_cluster: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    cluster_type: ClusterType = proto.Field(
        proto.ENUM,
        number=4,
        enum=ClusterType,
    )


class MultiCloudCluster(proto.Message):
    r"""MultiCloudCluster contains information specific to GKE
    Multi-Cloud clusters.

    Attributes:
        resource_link (str):
            Immutable. Self-link of the GCP resource for
            the GKE Multi-Cloud cluster. For example:

            //gkemulticloud.googleapis.com/projects/my-project/locations/us-west1-a/awsClusters/my-cluster
            //gkemulticloud.googleapis.com/projects/my-project/locations/us-west1-a/azureClusters/my-cluster
            //gkemulticloud.googleapis.com/projects/my-project/locations/us-west1-a/attachedClusters/my-cluster
        cluster_missing (bool):
            Output only. If cluster_missing is set then it denotes that
            API(gkemulticloud.googleapis.com) resource for this GKE
            Multi-Cloud cluster no longer exists.
    """

    resource_link: str = proto.Field(
        proto.STRING,
        number=1,
    )
    cluster_missing: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class EdgeCluster(proto.Message):
    r"""EdgeCluster contains information specific to Google Edge
    Clusters.

    Attributes:
        resource_link (str):
            Immutable. Self-link of the GCP resource for
            the Edge Cluster. For example:

            //edgecontainer.googleapis.com/projects/my-project/locations/us-west1-a/clusters/my-cluster
    """

    resource_link: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ApplianceCluster(proto.Message):
    r"""ApplianceCluster contains information specific to GDC Edge
    Appliance Clusters.

    Attributes:
        resource_link (str):
            Immutable. Self-link of the GCP resource for
            the Appliance Cluster. For example:

            //transferappliance.googleapis.com/projects/my-project/locations/us-west1-a/appliances/my-appliance
    """

    resource_link: str = proto.Field(
        proto.STRING,
        number=1,
    )


class KubernetesMetadata(proto.Message):
    r"""KubernetesMetadata provides informational metadata for
    Memberships representing Kubernetes clusters.

    Attributes:
        kubernetes_api_server_version (str):
            Output only. Kubernetes API server version
            string as reported by '/version'.
        node_provider_id (str):
            Output only. Node providerID as reported by the first node
            in the list of nodes on the Kubernetes endpoint. On
            Kubernetes platforms that support zero-node clusters (like
            GKE-on-GCP), the node_count will be zero and the
            node_provider_id will be empty.
        node_count (int):
            Output only. Node count as reported by
            Kubernetes nodes resources.
        vcpu_count (int):
            Output only. vCPU count as reported by
            Kubernetes nodes resources.
        memory_mb (int):
            Output only. The total memory capacity as
            reported by the sum of all Kubernetes nodes
            resources, defined in MB.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which these details were last
            updated. This update_time is different from the
            Membership-level update_time since EndpointDetails are
            updated internally for API consumers.
    """

    kubernetes_api_server_version: str = proto.Field(
        proto.STRING,
        number=1,
    )
    node_provider_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    node_count: int = proto.Field(
        proto.INT32,
        number=3,
    )
    vcpu_count: int = proto.Field(
        proto.INT32,
        number=4,
    )
    memory_mb: int = proto.Field(
        proto.INT32,
        number=5,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=100,
        message=timestamp_pb2.Timestamp,
    )


class Authority(proto.Message):
    r"""Authority encodes how Google will recognize identities from
    this Membership. See the workload identity documentation for
    more details:

    https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity

    Attributes:
        issuer (str):
            Optional. A JSON Web Token (JWT) issuer URI. ``issuer`` must
            start with ``https://`` and be a valid URL with length <2000
            characters.

            If set, then Google will allow valid OIDC tokens from this
            issuer to authenticate within the workload_identity_pool.
            OIDC discovery will be performed on this URI to validate
            tokens from the issuer.

            Clearing ``issuer`` disables Workload Identity. ``issuer``
            cannot be directly modified; it must be cleared (and
            Workload Identity disabled) before using a new issuer (and
            re-enabling Workload Identity).
        workload_identity_pool (str):
            Output only. The name of the workload identity pool in which
            ``issuer`` will be recognized.

            There is a single Workload Identity Pool per Hub that is
            shared between all Memberships that belong to that Hub. For
            a Hub hosted in {PROJECT_ID}, the workload pool format is
            ``{PROJECT_ID}.hub.id.goog``, although this is subject to
            change in newer versions of this API.
        identity_provider (str):
            Output only. An identity provider that reflects the
            ``issuer`` in the workload identity pool.
        oidc_jwks (bytes):
            Optional. OIDC verification keys for this Membership in JWKS
            format (RFC 7517).

            When this field is set, OIDC discovery will NOT be performed
            on ``issuer``, and instead OIDC tokens will be validated
            using this field.
    """

    issuer: str = proto.Field(
        proto.STRING,
        number=1,
    )
    workload_identity_pool: str = proto.Field(
        proto.STRING,
        number=2,
    )
    identity_provider: str = proto.Field(
        proto.STRING,
        number=3,
    )
    oidc_jwks: bytes = proto.Field(
        proto.BYTES,
        number=4,
    )


class MonitoringConfig(proto.Message):
    r"""This field informs Fleet-based applications/services/UIs with
    the necessary information for where each underlying Cluster
    reports its metrics.

    Attributes:
        project_id (str):
            Immutable. Project used to report Metrics
        location (str):
            Immutable. Location used to report Metrics
        cluster (str):
            Immutable. Cluster name used to report metrics. For Anthos
            on VMWare/Baremetal, it would be in format
            ``memberClusters/cluster_name``; And for Anthos on
            MultiCloud, it would be in format
            ``{azureClusters, awsClusters}/cluster_name``.
        kubernetes_metrics_prefix (str):
            Kubernetes system metrics, if available, are
            written to this prefix. This defaults to
            kubernetes.io for GKE, and kubernetes.io/anthos
            for Anthos eventually. Noted: Anthos MultiCloud
            will have kubernetes.io prefix today but will
            migration to be under kubernetes.io/anthos
        cluster_hash (str):
            Immutable. Cluster hash, this is a unique
            string generated by google code, which does not
            contain any PII, which we can use to reference
            the cluster. This is expected to be created by
            the monitoring stack and persisted into the
            Cluster object as well as to GKE-Hub.
    """

    project_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    location: str = proto.Field(
        proto.STRING,
        number=2,
    )
    cluster: str = proto.Field(
        proto.STRING,
        number=3,
    )
    kubernetes_metrics_prefix: str = proto.Field(
        proto.STRING,
        number=4,
    )
    cluster_hash: str = proto.Field(
        proto.STRING,
        number=5,
    )


class MembershipState(proto.Message):
    r"""State of the Membership resource.

    Attributes:
        code (google.cloud.gkehub_v1beta1.types.MembershipState.Code):
            Output only. The current state of the
            Membership resource.
        description (str):
            This field is never set by the Hub Service.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            This field is never set by the Hub Service.
    """

    class Code(proto.Enum):
        r"""Code describes the state of a Membership resource.

        Values:
            CODE_UNSPECIFIED (0):
                The code is not set.
            CREATING (1):
                The cluster is being registered.
            READY (2):
                The cluster is registered.
            DELETING (3):
                The cluster is being unregistered.
            UPDATING (4):
                The Membership is being updated.
            SERVICE_UPDATING (5):
                The Membership is being updated by the Hub
                Service.
        """

        CODE_UNSPECIFIED = 0
        CREATING = 1
        READY = 2
        DELETING = 3
        UPDATING = 4
        SERVICE_UPDATING = 5

    code: Code = proto.Field(
        proto.ENUM,
        number=1,
        enum=Code,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )


class ListMembershipsRequest(proto.Message):
    r"""Request message for ``GkeHubMembershipService.ListMemberships``
    method.

    Attributes:
        parent (str):
            Required. The parent (project and location) where the
            Memberships will be listed. Specified in the format
            ``projects/*/locations/*``. ``projects/*/locations/-`` list
            memberships in all the regions.
        page_size (int):
            Optional. When requesting a 'page' of resources,
            ``page_size`` specifies number of resources to return. If
            unspecified or set to 0, all resources will be returned.
        page_token (str):
            Optional. Token returned by previous call to
            ``ListMemberships`` which specifies the position in the list
            from where to continue listing the resources.
        filter (str):
            Optional. Lists Memberships that match the filter
            expression, following the syntax outlined in
            https://google.aip.dev/160.

            Examples:

            - Name is ``bar`` in project ``foo-proj`` and location
              ``global``:

              name = "projects/foo-proj/locations/global/membership/bar"

            - Memberships that have a label called ``foo``:

              labels.foo:\*

            - Memberships that have a label called ``foo`` whose value
              is ``bar``:

              labels.foo = bar

            - Memberships in the CREATING state:

              state = CREATING
        order_by (str):
            Optional. One or more fields to compare and
            use to sort the output. See
            https://google.aip.dev/132#ordering.
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


class ListMembershipsResponse(proto.Message):
    r"""Response message for the ``GkeHubMembershipService.ListMemberships``
    method.

    Attributes:
        resources (MutableSequence[google.cloud.gkehub_v1beta1.types.Membership]):
            The list of matching Memberships.
        next_page_token (str):
            A token to request the next page of resources from the
            ``ListMemberships`` method. The value of an empty string
            means that there are no more resources to return.
        unreachable (MutableSequence[str]):
            List of locations that could not be reached
            while fetching this list.
    """

    @property
    def raw_page(self):
        return self

    resources: MutableSequence["Membership"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Membership",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetMembershipRequest(proto.Message):
    r"""Request message for ``GkeHubMembershipService.GetMembership``
    method.

    Attributes:
        name (str):
            Required. The Membership resource name in the format
            ``projects/*/locations/*/memberships/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateMembershipRequest(proto.Message):
    r"""Request message for the ``GkeHubMembershipService.CreateMembership``
    method.

    Attributes:
        parent (str):
            Required. The parent (project and location) where the
            Memberships will be created. Specified in the format
            ``projects/*/locations/*``.
        membership_id (str):
            Required. Client chosen ID for the membership.
            ``membership_id`` must be a valid RFC 1123 compliant DNS
            label:

            1. At most 63 characters in length
            2. It must consist of lower case alphanumeric characters or
               ``-``
            3. It must start and end with an alphanumeric character

            Which can be expressed as the regex:
            ``[a-z0-9]([-a-z0-9]*[a-z0-9])?``, with a maximum length of
            63 characters.
        resource (google.cloud.gkehub_v1beta1.types.Membership):
            Required. The membership to create.
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server will guarantee that for at
            least 60 minutes after the first request.

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
    membership_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    resource: "Membership" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Membership",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class DeleteMembershipRequest(proto.Message):
    r"""Request message for ``GkeHubMembershipService.DeleteMembership``
    method.

    Attributes:
        name (str):
            Required. The Membership resource name in the format
            ``projects/*/locations/*/memberships/*``.
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server will guarantee that for at
            least 60 minutes after the first request.

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
        force (bool):
            Optional. If set to true, any subresource
            from this Membership will also be deleted.
            Otherwise, the request will only work if the
            Membership has no subresource.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class UpdateMembershipRequest(proto.Message):
    r"""Request message for ``GkeHubMembershipService.UpdateMembership``
    method.

    Attributes:
        name (str):
            Required. The membership resource name in the format:
            ``projects/[project_id]/locations/global/memberships/[membership_id]``
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Mask of fields to update. At least
            one field path must be specified in this mask.
        resource (google.cloud.gkehub_v1beta1.types.Membership):
            Required. Only fields specified in update_mask are updated.
            If you specify a field in the update_mask but don't specify
            its value here that field will be deleted. If you are
            updating a map field, set the value of a key to null or
            empty string to delete the key from the map. It's not
            possible to update a key's value to the empty string. If you
            specify the update_mask to be a special path "\*", fully
            replaces all user-modifiable fields to match ``resource``.
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server will guarantee that for at
            least 60 minutes after the first request.

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

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )
    resource: "Membership" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Membership",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class GenerateConnectManifestRequest(proto.Message):
    r"""Request message for
    ``GkeHubMembershipService.GenerateConnectManifest`` method.

    Attributes:
        name (str):
            Required. The Membership resource name the Agent will
            associate with, in the format
            ``projects/*/locations/*/memberships/*``.
        connect_agent (google.cloud.gkehub_v1beta1.types.ConnectAgent):
            Optional. The connect agent to generate
            manifest for.
        version (str):
            Optional. The Connect agent version to use.
            Defaults to the most current version.
        is_upgrade (bool):
            Optional. If true, generate the resources for
            upgrade only. Some resources generated only for
            installation (e.g. secrets) will be excluded.
        registry (str):
            Optional. The registry to fetch the connect
            agent image from. Defaults to gcr.io/gkeconnect.
        image_pull_secret_content (bytes):
            Optional. The image pull secret content for
            the registry, if not public.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    connect_agent: "ConnectAgent" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ConnectAgent",
    )
    version: str = proto.Field(
        proto.STRING,
        number=3,
    )
    is_upgrade: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    registry: str = proto.Field(
        proto.STRING,
        number=5,
    )
    image_pull_secret_content: bytes = proto.Field(
        proto.BYTES,
        number=6,
    )


class GenerateConnectManifestResponse(proto.Message):
    r"""GenerateConnectManifestResponse contains manifest information
    for installing/upgrading a Connect agent.

    Attributes:
        manifest (MutableSequence[google.cloud.gkehub_v1beta1.types.ConnectAgentResource]):
            The ordered list of Kubernetes resources that
            need to be applied to the cluster for GKE
            Connect agent installation/upgrade.
    """

    manifest: MutableSequence["ConnectAgentResource"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ConnectAgentResource",
    )


class ConnectAgentResource(proto.Message):
    r"""ConnectAgentResource represents a Kubernetes resource
    manifest for Connect Agent deployment.

    Attributes:
        type_ (google.cloud.gkehub_v1beta1.types.TypeMeta):
            Kubernetes type of the resource.
        manifest (str):
            YAML manifest of the resource.
    """

    type_: "TypeMeta" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="TypeMeta",
    )
    manifest: str = proto.Field(
        proto.STRING,
        number=2,
    )


class TypeMeta(proto.Message):
    r"""TypeMeta is the type information needed for content
    unmarshalling of Kubernetes resources in the manifest.

    Attributes:
        kind (str):
            Kind of the resource (e.g. Deployment).
        api_version (str):
            APIVersion of the resource (e.g. v1).
    """

    kind: str = proto.Field(
        proto.STRING,
        number=1,
    )
    api_version: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ConnectAgent(proto.Message):
    r"""The information required from end users to use GKE Connect.

    Attributes:
        name (str):
            Do not set.
        proxy (bytes):
            Optional. URI of a proxy if connectivity from the agent to
            gkeconnect.googleapis.com requires the use of a proxy.
            Format must be in the form ``http(s)://{proxy_address}``,
            depending on the HTTP/HTTPS protocol supported by the proxy.
            This will direct the connect agent's outbound traffic
            through a HTTP(S) proxy.
        namespace (str):
            Optional. Namespace for GKE Connect agent resources.
            Defaults to ``gke-connect``.

            The Connect Agent is authorized automatically when run in
            the default namespace. Otherwise, explicit authorization
            must be granted with an additional IAM binding.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    proxy: bytes = proto.Field(
        proto.BYTES,
        number=2,
    )
    namespace: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ValidateExclusivityRequest(proto.Message):
    r"""The request to validate the existing state of the membership
    CR in the cluster.

    Attributes:
        parent (str):
            Required. The parent (project and location) where the
            Memberships will be created. Specified in the format
            ``projects/*/locations/*``.
        cr_manifest (str):
            Optional. The YAML of the membership CR in
            the cluster. Empty if the membership CR does not
            exist.
        intended_membership (str):
            Required. The intended membership name under the ``parent``.
            This method only does validation in anticipation of a
            CreateMembership call with the same name.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    cr_manifest: str = proto.Field(
        proto.STRING,
        number=2,
    )
    intended_membership: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ValidateExclusivityResponse(proto.Message):
    r"""The response of exclusivity artifacts validation result
    status.

    Attributes:
        status (google.rpc.status_pb2.Status):
            The validation result.

            - ``OK`` means that exclusivity is validated, assuming the
              manifest produced by GenerateExclusivityManifest is
              successfully applied.
            - ``ALREADY_EXISTS`` means that the Membership CRD is
              already owned by another Hub. See ``status.message`` for
              more information.
    """

    status: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=1,
        message=status_pb2.Status,
    )


class GenerateExclusivityManifestRequest(proto.Message):
    r"""The request to generate the manifests for exclusivity
    artifacts.

    Attributes:
        name (str):
            Required. The Membership resource name in the format
            ``projects/*/locations/*/memberships/*``.
        crd_manifest (str):
            Optional. The YAML manifest of the membership CRD retrieved
            by ``kubectl get customresourcedefinitions membership``.
            Leave empty if the resource does not exist.
        cr_manifest (str):
            Optional. The YAML manifest of the membership CR retrieved
            by ``kubectl get memberships membership``. Leave empty if
            the resource does not exist.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    crd_manifest: str = proto.Field(
        proto.STRING,
        number=2,
    )
    cr_manifest: str = proto.Field(
        proto.STRING,
        number=3,
    )


class GenerateExclusivityManifestResponse(proto.Message):
    r"""The response of the exclusivity artifacts manifests for the
    client to apply.

    Attributes:
        crd_manifest (str):
            The YAML manifest of the membership CRD to
            apply if a newer version of the CRD is
            available. Empty if no update needs to be
            applied.
        cr_manifest (str):
            The YAML manifest of the membership CR to
            apply if a new version of the CR is available.
            Empty if no update needs to be applied.
    """

    crd_manifest: str = proto.Field(
        proto.STRING,
        number=1,
    )
    cr_manifest: str = proto.Field(
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
        status_detail (str):
            Output only. Human-readable status of the
            operation, if any.
        cancel_requested (bool):
            Output only. Identifies whether the user has requested
            cancellation of the operation. Operations that have
            successfully been cancelled have [Operation.error][] value
            with a [google.rpc.Status.code][google.rpc.Status.code] of
            1, corresponding to ``Code.CANCELLED``.
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


__all__ = tuple(sorted(__protobuf__.manifest))
