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
import google.type.date_pb2 as date_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.gdchardwaremanagement_v1alpha.types import resources

__protobuf__ = proto.module(
    package="google.cloud.gdchardwaremanagement.v1alpha",
    manifest={
        "ListOrdersRequest",
        "ListOrdersResponse",
        "GetOrderRequest",
        "CreateOrderRequest",
        "UpdateOrderRequest",
        "DeleteOrderRequest",
        "SubmitOrderRequest",
        "CancelOrderRequest",
        "ListSitesRequest",
        "ListSitesResponse",
        "GetSiteRequest",
        "CreateSiteRequest",
        "UpdateSiteRequest",
        "DeleteSiteRequest",
        "ListHardwareGroupsRequest",
        "ListHardwareGroupsResponse",
        "GetHardwareGroupRequest",
        "CreateHardwareGroupRequest",
        "UpdateHardwareGroupRequest",
        "DeleteHardwareGroupRequest",
        "ListHardwareRequest",
        "ListHardwareResponse",
        "GetHardwareRequest",
        "CreateHardwareRequest",
        "UpdateHardwareRequest",
        "DeleteHardwareRequest",
        "ListCommentsRequest",
        "ListCommentsResponse",
        "GetCommentRequest",
        "CreateCommentRequest",
        "RecordActionOnCommentRequest",
        "ListChangeLogEntriesRequest",
        "ListChangeLogEntriesResponse",
        "GetChangeLogEntryRequest",
        "ListSkusRequest",
        "ListSkusResponse",
        "GetSkuRequest",
        "ListZonesRequest",
        "ListZonesResponse",
        "GetZoneRequest",
        "CreateZoneRequest",
        "UpdateZoneRequest",
        "DeleteZoneRequest",
        "SignalZoneStateRequest",
        "OperationMetadata",
        "RequestOrderDateChangeRequest",
    },
)


