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

from google.ads.admanager_v1.types import line_item_messages

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "GetLineItemRequest",
        "ListLineItemsRequest",
        "ListLineItemsResponse",
        "CreateLineItemRequest",
        "BatchCreateLineItemsRequest",
        "BatchCreateLineItemsResponse",
        "UpdateLineItemRequest",
        "BatchUpdateLineItemsRequest",
        "BatchUpdateLineItemsResponse",
        "BatchActivateLineItemsRequest",
        "BatchActivateLineItemsResponse",
        "BatchPauseLineItemsRequest",
        "BatchPauseLineItemsResponse",
        "BatchResumeLineItemsRequest",
        "BatchResumeLineItemsResponse",
        "BatchResumeAndOverbookLineItemsRequest",
        "BatchResumeAndOverbookLineItemsResponse",
        "BatchDeleteLineItemsRequest",
        "BatchReserveLineItemsRequest",
        "BatchReserveLineItemsResponse",
        "BatchReserveAndOverbookLineItemsRequest",
        "BatchReserveAndOverbookLineItemsResponse",
        "BatchReleaseLineItemsRequest",
        "BatchReleaseLineItemsResponse",
        "BatchArchiveLineItemsRequest",
        "BatchArchiveLineItemsResponse",
        "BatchUnarchiveLineItemsRequest",
        "BatchUnarchiveLineItemsResponse",
    },
)


