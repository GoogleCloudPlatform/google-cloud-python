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

from google.cloud.saasplatform_saasservicemgmt_v1beta1.types import (
    deployments_resources,
)

__protobuf__ = proto.module(
    package="google.cloud.saasplatform.saasservicemgmt.v1beta1",
    manifest={
        "ListSaasRequest",
        "ListSaasResponse",
        "GetSaasRequest",
        "CreateSaasRequest",
        "UpdateSaasRequest",
        "DeleteSaasRequest",
        "ListTenantsRequest",
        "ListTenantsResponse",
        "GetTenantRequest",
        "CreateTenantRequest",
        "UpdateTenantRequest",
        "DeleteTenantRequest",
        "ListUnitKindsRequest",
        "ListUnitKindsResponse",
        "GetUnitKindRequest",
        "CreateUnitKindRequest",
        "UpdateUnitKindRequest",
        "DeleteUnitKindRequest",
        "ListUnitsRequest",
        "ListUnitsResponse",
        "GetUnitRequest",
        "CreateUnitRequest",
        "UpdateUnitRequest",
        "DeleteUnitRequest",
        "ListUnitOperationsRequest",
        "ListUnitOperationsResponse",
        "GetUnitOperationRequest",
        "CreateUnitOperationRequest",
        "UpdateUnitOperationRequest",
        "DeleteUnitOperationRequest",
        "ListReleasesRequest",
        "ListReleasesResponse",
        "GetReleaseRequest",
        "CreateReleaseRequest",
        "UpdateReleaseRequest",
        "DeleteReleaseRequest",
    },
)


class ListSaasRequest(proto.Message):
    r"""The request structure for the ListSaas method.

    Attributes:
        parent (str):
            Required. The parent of the saas.
        page_size (int):
            The maximum number of saas to send per page.
        page_token (str):
            The page token: If the next_page_token from a previous
            response is provided, this request will send the subsequent
            page.
        filter (str):
            Filter the list as specified in
            https://google.aip.dev/160.
        order_by (str):
            Order results as specified in
            https://google.aip.dev/132.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=10006,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=10505,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=10506,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=10507,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=10508,
    )


class ListSaasResponse(proto.Message):
    r"""The response structure for the ListSaas method.

    Attributes:
        saas (MutableSequence[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.Saas]):
            The resulting saas.
        next_page_token (str):
            If present, the next page token can be
            provided to a subsequent ListSaas call to list
            the next page. If empty, there are no more
            pages.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    saas: MutableSequence[deployments_resources.Saas] = proto.RepeatedField(
        proto.MESSAGE,
        number=10509,
        message=deployments_resources.Saas,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=10510,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=10511,
    )


class GetSaasRequest(proto.Message):
    r"""The request structure for the GetSaas method.

    Attributes:
        name (str):
            Required. The resource name of the resource
            within a service.
    """

    name: str = proto.Field(
        proto.STRING,
        number=10001,
    )


class CreateSaasRequest(proto.Message):
    r"""The request structure for the CreateSaas method.

    Attributes:
        parent (str):
            Required. The parent of the saas.
        saas_id (str):
            Required. The ID value for the new saas.
        saas (google.cloud.saasplatform_saasservicemgmt_v1beta1.types.Saas):
            Required. The desired state for the saas.
        validate_only (bool):
            If "validate_only" is set to true, the service will try to
            validate that this request would succeed, but will not
            actually make changes.
        request_id (str):
            An optional request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server will guarantee that for at
            least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    parent: str = proto.Field(
        proto.STRING,
        number=10006,
    )
    saas_id: str = proto.Field(
        proto.STRING,
        number=10503,
    )
    saas: deployments_resources.Saas = proto.Field(
        proto.MESSAGE,
        number=10504,
        message=deployments_resources.Saas,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=10501,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=10502,
    )


class UpdateSaasRequest(proto.Message):
    r"""The request structure for the UpdateSaas method.

    Attributes:
        saas (google.cloud.saasplatform_saasservicemgmt_v1beta1.types.Saas):
            Required. The desired state for the saas.
        validate_only (bool):
            If "validate_only" is set to true, the service will try to
            validate that this request would succeed, but will not
            actually make changes.
        request_id (str):
            An optional request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server will guarantee that for at
            least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Field mask is used to specify the fields to be overwritten
            in the Saas resource by the update.

            The fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask.

            If the user does not provide a mask then all fields in the
            Saas will be overwritten.
    """

    saas: deployments_resources.Saas = proto.Field(
        proto.MESSAGE,
        number=10504,
        message=deployments_resources.Saas,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=10501,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=10502,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=10512,
        message=field_mask_pb2.FieldMask,
    )


class DeleteSaasRequest(proto.Message):
    r"""The request structure for the DeleteSaas method.

    Attributes:
        name (str):
            Required. The resource name of the resource
            within a service.
        etag (str):
            The etag known to the client for the expected state of the
            saas. This is used with state-changing methods to prevent
            accidental overwrites when multiple user agents might be
            acting in parallel on the same resource.

            An etag wildcard provide optimistic concurrency based on the
            expected existence of the saas. The Any wildcard (``*``)
            requires that the resource must already exists, and the Not
            Any wildcard (``!*``) requires that it must not.
        validate_only (bool):
            If "validate_only" is set to true, the service will try to
            validate that this request would succeed, but will not
            actually make changes.
        request_id (str):
            An optional request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server will guarantee that for at
            least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    name: str = proto.Field(
        proto.STRING,
        number=10001,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=10202,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=10501,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=10502,
    )


