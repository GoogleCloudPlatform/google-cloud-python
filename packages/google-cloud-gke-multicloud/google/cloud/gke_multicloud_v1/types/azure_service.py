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
import proto  # type: ignore

from google.cloud.gke_multicloud_v1.types import azure_resources

__protobuf__ = proto.module(
    package="google.cloud.gkemulticloud.v1",
    manifest={
        "CreateAzureClusterRequest",
        "UpdateAzureClusterRequest",
        "GetAzureClusterRequest",
        "ListAzureClustersRequest",
        "ListAzureClustersResponse",
        "DeleteAzureClusterRequest",
        "CreateAzureNodePoolRequest",
        "UpdateAzureNodePoolRequest",
        "GetAzureNodePoolRequest",
        "ListAzureNodePoolsRequest",
        "ListAzureNodePoolsResponse",
        "DeleteAzureNodePoolRequest",
        "GetAzureOpenIdConfigRequest",
        "GetAzureJsonWebKeysRequest",
        "GetAzureServerConfigRequest",
        "CreateAzureClientRequest",
        "GetAzureClientRequest",
        "ListAzureClientsRequest",
        "ListAzureClientsResponse",
        "DeleteAzureClientRequest",
        "GenerateAzureAccessTokenRequest",
        "GenerateAzureAccessTokenResponse",
        "GenerateAzureClusterAgentTokenRequest",
        "GenerateAzureClusterAgentTokenResponse",
    },
)