class GetLineItemRequest(proto.Message):
    r"""Request object for ``GetLineItem`` method.

    Attributes:
        name (str):
            Required. The resource name of the LineItem. Format:
            ``networks/{network_code}/lineItems/{line_item_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListLineItemsRequest(proto.Message):
    r"""Request object for ``ListLineItems`` method.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of
            LineItems. Format: ``networks/{network_code}``
        page_size (int):
            Optional. The maximum number of ``LineItems`` to return. The
            service may return fewer than this value. If unspecified, at
            most 50 ``LineItems`` will be returned. The maximum value is
            1000; values greater than 1000 will be coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListLineItems`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListLineItems`` must match the call that provided the page
            token.
        filter (str):
            Optional. Expression to filter the response. See syntax
            details at
            https://developers.google.com/ad-manager/api/beta/filters

            **Filterable fields:**

            - ``archived``
            - ``contractedUnitsBought``
            - ``costType``
            - ``createTime``
            - ``creativePlaceholders.size.canonicalName``
            - ``dealInfo.externalDealId``
            - ``deliveryRateType``
            - ``displayName``
            - ``endTime``
            - ``environmentType``
            - ``externalLineItemId``
            - ``goal.units``
            - ``grpSettings.growbirdNielsenEnabled``
            - ``grpSettings.inTargetRatioEstimateMilliPercent``
            - ``lineItemType``
            - ``missingCreatives``
            - ``name``
            - ``notes``
            - ``order``
            - ``orderDisplayName``
            - ``priority``
            - ``roadblockingType``
            - ``startTime``
            - ``stats.clickThroughRate``
            - ``stats.clicksDelivered``
            - ``stats.impressionsDelivered``
            - ``stats.viewableImpressionsDelivered``
            - ``status``
            - ``targeting.inventoryTargeting.targetedAdUnits.adUnit``
            - ``targeting.inventoryTargeting.targetedPlacements``
            - ``targeting.mobileApplicationTargeting.firstPartyTargeting.targetedApplications``
            - ``updateSource``
            - ``updateTime``
            - ``webPropertyCode``
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


class ListLineItemsResponse(proto.Message):
    r"""Response object for ``ListLineItemsRequest`` containing matching
    ``LineItem`` objects.

    Attributes:
        line_items (MutableSequence[google.ads.admanager_v1.types.LineItem]):
            The ``LineItem`` objects from the specified network.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        total_size (int):
            Total number of ``LineItem`` objects. If a filter was
            included in the request, this reflects the total number
            after the filtering is applied.

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

    line_items: MutableSequence[line_item_messages.LineItem] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=line_item_messages.LineItem,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    total_size: int = proto.Field(
        proto.INT32,
        number=3,
    )


class CreateLineItemRequest(proto.Message):
    r"""Request object for ``CreateLineItem`` method.

    Attributes:
        parent (str):
            Required. The parent resource where this ``LineItem`` will
            be created. Format: ``networks/{network_code}``
        line_item (google.ads.admanager_v1.types.LineItem):
            Required. The ``LineItem`` to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    line_item: line_item_messages.LineItem = proto.Field(
        proto.MESSAGE,
        number=2,
        message=line_item_messages.LineItem,
    )


class BatchCreateLineItemsRequest(proto.Message):
    r"""Request object for ``BatchCreateLineItems`` method.

    Attributes:
        parent (str):
            Required. The parent resource where ``LineItems`` will be
            created. Format: ``networks/{network_code}`` The parent
            field in the CreateLineItemRequest must match this field.
        requests (MutableSequence[google.ads.admanager_v1.types.CreateLineItemRequest]):
            Required. The ``LineItem`` objects to create. A maximum of
            100 objects can be created in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["CreateLineItemRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="CreateLineItemRequest",
    )


class BatchCreateLineItemsResponse(proto.Message):
    r"""Response object for ``BatchCreateLineItems`` method.

    Attributes:
        line_items (MutableSequence[google.ads.admanager_v1.types.LineItem]):
            The ``LineItem`` objects created.
    """

    line_items: MutableSequence[line_item_messages.LineItem] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=line_item_messages.LineItem,
    )


class UpdateLineItemRequest(proto.Message):
    r"""Request object for ``UpdateLineItem`` method.

    Attributes:
        line_item (google.ads.admanager_v1.types.LineItem):
            Required. The ``LineItem`` to update.

            The ``LineItem``'s ``name`` is used to identify the
            ``LineItem`` to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update.
    """

    line_item: line_item_messages.LineItem = proto.Field(
        proto.MESSAGE,
        number=1,
        message=line_item_messages.LineItem,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class BatchUpdateLineItemsRequest(proto.Message):
    r"""Request object for ``BatchUpdateLineItems`` method.

    Attributes:
        parent (str):
            Required. The parent resource where ``LineItems`` will be
            updated. Format: ``networks/{network_code}`` The parent
            segment of the ``line_item.name`` in each
            ``UpdateLineItemRequest`` must match this field.
        requests (MutableSequence[google.ads.admanager_v1.types.UpdateLineItemRequest]):
            Required. The ``LineItem`` objects to update. A maximum of
            100 objects can be updated in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["UpdateLineItemRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="UpdateLineItemRequest",
    )


class BatchUpdateLineItemsResponse(proto.Message):
    r"""Response object for ``BatchUpdateLineItems`` method.

    Attributes:
        line_items (MutableSequence[google.ads.admanager_v1.types.LineItem]):
            The ``LineItem`` objects updated.
    """

    line_items: MutableSequence[line_item_messages.LineItem] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=line_item_messages.LineItem,
    )


class BatchActivateLineItemsRequest(proto.Message):
    r"""Request object for ``BatchActivateLineItems`` method.

    Attributes:
        parent (str):
            Required. The parent resource where ``LineItems`` will be
            updated. Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. The names of the ``LineItem`` objects to activate.
            Format: ``networks/{network_code}/lineItems/{line_item}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchActivateLineItemsResponse(proto.Message):
    r"""Response object for ``BatchActivateLineItems`` method."""


class BatchPauseLineItemsRequest(proto.Message):
    r"""Request object for ``BatchPauseLineItems`` method.

    Attributes:
        parent (str):
            Required. The parent resource where ``LineItems`` will be
            updated. Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. The names of the ``LineItem`` objects to pause.
            Format: ``networks/{network_code}/lineItems/{line_item}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchPauseLineItemsResponse(proto.Message):
    r"""Response object for ``BatchPauseLineItems`` method."""


class BatchResumeLineItemsRequest(proto.Message):
    r"""Request object for ``BatchResumeLineItems`` method.

    Attributes:
        parent (str):
            Required. The parent resource where ``LineItems`` will be
            updated. Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. The names of the ``LineItem`` objects to resume.
            Format: ``networks/{network_code}/lineItems/{line_item}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchResumeLineItemsResponse(proto.Message):
    r"""Response object for ``BatchResumeLineItems`` method."""


class BatchResumeAndOverbookLineItemsRequest(proto.Message):
    r"""Request object for ``BatchResumeAndOverbookLineItems`` method.

    Attributes:
        parent (str):
            Required. The parent resource where ``LineItems`` will be
            updated. Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. The names of the ``LineItem`` objects to resume
            and overbook. Format:
            ``networks/{network_code}/lineItems/{line_item}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchResumeAndOverbookLineItemsResponse(proto.Message):
    r"""Response object for ``BatchResumeAndOverbookLineItems`` method."""


class BatchDeleteLineItemsRequest(proto.Message):
    r"""Request object for ``BatchDeleteLineItems`` method.

    Attributes:
        parent (str):
            Required. The parent resource where ``LineItems`` will be
            updated. Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. The names of the ``LineItem`` objects to delete.
            Format: ``networks/{network_code}/lineItems/{line_item}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchReserveLineItemsRequest(proto.Message):
    r"""Request object for ``BatchReserveLineItems`` method.

    Attributes:
        parent (str):
            Required. The parent resource where ``LineItems`` will be
            updated. Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. The names of the ``LineItem`` objects to reserve.
            Format: ``networks/{network_code}/lineItems/{line_item}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchReserveLineItemsResponse(proto.Message):
    r"""Response object for ``BatchReserveLineItems`` method."""


class BatchReserveAndOverbookLineItemsRequest(proto.Message):
    r"""Request object for ``BatchReserveAndOverbookLineItems`` method.

    Attributes:
        parent (str):
            Required. The parent resource where ``LineItems`` will be
            updated. Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. The names of the ``LineItem`` objects to reserve
            and overbook. Format:
            ``networks/{network_code}/lineItems/{line_item}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchReserveAndOverbookLineItemsResponse(proto.Message):
    r"""Response object for ``BatchReserveAndOverbookLineItems`` method."""


class BatchReleaseLineItemsRequest(proto.Message):
    r"""Request object for ``BatchReleaseLineItems`` method.

    Attributes:
        parent (str):
            Required. The parent resource where ``LineItems`` will be
            updated. Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. The names of the ``LineItem`` objects to release.
            Format: ``networks/{network_code}/lineItems/{line_item}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchReleaseLineItemsResponse(proto.Message):
    r"""Response object for ``BatchReleaseLineItems`` method."""


class BatchArchiveLineItemsRequest(proto.Message):
    r"""Request object for ``BatchArchiveLineItems`` method.

    Attributes:
        parent (str):
            Required. The parent resource where ``LineItems`` will be
            updated. Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. The names of the ``LineItem`` objects to archive.
            Format: ``networks/{network_code}/lineItems/{line_item}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchArchiveLineItemsResponse(proto.Message):
    r"""Response object for ``BatchArchiveLineItems`` method."""


class BatchUnarchiveLineItemsRequest(proto.Message):
    r"""Request object for ``BatchUnarchiveLineItems`` method.

    Attributes:
        parent (str):
            Required. The parent resource where ``LineItems`` will be
            unarchived. Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. The names of the ``LineItem`` objects to extract.
            Format: ``networks/{network_code}/lineItems/{line_item}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchUnarchiveLineItemsResponse(proto.Message):
    r"""Response object for ``BatchUnarchiveLineItems`` method."""


__all__ = tuple(sorted(__protobuf__.manifest))