class ListTenantsRequest(proto.Message):
    r"""The request structure for the ListTenants method.

    Attributes:
        parent (str):
            Required. The parent of the tenant.
        page_size (int):
            The maximum number of tenants to send per
            page.
        page_token (str):
            The page token: If the next_page_token from a previous
            response is provided, this request will send the subsequent
            page.
        filter (str):
            Filter the list as specified in
            https://google.aip.dev/160.
        order_by (str):
            Order results as specified in
            https://google.aip.dev/132.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=10006,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=10505,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=10506,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=10507,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=10508,
    )


class ListTenantsResponse(proto.Message):
    r"""The response structure for the ListTenants method.

    Attributes:
        tenants (MutableSequence[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.Tenant]):
            The resulting tenants.
        next_page_token (str):
            If present, the next page token can be
            provided to a subsequent ListTenants call to
            list the next page. If empty, there are no more
            pages.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    tenants: MutableSequence[deployments_resources.Tenant] = proto.RepeatedField(
        proto.MESSAGE,
        number=10509,
        message=deployments_resources.Tenant,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=10510,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=10511,
    )


class GetTenantRequest(proto.Message):
    r"""The request structure for the GetTenant method.

    Attributes:
        name (str):
            Required. The resource name of the resource
            within a service.
    """

    name: str = proto.Field(
        proto.STRING,
        number=10001,
    )


class CreateTenantRequest(proto.Message):
    r"""The request structure for the CreateTenant method.

    Attributes:
        parent (str):
            Required. The parent of the tenant.
        tenant_id (str):
            Required. The ID value for the new tenant.
        tenant (google.cloud.saasplatform_saasservicemgmt_v1beta1.types.Tenant):
            Required. The desired state for the tenant.
        validate_only (bool):
            If "validate_only" is set to true, the service will try to
            validate that this request would succeed, but will not
            actually make changes.
        request_id (str):
            An optional request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server will guarantee that for at
            least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    parent: str = proto.Field(
        proto.STRING,
        number=10006,
    )
    tenant_id: str = proto.Field(
        proto.STRING,
        number=10503,
    )
    tenant: deployments_resources.Tenant = proto.Field(
        proto.MESSAGE,
        number=10504,
        message=deployments_resources.Tenant,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=10501,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=10502,
    )


class UpdateTenantRequest(proto.Message):
    r"""The request structure for the UpdateTenant method.

    Attributes:
        tenant (google.cloud.saasplatform_saasservicemgmt_v1beta1.types.Tenant):
            Required. The desired state for the tenant.
        validate_only (bool):
            If "validate_only" is set to true, the service will try to
            validate that this request would succeed, but will not
            actually make changes.
        request_id (str):
            An optional request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server will guarantee that for at
            least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Field mask is used to specify the fields to be overwritten
            in the Tenant resource by the update.

            The fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask.

            If the user does not provide a mask then all fields in the
            Tenant will be overwritten.
    """

    tenant: deployments_resources.Tenant = proto.Field(
        proto.MESSAGE,
        number=10504,
        message=deployments_resources.Tenant,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=10501,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=10502,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=10512,
        message=field_mask_pb2.FieldMask,
    )


class DeleteTenantRequest(proto.Message):
    r"""The request structure for the DeleteTenant method.

    Attributes:
        name (str):
            Required. The resource name of the resource
            within a service.
        etag (str):
            The etag known to the client for the expected state of the
            tenant. This is used with state-changing methods to prevent
            accidental overwrites when multiple user agents might be
            acting in parallel on the same resource.

            An etag wildcard provide optimistic concurrency based on the
            expected existence of the tenant. The Any wildcard (``*``)
            requires that the resource must already exists, and the Not
            Any wildcard (``!*``) requires that it must not.
        validate_only (bool):
            If "validate_only" is set to true, the service will try to
            validate that this request would succeed, but will not
            actually make changes.
        request_id (str):
            An optional request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server will guarantee that for at
            least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    name: str = proto.Field(
        proto.STRING,
        number=10001,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=10202,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=10501,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=10502,
    )


