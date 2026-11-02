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

from google.ads.admanager_v1.types import ad_break_messages

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "GetAdBreakRequest",
        "ListAdBreaksRequest",
        "ListAdBreaksResponse",
        "CreateAdBreakRequest",
        "UpdateAdBreakRequest",
        "DeleteAdBreakRequest",
    },
)


class GetAdBreakRequest(proto.Message):
    r"""Request object for ``GetAdBreak`` method.

    Attributes:
        name (str):
            Required. The resource name of the AdBreak using the asset
            key or custom asset key.

            Format:
            ``networks/{network_code}/liveStreamEventsByAssetKey/{asset_key}/adBreaks/{ad_break_id}``
            ``networks/{network_code}/liveStreamEventsByCustomAssetKey/{custom_asset_key}/adBreaks/{ad_break_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListAdBreaksRequest(proto.Message):
    r"""Request object for ``ListAdBreaks`` method.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of
            AdBreaks.

            Formats:
            ``networks/{network_code}/liveStreamEventsByAssetKey/{asset_key}``
            ``networks/{network_code}/liveStreamEventsByCustomAssetKey/{custom_asset_key}``
        page_size (int):
            Optional. The maximum number of ``AdBreaks`` to return. The
            service might return fewer than this value. If unspecified,
            at most 10 ad breaks are returned. The maximum value is
            ``100``. Values above ``100`` are coerced to ``100``.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListAdBreaks`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListAdBreaks`` must match the call that provided the page
            token.
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


class ListAdBreaksResponse(proto.Message):
    r"""Response object for ``ListAdBreaksRequest`` containing matching
    ``AdBreak`` objects.

    Attributes:
        ad_breaks (MutableSequence[google.ads.admanager_v1.types.AdBreak]):
            The ``AdBreak`` objects from the specified network.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages. This field expires after five minutes.
        total_size (int):
            Total number of ``AdBreak`` objects. If a filter was
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

    ad_breaks: MutableSequence[ad_break_messages.AdBreak] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=ad_break_messages.AdBreak,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    total_size: int = proto.Field(
        proto.INT32,
        number=3,
    )


class CreateAdBreakRequest(proto.Message):
    r"""Request object for ``CreateAdBreak`` method.

    Attributes:
        parent (str):
            Required. The parent resource where this ``AdBreak`` will be
            created identified by an asset key or custom asset key.

            Formats:
            ``networks/{network_code}/liveStreamEventsByAssetKey/{asset_key}``
            ``networks/{network_code}/liveStreamEventsByCustomAssetKey/{custom_asset_key}``
        ad_break (google.ads.admanager_v1.types.AdBreak):
            Required. The ``AdBreak`` to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    ad_break: ad_break_messages.AdBreak = proto.Field(
        proto.MESSAGE,
        number=2,
        message=ad_break_messages.AdBreak,
    )


class UpdateAdBreakRequest(proto.Message):
    r"""Request object for ``UpdateAdBreak`` method.

    Attributes:
        ad_break (google.ads.admanager_v1.types.AdBreak):
            Required. The ``AdBreak`` to update.

            The ``AdBreak``'s ``name`` is used to identify the
            ``AdBreak`` to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update.
    """

    ad_break: ad_break_messages.AdBreak = proto.Field(
        proto.MESSAGE,
        number=1,
        message=ad_break_messages.AdBreak,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteAdBreakRequest(proto.Message):
    r"""Request object for ``DeleteAdBreak`` method.

    Attributes:
        name (str):
            Required. The name of the ad break to delete.

            Format:
            ``networks/{network_code}/liveStreamEventsByAssetKey/{asset_key}/adBreaks/{ad_break}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
