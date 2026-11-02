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
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.gkehub.v1",
    manifest={
        "Membership",
        "MembershipEndpoint",
        "KubernetesResource",
        "ResourceOptions",
        "ResourceManifest",
        "GkeCluster",
        "KubernetesMetadata",
        "MonitoringConfig",
        "MembershipState",
        "Authority",
    },
)


class Membership(proto.Message):
    r"""Membership contains information about a member cluster.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        endpoint (google.cloud.gkehub_v1.types.MembershipEndpoint):
            Optional. Endpoint information to reach this
            member.

            This field is a member of `oneof`_ ``type``.
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
            Optional. Labels for this membership.
        description (str):
            Output only. Description of this membership, limited to 63
            characters. Must match the regex:
            ``[a-zA-Z0-9][a-zA-Z0-9_\-\.\ ]*``

            This field is present for legacy purposes.
        state (google.cloud.gkehub_v1.types.MembershipState):
            Output only. State of the Membership
            resource.
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
            is not recommended.

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
        authority (google.cloud.gkehub_v1.types.Authority):
            Optional. How to identify workloads from this
            Membership. See the documentation on Workload
            Identity for more details:

            https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity
        monitoring_config (google.cloud.gkehub_v1.types.MonitoringConfig):
            Optional. The monitoring config information
            for this membership.
    """

    endpoint: "MembershipEndpoint" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="type",
        message="MembershipEndpoint",
    )
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
    state: "MembershipState" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="MembershipState",
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
        number=9,
    )
    last_connection_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10,
        message=timestamp_pb2.Timestamp,
    )
    unique_id: str = proto.Field(
        proto.STRING,
        number=11,
    )
    authority: "Authority" = proto.Field(
        proto.MESSAGE,
        number=12,
        message="Authority",
    )
    monitoring_config: "MonitoringConfig" = proto.Field(
        proto.MESSAGE,
        number=14,
        message="MonitoringConfig",
    )


class MembershipEndpoint(proto.Message):
    r"""MembershipEndpoint contains information needed to contact a
    Kubernetes API, endpoint and any additional Kubernetes metadata.

    Attributes:
        gke_cluster (google.cloud.gkehub_v1.types.GkeCluster):
            Optional. GKE-specific information. Only
            present if this Membership is a GKE cluster.
        kubernetes_metadata (google.cloud.gkehub_v1.types.KubernetesMetadata):
            Output only. Useful Kubernetes-specific
            metadata.
        kubernetes_resource (google.cloud.gkehub_v1.types.KubernetesResource):
            Optional. The in-cluster Kubernetes Resources that should be
            applied for a correctly registered cluster, in the steady
            state. These resources:

            - Ensure that the cluster is exclusively registered to one
              and only one Hub Membership.
            - Propagate Workload Pool Information available in the
              Membership Authority field.
            - Ensure proper initial configuration of default Hub
              Features.
        google_managed (bool):
            Output only. Whether the lifecycle of this
            membership is managed by a google cluster
            platform service.
    """

    gke_cluster: "GkeCluster" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="GkeCluster",
    )
    kubernetes_metadata: "KubernetesMetadata" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="KubernetesMetadata",
    )
    kubernetes_resource: "KubernetesResource" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="KubernetesResource",
    )
    google_managed: bool = proto.Field(
        proto.BOOL,
        number=8,
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
        membership_resources (MutableSequence[google.cloud.gkehub_v1.types.ResourceManifest]):
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
        connect_resources (MutableSequence[google.cloud.gkehub_v1.types.ResourceManifest]):
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
        resource_options (google.cloud.gkehub_v1.types.ResourceOptions):
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
            Immutable. Self-link of the Google Cloud
            resource for the GKE cluster. For example:

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
        number=2,
    )


class KubernetesMetadata(proto.Message):
    r"""KubernetesMetadata provides informational metadata for
    Memberships representing Kubernetes clusters.

    Attributes:
        kubernetes_api_server_version (str):
            Output only. Kubernetes API server version string as
            reported by ``/version``.
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
    r"""MembershipState describes the state of a Membership resource.

    Attributes:
        code (google.cloud.gkehub_v1.types.MembershipState.Code):
            Output only. The current state of the
            Membership resource.
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


__all__ = tuple(sorted(__protobuf__.manifest))
