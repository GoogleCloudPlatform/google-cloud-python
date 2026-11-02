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

from google.cloud.vmwareengine_v1.types import vmwareengine_resources

__protobuf__ = proto.module(
    package="google.cloud.vmwareengine.v1",
    manifest={
        "ListPrivateCloudsRequest",
        "ListPrivateCloudsResponse",
        "GetPrivateCloudRequest",
        "CreatePrivateCloudRequest",
        "UpdatePrivateCloudRequest",
        "DeletePrivateCloudRequest",
        "UndeletePrivateCloudRequest",
        "ListClustersRequest",
        "ListClustersResponse",
        "GetClusterRequest",
        "CreateClusterRequest",
        "UpdateClusterRequest",
        "DeleteClusterRequest",
        "ListNodesRequest",
        "ListNodesResponse",
        "GetNodeRequest",
        "ListExternalAddressesRequest",
        "ListExternalAddressesResponse",
        "FetchNetworkPolicyExternalAddressesRequest",
        "FetchNetworkPolicyExternalAddressesResponse",
        "GetExternalAddressRequest",
        "CreateExternalAddressRequest",
        "UpdateExternalAddressRequest",
        "DeleteExternalAddressRequest",
        "ListSubnetsRequest",
        "ListSubnetsResponse",
        "GetSubnetRequest",
        "UpdateSubnetRequest",
        "ListExternalAccessRulesRequest",
        "ListExternalAccessRulesResponse",
        "GetExternalAccessRuleRequest",
        "CreateExternalAccessRuleRequest",
        "UpdateExternalAccessRuleRequest",
        "DeleteExternalAccessRuleRequest",
        "ListLoggingServersRequest",
        "ListLoggingServersResponse",
        "GetLoggingServerRequest",
        "CreateLoggingServerRequest",
        "UpdateLoggingServerRequest",
        "DeleteLoggingServerRequest",
        "OperationMetadata",
        "ListNodeTypesRequest",
        "ListNodeTypesResponse",
        "GetNodeTypeRequest",
        "ShowNsxCredentialsRequest",
        "ShowVcenterCredentialsRequest",
        "ResetNsxCredentialsRequest",
        "ResetVcenterCredentialsRequest",
        "ListHcxActivationKeysResponse",
        "ListHcxActivationKeysRequest",
        "GetHcxActivationKeyRequest",
        "CreateHcxActivationKeyRequest",
        "GetDnsForwardingRequest",
        "UpdateDnsForwardingRequest",
        "CreateNetworkPeeringRequest",
        "DeleteNetworkPeeringRequest",
        "GetNetworkPeeringRequest",
        "ListNetworkPeeringsRequest",
        "UpdateNetworkPeeringRequest",
        "ListNetworkPeeringsResponse",
        "ListPeeringRoutesRequest",
        "ListPeeringRoutesResponse",
        "ListNetworkPoliciesRequest",
        "ListNetworkPoliciesResponse",
        "GetNetworkPolicyRequest",
        "UpdateNetworkPolicyRequest",
        "CreateNetworkPolicyRequest",
        "DeleteNetworkPolicyRequest",
        "ListManagementDnsZoneBindingsRequest",
        "ListManagementDnsZoneBindingsResponse",
        "GetManagementDnsZoneBindingRequest",
        "CreateManagementDnsZoneBindingRequest",
        "UpdateManagementDnsZoneBindingRequest",
        "DeleteManagementDnsZoneBindingRequest",
        "RepairManagementDnsZoneBindingRequest",
        "CreateVmwareEngineNetworkRequest",
        "UpdateVmwareEngineNetworkRequest",
        "DeleteVmwareEngineNetworkRequest",
        "GetVmwareEngineNetworkRequest",
        "ListVmwareEngineNetworksRequest",
        "ListVmwareEngineNetworksResponse",
        "CreatePrivateConnectionRequest",
        "GetPrivateConnectionRequest",
        "ListPrivateConnectionsRequest",
        "ListPrivateConnectionsResponse",
        "UpdatePrivateConnectionRequest",
        "DeletePrivateConnectionRequest",
        "ListPrivateConnectionPeeringRoutesRequest",
        "ListPrivateConnectionPeeringRoutesResponse",
        "GrantDnsBindPermissionRequest",
        "RevokeDnsBindPermissionRequest",
        "GetDnsBindPermissionRequest",
    },
)


class ListPrivateCloudsRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.ListPrivateClouds][google.cloud.vmwareengine.v1.VmwareEngine.ListPrivateClouds]

    Attributes:
        parent (str):
            Required. The resource name of the private cloud to be
            queried for clusters. Resource names are schemeless URIs
            that follow the conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example: ``projects/my-project/locations/us-central1-a``
        page_size (int):
            The maximum number of private clouds to
            return in one page. The service may return fewer
            than this value. The maximum value is coerced to
            1000.
            The default value of this field is 500.
        page_token (str):
            A page token, received from a previous ``ListPrivateClouds``
            call. Provide this to retrieve the subsequent page.

            When paginating, all other parameters provided to
            ``ListPrivateClouds`` must match the call that provided the
            page token.
        filter (str):
            A filter expression that matches resources returned in the
            response. The expression must specify the field name, a
            comparison operator, and the value that you want to use for
            filtering. The value must be a string, a number, or a
            boolean. The comparison operator must be ``=``, ``!=``,
            ``>``, or ``<``.

            For example, if you are filtering a list of private clouds,
            you can exclude the ones named ``example-pc`` by specifying
            ``name != "example-pc"``.

            You can also filter nested fields. For example, you could
            specify ``networkConfig.managementCidr = "192.168.0.0/24"``
            to include private clouds only if they have a matching
            address in their network configuration.

            To filter on multiple expressions, provide each separate
            expression within parentheses. For example:

            ::

               (name = "example-pc")
               (createTime > "2021-04-12T08:15:10.40Z")

            By default, each expression is an ``AND`` expression.
            However, you can include ``AND`` and ``OR`` expressions
            explicitly. For example:

            ::

               (name = "private-cloud-1") AND
               (createTime > "2021-04-12T08:15:10.40Z") OR
               (name = "private-cloud-2")
        order_by (str):
            Sorts list results by a certain order. By default, returned
            results are ordered by ``name`` in ascending order. You can
            also sort results in descending order based on the ``name``
            value using ``orderBy="name desc"``. Currently, only
            ordering by ``name`` is supported.
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


