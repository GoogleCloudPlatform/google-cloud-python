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

from google.ads.admanager_v1.types import application_messages

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "GetApplicationRequest",
        "ListApplicationsRequest",
        "ListApplicationsResponse",
        "CreateApplicationRequest",
        "BatchCreateApplicationsRequest",
        "BatchCreateApplicationsResponse",
        "UpdateApplicationRequest",
        "BatchUpdateApplicationsRequest",
        "BatchUpdateApplicationsResponse",
        "BatchArchiveApplicationsRequest",
        "BatchArchiveApplicationsResponse",
        "BatchUnarchiveApplicationsRequest",
        "BatchUnarchiveApplicationsResponse",
    },
)


class GetApplicationRequest(proto.Message):
    r"""Request object for ``GetApplication`` method.

    Attributes:
        name (str):
            Required. The resource name of the Application. Format:
            ``networks/{network_code}/applications/{application_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListApplicationsRequest(proto.Message):
    r"""Request object for ``ListApplications`` method.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of
            Applications. Format: ``networks/{network_code}``
        page_size (int):
            Optional. The maximum number of ``Applications`` to return.
            The service may return fewer than this value. If
            unspecified, at most 50 ``Applications`` will be returned.
            The maximum value is 1000; values greater than 1000 will be
            coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListApplications`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListApplications`` must match the call that provided the
            page token.
        filter (str):
            Optional. Expression to filter the response. See syntax
            details at
            https://developers.google.com/ad-manager/api/beta/filters

            **Filterable fields:**

            - ``appStoreId``
            - ``appStores``
            - ``applicationCode``
            - ``approvalStatus``
            - ``archived``
            - ``displayName``
            - ``name``
            - ``platform``
            - ``webviewClaimingStatus``
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


class ListApplicationsResponse(proto.Message):
    r"""Response object for ``ListApplicationsRequest`` containing matching
    ``Application`` objects.

    Attributes:
        applications (MutableSequence[google.ads.admanager_v1.types.Application]):
            The ``Application`` objects from the specified network.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        total_size (int):
            Total number of ``Application`` objects. If a filter was
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

    applications: MutableSequence[application_messages.Application] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=application_messages.Application,
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


class CreateApplicationRequest(proto.Message):
    r"""Request object for ``CreateApplication`` method.

    Attributes:
        parent (str):
            Required. The parent resource where this ``Application``
            will be created. Format: ``networks/{network_code}``
        application (google.ads.admanager_v1.types.Application):
            Required. The ``Application`` to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    application: application_messages.Application = proto.Field(
        proto.MESSAGE,
        number=2,
        message=application_messages.Application,
    )


class BatchCreateApplicationsRequest(proto.Message):
    r"""Request object for ``BatchCreateApplications`` method.

    Attributes:
        parent (str):
            Required. The parent resource where ``Applications`` will be
            created. Format: ``networks/{network_code}`` The parent
            field in the CreateApplicationRequest must match this field.
        requests (MutableSequence[google.ads.admanager_v1.types.CreateApplicationRequest]):
            Required. The ``Application`` objects to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["CreateApplicationRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="CreateApplicationRequest",
    )


class BatchCreateApplicationsResponse(proto.Message):
    r"""Response object for ``BatchCreateApplications`` method.

    Attributes:
        applications (MutableSequence[google.ads.admanager_v1.types.Application]):
            The ``Application`` objects created.
    """

    applications: MutableSequence[application_messages.Application] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=application_messages.Application,
        )
    )


class UpdateApplicationRequest(proto.Message):
    r"""Request object for ``UpdateApplication`` method.

    Attributes:
        application (google.ads.admanager_v1.types.Application):
            Required. The ``Application`` to update.

            The ``Application``'s ``name`` is used to identify the
            ``Application`` to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update.
    """

    application: application_messages.Application = proto.Field(
        proto.MESSAGE,
        number=1,
        message=application_messages.Application,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class BatchUpdateApplicationsRequest(proto.Message):
    r"""Request object for ``BatchUpdateApplications`` method.

    Attributes:
        parent (str):
            Required. The parent resource where ``Applications`` will be
            updated. Format: ``networks/{network_code}`` The parent
            field in the UpdateApplicationRequest must match this field.
        requests (MutableSequence[google.ads.admanager_v1.types.UpdateApplicationRequest]):
            Required. The ``Application`` objects to update.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["UpdateApplicationRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="UpdateApplicationRequest",
    )


class BatchUpdateApplicationsResponse(proto.Message):
    r"""Response object for ``BatchUpdateApplications`` method.

    Attributes:
        applications (MutableSequence[google.ads.admanager_v1.types.Application]):
            The ``Application`` objects updated.
    """

    applications: MutableSequence[application_messages.Application] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=application_messages.Application,
        )
    )


class BatchArchiveApplicationsRequest(proto.Message):
    r"""Request object for ``BatchArchiveApplications`` method.

    Attributes:
        parent (str):
            Required. The parent resource shared by all ``Applications``
            to archive. Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. The ``Application`` objects to archive.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchArchiveApplicationsResponse(proto.Message):
    r"""Response object for ``BatchArchiveApplications`` method."""


class BatchUnarchiveApplicationsRequest(proto.Message):
    r"""Request object for ``BatchUnarchiveApplications`` method.

    Attributes:
        parent (str):
            Required. The parent resource shared by all ``Applications``
            to Unarchive. Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. The ``Application`` objects to unarchive.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchUnarchiveApplicationsResponse(proto.Message):
    r"""Response object for ``BatchUnarchiveApplications`` method."""


__all__ = tuple(sorted(__protobuf__.manifest))
