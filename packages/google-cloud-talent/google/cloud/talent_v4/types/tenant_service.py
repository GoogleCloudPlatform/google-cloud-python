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
from google.cloud.talent_v4.types import tenant as gct_tenant

__protobuf__ = proto.module(
    package="google.cloud.talent.v4",
    manifest={
        "CreateTenantRequest",
        "GetTenantRequest",
        "UpdateTenantRequest",
        "DeleteTenantRequest",
        "ListTenantsRequest",
        "ListTenantsResponse",
    },
)


class CreateTenantRequest(proto.Message):
    r"""The Request of the CreateTenant method.

    Attributes:
        parent (str):
            Required. Resource name of the project under which the
            tenant is created.

            The format is "projects/{project_id}", for example,
            "projects/foo".
        tenant (google.cloud.talent_v4.types.Tenant):
            Required. The tenant to be created.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    tenant: gct_tenant.Tenant = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gct_tenant.Tenant,
    )


class GetTenantRequest(proto.Message):
    r"""Request for getting a tenant by name.

    Attributes:
        name (str):
            Required. The resource name of the tenant to be retrieved.

            The format is "projects/{project_id}/tenants/{tenant_id}",
            for example, "projects/foo/tenants/bar".
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateTenantRequest(proto.Message):
    r"""Request for updating a specified tenant.

    Attributes:
        tenant (google.cloud.talent_v4.types.Tenant):
            Required. The tenant resource to replace the
            current resource in the system.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Strongly recommended for the best service experience.

            If
            [update_mask][google.cloud.talent.v4.UpdateTenantRequest.update_mask]
            is provided, only the specified fields in
            [tenant][google.cloud.talent.v4.UpdateTenantRequest.tenant]
            are updated. Otherwise all the fields are updated.

            A field mask to specify the tenant fields to be updated.
            Only top level fields of
            [Tenant][google.cloud.talent.v4.Tenant] are supported.
    """

    tenant: gct_tenant.Tenant = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gct_tenant.Tenant,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteTenantRequest(proto.Message):
    r"""Request to delete a tenant.

    Attributes:
        name (str):
            Required. The resource name of the tenant to be deleted.

            The format is "projects/{project_id}/tenants/{tenant_id}",
            for example, "projects/foo/tenants/bar".
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListTenantsRequest(proto.Message):
    r"""List tenants for which the client has ACL visibility.

    Attributes:
        parent (str):
            Required. Resource name of the project under which the
            tenant is created.

            The format is "projects/{project_id}", for example,
            "projects/foo".
        page_token (str):
            The starting indicator from which to return
            results.
        page_size (int):
            The maximum number of tenants to be returned,
            at most 100. Default is 100 if a non-positive
            number is provided.
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


class ListTenantsResponse(proto.Message):
    r"""The List tenants response object.

    Attributes:
        tenants (MutableSequence[google.cloud.talent_v4.types.Tenant]):
            Tenants for the current client.
        next_page_token (str):
            A token to retrieve the next page of results.
        metadata (google.cloud.talent_v4.types.ResponseMetadata):
            Additional information for the API
            invocation, such as the request tracking id.
    """

    @property
    def raw_page(self):
        return self

    tenants: MutableSequence[gct_tenant.Tenant] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gct_tenant.Tenant,
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