class ListPrivateCloudsResponse(proto.Message):
    r"""Response message for
    [VmwareEngine.ListPrivateClouds][google.cloud.vmwareengine.v1.VmwareEngine.ListPrivateClouds]

    Attributes:
        private_clouds (MutableSequence[google.cloud.vmwareengine_v1.types.PrivateCloud]):
            A list of private clouds.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        unreachable (MutableSequence[str]):
            Locations that could not be reached when
            making an aggregated query using wildcards.
    """

    @property
    def raw_page(self):
        return self

    private_clouds: MutableSequence[vmwareengine_resources.PrivateCloud] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=vmwareengine_resources.PrivateCloud,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetPrivateCloudRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.GetPrivateCloud][google.cloud.vmwareengine.v1.VmwareEngine.GetPrivateCloud]

    Attributes:
        name (str):
            Required. The resource name of the private cloud to
            retrieve. Resource names are schemeless URIs that follow the
            conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example:
            ``projects/my-project/locations/us-central1-a/privateClouds/my-cloud``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreatePrivateCloudRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.CreatePrivateCloud][google.cloud.vmwareengine.v1.VmwareEngine.CreatePrivateCloud]

    Attributes:
        parent (str):
            Required. The resource name of the location to create the
            new private cloud in. Resource names are schemeless URIs
            that follow the conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example: ``projects/my-project/locations/us-central1-a``
        private_cloud_id (str):
            Required. The user-provided identifier of the private cloud
            to be created. This identifier must be unique among each
            ``PrivateCloud`` within the parent and becomes the final
            token in the name URI. The identifier must meet the
            following requirements:

            - Only contains 1-63 alphanumeric characters and hyphens
            - Begins with an alphabetical character
            - Ends with a non-hyphen character
            - Not formatted as a UUID
            - Complies with `RFC
              1034 <https://datatracker.ietf.org/doc/html/rfc1034>`__
              (section 3.5)
        private_cloud (google.cloud.vmwareengine_v1.types.PrivateCloud):
            Required. The initial description of the new
            private cloud.
        request_id (str):
            Optional. The request ID must be a valid UUID
            with the exception that zero UUID is not
            supported
            (00000000-0000-0000-0000-000000000000).
        validate_only (bool):
            Optional. True if you want the request to be
            validated and not executed; false otherwise.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    private_cloud_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    private_cloud: vmwareengine_resources.PrivateCloud = proto.Field(
        proto.MESSAGE,
        number=3,
        message=vmwareengine_resources.PrivateCloud,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class UpdatePrivateCloudRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.UpdatePrivateCloud][google.cloud.vmwareengine.v1.VmwareEngine.UpdatePrivateCloud]

    Attributes:
        private_cloud (google.cloud.vmwareengine_v1.types.PrivateCloud):
            Required. Private cloud description.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask is used to specify the fields to be
            overwritten in the ``PrivateCloud`` resource by the update.
            The fields specified in ``updateMask`` are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask. If the user does not provide a mask
            then all fields will be overwritten.
        request_id (str):
            Optional. The request ID must be a valid UUID
            with the exception that zero UUID is not
            supported
            (00000000-0000-0000-0000-000000000000).
    """

    private_cloud: vmwareengine_resources.PrivateCloud = proto.Field(
        proto.MESSAGE,
        number=1,
        message=vmwareengine_resources.PrivateCloud,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeletePrivateCloudRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.DeletePrivateCloud][google.cloud.vmwareengine.v1.VmwareEngine.DeletePrivateCloud]


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Required. The resource name of the private cloud to delete.
            Resource names are schemeless URIs that follow the
            conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example:
            ``projects/my-project/locations/us-central1-a/privateClouds/my-cloud``
        request_id (str):
            Optional. The request ID must be a valid UUID
            with the exception that zero UUID is not
            supported
            (00000000-0000-0000-0000-000000000000).
        force (bool):
            Optional. If set to true, cascade delete is
            enabled and all children of this private cloud
            resource are also deleted. When this flag is set
            to false, the private cloud will not be deleted
            if there are any children other than the
            management cluster. The management cluster is
            always deleted.
        delay_hours (int):
            Optional. Time delay of the deletion specified in hours. The
            default value is ``3``. Specifying a non-zero value for this
            field changes the value of ``PrivateCloud.state`` to
            ``DELETED`` and sets ``expire_time`` to the planned deletion
            time. Deletion can be cancelled before ``expire_time``
            elapses using
            [VmwareEngine.UndeletePrivateCloud][google.cloud.vmwareengine.v1.VmwareEngine.UndeletePrivateCloud].
            Specifying a value of ``0`` for this field instead begins
            the deletion process and ceases billing immediately. During
            the final deletion process, the value of
            ``PrivateCloud.state`` becomes ``PURGING``.

            This field is a member of `oneof`_ ``_delay_hours``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    delay_hours: int = proto.Field(
        proto.INT32,
        number=4,
        optional=True,
    )


class UndeletePrivateCloudRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.UndeletePrivateCloud][google.cloud.vmwareengine.v1.VmwareEngine.UndeletePrivateCloud]

    Attributes:
        name (str):
            Required. The resource name of the private cloud scheduled
            for deletion. Resource names are schemeless URIs that follow
            the conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example:
            ``projects/my-project/locations/us-central1-a/privateClouds/my-cloud``
        request_id (str):
            Optional. The request ID must be a valid UUID
            with the exception that zero UUID is not
            supported
            (00000000-0000-0000-0000-000000000000).
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListClustersRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.ListClusters][google.cloud.vmwareengine.v1.VmwareEngine.ListClusters]

    Attributes:
        parent (str):
            Required. The resource name of the private cloud to query
            for clusters. Resource names are schemeless URIs that follow
            the conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example:
            ``projects/my-project/locations/us-central1-a/privateClouds/my-cloud``
        page_size (int):
            The maximum number of clusters to return in
            one page. The service may return fewer than this
            value. The maximum value is coerced to 1000.
            The default value of this field is 500.
        page_token (str):
            A page token, received from a previous ``ListClusters``
            call. Provide this to retrieve the subsequent page.

            When paginating, all other parameters provided to
            ``ListClusters`` must match the call that provided the page
            token.
        filter (str):
            To filter on multiple expressions, provide each separate
            expression within parentheses. For example:

            ::

               (name = "example-cluster")
               (nodeCount = "3")

            By default, each expression is an ``AND`` expression.
            However, you can include ``AND`` and ``OR`` expressions
            explicitly. For example:

            ::

               (name = "example-cluster-1") AND
               (createTime > "2021-04-12T08:15:10.40Z") OR
               (name = "example-cluster-2")
        order_by (str):
            Sorts list results by a certain order. By default, returned
            results are ordered by ``name`` in ascending order. You can
            also sort results in descending order based on the ``name``
            value using ``orderBy="name desc"``. Currently, only
            ordering by ``name`` is supported.
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
    [VmwareEngine.ListClusters][google.cloud.vmwareengine.v1.VmwareEngine.ListClusters]

    Attributes:
        clusters (MutableSequence[google.cloud.vmwareengine_v1.types.Cluster]):
            A list of private cloud clusters.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        unreachable (MutableSequence[str]):
            Locations that could not be reached when
            making an aggregated query using wildcards.
    """

    @property
    def raw_page(self):
        return self

    clusters: MutableSequence[vmwareengine_resources.Cluster] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=vmwareengine_resources.Cluster,
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
    [VmwareEngine.GetCluster][google.cloud.vmwareengine.v1.VmwareEngine.GetCluster]

    Attributes:
        name (str):
            Required. The cluster resource name to retrieve. Resource
            names are schemeless URIs that follow the conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example:
            ``projects/my-project/locations/us-central1-a/privateClouds/my-cloud/clusters/my-cluster``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateClusterRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.CreateCluster][google.cloud.vmwareengine.v1.VmwareEngine.CreateCluster]

    Attributes:
        parent (str):
            Required. The resource name of the private cloud to create a
            new cluster in. Resource names are schemeless URIs that
            follow the conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example:
            ``projects/my-project/locations/us-central1-a/privateClouds/my-cloud``
        cluster_id (str):
            Required. The user-provided identifier of the new
            ``Cluster``. This identifier must be unique among clusters
            within the parent and becomes the final token in the name
            URI. The identifier must meet the following requirements:

            - Only contains 1-63 alphanumeric characters and hyphens
            - Begins with an alphabetical character
            - Ends with a non-hyphen character
            - Not formatted as a UUID
            - Complies with `RFC
              1034 <https://datatracker.ietf.org/doc/html/rfc1034>`__
              (section 3.5)
        cluster (google.cloud.vmwareengine_v1.types.Cluster):
            Required. The initial description of the new
            cluster.
        request_id (str):
            Optional. The request ID must be a valid UUID
            with the exception that zero UUID is not
            supported
            (00000000-0000-0000-0000-000000000000).
        validate_only (bool):
            Optional. True if you want the request to be
            validated and not executed; false otherwise.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    cluster_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    cluster: vmwareengine_resources.Cluster = proto.Field(
        proto.MESSAGE,
        number=3,
        message=vmwareengine_resources.Cluster,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class UpdateClusterRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.UpdateCluster][google.cloud.vmwareengine.v1.VmwareEngine.UpdateCluster]

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask is used to specify the fields to be
            overwritten in the ``Cluster`` resource by the update. The
            fields specified in the ``updateMask`` are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask. If the user does not provide a mask
            then all fields will be overwritten.
        cluster (google.cloud.vmwareengine_v1.types.Cluster):
            Required. The description of the cluster.
        request_id (str):
            Optional. The request ID must be a valid UUID
            with the exception that zero UUID is not
            supported
            (00000000-0000-0000-0000-000000000000).
        validate_only (bool):
            Optional. True if you want the request to be
            validated and not executed; false otherwise.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    cluster: vmwareengine_resources.Cluster = proto.Field(
        proto.MESSAGE,
        number=2,
        message=vmwareengine_resources.Cluster,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class DeleteClusterRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.DeleteCluster][google.cloud.vmwareengine.v1.VmwareEngine.DeleteCluster]

    Attributes:
        name (str):
            Required. The resource name of the cluster to delete.
            Resource names are schemeless URIs that follow the
            conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example:
            ``projects/my-project/locations/us-central1-a/privateClouds/my-cloud/clusters/my-cluster``
        request_id (str):
            Optional. The request ID must be a valid UUID
            with the exception that zero UUID is not
            supported
            (00000000-0000-0000-0000-000000000000).
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListNodesRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.ListNodes][google.cloud.vmwareengine.v1.VmwareEngine.ListNodes]

    Attributes:
        parent (str):
            Required. The resource name of the cluster to be queried for
            nodes. Resource names are schemeless URIs that follow the
            conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example:
            ``projects/my-project/locations/us-central1-a/privateClouds/my-cloud/clusters/my-cluster``
        page_size (int):
            The maximum number of nodes to return in one
            page. The service may return fewer than this
            value. The maximum value is coerced to 1000.
            The default value of this field is 500.
        page_token (str):
            A page token, received from a previous ``ListNodes`` call.
            Provide this to retrieve the subsequent page.

            When paginating, all other parameters provided to
            ``ListNodes`` must match the call that provided the page
            token.
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


