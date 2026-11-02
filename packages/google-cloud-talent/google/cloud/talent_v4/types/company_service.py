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

from google.cloud.talent_v4.types import common
from google.cloud.talent_v4.types import company as gct_company

__protobuf__ = proto.module(
    package="google.cloud.talent.v4",
    manifest={
        "CreateCompanyRequest",
        "GetCompanyRequest",
        "UpdateCompanyRequest",
        "DeleteCompanyRequest",
        "ListCompaniesRequest",
        "ListCompaniesResponse",
    },
)


class CreateCompanyRequest(proto.Message):
    r"""The Request of the CreateCompany method.

    Attributes:
        parent (str):
            Required. Resource name of the tenant under which the
            company is created.

            The format is "projects/{project_id}/tenants/{tenant_id}",
            for example, "projects/foo/tenants/bar".
        company (google.cloud.talent_v4.types.Company):
            Required. The company to be created.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    company: gct_company.Company = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gct_company.Company,
    )


class GetCompanyRequest(proto.Message):
    r"""Request for getting a company by name.

    Attributes:
        name (str):
            Required. The resource name of the company to be retrieved.

            The format is
            "projects/{project_id}/tenants/{tenant_id}/companies/{company_id}",
            for example,
            "projects/api-test-project/tenants/foo/companies/bar".
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateCompanyRequest(proto.Message):
    r"""Request for updating a specified company.

    Attributes:
        company (google.cloud.talent_v4.types.Company):
            Required. The company resource to replace the
            current resource in the system.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Strongly recommended for the best service experience.

            If
            [update_mask][google.cloud.talent.v4.UpdateCompanyRequest.update_mask]
            is provided, only the specified fields in
            [company][google.cloud.talent.v4.UpdateCompanyRequest.company]
            are updated. Otherwise all the fields are updated.

            A field mask to specify the company fields to be updated.
            Only top level fields of
            [Company][google.cloud.talent.v4.Company] are supported.
    """

    company: gct_company.Company = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gct_company.Company,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteCompanyRequest(proto.Message):
    r"""Request to delete a company.

    Attributes:
        name (str):
            Required. The resource name of the company to be deleted.

            The format is
            "projects/{project_id}/tenants/{tenant_id}/companies/{company_id}",
            for example, "projects/foo/tenants/bar/companies/baz".
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListCompaniesRequest(proto.Message):
    r"""List companies for which the client has ACL visibility.

    Attributes:
        parent (str):
            Required. Resource name of the tenant under which the
            company is created.

            The format is "projects/{project_id}/tenants/{tenant_id}",
            for example, "projects/foo/tenants/bar".
        page_token (str):
            The starting indicator from which to return
            results.
        page_size (int):
            The maximum number of companies to be
            returned, at most 100. Default is 100 if a
            non-positive number is provided.
        require_open_jobs (bool):
            Set to true if the companies requested must have open jobs.

            Defaults to false.

            If true, at most
            [page_size][google.cloud.talent.v4.ListCompaniesRequest.page_size]
            of companies are fetched, among which only those with open
            jobs are returned.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    require_open_jobs: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class ListCompaniesResponse(proto.Message):
    r"""The List companies response object.

    Attributes:
        companies (MutableSequence[google.cloud.talent_v4.types.Company]):
            Companies for the current client.
        next_page_token (str):
            A token to retrieve the next page of results.
        metadata (google.cloud.talent_v4.types.ResponseMetadata):
            Additional information for the API
            invocation, such as the request tracking id.
    """

    @property
    def raw_page(self):
        return self

    companies: MutableSequence[gct_company.Company] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gct_company.Company,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    metadata: common.ResponseMetadata = proto.Field(
        proto.MESSAGE,
        number=3,
        message=common.ResponseMetadata,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
