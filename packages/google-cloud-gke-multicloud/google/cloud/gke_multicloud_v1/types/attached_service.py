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
import proto  # type: ignore

from google.cloud.gke_multicloud_v1.types import attached_resources

__protobuf__ = proto.module(
    package="google.cloud.gkemulticloud.v1",
    manifest={
        "GenerateAttachedClusterInstallManifestRequest",
        "GenerateAttachedClusterInstallManifestResponse",
        "CreateAttachedClusterRequest",
        "ImportAttachedClusterRequest",
        "UpdateAttachedClusterRequest",
        "GetAttachedClusterRequest",
        "ListAttachedClustersRequest",
        "ListAttachedClustersResponse",
        "DeleteAttachedClusterRequest",
        "GetAttachedServerConfigRequest",
        "GenerateAttachedClusterAgentTokenRequest",
        "GenerateAttachedClusterAgentTokenResponse",
    },
)


class GenerateAttachedClusterInstallManifestRequest(proto.Message):
    r"""Request message for
    ``AttachedClusters.GenerateAttachedClusterInstallManifest`` method.

    Attributes:
        parent (str):
            Required. The parent location where this
            [AttachedCluster][google.cloud.gkemulticloud.v1.AttachedCluster]
            resource will be created.

            Location names are formatted as
            ``projects/<project-id>/locations/<region>``.

            See `Resource
            Names <https://cloud.google.com/apis/design/resource_names>`__
            for more details on Google Cloud resource names.
        attached_cluster_id (str):
            Required. A client provided ID of the resource. Must be
            unique within the parent resource.

            The provided ID will be part of the
            [AttachedCluster][google.cloud.gkemulticloud.v1.AttachedCluster]
            resource name formatted as
            ``projects/<project-id>/locations/<region>/attachedClusters/<cluster-id>``.

            Valid characters are ``/[a-z][0-9]-/``. Cannot be longer
            than 63 characters.

            When generating an install manifest for importing an
            existing Membership resource, the attached_cluster_id field
            must be the Membership id.

            Membership names are formatted as
            ``projects/<project-id>/locations/<region>/memberships/<membership-id>``.
        platform_version (str):
            Required. The platform version for the cluster (e.g.
            ``1.19.0-gke.1000``).

            You can list all supported versions on a given Google Cloud
            region by calling
            [GetAttachedServerConfig][google.cloud.gkemulticloud.v1.AttachedClusters.GetAttachedServerConfig].
        proxy_config (google.cloud.gke_multicloud_v1.types.AttachedProxyConfig):
            Optional. Proxy configuration for outbound
            HTTP(S) traffic.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    attached_cluster_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    platform_version: str = proto.Field(
        proto.STRING,
        number=3,
    )
    proxy_config: attached_resources.AttachedProxyConfig = proto.Field(
        proto.MESSAGE,
        number=4,
        message=attached_resources.AttachedProxyConfig,
    )


class GenerateAttachedClusterInstallManifestResponse(proto.Message):
    r"""Response message for
    ``AttachedClusters.GenerateAttachedClusterInstallManifest`` method.

    Attributes:
        manifest (str):
            A set of Kubernetes resources (in YAML
            format) to be applied to the cluster to be
            attached.
    """

    manifest: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateAttachedClusterRequest(proto.Message):
    r"""Request message for ``AttachedClusters.CreateAttachedCluster``
    method.

    Attributes:
        parent (str):
            Required. The parent location where this
            [AttachedCluster][google.cloud.gkemulticloud.v1.AttachedCluster]
            resource will be created.

            Location names are formatted as
            ``projects/<project-id>/locations/<region>``.

            See `Resource
            Names <https://cloud.google.com/apis/design/resource_names>`__
            for more details on Google Cloud resource names.
        attached_cluster (google.cloud.gke_multicloud_v1.types.AttachedCluster):
            Required. The specification of the
            [AttachedCluster][google.cloud.gkemulticloud.v1.AttachedCluster]
            to create.
        attached_cluster_id (str):
            Required. A client provided ID the resource. Must be unique
            within the parent resource.

            The provided ID will be part of the
            [AttachedCluster][google.cloud.gkemulticloud.v1.AttachedCluster]
            resource name formatted as
            ``projects/<project-id>/locations/<region>/attachedClusters/<cluster-id>``.

            Valid characters are ``/[a-z][0-9]-/``. Cannot be longer
            than 63 characters.
        validate_only (bool):
            If set, only validate the request, but do not
            actually create the cluster.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    attached_cluster: attached_resources.AttachedCluster = proto.Field(
        proto.MESSAGE,
        number=2,
        message=attached_resources.AttachedCluster,
    )
    attached_cluster_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class ImportAttachedClusterRequest(proto.Message):
    r"""Request message for ``AttachedClusters.ImportAttachedCluster``
    method.

    Attributes:
        parent (str):
            Required. The parent location where this
            [AttachedCluster][google.cloud.gkemulticloud.v1.AttachedCluster]
            resource will be created.

            Location names are formatted as
            ``projects/<project-id>/locations/<region>``.

            See `Resource
            Names <https://cloud.google.com/apis/design/resource_names>`__
            for more details on Google Cloud resource names.
        validate_only (bool):
            If set, only validate the request, but do not
            actually import the cluster.
        fleet_membership (str):
            Required. The name of the fleet membership
            resource to import.
        platform_version (str):
            Required. The platform version for the cluster (e.g.
            ``1.19.0-gke.1000``).

            You can list all supported versions on a given Google Cloud
            region by calling
            [GetAttachedServerConfig][google.cloud.gkemulticloud.v1.AttachedClusters.GetAttachedServerConfig].
        distribution (str):
            Required. The Kubernetes distribution of the underlying
            attached cluster.

            Supported values: ["eks", "aks", "generic"].
        proxy_config (google.cloud.gke_multicloud_v1.types.AttachedProxyConfig):
            Optional. Proxy configuration for outbound
            HTTP(S) traffic.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    fleet_membership: str = proto.Field(
        proto.STRING,
        number=3,
    )
    platform_version: str = proto.Field(
        proto.STRING,
        number=4,
    )
    distribution: str = proto.Field(
        proto.STRING,
        number=5,
    )
    proxy_config: attached_resources.AttachedProxyConfig = proto.Field(
        proto.MESSAGE,
        number=6,
        message=attached_resources.AttachedProxyConfig,
    )


class UpdateAttachedClusterRequest(proto.Message):
    r"""Request message for ``AttachedClusters.UpdateAttachedCluster``
    method.

    Attributes:
        attached_cluster (google.cloud.gke_multicloud_v1.types.AttachedCluster):
            Required. The
            [AttachedCluster][google.cloud.gkemulticloud.v1.AttachedCluster]
            resource to update.
        validate_only (bool):
            If set, only validate the request, but do not
            actually update the cluster.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Mask of fields to update. At least one path must
            be supplied in this field. The elements of the repeated
            paths field can only include these fields from
            [AttachedCluster][google.cloud.gkemulticloud.v1.AttachedCluster]:

            - ``annotations``.
            - ``authorization.admin_groups``.
            - ``authorization.admin_users``.
            - ``binary_authorization.evaluation_mode``.
            - ``description``.
            - ``logging_config.component_config.enable_components``.
            - ``monitoring_config.managed_prometheus_config.enabled``.
            - ``platform_version``.
            - ``proxy_config.kubernetes_secret.name``.
            - ``proxy_config.kubernetes_secret.namespace``.
            - ``security_posture_config.vulnerability_mode``
            - ``monitoring_config.cloud_monitoring_config.enabled``
    """

    attached_cluster: attached_resources.AttachedCluster = proto.Field(
        proto.MESSAGE,
        number=1,
        message=attached_resources.AttachedCluster,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=3,
        message=field_mask_pb2.FieldMask,
    )


class GetAttachedClusterRequest(proto.Message):
    r"""Request message for ``AttachedClusters.GetAttachedCluster`` method.

    Attributes:
        name (str):
            Required. The name of the
            [AttachedCluster][google.cloud.gkemulticloud.v1.AttachedCluster]
            resource to describe.

            ``AttachedCluster`` names are formatted as
            ``projects/<project-id>/locations/<region>/attachedClusters/<cluster-id>``.

            See `Resource
            Names <https://cloud.google.com/apis/design/resource_names>`__
            for more details on Google Cloud Platform resource names.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListAttachedClustersRequest(proto.Message):
    r"""Request message for ``AttachedClusters.ListAttachedClusters``
    method.

    Attributes:
        parent (str):
            Required. The parent location which owns this collection of
            [AttachedCluster][google.cloud.gkemulticloud.v1.AttachedCluster]
            resources.

            Location names are formatted as
            ``projects/<project-id>/locations/<region>``.

            See `Resource
            Names <https://cloud.google.com/apis/design/resource_names>`__
            for more details on Google Cloud Platform resource names.
        page_size (int):
            The maximum number of items to return.

            If not specified, a default value of 50 will be used by the
            service. Regardless of the pageSize value, the response can
            include a partial list and a caller should only rely on
            response's
            [nextPageToken][google.cloud.gkemulticloud.v1.ListAttachedClustersResponse.next_page_token]
            to determine if there are more instances left to be queried.
        page_token (str):
            The ``nextPageToken`` value returned from a previous
            [attachedClusters.list][google.cloud.gkemulticloud.v1.AttachedClusters.ListAttachedClusters]
            request, if any.
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


class ListAttachedClustersResponse(proto.Message):
    r"""Response message for ``AttachedClusters.ListAttachedClusters``
    method.

    Attributes:
        attached_clusters (MutableSequence[google.cloud.gke_multicloud_v1.types.AttachedCluster]):
            A list of
            [AttachedCluster][google.cloud.gkemulticloud.v1.AttachedCluster]
            resources in the specified Google Cloud Platform project and
            region region.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
    """

    @property
    def raw_page(self):
        return self

    attached_clusters: MutableSequence[attached_resources.AttachedCluster] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=attached_resources.AttachedCluster,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DeleteAttachedClusterRequest(proto.Message):
    r"""Request message for ``AttachedClusters.DeleteAttachedCluster``
    method.

    Attributes:
        name (str):
            Required. The resource name the
            [AttachedCluster][google.cloud.gkemulticloud.v1.AttachedCluster]
            to delete.

            ``AttachedCluster`` names are formatted as
            ``projects/<project-id>/locations/<region>/attachedClusters/<cluster-id>``.

            See `Resource
            Names <https://cloud.google.com/apis/design/resource_names>`__
            for more details on Google Cloud Platform resource names.
        validate_only (bool):
            If set, only validate the request, but do not
            actually delete the resource.
        allow_missing (bool):
            If set to true, and the
            [AttachedCluster][google.cloud.gkemulticloud.v1.AttachedCluster]
            resource is not found, the request will succeed but no
            action will be taken on the server and a completed
            [Operation][google.longrunning.Operation] will be returned.

            Useful for idempotent deletion.
        ignore_errors (bool):
            If set to true, the deletion of
            [AttachedCluster][google.cloud.gkemulticloud.v1.AttachedCluster]
            resource will succeed even if errors occur during deleting
            in cluster resources. Using this parameter may result in
            orphaned resources in the cluster.
        etag (str):
            The current etag of the
            [AttachedCluster][google.cloud.gkemulticloud.v1.AttachedCluster].

            Allows clients to perform deletions through optimistic
            concurrency control.

            If the provided etag does not match the current etag of the
            cluster, the request will fail and an ABORTED error will be
            returned.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    allow_missing: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    ignore_errors: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=4,
    )