class ListNodesResponse(proto.Message):
    r"""Response message for
    [VmwareEngine.ListNodes][google.cloud.vmwareengine.v1.VmwareEngine.ListNodes]

    Attributes:
        nodes (MutableSequence[google.cloud.vmwareengine_v1.types.Node]):
            The nodes.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    nodes: MutableSequence[vmwareengine_resources.Node] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=vmwareengine_resources.Node,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetNodeRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.GetNode][google.cloud.vmwareengine.v1.VmwareEngine.GetNode]

    Attributes:
        name (str):
            Required. The resource name of the node to retrieve. For
            example:
            ``projects/{project}/locations/{location}/privateClouds/{private_cloud}/clusters/{cluster}/nodes/{node}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListExternalAddressesRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.ListExternalAddresses][google.cloud.vmwareengine.v1.VmwareEngine.ListExternalAddresses]

    Attributes:
        parent (str):
            Required. The resource name of the private cloud to be
            queried for external IP addresses. Resource names are
            schemeless URIs that follow the conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example:
            ``projects/my-project/locations/us-central1-a/privateClouds/my-cloud``
        page_size (int):
            The maximum number of external IP addresses
            to return in one page. The service may return
            fewer than this value. The maximum value is
            coerced to 1000.
            The default value of this field is 500.
        page_token (str):
            A page token, received from a previous
            ``ListExternalAddresses`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListExternalAddresses`` must match the call that provided
            the page token.
        filter (str):
            A filter expression that matches resources returned in the
            response. The expression must specify the field name, a
            comparison operator, and the value that you want to use for
            filtering. The value must be a string, a number, or a
            boolean. The comparison operator must be ``=``, ``!=``,
            ``>``, or ``<``.

            For example, if you are filtering a list of IP addresses,
            you can exclude the ones named ``example-ip`` by specifying
            ``name != "example-ip"``.

            To filter on multiple expressions, provide each separate
            expression within parentheses. For example:

            ::

               (name = "example-ip")
               (createTime > "2021-04-12T08:15:10.40Z")

            By default, each expression is an ``AND`` expression.
            However, you can include ``AND`` and ``OR`` expressions
            explicitly. For example:

            ::

               (name = "example-ip-1") AND
               (createTime > "2021-04-12T08:15:10.40Z") OR
               (name = "example-ip-2")
        order_by (str):
            Sorts list results by a certain order. By default, returned
            results are ordered by ``name`` in ascending order. You can
            also sort results in descending order based on the ``name``
            value using ``orderBy="name desc"``. Currently, only
            ordering by ``name`` is supported.
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


class ListExternalAddressesResponse(proto.Message):
    r"""Response message for
    [VmwareEngine.ListExternalAddresses][google.cloud.vmwareengine.v1.VmwareEngine.ListExternalAddresses]

    Attributes:
        external_addresses (MutableSequence[google.cloud.vmwareengine_v1.types.ExternalAddress]):
            A list of external IP addresses.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        unreachable (MutableSequence[str]):
            Locations that could not be reached when
            making an aggregated query using wildcards.
    """

    @property
    def raw_page(self):
        return self

    external_addresses: MutableSequence[vmwareengine_resources.ExternalAddress] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=vmwareengine_resources.ExternalAddress,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class FetchNetworkPolicyExternalAddressesRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.FetchNetworkPolicyExternalAddresses][google.cloud.vmwareengine.v1.VmwareEngine.FetchNetworkPolicyExternalAddresses]

    Attributes:
        network_policy (str):
            Required. The resource name of the network policy to query
            for assigned external IP addresses. Resource names are
            schemeless URIs that follow the conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example:
            ``projects/my-project/locations/us-central1/networkPolicies/my-policy``
        page_size (int):
            The maximum number of external IP addresses
            to return in one page. The service may return
            fewer than this value. The maximum value is
            coerced to 1000.
            The default value of this field is 500.
        page_token (str):
            A page token, received from a previous
            ``FetchNetworkPolicyExternalAddresses`` call. Provide this
            to retrieve the subsequent page.

            When paginating, all parameters provided to
            ``FetchNetworkPolicyExternalAddresses``, except for
            ``page_size`` and ``page_token``, must match the call that
            provided the page token.
    """

    network_policy: str = proto.Field(
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


class FetchNetworkPolicyExternalAddressesResponse(proto.Message):
    r"""Response message for
    [VmwareEngine.FetchNetworkPolicyExternalAddresses][google.cloud.vmwareengine.v1.VmwareEngine.FetchNetworkPolicyExternalAddresses]

    Attributes:
        external_addresses (MutableSequence[google.cloud.vmwareengine_v1.types.ExternalAddress]):
            A list of external IP addresses assigned to
            VMware workload VMs within the scope of the
            given network policy.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    external_addresses: MutableSequence[vmwareengine_resources.ExternalAddress] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=vmwareengine_resources.ExternalAddress,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetExternalAddressRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.GetExternalAddress][google.cloud.vmwareengine.v1.VmwareEngine.GetExternalAddress]

    Attributes:
        name (str):
            Required. The resource name of the external IP address to
            retrieve. Resource names are schemeless URIs that follow the
            conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example:
            ``projects/my-project/locations/us-central1-a/privateClouds/my-cloud/externalAddresses/my-ip``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateExternalAddressRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.CreateExternalAddress][google.cloud.vmwareengine.v1.VmwareEngine.CreateExternalAddress]

    Attributes:
        parent (str):
            Required. The resource name of the private cloud to create a
            new external IP address in. Resource names are schemeless
            URIs that follow the conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example:
            ``projects/my-project/locations/us-central1-a/privateClouds/my-cloud``
        external_address (google.cloud.vmwareengine_v1.types.ExternalAddress):
            Required. The initial description of a new
            external IP address.
        external_address_id (str):
            Required. The user-provided identifier of the
            ``ExternalAddress`` to be created. This identifier must be
            unique among ``ExternalAddress`` resources within the parent
            and becomes the final token in the name URI. The identifier
            must meet the following requirements:

            - Only contains 1-63 alphanumeric characters and hyphens
            - Begins with an alphabetical character
            - Ends with a non-hyphen character
            - Not formatted as a UUID
            - Complies with `RFC
              1034 <https://datatracker.ietf.org/doc/html/rfc1034>`__
              (section 3.5)
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server guarantees that a request
            doesn't result in creation of duplicate
            commitments for at least 60 minutes.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if the original
            operation with the same request ID was received,
            and if so, will ignore the second request. This
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
    external_address: vmwareengine_resources.ExternalAddress = proto.Field(
        proto.MESSAGE,
        number=2,
        message=vmwareengine_resources.ExternalAddress,
    )
    external_address_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateExternalAddressRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.UpdateExternalAddress][google.cloud.vmwareengine.v1.VmwareEngine.UpdateExternalAddress]

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask is used to specify the fields to be
            overwritten in the ``ExternalAddress`` resource by the
            update. The fields specified in the ``update_mask`` are
            relative to the resource, not the full request. A field will
            be overwritten if it is in the mask. If the user does not
            provide a mask then all fields will be overwritten.
        external_address (google.cloud.vmwareengine_v1.types.ExternalAddress):
            Required. External IP address description.
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server guarantees that a request
            doesn't result in creation of duplicate
            commitments for at least 60 minutes.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if the original
            operation with the same request ID was received,
            and if so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    external_address: vmwareengine_resources.ExternalAddress = proto.Field(
        proto.MESSAGE,
        number=2,
        message=vmwareengine_resources.ExternalAddress,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteExternalAddressRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.DeleteExternalAddress][google.cloud.vmwareengine.v1.VmwareEngine.DeleteExternalAddress]

    Attributes:
        name (str):
            Required. The resource name of the external IP address to
            delete. Resource names are schemeless URIs that follow the
            conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example:
            ``projects/my-project/locations/us-central1-a/privateClouds/my-cloud/externalAddresses/my-ip``
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server guarantees that a request
            doesn't result in creation of duplicate
            commitments for at least 60 minutes.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if the original
            operation with the same request ID was received,
            and if so, will ignore the second request. This
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
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListSubnetsRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.ListSubnets][google.cloud.vmwareengine.v1.VmwareEngine.ListSubnets]

    Attributes:
        parent (str):
            Required. The resource name of the private cloud to be
            queried for subnets. Resource names are schemeless URIs that
            follow the conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example:
            ``projects/my-project/locations/us-central1-a/privateClouds/my-cloud``
        page_size (int):
            The maximum number of subnets to return in
            one page. The service may return fewer than this
            value. The maximum value is coerced to 1000.
            The default value of this field is 500.
        page_token (str):
            A page token, received from a previous
            ``ListSubnetsRequest`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListSubnetsRequest`` must match the call that provided the
            page token.
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


class ListSubnetsResponse(proto.Message):
    r"""Response message for
    [VmwareEngine.ListSubnets][google.cloud.vmwareengine.v1.VmwareEngine.ListSubnets]

    Attributes:
        subnets (MutableSequence[google.cloud.vmwareengine_v1.types.Subnet]):
            A list of subnets.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        unreachable (MutableSequence[str]):
            Locations that could not be reached when
            making an aggregated query using wildcards.
    """

    @property
    def raw_page(self):
        return self

    subnets: MutableSequence[vmwareengine_resources.Subnet] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=vmwareengine_resources.Subnet,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetSubnetRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.GetSubnet][google.cloud.vmwareengine.v1.VmwareEngine.GetSubnet]

    Attributes:
        name (str):
            Required. The resource name of the subnet to retrieve.
            Resource names are schemeless URIs that follow the
            conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example:
            ``projects/my-project/locations/us-central1-a/privateClouds/my-cloud/subnets/my-subnet``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateSubnetRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.UpdateSubnet][google.cloud.vmwareengine.v1.VmwareEngine.UpdateSubnet]

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask is used to specify the fields to be
            overwritten in the ``Subnet`` resource by the update. The
            fields specified in the ``update_mask`` are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask. If the user does not provide a mask
            then all fields will be overwritten.
        subnet (google.cloud.vmwareengine_v1.types.Subnet):
            Required. Subnet description.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    subnet: vmwareengine_resources.Subnet = proto.Field(
        proto.MESSAGE,
        number=2,
        message=vmwareengine_resources.Subnet,
    )


class ListExternalAccessRulesRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.ListExternalAccessRules][google.cloud.vmwareengine.v1.VmwareEngine.ListExternalAccessRules]

    Attributes:
        parent (str):
            Required. The resource name of the network policy to query
            for external access firewall rules. Resource names are
            schemeless URIs that follow the conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example:
            ``projects/my-project/locations/us-central1/networkPolicies/my-policy``
        page_size (int):
            The maximum number of external access rules
            to return in one page. The service may return
            fewer than this value. The maximum value is
            coerced to 1000.
            The default value of this field is 500.
        page_token (str):
            A page token, received from a previous
            ``ListExternalAccessRulesRequest`` call. Provide this to
            retrieve the subsequent page.

            When paginating, all other parameters provided to
            ``ListExternalAccessRulesRequest`` must match the call that
            provided the page token.
        filter (str):
            A filter expression that matches resources returned in the
            response. The expression must specify the field name, a
            comparison operator, and the value that you want to use for
            filtering. The value must be a string, a number, or a
            boolean. The comparison operator must be ``=``, ``!=``,
            ``>``, or ``<``.

            For example, if you are filtering a list of external access
            rules, you can exclude the ones named ``example-rule`` by
            specifying ``name != "example-rule"``.

            To filter on multiple expressions, provide each separate
            expression within parentheses. For example:

            ::

               (name = "example-rule")
               (createTime > "2021-04-12T08:15:10.40Z")

            By default, each expression is an ``AND`` expression.
            However, you can include ``AND`` and ``OR`` expressions
            explicitly. For example:

            ::

               (name = "example-rule-1") AND
               (createTime > "2021-04-12T08:15:10.40Z") OR
               (name = "example-rule-2")
        order_by (str):
            Sorts list results by a certain order. By default, returned
            results are ordered by ``name`` in ascending order. You can
            also sort results in descending order based on the ``name``
            value using ``orderBy="name desc"``. Currently, only
            ordering by ``name`` is supported.
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


class ListExternalAccessRulesResponse(proto.Message):
    r"""Response message for
    [VmwareEngine.ListExternalAccessRules][google.cloud.vmwareengine.v1.VmwareEngine.ListExternalAccessRules]

    Attributes:
        external_access_rules (MutableSequence[google.cloud.vmwareengine_v1.types.ExternalAccessRule]):
            A list of external access firewall rules.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        unreachable (MutableSequence[str]):
            Locations that could not be reached when
            making an aggregated query using wildcards.
    """

    @property
    def raw_page(self):
        return self

    external_access_rules: MutableSequence[
        vmwareengine_resources.ExternalAccessRule
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=vmwareengine_resources.ExternalAccessRule,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetExternalAccessRuleRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.GetExternalAccessRule][google.cloud.vmwareengine.v1.VmwareEngine.GetExternalAccessRule]

    Attributes:
        name (str):
            Required. The resource name of the external access firewall
            rule to retrieve. Resource names are schemeless URIs that
            follow the conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example:
            ``projects/my-project/locations/us-central1/networkPolicies/my-policy/externalAccessRules/my-rule``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateExternalAccessRuleRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.CreateExternalAccessRule][google.cloud.vmwareengine.v1.VmwareEngine.CreateExternalAccessRule]

    Attributes:
        parent (str):
            Required. The resource name of the network policy to create
            a new external access firewall rule in. Resource names are
            schemeless URIs that follow the conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example:
            ``projects/my-project/locations/us-central1/networkPolicies/my-policy``
        external_access_rule (google.cloud.vmwareengine_v1.types.ExternalAccessRule):
            Required. The initial description of a new
            external access rule.
        external_access_rule_id (str):
            Required. The user-provided identifier of the
            ``ExternalAccessRule`` to be created. This identifier must
            be unique among ``ExternalAccessRule`` resources within the
            parent and becomes the final token in the name URI. The
            identifier must meet the following requirements:

            - Only contains 1-63 alphanumeric characters and hyphens
            - Begins with an alphabetical character
            - Ends with a non-hyphen character
            - Not formatted as a UUID
            - Complies with `RFC
              1034 <https://datatracker.ietf.org/doc/html/rfc1034>`__
              (section 3.5)
        request_id (str):
            A request ID to identify requests. Specify a
            unique request ID so that if you must retry your
            request, the server will know to ignore the
            request if it has already been completed. The
            server guarantees that a request doesn't result
            in creation of duplicate commitments for at
            least 60 minutes.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if the original
            operation with the same request ID was received,
            and if so, will ignore the second request. This
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
    external_access_rule: vmwareengine_resources.ExternalAccessRule = proto.Field(
        proto.MESSAGE,
        number=2,
        message=vmwareengine_resources.ExternalAccessRule,
    )
    external_access_rule_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateExternalAccessRuleRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.UpdateExternalAccessRule][google.cloud.vmwareengine.v1.VmwareEngine.UpdateExternalAccessRule]

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask is used to specify the fields to be
            overwritten in the ``ExternalAccessRule`` resource by the
            update. The fields specified in the ``update_mask`` are
            relative to the resource, not the full request. A field will
            be overwritten if it is in the mask. If the user does not
            provide a mask then all fields will be overwritten.
        external_access_rule (google.cloud.vmwareengine_v1.types.ExternalAccessRule):
            Required. Description of the external access
            rule.
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server guarantees that a request
            doesn't result in creation of duplicate
            commitments for at least 60 minutes.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if the original
            operation with the same request ID was received,
            and if so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    external_access_rule: vmwareengine_resources.ExternalAccessRule = proto.Field(
        proto.MESSAGE,
        number=2,
        message=vmwareengine_resources.ExternalAccessRule,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteExternalAccessRuleRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.DeleteExternalAccessRule][google.cloud.vmwareengine.v1.VmwareEngine.DeleteExternalAccessRule]

    Attributes:
        name (str):
            Required. The resource name of the external access firewall
            rule to delete. Resource names are schemeless URIs that
            follow the conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example:
            ``projects/my-project/locations/us-central1/networkPolicies/my-policy/externalAccessRules/my-rule``
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server guarantees that a request
            doesn't result in creation of duplicate
            commitments for at least 60 minutes.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if the original
            operation with the same request ID was received,
            and if so, will ignore the second request. This
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
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListLoggingServersRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.ListLoggingServers][google.cloud.vmwareengine.v1.VmwareEngine.ListLoggingServers]

    Attributes:
        parent (str):
            Required. The resource name of the private cloud to be
            queried for logging servers. Resource names are schemeless
            URIs that follow the conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example:
            ``projects/my-project/locations/us-central1-a/privateClouds/my-cloud``
        page_size (int):
            The maximum number of logging servers to
            return in one page. The service may return fewer
            than this value. The maximum value is coerced to
            1000.
            The default value of this field is 500.
        page_token (str):
            A page token, received from a previous
            ``ListLoggingServersRequest`` call. Provide this to retrieve
            the subsequent page.

            When paginating, all other parameters provided to
            ``ListLoggingServersRequest`` must match the call that
            provided the page token.
        filter (str):
            A filter expression that matches resources returned in the
            response. The expression must specify the field name, a
            comparison operator, and the value that you want to use for
            filtering. The value must be a string, a number, or a
            boolean. The comparison operator must be ``=``, ``!=``,
            ``>``, or ``<``.

            For example, if you are filtering a list of logging servers,
            you can exclude the ones named ``example-server`` by
            specifying ``name != "example-server"``.

            To filter on multiple expressions, provide each separate
            expression within parentheses. For example:

            ::

               (name = "example-server")
               (createTime > "2021-04-12T08:15:10.40Z")

            By default, each expression is an ``AND`` expression.
            However, you can include ``AND`` and ``OR`` expressions
            explicitly. For example:

            ::

               (name = "example-server-1") AND
               (createTime > "2021-04-12T08:15:10.40Z") OR
               (name = "example-server-2")
        order_by (str):
            Sorts list results by a certain order. By default, returned
            results are ordered by ``name`` in ascending order. You can
            also sort results in descending order based on the ``name``
            value using ``orderBy="name desc"``. Currently, only
            ordering by ``name`` is supported.
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


class ListLoggingServersResponse(proto.Message):
    r"""Response message for
    [VmwareEngine.ListLoggingServers][google.cloud.vmwareengine.v1.VmwareEngine.ListLoggingServers]

    Attributes:
        logging_servers (MutableSequence[google.cloud.vmwareengine_v1.types.LoggingServer]):
            A list of Logging Servers.
        next_page_token (str):
            A token, which can be send as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        unreachable (MutableSequence[str]):
            Locations that could not be reached when
            making an aggregated query using wildcards.
    """

    @property
    def raw_page(self):
        return self

    logging_servers: MutableSequence[vmwareengine_resources.LoggingServer] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=vmwareengine_resources.LoggingServer,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetLoggingServerRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.GetLoggingServer][google.cloud.vmwareengine.v1.VmwareEngine.GetLoggingServer]

    Attributes:
        name (str):
            Required. The resource name of the Logging Server to
            retrieve. Resource names are schemeless URIs that follow the
            conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example:
            ``projects/my-project/locations/us-central1-a/privateClouds/my-cloud/loggingServers/my-logging-server``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateLoggingServerRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.CreateLoggingServer][google.cloud.vmwareengine.v1.VmwareEngine.CreateLoggingServer]

    Attributes:
        parent (str):
            Required. The resource name of the private cloud to create a
            new Logging Server in. Resource names are schemeless URIs
            that follow the conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example:
            ``projects/my-project/locations/us-central1-a/privateClouds/my-cloud``
        logging_server (google.cloud.vmwareengine_v1.types.LoggingServer):
            Required. The initial description of a new
            logging server.
        logging_server_id (str):
            Required. The user-provided identifier of the
            ``LoggingServer`` to be created. This identifier must be
            unique among ``LoggingServer`` resources within the parent
            and becomes the final token in the name URI. The identifier
            must meet the following requirements:

            - Only contains 1-63 alphanumeric characters and hyphens
            - Begins with an alphabetical character
            - Ends with a non-hyphen character
            - Not formatted as a UUID
            - Complies with `RFC
              1034 <https://datatracker.ietf.org/doc/html/rfc1034>`__
              (section 3.5)
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server guarantees that a request
            doesn't result in creation of duplicate
            commitments for at least 60 minutes.

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
    logging_server: vmwareengine_resources.LoggingServer = proto.Field(
        proto.MESSAGE,
        number=2,
        message=vmwareengine_resources.LoggingServer,
    )
    logging_server_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateLoggingServerRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.UpdateLoggingServer][google.cloud.vmwareengine.v1.VmwareEngine.UpdateLoggingServer]

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask is used to specify the fields to be
            overwritten in the ``LoggingServer`` resource by the update.
            The fields specified in the ``update_mask`` are relative to
            the resource, not the full request. A field will be
            overwritten if it is in the mask. If the user does not
            provide a mask then all fields will be overwritten.
        logging_server (google.cloud.vmwareengine_v1.types.LoggingServer):
            Required. Logging server description.
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server guarantees that a request
            doesn't result in creation of duplicate
            commitments for at least 60 minutes.

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

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    logging_server: vmwareengine_resources.LoggingServer = proto.Field(
        proto.MESSAGE,
        number=2,
        message=vmwareengine_resources.LoggingServer,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteLoggingServerRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.DeleteLoggingServer][google.cloud.vmwareengine.v1.VmwareEngine.DeleteLoggingServer]

    Attributes:
        name (str):
            Required. The resource name of the logging server to delete.
            Resource names are schemeless URIs that follow the
            conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example:
            ``projects/my-project/locations/us-central1-a/privateClouds/my-cloud/loggingServers/my-logging-server``
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server guarantees that a request
            doesn't result in creation of duplicate
            commitments for at least 60 minutes.

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
    request_id: str = proto.Field(
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
        status_message (str):
            Output only. Human-readable status of the
            operation, if any.
        requested_cancellation (bool):
            Output only. True if the user has requested cancellation of
            the operation; false otherwise. Operations that have
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


class ListNodeTypesRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.ListNodeTypes][google.cloud.vmwareengine.v1.VmwareEngine.ListNodeTypes]

    Attributes:
        parent (str):
            Required. The resource name of the location to be queried
            for node types. Resource names are schemeless URIs that
            follow the conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example: ``projects/my-project/locations/us-central1-a``
        page_size (int):
            The maximum number of node types to return in
            one page. The service may return fewer than this
            value. The maximum value is coerced to 1000.
            The default value of this field is 500.
        page_token (str):
            A page token, received from a previous ``ListNodeTypes``
            call. Provide this to retrieve the subsequent page.

            When paginating, all other parameters provided to
            ``ListNodeTypes`` must match the call that provided the page
            token.
        filter (str):
            A filter expression that matches resources returned in the
            response. The expression must specify the field name, a
            comparison operator, and the value that you want to use for
            filtering. The value must be a string, a number, or a
            boolean. The comparison operator must be ``=``, ``!=``,
            ``>``, or ``<``.

            For example, if you are filtering a list of node types, you
            can exclude the ones named ``standard-72`` by specifying
            ``name != "standard-72"``.

            To filter on multiple expressions, provide each separate
            expression within parentheses. For example:

            ::

               (name = "standard-72")
               (virtual_cpu_count > 2)

            By default, each expression is an ``AND`` expression.
            However, you can include ``AND`` and ``OR`` expressions
            explicitly. For example:

            ::

               (name = "standard-96") AND
               (virtual_cpu_count > 2) OR
               (name = "standard-72")
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


class ListNodeTypesResponse(proto.Message):
    r"""Response message for
    [VmwareEngine.ListNodeTypes][google.cloud.vmwareengine.v1.VmwareEngine.ListNodeTypes]

    Attributes:
        node_types (MutableSequence[google.cloud.vmwareengine_v1.types.NodeType]):
            A list of Node Types.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        unreachable (MutableSequence[str]):
            Locations that could not be reached when
            making an aggregated query using wildcards.
    """

    @property
    def raw_page(self):
        return self

    node_types: MutableSequence[vmwareengine_resources.NodeType] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=vmwareengine_resources.NodeType,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetNodeTypeRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.GetNodeType][google.cloud.vmwareengine.v1.VmwareEngine.GetNodeType]

    Attributes:
        name (str):
            Required. The resource name of the node type to retrieve.
            Resource names are schemeless URIs that follow the
            conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example:
            ``projects/my-proj/locations/us-central1-a/nodeTypes/standard-72``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ShowNsxCredentialsRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.ShowNsxCredentials][google.cloud.vmwareengine.v1.VmwareEngine.ShowNsxCredentials]

    Attributes:
        private_cloud (str):
            Required. The resource name of the private cloud to be
            queried for credentials. Resource names are schemeless URIs
            that follow the conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example:
            ``projects/my-project/locations/us-central1-a/privateClouds/my-cloud``
    """

    private_cloud: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ShowVcenterCredentialsRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.ShowVcenterCredentials][google.cloud.vmwareengine.v1.VmwareEngine.ShowVcenterCredentials]

    Attributes:
        private_cloud (str):
            Required. The resource name of the private cloud to be
            queried for credentials. Resource names are schemeless URIs
            that follow the conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example:
            ``projects/my-project/locations/us-central1-a/privateClouds/my-cloud``
        username (str):
            Optional. The username of the user to be
            queried for credentials. The default value of
            this field is CloudOwner@gve.local. The provided
            value must be one of the following:

            CloudOwner@gve.local,
            solution-user-01@gve.local,
            solution-user-02@gve.local,
            solution-user-03@gve.local,
            solution-user-04@gve.local,
            solution-user-05@gve.local,
            zertoadmin@gve.local.
    """

    private_cloud: str = proto.Field(
        proto.STRING,
        number=1,
    )
    username: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ResetNsxCredentialsRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.ResetNsxCredentials][google.cloud.vmwareengine.v1.VmwareEngine.ResetNsxCredentials]

    Attributes:
        private_cloud (str):
            Required. The resource name of the private cloud to reset
            credentials for. Resource names are schemeless URIs that
            follow the conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example:
            ``projects/my-project/locations/us-central1-a/privateClouds/my-cloud``
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server guarantees that a request
            doesn't result in creation of duplicate
            commitments for at least 60 minutes.

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

    private_cloud: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ResetVcenterCredentialsRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.ResetVcenterCredentials][google.cloud.vmwareengine.v1.VmwareEngine.ResetVcenterCredentials]

    Attributes:
        private_cloud (str):
            Required. The resource name of the private cloud to reset
            credentials for. Resource names are schemeless URIs that
            follow the conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example:
            ``projects/my-project/locations/us-central1-a/privateClouds/my-cloud``
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server guarantees that a request
            doesn't result in creation of duplicate
            commitments for at least 60 minutes.

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
        username (str):
            Optional. The username of the user to be to
            reset the credentials. The default value of this
            field is CloudOwner@gve.local. The provided
            value should be one of the following:

            solution-user-01@gve.local,
            solution-user-02@gve.local,
            solution-user-03@gve.local,
            solution-user-04@gve.local,
            solution-user-05@gve.local,
            zertoadmin@gve.local.
    """

    private_cloud: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    username: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListHcxActivationKeysResponse(proto.Message):
    r"""Response message for
    [VmwareEngine.ListHcxActivationKeys][google.cloud.vmwareengine.v1.VmwareEngine.ListHcxActivationKeys]

    Attributes:
        hcx_activation_keys (MutableSequence[google.cloud.vmwareengine_v1.types.HcxActivationKey]):
            List of HCX activation keys.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        unreachable (MutableSequence[str]):
            Locations that could not be reached when
            making an aggregated query using wildcards.
    """

    @property
    def raw_page(self):
        return self

    hcx_activation_keys: MutableSequence[vmwareengine_resources.HcxActivationKey] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=vmwareengine_resources.HcxActivationKey,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class ListHcxActivationKeysRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.ListHcxActivationKeys][google.cloud.vmwareengine.v1.VmwareEngine.ListHcxActivationKeys]

    Attributes:
        parent (str):
            Required. The resource name of the private cloud to be
            queried for HCX activation keys. Resource names are
            schemeless URIs that follow the conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example:
            ``projects/my-project/locations/us-central1/privateClouds/my-cloud``
        page_size (int):
            The maximum number of HCX activation keys to
            return in one page. The service may return fewer
            than this value. The maximum value is coerced to
            1000.
            The default value of this field is 500.
        page_token (str):
            A page token, received from a previous
            ``ListHcxActivationKeys`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListHcxActivationKeys`` must match the call that provided
            the page token.
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


class GetHcxActivationKeyRequest(proto.Message):
    r"""Request message for [VmwareEngine.GetHcxActivationKeys][]

    Attributes:
        name (str):
            Required. The resource name of the HCX activation key to
            retrieve. Resource names are schemeless URIs that follow the
            conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example:
            ``projects/my-project/locations/us-central1/privateClouds/my-cloud/hcxActivationKeys/my-key``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateHcxActivationKeyRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.CreateHcxActivationKey][google.cloud.vmwareengine.v1.VmwareEngine.CreateHcxActivationKey]

    Attributes:
        parent (str):
            Required. The resource name of the private cloud to create
            the key for. Resource names are schemeless URIs that follow
            the conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example:
            ``projects/my-project/locations/us-central1/privateClouds/my-cloud``
        hcx_activation_key (google.cloud.vmwareengine_v1.types.HcxActivationKey):
            Required. The initial description of a new
            HCX activation key. When creating a new key,
            this field must be an empty object.
        hcx_activation_key_id (str):
            Required. The user-provided identifier of the
            ``HcxActivationKey`` to be created. This identifier must be
            unique among ``HcxActivationKey`` resources within the
            parent and becomes the final token in the name URI. The
            identifier must meet the following requirements:

            - Only contains 1-63 alphanumeric characters and hyphens
            - Begins with an alphabetical character
            - Ends with a non-hyphen character
            - Not formatted as a UUID
            - Complies with `RFC
              1034 <https://datatracker.ietf.org/doc/html/rfc1034>`__
              (section 3.5)
        request_id (str):
            A request ID to identify requests. Specify a
            unique request ID so that if you must retry your
            request, the server will know to ignore the
            request if it has already been completed. The
            server guarantees that a request doesn't result
            in creation of duplicate commitments for at
            least 60 minutes.

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
    hcx_activation_key: vmwareengine_resources.HcxActivationKey = proto.Field(
        proto.MESSAGE,
        number=2,
        message=vmwareengine_resources.HcxActivationKey,
    )
    hcx_activation_key_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class GetDnsForwardingRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.GetDnsForwarding][google.cloud.vmwareengine.v1.VmwareEngine.GetDnsForwarding]

    Attributes:
        name (str):
            Required. The resource name of a ``DnsForwarding`` to
            retrieve. Resource names are schemeless URIs that follow the
            conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example:
            ``projects/my-project/locations/us-central1-a/privateClouds/my-cloud/dnsForwarding``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateDnsForwardingRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.UpdateDnsForwarding][google.cloud.vmwareengine.v1.VmwareEngine.UpdateDnsForwarding]

    Attributes:
        dns_forwarding (google.cloud.vmwareengine_v1.types.DnsForwarding):
            Required. DnsForwarding config details.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask is used to specify the fields to be
            overwritten in the ``DnsForwarding`` resource by the update.
            The fields specified in the ``update_mask`` are relative to
            the resource, not the full request. A field will be
            overwritten if it is in the mask. If the user does not
            provide a mask then all fields will be overwritten.
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server guarantees that a request
            doesn't result in creation of duplicate
            commitments for at least 60 minutes.

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

    dns_forwarding: vmwareengine_resources.DnsForwarding = proto.Field(
        proto.MESSAGE,
        number=1,
        message=vmwareengine_resources.DnsForwarding,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class CreateNetworkPeeringRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.CreateNetworkPeering][google.cloud.vmwareengine.v1.VmwareEngine.CreateNetworkPeering]

    Attributes:
        parent (str):
            Required. The resource name of the location to create the
            new network peering in. This value is always ``global``,
            because ``NetworkPeering`` is a global resource. Resource
            names are schemeless URIs that follow the conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example: ``projects/my-project/locations/global``
        network_peering_id (str):
            Required. The user-provided identifier of the new
            ``NetworkPeering``. This identifier must be unique among
            ``NetworkPeering`` resources within the parent and becomes
            the final token in the name URI. The identifier must meet
            the following requirements:

            - Only contains 1-63 alphanumeric characters and hyphens
            - Begins with an alphabetical character
            - Ends with a non-hyphen character
            - Not formatted as a UUID
            - Complies with `RFC
              1034 <https://datatracker.ietf.org/doc/html/rfc1034>`__
              (section 3.5)
        network_peering (google.cloud.vmwareengine_v1.types.NetworkPeering):
            Required. The initial description of the new
            network peering.
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server guarantees that a request
            doesn't result in creation of duplicate
            commitments for at least 60 minutes.

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
    network_peering_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    network_peering: vmwareengine_resources.NetworkPeering = proto.Field(
        proto.MESSAGE,
        number=3,
        message=vmwareengine_resources.NetworkPeering,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class DeleteNetworkPeeringRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.DeleteNetworkPeering][google.cloud.vmwareengine.v1.VmwareEngine.DeleteNetworkPeering]

    Attributes:
        name (str):
            Required. The resource name of the network peering to be
            deleted. Resource names are schemeless URIs that follow the
            conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example:
            ``projects/my-project/locations/global/networkPeerings/my-peering``
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server guarantees that a request
            doesn't result in creation of duplicate
            commitments for at least 60 minutes.

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
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetNetworkPeeringRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.GetNetworkPeering][google.cloud.vmwareengine.v1.VmwareEngine.GetNetworkPeering]

    Attributes:
        name (str):
            Required. The resource name of the network peering to
            retrieve. Resource names are schemeless URIs that follow the
            conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example:
            ``projects/my-project/locations/global/networkPeerings/my-peering``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListNetworkPeeringsRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.ListNetworkPeerings][google.cloud.vmwareengine.v1.VmwareEngine.ListNetworkPeerings]

    Attributes:
        parent (str):
            Required. The resource name of the location (global) to
            query for network peerings. Resource names are schemeless
            URIs that follow the conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example: ``projects/my-project/locations/global``
        page_size (int):
            The maximum number of network peerings to
            return in one page. The maximum value is coerced
            to 1000. The default value of this field is 500.
        page_token (str):
            A page token, received from a previous
            ``ListNetworkPeerings`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListNetworkPeerings`` must match the call that provided
            the page token.
        filter (str):
            A filter expression that matches resources returned in the
            response. The expression must specify the field name, a
            comparison operator, and the value that you want to use for
            filtering. The value must be a string, a number, or a
            boolean. The comparison operator must be ``=``, ``!=``,
            ``>``, or ``<``.

            For example, if you are filtering a list of network
            peerings, you can exclude the ones named ``example-peering``
            by specifying ``name != "example-peering"``.

            To filter on multiple expressions, provide each separate
            expression within parentheses. For example:

            ::

               (name = "example-peering")
               (createTime > "2021-04-12T08:15:10.40Z")

            By default, each expression is an ``AND`` expression.
            However, you can include ``AND`` and ``OR`` expressions
            explicitly. For example:

            ::

               (name = "example-peering-1") AND
               (createTime > "2021-04-12T08:15:10.40Z") OR
               (name = "example-peering-2")
        order_by (str):
            Sorts list results by a certain order. By default, returned
            results are ordered by ``name`` in ascending order. You can
            also sort results in descending order based on the ``name``
            value using ``orderBy="name desc"``. Currently, only
            ordering by ``name`` is supported.
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


class UpdateNetworkPeeringRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.UpdateNetworkPeering][google.cloud.vmwareengine.v1.VmwareEngine.UpdateNetworkPeering]

    Attributes:
        network_peering (google.cloud.vmwareengine_v1.types.NetworkPeering):
            Required. Network peering description.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask is used to specify the fields to be
            overwritten in the ``NetworkPeering`` resource by the
            update. The fields specified in the ``update_mask`` are
            relative to the resource, not the full request. A field will
            be overwritten if it is in the mask. If the user does not
            provide a mask then all fields will be overwritten.
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server guarantees that a request
            doesn't result in creation of duplicate
            commitments for at least 60 minutes.

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

    network_peering: vmwareengine_resources.NetworkPeering = proto.Field(
        proto.MESSAGE,
        number=1,
        message=vmwareengine_resources.NetworkPeering,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListNetworkPeeringsResponse(proto.Message):
    r"""Response message for
    [VmwareEngine.ListNetworkPeerings][google.cloud.vmwareengine.v1.VmwareEngine.ListNetworkPeerings]

    Attributes:
        network_peerings (MutableSequence[google.cloud.vmwareengine_v1.types.NetworkPeering]):
            A list of network peerings.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        unreachable (MutableSequence[str]):
            Unreachable resources.
    """

    @property
    def raw_page(self):
        return self

    network_peerings: MutableSequence[vmwareengine_resources.NetworkPeering] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=vmwareengine_resources.NetworkPeering,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class ListPeeringRoutesRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.ListPeeringRoutes][google.cloud.vmwareengine.v1.VmwareEngine.ListPeeringRoutes]

    Attributes:
        parent (str):
            Required. The resource name of the network peering to
            retrieve peering routes from. Resource names are schemeless
            URIs that follow the conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example:
            ``projects/my-project/locations/global/networkPeerings/my-peering``
        page_size (int):
            The maximum number of peering routes to
            return in one page. The service may return fewer
            than this value. The maximum value is coerced to
            1000.
            The default value of this field is 500.
        page_token (str):
            A page token, received from a previous ``ListPeeringRoutes``
            call. Provide this to retrieve the subsequent page. When
            paginating, all other parameters provided to
            ``ListPeeringRoutes`` must match the call that provided the
            page token.
        filter (str):
            A filter expression that matches resources returned in the
            response. Currently, only filtering on the ``direction``
            field is supported. To return routes imported from the peer
            network, provide "direction=INCOMING". To return routes
            exported from the VMware Engine network, provide
            "direction=OUTGOING". Other filter expressions return an
            error.
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
        number=6,
    )


class ListPeeringRoutesResponse(proto.Message):
    r"""Response message for
    [VmwareEngine.ListPeeringRoutes][google.cloud.vmwareengine.v1.VmwareEngine.ListPeeringRoutes]

    Attributes:
        peering_routes (MutableSequence[google.cloud.vmwareengine_v1.types.PeeringRoute]):
            A list of peering routes.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    peering_routes: MutableSequence[vmwareengine_resources.PeeringRoute] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=vmwareengine_resources.PeeringRoute,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListNetworkPoliciesRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.ListNetworkPolicies][google.cloud.vmwareengine.v1.VmwareEngine.ListNetworkPolicies]

    Attributes:
        parent (str):
            Required. The resource name of the location (region) to
            query for network policies. Resource names are schemeless
            URIs that follow the conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example: ``projects/my-project/locations/us-central1``
        page_size (int):
            The maximum number of network policies to
            return in one page. The service may return fewer
            than this value. The maximum value is coerced to
            1000.
            The default value of this field is 500.
        page_token (str):
            A page token, received from a previous
            ``ListNetworkPolicies`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListNetworkPolicies`` must match the call that provided
            the page token.
        filter (str):
            A filter expression that matches resources returned in the
            response. The expression must specify the field name, a
            comparison operator, and the value that you want to use for
            filtering. The value must be a string, a number, or a
            boolean. The comparison operator must be ``=``, ``!=``,
            ``>``, or ``<``.

            For example, if you are filtering a list of network
            policies, you can exclude the ones named ``example-policy``
            by specifying ``name != "example-policy"``.

            To filter on multiple expressions, provide each separate
            expression within parentheses. For example:

            ::

               (name = "example-policy")
               (createTime > "2021-04-12T08:15:10.40Z")

            By default, each expression is an ``AND`` expression.
            However, you can include ``AND`` and ``OR`` expressions
            explicitly. For example:

            ::

               (name = "example-policy-1") AND
               (createTime > "2021-04-12T08:15:10.40Z") OR
               (name = "example-policy-2")
        order_by (str):
            Sorts list results by a certain order. By default, returned
            results are ordered by ``name`` in ascending order. You can
            also sort results in descending order based on the ``name``
            value using ``orderBy="name desc"``. Currently, only
            ordering by ``name`` is supported.
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


