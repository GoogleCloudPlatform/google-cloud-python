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

from google.ads.admanager_v1.types import private_auction_messages

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "GetPrivateAuctionRequest",
        "ListPrivateAuctionsRequest",
        "ListPrivateAuctionsResponse",
        "CreatePrivateAuctionRequest",
        "UpdatePrivateAuctionRequest",
    },
)


class GetPrivateAuctionRequest(proto.Message):
    r"""Request object for ``GetPrivateAuction`` method.

    Attributes:
        name (str):
            Required. The resource name of the PrivateAuction. Format:
            ``networks/{network_code}/privateAuctions/{private_auction_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListPrivateAuctionsRequest(proto.Message):
    r"""Request object for ``ListPrivateAuctions`` method.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of
            PrivateAuctions. Format: ``networks/{network_code}``
        page_size (int):
            Optional. The maximum number of ``PrivateAuctions`` to
            return. The service may return fewer than this value. If
            unspecified, at most 50 ``PrivateAuctions`` will be
            returned. The maximum value is 1000; values greater than
            1000 will be coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListPrivateAuctions`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListPrivateAuctions`` must match the call that provided
            the page token.
        filter (str):
            Optional. Expression to filter the response.
            See syntax details at
            https://developers.google.com/ad-manager/api/beta/filters
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


class ListPrivateAuctionsResponse(proto.Message):
    r"""Response object for ``ListPrivateAuctionsRequest`` containing
    matching ``PrivateAuction`` objects.

    Attributes:
        private_auctions (MutableSequence[google.ads.admanager_v1.types.PrivateAuction]):
            The ``PrivateAuction`` objects from the specified network.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        total_size (int):
            Total number of ``PrivateAuction`` objects. If a filter was
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

    private_auctions: MutableSequence[private_auction_messages.PrivateAuction] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=private_auction_messages.PrivateAuction,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    total_size: int = proto.Field(
        proto.INT32,
        number=3,
    )


class CreatePrivateAuctionRequest(proto.Message):
    r"""Request object for ``CreatePrivateAuction`` method.

    Attributes:
        parent (str):
            Required. The parent resource where this ``PrivateAuction``
            will be created. Format: ``networks/{network_code}``
        private_auction (google.ads.admanager_v1.types.PrivateAuction):
            Required. The ``PrivateAuction`` to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    private_auction: private_auction_messages.PrivateAuction = proto.Field(
        proto.MESSAGE,
        number=2,
        message=private_auction_messages.PrivateAuction,
    )


class UpdatePrivateAuctionRequest(proto.Message):
    r"""Request object for ``UpdatePrivateAuction`` method.

    Attributes:
        private_auction (google.ads.admanager_v1.types.PrivateAuction):
            Required. The ``PrivateAuction`` to update.

            The ``PrivateAuction``'s ``name`` is used to identify the
            ``PrivateAuction`` to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update.
    """

    private_auction: private_auction_messages.PrivateAuction = proto.Field(
        proto.MESSAGE,
        number=1,
        message=private_auction_messages.PrivateAuction,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