class ListOrdersRequest(proto.Message):
    r"""A request to list orders.

    Attributes:
        parent (str):
            Required. The project and location to list orders in.
            Format: ``projects/{project}/locations/{location}``

            To list orders across all locations, substitute ``-`` (the
            hyphen or dash character) for the location and check the
            unreachable field in the response message.
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
        filter (str):
            Optional. Filtering condition. See
            `AIP-160 <https://google.aip.dev/160>`__.
        order_by (str):
            Optional. Hint for how to order the results.
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


class ListOrdersResponse(proto.Message):
    r"""A list of orders.

    Attributes:
        orders (MutableSequence[google.cloud.gdchardwaremanagement_v1alpha.types.Order]):
            The list of orders.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached. Only used for queries
            to the wildcard location ``-``. If non-empty, it indicates
            that the results are incomplete.
    """

    @property
    def raw_page(self):
        return self

    orders: MutableSequence[resources.Order] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.Order,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetOrderRequest(proto.Message):
    r"""A request to get an order.

    Attributes:
        name (str):
            Required. Name of the resource
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateOrderRequest(proto.Message):
    r"""A request to create an order.

    Attributes:
        parent (str):
            Required. The project and location to create the order in.
            Format: ``projects/{project}/locations/{location}``
        order_id (str):
            Optional. ID used to uniquely identify the Order within its
            parent scope. This field should contain at most 63
            characters and must start with lowercase characters. Only
            lowercase characters, numbers and ``-`` are accepted. The
            ``-`` character cannot be the first or the last one. A
            system generated ID will be used if the field is not set.

            The order.name field in the request will be ignored.
        order (google.cloud.gdchardwaremanagement_v1alpha.types.Order):
            Required. The order to create.
        request_id (str):
            Optional. An optional unique identifier for this request.
            See `AIP-155 <https://google.aip.dev/155>`__.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    order_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    order: resources.Order = proto.Field(
        proto.MESSAGE,
        number=3,
        message=resources.Order,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateOrderRequest(proto.Message):
    r"""A request to update an order.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. A mask to specify the fields in the Order to
            overwrite with this update. The fields specified in the
            update_mask are relative to the order, not the full request.
            A field will be overwritten if it is in the mask. If you
            don't provide a mask then all fields will be overwritten.
        order (google.cloud.gdchardwaremanagement_v1alpha.types.Order):
            Required. The order to update.
        request_id (str):
            Optional. An optional unique identifier for this request.
            See `AIP-155 <https://google.aip.dev/155>`__.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    order: resources.Order = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.Order,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteOrderRequest(proto.Message):
    r"""A request to delete an order.

    Attributes:
        name (str):
            Required. The name of the order. Format:
            ``projects/{project}/locations/{location}/orders/{order}``
        request_id (str):
            Optional. An optional unique identifier for this request.
            See `AIP-155 <https://google.aip.dev/155>`__.
        force (bool):
            Optional. An option to delete any nested
            resources in the Order, such as a HardwareGroup.
            If true, any nested resources for this Order
            will also be deleted. Otherwise, the request
            will only succeed if the Order has no nested
            resources.
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


class SubmitOrderRequest(proto.Message):
    r"""A request to submit an order.

    Attributes:
        name (str):
            Required. The name of the order. Format:
            ``projects/{project}/locations/{location}/orders/{order}``
        request_id (str):
            Optional. An optional unique identifier for this request.
            See `AIP-155 <https://google.aip.dev/155>`__.
        type_ (google.cloud.gdchardwaremanagement_v1alpha.types.SubmitOrderRequest.Type):
            Optional. Type of this request. If unset, the request type
            is assumed to be ``INFO_PENDING``.
    """

    class Type(proto.Enum):
        r"""Valid types of submit order request.

        Values:
            TYPE_UNSPECIFIED (0):
                Request type is unspecified. This should not
                be used.
            INFO_PENDING (1):
                Use this request type to submit your order
                and initiate conversation with Google. After
                this submission, you will not be able to modify
                the number or SKU of your ordered hardware.
                Please note that this order will not be ready
                for fulfillment yet until you provide more
                information, such as zone network configuration,
                hardware physical and installation information,
                etc.
                If you are submitting an order for a SKU type of
                RACK, please use this request type, as
                additional information will be required outside
                of the API.
            INFO_COMPLETE (2):
                Use this request type if and when you are ready to submit
                your order for fulfillment. In addition to the information
                required for ``INFO_PENDING``, the order must contain all
                required information, such as zone network configuration,
                hardware physical and installation information, etc. Further
                changes to any order information will no longer be allowed.
        """

        TYPE_UNSPECIFIED = 0
        INFO_PENDING = 1
        INFO_COMPLETE = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    type_: Type = proto.Field(
        proto.ENUM,
        number=3,
        enum=Type,
    )


class CancelOrderRequest(proto.Message):
    r"""A request to cancel an order.

    Attributes:
        name (str):
            Required. The name of the order. Format:
            ``projects/{project}/locations/{location}/orders/{order}``
        request_id (str):
            Optional. An optional unique identifier for this request.
            See `AIP-155 <https://google.aip.dev/155>`__.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListSitesRequest(proto.Message):
    r"""A request to list sites.

    Attributes:
        parent (str):
            Required. The project and location to list sites in. Format:
            ``projects/{project}/locations/{location}``

            To list sites across all locations, substitute ``-`` (the
            hyphen or dash character) for the location and check the
            unreachable field in the response message.
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
        filter (str):
            Optional. Filtering condition. See
            `AIP-160 <https://google.aip.dev/160>`__.
        order_by (str):
            Optional. Hint for how to order the results.
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


class ListSitesResponse(proto.Message):
    r"""A list of sites.

    Attributes:
        sites (MutableSequence[google.cloud.gdchardwaremanagement_v1alpha.types.Site]):
            The list of sites.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached. Only used for queries
            to the wildcard location ``-``. If non-empty, it indicates
            that the results are incomplete.
    """

    @property
    def raw_page(self):
        return self

    sites: MutableSequence[resources.Site] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.Site,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetSiteRequest(proto.Message):
    r"""A request to get a site.

    Attributes:
        name (str):
            Required. The name of the site. Format:
            ``projects/{project}/locations/{location}/sites/{site}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateSiteRequest(proto.Message):
    r"""A request to create a site.

    Attributes:
        parent (str):
            Required. The project and location to create the site in.
            Format: ``projects/{project}/locations/{location}``
        site_id (str):
            Optional. ID used to uniquely identify the Site within its
            parent scope. This field should contain at most 63
            characters and must start with lowercase characters. Only
            lowercase characters, numbers and ``-`` are accepted. The
            ``-`` character cannot be the first or the last one. A
            system generated ID will be used if the field is not set.

            The site.name field in the request will be ignored.
        site (google.cloud.gdchardwaremanagement_v1alpha.types.Site):
            Required. The site to create.
        request_id (str):
            Optional. An optional unique identifier for this request.
            See `AIP-155 <https://google.aip.dev/155>`__.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    site_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    site: resources.Site = proto.Field(
        proto.MESSAGE,
        number=3,
        message=resources.Site,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateSiteRequest(proto.Message):
    r"""A request to update a site.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. A mask to specify the fields in the Site to
            overwrite with this update. The fields specified in the
            update_mask are relative to the site, not the full request.
            A field will be overwritten if it is in the mask. If you
            don't provide a mask then all fields will be overwritten.
        site (google.cloud.gdchardwaremanagement_v1alpha.types.Site):
            Required. The site to update.
        request_id (str):
            Optional. An optional unique identifier for this request.
            See `AIP-155 <https://google.aip.dev/155>`__.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    site: resources.Site = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.Site,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteSiteRequest(proto.Message):
    r"""A request to delete a site.

    Attributes:
        name (str):
            Required. The name of the site. Format:
            ``projects/{project}/locations/{location}/sites/{site}``
        request_id (str):
            Optional. An optional unique identifier for this request.
            See `AIP-155 <https://google.aip.dev/155>`__.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListHardwareGroupsRequest(proto.Message):
    r"""A request to list hardware groups.

    Attributes:
        parent (str):
            Required. The order to list hardware groups in. Format:
            ``projects/{project}/locations/{location}/orders/{order}``
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
        filter (str):
            Optional. Filtering condition. See
            `AIP-160 <https://google.aip.dev/160>`__.
        order_by (str):
            Optional. Hint for how to order the results.
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