class CreateAzureClusterRequest(proto.Message):
    r"""Request message for ``AzureClusters.CreateAzureCluster`` method.

    Attributes:
        parent (str):
            Required. The parent location where this
            [AzureCluster][google.cloud.gkemulticloud.v1.AzureCluster]
            resource will be created.

            Location names are formatted as
            ``projects/<project-id>/locations/<region>``.

            See `Resource
            Names <https://cloud.google.com/apis/design/resource_names>`__
            for more details on Google Cloud resource names.
        azure_cluster (google.cloud.gke_multicloud_v1.types.AzureCluster):
            Required. The specification of the
            [AzureCluster][google.cloud.gkemulticloud.v1.AzureCluster]
            to create.
        azure_cluster_id (str):
            Required. A client provided ID the resource. Must be unique
            within the parent resource.

            The provided ID will be part of the
            [AzureCluster][google.cloud.gkemulticloud.v1.AzureCluster]
            resource name formatted as
            ``projects/<project-id>/locations/<region>/azureClusters/<cluster-id>``.

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
    azure_cluster: azure_resources.AzureCluster = proto.Field(
        proto.MESSAGE,
        number=2,
        message=azure_resources.AzureCluster,
    )
    azure_cluster_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class UpdateAzureClusterRequest(proto.Message):
    r"""Request message for ``AzureClusters.UpdateAzureCluster`` method.

    Attributes:
        azure_cluster (google.cloud.gke_multicloud_v1.types.AzureCluster):
            Required. The
            [AzureCluster][google.cloud.gkemulticloud.v1.AzureCluster]
            resource to update.
        validate_only (bool):
            If set, only validate the request, but do not
            actually update the cluster.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Mask of fields to update. At least one path must
            be supplied in this field. The elements of the repeated
            paths field can only include these fields from
            [AzureCluster][google.cloud.gkemulticloud.v1.AzureCluster]:

            - ``description``.
            - ``azureClient``.
            - ``control_plane.version``.
            - ``control_plane.vm_size``.
            - ``annotations``.
            - ``authorization.admin_users``.
            - ``authorization.admin_groups``.
            - ``control_plane.root_volume.size_gib``.
            - ``azure_services_authentication``.
            - ``azure_services_authentication.tenant_id``.
            - ``azure_services_authentication.application_id``.
            - ``control_plane.proxy_config``.
            - ``control_plane.proxy_config.resource_group_id``.
            - ``control_plane.proxy_config.secret_id``.
            - ``control_plane.ssh_config.authorized_key``.
            - ``logging_config.component_config.enable_components``
            - ``monitoring_config.managed_prometheus_config.enabled``.
    """

    azure_cluster: azure_resources.AzureCluster = proto.Field(
        proto.MESSAGE,
        number=1,
        message=azure_resources.AzureCluster,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=4,
        message=field_mask_pb2.FieldMask,
    )


class GetAzureClusterRequest(proto.Message):
    r"""Request message for ``AzureClusters.GetAzureCluster`` method.

    Attributes:
        name (str):
            Required. The name of the
            [AzureCluster][google.cloud.gkemulticloud.v1.AzureCluster]
            resource to describe.

            ``AzureCluster`` names are formatted as
            ``projects/<project-id>/locations/<region>/azureClusters/<cluster-id>``.

            See `Resource
            Names <https://cloud.google.com/apis/design/resource_names>`__
            for more details on Google Cloud Platform resource names.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListAzureClustersRequest(proto.Message):
    r"""Request message for ``AzureClusters.ListAzureClusters`` method.

    Attributes:
        parent (str):
            Required. The parent location which owns this collection of
            [AzureCluster][google.cloud.gkemulticloud.v1.AzureCluster]
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
            [nextPageToken][google.cloud.gkemulticloud.v1.ListAzureClustersResponse.next_page_token]
            to determine if there are more instances left to be queried.
        page_token (str):
            The ``nextPageToken`` value returned from a previous
            [azureClusters.list][google.cloud.gkemulticloud.v1.AzureClusters.ListAzureClusters]
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


class ListAzureClustersResponse(proto.Message):
    r"""Response message for ``AzureClusters.ListAzureClusters`` method.

    Attributes:
        azure_clusters (MutableSequence[google.cloud.gke_multicloud_v1.types.AzureCluster]):
            A list of
            [AzureCluster][google.cloud.gkemulticloud.v1.AzureCluster]
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

    azure_clusters: MutableSequence[azure_resources.AzureCluster] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=azure_resources.AzureCluster,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DeleteAzureClusterRequest(proto.Message):
    r"""Request message for ``AzureClusters.DeleteAzureCluster`` method.

    Attributes:
        name (str):
            Required. The resource name the
            [AzureCluster][google.cloud.gkemulticloud.v1.AzureCluster]
            to delete.

            ``AzureCluster`` names are formatted as
            ``projects/<project-id>/locations/<region>/azureClusters/<cluster-id>``.

            See `Resource
            Names <https://cloud.google.com/apis/design/resource_names>`__
            for more details on Google Cloud Platform resource names.
        allow_missing (bool):
            If set to true, and the
            [AzureCluster][google.cloud.gkemulticloud.v1.AzureCluster]
            resource is not found, the request will succeed but no
            action will be taken on the server and a completed
            [Operation][google.longrunning.Operation] will be returned.

            Useful for idempotent deletion.
        validate_only (bool):
            If set, only validate the request, but do not
            actually delete the resource.
        etag (str):
            The current etag of the
            [AzureCluster][google.cloud.gkemulticloud.v1.AzureCluster].

            Allows clients to perform deletions through optimistic
            concurrency control.

            If the provided etag does not match the current etag of the
            cluster, the request will fail and an ABORTED error will be
            returned.
        ignore_errors (bool):
            Optional. If set to true, the deletion of
            [AzureCluster][google.cloud.gkemulticloud.v1.AzureCluster]
            resource will succeed even if errors occur during deleting
            in cluster resources. Using this parameter may result in
            orphaned resources in the cluster.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    allow_missing: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=4,
    )
    ignore_errors: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class CreateAzureNodePoolRequest(proto.Message):
    r"""Response message for ``AzureClusters.CreateAzureNodePool`` method.

    Attributes:
        parent (str):
            Required. The
            [AzureCluster][google.cloud.gkemulticloud.v1.AzureCluster]
            resource where this node pool will be created.

            ``AzureCluster`` names are formatted as
            ``projects/<project-id>/locations/<region>/azureClusters/<cluster-id>``.

            See `Resource
            Names <https://cloud.google.com/apis/design/resource_names>`__
            for more details on Google Cloud resource names.
        azure_node_pool (google.cloud.gke_multicloud_v1.types.AzureNodePool):
            Required. The specification of the
            [AzureNodePool][google.cloud.gkemulticloud.v1.AzureNodePool]
            to create.
        azure_node_pool_id (str):
            Required. A client provided ID the resource. Must be unique
            within the parent resource.

            The provided ID will be part of the
            [AzureNodePool][google.cloud.gkemulticloud.v1.AzureNodePool]
            resource name formatted as
            ``projects/<project-id>/locations/<region>/azureClusters/<cluster-id>/azureNodePools/<node-pool-id>``.

            Valid characters are ``/[a-z][0-9]-/``. Cannot be longer
            than 63 characters.
        validate_only (bool):
            If set, only validate the request, but do not
            actually create the node pool.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    azure_node_pool: azure_resources.AzureNodePool = proto.Field(
        proto.MESSAGE,
        number=2,
        message=azure_resources.AzureNodePool,
    )
    azure_node_pool_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class UpdateAzureNodePoolRequest(proto.Message):
    r"""Request message for ``AzureClusters.UpdateAzureNodePool`` method.

    Attributes:
        azure_node_pool (google.cloud.gke_multicloud_v1.types.AzureNodePool):
            Required. The
            [AzureNodePool][google.cloud.gkemulticloud.v1.AzureNodePool]
            resource to update.
        validate_only (bool):
            If set, only validate the request, but don't
            actually update the node pool.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Mask of fields to update. At least one path must
            be supplied in this field. The elements of the repeated
            paths field can only include these fields from
            [AzureNodePool][google.cloud.gkemulticloud.v1.AzureNodePool]:

            \*. ``annotations``.

            - ``version``.
            - ``autoscaling.min_node_count``.
            - ``autoscaling.max_node_count``.
            - ``config.ssh_config.authorized_key``.
            - ``management.auto_repair``.
            - ``management``.
    """

    azure_node_pool: azure_resources.AzureNodePool = proto.Field(
        proto.MESSAGE,
        number=1,
        message=azure_resources.AzureNodePool,
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


class GetAzureNodePoolRequest(proto.Message):
    r"""Request message for ``AzureClusters.GetAzureNodePool`` method.

    Attributes:
        name (str):
            Required. The name of the
            [AzureNodePool][google.cloud.gkemulticloud.v1.AzureNodePool]
            resource to describe.

            ``AzureNodePool`` names are formatted as
            ``projects/<project-id>/locations/<region>/azureClusters/<cluster-id>/azureNodePools/<node-pool-id>``.

            See `Resource
            Names <https://cloud.google.com/apis/design/resource_names>`__
            for more details on Google Cloud resource names.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListAzureNodePoolsRequest(proto.Message):
    r"""Request message for ``AzureClusters.ListAzureNodePools`` method.

    Attributes:
        parent (str):
            Required. The parent ``AzureCluster`` which owns this
            collection of
            [AzureNodePool][google.cloud.gkemulticloud.v1.AzureNodePool]
            resources.

            ``AzureCluster`` names are formatted as
            ``projects/<project-id>/locations/<region>/azureClusters/<cluster-id>``.

            See `Resource
            Names <https://cloud.google.com/apis/design/resource_names>`__
            for more details on Google Cloud resource names.
        page_size (int):
            The maximum number of items to return.

            If not specified, a default value of 50 will be used by the
            service. Regardless of the pageSize value, the response can
            include a partial list and a caller should only rely on
            response's
            [nextPageToken][google.cloud.gkemulticloud.v1.ListAzureNodePoolsResponse.next_page_token]
            to determine if there are more instances left to be queried.
        page_token (str):
            The ``nextPageToken`` value returned from a previous
            [azureNodePools.list][google.cloud.gkemulticloud.v1.AzureClusters.ListAzureNodePools]
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


class ListAzureNodePoolsResponse(proto.Message):
    r"""Response message for ``AzureClusters.ListAzureNodePools`` method.

    Attributes:
        azure_node_pools (MutableSequence[google.cloud.gke_multicloud_v1.types.AzureNodePool]):
            A list of
            [AzureNodePool][google.cloud.gkemulticloud.v1.AzureNodePool]
            resources in the specified ``AzureCluster``.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
    """

    @property
    def raw_page(self):
        return self

    azure_node_pools: MutableSequence[azure_resources.AzureNodePool] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=azure_resources.AzureNodePool,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DeleteAzureNodePoolRequest(proto.Message):
    r"""Request message for ``AzureClusters.DeleteAzureNodePool`` method.

    Attributes:
        name (str):
            Required. The resource name the
            [AzureNodePool][google.cloud.gkemulticloud.v1.AzureNodePool]
            to delete.

            ``AzureNodePool`` names are formatted as
            ``projects/<project-id>/locations/<region>/azureClusters/<cluster-id>/azureNodePools/<node-pool-id>``.

            See `Resource
            Names <https://cloud.google.com/apis/design/resource_names>`__
            for more details on Google Cloud resource names.
        validate_only (bool):
            If set, only validate the request, but do not
            actually delete the node pool.
        allow_missing (bool):
            If set to true, and the
            [AzureNodePool][google.cloud.gkemulticloud.v1.AzureNodePool]
            resource is not found, the request will succeed but no
            action will be taken on the server and a completed
            [Operation][google.longrunning.Operation] will be returned.

            Useful for idempotent deletion.
        etag (str):
            The current ETag of the
            [AzureNodePool][google.cloud.gkemulticloud.v1.AzureNodePool].

            Allows clients to perform deletions through optimistic
            concurrency control.

            If the provided ETag does not match the current etag of the
            node pool, the request will fail and an ABORTED error will
            be returned.
        ignore_errors (bool):
            Optional. If set to true, the deletion of
            [AzureNodePool][google.cloud.gkemulticloud.v1.AzureNodePool]
            resource will succeed even if errors occur during deleting
            in node pool resources. Using this parameter may result in
            orphaned resources in the node pool.
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
    etag: str = proto.Field(
        proto.STRING,
        number=4,
    )
    ignore_errors: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class GetAzureOpenIdConfigRequest(proto.Message):
    r"""GetAzureOpenIdConfigRequest gets the OIDC discovery document
    for the cluster. See the OpenID Connect Discovery 1.0
    specification for details.

    Attributes:
        azure_cluster (str):
            Required. The AzureCluster, which owns the
            OIDC discovery document. Format:

            projects/<project-id>/locations/<region>/azureClusters/<cluster-id>
    """

    azure_cluster: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetAzureJsonWebKeysRequest(proto.Message):
    r"""GetAzureJsonWebKeysRequest gets the public component of the keys
    used by the cluster to sign token requests. This will be the
    jwks_uri for the discover document returned by getOpenIDConfig. See
    the OpenID Connect Discovery 1.0 specification for details.

    Attributes:
        azure_cluster (str):
            Required. The AzureCluster, which owns the JsonWebKeys.
            Format:
            ``projects/<project-id>/locations/<region>/azureClusters/<cluster-id>``
    """

    azure_cluster: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetAzureServerConfigRequest(proto.Message):
    r"""GetAzureServerConfigRequest gets the server config of GKE
    cluster on Azure.

    Attributes:
        name (str):
            Required. The name of the
            [AzureServerConfig][google.cloud.gkemulticloud.v1.AzureServerConfig]
            resource to describe.

            ``AzureServerConfig`` names are formatted as
            ``projects/<project-id>/locations/<region>/azureServerConfig``.

            See `Resource
            Names <https://cloud.google.com/apis/design/resource_names>`__
            for more details on Google Cloud resource names.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateAzureClientRequest(proto.Message):
    r"""Request message for ``AzureClusters.CreateAzureClient`` method.

    Attributes:
        parent (str):
            Required. The parent location where this
            [AzureClient][google.cloud.gkemulticloud.v1.AzureClient]
            resource will be created.

            Location names are formatted as
            ``projects/<project-id>/locations/<region>``.

            See `Resource
            Names <https://cloud.google.com/apis/design/resource_names>`__
            for more details on Google Cloud resource names.
        azure_client (google.cloud.gke_multicloud_v1.types.AzureClient):
            Required. The specification of the
            [AzureClient][google.cloud.gkemulticloud.v1.AzureClient] to
            create.
        azure_client_id (str):
            Required. A client provided ID the resource. Must be unique
            within the parent resource.

            The provided ID will be part of the
            [AzureClient][google.cloud.gkemulticloud.v1.AzureClient]
            resource name formatted as
            ``projects/<project-id>/locations/<region>/azureClients/<client-id>``.

            Valid characters are ``/[a-z][0-9]-/``. Cannot be longer
            than 63 characters.
        validate_only (bool):
            If set, only validate the request, but do not
            actually create the client.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    azure_client: azure_resources.AzureClient = proto.Field(
        proto.MESSAGE,
        number=2,
        message=azure_resources.AzureClient,
    )
    azure_client_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class GetAzureClientRequest(proto.Message):
    r"""Request message for ``AzureClusters.GetAzureClient`` method.

    Attributes:
        name (str):
            Required. The name of the
            [AzureClient][google.cloud.gkemulticloud.v1.AzureClient]
            resource to describe.

            [AzureClient][google.cloud.gkemulticloud.v1.AzureClient]
            names are formatted as
            ``projects/<project-id>/locations/<region>/azureClients/<client-id>``.

            See `Resource
            Names <https://cloud.google.com/apis/design/resource_names>`__
            for more details on Google Cloud resource names.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListAzureClientsRequest(proto.Message):
    r"""Request message for ``AzureClusters.ListAzureClients`` method.

    Attributes:
        parent (str):
            Required. The parent location which owns this collection of
            [AzureClient][google.cloud.gkemulticloud.v1.AzureClient]
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
            [nextPageToken][google.cloud.gkemulticloud.v1.ListAzureClientsResponse.next_page_token]
            to determine if there are more instances left to be queried.
        page_token (str):
            The ``nextPageToken`` value returned from a previous
            [azureClients.list][google.cloud.gkemulticloud.v1.AzureClusters.ListAzureClients]
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


class ListAzureClientsResponse(proto.Message):
    r"""Response message for ``AzureClusters.ListAzureClients`` method.

    Attributes:
        azure_clients (MutableSequence[google.cloud.gke_multicloud_v1.types.AzureClient]):
            A list of
            [AzureClient][google.cloud.gkemulticloud.v1.AzureClient]
            resources in the specified Google Cloud project and region
            region.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
    """

    @property
    def raw_page(self):
        return self

    azure_clients: MutableSequence[azure_resources.AzureClient] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=azure_resources.AzureClient,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DeleteAzureClientRequest(proto.Message):
    r"""Request message for ``AzureClusters.DeleteAzureClient`` method.

    Attributes:
        name (str):
            Required. The resource name the
            [AzureClient][google.cloud.gkemulticloud.v1.AzureClient] to
            delete.

            [AzureClient][google.cloud.gkemulticloud.v1.AzureClient]
            names are formatted as
            ``projects/<project-id>/locations/<region>/azureClients/<client-id>``.

            See `Resource
            Names <https://cloud.google.com/apis/design/resource_names>`__
            for more details on Google Cloud resource names.
        allow_missing (bool):
            If set to true, and the
            [AzureClient][google.cloud.gkemulticloud.v1.AzureClient]
            resource is not found, the request will succeed but no
            action will be taken on the server and a completed
            [Operation][google.longrunning.Operation] will be returned.

            Useful for idempotent deletion.
        validate_only (bool):
            If set, only validate the request, but do not
            actually delete the resource.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    allow_missing: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class GenerateAzureAccessTokenRequest(proto.Message):
    r"""Request message for ``AzureClusters.GenerateAzureAccessToken``
    method.

    Attributes:
        azure_cluster (str):
            Required. The name of the
            [AzureCluster][google.cloud.gkemulticloud.v1.AzureCluster]
            resource to authenticate to.

            ``AzureCluster`` names are formatted as
            ``projects/<project-id>/locations/<region>/azureClusters/<cluster-id>``.

            See `Resource
            Names <https://cloud.google.com/apis/design/resource_names>`__
            for more details on Google Cloud resource names.
    """

    azure_cluster: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GenerateAzureAccessTokenResponse(proto.Message):
    r"""Response message for ``AzureClusters.GenerateAzureAccessToken``
    method.

    Attributes:
        access_token (str):
            Output only. Access token to authenticate to
            k8s api-server.
        expiration_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp at which the token
            will expire.
    """

    access_token: str = proto.Field(
        proto.STRING,
        number=1,
    )
    expiration_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )


class GenerateAzureClusterAgentTokenRequest(proto.Message):
    r"""

    Attributes:
        azure_cluster (str):
            Required.
        subject_token (str):
            Required.
        subject_token_type (str):
            Required.
        version (str):
            Required.
        node_pool_id (str):
            Optional.
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

    azure_cluster: str = proto.Field(
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
    node_pool_id: str = proto.Field(
        proto.STRING,
        number=5,
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


class GenerateAzureClusterAgentTokenResponse(proto.Message):
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