class ListNetworkPoliciesResponse(proto.Message):
    r"""Response message for
    [VmwareEngine.ListNetworkPolicies][google.cloud.vmwareengine.v1.VmwareEngine.ListNetworkPolicies]

    Attributes:
        network_policies (MutableSequence[google.cloud.vmwareengine_v1.types.NetworkPolicy]):
            A list of network policies.
        next_page_token (str):
            A token, which can be send as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        unreachable (MutableSequence[str]):
            Locations that could not be reached when
            making an aggregated query using wildcards.
    """

    @property
    def raw_page(self):
        return self

    network_policies: MutableSequence[vmwareengine_resources.NetworkPolicy] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=vmwareengine_resources.NetworkPolicy,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetNetworkPolicyRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.GetNetworkPolicy][google.cloud.vmwareengine.v1.VmwareEngine.GetNetworkPolicy]

    Attributes:
        name (str):
            Required. The resource name of the network policy to
            retrieve. Resource names are schemeless URIs that follow the
            conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example:
            ``projects/my-project/locations/us-central1/networkPolicies/my-network-policy``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateNetworkPolicyRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.UpdateNetworkPolicy][google.cloud.vmwareengine.v1.VmwareEngine.UpdateNetworkPolicy]

    Attributes:
        network_policy (google.cloud.vmwareengine_v1.types.NetworkPolicy):
            Required. Network policy description.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask is used to specify the fields to be
            overwritten in the ``NetworkPolicy`` resource by the update.
            The fields specified in the ``update_mask`` are relative to
            the resource, not the full request. A field will be
            overwritten if it is in the mask. If the user does not
            provide a mask then all fields will be overwritten.
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server guarantees that a request
            doesn't result in creation of duplicate
            commitments for at least 60 minutes.

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

    network_policy: vmwareengine_resources.NetworkPolicy = proto.Field(
        proto.MESSAGE,
        number=1,
        message=vmwareengine_resources.NetworkPolicy,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class CreateNetworkPolicyRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.CreateNetworkPolicy][google.cloud.vmwareengine.v1.VmwareEngine.CreateNetworkPolicy]

    Attributes:
        parent (str):
            Required. The resource name of the location (region) to
            create the new network policy in. Resource names are
            schemeless URIs that follow the conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example: ``projects/my-project/locations/us-central1``
        network_policy_id (str):
            Required. The user-provided identifier of the network policy
            to be created. This identifier must be unique within parent
            ``projects/{my-project}/locations/{us-central1}/networkPolicies``
            and becomes the final token in the name URI. The identifier
            must meet the following requirements:

            - Only contains 1-63 alphanumeric characters and hyphens
            - Begins with an alphabetical character
            - Ends with a non-hyphen character
            - Not formatted as a UUID
            - Complies with `RFC
              1034 <https://datatracker.ietf.org/doc/html/rfc1034>`__
              (section 3.5)
        network_policy (google.cloud.vmwareengine_v1.types.NetworkPolicy):
            Required. The network policy configuration to
            use in the request.
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server guarantees that a request
            doesn't result in creation of duplicate
            commitments for at least 60 minutes.

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
    network_policy_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    network_policy: vmwareengine_resources.NetworkPolicy = proto.Field(
        proto.MESSAGE,
        number=3,
        message=vmwareengine_resources.NetworkPolicy,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class DeleteNetworkPolicyRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.DeleteNetworkPolicy][google.cloud.vmwareengine.v1.VmwareEngine.DeleteNetworkPolicy]

    Attributes:
        name (str):
            Required. The resource name of the network policy to delete.
            Resource names are schemeless URIs that follow the
            conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example:
            ``projects/my-project/locations/us-central1/networkPolicies/my-network-policy``
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server guarantees that a request
            doesn't result in creation of duplicate
            commitments for at least 60 minutes.

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
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListManagementDnsZoneBindingsRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.ListManagementDnsZoneBindings][google.cloud.vmwareengine.v1.VmwareEngine.ListManagementDnsZoneBindings]

    Attributes:
        parent (str):
            Required. The resource name of the private cloud to be
            queried for management DNS zone bindings. Resource names are
            schemeless URIs that follow the conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example:
            ``projects/my-project/locations/us-central1-a/privateClouds/my-cloud``
        page_size (int):
            The maximum number of management DNS zone
            bindings to return in one page. The service may
            return fewer than this value. The maximum value
            is coerced to 1000.
            The default value of this field is 500.
        page_token (str):
            A page token, received from a previous
            ``ListManagementDnsZoneBindings`` call. Provide this to
            retrieve the subsequent page.

            When paginating, all other parameters provided to
            ``ListManagementDnsZoneBindings`` must match the call that
            provided the page token.
        filter (str):
            A filter expression that matches resources returned in the
            response. The expression must specify the field name, a
            comparison operator, and the value that you want to use for
            filtering. The value must be a string, a number, or a
            boolean. The comparison operator must be ``=``, ``!=``,
            ``>``, or ``<``.

            For example, if you are filtering a list of Management DNS
            Zone Bindings, you can exclude the ones named
            ``example-management-dns-zone-binding`` by specifying
            ``name != "example-management-dns-zone-binding"``.

            To filter on multiple expressions, provide each separate
            expression within parentheses. For example:

            ::

               (name = "example-management-dns-zone-binding")
               (createTime > "2021-04-12T08:15:10.40Z")

            By default, each expression is an ``AND`` expression.
            However, you can include ``AND`` and ``OR`` expressions
            explicitly. For example:

            ::

               (name = "example-management-dns-zone-binding-1") AND
               (createTime > "2021-04-12T08:15:10.40Z") OR
               (name = "example-management-dns-zone-binding-2")
        order_by (str):
            Sorts list results by a certain order. By default, returned
            results are ordered by ``name`` in ascending order. You can
            also sort results in descending order based on the ``name``
            value using ``orderBy="name desc"``. Currently, only
            ordering by ``name`` is supported.
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


