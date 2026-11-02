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

from google.ads.admanager_v1.types import ad_spot_messages

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "GetAdSpotRequest",
        "ListAdSpotsRequest",
        "ListAdSpotsResponse",
        "CreateAdSpotRequest",
        "BatchCreateAdSpotsRequest",
        "BatchCreateAdSpotsResponse",
        "UpdateAdSpotRequest",
        "BatchUpdateAdSpotsRequest",
        "BatchUpdateAdSpotsResponse",
    },
)


class GetAdSpotRequest(proto.Message):
    r"""Request object for ``GetAdSpot`` method.

    Attributes:
        name (str):
            Required. The resource name of the AdSpot. Format:
            ``networks/{network_code}/adSpots/{ad_spot_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListAdSpotsRequest(proto.Message):
    r"""Request object for ``ListAdSpots`` method.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of AdSpots.
            Format: ``networks/{network_code}``
        page_size (int):
            Optional. The maximum number of ``AdSpots`` to return. The
            service may return fewer than this value. If unspecified, at
            most 50 ``AdSpots`` will be returned. The maximum value is
            1000; values greater than 1000 will be coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListAdSpots`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListAdSpots`` must match the call that provided the page
            token.
        filter (str):
            Optional. Expression to filter the response. See syntax
            details at
            https://developers.google.com/ad-manager/api/beta/filters

            **Filterable fields:**

            - ``canonicalDisplayName``
            - ``customSpot``
            - ``displayName``
            - ``flexible``
            - ``name``
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


class ListAdSpotsResponse(proto.Message):
    r"""Response object for ``ListAdSpotsRequest`` containing matching
    ``AdSpot`` objects.

    Attributes:
        ad_spots (MutableSequence[google.ads.admanager_v1.types.AdSpot]):
            The ``AdSpot`` objects from the specified network.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        total_size (int):
            Total number of ``AdSpot`` objects. If a filter was included
            in the request, this reflects the total number after the
            filtering is applied.

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

    ad_spots: MutableSequence[ad_spot_messages.AdSpot] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=ad_spot_messages.AdSpot,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    total_size: int = proto.Field(
        proto.INT32,
        number=3,
    )


class CreateAdSpotRequest(proto.Message):
    r"""Request object for ``CreateAdSpot`` method.

    Attributes:
        parent (str):
            Required. The parent resource where this ``AdSpot`` will be
            created. Format: ``networks/{network_code}``
        ad_spot (google.ads.admanager_v1.types.AdSpot):
            Required. The ``AdSpot`` to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    ad_spot: ad_spot_messages.AdSpot = proto.Field(
        proto.MESSAGE,
        number=2,
        message=ad_spot_messages.AdSpot,
    )


class BatchCreateAdSpotsRequest(proto.Message):
    r"""Request object for ``BatchCreateAdSpots`` method.

    Attributes:
        parent (str):
            Required. The parent resource where ``AdSpots`` will be
            created. Format: ``networks/{network_code}`` The parent
            field in the CreateAdSpotRequest must match this field.
        requests (MutableSequence[google.ads.admanager_v1.types.CreateAdSpotRequest]):
            Required. The ``AdSpot`` objects to create. A maximum of 100
            objects can be created in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["CreateAdSpotRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="CreateAdSpotRequest",
    )


class BatchCreateAdSpotsResponse(proto.Message):
    r"""Response object for ``BatchCreateAdSpots`` method.

    Attributes:
        ad_spots (MutableSequence[google.ads.admanager_v1.types.AdSpot]):
            The ``AdSpot`` objects created.
    """

    ad_spots: MutableSequence[ad_spot_messages.AdSpot] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=ad_spot_messages.AdSpot,
    )


class UpdateAdSpotRequest(proto.Message):
    r"""Request object for ``UpdateAdSpot`` method.

    Attributes:
        ad_spot (google.ads.admanager_v1.types.AdSpot):
            Required. The ``AdSpot`` to update.

            The ``AdSpot``'s ``name`` is used to identify the ``AdSpot``
            to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update.
    """

    ad_spot: ad_spot_messages.AdSpot = proto.Field(
        proto.MESSAGE,
        number=1,
        message=ad_spot_messages.AdSpot,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class BatchUpdateAdSpotsRequest(proto.Message):
    r"""Request object for ``BatchUpdateAdSpots`` method.

    Attributes:
        parent (str):
            Required. The parent resource where ``AdSpots`` will be
            updated. Format: ``networks/{network_code}`` The parent
            field in the UpdateAdSpotRequest must match this field.
        requests (MutableSequence[google.ads.admanager_v1.types.UpdateAdSpotRequest]):
            Required. The ``AdSpot`` objects to update. A maximum of 100
            objects can be updated in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["UpdateAdSpotRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="UpdateAdSpotRequest",
    )


class BatchUpdateAdSpotsResponse(proto.Message):
    r"""Response object for ``BatchUpdateAdSpots`` method.

    Attributes:
        ad_spots (MutableSequence[google.ads.admanager_v1.types.AdSpot]):
            The ``AdSpot`` objects updated.
    """

    ad_spots: MutableSequence[ad_spot_messages.AdSpot] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=ad_spot_messages.AdSpot,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
