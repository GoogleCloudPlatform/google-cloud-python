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

from google.cloud.edgenetwork_v1.types import resources

__protobuf__ = proto.module(
    package="google.cloud.edgenetwork.v1",
    manifest={
        "ListZonesRequest",
        "ListZonesResponse",
        "GetZoneRequest",
        "ListNetworksRequest",
        "ListNetworksResponse",
        "GetNetworkRequest",
        "CreateNetworkRequest",
        "DeleteNetworkRequest",
        "ListSubnetsRequest",
        "ListSubnetsResponse",
        "GetSubnetRequest",
        "CreateSubnetRequest",
        "UpdateSubnetRequest",
        "DeleteSubnetRequest",
        "ListInterconnectsRequest",
        "ListInterconnectsResponse",
        "GetInterconnectRequest",
        "ListInterconnectAttachmentsRequest",
        "ListInterconnectAttachmentsResponse",
        "GetInterconnectAttachmentRequest",
        "CreateInterconnectAttachmentRequest",
        "DeleteInterconnectAttachmentRequest",
        "ListRoutersRequest",
        "ListRoutersResponse",
        "GetRouterRequest",
        "CreateRouterRequest",
        "UpdateRouterRequest",
        "DeleteRouterRequest",
        "OperationMetadata",
        "DiagnoseNetworkRequest",
        "DiagnoseNetworkResponse",
        "DiagnoseInterconnectRequest",
        "DiagnoseInterconnectResponse",
        "DiagnoseRouterRequest",
        "DiagnoseRouterResponse",
        "InitializeZoneRequest",
        "InitializeZoneResponse",
    },
)


class ListZonesRequest(proto.Message):
    r"""Deprecated: not implemented.
    Message for requesting list of Zones

    Attributes:
        parent (str):
            Required. Parent value for ListZonesRequest
        page_size (int):
            Requested page size. Server may return fewer
            items than requested. If unspecified, server
            will pick an appropriate default.
        page_token (str):
            A token identifying a page of results the
            server should return.
        filter (str):
            Filtering results
        order_by (str):
            Hint for how to order the results
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


class ListZonesResponse(proto.Message):
    r"""Deprecated: not implemented.
    Message for response to listing Zones

    Attributes:
        zones (MutableSequence[google.cloud.edgenetwork_v1.types.Zone]):
            The list of Zone
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    zones: MutableSequence[resources.Zone] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.Zone,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetZoneRequest(proto.Message):
    r"""Deprecated: not implemented.
    Message for getting a Zone

    Attributes:
        name (str):
            Required. Name of the resource
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListNetworksRequest(proto.Message):
    r"""Message for requesting list of Networks

    Attributes:
        parent (str):
            Required. Parent value for
            ListNetworksRequest
        page_size (int):
            Requested page size. Server may return fewer
            items than requested. If unspecified, server
            will pick an appropriate default.
        page_token (str):
            A token identifying a page of results the
            server should return.
        filter (str):
            Filtering results
        order_by (str):
            Hint for how to order the results
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


class ListNetworksResponse(proto.Message):
    r"""Message for response to listing Networks

    Attributes:
        networks (MutableSequence[google.cloud.edgenetwork_v1.types.Network]):
            The list of Network
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    networks: MutableSequence[resources.Network] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.Network,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetNetworkRequest(proto.Message):
    r"""Message for getting a Network

    Attributes:
        name (str):
            Required. Name of the resource
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateNetworkRequest(proto.Message):
    r"""Message for creating a Network

    Attributes:
        parent (str):
            Required. Value for parent.
        network_id (str):
            Required. Id of the requesting object If auto-generating Id
            server-side, remove this field and network_id from the
            method_signature of Create RPC
        network (google.cloud.edgenetwork_v1.types.Network):
            Required. The resource being created
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

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
    network_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    network: resources.Network = proto.Field(
        proto.MESSAGE,
        number=3,
        message=resources.Network,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class DeleteNetworkRequest(proto.Message):
    r"""Message for deleting a Network

    Attributes:
        name (str):
            Required. Name of the resource
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes after the first request.

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


