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

from google.ads.admanager_v1.types import order_messages

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "BatchApproveAndOverbookOrdersRequest",
        "BatchApproveAndOverbookOrdersResponse",
        "BatchApproveOrdersRequest",
        "BatchApproveOrdersResponse",
        "BatchSubmitOrdersForApprovalRequest",
        "BatchSubmitOrdersForApprovalResponse",
        "BatchSubmitOrdersForApprovalAndOverbookRequest",
        "BatchSubmitOrdersForApprovalAndOverbookResponse",
        "BatchPauseOrdersRequest",
        "BatchPauseOrdersResponse",
        "BatchResumeOrdersRequest",
        "BatchResumeOrdersResponse",
        "BatchResumeAndOverbookOrdersRequest",
        "BatchResumeAndOverbookOrdersResponse",
        "BatchApproveOrdersWithoutReservationRequest",
        "BatchApproveOrdersWithoutReservationResponse",
        "BatchArchiveOrdersRequest",
        "BatchArchiveOrdersResponse",
        "BatchUnarchiveOrdersRequest",
        "BatchUnarchiveOrdersResponse",
        "BatchDeleteOrdersRequest",
        "BatchDeleteOrdersResponse",
        "BatchDisapproveOrdersRequest",
        "BatchDisapproveOrdersResponse",
        "BatchDisapproveOrdersWithoutReservationChangesRequest",
        "BatchDisapproveOrdersWithoutReservationChangesResponse",
        "BatchRetractOrdersRequest",
        "BatchRetractOrdersResponse",
        "BatchRetractOrdersWithoutReservationChangesRequest",
        "BatchRetractOrdersWithoutReservationChangesResponse",
        "BatchSubmitOrdersForApprovalWithoutReservationChangesRequest",
        "BatchSubmitOrdersForApprovalWithoutReservationChangesResponse",
        "GetOrderRequest",
        "ListOrdersRequest",
        "ListOrdersResponse",
        "CreateOrderRequest",
        "UpdateOrderRequest",
        "BatchCreateOrdersRequest",
        "BatchCreateOrdersResponse",
        "BatchUpdateOrdersRequest",
        "BatchUpdateOrdersResponse",
    },
)


class BatchApproveAndOverbookOrdersRequest(proto.Message):
    r"""Request message for ``BatchApproveAndOverbookOrders`` method.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of Orders.
            Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. The resource names of the orders to approve and
            overbook. Format:
            ``networks/{network_code}/orders/{order_id}``
        skip_inventory_check (bool):
            Optional. Indicates whether the inventory
            check should be skipped when performing this
            action.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    skip_inventory_check: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class BatchApproveAndOverbookOrdersResponse(proto.Message):
    r"""Response object for ``BatchApproveAndOverbookOrders`` method."""


class BatchApproveOrdersRequest(proto.Message):
    r"""Request message for ``BatchApproveOrders`` method.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of Orders.
            Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. The resource names of the orders to approve.
            Format: ``networks/{network_code}/orders/{order_id}``
        skip_inventory_check (bool):
            Optional. Indicates whether the inventory
            check should be skipped when performing this
            action.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    skip_inventory_check: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class BatchApproveOrdersResponse(proto.Message):
    r"""Response object for ``BatchApproveOrders`` method."""


class BatchSubmitOrdersForApprovalRequest(proto.Message):
    r"""Request message for ``BatchSubmitOrdersForApproval`` method.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of Orders.
            Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. The resource names of the orders to submit for
            approval. Format:
            ``networks/{network_code}/orders/{order_id}``
        skip_inventory_check (bool):
            Optional. Indicates whether the inventory
            check should be skipped when performing this
            action.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    skip_inventory_check: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class BatchSubmitOrdersForApprovalResponse(proto.Message):
    r"""Response object for ``BatchSubmitOrdersForApproval`` method."""


class BatchSubmitOrdersForApprovalAndOverbookRequest(proto.Message):
    r"""Request message for ``BatchSubmitOrdersForApprovalAndOverbook``
    method.

    Attributes:
        parent (str):
            Required. Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. The resource names of the orders to submit for
            approval and overbook. Format:
            ``networks/{network_code}/orders/{order_id}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchSubmitOrdersForApprovalAndOverbookResponse(proto.Message):
    r"""Response object for ``BatchSubmitOrdersForApprovalAndOverbook``
    method.

    """


class BatchPauseOrdersRequest(proto.Message):
    r"""Request message for ``BatchPauseOrders`` method.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of Orders.
            Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. The resource names of the orders to pause. Format:
            ``networks/{network_code}/orders/{order_id}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchPauseOrdersResponse(proto.Message):
    r"""Response object for ``BatchPauseOrders`` method."""


class BatchResumeOrdersRequest(proto.Message):
    r"""Request message for ``BatchResumeOrders`` method.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of Orders.
            Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. The resource names of the orders to resume.
            Format: ``networks/{network_code}/orders/{order_id}``
        skip_inventory_check (bool):
            Optional. Indicates whether the inventory
            check should be skipped when performing this
            action.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    skip_inventory_check: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class BatchResumeOrdersResponse(proto.Message):
    r"""Response object for ``BatchResumeOrders`` method."""