class GetAttachedServerConfigRequest(proto.Message):
    r"""GetAttachedServerConfigRequest gets the server config for
    attached clusters.

    Attributes:
        name (str):
            Required. The name of the
            [AttachedServerConfig][google.cloud.gkemulticloud.v1.AttachedServerConfig]
            resource to describe.

            ``AttachedServerConfig`` names are formatted as
            ``projects/<project-id>/locations/<region>/attachedServerConfig``.

            See `Resource
            Names <https://cloud.google.com/apis/design/resource_names>`__
            for more details on Google Cloud resource names.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GenerateAttachedClusterAgentTokenRequest(proto.Message):
    r"""

    Attributes:
        attached_cluster (str):
            Required.
        subject_token (str):
            Required.
        subject_token_type (str):
            Required.
        version (str):
            Required.
        grant_type (str):
            Optional.
        audience (str):
            Optional.
        scope (str):
            Optional.
        requested_token_type (str):
            Optional.
        options (str):
            Optional.
    """

    attached_cluster: str = proto.Field(
        proto.STRING,
        number=1,
    )
    subject_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    subject_token_type: str = proto.Field(
        proto.STRING,
        number=3,
    )
    version: str = proto.Field(
        proto.STRING,
        number=4,
    )
    grant_type: str = proto.Field(
        proto.STRING,
        number=6,
    )
    audience: str = proto.Field(
        proto.STRING,
        number=7,
    )
    scope: str = proto.Field(
        proto.STRING,
        number=8,
    )
    requested_token_type: str = proto.Field(
        proto.STRING,
        number=9,
    )
    options: str = proto.Field(
        proto.STRING,
        number=10,
    )


class GenerateAttachedClusterAgentTokenResponse(proto.Message):
    r"""

    Attributes:
        access_token (str):

        expires_in (int):

        token_type (str):

    """

    access_token: str = proto.Field(
        proto.STRING,
        number=1,
    )
    expires_in: int = proto.Field(
        proto.INT32,
        number=2,
    )
    token_type: str = proto.Field(
        proto.STRING,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