class ListUnitKindsRequest(proto.Message):
    r"""The request structure for the ListUnitKinds method.

    Attributes:
        parent (str):
            Required. The parent of the unit kind.
        page_size (int):
            The maximum number of unit kinds to send per
            page.
        page_token (str):
            The page token: If the next_page_token from a previous
            response is provided, this request will send the subsequent
            page.
        filter (str):
            Filter the list as specified in
            https://google.aip.dev/160.
        order_by (str):
            Order results as specified in
            https://google.aip.dev/132.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=10006,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=10505,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=10506,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=10507,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=10508,
    )


class ListUnitKindsResponse(proto.Message):
    r"""The response structure for the ListUnitKinds method.

    Attributes:
        unit_kinds (MutableSequence[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.UnitKind]):
            The resulting unit kinds.
        next_page_token (str):
            If present, the next page token can be
            provided to a subsequent ListUnitKinds call to
            list the next page. If empty, there are no more
            pages.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    unit_kinds: MutableSequence[deployments_resources.UnitKind] = proto.RepeatedField(
        proto.MESSAGE,
        number=10509,
        message=deployments_resources.UnitKind,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=10510,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=10511,
    )


class GetUnitKindRequest(proto.Message):
    r"""The request structure for the GetUnitKind method.

    Attributes:
        name (str):
            Required. The resource name of the resource
            within a service.
    """

    name: str = proto.Field(
        proto.STRING,
        number=10001,
    )


class CreateUnitKindRequest(proto.Message):
    r"""The request structure for the CreateUnitKind method.

    Attributes:
        parent (str):
            Required. The parent of the unit kind.
        unit_kind_id (str):
            Required. The ID value for the new unit kind.
        unit_kind (google.cloud.saasplatform_saasservicemgmt_v1beta1.types.UnitKind):
            Required. The desired state for the unit
            kind.
        validate_only (bool):
            If "validate_only" is set to true, the service will try to
            validate that this request would succeed, but will not
            actually make changes.
        request_id (str):
            An optional request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server will guarantee that for at
            least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    parent: str = proto.Field(
        proto.STRING,
        number=10006,
    )
    unit_kind_id: str = proto.Field(
        proto.STRING,
        number=10503,
    )
    unit_kind: deployments_resources.UnitKind = proto.Field(
        proto.MESSAGE,
        number=10504,
        message=deployments_resources.UnitKind,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=10501,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=10502,
    )


class UpdateUnitKindRequest(proto.Message):
    r"""The request structure for the UpdateUnitKind method.

    Attributes:
        unit_kind (google.cloud.saasplatform_saasservicemgmt_v1beta1.types.UnitKind):
            Required. The desired state for the unit
            kind.
        validate_only (bool):
            If "validate_only" is set to true, the service will try to
            validate that this request would succeed, but will not
            actually make changes.
        request_id (str):
            An optional request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server will guarantee that for at
            least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Field mask is used to specify the fields to be overwritten
            in the UnitKind resource by the update.

            The fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask.

            If the user does not provide a mask then all fields in the
            UnitKind will be overwritten.
    """

    unit_kind: deployments_resources.UnitKind = proto.Field(
        proto.MESSAGE,
        number=10504,
        message=deployments_resources.UnitKind,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=10501,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=10502,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=10512,
        message=field_mask_pb2.FieldMask,
    )


class DeleteUnitKindRequest(proto.Message):
    r"""The request structure for the DeleteUnitKind method.

    Attributes:
        name (str):
            Required. The resource name of the resource
            within a service.
        etag (str):
            The etag known to the client for the expected state of the
            unit kind. This is used with state-changing methods to
            prevent accidental overwrites when multiple user agents
            might be acting in parallel on the same resource.

            An etag wildcard provide optimistic concurrency based on the
            expected existence of the unit kind. The Any wildcard
            (``*``) requires that the resource must already exists, and
            the Not Any wildcard (``!*``) requires that it must not.
        validate_only (bool):
            If "validate_only" is set to true, the service will try to
            validate that this request would succeed, but will not
            actually make changes.
        request_id (str):
            An optional request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server will guarantee that for at
            least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    name: str = proto.Field(
        proto.STRING,
        number=10001,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=10202,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=10501,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=10502,
    )


