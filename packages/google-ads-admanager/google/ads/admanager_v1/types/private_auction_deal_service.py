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

from google.ads.admanager_v1.types import private_auction_deal_messages

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "GetPrivateAuctionDealRequest",
        "ListPrivateAuctionDealsRequest",
        "ListPrivateAuctionDealsResponse",
        "CreatePrivateAuctionDealRequest",
        "UpdatePrivateAuctionDealRequest",
    },
)


class GetPrivateAuctionDealRequest(proto.Message):
    r"""Request object for ``GetPrivateAuctionDeal`` method.

    Attributes:
        name (str):
            Required. The resource name of the PrivateAuctionDeal.
            Format:
            ``networks/{network_code}/privateAuctionDeals/{private_auction_deal_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListPrivateAuctionDealsRequest(proto.Message):
    r"""Request object for ``ListPrivateAuctionDeals`` method.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of
            PrivateAuctionDeals. Format: ``networks/{network_code}``
        page_size (int):
            Optional. The maximum number of ``PrivateAuctionDeals`` to
            return. The service may return fewer than this value. If
            unspecified, at most 50 ``PrivateAuctionDeals`` will be
            returned. The maximum value is 1000; values greater than
            1000 will be coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListPrivateAuctionDeals`` call. Provide this to retrieve
            the subsequent page.

            When paginating, all other parameters provided to
            ``ListPrivateAuctionDeals`` must match the call that
            provided the page token.
        filter (str):
            Optional. Expression to filter the response. See syntax
            details at
            https://developers.google.com/ad-manager/api/beta/filters

            **Filterable fields:**

            - ``archived``
            - ``auctionPriorityEnabled``
            - ``blockOverrideEnabled``
            - ``buyerAccountId``
            - ``buyerPermissionType``
            - ``endTime``
            - ``externalDealId``
            - ``floorPrice``
            - ``name``
            - ``privateAuctionDealId``
            - ``privateAuctionDisplayName``
            - ``privateAuctionId``
            - ``publisherFloorExempt``
            - ``status``
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


class ListPrivateAuctionDealsResponse(proto.Message):
    r"""Response object for ``ListPrivateAuctionDealsRequest`` containing
    matching ``PrivateAuctionDeal`` objects.

    Attributes:
        private_auction_deals (MutableSequence[google.ads.admanager_v1.types.PrivateAuctionDeal]):
            The ``PrivateAuctionDeal`` objects from the specified
            network.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        total_size (int):
            Total number of ``PrivateAuctionDeal`` objects. If a filter
            was included in the request, this reflects the total number
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

    private_auction_deals: MutableSequence[
        private_auction_deal_messages.PrivateAuctionDeal
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=private_auction_deal_messages.PrivateAuctionDeal,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    total_size: int = proto.Field(
        proto.INT32,
        number=3,
    )


class CreatePrivateAuctionDealRequest(proto.Message):
    r"""Request object for ``CreatePrivateAuctionDeal`` method.

    Attributes:
        parent (str):
            Required. The parent resource where this
            ``PrivateAuctionDeal`` will be created. Format:
            ``networks/{network_code}``
        private_auction_deal (google.ads.admanager_v1.types.PrivateAuctionDeal):
            Required. The ``PrivateAuctionDeal`` to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    private_auction_deal: private_auction_deal_messages.PrivateAuctionDeal = (
        proto.Field(
            proto.MESSAGE,
            number=2,
            message=private_auction_deal_messages.PrivateAuctionDeal,
        )
    )


class UpdatePrivateAuctionDealRequest(proto.Message):
    r"""Request object for ``UpdatePrivateAuctionDeal`` method.

    Attributes:
        private_auction_deal (google.ads.admanager_v1.types.PrivateAuctionDeal):
            Required. The ``PrivateAuctionDeal`` to update.

            The ``PrivateAuctionDeal``'s ``name`` is used to identify
            the ``PrivateAuctionDeal`` to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update.
    """

    private_auction_deal: private_auction_deal_messages.PrivateAuctionDeal = (
        proto.Field(
            proto.MESSAGE,
            number=1,
            message=private_auction_deal_messages.PrivateAuctionDeal,
        )
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