class ListManagementDnsZoneBindingsResponse(proto.Message):
    r"""Response message for
    [VmwareEngine.ListManagementDnsZoneBindings][google.cloud.vmwareengine.v1.VmwareEngine.ListManagementDnsZoneBindings]

    Attributes:
        management_dns_zone_bindings (MutableSequence[google.cloud.vmwareengine_v1.types.ManagementDnsZoneBinding]):
            A list of management DNS zone bindings.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        unreachable (MutableSequence[str]):
            Locations that could not be reached when
            making an aggregated query using wildcards.
    """

    @property
    def raw_page(self):
        return self

    management_dns_zone_bindings: MutableSequence[
        vmwareengine_resources.ManagementDnsZoneBinding
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=vmwareengine_resources.ManagementDnsZoneBinding,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetManagementDnsZoneBindingRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.GetManagementDnsZoneBinding][google.cloud.vmwareengine.v1.VmwareEngine.GetManagementDnsZoneBinding]

    Attributes:
        name (str):
            Required. The resource name of the management DNS zone
            binding to retrieve. Resource names are schemeless URIs that
            follow the conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example:
            ``projects/my-project/locations/us-central1-a/privateClouds/my-cloud/managementDnsZoneBindings/my-management-dns-zone-binding``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateManagementDnsZoneBindingRequest(proto.Message):
    r"""Request message for [VmwareEngine.CreateManagementDnsZoneBindings][]

    Attributes:
        parent (str):
            Required. The resource name of the private cloud to create a
            new management DNS zone binding for. Resource names are
            schemeless URIs that follow the conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example:
            ``projects/my-project/locations/us-central1-a/privateClouds/my-cloud``
        management_dns_zone_binding (google.cloud.vmwareengine_v1.types.ManagementDnsZoneBinding):
            Required. The initial values for a new
            management DNS zone binding.
        management_dns_zone_binding_id (str):
            Required. The user-provided identifier of the
            ``ManagementDnsZoneBinding`` resource to be created. This
            identifier must be unique among ``ManagementDnsZoneBinding``
            resources within the parent and becomes the final token in
            the name URI. The identifier must meet the following
            requirements:

            - Only contains 1-63 alphanumeric characters and hyphens
            - Begins with an alphabetical character
            - Ends with a non-hyphen character
            - Not formatted as a UUID
            - Complies with `RFC
              1034 <https://datatracker.ietf.org/doc/html/rfc1034>`__
              (section 3.5)
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server guarantees that a request
            doesn't result in creation of duplicate
            commitments for at least 60 minutes.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if the original
            operation with the same request ID was received,
            and if so, will ignore the second request. This
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
    management_dns_zone_binding: vmwareengine_resources.ManagementDnsZoneBinding = (
        proto.Field(
            proto.MESSAGE,
            number=2,
            message=vmwareengine_resources.ManagementDnsZoneBinding,
        )
    )
    management_dns_zone_binding_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateManagementDnsZoneBindingRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.UpdateManagementDnsZoneBinding][google.cloud.vmwareengine.v1.VmwareEngine.UpdateManagementDnsZoneBinding]

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask is used to specify the fields to be
            overwritten in the ``ManagementDnsZoneBinding`` resource by
            the update. The fields specified in the ``update_mask`` are
            relative to the resource, not the full request. A field will
            be overwritten if it is in the mask. If the user does not
            provide a mask then all fields will be overwritten.
        management_dns_zone_binding (google.cloud.vmwareengine_v1.types.ManagementDnsZoneBinding):
            Required. New values to update the management
            DNS zone binding with.
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server guarantees that a request
            doesn't result in creation of duplicate
            commitments for at least 60 minutes.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if the original
            operation with the same request ID was received,
            and if so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    management_dns_zone_binding: vmwareengine_resources.ManagementDnsZoneBinding = (
        proto.Field(
            proto.MESSAGE,
            number=2,
            message=vmwareengine_resources.ManagementDnsZoneBinding,
        )
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteManagementDnsZoneBindingRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.DeleteManagementDnsZoneBinding][google.cloud.vmwareengine.v1.VmwareEngine.DeleteManagementDnsZoneBinding]

    Attributes:
        name (str):
            Required. The resource name of the management DNS zone
            binding to delete. Resource names are schemeless URIs that
            follow the conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example:
            ``projects/my-project/locations/us-central1-a/privateClouds/my-cloud/managementDnsZoneBindings/my-management-dns-zone-binding``
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server guarantees that a request
            doesn't result in creation of duplicate
            commitments for at least 60 minutes.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if the original
            operation with the same request ID was received,
            and if so, will ignore the second request. This
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
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class RepairManagementDnsZoneBindingRequest(proto.Message):
    r"""Request message for [VmwareEngine.RepairManagementDnsZoneBindings][]

    Attributes:
        name (str):
            Required. The resource name of the management DNS zone
            binding to repair. Resource names are schemeless URIs that
            follow the conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example:
            ``projects/my-project/locations/us-central1-a/privateClouds/my-cloud/managementDnsZoneBindings/my-management-dns-zone-binding``
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server guarantees that a request
            doesn't result in creation of duplicate
            commitments for at least 60 minutes.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if the original
            operation with the same request ID was received,
            and if so, will ignore the second request. This
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
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreateVmwareEngineNetworkRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.CreateVmwareEngineNetwork][google.cloud.vmwareengine.v1.VmwareEngine.CreateVmwareEngineNetwork]

    Attributes:
        parent (str):
            Required. The resource name of the location to create the
            new VMware Engine network in. A VMware Engine network of
            type ``LEGACY`` is a regional resource, and a VMware Engine
            network of type ``STANDARD`` is a global resource. Resource
            names are schemeless URIs that follow the conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example: ``projects/my-project/locations/global``
        vmware_engine_network_id (str):
            Required. The user-provided identifier of the new VMware
            Engine network. This identifier must be unique among VMware
            Engine network resources within the parent and becomes the
            final token in the name URI. The identifier must meet the
            following requirements:

            - For networks of type LEGACY, adheres to the format:
              ``{region-id}-default``. Replace ``{region-id}`` with the
              region where you want to create the VMware Engine network.
              For example, "us-central1-default".
            - Only contains 1-63 alphanumeric characters and hyphens
            - Begins with an alphabetical character
            - Ends with a non-hyphen character
            - Not formatted as a UUID
            - Complies with `RFC
              1034 <https://datatracker.ietf.org/doc/html/rfc1034>`__
              (section 3.5)
        vmware_engine_network (google.cloud.vmwareengine_v1.types.VmwareEngineNetwork):
            Required. The initial description of the new
            VMware Engine network.
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server guarantees that a request
            doesn't result in creation of duplicate
            commitments for at least 60 minutes.

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
    vmware_engine_network_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    vmware_engine_network: vmwareengine_resources.VmwareEngineNetwork = proto.Field(
        proto.MESSAGE,
        number=3,
        message=vmwareengine_resources.VmwareEngineNetwork,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateVmwareEngineNetworkRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.UpdateVmwareEngineNetwork][google.cloud.vmwareengine.v1.VmwareEngine.UpdateVmwareEngineNetwork]

    Attributes:
        vmware_engine_network (google.cloud.vmwareengine_v1.types.VmwareEngineNetwork):
            Required. VMware Engine network description.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask is used to specify the fields to be
            overwritten in the VMware Engine network resource by the
            update. The fields specified in the ``update_mask`` are
            relative to the resource, not the full request. A field will
            be overwritten if it is in the mask. If the user does not
            provide a mask then all fields will be overwritten. Only the
            following fields can be updated: ``description``.
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server guarantees that a request
            doesn't result in creation of duplicate
            commitments for at least 60 minutes.

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

    vmware_engine_network: vmwareengine_resources.VmwareEngineNetwork = proto.Field(
        proto.MESSAGE,
        number=1,
        message=vmwareengine_resources.VmwareEngineNetwork,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteVmwareEngineNetworkRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.DeleteVmwareEngineNetwork][google.cloud.vmwareengine.v1.VmwareEngine.DeleteVmwareEngineNetwork]

    Attributes:
        name (str):
            Required. The resource name of the VMware Engine network to
            be deleted. Resource names are schemeless URIs that follow
            the conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example:
            ``projects/my-project/locations/global/vmwareEngineNetworks/my-network``
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server guarantees that a request
            doesn't result in creation of duplicate
            commitments for at least 60 minutes.

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
        etag (str):
            Optional. Checksum used to ensure that the user-provided
            value is up to date before the server processes the request.
            The server compares provided checksum with the current
            checksum of the resource. If the user-provided value is out
            of date, this request returns an ``ABORTED`` error.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=3,
    )


class GetVmwareEngineNetworkRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.GetVmwareEngineNetwork][google.cloud.vmwareengine.v1.VmwareEngine.GetVmwareEngineNetwork]

    Attributes:
        name (str):
            Required. The resource name of the VMware Engine network to
            retrieve. Resource names are schemeless URIs that follow the
            conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example:
            ``projects/my-project/locations/global/vmwareEngineNetworks/my-network``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListVmwareEngineNetworksRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.ListVmwareEngineNetworks][google.cloud.vmwareengine.v1.VmwareEngine.ListVmwareEngineNetworks]

    Attributes:
        parent (str):
            Required. The resource name of the location to query for
            VMware Engine networks. Resource names are schemeless URIs
            that follow the conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example: ``projects/my-project/locations/global``
        page_size (int):
            The maximum number of results to return in
            one page. The maximum value is coerced to 1000.
            The default value of this field is 500.
        page_token (str):
            A page token, received from a previous
            ``ListVmwareEngineNetworks`` call. Provide this to retrieve
            the subsequent page.

            When paginating, all other parameters provided to
            ``ListVmwareEngineNetworks`` must match the call that
            provided the page token.
        filter (str):
            A filter expression that matches resources returned in the
            response. The expression must specify the field name, a
            comparison operator, and the value that you want to use for
            filtering. The value must be a string, a number, or a
            boolean. The comparison operator must be ``=``, ``!=``,
            ``>``, or ``<``.

            For example, if you are filtering a list of network
            peerings, you can exclude the ones named ``example-network``
            by specifying ``name != "example-network"``.

            To filter on multiple expressions, provide each separate
            expression within parentheses. For example:

            ::

               (name = "example-network")
               (createTime > "2021-04-12T08:15:10.40Z")

            By default, each expression is an ``AND`` expression.
            However, you can include ``AND`` and ``OR`` expressions
            explicitly. For example:

            ::

               (name = "example-network-1") AND
               (createTime > "2021-04-12T08:15:10.40Z") OR
               (name = "example-network-2")
        order_by (str):
            Sorts list results by a certain order. By default, returned
            results are ordered by ``name`` in ascending order. You can
            also sort results in descending order based on the ``name``
            value using ``orderBy="name desc"``. Currently, only
            ordering by ``name`` is supported.
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


