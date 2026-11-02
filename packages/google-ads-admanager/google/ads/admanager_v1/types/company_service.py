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

from google.ads.admanager_v1.types import company_messages

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "GetCompanyRequest",
        "ListCompaniesRequest",
        "ListCompaniesResponse",
        "CreateCompanyRequest",
        "BatchCreateCompaniesRequest",
        "BatchCreateCompaniesResponse",
        "UpdateCompanyRequest",
        "BatchUpdateCompaniesRequest",
        "BatchUpdateCompaniesResponse",
    },
)


class GetCompanyRequest(proto.Message):
    r"""Request object for ``GetCompany`` method.

    Attributes:
        name (str):
            Required. The resource name of the Company. Format:
            ``networks/{network_code}/companies/{company_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListCompaniesRequest(proto.Message):
    r"""Request object for ``ListCompanies`` method.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of
            [Companies][google.ads.admanager.v1.Company]. Format:
            ``networks/{network_code}``
        page_size (int):
            Optional. The maximum number of
            [Companies][google.ads.admanager.v1.Company] to return. The
            service may return fewer than this value. If unspecified, at
            most 50 [Companies][google.ads.admanager.v1.Company] will be
            returned. The maximum value is 1000; values greater than
            1000 will be coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListCompanies`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListCompanies`` must match the call that provided the page
            token.
        filter (str):
            Optional. Expression to filter the response. See syntax
            details at
            https://developers.google.com/ad-manager/api/beta/filters

            **Filterable fields:**

            - ``address``
            - ``comment``
            - ``companyId``
            - ``creditStatus``
            - ``displayName``
            - ``email``
            - ``externalId``
            - ``fax``
            - ``name``
            - ``phone``
            - ``thirdPartyCompanyId``
            - ``type``
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


class ListCompaniesResponse(proto.Message):
    r"""Response object for ``ListCompaniesRequest`` containing matching
    [Company][google.ads.admanager.v1.Company] objects.

    Attributes:
        companies (MutableSequence[google.ads.admanager_v1.types.Company]):
            The [Company][google.ads.admanager.v1.Company] objects from
            the specified network.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        total_size (int):
            Total number of [Company][google.ads.admanager.v1.Company]
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

    companies: MutableSequence[company_messages.Company] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=company_messages.Company,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    total_size: int = proto.Field(
        proto.INT32,
        number=3,
    )


class CreateCompanyRequest(proto.Message):
    r"""Request object for ``CreateCompany`` method.

    Attributes:
        parent (str):
            Required. The parent resource where this
            [Company][google.ads.admanager.v1.Company] will be created.
            Format: ``networks/{network_code}``
        company (google.ads.admanager_v1.types.Company):
            Required. The [Company][google.ads.admanager.v1.Company] to
            create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    company: company_messages.Company = proto.Field(
        proto.MESSAGE,
        number=2,
        message=company_messages.Company,
    )


class BatchCreateCompaniesRequest(proto.Message):
    r"""Request object for ``BatchCreateCompanies`` method.

    Attributes:
        parent (str):
            Required. The parent resource where
            [Companies][google.ads.admanager.v1.Company] will be
            created. Format: ``networks/{network_code}`` The parent
            field in the CreateCompanyRequest must match this field.
        requests (MutableSequence[google.ads.admanager_v1.types.CreateCompanyRequest]):
            Required. The [Company][google.ads.admanager.v1.Company]
            objects to create. A maximum of 100 objects can be created
            in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["CreateCompanyRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="CreateCompanyRequest",
    )


class BatchCreateCompaniesResponse(proto.Message):
    r"""Response object for ``BatchCreateCompanies`` method.

    Attributes:
        companies (MutableSequence[google.ads.admanager_v1.types.Company]):
            The [Company][google.ads.admanager.v1.Company] objects
            created.
    """

    companies: MutableSequence[company_messages.Company] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=company_messages.Company,
    )


class UpdateCompanyRequest(proto.Message):
    r"""Request object for ``UpdateCompany`` method.

    Attributes:
        company (google.ads.admanager_v1.types.Company):
            Required. The [Company][google.ads.admanager.v1.Company] to
            update.

            The [Company][google.ads.admanager.v1.Company]'s ``name`` is
            used to identify the
            [Company][google.ads.admanager.v1.Company] to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update.
    """

    company: company_messages.Company = proto.Field(
        proto.MESSAGE,
        number=1,
        message=company_messages.Company,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class BatchUpdateCompaniesRequest(proto.Message):
    r"""Request object for ``BatchUpdateCompanies`` method.

    Attributes:
        parent (str):
            Required. The parent resource where
            [Companies][google.ads.admanager.v1.Company] will be
            updated. Format: ``networks/{network_code}`` The parent
            field in the UpdateCompanyRequest must match this field.
        requests (MutableSequence[google.ads.admanager_v1.types.UpdateCompanyRequest]):
            Required. The [Company][google.ads.admanager.v1.Company]
            objects to update. A maximum of 100 objects can be updated
            in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["UpdateCompanyRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="UpdateCompanyRequest",
    )


class BatchUpdateCompaniesResponse(proto.Message):
    r"""Response object for ``BatchUpdateCompanies`` method.

    Attributes:
        companies (MutableSequence[google.ads.admanager_v1.types.Company]):
            The [Company][google.ads.admanager.v1.Company] objects
            updated.
    """

    companies: MutableSequence[company_messages.Company] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=company_messages.Company,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