class ListHardwareGroupsResponse(proto.Message):
    r"""A list of hardware groups.

    Attributes:
        hardware_groups (MutableSequence[google.cloud.gdchardwaremanagement_v1alpha.types.HardwareGroup]):
            The list of hardware groups.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    hardware_groups: MutableSequence[resources.HardwareGroup] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.HardwareGroup,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetHardwareGroupRequest(proto.Message):
    r"""A request to get a hardware group.

    Attributes:
        name (str):
            Required. The name of the hardware group. Format:
            ``projects/{project}/locations/{location}/orders/{order}/hardwareGroups/{hardware_group}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateHardwareGroupRequest(proto.Message):
    r"""A request to create a hardware group.

    Attributes:
        parent (str):
            Required. The order to create the hardware group in. Format:
            ``projects/{project}/locations/{location}/orders/{order}``
        hardware_group_id (str):
            Optional. ID used to uniquely identify the HardwareGroup
            within its parent scope. This field should contain at most
            63 characters and must start with lowercase characters. Only
            lowercase characters, numbers and ``-`` are accepted. The
            ``-`` character cannot be the first or the last one. A
            system generated ID will be used if the field is not set.

            The hardware_group.name field in the request will be
            ignored.
        hardware_group (google.cloud.gdchardwaremanagement_v1alpha.types.HardwareGroup):
            Required. The hardware group to create.
        request_id (str):
            Optional. An optional unique identifier for this request.
            See `AIP-155 <https://google.aip.dev/155>`__.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    hardware_group_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    hardware_group: resources.HardwareGroup = proto.Field(
        proto.MESSAGE,
        number=3,
        message=resources.HardwareGroup,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateHardwareGroupRequest(proto.Message):
    r"""A request to update a hardware group.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. A mask to specify the fields in the HardwareGroup
            to overwrite with this update. The fields specified in the
            update_mask are relative to the hardware group, not the full
            request. A field will be overwritten if it is in the mask.
            If you don't provide a mask then all fields will be
            overwritten.
        hardware_group (google.cloud.gdchardwaremanagement_v1alpha.types.HardwareGroup):
            Required. The hardware group to update.
        request_id (str):
            Optional. An optional unique identifier for this request.
            See `AIP-155 <https://google.aip.dev/155>`__.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    hardware_group: resources.HardwareGroup = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.HardwareGroup,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteHardwareGroupRequest(proto.Message):
    r"""A request to delete a hardware group.

    Attributes:
        name (str):
            Required. The name of the hardware group. Format:
            ``projects/{project}/locations/{location}/orders/{order}/hardwareGroups/{hardware_group}``
        request_id (str):
            Optional. An optional unique identifier for this request.
            See `AIP-155 <https://google.aip.dev/155>`__.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListHardwareRequest(proto.Message):
    r"""A request to list hardware.

    Attributes:
        parent (str):
            Required. The project and location to list hardware in.
            Format: ``projects/{project}/locations/{location}``

            To list hardware across all locations, substitute ``-`` (the
            hyphen or dash character) for the location and check the
            unreachable field in the response message.
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
        filter (str):
            Optional. Filtering condition. See
            `AIP-160 <https://google.aip.dev/160>`__.
        order_by (str):
            Optional. Hint for how to order the results.
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