class ListSubnetsRequest(proto.Message):
    r"""Message for requesting list of Subnets

    Attributes:
        parent (str):
            Required. Parent value for ListSubnetsRequest
        page_size (int):
            Requested page size. Server may return fewer
            items than requested. If unspecified, server
            will pick an appropriate default.
        page_token (str):
            A token identifying a page of results the
            server should return.
        filter (str):
            Filtering results
        order_by (str):
            Hint for how to order the results
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


class ListSubnetsResponse(proto.Message):
    r"""Message for response to listing Subnets

    Attributes:
        subnets (MutableSequence[google.cloud.edgenetwork_v1.types.Subnet]):
            The list of Subnet
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    subnets: MutableSequence[resources.Subnet] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.Subnet,
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
    r"""Message for getting a Subnet

    Attributes:
        name (str):
            Required. Name of the resource
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateSubnetRequest(proto.Message):
    r"""Message for creating a Subnet

    Attributes:
        parent (str):
            Required. Value for parent.
        subnet_id (str):
            Required. Id of the requesting object If auto-generating Id
            server-side, remove this field and subnet_id from the
            method_signature of Create RPC
        subnet (google.cloud.edgenetwork_v1.types.Subnet):
            Required. The resource being created
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

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
    subnet_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    subnet: resources.Subnet = proto.Field(
        proto.MESSAGE,
        number=3,
        message=resources.Subnet,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateSubnetRequest(proto.Message):
    r"""Message for updating a Subnet

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask is used to specify the fields to be
            overwritten in the Subnet resource by the update. The fields
            specified in the update_mask are relative to the resource,
            not the full request. A field will be overwritten if it is
            in the mask. If the user does not provide a mask then all
            fields will be overwritten.
        subnet (google.cloud.edgenetwork_v1.types.Subnet):
            Required. The resource being updated
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

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
    subnet: resources.Subnet = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.Subnet,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteSubnetRequest(proto.Message):
    r"""Message for deleting a Subnet

    Attributes:
        name (str):
            Required. Name of the resource
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes after the first request.

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


class ListInterconnectsRequest(proto.Message):
    r"""Message for requesting list of Interconnects

    Attributes:
        parent (str):
            Required. Parent value for
            ListInterconnectsRequest
        page_size (int):
            Requested page size. Server may return fewer
            items than requested. If unspecified, server
            will pick an appropriate default.
        page_token (str):
            A token identifying a page of results the
            server should return.
        filter (str):
            Filtering results
        order_by (str):
            Hint for how to order the results
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


class ListInterconnectsResponse(proto.Message):
    r"""Message for response to listing Interconnects

    Attributes:
        interconnects (MutableSequence[google.cloud.edgenetwork_v1.types.Interconnect]):
            The list of Interconnect
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    interconnects: MutableSequence[resources.Interconnect] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.Interconnect,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetInterconnectRequest(proto.Message):
    r"""Message for getting a Interconnect

    Attributes:
        name (str):
            Required. Name of the resource
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListInterconnectAttachmentsRequest(proto.Message):
    r"""Message for requesting list of InterconnectAttachments

    Attributes:
        parent (str):
            Required. Parent value for
            ListInterconnectAttachmentsRequest
        page_size (int):
            Requested page size. Server may return fewer
            items than requested. If unspecified, server
            will pick an appropriate default.
        page_token (str):
            A token identifying a page of results the
            server should return.
        filter (str):
            Filtering results
        order_by (str):
            Hint for how to order the results
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


class ListInterconnectAttachmentsResponse(proto.Message):
    r"""Message for response to listing InterconnectAttachments

    Attributes:
        interconnect_attachments (MutableSequence[google.cloud.edgenetwork_v1.types.InterconnectAttachment]):
            The list of InterconnectAttachment
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    interconnect_attachments: MutableSequence[resources.InterconnectAttachment] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=resources.InterconnectAttachment,
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


class GetInterconnectAttachmentRequest(proto.Message):
    r"""Message for getting a InterconnectAttachment

    Attributes:
        name (str):
            Required. Name of the resource
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateInterconnectAttachmentRequest(proto.Message):
    r"""Message for creating a InterconnectAttachment

    Attributes:
        parent (str):
            Required. Value for parent.
        interconnect_attachment_id (str):
            Required. Id of the requesting object If auto-generating Id
            server-side, remove this field and
            interconnect_attachment_id from the method_signature of
            Create RPC
        interconnect_attachment (google.cloud.edgenetwork_v1.types.InterconnectAttachment):
            Required. The resource being created
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

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
    interconnect_attachment_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    interconnect_attachment: resources.InterconnectAttachment = proto.Field(
        proto.MESSAGE,
        number=3,
        message=resources.InterconnectAttachment,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class DeleteInterconnectAttachmentRequest(proto.Message):
    r"""Message for deleting a InterconnectAttachment

    Attributes:
        name (str):
            Required. Name of the resource
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes after the first request.

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


class ListRoutersRequest(proto.Message):
    r"""Message for requesting list of Routers

    Attributes:
        parent (str):
            Required. Parent value for ListRoutersRequest
        page_size (int):
            Requested page size. Server may return fewer
            items than requested. If unspecified, server
            will pick an appropriate default.
        page_token (str):
            A token identifying a page of results the
            server should return.
        filter (str):
            Filtering results
        order_by (str):
            Hint for how to order the results
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


class ListRoutersResponse(proto.Message):
    r"""Message for response to listing Routers

    Attributes:
        routers (MutableSequence[google.cloud.edgenetwork_v1.types.Router]):
            The list of Router
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    routers: MutableSequence[resources.Router] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.Router,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetRouterRequest(proto.Message):
    r"""Message for getting a Router

    Attributes:
        name (str):
            Required. Name of the resource
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateRouterRequest(proto.Message):
    r"""Message for creating a Router

    Attributes:
        parent (str):
            Required. Value for parent.
        router_id (str):
            Required. Id of the requesting object If auto-generating Id
            server-side, remove this field and router_id from the
            method_signature of Create RPC
        router (google.cloud.edgenetwork_v1.types.Router):
            Required. The resource being created
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

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
    router_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    router: resources.Router = proto.Field(
        proto.MESSAGE,
        number=3,
        message=resources.Router,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateRouterRequest(proto.Message):
    r"""Message for updating a Router

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask is used to specify the fields to be
            overwritten in the Router resource by the update. The fields
            specified in the update_mask are relative to the resource,
            not the full request. A field will be overwritten if it is
            in the mask. If the user does not provide a mask then all
            fields will be overwritten.
        router (google.cloud.edgenetwork_v1.types.Router):
            Required. The resource being updated
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

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
    router: resources.Router = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.Router,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteRouterRequest(proto.Message):
    r"""Message for deleting a Router

    Attributes:
        name (str):
            Required. Name of the resource
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes after the first request.

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


class DiagnoseNetworkRequest(proto.Message):
    r"""Message for requesting the diagnostics of a network within a
    specific zone.

    Attributes:
        name (str):
            Required. The name of the network resource.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DiagnoseNetworkResponse(proto.Message):
    r"""DiagnoseNetworkResponse contains the current status for a
    specific network.

    Attributes:
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            The time when the network status was last
            updated.
        result (google.cloud.edgenetwork_v1.types.DiagnoseNetworkResponse.NetworkStatus):
            The network status of a specific network.
    """

    class NetworkStatus(proto.Message):
        r"""NetworkStatus has a list of status for the subnets under the
        current network.

        Attributes:
            subnet_status (MutableSequence[google.cloud.edgenetwork_v1.types.SubnetStatus]):
                A list of status for the subnets under the
                current network.
            macsec_status_internal_links (google.cloud.edgenetwork_v1.types.DiagnoseNetworkResponse.NetworkStatus.MacsecStatus):
                The MACsec status of internal links.
        """

        class MacsecStatus(proto.Enum):
            r"""Denotes the status of MACsec sessions for the links of a
            zone.

            Values:
                MACSEC_STATUS_UNSPECIFIED (0):
                    MACsec status not specified, likely due to
                    missing metrics.
                SECURE (1):
                    All relevant links have at least one MACsec
                    session up.
                UNSECURE (2):
                    At least one relevant link does not have any
                    MACsec sessions up.
            """

            MACSEC_STATUS_UNSPECIFIED = 0
            SECURE = 1
            UNSECURE = 2

        subnet_status: MutableSequence[resources.SubnetStatus] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=resources.SubnetStatus,
        )
        macsec_status_internal_links: "DiagnoseNetworkResponse.NetworkStatus.MacsecStatus" = proto.Field(
            proto.ENUM,
            number=2,
            enum="DiagnoseNetworkResponse.NetworkStatus.MacsecStatus",
        )

    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    result: NetworkStatus = proto.Field(
        proto.MESSAGE,
        number=2,
        message=NetworkStatus,
    )


class DiagnoseInterconnectRequest(proto.Message):
    r"""Message for requesting the diagnostics of an interconnect
    within a specific zone.

    Attributes:
        name (str):
            Required. The name of the interconnect
            resource.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DiagnoseInterconnectResponse(proto.Message):
    r"""DiagnoseInterconnectResponse contains the current diagnostics
    for a specific interconnect.

    Attributes:
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            The time when the interconnect diagnostics
            was last updated.
        result (google.cloud.edgenetwork_v1.types.InterconnectDiagnostics):
            The network status of a specific
            interconnect.
    """

    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    result: resources.InterconnectDiagnostics = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.InterconnectDiagnostics,
    )


class DiagnoseRouterRequest(proto.Message):
    r"""Message for requesting diagnostics of a router within a
    specific zone.

    Attributes:
        name (str):
            Required. The name of the router resource.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DiagnoseRouterResponse(proto.Message):
    r"""DiagnoseRouterResponse contains the current status for a
    specific router.

    Attributes:
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            The time when the router status was last
            updated.
        result (google.cloud.edgenetwork_v1.types.RouterStatus):
            The network status of a specific router.
    """

    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    result: resources.RouterStatus = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.RouterStatus,
    )


class InitializeZoneRequest(proto.Message):
    r"""Message for initializing a specified zone

    Attributes:
        name (str):
            Required. The name of the zone resource.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class InitializeZoneResponse(proto.Message):
    r"""The response of initializing a zone"""


__all__ = tuple(sorted(__protobuf__.manifest))
