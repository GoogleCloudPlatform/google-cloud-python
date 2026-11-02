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

from google.ads.admanager_v1.types import site_messages

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "GetSiteRequest",
        "ListSitesRequest",
        "ListSitesResponse",
        "CreateSiteRequest",
        "BatchCreateSitesRequest",
        "BatchCreateSitesResponse",
        "UpdateSiteRequest",
        "BatchUpdateSitesRequest",
        "BatchUpdateSitesResponse",
        "BatchDeactivateSitesRequest",
        "BatchDeactivateSitesResponse",
        "BatchSubmitSitesForApprovalRequest",
        "BatchSubmitSitesForApprovalResponse",
    },
)


class GetSiteRequest(proto.Message):
    r"""Request object for ``GetSite`` method.

    Attributes:
        name (str):
            Required. The resource name of the Site. Format:
            ``networks/{network_code}/sites/{site_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListSitesRequest(proto.Message):
    r"""Request object for ``ListSites`` method.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of Sites.
            Format: ``networks/{network_code}``
        page_size (int):
            Optional. The maximum number of ``Sites`` to return. The
            service may return fewer than this value. If unspecified, at
            most 50 ``Sites`` will be returned. The maximum value is
            1000; values greater than 1000 will be coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListSites`` call. Provide this to retrieve the subsequent
            page.

            When paginating, all other parameters provided to
            ``ListSites`` must match the call that provided the page
            token.
        filter (str):
            Optional. Expression to filter the response. See syntax
            details at
            https://developers.google.com/ad-manager/api/beta/filters

            **Filterable fields:**

            - ``approvalStatus``
            - ``approvalStatusUpdateTime``
            - ``childNetworkCode``
            - ``name``
            - ``url``
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


class ListSitesResponse(proto.Message):
    r"""Response object for ``ListSitesRequest`` containing matching
    ``Site`` objects.

    Attributes:
        sites (MutableSequence[google.ads.admanager_v1.types.Site]):
            The ``Site`` objects from the specified network.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        total_size (int):
            Total number of ``Site`` objects. If a filter was included
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

    sites: MutableSequence[site_messages.Site] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=site_messages.Site,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    total_size: int = proto.Field(
        proto.INT32,
        number=3,
    )


class CreateSiteRequest(proto.Message):
    r"""Request object for ``CreateSite`` method.

    Attributes:
        parent (str):
            Required. The parent resource where this ``Site`` will be
            created. Format: ``networks/{network_code}``
        site (google.ads.admanager_v1.types.Site):
            Required. The ``Site`` to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    site: site_messages.Site = proto.Field(
        proto.MESSAGE,
        number=2,
        message=site_messages.Site,
    )


class BatchCreateSitesRequest(proto.Message):
    r"""Request object for ``BatchCreateSites`` method.

    Attributes:
        parent (str):
            Required. The parent resource where ``Sites`` will be
            created. Format: ``networks/{network_code}`` The parent
            field in the CreateSiteRequest must match this field.
        requests (MutableSequence[google.ads.admanager_v1.types.CreateSiteRequest]):
            Required. The ``Site`` objects to create. A maximum of 100
            objects can be created in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["CreateSiteRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="CreateSiteRequest",
    )


class BatchCreateSitesResponse(proto.Message):
    r"""Response object for ``BatchCreateSites`` method.

    Attributes:
        sites (MutableSequence[google.ads.admanager_v1.types.Site]):
            The ``Site`` objects created.
    """

    sites: MutableSequence[site_messages.Site] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=site_messages.Site,
    )


class UpdateSiteRequest(proto.Message):
    r"""Request object for ``UpdateSite`` method.

    Attributes:
        site (google.ads.admanager_v1.types.Site):
            Required. The ``Site`` to update.

            The ``Site``'s ``name`` is used to identify the ``Site`` to
            update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update.
    """

    site: site_messages.Site = proto.Field(
        proto.MESSAGE,
        number=1,
        message=site_messages.Site,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class BatchUpdateSitesRequest(proto.Message):
    r"""Request object for ``BatchUpdateSites`` method.

    Attributes:
        parent (str):
            Required. The parent resource where ``Sites`` will be
            updated. Format: ``networks/{network_code}`` The parent
            field in the UpdateSiteRequest must match this field.
        requests (MutableSequence[google.ads.admanager_v1.types.UpdateSiteRequest]):
            Required. The ``Site`` objects to update. A maximum of 100
            objects can be updated in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["UpdateSiteRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="UpdateSiteRequest",
    )


class BatchUpdateSitesResponse(proto.Message):
    r"""Response object for ``BatchUpdateSites`` method.

    Attributes:
        sites (MutableSequence[google.ads.admanager_v1.types.Site]):
            The ``Site`` objects updated.
    """

    sites: MutableSequence[site_messages.Site] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=site_messages.Site,
    )


class BatchDeactivateSitesRequest(proto.Message):
    r"""Request message for ``BatchDeactivateSites`` method.

    Attributes:
        parent (str):
            Required. Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. The resource names of the ``Site`` objects to
            deactivate.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchDeactivateSitesResponse(proto.Message):
    r"""Response object for ``BatchDeactivateSites`` method."""


class BatchSubmitSitesForApprovalRequest(proto.Message):
    r"""Request message for ``BatchSubmitSitesForApproval`` method.

    Attributes:
        parent (str):
            Required. Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. The resource names of the ``Site`` objects to
            submit for approval.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchSubmitSitesForApprovalResponse(proto.Message):
    r"""Response object for ``BatchSubmitSitesForApproval`` method."""


__all__ = tuple(sorted(__protobuf__.manifest))