class ListVmwareEngineNetworksResponse(proto.Message):
    r"""Response message for
    [VmwareEngine.ListVmwareEngineNetworks][google.cloud.vmwareengine.v1.VmwareEngine.ListVmwareEngineNetworks]

    Attributes:
        vmware_engine_networks (MutableSequence[google.cloud.vmwareengine_v1.types.VmwareEngineNetwork]):
            A list of VMware Engine networks.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        unreachable (MutableSequence[str]):
            Unreachable resources.
    """

    @property
    def raw_page(self):
        return self

    vmware_engine_networks: MutableSequence[
        vmwareengine_resources.VmwareEngineNetwork
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=vmwareengine_resources.VmwareEngineNetwork,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class CreatePrivateConnectionRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.CreatePrivateConnection][google.cloud.vmwareengine.v1.VmwareEngine.CreatePrivateConnection]

    Attributes:
        parent (str):
            Required. The resource name of the location to create the
            new private connection in. Private connection is a regional
            resource. Resource names are schemeless URIs that follow the
            conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example: ``projects/my-project/locations/us-central1``
        private_connection_id (str):
            Required. The user-provided identifier of the new private
            connection. This identifier must be unique among private
            connection resources within the parent and becomes the final
            token in the name URI. The identifier must meet the
            following requirements:

            - Only contains 1-63 alphanumeric characters and hyphens
            - Begins with an alphabetical character
            - Ends with a non-hyphen character
            - Not formatted as a UUID
            - Complies with `RFC
              1034 <https://datatracker.ietf.org/doc/html/rfc1034>`__
              (section 3.5)
        private_connection (google.cloud.vmwareengine_v1.types.PrivateConnection):
            Required. The initial description of the new
            private connection.
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server guarantees that a request
            doesn't result in creation of duplicate
            commitments for at least 60 minutes.

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
    private_connection_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    private_connection: vmwareengine_resources.PrivateConnection = proto.Field(
        proto.MESSAGE,
        number=3,
        message=vmwareengine_resources.PrivateConnection,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class GetPrivateConnectionRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.GetPrivateConnection][google.cloud.vmwareengine.v1.VmwareEngine.GetPrivateConnection]

    Attributes:
        name (str):
            Required. The resource name of the private connection to
            retrieve. Resource names are schemeless URIs that follow the
            conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example:
            ``projects/my-project/locations/us-central1/privateConnections/my-connection``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListPrivateConnectionsRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.ListPrivateConnections][google.cloud.vmwareengine.v1.VmwareEngine.ListPrivateConnections]

    Attributes:
        parent (str):
            Required. The resource name of the location to query for
            private connections. Resource names are schemeless URIs that
            follow the conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example: ``projects/my-project/locations/us-central1``
        page_size (int):
            The maximum number of private connections to
            return in one page. The maximum value is coerced
            to 1000. The default value of this field is 500.
        page_token (str):
            A page token, received from a previous
            ``ListPrivateConnections`` call. Provide this to retrieve
            the subsequent page.

            When paginating, all other parameters provided to
            ``ListPrivateConnections`` must match the call that provided
            the page token.
        filter (str):
            A filter expression that matches resources returned in the
            response. The expression must specify the field name, a
            comparison operator, and the value that you want to use for
            filtering. The value must be a string, a number, or a
            boolean. The comparison operator must be ``=``, ``!=``,
            ``>``, or ``<``.

            For example, if you are filtering a list of private
            connections, you can exclude the ones named
            ``example-connection`` by specifying
            ``name != "example-connection"``.

            To filter on multiple expressions, provide each separate
            expression within parentheses. For example:

            ::

               (name = "example-connection")
               (createTime > "2022-09-22T08:15:10.40Z")

            By default, each expression is an ``AND`` expression.
            However, you can include ``AND`` and ``OR`` expressions
            explicitly. For example:

            ::

               (name = "example-connection-1") AND
               (createTime > "2021-04-12T08:15:10.40Z") OR
               (name = "example-connection-2")
        order_by (str):
            Sorts list results by a certain order. By default, returned
            results are ordered by ``name`` in ascending order. You can
            also sort results in descending order based on the ``name``
            value using ``orderBy="name desc"``. Currently, only
            ordering by ``name`` is supported.
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