class BatchResumeAndOverbookOrdersRequest(proto.Message):
    r"""Request message for ``BatchResumeAndOverbookOrders`` method.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of Orders.
            Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. The resource names of the orders to resume and
            overbook. Format:
            ``networks/{network_code}/orders/{order_id}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchResumeAndOverbookOrdersResponse(proto.Message):
    r"""Response object for ``BatchResumeAndOverbookOrders`` method."""


class BatchApproveOrdersWithoutReservationRequest(proto.Message):
    r"""Request message for ``BatchApproveOrdersWithoutReservation`` method.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of Orders.
            Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. The resource names of the orders to approve.
            Format: ``networks/{network_code}/orders/{order_id}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchApproveOrdersWithoutReservationResponse(proto.Message):
    r"""Response object for ``BatchApproveOrdersWithoutReservation`` method."""


class BatchArchiveOrdersRequest(proto.Message):
    r"""Request message for ``BatchArchiveOrders`` method.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of Orders.
            Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. The resource names of the orders to archive.
            Format: ``networks/{network_code}/orders/{order_id}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchArchiveOrdersResponse(proto.Message):
    r"""Response object for ``BatchArchiveOrders`` method."""


class BatchUnarchiveOrdersRequest(proto.Message):
    r"""Request message for ``BatchUnarchiveOrders`` method.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of Orders.
            Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. The resource names of the orders to extract.
            Format: ``networks/{network_code}/orders/{order_id}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchUnarchiveOrdersResponse(proto.Message):
    r"""Response object for ``BatchUnarchiveOrders`` method."""


class BatchDeleteOrdersRequest(proto.Message):
    r"""Request message for ``BatchDeleteOrders`` method.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of Orders.
            Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. The resource names of the orders to delete.
            Format: ``networks/{network_code}/orders/{order_id}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchDeleteOrdersResponse(proto.Message):
    r"""Response object for ``BatchDeleteOrders`` method."""


class BatchDisapproveOrdersRequest(proto.Message):
    r"""Request message for ``BatchDisapproveOrders`` method.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of Orders.
            Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. The resource names of the orders to disapprove.
            Format: ``networks/{network_code}/orders/{order_id}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchDisapproveOrdersResponse(proto.Message):
    r"""Response object for ``BatchDisapproveOrders`` method."""


class BatchDisapproveOrdersWithoutReservationChangesRequest(proto.Message):
    r"""Request message for
    ``BatchDisapproveOrdersWithoutReservationChanges`` method.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of Orders.
            Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. The resource names of the orders to disapprove
            without reservation changes. Format:
            ``networks/{network_code}/orders/{order_id}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchDisapproveOrdersWithoutReservationChangesResponse(proto.Message):
    r"""Response object for
    ``BatchDisapproveOrdersWithoutReservationChanges`` method.

    """


class BatchRetractOrdersRequest(proto.Message):
    r"""Request message for ``BatchRetractOrders`` method.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of Orders.
            Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. The resource names of the orders to retract.
            Format: ``networks/{network_code}/orders/{order_id}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchRetractOrdersResponse(proto.Message):
    r"""Response object for ``BatchRetractOrders`` method."""


class BatchRetractOrdersWithoutReservationChangesRequest(proto.Message):
    r"""Request message for ``BatchRetractOrdersWithoutReservationChanges``
    method.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of Orders.
            Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. The resource names of the orders to retract.
            Format: ``networks/{network_code}/orders/{order_id}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchRetractOrdersWithoutReservationChangesResponse(proto.Message):
    r"""Response object for ``BatchRetractOrdersWithoutReservationChanges``
    method.

    """


class BatchSubmitOrdersForApprovalWithoutReservationChangesRequest(proto.Message):
    r"""Request message for
    ``BatchSubmitOrdersForApprovalWithoutReservationChanges`` method.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of Orders.
            Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. The resource names of the orders to submit for
            approval. Format:
            ``networks/{network_code}/orders/{order_id}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchSubmitOrdersForApprovalWithoutReservationChangesResponse(proto.Message):
    r"""Response object for
    ``BatchSubmitOrdersForApprovalWithoutReservationChanges`` method.

    """


