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

from google.ads.admanager_v1.types import placement_messages

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "GetPlacementRequest",
        "ListPlacementsRequest",
        "ListPlacementsResponse",
        "CreatePlacementRequest",
        "BatchCreatePlacementsRequest",
        "BatchCreatePlacementsResponse",
        "UpdatePlacementRequest",
        "BatchUpdatePlacementsRequest",
        "BatchUpdatePlacementsResponse",
        "BatchActivatePlacementsRequest",
        "BatchActivatePlacementsResponse",
        "BatchDeactivatePlacementsRequest",
        "BatchDeactivatePlacementsResponse",
        "BatchArchivePlacementsRequest",
        "BatchArchivePlacementsResponse",
    },
)


class GetPlacementRequest(proto.Message):
    r"""Request object for ``GetPlacement`` method.

    Attributes:
        name (str):
            Required. The resource name of the Placement. Format:
            ``networks/{network_code}/placements/{placement_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListPlacementsRequest(proto.Message):
    r"""Request object for ``ListPlacements`` method.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of
            Placements. Format: ``networks/{network_code}``
        page_size (int):
            Optional. The maximum number of ``Placements`` to return.
            The service may return fewer than this value. If
            unspecified, at most 50 ``Placements`` will be returned. The
            maximum value is 1000; values greater than 1000 will be
            coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListPlacements`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListPlacements`` must match the call that provided the
            page token.
        filter (str):
            Optional. Expression to filter the response. See syntax
            details at
            https://developers.google.com/ad-manager/api/beta/filters

            **Filterable fields:**

            - ``description``
            - ``displayName``
            - ``name``
            - ``placementCode``
            - ``status``
            - ``targetedAdUnits``
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


class ListPlacementsResponse(proto.Message):
    r"""Response object for ``ListPlacementsRequest`` containing matching
    ``Placement`` objects.

    Attributes:
        placements (MutableSequence[google.ads.admanager_v1.types.Placement]):
            The ``Placement`` objects from the specified network.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        total_size (int):
            Total number of ``Placement`` objects. If a filter was
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

    placements: MutableSequence[placement_messages.Placement] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=placement_messages.Placement,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    total_size: int = proto.Field(
        proto.INT32,
        number=3,
    )


class CreatePlacementRequest(proto.Message):
    r"""Request object for ``CreatePlacement`` method.

    Attributes:
        parent (str):
            Required. The parent resource where this ``Placement`` will
            be created. Format: ``networks/{network_code}``
        placement (google.ads.admanager_v1.types.Placement):
            Required. The ``Placement`` to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    placement: placement_messages.Placement = proto.Field(
        proto.MESSAGE,
        number=2,
        message=placement_messages.Placement,
    )


class BatchCreatePlacementsRequest(proto.Message):
    r"""Request object for ``BatchCreatePlacements`` method.

    Attributes:
        parent (str):
            Required. The parent resource where the ``Placement``\ s
            will be created. Format: ``networks/{network_code}`` The
            parent field in the CreatePlacementRequest messages match
            this field.
        requests (MutableSequence[google.ads.admanager_v1.types.CreatePlacementRequest]):
            Required. The ``Placement`` objects to create. A maximum of
            100 objects can be created in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["CreatePlacementRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="CreatePlacementRequest",
    )


class BatchCreatePlacementsResponse(proto.Message):
    r"""Response object for ``BatchCreatePlacements`` method.

    Attributes:
        placements (MutableSequence[google.ads.admanager_v1.types.Placement]):
            The ``Placement`` objects created.
    """

    placements: MutableSequence[placement_messages.Placement] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=placement_messages.Placement,
    )


class UpdatePlacementRequest(proto.Message):
    r"""Request object for ``UpdatePlacement`` method.

    Attributes:
        placement (google.ads.admanager_v1.types.Placement):
            Required. The ``Placement`` to update.

            The ``Placement``'s name is used to identify the
            ``Placement`` to update. Format:
            ``networks/{network_code}/placements/{placement_id}``
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update.
    """

    placement: placement_messages.Placement = proto.Field(
        proto.MESSAGE,
        number=1,
        message=placement_messages.Placement,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class BatchUpdatePlacementsRequest(proto.Message):
    r"""Request object for ``BatchUpdatePlacements`` method.

    Attributes:
        parent (str):
            Required. The parent resource where ``Placements`` will be
            updated. Format: ``networks/{network_code}`` The parent
            field in the UpdatePlacementsRequest must match this field.
        requests (MutableSequence[google.ads.admanager_v1.types.UpdatePlacementRequest]):
            Required. The ``Placement`` objects to update. A maximum of
            100 objects can be updated in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["UpdatePlacementRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="UpdatePlacementRequest",
    )


class BatchUpdatePlacementsResponse(proto.Message):
    r"""Response object for ``BatchUpdatePlacements`` method.

    Attributes:
        placements (MutableSequence[google.ads.admanager_v1.types.Placement]):
            The ``Placement`` objects updated.
    """

    placements: MutableSequence[placement_messages.Placement] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=placement_messages.Placement,
    )


class BatchActivatePlacementsRequest(proto.Message):
    r"""Request message for ``BatchActivatePlacements`` method.

    Attributes:
        parent (str):
            Required. Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. The names of the ``Placement`` objects to
            activate. Format:
            ``networks/{network_code}/placements/{placement_id}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class BatchActivatePlacementsResponse(proto.Message):
    r"""Response object for ``BatchActivatePlacements`` method."""


class BatchDeactivatePlacementsRequest(proto.Message):
    r"""Request message for ``BatchDeactivatePlacements`` method.

    Attributes:
        parent (str):
            Required. Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. The names of the ``Placement`` objects to
            deactivate. Format:
            ``networks/{network_code}/placements/{placement_id}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class BatchDeactivatePlacementsResponse(proto.Message):
    r"""Response object for ``BatchDeactivatePlacements`` method."""


class BatchArchivePlacementsRequest(proto.Message):
    r"""Request message for ``BatchArchivePlacements`` method.

    Attributes:
        parent (str):
            Required. Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. The names of the ``Placement`` objects to archive.
            Format:
            ``networks/{network_code}/placements/{placement_id}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class BatchArchivePlacementsResponse(proto.Message):
    r"""Response object for ``BatchArchivePlacements`` method."""


__all__ = tuple(sorted(__protobuf__.manifest))