class ListUnitsRequest(proto.Message):
    r"""The request structure for the ListUnits method.

    Attributes:
        parent (str):
            Required. The parent of the unit.
        page_size (int):
            The maximum number of units to send per page.
        page_token (str):
            The page token: If the next_page_token from a previous
            response is provided, this request will send the subsequent
            page.
        filter (str):
            Filter the list as specified in
            https://google.aip.dev/160.
        order_by (str):
            Order results as specified in
            https://google.aip.dev/132.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=10006,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=10505,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=10506,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=10507,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=10508,
    )


class ListUnitsResponse(proto.Message):
    r"""The response structure for the ListUnits method.

    Attributes:
        units (MutableSequence[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.Unit]):
            The resulting units.
        next_page_token (str):
            If present, the next page token can be
            provided to a subsequent ListUnits call to list
            the next page. If empty, there are no more
            pages.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    units: MutableSequence[deployments_resources.Unit] = proto.RepeatedField(
        proto.MESSAGE,
        number=10509,
        message=deployments_resources.Unit,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=10510,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=10511,
    )


class GetUnitRequest(proto.Message):
    r"""The request structure for the GetUnit method.

    Attributes:
        name (str):
            Required. The resource name of the resource
            within a service.
    """

    name: str = proto.Field(
        proto.STRING,
        number=10001,
    )


class CreateUnitRequest(proto.Message):
    r"""The request structure for the CreateUnit method.

    Attributes:
        parent (str):
            Required. The parent of the unit.
        unit_id (str):
            Required. The ID value for the new unit.
        unit (google.cloud.saasplatform_saasservicemgmt_v1beta1.types.Unit):
            Required. The desired state for the unit.
        validate_only (bool):
            If "validate_only" is set to true, the service will try to
            validate that this request would succeed, but will not
            actually make changes.
        request_id (str):
            An optional request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server will guarantee that for at
            least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    parent: str = proto.Field(
        proto.STRING,
        number=10006,
    )
    unit_id: str = proto.Field(
        proto.STRING,
        number=10503,
    )
    unit: deployments_resources.Unit = proto.Field(
        proto.MESSAGE,
        number=10504,
        message=deployments_resources.Unit,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=10501,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=10502,
    )


class UpdateUnitRequest(proto.Message):
    r"""The request structure for the UpdateUnit method.

    Attributes:
        unit (google.cloud.saasplatform_saasservicemgmt_v1beta1.types.Unit):
            Required. The desired state for the unit.
        validate_only (bool):
            If "validate_only" is set to true, the service will try to
            validate that this request would succeed, but will not
            actually make changes.
        request_id (str):
            An optional request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server will guarantee that for at
            least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Field mask is used to specify the fields to be overwritten
            in the Unit resource by the update.

            The fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask.

            If the user does not provide a mask then all fields in the
            Unit will be overwritten.
    """

    unit: deployments_resources.Unit = proto.Field(
        proto.MESSAGE,
        number=10504,
        message=deployments_resources.Unit,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=10501,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=10502,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=10512,
        message=field_mask_pb2.FieldMask,
    )


class DeleteUnitRequest(proto.Message):
    r"""The request structure for the DeleteUnit method.

    Attributes:
        name (str):
            Required. The resource name of the resource
            within a service.
        etag (str):
            The etag known to the client for the expected state of the
            unit. This is used with state-changing methods to prevent
            accidental overwrites when multiple user agents might be
            acting in parallel on the same resource.

            An etag wildcard provide optimistic concurrency based on the
            expected existence of the unit. The Any wildcard (``*``)
            requires that the resource must already exists, and the Not
            Any wildcard (``!*``) requires that it must not.
        validate_only (bool):
            If "validate_only" is set to true, the service will try to
            validate that this request would succeed, but will not
            actually make changes.
        request_id (str):
            An optional request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server will guarantee that for at
            least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    name: str = proto.Field(
        proto.STRING,
        number=10001,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=10202,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=10501,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=10502,
    )