class ListHardwareResponse(proto.Message):
    r"""A list of hardware.

    Attributes:
        hardware (MutableSequence[google.cloud.gdchardwaremanagement_v1alpha.types.Hardware]):
            The list of hardware.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached. Only used for queries
            to the wildcard location ``-``. If non-empty, it indicates
            that the results are incomplete.
    """

    @property
    def raw_page(self):
        return self

    hardware: MutableSequence[resources.Hardware] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.Hardware,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetHardwareRequest(proto.Message):
    r"""A request to get hardware.

    Attributes:
        name (str):
            Required. The name of the hardware. Format:
            ``projects/{project}/locations/{location}/hardware/{hardware}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateHardwareRequest(proto.Message):
    r"""A request to create hardware.

    Attributes:
        parent (str):
            Required. The project and location to create hardware in.
            Format: ``projects/{project}/locations/{location}``
        hardware_id (str):
            Optional. ID used to uniquely identify the Hardware within
            its parent scope. This field should contain at most 63
            characters and must start with lowercase characters. Only
            lowercase characters, numbers and ``-`` are accepted. The
            ``-`` character cannot be the first or the last one. A
            system generated ID will be used if the field is not set.

            The hardware.name field in the request will be ignored.
        hardware (google.cloud.gdchardwaremanagement_v1alpha.types.Hardware):
            Required. The resource to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    hardware_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    hardware: resources.Hardware = proto.Field(
        proto.MESSAGE,
        number=3,
        message=resources.Hardware,
    )


