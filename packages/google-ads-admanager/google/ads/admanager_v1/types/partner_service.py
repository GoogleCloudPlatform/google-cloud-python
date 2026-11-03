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

from google.ads.admanager_v1.types import partner_messages

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "GetPartnerRequest",
        "ListPartnersRequest",
        "ListPartnersResponse",
        "UpdatePartnerRequest",
        "BatchUpdatePartnersRequest",
        "BatchUpdatePartnersResponse",
    },
)


class GetPartnerRequest(proto.Message):
    r"""Request object for ``GetPartner`` method.

    Attributes:
        name (str):
            Required. The resource name of the
            [Partner][google.ads.admanager.v1.Partner]. Format:
            ``networks/{network_code}/partners/{partner_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListPartnersRequest(proto.Message):
    r"""Request object for ``ListPartners`` method.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of
            [Partners][google.ads.admanager.v1.Partner]. Format:
            ``networks/{network_code}``
        page_size (int):
            Optional. The maximum number of
            [Partners][google.ads.admanager.v1.Partner] to return. The
            service may return fewer than this value. If unspecified, at
            most 50 [Partners][google.ads.admanager.v1.Partner] will be
            returned. The maximum value is 1000; values greater than
            1000 will be coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListPartners`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListPartners`` must match the call that provided the page
            token.
        filter (str):
            Optional. Expression to filter the response. See syntax
            details at
            https://developers.google.com/ad-manager/api/beta/filters

            **Filterable fields:**

            - ``address``
            - ``comment``
            - ``creditStatus``
            - ``displayName``
            - ``email``
            - ``externalId``
            - ``fax``
            - ``name``
            - ``phone``
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


class ListPartnersResponse(proto.Message):
    r"""Response object for ``ListPartnersRequest`` containing matching
    [Partner][google.ads.admanager.v1.Partner] objects.

    Attributes:
        partners (MutableSequence[google.ads.admanager_v1.types.Partner]):
            The [Partner][google.ads.admanager.v1.Partner] objects from
            the specified network.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        total_size (int):
            Total number of [Partner][google.ads.admanager.v1.Partner]
            objects. If a filter was included in the request, this
            reflects the total number after the filtering is applied.

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

    partners: MutableSequence[partner_messages.Partner] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=partner_messages.Partner,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    total_size: int = proto.Field(
        proto.INT32,
        number=3,
    )


class UpdatePartnerRequest(proto.Message):
    r"""Request object for ``UpdatePartner`` method.

    Attributes:
        partner (google.ads.admanager_v1.types.Partner):
            Required. The [Partner][google.ads.admanager.v1.Partner] to
            update.

            The [Partner][google.ads.admanager.v1.Partner]'s ``name`` is
            used to identify the
            [Partner][google.ads.admanager.v1.Partner] to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update.
    """

    partner: partner_messages.Partner = proto.Field(
        proto.MESSAGE,
        number=1,
        message=partner_messages.Partner,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class BatchUpdatePartnersRequest(proto.Message):
    r"""Request object for ``BatchUpdatePartners`` method.

    Attributes:
        parent (str):
            Required. The parent resource where
            [Partners][google.ads.admanager.v1.Partner] will be updated.
            Format: ``networks/{network_code}`` The parent field in the
            ``UpdatePartnerRequest`` must match this field.
        requests (MutableSequence[google.ads.admanager_v1.types.UpdatePartnerRequest]):
            Required. The [Partner][google.ads.admanager.v1.Partner]
            objects to update. A maximum of 100 objects can be updated
            in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["UpdatePartnerRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="UpdatePartnerRequest",
    )


class BatchUpdatePartnersResponse(proto.Message):
    r"""Response object for ``BatchUpdatePartners`` method.

    Attributes:
        partners (MutableSequence[google.ads.admanager_v1.types.Partner]):
            The [Partner][google.ads.admanager.v1.Partner] objects
            updated.
    """

    partners: MutableSequence[partner_messages.Partner] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=partner_messages.Partner,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