class ListUnitOperationsRequest(proto.Message):
    r"""The request structure for the ListUnitOperations method.

    Attributes:
        parent (str):
            Required. The parent of the unit operation.
        page_size (int):
            The maximum number of unit operations to send
            per page.
        page_token (str):
            The page token: If the next_page_token from a previous
            response is provided, this request will send the subsequent
            page.
        filter (str):
            Filter the list as specified in
            https://google.aip.dev/160.
        order_by (str):
            Order results as specified in
            https://google.aip.dev/132.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=10006,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=10505,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=10506,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=10507,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=10508,
    )


class ListUnitOperationsResponse(proto.Message):
    r"""The response structure for the ListUnitOperations method.

    Attributes:
        unit_operations (MutableSequence[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.UnitOperation]):
            The resulting unit operations.
        next_page_token (str):
            If present, the next page token can be
            provided to a subsequent ListUnitOperations call
            to list the next page. If empty, there are no
            more pages.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    unit_operations: MutableSequence[deployments_resources.UnitOperation] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=10509,
            message=deployments_resources.UnitOperation,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=10510,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=10511,
    )


class GetUnitOperationRequest(proto.Message):
    r"""The request structure for the GetUnitOperation method.

    Attributes:
        name (str):
            Required. The resource name of the resource
            within a service.
    """

    name: str = proto.Field(
        proto.STRING,
        number=10001,
    )


class CreateUnitOperationRequest(proto.Message):
    r"""The request structure for the CreateUnitOperation method.

    Attributes:
        parent (str):
            Required. The parent of the unit operation.
        unit_operation_id (str):
            Required. The ID value for the new unit
            operation.
        unit_operation (google.cloud.saasplatform_saasservicemgmt_v1beta1.types.UnitOperation):
            Required. The desired state for the unit
            operation.
        validate_only (bool):
            If "validate_only" is set to true, the service will try to
            validate that this request would succeed, but will not
            actually make changes.
        request_id (str):
            An optional request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server will guarantee that for at
            least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    parent: str = proto.Field(
        proto.STRING,
        number=10006,
    )
    unit_operation_id: str = proto.Field(
        proto.STRING,
        number=10503,
    )
    unit_operation: deployments_resources.UnitOperation = proto.Field(
        proto.MESSAGE,
        number=10504,
        message=deployments_resources.UnitOperation,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=10501,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=10502,
    )


class UpdateUnitOperationRequest(proto.Message):
    r"""The request structure for the UpdateUnitOperation method.

    Attributes:
        unit_operation (google.cloud.saasplatform_saasservicemgmt_v1beta1.types.UnitOperation):
            Required. The desired state for the unit
            operation.
        validate_only (bool):
            If "validate_only" is set to true, the service will try to
            validate that this request would succeed, but will not
            actually make changes.
        request_id (str):
            An optional request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server will guarantee that for at
            least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Field mask is used to specify the fields to be overwritten
            in the UnitOperation resource by the update.

            The fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask.

            If the user does not provide a mask then all fields in the
            UnitOperation will be overwritten.
    """

    unit_operation: deployments_resources.UnitOperation = proto.Field(
        proto.MESSAGE,
        number=10504,
        message=deployments_resources.UnitOperation,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=10501,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=10502,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=10512,
        message=field_mask_pb2.FieldMask,
    )


class DeleteUnitOperationRequest(proto.Message):
    r"""The request structure for the DeleteUnitOperation method.

    Attributes:
        name (str):
            Required. The resource name of the resource
            within a service.
        etag (str):
            The etag known to the client for the expected state of the
            unit operation. This is used with state-changing methods to
            prevent accidental overwrites when multiple user agents
            might be acting in parallel on the same resource.

            An etag wildcard provide optimistic concurrency based on the
            expected existence of the unit operation. The Any wildcard
            (``*``) requires that the resource must already exists, and
            the Not Any wildcard (``!*``) requires that it must not.
        validate_only (bool):
            If "validate_only" is set to true, the service will try to
            validate that this request would succeed, but will not
            actually make changes.
        request_id (str):
            An optional request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server will guarantee that for at
            least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    name: str = proto.Field(
        proto.STRING,
        number=10001,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=10202,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=10501,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=10502,
    )