class UpdateHardwareRequest(proto.Message):
    r"""A request to update hardware.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. A mask to specify the fields in the Hardware to
            overwrite with this update. The fields specified in the
            update_mask are relative to the hardware, not the full
            request. A field will be overwritten if it is in the mask.
            If you don't provide a mask then all fields will be
            overwritten.
        hardware (google.cloud.gdchardwaremanagement_v1alpha.types.Hardware):
            Required. The hardware to update.
        request_id (str):
            Optional. An optional unique identifier for this request.
            See `AIP-155 <https://google.aip.dev/155>`__.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    hardware: resources.Hardware = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.Hardware,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteHardwareRequest(proto.Message):
    r"""A request to delete hardware.

    Attributes:
        name (str):
            Required. The name of the hardware. Format:
            ``projects/{project}/locations/{location}/hardware/{hardware}``
        request_id (str):
            Optional. An optional unique identifier for this request.
            See `AIP-155 <https://google.aip.dev/155>`__.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListCommentsRequest(proto.Message):
    r"""A request to list comments.

    Attributes:
        parent (str):
            Required. The order to list comments on. Format:
            ``projects/{project}/locations/{location}/orders/{order}``
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
        filter (str):
            Optional. Filtering condition. See
            `AIP-160 <https://google.aip.dev/160>`__.
        order_by (str):
            Optional. Hint for how to order the results.
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


class ListCommentsResponse(proto.Message):
    r"""A request to list comments.

    Attributes:
        comments (MutableSequence[google.cloud.gdchardwaremanagement_v1alpha.types.Comment]):
            The list of comments.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    comments: MutableSequence[resources.Comment] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.Comment,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetCommentRequest(proto.Message):
    r"""A request to get a comment.

    Attributes:
        name (str):
            Required. The name of the comment. Format:
            ``projects/{project}/locations/{location}/orders/{order}/comments/{comment}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateCommentRequest(proto.Message):
    r"""A request to create a comment.

    Attributes:
        parent (str):
            Required. The order to create the comment on. Format:
            ``projects/{project}/locations/{location}/orders/{order}``
        comment_id (str):
            Optional. ID used to uniquely identify the Comment within
            its parent scope. This field should contain at most 63
            characters and must start with lowercase characters. Only
            lowercase characters, numbers and ``-`` are accepted. The
            ``-`` character cannot be the first or the last one. A
            system generated ID will be used if the field is not set.

            The comment.name field in the request will be ignored.
        comment (google.cloud.gdchardwaremanagement_v1alpha.types.Comment):
            Required. The comment to create.
        request_id (str):
            Optional. An optional unique identifier for this request.
            See `AIP-155 <https://google.aip.dev/155>`__.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    comment_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    comment: resources.Comment = proto.Field(
        proto.MESSAGE,
        number=3,
        message=resources.Comment,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class RecordActionOnCommentRequest(proto.Message):
    r"""A request to record an action on a comment.

    Attributes:
        name (str):
            Required. The name of the comment. Format:
            ``projects/{project}/locations/{location}/orders/{order}/comments/{comment}``
        action_type (google.cloud.gdchardwaremanagement_v1alpha.types.RecordActionOnCommentRequest.ActionType):
            Required. The action type of the recorded
            action.
    """

    class ActionType(proto.Enum):
        r"""Valid action types of Comment.

        Values:
            ACTION_TYPE_UNSPECIFIED (0):
                Action is unspecified.
            READ (1):
                Mark comment as read.
            UNREAD (2):
                Mark comment as unread.
        """

        ACTION_TYPE_UNSPECIFIED = 0
        READ = 1
        UNREAD = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    action_type: ActionType = proto.Field(
        proto.ENUM,
        number=2,
        enum=ActionType,
    )


class ListChangeLogEntriesRequest(proto.Message):
    r"""A request to list change log entries.

    Attributes:
        parent (str):
            Required. The order to list change log entries for. Format:
            ``projects/{project}/locations/{location}/orders/{order}``
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
        filter (str):
            Optional. Filtering condition. See
            `AIP-160 <https://google.aip.dev/160>`__.
        order_by (str):
            Optional. Hint for how to order the results.
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


class ListChangeLogEntriesResponse(proto.Message):
    r"""A list of change log entries.

    Attributes:
        change_log_entries (MutableSequence[google.cloud.gdchardwaremanagement_v1alpha.types.ChangeLogEntry]):
            The list of change log entries.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    change_log_entries: MutableSequence[resources.ChangeLogEntry] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.ChangeLogEntry,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetChangeLogEntryRequest(proto.Message):
    r"""A request to get a change log entry.

    Attributes:
        name (str):
            Required. The name of the change log entry. Format:
            ``projects/{project}/locations/{location}/orders/{order}/changeLogEntries/{change_log_entry}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListSkusRequest(proto.Message):
    r"""A request to list SKUs.

    Attributes:
        parent (str):
            Required. The project and location to list SKUs in. Format:
            ``projects/{project}/locations/{location}``

            To list SKUs across all locations, substitute ``-`` (the
            hyphen or dash character) for the location and check the
            unreachable field in the response message.
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
        filter (str):
            Optional. Filtering condition. See
            `AIP-160 <https://google.aip.dev/160>`__.
        order_by (str):
            Optional. Hint for how to order the results.
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


class ListSkusResponse(proto.Message):
    r"""A list of SKUs.

    Attributes:
        skus (MutableSequence[google.cloud.gdchardwaremanagement_v1alpha.types.Sku]):
            The list of SKUs.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached. Only used for queries
            to the wildcard location ``-``. If non-empty, it indicates
            that the results are incomplete.
    """

    @property
    def raw_page(self):
        return self

    skus: MutableSequence[resources.Sku] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.Sku,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetSkuRequest(proto.Message):
    r"""A request to get an SKU.

    Attributes:
        name (str):
            Required. The name of the SKU. Format:
            ``projects/{project}/locations/{location}/skus/{sku}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListZonesRequest(proto.Message):
    r"""A request to list zones.

    Attributes:
        parent (str):
            Required. The project and location to list zones in. Format:
            ``projects/{project}/locations/{location}``

            To list zones across all locations, substitute ``-`` (the
            hyphen or dash character) for the location and check the
            unreachable field in the response message.
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
        filter (str):
            Optional. Filtering condition. See
            `AIP-160 <https://google.aip.dev/160>`__.
        order_by (str):
            Optional. Hint for how to order the results.
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
    r"""A list of zones.

    Attributes:
        zones (MutableSequence[google.cloud.gdchardwaremanagement_v1alpha.types.Zone]):
            The list of zones.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached. Only used for queries
            to the wildcard location ``-``. If non-empty, it indicates
            that the results are incomplete.
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
    r"""A request to get a zone.

    Attributes:
        name (str):
            Required. The name of the zone. Format:
            ``projects/{project}/locations/{location}/zones/{zone}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateZoneRequest(proto.Message):
    r"""A request to create a zone.

    Attributes:
        parent (str):
            Required. The project and location to create the zone in.
            Format: ``projects/{project}/locations/{location}``
        zone_id (str):
            Optional. ID used to uniquely identify the Zone within its
            parent scope. This field should contain at most 63
            characters and must start with lowercase characters. Only
            lowercase characters, numbers and ``-`` are accepted. The
            ``-`` character cannot be the first or the last one. A
            system generated ID will be used if the field is not set.

            The zone.name field in the request will be ignored.
        zone (google.cloud.gdchardwaremanagement_v1alpha.types.Zone):
            Required. The zone to create.
        request_id (str):
            Optional. An optional unique identifier for this request.
            See `AIP-155 <https://google.aip.dev/155>`__.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    zone_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    zone: resources.Zone = proto.Field(
        proto.MESSAGE,
        number=3,
        message=resources.Zone,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateZoneRequest(proto.Message):
    r"""A request to update a zone.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. A mask to specify the fields in the Zone to
            overwrite with this update. The fields specified in the
            update_mask are relative to the zone, not the full request.
            A field will be overwritten if it is in the mask. If you
            don't provide a mask then all fields will be overwritten.
        zone (google.cloud.gdchardwaremanagement_v1alpha.types.Zone):
            Required. The zone to update.
        request_id (str):
            Optional. An optional unique identifier for this request.
            See `AIP-155 <https://google.aip.dev/155>`__.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    zone: resources.Zone = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.Zone,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteZoneRequest(proto.Message):
    r"""A request to delete a zone.

    Attributes:
        name (str):
            Required. The name of the zone. Format:
            ``projects/{project}/locations/{location}/zones/{zone}``
        request_id (str):
            Optional. An optional unique identifier for this request.
            See `AIP-155 <https://google.aip.dev/155>`__.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class SignalZoneStateRequest(proto.Message):
    r"""A request to signal the state of a zone.

    Attributes:
        name (str):
            Required. The name of the zone. Format:
            ``projects/{project}/locations/{location}/zones/{zone}``
        request_id (str):
            Optional. An optional unique identifier for this request.
            See `AIP-155 <https://google.aip.dev/155>`__.
        state_signal (google.cloud.gdchardwaremanagement_v1alpha.types.SignalZoneStateRequest.StateSignal):
            Optional. The state signal to send for this zone. Either
            state_signal or provisioning_state_signal must be set, but
            not both.
        provisioning_state_signal (google.cloud.gdchardwaremanagement_v1alpha.types.SignalZoneStateRequest.ProvisioningStateSignal):
            Optional. The provisioning state signal to send for this
            zone. Either state_signal or provisioning_state_signal must
            be set, but not both.
        step (str):
            Optional. The step being executed. Provides a finer grained
            status when the state_signal is
            FACTORY_TURNUP_CHECKS_STARTED or
            FACTORY_TURNUP_CHECKS_FAILED.
        details (str):
            Optional. Additional details, such as an error message when
            state_signal is FACTORY_TURNUP_CHECKS_FAILED.
    """

    class StateSignal(proto.Enum):
        r"""Valid state signals for a zone.

        Values:
            STATE_SIGNAL_UNSPECIFIED (0):
                State signal of the zone is unspecified.
            FACTORY_TURNUP_CHECKS_STARTED (3):
                Factory turnup checks have started.
            FACTORY_TURNUP_CHECKS_PASSED (1):
                The Zone is ready for site turnup.
            READY_FOR_SITE_TURNUP (1):
                The Zone is ready for site turnup.
                Deprecated, but not deleted.
            FACTORY_TURNUP_CHECKS_FAILED (2):
                The Zone failed in factory turnup checks.
            VERIFY_CLUSTER_INTENT_PRESENCE (4):
                Verify that a valid cluster intent is
                present.
        """

        _pb_options = {"allow_alias": True}
        STATE_SIGNAL_UNSPECIFIED = 0
        FACTORY_TURNUP_CHECKS_STARTED = 3
        FACTORY_TURNUP_CHECKS_PASSED = 1
        READY_FOR_SITE_TURNUP = 1
        FACTORY_TURNUP_CHECKS_FAILED = 2
        VERIFY_CLUSTER_INTENT_PRESENCE = 4

    class ProvisioningStateSignal(proto.Enum):
        r"""Valid provisioning state signals for a zone.

        Values:
            PROVISIONING_STATE_SIGNAL_UNSPECIFIED (0):
                Provisioning state signal is unspecified.
            PROVISIONING_IN_PROGRESS (1):
                Provisioning is in progress.
            PROVISIONING_COMPLETE (2):
                Provisioning is complete.
        """

        PROVISIONING_STATE_SIGNAL_UNSPECIFIED = 0
        PROVISIONING_IN_PROGRESS = 1
        PROVISIONING_COMPLETE = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    state_signal: StateSignal = proto.Field(
        proto.ENUM,
        number=3,
        enum=StateSignal,
    )
    provisioning_state_signal: ProvisioningStateSignal = proto.Field(
        proto.ENUM,
        number=4,
        enum=ProvisioningStateSignal,
    )
    step: str = proto.Field(
        proto.STRING,
        number=5,
    )
    details: str = proto.Field(
        proto.STRING,
        number=6,
    )


class OperationMetadata(proto.Message):
    r"""Represents the metadata of a long-running operation.

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
            Output only. The verb executed by the
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


class RequestOrderDateChangeRequest(proto.Message):
    r"""A request to change the requested date of an order.

    Attributes:
        name (str):
            Required. The name of the order to update.
            Format:
            projects/{project}/locations/{location}/orders/{order}
        requested_date (google.type.date_pb2.Date):
            Required. The date to which the customer or
            Google wants to set the scheduled installation
            date.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requested_date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=2,
        message=date_pb2.Date,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