class ListPrivateConnectionsResponse(proto.Message):
    r"""Response message for
    [VmwareEngine.ListPrivateConnections][google.cloud.vmwareengine.v1.VmwareEngine.ListPrivateConnections]

    Attributes:
        private_connections (MutableSequence[google.cloud.vmwareengine_v1.types.PrivateConnection]):
            A list of private connections.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        unreachable (MutableSequence[str]):
            Unreachable resources.
    """

    @property
    def raw_page(self):
        return self

    private_connections: MutableSequence[vmwareengine_resources.PrivateConnection] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=vmwareengine_resources.PrivateConnection,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class UpdatePrivateConnectionRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.UpdatePrivateConnection][google.cloud.vmwareengine.v1.VmwareEngine.UpdatePrivateConnection]

    Attributes:
        private_connection (google.cloud.vmwareengine_v1.types.PrivateConnection):
            Required. Private connection description.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask is used to specify the fields to be
            overwritten in the ``PrivateConnection`` resource by the
            update. The fields specified in the ``update_mask`` are
            relative to the resource, not the full request. A field will
            be overwritten if it is in the mask. If the user does not
            provide a mask then all fields will be overwritten.
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server guarantees that a request
            doesn't result in creation of duplicate
            commitments for at least 60 minutes.

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

    private_connection: vmwareengine_resources.PrivateConnection = proto.Field(
        proto.MESSAGE,
        number=1,
        message=vmwareengine_resources.PrivateConnection,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeletePrivateConnectionRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.DeletePrivateConnection][google.cloud.vmwareengine.v1.VmwareEngine.DeletePrivateConnection]

    Attributes:
        name (str):
            Required. The resource name of the private connection to be
            deleted. Resource names are schemeless URIs that follow the
            conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example:
            ``projects/my-project/locations/us-central1/privateConnections/my-connection``
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server guarantees that a request
            doesn't result in creation of duplicate
            commitments for at least 60 minutes.

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
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListPrivateConnectionPeeringRoutesRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.ListPrivateConnectionPeeringRoutes][google.cloud.vmwareengine.v1.VmwareEngine.ListPrivateConnectionPeeringRoutes]

    Attributes:
        parent (str):
            Required. The resource name of the private connection to
            retrieve peering routes from. Resource names are schemeless
            URIs that follow the conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example:
            ``projects/my-project/locations/us-west1/privateConnections/my-connection``
        page_size (int):
            The maximum number of peering routes to
            return in one page. The service may return fewer
            than this value. The maximum value is coerced to
            1000.
            The default value of this field is 500.
        page_token (str):
            A page token, received from a previous
            ``ListPrivateConnectionPeeringRoutes`` call. Provide this to
            retrieve the subsequent page. When paginating, all other
            parameters provided to
            ``ListPrivateConnectionPeeringRoutes`` must match the call
            that provided the page token.
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


class ListPrivateConnectionPeeringRoutesResponse(proto.Message):
    r"""Response message for
    [VmwareEngine.ListPrivateConnectionPeeringRoutes][google.cloud.vmwareengine.v1.VmwareEngine.ListPrivateConnectionPeeringRoutes]

    Attributes:
        peering_routes (MutableSequence[google.cloud.vmwareengine_v1.types.PeeringRoute]):
            A list of peering routes.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    peering_routes: MutableSequence[vmwareengine_resources.PeeringRoute] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=vmwareengine_resources.PeeringRoute,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GrantDnsBindPermissionRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.GrantDnsBindPermission][google.cloud.vmwareengine.v1.VmwareEngine.GrantDnsBindPermission]

    Attributes:
        name (str):
            Required. The name of the resource which stores the
            users/service accounts having the permission to bind to the
            corresponding intranet VPC of the consumer project.
            DnsBindPermission is a global resource. Resource names are
            schemeless URIs that follow the conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example:
            ``projects/my-project/locations/global/dnsBindPermission``
        principal (google.cloud.vmwareengine_v1.types.Principal):
            Required. The consumer provided user/service
            account which needs to be granted permission to
            bind with the intranet VPC corresponding to the
            consumer project.
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server guarantees that a request
            doesn't result in creation of duplicate
            commitments for at least 60 minutes.

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
    principal: vmwareengine_resources.Principal = proto.Field(
        proto.MESSAGE,
        number=2,
        message=vmwareengine_resources.Principal,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class RevokeDnsBindPermissionRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.RevokeDnsBindPermission][google.cloud.vmwareengine.v1.VmwareEngine.RevokeDnsBindPermission]

    Attributes:
        name (str):
            Required. The name of the resource which stores the
            users/service accounts having the permission to bind to the
            corresponding intranet VPC of the consumer project.
            DnsBindPermission is a global resource. Resource names are
            schemeless URIs that follow the conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example:
            ``projects/my-project/locations/global/dnsBindPermission``
        principal (google.cloud.vmwareengine_v1.types.Principal):
            Required. The consumer provided user/service
            account which needs to be granted permission to
            bind with the intranet VPC corresponding to the
            consumer project.
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server guarantees that a request
            doesn't result in creation of duplicate
            commitments for at least 60 minutes.

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
    principal: vmwareengine_resources.Principal = proto.Field(
        proto.MESSAGE,
        number=2,
        message=vmwareengine_resources.Principal,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class GetDnsBindPermissionRequest(proto.Message):
    r"""Request message for
    [VmwareEngine.GetDnsBindPermission][google.cloud.vmwareengine.v1.VmwareEngine.GetDnsBindPermission]

    Attributes:
        name (str):
            Required. The name of the resource which stores the
            users/service accounts having the permission to bind to the
            corresponding intranet VPC of the consumer project.
            DnsBindPermission is a global resource. Resource names are
            schemeless URIs that follow the conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example:
            ``projects/my-project/locations/global/dnsBindPermission``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