class ListReleasesRequest(proto.Message):
    r"""The request structure for the ListReleases method.

    Attributes:
        parent (str):
            Required. The parent of the release.
        page_size (int):
            The maximum number of releases to send per
            page.
        page_token (str):
            The page token: If the next_page_token from a previous
            response is provided, this request will send the subsequent
            page.
        filter (str):
            Filter the list as specified in
            https://google.aip.dev/160.
        order_by (str):
            Order results as specified in
            https://google.aip.dev/132.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=10006,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=10505,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=10506,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=10507,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=10508,
    )


class ListReleasesResponse(proto.Message):
    r"""The response structure for the ListReleases method.

    Attributes:
        releases (MutableSequence[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.Release]):
            The resulting releases.
        next_page_token (str):
            If present, the next page token can be
            provided to a subsequent ListReleases call to
            list the next page. If empty, there are no more
            pages.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    releases: MutableSequence[deployments_resources.Release] = proto.RepeatedField(
        proto.MESSAGE,
        number=10509,
        message=deployments_resources.Release,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=10510,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=10511,
    )


class GetReleaseRequest(proto.Message):
    r"""The request structure for the GetRelease method.

    Attributes:
        name (str):
            Required. The resource name of the resource
            within a service.
    """

    name: str = proto.Field(
        proto.STRING,
        number=10001,
    )


class CreateReleaseRequest(proto.Message):
    r"""The request structure for the CreateRelease method.

    Attributes:
        parent (str):
            Required. The parent of the release.
        release_id (str):
            Required. The ID value for the new release.
        release (google.cloud.saasplatform_saasservicemgmt_v1beta1.types.Release):
            Required. The desired state for the release.
        validate_only (bool):
            If "validate_only" is set to true, the service will try to
            validate that this request would succeed, but will not
            actually make changes.
        request_id (str):
            An optional request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server will guarantee that for at
            least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    parent: str = proto.Field(
        proto.STRING,
        number=10006,
    )
    release_id: str = proto.Field(
        proto.STRING,
        number=10503,
    )
    release: deployments_resources.Release = proto.Field(
        proto.MESSAGE,
        number=10504,
        message=deployments_resources.Release,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=10501,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=10502,
    )


class UpdateReleaseRequest(proto.Message):
    r"""The request structure for the UpdateRelease method.

    Attributes:
        release (google.cloud.saasplatform_saasservicemgmt_v1beta1.types.Release):
            Required. The desired state for the release.
        validate_only (bool):
            If "validate_only" is set to true, the service will try to
            validate that this request would succeed, but will not
            actually make changes.
        request_id (str):
            An optional request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server will guarantee that for at
            least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Field mask is used to specify the fields to be overwritten
            in the Release resource by the update.

            The fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask.

            If the user does not provide a mask then all fields in the
            Release will be overwritten.
    """

    release: deployments_resources.Release = proto.Field(
        proto.MESSAGE,
        number=10504,
        message=deployments_resources.Release,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=10501,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=10502,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=10512,
        message=field_mask_pb2.FieldMask,
    )


class DeleteReleaseRequest(proto.Message):
    r"""The request structure for the DeleteRelease method.

    Attributes:
        name (str):
            Required. The resource name of the resource
            within a service.
        etag (str):
            The etag known to the client for the expected state of the
            release. This is used with state-changing methods to prevent
            accidental overwrites when multiple user agents might be
            acting in parallel on the same resource.

            An etag wildcard provide optimistic concurrency based on the
            expected existence of the release. The Any wildcard (``*``)
            requires that the resource must already exists, and the Not
            Any wildcard (``!*``) requires that it must not.
        validate_only (bool):
            If "validate_only" is set to true, the service will try to
            validate that this request would succeed, but will not
            actually make changes.
        request_id (str):
            An optional request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server will guarantee that for at
            least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    name: str = proto.Field(
        proto.STRING,
        number=10001,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=10202,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=10501,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=10502,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
