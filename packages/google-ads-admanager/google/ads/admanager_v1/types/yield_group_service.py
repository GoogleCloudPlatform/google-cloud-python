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

from google.ads.admanager_v1.types import yield_group_messages

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "GetYieldGroupRequest",
        "ListYieldGroupsRequest",
        "ListYieldGroupsResponse",
        "CreateYieldGroupRequest",
        "BatchCreateYieldGroupsRequest",
        "BatchCreateYieldGroupsResponse",
        "UpdateYieldGroupRequest",
        "BatchUpdateYieldGroupsRequest",
        "BatchUpdateYieldGroupsResponse",
        "BatchActivateYieldGroupsRequest",
        "BatchActivateYieldGroupsResponse",
        "BatchDeactivateYieldGroupsRequest",
        "BatchDeactivateYieldGroupsResponse",
        "BatchArchiveYieldGroupsRequest",
        "BatchArchiveYieldGroupsResponse",
    },
)


class GetYieldGroupRequest(proto.Message):
    r"""Request object for ``GetYieldGroup`` method.

    Attributes:
        name (str):
            Required. The resource name of the ``YieldGroup``. Format:
            ``networks/{network_code}/yieldGroups/{yield_group_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListYieldGroupsRequest(proto.Message):
    r"""Request object for ``ListYieldGroups`` method.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of
            ``YieldGroups``. Format: ``networks/{network_code}``
        page_size (int):
            Optional. The maximum number of ``YieldGroups`` to return.
            The service may return fewer than this value. If
            unspecified, at most 50 ``YieldGroups`` will be returned.
            The maximum value is 1000; values greater than 1000 will be
            coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListYieldGroups`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListYieldGroups`` must match the call that provided the
            page token.
        filter (str):
            Optional. Expression to filter the response. See syntax
            details at
            https://developers.google.com/ad-manager/api/beta/filters

            Syntax summary: double-quoted ``"..."`` (never ``'...'``)
            strings and RFC 3339 timestamps, full resource names on
            reference fields (for example,
            ``order = "networks/123/orders/456"``, not ``*Id`` or bare
            IDs), prefix or suffix ``*`` wildcards with ``=``
            (``displayName = "foo*"``), ``:`` for substring or
            repeated-field matching, unquoted enums and booleans,
            uppercase ``AND``/``OR``/``NOT``, and standalone
            ``IN(field, SET(v1, v2))`` (not ``field IN (...)``).

            **Filterable fields:**

            - ``displayName``
            - ``name``
            - ``status``
            - ``targeting.geoTargeting.targetedGeos``
            - ``targeting.inventoryTargeting.targetedAdUnits.adUnit``
            - ``targeting.mobileApplicationTargeting.firstPartyTargeting.targetedApplications``
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


class ListYieldGroupsResponse(proto.Message):
    r"""Response object for ``ListYieldGroupsRequest`` containing matching
    ``YieldGroup`` objects.

    Attributes:
        yield_groups (MutableSequence[google.ads.admanager_v1.types.YieldGroup]):
            The ``YieldGroup`` objects from the specified network.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        total_size (int):
            Total number of ``YieldGroup`` objects. If a filter was
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

    yield_groups: MutableSequence[yield_group_messages.YieldGroup] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=yield_group_messages.YieldGroup,
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


class CreateYieldGroupRequest(proto.Message):
    r"""Request object for ``CreateYieldGroup`` method.

    Attributes:
        parent (str):
            Required. The parent resource where this ``YieldGroup`` will
            be created. Format: ``networks/{network_code}``
        yield_group (google.ads.admanager_v1.types.YieldGroup):
            Required. The ``YieldGroup`` to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    yield_group: yield_group_messages.YieldGroup = proto.Field(
        proto.MESSAGE,
        number=2,
        message=yield_group_messages.YieldGroup,
    )


class BatchCreateYieldGroupsRequest(proto.Message):
    r"""Request object for ``BatchCreateYieldGroups`` method.

    Attributes:
        parent (str):
            Required. The parent resource where ``YieldGroups`` will be
            created. Format: ``networks/{network_code}`` The parent
            field in the ``CreateYieldGroupRequest`` must match this
            field.
        requests (MutableSequence[google.ads.admanager_v1.types.CreateYieldGroupRequest]):
            Required. The ``YieldGroup`` objects to create. A maximum of
            100 objects can be created in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["CreateYieldGroupRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="CreateYieldGroupRequest",
    )


class BatchCreateYieldGroupsResponse(proto.Message):
    r"""Response object for ``BatchCreateYieldGroups`` method.

    Attributes:
        yield_groups (MutableSequence[google.ads.admanager_v1.types.YieldGroup]):
            The ``YieldGroup`` objects created.
    """

    yield_groups: MutableSequence[yield_group_messages.YieldGroup] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=yield_group_messages.YieldGroup,
        )
    )


class UpdateYieldGroupRequest(proto.Message):
    r"""Request object for ``UpdateYieldGroup`` method.

    Attributes:
        yield_group (google.ads.admanager_v1.types.YieldGroup):
            Required. The ``YieldGroup`` to update.

            The ``YieldGroup``'s ``name`` is used to identify the
            ``YieldGroup`` to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update.
    """

    yield_group: yield_group_messages.YieldGroup = proto.Field(
        proto.MESSAGE,
        number=1,
        message=yield_group_messages.YieldGroup,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class BatchUpdateYieldGroupsRequest(proto.Message):
    r"""Request object for ``BatchUpdateYieldGroups`` method.

    Attributes:
        parent (str):
            Required. The parent resource where ``YieldGroups`` will be
            updated. Format: ``networks/{network_code}`` The parent
            field in the ``UpdateYieldGroupRequest`` must match this
            field.
        requests (MutableSequence[google.ads.admanager_v1.types.UpdateYieldGroupRequest]):
            Required. The ``YieldGroup`` objects to update. A maximum of
            10 objects can be updated in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["UpdateYieldGroupRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="UpdateYieldGroupRequest",
    )


class BatchUpdateYieldGroupsResponse(proto.Message):
    r"""Response object for ``BatchUpdateYieldGroups`` method.

    Attributes:
        yield_groups (MutableSequence[google.ads.admanager_v1.types.YieldGroup]):
            The ``YieldGroup`` objects updated.
    """

    yield_groups: MutableSequence[yield_group_messages.YieldGroup] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=yield_group_messages.YieldGroup,
        )
    )


class BatchActivateYieldGroupsRequest(proto.Message):
    r"""Request object for ``BatchActivateYieldGroups`` method.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of
            ``YieldGroups``. Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. The resource names of the ``YieldGroups`` to
            activate. Format:
            ``networks/{network_code}/yieldGroups/{yield_group_id}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchActivateYieldGroupsResponse(proto.Message):
    r"""Response object for ``BatchActivateYieldGroups`` method."""


class BatchDeactivateYieldGroupsRequest(proto.Message):
    r"""Request object for ``BatchDeactivateYieldGroups`` method.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of
            ``YieldGroups``. Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. The resource names of the ``YieldGroups`` to
            deactivate. Format:
            ``networks/{network_code}/yieldGroups/{yield_group_id}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchDeactivateYieldGroupsResponse(proto.Message):
    r"""Response object for ``BatchDeactivateYieldGroups`` method."""


class BatchArchiveYieldGroupsRequest(proto.Message):
    r"""Request object for ``BatchArchiveYieldGroups`` method.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of
            ``YieldGroups``. Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. The resource names of the ``YieldGroups`` to
            archive. Format:
            ``networks/{network_code}/yieldGroups/{yield_group_id}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchArchiveYieldGroupsResponse(proto.Message):
    r"""Response object for ``BatchArchiveYieldGroups`` method."""


__all__ = tuple(sorted(__protobuf__.manifest))