class GetOrderRequest(proto.Message):
    r"""Request object for ``GetOrder`` method.

    Attributes:
        name (str):
            Required. The resource name of the Order. Format:
            ``networks/{network_code}/orders/{order_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListOrdersRequest(proto.Message):
    r"""Request object for ``ListOrders`` method.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of Orders.
            Format: ``networks/{network_code}``
        page_size (int):
            Optional. The maximum number of ``Orders`` to return. The
            service may return fewer than this value. If unspecified, at
            most 50 ``Orders`` will be returned. The maximum value is
            1000; values greater than 1000 will be coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListOrders`` call. Provide this to retrieve the subsequent
            page.

            When paginating, all other parameters provided to
            ``ListOrders`` must match the call that provided the page
            token.
        filter (str):
            Optional. Expression to filter the response. See syntax
            details at
            https://developers.google.com/ad-manager/api/beta/filters

            **Filterable fields:**

            - ``advertiser``
            - ``agency``
            - ``appliedTeams``
            - ``archived``
            - ``creator``
            - ``displayName``
            - ``endTime``
            - ``externalOrderId``
            - ``impressionsDelivered``
            - ``name``
            - ``orderId``
            - ``poNumber``
            - ``programmatic``
            - ``salesperson``
            - ``secondarySalespeople``
            - ``secondaryTraffickers``
            - ``startTime``
            - ``status``
            - ``totalClicksDelivered``
            - ``totalViewableImpressionsDelivered``
            - ``trafficker``
            - ``updateTime``
        order_by (str):
            Optional. Expression to specify sorting
            order. See syntax details at
            https://developers.google.com/ad-manager/api/beta/filters#order
        skip (int):
            Optional. Number of individual resources to
            skip while paginating.
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
    skip: int = proto.Field(
        proto.INT32,
        number=6,
    )


class ListOrdersResponse(proto.Message):
    r"""Response object for ``ListOrdersRequest`` containing matching
    ``Order`` resources.

    Attributes:
        orders (MutableSequence[google.ads.admanager_v1.types.Order]):
            The ``Order`` from the specified network.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        total_size (int):
            Total number of ``Orders``. If a filter was included in the
            request, this reflects the total number after the filtering
            is applied.

            ``total_size`` won't be calculated in the response unless it
            has been included in a response field mask. The response
            field mask can be provided to the method by using the URL
            parameter ``$fields`` or ``fields``, or by using the
            HTTP/gRPC header ``X-Goog-FieldMask``.

            For more information, see
            https://developers.google.com/ad-manager/api/beta/field-masks
    """

    @property
    def raw_page(self):
        return self

    orders: MutableSequence[order_messages.Order] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=order_messages.Order,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    total_size: int = proto.Field(
        proto.INT32,
        number=3,
    )


class CreateOrderRequest(proto.Message):
    r"""Request object for ``CreateOrder`` method.

    Attributes:
        parent (str):
            Required. The parent resource where this Order will be
            created. Format: ``networks/{network_code}``
        order (google.ads.admanager_v1.types.Order):
            Required. The ``Order`` to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    order: order_messages.Order = proto.Field(
        proto.MESSAGE,
        number=2,
        message=order_messages.Order,
    )


class UpdateOrderRequest(proto.Message):
    r"""Request object for ``UpdateOrder`` method.

    Attributes:
        order (google.ads.admanager_v1.types.Order):
            Required. The ``Order`` to update.

            The Order's name is used to identify the order to update.
            Format: ``networks/{network_code}/orders/{order_id}``
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update.
    """

    order: order_messages.Order = proto.Field(
        proto.MESSAGE,
        number=1,
        message=order_messages.Order,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class BatchCreateOrdersRequest(proto.Message):
    r"""Request object for ``BatchCreateOrders`` method.

    Attributes:
        parent (str):
            Required. The parent resource where ``Orders`` will be
            created. Format: ``networks/{network_code}`` The parent
            field in the CreateOrderRequest must match this field.
        requests (MutableSequence[google.ads.admanager_v1.types.CreateOrderRequest]):
            Required. The ``Order`` objects to create. A maximum of 100
            objects can be created in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["CreateOrderRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="CreateOrderRequest",
    )


class BatchCreateOrdersResponse(proto.Message):
    r"""Response object for ``BatchCreateOrders`` method.

    Attributes:
        orders (MutableSequence[google.ads.admanager_v1.types.Order]):
            The ``Order`` objects created.
    """

    orders: MutableSequence[order_messages.Order] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=order_messages.Order,
    )


class BatchUpdateOrdersRequest(proto.Message):
    r"""Request object for ``BatchUpdateOrders`` method.

    Attributes:
        parent (str):
            Required. The parent resource where ``Orders`` will be
            updated. Format: ``networks/{network_code}`` The parent
            field in the UpdateOrderRequest must match this field.
        requests (MutableSequence[google.ads.admanager_v1.types.UpdateOrderRequest]):
            Required. The ``Order`` objects to update. A maximum of 100
            objects can be updated in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["UpdateOrderRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="UpdateOrderRequest",
    )


class BatchUpdateOrdersResponse(proto.Message):
    r"""Response object for ``BatchUpdateOrders`` method.

    Attributes:
        orders (MutableSequence[google.ads.admanager_v1.types.Order]):
            The ``Order`` objects updated.
    """

    orders: MutableSequence[order_messages.Order] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=order_messages.Order,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
